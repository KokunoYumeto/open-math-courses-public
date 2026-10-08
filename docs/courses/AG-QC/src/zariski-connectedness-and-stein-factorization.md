# Zariski's connectedness theorem and Stein factorization

*Written by GPT-6.1 Sol (OpenAI), in Codex at Ultra, October 2026. Self-checked by the writing AI. Original text: public domain (CC0); Appendix A follows constructions of the Stacks Project, which it cites. See the course notice.*

A proper morphism can collapse a connected curve, identify several points, or carry a field extension in its constants. Its algebra of functions distinguishes these phenomena. Stein factorization puts the functions into a finite intermediate scheme; the remaining map has geometrically connected fibers. The theorem on formal functions explains why: a disconnected fiber would supply a compatible idempotent on every infinitesimal neighborhood, and hence an idempotent in a completed local ring.

We use [formal functions](the-theorem-on-formal-functions.md), [proper coherent direct images](proper-morphisms-and-coherent-direct-images.md), and [flat base change](base-change-and-the-grothendieck-complex.md). Relative Spec, its universal property and affine reconstruction are proved in the existing earlier *Affine morphisms, relative Spec, and finite morphisms*, Theorem 1.1 and Corollary 2.2. The earlier *Discrete valuation rings, normal rings and Serre's criterion* supplies normal rings; the proper birational application is proved here. Connected means nonempty throughout. Unless stated otherwise, the base is locally Noetherian.

## 1. Connected components as idempotents

For any scheme \(T\), a decomposition into open and closed subschemes
\[
T=T_1\amalg T_2
\]
defines an idempotent \(e\in\Gamma(T,\mathcal O_T)\): it is one on \(T_1\) and zero on \(T_2\). Conversely, an idempotent determines such a decomposition. At each point, its germ in the local ring is either zero or one. Indeed \(e(1-e)=0\), and at least one of \(e,1-e\) is a unit in a local ring; multiplication by that unit makes the other zero. The loci where these germs are one and zero are respectively \(D(e)\) and \(D(1-e)\). They are disjoint opens covering \(T\), so are also closed.

Thus a nonempty scheme is connected exactly when its global function ring has no idempotents except zero and one. This does not assert that its ring of functions is a field, reduced, or equal to the ground field.

**Lemma 1.1 (idempotents across a thickening).** If \(T_0\hookrightarrow T\) is a closed immersion defined by a nilpotent ideal, restriction induces a bijection on global idempotents.

**Proof.** The two schemes have the same underlying topological space, since every prime contains a nilpotent ideal. An open-and-closed decomposition of one is therefore precisely an open-and-closed decomposition of the other. Assigning its zero and one functions gives both the lift and its uniqueness. The idempotent/decomposition correspondence commutes with restriction. This proves the asserted bijection even when restriction on arbitrary global functions is not surjective. \(\square\)

This last qualification is useful. Lifting an idempotent involves a decomposition of the space, so it avoids the obstruction that can prevent other sections from lifting.

Now let \((A,\mathfrak m)\) be Noetherian local, let \(f:X\to\operatorname{Spec}A\) be proper, and put
\[
X_n=X\times_A\operatorname{Spec}(A/\mathfrak m^n),\qquad n\geq1.
\]
Every \(X_n\) has the same underlying space as the closed fiber \(X_1\). A decomposition of \(X_1\) gives unique idempotents \(e_n\) on all these schemes. Their uniqueness makes them compatible under restriction. Formal functions in degree zero identifies the resulting algebra with
\[
\widehat{\Gamma(X,\mathcal O_X)}
\cong\varprojlim_n\Gamma(X_n,\mathcal O_{X_n}).
\tag{1}
\]
The isomorphism is multiplicative, since its maps are restriction of functions. A nontrivial fiber decomposition gives a nontrivial idempotent in (1): its first coordinate is already neither zero nor one.

## 2. Zariski's connectedness theorem

**Theorem 2.1.** Let \(f:X\to S\) be proper, with \(S\) locally Noetherian. If the unit map
\[
\mathcal O_S\longrightarrow f_*\mathcal O_X
\]
is an isomorphism, then every fiber is geometrically connected.

**Proof of connectedness.** First the fibers are nonempty. Properness makes \(f(X)\) closed. If its complement contained a point, its nonempty open complement \(U\) would have \(f^{-1}U=\varnothing\), and hence \((f_*\mathcal O_X)|_U=0\). The assumed isomorphism would make \(\mathcal O_U=0\), impossible at any point of \(U\).

Fix \(s\in S\) and replace the base by \(\operatorname{Spec}A\), where \(A=\mathcal O_{S,s}\). Localization is flat. Flat base change therefore preserves the unit isomorphism, so the function algebra of the changed proper scheme is \(A\). Formula (1) becomes
\[
\widehat A\cong\varprojlim_n\Gamma(X_n,\mathcal O_{X_n}).
\]
The completion of a Noetherian local ring at its maximal ideal is local. For example, an element outside the extended maximal ideal has an inverse modulo that ideal; the successive corrections to this inverse converge in the complete ring. A local ring has only the idempotents zero and one. Lemma 1.1 would send a disconnected closed fiber to a nontrivial idempotent in this ring. This is impossible, proving connectedness of \(X_s\). \(\square\)

We give the extra argument for geometric connectedness rather than treating it as automatic. A connected proper scheme over a field need not remain connected after extension: \(\operatorname{Spec}\mathbf C\) over \(\mathbf R\) is an immediate example.

For the proper schemes needed here, the finite-separable test has the following direct proof. Let \(T/k\) be proper and connected and set \(B=\Gamma(T,\mathcal O_T)\), a finite \(k\)-algebra by proper coherence. It has no nontrivial idempotents, so its Artinian product decomposition has one factor: \(B\) is local, and \(B_{\mathrm{red}}=L\) is a finite field extension of \(k\). Flat base change identifies the function algebra after every field extension \(K/k\) with \(B\otimes_kK\). If the separable degree of \(L/k\) is larger than one, \(L\otimes_k k^{\mathrm{sep}}\) has more than one Artinian factor: its distinct separable embeddings give distinct maximal ideals. Its idempotents lift uniquely across the nilpotent radical of \(B\otimes k^{\mathrm{sep}}\), by Lemma 1.1. An idempotent uses finitely many coefficients, so a nontrivial one already occurs over a finite separable extension. Thus connectedness after every finite separable extension forces \(L/k\) purely inseparable. Conversely, for purely inseparable \(L/k\), the algebra \(L\otimes_k\overline K\) has exactly one prime over every field extension \(K\): every element of \(L\) has a power \(p^a\) in \(k\), and such an equation has a unique root in the algebraic closure (in characteristic zero \(L=k\)). Hence \(L\otimes K\) has no nontrivial idempotent, since faithful extension to \(\overline K\) would preserve one. Nilpotent thickening by the radical of \(B\) preserves that conclusion. Therefore \(T_K\) is connected for every \(K\), which proves the geometric connectedness criterion in the entire proper setting of Theorem 2.1.

