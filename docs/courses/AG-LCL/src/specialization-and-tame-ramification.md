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

The arithmetic input is the full Abhyankar theorem proved in the specialization lesson, Theorem 5.1 [Stacks, [Tag 0BRM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-abhyankar)]. If \(C\subset D\) is a local extension of DVRs with separable residue extension and tame index \(e\), and a finite extension of \(\operatorname{Frac}C\) has index divisible by \(e\) at a selected prime, every matching local DVR in the **normalized** base change has index one and separable residue extension. This also applies to residue extensions of positive transcendence degree. For finite field factors, the conclusion is unramifiedness.

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

The general **reduced-fibre theorem** provides another route to the vertical step. Its precise normalized form is: for a Nagata Dedekind ring \(A\), a flat finite-type \(T/A\) admits a finite extension of its fraction field such that its normalized base change is smooth at the generic points of every fibre [Stacks, [Tag 09IL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-theorem-normalized-base-change-with-reduced-fibre)]. If the generic component fields are separable over the base fraction field, the extension can be chosen separable [Stacks, [Tag 0BRR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-normalized-base-change-with-reduced-fibre-separable)]. The complete DVR reduction in Section 1 supplies the Nagata hypothesis. The ramification-elimination statements are part of the reduced-fibre theorem.

The conclusion is initially smoothness at generic fibre points. Normality of the total normalized scheme gives \((S_2)\); quotienting by a base uniformizer gives \((S_1)\) for each closed fibre, hence no embedded components. Generic smoothness then makes those fibres reduced. This explains the theorem's name. Lemma 3.1 uses the more explicit tame index-removal argument, which also identifies why only prime-to-\(p\) Galois covers are required in positive characteristic.

**Lemma 3.2 (descent through the special fibre).** Every cover produced in Lemma 3.1 is the geometric generic pullback of a finite étale cover of \(X\).

**Proof.** Write \(k=R/\mathfrak m_R\) and \(k'=R'/\mathfrak m_{R'}\). The extension \(k'/k\) is finite algebraic. Since \(k\) is separably closed, it is purely inseparable; in characteristic zero it is trivial. Thus \(X_{k'}\to X_k\) is a universal homeomorphism, and identifies their finite étale categories.

Restrict \(Z'\) to \(X_{k'}\) and descend that cover through this equivalence to \(X_k\). Proper henselian equivalence then gives a finite étale \(Y\to X\). Its pullback to \(X_{R'}\) and \(Z'\) have the same closed-fibre cover. Full faithfulness of the same proper henselian equivalence over \(R'\) gives an isomorphism between them. On the geometric generic fibre this identifies \(Y_{\bar K}\) with the original cover.

In the Galois case, transport the specified action through the closed-fibre equivalences and lift it by full faithfulness. The group identities and the torsor isomorphism are preserved by these equivalences, so \(Y\) is a \(G\)-cover. Its connectedness follows from the connected geometric generic cover: a clopen decomposition of \(Y\) would induce one there, while every nonempty component of a finite étale cover of the integral \(X\) meets the generic fibre. ∎

Both uses of the proper henselian theorem matter. The first constructs \(Y\); the second proves that its pullback is the particular normalized extension (3.1). Purely inseparable invariance handles the residue extension without assuming a perfect residue field.

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

The reduced-fibre theorem and its separable variant have the exact linked Stacks proofs at Tags 09IL and 0BRR. Formal closed-embedding algebraization in Lemma 5.2 uses the earlier Algebraization of formal schemes, Theorem 1.1, with projective existence, as explained in its proof. Étale quasi-coherent cohomology is the actual Topologies on schemes, Theorems 5.1 and 7.1, applied through the abelian-sheaf comparison (6.4a). The finite-cover comparison is Comparison with the classical topology, Proposition 2.1 and Theorem 3.1, with projective GAGA at the exact scope used here. Lemmas 5.A–5.B prove the polygon and genus calculations, using the earlier manifold sheaf/singular comparison, attaching-cell calculation, projective Serre duality and cohomological GAGA. The projectivity and ample-power arguments in Lemma 5.2 use the earlier Serre theorem lesson with its denominator and immersion proofs.

- [Stacks] The Stacks Project authors, *The Stacks Project*, [official project](https://stacks.math.columbia.edu/). The tag links refer to the AI Integrated Stacks Project edition. Its [English reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/) retains upstream tags. Relevant sections are Fundamental Groups of Schemes, specialization and tame ramification; More on Algebra, Abhyankar's lemma; More on Morphisms, the reduced-fibre theorem; and Cohomology of Schemes, formal algebraization.
- [Grothendieck–Raynaud] A. Grothendieck and M. Raynaud, *Revêtements étales et groupe fondamental (SGA 1)*, [revised edition, arXiv:math/0206203](https://arxiv.org/abs/math/0206203), Exposé X, Sections 2–3, and Exposé XIII, Section 5, for specialization and Abhyankar's lemma.

- [Gallier] Jean Gallier, *The Classification Theorem for Compact Surfaces and a Detour on Fractals*, [arXiv:0805.0562v1](https://arxiv.org/abs/0805.0562v1), Section 5.2, for the oriented polygon construction.
