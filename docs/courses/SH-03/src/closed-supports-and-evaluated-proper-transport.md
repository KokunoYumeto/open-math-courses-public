# Closed supports and evaluated proper transport

The characteristic class follows an identity through exceptional restriction, ordinary restriction and evaluation. To transport the class, we need the comparisons between these maps, not just isomorphisms between their objects. Closed embeddings let us test the comparisons by a fully faithful direct image. Proper-support base change and the two adjunctions then reduce them to units, counits and their triangular identities.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources retain their named credit and their own terms.*

The argument has three stages. First, closed direct image detects equality of two restriction comparisons. Second, tensor evaluation identifies the adjunction map that carries an endomorphism to its proper image. Finally, a graph factorization combines those comparisons and retains the closed support of the evaluated class. We use the identity, product evaluation and diagonal construction, the trace-normalized exceptional composition, and proper-support base change with its actual section map. The graph assembly below applies these maps explicitly; Proper characteristic classes and the compact index develops its compact-index consequence.

## Name both adjunctions before composing their maps

We work over a commutative characteristic-zero field $k$. For the two closed-support lemmas, spaces are locally compact Hausdorff with finite integral compact-support cohomological dimension, as required by the standing exceptional-operation contract. Inputs $G$ are bounded. The internal-Hom evaluation calculation has $G\in D^b(k_Y)$ and $F\in D^+(k_X)$, so bounded targets are included without requiring an upper bound on $F$. These domains keep every displayed operation in the constructed bounded-below category.

For a map $f:Y\to X$, abbreviate

\[
 L_f=Rf_!,\qquad S_f=Rf_*.
\]

The natural transformation $\pi_f:L_f\to S_f$ is the derived inclusion of properly supported sections into all sections. Its support-erasure proof (EX.36)–(EX.37a) checks compatibility with composition and base change on the same section maps. Thus its naturality is a statement about a specified transformation, not a choice of an isomorphism on objects with proper support. Write the adjunction maps as follows:

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

Indeed $\beta_{i,A}=i^{-1}t_{i,A}$ under $i^{-1}i_*i^!A\simeq i^!A$. Applying $i_*$ and using naturality of the ordinary unit gives (2). Conversely, applying $i^{-1}$ to (2) recovers this formula, because the unit restricts to the identity on the closed image. The closed-support identity $i_*i^!A=R\Gamma_ZA$ identifies $t_{i,A}$ with forgetting that closed support. Since $i_*$ is exact and fully faithful, including on the bounded-below derived category, it detects equality of these maps.

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

The first arrow inserts the exceptional unit on the upper space. The final arrow removes an ordinary inverse/direct-image pair by its counit. Their opposite adjunctions explain the direction of the path and determine the cancellations in the proof.

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
 h_*g^{-1}b_G\,a_{h,S_fG}\,\pi_{f,G}\,L_ft_{g,G}.
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

Postcomposing with $g^{-1}\pi_{f,G}$ gives the supported-to-ordinary comparison. Its right path first identifies the two proper-support objects and only then forgets the vertical support:

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

