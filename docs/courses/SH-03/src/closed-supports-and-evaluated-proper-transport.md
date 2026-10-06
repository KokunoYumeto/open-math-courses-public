# Closed supports and evaluated proper transport

The characteristic class follows an identity through exceptional restriction, ordinary restriction and evaluation. To transport the class, we need the comparisons between these maps, not just isomorphisms between their objects. Closed embeddings let us test the comparisons by a fully faithful direct image. Proper-support base change and the two adjunctions then reduce them to units, counits and their triangular identities.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 1 October 2026. Author self-check recorded; not independently reviewed. New original text is public domain (CC0).*

This lesson treats the identity square of the characteristic class under proper transport, together with its graph diagram and the supporting lemmas. Use Constructible traces and local Euler indices for the characteristic-class chain, graded contraction and closed-embedding comparison. We use the normalized exceptional and ordinary adjunctions, proper-support composition and base change, internal adjunction and compatibility with forgetting support in their bounded forms, with their evaluated maps. The full middle graph comparison, the proper characteristic-class theorem and the compact index formula are proved in Proper characteristic classes and the compact index.

## Name both adjunctions before composing their maps

We work over a commutative characteristic-zero field $k$. For the two closed-support lemmas, spaces are locally compact Hausdorff with finite integral compact-support cohomological dimension, as required by the standing exceptional-operation contract. Inputs $G$ are bounded. The internal-Hom evaluation calculation has $G\in D^b(k_Y)$ and $F\in D^+(k_X)$; it includes the source's bounded $F$ case. These domains keep every displayed operation in the constructed bounded-below category.

For a map $f:Y\to X$, abbreviate

\[
 L_f=Rf_!,\qquad S_f=Rf_*.
\]

The natural transformation $\pi_f:L_f\to S_f$ forgets proper support. Write the adjunction maps as follows:

| Adjunction | Unit | Counit |
|---|---|---|
| $L_f\dashv f^!$ | $u_G:G\to f^!L_fG$ | $t_A:L_ff^!A\to A$ |
| $f^{-1}\dashv S_f$ | $a_A:A\to S_ff^{-1}A$ | $b_G:f^{-1}S_fG\to G$ |

The exceptional unit starts at an object on $Y$. The ordinary unit starts at an object on $X$. In particular, $G\to f^{-1}S_fG$ is not the ordinary unit. The ordinary map with these two terms is the **counit in the opposite direction**, $b_G$.

Their triangular identities include

\[
 t_{L_fG}\,L_fu_G=\mathrm{id}_{L_fG},\qquad
 S_fb_G\,a_{S_fG}=\mathrm{id}_{S_fG}.
 \qquad\text{(1)}
\]

We use composition right to left. Units, counits and comparison maps have degree zero. The tensor comparisons later in the lesson retain the graded symmetry of the preceding lesson.

For a closed embedding $i$, $L_i=S_i=i_*$ and $i^{-1}i_*\simeq\mathrm{id}$. Its comparison is

\[
 \beta_{i,A}:i^!A\longrightarrow i^{-1}A,
 \qquad
 i_*\beta_{i,A}=a_{i,A}\,t_{i,A}.
 \qquad\text{(2)}
\]

The second formula is the pushforward form of ordinary restriction of the exceptional counit. Since $i_*$ is fully faithful, it determines $\beta$ uniquely and allows equality to be checked after applying $i_*$.

## A composite closed embedding keeps the ordinary counit

Let

\[
 Z\xrightarrow{g}Y\xrightarrow{f}X,\qquad h=fg,
\]

and assume that both $g$ and $h$ are closed embeddings. The map $f$ need not be proper. For $G\in D^b(k_Y)$, set $M=L_fG$. Exceptional composition identifies $g^!f^!M$ with $h^!M$, and ordinary inverse composition identifies $g^{-1}f^{-1}S_fG$ with $h^{-1}S_fG$.

**Composite comparison.** The following path equals $\beta_{g,G}$:

