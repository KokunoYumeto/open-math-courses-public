# SH02-MO-UNIT — Transporting directional obstructions

Original AI programme expression: CC0 1.0 Universal. The proofs use the exact local tests, propagation results, six-operation identities and Fourier equivalence identified below. Those dependencies require their own verification; a conditional proof here does not close them. This lesson retains bounded complexes of arbitrary sheaves over a commutative ring $k$ of finite global dimension. Only the Morse inequalities impose field coefficients.

All manifolds are finite dimensional, Hausdorff and countable at infinity. A map is $C^\infty$ unless stated otherwise. We use **submersion** for a map with surjective differential; mere differentiability is not sufficient for any submersion assertion. Test functions and exhaustion functions may be $C^1$. Tensor products and internal Hom are derived. Put $A^a=\{(x,-\xi):(x,\xi)\in A\}$ for a subset of a cotangent bundle.

The organizing question is whether a sheaf operation can create a failed local support test. Products separate the variables of such tests. Proper images collect tests along compact fibres. Noncharacteristic inverse images preserve the direction of a test. An exhaustion handles some nonproper maps by excluding the directions in which information could escape. Fourier transformation then exchanges a vector and a covector.

## SH02-MO-DEPENDENCIES — The contracts used in this lesson

The following are dependencies, not assertions that a heading elsewhere establishes their complete proof.

| Contract | Exact content used |
|---|---|
| `SH02-MST-TEST`, `SH02-MST-EQUIVALENCE` in [directional tests](../../SH02-microsupport-tests.html) | The neighborhood-uniform $C^1$ support test; the equivalent compact-cap restriction test; replacement, near a point, by a bounded complex $H$ with $R\phi_{\gamma*}H=0$ for a pointed cone detecting the prescribed covector |
| `SH02-MST-PROPAGATION` | Propagation between nested directionally open sets, with compact forward slices and the stated exclusion of interior polar covectors; both section and supported-projector conclusions |
| `SH02-MST-CUTOFF-FORWARD`, `SH02-MST-CUTOFF-CONVERSE` | For a product $B\times V$, complexes with microsupport in $T^*B\times(V\times\gamma^{\circ a})$ are exactly inverse images from the topology invariant under addition by $\gamma$; cones may have lines |
| `SH02-GAM-COH-OPEN`, `SH02-GAM-SUPPORT` in [cone topology](../../SH02-cone-topology.html) | Derived continuation from an ordinary convex open set to its directional saturation, and commutation of the directional direct image with directionally locally closed supports |
| `SH02-SUB-CONE-TOPOLOGY`, `SH02-SUB-BOUND` in [subset microsupport](../../SH02-subset-microsupport.html) | Strict normal geometry and its local cone topology criterion; $\operatorname{SS}(k_\Omega)\subset-N^*(\Omega)$ and $\operatorname{SS}(k_Z)\subset N^*(Z)$ |
| `SH02-EX-RECTANGLE` in [exceptional operations](../../SH02-exceptional-operations.html) | $R\Gamma(U\times V;R\mathcal Hom(q_V^{-1}G,q_U^!F))\simeq R\operatorname{Hom}_k(R\Gamma_c(V;G),R\Gamma(U;F))$, with its restriction and extension maps |
| `SH02-MD-SUBMERSION`, `SH02-MD-RELATIVE` in manifold duality | The relative orientation complex $\omega_f$ and $f^!F\simeq f^{-1}F\otimes\omega_f$ for submersions, with its canonical comparison |
| `SH02-MIC-STALKS` and the zero-section/Sato identifications in [microlocalization](../../SH02-microlocalization.html) | Closed-support tests for $\mu_MF$, the identities on its zero section, and the punctured-conormal localization triangle |
| `SH02-MH-HOM` in [microlocal Hom](../../SH02-microlocal-hom.html) | The definition $\mu hom(G,F)=\mu_\Delta R\mathcal Hom(q_2^{-1}G,q_1^!F)$ under $(x;\xi)\mapsto(x,x;\xi,-\xi)$ |
| `SH02-CB-EXTERNAL-HOM` in [biduality](../../SH02-cohomological-biduality.html) | The external dual–tensor comparison for a factor with cohomologically constructible local data |
| Fourier equivalence and its two kernel models in [Fourier–Sato transform](../../SH02-fourier-sato.html) | $T_EF=Rq_!(p^{-1}F\otimes k_{\{\langle x,y\rangle\leq0\}})\simeq Rq_*R\Gamma_{\{\langle x,y\rangle\geq0\}}p^{-1}F$; the inverse equivalence and its orientation normalization |

We also use proper base change, proper-support base change, localization, compact-neighborhood continuity, and the projection formula at their manifold bounded-derived generality. Compact-neighborhood continuity is only applied to compact sets. It is not used as base change across an arbitrary closed set for a nonproper map. The noncharacteristic deformation input uses the intersection of the **closures** of shrinking increments, as in the corrected foundation contract. Local constancy along interval fibres implies local derived descent; that contract includes higher extension data, not just descent of each cohomology sheaf.

## SH02-MO-COTANGENT — The correspondence attached to a map

For $f:Y\to X$, write

$$
T^*Y\xleftarrow{f_d}Y\times_XT^*X\xrightarrow{f_\pi}T^*X,
\qquad f_d(y,\xi)=(y,d f_y^t\xi),\quad f_\pi(y,\xi)=(f(y),\xi).
$$

The relative conormal is $\ker f_d$. For a submanifold $M\subset X$ it is the usual $T_M^*X$. For $A,B\subset T^*X$ their ordinary fibrewise sum is

$$
A+B=\{(x,\xi+\eta):(x,\xi)\in A,\ (x,\eta)\in B\}.
$$

This operation is not automatically closed. It must not replace the enlarged limiting operations used later for characteristic maps.

### SH02-MO-CONE-PROPER — No cancellation and closed images

If $A,B$ are closed conic sets and $A\cap B^a$ is contained in the zero section, addition $A\times_XB\to T^*X$ is proper. In particular $A+B$ is closed. Here properness is local over the base and hence global over compact subsets of the target.

**Proof.** Choose a relatively compact coordinate neighborhood and a Euclidean norm. If there were no uniform $c>0$ after shrinking the neighborhood, there would be $x_n\to x$, $\xi_n\in A_{x_n}$, $\eta_n\in B_{x_n}$ with

$$
|\xi_n|+|\eta_n|=1,\qquad |\xi_n+\eta_n|\longrightarrow0.
$$

Compactness of the unit sphere and closedness give a limit $\xi=-\eta\neq0$, contrary to the hypothesis. Thus

$$
|\xi+\eta|\geq c(|\xi|+|\eta|).
\tag{MO1}
$$

The inverse image of a compact set under addition is closed, has base in a compact set and has bounded fibre coordinates by MO1; it is compact. Finite coordinate covers handle an arbitrary compact target set. A proper map between locally compact Hausdorff spaces is closed, proving the assertion. The same normalization argument proves a second useful fact: if $f_d$ has no nonzero kernel vector in $f_\pi^{-1}A$, then its restriction to this closed conic set is proper. $\square$

## SH02-MO-CONE-AC — A support calculation in opposite cone topologies

Let $V$ be a finite-dimensional real vector space, $\gamma$ a closed pointed convex cone containing $0$, and $\phi_\gamma:V\to V_\gamma$ the identity into the topology of ordinary open sets $U$ satisfying $U+\gamma=U$. Suppose

$$
R\phi_{\gamma*}H=0,\qquad H\in D^b(k_V).
$$

Let $\Omega$ be open and invariant under addition by $-\gamma$, and assume that $\Omega\cap(K+\gamma)$ is relatively compact for every compact $K\subset V$. Then

$$
R\phi_{\gamma*}(H_\Omega)=0.
\tag{MO2}
$$

If $\Omega'\subset\Omega$ is also $(-\gamma)$-open and $\Omega\setminus\Omega'$ is relatively compact, extension of compactly supported sections induces an isomorphism

$$
R\Gamma_c(\Omega';H)\xrightarrow{\sim}R\Gamma_c(\Omega;H).
\tag{MO3}
$$

Here $H_\Omega=j_!j^{-1}H$; it is not $Rj_*j^{-1}H$.

**Proof.** It suffices to prove that $R\Gamma(U;H_\Omega)=0$ on a basis of $\gamma$-open sets with $U\cap\Omega$ relatively compact. Sets $U=B_\epsilon(v)+\gamma$ form such a basis by the support hypothesis. The sheaf extension-by-zero definition gives

$$
H^r(U;H_\Omega)=\varinjlim_K H^r_K(U;H),
\tag{MO4}
$$

where $K$ is closed in $U$ and contained in $\Omega$. The identity follows by resolving with sheaves acyclic for the relevant supports; their support families form a filtered union. Every such $K$ has compact closure in $V$. Put $C=\overline K-\gamma$. This set is closed and is $\gamma$-closed. If $z=w-v\in C\cap U$ with $v\in\gamma$, then $w=z+v\in U$; hence $w\in\overline K\cap U=K$. It follows that $z\in K-\gamma\subset\Omega$. Thus

$$
K\subset C\cap U\subset\Omega.
$$

These enlarged supports are cofinal in MO4. Directional support compatibility identifies their cohomology with cohomology with support $C\cap U$ of $R\phi_{\gamma*}H$, which is zero. This proves MO2 without any closed-fibre base-change assertion.

For MO3, the cone of $H_{\Omega'}\to H_\Omega$ is $H_{\Omega\setminus\Omega'}$. Its support is contained in the compact closure of $\Omega\setminus\Omega'$. Compactly supported and ordinary global cohomology therefore agree on that cone. MO2 gives $R\Gamma(V;H_\Omega)=R\Gamma(V;H_{\Omega'})=0$, since global sections factor through $R\phi_{\gamma*}$. Its global cohomology vanishes, so its compactly supported cohomology vanishes too. The compact-support localization triangle proves MO3. $\square$

## SH02-MO-EXTERNAL-TENSOR — Product tests

For $F\in D^b(k_X)$ and $G\in D^b(k_Y)$,

$$
\operatorname{SS}(F\boxtimes G)\subset
\operatorname{SS}(F)\times\operatorname{SS}(G).
\tag{MO5}
$$

**Proof.** Work in coordinate neighborhoods. Suppose $(x,\xi)\notin\operatorname{SS}(F)$. The compact-cap criterion gives a closed cone $\gamma$, a cap $C_z$ and its base $B_z$, depending on nearby $z$, such that restriction $R\Gamma(C_z;F)\to R\Gamma(B_z;F)$ is an isomorphism. Use $\gamma\times\{0\}$ in the product. Its cap and base at $(z,w)$ are $C_z\times\{w\}$ and $B_z\times\{w\}$. Compact base change and the projection formula give

$$
R\Gamma(C_z\times\{w\};F\boxtimes G)
\simeq R\Gamma(C_z;F)\otimes G_w,
$$

and the same formula for $B_z$. The restriction is therefore an isomorphism. It excludes every covector whose first component is $(x,\xi)$; the test is valid in a neighborhood, as required by the criterion. If instead $(y,\eta)\notin\operatorname{SS}(G)$, interchange the factors. This proves MO5. No finite-rank Künneth assertion is needed: the tensor factor is a fixed stalk complex and the cap is compact. $\square$

## SH02-MO-EXTERNAL-HOM — Reversing the second direction

For the projections $q_X,q_Y$ from $X\times Y$,

