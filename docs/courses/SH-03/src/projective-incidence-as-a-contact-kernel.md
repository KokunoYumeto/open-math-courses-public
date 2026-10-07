# Projective incidence as a contact kernel

A point of a projective space is a line. A point of its dual projective space is a hyperplane. Incidence between them defines a sheaf kernel. We will calculate its cotangent relation, including the input sign, and prove that it gives an equivalence after localization away from the zero covectors. We will also calculate its inverse kernel without discarding the real orientation line.

We apply the contact-kernel criterion, including its identity-induced morphism, and the relative-dual comparison. The application below verifies the required formal local constructibility, both selected microsupport conditions, and the actual identity section. The submanifold microlocal Hom formula and relative orientation formula specify the two different orientation calculations. The projective relation and its orientation monodromy are calculated directly.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

## Lines, hyperplanes and cotangent vectors

Let \(\mathbb F\) be \(\mathbb R\) or \(\mathbb C\), and let \(V\) have dimension \(N\geq2\) over \(\mathbb F\). Put

\[
X=\mathbb P(V),\qquad Y=\mathbb P(V^*),\qquad
Z=\{(\ell,m):m(\ell)=0\}\subset X\times Y.
\qquad\text{(1)}
\]

Here \(m\) is a line of covectors; the notation \(m(\ell)=0\) means that every member of \(m\) vanishes on \(\ell\). In the real case these are ordinary projective lines, with no choice of a positive ray. Let
\(\Omega_X=\dot T^*X\) and \(\Omega_Y=\dot T^*Y\), where a dot removes the zero section.

The coefficient ring \(k\) is commutative with identity and finite global dimension. All sheaf objects are bounded derived complexes of \(k\)-modules. Complex manifolds are regarded as real manifolds for these operations. We identify a complex cotangent vector with a real covector by taking the real part of its pairing; using this convention on both factors preserves the formulas below. For a complex vector space, every real covector is uniquely the real part of a complex-linear covector. The real-part trace pairing is nondegenerate, so (2) identifies the entire real cotangent fibre in the complex case; no conjugate transpose or extra factor of two is inserted.

The omitted smaller vector-space dimensions are vacuous for this selected-region assertion. If \(N=0\), both projective spaces are empty. If \(N=1\), both are points, their punctured cotangent spaces are empty, and incidence is empty. The localized categories on an empty cotangent region are zero: every object is null there. All graph and identity conditions on that region hold vacuously. We calculate the nonempty correspondence for \(N\geq2\).

For a line \(\ell\subset V\), differentiation of the graph of a linear map gives

\[
T_\ell X=\operatorname{Hom}_{\mathbb F}(\ell,V/\ell),\qquad
T_\ell^*X=\operatorname{Hom}_{\mathbb F}(V/\ell,\ell).
\qquad\text{(2)}
\]

The second identification uses the trace pairing: a map \(A:V/\ell\to\ell\) acts on a tangent map \(u:\ell\to V/\ell\) by \(\operatorname{tr}_\ell(Au)\), or its real part over \(\mathbb C\). Regard \(A\) as an endomorphism of \(V\) by composing the quotient and inclusion maps. It has image in \(\ell\) and kills \(\ell\). A nonzero such endomorphism has rank one, image exactly \(\ell\), and \(A^2=0\). Conversely, if a nonzero rank-one endomorphism has square zero, its image line lies in its kernel; it therefore factors uniquely through \(V/\operatorname{im}A\to\operatorname{im}A\). Thus

\[
\dot T^*X=\{A\in\operatorname{End}_{\mathbb F}(V):
\operatorname{rank}A=1,\ A^2=0\}.
\qquad\text{(3)}
\]

This description includes the base point; it does not forget it. There is a corresponding description of \(\dot T^*Y\) by endomorphisms \(B\) of \(V^*\).

## The conormal relation and its minus sign

