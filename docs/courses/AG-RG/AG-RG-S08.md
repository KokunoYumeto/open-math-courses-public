# Supporting proofs for the consumed group-scheme foundations

This lesson supplies the additional arguments consumed from the earlier group-scheme lessons, before their use in the following reductive-group lessons. The statements retain their field, characteristic, finiteness and base hypotheses. Definitions of a group scheme, a character, an fpqc form and a quasi-coherent representation are definitions, rather than theorem obligations.

The earlier algebra proofs used below are the current programme lessons, with their actual locators specified at the point of use. Those locators refer to written proofs. External free sources at the end explain provenance; none replaces a proof below or the stated earlier proof. The separate general flat quotient proof is Flat quotient bootstrap, Theorem 8.2 and Corollary 8.3; the further field scheme-quotient argument remains in the earlier quotient lesson.

## G.0. The component structure used in the field-group proof

<a id="canonical-flat-components"></a>

**Lemma G.0.1 (canonical flat closed structure).** Let \(X\) be any scheme and let \(Y\subset |X|\) be closed and stable under generalization. There is exactly one closed subscheme \(X_Y\subset X\) with underlying space \(Y\) whose inclusion is flat. Every scheme morphism \(f:T\to X\) with \(f(|T|)\subset Y\) factors uniquely through \(X_Y\). This structure commutes with base change, when the underlying subset is replaced by its inverse image. In particular it applies to every connected component of any scheme and retains its ambient local rings, including their nilpotents.

**Proof.** Begin with \(X=\operatorname{Spec}A\) and define
\[
 I_Y=\ker\left(A\longrightarrow\prod_{\mathfrak q\in Y}A_{\mathfrak q}\right).
\]
If \(Y\) is empty, this means \(I_Y=A\). For every \(\mathfrak q\in Y\), \((I_Y)_{\mathfrak q}=0\). We show that \((I_Y)_{\mathfrak p}=A_{\mathfrak p}\) for \(\mathfrak p\notin Y\). Write \(Y=V(K)\), and choose \(f\in K\setminus\mathfrak p\). Every prime of \(A_{\mathfrak q}\), for \(\mathfrak q\in Y\), comes from a prime contained in \(\mathfrak q\), hence still in \(Y\) by generalization stability. Thus \(f/1\) lies in every prime of \(A_{\mathfrak q}\). The prime-intersection proof in AG-RG-S04, Lemma P0.1 makes it nilpotent. Consequently there are \(n_{\mathfrak q}>0\) and \(s_{\mathfrak q}\notin\mathfrak q\) with \(s_{\mathfrak q}f^{n_{\mathfrak q}}=0\) in \(A\).

The opens \(D(s_{\mathfrak q})\) cover the closed subset \(Y\) of the quasi-compact affine scheme. Choose finitely many of them and let \(N\) be the largest of their exponents. At every \(\mathfrak r\in Y\), some chosen \(s_{\mathfrak q}\) is a unit in \(A_{\mathfrak r}\), so \(f^N/1=0\) there. Hence \(f^N\in I_Y\), while \(f^N\notin\mathfrak p\). This proves the assertion outside \(Y\). It also proves \(V(I_Y)=Y\).

Each localization of \(A/I_Y\), as an \(A\)-module, is therefore \(A_{\mathfrak p}\) if \(\mathfrak p\in Y\) and zero otherwise. It is flat at every prime, hence flat over \(A\) by the earlier localization criterion in AG-CA, *Tor and flat modules*, Theorem 3.3. That criterion follows by localizing every tensor-injection kernel and using the zero-module localization test. Thus \(\operatorname{Spec}(A/I_Y)\) is the required flat closed subscheme.

For uniqueness, suppose \(A/J\) is flat over \(A\) and \(V(J)=Y\). For \(\mathfrak p\in Y\), the quotient map \(A_{\mathfrak p}\to A_{\mathfrak p}/J_{\mathfrak p}\) is a flat local map of nonzero local rings, hence faithfully flat by AG-CA, *Faithful flatness and the local criterion for flatness*, Theorem 2.1. Flatness tensors the injection \(J_{\mathfrak p}\hookrightarrow A_{\mathfrak p}\) to an injection into \(A_{\mathfrak p}/J_{\mathfrak p}\), whose image is zero. Faithful flatness makes \(J_{\mathfrak p}=0\). For \(\mathfrak p\notin Y\), \(J_{\mathfrak p}=A_{\mathfrak p}\). Thus \(J\) and \(I_Y\) have the same localizations at all primes and are equal, by the earlier zero-module localization test applied to their sums and quotients.

If \(f:T\to\operatorname{Spec}A\) has image in \(Y\), any \(a\in I_Y\) is zero in \(A_{f(t)}\) at each \(t\in T\). Its image is therefore zero in \(\mathcal O_{T,t}\). A section whose every stalk is zero is zero, so \(f\) kills \(I_Y\) and factors through the quotient. Uniqueness follows from the closed immersion being a monomorphism.

