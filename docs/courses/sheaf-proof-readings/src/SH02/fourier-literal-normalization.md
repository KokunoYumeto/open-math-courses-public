# SH02-NDF-UNIT. The geometric normalization of Fourier adjunctions

Original English supplement for Course SH-02, dedicated under CC0 1.0 Universal. The proofs retain the named operation prerequisites and their stated scope.

Two presentations of an inverse Fourier transform can agree as functors while their chosen comparison has the wrong scalar for a prescribed pair of adjunctions. This lesson computes that scalar on the full conic derived category, then identifies the unique comparison that makes the two pairs of adjunction maps inverse. The proof first reduces an actual natural transformation to a base scalar, computes its trace, and finally uses a uniqueness argument to identify the normalized comparison.

The four Fourier presentations have published antecedents in Kashiwara–Schapira, *Microlocal Study of Sheaves*, Astérisque 128 (1985), §2.1, and Schapira, *An Introduction to Sheaves on Grothendieck Topologies*, Definition 5.4.5. Those presentations and the inverse-equivalence statements identify functors. Here the literal reversed-halfspace comparison, the orientation identification defining the second adjunction, and the adjunction-normalized comparison are separately specified maps. Their equality requires the calculation below; it is not inferred from the functor-level statements.

## SH02-NDF-DOMAINS. Fix the geometric maps before changing an adjunction

Let \(B\) be locally compact Hausdorff and \(E\) a real vector bundle of fixed finite rank \(n\). The coefficient ring \(k\) is commutative and unital, of finite global dimension. Work in the full parameter-conic globally bounded-below derived category \(D^+\). No finite stalk, constructibility, field, orientability, compactness, manifold-base or upper-bound assumption is used. Locally constant ranks may be used componentwise with the original global operation bounds. Every transformation below is the enhanced natural transformation supplied by the named derived operations.

Use \(X=E\times_BE^*\), projections \(p,q\), and cuts \(N=\{\langle x,y\rangle\leq0\}\), \(C=\{\langle x,y\rangle\geq0\}\). Write \(W_x=O_E[n]\), \(W_y=O_{E^*}[n]\), with their pullbacks suppressed and positive dual-orientation comparison \(\phi_+:W_x\to W_y\). All orientation complexes stay on the right of coefficients unless a symmetry is explicitly displayed.

Fix

\[
T F=Rq_!((p^{-1}F)_N),\qquad
U F=Rq_*R\Gamma_C(p^{-1}F),
\]
\[
S G=Rp_*R\Gamma_N(q^!G),\qquad
V G=Rp_!((q^!G)_C).
\tag{NDF1}
\]

The first adjunction \(T\dashv S\) is the raw \(q_!\dashv q^!\), cut tensor–Hom, \(p^{-1}\dashv Rp_*\) adjunction, with unit \(\eta\) and counit \(\epsilon\). The comparison \(c:T\to U\) is exactly FS6. The map \(d_{\rm lit}:V\to S\) has inverse the literal reverse-halfspace chain FTC19:

\[
\begin{aligned}
Rp_*R\Gamma_N L&\longrightarrow Rp_*((R\Gamma_NL)_C)
\longleftarrow Rp_!((R\Gamma_NL)_C)\\
&\simeq Rp_!R\Gamma_N(L_C)\longrightarrow Rp_!(L_C),
\qquad L=q^!G.
\end{aligned}
\tag{NDF2}
\]

The backward proper-support arrow is inverted on its proved zero-section support. The interchange is the map compatible with restriction \(L\to L_C\) and the functorial localization triangles. Invertible arrows use their fixed inverses. No arrow is multiplied by an unnamed scalar.

Let \(\phi:W_x\to W_y\) be an orientation-complex isomorphism. It has the form \(\phi=\rho\phi_+\), where \(\rho\) is a locally constant unit of \(k\) on \(B\). It defines the literal second adjunction \(V\dashv U\) by identifying the \(q^!\) and \(p^!\) orientation factors in the tensor–Hom adjunction. Denote its unit by \(z_\phi\) and counit by \(e_\phi\). Its counit is, before \(Rp_!\), the local-support evaluation followed by the \(\phi\) identification; in particular \(\phi\) appears once, in that direction. Define

\[
\Delta_\phi=e_\phi V(c)d_{\rm lit,T}^{-1}\eta:1\longrightarrow1.
\tag{NDF3}
\]

