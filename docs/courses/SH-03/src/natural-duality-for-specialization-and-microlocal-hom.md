# Natural duality for specialization and microlocal Hom

Specialization commutes with Verdier duality through a boundary connecting map. Microlocalization adds a Fourier transform, so its duality comparison also reverses the normal covector and retains the relative orientation complex. For microlocal Hom, exchanging the two manifold factors explains both the order of the dual inputs and the cancellation of one antipode.

The proof starts with the positive-parameter boundary map. We combine it with actual constructible biduality and the perfect inverse-image and tensor operations. The Fourier step uses the comparison with a variable test complex on the base, whose two exceptional adjunction maps we identify below. The specialization and microlocal-Hom constructibility proof supplies bounded constructible outputs.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

## Hypotheses and the four comparisons

Let \(k\) be commutative of finite global dimension. Manifolds and maps are real analytic, finite dimensional with uniform dimension bounds, Hausdorff and countable at infinity. All inputs are globally bounded and \(\mathbb R\)-constructible. Here constructibility includes perfect stalk complexes: locally each such coefficient complex has a bounded finite-projective representative. This is the perfect-coefficient convention, and does not replace perfection by finite generation over an arbitrary ring. No field, Noetherianity, compactness or global orientation is assumed.

Let \(M\) be an analytic embedded submanifold of \(X\), closed in the ambient neighborhood in use. Put \(E=T_MX\), \(E^*=T_M^*X\), and let \(\pi:E^*\to M\) be the projection. If the normal rank is \(c\), then

\[
\omega_{M/X}=\operatorname{or}_{M/X}[-c].
\qquad\text{(1)}
\]

This is a complex on \(M\), not a globally chosen trivialization. Write \(a\) for fibrewise negation on the conormal bundle or on \(T^*X\), as appropriate. Since \(a\) is an involutive diffeomorphism, \(a^{-1}\) and its direct image give canonically equivalent antipodal transport. We use inverse-image notation.

**Theorem.** The following are natural isomorphisms:

\[
\nu_M(D_XF)\simeq D_E(\nu_MF),
\qquad\text{(2)}
\]
\[
\mu_M(D_XF)\simeq
a^{-1}D_{E^*}(\mu_MF)\otimes\pi^{-1}\omega_{M/X},
\qquad\text{(3)}
\]
\[
\mu\operatorname{hom}(F,G)\simeq
a^{-1}\mu\operatorname{hom}(D_XG,D_XF),
\qquad\text{(4)}
\]
\[
D_{T^*X}\bigl(\mu\operatorname{hom}(F,G)\bigr)
\simeq\mu\operatorname{hom}(G,F)\otimes\pi_X^{-1}\omega_X.
\qquad\text{(5)}
\]

Here \(\pi_X:T^*X\to X\). In (4) the two inputs are swapped and dualized. In (5) they are swapped and the base dualizing complex is pulled back. The proof will identify every antipode and shift through actual maps.

## The deformation connecting map

Use the normal deformation \(D=\widetilde X_M\), its positive chamber \(\Omega=\{t>0\}\), and maps

\[
r:\Omega\to X,\qquad j:\Omega\hookrightarrow D,
\qquad s:E\hookrightarrow D.
\qquad\text{(6)}
\]

The whole analytic map \(p:D\to X\) has local formula \(p(v,z,t)=(tv,z)\); \(r=p|_\Omega\). The chamber is canonically \(X\times\mathbb R_{>0}\). The increasing positive parameter fixes
\(r^!F\simeq r^{-1}F[1]\).

Let \(H=r^{-1}F\). Open-complement localization of its open extension gives

\[
R\Gamma_{D\setminus\Omega}(j_!H)
\longrightarrow j_!H\longrightarrow Rj_*H\xrightarrow{+1}.
\qquad\text{(7)}
\]

The first term vanishes on \(\Omega\) and on the open negative chamber. Its support lies in \(E\), so it is \(s_*s^!j_!H\). Ordinary inverse image by \(s\) kills the middle term. The connecting arrow in (7) consequently gives

\[
s^{-1}Rj_*r^{-1}F
\xrightarrow{\sim}s^!j_!r^{-1}F[1]
\xrightarrow{\sim}s^!j_!r^!F.
\qquad\text{(8)}
\]

Denote this composite by \(\delta_F:\nu_MF\to s^!j_!r^!F\). Its sign is the one in the boundary comparison: first use the connecting arrow of (7), then the inverse of the oriented identification \(r^!F\simeq r^{-1}F[1]\). To make the connecting convention explicit, for a cochain map \(u:U^\bullet\to V^\bullet\) use

\[
\operatorname{Cone}(u)^q=V^q\oplus U^{q+1},\qquad
d(v,u')=(d_Vv+u(u'),-d_Uu').
\]

The localization fibre is \(\operatorname{Cone}(u)[-1]\); the last arrow of its triangle sends \(v\) to \((v,0)\) in \(\operatorname{Cone}(u)\). Applied to (7) and then restricted to \(E\), the middle complex is zero, so this very inclusion is the isomorphism in the first part of (8). No extra minus sign is inserted after rotating the triangle. For the one-dimensional parameter test with constant coefficient, the boundary stalk of the open extension is zero and the positive-side ordinary section complex is \(k\). The same cone therefore has the generator \((1,0)\) in degree zero after the shift; equivalently the unshifted boundary costalk is \(k[-1]\).