**Completion of the proof of Theorem 2.1.** Let \(k'/\kappa(s)\) be finite separable. It has a primitive element with monic irreducible polynomial \(\overline P\). Lift its coefficients to \(A=\mathcal O_{S,s}\), obtaining a monic polynomial \(P\), and set
\[
B=A[z]/(P(z)).
\]
This is a finite free \(A\)-algebra, hence flat and Noetherian. It is local with residue field \(k'\): every maximal ideal lies over \(\mathfrak m\), by integrality over the local ring, and \(B/\mathfrak mB=k'\) has only one maximal ideal. Base change to \(\operatorname{Spec}B\) preserves properness and the unit isomorphism by flat base change. The connectedness argument just proved, applied at its closed point, shows that \(X_s\times_{\kappa(s)}k'\) is connected. The finite-separable-extension criterion now proves geometric connectedness. \(\square\)

The theorem needs neither flatness of \(f\) nor reducedness of \(S\) or \(X\). The information used is the entire algebra \(f_*\mathcal O_X\), together with properness. No surjectivity of the ordinary comparison map to every fiber function algebra was assumed.

## 3. Constructing the Stein factorization

Let \(f:X\to S\) be proper. Its quasi-coherent algebra
\[
\mathcal B=f_*\mathcal O_X
\]
is coherent by proper coherence. Define
\[
Y=\underline{\operatorname{Spec}}_S\mathcal B.
\]
The evaluation map \(f^*\mathcal B\to\mathcal O_X\) gives a canonical \(S\)-morphism \(g:X\to Y\), and we have
\[
X\xrightarrow{g}Y\xrightarrow{\pi}S,\qquad f=\pi g.
\tag{2}
\]
On an affine open \(U=\operatorname{Spec}A\subset S\), this is the map to
\(\operatorname{Spec}\Gamma(f^{-1}U,\mathcal O_X)\) specified by its functions.

**Theorem 3.1 (Stein factorization).** In (2), \(\pi\) is finite, \(g\) is proper and surjective with geometrically connected fibers, and its unit map gives
\[
g_*\mathcal O_X=\mathcal O_Y.
\]
The factorization is canonical and commutes with flat base change.

**Proof.** Coherence makes \(\mathcal B\) finite as an \(\mathcal O_S\)-module, so \(\pi\) is finite. In particular it is separated and \(Y\) is locally Noetherian. To prove properness of \(g\), factor it through its graph:
\[
X\longrightarrow X\times_S Y\longrightarrow Y.
\]
The graph is a closed immersion because \(Y\to S\) is separated; the second map is a base change of the proper morphism \(f\). Their composite is proper.

For affine \(U\subset S\), write \(B=\Gamma(f^{-1}U,\mathcal O_X)\). The corresponding open in \(Y\) is \(\operatorname{Spec}B\). The quasi-coherent sheaf \(g_*\mathcal O_X\) there has module of sections precisely \(B\), since its inverse image is \(f^{-1}U\). Its module structure is the canonical evaluation action of \(B\) on itself. The affine module/sheaf correspondence therefore identifies the unit with an isomorphism to \(\mathcal O_Y\). These identifications glue. Theorem 2.1 applied to \(g\) proves its geometrically connected, nonempty fibers, including surjectivity.

The construction uses only the algebra \(f_*\mathcal O_X\) and its evaluation. Under a flat change \(S_1\to S\), flat base change identifies the new direct-image algebra with the pulled-back \(\mathcal B\); relative Spec commutes with pullback. Evaluation also pulls back to evaluation. Thus both maps in the factorization commute with flat base change. \(\square\)

There is a useful uniqueness statement with a precise hypothesis. Suppose \(f=\pi_0g_0\), where \(\pi_0:Z\to S\) is finite and the unit \(\mathcal O_Z\to(g_0)_*\mathcal O_X\) is an isomorphism. Then
\[
f_*\mathcal O_X=(\pi_0)_*\mathcal O_Z.
\]
The affine reconstruction of a finite morphism gives \(Z\cong Y\), and the maps from \(X\) agree by evaluation. Thus (2) is the unique such factorization. Geometrically connected fibers alone are insufficient for this uniqueness: a finite radicial field extension has geometrically connected fibers but has more functions than the target.

## 4. Reading the fibers correctly

**Proposition 4.1.** For \(s\in S\), the points of the finite scheme \(Y_s\) correspond bijectively to the connected components of \(X_s\). For a geometric point \(\overline s\), the geometric points of \(Y_{\overline s}\) correspond to the connected components of \(X_{\overline s}\).

**Proof.** A finite scheme over a field is the spectrum of a finite-dimensional algebra. Such an algebra is Artinian and decomposes into a finite product of local Artinian rings. Its points are therefore open and closed. The base changed map \(X_s\to Y_s\) is proper and surjective. The inverse image of each point is an open-and-closed part of \(X_s\). Its underlying space is the fiber of \(g\) over that point of \(Y\), with residue field unchanged; it is nonempty and connected by Theorem 3.1. Thus these parts are exactly the connected components. After extending the residue field to an algebraic closure, the same argument uses geometric connectedness of the fibers of \(g\). \(\square\)

The distinction between ordinary and geometric points matters. For \(\operatorname{Spec}\mathbf C\to\operatorname{Spec}\mathbf R\), the ordinary source has one component, whereas its geometric fiber has two. The finite intermediate scheme records the field extension that produces this splitting.

Another distinction matters even when the component count is correct. The algebra of the finite scheme \(Y_s\) is
\[
\mathcal B\otimes_{\mathcal O_S}\kappa(s),
\]
and need not equal \(\Gamma(X_s,\mathcal O_{X_s})\). Theorem 3.1 guarantees flat base change, whereas taking a fiber is generally not flat. Proposition 4.1 follows from the connected fibers of \(g\), so remains valid without identifying these two algebras. If \(f\) is proper, flat and of finite presentation with geometrically reduced fibers, the stronger degree-zero base-change theorem does apply; the preceding lesson on semicontinuity treats its connected-fiber case.

## 5. The birational form of Zariski's Main Theorem

**Theorem 5.1.** Let \(f:X\to S\) be a proper birational morphism of integral Noetherian schemes, and suppose \(S\) is normal. Then the unit is an isomorphism
\[
\mathcal O_S\xrightarrow{\sim}f_*\mathcal O_X,
\]
and all fibers of \(f\) are geometrically connected.

**Proof.** Work over a nonempty affine open \(U=\operatorname{Spec}A\subset S\). Normality says that the domain \(A\) is integrally closed in its fraction field \(K\). Because \(X\) is integral and birational to \(S\), restriction to its generic point embeds
\[
B=\Gamma(f^{-1}U,\mathcal O_X)\hookrightarrow K.
\]
The pullback of functions embeds \(A\) into this same field. Proper coherence makes \(B\) a finite \(A\)-module. Every element \(b\in B\) is integral over \(A\): multiplication by \(b\) on finitely many module generators yields, by the determinant trick, a monic equation for \(b\). Integral closedness therefore gives \(B\subset A\); the reverse inclusion is the unit map. Thus \(A=B\), with equality induced by that map. These local conclusions glue to the sheaf isomorphism. Theorem 2.1 now gives geometric connectedness. \(\square\)

Equivalently, the finite part of Stein factorization is a finite birational morphism to a normal scheme and hence an isomorphism. On affine opens this is exactly the argument that an integral intermediate ring between \(A\) and \(K\) must be \(A\). It also proves the corresponding assertion for integral birational morphisms, without a finiteness hypothesis.

This birational connectedness theorem does not assert that \(f\) is an isomorphism. A blow-up can have a positive-dimensional exceptional fiber. Adding finite fibers changes the conclusion: the finiteness theorem proved using formal functions makes \(f\) finite, and the preceding integral-closure argument then makes it an isomorphism.

## 6. Examples and the general-base extension

**A node.** Over a field of characteristic different from two, consider
\[
C=\operatorname{Spec}k[x,y]/(y^2-x^2(x+1)).
\]
Its normalization is \(\mathbf A^1_k\), with parameter \(u\) and
\[
x=u^2-1,\qquad y=u(u^2-1).
\]
Indeed \(u=y/x\) in the function field and is integral, satisfying \(u^2=x+1\). The ring \(k[u]\) is generated as a module over the cubic's coordinate ring by \(1,u\); it is integrally closed and has the same function field, hence is its integral closure. This finite map is proper and birational. The fiber over the node \((0,0)\) consists of \(u=1,-1\), two distinct points. Its finite Stein part is the normalization itself, and its connected part is the identity. The failure of normality of \(C\) is exactly what permits the disconnected fiber in this birational example.

**The plane blow-up.** For the blow-up \(b:\operatorname{Bl}_0\mathbf A^2\to\mathbf A^2\), the preceding lesson computed \(b_*\mathcal O=\mathcal O_{\mathbf A^2}\) and vanishing of the positive direct images. Its Stein intermediate scheme is \(\mathbf A^2\) itself. The exceptional fiber is \(\mathbf P^1\), while every other fiber is one point; all are geometrically connected. Theorem 5.1 supplies the same connectedness conclusion because the plane is normal.

**Squaring.** The finite map \(\mathbf A^1_k\to\mathbf A^1_k\) given by \(t=u^2\) has function algebra \(k[u]\) over \(k[t]\). Its Stein factorization is the identity on the source followed by this finite map. In characteristic different from two, a nonzero geometric fiber consists of two points; the fiber over zero has the local algebra \(k[u]/(u^2)\) and one point. In characteristic two every geometric fiber has one point, with multiplicity two. The finite algebra records both splitting and nilpotents, beyond the set of connected components.

**Theorem 6.1 (Stein factorization over an arbitrary base).** Let \(f:X\to S\) be proper, with \(S\) any scheme. Put
\[
\mathcal B=f_*\mathcal O_X,
\qquad Y=\underline{\operatorname{Spec}}_S\mathcal B.
\]
Evaluation gives a canonical factorization
\[
X\xrightarrow{g}Y\xrightarrow{\pi}S.
\]
The map \(\pi\) is integral; \(g\) is proper and surjective with geometrically connected fibers; and its unit is an isomorphism \(\mathcal O_Y\xrightarrow{\sim}g_*\mathcal O_X\). Formation of this factorization commutes with flat base change.

**Proof.** The direct-image algebra is quasi-coherent by the finite affine-cover calculation in A.1. On every affine base open \(U=\operatorname{Spec}A\), Lemma B.1 shows that \(\Gamma(f^{-1}U,\mathcal O_X)\) is integral over \(A\). Relative Spec therefore makes \(\pi\) an integral morphism. In particular it is affine and separated.

The evaluation map \(f^*\mathcal B\to\mathcal O_X\) constructs \(g\). Factor it through its graph \(X\to X\times_SY\to Y\). The graph is a closed immersion because \(Y\to S\) is separated, and the second map is the base change of the proper \(f\). Their composite is proper. This argument uses the finite-type nature of closed immersions and of \(f\), and does not require \(\pi\) to be of finite type.

Over \(U\), put \(B=\Gamma(f^{-1}U,\mathcal O_X)\). For each \(b\in B\), the inverse image of the principal open \(D(b)\subset\operatorname{Spec}B\) is the invertibility open \((f^{-1}U)_b\). Formula (A.1) identifies its function algebra with \(B_b\), with the evaluation module action. Since the principal opens form a basis, the unit identifies \(g_*\mathcal O_X\) with \(\mathcal O_Y\). Theorem C.2 now makes \(g\) surjective with geometrically connected fibers. Finally B.3 identifies the pulled-back direct-image algebra after any flat base change; relative Spec and evaluation commute with arbitrary pullback by their affine algebra constructions. Thus the factorization commutes with flat base change. \(\square\)

The integral assertion is the correct general-base conclusion. Noetherian coherence strengthens it to finiteness in Theorem 3.1. A proper morphism need not be finitely presented over a non-Noetherian base: for example, the closed immersion \(\operatorname{Spec}(A/I)\to\operatorname{Spec}A\) is proper for every ideal \(I\), even when \(I\) is not finitely generated. Lemma A.4.1 explicitly retains this case instead of hiding a finite-presentation assumption in a Noetherian reduction.

The uniqueness argument in Section 3 applies to an integral intermediate morphism as well, because an integral morphism is affine and is reconstructed from its direct-image algebra. Its hypothesis remains the unit isomorphism, not merely geometrically connected fibers.

## 7. Exercises with solutions

**Exercise 7.1 (easy: a finite morphism).** Determine the Stein factorization of a finite morphism \(f:X\to S\).

**Solution.** A finite morphism is affine, so its relative Spec reconstruction is \(X\cong\underline{\operatorname{Spec}}_S(f_*\mathcal O_X)\). The evaluation map to this scheme is the identity under that isomorphism. Thus its connected part is \(\operatorname{id}_X\), and its finite part is \(f\). This conclusion does not require reduced fibers or flatness.

**Exercise 7.2 (easy: the node).** Explain why the normalization in Section 6 does not contradict birational connectedness, and determine its Stein intermediate scheme.

**Solution.** The target's coordinate ring is not integrally closed: \(u=y/x\) satisfies \(u^2=x+1\) but is not in that ring. Thus the normality hypothesis of Theorem 5.1 fails. The normalization is finite, so Exercise 7.1 makes it the intermediate scheme, with identity connected part. Its two points above the node are the two components of that fiber.

**Exercise 7.3 (medium: when the connected part is trivial).** Suppose \(f\) is proper over a locally Noetherian base, the unit \(\mathcal O_S\to f_*\mathcal O_X\) is an isomorphism, and all fibers have finitely many points. Prove that \(f\) is an isomorphism.

**Solution.** The finiteness consequence of formal functions makes \(f\) finite. A finite morphism is affine and is reconstructed from its direct-image algebra. That algebra, with its unit, is \(\mathcal O_S\), whose relative Spec is \(S\). The reconstructed map is therefore the identity of \(S\), proving the claim. Merely counting one point per fiber would not suffice: the squaring map in characteristic two shows why the algebra hypothesis is needed.

**Exercise 7.4 (medium: normal targets).** Let \(f:X\to Y\) be proper birational between integral varieties over a field, with \(Y\) normal. Prove that the fibers are connected. What stronger conclusion holds?

**Solution.** Varieties here are integral separated schemes of finite type over the field, so are Noetherian. On every affine open \(\operatorname{Spec}A\subset Y\), functions upstairs form a finite \(A\)-algebra inside \(\operatorname{Frac}A\). Normality identifies this algebra with \(A\), as in Theorem 5.1. The unit is therefore an isomorphism, and Theorem 2.1 proves geometric connectedness, which is stronger than ordinary connectedness.

**Exercise 7.5 (hard: the formal-functions mechanism).** Prove connectedness in Theorem 2.1 directly from formal functions, explaining why no surjectivity of finite-level section maps is needed.

**Solution.** At \(s\), localize the base to \(A=\mathcal O_{S,s}\). Flat base change gives \(\Gamma(X_A,\mathcal O)=A\). A hypothetical nontrivial decomposition of the closed fiber is a decomposition of every thickening's identical underlying space. Its zero and one functions give uniquely compatible idempotents \(e_n\). Formal functions identifies their limit with an idempotent of \(\widehat A\). It is nontrivial because its first coordinate is nontrivial, contradicting locality of \(\widehat A\). The lift was made using decompositions, not by lifting arbitrary sections through a surjective restriction map. Nonemptiness follows separately from properness and the unit isomorphism as in Section 2.

**Exercise 7.6 (hard: inseparability and uniqueness).** In characteristic \(p>0\), let \(L/k\) be a nontrivial finite purely inseparable field extension. Explain why \(\operatorname{Spec}L\to\operatorname{Spec}k\) has geometrically connected fibers but is not its own connected part with direct-image algebra \(k\).

**Solution.** For any algebraically closed extension \(\Omega/k\), all elements of \(L\) have a unique image in \(\Omega\): a sufficiently high \(p\)-power equation has a unique root. The finite algebra \(L\otimes_k\Omega\) therefore has exactly one maximal ideal, so its spectrum is nonempty and connected. The separable-closure criterion, or invariance under purely inseparable extension, gives geometric connectedness. Nevertheless its direct-image algebra is \(L\), not \(k\). Its actual Stein factorization is the identity on \(\operatorname{Spec}L\) followed by the finite map. Thus replacing the unit-isomorphism condition in uniqueness by geometrically connected fibers would give a false statement.

## Appendix A. Approximation and connectedness over an arbitrary base

The exact earlier limit inputs are *Limits of schemes and Noetherian approximation*, Theorem 1.1, Lemmas 2.1–2.3, Theorems 4.1–4.2 and Theorem 5.1. Its externally supplied Theorem 5.2 is not an input: the gluing proof is given in Lemma A.2.1 below. The Chow input is *Projective morphisms and Chow’s lemma*, Theorem 4.1, over an affine Noetherian base. Proper coherence, formal functions and completion are the same earlier proved inputs as in Sections 1–3.

### A.1. Two elementary facts about quasi-compact schemes

If \(T\) is quasi-compact and quasi-separated and \(a\in\Gamma(T,\mathcal O_T)\), write \(T_a\) for its invertibility open. Then
\[
\Gamma(T,\mathcal O_T)_a=\Gamma(T_a,\mathcal O_T).
\tag{A.1}
\]
Indeed, use a finite affine cover and finite affine covers of its pairwise overlaps. Sections are the equalizer of two maps between finite products of the chart modules. Localization commutes with finite products and kernels, and on every chart it is ordinary ring localization. This proves (A.1). In particular \(T_a\) is quasi-compact.

A scheme covered by finitely many affine opens \(T_{a_r}\), where all the \(a_r\) are global functions, is canonically an open subscheme of \(\operatorname{Spec}\Gamma(T,\mathcal O_T)\). On \(T_{a_r}\), (A.1) identifies the canonical map with the isomorphism onto \(D(a_r)\). These maps agree on intersections and glue to the claimed open immersion. Notice that their union need not be the entire affine spectrum.

We also use quasi-coherence of the direct image for a quasi-compact, quasi-separated morphism. Here is the degree-zero calculation needed in this appendix. Over an affine target, choose a finite affine cover of the inverse image and finite affine covers of the pairwise intersections. Localizing the target ring localizes every term in the equalizer for sections, and localization is exact. Thus sections on each distinguished target open are the localization of sections on the whole inverse image. This is precisely the affine criterion for quasi-coherence. Kernels and images of maps of quasi-coherent modules are quasi-coherent by the corresponding affine module calculation.

### A.2. Absolute approximation, with the gluing step proved

**Lemma A.2.1.** Every qcqs scheme \(T\) is an inverse limit of schemes of finite type over \(\mathbf Z\), with affine transition maps. A prescribed finite affine cover of \(T\) can be represented eventually by an affine cover of the stages.

**Proof.** The second assertion follows once the first has been constructed: descend the finitely many opens by AG-MO-03 Lemma 2.1, make each model affine by Lemma 2.3, and make them cover at a common stage by Lemma 2.1.

We prove the first assertion by adding the members of a finite affine cover, keeping the already added open as the inverse image of a stage open. An affine scheme is approximated by its finitely generated \(\mathbf Z\)-subalgebras, by AG-MO-03 Theorem 5.1. We describe the induction step in full.

Suppose \(T=V\cup U\), where \(U=\operatorname{Spec}B\) is affine and \(V\) already has an approximation \(V=\varprojlim V_i\). Put \(W=U\cap V\). It is quasi-compact because \(T\) is quasi-separated. By finite open descent, after restricting to a cofinal tail there are quasi-compact opens \(W_i\subset V_i\), with exact inverse-image compatibility, whose limit is \(W\).

We first arrange that the \(W_i\) are quasi-affine. A quasi-compact quasi-affine scheme has finitely many global functions \(a_r\) whose invertibility opens are affine and cover it: choose a principal-open cover inside an affine scheme in which it is open. Refine so that each \(W_{a_r}\) is contained in the inverse image of an affine chart of one stage \(W_{i_0}\). Such a refinement is possible by intersecting the principal opens of the ambient affine scheme with the affine chart inverse images, then taking finitely many principal opens of that ambient scheme inside those intersections. Their defining functions restrict to global functions of \(W\).

By section descent, these functions come from a common stage. Eventual containment of quasi-compact opens makes their stage invertibility opens lie in the selected affine chart inverse images. Those inverse images are affine, so each invertibility open is affine. Eventual equality of opens makes them cover \(W_i\). The second fact in A.1 then identifies \(W_i\) with an open in \(\operatorname{Spec}R_i\), where \(R_i=\Gamma(W_i,\mathcal O_{W_i})\). Thus \(W_i\) is quasi-affine. Set \(R=\Gamma(W,\mathcal O_W)=\varinjlim R_i\), by section descent, and denote restriction \(B\to R\) by \(s\).

Form
\[
Q_i=B\times_R R_i
=\{(b,r_i):s(b)=r_i|_W\}.
\tag{A.2}
\]
Then \(\varinjlim Q_i=B\). Surjectivity follows by representing \(s(b)\) at a stage. For injectivity, an element of \(Q_i\) with first component zero has second component zero eventually, by the colimit description of \(R\).

Choose \(g_1,\ldots,g_m\in B\) with \(W=\bigcup D(g_l)\subset\operatorname{Spec}B\). Formula (A.1) gives \(B_{g_l}=R_{s(g_l)}\). Represent each \(s(g_l)\) by compatible functions \(g_{l,i}\in R_i\). Eventually the opens \((W_i)_{g_{l,i}}\) are affine, cover \(W_i\), and identify with \(D(g_{l,i})\subset\operatorname{Spec}R_i\). To check the affine assertion, their limits are the affine opens \(D(g_l)\subset U\), so use eventual affineness. Their cover is eventual open equality. Formula (A.1) then identifies an affine \((W_i)_{g_{l,i}}\) with \(D(g_{l,i})\). Put \(h_{l,i}=(g_l,g_{l,i})\in Q_i\).

The map \(Q_i\to R_i\) induces isomorphisms
\[
(Q_i)_{h_{l,i}}\xrightarrow{\sim}(R_i)_{g_{l,i}}.
\tag{A.3}
\]
Here is the algebra verification. For a fiber product \(Q=B\times_R C\), let \(h=(g,c)\), and suppose \(B_g\to R_{s(g)}\) is an isomorphism and \(c\) maps to \(s(g)\). Given \(d\in C\), its image in \(R_{s(g)}\) can be represented by \(b/g^n\). After multiplying by a further power of \(g\), the equality becomes an equality in \(R\). Thus some pair \((g^q b,c^{n+q}d)\) belongs to \(Q\), and division by \(h^{n+q}\) gives \(d\) in \(C_c\). This proves surjectivity after localization. If \((b,d)\) maps to zero in \(C_c\), some power of \(c\) kills \(d\); compatibility and injectivity of \(B_g\to R_{s(g)}\) then show that some power of \(g\) kills \(b\). A common power of \(h\) kills the pair. This proves injectivity and (A.3). Consequently \(W_i\) is an open subscheme of \(\operatorname{Spec}Q_i\), covered there by the \(D(h_{l,i})\).

For fixed \(i\), there is a finitely generated \(\mathbf Z\)-subalgebra \(C\subset Q_i\) for which this same \(W_i\) is an open in \(\operatorname{Spec}C\). Indeed each \(D(h_{l,i})\subset W_i\) is an affine of finite type over \(\mathbf Z\), because \(W_i\) is an open in the Noetherian finite-type scheme \(V_i\). Choose finitely many generators of its ring \((Q_i)_{h_{l,i}}\); multiply them by sufficiently large powers of \(h_{l,i}\) to place them in \(Q_i\). Take \(C\) generated by these numerators and all \(h_{l,i}\). Then \(C_{h_{l,i}}\to(Q_i)_{h_{l,i}}\) is surjective by the generators, and injective because \(C\subset Q_i\); a relation killed after localization in \(Q_i\) is already killed after localization in \(C\). Thus their spectra are identical. The identifications agree on intersections, so their unions identify \(W_i\) with \(\bigcup_lD_C(h_{l,i})\). Any larger finitely generated subalgebra still works. The working subalgebras are therefore a directed family with union \(Q_i\).

Glue \(V_i\) to \(\operatorname{Spec}C\) along \(W_i\); call the result \(T_{i,C}\). It is of finite type over \(\mathbf Z\), and hence Noetherian and qcqs. Order the pairs by \((i',C')\ge(i,C)\) when \(i'\ge i\) and \(Q_i\to Q_{i'}\) maps \(C\) into \(C'\). This is directed: at a common later \(i'\), the two finite sets of algebra generators fit inside one working finite subalgebra \(C'\). Each transition glues the given map on \(V_{i'}\) to the affine map on \(\operatorname{Spec}C'\). Its inverse image of \(V_i\) is exactly \(V_{i'}\), and its inverse image of \(\operatorname{Spec}C\) is exactly \(\operatorname{Spec}C'\): both assertions follow on the affine chart from the exact inverse-image condition for the open unions defined by the compatible \(h_l\). The transition is affine, since these two target opens cover and each restricted transition is affine.

The limit on the \(V_i\) side is \(V\); the limit on the affine side is \(\operatorname{Spec}(\varinjlim C)=\operatorname{Spec}B=U\). The overlap limit is \(W\). Scheme gluing therefore identifies the limit with \(T=V\cup U\), and retains \(V\) as the inverse image of each indicated stage open. This completes the induction. A directed preorder in this construction can be replaced by its quotient under mutual comparison; the transition maps on mutually comparable equivalent objects are inverse isomorphisms. \(\square\)

### A.3. Finite-type closed ambient schemes

**Lemma A.3.1 (finite submodules).** On a qcqs scheme, every quasi-coherent module is the directed union of its quasi-coherent submodules of finite type. In particular a quasi-coherent ideal is the directed union of finite-type quasi-coherent ideals.

**Proof.** First a finite-type quasi-coherent submodule \(G\subset F|_W\) on a quasi-compact open \(W\subset T\) extends as a finite-type submodule of \(F\). For an affine \(T=\operatorname{Spec}R\), first extend it without a finiteness condition by taking the kernel of \(F\to j_*(F|_W/G)\), where \(j:W\hookrightarrow T\). This kernel is quasi-coherent by A.1 and restricts to \(G\). Write it as \(\widetilde N\subset\widetilde M=F\). Cover \(W\) by finitely many principal opens on which \(N\) localizes to a finitely generated module. Choose finitely many numerators in \(N\) for generators on those opens. The submodule \(N'\subset N\) they generate restricts to \(N\) on all those opens, so \(\widetilde{N'}|_W=G\).