The exact prerequisites are Fourier kernels, The linear Fourier comparison, and [Comparing traces after Fourier transformation](fourier-trace-comparisons.md), with the following scoped uses: the actual FS6 comparison; SH02-FS-INVERSION (FS12 and its full proof), which makes both raw adjunctions equivalence adjunctions and hence makes their units and counits invertible; the full conic-topology derived equivalence SH02-LFT-CONIC-TOPOLOGY; the enhanced-center theorem SH02-LFT-CENTER; and the relative-cochain trace calculation FTC20–FTC22 and the following explicit counit and arbitrary-rank paragraphs, including its arbitrary-rank zero-section extension and the cancellation of the actual Thom trace coefficients. These are scoped mathematical prerequisites, with their operation imports retained.

## SH02-NDF-DEFECT. Determine the entire natural transformation

For every object in the stated full category,

\[
\Delta_\phi=\rho\,1.
\tag{NDF4}
\]

First, NDF3 is an enhanced exact natural automorphism of the identity: it is the composite of the two adjunction transformations, invertible by SH02-FS-INVERSION, and the specified enhanced comparison isomorphisms. The center theorem after conic descent therefore applies to this actual transformation. It says that such a transformation is multiplication by a locally constant base scalar, and that its scalar is determined by its component on \(i_*k_B\) for the zero section \(i:B\to E\). This is exactly the full-category conclusion of the center/conic-topology proofs; neither an ordinary triangulated generation assertion nor an isomorphism of stalk dimensions is substituted for it.

It remains to identify that scalar. This is local on \(B\). Trivialize \(E\), choose positive dual coordinates \(x,y\), and work at a base stalk \(b\). The coefficient \(i_*k_B\) has \(T(i_*k_B)=U(i_*k_B)=k_{E^*}\), and \(c\) on this object is the identity: the pulled-back coefficient is on \(x=0\) and projects isomorphically to \(E^*\). Proper-support base change and the product orientation trace reduce the other maps to the fiber calculation with the same coefficient \(k\). This reduction does not impose a dimension condition on \(B\).

Here is the actual fiber calculation, recalled to fix its signs. Put \(Q(x,y)=x\cdot y\), \(u=(x+y)/2\) and \(v=(x-y)/2\). Both \(\{Q>0\}\) and \(C\setminus\{0\}\) retract, by shrinking \(v\), onto the punctured graph \(x=y\). Its projections to the \(x\) and \(y\) spaces preserve the prescribed positive orientations. Projection \(\{Q>0\}\to\{x\ne0\}\) has contractible open-halfspace fibers, and the map from the vertical axis to the graph coordinate is \(y\mapsto y/2\). Thus the same relative-cochain/localization model carries the \(x\) Thom class to the \(y\) Thom class by a positive map through every arrow in NDF2. The support/tensor interchange is compatible with the same ambient restriction and complement maps. No independent choice of a one-dimensional cohomology identification occurs.

If the trace of the integral \(x\) relative class is \(t_x\), the raw unit uses \(t_x^{-1}\) times that class. Orientation-preserving coordinate compatibility gives \(t_y=t_x\). Keep \(W_x\) on the right throughout; no shifted \(W\) is moved past a relative cochain. NDF2 consequently carries the unit to \(t_x^{-1}\) times the \(y\) relative class with coefficient \(W_x\). The literal counit first applies \(\phi\) and then the \(y\) trace. Its value is \(t_x^{-1}\rho(b)t_y=\rho(b)\). This is the calculation in FTC20–FTC22 and the following explicit counit and arbitrary-rank paragraphs, with its orientation-preserving graph proof in every finite rank. The free integral orientation groups extend to every allowed \(k\). In rank zero all maps before \(\phi\) are identities. The empty base is vacuous.

Changes of local positive frames conjugate the two traces by the same transition map, so the calculation glues even when \(E\) is nonorientable. Therefore the component on \(i_*k_B\) is \(\rho\). The cited enhanced-center theorem now extends this equality to every conic globally bounded-below object, proving NDF4. The extension uses the entire independently proved center/descent input; it is not a claim that one component alone ordinarily determines a natural transformation. \(\square\)

## SH02-NDF-NORMALIZED. Identify the unique comparison with inverse adjunction maps

Let

\[
d_\phi=\rho\,d_{\rm lit}:V\longrightarrow S.
\tag{NDF5}
\]

Then the paired inverse equations are

\[
e_\phi V(c)d_{\phi,T}^{-1}=\eta^{-1},
\tag{NDF6}
\]
\[
T(d_\phi)c_V^{-1}z_\phi=\epsilon^{-1}.
\tag{NDF7}
\]