The remaining orientation identification is normalized by integration on an increasing interval, whose trace on \(R\Gamma_c(I;k[1])\) is \(+1\). We use that identification, with its specified tensor order, in the second part of (8). The cone convention and the positive-interval trace together specify \(\delta_F\), including its sign; an arbitrary isomorphism with the same source and target would not do so. Localization, oriented submersion comparison and their traces commute with open restriction. Thus \(\delta_F\) is natural in \(F\) and agrees on overlapping adapted charts. The left side of (8) is the definition of \(\nu_MF\).

The constructibility assertion needed here concerns \(A=j_!r^!F\) on the whole deformation, including its boundary. Put \(H_0=p^{-1}F\). The map \(p(v,z,t)=(tv,z)\) is analytic also at \(t=0\), so perfect inverse image makes \(H_0\) constructible. The chamber \(\Omega=\{t>0\}\) is open subanalytic. A compatible subanalytic stratification makes \(k_\Omega\) constant with coefficient \(k\) on its included strata and zero on all other strata; both coefficients are perfect. The subanalytic cutoff argument therefore applies. Open extension and the oriented submersion comparison give the actual identification

\[
A=j_!r^!F\simeq j_!j^{-1}H_0[1]
\simeq(k_\Omega\otimes^L H_0)[1].
\]

The last map is open-extension tensor comparison: its restriction to \(\Omega\) is the identity of \(H_0\), and both sides have zero ordinary stalk on the complement. Since \(k_\Omega\) has flat stalks \(k\) or zero, this comparison also gives the derived tensor identification. Tensor closure proves constructibility of \(A\); its global bounds are those of \(F\), shifted by \([1]\). Perfect exceptional inverse image then makes \(s^!A\) constructible and bounded. These assertions use no properness of \(j\), and do not claim that an arbitrary sheaf given only on \(\Omega\) has a constructible extension across its boundary. The ambient analytic object \(H_0\) is the extension used in this argument.

## Specialization duality through that map

For constructible \(B\) and an analytic map \(f:Y\to X\), exceptional duality and actual biduality give the natural pair

\[
f^!D_XB\simeq D_Y(f^{-1}B),\qquad
f^{-1}D_XB\simeq D_Y(f^!B).
\qquad\text{(9)}
\]

Write \(\alpha_B:f^!D_XB\to D_Y(f^{-1}B)\) for the first map. It is exceptional internal Hom, EX.26, applied to \((B,\omega_X)\), followed by the composition identification \(f^!\omega_X=\omega_Y\). More explicitly, its transpose is obtained from the projection formula, the exceptional counit and evaluation:

\[
Rf_!\bigl(f^!D_XB\otimes^L f^{-1}B\bigr)
\simeq Rf_!f^!D_XB\otimes^L B
\longrightarrow D_XB\otimes^L B
\longrightarrow\omega_X.
\]

Tensor–Hom and exceptional adjunction give \(\alpha_B\). This proof needs a bounded first Hom input and the bounded-below dualizing target; it does not use a stalkwise Hom substitution.

The second map can be specified without an unnamed inverse-image/Hom interchange. Let \(\eta_C:C\to D D C\) denote the actual evaluation and set \(L=f^{-1}D_XB\). It is the composite

\[
\begin{aligned}
L&\xrightarrow{\eta_L}D_YD_YL
\xrightarrow{D_Y(\alpha_{D_XB})}
D_Y\bigl(f^!D_XD_XB\bigr)
\xrightarrow{D_Y(f^!\eta_B)}D_Y(f^!B).
\end{aligned}
\]

The evaluation theorem makes \(\eta_B\) invertible. It also makes \(\eta_L\) invertible, because constructible duality and perfect ordinary inverse image make \(L\) constructible. Exceptional inverse image is constructible by the same perfect-operation theorem. Thus every arrow has its claimed range and is an isomorphism. This proves the second comparison in (9), with its map and variance fixed. Perfection is used at the two evaluations; (9) is not an inverse-image/internal-Hom assertion for arbitrary weak coefficients.

For bounded \(L\) on \(\Omega\), direct-image internal adjunction, EX.20–EX.22, with \(f=j\) and target \(\omega_D\), identifies
\(D_D(j_!L)\simeq Rj_*D_\Omega L\).
Here \(j^!\omega_D=\omega_\Omega\), since \(j\) is open. The map from right to left is adjoint to evaluation followed by the open-extension counit \(j_!j^!\omega_D\to\omega_D\). This is ordinary direct image on the dual side, with no claim that \(j\) is proper. Apply the second comparison in (9) first to \(r\) with input \(F\), and then to \(s\) with input \(A=j_!r^!F\). Together with the boundary map they give the chain