For general \(T\), add finitely many affine opens to \(W\). At a step, their intersection with the already treated quasi-compact open is quasi-compact. Apply the affine assertion to extend the given submodule across that affine open, then glue the two equal restrictions. Finitely many steps give a finite-type quasi-coherent submodule of \(F\) on \(T\). Starting with the module generated by one section on an affine chart shows that every local section is contained in such a submodule. Sums of two such submodules are again quasi-coherent and finite type, by the affine calculation of images. They form a directed union equal to \(F\). If \(F\subset\mathcal O_T\) is an ideal, its submodules are ideals, so the final assertion follows. \(\square\)

**Lemma A.3.2 (finite-type ambient embedding).** A separated finite-type morphism \(X\to\operatorname{Spec}A\) admits a closed immersion into a separated scheme \(Y\) of finite presentation over \(A\).

**Proof.** Approximate the qcqs scheme \(X\) absolutely by Lemma A.2.1, and represent a finite affine cover \(U_a\subset X\) by an affine cover \(U_{a,i}\subset T_i\) at the stages. Each \(\Gamma(U_a,\mathcal O)\) is a finitely generated \(A\)-algebra. By section descent, a finite list of its \(A\)-algebra generators comes from \(\Gamma(U_{a,i},\mathcal O)\) at one common stage \(i\). The canonical map
\[
X\longrightarrow T_i\times_{\mathbf Z}\operatorname{Spec}A
\]
has inverse image of \(U_{a,i}\times\operatorname{Spec}A\) exactly \(U_a\), and the chart ring map \(A\otimes_{\mathbf Z}\Gamma(U_{a,i},\mathcal O)\to\Gamma(U_a,\mathcal O)\) is surjective. Hence it is a closed immersion. Denote the ambient scheme by \(Y_0\); it is qcqs and of finite presentation over \(A\).

