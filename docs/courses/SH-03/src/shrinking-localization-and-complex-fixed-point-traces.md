# Shrinking localization and complex fixed-point traces

An expanding space computes a local contribution by compact cohomology. A shrinking space computes it by sections with support in that space. The two complexes can have different degrees even when their traces agree. We prove the supported formula, including singular maps on the shrinking space, then use complex scalar transport to compute holomorphic fixed-point traces. Constant real coefficients recover the determinant sign.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 2 October 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

Learn first Expanding subspaces and hyperbolic Lefschetz cutoffs, Homotopies and local cutoffs for Lefschetz contributions, Constructible costalks and Verdier duality, and Specializing Lefschetz contributions to the tangent space. The complex application also uses the written complex constructibility of specialization and complex Euler equation. The normalized support adjunctions, conic Euler and submersion descent, and complex-orbit descent are current SH-02 prerequisites. Their transitive foundations and independent review remain open.

Throughout the linear proof, \(V\) is a finite-dimensional real vector space, \(k\) a characteristic-zero field, and \(F\in D^b_{\mathbb R\text{-c}}(k_V)\) is positively conic with perfect stalks. Fix
\[
 u:V\longrightarrow V,\qquad \phi:u^{-1}F\longrightarrow F,
 \qquad 1\notin\operatorname{Ev}(u).
 \qquad\text{(1)}
\]
All supports are supports in the ambient space, with the locally closed convention \(R\Gamma_LF=R\mathcal Hom(k_L,F)\). A trace is the alternating trace of the actual induced endomorphism, denoted \(\operatorname{str}\).

## The supported action needs an inverse image of the support

Let \(S\subset V\) be a shrinking space: it is invariant, \(u|_S\) has no real eigenvalue greater than one, and \(u\) on \(V/S\) has no real eigenvalue in \([0,1)\). The spectral proof in the preceding lesson gives
\[
 u^{-1}S=S.
 \qquad\text{(2)}
\]
It does not require \(u|_S\) to be invertible. Put \(C_S=R\Gamma_S(V;F)\). Its action \(U_S\) is
\[
 \begin{aligned}
 C_S&\xrightarrow{u^*}
 R\Gamma_{u^{-1}S}(V;u^{-1}F)
 \xrightarrow{\phi}R\Gamma_{u^{-1}S}(V;F)
 =C_S.
 \end{aligned}
 \qquad\text{(3)}
\]
The first arrow is the supported ordinary pullback defined by the ordinary unit and the closed-support adjunction. No compact-support pullback by a singular map is being asserted.

For the closed inclusion \(i:S\hookrightarrow V\), put \(H=i^!F\). Constructible exceptional inverse image makes \(H\) perfect constructible, and equivariant exceptional inverse image makes it conic. Closed adjunction identifies \(C_S=R\Gamma(S;H)\); ordinary conic contraction identifies this complex with \(H_0\). It is therefore perfect.

The theorem to prove is
\[
 \boxed{C_0(\phi)=\operatorname{str}(U_S)
 \quad\text{for every shrinking space }S.}
 \qquad\text{(4)}
\]

## The supported hyperbolic box reverses both boundaries

First assume that no eigenvalue of \(u\) has modulus one. Retain the invariant splitting \(V=V_+\oplus V_-\) and adapted metric from the preceding lesson:
\[
 |u_+a|\ge c_2|a|,\qquad |u_-b|\le c_1|b|,
 \qquad 0<c_1<1<c_2.
 \qquad\text{(5)}
\]
The supported cutoff is now
\[
 Q_{a,b}=\overline B_a^+\times B_b^-.
 \qquad\text{(6)}
\]
The plus ball is closed, and the minus ball open. Its intersection with its inverse image is
\[
 u^{-1}Q_{a,b}\cap Q_{a,b}
 =u_+^{-1}\overline B_a^+\times B_b^-.
 \qquad\text{(7)}
\]
It is closed in \(Q_{a,b}\) and open in \(u^{-1}Q_{a,b}\). Closedness follows from the closed plus inverse ball; openness follows from the open minus ball inside its preimage. The adapted inequalities give the two containments required for this product identity.