The equation of incidence is intrinsically the zero section of the line bundle \(\ell^*\otimes m^*\) evaluated by \((v,\lambda)\mapsto\lambda(v)\). Choose nonzero local representatives \(v\in\ell\) and \(\lambda\in m\) near an incident pair. In these local frames the equation is the scalar function \(f(v,\lambda)=\lambda(v)=0\). Its derivative in the \(v\) direction is nonzero because \(\lambda\) induces a nonzero functional on \(V/\ell\); the derivative in the \(\lambda\) direction is nonzero for the same reason with the two spaces exchanged. Over \(\mathbb C\) these are nonzero complex-linear maps to \(\mathbb C\), hence surjective as real maps. The zero set is closed, since it is the zero set of this global section, and is smooth of real codimension \(c=1\) over \(\mathbb R\) or \(c=2\) over \(\mathbb C\).

Both incidence projections are submersions. For example, after specifying a tangent variation of \(\ell\), surjectivity of the derivative in \(m\) supplies a variation of \(m\) that cancels it in \(df\). This lifts every tangent vector of \(X\) to \(T Z\); the other projection is treated symmetrically. Their relative real dimension is \(D-c\), where \(D=\dim_{\mathbb R}X=\dim_{\mathbb R}Y\).

For tangent variations represented by \(\delta v\) and \(\delta\lambda\), the derivative is \(\lambda(\delta v)+\delta\lambda(v)\). Replacing either variation by a multiple of its original representative does not change this value at incidence. The trace pairings in (2) identify these two terms with the endomorphisms \(v\otimes\lambda\) and \(\lambda\otimes v\). Thus, for a nonzero conormal parameter \(t\in\mathbb F\), the two **physical** cotangent components of \(t\,df\) are

\[
A=t\,v\otimes\lambda,\qquad B_{\mathrm{physical}}=t\,\lambda\otimes v.
\qquad\text{(4)}
\]

For complex \(t\), this means the real covector \(\operatorname{Re}(t\,df)\). These are all the real conormals. Changing projective representatives changes \(t\) inversely to their product, so (4) defines intrinsic covectors. The kernel's input component is the negative of the physical component. Therefore its relation has

\[
B=-t\,\lambda\otimes v,\qquad A=-B^{\mathsf t}.
\qquad\text{(5)}
\]

Here transpose means the canonical dual endomorphism, using \(V^{**}=V\); no inner product or complex conjugation is involved.

Every nonzero rank-one square-zero \(B\) has the form \(-t\lambda\otimes v\). Its image determines \(m\), the image of \(B^{\mathsf t}\) determines \(\ell\), and square-zero says \(\lambda(v)=0\). This proves existence and uniqueness of its point in (4). Recovering these lines is smooth: locally choose a nonzero column of a rank-one matrix to represent its image. These local recovery formulas agree on overlaps. The two nonzero conormal projections are therefore diffeomorphisms, and the kernel transformation is

\[
\chi:\dot T^*Y\longrightarrow\dot T^*X,
\qquad B\longmapsto -B^{\mathsf t}.
\qquad\text{(6)}
\]

The inverse has the same negative-transpose formula with the spaces exchanged. In particular each projection is a proper homeomorphism, even though its domain is not compact.

To verify the symplectic normalization, take a tangent vector to the incidence relation. On it the sum of the physical tautological forms is \(t\,d(\lambda(v))=0\), or its real part in the complex case. Negating the input covector changes this equality to
\(\theta_X-\theta_Y=0\). Since both projections are diffeomorphisms,

\[
\chi^*\theta_X=\theta_Y,\qquad
\chi^*d\theta_X=d\theta_Y.
\qquad\text{(7)}
\]

Formula (6) commutes with positive cotangent dilation. It is a homogeneous symplectic transformation with exactly the sign required for a sheaf kernel.

## Verifying the sheaf criterion

Let \(K=k_Z\), extended by zero to \(P=X\times Y\). We check the formal local constructibility condition, including the neighborhood transition maps. Put \(d=\dim_{\mathbb R}Z=2D-c\). At \(z\in Z\), take a cofinal family of adapted product balls \(U_\epsilon=B_\epsilon^d\times B_\epsilon^c\) with \(Z\cap U_\epsilon=B_\epsilon^d\times\{0\}\). Closed extension and the ordinary and compact-support coefficient calculations, (M5)–(M6), give

