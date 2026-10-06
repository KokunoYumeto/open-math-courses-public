# Purity of the branch locus

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by GPT-6.1 Sol, the AI that wrote it. Public domain (CC0).*

A finite étale cover of a punctured regular local spectrum extends across its missing point when the dimension is at least two. The first case is a calculation: normality gives a Cohen–Macaulay surface, miracle flatness makes the cover free, and its discriminant cannot vanish only at a point. Higher dimensions follow by cutting with a regular parameter and using local Lefschetz. This local result then rules out a branch locus hidden in codimension two.

We use the depth and Hartogs results in Local cohomology, and the local comparison and completion gluing in Lefschetz theorems for finite étale covers. The flatness prerequisite is [Flatness criteria, dimension and the flat locus](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-FSE/flatness-criteria.html), Theorem 4.1. The finite local reduction is [Étale neighbourhoods, henselization and quasi-finite morphisms](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-FSE/etale-neighbourhoods-henselization-and-quasi-finite-morphisms.html), Theorem 4.2. These are actual inputs: their precise statements are recalled where used.

Rings are Noetherian unless indicated otherwise. A normal local ring is a domain. We use Serre's criterion, going down for an integral extension of a normal domain, invariance of regularity and normality under étale localization, and the usual finite-presentation spreading and descent properties. For a point \(x\), its codimension on its local component means \(\dim\mathcal O_{X,x}\). In \(x'\leadsto x\), the point \(x\) is a specialization of \(x'\). Fundamental-group maps use a chosen geometric point and its image; changing choices conjugates them.

## 1. What local purity says

Put \(X=\operatorname{Spec}A\), where \((A,\mathfrak m)\) is local, and \(U=X\setminus\{\mathfrak m\}\). Write \(\operatorname{FÉt}(T)\) for the category of finite étale schemes over \(T\). **Purity for \(A\)** means that
\[
\operatorname{FÉt}(X)\longrightarrow\operatorname{FÉt}(U)
\tag{1.1}
\]
is essentially surjective. If \(\operatorname{depth}A\ge2\), it is already fully faithful. Indeed the underlying modules of finite étale algebras and their internal Hom modules are finite free over local \(A\). Hartogs identifies their sections on \(X\) and \(U\). Algebra homomorphisms are the module maps satisfying the unit and product equations; faithful restriction detects those equations. Thus purity in this depth range makes (1.1) an equivalence.

**Lemma 1.1 (the section test).** Suppose \(\operatorname{depth}A\ge2\), and let \(V\to U\) be finite étale. It extends over \(X\) if and only if
\[
B=\Gamma(V,\mathcal O_V)
\tag{1.2}
\]
is a finite étale \(A\)-algebra. If it extends, its extension is \(\operatorname{Spec}B\).

**Proof.** If \(Y\to X\) is a finite étale extension, its coordinate algebra is finite free over \(A\), and has depth at least two. The support exact sequence makes its sections equal to those over \(Y\times_X U=V\). Conversely, the pushforward of the quasi-coherent algebra of \(V\) along the quasi-compact open \(U\subset X\) is quasi-coherent. It is associated to (1.2), and its restriction to \(U\) recovers that algebra. Hence \(\operatorname{Spec}B\) restricts to \(V\); if \(B\) is finite étale, it is the required extension. ∎

More generally the same section identification holds for a finite \(Y\to X\) whose local rings at the points over \(\mathfrak m\) have depth at least two. For its finite algebra \(C\),
\[
\operatorname{depth}_{\mathfrak m}C
=\min_{\mathfrak n\mid\mathfrak m}\operatorname{depth}C_{\mathfrak n}
\tag{1.3}
\]
by [Stacks, [Tag 0AUK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-depth-goes-down-finite)]. The support sequence then gives \(C=\Gamma(Y\times_XU,\mathcal O)\). This proves the section assertion [Stacks, [Tag 0BM8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-sections-over-punctured-spec)] and the test [Stacks, [Tag 0BLK](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-reformulate-purity)].

**Proposition 1.2 (normal algebra form).** Let \(A\) be normal of dimension at least two. Finite étale covers of \(U\) correspond, contravariantly, to finite normal \(A\)-algebras \(B\) which are étale over \(U\) and whose every irreducible component dominates \(X\). The correspondence is (1.2), with inverse given by restriction of \(\operatorname{Spec}B\).

**Proof.** The normal scheme \(V\) is a finite disjoint union of integral components. Each has a finite separable function field extension \(L/K\), where \(K=\operatorname{Frac}A\). The integral closure \(C\) of \(A\) in \(L\) is finite. Here is the useful trace argument for that finiteness. Choose a \(K\)-basis \(u_1,\ldots,u_r\) of \(L\), each integral over \(A\), by multiplying a basis by suitable nonzero elements of \(A\). For \(c\in C\), every \(cu_i\) is integral, so its trace lies in \(A\): the minimal polynomial has coefficients in the integrally closed \(A\), and its trace is an integer multiple of its next-to-leading coefficient. The nondegenerate separable trace pairing identifies
\[
\{z\in L:\operatorname{Tr}_{L/K}(zu_i)\in A\text{ for all }i\}
\simeq A^r.
\]
The integral closure is an \(A\)-submodule of this finite module, hence finite by Noetherianity. This is [Stacks, [Tag 032L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-Noetherian-normal-domain-finite-separable-extension)]; no excellence assumption is required for this separable extension.

On each principal open in \(U\), the given finite étale algebra is normal and is exactly this integral closure after localization. Thus \(\operatorname{Spec}C\) recovers that component of \(V\). Going down and incomparability for the integral inclusion \(A\subset C\) show that every local ring over \(\mathfrak m\) has dimension \(\dim A\). Normality gives depth at least two there. Formula (1.3) identifies \(C\) with the component's sections. Take the product over the components.

Conversely a finite normal algebra with all components dominant is such a product of finite normal domains. Its closed local rings have the same dimension as \(A\), and hence depth at least two. Its sections are therefore recovered from its restriction by (1.3). That restriction is finite étale by hypothesis. Maps of the covers give algebra maps in the opposite direction, and the same section identification gives every map back. ∎

The dominance qualification in this reformulation is essential. For example, if \(A=k[[s,t]]\), then
\[
A\longrightarrow A\times k,\qquad a\longmapsto(a,\bar a),
\tag{1.4}
\]
is finite with normal target, and restricts to the identity cover on \(U\). The extra field component disappears on \(U\), but the algebra is not flat over \(A\). Consequently arbitrary finite normal algebras cannot be reconstructed from their punctures. Proposition 1.2 is the normal-algebra interpretation of [Stacks, [Tag 0BM9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-reformulate-purity-normal)] with this necessary qualification. It has no effect on the extension question for actual covers, whose section algebras have no such extra component.

**Lemma 1.3 (completion detects extendability).** A given finite étale \(V\to U\) extends over \(A\) if and only if its base change to the punctured spectrum of \(\widehat A\) extends over \(\widehat A\).

**Proof.** One direction is base change. For the other, let \(\widehat Y\to\operatorname{Spec}\widehat A\) be the extension and identify it with the pulled-back \(V\) on the puncture. The finite-module completion-gluing input used in the preceding lesson applies to \(A\to\widehat A\): this map is flat and is an isomorphism modulo \(\mathfrak m\). Gluing the finite algebra on \(U\) with that of \(\widehat Y\), and gluing their multiplication and unit maps, gives a finite \(A\)-algebra whose completed algebra is that of \(\widehat Y\) and whose open restriction is that of \(V\). Faithfully flat descent of finite étaleness proves the assertion. No depth assumption is needed for this gluing statement. ∎

This is [Stacks, [Tag 0BLL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-purity-and-completion)].

## 2. Discriminants and the surface case

For a finite free algebra \(B\) with basis \(b_1,\ldots,b_r\), put
\[
\Delta_{B/A}=\det\bigl(\operatorname{Tr}_{B/A}(b_i b_j)\bigr).
\tag{2.1}
\]
A change of basis multiplies this by a unit square. Its vanishing defines the discriminant locus independently of the basis. A finite locally free morphism is étale exactly where its trace pairing is perfect [Stacks, [Tag 0BJF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/discriminant.html#discriminant-lemma-discriminant)], an input already checked in the preceding lesson. To recall why, trace commutes with base change, so one checks a finite-dimensional algebra over a field. A nondegenerate trace pairing kills no nonzero nilpotent, making that algebra a product of fields, and nondegeneracy for each field factor is precisely separability. These are the finite étale field algebras.

We spell out the slightly more general discriminant argument used in purity.

**Lemma 2.1 (flat quasi-finite purity).** Let \(g:T\to S\) be flat between locally Noetherian schemes, quasi-finite at \(t\), and suppose \(t\) is not a generic point of an irreducible component of \(T\). If \(g\) is unramified at every \(t'\leadsto t\) with \(\dim\mathcal O_{T,t'}=1\), then it is étale at \(t\).

**Proof.** The finite local reduction recalled in the introduction permits an elementary étale neighbourhood of \(g(t)\) and an open in its pullback on which the map is finite, with a unique point above the selected base point. Étale changes preserve local dimension and flatness, and preserve the unramified hypothesis at the indicated generizations; étaleness descends back to the original point. Localize the base at that point. We now have a finite flat algebra over a local ring, hence a finite free algebra, with a unique point over its maximal ideal. The closed source point is not generic, so its dimension, and therefore the base dimension, is at least one, by the flat dimension formula with zero-dimensional fibre.

We need an elementary fact: in a Noetherian local ring \(R\) of positive dimension, every element \(a\) of its maximal ideal lies in a prime \(\mathfrak p\) with \(\dim R_{\mathfrak p}=1\). Prove it by induction on \(\dim R\). In dimension one the maximal ideal works. Otherwise choose a minimal prime \(\mathfrak r\) with \(\dim(R/\mathfrak r)>1\). If the image of \(a\) is nonzero, a prime minimal over it in this local domain has height one by the principal ideal theorem. If that image is zero, use any nonzero nonunit in that domain to find a height-one prime instead. In both cases its inverse image \(\mathfrak q\) in \(R\) contains \(a\), is nonmaximal and is strictly larger than \(\mathfrak r\). Thus \(1\le\dim R_{\mathfrak q}<\dim R\). Induction in this localization supplies the required prime. This also proves [Stacks, [Tag 0BJG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-find-point-codim-1)].

If the discriminant were a nonunit, apply that fact to find a base prime \(\mathfrak p\) of local dimension one in its vanishing locus. The finite free algebra has a non-étale point above \(\mathfrak p\), by the trace criterion. That point specializes to the unique closed source point, and has local dimension one by flatness and the zero-dimensional fibre formula. Flatness makes étale and unramified equivalent here, contradicting the hypothesis. Hence the discriminant is a unit and the original map is étale. ∎

This proves [Stacks, [Tag 0BJH](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-ramification-quasi-finite-flat)], including the nonintegral flat case.

**Theorem 2.2 (purity in dimension two).** If \(A\) is regular local of dimension two, every finite étale cover of its puncture extends to a finite étale cover of \(\operatorname{Spec}A\).

**Proof.** By Proposition 1.2 its section algebra \(B\) is finite normal, with every component dominant, and is étale on the puncture. At every maximal ideal \(\mathfrak n\) of \(B\), going down and incomparability give \(\dim B_{\mathfrak n}=2\). The normal local ring \(B_{\mathfrak n}\) is \((S_2)\), hence Cohen–Macaulay of dimension two.

The local map \(A\to B_{\mathfrak n}\) has zero-dimensional closed fibre, because \(B\) is finite. The miracle-flatness theorem [Stacks, [Tag 00R4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-CM-over-regular-flat)] applies: the base is regular, the source is Cohen–Macaulay, and
\[
\dim B_{\mathfrak n}=2=\dim A+\dim(B_{\mathfrak n}/\mathfrak mB_{\mathfrak n}).
\]
It makes every \(B_{\mathfrak n}\) flat over \(A\), so \(B\) is flat. Since it is finite over local \(A\), it is free.

Now its discriminant is invertible away from \(\mathfrak m\). It is nonzero, since the generic algebra is étale. If it were a nonunit, a prime minimal over its principal ideal would have height one, while \(\mathfrak m\) has height two. The discriminant would vanish at a point of the puncture, a contradiction. It is a unit, so \(B\) is étale. Lemma 1.1 gives the required extension. The empty cover uses the zero algebra and extends as the empty cover. ∎

This gives the dimension-two case of [Stacks, [Tag 0BMA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-local-purity)]. Normality alone in dimension two provides the needed Cohen–Macaulayness; it would not do so in higher dimension.

## 3. Higher dimensions from local Lefschetz

Let \(f\in\mathfrak m\), with no regularity assumption for the next lemma, and set
\[
X_0=\operatorname{Spec}(A/fA),\qquad U_0=X_0\setminus\{\mathfrak m\}.
\]

**Lemma 3.1 (lifting an extension).** Suppose \(H^1_{\mathfrak m}(A)\) and \(H^2_{\mathfrak m}(A)\) are killed by a power of \(f\). If the restriction to \(U_0\) of a finite étale \(V\to U\) extends over \(X_0\), then \(V\) extends over \(X\). In particular this holds if \(\operatorname{depth}A\ge3\).

**Proof.** Lemma 1.3 reduces to the maximal-ideal completion. Flat Čech base change preserves the displayed annihilation hypotheses. A Noetherian complete local ring is also \(f\)-adically complete: a compatible sequence modulo \(f^n\) is Cauchy in the maximal-ideal topology, and its limit has the desired residues because each ideal \((f^n)\) is closed. Thus \((A,fA)\) is a henselian pair.

The finite étale equivalence for a henselian pair [Stacks, [Tag 09ZS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-gabber)] lifts the given extension \(Y_0\to X_0\) to a finite étale \(Y\to X\). The local Lefschetz theorem of the preceding lesson, Theorem 3.2, says that \(\operatorname{FÉt}(U)\to\operatorname{FÉt}(U_0)\) is fully faithful under precisely the bounded-annihilation hypotheses above. Therefore the prescribed isomorphism of \(V|_{U_0}\) with \(Y|_{U_0}\) lifts to an isomorphism \(V\simeq Y|_U\). Its inverse also lifts, and faithfulness checks both compositions. Completion descent now supplies the extension before completion.

If depth is at least three, both cohomology groups vanish by the depth criterion, so the first assertion applies. ∎

This proves [Stacks, [Tag 0BLS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-lift-purity-general), [Tag 0BLM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-lift-purity)]. In particular the induction uses local full faithfulness, not the global Lefschetz isomorphism that purity will later help prove.

**Theorem 3.2 (regular local purity).** Every regular local ring \(A\) of dimension \(d\ge2\) satisfies purity. Restriction in (1.1) is an equivalence. Consequently a finite normal \(A\)-algebra, étale on the puncture and with all components dominant, is étale over \(A\).

**Proof.** Theorem 2.2 is the base \(d=2\). For \(d\ge3\), choose \(f\in\mathfrak m\setminus\mathfrak m^2\) as one regular parameter. Then \(A/fA\) is regular of dimension \(d-1\ge2\). Given a cover \(V\to U\), its restriction to \(U_0\) extends over \(A/fA\) by induction. A regular local ring is Cohen–Macaulay, so \(\operatorname{depth}A=d\ge3\). Lemma 3.1 extends \(V\) over \(A\).

Depth at least two gives full faithfulness, proving the equivalence. The algebra assertion follows from Proposition 1.2 and Lemma 1.1. ∎

This proves the cover-extension theorem [Stacks, [Tag 0BMA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-local-purity)] in every dimension. The qualification in its algebra consequence excludes (1.4); an arbitrary normal finite algebra can contain an invisible closed-point factor.

## 4. Zariski–Nagata purity at a point

The branch-locus theorem has a more general pointwise form than the finite-cover extension statement.

**Theorem 4.1 (purity of the branch locus).** Let \(g:T\to S\) be a morphism of locally Noetherian schemes, let \(t\in T\), and put \(s=g(t)\). Suppose:

1. \(\mathcal O_{T,t}\) is normal and \(\mathcal O_{S,s}\) is regular;
2. \(g\) is quasi-finite at \(t\);
3. \(\dim\mathcal O_{T,t}=\dim\mathcal O_{S,s}=d\ge1\);
4. \(g\) is unramified at every \(t'\leadsto t\) with \(\dim\mathcal O_{T,t'}=1\).

Then \(g\) is étale at \(t\).

**Proof.** We induct on \(d\), including the generic points in the argument. First use the elementary étale finite local reduction from Lemma 2.1. Regularity, normality, local dimension and the hypotheses at codimension-one generizations are preserved under the étale changes; étaleness descends at the selected point. Localizing the new base at that point gives a finite algebra with a single maximal ideal. It is the normal local source ring, since it is its own localization at this unique maximal ideal. Write it as \(A\to B\), with \(A\) regular local, \(B\) normal local, and both of dimension \(d\).

The kernel is a prime, and is zero. A finite integral extension preserves the dimension of the quotient by the kernel, while a nonzero prime in the domain \(A\) has quotient dimension strictly smaller than \(d\): every chain above it can be preceded by \((0)\). Thus \(A\subset B\) is an integral inclusion of domains. Going down for a normal base [Stacks, [Tag 00H8](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-proposition-going-down-normal-integral)], together with incomparability, gives
\[
\dim B_{\mathfrak q}=\dim A_{\mathfrak p}
\quad\text{if }\mathfrak p=\mathfrak q\cap A.
\tag{4.1}
\]
Contraction of a chain in \(B_{\mathfrak q}\) is strict by incomparability; going down lifts any chain in \(A_{\mathfrak p}\) beneath the fixed \(\mathfrak q\). These give the two inequalities in (4.1).

If \(d=1\), the ring \(A\) is a DVR, and the finite \(A\)-module \(B\) is torsion-free since the inclusion is injective and \(B\) is a domain. A finite torsion-free module over a DVR is free, hence flat. Hypothesis 4 includes the closed source point itself, so the map is unramified there. Flat and unramified, with finite presentation, is étale. This settles the base case.

For \(d\ge2\), let \(\mathfrak q\) be a nonmaximal nonzero prime of \(B\). Its local dimension \(h\) satisfies \(1\le h<d\). The local source remains normal, the corresponding local base is regular, and (4.1) gives equal dimensions. Every height-one generization in this localized source is one in the original local source and satisfies hypothesis 4. Induction makes the map étale at \(\mathfrak q\).

At the generic point, choose a height-one prime of the positive-dimensional domain \(B\), using a nonzero nonunit and the principal ideal theorem. The morphism is unramified there by hypothesis. Its unramified locus is open, so it contains the generic point too. Consequently \(\operatorname{Frac}B/\operatorname{Frac}A\) is finite separable; the map at the generic point is étale. Thus \(\operatorname{Spec}B\to\operatorname{Spec}A\) is étale on the whole puncture.

Theorem 3.2 applies to this normal finite algebra. Its single component dominates the base by injectivity, so that theorem's qualified algebra consequence makes \(A\to B\) étale. Descend through the initial étale neighbourhood to obtain the assertion at \(t\). ∎

This is the full pointwise theorem [Stacks, [Tag 0BMB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-purity)]. The source normality, quasi-finiteness and dimension conditions belong to this theorem. The stronger ramification-locus theorem below has different hypotheses.

For a finite morphism from a normal scheme to a regular scheme, with every source component dominant over a base component and with a generically étale map, Theorem 4.1 says that étaleness at every codimension-one source point implies étaleness everywhere. At a positive-codimension point use (4.1) on its component; its height-one generizations are among the specified points. At a generic point use generic étaleness. This is the finite branch-purity criterion. Dominance and generic étaleness keep isolated and inseparable zero-dimensional components from being overlooked.

## 5. Removing a closed set of codimension at least two

**Theorem 5.1.** Let \(X\) be regular and locally Noetherian, and let \(Z\subset X\) be closed, all of whose points have codimension at least two. Put \(U=X\setminus Z\). Then
\[
\operatorname{FÉt}(X)\xrightarrow{\sim}\operatorname{FÉt}(U).
\tag{5.1}
\]
If \(X\) is connected, then \(U\) is connected and
\[
\pi_1(U,\bar u)\xrightarrow{\sim}\pi_1(X,\bar u).
\tag{5.2}
\]

**Proof.** First work on a Noetherian affine open of \(X\). Its regular irreducible components are disjoint, so treat one normal domain \(A\) at a time. Given a finite étale \(V\to U\), take the product of its finite separable generic function fields and normalize \(A\) in that product. The trace proof in Proposition 1.2 gives a finite normal algebra \(B\), all of whose components dominate the base. Localization of integral closure shows that its spectrum restricts to \(V\).

For a point \(b\) of this spectrum, with image \(x\in Z\), equation (4.1) gives
\(\dim B_b=\dim\mathcal O_{X,x}\ge2\). Every height-one generization of \(b\) maps to a height-one point of \(X\), which is outside \(Z\); the morphism is étale there. All hypotheses of Theorem 4.1 hold at \(b\), so the extension is étale there too. It is already étale over \(U\). This proves existence on the affine open.

For full faithfulness, the local depths of \(X\) at \(Z\) are their dimensions, hence at least two. The supported-depth criterion gives
\(\mathcal O_X=j_*\mathcal O_U\), with the same assertion for any vector bundle and its internal Hom. It identifies module maps between finite étale algebras before and after restriction. Faithfulness detects the algebra identities, so it also identifies algebra homomorphisms.

On intersections of affine opens, full faithfulness gives the unique isomorphism between two extensions recovering their identification over \(U\). These isomorphisms satisfy the cocycle equation by faithfulness. They glue the finite étale schemes. This proves (5.1) when \(X\) is only locally Noetherian, including the non-quasi-compact case.

A connected regular locally Noetherian scheme has one irreducible component: components are locally disjoint and open because each regular local ring is a domain. Thus it is integral, and its dense open \(U\) is connected. The fibre functors at \(\bar u\) commute with restriction. The equivalence of finite-cover categories induces (5.2) by the Galois-category argument in the preceding lesson. ∎

There is also a direct existence proof from local purity, explaining [Stacks, [Tag 0EY7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-extend-pure)]. In a Noetherian scheme suppose purity holds at every local ring of the missing closed set. At a generic point \(z\) of the remaining complement, the inverse image of the existing open in \(\operatorname{Spec}\mathcal O_{X,z}\) is the punctured spectrum. Purity extends the cover over this local spectrum. Finite-presentation spreading gives an extension over an ordinary neighbourhood of \(z\), identified with the old cover on the overlap. Shrinking preserves finite étaleness. Noetherian induction finishes. In the regular codimension-two setting Theorem 3.2 supplies this purity, and depth supplies the uniqueness for gluing. The proof above also identifies the canonical normalization extension.

The more general extension theorem [Stacks, [Tag 0H2W](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-purity-one-divisor-general)] assumes a dense open \(U\subset X\), regular local rings at all points of \(X\setminus U\), and a cover unramified in codimension one over \(X\). Here the last condition means that at each missing codimension-one point the generic finite algebra extends to a finite étale algebra over the corresponding DVR. Extend first over these points by spreading the DVR algebras. Then apply the preceding purity induction to the remaining complement, whose local dimensions are at least two. There are only finitely many generic codimension-one points on each Noetherian affine chart. The construction is local on \(X\); identifications with the original cover glue the extensions. Uniqueness at a missing DVR follows because finite étale algebras there are their normal integral closures in their generic algebras, and uniqueness at the remaining points follows from depth two. This also proves the stated locally Noetherian generality of the extension theorem.

**Example 5.2 (affine space).** For every field and closed \(Z\subset\mathbb A^n\) of codimension at least two, removal induces (5.2). In characteristic \(p>0\) this does not assert that the groups are trivial. Indeed
\[
\mathbb A^n\longrightarrow\mathbb A^n,\qquad
(t,x_2,\ldots,x_n)\longmapsto(t^p-t,x_2,\ldots,x_n)
\tag{5.3}
\]
is a connected finite étale cover of degree \(p\). Its coordinate algebra is free on \(1,t,\ldots,t^{p-1}\), its derivative is \(-1\), and its source is integral. The nonempty open obtained by removing the inverse image of \(Z\) is integral too, so this remains a nontrivial connected cover of the complement.

## 6. Global Lefschetz and two sharp examples

**Theorem 6.1 (smooth projective Lefschetz).** Let \(X\) be a smooth projective connected variety over a field, of dimension at least three. Let \(Y\subset X\) be an effective ample Cartier divisor. Then \(Y\) is connected and restriction gives
\[
\operatorname{FÉt}(X)\simeq\operatorname{FÉt}(Y),\qquad
\pi_1(Y,\bar y)\xrightarrow{\sim}\pi_1(X,\bar y).
\tag{6.1}
\]
The divisor itself need not be smooth or reduced.

**Proof.** Smoothness makes \(X\) regular, pure and Cohen–Macaulay. At every point outside \(Y\), the dimension formula gives
\[
\operatorname{depth}\mathcal O_{X,x}+\dim\overline{\{x\}}
=\dim X>2.
\]
The global neighbourhood equivalence in the preceding lesson, Theorem 5.2, applies. Each finite étale cover of \(Y\) extends to a neighbourhood \(V\supset Y\). The complement is proper and closed in the affine \(X\setminus Y\), so it is a finite set of closed points. At each its regular local ring has dimension \(\dim X\ge3\). Theorem 3.2 gives purity, and finite-presentation spreading extends the cover across the finitely many points. Global full faithfulness was already proved in the preceding lesson, Theorem 5.1. This proves the categorical equivalence, equivalently its Theorem 5.3 with purity now established rather than assumed.

An equivalence commuting with pullbacks detects connectedness by decompositions into clopen subcovers. Since \(X\) is connected, so is \(Y\); the equivalence of the pointed fibre functors gives (6.1). ∎

This is the explicit combination of [Stacks, [Tag 0ELE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-proposition-lefschetz-equivalence), [Tag 0BMA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-local-purity)]. In particular every smooth surface in \(\mathbb P^3\) over an algebraically closed field is simply connected. The preceding lesson proved \(\pi_1(\mathbb P^3)=1\) by starting with \(\mathbb P^1\) and the Lefschetz surjections; Theorem 6.1 now identifies the surface group with it. The split quadric \(\mathbb P^1\times\mathbb P^1\) is one such surface. Its two ruling line bundles give Picard group \(\mathbb Z^2\), as computed in Picard groups and Grothendieck–Lefschetz. That Picard phenomenon in dimension two is compatible with the fundamental group being trivial.

**Example 6.2 (a branch divisor).** Over a field of characteristic different from two, the finite map
\[
\mathbb A^2_{x,y}\longrightarrow\mathbb A^2_{x,t},
\qquad t=y^2,
\tag{6.2}
\]
is free of rank two. Its relative differentials are generated by \(dy\) with relation \(2y\,dy=0\). It is étale where \(y\ne0\) and ramified at \(y=0\); its branch locus on the target is the divisor \(t=0\). In the basis \(1,y\) its discriminant is \(4t\). In characteristic two it is generically inseparable and is nowhere étale: \(dy\) has no relation. Its branch locus is then the whole target, not a divisor. A branch-divisor conclusion requires the generic unramified hypothesis.

**Example 6.3 (the singular \(A_1\) cone).** Assume \(\operatorname{char}k\ne2\), and put
\[
A=k[[x,y,z]]/(xy-z^2),\qquad B=k[[u,v]],
\qquad x=u^2,\quad y=v^2,\quad z=uv.
\tag{6.3}
\]
The invariant power series under \((u,v)\mapsto(-u,-v)\) are exactly the even-total-degree series. Grouping their monomials by even-even and odd-odd exponents identifies them with
\(k[[x,y]]\oplus z k[[x,y]]\), with \(z^2=xy\), hence with \(A\). Every odd-total-degree series is an \(A\)-linear combination of \(u\) and \(v\), so \(B\) is finite over \(A\). The ring \(A\) is normal: an element of its fraction field integral over \(A\) is integral over the normal \(B\), hence lies in \(B\), and being invariant it lies in \(A\).

The inverse image of the vertex is the origin of \(\operatorname{Spec}B\). The puncture of \(A\) is \(D(x)\cup D(y)\), because a prime containing both also contains \(z\). On \(D(x)\) the algebra is
\[
B_x=A_x[u]/(u^2-x),\qquad v=z/u,
\tag{6.4}
\]
and \(2u\) is invertible; this is finite étale of rank two. The description on \(D(y)\) uses \(v^2=y\). Thus the punctured regular source gives a finite étale double cover of the punctured cone. It is connected because the source puncture is an open subset of an integral scheme.

It cannot extend étale over the vertex. Depth two of the regular \(B\) identifies the puncture sections with \(B\). Lemma 1.1 says that any extension must have this algebra. At the origin,
\[
\Omega_{B/A}\otimes_B k=k\,du\oplus k\,dv\ne0:
\tag{6.5}
\]
the relative cotangent sequence identifies this space with \(\mathfrak n/(\mathfrak n^2+\mathfrak mB)\), where \(\mathfrak n=(u,v)\). Here \(\mathfrak mB=(u^2,v^2,uv)=\mathfrak n^2\). Equivalently the vertex fibre has basis \(1,u,v\) and dimension three, while the generic rank is two, so the finite algebra is not flat. Thus purity fails for this normal two-dimensional singular target. Normality supplies the canonical finite extension; regularity is what forces it to be étale.

## 7. Complete intersections and the ramification locus

The neighbourhood version of local Lefschetz also lets us pass purity down through a regular equation. This explains why complete intersections have a different threshold from regular local rings.

**Theorem 7.1 (complete-intersection purity).** Let \(A\) be a Noetherian local ring of dimension at least three whose completion is a quotient of a regular local ring by a regular sequence. Then restriction from its spectrum to its puncture is an equivalence of finite étale categories.

**Proof.** Lemma 1.3 reduces existence to completion, and Cohen–Macaulay depth at least three gives full faithfulness. We induct simultaneously for all such local rings on the number of equations in a completed presentation. In length zero the complete ring is regular, so Theorem 3.2 applies.

Write the complete ring as
\[
A=B/(f_1,\ldots,f_r),\qquad
A'=B/(f_1,\ldots,f_{r-1}),\quad f=f_r,
\]
where \(B\) is complete regular local and the sequence is regular. The quotient \(A=A'/fA'\) is Cohen–Macaulay of dimension \(d\ge3\); hence \(H^1_{\mathfrak m}(A)=H^2_{\mathfrak m}(A)=0\). The ring \(A'\) is \(f\)-adically complete and \(f\) is regular. The neighbourhood equivalence in the preceding lesson, Theorem 4.2, lifts a finite étale cover of the puncture of \(A\) to a neighbourhood of that puncture in the puncture of \(A'\).

Its complement is a finite set of points maximal in \(A'_f\), by the omitted-point argument of that lesson. For any such prime \(\mathfrak p\), the local domain \(S=A'/\mathfrak p\) has \(S_f\) a field and \(f\) a nonzero nonunit. It has dimension one: otherwise choose \(g\) in its maximal ideal outside the finitely many height-one primes containing \(f\); a height-one prime minimal over \((g)\) would avoid \(f\) and survive as a nonzero prime of \(S_f\). This is impossible. The complete Cohen–Macaulay ring \(A'\) is equidimensional and catenary, so
\[
\dim A'_{\mathfrak p}=\dim A'-\dim(A'/\mathfrak p)=d\ge3.
\]
Moreover \(A'_{\mathfrak p}\) is a quotient of a localized regular ring by the first \(r-1\) equations. Completion preserves this presentation and its dimension. The inductive hypothesis gives purity for this possibly noncomplete local ring. Thus the cover extends across each omitted point by local purity and finite-presentation gluing, and becomes a finite étale cover of the whole puncture of \(A'\).

Purity for \(A'\), also by induction, extends it over \(\operatorname{Spec}A'\). Restricting to \(\operatorname{Spec}A\) gives the desired extension. Completion descent and depth full faithfulness finish the proof. ∎

This proves [Stacks, [Tag 0BPD](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-proposition-purity-complete-intersection)], including its completion definition of a complete intersection. The neighbourhood induction is the downward transfer [Stacks, [Tag 0BPC](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-purity-inherited-by-hypersurface)], preserving the exact finite local-cohomology conditions. It is distinct from Lemma 3.1, which lifts an extension upward. The local Picard vanishing theorem needed dimension four; this finite-cover theorem needs dimension three.

**Theorem 7.2 (purity of the ramification locus).** Let \(g:T\to S\) be locally of finite type between locally Noetherian schemes. Suppose \(\mathcal O_{T,t}\) is normal of positive dimension, \(\mathcal O_{S,g(t)}\) is regular, and \(g\) is étale at every \(t'\leadsto t\) with \(\dim\mathcal O_{T,t'}=1\). Then \(g\) is étale at \(t\).

The complete proof is provided by [Stacks, [Tag 0EA4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-purity-ramification)], with its linked completion and surface lemmas, notably [Stacks, [Tag 0EA3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-key-purity-ramification)]. It supplies the stronger theorem without the quasi-finite or equal-dimension assumptions of Theorem 4.1; the hypothesis at the indicated generizations is étaleness. The surface argument uses a resolution and the fundamental class in duality. The higher-dimensional reduction normalizes a parameter hypersurface, maps it to the regular quotient base, and applies induction there before recovering quasi-finiteness. In this reduction the normalized hypersurface maps to the quotient base \(S_0\); the printed target \(S\) in the inductive step must be read as \(S_0\).

This linked proof retains the Stacks Project's [GNU Free Documentation License](https://github.com/stacks/stacks-project/blob/master/COPYING). It is an exact open proof provider for this additional theorem; CC0 concerns the original lesson text. This theorem is not an input to the earlier regular purity or branch-locus proofs.

For further reading, Česnavičius–Scholze, *Purity for flat cohomology*, Section 3.3, broadens the local hypotheses using virtual dimension and formal algebraization. Its flat-cohomology purity theory is outside this lesson.

## 8. Exercises and solutions

**Exercise 8.1 (a branch divisor; elementary).** Compute the branch locus of (6.2), and determine the characteristic qualification needed for it to be a divisor.

**Solution.** The algebra is \(k[x,t][y]/(y^2-t)\), free on \(1,y\). Its relative differentials have generator \(dy\) and relation \(2y\,dy=0\). If the characteristic is not two, they vanish exactly where \(y\ne0\). Finite flatness makes this the étale locus, so the ramification locus is \(y=0\) and its image is the branch divisor \(t=0\). The trace matrix is diagonal with entries \(2,2t\), and determinant \(4t\), confirming the calculation. In characteristic two the derivative is identically zero, so the map is nowhere unramified and the branch locus is the whole target.

**Exercise 8.2 (a punctured double cover; intermediate).** Construct the cover (6.3), prove it connected and étale on the puncture, and show it cannot extend as a finite étale cover of the cone.

**Solution.** The even invariant series give \(A\), and the odd series are generated by \(u,v\), proving finiteness. The opens \(D(x),D(y)\) cover the base puncture. On them the algebras \(A_x[u]/(u^2-x)\) and \(A_y[v]/(v^2-y)\) have invertible derivatives, since the characteristic is not two and the respective root is a unit. They give an étale degree-two cover with integral source puncture, hence connected source. Its section algebra is \(B\), since \(B\) is regular of depth two. Any étale extension would be \(\operatorname{Spec}B\) by Lemma 1.1. But at the origin its relative cotangent space has the independent residue classes \(du,dv\), as in (6.5). This is not unramified, so no such extension exists.

**Exercise 8.3 (codimension-two removal; intermediate).** Prove the isomorphism (5.2).

**Solution.** Normalize a regular affine chart in the generic finite separable algebra of a cover of the complement. The trace argument makes the normalization finite. At each point over the missing set, heights agree by going down and incomparability; height-one generizations lie over points not removed, where the cover is étale. Theorem 4.1 makes the finite extension étale at the missing point. These affine extensions glue because supported depth at least two identifies internal Hom sections and algebra homomorphisms. This proves equivalence of cover categories. The connected regular scheme and its dense open are integral and connected. Their fibre functors at the same geometric point agree under that equivalence, giving the fundamental-group isomorphism.

**Exercise 8.4 (the dimension-two proof; intermediate).** Give the whole proof of purity for a regular local ring of dimension two, identifying where normality, flatness and the discriminant enter.

**Solution.** Start with a cover of the puncture. Its section algebra is finite normal by Proposition 1.2, using separable trace finiteness, and has no closed-point-only component. Every maximal localization has dimension two by integral going down and incomparability. Serre's \((S_2)\) condition makes each such normal surface Cohen–Macaulay. The base is regular of dimension two and the finite extension has closed fibre of dimension zero. Miracle flatness makes all those localizations flat and hence makes the finite algebra free over the local base. Its trace determinant is nonzero and a unit off the closed point. A nonzero nonunit determinant would have a height-one minimal prime by the principal ideal theorem; this prime lies in the puncture, contradicting étaleness there. The determinant is a unit, so the algebra is finite étale and its spectrum extends the cover. Depth two gives uniqueness.

**Exercise 8.5 (surfaces in projective three-space; intermediate).** Over an algebraically closed field, prove that every smooth surface in \(\mathbb P^3\) is simply connected, and check the smooth quadric.

**Solution.** A smooth projective surface in \(\mathbb P^3\) is a positive-degree effective Cartier divisor. Its homogeneous codimension-one components come from height-one primes principal in the polynomial UFD; their defining product cuts out its reduced scheme, since smoothness makes it reduced. The resulting line bundle is ample. The ambient \(\mathbb P^3\) is smooth connected of dimension three, so Theorem 6.1 identifies the surface's fundamental group with its own, and proves the surface connected. The ambient group is trivial by the projective-space result from the preceding lesson. For the smooth quadric identify it over the algebraically closed field with the Segre \(\mathbb P^1\times\mathbb P^1\). Its degree-two equation gives such an ample Cartier divisor, so it too has no nontrivial connected finite étale cover. Its Picard group \(\mathbb Z^2\) records the two rulings and imposes no contrary fundamental-group conclusion.

**Exercise 8.6 (audit the finite criterion; advanced).** Examine the assertion that a finite surjective morphism from a normal scheme to a regular scheme is étale if it is étale at every codimension-one source point. Give the missing qualifications and prove the corrected assertion.

**Solution.** Surjectivity permits an extra isolated component. The morphism
\[
\operatorname{Spec}(k[[s,t]]\times k)\longrightarrow
\operatorname{Spec}k[[s,t]]
\]
from (1.4) is finite and surjective, its source is normal, and all its codimension-one points lie on the identity component and are étale. The extra field component is not flat, so the morphism is not étale. A finite purely inseparable extension of fields also gives a surjective morphism between normal regular zero-dimensional schemes with no codimension-one points; this case must be included in a correct criterion.

Assume instead that every source component dominates a base component and that the morphism is generically étale, as well as being étale at all codimension-one source points. At a non-generic source point restrict to its normal integral component and the regular base component. The local map is injective integral, so going down and incomparability give equal positive local dimensions. The morphism is finite, hence quasi-finite. Its height-one generizations satisfy the assumption and in particular are unramified. Theorem 4.1 makes it étale there. It is already étale at every generic point, proving it étale everywhere. The reverse implication is immediate. If all components have positive dimension, the codimension-one assumption forces generic étaleness by openness and the existence of a height-one point on each component; the explicit generic assumption also handles zero-dimensional components.

## Proofs used from preceding lessons and open sources

Miracle flatness is supplied by the named flatness lesson with its three local hypotheses. The elementary étale finite reduction is supplied by the named neighbourhood lesson; it applies to a morphism locally of finite type and quasi-finite at the selected point and preserves the point's residue field. Normality's \((R_1),(S_2)\) criterion, going down and finite-presentation descent are commutative-algebra and descent inputs. Finite-algebra completion gluing and henselian-pair finite étale equivalence are the exact open inputs already identified in the preceding lesson.

Theorem 7.2 uses the linked open Stacks proof and its surface and completion lemmas. Theorems 2.2, 3.2, 4.1, 5.1, 6.1 and 7.1, and all six solutions, have their proofs above. The qualification about isolated normal components belongs to the algebra reformulation and the finite criterion; the regular local cover-extension theorem retains its full generality.

## References

- [Stacks] The Stacks Project authors, *The Stacks Project*, [official project](https://stacks.math.columbia.edu/). Tag links use AI Integrated Stacks Project, an edition containing AI-proposed corrections and AI-written additions which have not been reviewed by the Stacks Project maintainers. Its [English reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/) retains upstream tags. The principal sections here are Fundamental Groups of Schemes, “Purity in local case” and “Purity of branch locus”, together with Commutative Algebra, miracle flatness and integral extensions of normal domains. Linked source proofs retain their GNU Free Documentation License.
- [Grothendieck–Laszlo] A. Grothendieck, *Cohomologie locale des faisceaux cohérents et théorèmes de Lefschetz locaux et globaux (SGA 2)*, revised edition edited by Y. Laszlo, [arXiv:math/0511279](https://arxiv.org/abs/math/0511279), Exposé X, Section 3, for the local comparison and purity route.
- [Česnavičius–Scholze] K. Česnavičius and P. Scholze, *Purity for flat cohomology*, [arXiv:1912.10932](https://arxiv.org/abs/1912.10932), Section 3.3, for further reading on virtual dimension.