Its compact closure has no fixed point other than zero. The supported cutoff theorem gives
\[
 C_0(\phi)=\operatorname{str}(U_{Q_{a,b}})
 \quad\text{on }C_{Q_{a,b}}=R\Gamma_{Q_{a,b}}(V;F).
 \qquad\text{(8)}
\]
The operator is supported pullback to \(u^{-1}Q_{a,b}\), the coefficient map, open restriction to (7), then enlargement of its closed plus support to \(\overline B_a^+\).

We compare this complex with \(C_{V_-}\). Restrict to the open minus ball, then enlarge the zero plus support to the closed plus ball. These specified maps give
\[
 \beta_{a,b}:C_{V_-}\longrightarrow C_{Q_{a,b}}.
 \qquad\text{(9)}
\]
Here \(C_{Q_{a,b}}\) can be calculated as
\(R\Gamma(V_+\times B_b^-;R\Gamma_{\overline B_a^+\times B_b^-}F)\).
This is open restriction followed by closed support, with ordinary sections on the open ambient set.

## Duality proves stabilization of that support map

For each fixed \(a>0\), (9) is an isomorphism when \(b\) is sufficiently large. We prove this for the actual map.

For a locally closed inclusion \(\ell:L\hookrightarrow V\), duality and its adjunction maps give
\[
 D_V(R\ell_*\ell^!F)=\ell_!\ell^{-1}D_VF.
 \qquad\text{(10)}
\]
For a closed inclusion this is exceptional inverse-image duality; for an open inclusion it is ordinary/open-extension duality. Factoring a locally closed inclusion proves the stated formula, with no dimension inserted into \(D_VF\). These are the normalized Verdier duality maps.

Both the supported and compact complexes below are perfect. For a relatively compact locally closed set this follows from constructible operations with compact ambient closed support. For \(V_-\), ordinary contraction proves perfection of \(C_{V_-}\), and proper-support contraction proves perfection of \(R\Gamma_c(V_-;D_VF|_{V_-})\). Thus the general ordinary/proper duality identity and constructible biduality may be reversed to give
\[
 \begin{aligned}
 C_{Q_{a,b}}^\vee&\simeq R\Gamma_c(Q_{a,b};D_VF),\\
 C_{V_-}^\vee&\simeq R\Gamma_c(V_-;D_VF|_{V_-}).
 \end{aligned}
 \qquad\text{(11)}
\]
In particular, we established the finite coefficient condition before inverting a duality map for nonproper ordinary sections.

Apply the forward stabilization theorem of the preceding lesson to \(D_VF\), using \(V_-\) as its open expanding coordinate and \(V_+\) as its closed coordinate. That theorem concerns a conic coefficient and a box; its proof requires no linear dynamics in those coordinates. For fixed \(a\), it gives
\[
 R\Gamma_c(Q_{a,b};D_VF)
 \xrightarrow{\mathrm{open\ extension}}
 R\Gamma_c(\overline B_a^+\times V_-;D_VF)
 \quad(b\gg1).
 \qquad\text{(12)}
\]
Let \(q:V\to V_+\) project along \(V_-\), and put \(G=Rq_!D_VF\). The conic projection theorem makes \(G\) perfect constructible. Fibre base change and closed-ball contraction give
\[
 \begin{aligned}
 R\Gamma_c(\overline B_a^+\times V_-;D_VF)
 &\simeq R\Gamma(\overline B_a^+;G)\\
 &\xrightarrow{\mathrm{restriction}}G_0
 \simeq R\Gamma_c(V_-;D_VF|_{V_-}).
 \end{aligned}
 \qquad\text{(13)}
\]
The composite of (12) and (13) is the dual of (9). To check this, dualize its two defining steps. Ordinary restriction to the open minus ball becomes open extension in that coordinate. Enlargement of the zero plus support becomes restriction to the zero plus fibre. Those two maps commute: their inclusions concern different factors, and their interchange is the open/closed base-change identity. After integrating the minus coordinate, closed plus restriction is exactly the counit giving \(G|_0\) in (13). Thus the dual of (9) is this composite, not an unspecified isomorphism between its terms.

