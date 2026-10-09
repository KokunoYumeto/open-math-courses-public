# Fourier duality through a test complex on the base

Course: SH-02. Unit: SH02-FDN. Language: English.

The duality results below have proofs relative to the stated sheaf-operation imports. The final section distinguishes the literal and adjunction-normalized Fourier comparisons and uses their separately proved relation. The course supplies an explicit realization of the paired inverse equations without attributing an unrecorded geometric recipe to the antecedent.

Compare the ordinary Fourier-duality statement in Kashiwara and Schapira, [*Microlocal Study of Sheaves*, Astérisque 128 (1985), Theorem 2.1.3(iii), p. 40](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf#page=43), and the adjunction proofs in Schapira's [*An Introduction to Sheaves on Grothendieck Topologies*, 1 August 2026, §4.6](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=94). The proof below uses one variable test complex on the base to account for both dualities. Coefficient duals remain internal derived Hom objects; no biduality assumption occurs. The final source account distinguishes the source statements from the additional maps and boundedness arguments supplied here.

## SH02-FDN-SETUP. Coordinates, domains, and three different transforms

Let \(k\) be a commutative ring with identity and finite global dimension. Let \(B\) be a locally compact Hausdorff space and let \(\tau:E\to B\) be a real vector bundle of fixed finite rank \(n\). Denote its dual by \(\pi:E^*\to B\). Write

\[
X=E\times_B E^*,\qquad p:X\to E,\qquad q:X\to E^*,
\qquad \rho=\tau p=\pi q,
\]

and put \(N=\{(x,\xi):\langle x,\xi\rangle\leq0\}\). For a closed subset \(A\), the operations \(L_A=L\otimes_k^L k_A\) and \(R\Gamma_A L=R\mathcal Hom(k_A,L)\) remain distinct.

Let \(O\) be the orientation local system of \(E\), regarded as a sheaf on \(B\). The positive dual-orientation identification identifies it with the orientation local system of \(E^*\): a positively oriented basis determines the positive dual basis. The canonical pairing on the sign local system gives \(O\otimes_k O\simeq k_B\). Set \(W=O[n]\), so \(W^{-1}=O[-n]\), where the inverse refers to tensor product.

We use these functors:

\[
\begin{aligned}
T_EF&=Rq_!((p^{-1}F)_N), &&F\in D^+_{\mathbb R_{>0}}(E;k),\\
S_EG&=Rp_*R\Gamma_N(q^!G), &&G\in D^+_{\mathbb R_{>0}}(E^*;k),\\
I_EH&=Rq_*R\Gamma_N(p^!H), &&H\in D^+_{\mathbb R_{>0}}(E;k).
\end{aligned} \tag{FDN1}
\]

The first two are the transform and its inverse from [the Fourier kernel unit](../../SH02-fourier-sato.html). The third is the inverse transform with the roles of \(E\) and \(E^*\) exchanged; thus \(I_E=S_{E^*}\) after permuting the coordinates of the product. Both \(T_E\) and \(I_E\) go from \(E\) to \(E^*\). In particular, \(I_E\) in the duality theorem below is not \(S_E\), whose domain is different.

The boundedness symbols are global. We take \(F\in D^b_{\mathbb R_{>0}}(E;k)\) in every duality assertion. Its cohomology may have arbitrary stalk modules, angular variation, and base variation. There is no field, Noetherian, constructibility, finite-generation, or compactness assumption. A dual of such an \(F\) is asserted to belong to \(D^+\), not automatically to \(D^b\).

The sheaf-operation imports used here are the proper-support projection formula, \(Rf_!\dashv f^!\), \(f^{-1}\dashv Rf_*\), composition of extraordinary inverse images with its adjunction coherence, tensor–Hom adjunction, and the vector-bundle formula

\[
\tau^!H\simeq \tau^{-1}H\otimes_k\tau^{-1}O[n],
\qquad
\pi^!H\simeq \pi^{-1}H\otimes_k\pi^{-1}O[n]. \tag{FDN2}
\]

Finite cohomological dimension of the proper direct images of these finite-rank bundle projections supplies their extraordinary inverse images. This is a condition on abelian sheaves in the underlying foundation, not a replacement by a bound for one chosen coefficient object. The projection formula is the one for proper support and has no perfectness requirement on a bounded tensor factor. The [kernel unit](../../SH02-kernel-calculus.html) states these imports and their adjunction maps. Conicity of internal Hom with bounded first input and bounded-below second input is provided by [conic descent](../../SH02-conic-descent.html).

### SH02-FDN-PROJECTION-RANGE — Why bounded-below tests are allowed

The projection formula used in FDN5 and FDN6 has one bounded factor and one bounded-below factor. Its extension from the bounded formula can be checked degree by degree, without interchanging a direct image with an infinite limit. Let \(g\) be the finite global dimension of \(k\), let the bounded factor have lower bound \(a\), and let \(C\) be the bounded-below factor. Compare \(C\) with \(\tau_{\leq N}C\) by their truncation triangle. The tail is in \(D^{\geq N+1}\). In either side of the projection formula its contribution lies in \(D^{\geq N+1+a-g}\): ordinary inverse image is exact, derived tensor has this lower bound, and a right-derived proper image preserves lower bounds. The same estimate applies when the bounded factor is on the domain, because its proper image still has lower bound \(a\).

Fix a degree \(j\) and choose \(N\) so that \(N+a-g>j\). The truncation comparisons then induce isomorphisms in degree \(j\) on both sides. The natural projection-formula map for the truncated bounded factors is an isomorphism by the bounded formula, so naturality gives the same conclusion for the original map in degree \(j\). Since \(j\) was arbitrary, its cone has zero cohomology and the original map is an isomorphism. Finite cohomological dimension also keeps the proper image of a bounded factor bounded, as required in FDN4. Thus the tests in FDN5–FDN6 range over all of \(D^+\), and their Yoneda arguments do not silently replace that category by bounded objects.

## SH02-FDN-HOM. Two adjunction calculations with their maps

We give the calculations because replacing an internal Hom by a tensor with a coefficient dual would impose a false finiteness condition here.

**Lemma.** Suppose \(f:Y\to Z\) is a continuous map of locally compact Hausdorff spaces and \(f_!\) has finite cohomological dimension. Let \(A\in D^b(Z;k)\), \(L\in D^b(Y;k)\), and \(Q\in D^+(Z;k)\). There are natural isomorphisms

\[
f^!R\mathcal Hom(A,Q)
 \xrightarrow{\sim} R\mathcal Hom(f^{-1}A,f^!Q), \tag{FDN3}
\]

\[
Rf_*R\mathcal Hom(L,f^!Q)
 \xrightarrow{\sim}R\mathcal Hom(Rf_!L,Q). \tag{FDN4}
\]

**Proof of FDN3.** For an arbitrary \(C\in D^+(Y;k)\), the following natural bijections use, in order, the exceptional adjunction, tensor–Hom adjunction, the proper-support projection formula, and the two adjunctions in reverse order:

\[
\begin{aligned}
\operatorname{Hom}(C,f^!R\mathcal Hom(A,Q))
&\simeq\operatorname{Hom}(Rf_!C,R\mathcal Hom(A,Q))\\
&\simeq\operatorname{Hom}(Rf_!C\otimes_k^L A,Q)\\
&\simeq\operatorname{Hom}(Rf_!(C\otimes_k^L f^{-1}A),Q)\\
&\simeq\operatorname{Hom}(C\otimes_k^L f^{-1}A,f^!Q)\\
&\simeq\operatorname{Hom}(C,R\mathcal Hom(f^{-1}A,f^!Q)).
\end{aligned} \tag{FDN5}
\]

All these objects lie in \(D^+\): the bounded tensor factor and finite global dimension give a lower tensor bound, a bounded first input gives a lower internal-Hom bound, and \(f^!\) has a uniform lower amplitude bound. Yoneda on \(D^+(Y;k)\) therefore gives FDN3, including its direction.

Its actual morphism is adjoint to an evaluation map. Write \(J=R\mathcal Hom(A,Q)\). The counit \(Rf_!f^!J\to J\), tensor–Hom evaluation \(J\otimes_k^L A\to Q\), and projection formula give

\[
Rf_!(f^!J\otimes_k^L f^{-1}A)
 \simeq Rf_!f^!J\otimes_k^L A
 \longrightarrow J\otimes_k^L A
 \longrightarrow Q.
\]

Transpose this across \(Rf_!\dashv f^!\) and then tensor–Hom. Its effect on \(\operatorname{Hom}(C,-)\) is precisely FDN5. Thus the isomorphism is specified by the imported counit and evaluation; it is not an arbitrary choice of an isomorphism between the two objects.

**Proof of FDN4.** For an arbitrary \(C\in D^+(Z;k)\), similarly

\[
\begin{aligned}
\operatorname{Hom}(C,Rf_*R\mathcal Hom(L,f^!Q))
&\simeq\operatorname{Hom}(f^{-1}C,R\mathcal Hom(L,f^!Q))\\
&\simeq\operatorname{Hom}(f^{-1}C\otimes_k^L L,f^!Q)\\
&\simeq\operatorname{Hom}(Rf_!(f^{-1}C\otimes_k^L L),Q)\\
&\simeq\operatorname{Hom}(C\otimes_k^L Rf_!L,Q)\\
&\simeq\operatorname{Hom}(C,R\mathcal Hom(Rf_!L,Q)).
\end{aligned} \tag{FDN6}
\]

Here \(Rf_!L\) is bounded because \(L\) is bounded and \(f_!\) has finite cohomological dimension. Hence both representing objects are in \(D^+\), and Yoneda again applies.

For an explicit description put \(J=Rf_*R\mathcal Hom(L,f^!Q)\). The ordinary counit \(f^{-1}J\to R\mathcal Hom(L,f^!Q)\), evaluation, and the exceptional counit give

\[
J\otimes_k^L Rf_!L
 \simeq Rf_!(f^{-1}J\otimes_k^L L)
 \longrightarrow Rf_!f^!Q
 \longrightarrow Q.
\]

Tensor–Hom transposition is FDN4. In both calculations tensor symmetry means the usual Koszul symmetry. The proof never pulls internal Hom through an arbitrary ordinary inverse image. \(\square\)

## SH02-FDN-BASE. Duality relative to a variable test object

For \(H\in D^+(B;k)\), define

\[
\mathbb D_{E,H}F=R\mathcal Hom(F,\tau^!H),\qquad
\mathbb D_{E^*,H}G=R\mathcal Hom(G,\pi^!H).
\tag{FDN7}
\]

**Theorem.** For every \(F\in D^b_{\mathbb R_{>0}}(E;k)\) and \(H\in D^+(B;k)\), there is a natural isomorphism

\[
\Theta_{F,H}: I_E\mathbb D_{E,H}F
 \xrightarrow{\sim}\mathbb D_{E^*,H}(T_EF).
\tag{FDN8}
\]

It is contravariant in \(F\), covariant in \(H\), and is compatible with restriction to an open part of the base. Both sides are conic objects of \(D^+(E^*;k)\).

**Proof.** The two expressions \(\tau p\) and \(\pi q\) define the same map \(\rho:X\to B\). Composition of extraordinary inverse images gives the specified comparison

\[
p^!\tau^!H\simeq\rho^!H\simeq q^!\pi^!H.
\tag{FDN9}
\]

Use FDN3 for \(p\), this comparison, and tensor–Hom associativity. They give

\[
\begin{aligned}
I_E\mathbb D_{E,H}F
&=Rq_*R\mathcal Hom(k_N,p^!R\mathcal Hom(F,\tau^!H))\\
&\simeq Rq_*R\mathcal Hom(k_N,R\mathcal Hom(p^{-1}F,p^!\tau^!H))\\
&\simeq Rq_*R\mathcal Hom(k_N,R\mathcal Hom(p^{-1}F,q^!\pi^!H))\\
&\simeq Rq_*R\mathcal Hom(k_N\otimes_k^L p^{-1}F,q^!\pi^!H)\\
&\xrightarrow[\mathrm{FDN4}]{\sim}
R\mathcal Hom(Rq_!(k_N\otimes_k^L p^{-1}F),\pi^!H)\\
&=\mathbb D_{E^*,H}(T_EF).
\end{aligned} \tag{FDN10}
\]

The displayed composite defines \(\Theta_{F,H}\). In particular, its final arrow is the evaluation followed by the proper-support trace described in FDN4, and its first arrow is the mate described in FDN3. FDN9 is the unique composition comparison compatible with the composite exceptional adjunction; it does not involve choosing a trivialization of the bundle.

For the bounds, write \(F\in D^{[a,b]}\) and \(H\in D^{\geq c}\). FDN2 gives \(\tau^!H\in D^{\geq c-n}\), so \(\mathbb D_{E,H}F\in D^{\geq c-n-b}\). The sheaf \(k_N\) is flat over \(k\), as is seen at its stalks. Thus \(k_N\otimes_k^L p^{-1}F\) is bounded in \([a,b]\). Proper-support integration over a fiber of dimension \(n\) puts \(T_EF\) in \(D^{[a,b+n]}\). The right side of FDN8 therefore has lower bound \(c-b-2n\). This also agrees with the lower bound obtained by applying \(p^!\), internal Hom with \(k_N\), and the bounded-below ordinary direct image to the left side. No upper bound for the two internal Hom objects has been assumed.

The base-pulled object in FDN2 is conic. Conic internal Hom with bounded first input makes \(\mathbb D_{E,H}F\) conic, and the equivariant-operation theorem makes its transform conic. The same argument applies to \(T_EF\) on the other side. Naturality of all the arrows proves both stated variance assertions. Open restriction commutes with the projection formulas, evaluation, adjunction maps, and composition comparisons used here; consequently the displayed map restricts to the map for the restricted bundle. \(\square\)

This theorem does not need Fourier inversion: it is a comparison of two specified expressions.

## SH02-FDN-DUALITIES. The ordinary and absolute duals

Define the ordinary coefficient dual by

\[
D'_E F=R\mathcal Hom(F,k_E),\qquad
D'_{E^*}G=R\mathcal Hom(G,k_{E^*}).
\tag{FDN11}
\]

These objects exist in \(D^+\) for bounded inputs on the locally compact base specified above; defining them does not require an absolute dualizing complex.

**Corollary.** For every \(F\in D^b_{\mathbb R_{>0}}(E;k)\),

\[
I_E(D'_E F)\xrightarrow{\sim}D'_{E^*}(T_EF).
\tag{FDN12}
\]

**Proof.** Take \(H=W^{-1}=O[-n]\). Formula FDN2 and the evaluation of the invertible orientation complex give

\[
\tau^!W^{-1}\simeq k_E,
\qquad \pi^!W^{-1}\simeq k_{E^*}.
\]

For the second identification we use the positive dual-orientation comparison fixed in the setup. Substitution in FDN8 proves FDN12, with the map specified there. \(\square\)

For absolute duality, assume in addition that \(B\) has finite c-soft dimension. In this assumption, the bound is the usual bound for abelian sheaves. Let \(a_B:B\to\{\mathrm{pt}\}\), and put

\[
\omega_B=a_B^!k,\qquad
\omega_E=a_E^!k,\qquad \omega_{E^*}=a_{E^*}^!k.
\]

The spaces \(E\) and \(E^*\) have finite c-soft dimension as well. To see the required bound, if \(d\) bounds compact-support cohomology on \(B\), the proper-support Leray sequence for a bundle projection has \(q\leq n\) by the fiber formula and \(p\leq d\) on the base. Thus compact-support cohomology on the total space vanishes above \(d+n\), uniformly in the abelian sheaf. The c-soft dimension criterion supplies the asserted finite bound. This argument uses the proper-support projection and requires no compact total space.

Conversely, a finite c-soft-dimension bound on \(E\) implies one on \(B\). For the closed zero section \(i:B\hookrightarrow E\), its exact direct image satisfies \(R\Gamma_c(B;M)=R\Gamma_c(E;i_*M)\) for every abelian sheaf \(M\). The total-space bound therefore bounds the left side, and the same dimension criterion applies. Thus stating the ambient absolute-duality hypothesis on the base does not restrict the class of vector bundles whose total spaces have the required finite dimension.

Define \(D_EF=R\mathcal Hom(F,\omega_E)\) and similarly on \(E^*\). The composition comparisons identify

\[
\omega_E\simeq\tau^!\omega_B,
\qquad \omega_{E^*}\simeq\pi^!\omega_B.
\tag{FDN13}
\]

**Corollary.** Under this additional absolute-duality hypothesis,

\[
I_E(D_EF)\xrightarrow{\sim}D_{E^*}(T_EF)
\qquad(F\in D^b_{\mathbb R_{>0}}(E;k)).
\tag{FDN14}
\]

**Proof.** Take \(H=\omega_B\) in FDN8 and use FDN13. The construction of \(a_B^!\) supplies \(\omega_B\in D^+\), exactly the range required in that theorem. No biduality map is used. \(\square\)

The absolute-dual formula requires the stated dimension hypothesis because it uses the right adjoint for the map to a point. SHV, Definition 4.7.1, makes the corresponding finite-cohomological-dimension hypothesis explicit. The ordinary-dual formula uses the inverse orientation complex on the base and therefore does not require that additional hypothesis.

If \(a:E^*\to E^*\) is negation, the halfspace comparison in the Fourier kernel unit identifies

\[
I_EH\simeq a^{-1}(T_EH)\otimes_k\pi^{-1}O[n].
\tag{FDN15}
\]

Indeed, \(I_EH\) is \(Rq_!((p^!H)_C)\) with \(C=\{\langle x,\xi\rangle\geq0\}\); negation changes \(C\) to \(N\), and \(p^!\) contributes the orientation of its fiber \(E^*\), identified positively with \(O\). Projection formula moves that base-pulled invertible factor outside \(Rq_!\). Therefore either duality formula can equivalently be written

\[
D^{\diamond}_{E^*}(T_EF)
 \simeq a^{-1}T_E(D^{\diamond}_EF)\otimes_k\pi^{-1}O[n],
\qquad \diamond\in\{\prime,\ \}.
\tag{FDN16}
\]

The blank superscript means absolute duality with its stated extra hypothesis. The antipode and positive shift in FDN16 are essential. In particular the formula is not obtained by simply commuting \(D^{\diamond}\) and \(T\).

## SH02-FDN-EXAMPLE. An infinite coefficient module

Work over a point, take \(k=\mathbb Q\), give \(E=\mathbb R^2\) its usual orientation, and let \(M=\bigoplus_{j\geq0}k\). Let \(i:\{0\}\hookrightarrow E\), and put \(F=i_*M\). Its transform is \(M_{E^*}\): on the support \(x=0\), the pairing restriction is automatic and the output projection is the identity.

Write \(M^*=\operatorname{Hom}_k(M,k)=\prod_{j\geq0}k\). Closed-embedding duality and the codimension-two orientation give

\[
D'_E F=i_*M^*[-2].
\]

This calculation uses \(i^!k_E=k[-2]\), followed by module Hom over a field. The inverse transform of a zero-section object is the constant object tensored with the fiber orientation in shift \([2]\). Consequently

\[
I_E(D'_E F)=M^*_{E^*}
 =D'_{E^*}(M_{E^*}).
\]

The last equality also follows directly from FDN3 for the projection to a point, canceling its invertible orientation complex; it does not rely on commuting an infinite product with an arbitrary inverse image.

This example is outside a finite-dimensional biduality argument. The evaluation map \(M\to M^{**}\) is not surjective. To check this, view the finite-support sequences as a proper subspace of \(\prod_{j\geq0}k\), and choose a linear functional on the quotient that is nonzero on the class of \((1,1,\ldots)\). Composing with the quotient gives a functional \(\lambda\) on \(M^*\) that vanishes on every coordinate vector but is not zero. A functional in the image of \(M\) is a finite linear combination of coordinate evaluations. If it vanishes on every coordinate vector, all its coefficients vanish, so it is zero. Thus \(\lambda\) is not in that image. Fourier duality above remains valid.

## SH02-FDN-PROBLEMS. Checking the comparison

**Problem 1.** Over an oriented real \(n\)-space, compute both sides of FDN12 for \(F=k_E\), keeping the cohomological shifts. Explain which transform goes in the same direction as \(T_E\).

**Solution.** Proper-support halfspace integration gives \(T_Ek_E=k_{\{0\}}[-n]\). Its ordinary dual is \(k_{\{0\}}\), since \(D'_{E^*}k_{\{0\}}=k_{\{0\}}[-n]\) and dualizing the input shift \([-n]\) adds \([n]\). On the other side, \(D'_Ek_E=k_E\) and FDN15 gives
\(I_Ek_E=a^{-1}k_{\{0\}}[-n][n]=k_{\{0\}}\).
It is \(I_E\), the inverse transform for the dual bundle, that goes from \(E\) to \(E^*\); \(S_E\) goes the other way.

**Problem 2.** Why is the global boundedness of \(F\) used even though a dual may be only bounded below? Explain why replacing \(R\mathcal Hom(F,Q)\) with \(R\mathcal Hom(F,k)\otimes_k^L Q\) would not give the same proof.

**Solution.** A global upper bound \(b\) for \(F\) and a lower bound \(c\) for \(Q\) give a lower bound \(c-b\) for internal Hom. Boundedness also makes the kernel input \(k_N\otimes p^{-1}F\) bounded and hence its proper direct image bounded. These are precisely the bounds used in FDN3–FDN10. The proposed tensor replacement requires dualizability and fails for general infinite modules. Over a field, for example, \(\operatorname{Hom}(\bigoplus_jk,-)\) is a product functor and is not generally tensoring with \(\prod_jk\). The adjunction proof uses internal Hom throughout and therefore applies to these modules.

**Problem 3.** Set \(n=0\), let \(B\) be arbitrary under the setup, and verify the map in FDN8 itself.

**Solution.** Then \(E=E^*=X=B\), every projection is the identity, \(N=B\), and \(O=k_B\). Thus \(T_E=I_E=\mathrm{id}\), while both test objects are \(H\). The composition comparison FDN9, both adjunction counits, and the tensor-unit comparison in FDN10 are identities. The tensor–Hom transpositions are the unit identities, so \(\Theta_{F,H}\) is the identity of \(R\mathcal Hom(F,H)\), not merely some invertible endomorphism of that object.

## SH02-FDN-NORMALIZATION. A distinct equality of adjunction maps

There is another issue in the Fourier theory which the preceding proof does not resolve. It concerns the actual units and counits of two adjunctions between opposite halfspace presentations. To state it precisely, put

\[
U_EF=Rq_*R\Gamma_C(p^{-1}F),\qquad
V_EG=Rp_!((q^!G)_C),
\qquad C=\{\langle x,\xi\rangle\geq0\}.
\tag{FDN17}
\]

Let \(c:T_E\xrightarrow{\sim}U_E\) be the specific comparison formed from the support-restriction maps and the zero-section proper-support comparison in the Fourier kernel unit. There are two comparisons \(V_E\to S_E\) to distinguish. The literal comparison \(d_{\rm lit}\) has inverse the reversed-halfspace chain NDF2 in [The geometric normalization of Fourier adjunctions](../../SH02-fourier-literal-normalization.html). The adjunction-normalized comparison \(d_{\rm adj}\) is the explicit mate NDF8. Write \(d\) for a stated choice between them in the formulas below; the name alone does not identify the two maps.

The adjunction \(T_E\dashv S_E\) has unit \(\eta\) and counit \(\epsilon\). A second adjunction \(V_E\dashv U_E\) uses a comparison between the orientation traces for the two vector-bundle fibers. For that second adjunction this course fixes the comparison induced locally by a negative-definite symmetric identification \(E\to E^*\). Denote its unit and counit by \(\widetilde\eta\) and \(\widetilde\epsilon\).

With \(d=d_{\rm adj}\), the proved paired inverse equations, with every composite typed, are

\[
\widetilde\epsilon_F\circ V_E(c_F)\circ d^{-1}_{T_EF}
 =\eta_F^{-1}:S_ET_EF\longrightarrow F,
\tag{FDN18}
\]

\[
c^{-1}_{V_EG}\circ\widetilde\eta_G
\quad\text{followed by}\quad T_E(d_G)
 =\epsilon_G^{-1}:G\longrightarrow T_ES_EG.
\tag{FDN19}
\]

Equivalently, the left side of FDN19 is
\(T_E(d_G)\circ c^{-1}_{V_EG}\circ\widetilde\eta_G\).
The proof of equivalence in the Fourier kernel unit makes all four adjunction maps invertible. That observation alone does not prove FDN18 or FDN19: two adjunction structures on the same inverse equivalences can differ by a nontrivial natural automorphism.

The positive and negative-definite comparisons of the orientation lines differ by \((-1)^n\). In a positive basis, a negative-definite symmetric matrix has \(n\) negative eigenvalues and determinant of sign \((-1)^n\). All negative-definite symmetric forms are joined by a path through such forms, so their induced orientation comparison is the same. This proves independence of the local choice and shows that the local comparison glues, even when no global metric has been selected. The remaining support and adjunction maps are computed in SH02-NDF-DEFECT: their complete literal defect is \((-1)^n\) on every object in the stated conic category.

**The literal and normalized values.** The complete comparison is proved in SH02-NDF-DEFECT and SH02-NDF-NORMALIZED, including the trace and localization maps on the full conic category. For either named choice of \(d\), record the specific natural automorphism

\[
\Delta_F=
\widetilde\epsilon_F\circ V_E(c_F)\circ d^{-1}_{T_EF}\circ\eta_F
 :F\longrightarrow F.
\tag{FDN20}
\]

For \(d=d_{\rm lit}\), NDF4 gives \(\Delta_F=(-1)^n\mathrm{id}_F\); the FDN19 left side is likewise \((-1)^n\epsilon_G^{-1}\). For \(d=d_{\rm adj}=(-1)^n d_{\rm lit}\), both displayed paired equations hold exactly. The proof first applies the enhanced-center and conic-descent theorem to the actual transformation, then computes its scalar through the relative Thom maps. It therefore covers the entire category; equality of kernel stalk dimensions is not its argument. The duality proof FDN10 retains its independently specified positive-orientation maps. No unrecorded change to those maps is made.

The historical identifier SH02-FS-NORM-OPEN now distinguishes the resolved comparison of these explicit course maps from an unspecified opposite comparison in another treatment. SH02-NDF-SOURCE-MAPS proves that the asserted inverse equations uniquely determine \(d_{\rm adj}\) with the fixed first comparison. It does not attribute an unstated geometric recipe to the antecedent or close a later microlocal mate by its endpoint type.

**Reduction to one equality.** In fact it is enough to prove FDN18 for all \(F\). Let \(\lambda:S_ET_E\to\mathrm{id}\) be its left side and let \(\zeta:\mathrm{id}\to T_ES_E\) be the left side of FDN19. Transporting the second adjunction along \(c\) and \(d\) gives an adjunction \(S_E\dashv T_E\) with counit \(\lambda\) and unit \(\zeta\). This follows directly by substituting \(c\) and \(d\) in its natural Hom bijection; the images of the identity maps are the composites displayed in FDN18–FDN19.

If \(\lambda=\eta^{-1}\), its triangle identity at \(G\) gives

\[
\eta_{S_EG}^{-1}\circ S_E(\zeta_G)=\mathrm{id}_{S_EG},
\qquad\text{hence}\qquad S_E(\zeta_G)=\eta_{S_EG}.
\]

The first adjunction has \(S_E(\epsilon_G)\circ\eta_{S_EG}=\mathrm{id}_{S_EG}\). Therefore \(S_E(\epsilon_G\circ\zeta_G)=\mathrm{id}_{S_EG}\). The equivalence \(S_E\) is faithful, so \(\epsilon_G\circ\zeta_G=\mathrm{id}_G\), and invertibility of \(\epsilon_G\) proves FDN19. This establishes the second equation from the first. NDF4 supplies the first defect calculation, and NDF5–NDF9 identify the comparison for which that defect is the identity.

## SH02-FDN-SOURCES — Exact source scope and the variable-test argument

Astérisque 128, §2.1, explicitly presents its Fourier results without proofs. The ordinary-dual statement in Theorem 2.1.3(iii) includes the antipodal convention and a relative compact-support factor. It is a comparison for the classical result, not a proof of FDN8 for an arbitrary base test object or a normalization of the course's named transformations.

In SHV, Theorem 4.4.7 proves the bounded projection formula using flat and proper-image-acyclic resolutions. Proposition 4.6.5 derives the extraordinary inverse-image/internal-Hom comparison from projection and adjunction for bounded inputs. Proposition 4.6.6 constructs the direct-image/internal-Hom map using evaluation and the exceptional counit, then checks it on open-set sections. These are the foundational mechanisms compared with FDN3–FDN6. The truncation argument above supplies the bounded-below test range used here, and the proof explicitly transposes evaluation to identify each map, not just its source and target.

The organizing argument is FDN10: carry a single base test object through the two projections, identify their extraordinary pullbacks by the composite adjunction, and evaluate the kernel against it. The inverse orientation complex gives ordinary coefficient duality. The base dualizing complex gives absolute duality only under its extra finite-dimension hypothesis, matching the scope of SHV, Definition 4.7.1. The two-sided base/total-space dimension comparison, variance, open-restriction compatibility and lower amplitude bounds are proved in their respective paragraphs. Neither a finite-dimensional biduality theorem nor a tensor replacement for internal Hom is used. The infinite-module example and rank-zero map calculation check precisely these distinctions.

The final normalization discussion concerns the explicit comparisons in this course. Its determinant sign, transported adjunction, inverse equations and faithfulness reduction retain their own exact proof locators. The source passages compared here do not identify an unspecified geometric map with those comparisons. Conic internal Hom, the orientation formula, the underlying six operations and the later normalization provider remain separate programme prerequisites. This source repair does not declare them all transitively closed. Independently expressed programme prose is CC0; no source chapter, diagram or exercise sequence is incorporated, and existing human component terms are unchanged.

## SH02-FDN-BOUNDARY. What this unit supplies

FDN3–FDN16 give complete conditional proofs of the two Fourier duality formulas, their full bounded input range, the necessary ambient hypothesis for absolute duality, and the antipode/orientation form of the result. FDN18–FDN20 distinguish the literal and adjunction-normalized comparisons; SH02-NDF-DEFECT and SH02-NDF-NORMALIZED compute their complete relation and prove the two paired inverse equations for the normalized choice. The underlying six operations, conic descent, and halfspace comparison remain explicit course dependencies.