For NDF6 substitute NDF5 into NDF3: inverse comparison contributes \(\rho^{-1}\), so NDF4 gives identity after composition with \(\eta\). Every factor is an isomorphism, hence cancellation proves NDF6. Transporting \(V\dashv U\) along \(c\) and \(d_\phi\) yields \(S\dashv T\). Its counit is NDF6's left side and its unit is NDF7's left side; their types and order follow by applying these isomorphisms to the actual Hom bijection. Its triangle and the triangle for \(T\dashv S\) then prove NDF7 exactly as in FDN's reduction to one equality. For completeness, if the transported unit is \(\zeta\), its triangle gives \(S(\zeta_G)=\eta_{SG}\). The original triangle gives \(S(\epsilon_G)=\eta_{SG}^{-1}\). Faithfulness of \(S\) yields \(\epsilon_G\zeta_G=1\), hence \(\zeta_G=\epsilon_G^{-1}\).

This comparison is also exactly the adjunction-normalized map FTC16,

\[
d_{\rm adj}=S(z_\phi^{-1})\,S(c_V)\,\eta_V:V\longrightarrow S.
\tag{NDF8}
\]

Indeed FTC16's mate proof establishes NDF6 for \(d_{\rm adj}\). If \(d\) and \(d\prime\) both satisfy NDF6, cancel \(e_\phi V(c)\), which is invertible, to obtain \(d_T^{-1}=(d\prime_T)^{-1}\). Since \(T\) is essentially surjective, naturality along an isomorphism \(TF\to G\) gives \(d_G=d\prime_G\) for each \(G\). Thus the normalized comparison is unique, and NDF5 equals NDF8 as natural transformations. This is a proof of an equality of actual comparisons, not merely a replacement definition.

For a locally chosen negative-definite symmetric identification, \(\rho=(-1)^n\). Accordingly

\[
d_{\rm adj}=(-1)^n d_{\rm lit}.
\tag{NDF9}
\]

With \(d_{\rm lit}\) itself, the exact FDN18 left side is instead \((-1)^n\eta^{-1}\). The corresponding FDN19 left side is \((-1)^n\epsilon^{-1}\): the transported counit is scaled by \(\rho\), so its unit scales by \(\rho^{-1}\), and \(\rho^{-1}=\rho\) for this particular orientation choice. More generally with arbitrary \(\rho\) the two factors are \(\rho\) and \(\rho^{-1}\), respectively. Thus the originally fixed literal pair satisfies both inverse assertions precisely on components where \(\rho=1\) in \(k\). For odd rank over the integers it fails, already on the allowed zero-section object. Rank zero and characteristic two behave as the formulas state; no coefficient restriction is introduced to avoid the failure.

## SH02-NDF-SOURCE-MAPS. What the inverse equations determine

The normalization problem has fixed mathematical input: the four functors NDF1 with their raw adjunction, the actual first comparison FS6, the reverse-halfspace chain NDF2, and the negative-definite orientation identification in the second adjunction. The two desired inverse equations impose a condition on a comparison. Naming the functors or knowing that they are inverse equivalences does not determine whether the literal chain satisfies that condition.

There is a precise mathematical answer to that normalization condition. Keep the four functors NDF1, the first comparison \(c\), and the negative-definite second adjunction fixed. Then there exists exactly one comparison \(d:V\to S\) satisfying the first paired inverse equation for every \(F\). It also satisfies the second paired equation for every \(G\), and it is

\[
d=d_{\rm adj}=(-1)^n d_{\rm lit}.
\tag{NDF10}
\]

Existence and the displayed formula are NDF5–NDF9. The cancellation and essential-surjectivity argument following NDF8 proves uniqueness. Thus the paired assertions have a complete, explicit realization at the stated full generality. If a further construction is claimed to realize the same first comparison, orientation identification and inverse equations, uniqueness identifies it with NDF10.

NDF4 computes the literal defect before NDF5 corrects it, and NDF6–NDF7 then verify both inverse equations. For these explicitly specified maps, using the literal reversed chain with the negative-definite second adjunction in odd rank over \(\mathbb Z\) gives the nontrivial defect already proved above. The normalized comparison removes that computed defect. This conclusion concerns the declared constructions and follows from their cochain, orientation and adjunction maps.

## SH02-NDF-PROBLEMS. Test the scalar and its inverse

**Problem 1.** Take an oriented real line over a point, use integral coefficients and the negative-definite orientation identification. Compare the literal and normalized second maps. Does restricting to objects with finite stalks remove the defect?

**Solution.** The rank is one and the comparison scalar is \(\rho=-1\). The literal defect is \(-1\) on every conic object. Thus \(d_{\rm adj}=-d_{\rm lit}\); its inverse contributes the second minus sign in NDF6. The zero-section sheaf \(\mathbb Z_{\{0\}}\) already has finite stalks and detects the failure of the literal inverse equation. A finite-stalk restriction would not repair that equation. The normalized comparison satisfies both inverse equations for the full original coefficient category.

