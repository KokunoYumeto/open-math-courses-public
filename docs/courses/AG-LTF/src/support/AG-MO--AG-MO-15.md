# Effective Cartier divisors and invertible sheaves

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI), in Codex at Ultra. Public domain (CC0).*

A hypersurface has one equation locally. To behave as a divisor, that equation must also act injectively: it must not annihilate part of the ambient scheme. Effective Cartier divisors package these two requirements. Their equations can change by units from one neighborhood to another, so the natural global object is an invertible ideal sheaf. Dualizing that ideal gives a line bundle with a distinguished section.

We use ideals defining closed subschemes and invertible modules from the planned lessons *Closed subschemes and scheme-theoretic images*, *Quasi-coherent, coherent and locally free modules*, and *Quasi-coherent sheaves on schemes* of *Sheaves and schemes*. For Noetherian assertions we use [Associated primes and primary decomposition](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/AG-CA-04.html), Theorems 1.2, 2.2 and 3.1, and [Dimension theory of Noetherian local rings](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/AG-CA-11.html), Theorem 3.1. The affineness locality theorem is in Affine, integral and finite morphisms, and section extension for ample sheaves is in Ample invertible sheaves. Schemes need not be reduced, Noetherian or separated unless stated.

## 1. A local equation that does not annihilate

A closed subscheme \(D\subset X\) is an **effective Cartier divisor** if its ideal sheaf \(\mathcal I_D\) is invertible as an \(\mathcal O_X\)-module. This includes the empty divisor, whose ideal is \(\mathcal O_X\).

**Theorem 1.1 (local characterization).** A closed subscheme is an effective Cartier divisor precisely when, on a suitable affine open cover \(U=\operatorname{Spec}A\), its ideal is \((f)\) with \(f\) a nonzerodivisor of \(A\).

**Proof.** Trivialize the invertible ideal on a sufficiently small affine neighborhood. Its generator maps to an element \(f\in A\), and the ideal inclusion is multiplication \(A\xrightarrow{f}A\). This is injective, so \(f\) is a nonzerodivisor. Conversely, multiplication by a nonzerodivisor identifies \(A\) with \((f)\). These identifications show that the ideal sheaf is locally free of rank one. Away from \(D\), it is already the full structure sheaf. \(\square\)

See [Stacks, Tag 01WS](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-characterize-effective-Cartier-divisor). One must permit a sufficiently fine cover. An invertible ideal on an affine scheme need not be globally principal.

Two nonzerodivisor generators of the same ideal differ by a unit. If \(f=ag\) and \(g=bf\), then \((1-ab)f=0\); cancellation gives \(ab=1\). This elementary observation makes local equations compatible.

**Proposition 1.2 (complement).** The open immersion \(j:X\setminus D\to X\) is affine, and the complement is schematically dense: \(\mathcal O_X\to j_*\mathcal O_{X\setminus D}\) is injective. In particular, when \(X\) is affine, so is \(X\setminus D\).

**Proof.** On an affine neighborhood with equation \(f\), the complement is \(D(f)=\operatorname{Spec}A_f\). Affineness of a morphism is local on the target, so these local descriptions prove that \(j\) is affine. Because \(f\) is a nonzerodivisor, \(A\to A_f\) is injective. The sheaf map is therefore injective locally and hence globally. \(\square\)

This is [Stacks, Tag 07ZU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-complement-effective-Cartier-divisor). The argument does not assume a single global equation. A nonzerodivisor may lie in many maximal ideals; schematic density concerns the absence of a function supported only on the divisor.

Define the **sum** \(D+E\) by the product ideal \(\mathcal I_D\mathcal I_E\). Locally its equation is \(fg\). A product of two nonzerodivisors is a nonzerodivisor, so this is again effective Cartier. The multiplication map

\[
\mathcal I_D\otimes\mathcal I_E
\longrightarrow\mathcal I_{D+E}
\tag{1.1}
\]

