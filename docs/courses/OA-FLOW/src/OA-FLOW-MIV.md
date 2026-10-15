# Modular spectra and periods from the center flow

*Original exposition and illustration sources: CC0-1.0; earlier and font components retain their recorded terms.*

Two different subsets of the real line occur in the modular theory of a factor. One consists of times that fix its whole center flow. The other consists of frequencies carried by central eigenunitaries. The first determines the spectrum shared by all modular operators; the second determines when a modular automorphism is inner. We prove both identifications, keeping all faithful normal semifinite weights and arbitrary predual size.

<a id="miv-setting"></a>
## A trace-scaling presentation of the factor

Let \(N\ne0\) be a von Neumann algebra, let \(\theta:\mathbb R\to\operatorname{Aut}(N)\) be point-ultraweakly continuous, and let \(\tau\) be a faithful normal semifinite trace satisfying
\[
 \tau\circ\theta_s=e^{-s}\tau.
\tag{MIV0.a}
\]
Assume that the crossed product
\[
 P=N\rtimes_\theta\mathbb R
\tag{MIV0.b}
\]
is a type III factor. Here type III means that it has no nonzero finite projection. Every type III factor admits such a presentation at arbitrary predual size by [Continuous decompositions](OA-FLOW-CDEC.md#cdec-3). We identify \(N\) with its faithful normal coefficient copy in \(P\), and write \(u(s)\) for the crossed-product unitaries. Thus
\[
 u(s)xu(s)^*=\theta_s(x)\qquad(x\in N).
\tag{MIV0.c}
\]
The original group parameter is \(s\). We label dual characters by \(\chi_t(s)=e^{its}\); the dual action uses the multiplier \(\overline{\chi_t(s)}=e^{-its}\).

Let \(\Phi\) be the full dual weight of \(\tau\). The [modular and fixed-algebra calculation](OA-FLOW-L18.md#l18-1) proves, on the entire algebras,
\[
 \begin{aligned}
 \sigma_t^\Phi(x)&=x &&(x\in N),&
 \sigma_t^\Phi(u(s))&=e^{-its}u(s),\\
 P_\Phi&=N,&Z(P)&=Z(N)^\theta.
 \end{aligned}
\tag{MIV0.d}
\]
In particular \(\Phi\) is faithful normal semifinite and, on putting \(C=Z(N)\), we have \(C^\theta=\mathbb C1\). This is ergodicity of the center flow. The coefficient algebra \(N\) need not be a factor.

Our two modular invariants are
\[
 \begin{aligned}
 S(P)&=\bigcap_{\psi\ {\rm faithful\ normal\ semifinite}}
                  \operatorname{Sp}(\Delta_\psi),\\
 T(P)&=\{p\in\mathbb R:\sigma_p^\psi
                         \text{ is inner}\}.
 \end{aligned}
\tag{MIV0.e}
\]
The intersection in the first line includes every such weight, without requiring finite total mass. The second line is independent of the weight; Section 5 proves this explicitly. The modular operators and their spectra are those of the complete GNS constructions, including their unbounded domains.

There is no separability or sigma-finiteness assumption on either algebra or on its represented Hilbert space. The countable Fourier expansions in particular examples do not change these hypotheses. Some examples below are comparisons of commutative flows; assertions about a factor with such an associated flow are stated conditionally. The semifinite comparison is explicitly separated from the type III hypothesis in (MIV0.b).

<a id="miv-1"></a>
## 1. The center kernel through the full second crossing

Denote the coefficient inclusion by \(i:N\to P\), and put
\[
 K=\{s\in\mathbb R:\theta_s(z)=z\text{ for every }z\in C\}.
\]

Put \(\alpha=\sigma^\Phi=\widehat\theta\), with the equality supplied by [L18's dual-weight calculation](OA-FLOW-L18.md#l18-1), and write
\[
 D=P\rtimes_\alpha\mathbb R.
\]
Let \(j:P\to D\) be the coefficient map and \(v(t)\) its implementing unitary group. With the original Haar measure \(ds\) and its dual \(dt/(2\pi)\), the remaining dual action is
\[
 \delta_s(j(y))=j(y),\qquad
 \delta_s(v(t))=e^{-ist}v(t)
 \quad(y\in P).
 \tag{MIV1.a}
\]
The character used to label \(s\) on the second group is \(t\mapsto e^{ist}\); the dual action uses its conjugate. Haar rescaling gives the same normally represented crossed product: multiplication of \(L^2\) functions by the square root of the constant measure ratio is an onto unitary intertwining coefficient fields and translations. Thus choosing this dual Haar measure imposes no additional hypothesis on the modular action.

The full [normal double-duality construction](OA-FLOW-ND.md#nd-construction), applied to the original action \(\theta\), gives a normal isomorphism with normal inverse
\[
 \Xi:D\longrightarrow
       N\,\overline\otimes\,B(L^2(\mathbb R,dr)).
 \tag{MIV1.b}
\]
In an arbitrary faithful normal representation \(N\subseteq B(H)\), its exact values are
\[
 \begin{aligned}
 \bigl[\Xi(j(i(x)))\xi\bigr](r)&=\theta_{-r}(x)\xi(r),\\
 \Xi(j(u(s)))&=1\otimes L_s,
       & [L_s\xi](r)&=\xi(r-s),\\
 \Xi(v(t))&=1\otimes Q_t,
       & [Q_t\xi](r)&=e^{-itr}\xi(r).
 \end{aligned}
 \tag{MIV1.c}
\]
These formulas describe the full map. For its existence and onto image, ND first uses the partial Fourier unitary on the second real variable, then the shear \((q,r)\mapsto(q+r,r)\), and finally tensor regrouping. If \(\mathscr W\) is their composite and
\[
 [\rho(x)\eta](q)=\theta_{-q}(x)\eta(q),
\]
then its [whole-domain inverse formulas](OA-FLOW-ND.md#nd-inverse) are
\[
 \begin{aligned}
 \Xi(Y)&=(\rho^{-1}\bar\otimes\mathrm{id})
                 (\mathscr W Y\mathscr W^*),\\
 \Xi^{-1}(Z)&=\mathscr W^*
                 (\rho\bar\otimes\mathrm{id})(Z)\mathscr W .
 \end{aligned}
 \tag{MIV1.d}
\]
Here \(\rho\) is faithful and normal onto its von Neumann image. The [finite-matrix tensor proof](OA-FLOW-ND.md#nd-tensor) constructs both tensor maps normally on the entire tensor algebras. The [orbit-field and Weyl-pair proof](OA-FLOW-ND.md#nd-orbits) identifies the image after the Fourier transform and shear with that whole tensor algebra. Consequently (MIV1.d) proves normality and surjectivity of (MIV1.b), including its inverse; covariance on generators alone is not being used to obtain normal extension.

Let \(R_s\xi(r)=\xi(r+s)\). The surviving action is
\[
 \Xi\delta_s\Xi^{-1}
       =\theta_s\bar\otimes\operatorname{Ad}R_s .
 \tag{MIV1.e}
\]
One can check its sign on each family in (MIV1.c). On the coefficient field, the right translation first changes \(\theta_{-r}(x)\) to \(\theta_{-(r+s)}(x)\), and \(\theta_s\) restores it. Left and right translations commute. Finally
\[
 R_sQ_tR_s^*=e^{-ist}Q_t,
\]
which is exactly (MIV1.a). Both actions are normal and the three families generate the algebra, so these checks prove (MIV1.e) everywhere.

We need the entire center of the tensor algebra in (MIV1.b). Put \(K_0=L^2(\mathbb R,dr)\), choose an orthonormal basis \((e_k)\), and use its matrix units \(E_{kl}\). An operator \(Z\in N\bar\otimes B(K_0)\) has entries \(Z_{kl}\in N\), by the finite-compression proof in ND. If \(Z\) is central, commutation with \(1\otimes E_{kk}\) makes its off-diagonal entries zero; commutation with \(1\otimes E_{kl}\) makes all diagonal entries the same \(z\in N\). Equality of the operators follows on the dense finite-coordinate vectors, so \(Z=z\otimes1\). Commutation with every \(x\otimes1\) now says \(z\in Z(N)\). Conversely such a \(z\otimes1\) commutes with the algebraic tensor generators, and separate ultraweak continuity of multiplication extends this to their von Neumann closure. Hence
\[
 Z(N\bar\otimes B(K_0))=Z(N)\otimes1 .
 \tag{MIV1.f}
\]
The map \(z\mapsto z\otimes1\) is normal: for each positive bounded increasing net, its supremum is detected on elementary vectors, hence on all vectors by density and boundedness. Its inverse on this range is compression by the isometry \(\eta\mapsto\eta\otimes e_{k_0}\), and is normal as well. Thus (MIV1.f) is a normal identification in both directions, not just an algebraic center equality. No countable basis of \(H\), or of a representation of \(N\), has been assumed.

It follows that
\[
 \kappa_C:C=Z(N)\longrightarrow Z(D),\qquad
 \kappa_C(z)=\Xi^{-1}(z\otimes1)
\]
is an onto normal isomorphism with normal inverse. Equations (MIV1.e)–(MIV1.f) give
\[
 \delta_s\kappa_C(z)=\kappa_C(\theta_s(z)),\qquad
 \ker(\delta|_{Z(D)})=\ker(\theta|_C)=K .
 \tag{MIV1.g}
\]
This is the center map used here. The original coefficient \(j(i(z))\) has image \(r\mapsto\theta_{-r}(z)\), which need not be constant or central in the full tensor algebra.

For each \(z\in C\), the set \(\{s:\theta_s(z)=z\}\) is closed, since every normal functional evaluated on \(\theta_s(z)-z\) is continuous and the predual separates points. Their intersection \(K\) is therefore closed. The action law gives \(0\in K\), closure under addition, and closure under inverses. Thus \(K\) is a closed additive subgroup of \(\mathbb R\).

Finally apply the [dual-center kernel theorem, L115 equation K43](OA-FLOW-L115.md#oa-flow.connes.centerkernel), to \(\alpha=\sigma^\Phi\) on \(P\). Its hypotheses are a point-ultraweakly continuous action on an arbitrary von Neumann algebra and a locally compact Hausdorff abelian group. They all hold here. Its crossed product is \(D\), and its negative-character dual action is precisely \(\delta\). Therefore (MIV1.g) proves
\[
 \boxed{\ \Gamma(\sigma^\Phi)=K.\ }
 \tag{MIV1.h}
\]
L115's [Fourier conventions](OA-FLOW-L115.md#oa-flow.l115.conventions) identify the positive and negative conventions for whole action spectra: adjoint reflection makes those spectra symmetric. No reflection of an individual spectral vector is presumed. In particular the real subgroup in (MIV1.h) is expressed in the original parameter \(s\), with no extra \(2\pi\) factor. The proof of this section works for every specified trace-scaling system; factoriality and type III will enter the all-weight and zero-spectrum steps.

<a id="miv-2"></a>
## 2. Intersect over all faithful semifinite weights

Let \(\mathcal W_0(P)\) be the set of all faithful normal semifinite weights on \(P\). It is nonempty because \(\Phi\) belongs to it. For \(\psi\in\mathcal W_0(P)\), let \(\Delta_\psi\) be its complete modular operator on its GNS Hilbert space. Put
\[
 S_+(P)=
 \left(\bigcap_{\psi\in\mathcal W_0(P)}
                \operatorname{Sp}(\Delta_\psi)\right)
                 \cap(0,\infty).
 \tag{MIV2.a}
\]
The separate GNS Hilbert spaces present no difficulty: each spectrum is a subset of the same scalar half-line. All weights in this intersection may have infinite value at the identity.

We first recall the exact analytic link between a modular action and its operator. With the positive Fourier convention
\(\widehat f(r)=\int_{\mathbb R}f(t)e^{itr}\,dt\), put
\[
 T_f^\psi(x)=\int_{\mathbb R} f(t)\sigma_t^\psi(x)\,dt
 \quad(f\in L^1(\mathbb R)).
\]
The integral is normal and weak-star. The full GNS filter theorem [MG0](OA-FLOW-MG.md#oa-flow.mg.0) proves, on every element of the finite left ideal,
\[
 \begin{gathered}
 T_f^\psi(\mathfrak n_\psi)\subseteq\mathfrak n_\psi,\\
 \Lambda_\psi(T_f^\psi x)
    =\widehat f(\log\Delta_\psi)\Lambda_\psi(x),
       \qquad x\in\mathfrak n_\psi .
 \end{gathered}
 \tag{MIV2.b}
\]
That theorem obtains the domain inclusion from simultaneous bounded operator sums and convergent Hilbert-vector sums, followed by the closed GNS graph. Thus (MIV2.b) holds even though the GNS map need not be bounded on operator balls.

Here is how it gives the entire action spectrum. If \(T_f^\psi=0\), the multiplier on the right of (MIV2.b) vanishes on the dense range of \(\Lambda_\psi\), hence is zero. Conversely a zero multiplier makes \(\Lambda_\psi(T_f^\psi x)=0\) for every \(x\in\mathfrak n_\psi\). Faithfulness gives \(T_f^\psi x=0\). The finite left ideal is ultraweakly dense and \(T_f^\psi\) is normal, so it vanishes everywhere. The full spectral-support argument in [MG1](OA-FLOW-MG.md#oa-flow.mg.1) identifies the resulting filter annihilator:
\[
 \begin{aligned}
 \operatorname{Sp}(\sigma^\psi)
       &=\operatorname{Sp}(\log\Delta_\psi),\\
 \exp\operatorname{Sp}(\sigma^\psi)
       &=\operatorname{Sp}(\Delta_\psi)\cap(0,\infty).
 \end{aligned}
 \tag{MIV2.c}
\]
Indeed a neighborhood of a positive number \(\lambda\) has nonzero \(\Delta_\psi\)-spectral projection exactly when its logarithmic image has nonzero \(\log\Delta_\psi\)-spectral projection. MG1 proves the support criterion from the full resolvents and squared spectral-domain integrals. The statement at \(\lambda>0\) makes no assertion about zero.

Fix \(\alpha=\sigma^\Phi\), and let \(Z^1_\alpha(\mathbb R,P)\) denote the strongly continuous unitary cocycles:
\[
 w_{t+r}=w_t\alpha_t(w_r).
\]
Such a path is also strongly* continuous. For example,
\(\|(w_t^*-w_{t_0}^*)\xi\|
 =\|(w_{t_0}-w_t)w_{t_0}^*\xi\|\).
The [balanced-cocycle theorem BC4](OA-FLOW-BC.md#oa-flow.bc.4) assigns to every \(\psi\in\mathcal W_0(P)\) a cocycle
\[
 w_t^\psi=(D\psi:D\Phi)_t,\qquad
 \sigma_t^\psi=\operatorname{Ad}(w_t^\psi)\alpha_t .
 \tag{MIV2.d}
\]
Conversely, the complete [unitary-cocycle reconstruction UR0–5](OA-FLOW-UR.md#oa-flow.ur.0) assigns to every \(w\in Z^1_\alpha(\mathbb R,P)\) a unique faithful normal semifinite weight \(\psi_w\) on \(P\), with
\[
 (D\psi_w:D\Phi)_t=w_t,\qquad
 \sigma_t^{\psi_w}=\operatorname{Ad}(w_t)\alpha_t .
 \tag{MIV2.e}
\]
Its hypotheses are exactly a faithful n.s.f. reference and a strongly* continuous unitary cocycle. UR1 constructs the dense mixed analytic space with its GNS curve; UR2 closes its full involution; UR3 recovers a weight on the entire positive cone. UR4 aligns the natural cones, and [UR5's complete relative graph](OA-FLOW-UR.md#oa-flow.ur.5) gives the normalized derivative in (MIV2.e), including its scalar normalization. Thus every cocycle in the intersection below is realized on this same algebra. Neither a finite reference weight nor a countability assumption is required.

Since \(P\) is a factor, \(Z(P)^\alpha=\mathbb C1\). The full [cocycle spectral-intersection theorem L120](OA-FLOW-L120.md#ci-intersection), equation C29, therefore applies:
\[
 \Gamma(\alpha)
   =\bigcap_{w\in Z^1_\alpha(\mathbb R,P)}
         \operatorname{Sp}(\operatorname{Ad}(w)\alpha).
 \tag{MIV2.f}
\]
The [actual setting of L120](OA-FLOW-L120.md#ci-setting) allows arbitrary Hilbert dimension and arbitrary algebra cardinality. Its central-ergodicity assumption, just verified, is the only additional action hypothesis needed here. Its proof compares the reduced spectra of every nonzero fixed corner. The [matrix transport](OA-FLOW-L120.md#ci-transport) preserves the entire action spectrum under amplification by any nonzero Hilbert space; the first-corner construction fixes the prescribed corner exactly before lifting to a cocycle. The resulting containment for each fixed projection is what yields C29. Full central support alone is not substituted for an isomorphism \(ePe\cong P\).

We prove both inclusions in the weight intersection. If \(r\in\Gamma(\alpha)\), (MIV2.f) puts \(r\) in the spectrum of the perturbation associated with every \(\psi\) in (MIV2.d). Equation (MIV2.c) then puts \(e^r\) in every \(\operatorname{Sp}(\Delta_\psi)\), so \(e^r\in S_+(P)\).

Conversely let \(\lambda\in S_+(P)\) and set \(r=\log\lambda\). For any cocycle \(w\), use the weight \(\psi_w\) from (MIV2.e). Since \(\lambda\) belongs to that weight's complete modular spectrum, (MIV2.c) puts \(r\) in
\(\operatorname{Sp}(\operatorname{Ad}(w)\alpha)\).
This holds for every \(w\); (MIV2.f) therefore gives \(r\in\Gamma(\alpha)\). We have proved
\[
 \boxed{\quad S_+(P)=\exp\Gamma(\sigma^\Phi)=\exp K.\quad}
 \tag{MIV2.g}
\]
The logarithm and exponential in this proof are inverse bijections at positive scalar values. No closure operation at zero has been moved through an intersection.

Only factoriality was used in the comparison leading to the first equality in (MIV2.g). Thus the same argument proves, for every nonzero factor \(A\) and every faithful n.s.f. reference weight \(\omega\),
\[
 \left(\bigcap_{\psi\in\mathcal W_0(A)}
                \operatorname{Sp}(\Delta_\psi)\right)
       \cap(0,\infty)
       =\exp\Gamma(\sigma^\omega).
 \tag{MIV2.h}
\]
Such a reference always exists by [FR1](OA-FLOW-FR.md#oa-flow.fr.1), whose proof uses an arbitrary orthogonal family of normal-state supports. Formula (MIV2.h) is independent of the reference because its left side is. The proof used the unrestricted cocycle reconstruction and cocycle intersection; it did not use the separable-predual corner-isomorphism conclusion in MG4.

<a id="miv-3"></a>
## 3. Zero belongs to each complete modular spectrum

We retain the type III hypothesis on \(P\). In fact the argument in this section applies to any nonzero type III algebra equipped with a faithful normal semifinite weight. Fix such a weight \(\psi\). Its complete modular data satisfy the closed-operator identity
\[
 J_\psi\Delta_\psi J_\psi=\Delta_\psi^{-1}.
 \tag{MIV3.a}
\]
This includes equality of domains; \(\Delta_\psi\) is injective, even when zero belongs to its spectrum.

Suppose, for a contradiction, that \(0\notin\operatorname{Sp}(\Delta_\psi)\). The exact [reciprocal-domain argument in MT1](OA-FLOW-MT.md#oa-flow.mt.1) then gives a number \(0<c<1\) such that
\[
 cI\le\Delta_\psi\le c^{-1}I,\qquad
 L=\log\Delta_\psi=L^*\in B(H_\psi).
 \tag{MIV3.b}
\]
To recall the domain mechanism, the spectral gap at zero makes the reciprocal spectral function bounded, so \(\Delta_\psi^{-1}\) has domain all of \(H_\psi\). Conjugating (MIV3.a) then makes \(\Delta_\psi\) bounded on all of \(H_\psi\) as well. The same full spectral calculus makes the logarithm bounded, with \(\|L\|\le|\log c|\).

Identify \(P\) with its faithful normal GNS image. Modular implementation gives
\(\sigma_t^\psi(x)=e^{itL}xe^{-itL}\).
The norm-convergent exponential series yields the operator-norm limit
\[
 d(x)=\lim_{t\to0}\frac{\sigma_t^\psi(x)-x}{t}
       =i[L,x]\in P,\qquad
 \|d\|\le2\|L\|.
 \tag{MIV3.c}
\]
Membership in \(P\) follows because every difference quotient lies in its norm-closed image. The commutator identities show that \(d\) is a bounded star derivation. The [already-bounded implementer construction used in MT2](OA-FLOW-MT.md#oa-flow.mt.2) supplies \(b=b^*\in P\) with \(d(x)=i[b,x]\). The two norm-continuous groups with this bounded generator agree: differentiating \(e^{-td}\sigma_t^\psi\) gives zero derivative and value the identity at zero, and the same calculation applies to \(\operatorname{Ad}(e^{itb})\). Hence
\[
 \sigma_t^\psi=\operatorname{Ad}(e^{itb}),\qquad
 b\in P_\psi .
 \tag{MIV3.d}
\]
The last assertion follows by applying the first to \(b\). This argument invokes the proved bounded-derivation result inside MT2; it requires no automatic boundedness assertion about arbitrary derivations.

Put \(h=e^{-b}\). It is bounded, positive, invertible, and belongs to the centralizer. The [whole-positive-cone construction in MT3](OA-FLOW-MT.md#oa-flow.mt.3), using the bounded centralizer-density theorem, defines
\[
 \eta(a)=\psi(h^{1/2}ah^{1/2})
 \quad(a\in P_+)
\]
and proves
\[
 e^{-\|b\|}\psi\le\eta\le e^{\|b\|}\psi,\qquad
 \sigma_t^\eta(x)
   =h^{it}\sigma_t^\psi(x)h^{-it}=x .
 \tag{MIV3.e}
\]
These weight inequalities hold on the entire positive cone, including infinite values. They make \(\eta\) faithful and give exactly the same finite left ideal as \(\psi\), so semifiniteness is preserved. Normality follows from normal compression and normality of \(\psi\). The full trace criterion in MT3 now gives
\[
 \eta(x^*x)=\eta(xx^*)\quad(x\in P),
 \tag{MIV3.f}
\]
also when the values are infinite. Thus \(\eta\) is a faithful normal semifinite trace.

For completeness, here is the projection contradiction from [MT4](OA-FLOW-MT.md#oa-flow.mt.4). Semifiniteness on the nonzero algebra gives \(0\ne x\in\mathfrak n_\eta\). Then \(a=x^*x\ne0\) has \(0<\eta(a)<\infty\). Some spectral projection
\[
 q=1_{[\varepsilon,\infty)}(a),\qquad \varepsilon>0,
\]
is nonzero, since these projections increase to the support of \(a\) as \(\varepsilon\downarrow0\). Spectral order and faithfulness give
\[
 0<\eta(q)\le\varepsilon^{-1}\eta(a)<\infty.
 \tag{MIV3.g}
\]
If \(q'\le q\) is equivalent to \(q\), choose \(w\in P\) with \(w^*w=q\), \(ww^*=q'\). Equation (MIV3.f) gives \(\eta(q)=\eta(q')\). Additivity at \(q=q'+(q-q')\), and the finite value already proved in (MIV3.g), imply \(\eta(q-q')=0\). Faithfulness gives \(q'=q\). Therefore \(q\) is finite, contradicting the definition of type III.

The contradiction proves, for every weight in the full defining intersection,
\[
 0\in\operatorname{Sp}(\Delta_\psi)
 \quad(\psi\in\mathcal W_0(P)).
 \tag{MIV3.h}
\]
The spectrum of each positive self-adjoint modular operator is contained in \([0,\infty)\). Combining (MIV3.h) with (MIV2.g) therefore gives the complete invariant
\[
 \boxed{\quad
 S(P)=\bigcap_{\psi\in\mathcal W_0(P)}
                    \operatorname{Sp}(\Delta_\psi)
       =\{0\}\cup\exp K .
 \quad}
 \tag{MIV3.i}
\]
No weight in the intersection has been replaced by a state or by a restriction to a countably decomposable corner. The zero term was proved separately for each full modular operator. It is compatible with injectivity: \(E_{\Delta_\psi}(\{0\})=0\) excludes a zero eigenvector, whereas (MIV3.h) says there is no bounded everywhere-defined inverse.

<a id="miv-4"></a>
## 4. Three closed kernels and three modular spectra

The preceding sections have identified
\[
 K=\{s\in\mathbb R:\theta_s|_C=\operatorname{id}\},
 \qquad S(P)=\{0\}\cup\exp K.
\tag{MIV4.a}
\]
Here \(K\) is a closed additive subgroup, and \(\exp K=\{e^s:s\in K\}\). We now classify these subsets directly.

If \(K\) has no positive element, symmetry under negation gives \(K=\{0\}\). Otherwise let
\[
 a=\inf\bigl(K\cap(0,\infty)\bigr).
\tag{MIV4.b}
\]
Suppose first that \(a=0\). Choose \(k_n\in K\) with \(0<k_n<1/n\). For any \(r\in\mathbb R\), put \(m_n=\lfloor r/k_n\rfloor\). Then
\[
 0\le r-m_nk_n<k_n,\qquad m_nk_n\in K.
\tag{MIV4.c}
\]
Thus \(r\) is a limit of points of \(K\), so closedness gives \(r\in K\). Consequently \(K=\mathbb R\).

If \(a>0\), the definition of the infimum supplies \(k_n\in K\cap(0,\infty)\) tending to \(a\). Closedness puts \(a\) in \(K\). Given \(r\in K\), divide by \(a\): for \(m=\lfloor r/a\rfloor\),
\(r-ma\in K\cap[0,a)\). A positive remainder would contradict the definition of \(a\). Hence \(r=ma\), and conversely every integer multiple of \(a\) is in \(K\). We have proved the complete list
\[
 K=\{0\},\qquad K=a\mathbb Z\ (a>0),\qquad K=\mathbb R.
\tag{MIV4.d}
\]
This proof includes negative \(r\) and uses neither a measurable model of the center nor a countability assumption on its algebra.

Ergodicity identifies the last case precisely. If \(K=\mathbb R\), every element of \(C\) is fixed, so \(C=C^\theta=\mathbb C1\). If \(C=\mathbb C1\), every automorphism fixes it, so \(K=\mathbb R\). Therefore
\[
 K=\mathbb R\quad\Longleftrightarrow\quad C=\mathbb C1.
\tag{MIV4.e}
\]
In the case \(K=a\mathbb Z\), \(a\) is exactly the least positive period of the center flow. Put \(\lambda=e^{-a}\), so \(0<\lambda<1\). Negating the integer index gives
\(\exp(a\mathbb Z)=\lambda^{\mathbb Z}\). In the case \(K=\{0\}\), the center flow is faithful as an action of \(\mathbb R\), and its center cannot be scalar by (MIV4.e). Combining with (MIV4.a) gives:

| Center-flow condition | Modular spectrum \(S(P)\) | Type |
| --- | --- | --- |
| Kernel \(a\mathbb Z\), with least positive period \(a>0\) | \(\{0\}\cup\{\lambda^n:n\in\mathbb Z\}\), \(\lambda=e^{-a}\) | \({\rm III}_\lambda\) |
| Kernel \(\{0\}\) | \(\{0,1\}\) | \({\rm III}_0\) |
| Scalar center, equivalently kernel \(\mathbb R\) | \([0,\infty)\) | \({\rm III}_1\) |

These are equivalent spectral and center-flow descriptions of the subtypes of a given type III factor. The implications go in both directions: the positive part of \(S(P)\) recovers \(K\) by the logarithm, and (MIV4.d)–(MIV4.e) recover the corresponding center-flow condition. This is not an isomorphism classification within a subtype or an existence proof for a factor realizing a prescribed flow.

A trivial flow has every real time in its kernel. A faithful aperiodic flow has only zero in its kernel. The distinction between these statements, rather than the phrase “no least positive period,” separates the last two rows.

<a id="miv-5"></a>
## 5. Inner modular times are central eigenfrequencies

We first verify that the definition of \(T(P)\) is independent of \(\psi\). If \(\psi,\eta\) are faithful normal semifinite weights, the [balanced cocycle covariance theorem](OA-FLOW-BC.md#oa-flow.bc.4) gives unitary elements
\[
 v_t=[D\eta:D\psi]_t,\qquad
 \sigma_t^\eta=\operatorname{Ad}(v_t)\circ\sigma_t^\psi.
\tag{MIV5.a}
\]
For each fixed \(p\), the right side differs from \(\sigma_p^\psi\) by an inner automorphism. A composition of two inner automorphisms is inner, and the inverse of an inner automorphism is inner. It follows that \(\sigma_p^\eta\) is inner exactly when \(\sigma_p^\psi\) is inner. The modular group law also shows that \(T(P)\) is an additive subgroup: inner times are closed under addition and negation and contain zero. No closedness of this subgroup is asserted.

Define the central eigenfrequency group by
\[
 E_\theta(C)=
 \{p\in\mathbb R:\text{there is }a\in\mathcal U(C)
                 \text{ with }\theta_s(a)=e^{isp}a
                 \text{ for every }s\in\mathbb R\}.
\tag{MIV5.b}
\]
Then
\[
 \boxed{\quad T(P)=E_\theta(C).\quad}
\tag{MIV5.c}
\]
The units in (MIV5.b) are bounded elements of the whole center, and the equations are operator equalities for every \(s\).

To prove the forward implication, use weight independence to choose \(\Phi\). Let \(p\in T(P)\), and choose a unitary \(a\in P\) with
\(\sigma_p^\Phi=\operatorname{Ad}(a)\).
The whole-positive modular invariance gives
\[
 \Phi\circ\operatorname{Ad}(a)=\Phi.
\tag{MIV5.d}
\]
The [weight-preserving-unitary criterion](OA-FLOW-CZ.md#cz-0) now puts \(a\) in \(P_\Phi=N\). Its proof works on the full finite ideal of an arbitrary semifinite weight: preservation gives right stability and the finite cyclic identity, and the modular strip test then proves that the unitary is in the centralizer. In particular this step is valid when \(\Phi(1)=\infty\). It is also the precise mechanism in [PW1](OA-FLOW-PW.md#pw-1).

By (MIV0.d), \(\sigma_p^\Phi\) fixes \(N\) pointwise. Therefore \(a\), already known to belong to \(N\), commutes with every element of \(N\). Thus \(a\in C\). Apply its adjoint action to \(u(s)\). Covariance and (MIV0.d) give
\[
 a\theta_s(a^*)u(s)=a u(s)a^*
                 =e^{-ips}u(s).
\tag{MIV5.e}
\]
Cancel the unitary \(u(s)\), multiply by \(a^*\), and take adjoints. The result is
\[
 \theta_s(a)=e^{isp}a\qquad(s\in\mathbb R).
\tag{MIV5.f}
\]
This is (MIV5.b), with its positive eigenfrequency sign.

Conversely let \(a\in\mathcal U(C)\) satisfy (MIV5.f). Its adjoint action fixes \(N\). The same covariance calculation yields
\[
 a u(s)a^*=a\theta_s(a^*)u(s)=e^{-ips}u(s).
\tag{MIV5.g}
\]
Hence \(\operatorname{Ad}(a)\) and \(\sigma_p^\Phi\) agree on \(N\) and on every \(u(s)\). They are normal automorphisms, so agreement on the unital star algebra generated by these operators extends by ultraweak density to all of \(P\). Thus \(\sigma_p^\Phi\) is inner, proving (MIV5.c). The proof did not require a computation of \(N'\cap P\).

The eigenspaces have an additional rigidity. Suppose \(0\ne b\in C\) satisfies
\(\theta_s(b)=e^{isp}b\). Then \(b^*b\in C^\theta=\mathbb C1\), so \(b^*b=c1\) for a positive scalar \(c\). Since \(C\) is abelian, also \(bb^*=c1\). Thus \(c^{-1/2}b\) is an eigenunitary. If \(a_1,a_2\) are two eigenunitaries of frequency \(p\), their product \(a_1a_2^*\) is fixed and central, hence is a scalar of modulus one. We obtain
\[
 \{b\in C:\theta_s(b)=e^{isp}b\ \forall s\}
   =\mathbb C a
 \quad\text{whenever this space is nonzero.}
\tag{MIV5.h}
\]
Products and adjoints give eigenunitaries at frequencies \(p+q\) and \(-p\), respectively. Thus the right side of (MIV5.c) is an additive group directly as well.

The closed period kernel \(K\) and the possibly nonclosed group \(T(P)\) encode different properties. Any \(s\in K\) and \(p\in T(P)\) satisfy
\[
 e^{isp}=1,
\tag{MIV5.i}
\]
because \(\theta_s\) fixes the eigenunitary. This necessary relation does not say that every character trivial on \(K\) occurs as an eigenfrequency. The irrational-flow example below will show why it is essential to distinguish the kernel from the complete eigenfrequency group.

<a id="miv-6"></a>
## 6. Periods, eigenfrequencies and a semifinite comparison

For a commutative flow \((C,\theta)\), distinguish its period group from its unitary eigenfrequency group:
\[
 \begin{aligned}
 K(C,\theta)&=\{s\in\mathbb R:\theta_s=\mathrm{id}_C\},\\
 \mathcal E(C,\theta)
 &=\{p\in\mathbb R:\text{some }a\in\mathcal U(C)
                    \text{ satisfies }\theta_s(a)=e^{isp}a
                    \text{ for every }s\}.
 \end{aligned}
 \tag{MIV6.a}
\]
The first records times; the second records frequencies, with the positive phase fixed in [Section 5](#miv-5). We calculate three complete commutative flows. Whenever such a flow is the center flow of a trace-scaling system whose crossing is a type III factor as in the setting, [Sections 3–5](#miv-3) give
\[
 S(P)=\{0\}\cup\exp K(C,\theta),\qquad
 T(P)=\mathcal E(C,\theta).
 \tag{MIV6.b}
\]
The commutative calculations alone do not construct any such factor or assert a factor-realization theorem. Their use of finite-dimensional tori is a property of these examples, not a restriction on the earlier arbitrary-predual theorem.

**The complete Fourier basis needed below.** Put \(\mathbb T=\mathbb R/\mathbb Z\), with normalized Lebesgue measure, and let \(d=1\) or \(2\). The functions
\[
 \chi_k(x)=e^{2\pi i k\cdot x},\qquad k\in\mathbb Z^d,
 \tag{MIV6.c}
\]
are orthonormal: integration of \(e^{2\pi i nt}\) over \([0,1]\) is \(0\) for a nonzero integer \(n\) and \(1\) for \(n=0\), and product integration handles \(d=2\). Here is a proof that their span is dense.

Translations are strongly continuous on \(L^2(\mathbb T)\) by [LFT7's arc-indicator argument](OA-FLOW-LFT.md#lft-7), which proves density of the interval step functions as well. Finite sums of products of such functions are dense in \(L^2(\mathbb T^2)\): this is the onto scalar-product identification in [L24, Proposition 4.2](OA-FLOW-L24.md#oa-flow.grp.vectorintegration), or directly its proof by finite simple functions and scalar Fubini. Translations of each product are norm continuous, by the triangle inequality and invariance of the two \(L^2\) norms. Uniform norm one then extends continuity to every vector in \(L^2(\mathbb T^2)\).

For \(N\ge1\) define the one-variable Fejér kernel
\[
 \begin{aligned}
 F_N(t)
 &=\frac1N\left|\sum_{j=0}^{N-1}e^{2\pi ijt}\right|^2\\
 &=\sum_{|k|<N}\left(1-\frac{|k|}{N}\right)e^{2\pi ikt},
 \qquad F_N\ge0,\qquad \int_{\mathbb T}F_N=1.
 \end{aligned}
 \tag{MIV6.d}
\]
The expansion counts pairs of indices with difference \(k\), proving all these assertions by finite sums and the preceding scalar integral. If the distance of \(t\) to \(\mathbb Z\) is at least \(\delta\), where \(0<\delta<1/2\), the geometric-sum formula gives
\[
 F_N(t)\le\frac1{N\sin^2(\pi\delta)}.
 \tag{MIV6.e}
\]
For \(d=2\) use \(K_N(t_1,t_2)=F_N(t_1)F_N(t_2)\), and for \(d=1\) put \(K_N=F_N\). The integral over the set where at least one coordinate has distance at least \(\delta\) from \(\mathbb Z\) is at most \(d/(N\sin^2(\pi\delta))\), by the union bound and the integral-one identities.

For \(f\in L^2(\mathbb T^d)\), its continuous translation orbit is Bochner integrable against \(K_N\); the elementary Hilbert integral estimate, also proved in [L24, Section 4](OA-FLOW-L24.md#oa-flow.grp.vectorintegration), gives
\[
 \|K_N*f-f\|_2
 \le\int_{\mathbb T^d}K_N(t)\|f(\,\cdot-t)-f\|_2\,dt
 \longrightarrow0.
 \tag{MIV6.f}
\]
Indeed first make the norm difference uniformly small near \(0\), and then use the displayed tail bound and the global bound \(2\|f\|_2\). Since \(L^2\subset L^1\) on this probability space, finite expansion of \(K_N\) and scalar integration show that \(K_N*f\) is a finite linear combination of the \(\chi_k\), with coefficient
\(\prod_{j=1}^d(1-|k_j|/N)\widehat f(k)\) when all \(|k_j|<N\), and zero otherwise. This proves completeness. In particular a nonzero \(L^2\) function has a nonzero Fourier coefficient, and two functions with the same coefficients agree in \(L^2\).

These arguments also verify continuity of the flows used below. Translations of multipliers are implemented on \(L^2(\mathbb T^d)\) by the strongly continuous translation unitaries, so their conjugations are pointwise ultraweakly continuous. The multiplication algebra, its inherited normal topology and its \(L^1\) predual are the full construction in [ND's multiplication lemma](OA-FLOW-ND.md#nd-multiplication).

**The circle of circumference \(a\).** Let \(a>0\), let
\(C_a=L^\infty(\mathbb R/a\mathbb Z,dr/a)\), and put
\[
 (\theta_s f)(r)=f(r+s),\qquad
 e_n(r)=e^{2\pi inr/a}.
 \tag{MIV6.g}
\]
Rescaling \(r=ax\) identifies the preceding orthonormal basis with \((e_n)_{n\in\mathbb Z}\), and
\[
 \theta_s(e_n)=e^{2\pi ins/a}e_n,\qquad
 K(C_a,\theta)=a\mathbb Z,\qquad
 \mathcal E(C_a,\theta)=\frac{2\pi}{a}\mathbb Z.
 \tag{MIV6.h}
\]
For the period assertion, \(s\in a\mathbb Z\) acts trivially; conversely triviality on \(e_1\) forces \(e^{2\pi is/a}=1\), hence \(s\in a\mathbb Z\). To prove the entire eigenfrequency assertion, suppose \(0\ne f\in C_a\) satisfies \(\theta_s(f)=e^{isp}f\) for all \(s\). If its coefficient at \(e_n\) is nonzero, comparison of that coefficient for all real \(s\) gives \(p=2\pi n/a\). Completeness ensures such a coefficient exists. Distinct integers have distinct frequencies, so all other coefficients vanish and \(f\) is a scalar multiple of \(e_n\). For a unitary \(f\), that scalar has modulus one. In particular the fixed functions are precisely the constants; this flow is ergodic.

Conditionally on the type III setting, (MIV6.b) therefore reads
\[
 \begin{aligned}
 S(P)&=\{0\}\cup\{e^{an}:n\in\mathbb Z\}\\
     &=\{0\}\cup\{\lambda^n:n\in\mathbb Z\},\qquad\lambda=e^{-a},\\
 T(P)&=\frac{2\pi}{a}\mathbb Z.
 \end{aligned}
 \tag{MIV6.i}
\]
The last equality of the two multiplicative groups uses \(n\mapsto-n\); it introduces no sign change in the eigenunitary equation.

**The scalar flow.** On \(C=\mathbb C1\) every complex-linear unital automorphism is the identity. Every nonzero scalar is fixed, so its eigenfrequency must be zero. Thus
\[
 C^\theta=\mathbb C1,\qquad K(C,\theta)=\mathbb R,\qquad
 \mathcal E(C,\theta)=\{0\}.
 \tag{MIV6.j}
\]
In the type III setting this gives \(S(P)=[0,\infty)\) and \(T(P)=\{0\}\). Here “scalar flow” means the action on a scalar center; it is different from the translation action on an algebra of scalar-valued functions considered below.

**An irrational Kronecker flow.** On \(C=L^\infty(\mathbb T^2)\), let
\[
 (\theta_s f)(x,y)=f(x+s,y+\sqrt2\,s),\qquad
 \chi_{m,n}(x,y)=e^{2\pi i(mx+ny)}.
 \tag{MIV6.k}
\]
Coordinates are taken modulo \(1\). Direct substitution gives
\[
 \theta_s(\chi_{m,n})
   =e^{\,2\pi i(m+\sqrt2\,n)s}\chi_{m,n}.
 \tag{MIV6.l}
\]
If \(m+\sqrt2\,n=0\) with integers \(m,n\), then \(m=n=0\), because \(\sqrt2\) is irrational. Its irrationality follows from the parity proof in [LFT7](OA-FLOW-LFT.md#lft-7). More generally these frequencies are distinct for distinct pairs.

For an invariant \(f\in C\), each nonconstant Fourier coefficient is zero: its coefficient must equal that coefficient times the nontrivial phase in (MIV6.l) for every \(s\). Completeness proves \(f\) constant, hence ergodicity. For any nonzero bounded eigenfunction with frequency \(p\), one nonzero Fourier coefficient gives \(p=2\pi(m+\sqrt2\,n)\). Distinctness and completeness show that this eigenfunction is a scalar multiple of the corresponding character. Consequently
\[
 K(C,\theta)=\{0\},\qquad
 \mathcal E(C,\theta)=2\pi(\mathbb Z+\sqrt2\,\mathbb Z).
 \tag{MIV6.m}
\]
To check the period group independently, triviality on \(\chi_{1,0}\) and \(\chi_{0,1}\) requires \(s\in\mathbb Z\) and \(\sqrt2\,s\in\mathbb Z\). Irrationality forces \(s=0\).

The eigenfrequency group is dense in \(\mathbb R\), despite being countable. Here is the full approximation argument. Pigeonholing the \(N+1\) fractional parts of \(0,\sqrt2,\ldots,N\sqrt2\) into \(N\) equal intervals produces integers \(q\ne0,p\) with
\[
 0<|q\sqrt2-p|<1/N.
 \tag{MIV6.n}
\]
Write \(\beta=|q\sqrt2-p|\), which belongs to \(\mathbb Z+\sqrt2\mathbb Z\). For any \(u\in\mathbb R\), choose an integer \(k\) nearest to \(u/\beta\). Then \(|u-k\beta|\le\beta/2<1/(2N)\). Letting \(N\) increase proves density, and multiplication by \(2\pi\) preserves it. The group is proper: \(1/2\notin\mathbb Z+\sqrt2\mathbb Z\), since a nonzero coefficient of \(\sqrt2\) would make it rational and a zero coefficient would make \(1/2\) an integer.

Thus, conditionally on the type III setting,
\[
 S(P)=\{0,1\},\qquad
 T(P)=2\pi(\mathbb Z+\sqrt2\,\mathbb Z),
 \tag{MIV6.o}
\]
and \(T(P)\) is a proper dense subgroup of \(\mathbb R\). A nonzero period of the center action and a nonzero eigenfrequency are different assertions.

**A trace-scaling translation whose crossing is semifinite.** This comparison deliberately drops the type III hypothesis. Let
\[
 N_0=L^\infty(\mathbb R,dx),\qquad
 \tau_0(f)=\int_{\mathbb R}e^x f(x)\,dx\quad(f\ge0),\qquad
 (\theta_s f)(x)=f(x+s).
 \tag{MIV6.p}
\]
The multiplier representation on \(L^2(\mathbb R,dx)\) is faithful and normal by ND's multiplication lemma. The weight is faithful since \(e^x>0\). It is normal: each integral restricted to \([-n,n]\) is a positive normal vector functional, represented by \(e^{x/2}1_{[-n,n]}\); their increasing supremum is the displayed weight and preserves bounded increasing positive suprema. It is a trace because the algebra is commutative. For \(f\in(N_0)_+\), the elements \(f1_{[-n,n]}\) increase to \(f\), and
\(\tau_0(f1_{[-n,n]})\le\|f\|(e^n-e^{-n})<\infty\). This proves semifiniteness on the whole positive cone. Substitution \(u=x+s\) gives
\[
 \tau_0(\theta_s f)=e^{-s}\tau_0(f).
 \tag{MIV6.q}
\]
The translation unitaries on \(L^2(\mathbb R)\) are strongly continuous: verify this first on compactly supported continuous functions by uniform continuity and a common compact bound, then use their scalar \(L^2\) density from [FF2](OA-FLOW-FF.md#oa-flow.ff.2). They implement \(\theta\), proving pointwise ultraweak continuity.

The center is all of \(N_0\). Its fixed functions are constants by [ND's convolution proof of translation invariance](OA-FLOW-ND.md#nd-weyl-proof), which applies to \(L^\infty(\mathbb R)\) without a finite measure assumption. Its periods and eigenfrequencies are
\[
 \begin{aligned}
 K(N_0,\theta)&=\{0\},\qquad
 \mathcal E(N_0,\theta)=\mathbb R,\\
 a_p(x)&=e^{ipx},\qquad\theta_s(a_p)=e^{isp}a_p.
 \end{aligned}
 \tag{MIV6.r}
\]
Every real number occurs in the eigenfrequency group. If \(\theta_s=\mathrm{id}\), the equality \(e^{ips}=1\) for every \(p\in\mathbb R\) forces \(s=0\).

We identify the entire crossing, including its representation multiplicity. Its regular representation on \(L^2(\mathbb R_r\times\mathbb R_x,dr\,dx)\) is
\[
 \begin{aligned}
 (\pi(f)\xi)(r,x)&=f(x-r)\xi(r,x),\\
 (u(s)\xi)(r,x)&=\xi(r-s,x).
 \end{aligned}
 \tag{MIV6.s}
\]
Set \(y=x-r,\ z=x\), and define
\[
 (W\xi)(y,z)=\xi(z-y,z),\qquad
 (W^*\eta)(r,x)=\eta(x-r,x).
 \tag{MIV6.t}
\]
The linear change of variables has absolute determinant \(1\). Scalar change of variables proves equality of norms; the displayed inverse proves onto unitarity. On all vectors the generators become
\[
 \begin{aligned}
 W\pi(f)W^*&=M_f\otimes I,\\
 Wu(s)W^*&=R_s\otimes I,\qquad (R_sg)(y)=g(y+s).
 \end{aligned}
 \tag{MIV6.u}
\]
In particular the sign of the translation is positive in \(y\), since replacing \(r\) by \(r-s\) replaces \(x-r\) by \(y+s\).

All first-factor multipliers occur, and they include \(e^{ipy}\). [ND's proved concrete Weyl lemma](OA-FLOW-ND.md#nd-weyl-proof) therefore gives
\[
 \begin{aligned}
 W(N_0\rtimes_\theta\mathbb R)W^*
   &=B(L^2(\mathbb R_y))\otimes I_{L^2(\mathbb R_z)},\\
 N_0\rtimes_\theta\mathbb R&\cong B(L^2(\mathbb R)).
 \end{aligned}
 \tag{MIV6.v}
\]
This is equality of the full generated von Neumann algebras. The map \(A\mapsto A\otimes I\) is normal by expanding vector coefficients in an orthonormal basis of the second factor and taking their absolutely summable series. Its inverse is normal as well: for any unit vector \(v\) in that factor, each coefficient \(\langle A\xi,\eta\rangle\) is the ambient coefficient at \(\xi\otimes v,\eta\otimes v\). Summable vector series give all normal functionals, as in ND's multiplication and tensor proofs. Thus (MIV6.v) is a normal isomorphism, with no missing multiplicity or proper-subalgebra assertion.

For completeness, the canonical trace on \(B(H)\), here \(H=L^2(\mathbb R)\), is
\[
 \operatorname{Tr}(A)=\sum_j\langle Ae_j,e_j\rangle
 \quad(A\ge0)
 \tag{MIV6.w}
\]
for an orthonormal basis. Nonnegative sums mean suprema of finite subsums. Faithfulness follows because all \(A^{1/2}e_j\) vanish if this sum is zero. Normality follows by interchanging two increasing suprema. The matrix-entry identity
\(\sum_j\|Ae_j\|^2=\sum_{i,j}|\langle Ae_j,e_i\rangle|^2
=\sum_i\|A^*e_i\|^2\)
proves the trace identity, including infinity. If \(q_F\) is the projection onto a finite set of basis vectors, then \(A^{1/2}q_FA^{1/2}\uparrow A\); its trace is at most \(|F|\|A\|\). This proves semifiniteness. The trace identity also gives invariance under unitary changes of basis, so the trace is independent of the chosen basis. The algebra is a factor since an operator commuting with every rank-one matrix unit is scalar. Rank-one projections are nonzero finite projections, so this factor is not type III.

By [TD1's full trace GNS proof](OA-FLOW-TD.md#oa-flow.td.1), its modular operator for \(\operatorname{Tr}\) is \(I\), so \(S(B(H))\subseteq\{1\}\). Conversely \(1\) belongs to the modular spectrum of every faithful normal semifinite weight \(\psi\): every modular action fixes the identity, so an integrable filter annihilating the action on all of \(B(H)\) has \(\int f(t)\,dt=0\). Thus \(0\) belongs to its action spectrum, and [MG1's arbitrary-weight full GNS spectral identity](OA-FLOW-MG.md#oa-flow.mg.1) gives \(1\in\operatorname{Sp}\Delta_\psi\). Finally [BC4's entire cocycle conjugacy formula](OA-FLOW-BC.md#bc-4), with the trace as reference, makes every \(\sigma_t^\psi\) inner. We have proved
\[
 \begin{aligned}
 S(N_0\rtimes_\theta\mathbb R)&=\{1\},\\
 T(N_0\rtimes_\theta\mathbb R)&=\mathbb R.
 \end{aligned}
 \tag{MIV6.x}
\]
The zero term in (MIV6.b) is therefore a substantive type III conclusion. Trace scaling, an ergodic center action and \(K=\{0\}\) by themselves do not supply it.

![Periods and eigenfrequencies of the circle and irrational torus flows, with the exact translation-crossing coordinate change](../assets/modular-invariants/modular-invariants.png)

The circle panel uses circumference \(a=\log4\), and labels a time \(s=a/4\) and its eigenfunction phase \(e^{2\pi is/a}=i\). The torus panel displays a finite segment of the exact curve \(s\mapsto(s,\sqrt2 s)\bmod\mathbb Z^2\); the drawn segment does not prove ergodicity or the Fourier-basis assertion. The frequency panel shows only the specified finite lattice sample \(2\pi(m+\sqrt2 n)\); density is proved by (MIV6.n), not inferred from the dots. The translation panel retains the coordinate \(z\) as a representation multiplicity and displays the entire crossing (MIV6.v). Conditional type III consequences require the setting of this lesson; no factor existence is inferred from these diagrams. For human-source context see [Further reading](#miv-reading). Original diagram, exact data and renderer: CC0-1.0 to the extent of rights held, with separate font terms. [Editable SVG](../assets/modular-invariants/modular-invariants.svg), [data](../assets/modular-invariants/data.json), [renderer](../assets/modular-invariants/render.py), and font terms are retained.

<a id="miv-7"></a>
## 7. Five solved diagnostics

**Diagnostic A: the period \(\log4\).** Suppose the center flow of a system satisfying the type III setting is the circle translation flow of circumference \(a=\log4\). Compute \(K,S(P),T(P)\), the parameter \(\lambda\), and a central eigenunitary for the smallest positive element of \(T(P)\).

**Solution.** Equations (MIV6.h)–(MIV6.i) give
\[
 \begin{aligned}
 K&=(\log4)\mathbb Z,&
 \lambda&=e^{-\log4}=\frac14,\\
 S(P)&=\{0\}\cup\{4^n:n\in\mathbb Z\},&
 T(P)&=\frac{2\pi}{\log4}\mathbb Z.
 \end{aligned}
 \tag{MIV7.a}
\]
The eigenunitary is \(a_1(r)=e^{2\pi ir/\log4}\), since
\(\theta_s(a_1)=e^{is(2\pi/\log4)}a_1\).
At \(s=(\log4)/4\) this multiplier is \(i\), and at \(s=\log4\) it is \(1\). The period \(a\) and the smallest positive frequency \(2\pi/a\) have different roles.

**Diagnostic B: a dense \(T\)-group with only two \(S\)-values.** Suppose instead that the center flow in the type III setting is the irrational torus flow (MIV6.k). Determine whether \(2\pi\sqrt2,\pi,2\pi(1-\sqrt2)\) belong to \(T(P)\). Does density of \(T(P)\) force \(T(P)=\mathbb R\) or force \(S(P)=[0,\infty)\)?

**Solution.** The characters \(e^{2\pi iy}\) and \(e^{2\pi i(x-y)}\) have frequencies \(2\pi\sqrt2\) and \(2\pi(1-\sqrt2)\), respectively. Both belong to \(T(P)\). If \(\pi\in T(P)\), then \(m+\sqrt2 n=1/2\) for integers \(m,n\), which is impossible by the argument after (MIV6.n). Thus
\[
 T(P)=2\pi(\mathbb Z+\sqrt2\mathbb Z)\ne\mathbb R,
 \qquad \overline{T(P)}=\mathbb R,\qquad S(P)=\{0,1\}.
 \tag{MIV7.b}
\]
The group is dense by the complete pigeonhole argument, while \(S(P)\) follows from the period group \(K=\{0\}\). Replacing \(T(P)\) by its closure would erase information.

**Diagnostic C: one sampled translation does not test flow ergodicity.** The torus flow satisfies \(\theta_1(e^{2\pi ix})=e^{2\pi ix}\). Does this contradict the ergodicity proved in Section 6? Is \(s=1\) a period of the flow?

**Solution.** Ergodicity concerns invariance for every real \(s\). Here
\[
 \theta_s(e^{2\pi ix})=e^{2\pi is}e^{2\pi ix},
 \qquad
 \theta_1(e^{2\pi iy})=e^{2\pi i\sqrt2}e^{2\pi iy}.
 \tag{MIV7.c}
\]
The first function is fixed at integer times but not, for example, at \(s=1/2\). The second is not fixed at \(s=1\), because \(\sqrt2\notin\mathbb Z\). Hence the time-one automorphism has nonconstant fixed functions and is not the identity, while the full real flow has only constant fixed functions and \(1\notin K\). Neither a finite trajectory plot nor the fixed algebra of a single sampled time replaces the full Fourier argument.

**Diagnostic D: test the sign of the implementing eigenunitary.** In the setting of this lesson, suppose \(a\in\mathcal U(Z(N))\) obeys \(\theta_s(a)=e^{isp}a\). Show directly on the coefficient and group generators that \(\operatorname{Ad}i(a)\) has the modular sign \(\sigma_p^\Phi(u(s))=e^{-ips}u(s)\). What changes if \(a\) is replaced by \(a^*\)?

**Solution.** The covariance relation is \(u(s)i(b)u(s)^*=i(\theta_s(b))\). Centrality of \(a\) makes conjugation by \(i(a)\) fix every \(i(x)\). On the group generator,
\[
 \begin{aligned}
 i(a)u(s)i(a)^*
 &=i\bigl(a\,\theta_s(a^*)\bigr)u(s)\\
 &=e^{-isp}u(s).
 \end{aligned}
 \tag{MIV7.d}
\]
These are exactly the two values of \(\sigma_p^\Phi\). Both automorphisms are normal, so equality on the generating families gives equality on the entire crossing. The adjoint \(a^*\) has eigenfrequency \(-p\) and implements \(\sigma_{-p}^\Phi\). Thus the positive phase in the center-flow eigenunitary equation and the negative modular phase on \(u(s)\) agree.

**Diagnostic E: the scalar-valued translation trap.** Take \(N_0,\tau_0,\theta\) from (MIV6.p). Since the center action is ergodic and has \(K=\{0\}\), may one conclude that its crossing is type \(\mathrm{III}_0\)? Compute the trace-scaling test at \(f=1_{[0,1]}\) and \(s=\log2\), and identify a nonzero finite projection in the crossing.

**Solution.** The full normal coordinate calculation (MIV6.s)–(MIV6.v) gives \(B(L^2(\mathbb R))\), so the proposed conclusion is false. Explicitly,
\[
 \begin{aligned}
 \tau_0(1_{[0,1]})&=e-1,\\
 \theta_{\log2}(1_{[0,1]})
   &=1_{[-\log2,\,1-\log2]},\\
 \tau_0\!\left(\theta_{\log2}(1_{[0,1]})\right)
   &=\frac{e-1}{2}.
 \end{aligned}
 \tag{MIV7.e}
\]
This verifies trace scaling without implying type III. For the unit vector \(g=1_{[0,1]}\in L^2(\mathbb R_y)\), let \(q=|g\rangle\langle g|\). The projection
\[
 W^*(q\otimes I_{L^2(\mathbb R_z)})W
 \tag{MIV7.f}
\]
belongs to the crossing by the proved onto algebra equality. It is finite as an algebra projection: its corresponding corner \(qB(L^2(\mathbb R_y))q\) is one-dimensional, and no proper nonzero subprojection can be equivalent to \(q\). Its canonical factor trace is \(1\), even though \(q\otimes I\) has an infinite-dimensional range in the regular representation. Thus representation multiplicity does not alter finiteness inside the algebra. The complete invariants here are \(S=\{1\}\), \(T=\mathbb R\), from (MIV6.x). The type III hypothesis is the missing premise; the phrase “scalar-valued functions” does not mean the scalar algebra \(\mathbb C\).

<a id="miv-product-times"></a>
## 8. Inner modular times for products of matrix states

We now change the setting: this section concerns a countable product of finite matrix factors, with no type assumption. For each \(n\ge1\), choose \(d_n\ge1\) and numbers
\[
 p_{n,j}>0,\qquad \sum_{j=1}^{d_n}p_{n,j}=1,\qquad
 D_n=\operatorname{diag}(p_{n,1},\ldots,p_{n,d_n}).
 \tag{MIV8.a}
\]
Put \(\varphi_n(x)=\operatorname{Tr}(D_nx)\) on \(M_{d_n}(\mathbb C)\). The trace here is the usual, unnormalized matrix trace. Represent this matrix algebra by left multiplication on its Hilbert–Schmidt space, pointed by \(D_n^{1/2}\), and form the pointed Hilbert tensor product. Let \(M\) be the von Neumann algebra generated by the finite tensor legs, and let \(\Omega=\bigotimes_nD_n^{1/2}\) and \(\varphi(x)=\langle x\Omega,\Omega\rangle\).

The earlier programme lesson Infinite tensor products, Theorems 4.1 and 5.1 and Proposition 5.2 proves the needed construction: \(M\) is a factor, \(\varphi\) is faithful and normal, and the product-state expectations \(E_m\) onto the first \(m\) legs converge strongly* to the identity on each element of \(M\). That lesson also proves that the relative commutant of these first legs is precisely the remaining tensor product. These conclusions use the finite factors and their faithful states, not an assertion about the type of \(M\).

On one Hilbert–Schmidt leg, the Tomita operator and its polar factors are
\[
 S_n(xD_n^{1/2})=x^*D_n^{1/2},\qquad
 J_nX=X^*,\qquad
 \Delta_n^{1/2}X=D_n^{1/2}XD_n^{-1/2}.
\]
Indeed \(J_n\Delta_n^{1/2}(xD_n^{1/2})=x^*D_n^{1/2}\), and the displayed positive operator is diagonal on the matrix units. The full product modular theorem, Theorem 6.1 of that earlier lesson, includes the Tomita graph closure and therefore gives
\[
 \sigma_t^\varphi(x)=D_n^{it}xD_n^{-it}
       \quad(x\text{ in leg }n).
 \tag{MIV8.b}
\]
The product modular operator is not being defined merely on a formal algebraic tensor product.

Set
\[
 z_n(t)=\sum_jp_{n,j}e^{it\log p_{n,j}},\qquad
 a_n(t)=|z_n(t)|.
 \tag{MIV8.c}
\]
The triangle inequality gives \(0\le a_n(t)\le1\). Then the exact answer is
\[
 \boxed{\quad T(M)=
   \left\{t\in\mathbb R:\sum_{n=1}^{\infty}(1-a_n(t))<\infty\right\}.\quad}
 \tag{MIV8.d}
\]
Here \(T(M)\) means inner modular times, as in Section 5. Its independence of the faithful normal state follows from the cocycle argument at the start of that section, which does not require the trace-scaling presentation or the type III assumption.

We prove (MIV8.d) and a useful estimate. Fix \(t\), suppress it in the notation, and multiply each \(D_n^{it}\) by a scalar of modulus one to obtain \(v_n\) with
\(\varphi_n(v_n)=a_n\ge0\). If \(z_n=0\), any phase works. Write \(V_m=v_1\cdots v_m\), with each factor embedded in its own tensor leg.

Suppose first that \(\sum_n(1-a_n)<\infty\). For \(x\) supported on the first \(m\) legs and \(\ell>m\), tensor factorization and unitarity give
\[
 \begin{aligned}
 \|(V_\ell-V_m)x\Omega\|^2
 &=2\|x\Omega\|^2
       \left(1-\prod_{m<n\le\ell}a_n\right)\\
 &\le2\|x\Omega\|^2\sum_{m<n\le\ell}(1-a_n).
 \end{aligned}
 \tag{MIV8.e}
\]
The last inequality follows inductively from
\(1-ab=(1-a)+a(1-b)\le(1-a)+(1-b)\) for \(a,b\in[0,1]\).
The same calculation holds for \(V_\ell^*-V_m^*\): the tail state values remain \(a_n\). Vectors \(x\Omega\) with finite support are dense. Since the partial products and their adjoints have norm one, these estimates give strong limits \(V\) and \(W\) of \(V_m\) and \(V_m^*\). Taking inner products identifies \(W=V^*\); taking strong limits of the bounded products \(V_m^*V_m\) and \(V_mV_m^*\) gives \(V^*V=VV^*=1\). Strong closedness puts \(V\) in \(M\). On every finite set of legs, \(\operatorname{Ad}V_m\) eventually equals (MIV8.b), so normality and generation give \(\operatorname{Ad}V=\sigma_t^\varphi\) on all of \(M\). Moreover,
\[
 \|(V-V_m)x\Omega\|
 \le \left(2\sum_{n>m}(1-a_n(t))\right)^{1/2}\|x\Omega\|
 \quad(x\text{ supported in the first }m\text{ legs}).
 \tag{MIV8.f}
\]

Conversely, suppose a unitary \(u\in M\) implements \(\sigma_t^\varphi\). On the first \(m\) legs it implements the same automorphism as \(V_m\); consequently \(V_m^*u\) belongs to their relative commutant. Applying the product-state expectation therefore gives
\[
 E_m(u)=c_mV_m,\qquad |c_m|\le1.
\]
Strong convergence \(E_m(u)\Omega\to u\Omega\) gives \(|c_m|\to1\). The expectation tower and product states imply, for \(\ell>m\),
\[
 c_m=c_\ell\prod_{m<n\le\ell}a_n.
 \tag{MIV8.g}
\]
Choose \(m\) with \(|c_m|>0\). Every tail factor \(a_n\), \(n>m\), is then nonzero, and every finite tail product is at least \(|c_m|\). Since \(1-a\le-\log a\) for \(0<a\le1\) (integrate \(1/s\ge1\) from \(a\) to \(1\)), we obtain
\[
 \sum_{m<n\le\ell}(1-a_n)
 \le-\log\prod_{m<n\le\ell}a_n
 \le-\log|c_m|.
\]
The nonnegative partial sums are bounded. The finite initial part adds a finite amount, proving necessity. This is the product-innerness argument of the earlier Theorem 7.2, specialized here with its coefficients and estimates explicit.

In particular, finitely many zero values of \(z_n(t)\) cause no obstruction. Nor does changing, deleting or inserting finitely many faithful matrix states change \(T(M)\). The criterion involves the tail sum, not positivity of the product beginning at \(n=1\). The phase choices above concern one fixed \(t\); no continuity of the chosen implementing unitary as a function of \(t\) has been asserted.

<a id="miv-product-dispersion"></a>
## 9. Phase dispersion and the exact state-period group

The criterion has a real, nonnegative form that makes both estimates and examples transparent. Define
\[
 \begin{aligned}
 d_n(t)&=1-|z_n(t)|^2\\
 &=\sum_{j,k}p_{n,j}p_{n,k}
       \left(1-\cos\left(t\log\frac{p_{n,j}}{p_{n,k}}\right)\right)\\
 &=\frac12\sum_{j,k}p_{n,j}p_{n,k}
       \left|e^{it\log(p_{n,j}/p_{n,k})}-1\right|^2.
 \end{aligned}
 \tag{MIV9.a}
\]
To verify this, expand \(z_n\overline{z_n}\). The imaginary terms cancel in pairs \(j,k\) and \(k,j\), while \(\sum_{j,k}p_{n,j}p_{n,k}=1\). The last equality is \(|e^{ir}-1|^2=2(1-\cos r)\). Since
\[
 1-a_n\le d_n=(1-a_n)(1+a_n)\le2(1-a_n),
\]
(MIV8.d) becomes
\[
 T(M)=\left\{t:\sum_nd_n(t)<\infty\right\}.
 \tag{MIV9.b}
\]
All pair weights are strictly positive. Thus \(d_n(t)=0\) holds exactly when every phase ratio in (MIV9.a) is one.

This description also gives the group and descriptive-topology properties without closing the group artificially. We have \(d_n(0)=0\), \(d_n(-t)=d_n(t)\), and
\[
 d_n(s+t)\le2d_n(s)+2d_n(t).
 \tag{MIV9.c}
\]
For the last inequality, apply
\[
 |e^{i(s+t)r}-1|
 \le |e^{isr}-1|+|e^{itr}-1|
\]
and \((A+B)^2\le2A^2+2B^2\) to every summand of (MIV9.a). Summing proves that the set in (MIV9.b) is a subgroup. Each finite partial sum is continuous. Consequently
\[
 T(M)=\bigcup_{K=1}^{\infty}
       \bigcap_{N=1}^{\infty}
       \left\{t:\sum_{n=1}^{N}d_n(t)\le K\right\}.
 \tag{MIV9.d}
\]
The inner intersections are closed, so this is an \(F_\sigma\) subgroup of \(\mathbb R\). Intersecting each of them with \([-m,m]\), \(m\ge1\), expresses the same group as a countable union of closed bounded, hence compact, subsets of \(\mathbb R\). Thus \(T(M)\) is sigma-compact in this countable matrix-product setting. This argument does not say it is closed.

A different group records when the chosen state's modular automorphism is actually the identity:
\[
 \begin{aligned}
 \operatorname{Per}(\varphi)
 &:=\{t:\sigma_t^\varphi=\operatorname{id}_M\}\\
 &=\left\{t:
 t\log(p_{n,j}/p_{n,k})\in2\pi\mathbb Z
 \text{ for every }n,j,k\right\}\\
 &=\{t:d_n(t)=0\text{ for every }n\}.
 \end{aligned}
 \tag{MIV9.e}
\]
Indeed (MIV8.b) multiplies a matrix unit \(e_{jk}\) in leg \(n\) by \(e^{it\log(p_{n,j}/p_{n,k})}\). Identity on \(M\) forces all these multipliers to be one; conversely that condition fixes the generating finite-leg algebras, hence all of \(M\). We therefore have \(\operatorname{Per}(\varphi)\subset T(M)\). This is the period group of the particular modular action, not the period group of the center flow in Sections 1–7. A finite change of the matrix states can change \(\operatorname{Per}(\varphi)\) even though it leaves \(T(M)\) unchanged.

<a id="miv-product-examples"></a>
## 10. Three explicit products and an implementer bound

**A repeated two-level state.** Fix \(c>0\), and at every leg take
\[
 D_n=\frac{\operatorname{diag}(1,e^{-c})}{1+e^{-c}},
 \qquad p=\frac1{1+e^{-c}},\quad q=\frac{e^{-c}}{1+e^{-c}}.
\]
There are two off-diagonal pairs in (MIV9.a), so
\[
 d_n(t)=2pq(1-\cos(ct)).
 \tag{MIV10.a}
\]
This nonnegative constant sequence has a finite sum precisely when it is zero. Equations (MIV9.b) and (MIV9.e) give
\[
 T(M)=\operatorname{Per}(\varphi)=\frac{2\pi}{c}\mathbb Z.
 \tag{MIV10.b}
\]
If instead \(c=0\), each density is scalar, and both groups are \(\mathbb R\).

**One exceptional first leg.** Take \(c=\sqrt2\) in the first leg and \(c=1\) in every later leg. Removing the first summand leaves the repeated-state criterion, so
\[
 T(M)=2\pi\mathbb Z.
\]
An exact period must satisfy \(t=2\pi k\) and \(\sqrt2\,t=2\pi l\) for integers \(k,l\). If \(k\ne0\), this says \(\sqrt2=l/k\), contradicting the irrationality proved in Section 6; hence
\[
 \operatorname{Per}(\varphi)=\{0\}.
 \tag{MIV10.c}
\]
At \(t=2\pi\) there is an especially simple implementer:
\[
 u=D_1^{i2\pi}\otimes1_{\mathrm{tail}}.
 \tag{MIV10.d}
\]
Every tail modular action is the identity. The first leg has eigenvalue ratio \(e^{i2\pi\sqrt2}\ne1\), so \(u\) is nonscalar and its conjugation is not the identity. This directly exhibits a nonzero inner modular time that is not an exact period of the chosen state.

**A summably small departure from the trace.** For \(n\ge1\), set
\[
 \varepsilon_n=\frac1{n+2},\qquad
 p_n=\frac{1+\varepsilon_n}{2},\qquad
 q_n=\frac{1-\varepsilon_n}{2},\qquad
 D_n=\operatorname{diag}(p_n,q_n).
 \tag{MIV10.e}
\]
Every state is faithful. Put
\(\ell_n=\log(p_n/q_n)=\log((1+\varepsilon_n)/(1-\varepsilon_n))\).
Since \(0<\varepsilon_n\le1/3\),
\[
 0<\ell_n
   =\int_{-\varepsilon_n}^{\varepsilon_n}\frac{ds}{1+s}
   \le\frac{2\varepsilon_n}{1-\varepsilon_n}
   \le3\varepsilon_n.
\]
The elementary bound \(1-\cos r=2\sin^2(r/2)\le r^2/2\) follows from \(|\sin v|\le|v|\), obtained by integrating \(\cos v\). Together with \(p_nq_n\le1/4\), it gives
\[
 d_n(t)=2p_nq_n(1-\cos(t\ell_n))
       \le\frac94\,t^2\varepsilon_n^2.
 \tag{MIV10.f}
\]
For \(m\ge0\), telescoping yields
\[
 \sum_{n>m}\varepsilon_n^2
 =\sum_{k=m+3}^{\infty}\frac1{k^2}
 \le\sum_{k=m+3}^{\infty}
       \left(\frac1{k-1}-\frac1k\right)
 =\frac1{m+2}.
 \tag{MIV10.g}
\]
Thus the dispersion series converges for every real \(t\), and \(T(M)=\mathbb R\). More quantitatively, the phase-adjusted products of Section 8 have a unitary limit \(V(t)\), and for \(m\ge1\),
\[
 \|(V(t)-V_m(t))x\Omega\|
 \le \frac{3|t|}{\sqrt{2(m+2)}}\,\|x\Omega\|
 \quad(x\text{ supported on the first }m\text{ legs}).
 \tag{MIV10.h}
\]
This is (MIV8.f) using \(1-a_n\le d_n\) and (MIV10.f)–(MIV10.g). It bounds convergence on each local vector, not the operator norm.

Nevertheless \(\operatorname{Per}(\varphi)=\{0\}\). The first two eigenvalue ratios are \(2\) and \(5/3\). A nonzero exact period would give
\(t\log2=2\pi k\) and \(t\log(5/3)=2\pi l\) with nonzero integers \(k,l\) of the same sign. Eliminating \(t\) and exponentiating gives
\[
 2^{|l|}3^{|k|}=5^{|k|},
\]
an even integer equal to an odd integer. This is impossible. Here every modular time is inner, but no nonzero time fixes the entire algebra pointwise.

![Partial dispersion sums for the repeated binary state and a sequence approaching the trace.](../assets/product-modular-times/product-modular-times.png)

*Figure 2.* The horizontal coordinate is \(r=t/(2\pi)\). On the left, the repeated state with \(c=1\) has partial sum \(N\,2pq(1-\cos(2\pi r))\); its zeros at integer \(r\) persist for every \(N\), while the sum diverges at every other fixed \(r\). On the right, the nearly tracial states (MIV10.e) have bounded partial sums. The shaded strip above the \(N=256\) curve has height \((9/4)(2\pi r)^2/(256+2)\), the proved bound for the omitted tail from (MIV10.f)–(MIV10.g). Curves are numerical samples of the displayed formulas; the convergence and exact group statements are established by the proofs. [Vector figure](../assets/product-modular-times/product-modular-times.svg), [reproducible renderer](../assets/product-modular-times/render.py), [sample values and formulas](../assets/product-modular-times/data.json).

These computations determine \(T(M)\) and \(\operatorname{Per}(\varphi)\) for the stated products. They do not by themselves compute \(S(M)\), an asymptotic ratio set, or the factor's type. The finite-prefix example explains why exact state periods cannot replace inner modular times in those further questions.

<a id="miv-countable-support"></a>
## 11. Countable support inside an arbitrary tensor product

The finite-leg construction is available for an arbitrary index set \(I\), including an uncountable one. At index \(i\), take a finite matrix factor and a faithful state as in (MIV8.a), with density \(D_i\). Use the pointed product representation and denote its product state by \(\varphi\). For \(J\subset I\), write \(M_J\) for the von Neumann subalgebra generated by the legs in \(J\), represented with the identity on the complementary tensor factor. The earlier programme product construction and grouping theorem prove
\[
 M=M_J\ \overline\otimes\ M_{I\setminus J};
\]
both factors and the product state are faithful in the indicated representations. For \(I=\varnothing\), the convention is \(M=\mathbb C\).

Here is a distinction that will be useful: **each individual operator of \(M\) belongs to some \(M_J\) with \(J\) countable.** The set \(J\) may depend on the operator. There need not be one countable \(J\) that contains the entire algebra.

We prove the assertion without choosing a sequence cofinal among all finite subsets of \(I\). For a fixed \(x\in M\), the finite-part expectations satisfy
\[
 E_F(x)\Omega\longrightarrow x\Omega,\qquad
 E_F(x)^*\Omega\longrightarrow x^*\Omega
 \quad(F\subset I\text{ finite},\ F\uparrow I).
 \tag{MIV11.a}
\]
Choose nested finite sets \(F_1\subset F_2\subset\cdots\) so that both errors in (MIV11.a) are less than \(2^{-n}\) at \(F_n\). This is possible by the definition of convergence of the two nets: after finding their finite thresholds, enlarge their union to contain \(F_{n-1}\). Put \(J=\bigcup_nF_n\) and \(x_n=E_{F_n}(x)\in M_J\). The sequence is uniformly bounded by \(\|x\|\).

The product vector is cyclic for \(M'\), by the faithful-state proof in Proposition 5.2. For \(y'\in M'\), commutation gives
\[
 \|(x_n-x)y'\Omega\|
 =\|y'(x_n-x)\Omega\|
 \le\|y'\|\,2^{-n}.
\]
For an arbitrary \(\xi\in H\), approximation by \(y'\Omega\) gives
\[
 \|(x_n-x)\xi\|
 \le2\|x\|\,\|\xi-y'\Omega\|+\|y'\|\,2^{-n}.
 \tag{MIV11.b}
\]
First make the approximation term small, then let \(n\) tend to infinity. The same argument applies to the adjoints. Thus \(x_n\to x\) strongly*, and the strong closedness of \(M_J\) puts \(x\) in \(M_J\). This proves countable support. For any countable family \(x_1,x_2,\ldots\), the union of their countable supports is countable, so the entire von Neumann algebra they generate lies in one such \(M_J\).

The approximation in (MIV11.b) concerns a fixed operator and the dense commutant orbit. It does not assert that the full Hilbert space is separable, that \(I\) is countable, or that one sequence of finite-part expectations works simultaneously for all operators.

<a id="miv-arbitrary-times"></a>
## 12. The modular-time criterion without an index restriction

Define \(z_i(t),a_i(t),d_i(t)\) by the same finite matrix formulas as in (MIV8.c) and (MIV9.a). For nonnegative numbers \((b_i)_{i\in I}\), the meaning of their sum is
\[
 \sum_{i\in I}b_i
 :=\sup_{F\subset I\ {\rm finite}}\sum_{i\in F}b_i
 \quad\text{in }[0,\infty].
 \tag{MIV12.a}
\]
If this number is finite, only countably many \(b_i\) are nonzero. To see this, each set \(\{i:b_i\ge1/k\}\) is finite: otherwise finite subsets of arbitrarily large cardinality would make the sums unbounded. Their countable union contains every index with \(b_i>0\).

For the full arbitrary product, the exact formula is
\[
 \boxed{\quad
 T(M)=
 \left\{t:\sum_{i\in I}(1-a_i(t))<\infty\right\}
 =
 \left\{t:\sum_{i\in I}d_i(t)<\infty\right\}.
 \quad}
 \tag{MIV12.b}
\]
The single-leg modular formula remains (MIV8.b): the earlier full product modular theorem was proved for arbitrary \(I\), using finite-subset nets and full graph cores. The second equality in (MIV12.b) follows from
\(1-a_i\le d_i\le2(1-a_i)\) by taking finite sums and suprema.

For necessity, suppose \(\sigma_t^\varphi=\operatorname{Ad}u\) with a unitary \(u\in M\). Section 11 places \(u\) in \(M_J\) for some countable \(J\). On every leg outside \(J\), conjugation by \(u\) is the identity. Hence the modular action on that leg is the identity. The matrix-unit calculation of Section 9 says that all eigenvalue phases of \(D_i^{it}\) agree, so \(a_i(t)=1\) and \(d_i(t)=0\) there. On \(M_J\), the product modular action is implemented by the same \(u\). If \(J\) is countably infinite, Section 8 proves summability over \(J\). If \(J\) is finite, the sum is finite directly. Thus the unrestricted sum in (MIV12.b) is finite.

For sufficiency, let that sum be finite and put
\[
 A_t=\{i\in I:1-a_i(t)>0\}.
 \tag{MIV12.c}
\]
This set is countable by the argument after (MIV12.a). Outside \(A_t\), the positive pair weights in (MIV9.a) force every phase ratio to be one, so the modular action is the identity. On \(M_{A_t}\), Section 8 supplies an implementing unitary. In the finite or empty case the finite product, or the scalar unit, does so. Embed this unitary in \(M\). Its conjugation is the required modular action on \(M_{A_t}\) and the identity on the complementary factor; these two algebras generate \(M\). This proves sufficiency on the whole algebra.

The implementer can also be recovered as a net over finite subsets, with an explicit error bound. Fix \(t\in T(M)\), and choose \(v_i=\zeta_iD_i^{it}\) so that \(\varphi_i(v_i)=a_i(t)\ge0\). For \(i\notin A_t\), this choice gives \(v_i=1\). Indeed
\(\varphi_i((v_i-1)^*(v_i-1))=2-2\operatorname{Re}\varphi_i(v_i)=0\), and faithfulness gives the assertion. For finite \(F\subset I\), put \(V_F=\prod_{i\in F}v_i\). If \(E\supset F\) and \(x\in M_F\), product factorization gives
\[
 \|(V_E-V_F)x\Omega\|^2
 =2\|x\Omega\|^2\left(1-\prod_{i\in E\setminus F}a_i(t)\right).
 \tag{MIV12.d}
\]
Enumerate the countable set \(A_t\) and use its unitary limit from Section 8. For fixed \(F\), apply (MIV12.d) to the finite unions of \(F\) with the initial segments of that enumeration. Passing to the limit yields
\[
 \|(V-V_F)x\Omega\|
 \le\left(2\sum_{i\notin F}(1-a_i(t))\right)^{1/2}\|x\Omega\|.
 \tag{MIV12.e}
\]
The omitted sum tends to zero along the finite-subset net. Indeed, if the total sum is \(L<\infty\), choose a finite \(F_0\) whose sum exceeds \(L-\varepsilon\). For any finite \(E\subset I\setminus F_0\), its sum is at most \(L-\sum_{F_0}(1-a_i)<\varepsilon\); taking a supremum gives the same tail bound. This remains true for \(F\supset F_0\).

For each fixed local vector, eventually \(F\) also contains its support. Equation (MIV12.e), and the corresponding adjoint estimate, then prove \(V_F\to V\) strongly*. The unitary obtained is independent of the enumeration of \(A_t\), because every enumeration has the same finite-net limit. No enumeration of the uncountable set \(I\) has been used.

The state-period criterion likewise becomes
\[
 \operatorname{Per}(\varphi)
 =\{t:d_i(t)=0\text{ for all }i\in I\}\subset T(M).
 \tag{MIV12.f}
\]
As before, it follows by testing matrix units in every leg and then using normality on the generated algebra.

<a id="miv-countable-detection"></a>
## 13. One countable subproduct detects all modular times

The countable support of a particular implementer depends on its time parameter. A separate argument gives a single countable set of legs that detects the invariant for every time simultaneously.

We first prove a scalar lemma. Let \((f_i)_{i\in I}\) be any family of nonnegative continuous functions on \(\mathbb R\), and define
\[
 F(t)=\sup_{A\subset I\ {\rm finite}}\sum_{i\in A}f_i(t).
\]
There is a countable \(J\subset I\) such that
\[
 F(t)=\sum_{i\in J}f_i(t)\qquad(t\in\mathbb R),
 \tag{MIV13.a}
\]
including at points where either side is infinite.

For the proof, fix a nonnegative rational \(q\). The set
\[
 U_q=\{t:F(t)>q\}
 =\bigcup_{A\subset I\ {\rm finite}}
      \left\{t:\sum_{i\in A}f_i(t)>q\right\}
 \tag{MIV13.b}
\]
is open. Consider all open intervals with rational endpoints. For each such interval \(B\) that is contained in
\(\{\sum_{i\in A}f_i>q\}\) for at least one finite \(A\), select one such finite set \(A_{q,B}\). There are only countably many pairs \((q,B)\); the union \(J\) of their selected finite sets is therefore countable.

If \(t\in U_q\), some finite sum exceeds \(q\) at \(t\). Its continuity supplies an open neighborhood on which the inequality persists. Density of the rationals gives a rational-endpoint interval \(B\) containing \(t\) inside that neighborhood. The selected set \(A_{q,B}\), whether or not it is the original witness, still has sum greater than \(q\) at \(t\). Since \(A_{q,B}\subset J\), the sum over \(J\) exceeds \(q\). Conversely, a sum over \(J\) cannot exceed \(F\). Thus the two nonnegative extended-real quantities have exactly the same strict rational lower bounds at every \(t\). If they differed, a rational between them would separate those bounds, also when the larger value is infinite. This proves (MIV13.a).

Apply the lemma to \(f_i=d_i\), which is continuous and nonnegative by its finite phase formula. For the resulting countable \(J\), (MIV12.b) and (MIV12.f) give
\[
 \boxed{\quad
 T(M)=T(M_J),\qquad
 \operatorname{Per}(\varphi)
   =\operatorname{Per}(\varphi|_{M_J}).
 \quad}
 \tag{MIV13.c}
\]
The same \(J\) works at all times, and it preserves the entire dispersion function, not just its finiteness set. The restricted product state is faithful, and its modular action is the restriction on these tensor legs. If \(J\) is finite, its \(T\)-group is all of \(\mathbb R\), as (MIV12.b) also shows.

There is also a common location for the implementers. If \(t\in T(M)\), the sum over \(J\) in (MIV13.a) is finite. For \(i\notin J\), adjoining \(i\) to finite subsets of \(J\) gives
\(\sum_{k\in I}d_k(t)\ge\sum_{k\in J}d_k(t)+d_i(t)\); equality in (MIV13.a) therefore forces \(d_i(t)=0\). Thus the modular action is the identity outside \(J\) at every inner time, and Section 8 supplies an implementing unitary inside this same \(M_J\) for each such time. This is a choice of location, not a claim that the implementing unitaries can be chosen continuously in time.

The argument of Section 9 now applies to the countable subproduct. Hence \(T(M)\) is an \(F_\sigma\), sigma-compact subgroup even for the arbitrary product. One can also see closedness of the level sets directly:
\[
 \left\{t:\sum_{i\in I}d_i(t)\le K\right\}
 =\bigcap_{A\subset I\ {\rm finite}}
     \left\{t:\sum_{i\in A}d_i(t)\le K\right\}.
\]
An arbitrary intersection of closed sets is closed. The countable union over integer \(K\), followed by intersection with bounded closed intervals, gives the same conclusion. Neither proof asserts closedness of \(T(M)\) itself.

**A large algebra can have a very small detector.** Let \(I\) be uncountable and take \(D_i=\tfrac12 1_2\) at every leg. All \(d_i\) vanish; the empty subproduct detects both groups, which are \(\mathbb R\). Nevertheless the full algebra has nonseparable predual. To prove this directly, let \(z_i=\operatorname{diag}(1,-1)\) in leg \(i\) and put \(\eta_i(x)=\varphi(z_i x)\). These are normal functionals of norm one: bounded multiplication preserves normality, \(|\eta_i(x)|\le\|x\|\), and \(\eta_i(z_i)=1\). Product independence gives
\[
 \eta_j(z_i)=0\quad(i\ne j),\qquad
 \|\eta_i-\eta_j\|\ge1.
 \tag{MIV13.d}
\]
If the predual had a countable dense subset, choose a member within distance \(1/3\) of each \(\eta_i\). One member cannot serve two different indices, by the triangle inequality. This would inject the uncountable set \(I\) into a countable set, a contradiction. Also, no countable coordinate subproduct is all of \(M\): for \(i\notin J\), every element of \(M_J\) commutes with the matrix unit \(e_{12}\) in leg \(i\), whereas \([z_i,e_{12}]=2e_{12}\ne0\). Thus countable detection in (MIV13.c) is an equality of invariants, not a countable generation or an isomorphism assertion.

**Continuously many two-level states.** At each \(c\in[1,2]\), take
\[
 D_c=\frac{\operatorname{diag}(1,e^{-c})}{1+e^{-c}},\qquad
 d_c(t)=2\,\frac{e^{-c}}{(1+e^{-c})^2}\,(1-\cos(ct)).
 \tag{MIV13.e}
\]
For fixed \(t\ne0\), only finitely many \(c\in[1,2]\) satisfy \(ct\in2\pi\mathbb Z\): the integer multiples involved lie in a bounded interval. Choose an interior \(c_0\) outside that finite set. By continuity in \(c\), there are an open interval \(B\subset[1,2]\) and \(\delta>0\) with \(d_c(t)>\delta\) for all \(c\in B\). Selecting arbitrarily many distinct indices in \(B\) makes the finite sums arbitrarily large. At \(t=0\), every summand is zero. Therefore
\[
 T(M)=\operatorname{Per}(\varphi)=\{0\}.
 \tag{MIV13.f}
\]
In this example one explicit detector is \(J=\mathbb Q\cap[1,2]\). Every nonempty open interval contains arbitrarily many distinct rationals: recursively choose one in each of finitely many disjoint subintervals. The same lower bound on \(B\) therefore proves divergence already over \(J\) at every nonzero \(t\). This detector has the full dispersion sum \(0\) at zero and \(+\infty\) elsewhere. No factor-type conclusion is being drawn from (MIV13.f).

![Phase dispersion for continuously indexed binary states and the countable detection mechanism.](../assets/uncountable-product-times/uncountable-product-times.png)

*Figure 3.* Left: numerical samples of the continuous scalar function in (MIV13.e), with \(r=t/(2\pi)\) and \(1\le c\le2\). The marked zero curves satisfy \(rc\in\mathbb Z\). At each nonzero fixed \(r\), a whole interval of \(c\)-values has a positive lower bound, which forces the unrestricted sum to be infinite; rational indices already suffice. Right: the exact quantifier structure of the rational-interval selection in (MIV13.b). It selects countably many finite sets of indices, whose union preserves all rational threshold tests and therefore the entire extended dispersion function. The diagram records logical steps and assigns no geometry or cardinality scale to the tensor-index set. Proofs and limitations are in Sections 11–13. [Vector figure](../assets/uncountable-product-times/uncountable-product-times.svg), [renderer](../assets/uncountable-product-times/render.py), [formulas and sample data](../assets/uncountable-product-times/data.json).

<a id="miv-reading"></a>
## Further reading

M. Takesaki, *Theory of Operator Algebras II*, Chapter XII, §1, Definition 1.5 and Theorem 1.6, printed pp. 368–370, introduce the modular spectrum and modular period group and connect them with the flow of weights. The all-weight argument here uses the complete arbitrary-cardinal corner amplification and unrestricted cocycle reconstruction proved earlier in the programme. It does not identify an arbitrary nonzero corner of a large factor with the whole factor.

The distinction between an individual modular spectrum and their intersection is developed in [The full weight spectral identity](OA-FLOW-MG.md#oa-flow.mg.1). The [arbitrary-cardinal cocycle intersection](OA-FLOW-L120.md#ci-intersection) is the step that makes the present all-weight theorem independent of a separable-predual restriction. [Zero in every modular spectrum](OA-FLOW-MT.md#mt-1) explains the type III zero term. The examples retain separate calculations of kernel, eigenfrequency group, and modular intersection so that these invariants are not conflated.

For the original infinite-product setting, see H. Araki and E. J. Woods, [A Classification of Factors](https://ems.press/journals/prims/articles/2441), available as a [free article PDF](https://ems.press/content/serial-article-files/41616?nt=1). Sections 8–10 use the complete product construction and innerness arguments already proved in the programme and give the summability and exact-period calculations explicitly.