On an affine open of a general \(X\), use this construction for its intersection with \(Y\). Restrictions to further affine opens remain flat closed subschemes with that same underlying subset, so affine uniqueness identifies the restrictions. Their quotient ideals glue and give \(X_Y\). The same local uniqueness proves global uniqueness and the factorization assertion. Under any base change, the pulled-back closed subscheme is flat and has the inverse-image underlying subset; that subset is closed and stable under generalization. Uniqueness proves the asserted compatibility.

A connected component is closed: the closure of a connected set is connected, since any separation of the closure by two nonempty relatively open sets would meet the dense original set on both sides and separate it. Maximality thus makes the closure the component itself. It is stable under generalization: if \(y\) is in the component and \(x\) generalizes \(y\), every nonempty open in the closure of \(\{x\}\) contains \(x\), so that closure is irreducible and connected and contains \(y\). Its union with the component is connected: a separation of the union would put both intersecting connected sets on the side containing their common point. Maximality therefore puts \(x\) in the component. The construction thus applies. The localized quotient at a point of the component is exactly the ambient local ring, as already computed. \(\square\)

<a id="algebraic-extension-connectedness"></a>

**Lemma G.0.2 (the algebraic-extension connectedness step).** Let \(X\) be a connected scheme over a field \(k\) with a \(k\)-rational point. Then \(X_L\) is connected for every algebraic field extension \(L/k\), including infinite extensions and imperfect fields. No finiteness or reducedness assumption on \(X\) is needed.

**Proof.** The projection \(p:X_L\to X\) is integral and closed. On an affine chart its algebra is \(A\otimes_kL\), the filtered union of the finite \(A\)-algebras \(A\otimes_kE\), where \(E/k\) ranges over finite subextensions. Every element is therefore integral over \(A\). The actual integral closed-image proof is AG-RG-S04, Lemma P0.4, applied also to quotients defining closed subsets.

This projection is open as well. Every principal open \(D(b)\subset\operatorname{Spec}(A\otimes_kL)\) is the pullback of such an open at one finite subextension \(E\), since \(b\) has finitely many coefficients. The projection to \(\operatorname{Spec}(A\otimes_kE)\) is surjective, by faithful flatness of the field extension \(L/E\) and its prime-fibre argument. Thus the image of this principal open in \(\operatorname{Spec}A\) equals its image at that finite level. The finite-dimensional algebra \(E/k\) is free as a vector space, and finitely presented as an algebra: a finite basis generates it, and the polynomial presentation kernel is finite by the Hilbert basis proof in AG-RG-S01, Lemma 1.3. Its base change is therefore flat and finitely presented, hence open by AG-FSE, *Flat morphisms*, Theorem 3.2. Principal opens form a basis, proving openness of \(p\) without a finite-presentation assumption on \(L/k\).

If \(X_L=U\amalg V\) were a decomposition into nonempty clopen subsets, both images \(p(U)\) and \(p(V)\) would be nonempty clopen subsets of the connected \(X\), hence both would equal \(X\). The fibre at the rational point is \(\operatorname{Spec}L\), which has one point. It cannot meet both disjoint \(U\) and \(V\). This contradiction proves the assertion, including inseparable extensions. \(\square\)

<a id="field-group-components"></a>

**Lemma G.0.3 (the consumed field-group identity component).** Let \(G/k\) be a group scheme locally of finite type over any field. Its connected components are open, closed and irreducible. The component \(G^0\) through the identity, with its open subscheme structure, is a normal, geometrically irreducible, quasi-compact subgroup; its inclusion is a flat closed immersion and its formation commutes with every field extension. No reducedness or characteristic assumption is imposed.

**Proof.** The complete earlier proof of AG-GS-03, Theorem 1.3 says that every point belongs to exactly one irreducible component, and that the component through the identity is geometrically irreducible. Every affine chart is Noetherian. Its finitely many irreducible components are pairwise disjoint, so each is open and closed there. The closure in \(G\) of a chart component is a global component: a larger irreducible closed subset would meet the chart in an irreducible closed subset containing that chart component, hence equal it by maximality; this nonempty open is dense in the larger irreducible subset, so their closures coincide. Conversely a global component meeting the chart has that same intersection, by uniqueness through each point. Thus the global components are open as well as closed and pairwise disjoint. They are exactly the connected components. In particular a connected locally finite-type group is irreducible.

Let \(C\) be the identity component with the open subscheme structure. Its inclusion is flat and closed, so Lemma G.0.1 identifies it with the canonical structure. The geometric irreducibility of Theorem 1.3 also applies to this structure: on each Noetherian affine chart reduction is a nilpotent closed immersion, and after every field extension its nilpotent ideal still gives the same underlying space. The geometric irreducibility assertion about the reduced component therefore gives the assertion about \(C\) with its original nilpotents.

The product \(C\times C\) is irreducible, by the actual product proof preceding AG-GS-03, Theorem 1.3, applied after algebraic closure and retaining the nilpotent thickenings on its affine charts. Its multiplication image contains the identity, so is in the component \(C\). Inversion preserves that component too. Lemma G.0.1 factors both morphisms through \(C\), and the group identities follow from the closed immersion being a monomorphism.