is an isomorphism: locally it sends the free generator \(f\otimes g\) to the free generator \(fg\). Sums are associative and commutative. They add multiplicities, rather than merely taking set-theoretic unions: on the affine line, \(V(t)+V(t)=V(t^2)\).

For \(h:X'\to X\), the **pullback** \(h^*D\) is defined as an effective Cartier divisor when the inverse-image closed subscheme is effective Cartier. By Theorem 1.1 this happens exactly when the local pulled-back equations remain nonzerodivisors. In that case \(\mathcal I_{h^*D}\cong h^*\mathcal I_D\), because both are locally generated freely by \(h^\sharp(f)\). If the pullbacks of \(D,E\) are defined, their product equation proves

\[
h^*(D+E)=h^*D+h^*E.
\]

Flat maps always allow pullback: tensor the injection given by multiplication by \(f\) with the flat source algebra. A dominant map of integral schemes also allows it, since a nonzero equation remains nonzero in the source domain. An arbitrary map need not. Pulling \(V(t)\subset\mathbb A^1\) back along the zero point gives the entire point, defined by zero, whose ideal is not a rank-one free module. See [Stacks, Tags 02OO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-pullback-effective-Cartier-defined) and [01WW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-pullback-effective-Cartier-divisors-additive).

## 2. The line bundle and its canonical section

Write

\[
\mathcal O_X(-D)=\mathcal I_D,
\qquad
\mathcal O_X(D)=\mathcal I_D^\vee
=\mathcal Hom(\mathcal I_D,\mathcal O_X).
\]

Dualizing the inclusion \(\mathcal I_D\hookrightarrow\mathcal O_X\) gives a canonical section \(1_D\) of \(\mathcal O_X(D)\). If \(f\) is a local equation and \(e\) is the dual frame characterized by \(e(f)=1\), this section is \(fe\). Thus its local coefficient is the equation of the divisor, not a unit. The notation \(1_D\) will later mean the rational function one in a fractional realization of this line bundle.

A section \(s\) of an invertible sheaf \(\mathcal L\) is **regular** when multiplication by it defines an injection \(\mathcal O_X\to\mathcal L\). In a frame \(e\), write \(s=fe\); regularity means exactly that \(f\) is a nonzerodivisor. Its **zero scheme** \(Z(s)\) is defined by the image of

\[
\mathcal L^{-1}\longrightarrow\mathcal O_X,
\qquad \lambda\longmapsto\lambda(s).
\tag{2.1}
\]

Locally this image is \((f)\). A regular section is allowed to vanish at points. Regular means injective multiplication, rather than nowhere-vanishing value.

**Theorem 2.1 (divisor–section correspondence).** Effective Cartier divisors on \(X\) correspond bijectively to isomorphism classes of pairs \((\mathcal L,s)\) consisting of an invertible sheaf and a regular global section. The correspondence is

\[
D\longmapsto(\mathcal O_X(D),1_D),
\qquad(\mathcal L,s)\longmapsto Z(s).
\]

For a regular section, there is a unique isomorphism \(\mathcal O_X(Z(s))\to\mathcal L\) carrying the canonical section to \(s\).

**Proof.** The preceding local calculation makes \(1_D\) regular and gives \(Z(1_D)=D\). Conversely, for regular \(s=fe\), map (2.1) identifies \(\mathcal L^{-1}\) with the ideal \((f)\). The ideal is invertible, hence defines an effective Cartier divisor \(D\). Dualizing that identification gives \(\mathcal O_X(D)\cong\mathcal L\), carrying \(1_D\) to \(s\).

For uniqueness, compare two such isomorphisms in a frame. Their difference multiplies the image of the local regular section by some coefficient \(a\). If they have the same value on the section, then \(af=0\), and \(f\) is a nonzerodivisor; thus \(a=0\). The local uniqueness glues. Finally an isomorphism of pairs preserves the evaluation ideal (2.1), so passage to isomorphism classes is legitimate. \(\square\)

The statement is [Stacks, Tag 01X0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-characterize-OD); the frame argument above supplies its proof. Dualizing (1.1) gives

\[
\mathcal O_X(D+E)\cong\mathcal O_X(D)\otimes\mathcal O_X(E),
\qquad 1_{D+E}\longleftrightarrow1_D\otimes1_E.
\tag{2.2}
\]

The same local frames prove compatibility with every defined pullback. There is also an exact sequence

\[
0\longrightarrow\mathcal O_X
\xrightarrow{1_D}\mathcal O_X(D)
\longrightarrow i_*\bigl(\mathcal O_X(D)|_D\bigr)
\longrightarrow0,
\tag{2.3}
\]

where \(i:D\hookrightarrow X\). Locally it is the sequence \(0\to A\xrightarrow{f}A\to A/(f)\to0\) in the frame \(e\). Its last invertible module on \(D\) is the normal line bundle of this effective Cartier embedding.

## 3. Meromorphic functions and denominators

For an open \(U\), let \(\mathcal S(U)\) consist of regular sections of \(\mathcal O_X\): their germs are nonzerodivisors at every point of \(U\). These sets restrict and multiply. Define \(\mathcal K_X\) as the sheafification of

\[
U\longmapsto\mathcal S(U)^{-1}\mathcal O_X(U).
\tag{3.1}
\]

The natural inclusion \(\mathcal O_X\hookrightarrow\mathcal K_X\) is injective. A meromorphic section of \(\mathcal L\) is a section of \(\mathcal L\otimes\mathcal K_X\); it is regular meromorphic if the induced multiplication \(\mathcal K_X\to\mathcal L\otimes\mathcal K_X\) is injective. These are the conventions of [Stacks, Tags 01X2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-definition-sheaf-meromorphic-functions) and [02OX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-definition-regular-meromorphic-section).

For arbitrary schemes, a germ of \(\mathcal K_X\) need not be every fraction in the total quotient ring of the local ring. A local nonzerodivisor need not extend to a nonzerodivisor on a neighborhood. Definition (3.1) retains that distinction.

For an integral scheme, the distinction disappears: \(\mathcal K_X\) is the constant sheaf of the function field \(K(X)\). On a nonempty affine \(\operatorname{Spec}A\), all nonzero elements of the domain are regular denominators and their localization is \(\operatorname{Frac}(A)\). These fields identify on all nonempty overlaps. A nonzero meromorphic section of an invertible sheaf then gives a basis at the generic point, and is regular meromorphic.

Let \(X\) now be integral and let \(s\) be such a section. Its **ideal of denominators** is

\[
\mathcal I_s(U)=\{a\in\mathcal O_X(U):as\in\mathcal L(U)\}.
\tag{3.2}
\]

It is a quasi-coherent ideal. To check this, trivialize \(\mathcal L\) on \(\operatorname{Spec}A\) and write \(s=a/b\) with \(a,b\ne0\). The ideal is \(I=(b):(a)\). For \(c/f^n\in A_f\) satisfying \((c/f^n)(a/b)\in A_f\), clearing a power of \(f\) gives \(f^mca\in bA\) for some \(m\); thus \(c/f^n\in I_f\). The converse is immediate. This localization identity proves quasi-coherence. Both maps

\[
\mathcal I_s\hookrightarrow\mathcal O_X,
\qquad \mathcal I_s\xrightarrow{s}\mathcal L
\]

are injective. Locally the first image contains \(bA\), and the second contains \(aA\), so their cokernels vanish off the respective proper closed sets. The more general regular-meromorphic statement, with its complete proof, is [Stacks, Tag 02P0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-regular-meromorphic-ideal-denominators). A denominator ideal need not be invertible; clearing poles and having a Cartier divisor are different requirements.

## 4. Cartier divisors and the Picard group

The sheaves \(\mathcal O_X^*\) and \(\mathcal K_X^*\) consist of units. Define the **Cartier divisor group** by

\[
\operatorname{CaDiv}(X)
=\Gamma(X,\mathcal K_X^*/\mathcal O_X^*),
\tag{4.1}
\]

where the quotient is a quotient **sheaf**. Thus a Cartier divisor can be represented on an open cover by invertible meromorphic functions \(f_i\), with \(f_i/f_j\in\mathcal O_X^*\) on overlaps. Local representatives may require refinements; a Cartier divisor need not come from one global meromorphic function. The group operation multiplies representatives and is written additively. A global \(h\in\Gamma(X,\mathcal K_X^*)\) gives the **principal divisor** \(\operatorname{div}(h)\). Quotienting by these defines the Cartier class group \(\operatorname{CaCl}(X)\).

The fractional modules \(f_i^{-1}\mathcal O_{U_i}\subset\mathcal K_X|_{U_i}\) agree on overlaps and define an invertible sheaf \(\mathcal O_X(D)\). Multiplication of fractions gives \(\mathcal O_X(D+E)\cong\mathcal O_X(D)\otimes\mathcal O_X(E)\). For a principal divisor, \(h^{-1}\) is a global frame, so this construction induces a homomorphism

\[
\operatorname{CaCl}(X)\longrightarrow\operatorname{Pic}(X).
\tag{4.2}
\]

An effective Cartier divisor gives (4.1) by its regular local equations, which become units in \(\mathcal K_X\). Its fractional realization agrees with Section 2: the frame dual to \(f_i\) corresponds to \(1/f_i\), and the canonical section corresponds to the rational function one.

**Theorem 4.1.** If \(X\) is integral, (4.2) is an isomorphism. More precisely, Cartier divisors map onto \(\operatorname{Pic}(X)\), and the kernel consists exactly of principal divisors.

**Proof.** Let \(\mathcal L\) be invertible. Choose a nonzero element \(s\in\mathcal L_\eta\), where \(\eta\) is the generic point. Since \(\mathcal K_X\) is the constant function-field sheaf, this determines a global nonzero meromorphic section. In local frames \(e_i\), write \(s=f_i e_i\), with \(f_i\in K(X)^*\). On overlaps the frame changes by a unit, so \(f_i/f_j\) is a unit. These functions define a Cartier divisor \(D\). The local maps \(f_i^{-1}\mathcal O_{U_i}\to\mathcal L|_{U_i}\), sending \(q\) to \(qs\), are isomorphisms and agree on overlaps. Hence \(\mathcal O_X(D)\cong\mathcal L\), proving surjectivity.

Suppose now \(\mathcal O_X(D)\cong\mathcal O_X\). The image of the global frame one is a section \(h\) of the fractional module \(\mathcal O_X(D)\subset\mathcal K_X\). It is a nonzero element of \(K(X)\). On each representative open, equality of frames gives \(h=u_i/f_i\) for a unit \(u_i\). Thus \(f_i=u_i/h\); modulo units the divisor is \(\operatorname{div}(h^{-1})\). Conversely every principal divisor gives a trivial line bundle as observed above. The construction is additive, so passage to the quotient proves the isomorphism. \(\square\)

No Noetherian, normal or separated hypothesis enters this proof. Integralness provides the common field and its nonzero generic frame. On a nonintegral scheme, one must first establish an appropriate meromorphic trivialization; the proof should not be transferred merely by replacing a field symbol by a total quotient ring.

## 5. Associated points and effective representatives

**Theorem 5.1.** On a locally Noetherian scheme, a section of an invertible sheaf is regular if and only if it does not vanish at any associated point. An effective Cartier divisor therefore contains no associated point. At the generic point \(\xi\) of each of its irreducible components,

\[
\dim\mathcal O_{X,\xi}=1.
\]

**Proof.** On an affine trivializing open, regularity of \(s=fe\) is injectivity of multiplication by \(f\). The zero-divisor theorem identifies its failure with membership of \(f\) in an associated prime. Membership is exactly vanishing of the section in the residue field at that associated point. Associated primes localize, so this affine criterion gives the scheme statement.

For the dimension assertion, choose an affine neighborhood where the divisor is \(V(f)\). Its component generic point corresponds to a prime \(\mathfrak p\) minimal over \((f)\). The principal ideal theorem gives \(\dim A_{\mathfrak p}\le1\). This dimension cannot be zero: then the maximal ideal of \(A_{\mathfrak p}\) would be its only prime, hence its nilradical, and \(f\) in it would be nilpotent. In a nonzero ring a nilpotent element cannot act injectively. But a localization of a nonzerodivisor remains a nonzerodivisor. Thus the dimension is one. \(\square\)

See [Stacks, Tags 0AYL](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-regular-section-associated-points) and [0BCN](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-effective-Cartier-codimension-1). In a scheme with embedded associated points, avoiding only component generic points is insufficient. For instance, in \(k[t,\epsilon]/(\epsilon^2,t\epsilon)\), the element \(t\) misses the generic point but kills \(\epsilon\); its zero scheme is not effective Cartier.

**Theorem 5.2 (differences of effective divisors).** If \(X\) is Noetherian and admits an ample invertible sheaf, every invertible \(\mathcal N\) is \(\mathcal O_X(D-E)\) for effective Cartier divisors \(D,E\). They can be chosen to avoid any prescribed finite set of points. If \(X\) is quasi-affine, one may take \(E\) empty.

The exact complete open proof is [Stacks, Tag 0AYM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-quasi-projective-Noetherian-pic-effective-Cartier). Its construction fits our earlier results as follows. The associated set is finite, so adjoin it to the prescribed finite set. For an ample \(\mathcal A\), choose a section \(a\) of some positive power with an affine nonvanishing open containing that set; the full finite-set argument is [Stacks, Tag 09NV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/properties.html#properties-lemma-ample-finite-set-in-principal-affine). On this affine open choose a section of \(\mathcal N\) nonvanishing at the set. The precise quasi-affine selection lemma, including its proof by finite-point induction, is [Stacks, Tag 0F20](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/properties.html#properties-lemma-quasi-affine-invertible-nonvanishing-section). It also proves the quasi-affine case directly.

In the general case, the section-extension lemma of the ample lesson extends that chosen section after multiplying by \(a^r\), with \(r>0\) chosen sufficiently large. The resulting global section of \(\mathcal N\otimes\mathcal A^{mr}\) and the section \(a^r\) of \(\mathcal A^{mr}\) avoid every associated point, so are regular by Theorem 5.1. Their zero schemes are \(D,E\); Theorem 2.1 gives \(\mathcal N\cong\mathcal O_X(D-E)\). This proof does not assume an infinite residue field when selecting a section.

## 6. Examples and exercises

A hyperplane \(H=V(X_0)\subset\mathbb P^n_k\), for \(n\ge1\), is effective Cartier. On each affine chart, its equation is either a coordinate or a unit; these are nonzerodivisors. The homogeneous section \(X_0\) of \(\mathcal O(1)\) is regular and has zero scheme \(H\), hence \(\mathcal O(H)\cong\mathcal O(1)\). Every closed point on a regular integral finite-type curve is effective Cartier: at that point its maximal ideal is generated by a DVR uniformizer, and away from it the ideal is the full structure sheaf. The residue field need not equal the ground field.

**Exercise 6.1 (easy).** Show that \(V(f)\subset\mathbb A^n_k\) is effective Cartier for every nonzero polynomial \(f\). What happens if \(f\) is a nonzero constant?

**Solution.** The polynomial ring is a domain, so multiplication by \(f\) is injective and its principal ideal is free of rank one. Apply Theorem 1.1. A nonzero constant is a unit and defines the empty effective divisor. The zero polynomial instead defines the entire nonempty affine scheme and is not a regular equation.

**Exercise 6.2 (easy).** Establish (2.2) with its canonical sections, and compute \(\mathcal O(H_1+H_2)\) for two hyperplanes of \(\mathbb P^n_k\).

**Solution.** With local equations \(f,g\), use the dual frames \(1/f,1/g\). Multiplication identifies their tensor product with the frame \(1/(fg)\). The sections \(f(1/f)\) and \(g(1/g)\) multiply to \(fg(1/(fg))\), the canonical section of the sum. These identifications agree with changes of generators by units and glue. Since each hyperplane has line bundle \(\mathcal O(1)\), the sum has \(\mathcal O(2)\), even if the two hyperplanes coincide; then the zero scheme records multiplicity two.

**Exercise 6.3 (medium).** In the cone \(X=\operatorname{Spec}k[x,y,z]/(xy-z^2)\), show that the ruling \(L=V(x,z)\) is not effective Cartier at the vertex.

**Solution.** Let \(A\) be this graded ring, \(\mathfrak m=(x,y,z)\), and \(I=(x,z)\). The degree-one part of \(A\) has basis \(x,y,z\), because the relation is homogeneous of degree two. The ideal \(\mathfrak m I\) has no degree-one part, so the classes of \(x,z\) are linearly independent in \(I/\mathfrak m I\), and they generate it. Localization gives \(I_{\mathfrak m}/\mathfrak m I_{\mathfrak m}\cong k^2\). A principal module over the local ring would have a quotient generated by one vector; an invertible ideal would have a one-dimensional quotient. Thus this ideal is not invertible. This argument works in characteristic two as well.

**Exercise 6.4 (medium).** Explain how changing the chosen generic section of a line bundle affects the Cartier divisor in Theorem 4.1, and prove that its Cartier class is independent of this choice.

**Solution.** Two nonzero generic sections differ by a unique \(h\in K(X)^*\), since the generic fibre is one-dimensional. If \(s=f_i e_i\), then \(hs=(hf_i)e_i\). The resulting divisors differ by \(\operatorname{div}(h)\). Their classes are therefore equal, and their fractional line bundles are identified by multiplication by \(h^{-1}\). Conversely, if a Cartier divisor gives a trivial line bundle, its global frame in the fractional realization is a nonzero rational function, and the local equations differ from its inverse by units. Hence the divisor is principal. Together with the generic-section construction, this proves \(\operatorname{CaCl}(X)\cong\operatorname{Pic}(X)\).

**Exercise 6.5 (medium).** Prove that the complement of an effective Cartier divisor on an affine scheme is affine, without assuming its ideal is principal on the entire scheme.

**Solution.** Take an affine cover trivializing the ideal. Over every member its complement is a principal open, and its map to that member is affine. Target locality for affine morphisms makes the full complement immersion affine. An affine morphism to an affine scheme has affine source, by relative Spec or the characterization proved in the affine-morphism lesson. This establishes the result for arbitrary invertible ideals. Replacing the cover by the assertion that every invertible ideal of the original affine coordinate ring is principal would introduce a false premise.

## References and proof dependencies

The central characterizations, pullback rule, divisor–section correspondence, Cartier-class comparison and associated-point assertions are proved above. The supplemental effective-difference theorem uses the exact complete open proofs linked in Section 5 and the preceding ample-sheaf lesson. The Stacks project authors, *The Stacks project*, are consulted in the AI Integrated Stacks Project edition at commit `565b10e987aba5969b21145a0833f42d69f96790`; the linked expression retains GNU FDL 1.2 and is not reproduced here.

Ravi Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, draft of 27 July 2024, §§9.5, 15.4 and 15.6, provides the alternative geometric viewpoint through equations, rational sections and line bundles. The next lesson uses effective Cartier divisors to formulate the universal property of blowing up; the final lesson compares Cartier classes with codimension-one cycles on a normal scheme.
