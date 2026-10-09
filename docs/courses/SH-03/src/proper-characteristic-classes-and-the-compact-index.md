# Proper characteristic classes and the compact index

The characteristic class of a constructible complex is obtained by evaluating its identity along the diagonal. Proper transport must preserve that entire map. The two closed-support comparisons place the identity inside a graph factorization; product evaluation and internal adjunction then identify its transported endomorphism. The resulting supported trace gives the Euler index when the target is a point.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources retain their named credit and their own terms.*

M. Kashiwara's [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), develops the characteristic-cycle index theorem in §§3–4. Here we prove the compact index through the proper transport of a supported dualizing class, keeping the diagonal evaluation, support maps and coefficient supertrace explicit. The proof follows three objects: the supported endomorphism complex, its image through a graph, and the finite coefficient complex obtained at a point. The [diagonal evaluation construction](../../analytic-boundaries-and-constructible-traces/src/constructible-traces-and-local-euler-indices.md#the-identity-and-the-evaluated-tensor) specifies the class we transport. The [closed comparison proofs](closed-supports-and-evaluated-proper-transport.md#a-composite-closed-embedding-keeps-the-ordinary-counit) and [evaluated internal adjunction](closed-supports-and-evaluated-proper-transport.md#the-evaluated-proper-hom-map-has-a-prescribed-tensor-order) supply its actual maps. We assemble these maps below, construct the transport with its closed support, and calculate the resulting compact index on a finite complex. The [proper perfect-image proof](../../sheaf-proof-readings/src/SH03/perfect-coefficients-on-compact-fibres.md#proper-direct-image-with-perfect-stalks) supplies the required finiteness.

## Properness is imposed on a closed support

Let $k$ be a commutative field of characteristic zero. Manifolds and maps are real analytic, with the standing finite uniform dimension bounds. Suppose

\[
 f:Y\longrightarrow X,\qquad G\in D^b_{\mathbb R\text{-c}}(k_Y),
 \qquad Z=\operatorname{supp}(G),\qquad f|_Z\text{ proper}.
 \qquad\text{(1)}
\]