Let \(J\subset\mathcal O_{Y_0}\) define \(X\). By Lemma A.3.1 write \(J=\bigcup J_\alpha\), with \(J_\alpha\) finite-type quasi-coherent ideals. The schemes \(Y_\alpha=V(J_\alpha)\subset Y_0\) are of finite presentation over \(A\), their transitions are closed immersions, and their limit is \(X\) by the affine quotient-ring calculation.

Some \(Y_\alpha\to\operatorname{Spec}A\) is separated. To verify this claim rather than assuming it, take a finite affine cover of a stage and pull it back through the system. At the limit its pairwise intersections are affine because \(X\to\operatorname{Spec}A\) is separated. They become affine at a common stage by eventual affineness. For a pair of chart rings at that stage, write the separatedness test as
\[
R_\alpha\otimes_A R'_\alpha\longrightarrow C_\alpha
\tag{A.4}
\]
for the intersection ring. At the chosen stage the affine intersection is a quasi-compact open of a scheme of finite presentation over \(A\), so its ring is a finite-type \(A\)-algebra. Hence (A.4) is a finite-type algebra map as well, since its source already contains the image of \(A\). Choose finitely many algebra generators of \(C_\alpha\) over its source. Later intersection rings are quotients of this one, since the transition maps are closed immersions; these same generators therefore generate later rings over their corresponding chart-ring tensor products. At the limit (A.4) is surjective by separatedness of \(X\). Represent the preimages of the finite list of generators and their equality equations at one common stage. Formula (A.4) is then surjective there. Do this for the finitely many chart pairs. The affine diagonal criterion proves separatedness at that stage. Choose it as \(Y\). The closed immersion \(X\hookrightarrow Y\) remains. \(\square\)