\[
R\Gamma(U_\epsilon;k_Z)\simeq k,
\qquad R\Gamma_c(U_\epsilon;k_Z)
\simeq\operatorname{or}_{T_zZ}[-d].
\]

The ordinary identifications are the constant-section units and commute with restriction. For compact supports, the local orientation generator and open-extension trace identify every map from a smaller ball with the same generator in the larger ball. The comparison from the point costalk is the support-forgetting isomorphism (M5), applied within \(Z\). Hence the formal ordinary and compact-support systems themselves are represented by the displayed stalk and costalk complexes. Both are perfect: locally they are one copy of \(k\) with an integral shift. Off \(Z\), a cofinal family misses the closed support and both systems are zero. This proves the criterion's cohomological constructibility, over the stated ring, without imposing any finiteness condition on the sheaves later transformed.

The closed-submanifold microsupport formula, (S16) gives \(\operatorname{SS}(k_Z)\subset T_Z^*P\). For the zero ring this inclusion follows directly from \(K=0\); for a nonzero ring the provider gives equality. In (4), one cotangent component is nonzero if and only if \(t\ne0\), if and only if the other component is nonzero. Thus the union \(p_1^{-1}\Omega_X\cup(p_2^a)^{-1}\Omega_Y\) meets this microsupport only in the selected graph. This is the union condition of the contact criterion. The graph is relatively closed in \(\Omega_X\times\Omega_Y^a\), since it is the graph of a continuous map between Hausdorff spaces. Both graph projections are the proper homeomorphisms already proved, giving forward and reverse admissibility.

The remaining condition is the identity-induced microlocal unit, (MH32). The closed-submanifold Hom comparison, with the conormal extension understood, gives

\[
\mu\operatorname{hom}(k_Z,k_Z)
\simeq\mu_Zk_Z\simeq k_{T_Z^*(X\times Y)}.
\qquad\text{(8)}
\]

To compute the second comparison, use normal coordinates \((z,u)\) with \(Z=\{u=0\}\). In the deformation defining specialization, the map to \(P\) is \((z,v,s)\mapsto(z,sv)\), \(s>0\). The pulled-back coefficient is supported on \(v=0\). At a central point with \(v\ne0\) it vanishes on a small neighborhood; at \(v=0\) the ordinary direct image has the constant-section generator on the interval \(0<s<\epsilon\). Its specialization is consequently the constant sheaf on the zero section of the normal bundle, with that same generator. The negative Fourier calculation for a zero-supported coefficient then gives the constant sheaf on the whole dual normal bundle: the support inequality is automatic, and the integration map on this support is an isomorphism onto that bundle. There is no fibre dimension to integrate and no codimension shift.

The microlocal unit is obtained from \(\operatorname{id}_K\) by exceptional diagonal adjunction before specialization. In a coefficient chart its section is \(1\mapsto\operatorname{id}_k\). The preceding specialization unit and zero-section Fourier map carry it to the section \(1\) in (8), as in the submanifold identity calculation. These constructions use restriction, adjunction and evaluation, so their local comparisons agree on overlaps. A coordinate change conjugates a coefficient endomorphism and fixes its identity; a change of normal orientation contributes no choice to the zero-section Fourier map. Thus the identity-induced map, rather than merely some abstract isomorphism of its source and target, is invertible on the selected graph.

All three conditions of the contact-kernel theorem now hold. Its adjunction unit is the kernel map constructed from the identity section just checked; its inverse comparison and counit are those of the same adjunction. We obtain inverse localized equivalences

\[
\Phi_{k_Z}:\mathcal D_Y(\dot T^*Y)\rightleftarrows
\mathcal D_X(\dot T^*X):\Psi_{k_Z},
\qquad\text{(9)}
\]

and, for arbitrary bounded inputs \(G_1,G_2\), the theorem's actual natural comparison gives

