# Proper characteristic classes and the compact index

The characteristic class of a constructible complex is obtained by evaluating its identity along the diagonal. Proper transport must preserve that entire map. The two closed-support comparisons place the identity inside a graph factorization; product evaluation and internal adjunction then identify its transported endomorphism. The resulting supported trace gives the Euler index when the target is a point.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 1 October 2026. New original text is public domain (CC0).*

This lesson proves the compact index formula through proper characteristic classes, the global form of the index theorem of M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985). Use Constructible traces and local Euler indices for the supported characteristic class and graded point trace, Closed supports and evaluated proper transport for the closed comparison, evaluated Hom and identity maps, and Perfect coefficients on compact fibres for proper constructible finiteness. The product evaluation, exceptional composition and Hom, base change, projection and support-forgetting comparisons are foundational inputs. We prove the index theorem relative to those maps; cotangent characteristic cycles are constructed in the following lessons.

## Properness is imposed on a closed support

Let $k$ be a commutative field of characteristic zero. Manifolds and maps are real analytic, with the standing finite uniform dimension bounds. Suppose

\[
 f:Y\longrightarrow X,\qquad G\in D^b_{\mathbb R\text{-c}}(k_Y),
 \qquad Z=\operatorname{supp}(G),\qquad f|_Z\text{ proper}.
 \qquad\text{(1)}
\]

The support $Z$ is closed, with the convention of the preceding lessons, and is subanalytic. Its image $S=f(Z)$ is closed because $f|_Z$ is proper. The proper perfect-image theorem and constructible duality give bounded constructible complexes

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

This is proper duality with its evaluated normalization. It contains the manifold orientation complexes; there is no extra dimension shift to append to (3).

For a constructible complex $B$ on a manifold $W$, abbreviate the pre-contraction part of its characteristic-class map by

\[
 h_B:R\mathcal Hom(B,B)
 \xrightarrow{\theta_B}\delta_W^!(B\boxtimes D_WB)
 \xrightarrow{\beta_{\delta_W}}B\otimes^LD_WB.
 \qquad\text{(4)}
\]

Contraction $\operatorname{tr}_B:B\otimes D_WB\to\omega_W$ is graded symmetry followed by dual-first evaluation. The identity unit followed by $\operatorname{tr}_Bh_B$ defines $C(B)$ with its closed support.

## Product maps provide the middle comparison

Put $A=G\boxtimes E$ on $Y\times Y$ and $K=P\boxtimes E$ on $X\times Y$. Use the graph maps

\[
 f_1=(f,\mathrm{id}_Y),\quad f_2=(\mathrm{id}_X,f),\quad
 \gamma(y)=(f(y),y).
 \qquad\text{(5)}
\]

The preceding lesson proves $f_1\delta_Y=\gamma$ with both embeddings closed, and the cartesian square with top $\gamma$, bottom $\delta_X$ and vertical maps $f,f_2$.

The map $f_1$ is proper on the support of $A$: that support lies in $Z\times Z$, inside the domain of the proper product $f|_Z\times\mathrm{id}_Y$. Similarly $f_2$ is proper on the support of $K$, which lies in $\operatorname{supp}(P)\times Z$. Thus support forgetting is an isomorphism on these product objects.

Projection formula and proper-support base change supply actual product isomorphisms

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

The map $c$ is the transpose of the closed-embedding counit through proper composition, exactly as in the preceding lesson. We first use it as a morphism.

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

In the first line, exceptional composition identifies $\delta_Y^!f_1^!K$ with $\gamma^!K$. In the second, ordinary diagonal restriction identifies $\delta_X^{-1}(P\boxtimes Q)$ with $P\otimes Q$.

**Middle restriction identity.** These maps satisfy

\[
 L_f\beta_{\delta_Y,A}
 =m\,\beta_{\delta_X,P\boxtimes Q}\,\alpha.
 \qquad\text{(9)}
\]

**Proof.** Apply the composite closed-comparison lemma to $\delta_Y,f_1,\gamma$ and $A$. Its exceptional unit is $U$. Since $\pi_{f_1,A}$ is an isomorphism, the composite path gives