This identity is an equality from $L_fG$ to $g_*L_{f'}g'^{-1}G$. We verify its adjunction mates explicitly. For $D\in D^+(k_{Y'})$, the transpose of $K_D$ under $g^{-1}\dashv g_*$ is

\[
\overline K_D:
g^{-1}L_fg'_*D
\xrightarrow{B_{g'_*D}}L_{f'}g'^{-1}g'_*D
\xrightarrow{L_{f'}b_{g',D}}L_{f'}D.
\]

This is the closed-horizontal case of the mixed exchange identity (EX.37a). It can be checked before deriving: both sides pull a properly supported section to the fibre-product square and evaluate it at its pulled-back germ. Since the horizontal inclusions are closed, their proper and ordinary direct images coincide. The finite proper-support model and its pullback compute base change and composition using those same maps, so the equality survives derivation. No support is erased in either vertical direction.

The left side of (15) has transpose $B_G$, by the ordinary triangular identity. The transpose of the right side, with $D=g'^{-1}G$, is

\[
\begin{aligned}
&L_{f'}b_{g',g'^{-1}G}\,
B_{g'_*g'^{-1}G}\,g^{-1}L_fa_{g',G}\\
&\quad=L_{f'}\bigl(b_{g',g'^{-1}G}\,g'^{-1}a_{g',G}\bigr)\,B_G
=B_G.
\end{aligned}
\]

The first equality is naturality of $B$; the second is the other ordinary triangular identity. Equality of these two transposes proves (15). This verifies the needed mixed comparison rather than assuming that two identifications of the same objects agree.

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

where (15) supplies the last equality. This is (16). Full faithfulness proves (13), and postcomposition gives the supported-to-ordinary comparison to $g^{-1}S_fG$. Every comparison retains the same units, counits and properly supported sections. $\square$

## The evaluated proper-Hom map has a prescribed tensor order

Let $G\in D^b(k_Y)$ and $F\in D^+(k_X)$, and put

\[
 H=R\mathcal Hom_Y(G,f^!F).
\]

Boundedness of the first Hom input makes $H$ bounded below. The finite dimension bound makes $L_fG$ bounded, so the corresponding Hom on $X$ is bounded below too. The evaluated internal exceptional adjunction is the natural isomorphism

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

**Evaluation compatibility.** Evaluating $1\otimes v$ gives exactly (18), including the map from $L_fG\otimes S_fH$ toward $L_f(G\otimes H)$. The latter map uses $b_H$ and is not asserted invertible.

**Proof.** Tensor–Hom adjunction identifies maps from $S_fH$ into $R\mathcal Hom(L_fG,F)$ with pairings from $L_fG\otimes S_fH$ to $F$, using the stated symmetry. Define $v$ as the curry of (18). Evaluating that curry returns (18) by the tensor–Hom triangular identity.

To prove that this actual map is invertible, test against any $C\in D^+(k_X)$. The ordinary adjunction, tensor–Hom adjunction, exceptional adjunction and projection formula (EX.11) give

\[
\begin{aligned}
\operatorname{Hom}_X(C,S_fH)
&\simeq\operatorname{Hom}_Y(f^{-1}C,R\mathcal Hom(G,f^!F))\\
&\simeq\operatorname{Hom}_Y(f^{-1}C\otimes^LG,f^!F)\\
&\simeq\operatorname{Hom}_X(L_f(f^{-1}C\otimes^LG),F)\\
&\simeq\operatorname{Hom}_X(C\otimes^LL_fG,F)\\
&\simeq\operatorname{Hom}_X(C,R\mathcal Hom(L_fG,F)).
\end{aligned}
\]

All tensors lie in $D^+$ because $C$ is bounded below and $G,L_fG$ are bounded. The two represented Hom objects also lie in $D^+$. Tracking the counits through this chain gives the ordinary $b_H$, then evaluation and the exceptional $t_F$ in (18); exchanging the displayed tensor factors uses exactly its graded symmetry. Hence this natural bijection is induced by $v$, not another map between its objects. Yoneda proves that $v$ is an isomorphism. The finite-resolution calculation (EX.20a) and evaluated comparison (EX.22) give the same normalization on every open set. $\square$

The bounded first input is retained throughout this proof. An arbitrary bounded-below $G$ can have internal Hom unbounded below: on a point, $G=\bigoplus_{n\ge0}k[-n]$ and $F=k$ have dual cohomology in every degree $-n$. The present argument does not use an unbounded proper-image construction to enlarge its stated domain.

## The transported identity follows from the exceptional triangle

The identity comparison itself only needs the standing finite-dimensional adjunctions and $G\in D^b(k_Y)$. Put $P=L_fG$, which is bounded by the finite cohomological dimension of $f_!$. No properness or constructibility assumption is required for the identity calculation below.

For its later geometric application, take $f:Y\to X$ real analytic between real analytic manifolds, $G\in D^b_{\mathbb R\text{-c}}(k_Y)$, and $f$ proper on the closed support of $G$. Then

\[
 P=L_fG\simeq S_fG
\]

is bounded constructible by the proper perfect-image theorem for analytic maps. Analyticity is used in this constructibility conclusion; it is not a consequence of assuming only that the two underlying manifolds are analytic. The unit $u_G:G\to f^!P$ induces

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

We now apply these two placements to their actual product objects. This completes the graph comparison rather than only identifying the square of spaces.

Assume the analytic proper-support hypotheses just stated, and put $Z=\operatorname{supp}(G)$, $E=D_YG$, $P=L_fG\simeq S_fG$, $Q=D_XP$, $A=G\boxtimes E$ and $\mathscr K=P\boxtimes E$. The constructible duality theorem makes $E,Q$ bounded constructible. The supports of $E$ and $R\mathcal Hom(G,G)$ lie in $Z$, because these objects vanish on every open set where $G$ does. Thus support forgetting is invertible on them. The same holds for $f_1$ on $A$ and for $f_2$ on $\mathscr K$: their supports lie respectively in $Z\times Z$ and $\operatorname{supp}(P)\times Z$, where the relevant maps are restrictions of the proper product maps $f|_Z\times\mathrm{id}$ and $\mathrm{id}\times f|_Z$.

Internal adjunction with target $\omega_X$ defines proper duality as the actual map $d=v_E\pi_{f,E}:L_fE\xrightarrow{\sim}Q$, using $f^!\omega_X=\omega_Y$. Projection and proper-support base change give

\[
\sigma_1:L_{f_1}A\xrightarrow{\sim}\mathscr K,
\qquad
\sigma_2:P\boxtimes Q\xrightarrow{\sim}L_{f_2}\mathscr K.
\]

The first pulls the independent $E$ factor out of $L_{f_1}$; the second is the inverse of $L_{f_2}\mathscr K\simeq P\boxtimes L_fE\xrightarrow{1\boxtimes d}P\boxtimes Q$. These specifications fix both maps and the tensor order.

Let $U:A\to f_1^!\mathscr K$ be the exceptional unit followed by $f_1^!\sigma_1$. For (21), write $c:L_f\gamma^!\mathscr K\to\delta_X^!L_{f_2}\mathscr K$ for (11), and $B:\delta_X^{-1}L_{f_2}\mathscr K\xrightarrow{\sim}L_f\gamma^{-1}\mathscr K$ for (9). Define

\[
\begin{aligned}
\alpha&=(\delta_X^!\sigma_2)^{-1}\,c\,L_f(\delta_Y^!U),\\
m&=L_f(b_G\otimes1_E)\,B\,(\delta_X^{-1}\sigma_2).
\end{aligned}
\]

Here exceptional composition gives $\delta_Y^!f_1^!=\gamma^!$, while $\gamma^{-1}\mathscr K=f^{-1}P\otimes E$ and $\delta_X^{-1}(P\boxtimes Q)=P\otimes Q$. The typed graph diagram is

\[
\begin{array}{ccc}
L_f\delta_Y^!A&\xrightarrow{\alpha}&\delta_X^!(P\boxtimes Q)\\
{\scriptstyle L_f\beta_{\delta_Y,A}}\downarrow&&
\downarrow{\scriptstyle\beta_{\delta_X,P\boxtimes Q}}\\
L_f(G\otimes E)&\xleftarrow{m}&P\otimes Q.
\end{array}
\]

Its commutativity means $L_f\beta_{\delta_Y,A}=m\beta_{\delta_X,P\boxtimes Q}\alpha$. Indeed, (3) applied to $\delta_Y,f_1,\gamma$ expresses $\beta_{\delta_Y,A}$ as $\delta_Y^!U$, then $\beta_{\gamma,\mathscr K}$, then $b_G\otimes1_E$. The last identification follows by restricting the first-factor ordinary counit for $f_1$; the independent second factor remains $E$. Next (13), applied to (21), gives

\[
L_f\beta_{\gamma,\mathscr K}
=B\,\beta_{\delta_X,L_{f_2}\mathscr K}\,c.
\]

Naturality of $\beta$ with respect to $\sigma_2$ changes the middle factor to $\beta_{\delta_X,P\boxtimes Q}$ and gives exactly the asserted equation. Thus both substantive cells of the graph diagram are the closed comparisons already proved above.

It remains to identify $\alpha$ on endomorphisms. For a bounded constructible $B$ on a manifold $W$, let $\theta_B:R\mathcal Hom(B,B)\xrightarrow{\sim}\delta_W^!(B\boxtimes D_WB)$ be the inverse of the evaluated diagonal identification. Let $\rho:S_fR\mathcal Hom(G,G)\to R\mathcal Hom(P,P)$ be postcomposition with $u_G$ followed by (17), the endomorphism comparison used in (19). We claim

\[
\alpha L_f\theta_G=\theta_P\rho\,\pi_{f,R\mathcal Hom(G,G)}.
\]

To verify the claim, write $p_Y,p_X$ for the projections of $X\times Y$. The actual external-Hom evaluation, with the constructible factor on $Y$, and exceptional inverse image of Hom (EX.26) give

\[
\mathscr K\simeq R\mathcal Hom(p_Y^{-1}G,p_X^!P),
\qquad
\gamma^!\mathscr K\simeq R\mathcal Hom(G,f^!P).
\]

Under the corresponding identification $f_1^!\mathscr K\simeq f^!P\boxtimes E$, the candidate $u_G\boxtimes1_E$ has adjunction transpose $(t_P L_fu_G)\boxtimes1_E=\mathrm{id}_{\mathscr K}$. Uniqueness of the transpose makes it exactly $U$. Thus $\delta_Y^!U$ is postcomposition with $u_G$, including its evaluation normalization.

For the rest of $\alpha$, exceptional exchange and support forgetting, (EX.39), identify $c$ with the ordinary exceptional base-change isomorphism in this supported situation: $\gamma^!\mathscr K$ is supported on $Z$ by the displayed Hom formula, and $f_2$ is proper on $\operatorname{supp}(\mathscr K)$. Both comparisons have the same closed-counit transpose. If $q_1,q_2:X\times X\to X$ are the target projections, proper-support base change and exceptional composition give $L_{f_2}p_Y^{-1}G=q_2^{-1}P$ and $f_2^!q_1^!P=p_X^!P$. Internal adjunction for $f_2$ therefore gives

\[
S_{f_2}\mathscr K
\simeq R\mathcal Hom(q_2^{-1}P,q_1^!P)
\simeq P\boxtimes Q.
\]

The last comparison is target product evaluation in the inverse direction. This combined identification agrees with the inverse of $\sigma_2$ after support forgetting: curry both maps against $q_2^{-1}P$. Pulling the independent first factor through projection leaves in each case the original evaluation $E\otimes G\to\omega_Y$ followed by the trace defining $d$. The projection symmetries are the same, so this also checks the graded order.

Explicitly, testing the resulting map against any $C\in D^+(k_X)$ gives the chain

\[
\begin{aligned}
\operatorname{Hom}_X(C,S_f\gamma^!\mathscr K)
&\simeq\operatorname{Hom}_{X\times Y}(\gamma_*f^{-1}C,\mathscr K)\\
&\simeq\operatorname{Hom}_{X\times Y}
 (\gamma_*(f^{-1}C\otimes G),p_X^!P)\\
&\simeq\operatorname{Hom}_X(L_f(f^{-1}C\otimes G),P)\\
&\simeq\operatorname{Hom}_X(C\otimes P,P).
\end{aligned}
\]

The second line uses external evaluation and projection for the closed graph; the third uses $p_X\gamma=f$ with its composite trace. This is exactly the adjunction chain defining (17). Each tensor is bounded below since $G$ is bounded. It proves the claimed Hom identification of $\alpha$, not merely an equality of its source and target objects.

Finally let $\operatorname{tr}_B:B\otimes D_WB\to\omega_W$ be graded symmetry followed by dual-first evaluation. Under $d$, the map $m$ is

\[
P\otimes L_fE\longrightarrow
L_f(f^{-1}P\otimes E)
\xrightarrow{L_f(b_G\otimes1_E)}L_f(G\otimes E).
\]

This follows directly by restricting $\sigma_2$ to the cartesian graph. Its evaluation agrees with $\operatorname{tr}_P$:

\[
t_{\omega_X}L_f\operatorname{tr}_G\,m=\operatorname{tr}_P.
\]

Here the two possible orders of proper projection require a genuine comparison. Let $\widetilde v_E:L_fE\to R\mathcal Hom(S_fG,\omega_X)$ be the curry of projection on $E$, the ordinary counit on $G$, evaluation and trace. The evaluated support-forgetting identity (EX.41) says

\[
R\mathcal Hom(\pi_{f,G},\omega_X)\,\widetilde v_E
=v_E\pi_{f,E}=d.
\]

To see why, uncurry both sides against $L_fG$. Each evaluates a properly supported $G$ section and a properly supported $E$ section, with support in their intersection, then applies the same trace. The finite flat/soft models derive these identical section maps with the same Koszul symmetry. Since both $\pi$ maps are isomorphisms on these supports, evaluating this equality in the $P$-before-$Q$ order gives the preceding contraction formula. The intermediate counit need not be invertible; its evaluated composite is the map being compared.

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

The generator of $G_b$ has degree $-1$ and its dual generator in $H_b$ has degree $1$. In the displayed order, evaluation first swaps them, producing $(-1)^{-1\cdot1}=-1$, and dual-first evaluation then gives $1$. The value is therefore $-1_k$. At $a$ it is $1_k$. If one displays the dual factor first instead, that first swap has already occurred; the ordinary dual-first pairing has value $1$. Formula (17) and its evaluated use must use the same ordering. Their currying/evaluation identity proves the evaluated compatibility of (17)–(18) with precisely this sign.

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

## Keeping the evaluated class on its closed support

The graph argument supplies the complete evaluated endomorphism comparison. Put

\[
\mathcal T_B=\operatorname{tr}_B\,\beta_{\delta_W,B\boxtimes D_WB}\,\theta_B.
\]

Combining its three proved cells gives the commutative diagram

\[
\begin{array}{ccc}
L_fR\mathcal Hom(G,G)&\xrightarrow{\rho\pi_f}&R\mathcal Hom(P,P)\\
{\scriptstyle L_f\mathcal T_G}\downarrow&&\downarrow{\scriptstyle\mathcal T_P}\\
L_f\omega_Y&\xrightarrow{t_{\omega_X}}&\omega_X.
\end{array}
\]

Here $f$ is analytic and proper on $Z=\operatorname{supp}(G)$, as in the graph application. Set $S=f(Z)$, a closed subset of $X$, and $T_Z=R\Gamma_Z\omega_Y$. The closed-support source is essential: for every complex $V$ supported on a closed set $S$, the localization isomorphism $R\Gamma_SV\simeq V$ and the adjunction for closed support give

\[
\operatorname{Hom}(V,R\Gamma_S A)
\xrightarrow{\sim}\operatorname{Hom}(V,A).
\]

Thus a map from such $V$ has one and only one supported lift. Merely knowing that a map from $k_X$ restricts to zero outside $S$ would not prove this uniqueness. This is the supported-source construction of the characteristic class.

The object $T_Z$ is supported on $Z$. Properness there identifies $S_fT_Z\simeq L_fT_Z$, and the composite

\[
L_fT_Z\longrightarrow L_f\omega_Y
\xrightarrow{t_{\omega_X}}\omega_X
\]

has a unique lift to $R\Gamma_S\omega_X$, because its source is supported on $S$. Its induced global-section map is the specified proper transport

\[
f_\#:H_Z^0(Y;\omega_Y)\longrightarrow H_S^0(X;\omega_X).
\]

Likewise $L_fR\mathcal Hom(G,G)$ is supported on $S$, so the two paths of the evaluated diagram have equal unique lifts to $R\Gamma_S\omega_X$. Precompose this supported equality with the identity path (19), using ordinary direct image for its constant-sheaf unit and the support-forgetting isomorphism on the endomorphism object. The identity square sends that unit to $e_P$. The source characteristic-class path factors through $T_Z$ by its definition. Consequently

\[
f_\#C(G)=C(P)\quad\text{in }H_S^0(X;\omega_X),
\]

where the class of $P$ is enlarged from $\operatorname{supp}(P)\subset S$ to $S$. The image $S$ need not equal the output support. This proves the support map and its compatibility with the actual evaluated identity, rather than only equality after forgetting support. For a point target and compact $Z$, the compact index calculation identifies this trace with the finite coefficient supertrace.

## Sources and mathematical credit

Pierre Schapira, [*An Introduction to Sheaves on Grothendieck Topologies*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf), the freely available edition dated 01/08/2026, gives exceptional composition and internal exceptional adjunction in §4.6, especially Corollary 4.6.2 and Proposition 4.6.6 (pp. 95–96). Propositions 4.6.7–4.6.8 (pp. 96–97) treat closed support and the diagonal Hom formula; §4.7 (pp. 97–98) introduces the dualizing object. These results are the human mathematical sources for the operations used here.

The closed-comparison cancellations, explicit evaluated graph diagram, supported-source lifting argument and six worked exercises are developed here from the named programme proofs of those operations. The internal-Hom bijection keeps the first input bounded and the target bounded below. Proper constructibility additionally uses the stated analytic-map and support hypotheses. Source statements about adjunction objects alone do not replace these comparisons of the actual maps.
