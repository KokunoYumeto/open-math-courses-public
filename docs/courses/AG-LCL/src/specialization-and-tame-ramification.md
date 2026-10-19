# Specialization and tame ramification

*Mathematical exposition by GPT-6.1 Sol (OpenAI). Original exposition: CC0 1.0.*

For a smooth proper family, a cover of the special fibre extends over a henselian neighbourhood and restricts to the geometric generic fibre. The resulting map of fundamental groups is surjective. To prove injectivity, we must go the other way: extend a geometric generic cover across the special fibre. Tame ramification can be removed by a ramified extension of the base, and purity then makes the extension étale everywhere.

In residue characteristic zero this works for every cover. In characteristic \(p\), it works for Galois covers whose groups have order prime to \(p\). Thus the theorem preserves the full prime-to-\(p\) fundamental group, including its nonabelian finite quotients. Wild covers can disappear under specialization.

We use Purity of the branch locus, and the written programme lessons Specialization maps and tame ramification, especially Proposition 1.1, Proposition 2.1 and Theorem 5.1, and Fundamental groups of proper schemes and the homotopy exact sequence, Sections 1–3 and Theorem 6.1. The first supplies the chosen specialization, its valuation reductions and the full DVR form of Abhyankar's lemma. The second supplies universal-homeomorphism invariance, proper henselian equivalence, proper field invariance and the homotopy sequence. Their precise uses are recalled below.

A geometric point has an algebraically closed residue field. A strictly henselian local ring has a separably closed residue field, which need not be algebraically closed in positive characteristic. Write \(s'\leadsto s\) when \(s\) is a specialization of \(s'\). All connected fibres are nonempty. Choices of geometric lifts and fibre-functor identifications belong to the specialization data.

## 1. Specialization, surjectivity and valuation reductions