Equations (12) and (13) make the dual map invertible. Perfect biduality then makes \(\beta_{a,b}\) invertible. This proves the support stabilization.

## The original shrinking operator commutes with stabilization

Since \(u^{-1}V_-=V_-\), (3) gives \(U_{V_-}\). We have an equality of actual maps
\[
 \beta_{a,b}U_{V_-}=U_{Q_{a,b}}\beta_{a,b}.
 \qquad\text{(14)}
\]
Indeed, the zero plus support is contained in \(u_+^{-1}\overline B_a^+\). Pullback therefore sends its enlargement into the support enlargement used in the cutoff. In the minus coordinate, pulling back the open restriction produces restriction to \(u_-^{-1}B_b^-\); the cutoff then restricts to \(B_b^-\). The containment \(u_-B_b^-\subset B_b^-\) makes this the same restriction as taking (3) and restricting its result to \(B_b^-\). The coefficient map commutes with each restriction. Naturality and transitivity of the closed-support counits identify both plus enlargements with enlargement of zero support to \(\overline B_a^+\). These facts prove (14) before either map is an isomorphism.

For sufficiently large \(b\), (9) is invertible. Equations (8) and (14) prove (4) for \(S=V_-\) in the hyperbolic case. Singular \(u_-\) causes no difficulty: the proof uses ordinary supported pullback, and duality was used to check \(\beta\), not to replace \(u_-\) by an inverse.

## A minimal shrinking space compares all choices

Let
\[
 P=\left(\bigoplus_{\lambda\in[0,1)}V^\mathbb C_\lambda\right)\cap V.
 \qquad\text{(15)}
\]
Every shrinking space contains \(P\), and \(P\) is itself shrinking. For a shrinking \(S\), retain \(H=i^!F\) on \(S\). The inverse support comparison for \(u^{-1}S=S\), followed by \(\phi\), defines
\[
 \chi:u_S^{-1}H\longrightarrow H.
 \qquad\text{(16)}
\]
This is obtained by restricting the map
\(u^{-1}R\Gamma_SF\to R\Gamma_S(u^{-1}F)\to R\Gamma_SF\)
to \(S\); closed proper base change identifies its source with \(u_S^{-1}H\). Its ordinary section operator is (3).

Put \(L=S/P\), \(A=u_{S/P}\), \(p:S\to L\), and \(G=Rp_*H\). The induced \(A\) has no real eigenvalue in \([0,\infty)\): the full primary blocks in \([0,1)\) have been removed, blocks greater than one were excluded from \(S\), and one is absent. In particular \(A\) is invertible. The conic projection theorem makes \(G\) perfect constructible.

The coefficient map on \(G\) is the ordinary comparison followed by \(Rp_*\chi\):
\[
 \psi:A^{-1}Rp_*H
 \longrightarrow Rp_*u_S^{-1}H
 \xrightarrow{Rp_*\chi}Rp_*H.
 \qquad\text{(17)}
\]
The first arrow is defined by adjunction from the ordinary counit
\[
 p^{-1}A^{-1}Rp_*H
 =u_S^{-1}p^{-1}Rp_*H
 \longrightarrow u_S^{-1}H.
 \qquad\text{(18)}
\]
We do not declare this comparison invertible. The square need not be Cartesian when \(u|_P\) is singular, and no such assertion is needed.