\[
\begin{aligned}
\nu_M(D_XF)
&=s^{-1}Rj_*r^{-1}D_XF\\
&\simeq s^{-1}D_D(j_!r^!F)\\
&\simeq D_E(s^!j_!r^!F)\\
&\simeq D_E(\nu_MF).
\end{aligned}
\qquad\text{(10)}
\]

The last arrow is exactly \(D_E(\delta_F)\), from \(D_E(s^!j_!r^!F)\) to \(D_E(\nu_MF)\), since Verdier duality reverses the boundary map's direction. The earlier arrows are the just-defined second comparison in (9) for \(r\), open-extension duality, and the second comparison in (9) for \(s\), in that order. All inputs have been checked constructible before either evaluation is inverted. The composition proves (2) naturally in \(F\). Its parameter degree is fixed already in (8): the connecting map contributes the shift of the boundary fibre and the increasing-parameter formula identifies that shifted fibre with \(s^!j_!r^!F\). No further parameter shift or separately chosen sign is introduced while dualizing.

For a locally closed \(M\), restrict to ambient open neighborhoods where it is closed. The boundary construction, the exceptional composition maps and evaluation all commute with open restriction, so the comparisons agree and glue. In rank zero \(M\) is open in \(X\), and the local deformation is \(M\times\mathbb R\). The same positive-parameter boundary map identifies specialization with \(F|_M\); when the ambient space is \(M\), this is the identity functor. Thus the rank-zero case retains the restriction required by its domain.

## Fourier duality supplies the antipode and relative complex

For a rank-\(c\) bundle \(E\to M\), let \(O\) be its fibre orientation line on \(M\), and set \(W=O[c]\). Positive dual bases identify the fibre orientations of \(E\) and \(E^*\), with \(O\otimes O\simeq k_M\).

Use \(\tau:E\to M\) and \(\pi:E^*\to M\). On \(Z=E\times_M E^*\), write \(u:Z\to E\), \(v:Z\to E^*\), and \(\rho=\tau u=\pi v\), and put \(N_- =\{\langle e,\eta\rangle\leq0\}\). The three-transform convention is

\[
T_EB=Rv_!(k_{N_-}\otimes^L u^{-1}B),\qquad
I_EC=Rv_*R\mathcal Hom(k_{N_-},u^!C).
\]

Both functors go from conic complexes on \(E\) to conic complexes on \(E^*\). The second is \(S_{E^*}\) with the product factors exchanged; \(S_E\) instead has domain \(E^*\) and codomain \(E\). The distinction between tensor cutoff and sections with support is part of these definitions. With these domains, the full variable-test comparison, FDN8, reads

\[
I_E R\mathcal Hom(B,\tau^!Q)
\xrightarrow{\sim}
R\mathcal Hom(T_EB,\pi^!Q)
\qquad\text{(11)}
\]

for \(B\in D^b_{\mathbb R_{>0}}(k_E)\) and \(Q\in D^+(k_M)\). Both sides lie in the conic bounded-below category on \(E^*\). To see the precise comparison, set \(V_Q=\pi^!Q\). The two exceptional internal-Hom adjunctions, FDN3–FDN4, give

\[
\begin{aligned}
I_E R\mathcal Hom(B,\tau^!Q)
&=Rv_*R\mathcal Hom\bigl(k_{N_-},u^!R\mathcal Hom(B,\tau^!Q)\bigr)\\
&\simeq Rv_*R\mathcal Hom\bigl(k_{N_-},
 R\mathcal Hom(u^{-1}B,u^!\tau^!Q)\bigr)\\
&\simeq Rv_*R\mathcal Hom\bigl(k_{N_-}\otimes^L u^{-1}B,v^!V_Q\bigr)\\
&\simeq R\mathcal Hom\bigl(Rv_!(k_{N_-}\otimes^L u^{-1}B),V_Q\bigr).
\end{aligned}
\]

The middle step uses \(u^!\tau^!Q\simeq\rho^!Q\simeq v^!\pi^!Q\), with the exceptional composition comparison, and then curries the two Hom inputs. The final arrow is the adjoint of evaluation followed by the proper-support counit for \(v\); the first arrow is the exceptional-Hom mate specified in FDN3. These operations fix (11), rather than choosing an isomorphism after computing its two objects. Derived permutations use the Koszul symmetry. The construction is contravariant in \(B\), covariant in \(Q\), and respects open restriction on \(M\).

The bounds also have to match. If \(B\in D^{[a,b]}\) and \(Q\in D^{\geq q}\), the submersion formula puts \(\tau^!Q\) in \(D^{\geq q-c}\). Thus the first Hom has lower bound \(q-c-b\). The flat cutoff \(k_{N_-}\) leaves the bounds of \(u^{-1}B\) unchanged, and the rank-\(c\) proper-support projection puts \(T_EB\) in \(D^{[a,b+c]}\). The target of (11) has lower bound \(q-b-2c\). The bounded-below projection argument proves the adjunction calculations throughout this range by truncating the test complex in each fixed degree. Conic internal Hom and the transform give conicity. No upper bound for the two Hom objects is required in the general statement, and no perfection, finite generation or coefficient biduality is used there.

