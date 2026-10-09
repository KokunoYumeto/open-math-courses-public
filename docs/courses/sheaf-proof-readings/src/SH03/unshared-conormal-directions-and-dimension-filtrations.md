# Unshared conormal directions and dimension filtrations

A μ-stratification controls how normal covectors approach a lower stratum. We will prove a more precise consequence: in each conormal fibre of a stratum, an open dense set of covectors avoids the conormal closures of all other strata. We will then organize the strata into a decreasing dimension filtration, checking its closedness, smooth layers, ordered μ-conditions and compatibility with a prescribed cover.

Let \(X\) be an \(n\)-dimensional real analytic manifold, Hausdorff and countable at infinity. All subanalyticity and local finiteness are in the ambient manifold. Strata are subanalytic analytic submanifolds of fixed dimension and may be disconnected. Write \(\pi:T^*X\to X\). Conic means invariant under positive cotangent dilations, including for sets that need not contain their zero limits.

We use the [full normal-cone theorem](boundary-forms-and-lagrangian-normal-cones.md#the-full-lagrangian-normal-cone-theorem), [generic conormality along a prescribed base](finite-conormal-closures-and-generic-base-directions.md#generic-conormality-along-any-subanalytic-base), the [weighted limiting-sum criterion](limiting-cotangent-sums-and-characteristic-inverse-images.md#the-product-bounds-in-the-definitions), and the [compatible μ-refinement construction](microlocal-stratifications-by-removing-bad-loci.md#closed-bad-set-induction). The local subanalytic set calculus supplies closures and Boolean operations, while the singular one-form rules preserve isotropy under subanalytic subsets, closure and locally finite unions. The [dimension argument](finite-conormal-closures-and-generic-base-directions.md#the-precise-dimension-prerequisite) supplies closure invariance and strict singular-dimension decrease. The proof below combines these results through three separate operations: constrain a full normal cone, eliminate its nonzero directions over a generic part of a fibre, and use local finiteness to pass from one conormal to all strata.

The classical cotangent framework is due to Kashiwara and Schapira. Their freely readable [*Microlocal Study of Sheaves*, Proposition 8.1.4 and Propositions 8.2.2–8.2.4, printed pp. 142–145](https://www.numdam.org/item/AST_1985__128__1_0/) relates Whitney limiting tangent spaces to conormal unions, proves stability of isotropy for conic subanalytic subsets, and uses a dimension filtration in an involutivity argument. Those statements explain the framework; they do not assert the fibrewise-avoidance theorem below or replace its full normal-cone and generic-base inputs. In particular, a Whitney condition alone must not be substituted for the stronger μ-hypothesis.

[David Trotman, *Une version microlocale de la condition (w) de Verdier*, §§1–2, printed 826–828](https://www.numdam.org/articles/10.5802/aif.1190/), gives the precise bridge: the Kashiwara–Schapira μ-condition for an approaching pair of strata is equivalent to Verdier’s condition. His proof normalizes the component of a conormal orthogonal to the other normal space and retains the product of base separation with covector size. This is why unbounded covectors in the limiting sum cannot be replaced by pointwise or bounded sums here. The linked refinement proof constructs a compatible μ-stratification.

*Original exposition by GPT-6.1 Sol (OpenAI), Ultra, September 2026; source reconstruction and bounded mathematical review by GPT-6 Astra (OpenAI), Ultra, October 2026. Original programme expression is public domain (CC0); human results retain their named credit.*

## Fibrewise avoidance of a conormal

Let \(M\subset X\) be an analytic submanifold and let \(A\subset T^*X\) be conic, subanalytic and isotropic. It may be nonclosed. Global subanalyticity of \(M\) is unnecessary: near any of its points, take an ambient chart in which \(M\) is closed analytic, and all the subanalytic arguments below take place in that chart. Put \(L=T_M^*X\), and assume

\[
A\cap L=\varnothing,\qquad
(A\widehat{+}L)\cap\pi^{-1}(M)\subset L.
\tag{1}
\]

**Fibrewise avoidance theorem.** For every \(x_0\in M\), the closed set

\[
\overline A\cap T_{x_0,M}^*X
\tag{2}
\]

is nowhere dense in the vector space \(T_{x_0,M}^*X\). The bar in (2) is part of the assertion: \(A\) itself misses the whole conormal by hypothesis, but its limits can meet it.

We prove the result in three steps, retaining the normal-cone sign and the unbounded covectors in the limiting operation.

## The normal-cone constraint

Take analytic coordinates \((u,z)\) near \(x_0\), with \(M=\{u=0\}\). If \(r=\operatorname{codim}M\), then \(u\in\mathbb R^r\) and \(z\in\mathbb R^{n-r}\). Write the associated cotangent coordinates as \((a,b)\), so that

\[
\alpha_X=a\,du+b\,dz,\qquad
L=\{u=0,b=0\}.
\tag{3}
\]

The manifold \(L\) has coordinates \((z,a)\). In its normal bundle inside \(T^*X\), use \((v,w)\) for the normal components of \(u\) and \(b\). The intrinsic normal identification is

\[
K:N_L(T^*X)\longrightarrow T^*L,
\qquad K(v,w)=w\,dz-v\,da.
\tag{4}
\]

Indeed, \(\omega_X=d\alpha_X=da\wedge du+db\wedge dz\). Pairing a representative \(v\partial_u+w\partial_b\) of the normal vector with a tangent vector to \(L\) under \(\omega_X\) gives the right side of (4). Its inverse is the normal identification induced by the quotient of \(-H\) established in the normal-cone lesson.

We claim that the second hypothesis in (1) gives

\[
C_L(A)\cap\{v=0\}\subset\{w=0\}.
\tag{5}
\]

To prove it, let a point of the left side have normal coordinate \((0,w)\) over \((z,a)\in L\). Its actual positive-deformation witnesses satisfy

\[
\begin{gathered}
(u_j,z_j;a_j,b_j)\in A,
\quad (u_j,z_j;a_j,b_j)\to(0,z;a,0),\\
t_j>0,\quad t_j\to0,\quad
u_j/t_j\to0,\quad b_j/t_j\to w.
\end{gathered}
\tag{6}
\]

By positive conicity, at the first base \((u_j,z_j)\) the covector \((a_j/t_j,b_j/t_j)\) still belongs to \(A\). At the second base \((0,z_j)\in M\), take the conormal covector \((-a_j/t_j,0)\in L\). Their sum tends to \((0,w)\), and the required position-covector product is

\[
|u_j|\,\frac{|(a_j,b_j)|}{t_j}
=\frac{|u_j|}{t_j}|(a_j,b_j)|\longrightarrow0.
\tag{7}
\]

The unscaled covectors converge and are bounded, even when their limit is zero. The scaled covectors can be unbounded, as allowed by the full \(\widehat{+}\) criterion. Thus \((0,z;0,w)\in A\widehat{+}L\). Hypothesis (1) forces its \(dz\) component to be zero, proving (5). No closedness of \(A\), properness of a projection, or noncharacteristic condition was used.

## Generic normal directions over a fixed fibre

The conormal \(L\) is an analytic conic Lagrangian. The full Lagrangian-normal-cone theorem therefore makes

\[
C=K\bigl(C_L(A)\bigr)\subset T^*L
\tag{8}
\]

a closed conic subanalytic isotropic set, where closedness is in the normal bundle and its identified cotangent bundle. For locally closed \(M\), work near the point in an open neighborhood where the normal construction is defined with a closed \(L\); its locality comparisons preserve the statement.

Let \(F=T_{x_0,M}^*X\), regarded as an analytic submanifold of the base manifold \(L\). In the coordinates above, \(F=\{z=z_0\}\), with free coordinate \(a\). Apply the generic-base theorem on \(L\) with prescribed base \(F\). It gives a relatively open dense subanalytic \(U\subset F\) such that

\[
C\cap\pi_L^{-1}(U)\subset T_F^*L.
\tag{9}
\]

The tangent to \(F\) is spanned by the \(a\)-directions, so (4) is conormal to \(F\) precisely when \(v=0\). By (5), it then also has \(w=0\). Consequently every fibre of \(C_L(A)\) over \(U\) is contained in the zero normal vector. A fibre may be empty; that also satisfies the conclusion.

## Zero normal directions imply actual avoidance

We need an elementary fact about normal cones. If \(P\) is an analytic submanifold of an analytic manifold \(Q\), and

\[
C_P(B)|_p\subset\{0\}\quad\text{for a point }p\in P,
\tag{10}
\]

then \(p\notin\overline{B\setminus P}\).

**Proof.** If points of \(B\setminus P\) approached \(p\), take adapted coordinates \((h,e)\), where \(P=\{e=0\}\). Along such a sequence \((h_j,e_j)\), each \(e_j\ne0\) and \(e_j\to0\). Set \(t_j=|e_j|>0\). After taking a subsequence, compactness of the unit sphere gives

\[
e_j/t_j\longrightarrow e_\infty,
\qquad |e_\infty|=1.
\tag{11}
\]

The base coordinates tend to \(p\) and \(t_j\to0\). This is an actual positive normal-cone witness for the nonzero vector \(e_\infty\), contradicting (10). \(\square\)

Apply this fact with \(P=L\), \(Q=T^*X\), \(B=A\), at each \(p\in U\). We obtain a neighborhood of \(p\) on which \(A\) is contained in \(L\). The first hypothesis in (1) makes \(A\) empty on that neighborhood. Hence

\[
U\cap\overline A=\varnothing.
\tag{12}
\]

Since \(U\) is open dense in \(F\), the closed subset (2) is nowhere dense, proving the theorem. If \(M\) has codimension zero, \(F\) is a single zero covector; its only open dense subset is itself, so (2) is empty. This case has not been discarded by removing the zero section.

## A covector that belongs only to one stratum

Let \(\mathcal S=(S_a)\) be a μ-stratification of \(X\). For each stratum,

\[
\pi\left(
T_{S_a}^*X\setminus\bigcup_{b\ne a}\overline{T_{S_b}^*X}
\right)=S_a.
\tag{13}
\]

In fact the covectors retained by this difference form an open dense subset of each conormal fibre.

**Proof.** Fix \(a\), and use the fibrewise avoidance theorem with \(M=S_a\) and

\[
A=\bigcup_{b\ne a}T_{S_b}^*X.
\tag{14}
\]

This locally finite union is conic subanalytic isotropic, and its base is disjoint from \(S_a\). Thus \(A\cap T_{S_a}^*X=\varnothing\).

For the limiting-sum hypothesis, take any full \(\widehat{+}\) witness with output base \(x\in S_a\). Near \(x\) only finitely many first-base strata occur, so a subsequence of the witness has a fixed first stratum \(S_b\), \(b\ne a\). Its approach to \(x\) and the frontier rule imply \(S_a\subset\overline{S_b}\setminus S_b\). The ordered μ-condition for \((S_b,S_a)\) sends that limiting output into \(T_{S_a}^*X\). This checks the full operation, including unbounded cancelling covectors.

The theorem shows that \(\overline A\) is nowhere dense in each fibre of \(T_{S_a}^*X\). By local finiteness,

\[
\overline A=\bigcup_{b\ne a}\overline{T_{S_b}^*X}.
\tag{15}
\]

One inclusion is immediate. For the other, a neighborhood of a limit point meets only finitely many conormal pieces, and a finite union commutes with closure. Every conormal fibre is nonempty; its open dense complement to (15) therefore supplies a covector over each point of \(S_a\). All such covectors have base in \(S_a\), giving both inclusions in (13). \(\square\)

For a positive-codimension stratum, a nonzero covector can be chosen: an open dense subset of a positive-dimensional vector space cannot consist only of its origin. For an open stratum, the fibre consists only of zero, and zero itself is its unshared covector.

## Decreasing filtrations and the order of a pair

A **decreasing filtration** of a topological space \(X\) is a sequence of closed subsets \((F_j)_{j\in\mathbb Z}\) such that

\[
F_{j+1}\subset F_j,\qquad
F_j=X\ (j\ll0),\qquad F_j=\varnothing\ (j\gg0).
\tag{16}
\]

It is subanalytic when each \(F_j\) is subanalytic and each layer

\[
H_j=F_j\setminus F_{j+1}
\tag{17}
\]

is an analytic submanifold. Empty layers are allowed.

We distinguish two index conventions explicitly. Call a filtration an **ordered μ-filtration** if it asks for the μ-condition on \((H_j,H_k)\) when \(j>k\). The direction of this indexing has a direct consequence. For any decreasing closed filtration and \(j>k\),

\[
\overline{H_j}\subset F_j\subset F_{k+1},
\qquad H_k\cap F_{k+1}=\varnothing.
\tag{18}
\]

Every limiting sum has base in the closures of both input bases. Therefore

\[
(T_{H_j}^*X\widehat{+}T_{H_k}^*X)
\cap\pi^{-1}(H_k)=\varnothing
\quad (j>k).
\tag{19}
\]

In this direction the condition is automatic. The dimension construction below additionally proves the approaching-direction condition on \((H_j,H_k)\) for \(j<k\). We keep both orders explicit, since the latter supplies the conormal control of a higher-dimensional layer approaching a lower one.

## Building the dimension filtration

**Filtration theorem.** Let \((E_i)\) be a locally finite cover of \(X\) by closed subanalytic subsets. There is a decreasing subanalytic filtration whose layer components lie in cover members and which satisfies both the order in (19) and

\[
(T_{H_j}^*X\widehat{+}T_{H_k}^*X)
\cap\pi^{-1}(H_k)\subset T_{H_k}^*X
\quad (j<k).
\tag{20}
\]

**Proof.** Use the μ-refinement theorem to obtain a μ-stratification \((S_a)\) compatible with the cover. Set

\[
F_j=\bigcup_{\dim S_a\le-j}S_a.
\tag{21}
\]

First establish the strict dimension of a smooth frontier. A locally closed subanalytic analytic submanifold \(S\) is open in \(\overline S\). Thus \(\overline S\setminus S\) is closed and nowhere dense in \(\overline S\). The closed nowhere-dense dimension argument in the μ-refinement lesson gives

\[
\dim(\overline S\setminus S)<\dim\overline S=\dim S.
\tag{22}
\]

Consequently a distinct stratum in the closure of \(S_a\) has smaller dimension.

Now take a convergent sequence in \(F_j\). Local finiteness allows a subsequence in a fixed eligible \(S_a\). If its limit belongs to \(S_b\), the frontier rule and (22) give \(\dim S_b\le\dim S_a\le-j\). The limit belongs to \(F_j\), so \(F_j\) is closed. It is subanalytic by local finiteness. The sequence is decreasing, and its endpoints obey

\[
F_j=X\quad(j\le-n),\qquad
F_j=\varnothing\quad(j\ge1).
\tag{23}
\]

The layer \(H_j\) is the union of the dimension-\(-j\) strata. Near a point of one such stratum \(S_b\), no other stratum of that dimension can accumulate: the frontier rule would contradict (22). There are only finitely many such strata locally. Shrink the neighborhood to exclude their closures. On it, \(H_j\) coincides with \(S_b\). This proves that \(H_j\) is an analytic submanifold, with the same local tangent and conormal as \(S_b\).

To prove (20), let the target base be \(x\in H_k\). Near \(x\), \(H_k\) coincides with one stratum \(S_b\). A full limiting witness from \(H_j\) can be reduced to a fixed first stratum \(S_a\) by local finiteness. Since \(j<k\), it has larger dimension and is distinct from \(S_b\). Its approach to \(x\) gives \(S_b\subset\overline{S_a}\setminus S_a\). The original μ-condition sends the limiting output into \(T_{S_b}^*X=T_{H_k}^*X|_x\). This proves (20); the other order was already proved in (19).

Finally, each dimension-\(-j\) stratum is open and closed in \(H_j\), since all the other strata in that layer are also open. A connected component of \(H_j\) lies in one such stratum and hence in a member of the prescribed cover. This proves every assertion. \(\square\)

The layers can have infinitely many global components. The finite interval of indices in (23) depends on dimension and does not assert a finite global stratification.

## Exercises with complete solutions

### Normal coordinates over a line conormal

*Difficulty: Introductory.*

Let \(X=\mathbb R^2\) with coordinates \((u,z)\), and \(M=\{u=0\}\). Use \((a,b)\) for cotangent coordinates. Compute \(K\) on the normal bundle of \(L=T_M^*X\), then compute the conormal in \(L\) to the fixed fibre \(F=\{z=z_0\}\). Which normal component must vanish for membership in that conormal?

**Solution.** The conormal is \(L=\{u=0,b=0\}\) with coordinates \((z,a)\). Write the normal representative as \(v\partial_u+w\partial_b\). For a tangent vector \(\delta z\partial_z+\delta a\partial_a\),

\[
\omega_X(v\partial_u+w\partial_b,
\delta z\partial_z+\delta a\partial_a)
=w\delta z-v\delta a.
\tag{24}
\]

Hence \(K(v,w)=w\,dz-v\,da\). The tangent to \(F\) is spanned by \(\partial_a\). Its annihilator in \(T^*L\) consists of multiples of \(dz\), so \(K(v,w)\in T_F^*L\) precisely when \(v=0\). The remaining component \(w\) is removed by the separate limiting-sum constraint (5); generic conormality alone does not remove it.

### Having a zero normal is insufficient

*Difficulty: Intermediate.*

In \(Q=\mathbb R^2\), let \(P=\{e=0\}\) and \(B=\{(h,e):e=h^2,\ h\ne0\}\). At the origin, show that \(C_P(B)\) contains a zero normal and a nonzero normal. Explain which exact hypothesis in (10) supplies avoidance.

**Solution.** Take \(h_j\to0\) nonzero and \(e_j=h_j^2\). With positive deformation parameter \(t_j=|h_j|\), the ratio \(e_j/t_j=|h_j|\) tends to zero, giving a zero normal over the origin. With \(t_j=h_j^2\), the ratio is one, giving a nonzero normal. The set \(B\setminus P=B\) approaches the origin, as both sequences show.

Condition (10) requires every normal in that fibre to be zero, rather than the existence of a zero normal. Normalizing the actual nonzero displacement by its norm detects a nonzero limit and is the compactness step that rules out approach. The first sequence alone would give no avoidance conclusion.

### Unshared directions in a crossing

*Difficulty: Intermediate.*

Stratify \(\mathbb R^2\) into its four open quadrants, four open half-axes and the origin. For covectors \(a\,dx+b\,dy\), determine the unshared covectors in (13) over the origin, a point on the positive horizontal half-axis, and a point in an open quadrant. Verify that this is a μ-stratification.

**Solution.** Every incident pair with an open quadrant first satisfies μ because its conormal is zero. Every incident pair with the origin second satisfies μ because its conormal is the full cotangent fibre. These are all distinct incidences besides the half-axes approaching the origin, which are included in the second case. The ordinary frontier rule holds for the usual quadrant boundaries, so this is a μ-stratification.

At the origin, the closures of the horizontal half-axis conormals give the line \(a=0\), and those of the vertical half-axis conormals give the line \(b=0\). The quadrant conormals add only the zero covector, already in both lines. Thus the unshared part of the full point conormal is

\[
\{(a,b):a\ne0,\ b\ne0\}.
\tag{25}
\]

At a point on the positive horizontal half-axis, its conormal is \(\mathbb R\,dy\). Only the adjacent quadrant conormal closures meet that base, and they contribute zero. The unshared part is \(\{b\,dy:b\ne0\}\). At a point in a quadrant, no other stratum closure reaches the point. The sole conormal covector, zero, is therefore unshared. All three answers are open dense in their respective fibres.

### Isotropy is needed for fibrewise avoidance

*Difficulty: Advanced.*

In the coordinates of (3), with \(X=\mathbb R^2\), put \(M=\{u=0\}\) and \(A=\{u>0,b=0\}\). Show that \(A\) is conic and subanalytic, misses \(T_M^*X\), and satisfies the limiting-sum hypothesis in (1). Compute its conormal limits and identify the failed hypothesis of the theorem.

**Solution.** The inequality and equality defining \(A\) are semianalytic. Positive covector dilation preserves \(b=0\), so \(A\) is conic. Its base has \(u>0\), which is disjoint from \(M\).

Both an input covector of \(A\) and a covector of \(T_M^*X\) have zero \(dz\) component. Every convergent sum of such covectors still has that component zero. Thus every limiting-sum output over \(M\) is in \(T_M^*X\), regardless of whether individual \(du\) components are bounded. However,

\[
\overline A=\{u\ge0,b=0\},\qquad
\overline A\cap T_M^*X=T_M^*X.
\tag{26}
\]

The intersection is the whole fibre at every base point, so it is not nowhere dense. The missing hypothesis is isotropy: on this smooth three-dimensional \(A\), \(\alpha_X=a\,du\) does not vanish, for example on \(\partial_u\) at \(a=1\). The isotropic normal-cone and generic-base step cannot be applied to it.

### The two orders are different conditions

*Difficulty: Advanced.*

For \(F=\{x^3=y^3z\}\subset\mathbb R^3\) and \(N=\{x=y=0\}\), define \(F_{-3}=\mathbb R^3\), \(F_{-2}=F\), \(F_{-1}=N\), \(F_0=\varnothing\), extending by whole and empty sets at the two ends. Prove this is a subanalytic filtration satisfying the ordered condition for \(j>k\). Show that the condition for \(j<k\) fails for its surface and line layers.

**Solution.** The filtration sets are closed semianalytic. Its nonempty layers are \(O=\mathbb R^3\setminus F\), \(M=F\setminus N\), and \(N\). The first is open, the last is a line. The middle has the analytic embedding \((s,t)\mapsto(st,s,t^3)\), \(s\ne0\), with independent tangent vectors \((t,1,0)\), \((s,0,3t^2)\), so it is smooth. The conditions for \(j>k\) follow from (18)–(19): the closure of a later layer cannot meet an earlier layer's base.

For the approaching direction, take \(j=-2\), \(k=-1\), so the pair is \((M,N)\). At \((0,s,0)\in M\), \(s\ne0\), the covector \(dz\) annihilates both tangent vectors. Let \(s\to0\); take the second base to be the origin in \(N\) and its covector to be zero. The sum remains \(dz\), and the mismatch product is \(|s|\to0\). Yet \(dz\) does not annihilate the tangent \(\partial_z\) to \(N\). Thus the \(j<k\) condition fails. The additional property (20) in the constructed filtration carries information beyond the separated-base order (19).

### The axes filtration respects a closed quadrant cover

*Difficulty: Intermediate.*

Use the four closed quadrants as a cover of \(\mathbb R^2\), and the nine-stratum μ-stratification in the crossing exercise. Compute (21), its layers and their connected components. Verify compatibility with the cover.

**Solution.** The filtration is

\[
F_{-2}=\mathbb R^2,\qquad
F_{-1}=\{xy=0\},\qquad
F_0=\{0\},\qquad F_1=\varnothing,
\tag{27}
\]

with whole sets for earlier indices and empty sets for later ones. These are closed semianalytic sets. The dimension-two layer has the four open quadrants as components. The dimension-one layer is the axes with the origin removed and has the four half-axes as components. The dimension-zero layer is the origin. Their components lie respectively in a closed quadrant, in either adjacent closed quadrant, and in all four closed quadrants. The preceding μ calculation proves (20); (19) follows from closedness. The dimension-one layer is smooth because its two axes no longer meet in that layer.

### Infinitely many components with finite filtration endpoints

*Difficulty: Introductory.*

Cover \(\mathbb R\) by the closed intervals \([m,m+1]\), \(m\in\mathbb Z\). Give a compatible filtration and determine every layer component. Explain why connected components of a layer cannot join distinct strata of the same dimension in the general construction.

**Solution.** Use the μ-stratification by integer points and the open intervals between them. Its filtration has

\[
F_{-1}=\mathbb R,\qquad F_0=\mathbb Z,\qquad F_1=\varnothing.
\tag{28}
\]

The set of integers is closed and subanalytic, since a bounded neighborhood contains only finitely many integers; it is a zero-dimensional analytic submanifold. The layer components are the intervals \((m,m+1)\), each contained in \([m,m+1]\), and the singleton integers, each contained in an adjacent closed interval. There are infinitely many global components and only two nonempty layer indices.

In the general construction, each stratum in a fixed-dimensional layer is open there. Its complement, the union of the other same-dimensional strata, is also open, so the stratum is closed in that layer. A connected subset meeting it and its complement would be split into two nonempty relatively open subsets. A layer component must therefore stay in a single stratum. This is the component-containment argument used in the theorem.

## Passing from strata to functions

The unshared-direction theorem separates each stratum from conormal limits of the others. The filtration theorem keeps the same approaching-direction control while collecting strata of equal dimension into smooth layers. We next choose squared-distance functions whose differential graphs avoid lower-dimensional singular cotangent pieces and meet the smooth pieces transversely.