Ordinary composition gives \(R\Gamma(L;G)=R\Gamma(S;H)=C_S\), with its operator (3). At zero, the closed-support adjunction gives
\[
 R\Gamma_{\{0\}}(L;Rp_*H)
 \simeq R\Gamma_P(S;H)
 \simeq R\Gamma_P(V;F)=C_P.
 \qquad\text{(19)}
\]
Here is the nonproper adjunction check. For the point inclusion \(e:0\hookrightarrow L\), the inclusion \(j:P\hookrightarrow S\), and \(p_0:P\to0\), closed proper base change gives \(p^{-1}e_*Q=j_*p_0^{-1}Q\). Thus
\[
 \begin{aligned}
 \operatorname{Hom}(Q,e^!Rp_*H)
 &\simeq\operatorname{Hom}(p^{-1}e_*Q,H)\\
 &\simeq\operatorname{Hom}(p_0^{-1}Q,j^!H)
 \simeq\operatorname{Hom}(Q,Rp_{0*}j^!H).
 \end{aligned}
 \qquad\text{(20)}
\]
This proves the first map of (19) by Yoneda. The second is exceptional composition for the two closed inclusions. Transposing (18) through these same adjunctions gives the supported \(u_S\)-pullback on \(P\), followed by \(\chi\). Indeed \(u_S^{-1}P=P\), since \(A^{-1}(0)=0\). Exceptional composition and the support comparison in (16) identify it with \(U_P\). Consequently (19) intertwines the actual operators.

The positive-ray lemma from the preceding lesson says that the punctured ordinary trace on \(L\setminus0\) is zero. Its proof applies to the given \(\psi\), whether or not that coefficient map is invertible. Localization at zero, together with (19), therefore gives
\[
 \operatorname{str}(U_S)=\operatorname{str}(U_P).
 \qquad\text{(21)}
\]
For \(L=0\) this is the identity. In the hyperbolic case \(V_-\) is shrinking, so (21) compares any \(S\) with \(V_-\) through \(P\). The already proved case \(S=V_-\) proves (4) for every shrinking space in that case.

## Scalar deformation also preserves the supported operator

Choose positive \(t\) near one with \(tu\) never having eigenvalue one. A fixed shrinking space \(S\) remains shrinking: its finitely many positive eigenvalues remain on their original side of one, and zero remains inside \([0,1)\). Normalized positive conic transport gives one family \(\phi_t:(tu)^{-1}F\to F\).

The linear-family class theorem gives constant \(C_0(\phi_t)\). The operators \(U_{S,t}\) have constant trace too. To prove this without assuming that \(u_S\) is proper or invertible, use the support \(S\times I\) on \(V\times I\). Its inverse image under \((v,t)\mapsto(tuv,t)\) is itself, because the quotient map is invertible for every \(t\). The ordinary unit, support comparison and family coefficient map consequently define its supported section operator over \(I\).

On every open parameter interval \(J\), closed-support adjunction and ordinary interval descent identify
\[
 R\Gamma_{S\times J}(V\times J;\mathrm{pr}_V^{-1}F)
 \simeq C_S.
 \qquad\text{(22)}
\]
The restriction maps are the identity under this identification: both are inverse slice restrictions after ordinary pullback. Hence the parameter direct image is the constant perfect complex \(C_S\). Its induced family endomorphism has identical slice maps by interval descent. This proves trace constancy for the supported operators.

Choose \(t\) avoiding the finitely many values \(1/|\lambda|\) for nonzero eigenvalues. The hyperbolic theorem applies to \(tu\). Constancy of both sides now proves (4) for the original \(u\). The shrinking-space theorem is complete.

## Complex constructibility supplies local scalar transport