The support $Z$ is closed, with the convention of the preceding lessons, and is subanalytic. Its image $S=f(Z)$ is closed because $f|_Z$ is proper. The [proper perfect-image theorem](../../sheaf-proof-readings/src/SH03/perfect-coefficients-on-compact-fibres.md#proper-direct-image-with-perfect-stalks) and [constructible Verdier duality](../../sheaf-proof-readings/src/SH03/constructible-costalks-and-verdier-duality.md#the-evaluation-map-is-biduality) give bounded constructible complexes

\[
 P=Rf_!G\simeq Rf_*G,\qquad E=D_YG,\qquad Q=D_XP.
 \qquad\text{(2)}
\]

Both $E$ and $R\mathcal Hom(G,G)$ are supported on $Z$. The first assertion follows from local vanishing of $G$ outside $Z$; the second follows from local vanishing of the first Hom input. Hence proper and ordinary direct images agree for these two complexes too. The support of $P$ is contained in $S$, but need not equal $S$.

Write $L_f=Rf_!$, $S_f=Rf_*$ and $\pi_f:L_f\to S_f$. As before, $u_G:G\to f^!L_fG$ is the exceptional unit, $t_F:L_ff^!F\to F$ its counit, and $b_H:f^{-1}S_fH\to H$ the ordinary counit. Exceptional composition gives $f^!\omega_X=\omega_Y$. Internal adjunction, applied to the bounded input $G$ and the dualizing target, supplies the actual isomorphism

\[
 d:L_fE\xrightarrow{\pi_{f,E}}S_fE
 \xrightarrow{\sim}R\mathcal Hom(P,\omega_X)=Q.
 \qquad\text{(3)}
\]

To specify the map in (3), first curry the pairing

\[
P\otimes S_fE
\longrightarrow L_f(G\otimes f^{-1}S_fE)
\xrightarrow{L_f(1\otimes b_E)}L_f(G\otimes E)
\xrightarrow{L_f\operatorname{tr}_G}L_f\omega_Y
\xrightarrow{t_{\omega_X}}\omega_X.
\]

Then precompose the curry with $\pi_{f,E}$. The first arrow is inverse projection, and $\operatorname{tr}_G$ contains the graded flip into dual-first evaluation. This is exactly the [evaluated internal-Hom comparison (EX.20)–(EX.22)](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-internal--internal-adjunction-and-its-tensor-structure). Its first input $G$ is bounded and its target $\omega_X$ is bounded below; the finite dimension bound keeps all its functors in the constructed range. Properness on $Z$ makes the precomposition invertible. Thus (3) fixes proper duality as a map. Its orientation complexes are already contained in $f^!\omega_X=\omega_Y$ and the two dualities, so no further shift is appended.

For a constructible complex $B$ on a manifold $W$, abbreviate the pre-contraction part of its characteristic-class map by

\[
 h_B:R\mathcal Hom(B,B)
 \xrightarrow{\theta_B}\delta_W^!(B\boxtimes D_WB)
 \xrightarrow{\beta_{\delta_W}}B\otimes^LD_WB.
 \qquad\text{(4)}
\]

Contraction $\operatorname{tr}_B:B\otimes D_WB\to\omega_W$ is graded symmetry followed by dual-first evaluation. The identity unit followed by $\operatorname{tr}_Bh_B$ defines $C(B)$ with its closed support. Here $\theta_B$ is the inverse of the evaluated diagonal Hom isomorphism, and $\beta_{i,A}=i^{-1}(i_*i^!A\to A)$ is restriction of the exceptional counit. This [closed-embedding comparison](closed-supports-and-evaluated-proper-transport.md#name-both-adjunctions-before-composing-their-maps) is fixed by its counit; it need not be invertible. The source $R\mathcal Hom(B,B)$ is supported on $\operatorname{supp}(B)$, which gives the unique supported lift used in the definition.

## Product maps provide the middle comparison

Put $A=G\boxtimes E$ on $Y\times Y$ and $K=P\boxtimes E$ on $X\times Y$. Use the graph maps

\[
 f_1=(f,\mathrm{id}_Y),\quad f_2=(\mathrm{id}_X,f),\quad
 \gamma(y)=(f(y),y).
 \qquad\text{(5)}
\]

The equality $f_1\delta_Y=\gamma$ follows by evaluating both maps at $y$. Both embeddings are closed: the diagonal is closed in a Hausdorff space, and the graph of a continuous map to a Hausdorff space is closed. The other placement is the cartesian square

\[
\begin{array}{ccc}
Y&\xrightarrow{\gamma}&X\times Y\\
f\downarrow&&\downarrow f_2\\
X&\xrightarrow{\delta_X}&X\times X.
\end{array}
\]

Indeed $(x,f(y))=(z,z)$ forces $x=z=f(y)$; the inverse parametrization of the fibre product is $y\mapsto((f(y),y),f(y))$. This verifies the graph placement, with its topology and maps, for the [two closed comparison lemmas](closed-supports-and-evaluated-proper-transport.md#a-cartesian-closed-restriction-compares-before-support-is-forgotten).

The map $f_1$ is proper on the support of $A$: that support lies in $Z\times Z$, inside the domain of the proper product $f|_Z\times\mathrm{id}_Y$. Similarly $f_2$ is proper on the support of $K$, which lies in $\operatorname{supp}(P)\times Z$. Thus support forgetting is an isomorphism on these product objects.

The [projection map (EX.11)](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-projection--projection-with-arbitrary-coefficients) and [proper-support base change](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-basechange-bridge--a-finite-dimensional-base-change-proof) supply actual product isomorphisms

\[
 \sigma_1:L_{f_1}A\xrightarrow{\sim}K,\qquad
 \sigma_2:P\boxtimes Q\xrightarrow{\sim}L_{f_2}K.
 \qquad\text{(6)}
\]

For the first, pull the second factor $E$ out by projection formula, then use base change for the first factor to get $(L_fG)\boxtimes E$. For the second, the analogous calculation gives $L_{f_2}K\simeq P\boxtimes L_fE$; apply (3) and invert that calculation. These maps retain the indicated order of the two tensor factors and the graded permutations in the projection comparisons.

Let

\[
 U:A\longrightarrow f_1^!K
\]

be the exceptional unit for $f_1$, followed by $f_1^!\sigma_1$. Define the closed cartesian exceptional exchange and proper base change by

\[
 c:L_f\gamma^!K\longrightarrow\delta_X^!L_{f_2}K,
 \qquad
 B:\delta_X^{-1}L_{f_2}K\xrightarrow{\sim}L_f\gamma^{-1}K.
 \qquad\text{(7)}
\]

The map $c$ is the $\delta_{X*}\dashv\delta_X^!$ transpose of

\[
\delta_{X*}L_f\gamma^!K
\xrightarrow{\sim}L_{f_2}\gamma_*\gamma^!K
\xrightarrow{L_{f_2}t_{\gamma,K}}L_{f_2}K.
\]

Proper composition supplies the first arrow because $\delta_Xf=f_2\gamma$ and both horizontal embeddings are closed. This is the [exceptional exchange (EX.38)](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-support-erasure--forgetting-support-and-checking-the-resulting-maps); the extra exceptional functors exist since closed direct image has dimension zero. We first use $c$ as a morphism, with no general claim of invertibility.

Since $\gamma^{-1}K=f^{-1}P\otimes E$, the ordinary counit gives

\[
 \psi=b_G\otimes1_E:\gamma^{-1}K\longrightarrow G\otimes E.
\]

Here $P=S_fG$ via the canonical support-forgetting isomorphism in (2). Define

\[
 \begin{aligned}
 \alpha&=(\delta_X^!\sigma_2)^{-1}\,c\,
             L_f(\delta_Y^!U),\\
 m&=L_f\psi\,B\,(\delta_X^{-1}\sigma_2).
 \end{aligned}
 \qquad\text{(8)}
\]

Their types are

\[
 \alpha:L_f\delta_Y^!A\longrightarrow\delta_X^!(P\boxtimes Q),
 \qquad m:P\otimes Q\longrightarrow L_f(G\otimes E).
\]

In the first line, exceptional composition identifies $\delta_Y^!f_1^!K$ with $\gamma^!K$. In the second, ordinary diagonal restriction identifies $\delta_X^{-1}(P\boxtimes Q)$ with $P\otimes Q$. The diagram to be proved is therefore

\[
\begin{array}{ccc}
L_f\delta_Y^!A&\xrightarrow{\alpha}&\delta_X^!(P\boxtimes Q)\\
{\scriptstyle L_f\beta_{\delta_Y,A}}\downarrow&&
\downarrow{\scriptstyle\beta_{\delta_X,P\boxtimes Q}}\\
L_f(G\otimes E)&\xleftarrow{m}&P\otimes Q.
\end{array}
\]

The bottom arrow points toward the source manifold's integrated tensor. Its direction is what allows contraction there to be compared with contraction on $X$.

**Middle restriction identity.** These maps satisfy

\[
 L_f\beta_{\delta_Y,A}
 =m\,\beta_{\delta_X,P\boxtimes Q}\,\alpha.
 \qquad\text{(9)}
\]

**Proof.** Apply [the composite closed-comparison identity (3)](closed-supports-and-evaluated-proper-transport.md#a-composite-closed-embedding-keeps-the-ordinary-counit) to $\delta_Y,f_1,\gamma$ and $A$. Its exceptional unit is $U$. Since $\pi_{f_1,A}$ is an isomorphism, the composite path gives

\[
 L_f\beta_{\delta_Y,A}
 =L_f\psi\,L_f\beta_{\gamma,K}\,L_f(\delta_Y^!U).
 \qquad\text{(10)}
\]

The ordinary counit for $f_1$ restricts on the diagonal to $b_G\otimes1_E$: under (6), its first-factor counit is $f^{-1}S_fG\to G$ and the second factor is unchanged. This is the ordinary arrow in (10), not an exceptional-to-ordinary identification for $f$ itself.

The [cartesian closed-comparison identity (13)](closed-supports-and-evaluated-proper-transport.md#a-cartesian-closed-restriction-compares-before-support-is-forgotten), before support forgetting, gives

\[
 L_f\beta_{\gamma,K}=B\,\beta_{\delta_X,L_{f_2}K}\,c.
\]

Naturality of $\beta$ with respect to $\sigma_2$ gives

\[
 \beta_{\delta_X,L_{f_2}K}\,\delta_X^!\sigma_2
 =\delta_X^{-1}\sigma_2\,\beta_{\delta_X,P\boxtimes Q}.
\]

Substitute these two equalities in (10), then use (8). This is (9). Each of its two substantive cells is the full closed-comparison lemma already proved; the other equalities are the specified product identifications and naturality of their actual maps. $\square$

## The Hom comparison transports the endomorphism itself

The source-to-target endomorphism map is

\[
 \rho:S_fR\mathcal Hom(G,G)\longrightarrow R\mathcal Hom(P,P).
 \qquad\text{(11)}
\]

It first postcomposes with $u_G:G\to f^!P$, then applies the actual internal adjunction $S_fR\mathcal Hom(G,f^!P)\simeq R\mathcal Hom(P,P)$. To check the identity path, the ordinary unit $k_X\to S_fk_Y$ followed by $S_fe_G$ represents $\mathrm{id}_G$. Postcomposition sends it to $u_G$, whose exceptional adjoint is $t_P L_fu_G=\mathrm{id}_P$. Hence its image by $\rho$ is $e_P$. The same adjunction calculation on each open subset gives the sheaf morphism, with the normalization in [the transported identity proof](closed-supports-and-evaluated-proper-transport.md#the-transported-identity-follows-from-the-exceptional-triangle).

When the domain is $L_fR\mathcal Hom(G,G)$, the notation $\rho$ in (12), (16) and (20) means $\rho\,\pi_{f,R\mathcal Hom(G,G)}$. This is the canonical identification on the supported endomorphism object, rather than a replacement of ordinary direct image on every term. In particular the initial constant-sheaf unit remains ordinary.

**Hom identification of the middle map.** With proper and ordinary images identified on the supported endomorphism object,

\[
 \alpha\,L_f\theta_G=\theta_P\,\rho.
 \qquad\text{(12)}
\]

**Proof.** Denote by $p_Y,p_X$ the projections from $W=X\times Y$. The [external-Hom evaluation](../../sheaf-proof-readings/src/SH02/cohomological-biduality.md#sh02-cb-external-hom--a-constructible-factor-in-a-product), applied to the constructible factor $G$ on $Y$ and then placed in the indicated product order, gives

\[
 K=P\boxtimes E\simeq
 R\mathcal Hom(p_Y^{-1}G,p_X^!P).
 \qquad\text{(13)}
\]

[Exceptional inverse image of Hom (EX.26)](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-hom--exceptional-inverse-image-of-internal-hom) applies because $p_Y^{-1}G$ is bounded and $p_X^!P$ is bounded below. Together with [trace-normalized exceptional composition (EX.13)–(EX.14)](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-composition--composition-restriction-and-change-of-base), it gives

\[
 \gamma^!K\simeq R\mathcal Hom(G,f^!P),\qquad
 \delta_Y^!f_1^!K\simeq R\mathcal Hom(G,f^!P).
 \qquad\text{(14)}
\]

The corresponding calculation on $Y\times Y$ identifies $\delta_Y^!A$ with $R\mathcal Hom(G,G)$. Under these identifications, $\delta_Y^!U$ is postcomposition with $u_G$. To check its normalization, the product exceptional-Hom comparison identifies $f_1^!K$ with $f^!P\boxtimes E$. Transpose the candidate $u_G\boxtimes1_E$ along $L_{f_1}\dashv f_1^!$, using the projection/composition maps defining (6). Its transpose is

\[
 (t_P\,L_fu_G)\boxtimes1_E=\mathrm{id}_{P\boxtimes E}.
\]

The equality is the exceptional triangular identity. Uniqueness of the adjunction transpose makes this candidate exactly $U$. Restricting by the evaluated exceptional-Hom comparison gives precisely postcomposition with $u_G$ in (14).

We next check the remaining part of $\alpha$. The object $\gamma^!K$ is supported on $Z$, by (14), and $f_2$ is proper on the support of $K$. Therefore the support-forgetting comparisons identify $c$ with the ordinary exceptional base-change isomorphism $S_f\gamma^!K\simeq\delta_X^!S_{f_2}K$. More precisely, if $c_*:S_f\gamma^!K\xrightarrow{\sim}\delta_X^!S_{f_2}K$ denotes ordinary exceptional base change, [the supported exchange identity (EX.39)](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-support-erasure--forgetting-support-and-checking-the-resulting-maps) is

\[
\delta_X^!\pi_{f_2,K}\,c
=c_*\,\pi_{f,\gamma^!K}.
\]

Both $\pi$ maps here are invertible on the supports just checked. This determines $c$ in terms of $c_*$, with its counit normalization, and proves invertibility in this particular supported application.

After using (13), internal adjunction for $f_2$ identifies $S_{f_2}K$ with

\[
 R\mathcal Hom(q_2^{-1}P,q_1^!P),
\]

where $q_1,q_2$ are the projections of $X\times X$. Here $L_{f_2}p_Y^{-1}G=q_2^{-1}P$ by proper-support base change, and $f_2^!q_1^!P=p_X^!P$ by exceptional composition. The product evaluation for $P$ identifies this Hom object with $P\boxtimes Q$.

Let $J:S_{f_2}K\xrightarrow{\sim}P\boxtimes Q$ denote this combined internal-Hom and product-evaluation identification. Its direction is opposite to $\sigma_2$ in (6); the required equality is

\[
J\,\pi_{f_2,K}=\sigma_2^{-1}.
\]

Curry both sides against $q_2^{-1}P$. Pulling the independent first factor through projection leaves the same second-factor evaluation $E\otimes G\to\omega_Y$ and the same trace defining (3). Equivalently one may use $G\otimes E$ with the graded flip in $\operatorname{tr}_G$. The ordered product evaluations use the same permutations in either description. Thus the evaluated projection and internal-adjunction comparisons prove this equality of maps. Inverting it supplies exactly the direction of $\sigma_2$ used in (8).

For an explicit check of the resulting graph-Hom adjunction, test it against $C\in D^+(k_X)$. Its chain of bijections is

\[
 \begin{aligned}
 \operatorname{Hom}_X(C,S_f\gamma^!K)
 &\simeq\operatorname{Hom}_Y(f^{-1}C,\gamma^!K)\\
 &\simeq\operatorname{Hom}_W(\gamma_!f^{-1}C,K)\\
 &\simeq\operatorname{Hom}_W(
       \gamma_!(f^{-1}C\otimes G),p_X^!P)\\
 &\simeq\operatorname{Hom}_X(L_f(f^{-1}C\otimes G),P)\\
 &\simeq\operatorname{Hom}_X(C\otimes P,P).
 \end{aligned}
 \qquad\text{(15)}
\]

The third step uses (13), tensor–Hom adjunction and projection for the closed graph; the fourth uses $p_X\gamma=f$ and its trace-normalized exceptional composition; the fifth uses projection formula for $f$. This is exactly the evaluated internal adjunction used in (11). Equivalently, the exceptional base-change step tests the same object $f_2^{-1}\delta_{X*}C=\gamma_*f^{-1}C$, since the diagonal is closed. All tensors remain bounded below: $C$ is bounded below and $G$ is bounded. The bijections retain the normalized evaluations and their symmetries.

Thus the first part of $\alpha$ is the unit postcomposition in (11), and its remainder is that map's evaluated internal adjunction, with the target's diagonal evaluation inverse. This proves (12). $\square$

Combining (9) and (12) yields the complete middle equality

\[
 L_fh_G=m\,h_P\,\rho.
 \qquad\text{(16)}
\]

This is the content of the two middle squares of the proper trace diagram. It has been proved on the actual endomorphism maps, before contracting them.

## Evaluation completes the trace diagram

Under (3), the map $m$ of (8) is the ordered projection pairing

\[
 P\otimes L_fE\xrightarrow{\sim}L_f(f^{-1}P\otimes E)
 \xrightarrow{L_f(b_G\otimes1)}L_f(G\otimes E).
 \qquad\text{(17)}
\]

This identification follows by proper base change for the cartesian graph square applied to $\sigma_2$; it restricts the independent first factor to $f^{-1}P$ and leaves the properly integrated second factor $E$ unchanged.

There are two ways to compare such an evaluated pairing with internal adjunction. The usual evaluated-Hom square uses the ordinary counit on $E$ after projection on $G$. Formula (17) uses the counit on $G$ after projection on $E$. The [evaluated support-forgetting identity (EX.40)–(EX.41)](../../sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-hom-support-compatibility--evaluation-when-either-support-is-forgotten) asserts

\[
 R\mathcal Hom(\pi_{f,G},\omega_X)\,u_E
 =v_E\,\pi_{f,E},
 \qquad\text{(18)}
\]

Here $v_E:S_fE\simeq R\mathcal Hom(L_fG,\omega_X)$ is internal adjunction. The notation $u_E$ in (18) denotes the supported evaluation map, not an exceptional unit: it is the curry of

\[
L_fE\otimes S_fG
\longrightarrow L_f(E\otimes f^{-1}S_fG)
\xrightarrow{L_f(1\otimes b_G)}L_f(E\otimes G)
\xrightarrow{L_f\mathrm{ev}}L_f\omega_Y
\xrightarrow{t_{\omega_X}}\omega_X.
\]

Uncurry both sides of (18) against $L_fG$. The left path forgets support on the $G$ section; the right forgets support on the $E$ section. They evaluate the same two sections, whose common tensor is properly supported on the intersection of their supports, and apply the same trace. On the finite flat/soft models for proper image and the comparison to ordinary injective models, these are the identical section-evaluation chain maps. The projection and support-forgetting compatibilities therefore derive this equality with the same Koszul symmetry. This proves the comparison needed here without inverting either ordinary counit.

Both support-forgetting maps in (18) are isomorphisms under (1). Consequently, evaluating (18) in the $P$-before-$Q$ order gives

\[
 t_{\omega_X}\,L_f\operatorname{tr}_G\,m
 =\operatorname{tr}_P.
 \qquad\text{(19)}
\]

This proves the last trace square for the actual $m$ used in (16). In particular, a bare projection pairing is not incorrectly declared invertible, and the two evaluation orders are compared with their graded signs. One may also verify (19) directly in the evaluated resolution model; (18) records precisely the needed compatibility.

The identity calculation, Hom identification (12), closed restriction (9) and contraction (19) account for the four maps in the trace comparison. Combining (16) with (19), the whole evaluated endomorphism map satisfies

\[
 t_{\omega_X}\,L_f(\operatorname{tr}_Gh_G)
 =\operatorname{tr}_Ph_P\,\rho.
 \qquad\text{(20)}
\]

The top constant-sheaf term remains $S_fk_Y$, with unit $k_X\to S_fk_Y$. Nothing in this proof asserts that $f$ is proper on the support of $k_Y$.

## The supported trace transports the characteristic class

Set $T_Z=R\Gamma_Z\omega_Y$. For the closed inclusion $i:Z\hookrightarrow Y$, the support adjunction gives $T_Z=R\mathcal Hom(k_Z,\omega_Y)=D_Yk_Z$. A compatible subanalytic stratification makes $k_Z$ constructible, so constructible duality makes $T_Z$ bounded constructible. Its restriction to $Y\setminus Z$ is zero, hence its support lies in $Z$. Properness on $Z$ identifies $S_fT_Z$ with $L_fT_Z$.

To justify the supported lift, let $j:X\setminus S\hookrightarrow X$ and let $V$ be any bounded-below complex supported on $S$. For every $A\in D^+(k_X)$, localization gives the triangle $R\Gamma_SA\to A\to Rj_*j^{-1}A\xrightarrow{+1}$. Adjunction gives $\operatorname{Hom}(V,Rj_*j^{-1}A[n])=\operatorname{Hom}(j^{-1}V,j^{-1}A[n])=0$ for every integer $n$. Applying $\operatorname{Hom}(V,-)$ therefore proves

\[
\operatorname{Hom}(V,R\Gamma_SA)
\xrightarrow{\sim}\operatorname{Hom}(V,A).
\]

This proves existence and uniqueness from the supported source. Apply it to $V=L_fT_Z$, which is supported on $S$ by proper-support base change, and to $A=\omega_X$. The trace has the unique supported lift

\[
 L_fT_Z\longrightarrow R\Gamma_S\omega_X
 \qquad\text{(21)}
\]

of $L_fT_Z\to L_f\omega_Y\xrightarrow{t_{\omega_X}}\omega_X$. Write $\ell:L_fT_Z\to R\Gamma_S\omega_X$ for (21). The actual map on section complexes is

\[
\begin{aligned}
R\Gamma(Y;T_Z)&\simeq R\Gamma(X;S_fT_Z)\\
&\xrightarrow{R\Gamma(\pi_{f,T_Z}^{-1})}R\Gamma(X;L_fT_Z)
\xrightarrow{R\Gamma(\ell)}R\Gamma(X;R\Gamma_S\omega_X).
\end{aligned}
\]

Every inverse in this chain is justified by properness on $Z$. Taking degree-zero cohomology gives

\[
 f_\#:H_Z^0(Y;\omega_Y)\longrightarrow H_S^0(X;\omega_X).
 \qquad\text{(22)}
\]

**Proper characteristic-class theorem.** Under (1),

\[
 C(P)=f_\#C(G)
 \quad\text{in }H_S^0(X;\omega_X).
 \qquad\text{(23)}
\]

On the left, the class with support $\operatorname{supp}(P)$ is enlarged to $S$.

**Proof.** Equation (20) is an equality of maps from $L_fR\mathcal Hom(G,G)$ to $\omega_X$. That source is supported on $S$, so both maps lift uniquely to $R\Gamma_S\omega_X$. Hence (20) is also an equality of supported maps, not merely an equality after support is forgotten.

Let $E_G=R\mathcal Hom(G,G)$. Precompose the lifted equality with the actual path

\[
k_X\longrightarrow S_fk_Y
\xrightarrow{S_fe_G}S_fE_G
\xrightarrow{\pi_{f,E_G}^{-1}}L_fE_G.
\]

The first arrow is the ordinary unit, whose input is on $X$; its image on global units is $1_Y$. The final inverse is legitimate because $E_G$ is supported on $Z$. On the target path it cancels the $\pi_{f,E_G}$ suppressed in (20), and the identity calculation above gives $e_P$. The target's supported evaluation is therefore $C(P)$ enlarged to $S$.

For the source path, the defining supported evaluation $E_G\to T_Z$ commutes with $\pi_f$ by naturality. It consequently gives exactly the section-complex path defining $f_\#$ after the image of $C(G)$ in $R\Gamma(Y;T_Z)$. Thus the two lifted paths yield (23), with the same support map, not merely after passing to ordinary cohomology. $\square$

This argument also fixes the support-image map, rather than introducing an unspecified pushforward on cohomology groups. The image $S$ can be larger than the output support, and the target comparison remains the natural enlargement of a closed support condition.

## Compact support gives an integer index

Let $F\in D^b_{\mathbb R\text{-c}}(k_X)$ have compact closed support $Z$, and let $a:X\to\{\mathrm{pt}\}$. The map is proper on $Z$, so (23) applies. Compact constructible finiteness and the actual comparison give

\[
 P=Ra_!F=R\Gamma_c(X;F)\simeq R\Gamma(X;F).
\]

Finiteness here concerns the entire coefficient complex. One way to see it is the [finite compact-triangulation descent proof](../../sheaf-proof-readings/src/SH03/perfect-coefficients-on-compact-fibres.md#finite-descent-on-a-compact-triangulation): a triangulation compatible with the finitely many cohomology sheaves has only finitely many simplices on $Z$. Its finite open-star cover has perfect section complexes on every nonempty intersection. Finite derived Čech descent uses their actual alternating restriction maps, and filtration by its finitely many columns expresses the result by finite sums, shifts and cones of perfect complexes. Thus $P$ has a bounded representative $V^\bullet$ of finite-dimensional vector spaces. This does not replace the differentials by stalk dimensions.

We calculate the point class on this representative. At a point the diagonal and its two restrictions are identities. The evaluated tensor–Hom map is

\[
V^\bullet\otimes(V^\bullet)^\vee
\longrightarrow\operatorname{Hom}^\bullet(V^\bullet,V^\bullet),
\qquad v\otimes\varphi\longmapsto(w\mapsto v\varphi(w)).
\]

For $\varphi$ of degree $b$, the dual differential is $d\varphi=(-1)^{b+1}\varphi d$. Substitution shows that the displayed map commutes with differentials. If $e_{q,j}$ is a homogeneous basis of $V^q$, its inverse sends the identity to the closed element $\sum_{q,j}e_{q,j}\otimes e_{q,j}^*$. Contraction flips degrees $q$ and $-q$, contributing $(-1)^{-q^2}=(-1)^q$, and then evaluates each matching pair to $1$. Hence

\[
C(P)=\left(\sum_q(-1)^q\dim_k V^q\right)1_k.
\]

To replace terms by cohomology, set $B^q=\operatorname{im}d^{q-1}$ and $Z^q=\ker d^q$. The exact sequences $0\to Z^q\to V^q\to B^{q+1}\to0$ and $0\to B^q\to Z^q\to H^q(V)\to0$ give $\dim V^q=\dim B^q+\dim H^q(V)+\dim B^{q+1}$. The two boundary sums cancel in the finite alternating sum. Therefore $C(P)=\chi(X;F)1_k$, with precisely the [graded point-trace normalization](../../analytic-boundaries-and-constructible-traces/src/constructible-traces-and-local-euler-indices.md#a-point-fixes-the-trace-sign). No splitting of the original sheaf complex into its cohomology is used.

The trace $Ra_!\omega_X\to k$ defines integration on **compactly supported** cohomology,

\[
 \int_X:H_c^0(X;\omega_X)\longrightarrow k.
 \qquad\text{(24)}
\]

Since $Z$ is compact, the actual map of section complexes is

\[
R\Gamma(X;T_Z)
\xrightarrow{\sim}R\Gamma_c(X;T_Z)
\longrightarrow R\Gamma_c(X;\omega_X)
\xrightarrow{t_{\omega_X}}k.
\]

The first arrow is the inverse of support forgetting on $T_Z$, and the middle arrow forgets the closed condition $Z$ while retaining compact support. This is exactly the specialization of the section-complex construction (21)–(22) to $a$. Thus its degree-zero map first sends $H_Z^0(X;\omega_X)$ to the compactly supported group and then applies (24), giving

\[
 \int_X C(F)=\chi(X;F)1_k.
 \qquad\text{(25)}
\]

This is the compact index identity with its specified support map and graded trace normalization. An ordinary group $H^0(X;\omega_X)$ need not admit this integration when $X$ is noncompact. Even a class supported on a compact set can vanish after it is mapped to ordinary cohomology, while its integral remains nonzero. Characteristic zero lets the resulting field element recover the integer index; in positive characteristic it would record only its reduction.

## Exercises with complete solutions

### A point-supported class carries the coefficient supertrace

*Difficulty: Introductory.*

Let $i:\{x\}\hookrightarrow X$ be a closed point inclusion and $V$ a bounded finite coefficient complex. Describe $C(i_*V)$ and its integral. In particular, what happens for $V=k[r]$ and for $V=k\oplus k[1]$? Does the dimension or orientation of $X$ insert another sign?

**Solution.** The point map is proper and $i^!\omega_X=\omega_{\{x\}}=k$ by exceptional composition. Consequently $H_{\{x\}}^0(X;\omega_X)=k$ canonically. Let $\delta_x$ denote the image of $1_k$ in that supported group. Trace composition for $a_Xi=a_{\{x\}}$ gives $\int_X\delta_x=1_k$.

The proper class theorem and the point supertrace calculation give $C(i_*V)=\chi(V)\delta_x$ and $\int_XC(i_*V)=\chi(V)1_k$. For $k[r]$ the coefficient is $(-1)^r$, with the cohomological shift placing its nonzero cohomology in degree $-r$. For $k\oplus k[1]$ the coefficient is zero despite two nonzero cohomology groups.

There is no further ambient-dimension sign. The orientation line and real-dimension shift of $\omega_X$ are already paired with the normal costalk in $i^!\omega_X=k$. Choosing a global orientation is unnecessary for this canonical point class.

### A nonproper map can transport a finite closed support

*Difficulty: Intermediate.*

Take $f:\mathbb R\to\mathbb R$, $f(y)=\sin y$, and let $G=i_{0*}V\oplus i_{\pi*}W$ for two bounded finite coefficient complexes. Compute $Rf_*G$, the image of its characteristic class, and the integral. Do the opposite derivative signs of $f$ at $0$ and $\pi$ change the two weights?

**Solution.** The map has infinite noncompact fibres and is not globally proper. Its restriction to the containing two-point closed set is proper, hence so is its restriction to the support of $G$. Both points map to $0$, and exact finite closed direct image gives $Rf_*G=Rf_!G=i_{0*}(V\oplus W)$ on the target.

On the source, point-class evaluation is block diagonal and yields $C(G)=\chi(V)\delta_0+\chi(W)\delta_\pi$. Trace composition for $fi_0=i_0$ and $fi_\pi=i_0$ sends each normalized point class to the same target point class. Hence its image is $(\chi(V)+\chi(W))\delta_0$, and its integral is $(\chi(V)+\chi(W))1_k$.

The derivative values $+1$ and $-1$ do not introduce weights into this degree-zero point pushforward. These are canonical point dualizing classes, with their ambient orientation factors already accounted for. Composition of the closed-point traces proves each coefficient is $+1$. For $V=k$ and $W=k[1]$ the weights cancel, although the output complex is nonzero. Properness is on the closed support throughout.

### Compact integration can detect a class forgotten by ordinary cohomology

*Difficulty: Advanced.*

On $X=\mathbb R$ let $Z=[0,1]$, $F_c=k_{[0,1]}$ and $F_o=k_{(0,1)}$ extended by zero. Compute $H_Z^0(X;\omega_X)$, $H_c^0(X;\omega_X)$ and $H^0(X;\omega_X)$, then determine the characteristic classes and their integrals. Why would integrating only the ordinary images fail?

**Solution.** Choose the increasing orientation, so $\omega_X=k[1]$. Ordinary cohomology of the contractible line gives $H^0(X;\omega_X)=H^1(\mathbb R;k)=0$. Compact cohomology gives $R\Gamma_c(\mathbb R;\omega_X)=k$, so $H_c^0(X;\omega_X)=k$, with trace identifying its generator.

For supported cohomology, localization deletes the closed interval. The two complementary rays have derived sections $k\oplus k$, and the restriction $k\to k\oplus k$ is diagonal. Thus $R\Gamma_Z(\mathbb R;k)=k[-1]$, and shifting by $[1]$ gives $H_Z^0(X;\omega_X)=k$.

Normalize its generator by the point class $\delta_x$ for any $x\in Z$, enlarged to support $Z$. Its image in the compact group integrates to $1$ by the preceding exercise, so it is a basis of the one-dimensional supported group. The actual interval computations give $R\Gamma(X;F_c)=k$ and $R\Gamma(X;F_o)=k[-1]$, both with compact closed support. Formula (25) therefore determines $C(F_c)=\delta_x$ and $C(F_o)=-\delta_x$ in $H_Z^0(X;\omega_X)$, with integrals $1_k$ and $-1_k$.

Their ordinary images are both zero because the ordinary target group is zero. Forgetting the compact support condition before using (24) loses these nonzero integrals. The map used in the theorem is the supported-to-compact map, followed by the trace, exactly as in (21)–(24).

### A compact rectangle checks the proper-duality shift

*Difficulty: Intermediate.*

Let $f:\mathbb R_t\times\mathbb R_y\to\mathbb R_t$ be projection and $G=k_{[0,1]\times[-1,1]}$. Compute $P$, $E$, $Q$ and $L_fE$ with their shifts. Determine the transported class and its global index, and repeat the index for $G[r]$.

**Solution.** The rectangle is compact, so $f$ is proper on its closed support despite being globally nonproper. Each nonempty closed-interval fibre has ordinary cohomology $k$ in degree zero; the constant-section comparison commutes with all restrictions. Thus $P=k_{[0,1]}$.

For the open rectangle $U=(0,1)\times(-1,1)$, open internal duality gives $Dk_U=Rj_*k_U[2]$. Small neighborhoods intersect $U$ in [convex sets with their constant-section comparison](../../sheaf-proof-readings/src/SH02/convex-acyclicity.md#sh02-ca-constant--constant-coefficients), including at corners, so the actual constant-section maps identify $Rj_*k_U$ with the closed-rectangle constant sheaf. Constructible biduality therefore gives $E=D_YG=k_U[2]$. On the real-line target, the same interval duality gives $Q=k_{(0,1)}[1]$.

Compact cohomology of the open $y$-interval is $k[-1]$. Projection formula and proper-support base change consequently give $L_fE=k_{(0,1)}[2-1]=k_{(0,1)}[1]=Q$, matching the actual proper-duality map (3). The real dimensions two and one have already supplied all shifts.

The transported class is $C(P)$ supported in $[0,1]$; its integral is $1$. The source closed rectangle is contractible and compact, so its global index is also $1$. For $G[r]$, the section complex is $k[r]$ and the index is $(-1)^r$. Its transported object is $P[r]$, with the same integral by (25). No Jacobian factor or additional fibre shift is inserted into the characteristic class.

### A circle can have a nonzero local rank and zero characteristic class

*Difficulty: Intermediate.*

Let $L$ be a rank-$r$ local system on a circle, with $r>0$ and monodromy $T\in\operatorname{GL}_r(k)$. Compute its global Euler index and its characteristic class in $H^0(S^1;\omega_{S^1})$. Explain the case where $T-1$ is invertible, including the support of the proper image to a point.

**Solution.** The [two-arc descent calculation](../../analytic-boundaries-and-constructible-traces/src/local-systems-across-an-analytic-boundary.md#a-puncture-measures-monodromy-by-a-mapping-fibre) gives the actual monodromy complex $\operatorname{Cone}(T-1:k^r\to k^r)[-1]$. It has $H^0=\ker(T-1)$ and $H^1=\operatorname{coker}(T-1)$. Rank-nullity makes these two spaces have equal dimension, so the global index is zero for every $T$.

With an orientation of the circle, $\omega_{S^1}=k[1]$ and $H^0(S^1;\omega_{S^1})=H^1(S^1;k)=k$. Compact duality identifies this group with the dual of $H^0(S^1;k)=k$, and the trace is evaluation at the constant section $1$. Integration is therefore an isomorphism. Since the circle is compact, (25) gives integral zero, hence $C(L)=0$.

If $T-1$ is invertible, the monodromy complex is acyclic, so the proper image to a point is the zero derived object. Its support is empty, even though the image of the nonempty closed support of $L$ is the point. Theorem (23) compares its class in that larger image support by the natural enlargement map. The local Euler function is still the constant rank $r$; it is not the global Euler index, nor a degree-zero constant-coefficient description of the characteristic class.

### Locate the failure when the source support is noncompact

*Difficulty: Advanced.*

Let $Y=(0,1)$, $f:Y\to\{\mathrm{pt}\}$ and $G=k_Y$. Both ordinary and proper direct images are bounded finite complexes. Compute their indices and $H^0(Y;\omega_Y)$. Identify the precise support-forgetting step that prevents (22)–(23) from being applied. Compare extension by zero into the ambient line.

**Solution.** Ordinary sections give $S_fG=k$, while compact sections give $L_fG=k[-1]$. Their indices are $1$ and $-1$. The support of $G$ as an object on $Y$ is all of $Y$, which is noncompact; thus $f$ is not proper on that closed support.

With the increasing orientation, $\omega_Y=k_Y[1]$, and $H^0(Y;\omega_Y)=H^1((0,1);k)=0$. In particular the characteristic class $C(G)$ in its ordinary supported group for $Z=Y$ is zero. The construction of (22) would require $S_fR\Gamma_Z\omega_Y$ to be identified with $L_fR\Gamma_Z\omega_Y$. But $R\Gamma_Z\omega_Y=\omega_Y$, and these two images are $k[1]$ and $k$, respectively. Their support-forgetting comparison is not an isomorphism. We cannot invert it to send the ordinary class through the proper trace.

The bounded constructibility of both output objects does not repair this missing hypothesis. An unconditional image rule from the zero ordinary class would also be incompatible with the nonzero point class $C(L_fG)=-1_k$.

For the open inclusion $j:(0,1)\hookrightarrow\mathbb R$, the ambient extension $j_!G$ has compact closed support $[0,1]$, including its zero-stalk endpoints. Its supported characteristic class on the ambient line is the nonzero negative generator calculated above. Formula (25) now applies and gives the compact index $-1$. The two settings have different closed supports and different available supported-to-compact maps.

## From supported traces to cycle comparisons

Proper transport retains the closed image support while the identity, graph restriction and ordered contraction determine its map. For a compact source support, the same map becomes integration of the supported class and gives the finite coefficient index in (25). Relating this dualizing class to geometric cycles requires the further constructions in [subanalytic chains](subanalytic-chains-and-closed-cycle-supports.md), [the dualizing chain resolution](the-dualizing-resolution-by-subanalytic-chains.md), and [supported intersections](intersections-of-supported-subanalytic-cycles.md).

## Mathematical sources

M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985), §3.4 and Theorems 4.2–4.3, pp. 199–200, gives the microlocal characteristic-cycle index formulas with their support conditions. The supported characteristic-class transport proved here is organized around the graph, the two closed comparisons and the identity endomorphism. Its final scalar is computed directly on a finite coefficient complex.

P. Schapira, [*An Introduction to Sheaves on Grothendieck Topologies*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=95), edition dated 01/08/2026, Corollary 4.6.2, Propositions 4.6.5–4.6.8 and §4.7, pp. 95–98, treats exceptional composition, evaluated internal adjunction, closed support, diagonal Hom and the dualizing object. The linked programme proofs supply the required adjoint construction, product evaluation and support-forgetting compatibilities; the complete graph and trace calculations are given above. These mathematical sources retain their authorship and their own terms.