\[
 \begin{aligned}
 g^!G&\xrightarrow{g^!u_G}h^!M
 \xrightarrow{\beta_{h,M}}h^{-1}M\\
 &\xrightarrow{h^{-1}\pi_{f,G}}h^{-1}S_fG
 \xrightarrow{g^{-1}b_G}g^{-1}G.
 \end{aligned}
 \qquad\text{(3)}
\]

The last arrow is upward on the right side of the source's diagram (9.1.9). It comes from the ordinary counit, whereas the first arrow comes from the exceptional unit.

**Proof.** Apply the fully faithful $h_*$. Put $C=g^!G$. Proper composition gives

\[
 h_*C=L_fg_*C\simeq S_fg_*C.
 \qquad\text{(4)}
\]

Here the identification is canonical: $g$ and $h$ are proper closed embeddings, and $\pi$ respects composition. In particular $f$ is proper on the closed image $g(Z)$ because there it is identified with the proper map $h$. No properness on all of $Y$ follows from (4).

First compare the exceptional part of (3). The counit for $h=fg$ is the counit for $g$ followed by that for $f$. Naturality of $t_g$, followed by the first triangular identity in (1), gives

\[
 t_{h,M}\,h_*(g^!u_G)=L_f t_{g,G}.
 \qquad\text{(5)}
\]

To spell out the cancellation, its left side is

\[
 L_fg_*g^!G\longrightarrow
 L_fg_*g^!f^!M\longrightarrow L_ff^!M\longrightarrow M.
\]

Move $u_G$ past the middle counit by naturality. The resulting last two maps are $L_fu_G$ and $t_{f,M}$, whose composite is the identity on $M=L_fG$. The remaining map is $L_ft_{g,G}$, as claimed.

Use (2) for $h$ and naturality of the ordinary unit to push forward the whole path (3). Equation (5) reduces it to

\[
 h_*g^{-1}b_G\,a_{h,S_fG}\,pi_{f,G}\,L_ft_{g,G}.
 \qquad\text{(6)}
\]

For ordinary inverse/direct composition, the unit for $h=fg$ is

\[
 a_{h,A}=S_fa_{g,f^{-1}A}\,a_{f,A}.
\]

At $A=S_fG$, naturality of $a_g$ with respect to $b_G$ and the second identity in (1) give

\[
 h_*g^{-1}b_G\,a_{h,S_fG}=S_fa_{g,G}.
 \qquad\text{(7)}
\]

Indeed moving $b_G$ past $a_g$ leaves $S_fb_G\,a_{f,S_fG}$, which is the identity. Notice that the unit in this cancellation has input $S_fG$ on $X$.

Finally naturality of support forgetting gives

\[
 \pi_{f,G}\,L_ft_{g,G}
 =S_ft_{g,G}\,\pi_{f,g_*C}.
\]

Substitute this and (7) in (6). The result is

\[
 S_f(a_{g,G}t_{g,G})\,\pi_{f,g_*C}
 =S_f(g_*\beta_{g,G})\,\pi_{f,g_*C}.
\]

Under (4) this is exactly $h_*\beta_{g,G}$. Full faithfulness of $h_*$ proves (3). The argument uses both triangular identities and the actual support-forgetting comparison; it does not infer equality merely from equal source and target objects. $\square$

## A cartesian closed restriction compares before support is forgotten

Consider a cartesian square with horizontal closed embeddings:

\[
 \begin{array}{ccc}
 Y'&\xrightarrow{g'}&Y\\
 f'\downarrow&&\downarrow f\\
 X'&\xrightarrow{g}&X.
 \end{array}
 \qquad\text{(8)}
\]

It suffices to assume $g$ closed, since $g'$ is its base change. The finite cohomological-dimension assumptions make the exceptional functors available; closed direct image itself has dimension zero. Proper-support base change gives

\[
 B:g^{-1}L_f\xrightarrow{\sim}L_{f'}g'^{-1}.
 \qquad\text{(9)}
\]

Both horizontal maps are proper, so proper composition also gives

\[
 K:L_fg'_*=g_*L_{f'}.
 \qquad\text{(10)}
\]