Let \(X\) now be a complex analytic manifold, \(F\in D^b_{\mathbb C\text{-c}}(k_X)\) have perfect stalks, and let
\[
 f:X\longrightarrow X\text{ be holomorphic},\qquad
 f(x)=x,\qquad \phi:f^{-1}F\longrightarrow F,
 \qquad \det_{\mathbb C}(1-df_x)\ne0.
 \qquad\text{(23)}
\]
The tangent-specialization theorem replaces this local number by the number for \(V=T_xX\), \(u=df_x\), and the actual induced coefficient map on \(K=\nu_xF\). It also gives \(K_0\simeq F_x\) and the normalized point-costalk comparison. Complex constructibility of specialization makes \(K\) complex constructible; specialization also makes it positively conic.

We need transport by a small complex scalar, not a globally trivial action of \(\mathbb C^*\). Write a cotangent covector as the real part of a complex covector \(\xi\). The conic Euler criterion gives \(\operatorname{Re}\langle v,\xi\rangle=0\) on \(\operatorname{SS}(K)\). Complex cotangent conicity also puts \(i\xi\) in that set; its Euler equation gives the imaginary part zero. Thus
\[
 \langle v,\xi\rangle=0
 \quad\text{on }\operatorname{SS}(K).
 \qquad\text{(24)}
\]
The factor two in the alternative real-covector convention does not change this annihilator.

Let \(D\subset\mathbb C^*\) be a sufficiently small contractible disk about one and \(a(v,\lambda)=\lambda v\), \(p(v,\lambda)=v\). Since \(a\) is a submersion, exact submersion pullback computes its microsupport. By (24), the parameter component of every pulled-back covector vanishes: differentiation in the two real parameter directions gives the real and imaginary parts of \(\langle v,\xi\rangle\). The horizontal microsupport criterion therefore makes \(a^{-1}K\) locally constant along the \(D\)-fibres of \(p\).

Whole-complex descent over this contractible two-dimensional parameter gives an isomorphism
\[
 a^{-1}K\simeq p^{-1}K
 \quad\text{normalized to the identity at }\lambda=1.
 \qquad\text{(25)}
\]
One may use a rectangular coordinate disk and apply contractible-parameter descent twice; restriction to the smaller disk gives the same normalized map by uniqueness. This retains the extension data of the bounded complex. Nontrivial monodromy around a complete punctured orbit is allowed.

Shrink \(D\) so that \(\lambda u\) has no eigenvalue one throughout it. The induced coefficient morphism and (25) give one family for \(\lambda u\). Choose \(\lambda\in D\) such that each nonzero complex eigenvalue of \(\lambda u\) is nonreal. Only finitely many real lines in the scalar plane are forbidden, so such a choice exists arbitrarily close to one. A path in \(D\) joins it to one, and the linear-family theorem preserves the local contribution.

## Stalk trace, and costalk trace for a local isomorphism

For the rotated \(\lambda u\), the zero subspace is expanding: its restriction has no eigenvalues, and the quotient has no positive real eigenvalue greater than one. Its compact complex is \(K_0\). The expanding theorem yields
\[
 \boxed{C_x(\phi)=\operatorname{str}(\phi_x).}
 \qquad\text{(26)}
\]
The point coefficient map in the parameter family is the original one: restriction of (25) to the fixed zero orbit is the identity, and a morphism of constant complexes on the connected disk has one slice map. The specialization zero-section comparison intertwines that map with \(\phi_x\).

If \(0\notin\operatorname{Ev}(df_x)\), the inverse function theorem makes \(f\) a local isomorphism at \(x\). Its point-support operator \(U_{\{x\}}\) is therefore defined by supported pullback near \(x\), followed by \(\phi\). The normal map \(u\) is invertible. After the same scalar rotation, the zero subspace is also shrinking, because every quotient eigenvalue is nonreal and zero is absent. The shrinking theorem gives
\[
 \boxed{C_x(\phi)
 =\operatorname{str}\bigl(U_{\{x\}}:
 R\Gamma_{\{x\}}(X;F)\longrightarrow R\Gamma_{\{x\}}(X;F)\bigr).}
 \qquad\text{(27)}
\]
To identify the action, the family inverse image of zero is zero at every parameter. Apply the supported parameter argument (22) with \(S=0\), using the transport (25). Its point-support operators are identical under the normalized slice maps. The tangent-specialization point-support comparison is built from the same closed counit and boundary connecting map; naturality for \(f^{-1}(x)=\{x\}\) near \(x\) intertwines the original and normal operators. Hence (27) concerns the original point-support action, without an extra parameter or orientation sign.