For any field extension \(K/k\), \(C_K\) is connected and contains the identity, so lies in its connected component \(D\) in \(G_K\). Conversely \(D\) projects into \(C\), since its connected image contains the identity. Lemma G.0.1 factors its projection through \(C\), hence puts \(D\) inside \(C_K\). The two underlying spaces coincide, and both are flat closed subschemes of \(G_K\); uniqueness in Lemma G.0.1 proves \(D=C_K\). For every field-valued \(g\in G(K)\), conjugation preserves this identity component. Every point of \(G\times C\) can be lifted to such a field-valued pair. Consequently conjugation has set-theoretic image in \(C\), and Lemma G.0.1 factors the entire conjugation morphism through \(C\). This proves normality schematically.

Finally extend to an algebraic closure. Choose a nonempty affine open \(U\subset C_{\overline k}\). For every rational point \(g\), irreducibility makes \(gU\cap U\) nonempty, and the Nullstellensatz supplies a rational point in this intersection. Hence \(g=u_1u_2^{-1}\) for \(u_1,u_2\in U(\overline k)\). The image of \(U\times U\to C_{\overline k}\) under \((u_1,u_2)\mapsto u_1u_2^{-1}\) is open. Indeed \(C_{\overline k}\) is flat and locally finitely presented over the field, so projection from its product is open by AG-FSE, *Flat morphisms*, Theorem 3.2. The shear isomorphism \((a,b)\mapsto(ab^{-1},b)\) identifies this projection with \((a,b)\mapsto ab^{-1}\). Restricting an open map to the open subset \(U\times U\) preserves openness. This proves exactly the locally finite-type case of AG-GS-03, Proposition 1.1 needed here. Its closed complement, if nonempty, would have a rational point on a finite-type affine chart by the Nullstellensatz. Thus the image is all of \(C_{\overline k}\). A continuous image of the quasi-compact affine \(U\times U\) is quasi-compact. The surjective projection to \(C\) then makes \(C\) quasi-compact as well. This proves all assertions. \(\square\)

Lemmas G.0.1 and G.0.3 supply the precise identity-component inputs consumed from AG-GS-03, Theorems 2.2–2.3 in the following reductive-group lessons. Their geometric connectedness and product connectedness follow from the proved geometric irreducibility, rather than an additional arbitrary-scheme theorem. Lemma G.0.2 independently supplies the algebraic-extension connectedness step.