Here and below equality in (10) denotes the normalized composition isomorphism. This uses $fg'=gf'$ and closed horizontal maps; it makes no properness assumption on either vertical map.

Define the exceptional exchange

\[
 c_G:L_{f'}g'^!G\longrightarrow g^!L_fG
 \qquad\text{(11)}
\]

as the transpose along $g_*\dashv g^!$ of

\[
 g_*L_{f'}g'^!G
 \xrightarrow{K^{-1}}L_fg'_*g'^!G
 \xrightarrow{L_ft_{g',G}}L_fG.
 \qquad\text{(12)}
\]

This is a morphism. It is not declared an isomorphism for an arbitrary square.

**Closed cartesian comparison.** Before forgetting vertical proper support, there is the equality

\[
 \beta_{g,L_fG}\,c_G
 =B_G^{-1}\,L_{f'}\beta_{g',G}
 :L_{f'}g'^!G\longrightarrow g^{-1}L_fG.
 \qquad\text{(13)}
\]

Postcomposing with $g^{-1}\pi_{f,G}$ gives precisely the supported-to-ordinary comparison of Lemma 9.1.5. Its right path is

\[
 L_{f'}g'^{-1}G\xrightarrow{B_G^{-1}}g^{-1}L_fG
 \xrightarrow{g^{-1}\pi_{f,G}}g^{-1}S_fG.
 \qquad\text{(14)}
\]

Thus (14) does not require an inverse of ordinary base change. Ordinary base change is generally only a morphism.

**Proof.** We first need the compatibility of the proper comparison $B$ with the closed ordinary unit:

\[
 g_*B_G\,a_{g,L_fG}
 =K_{g'^{-1}G}\,L_fa_{g',G}.
 \qquad\text{(15)}
\]

This identity is an equality of maps from $L_fG$ to $g_*L_{f'}g'^{-1}G$. To verify it, transpose both maps along $g^{-1}\dashv g_*$. The left transpose is $B_G$. For the right, the proper-composition map $K$ has transpose $B$ followed by the ordinary counit $g'^{-1}g'_*$; this is the normalized mixed-exchange/proper-composition identity for closed $g,g'$. The remaining pullback of $a_{g',G}$ cancels with that counit by the ordinary triangular identity. Its transpose is again $B_G$. This proves (15) by the adjunction bijection. The stated transpose identity follows from proper-support base change on supported sections and proper composition: both evaluate the same section at its pulled-back germ. It is part of the current support-forgetting compatibility, before any vertical support is forgotten.

Apply the faithful $g_*$ to (13), and put $M=L_fG$. By (2) and the definition (12), the pushed-forward left path is

\[
 a_{g,M}\,L_ft_{g',G}\,K_{g'^!G}^{-1}.
 \qquad\text{(16)}
\]

For the right path, use naturality of $K$ to move $L_{f'}\beta_{g',G}$ across it. Equation (2) for $g'$ gives $g'_*\beta_{g',G}=a_{g',G}t_{g',G}$. Hence the right path is

\[
 \begin{aligned}
 &(g_*B_G^{-1})\,K_{g'^{-1}G}\,
       L_f(a_{g',G}t_{g',G})\,K_{g'^!G}^{-1}\\
 &\qquad=a_{g,M}\,L_ft_{g',G}\,K_{g'^!G}^{-1},
 \end{aligned}
\]

where (15) supplies the last equality. This is (16). Full faithfulness proves (13), and postcomposition gives the source comparison to $g^{-1}S_fG$. Every comparison retains the same units, counits and properly supported sections. $\square$

## The evaluated proper-Hom map has a prescribed tensor order

Let $G\in D^b(k_Y)$ and $F\in D^+(k_X)$, and put

\[
 H=R\mathcal Hom_Y(G,f^!F).
\]

Boundedness of the first Hom input makes $H$ bounded below. The finite dimension bound makes $L_fG$ bounded, so the corresponding Hom on $X$ is bounded below too. The current internal exceptional adjunction is the actual isomorphism

\[
 v:S_fH\xrightarrow{\sim}R\mathcal Hom_X(L_fG,F).
 \qquad\text{(17)}
\]

Its definition, including its tensor order, is the curry of the pairing

\[
 \begin{aligned}
 L_fG\otimes^LS_fH
 &\xrightarrow{\sim}L_f(G\otimes^Lf^{-1}S_fH)\\
 &\xrightarrow{L_f(1\otimes b_H)}L_f(G\otimes^LH)\\
 &\xrightarrow{L_f\mathrm{ev}}L_ff^!F
 \xrightarrow{t_F}F.
 \end{aligned}
 \qquad\text{(18)}
\]

The first map is the inverse projection-formula comparison. The second uses the ordinary counit; it is not generally invertible. The evaluation $G\otimes H\to f^!F$ includes the graded symmetry placing the Hom factor before its argument.

**Evaluation compatibility.** Evaluating $1\otimes v$ gives the same pairing as (18). This is Lemma 9.1.6, including the map from $L_fG\otimes S_fH$ toward $L_f(G\otimes H)$.

**Proof.** Tensor–Hom adjunction identifies maps from $S_fH$ into $R\mathcal Hom(L_fG,F)$ with maps from $L_fG\otimes S_fH$ to $F$, after its specified graded symmetry. By definition, (17) corresponds under this bijection to (18). Evaluating its curry returns (18) by the tensor–Hom triangular identity. Invertibility of (17) is the existing internal-adjunction theorem; it is proved with the same evaluated map on bounded/soft and injective resolutions. Therefore using (17) here has not replaced its map by an arbitrary isomorphism. All arrows remain in $D^+$ because $G$ is bounded and the coefficient field has finite global dimension. $\square$

This proof supplies the arrows omitted in the source's brief supporting proof. It does not extend the whole formula to an unrestricted bounded-below first input $G$: its internal Hom could then become unbounded below, beyond the proper-direct-image construction being reused.

## The transported identity follows from the exceptional triangle

Now suppose $X,Y$ are real analytic manifolds and $G\in D^b_{\mathbb R\text{-c}}(k_Y)$. Assume $f$ is proper on the closed support of $G$. Then

\[
 P=L_fG\simeq S_fG
\]

is bounded constructible by the proper perfect-image theorem. The unit $u_G:G\to f^!P$ induces

\[
 R\mathcal Hom(G,G)\longrightarrow R\mathcal Hom(G,f^!P).
\]

Apply $S_f$, then (17) with $F=P$, to obtain the endomorphism comparison. The identity path is

\[
 k_X\xrightarrow{a_{k_X}}S_fk_Y
 \xrightarrow{S_fe_G}S_fR\mathcal Hom(G,G)
 \longrightarrow R\mathcal Hom(P,P).
 \qquad\text{(19)}
\]

**Identity square.** Formula (19) is the identity unit $e_P$.

**Proof.** The first two arrows send the global unit to the identity of $G$. Postcomposition with $u_G$ sends it to $u_G$. Internal adjunction carries this morphism to $t_P L_fu_G:P\to P$. Equation (1) says this is $\mathrm{id}_P$, which proves (19) by internal-Hom adjunction. The same argument works on every open subset of $X$, where the normalized functors and maps restrict to their counterparts. Thus it identifies the sheaf morphism, not just a numerical trace. $\square$

The top term here is $S_fk_Y$. Support properness for $G$ does not change it to $L_fk_Y$: the constant sheaf may have support all of $Y$, where $f$ need not be proper.

## The two closed comparisons occur in one graph factorization

For any analytic $f:Y\to X$, define

\[
 \begin{aligned}
 f_1:Y\times Y&\longrightarrow X\times Y,&(y_1,y_2)&\longmapsto(f(y_1),y_2),\\
 f_2:X\times Y&\longrightarrow X\times X,&(x,y)&\longmapsto(x,f(y)),\\
 \gamma:Y&\longrightarrow X\times Y,&y&\longmapsto(f(y),y).
 \end{aligned}
 \qquad\text{(20)}
\]

The original diagonal $\delta_Y$ and the graph satisfy $f_1\delta_Y=\gamma$. Both are closed embeddings because the manifolds are Hausdorff. Thus (3) applies to $g=\delta_Y$, $f=f_1$ and $h=\gamma$.

The graph also gives the cartesian square

\[
 \begin{array}{ccc}
 Y&\xrightarrow{\gamma}&X\times Y\\
 f\downarrow&&\downarrow f_2\\
 X&\xrightarrow{\delta_X}&X\times X.
 \end{array}
 \qquad\text{(21)}
\]

Indeed the fibre-product condition for $(x,y)$ and $z\in X$ is $(x,f(y))=(z,z)$. It forces $x=z=f(y)$, leaving exactly $y$. This identifies the fibre product with $Y$ and its maps with $\gamma,f$. The closed cartesian comparison (13)–(14) applies to this square. Neither application assumes that $f,f_1$ or $f_2$ is globally proper.

These are the two geometric placements of the closed-support lemmas in the middle of the source's proper trace diagram. Applying them to the actual external-Hom object, retaining product evaluation and proper duality, is still needed to finish that middle comparison.

## Exercises with complete solutions

### Identify the adjunction from the domain of its unit

*Difficulty: Introductory.*

An attempted proof writes an “ordinary unit” $G\to f^{-1}S_fG$ and uses it on the right side of (3). Correct the proof and list the two triangular identities it needs. For a map from two discrete points to a point, describe the ordinary unit and counit explicitly. Does a special map between the wrongly ordered terms change which adjunction supplies the unit?

**Solution.** The ordinary adjunction is $f^{-1}\dashv S_f$. Its unit has an object $A$ on the target as input, $A\to S_ff^{-1}A$, and its counit is $f^{-1}S_fG\to G$. Thus the last arrow of (3) is $g^{-1}b_G$, from $h^{-1}S_fG$ to $g^{-1}G$. The exceptional unit instead goes $G\to f^!L_fG$ and supplies the first arrow.

The proof needs $t_{L_fG}L_fu_G=\mathrm{id}_{L_fG}$ and $S_fb_G a_{S_fG}=\mathrm{id}_{S_fG}$. In the second identity, the ordinary unit starts at $S_fG$ on $X$, as it must.

For two points, inverse image sends $A$ to $(A,A)$ and ordinary direct image sends $(G_1,G_2)$ to $G_1\times G_2$. The unit is the diagonal $A\to A\times A$; the counit at the two points consists of the two projections $G_1\times G_2\to G_i$. Their triangular identity states that projecting a diagonal recovers $A$, and the corresponding induced projections after the unit recover each component of $S_fG$.

Finite direct sums and products coincide in this example. Extra maps, such as the inclusion of one component with zero in the other, are therefore available. They do not turn $G\to f^{-1}S_fG$ into the unit of the named ordinary adjunction. The domains and triangular identities continue to distinguish the maps.

### A nonproper open map still has a closed composite

*Difficulty: Intermediate.*

Take $f:(0,\infty)\hookrightarrow\mathbb R$, $g:\{1\}\hookrightarrow(0,\infty)$ and $h=fg$. Check (3) first for $G=k_{(0,\infty)}$, then for $G=g_*Q$, where $Q$ is a bounded finite coefficient complex. Which map is zero in the first case, and why does the second case give an identity?

**Solution.** Both $g,h$ are closed point embeddings, although $f$ is a nonproper open embedding. Near $1$, $f$ is an isomorphism onto an open interval. For the constant input, $g^!G=k[-1]$ and $g^{-1}G=k$. The comparison $\beta_g$ is zero because $\operatorname{Hom}_{D(k)}(k[-1],k)=0$.

The proper image is $M=f_!G$, the positive half-line extended by zero. At $1$, $h^!M=k[-1]$ and $h^{-1}M=k$, so the middle $\beta_h$ is likewise zero. The exceptional unit is an isomorphism because $f^!f_!=\mathrm{id}$ for an open embedding, and the ordinary counit is an isomorphism on that open set. The composite path is consequently zero, as (3) requires.

For $G=g_*Q$, the direct image $M=h_*Q$ is supported on the same point in $\mathbb R$. Both exceptional and ordinary point restrictions recover $Q$. Closed-support counits make $\beta_g$ and $\beta_h$ identities, and open extension/restriction makes the remaining comparisons identities there. Thus both paths are the identity of $Q$, including all its shifts and differentials. Only the point-supported terms used properness; no global properness of $f$ was introduced.

### Proper base change does not turn an ordinary image into a proper image

*Difficulty: Advanced.*

In (8), let $f:\mathbb R_t\times\mathbb R_y\to\mathbb R_t$ be projection, $g:\{0\}\hookrightarrow\mathbb R_t$, and $G=k_{\mathbb R^2}$. Then $Y'=\{0\}\times\mathbb R_y$ and $g'$ is its closed inclusion. Compute the source, top-right and bottom-right terms of (13), and the ordinary target in (14). Determine the two paths to that ordinary target. Why is $\pi_f$ not an isomorphism here?

**Solution.** Constant cohomology on an ordinary real-line fibre is $k$, while compact cohomology is $k[-1]$. Thus $L_fG=k_{\mathbb R_t}[-1]$ and $S_fG=k_{\mathbb R_t}$. The normal point costalk for $g'$ contributes another shift $[-1]$, giving $g'^!G=k_{\mathbb R_y}[-1]$. Hence

\[
 L_{f'}g'^!G=k[-2],\qquad
 L_{f'}g'^{-1}G=k[-1],\qquad
 g^{-1}L_fG=k[-1],\qquad g^{-1}S_fG=k.
\]

The top map $L_{f'}\beta_{g',G}$ is zero. Indeed $\beta_{g',G}$ has source $k_{\mathbb R_y}[-1]$ and target $k_{\mathbb R_y}$, and the group of such derived sheaf morphisms is $H^1(\mathbb R_y;k)=0$. This proves the map is zero as a sheaf morphism, beyond its local point calculation. Therefore the right path is zero. The closed cartesian equality proves the left path is zero as well; alternatively its intermediate $\beta_{g,L_fG}:k[-2]\to k[-1]$ is zero in $D(k)$.

The pullback of $\pi_f$ to any $t$ is a map $k[-1]\to k$, so it is zero. In particular it is not an isomorphism. The ordinary and proper images have different nonzero cohomology degrees. Proper base change (9) remains an isomorphism between the two proper-support terms $k[-1]$, but the following support-forgetting map can still lose all information. The comparison does not invoke an inverse of ordinary base change.

### Keep the odd evaluation sign in a finite proper image

*Difficulty: Intermediate.*

Let $Y=\{a,b\}$, $X=\{\mathrm{pt}\}$ and $f:Y\to X$. Put $G_a=k$, $G_b=k[1]$ and $F=k$. Compute $L_fG$, $S_fH$ and the pairing (18). Name the two cross terms and the value of the pairing on a generator of the $b$ term followed by its dual generator, in the displayed $G$-before-$H$ order.

**Solution.** The finite map is proper. Its exceptional inverse image takes $F$ to the constant pair $(k,k)$, and

\[
 H_a=k,\quad H_b=k[-1],\quad
 L_fG=k\oplus k[1],\quad S_fH=k\oplus k[-1].
\]

The projection-formula map followed by the ordinary counit selects matching point components. The cross terms $G_a\otimes H_b$ and $G_b\otimes H_a$ evaluate to zero because they involve distinct points. The two matching terms pair $k$ with $k$ at $a$, and $k[1]$ with $k[-1]$ at $b$.

The generator of $G_b$ has degree $-1$ and its dual generator in $H_b$ has degree $1$. In the displayed order, evaluation first swaps them, producing $(-1)^{-1\cdot1}=-1$, and dual-first evaluation then gives $1$. The value is therefore $-1_k$. At $a$ it is $1_k$. If one displays the dual factor first instead, that first swap has already occurred; the ordinary dual-first pairing has value $1$. Formula (17) and its evaluated use must use the same ordering. Their currying/evaluation identity proves the equality in Lemma 9.1.6 with precisely this sign.

### Support properness leaves the constant-sheaf unit ordinary

*Difficulty: Advanced.*

Let $f:\mathbb R\to\{\mathrm{pt}\}$ and $G=k_{[0,1]}$. Compute $P=L_fG$, $S_fk_{\mathbb R}$ and $L_fk_{\mathbb R}$. Explain why (19) produces the identity of $P$, and why replacing its top constant-sheaf term by $L_fk_{\mathbb R}$ would fail.

**Solution.** The closed support of $G$ is compact, so $P=L_fG=S_fG=k$ in degree zero. Ordinary sections of the constant sheaf on the line are $S_fk_{\mathbb R}=k$, whereas compact sections are $L_fk_{\mathbb R}=k[-1]$. The map $f$ is proper on the support of $G$, but is not proper on the support of $k_{\mathbb R}$.

The ordinary unit in (19) sends $1_k$ to the constant section on the line. The identity-unit map for $G$ sends that section to $\mathrm{id}_G$. Postcomposition gives the exceptional unit $u_G:G\to f^!P$. Internal adjunction sends it to $t_P L_fu_G=\mathrm{id}_P$. This proves the required identity without declaring $f$ globally proper.

If the initial term were $L_fk_{\mathbb R}=k[-1]$, every map $k\to k[-1]$ in $D(k)$ would be zero. Such a path could not produce the nonzero identity of $P=k$. The ordinary constant-sheaf unit is essential, even though the later constructible objects have proper support.

### Place the closed lemmas in a nonproper graph factorization

*Difficulty: Intermediate.*

Use $f:\mathbb R^2\to\mathbb R$, $(s,t)\mapsto s$, in (20). Verify that $\delta_Y$ and $\gamma$ are closed, show that $f_1$ is nonproper, and prove the cartesian property of (21) directly. State exactly which maps must be closed for each of (3) and (13).

**Solution.** The diagonal is closed because $\mathbb R^2$ is Hausdorff. The graph is the zero set of the equation $x-s=0$ in $\mathbb R_x\times\mathbb R^2_{s,t}$ and its projection to $(s,t)$ is its inverse, so it is a closed embedding. The fibre of $f_1$ over $(x,y_2)$ consists of $y_1=(x,t_1)$ with arbitrary $t_1\in\mathbb R$, and is noncompact. Thus $f_1$ is not proper.

For the cartesian square, the equations $f_2(x,(s,t))=(z,z)$ are $x=z$ and $s=z$. They leave exactly $(s,t)\in Y$, with $(x,y)=(s,(s,t))=\gamma(s,t)$ and $z=f(s,t)$. This gives the full fibre-product identification, not merely a bijection of images.

For (3), use $g=\delta_Y$, the intervening map $f_1$, and the composite $h=\gamma$. The hypotheses require $\delta_Y$ and $\gamma$ closed, both verified, and impose no global properness on $f_1$. For (13), use bottom closed map $g=\delta_X$, top base-change embedding $g'=\gamma$, and the vertical maps $f_2,f$. The closed diagonal makes both horizontal direct images proper. The vertical projections remain nonproper, and their proper-support operations remain distinct from ordinary direct image.

## Remaining work in the proper trace comparison

We have proved the two closed-support comparisons with actual units, counits and support maps, the evaluated internal-adjunction square, the transported identity square and the graph placements. The full proper trace diagram must still apply these comparisons to its external-Hom/product objects and proper duality, then assemble the middle squares with their tensor order. Theorem 9.1.7 and the compact index formula follow only after that assembly and the supported trace are proved. None is inferred from the individual comparison lemmas alone.