The additional invertibility condition has content. A branched holomorphic map can have a defined point-support action whose trace differs from the local contribution, as the fourth exercise shows.

## Constant real coefficients give the determinant sign

Return to a real analytic manifold, constant \(F=k_X\), canonical coefficient map, and a transverse fixed point \(x\). Transversality is \(\det_{\mathbb R}(1-u)\ne0\), where \(u=df_x\). Tangent specialization gives \(k_V\) with its canonical map. Choose the minimal expanding space \(W\), the sum of the real generalized eigenspaces with eigenvalue greater than one, and set \(d=\dim_{\mathbb R}W\).

Compact cohomology of \(W\) is its orientation line in degree \(d\), written \(k[-d]\) after an orientation is chosen. All eigenvalues of \(u|_W\) are positive, so \(\det(u|_W)>0\). Its proper pullback preserves the compact orientation generator. The expanding theorem gives \(C_x(\phi)=(-1)^d\).

This equals the determinant sign. A real eigenvalue greater than one contributes a negative factor to \(\det(1-u)\), with its algebraic multiplicity. Every other real eigenvalue contributes a positive factor, since one is excluded. Each nonreal conjugate pair contributes
\[
 (1-\lambda)(1-\overline\lambda)=|1-\lambda|^2>0.
 \qquad\text{(28)}
\]
The Jordan off-diagonal entries do not change a determinant. Consequently
\[
 \boxed{C_x(\phi)=\operatorname{sgn}\det_{\mathbb R}(1-df_x).}
 \qquad\text{(29)}
\]
More generally a locally constant perfect coefficient complex \(P\), with constant coefficient endomorphism \(b\), gives
\[
 C_x(\phi)=\operatorname{sgn}\det_{\mathbb R}(1-df_x)\,
 \operatorname{str}(b).
 \qquad\text{(30)}
\]
Indeed its compact expanding complex is \(P[-d]\), with identity on the orientation factor and \(b\) on \(P\). Rank \(m\) in shift \([r]\) gives \(m(-1)^r\) times (29).

For a complex-linear derivative,
\[
 \det_{\mathbb R}(1-u)=|\det_{\mathbb C}(1-u)|^2>0.
 \qquad\text{(31)}
\]
This explains the positive constant-coefficient holomorphic contribution. The real orientation computation uses the real dimension; a complex expanding line has dimension two.

## Exercises with complete solutions

### Equal traces can come from different degrees

*Difficulty: Introductory.*

Let \(u=-\mathrm{id}\) on \(\mathbb R\), with constant coefficient and its canonical map. Compare the expanding space zero and the shrinking space zero.

**Solution.** Both spaces satisfy their spectral conditions because the quotient eigenvalue is \(-1\). The expanding complex is the stalk \(k\), with identity and trace one. The shrinking complex is the zero costalk \(k[-1]\). Reflection acts by \(-1\) on its degree-one orientation generator, so its alternating trace is also one. The complexes have nonzero cohomology in different degrees. Both compute \(C_0=1\).

### A shrinking map can collapse a direction

*Difficulty: Intermediate.*

Take \(u=\operatorname{diag}(2,0,\tfrac12)\) on \(\mathbb R^3\), \(F=k_{\mathbb R^3}\), and \(S=\{x_1=0\}\). Calculate (3), including its degree.