For free comparison, the corresponding canonical identity-component statement is [Stacks, Proposition 39.7.11, Tag 0B7R](https://stacks.math.columbia.edu/tag/0B7R), and the geometric irreducibility input is [Tag 047M](https://stacks.math.columbia.edu/tag/047M). The complete arguments used here are the proofs above and the exact earlier programme proofs they specify.

## G.1. Dimension at a point after field extension

We use the earlier proofs in AG-CA, *Krull dimension and Noether normalization*, Corollary 3.2, Theorems 4.2 and 6.1: normalization over a polynomial ring, dimension as transcendence degree for a finite-type domain, and dimension at a point as the largest dimension of a component through it. We also use *Associated primes and primary decomposition*, Theorem 3.2 and Theorem 1.2, for minimal primes being associated and the associated-prime description of zero divisors. For an integral inclusion, going up lifts every finite prime chain and incomparability makes the contraction of every strict chain strict, so the two dimensions agree. These two assertions have their complete earlier proofs in Descent and Zariski Main, Lemma P0.4; its normal going-down proof P0.8 supplies the further input used by the earlier normalization dimension argument.

**Lemma G.1.1 (flat going down).** If \(A\to B\) is flat, \(\mathfrak q\subset B\) contracts to \(\mathfrak p\subset A\), and \(\mathfrak p_0\subset\mathfrak p\), there is \(\mathfrak q_0\subset\mathfrak q\) contracting to \(\mathfrak p_0\).

**Proof.** The local map \(A_{\mathfrak p}\to B_{\mathfrak q}\) is flat and faithfully flat. The latter assertion is proved in AG-CA, *Faithful flatness and the local criterion for flatness*, Theorem 2.1: a proper ideal of the source lies in its maximal ideal and its extension lies in the target maximal ideal, so the residue-field test for faithful flatness applies. Consequently
\[
B_{\mathfrak q}\otimes_{A_{\mathfrak p}}\kappa(\mathfrak p_0)
\]
is a nonzero ring. A maximal ideal of it gives a prime of \(B_{\mathfrak q}\) over \(\mathfrak p_0A_{\mathfrak p}\), by the fibre prime correspondence of AG-CA, *Localization, local properties and support*, Theorem 3.2. Contracting this prime to \(B\) proves the assertion. This is also the complete earlier proof in *Tor and flat modules*, Theorem 6.3. \(\square\)

**Lemma G.1.2.** Let \(X\) be locally of finite type over a field \(k\), let \(K/k\) be any field extension, and let \(y\in X_K\) lie over \(x\in X\). Then
\[
\dim_yX_K=\dim_xX.
\]

**Proof.** Work on an affine finite-type neighbourhood, with algebra \(A\). First suppose \(A\) is a domain of dimension \(d\). Choose a normalization \(P=k[t_1,\ldots,t_d]\subset A\), finite over \(P\). Put \(F=\operatorname{Frac}P\). The inclusion
\[
A\hookrightarrow A\otimes_PF\simeq F^r
\]
is an injection of \(P\)-modules for some finite \(r\). Tensoring over \(k\) preserves injection and embeds \(A_K\) into
\[
(F\otimes_kK)^r.
\]
Here \(F\otimes_kK\) is a localization of the domain \(P_K=K[t_1,\ldots,t_d]\). Thus \(A_K\) is torsion-free over \(P_K\), as well as finite over it. A minimal prime \(\mathfrak q\) of the Noetherian ring \(A_K\) is associated. It cannot contain a nonzero element of \(P_K\), since such an element acts injectively on \(A_K\). Therefore \(P_K\to A_K/\mathfrak q\) is an integral inclusion and every component of \(\operatorname{Spec}A_K\) has dimension \(d\).

For general \(A\), flat going down shows that every minimal prime of \(A_K\) contracts to a minimal prime of \(A\). Indeed, a smaller prime downstairs could be lifted below it, contrary to minimality. If \(\mathfrak q\) is a minimal prime upstairs contracting to \(\mathfrak p\), it is minimal in the quotient \((A/\mathfrak p)_K\), so the preceding domain argument gives component dimension \(\dim(A/\mathfrak p)\).

Conversely, for every minimal \(\mathfrak p\subset\mathfrak p_x\), Lemma G.1.1 lifts \(\mathfrak p\) below the prime of \(y\); choosing a minimal prime below that lift produces an upstairs component through \(y\) contracting to \(\mathfrak p\). Thus the component dimensions through \(y\) are exactly those through \(x\). The point-dimension formula of AG-CA, *Krull dimension and Noether normalization*, Theorem 6.1 takes their maximum on each side and proves the equality. \(\square\)

This supplies the field-extension step in AG-GS-02, Lemma 3.1 and Theorem 3.2, without identifying point dimension with local-ring dimension at a nonclosed point.

## G.2. Smoothness descends under field extension

**Lemma G.2.1.** For a locally finite-type \(k\)-scheme \(X\) and a field extension \(K/k\), if \(X_K/K\) is smooth, then \(X/k\) is smooth.

**Proof.** It suffices to treat an affine chart \(S=k[X_1,\ldots,X_n]/I\). The polynomial ring is Noetherian by the earlier Hilbert basis theorem, so \(I\) has a finite generating list and \(S\) is finitely presented. Its conormal sequence is
\[
I/I^2\longrightarrow S^n\longrightarrow\Omega_{S/k}\longrightarrow0.
\]
Formation of every term and map commutes with the flat scalar extension \(k\to K\), by the polynomial presentation and conormal calculation in AG-CA, *Kähler differentials*, Theorems 3.3 and 5.1. Upstairs smoothness makes the conormal arrow injective and \(\Omega_{S_K/K}\) finite projective: this is proved by the lifting argument in AG-CA, *Formally smooth, unramified and étale ring maps*, Theorem 3.1. Smoothness is local on the affine chart, so these properties hold on the whole upstairs module by localization and the earlier local criterion for finite projectivity.

Faithful scalar extension detects the kernel of the conormal arrow. Finite projectivity of \(\Omega_{S/k}\) descends by AG-CA, *Faithful flatness and the local criterion for flatness*, Corollary 3.2. The conormal sequence downstairs is consequently split exact. The converse lifting construction in the same Theorem 3.1 then makes \(S\) formally smooth: for a square-zero test, the error on \(I/I^2\) extends to the free polynomial differential module using this splitting, and subtracting that derivation corrects all defining equations. Finite presentation now makes \(S\) smooth. Apply this to each affine chart. \(\square\)

No perfectness hypothesis occurs in this descent argument.

## G.3. The local regularity step in Cartier's theorem

The local assertions needed here have complete earlier programme proofs: Nakayama in AG-CA, *Localization, local properties and support*, Theorem 4.2; Krull intersection in *Noetherian and Artinian rings*, Theorem 6.1; the one-equation dimension theorem in *Dimension theory of Noetherian local rings*, Theorem 3.2; and rational closed-point smoothness in *Smooth algebras over a field and the Jacobian criterion*, Proposition 3.1 and Theorem 2.1.

**Lemma G.3.1 (lifting regularity).** If \((R,\mathfrak m)\) is Noetherian local, \(f\in\mathfrak m\) is a nonzerodivisor, and \(R/fR\) is regular local, then \(R\) is regular local.

**Proof.** Put \(D=\dim R\). The earlier one-equation theorem gives \(\dim(R/fR)=D-1\). Lift \(D-1\) generators of the quotient maximal ideal. Together with \(f\) they generate \(\mathfrak m\), so the embedding dimension of \(R\) is at most \(D\). The reverse inequality follows from the earlier height theorem, applied to a minimal generating list of \(\mathfrak m\). Thus embedding dimension equals dimension. This is exactly regularity. The same proof is already AG-CA, *Regular local rings*, Proposition 1.3; this explicit restatement replaces the external proof link used at the end of AG-GS-02, Lemma 4.2. \(\square\)

**Lemma G.3.2.** Suppose \(R\) is a Noetherian local algebra over a characteristic-zero field, \(f\in\mathfrak m\), and a derivation \(\delta:R\to R\) satisfies \(\delta(f)=1\). Then \(f\) is a nonzerodivisor.

**Proof.** If \(fa=0\), the iterated product rule gives
\[
f\delta^n(a)+n\delta^{n-1}(a)=0\qquad(n\geq1).
\]
Since \(n!\) is invertible,
\[
a=(-1)^n\frac{f^n\delta^n(a)}{n!}\in f^nR.
\]
Krull intersection gives \(a=0\). \(\square\)

**Lemma G.3.3.** Let \(k\) be algebraically closed of characteristic zero, let \(\mathfrak m\) be a closed point of a finite-type \(k\)-algebra, and let \(R\) be its local ring. If \(\Omega_{R/k}\) is free, then \(R\) is regular.

**Proof.** Its residue field is \(k\), by the earlier Nullstellensatz. The rational-point cotangent calculation identifies
\[
\mathfrak m/\mathfrak m^2\simeq\Omega_{R/k}\otimes_R k.
\]
Let the free rank be \(r\), and induct on \(r\). If \(r=0\), Nakayama gives \(\mathfrak m=0\). If \(r>0\), choose \(f\in\mathfrak m\) with \(df\) nonzero modulo \(\mathfrak m\). One coordinate of \(df\) in a free basis is a unit. Elementary changes of basis therefore make \(df\) a basis vector. The functional taking value \(1\) on it corresponds, by the universal differential property, to a derivation with \(\delta(f)=1\). Lemma G.3.2 makes \(f\) a nonzerodivisor.

The quotient conormal sequence gives
\[
\Omega_{(R/fR)/k}
=\bigl(\Omega_{R/k}\otimes_RR/fR\bigr)/(R/fR)\,df,
\]
which is free of rank \(r-1\). The induction hypothesis makes \(R/fR\) regular, and Lemma G.3.1 makes \(R\) regular. \(\square\)

**Theorem G.3.4 (Cartier, with the consumed scope).** A group scheme locally of finite type over a characteristic-zero field is smooth.

**Proof.** Extend the field to its algebraic closure. The cotangent sheaf of any group scheme is
\[
\Omega_{G/k}\simeq\mathcal O_G\otimes_k e^*\Omega_{G/k}.
\]
The complete earlier proof is AG-GS-02, Proposition 2.7: the automorphism \((g,x)\mapsto(g,gx)\) over the first factor carries the identity section to the diagonal, and its relative differential gives the displayed identification. In the present locally finite-type scope, \(e^*\Omega\) is a finite-dimensional vector space, so the cotangent sheaf is free.

Every closed point of each finite-type affine chart is rational. Lemma G.3.3 makes its local ring regular; the earlier rational-point Jacobian criterion makes that point smooth. The nonsmooth locus is closed on the chart by the earlier open-locus proof. If nonempty it has a rational closed point by the Nullstellensatz, a contradiction. Hence the group is smooth after algebraic closure. Lemma G.2.1 descends smoothness to the original field. This proof permits infinitely many components and makes no global affineness or quasi-compactness assumption. \(\square\)

<a id="universal-schematic-density"></a>

**Lemma G.3.5 (universal schematic density).** Let $p:X\to S$ be smooth, with geometrically irreducible nonempty fibres, and let $U\subset X$ be an open whose intersection with every fibre is dense. After every base change $S'\to S$, the restriction $\mathcal O_{X_{S'}}\to (j_{S'})_*\mathcal O_{U_{S'}}$ is injective, where $j_{S'}:U_{S'}\hookrightarrow X_{S'}$. Consequently two maps from $X_{S'}$ to a separated $S'$-scheme which agree on $U_{S'}$ agree everywhere.