\[
 L_f\beta_{\delta_Y,A}
 =L_f\psi\,L_f\beta_{\gamma,K}\,L_f(\delta_Y^!U).
 \qquad\text{(10)}
\]

The ordinary counit for $f_1$ restricts on the diagonal to $b_G\otimes1_E$: under (6), its first-factor counit is $f^{-1}S_fG\to G$ and the second factor is unchanged. This is the ordinary arrow in (10), not an exceptional-to-ordinary identification for $f$ itself.

The cartesian closed-comparison lemma, before support forgetting, gives

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

It first postcomposes with $u_G:G\to f^!P$, then applies the actual internal adjunction $S_fR\mathcal Hom(G,f^!P)\simeq R\mathcal Hom(P,P)$. Its identity-square proof in the preceding lesson shows that $k_X\to S_fk_Y\to S_fR\mathcal Hom(G,G)\xrightarrow{\rho}R\mathcal Hom(P,P)$ is the identity unit of $P$.

**Hom identification of the middle map.** With proper and ordinary images identified on the supported endomorphism object,

\[
 \alpha\,L_f\theta_G=\theta_P\,\rho.
 \qquad\text{(12)}
\]

**Proof.** Denote by $p_Y,p_X$ the projections from $W=X\times Y$. Current product evaluation with its constructible second factor gives

\[
 K=P\boxtimes E\simeq
 R\mathcal Hom(p_Y^{-1}G,p_X^!P).
 \qquad\text{(13)}
\]

Exceptional-Hom restriction and composition then give

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

We next check the remaining part of $\alpha$. The object $\gamma^!K$ is supported on $Z$, by (14), and $f_2$ is proper on the support of $K$. Therefore the support-forgetting comparisons identify $c$ with the ordinary exceptional base-change isomorphism $S_f\gamma^!K\simeq\delta_X^!S_{f_2}K$. The current exceptional/proper-to-ordinary compatibility fixes this identification: both are transposes of the same closed-embedding counit. There is no arbitrary choice of the isomorphism $c$ in this supported situation.

After using (13), internal adjunction for $f_2$ identifies $S_{f_2}K$ with

\[
 R\mathcal Hom(q_2^{-1}P,q_1^!P),
\]

where $q_1,q_2$ are the projections of $X\times X$. Here $L_{f_2}p_Y^{-1}G=q_2^{-1}P$ by proper-support base change, and $f_2^!q_1^!P=p_X^!P$ by exceptional composition. The product evaluation for $P$ identifies this Hom object with $P\boxtimes Q$.

This latter identification agrees with $\sigma_2$ in (6). Curry both product maps against $q_2^{-1}P$. Pulling the independent first factor through projection formula leaves, in both cases, the same pairing $G\otimes E\to\omega_Y$ followed by the trace $L_f\omega_Y\to\omega_X$, which defines (3). The ordered product evaluations use the same graded permutations. The evaluated internal-adjunction and normalized projection comparisons thus give the same map, not just isomorphic objects.

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

There are two ways to compare such an evaluated pairing with internal adjunction. The usual evaluated-Hom square uses the ordinary counit on $E$ after projection on $G$. Formula (17) uses the counit on $G$ after projection on $E$. The current support-forgetting evaluation identity asserts

\[
 R\mathcal Hom(\pi_{f,G},\omega_X)\,u_E
 =v_E\,\pi_{f,E},
 \qquad\text{(18)}
\]

where $v_E:S_fE\simeq R\mathcal Hom(L_fG,\omega_X)$ is internal adjunction and $u_E:L_fE\to R\mathcal Hom(S_fG,\omega_X)$ is the curry of the second pairing. Its proof curries both paths, evaluates the same two properly supported sections, and then applies the same trace; support lies in their intersection. The flat/soft resolution maps and Koszul symmetries are the same on both paths.

Both support-forgetting maps in (18) are isomorphisms under (1). Consequently, evaluating (18) in the $P$-before-$Q$ order gives

\[
 t_{\omega_X}\,L_f\operatorname{tr}_G\,m
 =\operatorname{tr}_P.
 \qquad\text{(19)}
\]