**Solution.** The restriction to \(S\) has eigenvalues zero and \(1/2\), and its quotient has eigenvalue two, so \(S\) is shrinking and \(u^{-1}S=S\). Exceptional restriction to the codimension-one plane is the normal orientation line shifted by \(-1\); its ordinary sections on \(S\) are \(k[-1]\). The normal map \(x_1\mapsto2x_1\) preserves the generator. Pullback on the constant ordinary sections on \(S\), even though it collapses the zero-eigenvalue coordinate, is the identity. Thus \(U_S\) has degree-one action \(+1\) and trace \(-1\). The shrinking theorem gives \(C_0=-1\), agreeing with \(\det(1-u)=(-1)(1)(1/2)<0\).

### The closed-plus open-minus box has one supported degree

*Difficulty: Intermediate.*

For \(u(x,y)=(2x,y/2)\) and constant coefficients, compute \(R\Gamma_{[-a,a]\times(-b,b)}(\mathbb R^2;k)\) and its cutoff trace.

**Solution.** Localize the constant sheaf on the plus line into the closed interval and its two complementary rays. Ordinary sections give the diagonal map \(k\to k^2\). Its fibre has one copy of \(k\) in degree one, so the plus support complex is \(k[-1]\). The open minus factor contributes ordinary sections \(R\Gamma((-b,b);k)=k\); it contributes no compact-support degree. The product gives \(k[-1]\). Positive dilation in the plus normal direction preserves the supported generator, and contraction in the minus direction preserves the constant section. The cutoff trace is therefore \(-1\), equal to the shrinking-plane trace and \(C_0\).

### Branching separates local and point-support traces

*Difficulty: Advanced.*

For \(f(z)=z^2\) near zero in \(\mathbb C\), with constant coefficient and canonical map, calculate the stalk, local and point-support traces. Explain the extra hypothesis in (27).

**Solution.** The derivative at zero is zero, so one is absent. The stalk map is the identity on \(k\), and (26) gives local contribution one. The point preimage is \(\{0\}\), so a point-support operator is defined, although \(f\) is branched. Localization identifies \(H^2_{\{0\}}(\mathbb C;k)\) with \(H^1(\mathbb C^*;k)\) near zero. On a small circle, \(z\mapsto z^2\) has degree two, so pullback multiplies the degree-one circle class, and hence the degree-two support generator, by two. The costalk is \(k[-2]\) and its trace is two. Thus the costalk trace need not equal the local contribution when \(df_x\) has a zero eigenvalue. The local-isomorphism condition in (27) excludes this branching.

### Puncture monodromy survives scalar transport

*Difficulty: Advanced.*

Let \(j:\mathbb C^*\hookrightarrow\mathbb C\), let \(L\) have finite-dimensional fibre \(M\) and monodromy \(T\), and put \(F=j_!L\). For \(f(z)=az\), \(a\ne0,1\), choose a scalar-path lift and a coefficient morphism inducing an endomorphism \(B\) commuting with \(T\). Determine the local trace and check it using compact cohomology.

**Solution.** The zero stalk of \(j_!L\) is zero, so (26) gives contribution zero. A path lift identifies the scalar rotation with its continued coefficient action; different lifts can change that action by powers of \(T\), but do not remove the monodromy. Polar coordinates give
\[
 R\Gamma_c(\mathbb C^*;L)
 \simeq R\Gamma(S^1;L)[-1].
 \qquad\text{(32)}
\]
The circle complex is \([M\xrightarrow{T-1}M]\) in degrees zero and one. Under the chosen continuation its action is represented, up to the corresponding homotopy, by \(B\) on both terms. The shifted compact complex has degrees one and two; its trace is \(-\operatorname{tr}B+\operatorname{tr}B=0\). Equivalently, the traces on \(\ker(T-1)\) and \(\operatorname{coker}(T-1)\) agree by the invariant kernel/image exact sequences. The same cancellation holds after replacing \(B\) by \(BT^q\). This calculation allows nontrivial \(T\); no global trivialization of complex scaling was used.

### Graded point coefficients need their alternating trace