**Proof.** Schematic density is local on the source and the base. Choose a smooth affine chart $V\to\operatorname{Spec}R$ of finite presentation. Its image in the base is open. Over each principal base open contained in that image, replace $R,V$ by their restrictions; then every fibre of $V$ is nonempty. It is geometrically integral: after a geometric field extension it is a nonempty open of the smooth irreducible fibre of $X$, hence reduced and irreducible. An empty chart contributes no condition.

Write $V=\operatorname{Spec}A$. The principal opens $D(f)\subset U\cap V$ cover $U\cap V$. Their base images are open because their morphisms to the base are smooth. They cover $\operatorname{Spec}R$: the dense $U_s$ meets each nonempty $V_s$. Quasi-compactness of this affine base therefore selects finitely many $f_1,\ldots,f_m$ whose base images cover it. No quasi-compactness of $U$ has been assumed.

Use AG-RG-S02 Theorem 4.5 to choose a smooth affine model $V_0=\operatorname{Spec}A_0$ over a finitely generated $\mathbf Z$-algebra $R_0$, with geometrically connected nonempty fibres. These fibres are geometrically integral by the smooth component argument in its Lemma 4.1. Enlarge the coefficient ring to retain the finitely many $f_i$, using the finite-presentation map and equality proof. All these enlargements are base changes of that model. In the Noetherian model the base images $W_i$ of $D(f_i)$ are open and constructible; their union $E$ pulls back to the whole final base. AG-RG-S02 Lemma 4.4 therefore gives a finite coefficient stage at which their pullbacks cover the base. We retain this finite stage and its specified functions.