The finite-dimensional manifold \(M\) has the uniform finite compact-support cohomological dimension required in absolute Fourier duality, FDN13–FDN14. The dimension condition concerns all abelian sheaves, not only the chosen coefficient complex, and requires no compact base. Take \(Q=\omega_M\), a bounded orientation complex under our dimension bounds. Exceptional composition supplies \(\tau^!\omega_M=\omega_E\) and \(\pi^!\omega_M=\omega_{E^*}\); hence (11) becomes \(I_ED_EB\simeq D_{E^*}T_EB\), with exactly its preceding evaluation-and-trace map. The signed halfspace comparison identifies

\[
I_EB\simeq a^{-1}T_EB\otimes\pi^{-1}O[c].
\qquad\text{(12)}
\]

Here is the support comparison behind (12). Put \(N_+=\{\langle e,\eta\rangle\geq0\}\). Apply FS4, with its comparison maps FS5–FS6, to the exchanged bundle. It gives

\[
Rv_*R\Gamma_{N_-}(u^!C)
\simeq Rv_!\bigl((u^!C)\otimes k_{N_+}\bigr).
\]

This changes both the inequality and the operation on the halfspace. The proof passes through a kernel supported on the first-coordinate zero section, where the projection is proper, and uses the ordinary and proper-support radial contraction maps. It does not assert properness of \(v\) on the whole halfspace. The submersion comparison is \(u^!C=u^{-1}C\otimes\rho^{-1}O[c]\), since the fibre of \(u\) is \(E^*\) with its positive dual orientation. The map \((e,\eta)\mapsto(e,-\eta)\) exchanges \(N_+\) and \(N_-\), lies over \(a\) on \(E^*\), and fixes \(u^{-1}C\). Diffeomorphism base change and projection formula therefore give (12), with its base-pulled factor \(\pi^{-1}O[c]\). It is the comparison of these specified kernels; no separate normalization of a Fourier inverse unit is substituted. Solve (11)–(12) for \(T_ED_EB\):

\[
T_ED_EB\simeq a^{-1}D_{E^*}T_EB
\otimes\pi^{-1}O[-c].
\qquad\text{(13)}
\]

To track the inverse orientation factor, (11) and (12), applied to \(D_EB\), first give

\[
a^{-1}T_ED_EB\otimes\pi^{-1}W
\simeq D_{E^*}T_EB.
\]

Pull back by \(a\). Since \(a^2=1\) and \(\pi a=\pi\), this gives \(T_ED_EB\otimes\pi^{-1}W\simeq a^{-1}D_{E^*}T_EB\). Tensor on the right by \(\pi^{-1}W^{-1}\) and use the ordered evaluation \(W\otimes W^{-1}\to k_M\). This is precisely (13); it is the inverse complex \(W^{-1}=O[-c]\) that remains. The sign local system is self-dual via its canonical pairing, but reversing its shift is still necessary. No permutation of the two shifted factors is made without its Koszul symmetry.

For the normal bundle, the tangent exact sequence \(0\to TM\to TX|_M\to E\to0\) identifies its fibre orientation line \(O\) with \(\operatorname{or}_{M/X}\). The relative dualizing formula M16–M19 identifies its inverse complex \(O[-c]\) with \(\omega_{M/X}\), with the same ordered orientation evaluation. This identification retains the line's monodromy on a nonorientable normal bundle.

Finally take \(B=\nu_MF\). The specialization proof makes \(B\) bounded, constructible and conic; Fourier perfection keeps its transform bounded and constructible. Constructible Verdier duality supplies the same bounds for \(D_EB\), so (12) applies to it as well. Compose \(T_E\) of (10) with (13) and use \(\mu_MF=T_E\nu_MF\). This proves (3) through the specified natural maps. In rank zero the antipode is the identity and the relative orientation complex is \(k_M\); the conclusion reduces to ordinary duality of restriction to the open submanifold \(M\), as in the preceding rank-zero specialization check.

## Factor exchange reverses the dual inputs

On \(X^2\), with projections \(q_1,q_2\), define

\[
K_{F,G}=R\mathcal Hom(q_2^{-1}F,q_1^!G),
\qquad\mu\operatorname{hom}(F,G)=\mu_{\Delta_X}K_{F,G}.
\qquad\text{(14)}
\]

The two inputs of this kernel are constructible by perfect inverse-image and internal-Hom closure. We specify the internal reversal used below. On a manifold \(Y\), put \(D=D_Y\). For constructible \(A,B\), substitute the actual bidual evaluation \(\eta_B:B\to DDB\), then curry with the tensor symmetry:

\[
R\mathcal Hom(A,B)
\xrightarrow{\eta_B}
R\mathcal Hom(A,R\mathcal Hom(DB,\omega_Y))
\simeq R\mathcal Hom(DB,R\mathcal Hom(A,\omega_Y)).
\]

This is the reversal map to \(R\mathcal Hom(DB,DA)\). Its transpose evaluates \(R\mathcal Hom(A,B)\) on \(A\), then evaluates \(DB\) on the resulting \(B\), with the Koszul symmetry placing those factors next to one another. The first arrow is invertible by constructible biduality and the second by tensor–Hom adjunction. Thus this proves an isomorphism of internal-Hom sheaves, natural in both variables, without substituting Hom of ordinary stalks. Take \(Y=X^2\), \(A=q_2^{-1}F\), \(B=q_1^!G\). Formula (9), whose exceptional comparison is the evaluated map (EX.26), now gives