This proves the last trace square for the actual $m$ used in (16). In particular, a bare projection pairing is not incorrectly declared invertible, and the two evaluation orders are compared with their graded signs. One may also verify (19) directly in the evaluated resolution model; (18) records precisely the needed compatibility.

The identity-square proof, (12), (9) and (19) now give all four parts of Proposition 9.1.3. Combining (16) with (19), the whole evaluated endomorphism map satisfies

\[
 t_{\omega_X}\,L_f(\operatorname{tr}_Gh_G)
 =\operatorname{tr}_Ph_P\,\rho.
 \qquad\text{(20)}
\]

The top constant-sheaf term remains $S_fk_Y$, with unit $k_X\to S_fk_Y$. Nothing in this proof asserts that $f$ is proper on the support of $k_Y$.

## The supported trace transports the characteristic class

Set $T_Z=R\Gamma_Z\omega_Y$. This is supported on $Z$ and is constructible by the closed subanalytic support operation. Properness on $Z$ identifies $S_fT_Z$ with $L_fT_Z$. Since the latter is supported on the closed set $S=f(Z)$, the trace has a unique supported lift

\[
 L_fT_Z\longrightarrow R\Gamma_S\omega_X
 \qquad\text{(21)}
\]

of $L_fT_Z\to L_f\omega_Y\xrightarrow{t_{\omega_X}}\omega_X$. The uniqueness uses its supported source, as in the characteristic-class construction. Applying global sections, with the proper-to-ordinary comparison on $T_Z$, gives

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

On global sections, the unit $k_X\to S_fk_Y$ sends $1_X$ to $1_Y$. The identity-square proof says that applying $S_fe_G$ and then $\rho$ sends that unit to $e_P$. The definition of $C(G)$ factors the other path through $T_Z$. Properness on $Z$ is exactly what allows its ordinary global sections to pass through $L_fT_Z$ in (21). Applying the supported equality to this unit gives (23). $\square$

This argument also fixes the support-image map, rather than introducing an unspecified pushforward on cohomology groups. The image $S$ can be larger than the output support, and the target comparison remains the natural enlargement of a closed support condition.

## Compact support gives an integer index

Let $F\in D^b_{\mathbb R\text{-c}}(k_X)$ have compact closed support $Z$, and let $a:X\to\{\mathrm{pt}\}$. The map is proper on $Z$, so (23) applies. Compact constructible finiteness and the actual comparison give

\[
 P=Ra_!F=R\Gamma_c(X;F)\simeq R\Gamma(X;F).
\]

The point trace theorem gives $C(P)=\chi(X;F)1_k$. The trace $Ra_!\omega_X\to k$ defines integration on **compactly supported** cohomology,

\[
 \int_X:H_c^0(X;\omega_X)\longrightarrow k.
 \qquad\text{(24)}
\]

Since $Z$ is compact, the supported class maps naturally from $H_Z^0(X;\omega_X)$ into this compactly supported group. The special case of (22) for $a$ is exactly that map followed by (24). Thus

\[
 \int_X C(F)=\chi(X;F)1_k.
 \qquad\text{(25)}
\]

This proves (9.1.14) with its support and trace normalization. An ordinary group $H^0(X;\omega_X)$ need not admit this integration when $X$ is noncompact. Even a class supported on a compact set can vanish after it is mapped to ordinary cohomology, while its integral remains nonzero. Characteristic zero lets the resulting field element recover the integer index; in positive characteristic it would record only its reduction.

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

For the open rectangle $U=(0,1)\times(-1,1)$, open internal duality gives $Dk_U=Rj_*k_U[2]$. Small neighborhoods intersect $U$ in convex sets, including at corners, so the actual constant-section maps identify $Rj_*k_U$ with the closed-rectangle constant sheaf. Constructible biduality therefore gives $E=D_YG=k_U[2]$. On the real-line target, the same interval duality gives $Q=k_{(0,1)}[1]$.

Compact cohomology of the open $y$-interval is $k[-1]$. Projection formula and proper-support base change consequently give $L_fE=k_{(0,1)}[2-1]=k_{(0,1)}[1]=Q$, matching the actual proper-duality map (3). The real dimensions two and one have already supplied all shifts.