The finite-type assertion for a quasi-compact immersion used above can also be checked directly: a closed immersion is finite type; a quasi-compact open immersion into an affine scheme is covered by finitely many principal opens, whose rings are generated by one inverse. This gives finite type locally and quasi-compactness globally.

### A.4. From a proper scheme to proper finitely presented thickenings

**Lemma A.4.1 (relative proper approximation).** If \(X\to\operatorname{Spec}A\) is proper, then
\[
X=\varprojlim_\alpha X_\alpha,
\tag{A.5}
\]
where all \(X_\alpha\to\operatorname{Spec}A\) are proper and of finite presentation, and every transition and every map \(X\to X_\alpha\) is a closed immersion.

**Proof.** By Lemma A.3.2 choose a separated finitely presented ambient \(Y\to\operatorname{Spec}A\) containing \(X\) closedly. First construct a proper surjection \(q:Y'\to Y\) with an immersion \(Y'\to\mathbf P^n_A\), with both \(Y'\) and \(q\) of finite presentation over the indicated bases. Descend \(Y\) to a finitely generated integer subalgebra of \(A\), by AG-MO-03 Theorems 5.1 and 4.1, and retain separatedness using its Theorem 4.2. That base is affine Noetherian. Apply the complete Noetherian Chow theorem AG-MO-10 Theorem 4.1 there, and pull its diagram back to \(A\). Every scheme and map in the Noetherian diagram is of finite presentation. Properness, the immersion, and surjectivity survive this base change. For surjectivity, every nonempty fiber remains nonempty after field extension: on a nonzero affine fiber ring, tensoring with a field extension is faithful.

Write \(X=V(J)\subset Y\). Lemma A.3.1 expresses \(J\) as a directed union of finite-type ideals \(J_\alpha\). Put \(X_\alpha=V(J_\alpha)\subset Y\), \(X'_\alpha=Y'\times_Y X_\alpha\), and \(X'=Y'\times_Y X\). The limit of the \(X'_\alpha\) is \(X'\). Their transitions are closed immersions and their maps to \(\mathbf P^n_A\) are finite type. The map \(X'\to\operatorname{Spec}A\) is proper, since \(q|_{X'}\) is proper and \(X\to\operatorname{Spec}A\) is proper. Its immersion into \(\mathbf P^n_A\) is a closed immersion: its graph is closed because projective space is separated, so the immersion is proper, and a proper immersion is a closed immersion.