\[
\begin{aligned}
K_{F,G}
&\simeq R\mathcal Hom(D_{X^2}q_1^!G,D_{X^2}q_2^{-1}F)\\
&\simeq R\mathcal Hom(q_1^{-1}D_XG,q_2^!D_XF)\\
&=\sigma^{-1}K_{D_XG,D_XF},
\end{aligned}
\qquad\text{(15)}
\]

where \(\sigma(x_1,x_2)=(x_2,x_1)\). Its map on the diagonal conormal sends
\((x,x;\xi,-\xi)\) to \((x,x;-\xi,\xi)\).
Under our identification with \(T^*X\), \((\xi,-\xi)\mapsto\xi\), this is exactly \(a\).

The action on the functor can be checked on the deformation itself. In a coordinate chart write \(x_1=z+tu\), \(x_2=z\). The lift of \(\sigma\) is

\[
\widetilde\sigma(u,z,t)=(-u,z+tu,t).
\]

It squares to the identity, preserves the positive chamber, and restricts at \(t=0\) to \(h(u,z)=(-u,z)\). These coordinate maps are the maps induced by the same exchange of the original pair, so they agree on overlaps. The parameter is unchanged, including its increasing orientation. Apply inverse image under this diffeomorphism to \(s^{-1}Rj_*r^{-1}K\). The cartesian central and chamber squares, and ordinary base change for a diffeomorphism, give the actual natural comparison
\(\nu_\Delta(\sigma^{-1}K)\simeq h^{-1}\nu_\Delta K\). It is the invertible instance of the specialization inverse map, with no exceptional shift.

On the normal bundle, the transpose of \(h=-1\) is conormal negation \(a\). The Fourier kernel map (FF4–FF6) gives \(T_Eh^{-1}\simeq a^{-1}T_E\): here \(Rh_!=h^{-1}\) since \(h\) is an involutive homeomorphism. Equivalently, the change \((u,\xi)\mapsto(-u,-\xi)\) preserves the incidence inequality, and proper-support base change gives the same map. This includes the induced action on compact orientation classes; it does not replace that action by a chosen unsigned scalar. Composing these two comparisons proves

\[
\mu_{\Delta_X}(\sigma^{-1}K)
\simeq a^{-1}\mu_{\Delta_X}K.
\qquad\text{(16)}
\]

Applying (16) to (15) proves (4). Pullback composition for \(\widetilde\sigma\), and the composition compatibility proved after (FF6), identify two successive exchanges with the identity comparison. Thus the antipodal involution used here is coherent at the level of maps, including on the zero section; it is not merely an equality of supports. The defining kernel retains its exceptional projection throughout.

## The cotangent dual has one base dualizing factor

There is a specific external evaluation map \(G\boxtimes D_XF\to K_{F,G}\). Its transpose is

\[
\begin{aligned}
(q_1^{-1}G\otimes q_2^{-1}D_XF)\otimes q_2^{-1}F
&\longrightarrow q_1^{-1}G\otimes q_2^{-1}\omega_X\\
&\xrightarrow{\sim}q_1^!G.
\end{aligned}
\]

The first arrow pulls back the Verdier evaluation \(D_XF\otimes F\to\omega_X\); the second is the smooth projection comparison, with the second-factor orientation complex. Currying gives the claimed map. The following argument proves it invertible, so its inverse gives the displayed identification

\[
K_{F,G}\simeq G\boxtimes D_XF.
\qquad\text{(17)}
\]

Here is the rectangle check, in the factor order of (14). Exceptional adjunction and proper-support base change identify the sections of the kernel on \(U\times V\) with

\[
R\Gamma(U\times V;K_{F,G})
\simeq R\operatorname{Hom}_k
\bigl(R\Gamma_c(V;F),R\Gamma(U;G)\bigr).
\]

Restriction in \(V\) is precomposition with extension of compact supports; restriction in \(U\) acts on the second argument. At \(y\), the actual small-ball compact-section system of \(F\) is represented by the perfect costalk \(C_y=i_y^!F\). Its dual represents \((D_XF)_y\). After inserting this fixed perfect representative, a bounded finite-projective model gives \(R\operatorname{Hom}_k(C_y,-)=C_y^\vee\otimes^L-\), which commutes with the filtered passage \(U\to x\). The stalk comparison is therefore the finite-projective evaluation
\(G_x\otimes C_y^\vee\to R\operatorname{Hom}_k(C_y,G_x)\), with the same tensor symmetry as the displayed transpose. It is invertible. Stalkwise detection proves the actual external map an isomorphism. This is the rectangle proof (25)–(26), with the factors interchanged, using the costalk dual pairing (5)–(7). Perfection is used on the represented compact-section complex before Hom is passed to a stalk; no general Hom-of-stalks rule is invoked. The argument even allows an arbitrary bounded \(G\), although both inputs here are constructible.