$$
\operatorname{SS}\bigl(R\mathcal Hom(q_Y^{-1}G,q_X^{-1}F)\bigr)
\subset\operatorname{SS}(F)\times\operatorname{SS}(G)^a.
\tag{MO6}
$$

The same estimate holds with $q_X^!F$ in place of $q_X^{-1}F$: locally the two differ by an invertible constant orientation complex and a shift, which do not affect support-test vanishing.

**Proof.** Put $K=R\mathcal Hom(q_Y^{-1}G,q_X^!F)$. First compute on an open rectangle $U\times V$. Exceptional adjunction for $p:U\times V\to U$, proper-support base change from $V\to\{*\}$, and the constant-sheaf adjunction give

$$
\begin{aligned}
R\Gamma(U\times V;K)
&\simeq R\operatorname{Hom}_{k_U}
 \bigl(Rp_!q_V^{-1}(G|_V),F|_U\bigr)\\
&\simeq R\operatorname{Hom}_k
 \bigl(R\Gamma_c(V;G),R\Gamma(U;F)\bigr).
\end{aligned}
\tag{MO7}
$$

Here $q_V:U\times V\to V$ is the second projection. The proper-support base-change isomorphism identifies $Rp_!q_V^{-1}(G|_V)$ with the constant complex on $U$ having value $R\Gamma_c(V;G)$. All maps in MO7 commute with restriction to smaller open rectangles. The finite-dimensional manifold and finite-global-dimension hypotheses supply the boundedness required by these adjunctions. In particular, this calculation uses open restriction of internal Hom; it does not replace either open neighborhood by a compact subset inside a Hom argument.

Suppose $(x,\xi)\notin\operatorname{SS}(F)$. For $\xi=0$, the constant-function support tests imply that $F$ vanishes near $x$, so $K$ vanishes on the corresponding product neighborhood. For $\xi\ne0$, `SH02-MST-EQUIVALENCE` supplies a pointed closed convex cone $\gamma$ and a bounded representative $H$ on the coordinate vector space $E$, agreeing with $F$ near $x$, such that

$$
R\phi_{\gamma*}H=0,
\qquad \langle v,\xi\rangle<0
\quad(v\in\gamma\setminus\{0\}).
$$

Replace $F$ by $H$ in $K$ and denote the resulting complex by $K_H$. It is bounded by the bounded internal-Hom estimate, and agrees with $K$ near $\{x\}\times Y$. If $U$ is $\gamma$-open, derived direct-image composition gives $R\Gamma(U;H)=0$. Formula MO7 therefore gives $R\Gamma(U\times V;K_H)=0$ for every ordinary open $V\subset Y$.

These rectangles form a basis for the directional topology with cone $\gamma\times\{0\}$. Indeed, an ordinary open set invariant under this cone contains, around any one of its points, an ordinary rectangle $B\times V$ and hence $(B+\gamma)\times V$. Derived sections of $R\phi_{\gamma\times\{0\}*}K_H$ on each such basis member are the just-computed zero complexes. Their filtered stalk colimits are zero, so

$$
R\phi_{\gamma\times\{0\}*}K_H=0.
$$

For every second covector $\eta$, pairing $(\xi,\eta)$ with a nonzero vector $(v,0)$ in this pointed cone gives the strictly negative number $\langle\xi,v\rangle$. The cone-to-test implication `SH02-MST-CONE-TO-TEST` therefore excludes $(x,y;\xi,\eta)$ from $\operatorname{SS}(K_H)$ and hence from $\operatorname{SS}(K)$. This implication allows cones of empty interior. Compactness of their unit directions makes strict negativity persist in a covector neighborhood, as the definition of microsupport requires.

Now suppose $(y,\eta)\notin\operatorname{SS}(G)$. The directional test equivalence permits replacement of $G$ near $y$ by a bounded $H$ with $R\phi_{\gamma*}H=0$, where $\eta$ lies strictly in the polar direction detected by $\gamma$. To test the opposite direction in $K$, choose nested $(-\gamma)$-open sets $\Omega'\subset\Omega$ whose difference is relatively compact, with $\Omega\cap(L+\gamma)$ relatively compact for compact $L$. Such sets are supplied by bounded transverse caps of the pointed cone. MO3 makes