On each $W_i$ every fibre of $V_0$ is integral and $f_i$ is nonzero in it, because $D(f_i)$ has a point in that fibre. At a local ring of $V_0$ where $f_i$ is not a unit, the local map from the corresponding Noetherian base local ring is flat and $f_i$ is regular in its closed fibre. The written slicing proof in [*Faithful flatness and the local criterion for flatness*, Theorem 5.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/faithful-flatness-and-the-local-criterion-for-flatness.html#5-lifting-a-regular-equation-from-the-fibre), shows that multiplication by $f_i$ is injective and that its cokernel is flat over that base local ring. Where $f_i$ is a unit the same conclusions are immediate, with zero cokernel. Thus, locally over $W_i$, the sequence
\[
0\longrightarrow\mathcal O_{V_0}\xrightarrow{f_i}\mathcal O_{V_0}\longrightarrow\mathcal O_{V_0}/f_i\mathcal O_{V_0}\longrightarrow0
\]
remains exact after every base change: the last module is base-flat, so its first Tor vanishes. This assertion is made on affine base charts and their affine inverse images, and then glues.

It follows that, after base change first to $R$ and then to any $R$-algebra, restriction to $D(f_i)$ is injective on every open of the inverse image of $W_i$. Indeed an element killed by localization is killed by a power of $f_i$, and injectivity of multiplication by $f_i$ and of all its localizations makes that element zero. A function vanishing on $U$ vanishes on every such $D(f_i)$. The $W_i$ cover the base, so it vanishes on $V$. The argument applies after every further base change and on all source charts, proving the sheaf injection. Finally the equalizer of two maps to a separated target is closed; its defining ideal restricts to zero on $U_{S'}$, so the injection makes that ideal zero everywhere. $\square$

## G.4. The reduced products used in the closed-orbit argument

**Lemma G.4.1.** Over an algebraically closed field, the product of two reduced finite-type schemes is reduced, and the product of two integral finite-type schemes is integral.

**Proof.** On affine charts let the algebras be \(A,B\). The earlier Nullstellensatz says that an element of \(A\) vanishing at every \(k\)-point is zero when \(A\) is reduced. For a tensor \(u=\sum_i a_i\otimes b_i\), choose the \(b_i\) linearly independent over \(k\). If all evaluations of \(u\) at \(k\)-points of \(\operatorname{Spec}A\) are zero in \(B\), coefficient independence makes each \(a_i\) vanish at every such point, so \(u=0\). If \(u\) is nilpotent and \(B\) is reduced, each of those evaluations is zero. This proves reducedness.

If \(A,B\) are domains and \(u,v\) are nonzero tensors, the locus in \(\operatorname{Spec}A\) where the evaluation of \(u\) is nonzero contains a nonempty open: choose one nonzero coefficient in an independent expression. The analogous open for \(v\) meets it, since \(\operatorname{Spec}A\) is irreducible. Their intersection has a \(k\)-point. At this point both evaluations are nonzero in the domain \(B\), so their product is nonzero. Thus \(uv\ne0\). Finite affine covers give the stated scheme assertions. \(\square\)

**Theorem G.4.2 (the closed-orbit argument).** Let a smooth finite-type group \(G\) over an algebraically closed field \(k\) act on a nonempty reduced separated finite-type \(k\)-scheme \(X\). The reduced orbits are locally closed, and \(X\) contains a closed orbit.

**Proof.** Choose \(x\in X(k)\). Let \(O\) be the topological image of \(G\to X\), \(g\mapsto gx\), and let \(Y\) be its reduced closure. The earlier Noetherian Chevalley proof is AG-MO, *Quasi-finite morphisms and Chevalley*, Theorems 3.1 and 4.2, with Lemma 4.1. Its dense-open step uses the fully proved normalization and lying-over arguments: normalize the generic affine algebra over \(\operatorname{Frac}A\), clear the finitely many denominators in the monic equations, then use lying over on the resulting finite algebra over a polynomial ring. Noetherian induction gives constructibility on every closed subset.

Consequently \(O\) is constructible and contains a dense open \(U\) of \(Y\). The union \(V=\bigcup_{g\in G(k)}gU\) is open in \(Y\) and contained in \(O\). It contains all rational points of \(O\): a nonempty orbit-map fibre is finite type and has a rational point, so \(G(k)\) is transitive on those points. The constructible subset \(O\setminus V\), if nonempty, has a rational point; hence it is empty. Thus \(O\) is open in \(Y\), proving local closedness.

Translations preserve \(Y\). The action restricts schematically to \(Y\) and to \(O\). Indeed Lemma G.4.1 makes \(G\times Y\) reduced. Each defining equation of \(Y\) pulls back to a function vanishing at every rational point, so the Nullstellensatz makes it zero. The inverse image of the boundary \(Y\setminus O\) under the restricted action on \(G\times O\) is a closed subset with no rational point and is therefore empty.

For completeness, the components of smooth \(G\) are open and disjoint: its local rings are regular domains by the earlier smoothness and regular-local proofs, so two distinct irreducible components cannot meet. There are finitely many components. Its identity component \(G^0\) is therefore irreducible. Lemma G.4.1 makes \(G^0\times G^0\) irreducible; multiplication and inversion preserve the component containing the identity, so \(G^0\) is a subgroup. Every component contains a rational point and is a translate of \(G^0\).

The closures of the images of those finitely many translated components under the orbit map are translates of one irreducible closed set, and have a common dimension \(d\). They cover \(Y\); after repetitions are removed they are precisely its irreducible components. The boundary meets each component in a proper closed subset, so every boundary component has dimension less than \(d\). This strict inequality is the earlier finite-type domain dimension theorem: a nonzero prime in a finite-type domain lowers the transcendence degree and hence the dimension.

Choose an orbit of minimum dimension; this is possible among the nonnegative integers since \(X(k)\ne\varnothing\). If its boundary were nonempty, that boundary would contain a rational point, whose orbit lies in it by invariance and has smaller dimension. This contradicts minimality. The chosen orbit is closed. The same argument inside any orbit closure or nonempty invariant closed reduced subscheme gives a closed orbit there. \(\square\)

For arbitrary finite-type \(G\), without smoothness or reducedness, retain AG-GS-03, Lemma 7.12 and Theorem 7.13 with their original scheme structures. Their generic monomorphism argument is compatible with nilpotents: at a minimal prime the target ring is Artinian; a finite-type algebra with the same residue field becomes finite because its lifted generators differ from scalars by nilpotents; a finite monomorphism is a closed immersion by the residue-field test and Nakayama. Schematic dominance then makes it an isomorphism on a generic open. Translating that open proves the orbit immersion once the scheme quotient \(G/H\) exists. The full quotient and schematic-orbit arguments retain their separate exact earlier proofs; this reduced closed-orbit theorem does not change their scheme structures.

## G.5. The semilinear descent used for character modules

**Lemma G.5.1 (independence of automorphisms).** Distinct automorphisms \(\sigma_1,\ldots,\sigma_s\) of a field \(K\) are linearly independent over \(K\) as functions \(K\to K\).

**Proof.** In a nonzero relation with the fewest terms, normalize the first coefficient to \(1\). A relation with one term is impossible by evaluation at \(1\). Choose \(b\) with \(\sigma_1(b)\ne\sigma_j(b)\) for another participating automorphism. Evaluate the relation at \(bx\) and subtract \(\sigma_1(b)\) times the relation at \(x\). The first term disappears and the \(j\)-th term remains. This is a shorter nonzero relation, a contradiction. \(\square\)

**Lemma G.5.2 (finite Galois descent).** Let \(K/k\) be finite Galois with group \(\Delta\), and let \(V\) be any \(K\)-vector space with a semilinear \(\Delta\)-action. Then
\[
K\otimes_kV^\Delta\longrightarrow V,\qquad a\otimes v\longmapsto av
\]
is an isomorphism. Equivariant maps descend uniquely. Tensor products, algebras, Hopf operations and their identities descend through this isomorphism.

**Proof.** Lemma G.5.1 shows that the vectors \((\sigma(b))_{\sigma\in\Delta}\), \(b\in K\), span \(K^\Delta\) as a \(K\)-vector space: otherwise a nonzero linear functional annihilating their span would give a relation among the automorphisms. Consequently there are finite lists \(a_i,b_i\in K\) such that
\[
\sum_i a_i\sigma(b_i)=
\begin{cases}1&\sigma=1,\\0&\sigma\ne1.\end{cases}
\]
For \(v\in V\) set \(w_i=\sum_{\sigma\in\Delta}\sigma(b_iv)\). These vectors are invariant, and
\[
\sum_i a_iw_i=v.
\]
This proves surjectivity, with no finite-dimensionality hypothesis on \(V\).

Vectors in \(V^\Delta\) independent over \(k\) remain independent over \(K\). Otherwise choose a shortest relation among them and normalize its first coefficient to \(1\). Applying any \(\sigma\) and subtracting gives a shorter relation, so all its coefficients are fixed by \(\Delta\), hence belong to \(k\). This contradicts the original independence. A \(k\)-basis of \(V^\Delta\) therefore proves injectivity.

An equivariant map preserves invariant vectors, and the displayed isomorphisms recover it from its restriction. They also identify the scalar extension of \(V^\Delta\otimes_kW^\Delta\) with \(V\otimes_KW\), compatibly with descent. An equivariant unit, multiplication, comultiplication, counit or antipode thus descends as a map on invariant spaces. The algebra and Hopf identities can be checked after the injective scalar extension to \(K\).

If the \(K\)-algebra \(V\) is finitely generated, write a finite generating list as finite linear combinations of invariant vectors. Let \(B_0\) be the \(k\)-algebra generated by those finitely many invariant vectors in \(B=V^\Delta\). Then \(K\otimes B_0=V=K\otimes B\), so faithful scalar extension detects \(B/B_0=0\). Thus \(B=B_0\) is finite type and is finitely presented by the earlier Hilbert basis theorem. \(\square\)

The usual field facts in this argument can be checked without an unstated descent theorem. In a finite normal separable extension, count embeddings by adjoining generators one at a time: each embedding of the preceding field extends by choosing one of the distinct roots of the next minimal polynomial. Normality puts all these embeddings in the field itself, giving \(|\Delta|=[K:k]\). If \(F=K^\Delta\), Lemma G.5.1 shows \(|\Delta|\leq[K:F]\): apply its spanning argument to an \(F\)-basis of \(K\). The degree tower then gives \(F=k\). A finite separable extension embeds in a finite normal separable extension by adjoining the finitely many roots of the minimal polynomials of its generators; every embedding permutes those root sets. These arguments justify the fixed-field and normal-closure facts used here.

**Corollary G.5.3.** For a finitely generated abelian group \(M\) with a continuous action of \(\operatorname{Gal}(k_s/k)\), choose a finite Galois splitting quotient \(\Delta=\operatorname{Gal}(K/k)\). The semilinear action
\[
\sigma(ae^m)=\sigma(a)e^{\sigma m}
\]
on \(K[M]\) descends all its Hopf operations to
\[
B=K[M]^\Delta,\qquad K\otimes_kB=K[M].
\]
The descended group has geometric character group \(M\), with the prescribed action. Equivariant character homomorphisms descend uniquely in the reverse direction.

**Proof.** The intersection of the open stabilizers of a finite generating list is open and fixes all of \(M\); the kernel is consequently an open normal subgroup, giving the finite Galois quotient. Apply Lemma G.5.2 to \(K[M]\) and its displayed operations. The character calculation is the coefficient proof already written in AG-GS-05, Lemma 2.1 and Theorem 2.2: a group-like element over a connected field is one monomial, so a Hopf map is precisely its homomorphism on exponents. Transport of that monomial is exactly \(e^m\mapsto e^{\sigma m}\). This proves the assertion and supplies the descent step of AG-GS-05, Theorem 5.2. \(\square\)

AG-GS-05, Theorem 5.0 has its full separable-splitting argument: finite-dimensional subcoalgebras cover the Hopf algebra; the scheme of group-like elements in one is finite étale because its scalar extension is a finite disjoint union of points; over \(k_s\) each such point descends; the resulting monomials form the entire Hopf basis after faithful extension. Its finite splitting-field step is Lemma 5.1, where finitely many expressions for an algebra isomorphism and its inverse descend to a finite separable field and then a finite Galois field. These arguments do not assume perfectness of \(k\). They remain required earlier written proofs, together with the affine descent argument of AG-GS-04.

## Free provenance and rights

The source comparisons for point dimension and field descent are the freely accessible official Stacks Project, [02FX](https://stacks.math.columbia.edu/tag/02FX), [02FY](https://stacks.math.columbia.edu/tag/02FY) and [0CDR](https://stacks.math.columbia.edu/tag/0CDR). The proof arguments actually needed in this draft have been supplied above, with the named earlier programme algebra proofs.

For the character classification the verified free author version is J. S. Milne, *Algebraic Groups*, version 2.00, 20 December 2015, [author PDF](https://www.jmilne.org/math/CourseNotes/iAG200.pdf), Chapter 14, especially Theorem 14.17. Its numbering is specific to that free version. The later corrected author edition is also freely accessible: [5 October 2021 text, published in 2022](https://www.jmilne.org/math/Books/iAG2022.pdf). That edition uses Chapter 12 for character classification. Edition-specific locators must be matched to the cited free PDF; both free versions remain valid comparison sources.

## History

Source and modification history: Stacks Project authors and the named earlier programme authors, earlier algebra and descent proofs; OpenAI GPT-6.1 Sol, supporting arguments and explicit prerequisite reconciliation, 5 October 2026. This combined supporting draft is distributed under GNU Free Documentation License, version 1.2 or any later version, with no Invariant Sections, no Front-Cover Texts and no Back-Cover Texts. The complete [GNU FDL 1.2](assets/GFDL-1.2.txt) accompanies this edition. Copyright (C) 2005–2025 Johan de Jong is retained in the adapted Stacks material. The independently written additions may also be used under CC0. Existing GFDL source rights are retained.