We calculate the dual kernel with the same bidual map, rather than assuming an external-dual formula. Put \(P=D_{X^2}q_1^!G\otimes q_2^{-1}F\). Insert \(\eta_{q_1^!G}\) in the target of (14), curry, and use the Koszul symmetry to put the factors in the stated order. This gives the natural isomorphism \(c:K_{F,G}\xrightarrow{\sim}D_{X^2}P\). Constructible duality, inverse-image closure and tensor closure make \(P\) constructible. Consequently the composite

\[
D_{X^2}K_{F,G}
\xrightarrow{(D_{X^2}c)^{-1}}D_{X^2}D_{X^2}P
\xrightarrow{\eta_P^{-1}}P
\]

is defined and invertible. Formula (9) identifies \(D_{X^2}q_1^!G\) with \(q_1^{-1}D_XG\). This proves the actual comparison

\[
D_{X^2}K_{F,G}\simeq
q_1^{-1}D_XG\otimes q_2^{-1}F
=D_XG\boxtimes F.
\qquad\text{(18)}
\]

Apply (3) with ambient space \(X^2\), submanifold \(\Delta_X\), and constructible input \(K\). Pull its comparison back by \(a\). Since the relative complex is pulled back from the diagonal, that inverse image leaves it unchanged, and \(a^{-1}a^{-1}\) is the identity. Tensor on the right by its tensor inverse, evaluating the adjacent relative factors. Solving the resulting actual comparison gives

\[
D_{T^*X}\mu_{\Delta_X}K
\simeq a^{-1}\mu_{\Delta_X}(D_{X^2}K)
\otimes\pi_X^{-1}\omega_{\Delta_X/X^2}^{-1}.
\qquad\text{(19)}
\]

The trace-compatible relative complex on the diagonal is
\(\omega_{\Delta_X/X^2}=\omega_{\Delta_X}\otimes\delta^{-1}\omega_{X^2}^{-1}\), where \(\delta:X\to X^2\) is the diagonal. To specify its identification with \(\omega_X^{-1}\), use \(q_1\delta=\operatorname{id}_X\). The ordered exceptional-composition pairing (M16)–(M19) gives

\[
\omega_\delta\otimes\delta^{-1}\omega_{q_1}
\xrightarrow{\sim}\omega_{q_1\delta}=k_X,
\qquad
\delta^{-1}\omega_{q_1}\simeq\omega_X.
\]

The second identification is the smooth projection's second-factor dualizing complex. The first pairing is invertible and specifies \(\omega_\delta\simeq\omega_X^{-1}\) uniquely by tensor–Hom adjunction; its inverse-line comparison gives \(\omega_\delta^{-1}\simeq\omega_X\). In the product description, \(\delta^{-1}\omega_{X^2}\simeq\omega_X\otimes\omega_X\), this is exactly the composition cancellation after moving the factors into the prescribed order. Every such move uses the Koszul symmetry: interchanging the two dimension-\(n\) dualizing factors carries \((-1)^{n^2}\). No permutation is silently treated as sign-free. The resulting relative complex has shift \([-n]\) and its orientation line is retained; no normal or ambient orientation is trivialized.

Pull (18) back by \(\sigma\). Its right side first has the ordered factors \(q_2^{-1}D_XG\otimes q_1^{-1}F\). The Koszul symmetry, followed by the external evaluation (17) for \((G,F)\), gives the natural isomorphism
\(\sigma^{-1}D_{X^2}K_{F,G}\simeq F\boxtimes D_XG\xrightarrow{\sim}K_{G,F}\). Thus (16), now applied to \(D_{X^2}K_{F,G}\), supplies the actual chain

\[
a^{-1}\mu_\Delta(D_{X^2}K_{F,G})
\xleftarrow{\sim}\mu_\Delta(\sigma^{-1}D_{X^2}K_{F,G})
\xrightarrow{\sim}\mu_\Delta K_{G,F}.
\]

Substitute this chain and the specified \(\omega_\delta^{-1}\simeq\omega_X\) into (19). The result is (5). This cancellation uses the same exchange diffeomorphism and its functorial base-change maps as (16); the square of that exchange and the square of the tensor symmetry are identities. Hence no residual antipode, shift, or freely chosen orientation scalar is introduced. Evaluation, biduality, the two exchange comparisons and the ordered line pairing are all natural, so the conclusion is natural in \(F\) and \(G\).

## Examples and exercises with solutions

### A ray tests both the antipode and the normal shift

*Difficulty: Intermediate.*

On the increasing oriented line \(X=\mathbb R\), let \(M=\{0\}\) and \(F=k_{[0,\infty)}\). Compute both sides of (2) and (3), including the zero covector.

**Solution.** In the positive deformation chamber \(p(v,t)=tv\), the condition \(tv\geq0\) is \(v\geq0\). Hence \(\nu_MF=k_{[0,\infty)}\) on the normal line. The ambient dual is \(D_XF=k_{(0,\infty)}[1]\); its specialization is \(k_{(0,\infty)}[1]\), also the dual of the closed normal ray. This verifies (2).