Consequently \(X'_\alpha\to\mathbf P^n_A\) is a closed immersion eventually. Here is the exact limit argument. On a finite affine cover \(V_r\) of \(\mathbf P^n_A\), the inverse-image limits are affine. Make the stage inverse images affine by eventual affineness. Write their chart maps \(R\to C_\alpha\). Their colimit \(R\to C\) is surjective; transitions \(C_\alpha\to C_\beta\) are surjective because they come from closed immersions; and \(C_\alpha\) is a finite-type \(R\)-algebra. Choose its finitely many algebra generators. Their limit images are elements from \(R\), so the finitely many corresponding equations hold at one later stage. Because every later \(C_\beta\) is a quotient, those same generator images still generate it. Thus \(R\to C_\beta\) is surjective at that stage. A common stage handles all \(V_r\), proving the assertion.

The resulting \(X'_\alpha\) are proper over \(A\). The maps \(X'_\alpha\to X_\alpha\) are proper surjections. Hence \(X_\alpha\to\operatorname{Spec}A\) is universally closed: after any base change, the image of a closed subset \(Z\subset X_\alpha\) equals the image of its closed inverse image in \(X'_\alpha\), which is closed. Each \(X_\alpha\) is separated and of finite presentation over \(A\), so universal closedness makes it proper. Restrict to the cofinal tail of such indices. The quotient-ring limit is \(X\), and all indicated maps are closed immersions. \(\square\)

**Lemma A.4.2 (properness at a Noetherian base stage).** Every proper finitely presented \(Z\to\operatorname{Spec}A\) descends to a proper morphism over a finitely generated \(\mathbf Z\)-subalgebra \(A_i\subset A\).

**Proof.** Descend the finite presentation and then separatedness by AG-MO-03 Theorems 4.1 and 4.2. At this Noetherian stage apply Noetherian Chow to obtain a proper surjection \(Z'_i\to Z_i\) and an immersion \(Z'_i\to\mathbf P^n_{A_i}\). After base change to \(A\), its source \(Z'=Z'_i\times_{A_i}A\) is proper over \(A\), because it is proper over the proper \(Z\). Its immersion into \(\mathbf P^n_A\) is therefore closed by the graph argument in Lemma A.4.1. Theorem 4.2 of AG-MO-03, applied to these finitely presented models, makes \(Z'_j\to\mathbf P^n_{A_j}\) a closed immersion at a later stage. Hence \(Z'_j\to\operatorname{Spec}A_j\) is proper. Its proper surjection onto \(Z_j\), which remains separated and finitely presented, makes \(Z_j\to\operatorname{Spec}A_j\) universally closed and therefore proper, by the closed-subset argument in A.4.1. \(\square\)

This two-step construction is sufficient. We do not need to assert without construction that an arbitrary finite-type proper \(X\) is the base change of a single Noetherian model. Such an assertion would be false without finite presentation. First take the closed-immersion limit (A.5); only its finitely presented terms are descended to Noetherian bases.

### B. General-base integrality and fiber idempotents

**Lemma B.1 (functions are integral).** If \(f:X\to\operatorname{Spec}A\) is proper, then \(B=\Gamma(X,\mathcal O_X)\) is an integral \(A\)-algebra.

**Proof.** Let \(b\in B\). The section limit theorem applied to (A.5) represents \(b\) by a function \(b_\alpha\) on a proper finitely presented \(X_\alpha\) over \(A\). Descend \(X_\alpha\) to a proper Noetherian model using Lemma A.4.2. Sections again commute with the affine-base limit, so \(b_\alpha\) comes from a function \(b_i\) on a proper model over some later finitely generated integer subalgebra \(A_i\). Proper coherence makes its function algebra finite as an \(A_i\)-module. The determinant trick gives a monic polynomial annihilating \(b_i\): multiplication by \(b_i\) on finitely many module generators gives a matrix of coefficients, and the adjugate identity makes its monic characteristic polynomial kill every generator and hence the unit. Pull that equation back to \(A\) and then to \(X\). Thus \(b\) is integral over \(A\). \(\square\)

**Lemma B.2 (fiber idempotents lift as functions).** For a proper morphism \(f:X\to S\), a point \(s\in S\), and an idempotent \(e\in\Gamma(X_s,\mathcal O_{X_s})\), there is an element of the stalk \((f_*\mathcal O_X)_s\) whose restriction to the fiber is \(e\). The stalk element itself need not be an idempotent.

**Proof in the Noetherian case.** Replace the base by its local ring \(A=\mathcal O_{S,s}\), using localization and the degree-zero flat base-change calculation in B.3 below. Proper coherence makes \(M=\Gamma(X_A,\mathcal O)\) finite over \(A\). The zero and one loci of \(e\) partition the closed fiber into two open-and-closed pieces. Each thickening \(X_n=X_A\times_A A/\mathfrak m^{n+1}\) has the same underlying space, and the zero and one functions on these two pieces give compatible idempotents \(e_n\). Formal functions identifies their limit with an element of \(\widehat M\). Its image on the closed fiber factors through
\[
\widehat M/\mathfrak m\widehat M=M/\mathfrak mM.
\]
This equality is the finite-module quotient formula of AG-CA19, Proposition 2.2, equation (4). Choose a representative in \(M\) of that residue class. It restricts to \(e\), proving the assertion in this case.

**Proof over an arbitrary base.** Work on an affine neighborhood \(\operatorname{Spec}A\) of \(s\). By (A.5), \(X_s=\varprojlim (X_\alpha)_s\), with closed transitions. Sections commute with the limit. Represent \(e\) at a stage and move once further so that its equation \(e^2-e=0\) also holds. We obtain an idempotent \(e_\alpha\) on the fiber of a proper finitely presented \(X_\alpha\to\operatorname{Spec}A\).

Descend this morphism properly to a finitely generated integer subalgebra \(A_i\subset A\) using A.4.2. Write \(\mathfrak p\subset A\) for \(s\) and \(\mathfrak p_j=\mathfrak p\cap A_j\). Then
\[
\kappa(s)=\varinjlim_{j\ge i}\kappa(\mathfrak p_j).
\tag{B.1}
\]
Indeed the quotients \(A_j/\mathfrak p_j\) are subrings of \(A/\mathfrak p\) with union \(A/\mathfrak p\), and every fraction uses a numerator and a nonzero denominator lying in a common stage. The fiber of \(X_\alpha\) is therefore the inverse limit of the Noetherian model fibers over the \(\mathfrak p_j\), with affine transitions. Section descent and eventual equality represent \(e_\alpha\) as an idempotent on one such fiber. The Noetherian assertion produces a stalk element of the model direct image mapping to that idempotent. Pullback gives a function on a neighborhood of \(s\) in \(X_\alpha\), and restriction to \(X\) gives a stalk element of \(f_*\mathcal O_X\). Its fiber restriction is \(e\). \(\square\)

**Lemma B.3 (degree-zero flat base change).** For a proper morphism \(f:X\to S\), formation of \(f_*\mathcal O_X\) commutes with flat base change, without a Noetherian or finite-presentation assumption.

**Proof.** Over \(\operatorname{Spec}A\subset S\), its inverse image has a finite affine cover \(U_a\). Since \(f\) is separated and the base is affine, every \(U_a\cap U_b\) is affine: it is the inverse image of the closed diagonal under the affine map \(U_a\times_AU_b\to X\times_AX\). Thus
\[
\Gamma(X_A,\mathcal O)
=\ker\left(\prod_a\Gamma(U_a,\mathcal O)
\longrightarrow\prod_{a,b}\Gamma(U_a\cap U_b,\mathcal O)\right).
\tag{B.2}
\]
Tensoring with a flat \(A\)-algebra preserves this kernel and the finite products. The tensor products are exactly the chart rings and overlap rings of the base-changed cover. Hence (B.2) computes its sections as the tensor product of the original function algebra. These identifications localize and glue, proving the sheaf assertion. \(\square\)

### C. Connectedness over arbitrary bases, including field extensions

**Lemma C.1.** A nonempty proper scheme \(T\) over a field \(k\) is geometrically connected if it is connected after every finite separable extension of \(k\).

**Proof.** A proper \(k\)-scheme is Noetherian, so \(B=\Gamma(T,\mathcal O_T)\) is a nonzero finite-dimensional \(k\)-algebra by proper coherence. An idempotent of the function algebra is exactly a decomposition of the scheme into two open-and-closed pieces: the local function takes the value zero or one on the respective pieces; conversely an idempotent's invertibility open and that of its complement form such a partition. Thus connectedness of \(T\) says that \(B\) has no nontrivial idempotents. A finite-dimensional commutative algebra decomposes into finitely many local algebras. Indeed every prime quotient is a finite-dimensional domain, hence a field because multiplication by a nonzero element is an injective and therefore surjective linear map. There are at most \(\dim_k B\) maximal ideals: \(r\) distinct maximal ideals give, by the Chinese remainder theorem, a quotient with \(k\)-dimension at least \(r\). Their intersection is the nilradical \(J\). It is generated by finitely many nilpotent elements, since it is finite-dimensional; a sufficiently high power of \(J\) is zero by the pigeonhole principle applied to the exponents of these generators. The powers of the distinct maximal ideals remain pairwise comaximal, and the intersection of common sufficiently high powers is their product, equal to a power of \(J\), and hence zero. The Chinese remainder theorem now decomposes \(B\) into local quotients. Since \(B\) has no nontrivial idempotents, only one factor occurs. Consequently \(B\) is local and \(B/J\) is a finite field extension \(L/k\).

Choose algebraic generators \(\lambda_r\) of \(L/k\). In positive characteristic an irreducible polynomial with zero derivative is a polynomial in \(x^p\); repeating until the derivative is nonzero shows that some \(\lambda_r^{p^{n_r}}\) has separable minimal polynomial over \(k\). Let \(M\subset L\) be generated by those powers. It is a finite separable extension of \(k\), and \(L/M\) is purely inseparable. In characteristic zero put \(M=L\). If \(M\ne k\), then \(M\otimes_k k^{\mathrm{sep}}\) is a product of at least two copies of \(k^{\mathrm{sep}}\): adjoin a finite list of separable generators one at a time; in each existing factor the generator's square-free minimal polynomial splits into distinct linear factors in the separable closure, and the Chinese remainder theorem splits that factor accordingly. Induction gives \([M:k]\) factors. Tensoring onward with \(L\) gives at least two nonzero factors, since field extension is faithful. Hence \(L\otimes_k k^{\mathrm{sep}}\) has a nontrivial idempotent. This lifts across the nilpotent kernel of \(B\otimes_k k^{\mathrm{sep}}\to L\otimes_k k^{\mathrm{sep}}\). One elementary proof of nilpotent idempotent lifting is to correct \(x\) with \(x^2-x\in I\) by Newton's formula \(x\mapsto x-(2x-1)^{-1}(x^2-x)\): \(2x-1\) is invertible because its square is \(1+4(x^2-x)\), and the new error lies in \(I^2\). Repeated squaring of the error terminates for nilpotent \(I\). The lift is nontrivial because its quotient is.

Its finitely many coefficients and its idempotent equation occur over one finite separable extension contained in \(k^{\mathrm{sep}}\). Flat base change B.3 would then give a nontrivial idempotent on \(T\) after that finite separable extension, contradicting the hypothesis. Hence \(L/k\) is purely inseparable.

For any field extension \(K/k\), pass faithfully to an algebraic closure \(\Omega\supset K\). A finite purely inseparable extension has generators satisfying equations \(x_r^{p^{n_r}}=a_r\in k\). Over \(\Omega\) each polynomial has exactly one root, so all primes of \(L\otimes_k\Omega\) contain the differences between these generators and their unique roots. Their common quotient is \(\Omega\); the tensor algebra is nonzero by faithfulness, so it has exactly this one prime. In characteristic zero \(L=k\), giving the same conclusion. Thus it has no nontrivial idempotents. Faithful scalar extension shows \(L\otimes_k K\) has none, and lifting or reducing across the nilpotent radical shows the same for \(B\otimes_k K\). By B.3 this is the function algebra of \(T_K\), which is therefore connected. Nonemptiness is preserved by field extension as above. \(\square\)

**Theorem C.2 (arbitrary-base connectedness).** If \(f:X\to S\) is proper and the unit \(\mathcal O_S\to f_*\mathcal O_X\) is an isomorphism, its fibers are nonempty and geometrically connected.

**Proof.** Properness makes the image closed. Its open complement, if nonempty, would have zero direct-image structure sheaf, contradicting the unit isomorphism at any point of that open. Thus all fibers are nonempty.

For \(s\in S\), B.2 says that every idempotent \(e\) of the fiber function algebra comes from \((f_*\mathcal O_X)_s=\mathcal O_{S,s}\). The map from this local ring to the fiber function algebra factors through \(\kappa(s)\). In a nonempty fiber the field \(\kappa(s)\) embeds into the function algebra, since a unital map from a field to a nonzero ring is injective. Hence an idempotent in its image is zero or one. There are no nontrivial fiber idempotents, so \(X_s\) is connected.

Let \(k'/\kappa(s)\) be finite separable. Localize the base to \(A=\mathcal O_{S,s}\), using B.3. Choose finitely many algebraic generators \(\alpha_r\) of this field extension, lift the coefficients of each generator's monic minimal polynomial to a monic \(P_r\in A[z_r]\), and put \(C_0=A[z_1,\ldots,z_m]/(P_1,\ldots,P_m)\). The residue classes of the monomials with each exponent smaller than \(\deg P_r\) form an \(A\)-basis, by successive monic division; thus \(C_0\) is finite free and flat over \(A\). Reduction modulo the maximal ideal of \(A\) and evaluation \(z_r\mapsto\alpha_r\) give a surjection \(C_0\to k'\). Its kernel \(N\) is maximal and lies over that maximal ideal. The local ring \(C=(C_0)_N\) is flat over \(A\) and has residue field \(k'\). Properness and the unit isomorphism survive base change to \(C\), by B.3. The connectedness assertion just proved applies over this arbitrary local ring and shows that \(X_s\times_{\kappa(s)}k'\) is connected. Lemma C.1 completes geometric connectedness. This construction requires no primitive-element theorem. \(\square\)

## References

- **[Stacks]** The Stacks project authors, *The Stacks project*, in its AI Integrated Stacks Project edition: construction [Tag 03GY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-stein-universally-closed); Noetherian Stein factorization [Tag 03H0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-theorem-stein-factorization-Noetherian); general Stein factorization [Tag 03H2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-theorem-stein-factorization-general).
- The exact open field-extension criteria are [Tag 0389](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-characterize-geometrically-disconnected), [Tag 0387](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-characterize-geometrically-connected) and [Tag 0363](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-separably-closed-field-connected-components). Fiber idempotent lifting over arbitrary bases is [Tag 0G7X](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/perfect.html#perfect-lemma-proper-idempotent-on-fibre).
- Normal targets: [Tag 0AY8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-geometrically-connected-fibres-towards-normal), and integral birational maps [Tag 0AB1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-finite-birational-over-normal).
- The linked Stacks Project texts are under GNU FDL 1.2. The arbitrary-base construction and its geometric-connectedness criterion are proved in Appendix A and Theorem 6.1, following the Stacks constructions; the references are supplementary reading, not substitutes for those arguments. The whole lesson is CC0.