\[
\chi_*\mu\operatorname{hom}_Y(G_2,G_1)
\simeq\mu\operatorname{hom}_X(\Phi_{k_Z}G_2,\Phi_{k_Z}G_1)
\quad\text{on }\dot T^*X.
\qquad\text{(10)}
\]

The support \(Z\) is compact, so its ordinary support projections are proper too. Properness of the selected conormal projections, used in (9), was proved separately by their homeomorphism property. The result concerns the indicated localizations; it does not assert an equivalence of the full ordinary sheaf categories.

## The inverse kernel retains an orientation line

Write \(P=X\times Y\), let \(q_X,q_Y\) be its two projections, and let \(\mathrm t\) exchange the factors. Put \(D=\dim_{\mathbb R}Y\) and write \(i:Z\hookrightarrow P\). Closed-embedding adjunction identifies \(R\mathcal Hom_P(i_*k_Z,k_P)\) with \(i_*i^!k_P\). The relative orientation formula, (M16)–(M17), gives \(i^!k_P=\operatorname{or}_{Z/P}[-c]\). Equivalently, normal local cohomology is the relative complex of a \(c\)-ball and its punctured ball, whose generator has degree \(c\) and changes by the normal determinant sign. Thus

\[
R\mathcal Hom_P(k_Z,k_P)
\simeq k_Z\otimes\operatorname{or}_{Z/P}[-c].
\qquad\text{(11)}
\]

Here \(\operatorname{or}_{Z/P}\) is the normal orientation local system, with its exceptional degree written separately. The right relative dual is consequently

\[
K_R=\mathrm t\bigl(k_Z\otimes\operatorname{or}_{Z/P}
\otimes q_Y^{-1}\operatorname{or}_Y\bigr)[D-c].
\qquad\text{(12)}
\]

Here is the actual comparison for an arbitrary bounded \(F\) on \(X\). Put \(W_Y=q_Y^{-1}\omega_Y\), so the submersion formula gives \(q_X^!F=W_Y\otimes^Lq_X^{-1}F\). Evaluation and tensor–Hom adjunction give a natural arrow on \(P\):

\[
\bigl(R\mathcal Hom(K,k_P)\otimes^LW_Y\bigr)
 \otimes^Lq_X^{-1}F
\longrightarrow R\mathcal Hom(K,q_X^!F).
\]

For this incidence kernel the arrow can be checked directly. Set \(f=q_X\) and \(g=i\). Both \(f\) and \(fg=q_X|_Z\) are submersions, of relative dimensions \(D\) and \(D-c\). The submersion composition comparison, (M18), therefore identifies

\[
i^!q_X^{-1}F\simeq
(q_X|_Z)^{-1}F\otimes\operatorname{or}_{Z/P}[-c].
\]

Under closed-embedding Hom adjunction, the displayed evaluation arrow is this normal-support comparison, tensored with \(i^{-1}W_Y\) and extended by \(i_*\). In local coordinates for the submersion pair, the normal ball contributes its oriented relative generator and the comparison is the identity on the pulled-back \(F\); (M18) glues these comparisons by exceptional composition and orientation cancellation. Hence the arrow is an isomorphism for every bounded \(F\).

Apply \(Rq_{Y!}\) and the canonical forget-support map to \(Rq_{Y*}\). Both complexes are supported on the compact set \(Z\), so this latter map is an isomorphism. The source is convolution by (12), and the target is the right operator \(\Psi_{k_Z}(F)\). This proves its identification with the right adjoint, with the evaluation normalization used by the dual-kernel theorem, Corollary 2. After localization it is the inverse in (9). No perfectness of \(F\) is used in this comparison.

In the complex case the normal bundle and \(TY\) are complex vector bundles, so their underlying real orientation systems have the canonical complex orientations. Since \(D=2N-2\) and \(c=2\), the inverse is \(k_{Z^{\mathsf t}}[2N-4]\). This uses real dimensions, consistently with the real-part cotangent convention in (4).