The negative-pairing ray calculation gives \(\mu_MF=k_{(0,\infty)}\) on the conormal line. Its absolute dual is \(k_{[0,\infty)}[1]\). Covector negation gives \(k_{(-\infty,0]}[1]\), and \(\omega_{M/X}=k[-1]\) changes it to \(k_{(-\infty,0]}\). Independently, specializing \(D_XF\) and transforming the open positive normal ray gives \(k_{(-\infty,0]}[-1][1]=k_{(-\infty,0]}\). At the zero covector \(\mu_MF\) is zero, while \(\mu_M(D_XF)\) has coefficient \(k\). The antipode determines which half-line is closed; the relative shift removes the dual line's degree minus one.

### A point coefficient has no extra normal integration degree

*Difficulty: Introductory.*

In an oriented \(c\)-dimensional real vector space, take \(M=\{0\}\) and \(F=k_{\{0\}}\). Compute the two duality comparisons and also check \(c=0\).

**Solution.** Specialization is the sheaf at the zero normal vector. Its Fourier transform is the constant coefficient on the whole conormal vector space: the incidence restricted to the zero vector has pairing zero and projects identically to every covector. Thus \(\mu_MF=k_{E^*}\). The dual of the original closed point coefficient is again that point coefficient, since its intrinsic dualizing complex is \(k\). The same statement holds for its specialized point coefficient, verifying (2).

On the dual normal space, \(D_{E^*}k_{E^*}=\operatorname{or}_{E^*}[c]\). The antipode preserves the underlying orientation local-system type, and positive dual bases pair it with \(\omega_{M/X}=\operatorname{or}_{E}[-c]\). The orientation evaluation and opposite shifts give the constant coefficient \(k\), exactly \(\mu_M(D_XF)\). No additional normal shift remains. When \(c=0\), both vector spaces are points, both orientation factors are \(k\), and every displayed operation is the identity.

### A Möbius normal line retains its sign monodromy

*Difficulty: Advanced.*

Work over \(\mathbb Z\). Let \(X\) be the total space of the real analytic Möbius line bundle \(L\to S^1\), let \(M=S^1\) be its zero section, and let \(F=\mathbb Z_M\). Calculate (3) without trivializing the normal orientation globally.

**Solution.** The normal bundle is \(E=L\). Its fibre orientation line \(O\) on \(S^1\) has monodromy \(-1\): traversing the base once reverses a fibre basis. The dual line bundle has the same orientation monodromy. The circle itself is oriented and has \(\omega_M=\mathbb Z_M[1]\).

The coefficient is supported on the zero section, so \(\nu_MF\) is its zero-section coefficient on \(L\). The zero-vector Fourier calculation gives \(\mu_MF=\pi^{-1}\mathbb Z_M\) on \(L^*\). Closed-embedding duality gives \(D_XF=i_*\omega_M=\mathbb Z_M[1]\); hence its microlocalization is \(\pi^{-1}\mathbb Z_M[1]\).

The dual of the constant coefficient on \(L^*\) is its total-space dualizing complex \(\pi^{-1}O[2]\): one circle dimension and one fibre dimension contribute the shift two, while the fibre contributes the sign local system. The antipode covers the identity of the base, so its transported orientation line still has monodromy \(-1\). The relative embedding complex is \(\omega_{M/X}=O[-1]\). Their tensor product is
\(\pi^{-1}(O\otimes O)[1]\simeq\pi^{-1}\mathbb Z_M[1]\), as required. Omitting \(O[-1]\) would leave both the wrong degree and the wrong integral monodromy.

### The positive parameter fixes the boundary degree

*Difficulty: Intermediate.*

Take the constant coefficient on the oriented line and specialize at its origin. Use (7) to compute the boundary map and the degrees in the two middle expressions of (10).

**Solution.** The deformation is the \((v,t)\)-plane, with \(\Omega=\{t>0\}\). Its ordinary chamber pullback is constant. At a central point, its open extension has ordinary stalk zero, and ordinary direct image from the positive chamber has stalk \(k\) in degree zero: the small chamber intersection is a product of intervals with ordinary coefficient \(k\). Restricting (7) therefore gives a triangle
\(C\to0\to k\to C[1]\).
The last arrow is the actual localization connecting isomorphism, so \(C=s^!j_!r^{-1}k=k[-1]\), with its generator fixed by increasing \(t\).

The smooth inverse \(r^!k=r^{-1}k[1]\) shifts this costalk back: \(s^!j_!r^!k=k\). Thus specialization has coefficient \(k\) in degree zero. In the oriented deformation plane, duality sends \(j_!r^!k=k_{\{t>0\}}[1]\) to \(k_{\{t\geq0\}}[1]\). Its central ordinary restriction is \(k_E[1]\), the dual of the constant coefficient on the normal line. This is also the specialization of \(D_Xk_X=k_X[1]\). The two appearances of \([1]\) have distinct origins; (8) fixes their cancellation before the normal Verdier shift is calculated.

### A zero-section morphism coefficient uses the base dimension

*Difficulty: Intermediate.*

Let \(X\) be an oriented \(n\)-manifold, and \(P,Q\) perfect coefficient complexes, constant on \(X\). Calculate (4) and (5) for their microlocal Hom, using finite-projective evaluation.