$$
R\operatorname{Hom}_k(R\Gamma_c(\Omega;H),R\Gamma(U;F))
\longrightarrow
R\operatorname{Hom}_k(R\Gamma_c(\Omega';H),R\Gamma(U;F))
$$

an isomorphism for every open $U\subset X$. By external adjunction these are exactly the restriction maps for $K$ on $U\times\Omega$ and $U\times\Omega'$. The cone form of the local test excludes $(x,y;\xi,-\eta)$, uniformly near the prescribed point. This gives MO6. $\square$

## SH02-MO-PROPER-PUSH — Collecting tests along a fibre

Let $f:Y\to X$ be any manifold map and assume that $f$ is proper on $\operatorname{supp}(G)$. Then

$$
\operatorname{SS}(Rf_*G)\subset
f_\pi f_d^{-1}\operatorname{SS}(G).
\tag{MO8}
$$

For a closed embedding this is an equality.

**Proof.** The set on the right is closed: $f_\pi$ is proper on the closed subset in question, because its base lies in $\operatorname{supp}(G)$ and the covector in its source is the target covector. Take a covector outside it and a sufficiently small cotangent neighborhood disjoint from it. Every test function $h$ whose differential lies there satisfies $d(hf)_y\notin\operatorname{SS}(G)$ at every relevant point of the fibre. Localization commutes with ordinary direct image, and proper base change on the support gives

$$
\bigl(R\Gamma_{\{h\geq h(x)\}}Rf_*G\bigr)_x
\simeq
R\Gamma\bigl(f^{-1}(x);
R\Gamma_{\{hf\geq h(x)\}}G\bigr)=0.
\tag{MO9}
$$

The last complex restricts to zero on the fibre because each of its stalks is a vanishing local test. This proves MO8.

For a closed embedding, straighten $Y$ to a vector subspace in a chart. A compact cap test for $i_*G$ is exactly its intersection with $Y$ tested against $G$, since $i$ is proper and $i_*G$ is supported on $Y$. Intersecting the cap and its base with $Y$ replaces the testing covector by its restriction to $TY$; their proper-cone conditions are preserved. Thus a covector absent from $\operatorname{SS}(i_*G)$ has restricted covector absent from $\operatorname{SS}(G)$. Together with MO8 this gives equality, including covectors conormal to $Y$. $\square$

## SH02-MO-SUBMERSION — Exact pullback and local descent

If $f:Y\to X$ is a submersion, then

$$
\operatorname{SS}(f^{-1}F)=f_df_\pi^{-1}\operatorname{SS}(F).
\tag{MO10}
$$

For $G\in D^b(k_Y)$ the following conditions are equivalent:

1. every $H^j(G)$ restricts to a locally constant sheaf on each fibre;
2. locally on $Y$, the complex $G$ is isomorphic to $f^{-1}F$ for a bounded complex on an open subset of $X$;
3. $\operatorname{SS}(G)\subset f_d(Y\times_XT^*X)$.

**Proof.** Locally $f$ is a projection $U\times V\to U$, and $f^{-1}F=F\boxtimes k_V$. MO5 proves the inclusion in MO10, since the constant sheaf has only zero covectors. Conversely, pull a test function $h$ on $U$ back to the product. Its local support complex is the pullback of that on $U$: this follows from open-product base change in the localization triangle. The stalks at $(x,y)$ and $x$ are equal. If a covector downstairs fails a support test arbitrarily near $(x,\xi)$, its horizontal pullback fails the corresponding tests arbitrarily near $(x,y;\xi,0)$. This proves equality.

The interval-fibre descent contract gives (1)$\Leftrightarrow$(2), locally in a contractible coordinate box in $V$; it applies to the whole bounded complex and preserves its extension data. MO10 gives (2)$\Rightarrow$(3). For (3)$\Rightarrow$(1), use the directional cutoff characterization with the entire vector space $V$ as cone. Its polar is $\{0\}$, so its directional topology forgets the $V$ coordinate. It identifies $G$ locally with a pullback, giving (2) and hence (1). $\square$

### SH02-MO-FIBER-REMARK — A special cohomology-sheaf criterion

The horizontal bundle $V_f=f_d(Y\times_XT^*X)$ is a smooth coisotropic, hence involutive, submanifold. In projection coordinates it is defined by $\eta_1=\cdots=\eta_r=0$; its symplectic orthogonal is spanned by the vertical vectors $\partial/\partial y_j$, which are tangent to it. The equivalence above gives

$$
\operatorname{SS}(G)\subset V_f
\quad\Longleftrightarrow\quad
\operatorname{SS}(H^jG)\subset V_f\text{ for every }j.
$$

This statement concerns this particular horizontal set. It does not assert $\operatorname{SS}(H^jG)\subset\operatorname{SS}(G)$ for an arbitrary complex.

## SH02-MO-BOUNDARY — Four ways to impose a boundary

For a subset $S\subset X$, let $N_x(S)$ be its strict normal cone and let $N_x^*(S)=N_x(S)^\circ$ use the nonnegative polar. Thus the convention from the subset lesson is

$$
N_x(S)=T_xX\setminus C_x(X\setminus S,S),\qquad
N^*(X\setminus S)=-N^*(S).
$$

These strict normal polars need not be conormal bundles, even when $S$ is a submanifold. The following table describes the four operations on $F\in D^b(k_X)$. Every intersection condition is required over the full base, and “zero” means contained in $T_X^*X$.

| Subset and operation | Assumption | Resulting bound |
|---|---|---|
| Open $\Omega$, $Rj_*j^{-1}F$ | $\operatorname{SS}(F)\cap(-N^*(\Omega))$ is zero | $\operatorname{SS}(Rj_*j^{-1}F)\subset\operatorname{SS}(F)+N^*(\Omega)$ |
| Open $\Omega$, $j_!j^{-1}F$ | $\operatorname{SS}(F)\cap N^*(\Omega)$ is zero | $\operatorname{SS}(j_!j^{-1}F)\subset\operatorname{SS}(F)-N^*(\Omega)$ |
| Closed $Z$, $R\Gamma_ZF$ | $\operatorname{SS}(F)\cap N^*(Z)$ is zero | $\operatorname{SS}(R\Gamma_ZF)\subset\operatorname{SS}(F)-N^*(Z)$ |
| Closed $Z$, $F_Z$ | $\operatorname{SS}(F)\cap(-N^*(Z))$ is zero | $\operatorname{SS}(F_Z)\subset\operatorname{SS}(F)+N^*(Z)$ |

Here $F_Z=i_*i^{-1}F$ and $R\Gamma_ZF=i_*i^!F$. The two closed-set constructions have different signs. The assumptions make the indicated sums closed by MO1.

**Proof of the ordinary open image.** Work near $x$ in a vector space and put $A=\operatorname{SS}(F)_x$, $N=N_x^*(\Omega)$. Outside the closed support of $F$ the assertion is immediate, so assume $0\in A$. Take $\xi\notin A+N$. The cone $N+\mathbb R_{\geq0}(-\xi)$ has no nonzero intersection with $-A$: an equality $n-t\xi=-a$ with $t>0$ would give $\xi=t^{-1}(a+n)\in A+N$, and $t=0$ is excluded by the transversality assumption. Separate their compact angular parts and enlarge the first cone slightly to a closed pointed convex cone $K$ such that

$$
N+\mathbb R_{\geq0}(-\xi)\subset\operatorname{Int}K\cup\{0\},
\qquad K\cap(-A)\subset\{0\}.
\tag{MO11}
$$

If the right-hand bound is the entire fibre there is nothing to test; otherwise this pointed enlargement is possible. One direct construction is to choose a strictly positive linear functional on the first pointed cone, take its compact affine section, enlarge that section inside the complement of $-A$, and take its cone. Compactness gives a strict angular margin. With $\gamma=K^\circ$, every nonzero $v\in\gamma$ satisfies $\langle v,\xi\rangle<0$. The strict-normal criterion makes $\Omega$ locally $\gamma$-open. Closedness of microsupport permits a neighborhood $U$ of $x$ on which

$$
\operatorname{SS}(F)\cap(U\times(-\gamma^\circ))
\subset U\times\{0\}.
$$

Choose nested $\gamma$-open caps $\Omega_0\subset\Omega_1$ with $\Omega_1\setminus\Omega_0\subset U$ and compact forward slices, so that their difference tests a neighborhood of $x$. Propagation gives

$$
\bigl(R\phi_{\gamma*}R\Gamma_{X\setminus\Omega_0}F\bigr)|_{\Omega_1}=0.
\tag{MO12}
$$

Both $\Omega$ and the caps are open in the directional topology. Consequently direct-image composition, open restriction and the directional support identity carry MO12 to the same statement with $F$ replaced by $Rj_*j^{-1}F$. The cone test therefore excludes $(x,\xi)$ from its microsupport. This argument only uses identities for open subsets in the two topologies; it does not commute a nonproper direct image with arbitrary closed restriction.

**Proof of extension by zero.** Now take $\xi\notin A-N$ and assume $A\cap N$ is zero. The same separation, with the opposite normal, provides a cone $\gamma$ detecting $\xi$ for which $\Omega$ is locally $(-\gamma)$-open and $\operatorname{SS}(F)$ avoids the required negative polar cone. The supported version of propagation produces a bounded representative

$$
F'=R\Gamma_{\Omega_1\setminus\Omega_0}F,
\qquad R\phi_{\gamma*}F'=0,
$$

which agrees with $F$ near $x$. Shrink the local model for $\Omega$ by an opposite directional cap, retaining its germ at $x$, so that $\Omega\cap(K+\gamma)$ is relatively compact for every compact $K$. This is possible because $\gamma$ is pointed: a linear functional strictly positive on its nonzero directions cuts off every forward slice. MO2 then gives $R\phi_{\gamma*}(F'_\Omega)=0$. Near $x$ this is the extension by zero of $F|_\Omega$, so the local cone test proves the second row of the table.

For closed $Z$, apply the two open results to $\Omega=X\setminus Z$ and use

$$
R\Gamma_ZF\longrightarrow F\longrightarrow Rj_*j^{-1}F\xrightarrow{+1},
\qquad
j_!j^{-1}F\longrightarrow F\longrightarrow F_Z\xrightarrow{+1}.
$$

The triangle inequality for microsupport and $N^*(\Omega)=-N^*(Z)$ give the last two rows. $\square$

The four rows align with Kashiwara–Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985), Propositions 4.3.1–4.3.2, pp. 67–69](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf#page=70), and the two localization triangles. The source uses the nonnegative polar convention, as here. Its Corollary 4.3.3 already places the point on the boundary of the closed subset. The boundary qualification in the next statement therefore agrees with that source; it corrects an overbroad formulation, not that corollary.

## SH02-MO-VANISH — An outward direction forces a costalk to vanish

Let $Z$ be closed, let $x\in\partial Z$ be a boundary point, and suppose

$$
N_x^*(Z)\neq T_x^*X,
\qquad \operatorname{SS}(F)_x\cap N_x^*(Z)\subset\{0\}.
\tag{MO13}
$$

Then $(R\Gamma_ZF)_x=0$. The boundary qualification is necessary: if $Z=X$ in positive dimension, then $N_x^*(Z)=\{0\}\neq T_x^*X$, but $R\Gamma_Zk_X=k_X$. A hypothesis merely saying $x\in Z$ would therefore give a false statement. At a boundary point $N_x^*(Z)$ is nonzero; the first condition of MO13 also makes it proper.

**Proof.** Put $H=R\Gamma_ZF$ and $N=N_x^*(Z)$. Under the first condition in MO13 the strict normal $N_x(Z)$ is a nonempty open convex cone, so its polar $N$ contains no nonzero line. The boundary estimate gives $\operatorname{SS}(H)_x\subset\operatorname{SS}(F)_x-N$. This set has only the zero vector in common with $N$: if $a-n\in N$, then $a\in N+N=N$, so $a=0$ by MO13; pointedness then forces $n=0$. Separate this closed conic bound from a sufficiently small pointed convex enlargement of $N$.

Choose a closed pointed $\gamma$ with

$$
N\subset\operatorname{Int}(-\gamma^\circ)\cup\{0\},
\qquad \operatorname{SS}(H)_x\cap(-\gamma^\circ)\subset\{0\}.
\tag{MO14}
$$

The strict-normal criterion makes $Z$ locally $\gamma$-closed. Propagation now supplies $\gamma$-open $\Omega_0\subset\Omega_1$ such that $\Omega_1\setminus\Omega_0$ contains a relatively compact neighborhood of $x$ and

$$
\bigl(R\phi_{\gamma*}R\Gamma_{X\setminus\Omega_0}H\bigr)|_{\Omega_1}=0.
$$

Here is the needed neighborhood comparison in detail. MO14 gives $-\gamma\setminus\{0\}\subset N_x(Z)$. Enlarge $\gamma$ slightly to a closed cone $\Gamma$ with $\gamma\setminus\{0\}\subset\operatorname{Int}\Gamma$ and $-\Gamma\setminus\{0\}\subset N_x(Z)$. Compactness of its angular section gives a coordinate ball $U$ in which displacements in $-\Gamma$ preserve $Z$ whenever both endpoints remain in $U$. No point $z\in Z\cap U$ can satisfy $z-x\in\operatorname{Int}\Gamma$: the allowed displacements near $x-z$ would otherwise put a whole ball around $x$ inside $Z$, contradicting $x\in\partial Z$.

There is $c>0$ such that $\operatorname{dist}(v,E\setminus\operatorname{Int}\Gamma)\geq c|v|$ for $v\in\gamma$. If $z=x+b+v\in Z\cap U$, $|b|<\epsilon$ and $v\in\gamma$, the preceding exclusion gives $c|v|\leq\epsilon$. Therefore

$$
\bigl(B_\epsilon(x)+\gamma\bigr)\cap Z\cap U
\subset B_{(1+c^{-1})\epsilon}(x).
$$

This proves cofinality in the ordinary neighborhoods of $x$ in $Z\cap U$. All propagation here is on the local domain $U$, as permitted by its exact contract; no claim is made about distant components of the original $Z$. Since $H|_U$ is supported on $Z\cap U$, its stalk is the colimit of $H^r(\Omega\cap U;H|_U)$ over these directional neighborhoods $\Omega\subset\Omega_1$. Propagation identifies each group with $H^r(\Omega\cap\Omega_0\cap U;H|_U)$. Choose $\Omega$ so that $\Omega\cap Z\cap U\subset\Omega_1\setminus\Omega_0$. Then $\Omega\cap\Omega_0\cap Z\cap U$ is empty. The colimit is zero in every degree. $\square$

## SH02-MO-MICROLOCAL-SUPPORT — Where directional sheaves can live

For a closed submanifold $M\subset X$ and bounded complexes $F,G$,

$$
\operatorname{supp}(\mu_MF)\subset T_M^*X\cap\operatorname{SS}(F),
\qquad
\operatorname{supp}(\mu hom(G,F))
\subset\operatorname{SS}(G)\cap\operatorname{SS}(F).
\tag{MO15}
$$

**Proof.** A stalk of $\mu_MF$ at $p\in T_M^*X$ is the filtered colimit of $(R\Gamma_ZF)_x$ over the strict closed-support tests in `SH02-MIC-STALKS`. If $p\neq0$ and $p\notin\operatorname{SS}(F)$, its angular neighborhood may be chosen disjoint from microsupport. The strict support tests can be refined so that their nonzero normal polars lie in that neighborhood and their strict normal cone is nonempty. The strict positivity condition excludes an ordinary neighborhood of $x$ from such a support, so $x$ is either outside the support or on its boundary. In the first case its costalk is zero directly; in the second case the corrected MO13 applies. This is a cofinal refinement, so it annihilates the stalk, proving the first inclusion. At a zero covector outside microsupport the sheaf itself vanishes near the base point, and the conclusion is immediate.

To spell out the support refinement, use normal coordinates $(x',x'')$ with $M=\{x''=0\}$. The strict condition on $C_M(Z)_x$ gives, after shrinking, a constant $c>0$ with $\langle p,x''\rangle\geq c|x''|$ for points of $Z$ near $x$. Otherwise a sequence of violating normalized normal coordinates would give a nonzero vector in $C_M(Z)_x$ pairing nonpositively with $p$. Choose a small $0<\epsilon<c$ and enlarge the support locally to $\{\langle p,x''\rangle\geq\epsilon|x''|\}$. This remains an allowed strict support, contains the original germ, and has at $x$ a nonzero strict normal polar concentrated in an arbitrarily small angular neighborhood of $p$ when $\epsilon$ is small. Tangential components of that polar vanish. The point $x$ lies on its boundary. These enlargements therefore give the asserted cofinal family and make the application of MO13 explicit.

For the second inclusion apply the first one on $X\times X$ to $R\mathcal Hom(q_2^{-1}G,q_1^!F)$. Its microsupport lies in $\operatorname{SS}(F)\times\operatorname{SS}(G)^a$ by MO6. The diagonal conormal is $(x,x;\xi,-\xi)$. Intersecting the product bound with it gives exactly the second set in MO15. $\square$

## SH02-MO-EMBEDDING — Restricting across a transverse submanifold

Let $i:M\hookrightarrow X$ be a closed submanifold and assume

$$
\operatorname{SS}(F)\cap T_M^*X\subset T_X^*X.
\tag{MO16}
$$

Then

$$
\operatorname{SS}(F_M)\subset\operatorname{SS}(F)+T_M^*X,
\qquad
i^{-1}F\otimes\omega_i\xrightarrow{\sim}i^!F,
\tag{MO17}
$$

where the second arrow is the canonical tensor–exceptional comparison and

$$
\omega_i=\operatorname{or}_{M/X}[\dim M-\dim X].
$$

**Proof of the bound.** For a hypersurface, work in a chart where it separates two open sides $\Omega_+$ and $\Omega_-$. Their strict normal polars are the two opposite conormal rays. Apply the extension-by-zero boundary estimate to both sides and the triangle

$$
F_{\Omega_+}\oplus F_{\Omega_-}\longrightarrow F
\longrightarrow F_M\xrightarrow{+1}.
$$

Their two bounds lie in $\operatorname{SS}(F)+T_M^*X$, proving the claim. The equality for closed direct images in MO8 simultaneously gives

$$
\operatorname{SS}(i^{-1}F)\subset i_di_\pi^{-1}\operatorname{SS}(F)
\tag{MO18}
$$

for a hypersurface: applying $i_d$ kills the added conormal covector. For higher codimension use a local flag of hypersurfaces ending at $M$ and induct on this pair of assertions. At each stage the next inclusion is noncharacteristic: a restricted covector annihilating its tangent space lifts to a covector of $\operatorname{SS}(F)$ annihilating $TM$, which must vanish by MO16. The conormal additions along the flag sum to $T_M^*X$. This proves MO17 and MO18 without identifying $N^*(M)$ with the conormal bundle.

**Proof of the comparison.** MO15 says that $\mu_MF$ is supported on its zero section $s:M\hookrightarrow T_M^*X$. The localization triangle for the complement of that section makes the natural arrow

$$
s^!\mu_MF\longrightarrow R\pi_*\mu_MF
$$

an isomorphism. The zero-section and Sato identifications identify its source with $i^{-1}F\otimes\omega_i$ and its target with $i^!F$. Their trace compatibility identifies this particular arrow with the canonical tensor–exceptional comparison. Thus MO17 is an isomorphism of the specified maps, conditional on that map-identification contract. $\square$

## SH02-MO-NONCHAR — A map transverse to a conic set

A map $f:Y\to X$ is **noncharacteristic for $A\subset T^*X$** if

$$
f_\pi^{-1}A\cap\ker f_d
\subset Y\times_XT_X^*X.
\tag{MO19}
$$

For a closed conic $A$, MO1 shows that $f_d:f_\pi^{-1}A\to T^*Y$ is proper. Thus its image is a closed conic set. A submersion is noncharacteristic for every $A$, since its transposed differential is injective. A closed embedding need not be noncharacteristic.

## SH02-MO-PULLBACK — The general noncharacteristic inverse image

If $f$ is noncharacteristic for $\operatorname{SS}(F)$, then

$$
\operatorname{SS}(f^{-1}F)\subset f_df_\pi^{-1}\operatorname{SS}(F),
\qquad
f^{-1}F\otimes\omega_f\xrightarrow{\sim}f^!F.
\tag{MO20}
$$

**Proof.** Factor $f$ as its graph $g:Y\hookrightarrow Y\times X$, followed by the projection $q:Y\times X\to X$. MO10 describes the microsupport of $q^{-1}F$ as the covectors $(y,f(y);0,\xi)$ with $(f(y),\xi)\in\operatorname{SS}(F)$. Such a covector is conormal to the graph precisely when $d f_y^t\xi=0$. Thus MO19 is exactly the hypothesis needed to apply MO17 to the graph. MO18 followed by the cotangent map of the projection proves the estimate. The canonical comparisons for $q$ and $g$ compose to that for $qg=f$, while

$$
\omega_g\otimes g^{-1}\omega_q\simeq\omega_f.
$$

The submersion formula and MO17 therefore prove the second statement with its canonical map. $\square$

## SH02-MO-DIAGONAL — Tensor and Hom on one manifold

If $\operatorname{SS}(F)\cap\operatorname{SS}(G)^a$ is zero, then

$$
\operatorname{SS}(F\otimes G)\subset\operatorname{SS}(F)+\operatorname{SS}(G).
\tag{MO21}
$$

If $\operatorname{SS}(F)\cap\operatorname{SS}(G)$ is zero, then

$$
\operatorname{SS}(R\mathcal Hom(G,F))
\subset\operatorname{SS}(F)+\operatorname{SS}(G)^a.
\tag{MO22}
$$

Under the second assumption, if $G$ also has cohomologically constructible local data in the precise biduality sense, evaluation gives

$$
R\mathcal Hom(G,k_X)\otimes F
\xrightarrow{\sim}R\mathcal Hom(G,F).
\tag{MO23}
$$

**Proof.** Let $\delta:X\hookrightarrow X\times X$ be the diagonal. The identities

$$
F\otimes G=\delta^{-1}(F\boxtimes G),
\qquad
R\mathcal Hom(G,F)
\simeq\delta^!R\mathcal Hom(q_2^{-1}G,q_1^!F)
$$

are respectively tensor restriction and exceptional internal adjunction. The cotangent map of $\delta$ adds the two covectors; its kernel consists of $(\xi,-\xi)$. MO5 and MO6 show that the two different intersection assumptions make this embedding noncharacteristic for the corresponding external complex. Apply MO20. Its orientation factor does not change microsupport, so it applies equally to $\delta^!$ and $\delta^{-1}$; this proves MO21–MO22.

For MO23, the external constructibility comparison identifies $R\mathcal Hom(q_2^{-1}G,q_1^!F)$ with the external dual–tensor expression. Pull its evaluation map back to the diagonal and apply the canonical noncharacteristic comparison. The relative diagonal orientation cancels the orientation in $q_1^!$, since $q_1\delta=\mathrm{id}$. The resulting map is precisely ordinary internal evaluation in MO23. No constructibility assumption is used in MO21 or MO22. $\square$

### SH02-MO-CHARACTERISTIC-BOUNDARY — The range of these estimates

The ordinary sum in MO21 and the ordinary cotangent image in MO20 depend on the no-cancellation hypotheses. Their characteristic analogues involve limiting cone operations. This lesson does not infer such an analogue by dropping the hypotheses from either formula.

## SH02-MO-RELATIVE-CUTOFF — Replacing a nonproper map by a bounded part

Let $f:Y\to X$, $G\in D^b(k_Y)$, and $\varphi:Y\to\mathbb R$ be $C^1$. Write

$$
Y_t=\{\varphi<t\},\quad \overline Y_t=\{\varphi\leq t\},
\quad j_t:Y_t\hookrightarrow Y,\quad i_t:\overline Y_t\hookrightarrow Y.
$$

The bar here denotes a closed sublevel, not an assertion that it is the closure of the open sublevel. Set $f_t=fj_t$ and $\overline f_t=fi_t$. Assume

$$
f:\operatorname{supp}(G)\cap\overline Y_t\longrightarrow X
\text{ is proper for every real }t.
\tag{MO24}
$$

Put $V_f=f_d(Y\times_XT^*X)$, and fix $t_0\in\mathbb R$.

If

$$
d\varphi_y\notin\operatorname{SS}(G)_y+(V_f)_y
\quad\text{for }\varphi(y)>t_0,
\tag{MO25+}
$$

restriction gives the isomorphisms

$$
Rf_*G\xrightarrow{\sim}R(f_t)_*j_t^{-1}G\quad(t>t_0),
\qquad
Rf_*G\xrightarrow{\sim}R(\overline f_t)_*i_t^{-1}G\quad(t\geq t_0).
\tag{MO26+}
$$

If instead

$$
-d\varphi_y\notin\operatorname{SS}(G)_y+(V_f)_y
\quad\text{for }\varphi(y)>t_0,
\tag{MO25-}
$$

extension and the exceptional counit give

$$
R(f_t)_!j_t^{-1}G\xrightarrow{\sim}Rf_!G\quad(t>t_0),
\qquad
R(\overline f_t)_*i_t^!G\xrightarrow{\sim}Rf_!G\quad(t\geq t_0).
\tag{MO26-}
$$

In the closed formula of MO26−, the ordinary direct image is legitimate because its support is proper by MO24. Under MO25+ for $Rf_*$, or under MO25− for $Rf_!$, respectively, one has

$$
\operatorname{SS}(Rf_{\diamond}G)
\subset
f_\pi f_d^{-1}\bigl(\operatorname{SS}(G)\cap T^*Y|_{\overline Y_{t_0}}\bigr)
\subset f_\pi f_d^{-1}\operatorname{SS}(G),
\qquad \diamond\in\{*,!\}.
\tag{MO27}
$$

The second relation is an inclusion. Equality of those two geometric images does not follow from the hypotheses; an example below shows why.

The antecedent for nonproper control is Kashiwara–Schapira, *Microlocal Study of Sheaves*, Theorem 4.4.1, pp. 73–75 (PDF pp. 76–78): an exhausting family with proper support and one-sided strict-normal exclusion gives stable open cutoffs and the direct-image estimate. That theorem explains why horizontal covectors must be included in the exclusion. Its printed statement is not the four-map endpoint statement (MO26) or the localized bound (MO27). Those statements are proved below by the proper map formed from the original map and the exhaustion, the two one-sided mechanisms (MO29)–(MO30), and the separate compact-neighborhood and support-colimit passages. In particular, the relative cutoff proof is part of this unit; neither its negative-sign case nor its closed endpoint is being supplied by a change of citation.

### SH02-MO-ONE-SIDED — The one-parameter mechanism

We first justify the section argument used in the proof. Suppose $H\in D^b(k_{U\times\mathbb R})$ satisfies

$$
\operatorname{SS}(H)|_{s>t_0}\subset
\{(x,s;\xi,\sigma):\sigma\leq0\}.
\tag{MO28}
$$

For any convex coordinate open $W\subset U$ and $t>t_0$,

$$
R\Gamma(W\times\mathbb R;H)
\xrightarrow{\sim}R\Gamma(W\times(-\infty,t);H).
\tag{MO29}
$$

Indeed, on the upper tail the cone characterization with the positive vertical ray makes $H$ a pullback from that directional topology. The ordinary convex set $W\times(t_0,t)$ has directional saturation $W\times(t_0,\infty)$. Derived convex continuation identifies their section complexes by restriction. Apply Mayer–Vietoris to the cover of $W\times\mathbb R$ by $W\times(-\infty,t)$ and $W\times(t_0,\infty)$: since the latter term maps isomorphically to the intersection, the former computes the global sections. The same argument is valid after an increasing coordinate change identifying a tail with a full line; microsupport transforms with the positive derivative, so the sign is unchanged.

With $\sigma\geq0$ in MO28, the opposite cone gives, for $t_0<t<t'$,

$$
R\Gamma_{W\times(-\infty,t]}(W\times\mathbb R;H)
\xrightarrow{\sim}
R\Gamma_{W\times(-\infty,t']}(W\times\mathbb R;H).
\tag{MO30}
$$

To check this without dualizing an arbitrary sheaf, use the support triangle for the difference $(t,t']$. On $W\times(t,\infty)$, restriction to $W\times(t',\infty)$ is an isomorphism: both have the same saturation for the negative vertical cone. Their localization fibre, the derived sections with support in $(t,t']$, is zero. This is precisely the cone of MO30. The argument proves the supported statement directly and does not require reflexive Verdier duality.

### SH02-MO-CUTOFF-PROOF — Proof of the four cutoff maps

The map $h=(f,\varphi):Y\to X\times\mathbb R$ is proper on $\operatorname{supp}(G)$. The inverse image of a compact subset is closed in the inverse image of a compact base set intersected with some closed sublevel, which is compact by MO24. Put $H=Rh_*G$ and let $q:X\times\mathbb R\to X$ be projection. Proper base change identifies every cutoff in MO26 with the corresponding cutoff for $H$, and $Rf_*G=Rq_*H$, $Rf_!G=Rq_!H$.

Under MO25+, MO8 implies MO28. In fact a covector $(x,s;\xi,\sigma)$ in the estimated microsupport comes from

$$
d f_y^t\xi+\sigma\,d\varphi_y\in\operatorname{SS}(G)_y.
$$

If $s>t_0$ and $\sigma>0$, division by $\sigma$ contradicts MO25+, since $V_f$ is a vector space in each fibre. MO29 on a basis of $X$ proves the open ordinary formula in MO26+.

To obtain the closed formula, fix $x\in X$ and $b>t$. The set $C=\operatorname{supp}(H)\cap(\{x\}\times(-\infty,t])$ is compact. Neighborhoods $W\times(-\infty,u)$, with $W\ni x$ shrinking and $t<u<b$ decreasing to $t$, are cofinal neighborhoods of $C$ relative to the support. Otherwise points escaping a prescribed neighborhood would have base tending to $x$ and height at most $u$; properness below $b$, after fixing a compact base neighborhood, gives a convergent subsequence with limit in $C$, a contradiction. Compact-neighborhood continuity therefore identifies the colimit of their cohomology with $H^r(\{x\}\times(-\infty,t];H)$. Proper base change identifies the latter with the closed-cutoff image stalk. The maps from the full image into all the open-cutoff stalk systems are already isomorphisms. Their colimit proves the closed comparison at $x$. This includes $t=t_0$, since only $u>t_0$ was used. The argument always keeps both the compact support sublevel and the shrinking base neighborhood; it never treats an unbounded half-strip as a compact set.

Under MO25− the same argument gives $\sigma\geq0$ on the upper tail. MO30 makes the supported closed cutoffs constant for $t>t_0$. Their filtered colimit is $Rq_!H$: locally over a compact base set, every support proper over that base is compact and therefore lies below some finite level; conversely supports in a closed sublevel are proper by MO24. This is a cofinality statement about proper supports, not a claim that ordinary sections commute with an arbitrary closed exhaustion. The finite cohomological dimension of proper direct image permits the support-family colimit on bounded resolutions. It proves the closed formula for $t>t_0$. For $t=t_0$, use localization and the increasing union $\{s>t_0\}=\bigcup_{t>t_0}\{s>t\}$. On a flabby resolution, sections on that increasing union are computed by the standard inverse-limit complex, with surjective termwise restrictions. The already constant cohomology systems give zero derived-limit obstruction. Taking fibres in the localization triangle proves the endpoint formula. Open cutoffs are the filtered union of smaller closed support cutoffs; their extension maps are the maps in MO26−. This proves the open exceptional formula for $t>t_0$.

It remains to prove the localized bound. For the ordinary case apply the open boundary estimate to $H$ on $\{s<t\}$, and then proper image to its ordinary extension $Rj_*j^{-1}H$, whose support lies in $\{s\leq t\}$. At the new boundary, both its added normal covector and a preexisting vertical covector of $H$ are nonpositive. A sum with vertical component zero must have both components zero. Away from the boundary no normal is added. The result is

$$
\operatorname{SS}(Rq_*H)
\subset\{(x,\xi): (x,s;\xi,0)\in\operatorname{SS}(H)
\text{ for some }s\leq t\}.
$$

Use MO8 for $h$ to lift such a covector to $\operatorname{SS}(G)$ over $\varphi\leq t$. For the exceptional case use the closed supported cutoff and its boundary estimate; both vertical signs are now nonnegative and the same no-cancellation conclusion holds. Finally let $t\downarrow t_0$. The lifting points lie over a fixed base point in the compact support sublevel for any fixed $t_1>t_0$, and their covectors equal $d f_y^t\xi$. A convergent subsequence and closedness give a lift with $\varphi\leq t_0$. This proves MO27. $\square$

### SH02-MO-RELATIVE-COVECTOR — A quotient formulation

If $f$ is a submersion, the quotient bundle

$$
T^*(Y/X)=T^*Y/V_f
$$

is the relative cotangent bundle. If $p$ is its quotient map, MO25± says exactly

$$
\pm p(d\varphi_y)\notin p(\operatorname{SS}(G)_y)
\quad(\varphi(y)>t_0).
$$

Indeed two covectors have the same quotient precisely when their difference is horizontal. For a general map the same fibrewise quotient statement makes sense as a quotient of vector spaces; it need not form a vector bundle when the differential changes rank.

## SH02-MO-MORSE — Cohomology between two levels

Let $\varphi:X\to\mathbb R$ be $C^1$, proper on $\operatorname{supp}(F)$, and let $a<b$.

If $d\varphi_x\notin\operatorname{SS}(F)$ whenever $a\leq\varphi(x)<b$, then the natural restrictions

$$
R\Gamma(\{\varphi<b\};F)
\xrightarrow{\sim}R\Gamma(\{\varphi\leq a\};F)
\xrightarrow{\sim}R\Gamma(\{\varphi<a\};F)
\tag{MO31}
$$

are isomorphisms. If $-d\varphi_x\notin\operatorname{SS}(F)$ for $a<\varphi(x)\leq b$, then

$$
R\Gamma_{\{\varphi\leq a\}}(X;F)
\xrightarrow{\sim}R\Gamma_{\{\varphi\leq b\}}(X;F).
\tag{MO32}
$$

If the negative exclusion instead holds on $a\leq\varphi(x)<b$, then

$$
R\Gamma_c(\{\varphi<a\};F)
\xrightarrow{\sim}R\Gamma_c(\{\varphi<b\};F).
\tag{MO33}
$$

**Proof.** Properness permits replacement of $F$ by $H=R\varphi_*F$ on the line, using MO8 and proper base change for both ordinary and supported sections. Its microsupport has no positive covectors on $[a,b)$ in the first case and no negative covectors on the corresponding interval in the other cases. The one-sided argument proves invariance between levels strictly inside these intervals. Endpoint passage is local near $a$ or $b$: split off a fixed lower open tail by Mayer–Vietoris, so the varying part lies in a compact interval. Compact-neighborhood continuity gives a closed endpoint as a colimit of larger open neighborhoods. An open endpoint is the increasing union of smaller opens; their already constant cohomology system has no derived-limit obstruction. This gives the two arrows of MO31 with the stated inclusion of $a$ and exclusion of $b$.

For MO32 use the supported argument MO30; the varying support is the half-open band $(a,b]$, so precisely that band requires the negative exclusion. For MO33 write compactly supported cohomology of an open sublevel as the filtered colimit over closed supports strictly inside it and use the same supported localization argument. The changing band is now $[a,b)$. The properness of $\varphi$ on the support makes every closed bounded band compact; the unchanged lower tail may be noncompact and is retained throughout. No bounded-below exhaustion of the whole support is being assumed here. $\square$

## SH02-MO-FIELD-BOUNDARY — Local jumps and finite Morse data

Only in this section and the following proof, assume that $k$ is a field. Let $F\in D^b(k_X)$ and let $\varphi$ be $C^\infty$. Suppose:

1. $\operatorname{supp}(F)\cap\{\varphi\leq t\}$ is compact for every $t$;
2. the graph $\{(x,d\varphi_x):x\in X\}$ meets $\operatorname{SS}(F)$ at finitely many points $p_1,\ldots,p_N$;
3. for $x_i=\pi(p_i)$, the jump complex

$$
J_i=\bigl(R\Gamma_{\{\varphi\geq\varphi(x_i)\}}F\bigr)_{x_i}
$$

has finite-dimensional cohomology in a bounded range.

The graph of $d\varphi$ is Lagrangian: pullback of the tautological one-form is $d\varphi$, hence pullback of its exterior derivative vanishes, and the graph has half the cotangent dimension. It need not be conic. No nondegenerate critical-point hypothesis is imposed on these finitely many intersections.

## SH02-MO-MORSE-INEQUALITIES — A finite filtration by local tests

Under those three hypotheses, $R\Gamma(X;F)$ has bounded finite-dimensional cohomology. Set

$$
b_j=\dim_k H^j(X;F),\qquad
m_j=\sum_{i=1}^N\dim_k H^j(J_i).
$$

For every integer $\ell$,

$$
\sum_{j\leq\ell}(-1)^{\ell-j}b_j
\leq\sum_{j\leq\ell}(-1)^{\ell-j}m_j,
\qquad
\sum_j(-1)^j b_j=\sum_j(-1)^j m_j.
\tag{MO34}
$$

**Proof.** First suppose $N=0$. The closed support is bounded below under $\varphi$: otherwise the nonempty nested compact sets $\operatorname{supp}(F)\cap\{\varphi\leq-n\}$ would have nonempty intersection inside one compact sublevel, which is impossible for a real-valued function. Choose $a$ below this support. There are no failed positive tests at any level, so MO31 identifies $R\Gamma(\{\varphi<b\};F)$ with $R\Gamma(\{\varphi<a\};F)=0$ for every $b>a$. An increasing sequence $b\to+\infty$ exhausts $X$. The open-union Milnor comparison gives $R\Gamma(X;F)=0$, since both the inverse limit and its first derived limit of these zero groups vanish in every degree. If the support is empty, the conclusion holds immediately. Thus $b_j=m_j=0$ for every $j$, proving both assertions in this case.

Now suppose $N>0$. Put $H=R\varphi_*F$. The function is proper on the support because every compact interval lies in a compact sublevel. Let $c_1<\cdots<c_r$ be the distinct values of the $\varphi(x_i)$. Proper base change and localization identify the jump of $H$ at $c_\nu$ with

$$
L_\nu=\bigl(R\Gamma_{[c_\nu,\infty)}H\bigr)_{c_\nu}
\simeq\bigoplus_{\varphi(x_i)=c_\nu}J_i.
\tag{MO35}
$$

Indeed the supported sheaf restricted to that compact fibre has zero stalk away from the finitely many $x_i$, by the definition of microsupport. A sheaf complex supported at finitely many isolated points has global sections equal to the direct sum of its stalk complexes. This proves MO35 without assuming constructibility of $F$ elsewhere.

There is no contribution below $c_1$. One way to see this is to use compact sublevels: their nonempty intersection as the level tends to $-\infty$ would contradict compactness of any one sublevel, so the support is bounded below. MO31 then propagates the zero section complex up to the first exceptional level. Between consecutive $c_\nu$, and above $c_r$, MO31 identifies the section complexes. At a level $c_\nu$, localization supplies the triangle

$$
L_\nu\longrightarrow B_\nu\longrightarrow B_{\nu-1}\xrightarrow{+1},
\tag{MO36}
$$

where $B_\nu$ is cohomology up through that closed level and $B_{\nu-1}$ is cohomology just below it. The endpoint identifications use compact sublevels and compact-neighborhood continuity. Thus $B_0=0$, $B_r\simeq R\Gamma(X;F)$, and a finite induction in MO36 proves bounded finite-dimensional cohomology of every $B_\nu$.

For completeness, take any triangle $A\to B\to C\xrightarrow{+1}$ of bounded finite-dimensional complexes. If $r_j$ is the rank of its connecting map $H^j(C)\to H^{j+1}(A)$, exactness gives

$$
\dim H^j(B)=\dim H^j(A)+\dim H^j(C)-r_{j-1}-r_j.
$$

Alternating up to degree $\ell$ cancels all ranks except $r_\ell$, yielding

$$
\sum_{j\leq\ell}(-1)^{\ell-j}\dim H^j(B)
=\sum_{j\leq\ell}(-1)^{\ell-j}
\bigl(\dim H^j(A)+\dim H^j(C)\bigr)-r_\ell.
$$

Apply this to MO36 and telescope. The nonnegative ranks give the inequality in MO34. Alternating over the entire bounded range eliminates every rank and gives Euler equality. $\square$

We now return to an arbitrary commutative coefficient ring of finite global dimension. The remaining conic and Fourier statements do not require a field.

## SH02-MO-LEGENDRE — Exchanging a vector with a covector

Let $\tau:E\to Z$ be a real vector bundle. Its Euler field is the infinitesimal fibre dilation,

$$
e=\sum_i x_i\frac{\partial}{\partial x_i}.
$$

For $p\in T^*E$, define $\theta_E(p)=p(e)$. In local bundle coordinates $(z,x;\zeta,\xi)$,

$$
\theta_E=\langle x,\xi\rangle,
\qquad \alpha_E=\langle\zeta,dz\rangle+\langle\xi,dx\rangle.
$$

The restriction of a covector to the vertical tangent defines a canonical map $\psi_E:T^*E\to E^*$ over $Z$.

Let $V_E=\ker(d\tau:TE\to\tau^{-1}TZ)$ be the vertical tangent bundle. A fibre vector gives its translation-invariant tangent vector in that fibre, so $V_E\simeq E\times_ZE$. In a bundle chart, $d\tau$ is projection onto the base tangent coordinates. Consequently it is surjective, and dualizing its kernel sequence gives the intrinsic exact sequence over $E$
\[
0\longrightarrow E\times_ZT^*Z
\xrightarrow{{}^td\tau}T^*E
\longrightarrow V_E^*=T^*(E/Z)\longrightarrow0.
\]
The last map is restriction to vertical tangent vectors. The identification $V_E^*\simeq E\times_ZE^*$ identifies its fibre over a point of $Z$ with $T^*(E_z)=E_z\times E_z^*$. Projection to the second factor is the map $\psi_E$. This construction uses the vertical bundle itself and requires no choice of a horizontal splitting.

There is a unique map

$$
\Phi_E:T^*E\longrightarrow T^*E^*
$$

whose base projection is $\psi_E$ and which satisfies

$$
\Phi_E^*\alpha_{E^*}=\alpha_E-d\theta_E.
\tag{MO37}
$$

Its coordinate expression is

$$
\Phi_E(z,x;\zeta,\xi)=(z,\xi;\zeta,-x).
\tag{MO38}
$$

**Proof.** Since $\alpha_E-d\theta_E=\langle\zeta,dz\rangle-\langle x,d\xi\rangle$, the proposed expression has both required properties. Conversely its prescribed base coordinates are $(z,\xi)$; equality of the coefficients of $dz$ and $d\xi$ forces its remaining coordinates to be $(\zeta,-x)$. This proves local uniqueness, so local expressions agree under bundle coordinate changes and define a global map. The formula also gives

$$
\theta_{E^*}\Phi_E=-\theta_E,
\qquad
\Phi_{E^*}\Phi_E(z,x;\zeta,\xi)=(z,-x;\zeta,-\xi).
\tag{MO39}
$$

The latter is the **cotangent lift of the fibre antipode** $a_E(z,x)=(z,-x)$; it is not the antipode of every cotangent fibre over the same point. In particular it fixes the base covector $\zeta$. $\square$

### SH02-MO-SYMPLECTIC — Symplectic, with two different dilations

Taking exterior derivatives in MO37 gives $\Phi_E^*d\alpha_{E^*}=d\alpha_E$, so $\Phi_E$ is symplectic. On every component where $E$ has positive rank, $\Phi_E$ does not preserve the tautological one-form or ordinary cotangent dilation: for instance, scaling a nonzero $\xi$ changes the base point in $E^*$ in MO38. In rank zero, $E=Z$, $\theta_E=0$, and $\Phi_E$ is the identity on $T^*Z$, preserving both.

The two natural positive actions on $T^*E$ are

$$
r_\lambda(z,x;\zeta,\xi)=(z,x;\lambda\zeta,\lambda\xi),
\qquad
s_\mu(z,x;\zeta,\xi)=(z,\mu x;\zeta,\mu^{-1}\xi).
\tag{MO40}
$$

The first dilates cotangent fibres, while the second is the cotangent lift of fibre dilation on $E$. A set invariant under both is called **biconic**. These actions commute. Their behavior under Fourier exchange is

$$
\Phi_E r_\lambda=r_\lambda s_\lambda\Phi_E,
\qquad \Phi_E s_\mu=s_{\mu^{-1}}\Phi_E,
$$

where the actions on the right are on $T^*E^*$. Thus $\Phi_E$ carries biconic sets to biconic sets.

## SH02-MO-CONIC-TEST — The Euler equation detects conic sheaves

Put $S_E=\theta_E^{-1}(0)$. For $F\in D^b(k_E)$,

$$
F\text{ is conic}\quad\Longleftrightarrow\quad
\operatorname{SS}(F)\subset S_E.
\tag{MO41}
$$

Here conic means that each cohomology sheaf is locally constant along positive radial orbits, with the orbit topology used in the conic descent lesson. If $F$ is conic, its microsupport is biconic.

**Proof.** Remove the zero section. The positive-ray quotient $\dot E/\mathbb R_{>0}$ is a manifold, and the quotient map is a submersion; locally this is the projection from an angular patch times $(0,\infty)$. Its vertical tangent is spanned by the Euler field. Hence its horizontal cotangent set is exactly $S_E|_{\dot E}$. MO10 and local descent prove MO41 off the zero section. On the zero section the Euler field is zero, so $S_E$ contains every cotangent vector there; also each radial orbit there is a point. Both conditions impose no further constraint at those points. This proves the global equivalence.

Microsupport is always invariant under $r_\lambda$. Conic descent gives a sheaf isomorphism under each positive bundle dilation; covariance under that diffeomorphism makes microsupport invariant under $s_\mu$. This proves biconicity. $\square$

### SH02-MO-BICONIC-PROJECTION — Horizontal directions move to the zero section

The zero section identifies $T^*Z$ with $\{(z,0;\zeta,0)\}\subset T^*E$. If $A\subset T^*E$ is closed and biconic, then

$$
\tau_\pi\tau_d^{-1}A=A\cap T^*Z.
\tag{MO42}
$$

**Proof.** A point on the left is represented by $(z,x;\zeta,0)\in A$. Apply $s_\mu$ and let $\mu\downarrow0$. Closedness gives $(z,0;\zeta,0)\in A$. Conversely that point itself represents the required horizontal lift. Only the $s_\mu$ invariance is needed for this argument. $\square$

## SH02-MO-CONIC-PUSH — Radial control replaces support properness

Let $F\in D^b(k_E)$ be conic, and write $\dot\tau:\dot E\to Z$ for the projection with the zero section removed. Then

$$
\begin{aligned}
\operatorname{SS}(R\tau_*F)&\subset T^*Z\cap\operatorname{SS}(F),\\
\operatorname{SS}(R\tau_!F)&\subset T^*Z\cap\operatorname{SS}(F),\\
\operatorname{SS}(R\dot\tau_*(F|_{\dot E}))
&\subset\dot\tau_\pi\dot\tau_d^{-1}\operatorname{SS}(F|_{\dot E}),\\
\operatorname{SS}(R\dot\tau_!(F|_{\dot E}))
&\subset\dot\tau_\pi\dot\tau_d^{-1}\operatorname{SS}(F|_{\dot E}).
\end{aligned}
\tag{MO43}
$$

No properness of $\tau$ on the whole support is required.

**Proof.** The assertion is local over $Z$, so choose a bundle metric there. On $E$ use $\varphi(x)=|x|^2$. Its sublevels are proper over $Z$. At $x\neq0$, $d\varphi(e)=2|x|^2>0$, while every covector of $\operatorname{SS}(F)$ and every horizontal covector annihilates $e$, by MO41. Both signs in MO25 therefore hold outside $\varphi\leq0$. MO27 bounds the two full-bundle images by the horizontal microsupport over the zero section, proving the first two formulas.

On $\dot E$ use $\varphi(x)=|x|^2+|x|^{-2}$. Its sublevels are compact radial annuli over compact base sets. The derivative on the Euler field is $2(|x|^2-|x|^{-2})$, which is nonzero when $\varphi>2$. The same argument with $t_0=2$ bounds both punctured images by the horizontal microsupport on the unit sphere. This is contained in the stated image. Positive dilation carries every horizontal microsupport point on $\dot E$ to the unit sphere, so this description also proves closedness of the stated image locally: the relevant sphere projection is proper. Different local metrics yield the same intrinsic estimate. $\square$

## SH02-MO-STABILIZATION — A harmless extra pair of variables

Use the Fourier convention in the dependency table. Let $K=k_{\mathbb R\times\{0\}}$ on an extra plane with coordinates $(s,t)$, and give its dual plane coordinates $(u,v)$. With the usual orientation of the $s$-line,

$$
T_{E\oplus\mathbb R^2}(F\boxtimes K)
\simeq (T_EF)\boxtimes k_{\{0\}\times\mathbb R}[-1].
\tag{MO44}
$$

The external product here is with the trivial plane; the base remains $Z$.

**Proof.** Compute from the proper-support kernel. The $t$ variable is fixed to zero, and the inequality becomes $\langle x,y\rangle+su\leq0$. Integrate first in $s$. For $u\neq0$, its allowed set is a closed half-line, whose compactly supported cohomology is zero. For $u=0$, it is either empty or the full line, according as $\langle x,y\rangle>0$ or $\leq0$. The full line contributes $k[-1]$ with the chosen orientation. Proper-support base change, valid also along the closed locus $u=0$, therefore identifies the intermediate image with the negative-pairing kernel supported on $u=0$, shifted by $[-1]$. Its identification is a sheaf identification: the restriction off $u=0$ is zero, and the closed localization triangle identifies it with the closed image of its restriction to $u=0$. The remaining proper-support integration is exactly $T_EF$, and $v$ is unrestricted. This proves MO44 without assuming a separate general product theorem. $\square$

## SH02-MO-FS-SS — Fourier transformation of microsupport

For every bounded conic complex $F$ on a real vector bundle $E$,

$$
\operatorname{SS}(T_EF)=\Phi_E\bigl(\operatorname{SS}(F)\bigr).
\tag{MO45}
$$

The equality includes base points on the zero section and covectors whose vertical component is zero. It uses the general coefficient ring, with no constructibility condition.

Kashiwara–Schapira, *Microlocal Study of Sheaves*, Propositions 5.1.1–5.1.3 and Theorem 5.1.4, pp. 77–80 (PDF pp. 80–83), give the Euler criterion, conic direct-image bounds, the same canonical exchange, and the Fourier microsupport equality. Their proof also uses an extra pair of variables to reach the two zero loci. Here the supported-zero-section triangle first reduces to a nonzero incidence calculation, so the boundary estimate used there has no characteristic zero-vector exception. The kernel computation (MO44) and the closed-image and submersion equalities then verify the stabilization explicitly. The fibre antipode in (MO39) leaves the base covector fixed, exactly as in Proposition 5.1.3.

### SH02-MO-INCIDENCE — The nonzero incidence calculation

We first prove the inclusion in MO45 at points

$$
p=(z,x_0;\zeta,\xi_0),\qquad x_0\neq0,\quad\xi_0\neq0.
$$

Assume temporarily that $R\Gamma_ZF=0$, where $Z$ is the zero section. Let $P=\{\langle x,y\rangle\geq0\}\subset E\times_ZE^*$ and let $p_1,p_2$ be its ambient projections. Put

$$
H=R\Gamma_Pp_1^{-1}F.
$$

Since $F\simeq Rj_*F|_{\dot E}$ under the temporary assumption, open-product base change and localization give

$$
T_EF\simeq R\dot p_{2*}(H|_{\dot E\times_ZE^*}).
\tag{MO46}
$$

The sheaf inside this image is conic under positive dilation of $x$. If $\Phi_E(p)=(z,\xi_0;\zeta,-x_0)$ belongs to $\operatorname{SS}(T_EF)$, the punctured estimate MO43 supplies some $x_1\neq0$ for which

$$
(z,x_1,\xi_0;\zeta,0,-x_0)\in\operatorname{SS}(H).
\tag{MO47}
$$

If $\langle x_1,\xi_0\rangle\neq0$, either $H$ is zero nearby or it is $p_1^{-1}F$, whose $y$-covector is zero by MO10. Either possibility contradicts MO47. Hence the point lies on the boundary of $P$. That boundary is smooth there and has defining differential

$$
d\langle x,y\rangle=\langle y,dx\rangle+\langle x,dy\rangle.
$$

The closed-halfspace computation gives the nonnegative multiples of this differential as the nonzero microsupport of $k_P$. The sheaf $p_1^{-1}F$ has $y$-covector zero, while a nonzero such boundary normal has $y$-covector $\lambda x_1\neq0$. Therefore the two microsupports have no nonzero intersection, and MO22 applies to $H=R\mathcal Hom(k_P,p_1^{-1}F)$. It expresses MO47 as

$$
(\zeta,0,-x_0)=(\zeta,\alpha,0)-\lambda(0,\xi_0,x_1),
\quad\lambda\geq0,
\quad(z,x_1;\zeta,\alpha)\in\operatorname{SS}(F).
$$

Consequently $x_0=\lambda x_1$, $\alpha=\lambda\xi_0$, and $\lambda>0$. Apply $s_\lambda$ from MO40 to this microsupport point. Biconicity gives $(z,x_0;\zeta,\xi_0)\in\operatorname{SS}(F)$. Thus membership in the transformed microsupport implies membership at $p$, proving the desired inclusion in this case.

Remove the temporary assumption with the triangle

$$
R\Gamma_ZF\longrightarrow F\longrightarrow Rj_*F|_{\dot E}\xrightarrow{+1}.
$$

Near $x_0\neq0$, its first term is zero, so $p$ is absent from the third term whenever it is absent from $F$. The preceding calculation applies to the third term because its supported restriction to $Z$ is zero. The Fourier transform of the first term is a pullback from $Z$: writing it as $i_*i^!F$, the proper-support kernel directly gives $T_E(i_*i^!F)\simeq\tau_{E^*}^{-1}i^!F$. Its microsupport has vertical dual covector zero by MO10, so it cannot contain $\Phi_E(p)$ when $x_0\neq0$. The triangle inequality proves the inclusion at all points with $x_0\neq0$, $\xi_0\neq0$.

### SH02-MO-ZERO-DIRECTIONS — Reaching the two zero loci

For an arbitrary $p=(z,x_0;\zeta,\xi_0)\notin\operatorname{SS}(F)$, form $F'=F\boxtimes k_{\mathbb R\times\{0\}}$ and the enlarged point

$$
p'=(z,x_0,1,0;\zeta,\xi_0,0,1).
$$

The product estimate MO5 makes $p'$ absent from $\operatorname{SS}(F')$. Both its vector $(x_0,1,0)$ and its vertical covector $(\xi_0,0,1)$ are nonzero, so the incidence calculation applies. It excludes

$$
\Phi(p')=(z,\xi_0,0,1;\zeta,-x_0,-1,0)
$$

from the microsupport of $T F'$. By MO44 this transform is $T_EF\boxtimes k_{\{0\}\times\mathbb R}[-1]$. Its microsupport is exactly

$$
\{(z,y,0,v;\zeta,\eta,\alpha,0):
(z,y;\zeta,\eta)\in\operatorname{SS}(T_EF),\ \alpha\in\mathbb R\}.
$$

To verify this equality, first pull $T_EF$ back under the submersion adding $v$, then push forward by the closed embedding $u=0$; use the equalities MO10 and MO8. The shift has no effect. Exclusion of $\Phi(p')$ therefore excludes $(z,\xi_0;\zeta,-x_0)$ from $\operatorname{SS}(T_EF)$. This proves the inclusion everywhere.

Finally apply that inclusion to $T_EF$ on $E^*$. The twice-applied same-sign Fourier transform is pullback by the fibre antipode on $E$, tensored with an invertible orientation complex and shifted. Hence its microsupport is the cotangent lift $a_E^\#\operatorname{SS}(F)$. MO39 says $\Phi_{E^*}\Phi_E=a_E^\#$. Applying the inverse of $\Phi_{E^*}$ to the second inclusion proves the reverse inclusion in MO45. The orientation and shift affect the sheaf equivalence but do not affect microsupport. $\square$

## SH02-MO-STRICT-PUSH — Two reasons a proper image estimate can be strict

All the examples asserting nonempty microsupport assume $k\neq0$.

First consider the proper homeomorphism

$$
f:\mathbb R^2\longrightarrow\mathbb R^2,
\qquad f(s,t)=(s,t^3+s^2t).
$$

For each fixed $s$, the second coordinate is strictly increasing from $-\infty$ to $+\infty$. Also $|t^3+s^2t|\geq|t|^3$, so inverse images of compact sets are bounded and closed. Thus the continuous bijection is proper and is a homeomorphism. Its constant sheaf image is constant, so its microsupport is the zero section. At $(0,0)$, however, the differential has rank one; every target covector in the second-coordinate direction pulls back to zero. The geometric right side of MO8 contains that entire line of covectors at the origin. The strictness comes from degeneracy of the differential, even though the underlying map loses no topological information.

There is also cancellation in cohomology. Take $k=\mathbb Q$ and let $L$ be the rank-one local system on the circle with monodromy $-1$. A cell decomposition with one vertex and one edge computes its cohomology by $[\mathbb Q\xrightarrow{-2}\mathbb Q]$, which is acyclic. For the proper map to a point, $Rf_*L=0$, so its microsupport is empty. The geometric image of the zero-section microsupport of $L$ is the nonempty zero cotangent fibre of the point. This is strictness without a critical differential in the manifold map to a point.

### SH02-MO-HOLOMORPHIC-IMPORT — A distinct finite complex-analytic phenomenon

[Finite holomorphic maps with arbitrary weak coefficients](../../../SH-02/weak-coefficients.html#WC6) proves the stronger equality over every commutative coefficient ring, for bounded complexes locally constant in cohomology on a locally finite complex analytic stratification. Its statement is

$$
\operatorname{SS}(Rf_*G)=f_\pi f_d^{-1}\operatorname{SS}(G)
$$

for finite holomorphic $f$, with $G$ complex constructible in the relevant bounded coefficient category. The [proof over arbitrary weak coefficients](../../../SH-02/weak-coefficients.html#WC6) includes infinitely generated and nonperfect stalks, ramification, and positive-codimension images. It retains the actual vanishing-cycle unit, finite direct-sum stalk maps, and closed-support comparison. The two real examples above do not have the required holomorphic hypotheses.

## SH02-MO-STRICT-PULL — A disappearing sector with a nonempty estimate

On $\mathbb R^2$ with coordinates $(u,v)$, let

$$
F=k_{\{u>0,\ v\geq0\}},\qquad M=\{u+v=0\}.
$$

At the origin the exact microsupport cone is

$$
\operatorname{SS}(F)_0
=\{a\,du+b\,dv:a\leq0,\ b\geq0\}.
\tag{MO46a}
$$

The product estimate and the open/closed half-line calculations give the upper inclusion. For the reverse inclusion first take $a<0$, $b>0$ and the linear test $h=au+bv$. The stalk $F_0$ is zero. In $\{h<0\}$ near the origin, the inequality $v\geq0$ already forces $u>0$, so the restricted sheaf is the constant sheaf on a nonempty convex closed half-region, extended from that closed region. Its derived sections are $k$ in degree zero, by convex acyclicity. The local support triangle then gives the nonzero test complex $k[-1]$. Thus every interior covector of the asserted cone occurs, and closedness supplies its boundary.

The conormal to $M$ consists of multiples of $du+dv$. It meets MO46a only at zero. Away from the origin, $M$ does not meet the closed support, so $M$ is noncharacteristic everywhere. Nevertheless $F|_M=0$, since $u+v=0$ cannot hold with $u>0$ and $v\geq0$. Its exceptional restriction is also zero by MO20. The estimated image at the origin is nonempty: on the tangent vector $(1,-1)$ it takes every value $a-b\leq0$. Thus both inverse-image estimates can be strict.

If $t=(u+v)/2$ and $y=(u-v)/2$, the same region is $t>0$, $-t<y\leq t$. Since

$$
a\,du+b\,dv=(a+b)\,dt+(a-b)\,dy,
$$

its cone in covector coordinates $(\tau,\eta)$ is

$$
\eta\leq-|\tau|.
\tag{MO46b}
$$

This cone meets the conormal to $t=0$ only at zero. Swapping $\eta$ and $\tau$ would incorrectly make that submanifold characteristic. The calculation derives the sign from the two boundary conditions rather than from a picture of the sector.

## SH02-MO-CUTOFF-STRICT-IMAGE — Why the two geometric cutoff images differ

Let $f:\mathbb R\to\mathrm{pt}$, $\varphi(s)=s$, $G=k_{(0,1]}$, and $t_0=-1$. All support sublevels are compact. Both endpoint microsupport cones are nonpositive multiples of $ds$, and interior covectors are zero. Therefore MO25+ holds everywhere. The triangle

$$
k_{(0,1]}\longrightarrow k_{[0,1]}\longrightarrow k_{\{0\}}\xrightarrow{+1}
$$

shows $R\Gamma(\mathbb R;G)=0$: the two right section complexes are $k$ and their restriction is the identity. The localized geometric image in MO27 is empty, because the support has no point with $s\leq-1$. The full geometric image is the zero cotangent fibre of the point, which is nonempty. Thus the inclusion between these two images cannot be replaced by equality.

For the exceptional case use $G=k_{[0,1)}$. Both endpoint cones are nonnegative multiples of $ds$, so MO25− holds everywhere. Compactly supported cohomology is zero by the corresponding triangle with the removed endpoint $1$. Again the localized image is empty and the full image is nonempty. These computations preserve the valid cutoff isomorphisms and microsupport bounds while separating them from a false stronger geometric equality.

## SH02-MO-PROBLEMS — Exercises with complete solutions

### SH02-MO-CONIC-NEIGHBORHOOD-TEST — A family of support tests must detect nearby directions

Let $E$ be a real vector space and $F\in D^b(k_E)$ be conic. For a nonempty convex conic open $U\subset E^*$ write

$$
U^\circ=\{x\in E:\langle x,\xi\rangle\geq0\text{ for every }\xi\in U\}.
$$

Prove the following neighborhood criterion and explain why a cofinal family consisting only of neighborhoods of the single direction $\xi_0$ is insufficient:

$$
(0,\xi_0)\notin\operatorname{SS}(F)
\quad\Longleftrightarrow\quad
\begin{gathered}
\text{there is a conic open neighborhood }W\text{ of }\xi_0\text{ such that}\\
R\Gamma_{U^\circ}(E;F)=0
\text{ for every nonempty convex conic open }U\subset W.
\end{gathered}
\tag{MO48}
$$

The cones $U$ in the right side may be centered on any direction in $W$; they need not contain $\xi_0$. Nonemptiness matters for the displayed polar convention: the vacuous polar of an empty set would be all of $E$ and would not satisfy the open-cone section formula below.

**Solution.** Put $H=T_EF$. The Fourier open-cone section formula gives

$$
R\Gamma(U;H)\simeq R\Gamma_{U^\circ}(E;F).
\tag{MO49}
$$

MO45 identifies the condition on the left of MO48 with $(\xi_0,0)\notin\operatorname{SS}(H)$. Zero covectors of microsupport record the closed support, so this means that $H$ vanishes on an ordinary neighborhood of $\xi_0$. Since $H$ is conic, saturating that neighborhood by positive scalars yields a conic open $W$ on which it still vanishes. MO49 proves the forward implication.

Conversely assume the right side. At any nonzero $\xi\in W$, small angular convex cones form a basis of neighborhoods of its radial orbit. Their sections compute the stalk: intersect a cone with a small annulus about $\xi$, apply conic restriction along the contractible radial parameter intervals, and then shrink the angular cap and the annulus. The groups in MO49 are zero for every such cone, so every cohomology stalk of $H$ at $\xi$ is zero. If $0\notin W$, this proves $H|_W=0$. If $0\in W$, conic openness forces $W=E^*$. We have already shown that $H$ is supported at zero. Taking $U=E^*$ in MO49 gives $R\Gamma(E^*;H)=0$, which for a complex supported at a point is its stalk complex. Thus the zero stalk also vanishes. In either case $\xi_0$ lies outside the closed support, proving MO48, including $\xi_0=0$.

Here is a counterexample to the weaker, single-direction formulation. Take $E=\mathbb R^2$, $F=k_{\mathbb R_{\geq0}\times\{0\}}$, $k\neq0$, and $\xi_0=(0,1)$ in dual coordinates $(u,v)$. The closed-convex vertex calculation gives

$$
\operatorname{SS}(F)_0=\{(u,v):u\geq0\},
$$

so $(0,\xi_0)$ belongs to microsupport. Nevertheless every convex conic open neighborhood $U$ of $\xi_0$ contains a covector with $u<0$. Hence $U^\circ$ meets the positive horizontal ray only at its endpoint. It follows that

$$
R\Gamma_{U^\circ}(E;F)=R\Gamma_{\{0\}}(E;F)=0.
$$

For the last equality, compute the endpoint costalk of the closed ray: the local support triangle compares the constant section on a short closed ray with the same section on the ray with its endpoint deleted. Both section complexes are $k$ and the map is the identity, so the supported complex is zero. Equivalently $T_EF=k_{\{u>0\}}$, whose sections on every convex cone crossing $u=0$ vanish, although it is nonzero arbitrarily close to $\xi_0$. Thus even vanishing on **every** convex conic neighborhood of that one direction does not replace the uniformly varying family required in MO48. This preserves the useful support-testing phenomenon while correcting the weaker formulation.

### SH02-MO-PROBLEM-ESCAPE — Information arriving from infinity

Let $C=\{(x,y):xy=1,\ x>0\}\subset\mathbb R^2$, let $F=k_C$, and let $q(x,y)=x$. Compute $Rq_*F$ and explain why MO8 does not apply.

**Solution.** The set $C$ is closed in $\mathbb R^2$ and $q|_C$ identifies it with $(0,\infty)$. Therefore $Rq_*F=Rj_*k_{(0,\infty)}\simeq k_{[0,\infty)}$; the stalk at $0$ is computed by ordinary cohomology of a contractible positive interval, with no higher cohomology. Its microsupport at $0$ consists of nonnegative multiples of $dx$. A tangent vector to $C$ at $(x,1/x)$ is $(1,-1/x^2)$. A covector $(\xi,0)$ conormal to $C$ must consequently have $\xi=0$. Thus $q_\pi q_d^{-1}\operatorname{SS}(F)$ contains only zero covectors over $x>0$, and no point over $0$. Properness on the support fails: the inverse image in $C$ of a compact interval containing $0$ has $y\to\infty$. This explicitly exhibits a boundary covector created by escape from every compact set.

### SH02-MO-PROBLEM-NO-CANCEL — What failure of transversality looks like

On the line take $A=\{(x,\xi):x>0,\ \xi\geq0\}\cup T_0^*\mathbb R$ and $B=A^a$. Explain why addition on $A\times_\mathbb RB$ is not proper and why ordinary cone sums need a hypothesis even when both summands are closed.

**Solution.** The term $T_0^*\mathbb R$ retains all finite limits at the base boundary $0$, so the displayed sets are closed in $T^*\mathbb R$. At any fixed $x>0$, the sequence $((x,n),(x,-n))$ has constant sum $(x,0)$ but no convergent subsequence. Hence addition is not proper. The failure is precisely a nonzero covector in $A\cap B^a=A$. This example disproves automatic properness; it does not itself show that every such sum is nonclosed. For an explicit nonclosed sum, take over base $x\geq0$ the rays $A_x=\mathbb R_{\geq0}(1,0)$ and $B_x=\mathbb R_{\geq0}(-1,x)$ in a trivial two-dimensional cotangent fibre, and empty fibres for $x<0$. Both total sets are closed. For $x>0$, $(0,1)=x^{-1}(1,0)+x^{-1}(-1,x)$ is in the sum, while at $x=0$ the sum is the horizontal line and omits $(0,1)$. Their sum is therefore not closed. This local trivial-bundle example embeds in $T^*\mathbb R^2$ by letting $x$ be the first base coordinate and making the construction independent of the second.

### SH02-MO-PROBLEM-MORSE — The two jumps of a circle

Let $k$ be a field, $F=k_{S^1}$ and let $\varphi$ be the vertical coordinate on the unit circle. Find the jump complexes and verify MO34.

**Solution.** Microsupport of the constant sheaf is the zero section, so the graph of $d\varphi$ meets it at the bottom and top points. At the minimum the set $\{\varphi\geq\varphi(x)\}$ contains a neighborhood and the jump is $k$. At the maximum that set is locally the single point; its costalk on the one-dimensional manifold is the orientation complex $k[-1]$. Thus $m_0=m_1=1$ and all other $m_j$ vanish. Ordinary cohomology of the circle has the same two Betti numbers, so every strong inequality is an equality and both Euler sums are zero. The compactness and finite-dimensionality hypotheses are all satisfied.

### SH02-MO-PROBLEM-LINEAR — Fourier transformation of a linear support

Let $L$ be a linear subspace of a finite-dimensional real vector space $E$, and use an orientation of $L$ to trivialize its orientation line. Verify MO45 for $k_L$.

**Solution.** Closed-image equality applied to $L\hookrightarrow E$ gives $\operatorname{SS}(k_L)=L\times L^\perp$. The Fourier kernel integrates a constant sheaf on a closed halfspace of $L$ when the dual vector does not annihilate $L$, giving zero compact cohomology, and on all of $L$ otherwise. Proper-support base change gives

$$
T_Ek_L\simeq k_{L^\perp}[-\dim L].
$$

Without the orientation choice its coefficient is the orientation line of $L$. The microsupport of this sheaf is $L^\perp\times L$, because the annihilator of $L^\perp$ is $L$ and a shift and an invertible line do not change support tests. MO38 carries $L\times L^\perp$ to $L^\perp\times(-L)=L^\perp\times L$, as required. Both extreme cases $L=0$ and $L=E$ are included.

## SH02-MO-RESEARCH — What these results make possible

The next microlocal operation estimates replace transversality by limiting cones, so their inputs should be compared with MO1 and MO19 rather than obtained by erasing an assumption. The Euler test MO41 is the entry point for conic microsupport calculations on deformation spaces. MO45 then turns specialization estimates into microlocalization estimates, including directions based on zero sections. The finite filtration in MO36 separates the sheaf-theoretic Morse argument from later questions about nondegenerate intersections, characteristic cycles and numerical indices.

The mathematical source comparison uses M. Kashiwara and P. Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), and Pierre Schapira, [*A short review on microlocal sheaf theory*, version dated 19 January 2016](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf). The Astérisque scan has three preliminary PDF pages before printed page 1; the review’s printed and PDF page numbers agree. These are the editions actually compared with the present proofs.

| Results here | Exact source passage | Mechanism and scope retained here |
|---|---|---|
| (MO1), (MO5)–(MO10), (MO19)–(MO22) | Astérisque, Propositions 4.1.1–4.1.2 and 4.2.1–4.2.2, pp. 61–65, and Proposition 5.3.2, pp. 83–84; review, Definition 2.7, Theorems 2.8–2.9 and 2.11, Corollary 2.12, pp. 10–13 | Compact-cap tests give the product estimate; open-rectangle adjunction and opposite directional supports give external Hom. Proper-support base change proves the proper-image bound. The graph and diagonal reductions preserve the actual noncharacteristic comparison and the two different no-cancellation hypotheses. |
| (MO2)–(MO4), the four boundary operations, (MO13)–(MO18) | Astérisque, proof of Proposition 4.2.2, pp. 64–65; Propositions 4.3.1–4.3.2 and Corollary 4.3.3, pp. 67–70; Theorem 5.2.1(iii), p. 81, and Proposition 5.3.2, pp. 83–84 | The proof here makes enlarged supports cofinal and uses open directional identities. Boundary-point vanishing and the microlocal support test then supply the transverse embedding comparison. None of these arguments requires arbitrary closed restriction to commute with a nonproper ordinary image. |
| (MO23) | Astérisque, Definition 5.6.1 and Proposition 5.6.2(ii), p. 98 | Perfect local cohomological data, with the pro- and ind-representability required by the biduality contract, supplies external dual–tensor evaluation. Pullback to the diagonal gives the displayed internal comparison. Constructibility is used at this step, not added to the earlier tensor and Hom estimates. |
| (MO24)–(MO30) | Astérisque, Theorem 4.4.1 and its proof, pp. 73–75 | The exhausting-family theorem supplies the source antecedent. The present proper-map reduction, two signs, separate endpoint proofs and compact limit of lifted covectors establish the more explicit four cutoff maps and the localized estimate. The half-open interval examples show why the two geometric images in (MO27) need not be equal. |
| (MO31)–(MO36) | Review, Lemma 3.5 and Theorem 3.6, pp. 16–17 | The source proves the ordinary one-sided Morse comparison, including its half-open level convention. The supported and compact-support versions, finite jump filtration, zero-jump case and rank cancellation proving the inequalities are given here. Field coefficients enter only the finite-dimensional inequalities. |
| (MO37)–(MO45), the Fourier support-test exercise (MO48)–(MO49) | Astérisque, Propositions 5.1.1–5.1.3 and Theorem 5.1.4, pp. 77–80 | Euler annihilation, radial cutoffs and the canonical symplectic exchange give the Fourier estimate. The added-variable kernel and inverse transform prove equality at both zero loci. The exercise uses that equality and the separately named Fourier open-cone formula; the requirement to test all nearby directions is kept explicit. |

The coefficient conventions also match at the relevant level: Astérisque §1.3, pp. 21–24, treats modules over a unital ring and imposes finite weak global dimension for tensor operations; the review, p. 6, uses a commutative ring of finite global dimension. This unit keeps its stated bounded complexes of arbitrary sheaves and arbitrary modules. It does not turn the finite-dimensional Morse argument or the perfect-data evaluation step into a restriction on the entire lesson.

The review states the external estimates and gives only a sketch of the inverse-image theorem; its proof explicitly refers elsewhere for one estimate. The local cone, boundary, graph and diagonal arguments above remain the proof route for that estimate here. Likewise, the named Fourier, propagation, microlocalization and exceptional-operation contracts retain their precise roles.

The finite complex-constructible equality in `SH02-MO-HOLOMORPHIC-IMPORT` remains a distinct external obligation, exactly as stated there; it is not needed for the real operation, cutoff or Fourier proofs. The worked strictness examples, the corrected sector coordinates, and the counterexample to testing only one conic direction are all retained.

Original AI expression in this lesson and its new comparison is CC0 1.0 Universal. The human results are credited to their authors above. The Astérisque volume retains the Société mathématique de France’s 1985 copyright and archive terms; neither that source nor the review is placed under CC0 by a programme citation.