Let \(f:X\to S\) be proper with geometrically connected fibres, and choose \(s'\leadsto s\). Put
\[
A=\mathcal O_{S,s}^{\mathrm{sh}},
\]
using the separable closure of \(\kappa(s)\) inside the chosen geometric field. Choose a lift \(\bar s'\to\operatorname{Spec}A\). Proper henselian equivalence and purely inseparable invariance give
\[
\operatorname{FÉt}(X_A)\simeq
\operatorname{FÉt}(X_{\bar s}).
\tag{1.1}
\]
For the passage to an arbitrarily large geometric field, proper algebraically closed field invariance is also used. The specialization functor extends a cover through (1.1) and pulls it back to \(\bar s'\). On automorphism groups of the fibre functors, it gives
\[
\operatorname{sp}:\pi_1(X_{\bar s'})\longrightarrow
\pi_1(X_{\bar s}).
\tag{1.2}
\]
This explains its direction.

**Proposition 1.1 (compatible choices).** Specialization commutes with morphisms of proper families and with successive specializations, when the lifts and fibre identifications are chosen compatibly. In particular it commutes with base change.

**Proof.** For a morphism of families over \(T\to S\), a strict henselization \(B\) at the selected point of \(T\) receives the corresponding strict henselization \(A\) on \(S\). Take the geometric generic lift to \(A\) to be the composite of its lift to \(B\). Pullback of covers commutes in both the closed-fibre and the more general fibre squares. Combining these squares with (1.1) gives the square of specialization functors, hence of their group maps.

For \(s''\leadsto s'\leadsto s\), functoriality of strict henselization lifts the chosen map from \(A\) to the geometric field at \(s'\) through the strict henselization \(A'\) there. Use \(A\to A'\to\kappa(\bar s'')\) for the direct lift. The unique extension of a special-fibre cover, restricted along this composite, is the same as its two successive restrictions. Full faithfulness in (1.1) gives the natural identification, including all morphisms. On fibre functors this is composition of the maps in (1.2). ∎

This gives [Stacks, [Tag 0C0K](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-specialization-map-base-change), [Tag 0C0L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-specialization-map-composition)]. Changing paths or identifications for a fixed lift changes the group maps by conjugacy. Arbitrary different geometric lifts need not give inner-conjugate maps between fixed fibres; the specialization lesson gives an explicit example. The statements below hold for every chosen lift.

We will use its Proposition 2.1: for a Noetherian base, a chosen specialization can be represented by a strictly henselian DVR \(R\to S\), with geometric generic and closed points, and proper field invariance identifies the resulting group map with (1.2) [Stacks, [Tag 0C0N](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-specialization-map-discrete-valuation-ring)]. For a general base a valuation-ring representation is available [Stacks, [Tag 0C0M](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-specialization-map-valuation-ring)].

For the smooth proper theorem we can reduce further to a Noetherian base. Work on an affine neighbourhood of \(s\). Its ring is a filtered union of finitely generated \(\mathbb Z\)-algebras. Finite-presentation approximation descends the smooth proper family to one of them. The fibre at the image of \(s\) is geometrically connected, because it becomes the given connected geometric fibre after a field extension. The geometrically connected locus for a proper smooth family is open; shrink around that image. It still contains the image of \(s'\). Proper field invariance identifies the two pairs of geometric fibre groups, and Proposition 1.1 identifies their specialization maps. Thus a theorem for this Noetherian model proves the theorem for the original family.

After the DVR reduction we may also replace \(R\) by its completion. It remains a strictly henselian DVR with the same residue field. Embedding an algebraic closure of its fraction field in an algebraic closure of the new fraction field, proper field invariance identifies the geometric generic cover categories; the closed ones are unchanged. This replacement supplies a complete, hence Nagata, base when needed. It does not assert that an arbitrary cover descends merely by completing a ring.

**Lemma 1.2 (surjectivity).** If \(X\to S\) is smooth proper with geometrically connected fibres, (1.2) is surjective.

**Proof.** Use the reductions above and let \(S=\operatorname{Spec}R\), with \(R\) a strictly henselian DVR. The family is flat and of finite presentation, with geometrically reduced and connected fibres. The homotopy sequence recalled from the proper-schemes lesson is
\[
\pi_1(X_{\bar\eta})\longrightarrow\pi_1(X)
\longrightarrow\pi_1(\operatorname{Spec}R)\longrightarrow1.
\tag{1.3}
\]
The last group is trivial, since finite étale covers of a strictly henselian local scheme split. Hence the first arrow is onto. The proper henselian equivalence identifies its target with \(\pi_1(X_{\bar s})\), and the construction identifies that arrow with specialization. ∎

The more general surjectivity result for a flat proper family with geometrically connected fibres and geometrically reduced special fibre is Theorem 2.2 in the specialization lesson [Stacks, [Tag 0C0P](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-specialization-map-surjective)]. Its proof uses valuation-ring approximation to retain the arbitrary-base generality. We will use it for a nodal degeneration.

## 2. A regular divisor and tame covers

For a DVR \(C\) with uniformizer \(\pi\), a finite separable field extension is **tame** when all local integral-closure DVRs have separable residue extension and ramification index prime to the residue characteristic. It is **unramified** when those indices are one. In characteristic zero every finite separable extension is tame.

For a dense open \(U\subset X\), with DVRs at the generic points of the missing prime divisors, a finite étale \(V\to U\) is tame in codimension one if its generic field factors are tame at all those DVRs. The definition refers to the specified boundary. A cover is unramified there if every index is one and every residue extension is separable.

The arithmetic input is the full DVR Abhyankar theorem, with its normalized-base-change proof in Lemmas K.1–K.3 below; see also the specialization lesson, Theorem 5.1 [Stacks, [Tag 0BRM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-abhyankar)]. If \(C\subset D\) is a local extension of DVRs with separable residue extension and tame index \(e\), and a finite extension of \(\operatorname{Frac}C\) has index divisible by \(e\) at a selected prime, every matching local DVR in the **normalized** base change has index one and separable residue extension. This also applies to residue extensions of positive transcendence degree. For finite field factors, the conclusion is unramifiedness.

Its mechanism is worth retaining. Write \(\pi=wq^e\) in \(D\). After adjoining \(\theta\) with \(\theta^e=\pi\), the normalized tensor algebra is obtained by adjoining \(\theta/q\), an \(e\)-th root of the unit \(w\). That algebra is étale over \(D\). Index multiplication gives index one over the new base. A more general base extension with index divisible by \(e\) reduces to this case after an unramified extension extracting a root of a unit. The cited internal proof checks that reduction and its descent at every prime.

**Lemma 2.1 (the standard model).** Let \(A\) be Noetherian, let \(a\) be a nonzerodivisor with \(A/aA\) reduced, and let \(e\ge1\) be invertible in \(A\). Then
\[
C=A[z]/(z^e-a)
\tag{2.1}
\]
is finite free of rank \(e\), étale over \(D(a)\), and tame along the boundary \(V(a)\) in codimension one.

**Proof.** The monic equation gives the basis \(1,z,\ldots,z^{e-1}\). On \(D(a)\), \(z\) is a unit, so its derivative \(ez^{e-1}\) is a unit; the algebra is étale there. At a prime minimal over \(a\), the localized quotient by \(a\) is a reduced zero-dimensional local ring, hence a field. The local maximal ideal is generated by the regular element \(a\); this is a DVR with uniformizer \(a\). The root-uniformizer calculation in the specialization lesson, Proposition 4.1, gives index \(e\) and unchanged residue field. Thus the extension is tame. ∎

This proves [Stacks, [Tag 0EYF](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-example-tamely-ramified)]. Tameness does not say that the cover (2.1) is étale on the divisor when \(e>1\).

**Theorem 2.2 (extension across a regular divisor).** Let \(D\subset X\) be an effective Cartier divisor on a locally Noetherian scheme, and suppose that \(D\) is regular. A finite étale cover of \(X\setminus D\) unramified over \(X\) in codimension one extends uniquely to a finite étale cover of \(X\).

**Proof.** At \(x\in D\), write its local equation as \(a\). It is regular, and \(A/aA=\mathcal O_{D,x}\) is regular local, say of dimension \(r\). Lifts of its \(r\) parameters together with \(a\) generate the maximal ideal of \(A\), while regularity of \(a\) gives \(\dim A=r+1\). Thus the embedding dimension equals the dimension, and \(A\) is regular. The complement of a Cartier divisor is dense. Consequently all missing local rings are regular, and the general unramified-codimension-one extension theorem proved in Purity of the branch locus, Section 5, applies. It supplies existence at the DVR points, purity at the points of local dimension at least two, and unique gluing. ∎

This is [Stacks, [Tag 0EYE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-purity-one-divisor)]. Regularity is required along \(D\); no regularity of \(X\setminus D\) has been added.

**Theorem 2.3 (Abhyankar for a regular divisor).** Under the same hypotheses on \(X,D\), every finite étale cover of \(X\setminus D\) tame in codimension one is, étale locally on \(X\), a finite disjoint union of the punctured standard models (2.1). Their exponents are invertible on their respective neighbourhoods.

**Proof.** Away from \(D\), étale-local splitting of a finite étale cover gives the assertion with \(e=1\). At \(x\in D\), pass to the strict henselization \(A\) of its local ring. The quotient \(A/aA\) is the strict henselization of the regular divisor local ring, hence regular, and \(a\) remains regular. The preceding parameter argument makes \(A\) regular. It is a normal domain, and \(aA\) is prime. Étale base change preserves the tame DVR extensions at this boundary, by the permanence results in the specialization lesson, Section 6.

The cover algebra over \(A_a\) is normal and splits into normal domains. Treat one such domain \(B\), with fraction field \(L\), and put \(K=\operatorname{Frac}A\). Let \(e\) be a common multiple of its ramification indices at the DVR \(A_{(a)}\). It is a unit in \(\kappa((a))\); at this point we do not assume that it is a unit at the closed point.

Form
\[
A'=A[z]/(z^e-a).
\tag{2.2}
\]
This is finite free over the henselian \(A\), and is local since its closed residue algebra is \(k[z]/(z^e)\). Its residue field is the separably closed \(k\), so it is strictly henselian. The element \(z\) is regular and \(A'/zA'=A/aA\) is regular. The parameter argument again makes \(A'\) regular. Abhyankar's DVR theorem kills all ramification after this base change, since its index over \(A_{(a)}\) is \(e\). Theorem 2.2 extends the pulled-back cover over \(A'\). Every finite étale cover of the strictly henselian \(A'\) splits. A section of that extension therefore gives an inclusion
\[
B\hookrightarrow A'_z,\qquad
K\subset L\subset K(a^{1/e}).
\tag{2.3}
\]

Apply the root-uniformizer intermediate-field result to the DVR \(A_{(a)}\), where \(e\) is invertible in the residue field. It is Proposition 4.1 of the specialization lesson, proved there by valuations and norms [Stacks, [Tag 09EV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-pull-root-uniformizer)]. It gives \(L=K(a^{1/n})\) for some \(n\mid e\). The finite algebra \(C_n=A[y]/(y^n-a)\) is local: its residue algebra is \(k[y]/(y^n)\), with one maximal ideal. The element \(y\) is regular, and \(C_n/yC_n=A/aA\) is regular local. The same parameter argument therefore makes \(C_n\) a regular local ring, without any assumption yet that \(n\) is a unit at the closed point. Every localization of this ring is regular and normal. Its fraction field is \(L\), by the root-uniformizer degree calculation at \(A_{(a)}\). Thus \((C_n)_a\) is a normal finite integral \(A_a\)-algebra with fraction field \(L\), and equals the integral closure \(B\). We obtain
\[
B=A_a[y]/(y^n-a).
\tag{2.4}
\]

Since (2.4) is étale, its module of differentials
\(B\,dy/(ny^{n-1}dy)\) is zero. The element \(y\) is a unit, so \(n\) is a unit in \(B\), and faithful finite freeness makes it a unit in \(A_a\). Because \(a\) is prime, an element of \(A\) invertible in \(A_a\) has the form \(u a^j\), with \(u\) a unit and \(j\ge0\): cancel the prime factors \(a\) from an equation \(nb=a^r\). But \(n\) is already a unit in \(A_{(a)}\), so \(j=0\). Hence \(n\) is a unit in \(A\). The standard model now has exactly the required hypotheses.

Take the product of the component descriptions. All algebras, exponents, maps and inverse maps involve finitely many coefficients. The isomorphism over the strict henselization descends to a pointed étale neighbourhood; enlarge it to make the finitely many exponents units. This proves the asserted étale-local description. ∎

This is [Stacks, [Tag 0EYG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-lemma-abhyankar-one-divisor)]. Normalized base change in the argument is essential.

## 3. Extending a geometric generic cover

Let \(R\) be a strictly henselian DVR, \(K=\operatorname{Frac}R\), and let \(X/R\) be smooth proper with geometrically connected fibres. Its geometric fibres are integral: their regular irreducible components are disjoint, and connectedness leaves one. The total scheme is regular and connected, hence integral too. The closed fibre is a regular effective Cartier divisor.

**Lemma 3.1 (extension after a base change).** If the residue characteristic is zero, every finite étale cover of \(X_{\bar K}\) extends after a finite separable extension of \(K\) to a finite étale cover of the corresponding base-changed family. In residue characteristic \(p\), this holds for a connected Galois cover with group of order prime to \(p\).

**Proof.** Purely inseparable invariance descends the cover from \(\bar K\) to \(K^{\mathrm{sep}}\). Finite presentation then descends it to \(X_L\) for a finite separable \(L/K\), including the Galois action when specified. The integral closure \(R_L\) is a finite DVR extension of \(R\): finiteness follows from the separable trace argument, and henselianity gives its unique maximal ideal. Normalize \(X_{R_L}\) in the cover. On normal Noetherian affine charts the same trace-lattice argument makes this normalization finite; the charts glue. It is a finite normal scheme \(Z\), with only dominant components, and agrees with the given cover on the generic fibre.

All horizontal codimension-one points are already in the étale locus. At the generic point of the special fibre, its local base ring is a DVR. The finitely many local normalization DVRs have ramification indices \(e_i\). They are tame in characteristic zero. In the Galois case of order prime to \(p\), index multiplication and the degree formula give indices prime to \(p\) and separable residues: the inseparable residue degree is a power of \(p\) dividing the group order, hence one [Stacks, [Tag 09EB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-galois-conclusion)].

Let \(e\) be a common multiple of the \(e_i\), and adjoin an \(e\)-th root of a uniformizer of \(R_L\). Since \(e\) is prime to its residue characteristic, this is a finite separable extension with index \(e\). Take the normalized base change \(Z'\) over its DVR \(R'\). Localization of integral closure identifies the DVRs above the generic special-fibre point with exactly the normalized tensor factors in Abhyankar's lemma. That lemma makes them unramified. All horizontal points remain étale. The finite branch-purity criterion of the preceding lesson, with normal dominant source and regular target, therefore makes
\[
Z'\longrightarrow X_{R'}
\tag{3.1}
\]
finite étale everywhere. It recovers the original geometric generic cover. In the Galois case the action extends uniquely to each normalization. Its torsor map is an isomorphism on the generic fibre; as a map between finite étale covers, its isomorphism locus is clopen. The generic fibre is dense and meets every component, so it is an isomorphism everywhere. ∎

Here a common multiple kills all finitely many vertical indices at once; no assertion about an unnormalized tensor product has been made.

The general **reduced-fibre theorem**, proved in Theorem 3.3 below, gives another route to the vertical step. For every Nagata Dedekind domain and every flat finite-type scheme, a finite fraction-field extension makes the normalized base change smooth at every generic point of every fibre. If all generic component fields are separable, the extension can be finite separable. The complete DVR reduction in Section 1 supplies the Nagata hypothesis in the specialization application.

The conclusion is initially smoothness at generic fibre points. Normality of the total normalized scheme gives \((S_2)\); quotienting by a base uniformizer gives \((S_1)\) for each closed fibre, hence no embedded components. Generic smoothness then makes those fibres reduced. This explains the theorem's name. Lemma 3.1 uses the more explicit tame index-removal argument, which also identifies why only prime-to-\(p\) Galois covers are required in positive characteristic.

**Lemma 3.2 (descent through the special fibre).** Every cover produced in Lemma 3.1 is the geometric generic pullback of a finite étale cover of \(X\).

**Proof.** Write \(k=R/\mathfrak m_R\) and \(k'=R'/\mathfrak m_{R'}\). The extension \(k'/k\) is finite algebraic. Since \(k\) is separably closed, it is purely inseparable; in characteristic zero it is trivial. Thus \(X_{k'}\to X_k\) is a universal homeomorphism, and identifies their finite étale categories.

Restrict \(Z'\) to \(X_{k'}\) and descend that cover through this equivalence to \(X_k\). Proper henselian equivalence then gives a finite étale \(Y\to X\). Its pullback to \(X_{R'}\) and \(Z'\) have the same closed-fibre cover. Full faithfulness of the same proper henselian equivalence over \(R'\) gives an isomorphism between them. On the geometric generic fibre this identifies \(Y_{\bar K}\) with the original cover.

In the Galois case, transport the specified action through the closed-fibre equivalences and lift it by full faithfulness. The group identities and the torsor isomorphism are preserved by these equivalences, so \(Y\) is a \(G\)-cover. Its connectedness follows from the connected geometric generic cover: a clopen decomposition of \(Y\) would induce one there, while every nonempty component of a finite étale cover of the integral \(X\) meets the generic fibre. ∎

Both uses of the proper henselian theorem matter. The first constructs \(Y\); the second proves that its pullback is the particular normalized extension (3.1). Purely inseparable invariance handles the residue extension without assuming a perfect residue field.

### 3.1. Normalized base change of DVRs

The following proofs use the Normalization trace-lattice theorem, Theorem 4.1, its inseparability reduction, Lemma N.2.2, and its complete-local and finite-type Nagata theorems, Lemma N.3.3 and Theorem 5.2. The local DVR and reducedness criteria are Discrete valuation rings, normal rings and Serre's criterion, Theorem 1.2, Proposition 3.4 and Theorems 4.2–4.4. Integral extensions, Theorems 2.1, 3.2–3.3 and 4.3, gives localization of normalization, lying over, incomparability and going down.

Coefficient fields, Cohen rings and the required infinitesimal lifts are proved in Coefficient rings and the Cohen structure theorem, Lemmas 1.1, 2.1 and 3.1 and Theorems 4.1–5.1. Henselian local rings and henselization, Theorems 1.2, 5.1 and 6.3, supplies the residue-compatible strict henselizations and their Noetherianity. Completion, Theorems 3.1–3.3 and 5.1–5.2, supplies finite-module completion, faithful flatness and Hensel lifting.

The finite algebraic separability test is Formally smooth, unramified and étale ring maps, Lemma 7.1. For fibres we use Smooth algebras over a field and the Jacobian criterion, Theorems 2.1 and 3.2, and Smooth morphisms, Theorems 2.1 and 3.1. All finite-extension and normalized-base-change arguments needed below are included explicitly.

**Lemma K.1 (finite field extensions of a DVR).** If \(V\) is a DVR with fraction field \(F\), and \(E/F\) is finite, its integral closure \(W\) is a semilocal Noetherian normal domain of dimension one. Its local rings at maximal ideals are DVRs, and their residue fields are finite over \(\kappa_V\). Finiteness of \(W\) as a \(V\)-module is not assumed.

**Proof.** Choose a finite \(V\)-order \(V_0\subset E\) with fraction field \(E\): multiply finitely many field generators by powers of a uniformizer \(\pi\) to make them integral, and adjoin them. This order is finite and torsion-free over \(V\), hence free of rank \([E:F]\). The normalization \(W\) is the directed union of its finite \(V_0\)-subalgebras \(C\). Each is a finite free \(V\)-module of the same rank, and \(C/V_0\) is a finite torsion \(V\)-module. In the multiplication-by-\(\pi\) diagram of \(0\to V_0\to C\to C/V_0\to0\), kernel and cokernel of multiplication on the last finite-length module have equal length. Therefore
\[
\operatorname{length}_V(C/\pi C)
 =\operatorname{length}_V(V_0/\pi V_0)=[E:F].
\tag{K.1}
\]
The filtered limit \(W/\pi W=\varinjlim C/\pi C\) has length at most this fixed bound. Indeed every finite list of its elements comes from one stage, whose image has at most that length. Choose a finite submodule of maximal possible length; adjoining any further element cannot increase it, so it is the whole limit. In particular \(W/\pi W\) is finite over \(V\). Cancellation of \(\pi\) shows that the successive quotients of \(W/\pi^nW\) are copies of \(W/\pi W\), so these are finite \(V\)-modules too.

Every nonzero ideal \(J\subset W\) contains a power of \(\pi\). For \(0\ne x\in J\), the monic minimal polynomial of the integral element \(x\) has coefficients in the integrally closed \(V\) and nonzero constant term. Its equation puts a nonzero element of \(V\) in \(xW\). Hence \(J/\pi^nW\) is a submodule of a finite \(V\)-module for a suitable \(n\), and is finitely generated. Lift its generators and add \(\pi^n\); they generate \(J\) as a \(W\)-ideal. Thus \(W\) is Noetherian. Integrality gives dimension one, normality is its definition, and the earlier one-dimensional normal-local criterion makes its closed local rings DVRs. All maximal ideals contain \(\pi\), and the finite-length ring \(W/\pi W\) has finitely many maximal ideals with finite residue fields over \(\kappa_V\). This proves every assertion. ∎

**Lemma K.2 (index-one stability).** Let \(A\subset B\) be a local inclusion of DVRs, with ramification index one and separable residue extension \(F/k\), possibly transcendental. For any finite extension \(E/K\), every normalized branch has ramification index one and separable residue extension over the matching local integral-closure DVR of \(A\).

**Proof.** Let \(A_E\) be the integral closure of \(A\), and \(B_E\) the integral closure of \(B\) in \((\operatorname{Frac}(B)\otimes_KE)_{\mathrm{red}}\). Lemma K.1 supplies their local DVRs. Fix a maximal ideal of \(B_E\), let \(D\) be its local DVR, and let \(C=(A_E)_{\mathfrak p}\) be the matching DVR, with uniformizer \(t\). The local tensor ring dominated by \(D\) is a localization \(T\) of \(B\otimes_AC\). It is flat over \(C\), since \(B\) is flat over \(A\). Moreover,
\[
(B\otimes_AC)/t(B\otimes_AC)
 =F\otimes_k\kappa(\mathfrak p).
\tag{K.2}
\]
The second field is finite over \(k\), by K.1. Separability of \(F/k\) means that this finite-dimensional \(F\)-algebra is reduced; it is a finite product of fields, each separable over \(\kappa(\mathfrak p)\). Hence \(T/tT\) is a field and its maximal ideal is generated by \(t\).

Take the image \(R\) of \(T\) in \(D\). Its maximal ideal is still generated by the nonzero \(t\). It is separated in powers of \(t\), since it is a subring of the DVR \(D\) and \(v_D(t)>0\). Thus each nonzero element of \(R\) is a unit times a finite power of \(t\): division by \(t\) cannot continue indefinitely. Every nonzero ideal has an element of least such order and is generated by it. This proves that \(R\) itself is a DVR. Its fraction field is that of \(D\), because the chosen tensor factor is generated by \(\operatorname{Frac}(B)\) and \(E\), both contained in its fraction field. A DVR dominated by another valuation ring in the same fraction field is equal to it, by the same unit-and-uniformizer expression. Therefore \(R=D\). Its uniformizer is \(t\), and its residue field is the field factor in (K.2). This proves index one and residue separability. The argument does not require the tensor ring to be Noetherian or reduced. ∎

**Lemma K.3 (DVR Abhyankar theorem).** Let \(A\subset B\) be a local inclusion of DVRs with separable residue extension and ramification index \(e\) invertible in the residue field. If \(E/K\) is finite and a matching base DVR has ramification index divisible by \(e\), every normalized branch over it has index one and separable residue extension.

**Proof.** First take \(E_0=K(\theta)\), \(\theta^e=\pi\). Its base DVR is \(A[\theta]\), by the Eisenstein and principal-maximal-ideal argument. For a uniformizer \(q\in B\), write \(\pi=wq^e\) with \(w\in B^*\). The generic tensor is generated by \(z=\theta/q\), with \(z^e=w\). The ring \(B[z]/(z^e-w)\) is finite étale: both \(e\) and \(z\) are units. It is normal over the regular DVR \(B\), so is the normalization in the generic tensor. Its local DVRs have index one over \(B\). Multiplying indices around the square gives index one over \(A[\theta]\), and the residue extensions are separable because this base DVR has the original residue field. K.2 preserves the conclusion after every further finite extension of \(E_0\).

For the specified local base DVR \(C\) in \(E\), choose a uniformizer \(t\) and write \(\pi=ut^{e_1}\), with \(e\mid e_1\) and \(u\in C^*\). Adjoin an \(e\)-th root of \(u\). Its monic polynomial gives a finite étale algebra over both \(C\) and every prescribed normalized local DVR \(D\) over it. Choose matching local factors \(C'\subset D'\). Both horizontal maps \(C\to C'\), \(D\to D'\) have index one and finite separable residues. The new fraction field contains \(u^{1/e}t^{e_1/e}\), an \(e\)-th root of \(\pi\), so the preceding case and K.2 give index one and separable residues for \(C'\to D'\). Index multiplication gives the same index for \(C\to D\). The field \(\kappa(D)\) is a subextension of the separable extension \(\kappa(D')/\kappa(C)\), hence is separable. This proves the theorem for every matching branch. ∎

These arguments give the normalized-DVR statements corresponding to [Stacks, Tags 09EQ](https://stacks.math.columbia.edu/tag/09EQ) and [0BRM](https://stacks.math.columbia.edu/tag/0BRM), with finite-field normalization supplied by K.1. They concern local rings in the normalized reduced base change.

### 3.2. Finite orders and separable elimination

For a local inclusion of DVRs \(A\subset B\), put \(K=\operatorname{Frac}(A)\) and \(L=\operatorname{Frac}(B)\). If \(E/K\) is finite, write \(A_E\) for the integral closure of \(A\) in \(E\), and \(B_E\) for its integral closure in \((L\otimes_KE)_{\mathrm{red}}\). Call \(E\) a **solution** when, for every maximal ideal \(\mathfrak q\subset B_E\) and its contraction \(\mathfrak p\subset A_E\), the local rings are DVRs and
\[
\mathfrak p(B_E)_{\mathfrak q}=\mathfrak q(B_E)_{\mathfrak q},
\qquad
\kappa(\mathfrak q)/\kappa(\mathfrak p)
\text{ is separable}.
\tag{E.1}
\]
Separability here is separability of a possibly transcendental field extension. A solution has both ramification index one and the required residue-field condition.

**Lemma E.1 (transfer of a finite order).** Let \(R\subset S\) be a finite ring extension and \(f\in R\) a nonzerodivisor on \(S\), with \(R[1/f]=S[1/f]\). Choose \(c\ge1\) with \(f^cS\subset R\), and let \(N\ge2c+1\). Suppose \(g\) is a nonzerodivisor on a ring \(R'\), and an isomorphism
\[
\theta:R/f^NR\xrightarrow{\sim}R'/g^NR'
\quad\text{sends }f\text{ to }g.
\tag{E.2}
\]
There is a finite ring extension \(R'\subset S'\subset R'[1/g]\) and a compatible ring isomorphism
\[
S/fS\xrightarrow{\sim}S'/gS'.
\tag{E.3}
\]
The construction is compatible with a commutative diagram of such extensions and congruences, using the same \(c,N,f,g\).

**Proof.** Finitely many generators of \(S\) have denominators that are powers of \(f\), so such a \(c\) exists. Let \(J\subset R'\) be the inverse image under \(R'\to R'/g^NR'\) of
\(\theta(f^cS/f^NR)\), and put \(S'=g^{-c}J\). Since \(g^cR'\subset J\), this contains \(R'\). Products satisfy \(J^2\subset g^cJ\): modulo \(g^N\), a product corresponds to \(f^{2c}st=f^c(f^cst)\), with \(f^cst\in f^cS\); the possible error \(g^NR'\) lies in \(g^cJ\), because \(N\ge2c\). Thus \(S'\) is a subring of \(R'[1/g]\). The module \(J/g^NR'\) corresponds to the finite \(R/f^NR\)-module \(f^cS/f^NR\). Lifting its finitely many generators, and adding \(g^N\), shows that \(J\), and hence \(S'\), is finite over \(R'\).

For \(s\in S\), choose \(b_s\in J\) whose residue is \(\theta(f^cs)\), and send \(s\) to \(g^{-c}b_s\bmod gS'\). Changing the lift changes it by an element of \(g^{N-c}R'\subset gS'\). This defines an additive map \(S\to S'/gS'\), and it kills \(fS\): one may choose \(b_{fs}=gb_s\). It sends one to one, by choosing \(b_1=g^c\). For multiplication,
\[
b_sb_t-g^cb_{st}\in g^NR',
\qquad
g^{-2c}(b_sb_t-g^cb_{st})\in gR'\subset gS',
\]
where the second assertion uses \(N\ge2c+1\). Thus it is a ring map.

Every element of \(S'\) has the form \(g^{-c}b\), \(b\in J\), so it comes from some \(s\in S\) modulo \(gS'\). If \(g^{-c}b_s\in gS'\), then \(b_s\in gJ\). Transporting the residues back gives
\(f^cs\in f^{c+1}S+f^NR\subset f^{c+1}S\), since \(N\ge c+1\). Cancellation of the nonzerodivisor \(f^c\) gives \(s\in fS\). This proves injectivity and (E.3). A homomorphism of the original diagrams sends \(f^cS_1\) into \(f^cS_2\), hence \(J_1\) into \(J_2\). Dividing by the same \(g^c\) gives the required homomorphism \(S'_1\to S'_2\), and the displayed construction of (E.3) commutes with it. ∎

**Lemma E.2 (a separable perturbation).** Suppose \(K\) has characteristic \(p>0\), \(L/K\) is separable, and both \(A\) and \(B\) are Nagata. Let \(E/K\) be finite, and suppose \(F/E\) is purely inseparable of degree \(p\). If \(F\) is a solution, there is a finite separable extension \(E'/E\) that is a solution for \(A\subset B\).

**Proof.** The separability of \(L/K\) makes \(L\otimes_KE\) and \(L\otimes_KF\) reduced finite algebras over \(L\), hence products of fields. All four integral closures \(A_E,A_F,B_E,B_F\) are finite over the corresponding Nagata DVRs. They are Noetherian normal one-dimensional rings, with finitely many maximal ideals. Their local rings at maximal ideals are DVRs. For a uniformizer \(\pi\in A\), inverting \(\pi\) gives precisely their indicated field algebras.

Write \(F=E(\alpha)\), \(\alpha^p=a\). Multiplying \(\alpha\) by a sufficiently large power of \(\pi\) makes \(a\in A_E\). The finite orders
\[
R_A=A_E[x]/(x^p-a)\subset A_F,
\qquad
R_B=B_E[x]/(x^p-a)\subset B_F
\tag{E.4}
\]
are embedded because their generic algebras are \(F\) and \(L\otimes_KF\), respectively. Apply Lemma E.1 to these two orders with \(f=\pi^2\), choosing one conductor exponent \(c\) for both. Fix \(N\ge2c+1\), and put
\[
\begin{aligned}
P(x)&=x^p-\pi^{2N}x-a,\\
R'_A&=A_E[x]/(P),&
R'_B&=B_E[x]/(P),\\
D&=E[x]/(P),&
T&=(L\otimes_KE)[x]/(P).
\end{aligned}
\tag{E.5}
\]
The derivative \(-\pi^{2N}\) is invertible in the generic algebras. Thus \(D\) is a product of finite separable extensions of \(E\), and \(T=L\otimes_KD\) is a product of fields. The two orders \(R'_A,R'_B\) are free on \(1,x,\ldots,x^{p-1}\) over \(A_E,B_E\); they embed into \(D,T\), and \(\pi\) is a nonzerodivisor. Reduction modulo \(\pi^{2N}\) identifies (E.4) with these orders, by the coefficientwise identity and \(x\mapsto x\).

Lemma E.1 and its diagram compatibility produce finite extensions
\(R'_A\subset C\subset D\) and \(R'_B\subset H\subset T\), a map \(C\to H\), and a commuting square of isomorphisms
\[
\begin{array}{ccc}
A_F/\pi^2A_F&\xrightarrow{\sim}&C/\pi^2C\\
\downarrow&&\downarrow\\
B_F/\pi^2B_F&\xrightarrow{\sim}&H/\pi^2H.
\end{array}
\tag{E.6}
\]
All maps agree with the original maps from \(A_E\) and \(B_E\).

We verify that \(C,H\) already are the integral closures. They are reduced Noetherian rings, finite respectively over \(A,B\), inside their finite generic field algebras. Every maximal ideal contains \(\pi\), since it lies over the maximal ideal of the corresponding DVR. At a maximal ideal of \(C\), (E.6) identifies its quotient modulo \(\pi^2\) with a local quotient of a DVR \((A_F)_{\mathfrak p}\). Its maximal ideal is consequently principal modulo \(\pi^2\). As \(\pi^2\) lies in the square of the maximal ideal, Nakayama makes the maximal ideal itself principal. The local ring has dimension one by integrality over the DVR, so it is a regular local ring of dimension one and hence a DVR. The same argument applies to \(H\). Thus both rings are normal. Any element of \(D\) integral over \(A\) is integral over \(C\), since its monic equation over \(A\) is also one over \(C\), and belongs to \(C\) by normality. The reverse containment follows from finiteness. Hence \(C=A_D\) and \(H=B_D\).

Let \(\mathfrak q\subset H\) lie over \(\mathfrak p\subset C\). The isomorphisms (E.6) identify their residue fields and the residue-field map with those of the corresponding maximal ideals of \(B_F\) and \(A_F\). That map is separable because \(F\) is a solution. They also identify the equality of the extended maximal ideal with the maximal ideal modulo \(\pi^2\). This equality lifts to the local rings themselves: \(\pi\in\mathfrak p\), so \(\pi^2H_{\mathfrak q}\subset\mathfrak pH_{\mathfrak q}\). Thus (E.1) holds for the finite separable algebra \(D/E\). Select any field factor \(E'\) of \(D\). Its integral closures are the corresponding direct factors of \(C,H\), so (E.1) holds at all their maximal ideals. This is the required finite separable solution over \(E\). ∎

**Lemma E.3 (separable solutions).** Let \(A\subset B\) be a local inclusion of DVRs, with \(L/K\) separable and \(B\) Nagata. If a finite solution exists, a finite separable solution exists.

**Proof.** First \(A\) is Nagata. In characteristic zero this follows from the trace-lattice finiteness theorem in Normalization, Theorem 4.1. In characteristic \(p\), Lemma N.2.2 of that lesson reduces the N-2 property to finite purely inseparable fraction-field extensions. A DVR has only its zero and maximal prime; its maximal-prime quotient is a field, which is N-2. Thus N-2 for the DVR is exactly the Nagata condition. For a finite purely inseparable \(E/K\), the tensor product \(L\otimes_KE\) is a field. If \(A_E\) and \(B_E\) denote the integral closures, flatness of the DVR inclusion gives an injection
\(B\otimes_AA_E\hookrightarrow L\otimes_KE\), whose image lies in \(B_E\). Indeed each tensor generator is integral over \(B\). The ring \(B_E\) is finite over \(B\), and its submodule \(B\otimes_AA_E\) is finite because \(B\) is Noetherian. Faithful flatness of \(A\to B\) descends finite generation: lift the finitely many tensor generators using finitely many elements of \(A_E\), and kill their cokernel by faithful flatness. Thus \(A_E\) is finite over \(A\), proving the assertion.

In characteristic zero every finite field extension is separable. In characteristic \(p>0\), let \(F/K\) be a solution and induct on its inseparable degree. If that degree exceeds one, choose \(K\subset E\subset F\) with \([F:E]=p\) purely inseparable. Such an \(E\) exists by a degree-\(p\) tower over the maximal separable intermediate field. Lemma E.2 replaces \(F\) by a finite extension \(E'/E\) that is separable and remains a solution. Multiplicativity of inseparable degrees gives
\[
[E':K]_{\mathrm i}=[E:K]_{\mathrm i}
 =[F:K]_{\mathrm i}/p.
\]
This positive integer decreases at each step. The process terminates with inseparable degree one, and therefore with a solution separable over \(K\). ∎

For the associated statements and the finite-order method, see the freely accessible Stacks Project, Tags [0GLT](https://stacks.math.columbia.edu/tag/0GLT), [0GLV](https://stacks.math.columbia.edu/tag/0GLV) and [0BRN](https://stacks.math.columbia.edu/tag/0BRN).

### 3.3. Complete DVRs and wild cyclic extensions

All inclusions of DVRs below are local. An inclusion is **weakly unramified** when its ramification index is one; its residue extension may be inseparable. A weak solution of \(A\subset C\) is a finite extension of \(K=\operatorname{Frac}(A)\) for which every local DVR of the normalized reduced base change is weakly unramified over the matching base DVR.

Fix complete DVRs \(A\subset B\) with the same uniformizer \(\pi\), fraction fields \(K\subset L\), and residue fields \(k\subset F\). Assume
\[
\operatorname{char}k=p>0,\qquad k\text{ algebraically closed},
\qquad \bigcap_{r\ge0}F^{p^r}=k.
\tag{W.1}
\]
Every finite extension of \(K\) has a finite complete integral-closure DVR \(A_E\), by the earlier complete-local Nagata and henselian theorems. If its uniformizer is \(t\), residue field \(k_E\), and index \(e\), its finite torsion-free \(A\)-module is free. Comparing its rank with the filtration of \(A_E/\pi A_E\) by \(1,t,\ldots,t^{e-1}\) gives \([E:K]=e[k_E:k]\), including inseparable extensions. Here \(k_E=k\) by algebraic closedness, so \([E:K]=e\). The valuation denominator of \(t\) gives \([K(t):K]\ge e\), hence \(E=K(t)\). Its minimal polynomial is Eisenstein: its conjugates have the same valuation, all nonleading coefficients have positive integral valuation, and the constant coefficient has valuation one. The Eisenstein quotient has principal maximal ideal \((t)\), so is a DVR and equals \(A_E=A[t]\). The same polynomial over \(B\) remains Eisenstein. Consequently every finite base extension preserves weak unramifiedness of \(A\subset B\), gives a field \(L\otimes_KE\), and leaves \(F\) unchanged.

The normalization input is Normalization, Lemma N.3.3 and Theorem 5.2. The length argument just given supplies the degree formula also for inseparable extensions; its separable version is the calculation in Specialization maps and tame ramification, Section 3.

**Lemma W.1 (a purely inseparable step).** If \(K\) has characteristic \(p\) and \(M/L\) is purely inseparable of degree \(p\), adjoining \(\pi^{1/p}\) to \(K\) is a weak solution for the integral-closure DVR of \(B\) in \(M\).

**Proof.** A compatible coefficient field identifies \(A=k[[\pi]]\), \(B=F[[\pi]]\). Coefficient fields exist by the earlier Cohen theorem. Their restrictions to the perfect field \(k\) agree: two lifts from a perfect field into a nilpotent thickening agree by taking sufficiently high Frobenius powers, and separatedness gives the assertion in the complete rings. Write \(M=L(y)\), \(y^p=b=\sum_{i\ge i_0}\lambda_i\pi^i\). After adjoining \(t\), \(t^p=\pi\), the normalized base is \(B_1=F[[t]]\).

If every \(\lambda_i\) is a \(p\)-th power in \(F\), the convergent series \(\sum\lambda_i^{1/p}t^i\) is a \(p\)-th root of \(b\). The reduced generic tensor algebra is then \(\operatorname{Frac}(B_1)\), so there is no ramification. Otherwise choose the smallest \(j\) with \(\lambda_j\notin F^p\). Subtract the \(p\)-th power of the finite series \(\sum_{i_0\le i<j}\lambda_i^{1/p}t^i\), and divide the root by \(t^j\). The resulting root has a monic equation with constant reduction \(X^p-\lambda_j\), irreducible over \(F\). Its finite order is local with maximal ideal generated by \(t\), and therefore a DVR. It has residue degree \(p\), hence ramification index one. This proves the assertion in every case. ∎

For a cyclic field extension of prime degree the following elementary field descriptions will be useful. In characteristic \(p\), if \(\sigma\) generates the Galois group, choose \(b\) of trace one, using nondegeneracy of the separable trace. Then \(z=-\sum_{i=0}^{p-1}i\sigma^i(b)\) satisfies \(\sigma z-z=1\), so \(z^p-z\in L\) and \(M=L(z)\). In characteristic zero with \(\zeta_p\in L\), the operator \(\sigma\) is diagonalizable, since \(X^p-1\) has distinct roots. A nonfixed eigenvector \(y\) has \(y^p\in L\) and generates \(M\). Thus these are respectively Artin–Schreier and Kummer equations. The trace nondegeneracy used here is Normalization, Lemma 4.0.

**Lemma W.2 (equal-characteristic cyclic step).** Under (W.1), if \(K\) has characteristic \(p\) and \(M/L\) is cyclic of degree \(p\), it has a finite weak solution over \(K\).

**Proof.** Write
\[
z^p-z=\xi=\sum_{i=1}^{n}\lambda_i\pi^{-i}+b,
\qquad \lambda_i\in F,\quad b\in B,
\tag{W.2}
\]
using the compatible coefficient fields. If all negative coefficients vanish, the monic equation has derivative \(-1\), so its order is finite étale over \(B\), and no extension is needed. Split the nonzero negative coefficients into those in \(k\) and those outside \(k\), with index sets \(I,J\).

First remove collisions along powers of \(p\) within \(J\). If \(j,j'=p^rj\) both belong to \(J\), replace \(z\) by
\[
z+\sum_{s=0}^{r-1}\lambda_j^{p^s}\pi^{-p^sj}.
\]
Its Artin–Schreier value changes by
\(\lambda_j^{p^r}\pi^{-j'}-\lambda_j\pi^{-j}\). Thus the coefficient at \(j\) disappears, the one at \(j'\) changes, and no other coefficient changes. The number of coefficients outside \(k\) decreases. Repeating terminates with no two indices of \(J\) having ratio a power of \(p\).

If \(J\) is empty, the entire polar part \(\xi_0\) belongs to \(K\). Adjoin a root \(v\) of \(v^p-v=\xi_0\) to \(K\). This gives either the trivial extension or a cyclic extension of degree \(p\). In the normalized base change the generator \(z-v\) has integral Artin–Schreier value \(b\). Its finite order is étale, hence its DVR factors have index one.

Suppose \(J\ne\varnothing\). For \(j\in J\), write \(\lambda_j=\mu_j^{p^{r_j}}\), where \(\mu_j\notin F^p\) and \(r_j\) is finite; finiteness follows from (W.1). Choose \(R>\max_j(r_j+1)\), large enough that \(jp^{R-r_j}>n\) for all \(j\in J\). Adjoin \(t\) with \(t^{p^R}=\pi\). Repeated changes by Artin–Schreier coboundaries reduce (W.2) to
\[
(z')^p-z'=
\sum_{i\in I}\lambda_i^{1/p^R}t^{-i}
 +\sum_{j\in J}\mu_jt^{-jp^{R-r_j}}+b'.
\tag{W.3}
\]
For example \(a^{p^r}t^{-dp^r}\) is replaced by \(at^{-d}\) by subtracting \(at^{-d}+a^pt^{-dp}+\cdots+a^{p^{r-1}}t^{-dp^{r-1}}\) from the generator. The new \(J\)-exponents are distinct, since equality would make the original indices have ratio a power of \(p\). Their largest value \(d\) exceeds \(n\) and is divisible by \(p\). Its coefficient is not a \(p\)-th power in \(F\).

Put \(u=t^{d/p}z'\). Its monic equation reduces to \(u^p-\mu=0\) over \(F\), with \(\mu\notin F^p\). The resulting finite order has residue field of degree \(p\) and maximal ideal generated by \(t\), so is a DVR of ramification index one. This proves the claim. The preprocessing of the \(J\)-indices is essential: adding coefficients at equal exponents can otherwise turn two non-\(p\)-th-power coefficients into a \(p\)-th power. ∎

For the coefficient-collision issue, see F.-V. Kuhlmann, [A correction to Epp's paper “Elimination of wild ramification”, arXiv:1003.5687v1](https://arxiv.org/abs/1003.5687v1).

**Lemma W.3 (mixed-characteristic polynomial).** Suppose \(A\) has mixed characteristic and contains \(\zeta=\zeta_p\). Put \(w=1-\zeta\), \(e_1=v_A(w)\), and
\[
P(X)=\frac{(1+wX)^p-1}{w^p}.
\tag{W.4}
\]
Then \(u=p/w^{p-1}\) is a unit, \(u\equiv-1\pmod w\), and
\[
P(X)=X^p+uX+
\sum_{i=2}^{p-1}\frac1p\binom pi u w^{i-1}X^i.
\tag{W.5}
\]
For \(x\oplus y=x+y+wxy\),
\[
P(x\oplus y)=P(x)+P(y)+w^pP(x)P(y).
\tag{W.6}
\]

**Proof.** Factoring \(p=\prod_{j=1}^{p-1}(1-\zeta^j)\) shows that \(u\) is a unit: the factor \((1-\zeta^j)/w\) has nonzero residue \(j\). Binomial expansion gives (W.5); its intermediate coefficients have valuation at least \((i-1)e_1\). Substitution of \(-1\) gives \(P(-1)=0\), since \(1-w=\zeta\). Reducing that equality modulo \(w\) proves \(u\equiv-1\), including \(p=2\). Finally \(1+w(x\oplus y)=(1+wx)(1+wy)\); taking \(p\)-th powers and dividing the difference from one by \(w^p\) proves (W.6). ∎

Suppose \(P(z)=\xi\in L\), with \(M=L(z)\) of degree \(p\). If \(\xi\in B\), reduction of its monic equation has derivative \(-1\), so the extension is unramified. If \(v_B(\xi)=-n<0\), then \(v(z)=-n/p\) in the valuation normalized on \(B\): for a negative valuation the leading term \(z^p\) has strictly smaller valuation than all other terms of (W.5). If \(p\nmid n\), its denominator forces ramification index \(p\). If \(p\mid n\) and the leading residue coefficient is not in \(F^p\), scaling by \(\pi^{n/p}\) gives a finite order whose reduction is irreducible \(X^p-\lambda\). Its maximal ideal is generated by \(\pi\); it is a DVR with residue degree \(p\) and ramification index one. These assertions also apply to the analogous Artin–Schreier polynomial used above.

**Lemma W.4 (lowering the level).** Under (W.1), suppose \(A\) has mixed characteristic, \(\zeta_p\in K\), and a degree-\(p\) extension \(M/L\) has a generator with \(P(z)=\xi\) and \(v_B(\xi)>-pe_1\). Its **level** is the minimum \(l=n/e_1\), where \(n=\max(0,-v_B(P(z)))\) over such generators. If \(l>0\), a finite base extension either is a weak solution or gives an extension of level at most
\[
\max(0,l-1,2l-p).
\tag{W.7}
\]

**Proof.** Choose a minimal positive \(n\), so \(0<n<pe_1\), and put
\[
m=\min(n,e_1,pe_1-n)>0.
\tag{W.8}
\]
For any \(a\in L\) with \(v_B(a)\ge-n/p\), (W.5) gives
\(P(a)\equiv a^p-a\pmod{\pi^{-n+m}B}\). Indeed the linear error has valuation at least \(e_1-n/p\), and the term of degree \(i\ge2\) has valuation at least \((i-1)e_1-in/p\ge -n+e_1\). For \(\eta_1,\eta_2\in\pi^{-n}B\), the final product term in (W.6) has valuation at least \(pe_1-2n\ge-n+m\). The binomial errors when adding such correction terms are also harmless: \(v_B(p)=(p-1)e_1\ge m\). Thus within this window the operation on the values is exactly the additive Artin–Schreier operation.

The quotients \(A/\pi^m\) and \(B/\pi^m\) have characteristic \(p\). The earlier coefficient-field theorem gives a map \(F\to B/\pi^m\); its restriction to the perfect \(k\) agrees with the coefficient map from \(A/\pi^m\), by uniqueness of perfect-field lifts. Choose representatives \(\sigma:F\to B\), with those from \(k\) in \(A\), respecting addition and multiplication modulo \(\pi^m\). Write
\[
\xi\equiv\sum_{i=n-m+1}^{n}\sigma(\lambda_i)\pi^{-i}
 \pmod{\pi^{-n+m}B}.
\tag{W.9}
\]
Let \(I,J\) again distinguish coefficients in \(k\) and outside it. Remove pairs \(j,j'=p^rj\) in \(J\) by replacing \(z\) with \(z\oplus a\), where
\(a=\sum_{s=0}^{r-1}\sigma(\lambda_j^{p^s})\pi^{-p^sj}\). Its pole is at most \(n/p\), so \(1+wa\) is a unit, and \(z\oplus a=(1+wa)z+a\) still generates the extension. The congruences just proved remove the coefficient at \(j\) and change only the one at \(j'\). Each step decreases \(|J|\). It cannot lower \(n\), by its minimal choice. We may therefore assume that no two remaining \(J\)-indices have ratio a power of \(p\).

If \(J\) is empty, write \(\xi=\xi_0+r\), where \(\xi_0\in K\) is the displayed polar sum and \(r\in\pi^{-n+m}B\). If \(p\mid n\), the perfectness of \(k\) supplies a lift of the \(p\)-th root of the leading coefficient. The correction \(a=-a_0\pi^{-n/p}\) cancels that coefficient modulo \(\pi^{-n+1}\), using the same bounds. It contradicts minimality of \(n\). Thus \(p\nmid n\). Adjoin \(y\) with \(P(y)=-\xi_0\) to \(K\). The valuation test after (W.6) makes this a degree-\(p\), totally ramified extension. After base change, the degree-\(p\) cyclic algebra \(M\) either splits, in which case we are done, or stays a field. In the latter case \(z\oplus y\) generates it and
\[
P(z\oplus y)=r-w^p\xi\xi_0\in\pi^{-n+m}B_1.
\]
Both \(n\) and \(e_1\) scale by the base ramification index. Its new level is therefore at most \((n-m)/e_1\), which is (W.7).

If \(J\) is nonempty, write \(\lambda_j=\mu_j^{p^{r_j}}\), \(\mu_j\notin F^p\), and choose \(R>\max(r_j+1)\) with \(jp^{R-r_j}>n\) for every \(j\in J\). Adjoin \(t\) with \(t^{p^R}=\pi\), a finite Eisenstein extension in characteristic zero. The bounds above scale by \(p^R\). Successive corrections \(z\mapsto z\oplus a\) consequently give, modulo \(t^{-(n-m)p^R}B_1\), exactly the value
\[
\sum_{i\in I}\sigma(\lambda_i^{1/p^R})t^{-i}
 +\sum_{j\in J}\sigma(\mu_j)t^{-jp^{R-r_j}}.
\tag{W.10}
\]
Each correction has pole at most \(np^R/p<e_1p^R\), so it preserves the generator. Coefficient errors vanish in the window because the representatives are ring maps modulo \(\pi^m=t^{mp^R}\). Formula (W.6), the bound on its product term, and the binomial bound justify a finite sequence of these corrections, just as in the exact calculation (W.3).

The largest \(J\)-exponent \(d\) is unique, exceeds every \(I\)-exponent, is divisible by \(p\), and has coefficient outside \(F^p\). If \(d>(n-m)p^R\), it is the actual leading term and the residue-degree test gives ramification index one. If \(d\le(n-m)p^R\), all terms and the error have pole at most \((n-m)p^R\); this gives (W.7). Equality with the boundary of the window belongs to this second case, so no conclusion about an unchecked leading coefficient is needed. ∎

**Lemma W.5 (mixed-characteristic cyclic step).** Under (W.1), if \(K\) has characteristic zero and \(M/L\) is cyclic of degree \(p\), it has a finite weak solution over \(K\).

**Proof.** First adjoin \(\zeta_p\) to \(K\). The weakly unramified base inclusion is preserved. After this or any later base change a cyclic degree-\(p\) algebra either splits into \(p\) copies of the base field or stays a degree-\(p\) field; this follows from the prime order of its Galois group and its transitive action on embeddings. In the split case there is nothing to prove.

By the elementary Kummer argument above, write \(M=L(y)\), \(y^p=b\). Adjoining \(\pi^{1/p}\) makes the valuation of \(b\) divisible by \(p\). Dividing \(y\) by a power of the new uniformizer then makes \(b\) a unit. If its residue is not a \(p\)-th power, its order has residue degree \(p\) and index one, as in W.1. Otherwise divide by a lifted \(p\)-th power to arrange \(y^p=1+\pi b'\). Then \(z=(y-1)/w\) satisfies
\[
P(z)=\pi b'/w^p,\qquad v_B(P(z))>-pe_1.
\]
The level is in \([0,p)\). Level zero gives a finite étale order. At positive level apply Lemma W.4. Its iteration terminates: while \(p-l<1\), the positive distance from \(p\) at least doubles. After finitely many steps \(l\le p-1\), and then (W.7) decreases the level by at least one until zero. Every step is a finite base extension; their finite composite is the required weak solution. ∎

The free Stacks proofs of the corresponding cyclic steps are Tags [09F1](https://stacks.math.columbia.edu/tag/09F1) and [09F2](https://stacks.math.columbia.edu/tag/09F2)–[09F5](https://stacks.math.columbia.edu/tag/09F5).

**Lemma W.6 (finite extensions over a weakly unramified coefficient DVR).** Under (W.1), let \(M/L\) be any finite extension and \(C\) the integral-closure DVR of \(B\) in \(M\). There is a finite weak solution for \(A\subset C\).

**Proof.** First the perfect core remains \(k\) after a finite residue-field extension. For a separable extension take a finite Galois closure. An element with all its \(p\)-power roots in that closure has minimal-polynomial coefficients whose \(p\)-power roots are in \(F\): Galois automorphisms commute with the unique roots and preserve their stabilizers. The coefficients lie in \(k\), so the element lies in the algebraically closed \(k\). For a finite purely inseparable extension of exponent \(s\), taking the \(p^s\)-th power of an element and of each of its successive roots reduces to the preceding field. Perfectness of \(k\) finishes that case. This also proves that the perfect core of \(F^{\mathrm{sep}}\) is \(k\): all successive roots of an element in this core lie in one finite Galois extension of \(F\), since a purely inseparable element of the separable closure of that extension already belongs to it.

We may make \(F\) separably closed for the proof. Replace \(B\) by the completion \(B^*\) of a strict henselization. It remains weakly unramified over \(A\), has residue \(F^{\mathrm{sep}}\), and has the same perfect core. The finite algebra \((M\otimes_L\operatorname{Frac}(B^*))_{\mathrm{red}}\) has finitely many field factors. Solve them one at a time. A branch already made weakly unramified over the base stays so under further finite constant extension, by the Eisenstein calculation above. Once all factors are solved, the solution restricts to every original branch over \(B\): the finite integral closure over the complete \(B\), tensored with the faithfully flat \(B^*\), has points above every closed branch, and its normalization supplies dominating DVRs. Their index-one composites force index one below. Thus it suffices to work with separably closed \(F\).

Enlarge \(M\) to a finite normal extension. A weak solution for the enlargement is one for \(M\), because every normalized intermediate DVR is dominated by one upstairs and its index divides the upstairs index. The complete-DVR Nagata theorem supplies finite integral closures, so lying over covers every intermediate branch.

Consider the separable normal part, with group \(G\), complete integral-closure DVR \(C\), uniformizer \(q\), and residue field \(F_C\). This residue extension is finite purely inseparable over the separably closed \(F\); hence \(G\) acts trivially on it. There is a homomorphism
\[
\theta:G\longrightarrow F_C^*,\qquad
\sigma\longmapsto\overline{\sigma(q)/q}.
\]
Its image is a finite cyclic group of order prime to \(p\), by the root-counting argument for finite subgroups of a field's multiplicative group. Its kernel \(P\) acts trivially on the entire graded ring \(F_C[\bar q]\). If \(\sigma\in P\) has order \(m\) prime to \(p\) and moves \(c\in C\), put \(\delta=\sigma(c)-c\), of valuation \(r\). Then
\[
0=\sigma^m(c)-c=\sum_{j=0}^{m-1}\sigma^j(\delta)
 \equiv m\delta\pmod{q^{r+1}},
\]
a contradiction. Thus \(P\) is a \(p\)-group. The group facts needed for this conclusion have short counting proofs. If a prime \(\ell\) divides the order of a finite group, cyclic rotation acts on the \(\ell\)-tuples with product one. Their number is divisible by \(\ell\), so the number of constant tuples \((a,\ldots,a)\), with \(a^\ell=1\), is divisible by \(\ell\). There is a nonidentity such \(a\). Applied to \(P\), this rules out every prime except \(p\). The class equation of a nontrivial \(p\)-group makes its centre nontrivial; the same counting gives a central subgroup of order \(p\), and induction gives a normal series with order-\(p\) factors. A finite subgroup of a field's multiplicative group is cyclic: commuting elements supply one of order its exponent, and the polynomial of that exponent has at most that many roots, forcing the exponent to be the group's order. Together with a prime-factor series of the cyclic quotient these facts give a tower of cyclic prime-degree extensions. A possible purely inseparable part is a tower of degree-\(p\) steps. All residue fields remain separably closed, and their perfect core remains \(k\).

Each prime-to-\(p\) step is tame: its degree formula forces inseparable residue degree one and index prime to \(p\). Its ramification is removed by the root-uniformizer calculation K.3. Lemmas W.1, W.2 and W.5 handle the other three kinds of step. At a given stage there may be finitely many normalized branches. Each earlier branch is weakly unramified over the current complete base. A further finite constant extension preserves this property and does not split that branch, by the Eisenstein calculation above. Treat the finitely many branches in turn. A prime-degree cyclic step stays cyclic of that degree or splits after base change; a purely inseparable degree-\(p\) step stays of that degree or becomes trivial after reduction. There are finitely many tower steps and branches. Their finite composite gives index one on every final branch. ∎

This is the complete-coefficient case of the ramification-elimination argument; compare [Stacks, Tag 09F8](https://stacks.math.columbia.edu/tag/09F8).

### 3.4. Finite descent of ramification elimination

We use the complete-coefficient case W.6, finite-order transfer E.1, and the normalized index-one and tame base-change theorems K.2–K.3. All DVR inclusions are local. In this section a solution has both index one and separable residue extensions at every normalized branch, as in (E.1).

**Lemma D.1 (approximation of a finite extension).** Let \(V\) be a DVR, \(K\) its fraction field, \(\widehat K\) that of its completion, and \(\pi\) a uniformizer. Every finite separable extension \(H/\widehat K\) has the form \(K_1\otimes_K\widehat K\), with \(K_1/K\) finite separable and this tensor product a field. The same conclusion holds for an extension separable over \(\widehat K(\pi^{1/p^r})\), after first adjoining \(\pi^{1/p^r}\) to \(K\).

**Proof.** Choose a primitive element \(a\), multiplying it by a power of \(\pi\) to make it integral. Its monic separable minimal polynomial \(f\) has coefficients in the completed DVR. Approximate them arbitrarily closely by those of a monic \(g\in V[X]\) of the same degree. In the complete valued field \(H\), Newton iteration at \(a\) gives a root \(b\) of \(g\) arbitrarily close to \(a\). Indeed, choose \(g\) so that \(v(g(a))>2v(g'(a))\); the iterations \(b_{n+1}=b_n-g(b_n)/g'(b_n)\) have errors of strictly increasing, eventually doubling valuation, with derivative valuation fixed. They converge in \(H\), and their first correction can be made as small as desired.

Choose \(|b-a|\) smaller than the distance from \(a\) to every other conjugate of \(a\). In a finite normal extension containing \(a,b\), every automorphism fixing \(b\) must fix \(a\): otherwise the invariant valuation and the ultrametric inequality give \(|\sigma a-a|\le|b-a|\), a contradiction. Galois correspondence gives \(\widehat K(a)\subset\widehat K(b)\). The degree of \(g\) is \([H:\widehat K]\), so equality holds and \(g\) is irreducible over \(\widehat K\), hence over \(K\). Set \(K_1=K[X]/(g)\). The same argument applies after the indicated uniformizer-root extension; its polynomial is Eisenstein and its completion is the corresponding root extension of \(\widehat K\). ∎

When the residue field \(k\) is perfect of characteristic \(p\), a complete equal-characteristic DVR has fraction field \(k((\pi))\), of \(p\)-degree one. Every finite extension \(H\) of this field is contained in a compositum \(H_s\,k((\pi^{1/p^r}))\), with \(H_s\) finite separable. To verify this, take the maximal separable intermediate field; the remaining extension is purely inseparable of bounded exponent. Frobenius preserves the degree of a finite extension, and the tower degree formula gives \([H_s:H_s^p]=[k((\pi)):k((\pi))^p]=p\). Since a separable extension and a purely inseparable extension are linearly disjoint, \(H_s^{1/p^r}=H_s\,k((\pi^{1/p^r}))\). In mixed characteristic every finite extension is already separable. Enlarging a solution to this compositum preserves it, by K.3 applied with index one.

**Lemma D.2 (complete base with perfect residue).** Let \(A\) be a complete DVR with perfect residue field \(k\), and \(A\subset B\) a local inclusion of DVRs with \(B\) essentially of finite type over \(A\). A finite solution exists.

**Proof.** In residue characteristic zero, K.3, applied to an appropriate root of the uniformizer, proves the assertion. Suppose \(\operatorname{char}k=p>0\), and write \(F=\kappa_B\). This is finitely generated over \(k\).

We first check the perfect-core condition needed in W.1. Every element of \(\bigcap F^{p^n}\) is algebraic over \(k\). If such an element \(x\) were transcendental, extend it to a transcendence basis of \(F/k\). The finite extension of its rational function field could not contain all \(x^{1/p^n}\): their degrees over that rational function field are \(p^n\), unbounded. This is a contradiction. In a separable algebraic closure \(F^{\mathrm{sep}}\), the perfect core is precisely \(\bar k\). In fact, for an element of that core choose a finite Galois extension of \(F\) containing it. Its successive \(p\)-th roots belong to the same extension, since they are both purely inseparable over it and separable over \(F\). Symmetric functions of their Galois conjugates show that the coefficients of its minimal polynomial have all their \(p\)-power roots in \(F\). Those coefficients are algebraic over \(k\) by the preceding argument. Hence the element is algebraic over \(k\) and lies in \(\bar k\). The reverse inclusion follows because \(k\) is perfect.

Let \(A^{\mathrm{nr}}\) be the union of the finite unramified extensions of \(A\) in a chosen separable closure, with residue field \(\bar k\). These extensions are obtained by lifting separable residue polynomials by the earlier henselian theorem; their directed union is a DVR with the same uniformizer. Its completion \(A^*\) is a complete DVR with residue \(\bar k\). Let \(B^*\) be the completion of a strict henselization of \(B\), with residue field \(F^{\mathrm{sep}}\). Choose the compatible embedding \(\bar k\subset F^{\mathrm{sep}}\). The henselian lifting property maps each finite unramified extension into the strict henselization of \(B\), and continuity extends their union to \(A^*\to B^*\).

Here is the coefficient reduction, including the mixed-characteristic case. In equal characteristic put \(\Lambda=\bar k[[t]]\), mapping \(t\) to the uniformizer of \(A^*\). A coefficient field of \(B^*\), compatible on the perfect \(\bar k\), gives a weakly unramified coefficient DVR \(\Lambda_F=F^{\mathrm{sep}}[[t]]\to B^*\). In mixed characteristic take a Cohen ring \(\Lambda\) of \(\bar k\). The maps from its quotients to \(A^*/\mathfrak m^n\) lift successively by Coefficient rings and the Cohen structure theorem, Theorem 4.1, giving \(\Lambda\to A^*\). Construct a flat residue extension of \(\Lambda\) with residue \(F^{\mathrm{sep}}\) by Lemma 3.1 of that lesson, and complete it in \((p)\), obtaining a Cohen DVR \(\Lambda_F\). The maps \(\Lambda/p^n\to\Lambda_F/p^n\) are formally smooth: in degree one, the prime-field lifting lemma lifts a map from \(F^{\mathrm{sep}}\) across a square-zero ideal. Its restriction to the perfect \(\bar k\) is the prescribed one, by uniqueness of perfect-field lifts, so this is formal smoothness over \(\bar k\). Cancellation of \(p\) proves quotient flatness exactly as in the Cohen-ring construction, and the split-conormal lifting lemma, Lemma 2.1, gives every higher quotient. Their lifting property constructs a compatible \(\Lambda\)-map \(\Lambda_F\to B^*\). In both characteristics \(\Lambda\subset\Lambda_F\) is weakly unramified and has the residue fields required by (W.1).

The ring \(B^*\) is finite over \(\Lambda_F\). Their residue fields agree and the image of a uniformizer of \(\Lambda_F\) is nonzero in \(B^*\). Lifts of a basis modulo that image generate by successive approximation and completeness; this gives a finite module. Thus W.6 supplies a finite weak solution for \(\Lambda\subset B^*\). Form its compositum with \(\operatorname{Frac}(A^*)\) and select a field factor. In every normalized branch, the index from the new coefficient DVR to the new \(B^*\)-DVR is one. Factoring it through the new \(A^*\)-DVR and multiplying indices shows that the latter index is also one. All its residue fields on the base side are \(\bar k\). We have obtained a solution \(H^*/\operatorname{Frac}(A^*)\) for \(A^*\subset B^*\).

We descend this extension and check every branch. Enlarge it, if necessary, to a separable extension after a uniformizer-root extension as described after D.1. Apply D.1 to the dense field \(\operatorname{Frac}(A^{\mathrm{nr}})\). All coefficients used by the approximating polynomial lie in one finite unramified extension \(K_j\) of \(K=\operatorname{Frac}(A)\). This gives a finite field extension \(H_j/K_j\) whose tensor product with \(\operatorname{Frac}(A^*)\) is exactly \(H^*\), a field of the same degree.

The residue degree of \(H_j/K_j\) is one. Otherwise its finite residue extension, which is separable because \(k\) is perfect, would lift by Hensel to a nontrivial unramified intermediate field. That field splits after extension to \(\operatorname{Frac}(A^*)\), contradicting the displayed field tensor product. Therefore a uniformizer of \(H_j\) has an Eisenstein polynomial of the full extension degree over \(K_j\). It remains Eisenstein over \(A^*\). The new \(A^*\)-DVR is consequently weakly unramified over the \(H_j\)-DVR. Multiplicativity of indices now shows that at least one normalized \(B\)-branch after \(H_j\) has index one: extend the valuation from \(B\) through \(B^*\), use the solution \(H^*\), and restrict it back. Its base residue field is finite over the perfect \(k\), so its residue extension is separable.

Take a finite normal closure \(H/K\) of \(H_j/K\). The index-one branch remains a solution in every further matching finite base extension, by K.3 with index one. Every normalized \(B\)-branch for the normal extension \(H/K\) is conjugate to this one. For a separable normal extension the field tensor product is a Galois algebra, and the integral closure has invariants equal to the normal DVR \(B\). If two maximal ideals had different orbits, prime avoidance would give an element in one and outside every conjugate of the other. Its product over the group would lie in \(B\), vanish in the first residue field and be nonzero in the second, although both maximal ideals contract to the maximal ideal of \(B\). This is impossible. For a normal extension with a purely inseparable part, apply the same argument after its maximal purely inseparable intermediate field; a purely inseparable field extension has a unique prolongation of each valuation. Thus all branches are solutions. All integral closures here are finite: \(A\) is complete Nagata, and \(B\) is Nagata by the earlier finite-type and localization theorem. This proves the lemma. ∎

**Proposition D.3 (DVR elimination with separable generic field).** Let \(A\) be a Nagata DVR and \(A\subset B\) a local inclusion of DVRs, with \(B\) essentially of finite type over \(A\) and \(L/K\) separable. A finite solution exists.

**Proof.** Only positive residue characteristic needs proof, by Abhyankar in residue characteristic zero. Choose lifts \(x_i\in A\) of a \(p\)-basis of \(k=\kappa_A\). In a fixed algebraic closure of \(K\), adjoin compatible \(p^n\)-th roots of the \(x_i\)'s. Each ring obtained using finitely many indices and a finite exponent is a finite free local DVR over \(A\), with the same uniformizer \(\pi\). Indeed its reduction is the field obtained by adjoining the corresponding \(p^n\)-th roots of the \(p\)-independent residue elements; its maximal ideal is generated by the nonzerodivisor \(\pi\). Their union \(A_\infty\) is again a DVR: every nonzero element is a unit times an integral power of \(\pi\) already in a finite stage, and every nonzero ideal is generated by an element of least valuation. Its residue field \(k_\infty\) is perfect. Put \(K_\infty=\operatorname{Frac}(A_\infty)\), and let \(A'\) be its completion, with fraction field \(K'\).

The closed fibre of \(B\otimes_AA'\) has finitely many points and dimension zero. It is a base change of the Artinian ring \(B/\pi B\) by an algebraic residue-field extension, and it is Noetherian because the whole tensor ring is essentially of finite type over the Noetherian \(A'\). Semilocalize at these points, obtaining \(R'\). It is reduced: \(\pi\) is a nonzerodivisor, and the separability of \(L/K\) makes the generic tensor ring reduced. At a closed-fibre prime, the principal ideal theorem gives local dimension one. The finite-type Nagata theorem over the complete \(A'\) therefore gives a finite normalization of \(R'\), a finite product of semilocal Dedekind domains. Its closed local rings are DVRs essentially of finite type over \(A'\).

Apply D.2 to their finitely many branches. Take a finite compositum of the resulting field extensions. A solution remains one under further finite extension by K.2. Thus for a finite \(H'/K'\), with base DVR \(A'_1\), the normalization \(S'\) of the corresponding vertical semilocal tensor ring has index one over \(A'_1\) at every closed point. Enlarge \(H'\) to a separable extension after a uniformizer-root extension, as after D.1. D.1 gives a finite \(H_\infty/K_\infty\) whose completed tensor field is exactly \(H'\).

Let \(A_1\) be the integral closure of \(A_\infty\) in \(H_\infty\). It is finite: first the uniformizer-root extension is a monogenic DVR, and the subsequent separable closure is finite by the earlier trace-lattice theorem. It has only one maximal ideal. In fact completion decomposes its finite normal algebra into the completions of its local DVRs; its generic tensor algebra is the single field \(H'\), so only one factor occurs. It is a DVR with perfect residue field \(k_1\), and its completion is \(A'_1\). Fix a uniformizer \(\rho\in A_1\).

Set \(R_1=B\otimes_AA_1\). It is Noetherian, because it is essentially of finite type over the Noetherian \(A_1\); it is integral over \(B\), and therefore has dimension one. All its maximal ideals contain \(\rho\). Its generic tensor is reduced by separability, and \(\rho\) is a nonzerodivisor, so \(R_1\) is reduced. The map from \(R_1\) to the vertical semilocal ring over \(A'_1\) induces isomorphisms modulo every \(\rho^n\). Completion of \(A_1\) does not change these quotients, and elements inverted in the vertical semilocalization are already units modulo \(\rho^n\).

The finite normalization \(S'\) agrees with that semilocal ring after inverting \(\rho\), since a reduced zero-dimensional Noetherian ring is a product of fields. Choose a conductor power and apply E.1 to transfer this finite order through an isomorphism modulo a sufficiently high power of \(\rho\). It produces a finite overring
\[
R_1\subset S_1\subset R_1[1/\rho],
\qquad S_1/\rho S_1\simeq S'/\rho S'.
\tag{D.1}
\]
The right-hand side is a product of finitely generated separable extensions of \(k_1\): the normalized branches have index one and \(k_1\) is perfect. Consequently every closed local ring of \(S_1\) has maximal ideal generated by \(\rho\), a nonzerodivisor, and is a DVR. Its generic local rings are fields. Thus \(S_1\) is normal and is the normalization of \(R_1\). In particular this normalization is finite. The residue algebra in (D.1) is geometrically reduced over \(k_1\).

Finally descend a finite algebra, rather than only residue-field generators. Write \(H_\infty\) as the directed union of its finite subextensions \(K_i/K\), and let \(A_i\) be the integral closure of \(A\) in \(K_i\). Since \(A\) is Nagata these are finite Dedekind domains, and \(A_1=\bigcup_i A_i\). Each \(A_i\) is local: its integral extension \(A_1\) is local, and lying over covers every maximal ideal. It is a DVR, and \(A_i\to A_1\) is faithfully flat, being a local torsion-free map of DVRs.

Choose the finite stage large enough to contain \(\rho\). It is then a uniformizer of \(A_i\): its valuation in \(A_1\) is one, so the ramification index of \(A_i\subset A_1\) and its own positive valuation in \(A_i\) must both be one. The finite \(R_1\)-algebra \(S_1\) has a finite presentation, including a monic relation for each algebra generator. All its coefficients lie at one further finite stage, which still contains \(\rho\). Thus there is a finite algebra \(T_i\) over \(B\otimes_AA_i\) with
\[
T_i\otimes_{A_i}A_1\simeq S_1.
\tag{D.2}
\]
After inverting the base uniformizer its structural map is an isomorphism: this can be checked after the faithfully flat field extension \(K_i\subset H_\infty\), where it is the generic equality for \(S_1\). The structural map is therefore injective, since \(B\otimes_AA_i\) has no base torsion. Faithful flatness in (D.2) also shows that \(T_i\) has no base torsion.

Let \(k_i=\kappa_{A_i}\). The closed fibre \(Q_i\) of \(T_i\) satisfies \(Q_i\otimes_{k_i}k_1=S_1/\rho S_1\). It is geometrically reduced. Indeed \(k_1/k_i\) is algebraic. For any field \(h/k_i\), embed \(k_1\) into an algebraic closure \(h'\) of \(h\), compatibly on \(k_i\). Then
\[
Q_i\otimes_{k_i}h'
 =(S_1/\rho S_1)\otimes_{k_1}h'
\]
is reduced. Faithful flatness of \(h\subset h'\) makes \(Q_i\otimes_{k_i}h\) reduced as well. Now \(Q_i\) is zero-dimensional and Noetherian, so is a product of fields. Each factor is finitely generated over \(k_i\), since \(T_i\) is essentially of finite type over \(A_i\), and is separable by its geometric reducedness. Every maximal ideal of \(T_i\) is thus generated locally by the uniformizer of \(A_i\). Its local rings are DVRs, and its generic local rings are the indicated fields. Hence \(T_i\) is normal and is exactly the normalization of \(B\otimes_AA_i\). Its closed local DVRs have index one and separable residues over \(A_i\). This says precisely that \(K_i/K\) is a finite solution. ∎

Combining D.3 with E.3 makes the solution finite separable whenever \(L/K\) is separable. The final assertion retains arbitrary residue fields of the original Nagata DVR; the perfection and completion occur only inside its proof.

### 3.5. Generic fields and normalized reduced fibres

**Lemma G.1 (perfect fields and generic smoothness).** A finitely generated field extension of a perfect field is separably generated. A geometrically reduced finite-type scheme over any field is smooth on an open subset meeting every irreducible component.

**Proof.** In characteristic zero a transcendence basis leaves a finite algebraic separable extension. In characteristic \(p\), let \(F/k\) have transcendence degree \(r\), with \(k\) perfect. For any transcendence basis \(t_1,\ldots,t_r\), Frobenius and tower degrees give
\[
[F:F^p]=p^r:
\quad [F:k(t)^p]=[F:k(t)]p^r,
\quad [F^p:k(t)^p]=[F:k(t)].
\tag{G.1}
\]
Choose a \(p\)-basis \(u_1,\ldots,u_r\) of \(F\), whose existence was proved in Coefficient rings and the Cohen structure theorem, Lemma 1.1. These elements are algebraically independent over \(k\). Otherwise take a nonzero polynomial relation of least degree and write its exponents modulo \(p\), using \(k=k^p\). Independence of the \(p\)-basis monomials over \(F^p\) says that each lower-degree coefficient polynomial is itself a relation, a contradiction. The \(p\)-basis presentation gives a basis \(du_i\) of \(\Omega_{F/k}\). Consequently \(\Omega_{F/k(u)}=0\). The extension \(F/k(u)\) is finite algebraic, and is separable by Formally smooth, unramified and étale ring maps, Lemma 7.1. This proves the first assertion.

For the second, pass to an algebraic closure \(\bar k\). The scheme stays reduced. At each generic point its local ring is a field, hence regular; its residue field over the perfect \(\bar k\) is separably generated by the first assertion. The separable-residue Jacobian criterion therefore makes every generic point smooth. The Jacobian rank at a generic point is unchanged by extending its residue field, and component dimensions are unchanged by an algebraic extension of the ground field. The same criterion descends smoothness to the original generic points. Its open locus contains them all. This uses the actual field criterion in Smooth algebras over a field and the Jacobian criterion, Theorems 2.1 and 3.2, including the distinction between local dimension and component dimension. ∎

A separably generated field is geometrically reduced: it is finite étale over a rational function field, and after any extension of the constant field its tensor algebra is finite étale over a localization of a polynomial ring, hence reduced. A reduced algebra embeds in the product of the fields of its irreducible components. Tensoring that injection by a field extension shows that it is geometrically reduced whenever those component fields are separable.

**Lemma G.2 (finite generic preparation).** If \(Z\) is of finite type over a field \(K\), there is a finite extension \(K_0/K\) for which \((Z_{K_0})_{\mathrm{red}}\) is geometrically reduced.

**Proof.** Only characteristic \(p>0\) needs proof. Extend first to the perfection \(K^{\mathrm{perf}}\). On each of finitely many affine charts the nilradical is a finitely generated ideal. Its generators, their finitely many expressions and nilpotence equations, and the comparisons on overlaps involve finitely many coefficients from the algebraic extension \(K^{\mathrm{perf}}/K\). Choose one finite subextension containing them. This gives a nilpotent ideal \(J\) on \(Z_{K_0}\) whose base change is exactly the nilradical on \(Z_{K^{\mathrm{perf}}}\). The quotient's base change is reduced, so faithful flatness makes the quotient itself reduced; since \(J\) is nilpotent it is precisely the nilradical already over \(K_0\).

Over the perfect field \(K^{\mathrm{perf}}\), a reduced algebra is geometrically reduced. Indeed its generic fields are separably generated by G.1, and the product-of-fields injection just described proves the assertion. Geometric reducedness descends from this field extension: embed the perfection compatibly into an algebraic closure of any proposed extension field and use faithful flatness to detect a nilpotent. Thus the reduced quotient over \(K_0\) is geometrically reduced. In characteristic zero the same argument over the already perfect \(K\) requires no extension. ∎

**Theorem 3.3 (normalized reduced-fibre theorem).** Let \(A\) be a Nagata Dedekind domain with fraction field \(K\), and \(X\) a flat scheme of finite type over \(A\). There is a finite extension \(E/K\) such that, for the integral closure \(A_E\) and the normalization
\[
Y=\operatorname{Nor}\bigl((X\times_A A_E)_{\mathrm{red}}\bigr),
\tag{G.2}
\]
the morphism \(Y\to\operatorname{Spec}A_E\) is smooth at every generic point of every fibre. All its fibres are reduced. If the field of each generic component of \(X\) is separable over \(K\), the extension \(E/K\) can be chosen separable.

**Proof.** If \(X\) is empty the assertion is immediate. All normalizations used below are finite by Normalization, Theorem 5.2: the base is Nagata and the schemes have finite type. Quotienting a torsion-free module by its nilradical in a flat algebra over a domain keeps it torsion-free. In fact \(ax\) nilpotent, with \(a\ne0\) in the base, implies \(a^n x^n=0\), then \(x^n=0\). Normalization in the dominant generic fields also has no base torsion. Over a Dedekind domain torsion-free modules are flat, as can be checked in its DVR localizations. Thus reductions and normalized base changes here remain flat, with only dominant components.

Apply G.2 to the generic fibre, make that finite extension of \(K\), and normalize the reduced base change. We may consequently start with \(X\) normal and with separable generic component fields. Indeed the generic normalization is birational to the geometrically reduced generic fibre, so has the same component fields. If the separability assumption in the last assertion of the theorem was given initially, reduction and normalization alone suffice and no initial extension is made. At the end, transitivity of integrality identifies the successive normalized base changes with (G.2) for the composite field extension.

By G.1 the smooth locus \(U\subset X\) meets every generic component. Only finitely many vertical height-one points lie outside \(U\). Such a point is necessarily a generic point of a component of the closed subset \(X\setminus U\): a component of that subset through it has positive height, because no generic point of \(X\) belongs to the subset, and its height is at most one. Enumerate these finitely many points as \(x_1,\ldots,x_s\), with images \(a_i\in\operatorname{Spec}A\). Each
\[
A_{a_i}\subset\mathcal O_{X,x_i}
\tag{G.3}
\]
is a local inclusion of DVRs. The right side is essentially of finite type, Nagata, and has separable fraction field over \(K\). Proposition D.3 gives a finite solution; Lemma E.3 permits a finite separable solution. Choose one common finite separable extension containing all these solutions. K.2 shows that they remain solutions after this enlargement. If there are no such points, use \(E=K\) at this stage.

Let \(Y\) be the resulting normalization, and take a generic point \(y\) of a closed fibre. Its local ring is a DVR: it is a height-one local ring of the normal scheme \(Y\), because it is minimal over the nonzero base uniformizer. The image \(x\in X\) also has height one. To check this, work in the dominant component. The finite map \(Y\to X\) is integral with normal target; going down and incomparability give equality of the heights at matching points. This is the earlier integral-extension theorem and does not assume that an unnormalized tensor product is normal.

The open \(U\times_A A_E\) is smooth over the regular base \(A_E\), hence regular and normal. Normalization is an isomorphism there. If \(y\) lies in it there is nothing to prove. Otherwise its image is one of the \(x_i\). Localization of integral closure identifies \(\mathcal O_{Y,y}\) with exactly the local normalization branch of (G.3) after the chosen field extension. By the solution property, the base uniformizer generates its maximal ideal and its residue field is separable over the base residue field. Its local fibre is therefore a separable finitely generated field. The field Jacobian criterion makes the fibre smooth at \(y\); flatness and the fibrewise smoothness theorem make \(Y\to\operatorname{Spec}A_E\) smooth at \(y\).

The generic fibre is smooth at its generic points by its separable component fields. This proves the asserted smoothness for every fibre, including the generic one. For reducedness of a closed fibre, normality of \(Y\) gives Serre's condition \(S_2\); quotienting by a nonzerodivisor gives \(S_1\). Thus the fibre has no embedded associated primes. It is generically reduced by the smoothness just proved, so is reduced: a nonzero nilpotent ideal would have an associated prime, necessarily a minimal prime, where it has already vanished. The generic fibre is normal and reduced as well. Empty fibres require no separate argument.

When the generic component fields were separable initially, every extension used in (G.3) and their common composite was finite separable. That is the last assertion. In the general case the first finite extension from G.2 may be inseparable; the conclusion still has precisely the unrestricted finite-extension scope stated. ∎

The normalized smoothness statements are [Stacks, Tag 09IL](https://stacks.math.columbia.edu/tag/09IL) and its [separable variant, Tag 0BRR](https://stacks.math.columbia.edu/tag/0BRR).

## 4. The specialization theorem

**Theorem 4.1 (residue characteristic zero).** For a smooth proper morphism \(X\to S\) with geometrically connected fibres and \(s'\leadsto s\), if \(\operatorname{char}\kappa(s)=0\), then
\[
\operatorname{sp}:\pi_1(X_{\bar s'})\xrightarrow{\sim}
\pi_1(X_{\bar s}).
\tag{4.1}
\]

**Proof.** Section 1 reduces to a strictly henselian DVR and proves surjectivity. Lemmas 3.1 and 3.2 put every finite étale cover of the geometric generic fibre in the essential image of restriction from the family. To check injectivity explicitly, let \(g\) belong to the kernel of specialization. Every finite quotient of the generic group is realized by a connected Galois cover. Its extension over the family is determined by a special-fibre cover, so that quotient map factors through specialization, up to the chosen fibre identification. It kills \(g\). An element of a profinite group killed by all its finite quotients is the identity. This proves injectivity. The reductions identify this map with the original chosen specialization. ∎

This proves [Stacks, [Tag 0C0Q](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-proposition-specialization-map-isomorphism)].

For a profinite group \(G\) and prime \(p\), write
\[
G^{(p')}=
\varprojlim_{\substack{N\triangleleft G\ {\rm open}\\
[G:N]\ {\rm prime\ to}\ p}}G/N.
\tag{4.2}
\]
Equivalently it is the largest quotient all of whose finite quotients have order prime to \(p\). We write \(\pi_1'\) for this group when \(p\) is fixed. This is a quotient of the entire group; it can be nonabelian.

**Theorem 4.2 (residue characteristic \(p\)).** Under the same family hypotheses, if \(\operatorname{char}\kappa(s)=p>0\), then specialization is surjective and induces
\[
\pi_1'(X_{\bar s'})\xrightarrow{\sim}\pi_1'(X_{\bar s}).
\tag{4.3}
\]

**Proof.** Surjectivity is Lemma 1.2. Every finite quotient of the generic group of order prime to \(p\) gives a connected Galois cover to which Lemmas 3.1 and 3.2 apply. The extended \(G\)-action shows that this exact quotient factors through specialization. Hence its kernel contains the specialization kernel. The intersection of the kernels of all these quotients is exactly the kernel of \(G\to G^{(p')}\). It follows that the induced map in (4.3) is injective. It is surjective because specialization is surjective and taking the specified maximal quotient preserves surjections. ∎

This proves [Stacks, [Tag 0C0R](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/pione.html#pione-theorem-specialization-map-isomorphism-prime-to-p)] at the full smooth proper generality. A nongalois cover of degree prime to \(p\) can have a Galois closure whose order is divisible by \(p\); that degree condition is not what the proof uses. Nor is (4.3) merely an equality of prime-to-\(p\) parts of abelianizations.

## 5. Smooth proper curves and their presentations

Put
\[
\Gamma_g=\left\langle a_1,b_1,\ldots,a_g,b_g
\middle|\ \prod_{i=1}^g[a_i,b_i]=1\right\rangle,
\qquad [a,b]=aba^{-1}b^{-1}.
\tag{5.1}
\]
Its profinite completion is formed from all finite quotients. Its prime-to-\(p\) completion is formed only from finite quotients of order prime to \(p\). For \(g=0\) the group is trivial.

The finite-cover comparison used here is Comparison with the classical topology, Proposition 2.1 and Theorem 3.1: for a proper complex scheme, analytification identifies finite étale covers with finite topological covers, including every morphism. Its proof gives a topological cover its unique locally isomorphic analytic structure, algebraizes its finite locally free analytic algebra and its product and unit by GAGA, and descends freeness and vanishing differentials at each point. Full faithfulness algebraizes every map of covers. For a projective curve the exact GAGA inputs are Serre's comparison theorems and Chow's theorem, Theorems 3.1, 4.1 and 5.2. The construction respects the fibre over a chosen complex point.

We prove the genus and surface presentation needed for this application. Constant-sheaf cohomology on a manifold agrees with singular cohomology by Sheaf cohomology and singular cohomology on manifolds, Theorem 1.3. The graph and attaching-cell fundamental-group calculations are Fundamental groups of graphs and two-complexes, Corollary 2.4 and Theorem 3.3. For homology we use the finite-skeleton excision argument in Comparison with singular cohomology, Section 14, and the explicit attaching-boundary calculation in Universal covers and cellular chains, Proposition 5.2. The calculation below only needs the graph and the single attached disc.

**Lemma 5.A (a polygon for the complex curve).** The classical space \(M=C(\mathbf C)\) of a smooth projective connected complex curve has a cell decomposition with one vertex, \(2h\) edges and one face, for some integer \(h\ge0\), whose oriented attaching word is
\[
\prod_{i=1}^h a_i b_i a_i^{-1}b_i^{-1}.
\tag{5.A1}
\]
Consequently \(\pi_1^{\mathrm{top}}(M)=\Gamma_h\),
\(\dim_{\mathbf C}H^1(M,\mathbf C_M)=2h\), and
\(H^2(M,\mathbf C_M)=\mathbf C\).

**Proof.** Smoothness supplies complex coordinate discs. The space is Hausdorff and compact, since it is closed in complex projective space. It is connected: a nontrivial clopen partition would give a section of the trivial two-sheeted topological cover. Full faithfulness of the finite-cover comparison would algebraize that section and give a nontrivial clopen partition of \(C\). Holomorphic coordinate changes preserve orientation, their real determinant being \(|f'|^2>0\).

We first construct a finite triangulation in this particular situation. Choose a nonconstant rational function \(t\) on \(C\). At every point its DVR either contains \(t\) or contains \(t^{-1}\); these charts extend it to a morphism \(C\to\mathbf P^1\). It is proper and quasi-finite, since a fibre is a proper closed subset of the integral curve. Zariski's Main Theorem, Theorem 4.2, factors it as an open immersion into a finite scheme. This immersion is also proper, since the curve is proper and the intermediate scheme is separated over the base; its image is therefore closed. Thus the morphism is finite. The complex-point map is proper with finite fibres, as proved in the finite-map calculation of the comparison lesson, Section 3.

There are only finitely many branch values. Indeed the nonzero differential of \(t\) in characteristic zero has finitely many zeros on the affine chart, and the same holds for \(t^{-1}\) above infinity. At a point, the convergent power series of the map has the form \(z^e u(z)\), with \(u(0)\ne0\). On a sufficiently small disc, the power-series root of the nonvanishing unit \(u\) gives the coordinate \(w=z\,u(z)^{1/e}\), in which the map is \(w\mapsto w^e\). The change is invertible because its derivative at zero is nonzero. Thus away from those finitely many values it is an ordinary finite covering, and over a branch value it has this explicit local form.

Triangulate the sphere with every branch value a vertex. This can be done starting with a tetrahedral triangulation and inserting the finitely many selected points one at a time, subdividing the face or edge containing the next point. Every open triangle and every open edge has trivial covering sheets. Their lifts close to finitely many triangles upstairs: near an endpoint the model \(w^e\) lifts the radial sectors to sectors, with a single vertex for each endpoint in the fibre. A triangle has distinct base vertices, so its lifted vertices remain distinct. These lifted triangles and edges give a finite cell triangulation; subdivision separates any distinct edges with the same endpoints. This supplies the finite triangulation of \(M\) used below.

Here is the oriented polygon reduction for a connected closed triangulated surface. Choose a spanning tree \(T\) in its edge graph. The dual graph remains connected after deleting the edges dual to \(T\). Otherwise the boundary, modulo two, of one nonempty proper collection of faces would be a nonzero cycle supported in \(T\); a tree has no such cycle. Choose a spanning tree \(T^*\) in this remaining dual graph. Gluing the triangles successively along \(T^*\) makes one polygonal disc: at each tree step one disc is joined to the current disc along a boundary edge.

Contract \(T\) to a point. This contraction preserves the homeomorphism type of the surface. To check it locally, take small vertex discs and rectangular edge bands around the embedded tree. Their union is a disc: remove a leaf vertex and its band successively. For a leaf edge, the two endpoint discs and connecting band are a disc neighbourhood of a polygonal arc. Straighten the arc in this neighbourhood. Boundaries of its nested rounded rectangular neighbourhoods give polar curves in the quotient: collapse the central arc to radius zero and send each surrounding curve to the circle of its radius. This gives a homeomorphism of the quotient neighbourhood to a disc, with the same outer boundary. Extending by the identity outside the neighbourhood and repeating proves the assertion for the tree. Equivalently the polygonal boundary moves merge the two endpoint vertices while deleting that tree edge. We now have one vertex and one face. Every remaining edge occurs twice on the boundary, once in each orientation.

Write \(r\) for the number of remaining edges. The cell counts give
\(r=2-\chi(M)\). If \(r=0\), the face has its boundary collapsed to the vertex, giving a sphere. If \(r>0\), some two pairs of boundary sides must interlace. If no two pairs interlaced, an innermost pair in the resulting noncrossing pairing would be adjacent. Since its two orientations are opposite, the intervening corner is identified only with itself and is a vertex distinct from all the other corners. That contradicts the one-vertex construction.

For two interlaced pairs, join their midpoints across the interior of the polygon. The two arcs can be chosen to cross transversely once and to have no other intersection. After the side identifications they are two embedded oriented circles meeting at one point. A small regular neighbourhood is a disc with two untwisted bands attached in alternating order. Tracing its boundary gives \(aba^{-1}b^{-1}\); it has one boundary circle and is the usual torus with an open disc removed. This description also follows by cutting the two bands along their centres: the resulting square has its opposite sides identified and one interior disc deleted.

Its complement is connected. Every component of the complement must meet the boundary, since a component with no boundary would be clopen in \(M\). A collar of the single boundary circle belongs to only one component, so there is only one. Cap that circle by a disc, obtaining another connected closed oriented surface \(M'\). The cuts are polygonal after subdivision, so \(M'\) still has a finite triangulation. Additivity of the cell counts along the boundary circle gives
\[
\chi(M')=\chi(M)+2,
\qquad 2-\chi(M')=r-2.
\tag{5.A2}
\]
This is again a nonnegative number of edges in the one-vertex, one-face construction. Repetition therefore terminates at a sphere. It expresses \(M\) as a sphere with \(h\) of these handles. Keep the two band loops on each handle and join their base points by a tree in the remaining sphere. Cutting along these loops and that tree gives a disc; tracing its oriented boundary gives (5.A1), in the order of the handles. This proves the stated cell decomposition.

The graph calculation gives a free group on its \(2h\) edges, and the attaching-cell theorem imposes exactly the normal closure of (5.A1). This proves the fundamental-group assertion.

Here is the homology calculation with \(\mathbf C\) coefficients. Write \(G\) for the one-skeleton and \(v\) for its vertex. Excision for the attached cells gives \(H_q(G,\{v\};\mathbf C)=\mathbf C^{2h}\) in degree one and zero in other degrees, and \(H_q(M,G;\mathbf C)=\mathbf C\) in degree two and zero in other degrees. These are exactly the relative disc generators in the finite-skeleton argument cited above: collapsing the preceding skeleton gives the wedge of its attached spheres, with each generator oriented by its characteristic disc. The graph's edges have the same initial and terminal vertex, so the first pair's connecting map is zero. Consequently \(H_1(G;\mathbf C)=\mathbf C^{2h}\) and \(H_2(G;\mathbf C)=0\). For the second pair, the connecting map sends the disc generator to the class of its boundary walk. Proposition 5.2 computes this as the sum of the oriented occurrences of each edge; every edge occurs once with each sign in (5.A1), so this map is zero. The pair's exact sequence is therefore
\[
0\longrightarrow H_2(M;\mathbf C)\longrightarrow\mathbf C
 \xrightarrow{0}\mathbf C^{2h}
 \longrightarrow H_1(M;\mathbf C)\longrightarrow0.
\]
Thus \(H_2(M;\mathbf C)=\mathbf C\) and \(H_1(M;\mathbf C)=\mathbf C^{2h}\). Dualizing a complex of vector spaces gives the dual homology in cohomology: a functional on cycles that kills boundaries extends to the whole chain space, and a functional vanishing on cycles factors through the boundary map and extends to the preceding chain space. This proves both surjectivity and the stated kernel of the evaluation map, without choosing a natural splitting. It gives singular cohomology of dimensions \(2h\) and one. The constant-sheaf comparison gives the cohomology assertions of the lemma, including \(h=0\). ∎

This polygon argument is the orientable case of the classification of triangulated surfaces; a freely accessible treatment is Jean Gallier, [*The Classification Theorem for Compact Surfaces and a Detour on Fractals*, arXiv:0805.0562v1](https://arxiv.org/abs/0805.0562v1), Section 5.2. The triangulation here comes directly from the finite map of the complex curve.

**Lemma 5.B (algebraic genus and handle number).** In Lemma 5.A,
\[
h=\dim_{\mathbf C}H^1(C,\mathcal O_C)=g.
\tag{5.B1}
\]

**Proof.** Let \(\Omega_M^1\) be the sheaf of holomorphic one-forms. On a coordinate disc every one-form \(\sum_{n\ge0}c_nz^n\,dz\) has the primitive \(\sum_{n\ge0}c_nz^{n+1}/(n+1)\), convergent on every smaller disc. The kernel of differentiation consists of locally constant functions. Thus the following is an exact sequence of sheaves of complex vector spaces:
\[
0\to\mathbf C_M\to\mathcal O_M
 \xrightarrow{d}\Omega_M^1\to0.
\tag{5.B2}
\]

The algebraic canonical bundle of the smooth curve is \(\Omega^1_{C/\mathbf C}\), by Dualizing sheaves and Serre duality for projective schemes, Proposition 8.2. Its analytification is \(\Omega_M^1\): an algebraic étale coordinate gives a local holomorphic coordinate, and the two transition rules are the same differential rule. Serre duality, Theorem 4.2 of that lesson, and cohomological GAGA give
\[
\begin{aligned}
h^0(M,\Omega_M^1)&=h^1(M,\mathcal O_M)=g,\\
h^1(M,\Omega_M^1)&=h^0(M,\mathcal O_M)=1,\\
H^2(M,\mathcal O_M)&=0.
\end{aligned}
\tag{5.B3}
\]
Here \(H^0(C,\mathcal O_C)=\mathbf C\): proper coherence makes it finite-dimensional, and integrality makes this finite-dimensional algebra a field, so algebraic closedness identifies it with \(\mathbf C\). The degree-two coherent vanishing can also be seen by covering the projective curve with two affine hyperplane complements whose omitted finite sets are disjoint; their intersection is affine. The two-open Čech complex has no degree-two term. GAGA transports that vanishing to \(M\).

The map \(H^0(M,\mathbf C_M)\to H^0(M,\mathcal O_M)\) is the identity on \(\mathbf C\). At the other end of the long exact sequence of (5.B2),
\[
H^1(M,\Omega_M^1)\longrightarrow H^2(M,\mathbf C_M)
 \longrightarrow H^2(M,\mathcal O_M)=0
\]
is surjective between one-dimensional spaces, by (5.B3) and Lemma 5.A. It is therefore an isomorphism. Exactness consequently gives
\[
0\to H^0(M,\Omega_M^1)\to H^1(M,\mathbf C_M)
 \to H^1(M,\mathcal O_M)\to0.
\tag{5.B4}
\]
Its dimensions give \(2h=2g\), proving (5.B1). ∎

Finite topological covers of the connected surface \(M\), with their fibre over a chosen point, are finite sets with an action of \(\Gamma_g\). Covering-space classification with all morphisms is proved in Galois categories, Section 5.2, and the fibre-functor argument for profinite completion is in the comparison lesson, Section 5. Thus the algebraic cover equivalence gives
\(\pi_1(C)\simeq\widehat{\Gamma_g}\). Equivalently its profinite presentation is the free profinite group on the displayed generators modulo the **closed** normal subgroup generated by the face word: the finite quotients of that group are exactly the finite quotients of \(\Gamma_g\). This includes \(g=0\), where both the presentation and the group are trivial.

**Proposition 5.1 (characteristic zero).** A smooth projective connected curve \(C\) of genus \(g\) over any algebraically closed field \(k\) of characteristic zero has
\[
\pi_1(C)\simeq\widehat{\Gamma_g}.
\tag{5.2}
\]

**Proof.** Its projective embedding and equations descend to a field \(K\subset k\) finitely generated over \(\mathbb Q\). Smoothness descends, and geometric connectedness is detected after extending to \(k\). Let \(k_0\) be the algebraic closure of \(K\) inside \(k\). Embed \(K\) in \(\mathbb C\) by choosing algebraically independent images for a transcendence basis, and extend the embedding to \(k_0\). Proper field invariance identifies the finite-cover categories of \(C\), its model over \(k_0\), and its complex base change. A finite affine Čech complex and flat extension of scalars preserve \(H^1(\mathcal O)\), so the genus is the same. The complex finite-cover comparison and Lemmas 5.A–5.B give (5.2). Only the finitely generated field of definition was embedded in \(\mathbb C\); no cardinality restriction on \(k\) is needed. ∎

To apply this in characteristic \(p\), the missing bridge is an actual smooth proper lift. The deformation theory is supplied by the lessons Formal moduli and Schlessinger's theorem, Proposition 7.2, and Deformations of rings and schemes and the naive cotangent complex, Theorem 8.1. They prove the small-extension obstruction theorem over a complete local coefficient ring, including mixed characteristic. We apply it rather than repeat its general proof.

**Lemma 5.2 (lifting a curve).** Every smooth proper connected curve \(C/k\), with \(k\) algebraically closed of characteristic \(p>0\), is the special fibre of a smooth projective family with geometrically connected fibres over a complete DVR of characteristic zero with uniformizer \(p\) and residue field \(k\).

**Proof.** Choose a Cohen ring \(R\) for \(k\): this is a complete DVR with uniformizer \(p\) and residue field \(k\), whose existence for every characteristic-\(p\) field is proved in Coefficient rings and the Cohen structure theorem, Theorem 4.1; see also [Stacks, Tag 0328](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-cohen-rings-exist). It has characteristic zero because \(p\) is nonzero and not a unit. We first verify projectivity of \(C\). A nonconstant rational function extends to a finite morphism \(f:C\to\mathbf P^1_k\), by the algebraic DVR and proper quasi-finite argument of Lemma 5.A, which works in every characteristic. Put \(L_0=f^*\mathcal O(1)\). For a standard affine chart of the line, its inverse image \(W=C_s\) is affine, since \(f\) is finite. If \(x\in U\subset C\) is open, choose such a \(W\) containing \(x\) and a distinguished open \(W_b\) with \(x\in W_b\subset U\cap W\). The extension-after-a-power lemma in Coherent sheaves on projective schemes: Serre's theorems, Lemma 1.1, extends \(b\) as \(\sigma/s^m\), for a global section \(\sigma\) of \(L_0^m\). The section \(s\sigma\) vanishes outside \(W\) and has nonvanishing open exactly \(W_b\). These affine section opens form a basis, so \(L_0\) is ample. Lemma 1.3 of that lesson embeds a positive power into projective space; properness makes the immersion closed. Thus \(C\) is projective.

In a projective embedding choose one hyperplane divisor, then another avoiding its finite support. Their affine complements cover \(C\); their intersection is affine because \(C\) is separated. The two-open Čech complex proves that every quasi-coherent sheaf on \(C\) has zero cohomology in degrees at least two.

The successive quotients \(R/p^{n+1}\to R/p^n\) are small extensions. The cited deformation theorem places the obstruction to lifting \(C_n\) in \(H^2(C,T_C)=0\). Starting from \(C_1=C\), choose compatible smooth proper lifts \(C_n/R/p^n\).

Choose a sufficiently high power \(L\) of an ample bundle so that it is very ample and \(H^1(C,L)=0\), by Coherent sheaves on projective schemes: Serre's theorems, Lemma 1.3 and Theorem 2.2. The square-zero units sequence proved in Picard groups and Grothendieck–Lefschetz places its lifting obstruction in \(H^2(C,\mathcal O_C)=0\). Thus it has compatible lifts \(L_n\) on the \(C_n\). Their successive reduction kernels are copies of \(L\); induction in the cohomology sequence gives \(H^1(C_n,L_n)=0\) and surjective reduction on sections. Lift a basis of \(H^0(C,L)\) compatibly. Nakayama makes these sections generate each \(L_n\), giving compatible maps
\[
C_n\longrightarrow\mathbb P^N_{R/p^n}.
\tag{5.3}
\]
They are closed immersions: reduction is the chosen closed embedding, and a closed immersion is detected across nilpotent thickenings. Concretely these proper maps are quasi-finite on their unchanged point spaces, hence finite; their finite-algebra maps are surjective modulo the nilpotent base ideal and therefore surjective by Nakayama.

Apply Algebraization of formal schemes, Theorem 1.1, to the projective ambient scheme \(X=\mathbb P^N_R\) and the ideal \((p)\) of the complete Noetherian ring \(R\). Its proof algebraizes the coherent quotient system using Grothendieck's existence theorem, Theorem 5.1, lifts the quotient map by full faithfulness, and detects its surjectivity by its zero formal cokernel. Thus the cartesian system (5.3) comes from a unique closed subscheme \(\mathcal C\subset\mathbb P^N_R\). It is projective, hence proper, over \(R\), and all its reductions are the specified \(C_n\). This is the projective case of the closed-subscheme algebraization theorem [Stacks, Tag 0899](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-algebraize-formal-closed-subscheme); the ambient scheme in this application is already projective.

We check the geometric properties of this algebraization. At a closed-fibre point the local ring modulo \(p^n\) is flat over \(R/p^n\). If \(px=0\) in the local ring, flatness modulo \(p^n\) puts its residue in \(p^{n-1}\) times that ring for every \(n\). Krull intersection gives \(x=0\). Thus it is torsion-free over the DVR, hence flat. Flatness and the smooth special fibre make \(\mathcal C/R\) smooth at all special-fibre points. The nonsmooth locus is closed; its proper image in the local base would contain the closed point if nonempty. It is therefore empty.

For a smooth proper family, the geometric connected-component scheme is finite étale over the base, as in the proper-schemes lesson's component theorem. Its special fibre is one point, so over the strictly henselian \(R\) it is the trivial one-point cover. Hence every fibre is geometrically connected. Projectivity was built into the embedding. ∎

Genus is constant in this family by Base change and the Grothendieck complex, Theorem 3.2 and Corollary 4.1. Apply them to the proper family and its structure sheaf, which is flat over the Noetherian DVR \(R\). They give one bounded complex \(K^\bullet\) of finite projective \(R\)-modules computing coherent cohomology after every base change, including each geometric fibre. Since \(R\) is local, these modules are finite free. For every fibre field \(\Omega\), cancellation of the boundary dimensions in a finite complex gives
\[
\chi(\mathcal C_\Omega,\mathcal O_{\mathcal C_\Omega})
 =\sum_i(-1)^i\dim_\Omega H^i(K^\bullet\otimes_R\Omega)
 =\sum_i(-1)^i\operatorname{rank}_R K^i.
\]
The right side is independent of the fibre. A smooth geometrically connected proper curve over an algebraically closed field has \(H^0(\mathcal O)=\Omega\), by proper finiteness and integrality as above, and no coherent cohomology above degree one by the two-affine cover. Its Euler characteristic is therefore \(1-g\). Equality of these Euler characteristics proves that the geometric generic and special fibres have the same genus.

**Corollary 5.3 (characteristic \(p\)).** Every smooth proper connected curve of genus \(g\) over an algebraically closed field of characteristic \(p\) has
\[
\pi_1'(C)\simeq\Gamma_g^{(p')}.
\tag{5.4}
\]

**Proof.** Lift by Lemma 5.2. Its geometric generic fibre has characteristic zero and the same genus. Proposition 5.1 computes its full group. Theorem 4.2 identifies its maximal prime-to-\(p\) quotient with that of \(C\). These quotients have exactly the finite quotients of \(\Gamma_g\) of order prime to \(p\), giving (5.4). ∎

For an elliptic curve this says
\[
\pi_1'(E)\simeq\prod_{\ell\ne p}\mathbb Z_\ell^2.
\tag{5.5}
\]
Indeed \(\Gamma_1=\mathbb Z^2\); its finite quotients of order prime to \(p\) are controlled by the subgroups \(n\mathbb Z^2\), with \(p\nmid n\). For good reduction of an elliptic curve over any DVR of residue characteristic \(p\), Theorem 4.2 identifies these geometric prime-to-\(p\) groups under specialization. The statement concerns geometric fibres; an arithmetic fundamental group also retains its absolute Galois group.

## 6. Nodal and wild changes

### 6.1. A nodal cubic

Let \(R=k[[t]]\), with \(k\) algebraically closed and \(2\ne0\) in \(k\), and consider
\[
\mathcal C:\quad y^2z=x(x-z)(x-tz)\subset\mathbb P^2_R.
\tag{6.1}
\]
The generic fibre is a smooth plane cubic, since its three roots \(0,1,t\) are distinct. The special fibre is the reduced nodal cubic
\[
y^2z=x^2(x-z).
\tag{6.2}
\]
The family is flat: its homogeneous equation is nonzero after reduction modulo \(t\). If \(tG=FH\), reduction in the residue polynomial domain gives \(\bar H=0\); canceling \(t\) proves the homogeneous quotient torsion-free, and its projective affine charts are torsion-free over the DVR as well. It is proper, and the two fibres are geometrically connected.

The flat proper surjectivity theorem gives
\[
\pi_1(\mathcal C_{\bar\eta})\twoheadrightarrow
\pi_1(\mathcal C_{\bar s})=\widehat{\mathbb Z}.
\tag{6.3}
\]
The special-fibre calculation is the normalization-and-two-branches proof in the fundamental-group lesson, Section 5.4: covers of its projective-line normalization are trivial, and gluing the two branches gives one permutation, hence a finite set with a \(\mathbb Z\)-action. This is also worked out in the specialization lesson, Section 7.2.

In characteristic zero, comparison makes the generic group \(\widehat{\mathbb Z}^2\). The surjection (6.3) is not injective: these groups have respectively four and two maps to \(\mathbb Z/2\). The family fails smoothness at the node, exactly where Theorem 4.1's hypothesis fails. This particular equation requires characteristic different from two for its two distinct tangent branches.

### 6.2. The abelian \(p\)-part of an elliptic curve

For an elliptic curve \(E/k\) over an algebraically closed field of characteristic \(p\), its maximal abelian pro-\(p\) quotient is
\[
\pi_1(E)^{\mathrm{ab},p}=
\begin{cases}
\mathbb Z_p,&E\text{ ordinary},\\
0,&E\text{ supersingular}.
\end{cases}
\tag{6.4}
\]
We give the cohomological proof, including the link to the usual \(p\)-rank distinction.

**Quasi-coherent comparison.** For any scheme \(S\), any quasi-coherent module \(\mathcal F\), and every \(q\ge0\), there are canonical natural isomorphisms
\[
H^q(S_{\mathrm{Zar}},\mathcal F)
 \simeq H^q(S_{\mathrm{\acute et}},\mathcal F_{\mathrm{\acute et}})
 \simeq H^q((\mathrm{Sch}/S)_\tau,\mathcal F^a),
\tag{6.4a}
\]
where \(\tau\) may be Zariski, étale, smooth, syntomic or fppf, and
\(\mathcal F^a(T\xrightarrow{u}S)=\Gamma(T,u^*\mathcal F)\).
No separation or quasi-compactness assumption on \(S\) is required.

These are Topologies on schemes, Theorems 5.1 and 7.1, with complete proofs. Lemma 4.1 there contracts the augmented Amitsur complex after faithfully flat base change; faithful flatness then proves its exactness before base change for every module. Its Proposition 4.2 identifies this with each standard affine covering complex. The vanishing criterion in Cohomology on sites, Theorem 4.1, gives positive-degree vanishing on every affine object. Restriction to the Zariski site has zero higher direct images, since these vanish on affine opens; Leray gives the comparison on arbitrary schemes. Theorem 7.1 proves the big/small étale comparison by exact restriction and acyclic resolutions. These comparisons are constructed on abelian sheaves and commute with their additive maps. In particular they commute with Frobenius on the structure sheaf in characteristic \(p\). This is the programme proof of [Stacks, Tag 03P2](https://stacks.math.columbia.edu/tag/03P2).

The Artin–Schreier sequence on the étale site is
\[
0\to\mathbb F_p\to\mathcal O_E
\xrightarrow{F-1}\mathcal O_E\to0.
\tag{6.5}
\]
It is exact: the roots of \(z^p-z=0\) are the constants \(\mathbb F_p\); any equation \(z^p-z=a\) has solutions after the finite étale extension defined by that polynomial, whose derivative is \(-1\). On \(H^0(\mathcal O_E)=k\), \(F-1\) is onto. On the one-dimensional \(H^1(\mathcal O_E)\), Frobenius is either zero or has form \(v\mapsto c v^p\) with \(c\ne0\). In the latter case \(cv^p-v\) is onto with a kernel of \(p\) elements; in the former case \(F-1=-1\) is bijective. Since \(H^2(\mathcal O_E)=0\), (6.5) gives
\[
H^1_{\mathrm{\acute et}}(E,\mathbb F_p)=
\begin{cases}\mathbb F_p,&F\ne0,\\0,&F=0,\end{cases}
\qquad H^2_{\mathrm{\acute et}}(E,\mathbb F_p)=0.
\tag{6.6}
\]

To identify the cases, use the genus-one identification
\(E\simeq\operatorname{Pic}^0(E)\), proved in The Picard functor and the Picard scheme of a curve, Section 8. The relative Frobenius \(F_E:E\to E^{(p)}\) has degree \(p\) and is radicial. Pullback on degree-zero Picard groups gives \(V:E^{(p)}\to E\). On a divisor \(P-O\), pullback of its Frobenius image has multiplicity \(p\); consequently
\[
V F_E=[p].
\tag{6.7}
\]
The degree formula for multiplication on an elliptic curve is \(p^2\), proved in Abelian varieties, Theorem 6.1. Hence \(V\) has degree \(p\). Its tangent map is Frobenius pullback on \(H^1(\mathcal O)\), by the transition-function description of the tangent of the Picard functor. If this map is nonzero, translation makes \(V\) étale everywhere and its kernel has \(p\) geometric points. Since \(F_E\) is bijective on geometric points, \(E[p]\) has \(p\) points: the ordinary case. If the tangent map is zero, a degree-\(p\) map of smooth curves is purely inseparable, so both factors of (6.7) are radicial and \(E[p]\) has only the identity: the supersingular case. This proves the usual equivalence with \(p\)-rank one or zero.

Put \(d=1\) or \(0\) in these two cases. The constant-sheaf sequences
\[
0\to\mathbb Z/p\to\mathbb Z/p^{n+1}
\to\mathbb Z/p^n\to0
\]
and \(H^2(E,\mathbb Z/p)=0\) show that reduction on \(H^1\) is onto, with kernel of order \(p^d\). The \(H^0\) reduction is onto since \(E\) is connected. Thus \(H^1(E,\mathbb Z/p^n)\) has order \(p^{nd}\). Its subgroup killed by \(p\) is \(H^1(E,\mathbb Z/p)\), because these groups are the continuous characters \(\operatorname{Hom}(\pi_1(E),\mathbb Z/p^n)\). The elementary-divisor theorem therefore gives \((\mathbb Z/p^n)^d\).

If \(d=1\), choose compatible generators under the surjective reductions. They define a character to \(\mathbb Z_p\) onto every finite quotient, hence onto \(\mathbb Z_p\). Every finite abelian \(p\)-quotient is detected by such characters; since the character groups above are cyclic and generated by these reductions, this character is the maximal abelian pro-\(p\) quotient. If \(d=0\), a nontrivial finite abelian \(p\)-quotient would have a quotient \(\mathbb Z/p\), contradicting (6.6). This proves (6.4).

### 6.3. A smooth family where the \(2\)-part disappears

Over an algebraically closed field \(k\) of characteristic two, set \(R=k[[t]]\) and
\[
\mathcal E:\quad
Y^2Z+tXYZ+YZ^2+X^3=0
\quad\subset\mathbb P^2_R.
\tag{6.8}
\]
Its special fibre \(y^2+y=x^3\) is smooth: the homogeneous partials are \(X^2,Z^2,Y^2\), with no common projective zero. The same torsion-free homogeneous-quotient argument as for (6.1) gives flatness. Smoothness holds along the special fibre, and properness forces the closed nonsmooth locus to be empty. Thus this is a smooth proper elliptic family, with the section \(O=[0:1:0]\).

Its generic fibre is ordinary. Inversion on its Weierstrass equation is
\[
(x,y)\longmapsto(x,y+tx+1).
\]
Over the algebraic closure of the fraction field, a fixed affine point has \(x=t^{-1}\) and \(y^2=t^{-3}\), hence exactly one solution. Together with \(O\) this gives two geometric points of order dividing two. On the special fibre inversion is \((x,y)\mapsto(x,y+1)\), with no fixed affine point. It is supersingular. These are the \(p\)-rank definitions just justified.

One can check the Frobenius calculation directly. For a plane cubic \(G=0\), the sequence
\(0\to\mathcal O_{\mathbb P^2}(-3)\xrightarrow{G}\mathcal O_{\mathbb P^2}\to\mathcal O_E\to0\)
identifies \(H^1(\mathcal O_E)\) with the one-dimensional Čech group generated by \(1/(XYZ)\). In characteristic two Frobenius sends that class to \(G/(X^2Y^2Z^2)\): lift a cocycle, square its coboundary and divide by \(G\) in the connecting map. In this Čech quotient only the \(XYZ\) monomial of \(G\) survives. Thus the scalar in (6.8) is \(t\), nonzero generically and zero specially.

Theorem 4.2 gives a surjective specialization and a prime-to-two isomorphism. But (6.4) changes its maximal abelian pro-two quotient from \(\mathbb Z_2\) to zero. Therefore the full specialization map is not injective. Both fibres are smooth; this example isolates the positive-characteristic qualification, independently of the nodal failure of smoothness.

## 7. Exercises and solutions

**Exercise 7.1 (specialization data; intermediate).** Prove compatibility with base change and composition, and explain the reduction to a strictly henselian DVR.

**Solution.** For a morphism of families, use the ring map between their selected strict henselizations and take the more general geometric lift to the lower ring by composition. The restriction squares for a cover commute on the closed and more general fibres. Proper henselian equivalence identifies the extensions, giving the square of specialization functors and group maps. For successive specializations, lift \(A\) through the strict henselization \(A'\) at the intermediate point and use the composite generic lift. Restriction along the composite is successive restriction, so the group maps compose. These assertions use compatible lifts; changing fibre identifications conjugates them.

For a Noetherian base and a nontrivial specialization, the chosen strict-local domain image in the more general geometric field admits a dominating DVR. Strict henselization of that DVR is again a DVR; choose its residue geometric field compatibly and embed its algebraic generic field in the chosen geometric field. Proper field invariance identifies the original and DVR fibre categories, and the compatible squares identify the maps. The specialization lesson, Proposition 2.1, proves this construction, including equal-point specializations by a power-series DVR. For a smooth proper family over a general base, first descend finite-presentation data to a Noetherian model, shrink its connected-fibre locus, and use the same field invariance and compatibility. This gives the reduction in Section 1 at its stated generality.

**Exercise 7.2 (good reduction; intermediate).** Let \(C/R\) be a smooth proper curve over a DVR with geometrically connected fibres and residue characteristic \(p\). Show that its geometric prime-to-\(p\) fundamental groups are isomorphic.

**Solution.** Choose a geometric specialization over the generic-to-closed specialization of \(\operatorname{Spec}R\). Theorem 4.2 applies to this exact family and gives (4.3). Alternatively, strict henselization identifies the two geometric fibre categories by proper field invariance. A prime-to-\(p\) Galois generic cover descends to a finite separable field extension; normalize the smooth family in it, kill its tame vertical indices by a root-uniformizer extension, and apply branch purity. Purely inseparable residue invariance and proper henselian equivalence descend this extension to the family. Every prime-to-\(p\) quotient therefore factors through specialization; together with surjectivity this is exactly the group isomorphism. It is not only an assertion about first cohomology.

**Exercise 7.3 (standard tameness; intermediate).** Under the hypotheses of Lemma 2.1, show that \(A[z]/(z^e-a)\) is étale on \(D(a)\) and tame along its boundary.

**Solution.** The monic polynomial gives finite freeness with the \(e\) powers of \(z\) as basis. On \(D(a)\), \(z\) is invertible and \(ez^{e-1}\) is a unit; the Jacobian criterion gives étaleness. For a minimal boundary prime, the localized quotient by \(a\) is a reduced zero-dimensional local ring, hence a field. Its maximal ideal is generated by the nonzerodivisor \(a\), so the local ring is a DVR. The root algebra over it is a DVR with uniformizer \(z\), unchanged residue field and index \(e\). Since \(e\) is prime to the residue characteristic, this is tame. When \(e>1\), the boundary differential relation \(ez^{e-1}dz=0\) shows why the cover is not étale on the boundary itself.

**Exercise 7.4 (the surface presentation; advanced).** Assuming complex comparison, deduce (5.2) for every algebraically closed field of characteristic zero.

**Solution.** Choose a finitely generated field of definition \(K/\mathbb Q\) for the projective curve, and its algebraic closure \(k_0\) inside the ground field. Embed \(K\) into \(\mathbb C\) using a finite transcendence basis and extend to \(k_0\). Proper algebraically closed field invariance identifies cover categories over \(k\), \(k_0\) and \(\mathbb C\), with compatible chosen geometric fibre functors. Flat Čech base change preserves \(H^1(\mathcal O)\), so all models have genus \(g\).

The classical complex curve is a compact orientable surface of genus \(g\), as explained in the comparison lesson, Section 6.2. Its polygon has one vertex, \(2g\) edge generators and one face attached by \(\prod_i[a_i,b_i]\). Van Kampen gives (5.1). Finite topological covers are finite sets with an action of this discrete group; every such action factors through a finite quotient. Complex comparison therefore identifies the algebraic group with its profinite completion. Transport through the proper field equivalences gives (5.2). The relation in the profinite presentation is the closed normal subgroup generated by this word; taking an unclosed normal subgroup would not specify a profinite quotient.

## Proof providers and references

The specialization and proper-schemes lessons supply the exact DVR reduction, arithmetic Abhyankar theorem, universal-homeomorphism invariance, proper henselian equivalence, proper algebraically closed field invariance and homotopy sequence used here. The deformation course supplies the proved mixed-characteristic small-extension obstruction theorem; Lemma 5.2 applies it and verifies the algebraized family's properties. The Picard-curve lesson supplies the genus-one identification with its Picard scheme, and the abelian-varieties lesson supplies the degree of multiplication and the \(p\)-rank terminology.

Theorem 3.3 gives the normalized reduced-fibre theorem and its finite-separable variant. Lemmas K.1–K.3 give normalized DVR base change and tame ramification removal; E.1–E.3 give finite-order transfer and separable replacement; W.1–W.6 give the complete-coefficient elimination; D.1–D.3 give approximation and descent. Lemmas G.1–G.2 supply the generic-field preparation. Formal closed-embedding algebraization in Lemma 5.2 uses the earlier Algebraization of formal schemes, Theorem 1.1, with projective existence, as explained in its proof. Étale quasi-coherent cohomology is the actual Topologies on schemes, Theorems 5.1 and 7.1, applied through the abelian-sheaf comparison (6.4a). The finite-cover comparison is Comparison with the classical topology, Proposition 2.1 and Theorem 3.1, with projective GAGA at the exact scope used here. Lemmas 5.A–5.B prove the polygon and genus calculations, using the earlier manifold sheaf/singular comparison, attaching-cell calculation, projective Serre duality and cohomological GAGA. The projectivity and ample-power arguments in Lemma 5.2 use the earlier Serre theorem lesson with its denominator and immersion proofs.

- [Stacks] The Stacks Project authors, *The Stacks Project*, [official project](https://stacks.math.columbia.edu/). The tag links refer to the AI Integrated Stacks Project edition. Its [English reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/) retains upstream tags. Relevant sections are Fundamental Groups of Schemes, specialization and tame ramification; More on Algebra, Abhyankar's lemma; More on Morphisms, the reduced-fibre theorem; and Cohomology of Schemes, formal algebraization.
- [Grothendieck–Raynaud] A. Grothendieck and M. Raynaud, *Revêtements étales et groupe fondamental (SGA 1)*, [revised edition, arXiv:math/0206203](https://arxiv.org/abs/math/0206203), Exposé X, Sections 2–3, and Exposé XIII, Section 5, for specialization and Abhyankar's lemma.

- [Gallier] Jean Gallier, *The Classification Theorem for Compact Surfaces and a Detour on Fractals*, [arXiv:0805.0562v1](https://arxiv.org/abs/0805.0562v1), Section 5.2, for the oriented polygon construction.

- [Kuhlmann] Franz-Viktor Kuhlmann, *A correction to Epp's paper “Elimination of wild ramification”*, [arXiv:1003.5687v1](https://arxiv.org/abs/1003.5687v1), for the coefficient-collision issue in the equal-characteristic cyclic step.