The transported class is $C(P)$ supported in $[0,1]$; its integral is $1$. The source closed rectangle is contractible and compact, so its global index is also $1$. For $G[r]$, the section complex is $k[r]$ and the index is $(-1)^r$. Its transported object is $P[r]$, with the same integral by (25). No Jacobian factor or additional fibre shift is inserted into the characteristic class.

### A circle can have a nonzero local rank and zero characteristic class

*Difficulty: Intermediate.*

Let $L$ be a rank-$r$ local system on a circle, with $r>0$ and monodromy $T\in\operatorname{GL}_r(k)$. Compute its global Euler index and its characteristic class in $H^0(S^1;\omega_{S^1})$. Explain the case where $T-1$ is invertible, including the support of the proper image to a point.

**Solution.** Two arcs and their two overlap components give the actual monodromy complex $\operatorname{Cone}(T-1:k^r\to k^r)[-1]$. It has $H^0=\ker(T-1)$ and $H^1=\operatorname{coker}(T-1)$. Rank-nullity makes these two spaces have equal dimension, so the global index is zero for every $T$.

With an orientation of the circle, $\omega_{S^1}=k[1]$ and $H^0(S^1;\omega_{S^1})=H^1(S^1;k)=k$. Compact duality identifies this group with the dual of $H^0(S^1;k)=k$, and the trace is evaluation at the constant section $1$. Integration is therefore an isomorphism. Since the circle is compact, (25) gives integral zero, hence $C(L)=0$.

If $T-1$ is invertible, the monodromy complex is acyclic, so the proper image to a point is the zero derived object. Its support is empty, even though the image of the nonempty closed support of $L$ is the point. Theorem (23) compares its class in that larger image support by the natural enlargement map. The local Euler function is still the constant rank $r$; it is not the global Euler index, nor a degree-zero constant-coefficient description of the characteristic class.

### Locate the failure when the source support is noncompact

*Difficulty: Advanced.*

Let $Y=(0,1)$, $f:Y\to\{\mathrm{pt}\}$ and $G=k_Y$. Both ordinary and proper direct images are bounded finite complexes. Compute their indices and $H^0(Y;\omega_Y)$. Identify the precise support-forgetting step that prevents (22)–(23) from being applied. Compare extension by zero into the ambient line.

**Solution.** Ordinary sections give $S_fG=k$, while compact sections give $L_fG=k[-1]$. Their indices are $1$ and $-1$. The support of $G$ as an object on $Y$ is all of $Y$, which is noncompact; thus $f$ is not proper on that closed support.

With the increasing orientation, $\omega_Y=k_Y[1]$, and $H^0(Y;\omega_Y)=H^1((0,1);k)=0$. In particular the characteristic class $C(G)$ in its ordinary supported group for $Z=Y$ is zero. The construction of (22) would require $S_fR\Gamma_Z\omega_Y$ to be identified with $L_fR\Gamma_Z\omega_Y$. But $R\Gamma_Z\omega_Y=\omega_Y$, and these two images are $k[1]$ and $k$, respectively. Their support-forgetting comparison is not an isomorphism. We cannot invert it to send the ordinary class through the proper trace.

The bounded constructibility of both output objects does not repair this missing hypothesis. An unconditional image rule from the zero ordinary class would also be incompatible with the nonzero point class $C(L_fG)=-1_k$.

For the open inclusion $j:(0,1)\hookrightarrow\mathbb R$, the ambient extension $j_!G$ has compact closed support $[0,1]$, including its zero-stalk endpoints. Its supported characteristic class on the ambient line is the nonzero negative generator calculated above. Formula (25) now applies and gives the compact index $-1$. The two settings have different closed supports and different available supported-to-compact maps.

## What has now been proved

The full proper trace diagram is established through its identity, Hom, closed-restriction and evaluated-tensor maps. The supported trace transports the characteristic class under properness on the closed support, and compact support gives the integer Euler index through (25). These results do not identify the class with a cotangent cycle or supply a cycle intersection formula. The lessons on subanalytic chains, the dualizing chain resolution, and supported intersections develop the cycle constructions needed for those further comparisons.