**Problem 2.** Over \(k=\mathbb Q\), replace the positive orientation-complex comparison by twice that comparison. What are the two literal paired maps after identification with the inverse first unit and counit? What scalar multiplies the normalized comparison?

**Solution.** Here \(\rho=2\). The literal counit composite in FDN18 is \(2\eta^{-1}\), whereas the literal unit composite in FDN19 is \(\frac12\epsilon^{-1}\). This reciprocal is forced by the two triangle identities. The normalized comparison is \(2d_{\rm lit}\), whose inverse contributes \(\frac12\) in the counit equation and whose direct occurrence contributes \(2\) in the unit equation. Both corrected composites therefore have scalar one. This is a change of the permitted coefficient-line isomorphism; it is not induced by a real coordinate orientation, whose geometric degree is a sign.

**Problem 3.** Suppose \(d,d':V\to S\) both satisfy NDF6 on every coefficient object. Why does this determine their components on an arbitrary \(G\), rather than only on objects written literally as \(TF\)?

**Solution.** Invertibility of \(e_\phi V(c)\) and equality in NDF6 give \(d_{TF}=d'_{TF}\). The Fourier equivalence supplies an isomorphism \(j:TF\to G\). Naturality says \(S(j)d_{TF}=d_GV(j)\), and the same identity holds for \(d'\). Since \(V(j)\) is invertible, cancellation gives \(d_G=d'_G\). No canonical choice of \(F\) or \(j\) is needed: every such choice gives the same equality. This is the specific uniqueness argument identifying NDF5 with NDF8.

## SH02-NDF-STATUS. Keep the three comparisons distinct

The literal comparison is defined by NDF2. The normalized comparison is defined by NDF8 and identified with \((-1)^n d_{\rm lit}\) for the negative-definite second adjunction. NDF6–NDF7 prove the paired inverse equations on the entire stated category. NDF10 characterizes the unique comparison satisfying those equations with the specified first comparison and second adjunction. Any additional geometric construction must be compared with these actual maps before the characterization applies.

In [Fourier duality](fourier-duality-normalization.md), SH02-FDN-NORMALIZATION, the second comparison must therefore be named. The literal choice gives the parity formulas, while the normalized choice gives exact inverse maps. The named prerequisite results and their precise operation domains remain in force when propagating either convention.

This theorem does not identify the precise microlocal mate PA32 and does not use the linear trace equation FTC14. To apply it to a later mate, expand that mate's actual unit, counit and orientation factors and substitute the chosen comparison at its exact occurrence. Matching endpoint objects does not specify that composite.

**Published source and proof mechanism.** [Kashiwara–Schapira, *Microlocal Study of Sheaves*, Astérisque 128 (1985)](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), printed pp. 39–40 (PDF pp. 42–43), Proposition 2.1.1, Definition 2.1.2 and Theorem 2.1.3(i), states the halfspace presentations and inverse equivalences for bounded-below conic complexes over a locally compact base; §2.1 supplies no proof of those statements. [Schapira, *An Introduction to Sheaves on Grothendieck Topologies*, 1 August 2026 version](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf), Definition 5.4.5 and Theorem 5.4.6, p. 114, states the same forward and inverse presentations in a bounded conic category over a real manifold. The latter scope alone does not establish this lesson's arbitrary locally compact base or globally bounded-below coefficient range. Neither consulted passage calculates the scalar of the particular literal chain NDF2 against the particular second adjunction used here.

The proof of that scalar has three separate inputs. The enhanced conic-descent and center results named before NDF4 reduce this actual natural transformation to its zero-section component. The relative-cochain calculation FTC20–FTC22 and its arbitrary-rank continuation then track the same Thom class through every arrow, keeping the orientation complex on the right. The final trace cancels the raw-unit trace coefficient and leaves the orientation-identification scalar. Faithfulness and essential surjectivity of the fixed Fourier equivalence prove NDF6–NDF10 from that value. The center/descent theorem is a substantive course prerequisite; checking a single object or citing a Fourier equivalence would not replace it. Conversely the zero-section trace calculation is supplied explicitly here and in FTC, rather than left as an unspecified comparison of one-dimensional groups.

The local orientation and adjunction primitives can be compared with Schapira's Theorem 4.6.1, pp. 94–95, the relative-dualizing comparison (4.7.4), p. 97, and Proposition 5.1.9 with its proof, pp. 107–108. The latter proof uses local product charts and integration for compact convex fibres; the course retains that trace mechanism but additionally fixes its occurrence and line order in NDF2–NDF3. The arbitrary coefficient and global lower-bound requirements are the explicit course operation contracts, including SH02-FF-BOUNDS, not an unstated extension of the bounded Fourier passage. The independently written argument is under CC0; the cited human works retain their own terms.