In the real case the degree is \(N-2\). Let \(O_\ell\) and \(O_m\) be the integral-sign orientation systems of the tautological real lines, with coefficients extended to \(k\). The normal derivative of the transverse incidence section identifies its normal bundle with \(\ell^*\otimes m^*\). Taking determinant signs gives \(\operatorname{or}_{Z/P}=O_\ell\otimes O_m\); dualizing a real line does not change its sign character.

For \(Y=\mathbb P(V^*)\), the tangent formula (2) gives \(TY=m^*\otimes(V^*/m)\). The determinant of a tensor product with a line and the exact sequence \(0\to m\to V^*\to V^*/m\to0\) give

\[
\det TY=(m^*)^{\otimes(N-1)}\otimes\det(V^*/m)
\simeq\det V^*\otimes m^{-N}.
\]

Taking sign systems and multiplying the normal line by \(q_Y^{-1}\operatorname{or}_Y\) gives the line before transposition in (12):

\[
\operatorname{or}_{V^*}\otimes O_\ell\otimes O_m^{\otimes(N+1)}
\quad\text{on }Z.
\qquad\text{(13)}
\]

The orientation of the fixed vector space \(V^*\) is a constant line. Orientation sign systems are their own inverses, which explains why the negative tensor powers from the determinant formula give the positive powers in (13). A coordinate choice can trivialize a constant line; it cannot erase nontrivial monodromy in \(O_\ell\) or \(O_m\).

These sign systems have their canonical square pairing; the assertion is stronger than saying that they have rank one. Along a loop in \(Z\) on which \(\ell\) and \(m\) return with signs \(\epsilon_\ell,\epsilon_m\), the line (13) has monodromy \(\epsilon_\ell\epsilon_m^{N+1}\). The constant factor \(\operatorname{or}_{V^*}\) has no monodromy. For \(N\geq3\), a projective-line loop in a fibre of \(Z\to Y\) has \(\epsilon_\ell=-1\), \(\epsilon_m=1\), so this line cannot be discarded when \(-1\ne1\) in the coefficient ring.

For \(N=2\), incidence is the graph of the annihilator diffeomorphism \(Y\to X\), over either field, and \(D=c\). In the real case the exact sequence \(0\to\ell\to V\to m^*\to0\) on incidence gives \(\operatorname{or}_V=O_\ell\otimes O_m\). Its dual has the same sign orientation, so (13) reduces canonically to \(O_\ell^{\otimes2}\otimes O_m^{\otimes4}\simeq k_Z\). The right kernel is therefore the unshifted transposed graph, agreeing with ordinary graph adjunction. In the complex case its two complex orientations give the same degree-zero conclusion. The dimensions \(N=0,1\) remain the empty-selected-region cases described above; these normal-bundle calculations are used for \(N\geq2\).

## Exercises with complete solutions

### Recovering the input sign

*Difficulty: Introductory.*

For \(V=\mathbb R^3\), take \(v=e_1\), \(\lambda=e_2^*\) and \(t=2\). Write the physical conormal pair and the input endomorphism. Check square-zero and the formula for \(\chi\).

**Solution.** The physical pair is \((2e_1\otimes e_2^*,2e_2^*\otimes e_1)\). The input is \(B=-2e_2^*\otimes e_1\). The first endomorphism sends \(e_2\) to \(2e_1\) and kills \(e_1\); the input sends \(e_1^*\) to \(-2e_2^*\) and kills \(e_2^*\). Both have square zero and rank one. Finally \(-B^{\mathsf t}=2e_1\otimes e_2^*\), the required output. Using the physical second component without the antipode would give the opposite sign.

### Incidence on a real projective line

*Difficulty: Intermediate.*

When \(V=\mathbb R^2\), show that incidence is the graph of a diffeomorphism between the two projective lines. Explain why the inverse kernel has degree zero and a trivial total orientation line.

**Solution.** A nonzero covector has a one-dimensional kernel. Thus \(m\mapsto\ker m\) is a bijection \(Y\to X\); its inverse sends a line to its annihilator line. Both maps are smooth in projective coordinate charts. Hence \(Z\) is its graph and the transform is pushforward along this diffeomorphism. The graph has real codimension one in the two-dimensional product, and \(Y\) has dimension one, so \(D-c=0\). Its normal orientation is the pullback of the orientation of \(Y\); tensoring it with that same orientation in (12) cancels it canonically. The inverse is the unshifted sheaf of the transposed graph, as ordinary graph calculus also shows.