*Difficulty: Intermediate.*

On \(\mathbb C\), take a coefficient supported at zero with two copies of \(k\) in degree zero and three in degree one. Let the coefficient map act by two and three on these respective summands. For \(f(z)=2z\), calculate the local trace and the point-support trace.

**Solution.** The stalk trace is \(2\cdot2-3\cdot3=-5\). Formula (26) gives local contribution \(-5\). Since \(df_0=2\) is invertible, (27) gives the same point-support trace. A sheaf complex already supported at a point has the same point costalk and stalk; no ambient real-dimensional shift is added to those coefficients. Thus the supported operator also has alternating trace \(-5\).

### Jordan blocks count with their multiplicity

*Difficulty: Advanced.*

Let \(u=\operatorname{diag}(3,J_2(2),-3,R_{\pi/2},0)\) on \(\mathbb R^7\), where \(J_2(2)\) is one two-dimensional Jordan block and \(R_{\pi/2}\) is plane rotation. For rank \(m\) constant coefficients in shift \([r]\), compute the determinant and local contribution.

**Solution.** The positive real eigenvalues greater than one occupy three real dimensions: the eigenvalue three and the full two-dimensional block at two. Thus \(d=3\). Direct multiplication gives \(\det(1-u)=(-2)\cdot1\cdot4\cdot2\cdot1=-16\). The expanding orientation map has determinant \(3\cdot4=12>0\), so it acts by \(+1\). The compact complex is \(k^m[r-3]\), with alternating trace \(-m(-1)^r\). This is (30). The Jordan off-diagonal entry affects neither determinant.

### A complex line has an even real orientation degree

*Difficulty: Introductory.*

For \(f(z)=2z\) on \(\mathbb C\), compute the local contribution of \(k_{\mathbb C}[r]\) using the real expanding space \(\mathbb C\) and using the stalk formula.

**Solution.** The real expanding space has dimension two. Its compact complex is \(k[r-2]\), and the positive complex dilation acts by \(+1\) on the real orientation generator. Its trace is \((-1)^{r-2}=(-1)^r\). The stalk formula gives the identity on \(k[r]\), with the same trace. Using complex dimension one as a compact cohomological degree would insert an erroneous minus sign.

### The endpoint coefficient changes the shrinking answer

*Difficulty: Intermediate.*

Let \(F=k_{[0,\infty)}\) on \(\mathbb R\) with its canonical positive-dilation map. Compute the local contribution for \(u(t)=2t\) and \(u(t)=t/2\) using shrinking spaces.

**Solution.** For expansion, zero is shrinking. Its supported complex vanishes: localization maps \(R\Gamma(\mathbb R;F)=k\) isomorphically to \(R\Gamma(\mathbb R\setminus0;F)=k\), so its fibre is zero. The local contribution is zero. For contraction, the entire line is shrinking, and its ordinary supported complex is \(R\Gamma(\mathbb R;F)=k\) with identity action; the contribution is one. Both match the preceding endpoint theorem. The coefficient support, rather than only the derivative, changes the answer from the constant-sheaf determinant sign.

## Source context and the next chapter

These results are the shrinking case and the complex fixed-point traces in Kashiwara's microlocal Lefschetz fixed-point formula for constructible sheaves. The supported proof above supplies the stabilization map, the singular shrinking comparison, the scalar-family action and the complex parameter descent.

Yuichi Ike, [Hyperbolic localization via shrinking subbundles](https://arxiv.org/abs/1602.04651v3), develops the shrinking construction for higher-dimensional fixed components. Its setting supplies useful further context; the point theorem and all coefficient maps used here have been proved in this course.

These three selected point targets are now taught relative to the stated written prerequisites. The course continues with constructible functions and Lagrangian cycles in §9.7, then the assigned perverse-sheaf and differential-system chapters. Full finer atomization, lower geometric proofs, existing-lesson reconciliation.