**Solution.** Put \(A=R\operatorname{Hom}_k(P,Q)=P^\vee\otimes^LQ\). The exceptional projection in (14) contributes its fibre orientation and \([n]\). Specialization of that constant kernel adds no degree; the normal Fourier transform contributes the matching inverse orientation and \([-n]\). Their actual trace pairings cancel, giving
\(\mu\operatorname{hom}(P_X,Q_X)=i_*A_X\), with \(i:X\hookrightarrow T^*X\) the zero section.

The dual inputs on \(X\) are \(Q^\vee_X[n]\) and \(P^\vee_X[n]\). Their equal shifts cancel inside coefficient Hom. Finite-projective evaluation gives
\(R\operatorname{Hom}(Q^\vee,P^\vee)\simeq R\operatorname{Hom}(P,Q)\), so (4) has the same coefficient \(A\); the antipode fixes the zero section.

Closed-embedding duality calculates
\(D_{T^*X}i_*A_X=i_*D_XA_X=i_*(A^\vee_X[n])\).
Again finite-projective evaluation gives
\(A^\vee\simeq Q^\vee\otimes^LP=R\operatorname{Hom}(Q,P)\).
This is exactly \(\mu\operatorname{hom}(Q_X,P_X)\otimes\pi_X^{-1}\omega_X\). The degree is the intrinsic base dimension \(n\); directly inserting the cotangent total-space dimension \(2n\) would miss the closed-embedding costalk adjustment.

### Integral torsion keeps both dual morphism degrees

*Difficulty: Advanced.*

On the increasing oriented line, take \(P=\mathbb Z/m\), \(Q=\mathbb Z/n\), \(m,n>1\). Find the cohomology degrees of the absolute cotangent dual of \(\mu\operatorname{hom}(P_X,Q_X)\), and verify (5).

**Solution.** Write \(d=\gcd(m,n)\). A two-term finite-free resolution of \(P\) gives
\(A=R\operatorname{Hom}_{\mathbb Z}(P,Q)\) with \(\mathbb Z/d\) in degrees zero and one. The whole complex is perfect. Microlocal Hom is its zero-section extension by the preceding calculation.

To compute \(A^\vee\), the two-column integral hyper-Ext sequences give \(\mathbb Z/d\) in degrees zero and one: the degree-zero group comes from \(\operatorname{Ext}^1(H^1(A),\mathbb Z)\), and the degree-one group from \(\operatorname{Ext}^1(H^0(A),\mathbb Z)\). The Hom terms vanish since these groups are torsion. Its zero-section ambient dual is therefore \(i_*(A^\vee[1])\), with those groups in degrees minus one and zero.

On the right of (5), \(R\operatorname{Hom}_{\mathbb Z}(Q,P)\) has the same gcd torsion in degrees zero and one. Tensoring its zero-section extension with \(\pi_X^{-1}\omega_X=k[1]\) gives degrees minus one and zero, agreeing exactly. Finite-projective tensor–Hom evaluation identifies the full complexes and their natural pairing, not merely their cohomology groups. The integral Ext degree cannot be discarded in this duality comparison.

## References

Masaki Kashiwara and Pierre Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), provides the following constructions and results.

- Definition 2.1.2 and Theorem 2.1.3(iii), printed pp. 39–40 (PDF pp. 42–43), fix the negative-pairing Fourier transform and its ordinary coefficient-dual comparison, including the antipode and relative compact-support factor. Section 2.1 states its results without proofs. The variable-test Fourier proof (FDN8–FDN16) supplies (11), and taking the base dualizing complex yields the absolute duality used here.
- Definition 2.2.1 and Proposition 2.2.1, printed pp. 41–43 (PDF pp. 44–46), construct specialization by the positive normal deformation and state its basic conic and section properties. The connecting map (8) above is derived from open-complement localization; its oriented parameter identifies the exceptional-pullback expression needed for (10).
- Definition 5.5.1, printed pp. 90–91 (PDF pp. 93–94), defines microlocal Hom by the diagonal Hom kernel with ordinary pullback in its first argument and exceptional pullback in its second. Its diagonal conormal convention uses the first covector, as in (14)–(16).
- Definition 5.6.1 and Proposition 5.6.2, printed pp. 97–98 (PDF pp. 100–101), specify perfect formal neighborhood systems, evaluation biduality and constructible external-Hom exchange. These are the classical constructibility conditions behind the evaluation biduality proof and the external-Hom map in (17).
- Remark 8.2.9 and Propositions 8.3.3–8.3.6, printed pp. 148–150 (PDF pp. 151–153), relate real constructibility to cohomological constructibility and preserve it under inverse operations, specialization, microlocalization, conic Fourier transformation, internal Hom and tensor. The perfect-operation proofs give the stated coefficient and boundedness conditions used throughout this lesson.

The four comparisons are obtained in the order of their constructions: the positive boundary connecting map, Fourier duality with its inverse relative complex, factor exchange on the diagonal deformation, and evaluation of the product dualizing complex. The ray, point, Möbius-line and torsion calculations show where the boundary, orientation and coefficient degrees enter.