### A complex projective plane

*Difficulty: Intermediate.*

For \(V=\mathbb C^3\), calculate the inverse degree. Explain why complex codimension must be converted before applying (11).

**Solution.** The dual projective plane has complex dimension two and real dimension four. Incidence has complex codimension one and real codimension two. The inverse degree is \(4-2=2\), so the right relative dual is \(k_{Z^{\mathsf t}}[2]\). A closed complex hypersurface has exceptional degree \(-2\) in real sheaf theory. Substituting complex codimension one into the real formula would give degree three and would use the wrong duality normalization. Complex orientations canonically trivialize the two orientation lines.

### Why zero covectors are excluded

*Difficulty: Intermediate.*

Assume \(N\geq3\). Show directly that the conormal relation does not have a graph projection over a zero covector of \(X\). Relate this to ordinary constant sheaves.

**Solution.** At \((\ell;0)\), parameter \(t=0\) is possible for every hyperplane containing \(\ell\). These hyperplanes form \(\mathbb P((V/\ell)^*)\), of positive dimension \(N-2\). Thus the projection has more than one point in this fibre. The nonzero recovery argument cannot be extended to it. A locally constant bounded sheaf has microsupport in the zero section and becomes zero in the selected localization. Hence (9) omits precisely such ordinary information; it does not prove an equivalence before localization. For \(N=2\) the incidence graph has the separate ordinary equivalence calculated in the previous exercise.

### A real orientation that cannot be dropped

*Difficulty: Advanced.*

Let \(V=\mathbb R^3\) and take \(k\) to be a field of characteristic different from two. Fix \(m\in Y\). Determine the monodromy of the inverse line along the fibre \(\{\ell\subset\ker m\}\simeq\mathbb R\mathbb P^1\) of \(Z\to Y\).

**Solution.** In (13), \(N+1=4\), so the fourth tensor power of \(O_m\) is trivial. On the specified fibre it is constant in any case. The fixed line \(\operatorname{or}_{V^*}\) is also constant. The remaining factor is \(O_\ell\), the tautological sign system on \(\mathbb R\mathbb P^1\). A lift of one circuit in the projective line changes a unit vector representing \(\ell\) to its negative; transport on this orientation line is multiplication by \(-1\). It is nontrivial over the stated field. The inverse degree is one, but replacing (12) by \(k_{Z^{\mathsf t}}[1]\) would lose this monodromy. In characteristic two this particular sign obstruction disappears, which is why the coefficient hypothesis matters for the example.

## References

Masaki Kashiwara and Pierre Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), Theorem 6.3.4, printed pp. 111–113 (PDF pp. 114–116), proves the contact-kernel equivalence from cohomological constructibility, the selected union-of-regions microsupport condition, and the identity-induced endomorphism isomorphism. Theorem 6.3.9 and Corollary 6.3.11, printed pp. 115–117 (PDF pp. 118–120), give the natural transport of microlocal Hom. Their transformed arguments are not both required to be constructible.

The source uses an ordinary-image Hom operator from \(Y\) to \(X\), and places the antipode on the \(X\) covector of its physical kernel. Here \(\Phi\) is the proper-support tensor operator from \(Y\) to \(X\), with the antipode on the input \(Y\) covector. The linked criterion and relative-dual theorem state this convention explicitly. Equations (4)–(5) derive the physical signs before the operator is applied, and the evaluation map above fixes which adjoint is the inverse.

The rank-one square-zero description, incidence submersions, determinant characters and real orientation monodromy are calculated in this lesson. The cited general theorem supplies the contact argument; it is not being cited as a source for these particular projective calculations. The coefficient and supported-specialization proofs check its hypotheses, including the actual identity section. The real and complex small-dimensional cases and the worked exercises retain the normalizations from those calculations.
