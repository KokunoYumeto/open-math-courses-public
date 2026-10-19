# Hilbert and Quot schemes

*Written by GPT-6.1 Sol (OpenAI) (Codex), October 2026. Public domain (CC0).*

A sheaf quotient can be recovered from enough of its sections, provided the meaning of “enough” is uniform across the family. A Grassmannian records a quotient of the resulting finite module of sections. It does not by itself ensure that the induced sheaf has the desired Hilbert polynomial or is flat. Flattening supplies those conditions, and a valuation argument closes the resulting locally closed subscheme. This is the construction of the projective Quot scheme.

We give the construction over a Noetherian base with a coherent source, allowing that source and its module of sections to be nonflat. The test schemes are arbitrary. We then construct finite-point Hilbert schemes by explicit algebra charts and calculate the two-point scheme of the affine plane.

The prerequisites are the representability and Plücker proofs in *Grassmannians*, the uniform kernel theorem in *Regularity and bounded families*, and the projective flattening theorem in *Flattening stratifications*. We also use [the arbitrary-base perfect pushforward theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-AS/moduli-stacks-are-algebraic.html#native-spaces-perfect-lemma-base-change-tensor-perfect), with its elementary cohomology consequences proved in the latter lesson, and the Noetherian discrete-valuation criterion for properness [Stacks, Tag 0208]. The corrected partial-coefficient strengthening discussed in the regularity lesson is not needed for the construction.

## 1 Quotients and their families

Let \(f:X\to S\) and let \(E\) be quasi-coherent on \(X\). The functor \(\operatorname{Quot}_{E/X/S}\) assigns to an \(S\)-scheme \(T\) the equivalence classes of surjections

\[
E_T\twoheadrightarrow G,
\]

where \(G\) is finitely presented, flat over \(T\), and has support proper over \(T\). Two quotients are equivalent if there is an isomorphism of their targets respecting the surjections. Equivalently, their kernels are equal. An automorphism respecting a surjection is the identity. Pullback preserves surjectivity, finite presentation and flatness, and proper support remains proper after base change, so this defines a functor.

The Hilbert functor is the special case \(E=\mathcal O_X\). A submodule \(I\subset\mathcal O_{X_T}\) is an ideal, and its quotient is \(\mathcal O_Z\) for the corresponding closed subscheme \(Z\subset X_T\). Thus

\[
\begin{gathered}
\operatorname{Hilb}_{X/S}(T)=\\
\left\{\begin{array}{l}
Z\subset X_T\text{ closed}:\\
Z\to T\text{ is proper, flat}\\
\text{and of finite presentation}
\end{array}\right\}.
\end{gathered}
\]

This identification respects arbitrary base change. It also explains why a Hilbert family consists of embedded subschemes, rather than abstract schemes with an embedding chosen up to an unrelated isomorphism.

These functors are sheaves for faithfully flat quasi-compact descent. To see the mechanism, a compatible family of quotient kernels is descent data for quasi-coherent submodules of \(E_T\). Faithfully flat descent glues the submodules and the quotient maps; equality can be tested after the cover. Finite presentation and flatness descend, as does properness of their support. This uses the usual faithfully flat descent theorem for quasi-coherent modules and morphisms. For the Hilbert case, it is descent of ideal sheaves and of the proper flat closed subschemes they define.

Now suppose \(f\) is projective and choose a relatively very ample invertible sheaf \(L\). Write \(G(m)=G\otimes L^m\). The fibre polynomial

\[
P_{G_t}(m)=\chi(X_t,G_t(m))
\]

is locally constant on \(T\), by flat proper cohomology. Let \(\operatorname{Quot}^{P,L}_{E/X/S}\) be the subfunctor where it is constantly \(P\). Decomposing every test scheme into its open and closed polynomial loci gives a decomposition of functors

\[
\operatorname{Quot}_{E/X/S}=
\coprod_P\operatorname{Quot}^{P,L}_{E/X/S}.
\]

The coproduct here is a sheaf coproduct: a map from a disconnected test scheme can have different polynomials on its open and closed pieces. It need not select one polynomial on the whole scheme.

## 2 One twist across the entire base

**Lemma 2.1.** Suppose \(S\) is Noetherian, \(f:X\to S\) is projective, \(L\) is relatively very ample, \(E\) is coherent, and \(P\) is fixed. There is \(m_0\) such that for every field-valued point \(s\) of \(S\), every quotient \(E_s\twoheadrightarrow G\) of polynomial \(P\), and every \(m\geq m_0\), its kernel \(K\), its quotient \(G\), and \(E_s\), after twist \(m\), are globally generated and have zero higher cohomology. Moreover, after increasing \(m_0\),

\[
V_m=f_*E(m)
\]

is coherent, its evaluation map \(f^*V_m\twoheadrightarrow E(m)\) is surjective, and

\[
V_m\otimes\kappa(s)\simeq H^0(X_s,E_s(m))
\]

for every \(s\), including after arbitrary extension of \(\kappa(s)\).

**Proof.** Take a finite affine cover of \(S\) on which \(X\) embeds in some \(\mathbb P^n\) with \(L=\mathcal O(1)|_X\). Such a cover exists even if the original projective presentation uses a coherent sheaf rather than a vector bundle: that sheaf has finitely many generators on each affine open, giving a closed immersion into a finite projective space there. Push \(E\) forward by the closed immersion.

On one affine open, relative Serre generation gives an integer \(a\) and a surjection \(\mathcal O^N\to E(a)\). It remains surjective on every fibre. The fibre polynomials of \(E_s\) range over a finite set, by the numerical finiteness argument in *Flattening stratifications*. Hence the kernels \(K_{0,s}\) of these surjections also have finitely many polynomials. The uniform kernel bound for subsheaves of \(\mathcal O^N\) makes all \(K_{0,s}\) uniformly regular, independent of their residue fields.

For a quotient \(E_s\to G\), let \(K'\) be the kernel of the composite \(\mathcal O^N\to G(a)\). Its polynomial is

\[
N\binom{t+n}{n}-P(t+a),
\]

so the same theorem uniformly bounds \(K'\). The exact sequence

\[
0\longrightarrow K_{0,s}\longrightarrow K'
\longrightarrow K(a)\longrightarrow0
\]

and the long exact cohomology sequence give a uniform regularity bound for \(K\). Explicitly, \(K(a)\) is \(b\)-regular if \(K'\) is \(b\)-regular and \(K_{0,s}\) is \((b+1)\)-regular. The sequence \(0\to K'\to\mathcal O^N\to G(a)\to0\) also uniformly bounds \(G\). The finitely many polynomials of \(E_s\), together with its fixed presentation, uniformly bound \(E_s\) in the same way. Regularity gives the claimed generation and vanishing.

For the last comparison, use a finite graded presentation of the pushed-forward \(E\). Its sufficiently high graded pieces equal \(H^0(E(m))\) on the original Noetherian affine base. The uniform fibre comparison in Lemma 5.1 of *Flattening stratifications* identifies these same graded pieces, after tensoring with any residue field, with \(H^0(E_s(m))\). Increase \(m_0\) to satisfy both comparisons. Coherence of \(V_m\) is the proper coherent pushforward theorem. Relative Serre generation makes its evaluation surjective for all sufficiently large \(m\). Taking the maximum of the finitely many integers from the affine cover completes the proof. \(\square\)

The lemma has not assumed that \(V_m\) is locally free. It has also not asserted arbitrary-base commutation for \(f_*E(m)\) when \(E\) is nonflat. The comparison with fields and the evaluation map are what the construction needs.

## 3 Grassmannians of coherent modules are projective

**Lemma 3.1.** For a finite-type quasi-coherent sheaf \(V\) on \(S\), the Grassmannian \(\operatorname{Gr}_r(V)\) of locally free rank-\(r\) quotients has a closed Plücker immersion

\[
\operatorname{Gr}_r(V)\hookrightarrow
\mathbb P_S(\wedge^rV).
\]

In particular, it is projective over \(S\), and the determinant of its universal quotient is relatively very ample.

**Proof.** Representability for quasi-coherent \(V\) was proved in *Grassmannians*. Locally choose a surjection \(\mathcal O^q\to V\). Factoring a locally free quotient of \(\mathcal O^q\) through \(V\) is a closed condition: the relations in the kernel must map to zero in the universal quotient. In quotient-basis charts these are equations in the matrix entries, so \(\operatorname{Gr}_r(V)\) is closed in \(\operatorname{Gr}_r(\mathcal O^q)\).

Taking determinants of the quotient gives a quotient line of \(\wedge^rV\). Thus its Plücker map factors through \(\mathbb P(\wedge^rV)\), a closed subscheme of \(\mathbb P(\wedge^r\mathcal O^q)\). The composite

\[
\operatorname{Gr}_r(V)\longrightarrow
\mathbb P(\wedge^r\mathcal O^q)
\]

is a closed immersion, since both the relation locus and the free-bundle Plücker map are closed immersions. A closed immersion factoring through a closed subscheme is a closed immersion into that subscheme: on an affine chart, the corresponding surjective ring map still factors surjectively through the quotient ring. This proves the claim locally and therefore globally. The pullback of \(\mathcal O(1)\) is the determinant of the universal quotient, by its defining line quotient. Since \(\wedge^rV\) is finite type, this is projectivity in the convention allowing \(\mathbb P\) of a finite-type quasi-coherent sheaf. \(\square\)

For \(r=0\), the Grassmannian is \(S\), \(\wedge^0V=\mathcal O_S\), and the same assertion holds. When a rank is impossible, the scheme is empty.

## 4 The flattening stratum is the Quot scheme

**Theorem 4.1 (Grothendieck).** Under the hypotheses of Lemma 2.1, \(\operatorname{Quot}^{P,L}_{E/X/S}\) is represented by a projective \(S\)-scheme \(Q\). For every sufficiently large \(m\), there is a closed immersion

\[
Q\hookrightarrow\operatorname{Gr}_{P(m)}(f_*E(m))
\hookrightarrow\mathbb P_S\!\left(\wedge^{P(m)}f_*E(m)\right).
\]

If \(\mathcal G\) is its universal quotient and \(p:X_Q\to Q\), the invertible sheaf

\[
\det p_*\mathcal G(m)
\]

is relatively very ample.

**Proof of representability.** Choose \(m\geq m_0\) from Lemma 2.1, set \(V=f_*E(m)\), and put \(r=P(m)\). If this number is negative, no quotient can exist, since it would equal \(h^0(G(m))\); the empty scheme represents the functor. Otherwise let \(H=\operatorname{Gr}_r(V)\). Write its universal sequence as

\[
0\longrightarrow U\longrightarrow V_H
\longrightarrow Q_H\longrightarrow0.
\]

The target \(Q_H\) is locally free. Consequently this sequence remains exact after every base change, even when \(V\) is nonflat. On \(X_H\), compose the inclusion of \(U\) with the evaluation map and untwist:

\[
p_H^*U\otimes L^{-m}\longrightarrow E_H.
\]

Let \(\mathcal F\) be its coherent cokernel. Apply the projective flattening theorem to \(\mathcal F\). Denote its polynomial-\(P\) stratum by \(H_P\), taking it empty if \(P\) does not occur. It is locally closed in \(H\). The flattening theorem applies to \(X_H\) with \(L\) by its local projective-space embeddings; the unique polynomial strata glue over a finite affine cover. On \(H_P\) the quotient \(E\to\mathcal F\) is flat, finitely presented and has polynomial \(P\). Its support is proper, since \(X\) is proper.

For any test quotient \(E_T\to G\) in the functor, proper flat cohomology and the uniform fibre vanishings give a finite locally free sheaf \(p_*G(m)\) of rank \(r\), compatible with arbitrary base change. The natural map

\[
V_T\longrightarrow p_*G(m)
\]

is surjective. On every residue field it is the map \(H^0(E_t(m))\to H^0(G_t(m))\), which is onto because \(H^1(K_t(m))=0\). Its cokernel is finite, so fibrewise surjectivity and Nakayama give surjectivity on \(T\). This defines a map \(T\to H\).

We claim that the candidate cokernel pulled back from \(H\) is exactly \(G\). Let \(W=\ker(V_T\to p_*G(m))\), and let \(K_T=\ker(E_T\to G)\). The evaluation image of \(W\otimes L^{-m}\) is contained in \(K_T\). Since \(G\) is flat over \(T\), tensoring the kernel sequence with a residue field gives the actual kernel \(K_t\) of \(E_t\to G_t\). Since \(p_*G(m)\) is locally free, tensoring the section-quotient sequence identifies \(W_t\) with \(H^0(K_t(m))\). Lemma 2.1 says that these sections generate \(K_t(m)\). The cokernel of evaluation into \(K_T\) is finite locally on \(X_T\) and has zero fibres at every parameter point. Nakayama at each source point makes it zero. Thus evaluation recovers the kernel, and its cokernel is \(G\). This proves that \(T\to H\) factors through \(H_P\).

Here finiteness of \(K_T\) follows from finite presentation of \(G\) and of \(E_T\): locally, lift a finite presentation of \(G\) through the finite module \(E_T\) to obtain finitely many generators of the kernel. We do not need to assume that \(K_T\) is flat or apply a cohomology theorem to it.

Conversely, on \(H_P\) the natural map \(V_{H_P}\to p_*\mathcal F(m)\) is surjective by the same argument. The original \(U\) maps to zero, by the definition of the cokernel. It therefore induces a surjection

\[
Q_H|_{H_P}\longrightarrow p_*\mathcal F(m).
\]

Both sides are locally free of rank \(r\), so this is an isomorphism. The same reasoning applies after any base change. Hence the two operations—taking the quotient of sections and taking the sheaf cokernel—are mutually inverse on every test scheme. This proves that \(H_P\) represents \(\operatorname{Quot}^{P,L}_{E/X/S}\). In particular it is a separated scheme of finite type over \(S\), with a locally closed immersion into \(H\).

**Proof of properness.** Let \(R\) be a discrete valuation ring with fraction field \(K\), and let \(\operatorname{Spec}R\to S\). Given \(E_K\twoheadrightarrow G_K\), let \(j:X_K\hookrightarrow X_R\), and define

\[
G_R=\operatorname{im}(E_R\longrightarrow j_*G_K).
\]

Equivalently, its kernel consists of sections of \(E_R\) whose localization belongs to the generic kernel. Since \(X_R\) is Noetherian, this kernel and its quotient are coherent. The image is torsion-free as an \(R\)-module: multiplication by a nonzero element of \(R\) is invertible on \(j_*G_K\), so it is injective on the image. A torsion-free module over a discrete valuation ring is flat. One proof is that its finitely generated submodules are free, and it is their filtered union. Thus \(G_R\) is flat over \(R\). Its support is closed in the proper scheme \(X_R\), and hence is proper. Its polynomial is constant on the connected base \(\operatorname{Spec}R\) and equals the generic polynomial \(P\).

This gives an extension in the quotient functor. It is unique. Any flat quotient \(E_R\twoheadrightarrow G'_R\) is torsion-free over \(R\) and therefore injects into the localization of its generic fibre. Its kernel is precisely the inverse image in \(E_R\) of the generic kernel; this is the kernel used above. Quotient equivalence is equality of kernels, so the two extensions agree.

The finite-type scheme \(H_P\to S\), with Noetherian base, thus satisfies existence and uniqueness for every discrete valuation ring diagram. The Noetherian valuative criterion [Stacks, Tag 0208] gives properness. Its immersion into \(H\) is proper, since \(H\to S\) is separated: its graph is closed and projection from \(H_P\times_S H\) to \(H\) is proper. A proper locally closed immersion is a closed immersion. For example, factor it into a closed immersion into an open subscheme of \(H\); properness makes its image closed in \(H\), and its closed scheme structure then extends across the complement. Consequently \(H_P\) is closed in the projective Grassmannian.

Finally, the universal Grassmannian quotient restricts to \(p_*\mathcal G(m)\). The Plücker line bundle restricts to its determinant. Lemma 3.1 makes it relatively very ample, completing the theorem. \(\square\)

The proof shows precisely where three different hypotheses enter: regularity gives a uniform twist, projective flattening represents the flat candidate quotients, and Noetherianity permits the discrete-valuation closure argument. A locally closed flattening stratum alone would prove neither properness nor the closed Grassmannian embedding.

**Corollary 4.2.** Every fixed-polynomial Hilbert functor \(\operatorname{Hilb}^{P,L}_{X/S}\) is represented by a projective \(S\)-scheme. The full Hilbert functor is represented by their disjoint union and is locally of finite type.

**Proof.** Apply Theorem 4.1 to \(E=\mathcal O_X\) and use Section 1. The polynomial is locally constant in every Hilbert family, so every map factors locally through the corresponding fixed-polynomial scheme, and these factorizations glue over its open and closed polynomial loci. This is the universal property of the disjoint union. Each piece is finite type. There can be infinitely many pieces: already subschemes of \(\mathbb P^1\) have arbitrary finite lengths. \(\square\)

Flatness of \(X\to S\) is not needed for this corollary. It is the members \(Z\to T\) of the Hilbert functor that must be flat.

### Arbitrary bases and proper algebraic spaces

The Noetherian hypothesis in the construction above can be removed from properness. In the following theorem, a line bundle ample on a morphism of algebraic spaces has its usual meaning: the morphism is representable by schemes, and the bundle is relatively ample after every scheme base change. The base space itself need not be a scheme or Noetherian.

**Theorem 4.3.** Let \(X\to S\) be proper and of finite presentation, let \(E\) be a finitely presented quasi-coherent sheaf, and let \(L\) be ample on \(X/S\). For every numerical polynomial \(P\), the functor \(\operatorname{Quot}^{P,L}_{E/X/S}\) is an algebraic space proper over \(S\). Its formation commutes with every base change. After an étale affine base change on \(S\), it is a projective scheme.

**Proof.** The general Quot space, including its arbitrary-base-change property and separatedness, is [Moduli stacks are algebraic, Theorem 6.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-AS/moduli-stacks-are-algebraic.html#6-quotients-and-closed-subschemes). The Hilbert polynomial of a flat finitely presented quotient with proper support is locally constant. This follows from the finite-projective cohomology complex for its twists: the first \(\dim\mathbf P^N+1\) Euler characteristics determine the polynomial on each projective chart. The fixed-polynomial condition therefore defines an open and closed subspace. We can also obtain that subspace directly from the local construction below, without first assuming its algebraicity.

Pass to an étale affine chart \(\operatorname{Spec}R\to S\). Representability in the ampleness hypothesis makes \(X_R\) a scheme. The [ample embedding theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-AS/moduli-stacks-are-algebraic.html#uncovered-morphisms-lemma-quasi-projective-finite-type-over-s) gives an immersion

\[
i:X_R\longrightarrow\mathbf P^N_R,
\qquad i^*\mathcal O(1)=L^{\otimes d},\quad d>0.
\]

Properness of \(X_R\) makes this a closed immersion: its graph is closed because the target is separated, so the immersion is proper. It is of finite presentation. Indeed both schemes are of finite presentation over \(R\); a map between finitely presented algebras over one ring is finitely presented, by adjoining the finitely many equations for the images of its generators, and the resulting local assertion applies on the standard affine charts.

Changing from \(L\) to \(L^{\otimes d}\) replaces \(P(t)\) by \(Q(t)=P(dt)\). This preserves the functor exactly. On a geometric fibre, if \(R_G(t)\) is the polynomial for \(G\) with respect to \(L\), its polynomial for \(L^{\otimes d}\) is \(R_G(dt)\). Equality \(R_G(dt)=P(dt)\) is equivalent to \(R_G=P\), because substitution by a positive integer is injective on \(\mathbf Q[t]\). This argument concerns integer Euler characteristics and works in every characteristic.

Closed-immersion pushforward gives, on every parameter scheme, a natural identification

\[
\operatorname{Quot}^{P,L}_{E/X_R/R}
\simeq
\operatorname{Quot}^{Q,\mathcal O(1)}_{i_*E/\mathbf P^N_R/R}.
\]

For completeness, the ideal of \(X_R\) annihilates \(i_*E\), and hence annihilates every quotient of it. Such a quotient is uniquely the pushforward of a sheaf on \(X_R\). Its finite presentation, relative flatness and proper support have the same meaning before and after pushforward; this is checked on affine charts of the closed immersion. Conversely pushforward is exact and preserves these properties. Quotient equivalence is equality of kernels, so the two constructions are inverse. They commute with all pullbacks, and the projection formula identifies their Hilbert polynomials. The sheaf \(i_*E\) is finitely presented: on an affine chart, a finite presentation over a finitely presented quotient ring is a finite presentation over the original ring.

Now descend only \(i_*E\) on the fixed projective space. Write \(R\) as the directed union of its finitely generated \(\mathbf Z\)-subalgebras. On the finitely many standard affine charts of \(\mathbf P^N_R\), choose finite module presentations. The overlaps and triple overlaps are principal localizations of those charts. The gluing isomorphisms, their inverses and their cocycle identities are specified by finitely many images of generators and finitely many relations. All coefficients and denominators belong to a common finitely generated subalgebra \(R_0\); enlarge it to a later stage so that all these finitely many identities hold. Thus there is a finitely presented sheaf \(E_0\) on \(\mathbf P^N_{R_0}\) whose pullback is \(i_*E\). This argument does not require the maps \(R_0\to R\) to be flat.

The ring \(R_0\) is Noetherian. Theorem 4.1 constructs the projective scheme

\[
Q_0=\operatorname{Quot}^{Q,\mathcal O(1)}
_{E_0/\mathbf P^N_{R_0}/R_0}.
\]

Its base change to \(R\) represents the required functor on **every** \(R\)-scheme: the pulled-back source sheaves agree, and finite presentation, flatness over the parameter scheme, support and the fibre polynomial are the same conditions. No new uniform regularity estimate over \(R\) is needed. Hence the fixed-polynomial space over our affine chart is projective and in particular proper.

These local identifications agree on overlaps by their common functor, giving the specified subspace of the general Quot space. Properness is étale local on the base. One can see its closedness assertion directly: after any base change, the inverse image of the image of a closed subset is its image after the étale surjective base change, by the residue-field tensor-product argument. That image is closed on the covering, and an étale surjection has the quotient topology. Universal closedness therefore descends; finite type and separatedness descend too. This proves properness over arbitrary \(S\). Finally, restriction of the functor to any new base is exactly the same Quot functor for the pulled-back data, proving the base-change assertion. \(\square\)


## 5 Finite points on affine schemes

For separated \(X\to S\), let \(\operatorname{Hilb}^d_{X/S}\) classify closed subschemes \(Z\subset X_T\) finite locally free of degree \(d\) over \(T\). For projective \(X\), it is the Hilbert functor of constant polynomial \(d\): a proper finitely presented family with zero-dimensional fibres is finite, and its flat finite algebra is locally free of rank \(d\).

**Proposition 5.1.** Suppose \(X\to S\) is separated and of finite presentation, and has the following affine neighbourhood property locally on \(S\): every finite set of points in a fibre is contained in an open \(U\subset X\) affine over that base neighbourhood. Then \(\operatorname{Hilb}^d_{X/S}\) is represented by a scheme. On an affine \(X\) it has explicit affine charts given by commuting matrices with a specified cyclic basis.

**Proof.** First let \(S=\operatorname{Spec}A\) and

\[
X=\operatorname{Spec}C,
\qquad C=A[z_1,\ldots,z_n]/(f_1,\ldots,f_l).
\]

For \(d=0\), the only quotient algebra is zero, and the representing scheme is \(S\). Suppose \(d>0\). A finite-dimensional quotient of this algebra over a field is spanned by monomials of degree at most \(d-1\). Indeed, let \(C_j\) be the subspace spanned by monomials of degree at most \(j\). It begins with dimension one. If \(C_j=C_{j+1}\), multiplication by every generator preserves \(C_j\); since these generators generate the algebra, \(C_j\) is the whole algebra. There can be at most \(d-1\) strict increases before dimension \(d\) is reached.

Choose \(d\) monomials \(m_1=1,m_2,\ldots,m_d\) from this finite set. For any finite locally free quotient \(C_B\twoheadrightarrow D\) of rank \(d\), the condition that their images form a basis is open on \(\operatorname{Spec}B\): it is invertibility of the determinant of the map \(B^d\to D\). These basis opens cover all parameter points by the preceding field argument.

On this basis open, multiplication by \(z_i\) is a \(d\)-by-\(d\) matrix \(Z_i\). The quotient algebra is specified by the equations

\[
\begin{gathered}
[Z_i,Z_j]=0,\qquad f_a(Z_1,\ldots,Z_n)=0,\\
m_j(Z_1,\ldots,Z_n)e_1=e_j.
\end{gathered}
\]

They are finitely many polynomial equations in the matrix entries. Conversely, matrices satisfying these equations give an action of \(C_B\) on \(B^d\), and the map

\[
C_B\longrightarrow B^d,\qquad h\longmapsto h(Z)e_1
\]

is surjective, since it contains every \(e_j\) in its image. Its kernel is an ideal: if \(h(Z)e_1=0\), then \((ah)(Z)e_1=a(Z)h(Z)e_1=0\). The resulting algebra quotient is free with the stated basis, and its multiplication matrices are exactly the original \(Z_i\). Thus the matrix equations represent the basis subfunctor. The ideal is finitely generated as well: monic degree-\(d\) characteristic equations for each \(Z_i\) reduce all monomials to a finite list, whose differences from their expressions in the chosen basis supply finitely many additional relations. Hence the subscheme family is of finite presentation over the base.

On the intersection of two basis opens, the change-of-basis matrix has columns \(m'_j(Z)e_1\). Inverting its determinant gives the open intersection; conjugating the multiplication matrices gives its inverse change of chart. The identities satisfy the cocycle condition because they are ordinary changes of basis of the same algebra. The affine charts therefore glue to a representing scheme for \(X\).

For the general affine neighbourhood property, a finite family \(Z\to T\) is contained in \(U_T\) on an open subset of \(T\): the complement is the image of the closed subset \(Z\cap(X_T\setminus U_T)\) under the finite, hence proper, map \(Z\to T\), and that image is closed. Thus the functors \(\operatorname{Hilb}^d_{U/S}\) are open subfunctors. The stated neighbourhood property makes them cover the whole functor. Their represented intersections and the sheaf property glue the affine constructions by the representable-open gluing theorem from *Representable functors and the functor of points*. This gives the representing scheme. \(\square\)

The affine neighbourhood condition has a specific role: the entire finite support of a fibre must fit into one affine open. Merely knowing that each of its points has an affine neighbourhood would not provide this cover of the Hilbert functor.

**Example 5.2.** If \(X\to S\) is separated, \(\operatorname{Hilb}^1_{X/S}=X\). A finite locally free rank-one algebra over \(T\) is \(\mathcal O_T\): its unit map is an isomorphism on every fibre and hence an isomorphism. Therefore \(Z\to T\) is an isomorphism and its embedding in \(X_T\) is the graph of a map \(T\to X\). Separatedness makes every such graph closed, giving the converse and the functorial identification.

## 6 The two-point affine plane

**Proposition 6.1.** Over any field \(k\), \(\operatorname{Hilb}^2(\mathbb A^2_k)\) is covered by two affine four-spaces and is smooth of dimension four.

**Proof.** In a length-two algebra generated by \(x,y\), at least one of \(1,x\) or \(1,y\) is a basis. Otherwise both generators would lie in the scalar subspace, and the algebra they generate would have dimension one. The corresponding basis opens therefore cover the Hilbert scheme.

On the \(1,x\) chart, every quotient has unique equations

\[
x^2=a+bx,\qquad y=c+dx.
\]

Conversely, these equations give the free algebra \(B[x]/(x^2-bx-a)\), with \(y\) acting as \(c+dx\), over every parameter algebra \(B\). Thus this chart is \(\mathbb A^4\) with coordinates \(a,b,c,d\), with no additional relations. On the \(1,y\) chart write

\[
y^2=a'+b'y,\qquad x=c'+d'y.
\]

The overlap of the charts is \(d\ne0\). Substituting \(x=(y-c)/d\) and expanding gives

\[
\begin{gathered}
a'=d^2a-c^2-bcd,\\
b'=2c+bd,\qquad c'=-c/d,\qquad d'=1/d.
\end{gathered}
\]

These changes are inverse to the analogous changes with primed variables. They are valid in every characteristic, including characteristic two. Both charts are smooth affine four-spaces, so the glued scheme is smooth of dimension four. \(\square\)

At a double point the parameter \(d\) records a tangent direction of finite slope. The other chart records the missing vertical direction. The collision is therefore a point of a projective line of possible tangent directions, rather than a single undifferentiated diagonal point.

## 7 A smooth curve: unordered divisors are the Hilbert scheme

### Affine neighbourhoods on regular curves

**Lemma 7.A.** Let \(C\) be a separated regular finite-type curve over a field, with every component of dimension one. Every finite set of its points has an affine open neighbourhood. An integral such curve is affine or projective. Removing a closed point from an integral regular projective curve gives an affine scheme. Every nonempty component has infinitely many closed points.

**Proof.** First suppose that \(C\) is integral. Apply [Chow’s lemma, Theorem 4.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-MO/projective-morphisms-and-chows-lemma.html#4-chow-s-lemma-over-a-noetherian-base), over the field, and take the reduced closure of the inverse image of its dense isomorphism open. This gives a proper birational map \(Z\to C\), where \(Z\) is an integral quasi-projective curve. A fibre over a closed point is a proper closed subset of this one-dimensional integral scheme, hence is zero-dimensional. The generic fibre is a point, since the map is an isomorphism on a dense open. The map is finite by [Zariski’s main theorem, Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-MO/zariskis-main-theorem.html#5-properness-and-normality). A finite birational map to a normal integral scheme is an isomorphism: over an affine open \(\operatorname{Spec}A\) of the target, its finite coordinate algebra is an integral \(A\)-subalgebra of \(\operatorname{Frac}A\), and integral closedness makes it exactly \(A\). Regularity implies normality. Thus \(C\) is quasi-projective.

It follows already that finite sets have affine neighbourhoods. Restrict a projective hyperplane bundle to \(C\), and apply [Effective Cartier divisors and invertible sheaves, Lemma 5.2a](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-MO/effective-cartier-divisors-and-invertible-sheaves.html#5-associated-points-and-effective-representatives). Its homogeneous prime-avoidance proof produces an affine section open containing the specified points, including over finite fields.

We also prove the affine-or-projective assertion used below. Take the reduced projective closure \(B\) of \(C\) in a projective embedding. If its boundary is empty, \(C=B\) is projective. Otherwise normalize \(B\). The normalization \(\overline C\to B\) is finite by [Normalization, Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-MO/normalization.html#5-finiteness-over-fields-including-inseparability), hence proper, and is an isomorphism over the normal open \(C\). The normal one-dimensional Noetherian scheme \(\overline C\) is regular. Its boundary is a nonempty finite set of closed points. Let \(D\) be their sum as an effective Cartier divisor.

Assume first that the ground field is infinite. For each boundary point \(q\), the inclusions
\[
\mathcal O((n-1)D)\subset\mathcal O(nD-q)
\subset\mathcal O(nD)
\]
have cokernels with finite support. Their induced maps on \(H^1\) are surjective, since such cokernels have zero higher cohomology. These \(H^1\) spaces are finite-dimensional by [Proper morphisms and coherent direct images, Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-QC/proper-morphisms-and-coherent-direct-images.html#5-finite-cohomology-and-global-functions). The nonincreasing sequence \(h^1(\mathcal O(nD))\) therefore stabilizes. For every sufficiently large \(n\), the two displayed maps on \(H^1\) have equal endpoint dimensions, so both are isomorphisms. The exact sequence for the last inclusion then makes
\[
H^0(\mathcal O(nD))\longrightarrow
H^0(\mathcal O(nD)|_q)
\]
surjective. Consequently the sections whose pole order at \(q\) is less than \(n\) form a proper linear subspace. Avoid these finitely many proper subspaces over the infinite field. The resulting rational function \(f\) has poles at every boundary point and nowhere else.

A rational function on a regular curve defines a morphism to \(\mathbb P^1\): at each DVR local ring, either \(f\) or \(f^{-1}\) is regular, and these two chart definitions agree. Here the map \(\overline C\to\mathbb P^1\) is nonconstant, proper, and has finite fibres, so it is finite. Its inverse image of the affine line is precisely \(\overline C\setminus D=C\), which is affine. This same construction with \(D=q\) proves that removing any closed point of a regular projective integral curve gives an affine scheme.

If the ground field is finite, it is perfect, so the regular curve \(\overline C\) is smooth over it; [Smooth morphisms, Section 2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-FSE/smooth-morphisms.html#2-over-a-field-regularity-must-be-geometric) proves this field criterion. After extension to an algebraic closure, its components are regular, and the nonempty boundary meets each of them. Indeed flat field extension makes each minimal prime contract to the generic point, while the algebraic field extension is integral and hence has closed image; each geometric component therefore maps onto the original integral curve. Apply the infinite-field argument on each component. The resulting complement is affine, and affineness descends along the faithfully flat field extension by [Descending properties of schemes and morphisms, Theorem 2.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-DFG/AG-DFG-03.html#2-checking-a-morphism-on-an-fpqc-covering-of-its-target). The removal assertion descends in the same way.

Finally, regular components of \(C\) are pairwise disjoint: a regular local ring is a domain, so two components cannot meet. There are finitely many components, each open and closed. Taking the finite disjoint union of the affine neighbourhoods constructed on the components proves the general finite-set assertion. To see that an integral component has infinitely many closed points, choose a nonempty affine open and apply Noether normalization to obtain a finite surjection onto \(\mathbb A^1\). The latter has infinitely many closed points: over an infinite field the linear polynomials suffice, and over a finite field the usual product-plus-one argument gives infinitely many monic irreducible polynomials. Lying over supplies a distinct closed point above each of them. \(\square\)

### Equations in flat families

**Lemma 7.B (the fibrewise Cartier criterion).** Let \(Y\to T\) be flat and locally of finite presentation.

1. If a local equation \(f\) is a nonzerodivisor in the fibre local ring at a point, then, near that point, it defines an effective Cartier divisor flat and locally of finite presentation over \(T\).
2. Let \(D\subset Y\) be a closed subscheme flat and locally of finite presentation over \(T\). Then \(D\) is a relative effective Cartier divisor exactly when every geometric fibre \(D_t\subset Y_t\) is an effective Cartier divisor. Its relative Cartier locus is open.
3. These divisor conditions persist after every change of base.

The equation may be a unit, giving the empty divisor. No Noetherian hypothesis on \(T\) is imposed.

**Proof.** We first prove the local equation assertion. Write the local base ring as \((A,\mathfrak m)\) and the local source ring as \(B\). Thus \(B\) is \(A\)-flat and essentially of finite presentation. Suppose first that \(A,B\) are Noetherian. If \(fx=0\), injectivity of \(\bar f\) on \(B/\mathfrak mB\) puts \(x\) in \(\mathfrak mB\). Flatness identifies
\[
\mathfrak m^jB/\mathfrak m^{j+1}B
=(\mathfrak m^j/\mathfrak m^{j+1})
 \otimes_{A/\mathfrak m}(B/\mathfrak mB).
\]
These are direct sums of copies of the fibre ring, so \(\bar f\) acts injectively on each of them. Induction puts \(x\) in every \(\mathfrak m^jB\). Their intersection is zero by [Noetherian and Artinian rings, Theorem 6.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/noetherian-and-artinian-rings.html#6-what-can-survive-every-power). Hence \(f\) is a nonzerodivisor on \(B\).

The sequence \(0\to B\xrightarrow{f}B\to B/(f)\to0\), with \(B\) flat over \(A\), gives
\[
\begin{gathered}
\operatorname{Tor}_1^A(A/\mathfrak m,B/(f))
\\
=\ker(\bar f:B/\mathfrak mB\to B/\mathfrak mB)=0.
\end{gathered}
\]
The residue-field local flatness criterion, proved in [Flatness criteria, Theorem 1.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-FSE/flatness-criteria.html#1-testing-a-quotient-by-an-ideal), now makes \(B/(f)\) flat over \(A\). Its reduction is a module over a field and is automatically flat, so all conditions of that criterion hold.

For an arbitrary \(A\), include \(f\) and a finite presentation of the local algebra in the models of [Flatness criteria, Lemma 6.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-FSE/flatness-criteria.html#6-finite-presentations-over-an-arbitrary-base). Since \(B\) is \(A\)-flat, some Noetherian local model \(A_\lambda\to B_\lambda\) is flat, and we may retain a representative \(f_\lambda\). Its local fibre maps faithfully flatly to the original local fibre: this is extension of the residue field followed by localization, and the map is local. Injectivity of \(\bar f\) therefore descends to injectivity of \(\bar f_\lambda\). The Noetherian argument gives a regular \(f_\lambda\) and an \(A_\lambda\)-flat quotient.

Flatness of this quotient makes its equation sequence remain exact after tensoring with any \(A_\lambda\)-algebra. Base change to \(A\) and localization consequently give regularity of \(f\), flatness of \(B/(f)\), and exactness after every further base change. To obtain a neighbourhood rather than only a local statement, use a finite-presentation model before the localizations. Over its Noetherian base, the coherent kernel of multiplication and the flat locus of the quotient are open conditions at the chosen point; [Flatness criteria, Theorem 5.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-FSE/flatness-criteria.html#5-the-flat-locus-over-a-noetherian-base) proves the latter. Shrink to that open and pull it back. This proves part 1, including its neighbourhood and arbitrary-base assertions.

For part 2, work locally with \(D=\operatorname{Spec}(B/I)\). Finite presentation of \(D\) and \(Y\) over the base makes \(I\) finitely generated: finite presentations for the two algebras give a finite presentation of the quotient as a \(B\)-algebra. Flatness of \(B/I\) identifies \(I\otimes_A\kappa(t)\) with the ideal of \(D_t\) in \(Y_t\). If that ideal is generated by a regular \(\bar f\), choose a lift \(f\in I\). Nakayama applied to the finite \(B\)-module \(I/(f)\) gives \(I=(f)\) in the local ring, hence on a neighbourhood by finite generation. Part 1 makes this equation regular and the divisor flat there. A geometric fibre condition descends to the residue field by faithful flatness, so geometric fibres suffice.

Conversely, for a regular equation whose quotient is base-flat, tensoring the equation sequence with a residue field preserves its injectivity. It therefore gives an effective Cartier divisor on every fibre. The neighbourhood construction in part 1 and the finite-generation argument just given also prove openness of the relative Cartier locus.

Finally, tensoring that equation sequence with an arbitrary base algebra stays exact, since its quotient is base-flat. The pulled-back equation is regular, and its quotient remains flat and finitely presented. This proves part 3. \(\square\)

**Theorem 7.1.** Let \(C\) be a smooth separated curve of finite type over a field \(k\), with all components of dimension one. Then

\[
\operatorname{Hilb}^d(C)\simeq\operatorname{Sym}^d(C)=C^d/\mathfrak S_d.
\]

This is an isomorphism of schemes, in every characteristic. Both schemes are smooth of dimension \(d\), component by component.

**Proof.** We give the scheme-theoretic argument, since a bijection of divisors over algebraically closed fields would not prove the theorem.

First, the required schemes exist and are finite type. Lemma 7.A proves that a regular irreducible curve is either affine or projective, that removing a closed point from a regular projective curve gives an affine open, and that every component has infinitely many closed points [Stacks, Tag 0A27]. Every finite set of points therefore has a common affine neighbourhood. There is even a finite cover sufficient for the length-\(d\) Hilbert functor: on a projective component choose \(d+1\) distinct closed points \(q_j\); any support of at most \(d\) points misses one of them and is contained in \(C\setminus\{q_j\}\). There are infinitely many closed points on a curve, so such a choice is possible. Smooth components are disjoint, and there are only finitely many of them; take the finitely many corresponding combinations of affine opens. Proposition 5.1 then gives a finite-type Hilbert scheme.

For the symmetric quotient, the invariant opens \(U^d\), with \(U\) a common affine neighbourhood of a finite set of points of \(C\), cover \(C^d\). On \(U^d=\operatorname{Spec}B\), use \(\operatorname{Spec}B^{\mathfrak S_d}\). Every element \(b\in B\) is integral over the invariant ring, since it satisfies \(\prod_\sigma(T-\sigma b)\). Finite generation of \(B\) makes this a finite ring extension; the invariant ring is finitely generated over \(k\) by the finite-extension algebra lemma proved in Section 9. Its geometric fibres are the finite orbits: invariant functions separate distinct finite orbits, by multiplying suitable separating functions and their translates. Images of invariant open subsets are open, because the finite quotient is closed and the complement is invariant. These affine quotients therefore glue, with their usual categorical universal property for invariant maps to schemes. This constructs \(\operatorname{Sym}^d C\).

Over \(C^d\), sum the \(d\) graph divisors in \(C\times C^d\). A graph of a section of a smooth relative curve is Cartier; locally its equation is a relative parameter. The sum is defined by the product of the graph ideals. On a geometric fibre it is the divisor consisting of the chosen points with their multiplicities. It is a relative effective Cartier divisor: the product remains a nonzerodivisor on every curve fibre, and the fibrewise Cartier criterion of Lemma 7.B [Stacks, Tag 062Y] gives flatness. Its support is a finite union of graphs; hence the divisor is proper with finite fibres, and is finite locally free of degree \(d\). It defines an invariant map \(C^d\to\operatorname{Hilb}^d C\), and the categorical quotient gives

\[
a:\operatorname{Sym}^d C\longrightarrow\operatorname{Hilb}^d C.
\]

After an algebraic closure of \(k\), every ideal of finite colength in the local ring of a smooth curve is a power of its maximal ideal, since that ring is a discrete valuation ring. Thus \(a\) is bijective on geometric points. We now compare completed local rings to check the infinitesimal structure.

Let \(D=\sum_i d_i p_i\) be such a divisor over an algebraically closed field. Choose formal parameters \(u_i\) at the distinct points \(p_i\), so their completed local rings are \(k[[u_i]]\). For a local Artinian \(k\)-algebra \(R\) with residue field \(k\), a finite flat embedded deformation of \(D\) splits uniquely into its clusters at the \(p_i\). This follows from lifting the idempotents of its special-fibre algebra through the nilpotent maximal ideal of \(R\). Each cluster is a free \(R\)-algebra of rank \(d_i\), a quotient of \(R[[u_i]]\).

Modulo the maximal ideal its basis is \(1,u_i,\ldots,u_i^{d_i-1}\). Nakayama and the rank show that these elements remain a basis over \(R\). There is therefore a unique relation

\[
u_i^{d_i}+a_{i,1}u_i^{d_i-1}+\cdots+a_{i,d_i}=0,
\qquad a_{i,j}\in\mathfrak m_R.
\]

Conversely every such monic relation defines a free rank-\(d_i\) quotient. The passage from polynomials to formal series is harmless: if \(\mathfrak m_R^N=0\), the relation makes \(u_i^{d_iN}=0\), so all series evaluate as finite polynomials. The polynomial quotient and the formal-series quotient are mutually inverse under this evaluation. The completed local ring of the Hilbert scheme at \(D\) is consequently

\[
k[[a_{i,j}\mid 1\leq j\leq d_i]].
\]

On the symmetric quotient, take an ordered tuple representing \(D\). Its stabilizer is \(\prod_i\mathfrak S_{d_i}\). Completion of the invariant affine quotient ring is the invariants of the product of completed local rings at its orbit: the coordinate ring upstairs is finite over the invariant ring, completion is flat over that invariant ring, and invariants are the kernel of the finite list of maps \(b\mapsto\sigma b-b\). Flat completion preserves this kernel. The group permutes the orbit factors transitively, leaving the invariants of one factor under its stabilizer. This gives

\[
\begin{gathered}
\widehat{\mathcal O}_{\operatorname{Sym}^d C,D}\\
=k[[u_{i,1},\ldots,u_{i,d_i}]]^{\prod_i\mathfrak S_{d_i}}\\
=k[[e_{i,1},\ldots,e_{i,d_i}]],
\end{gathered}
\]

where \(e_{i,j}\) is the \(j\)-th elementary symmetric polynomial in the \(i\)-th cluster. The final equality holds in every characteristic: apply the fundamental theorem of symmetric polynomials to each homogeneous degree of a symmetric series and pass to completion. Its weighted-degree topology agrees with the power-series topology, since all the weights \(j\) are positive. No averaging by the order of the group is used.

The sum-divisor morphism \(a\) takes \(a_{i,j}\) to \((-1)^j e_{i,j}\), by expanding \(\prod_l(u_i-u_{i,l})\). It is therefore an isomorphism of these completed local rings. This completed-local-ring isomorphism makes \(a\) étale at each closed point. Here are the local steps. Write the local map as \(A\to B\), with the same algebraically closed residue field. The completion \(\widehat B\simeq\widehat A\) is \(A\)-flat, and \(B\to\widehat B\) is faithfully flat by [Completion, Theorem 3.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/completion.html#3-noetherian-exactness-tensoring-and-flatness). Flatness therefore descends to \(B\) over \(A\). The isomorphism on completions identifies cotangent spaces, so
\[
\mathfrak m_B/(\mathfrak m_AB+\mathfrak m_B^2)=0.
\]
This is the residue-field fibre of the finite module \(\Omega_{B/A}\), since the residue fields are equal. Nakayama gives \(\Omega_{B/A}=0\). The flat, finitely presented, unramified criterion in [Étale morphisms and their local structure, Lemma 1.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-FSE/etale-morphisms-and-their-local-structure.html#1-a-definition-and-its-geometric-tests) proves étaleness. The non-étale locus is closed and, if nonempty, has a closed point, so \(a\) is étale everywhere. By [Étale morphisms and their local structure, Theorem 4.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-FSE/etale-morphisms-and-their-local-structure.html#4-the-topology-and-the-open-immersion-criterion), an étale morphism injective on geometric points is a universally injective open immersion; since it is also surjective on geometric points, it is an isomorphism. These are the standard étale and completion criteria recalled among the prerequisites below.

Finally, this argument after an algebraic closure descends by faithful flatness. The symmetric quotient commutes with a field extension because invariants are the same kernel construction and field extension is flat; the Hilbert scheme commutes with it by its functorial definition. Hence the isomorphism holds over the original field. The displayed completed local rings are power-series rings in \(\sum_i d_i=d\) variables, proving smoothness of the symmetric product and Hilbert scheme. \(\square\)

For \(d=2\) on \(\mathbb A^1\), this says that the unordered pair of roots is recorded by the coefficients of \(u^2+a_1u+a_2\). A double root is an ordinary point of the same affine plane of coefficients. On a general smooth curve, the completed local calculation is exactly the same around a double point.

## 8 Hypersurfaces and their projective parameter space

Use the quotient convention \(\mathbb P(V)=\operatorname{Proj}\operatorname{Sym}V\), so \(H^0(\mathbb P(V),\mathcal O(d))=\operatorname{Sym}^dV\). An equation up to nonzero scalar is a line subspace of this space, and is thus a point of its dual projective space.

**Proposition 8.1.** Let \(\dim V=n+1\), \(n\geq1\), and \(d\geq1\). Put

\[
P_d(t)=\binom{t+n}{n}-\binom{t-d+n}{n}.
\]

Then the Hilbert scheme of polynomial \(P_d\) on \(\mathbb P(V)\) is

\[
\mathbb P((\operatorname{Sym}^dV)^\vee).
\]

It classifies degree-\(d\) hypersurfaces, including singular and nonreduced ones, with its universal equation.

**Proof.** First show that every field-valued subscheme with this polynomial is a hypersurface; this also rules out additional subschemes with the same polynomial. Its ideal \(I\subset\mathcal O\) is torsion-free of rank one: \(P_d\) has degree \(n-1\), so the subscheme is not the entire projective space. Its double dual is invertible. Here is an elementary verification on a standard affine chart, whose ring \(A\) is a unique factorization domain. Write the ideal as \(gJ\), where \(g\) is the greatest common divisor of its finite set of generators. The generators of \(J\) have no common prime factor. A homomorphism \(J\to A\) is multiplication by an element \(q\) of the fraction field. If \(qJ\subset A\), every prime in the denominator of \(q\) would divide every generator of \(J\); thus \(q\in A\). It follows that \(J^*=A\), \(J^{**}=A\), and \(I^{**}=gA\). These local double duals glue to an invertible sheaf \(I^{**}=\mathcal O(-e)\), using \(\operatorname{Pic}(\mathbb P^n)=\mathbb Z\), [Stacks, Tag 0BXJ, with \(n\geq1\)]. The quotient \(I^{**}/I\) is supported in codimension at least two, since over a codimension-one discrete valuation ring the ideal is already free of rank one.

For \(n\geq2\), comparing the coefficient of \(t^{n-1}\) in \(P_I=P_{\mathcal O}-P_d\) and in \(P_{\mathcal O(-e)}\) gives \(e=d\): their difference has degree at most \(n-2\). For \(n=1\), the ideal is already invertible and its polynomial directly gives \(e=d\). Thus

\[
P_{I^{**}/I}=P_{\mathcal O(-d)}-P_I=0.
\]

A nonzero coherent sheaf on projective space has a Hilbert polynomial with positive leading coefficient, as proved in the regularity lesson, so this quotient is zero. Hence \(I=\mathcal O(-d)\), embedded by a nonzero degree-\(d\) equation.

Now take any Hilbert family \(Z\subset\mathbb P(V)_T\) of this polynomial. Its fibres are Cartier divisors by the field argument. Since \(Z\to T\) is flat and finitely presented and projective space is flat and finitely presented, the fibrewise Cartier criterion of Lemma 7.B [Stacks, Tag 062Y] makes \(Z\) a relative effective Cartier divisor. Its ideal \(I\) is invertible and flat over \(T\), with \(I(d)_t=\mathcal O\) on every fibre. Proper flat cohomology gives

\[
N=p_*I(d)
\]

locally free of rank one, compatible with base change. The evaluation \(p^*N\to I(d)\) is an isomorphism: it is so on every fibre, hence is surjective by Nakayama, and a surjection between invertible sheaves is an isomorphism. Pushing its inclusion in \(\mathcal O(d)\) to the base gives

\[
N\hookrightarrow\operatorname{Sym}^dV\otimes\mathcal O_T.
\]

This is a line subbundle. Its fibre is the nonzero equation line, so locally one coefficient is a unit and the inclusion splits with locally free cokernel. It is therefore exactly a \(T\)-point of \(\mathbb P((\operatorname{Sym}^dV)^\vee)\).

Conversely, a line subbundle \(N\) in this vector bundle evaluates as \(p^*N\otimes\mathcal O(-d)\to\mathcal O\). On every field fibre it is a nonzero equation in a polynomial ring, and hence a nonzerodivisor. Its zero scheme is locally principal with Cartier fibres, so Lemma 7.B gives a relative effective Cartier divisor flat over \(T\). Its ideal sequence yields polynomial \(P_d\). The two constructions are inverse, including on arbitrary nonreduced test schemes, proving the proposition. \(\square\)

This parameter space is all hypersurfaces, not just the smooth locus. Smooth hypersurfaces form an open subfunctor inside it. The use of the dual in the parameter space is forced by the quotient convention: equations are sublines of the space of sections.

## 9 Two points on a smooth surface

The exceptional divisor of a blow-up records the extra information needed when two points meet: a tangent direction. This statement includes the scheme structure of the parameter space, and remains valid in characteristic two.

### A finite-extension algebra lemma

We will need the finite-extension form of Artin–Tate, also used for the symmetric products in Section 7. Suppose that

\[
k\subset C\subset A,
\]

where $A$ is a finitely generated $k$-algebra and is finite as a $C$-module. Then $C$ is a finitely generated $k$-algebra. Here is the proof. Choose algebra generators $x_i$ of $A$ over $k$ and module generators $a_j$ over $C$, including $1$. Express every $x_i$ as a $C$-linear combination of the $a_j$, and do the same for every product $a_ja_l$. Let $C_0$ be the $k$-algebra generated by all the finitely many coefficients in these expressions. The $C_0$-span of the $a_j$ is a subring of $A$ containing $1$ and all $x_i$; hence it equals $A$. Thus $A$ is finite over $C_0$. The [Hilbert basis theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/noetherian-and-artinian-rings.html#2-polynomial-rings-and-finite-geometric-descriptions) makes $C_0$ Noetherian. Its submodule $C\subset A$ is consequently finite over $C_0$, and is therefore a finitely generated $k$-algebra. No assumption that arbitrary subrings of Noetherian rings are Noetherian has entered the argument.

### The quotient of a finite group action

The surface need not have a common affine neighbourhood of every finite set. The following theorem constructs the quotient in that case too.

**Theorem (finite group quotients).** Let a finite abstract group $\Gamma$ act on a separated finite-type $k$-scheme $U$. There is a separated finite-type algebraic space $Q$ and a finite surjective invariant morphism

\[
\pi:U\longrightarrow Q
\]

with the following properties. For every algebraically closed extension $\Omega/k$, its geometric fibres are exactly the $\Gamma$-orbits. For every algebraic space $E/k$, composition gives a bijection

\[
\operatorname{Hom}_k(Q,E)
\xrightarrow{\sim}
\operatorname{Hom}_k(U,E)^\Gamma.
\]

On the étale site of $Q$, its functions are the invariant functions upstairs:

\[
\mathcal O_Q\simeq(\pi_*\mathcal O_U)^\Gamma.
\]

The orbit, categorical and invariant-function properties remain true after every flat algebraic-space base change on $Q$. There is no restriction on the characteristic or on stabilizers.

**Proof.** For $U$ empty take $Q$ empty. Otherwise regard $\Gamma$ as the constant finite étale $k$-group scheme and form the algebraic stack

\[
\mathcal X=[U/\Gamma].
\]

The construction and its torsor description are proved in [Quotient stacks and Deligne–Mumford stacks, Section 3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-AS/quotient-and-dm-stacks.html#3-classifying-stacks-and-quotient-stacks). The atlas $U\to\mathcal X$ is a finite étale surjection: its pullback along an object over $T$ is that object's $\Gamma$-torsor. This remains true when the action on $U$ has fixed points.

The inertia is finite. On this atlas it is the disjoint union, indexed by $\gamma\in\Gamma$, of the fixed subschemes $U^\gamma$. Each is closed in $U$, since it is the inverse image of the closed diagonal of the separated scheme $U$ under $(1,\gamma)$. Thus the pulled-back inertia is finite over $U$, and finiteness descends through the atlas.

Apply [the finite-inertia coarse-space construction, Theorem 6.9](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-AS/quotient-and-dm-stacks.html#6-1-finite-inertia-and-the-coarse-space). It gives an algebraic space $Q$ and a separated, quasi-compact universal homeomorphism

\[
f:\mathcal X\longrightarrow Q
\]

which is categorical for algebraic-space targets and remains so after flat base change on $Q$. That proof constructs affine invariant charts, descends étale charts preserving the entire stabilizer, and glues their étale equivalence relation. The finite-part step used there has its scheme proof in Affine descent, Zariski Main and recognition of spaces, Proposition D3.3 and Lemma E4.3, including the complete finite pieces over an elementary étale neighbourhood. Thus the construction applies without invariant affine neighbourhoods in $U$.

Let $\pi$ be the composite of the atlas with $f$. Its geometric fibres are single $\Gamma$-orbits: over an algebraically closed field every finite constant-group torsor is trivial, and the coarse-space theorem identifies isomorphism classes with points. The same theorem gives the categorical assertion. More explicitly, an invariant map $U\to E$ descends along the torsor in each object of $[U/\Gamma]$, since maps to an algebraic space form a sheaf. It therefore gives a map $\mathcal X\to E$. Conversely every such map restricts to an invariant map. The two constructions are inverse on all parameter schemes, so initiality of $f$ proves the displayed bijection.

We prove that $\pi$ is finite. Its composite description makes it quasi-compact and universally closed: the atlas is finite, and $f$ is a quasi-compact universal homeomorphism. It is separated because its diagonal is the pullback of the closed diagonal of $U/k$.

It is also locally of finite type. To check this, choose an étale scheme chart $V\to Q$. The scheme $U\times_QV$ is étale over $U$, hence locally of finite type over $k$. On an affine open of this fibre product mapping into an affine open of $V$, its finitely many algebra generators over $k$ also generate over the coordinate algebra of that target open. This proves local finite type over $V$. Together with quasi-compactness it proves finite type of $\pi$.

The properties just proved make $\pi$ proper. Every geometric fibre has finitely many geometric points. On affine étale tests of $Q$, the finite-fibre form of [Zariski's Main Theorem, Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-MO/zariskis-main-theorem.html#5-properness-and-normality), therefore makes it finite. Finiteness descends from those tests, proving the assertion.

The invariant-function assertion can be proved before imposing any finite-type or separation condition on $Q$. For an étale scheme $V\to Q$, the base-changed stack has categorical quotient $V$, by the flat base-change property of $f$. Invariant regular functions on $U\times_QV$ are maps to $\mathbb A^1_k$ which descend to that stack. Categorical initiality identifies them uniquely with maps $V\to\mathbb A^1_k$, that is, regular functions on $V$. This identification commutes with restrictions. Hence it gives the displayed sheaf isomorphism, including all nilpotent functions.

Finite type of $Q/k$ now follows on affine étale charts. Over $V=\operatorname{Spec}C$, the inverse image is affine, say $\operatorname{Spec}A$, because $\pi$ is finite. It is quasi-compact and étale over $U$, so $A$ is finitely generated over $k$. The invariant-function assertion injects $C$ into $A$. The finite-extension algebra lemma makes $C$ finitely generated over $k$. Thus $Q$ is locally of finite type; surjectivity of the quasi-compact scheme $U$ makes $Q$ quasi-compact, and therefore finite type over $k$.

Finally we prove separatedness of $Q$. Put $D=U\times_QU$. Its first projection to $U$ is finite. The map

\[
D\longrightarrow U\times_kU
\]

is finite as well: factor it as the graph of its second projection, which is closed since $U/k$ is separated, followed by the base change of the finite first projection. It is the pullback of $\Delta_{Q/k}$ by the finite surjection $\pi\times\pi$.

After any affine scheme test $T\to Q\times_kQ$, the pullback of that finite surjection is finite and surjective over $T$. The inverse image of the tested diagonal is finite over $T$. It surjects finitely onto the tested diagonal itself. Consequently this diagonal is quasi-compact and universally closed over $T$: to test a closed subset after any further base change, pull it back through the finite surjection and use closedness of the composite finite map. The diagonal is locally of finite type, as is the diagonal of a locally finite-type algebraic space over a field, and is a separated monomorphism. It is therefore proper and quasi-finite on these scheme tests. The same proper quasi-finite theorem makes it finite. A finite monomorphism is a closed immersion: its finite residue algebra has dimension $d$ satisfying $d^2=d$, and Nakayama makes the ring map surjective. Thus $\Delta_{Q/k}$ is a closed immersion and $Q/k$ is separated.

The flat base-change assertions follow from the coarse-space theorem and the same function argument. Finiteness itself survives every base change, as do the orbit description and universal closedness. The invariant-function and categorical assertions use flatness. No averaging operator or division by $|\Gamma|$ has been used. $\square$

### Blow-up coordinates and the Hilbert family

**Proposition 9.1.** Let \(S\) be a smooth separated surface of finite type over a field \(k\). Let

\[
B=\operatorname{Bl}_{\Delta}(S\times_k S).
\]

The involution exchanging the two factors lifts to \(B\), and

\[
B/\mathfrak S_2\simeq\operatorname{Hilb}^2_S.
\]

The quotient is the geometric categorical quotient, rather than the quotient stack. In general the statement is in algebraic spaces. If \(S\) satisfies the affine-neighbourhood condition of Section 5, both sides are schemes. In particular this holds for a quasi-projective surface. The Hilbert space is smooth of dimension four.

**Proof.** The diagonal ideal is invariant under exchange, so its Rees algebra and its Proj inherit the involution. Over the complement of the exceptional divisor there is a family consisting of the two distinct points. Define \(Z\subset S\times B\) as the schematic closure of this family. It is contained in the union of the two graphs of \(B\to S\). Consequently \(Z\to B\) is proper and has finite fibres, hence is finite. We will show that it is flat of degree two.

The calculation can be made after passing to an algebraic closure of the ground field. At a point of the exceptional divisor above \(p\in S\), choose formal smooth coordinates \(x,y\) at \(p\). In the blow-up chart where the difference of the \(x\)-coordinates supplies the direction, put

\[
h=x_2-x_1,\qquad y_2-y_1=dh.
\]

At a direction of slope \(\lambda\), the completed local ring of \(B\) is

\[
R=k[[x_1,y_1,h,d-\lambda]],
\]

with the coordinates translated so that \(p=(0,0)\). On the target surface put \(X=x-x_1\), \(Y=y-y_1\). The completed ideal of the family is

\[
(Y-dX,\ X(X-h)).                                      \tag{9.1}
\]

Indeed, after inverting \(h\) it is the ideal of the two graphs. Its quotient is free over \(R\), with basis \(1,X\), so multiplication by \(h\) is injective. It is therefore already \(h\)-saturated and is exactly the schematic closure. Flat completion preserves the kernel defining this closure. The other blow-up chart gives the same calculation with \(x,y\) exchanged. Away from the exceptional divisor the two graphs are disjoint. Faithful flatness of local completion now proves that the finite module defining \(Z\) is locally free of rank two everywhere. Thus \(Z\) gives an invariant morphism

\[
B\longrightarrow\operatorname{Hilb}^2_S.
\]

Apply the finite-group quotient theorem above to the separated finite-type scheme \(B\). It gives the geometric categorical quotient \(Q=B/\mathfrak S_2\) as a separated finite-type algebraic space and a finite surjection \(B\to Q\), in every characteristic. Algebraicity of the Hilbert functor is proved in [Moduli stacks are algebraic, Corollary 6.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-AS/moduli-stacks-are-algebraic.html#6-quotients-and-closed-subschemes). For a quasi-projective surface the quotient also has the invariant-affine construction of Section 7. Categorical initiality for algebraic-space targets descends the invariant Hilbert morphism to \(q:Q\to\operatorname{Hilb}^2_S\).

We identify its completed local rings explicitly. In the affine-plane blow-up chart set

\[
c=y_1-dx_1,\qquad x_2=x_1+h.
\]

The chart ring is \(k[c,d,x_1,x_2]\). The involution fixes \(c,d\) and exchanges \(x_1,x_2\). Hence its invariant ring is

\[
k[c,d,b,a],\qquad b=x_1+x_2,\quad a=-x_1x_2.
\]

The family (9.1), expressed in \(x,y\), has equations

\[
x^2=a+bx,\qquad y=c+dx.
\]

This is precisely the first chart of Proposition 6.1. The other blow-up chart gives its second chart, with the same transition formulas. The symmetric-polynomial calculation does not divide by two.

For an arbitrary smooth surface, the completed calculation is identical: smooth coordinates identify the completion with the completed affine-plane calculation. Completion of the finite quotient takes invariants of the product of the local completions over an orbit. This follows by expressing invariants as a kernel and using the flatness of completion over the invariant ring, as in Section 7. Thus \(q\) induces an isomorphism of completed local rings at every double-point family. It also does so at every pair of distinct points: the two orders form one free orbit, and the local family is the product of the two independent point neighbourhoods.

There is exactly one geometric point of \(Q\) over each length-two subscheme. A subscheme supported at two points is their unordered pair. A subscheme supported at one point has local algebra \(k[\epsilon]/(\epsilon^2)\); its embedding is a one-dimensional quotient of \(\mathfrak m_p/\mathfrak m_p^2\), or equivalently a line in \(T_pS\). The exceptional fibre is exactly \(\mathbb P(T_pS)\). Exchange acts as minus the identity on the normal space to the diagonal, hence fixes its projective directions, also in characteristic two.

A finite-type morphism with the same residue fields and isomorphic completed local rings is étale at these points; the elementary completion argument is given below. Every nonempty closed subset of a finite-type space over an algebraically closed field has a closed point, so the étale locus is the whole source. The geometric injectivity and étaleness make \(q\) an open immersion; geometric surjectivity makes it an isomorphism. The completed rings just computed are power-series rings in four variables, giving smoothness. These conclusions descend from the algebraic closure by faithful flatness. If the affine-neighbourhood condition holds, Section 5 represents \(\operatorname{Hilb}^2_S\) by a scheme, so its identified quotient is a scheme as well. \(\square\)

Here and in Section 7 the completion criterion does not require a hidden characteristic assumption. If \(A\to D\) is the corresponding local homomorphism of Noetherian local rings and \(\widehat A\to\widehat D\) is an isomorphism, then \(\widehat D\) is flat over \(A\). Since \(D\to\widehat D\) is faithfully flat, \(D\) is flat over \(A\). Moreover \(D/\mathfrak m_A D=k\): its faithfully flat extension \(\widehat D/\mathfrak m_A\widehat D\) is \(k\), and injectivity into this field, together with the common coefficient field \(k\), forces the equality. Thus the fibre is unramified at the point. Flatness and unramifiedness give étaleness [Stacks, Tag 02GV]; the completion inputs are [Stacks, Tags 00MB–00MC]. The passage from an étale universally injective morphism to an open immersion is [Stacks, Tag 02LC], or its algebraic-space version [Stacks, Tag 05W5].

## 10 Lines and twisted cubics

Let \(V\) have dimension four and let \(F\in\operatorname{Sym}^3V\) define a cubic surface in \(\mathbb P(V)\). A line corresponds, in our quotient convention, to a rank-two quotient \(V\twoheadrightarrow Q\). It lies on the cubic exactly when the image of \(F\) in \(\operatorname{Sym}^3Q\) vanishes. The Fano scheme is therefore the zero scheme of the universal section

\[
F_Q\in H^0(\operatorname{Grass}_2(V),\operatorname{Sym}^3Q).
\]

On an affine Grassmannian chart this imposes the four coefficients of a binary cubic. This proves the representing equations, including their nonreduced test points, rather than only describing the set of lines. It is a closed projective subscheme of the Grassmannian. If the cubic surface is smooth, its Fano scheme is finite étale of degree \(27\); over an algebraic closure it consists of \(27\) reduced points. The tangent calculation and the degree computation are proved in *Tangent spaces and obstructions for Hilbert and Quot schemes*. Over a nonclosed field, the points need not all be rational.

The polynomial \(3t+1\) gives another useful warning about components. Over an algebraically closed field of any characteristic, the closure of the locus of twisted cubics in \(\operatorname{Hilb}^{3t+1}_{\mathbb P^3}\) is a smooth irreducible projective component of dimension \(12\). There is a second smooth component of dimension \(15\); their intersection is smooth of dimension \(11\), and the entire Hilbert scheme is singular there. Theorem 10.2 proves this classification, including rationality, the scheme-theoretic intersection and the complete singular locus. The historical theorem is Piene–Schlessinger; Heinrich–Skjelnes–Stevens, *The space of twisted cubics*, Proposition A.1 and Remark A.2, give its extension to characteristics two and three. The argument below retains those characteristics throughout.

One can see the dimension of the open twisted-cubic locus directly. Every smooth rational normal cubic is the image of \(\mathbb P^1\) under its complete linear system \(\mathcal O(3)\), followed by a projective change of coordinates. Its stabilizer in \(\operatorname{PGL}_4\) is \(\operatorname{PGL}_2\): restriction gives an automorphism of the curve, and each such automorphism acts on \(H^0(\mathcal O(3))\); an element restricting to the identity fixes four independent evaluation vectors and their further linear combinations, so is scalar. The orbit dimension is \(15-3=12\). The compactification and its boundary require the local equations and fixed-ideal argument below in addition to this orbit calculation.

### The formal meeting of the two components

A nonplanar boundary point already exhibits the different dimensions of the two components. We prove its entire formal neighbourhood, including the equations and their necessity in characteristics two and three. This calculation will also distinguish a flat family from a universal deformation.

**Theorem 10.1.** Let $k$ be any field and let $Z_0\subset\mathbb P^3_k$ have saturated ideal

\[
I_0=(zx,zy,z^2,x^3)\subset k[x,y,z,w].
\]

At the corresponding $k$-point of the Hilbert scheme, the completed local ring is

\[
\begin{gathered}
\widehat{\mathcal O}_{\operatorname{Hilb}^{3t+1},[Z_0]}
\simeq T/J,\\
T=k[[\mathbf a,\beta,c_1,c_2,c_3,c_4]],\\
J=(\beta c_1,\beta c_2,\beta c_3,\beta c_4),\\
|\mathbf a|=11.
\tag{10.1}
\end{gathered}
\]

The two formal branches are smooth of dimensions $12$ and $15$. Their scheme-theoretic intersection is smooth of dimension $11$, and their tangent spaces span the $16$-dimensional tangent space of the Hilbert scheme. The first branch lies in the closure of smooth twisted cubics; the second lies in the closure of plane cubics with a disjoint point. These assertions require no characteristic restriction.

**Proof.** We first connect the projective Hilbert problem to homogeneous ideals. Modulo $I_0$, the degree-$n$ monomials, for $n\geq1$, are

\[
\begin{gathered}
x^iy^jw^{n-i-j},\\
0\leq i\leq2,\quad i+j\leq n,\\
zw^{n-1}.
\end{gathered}
\tag{10.2}
\]

Their number is $3n+1$. Multiplication by $w$ is injective, so the ideal is saturated. Put $R=S/I_0$ and $C=k[x,y,w]/(x^3)$. There is a graded exact sequence, with its first map sending $1$ to $z$:

\[
0\longrightarrow k[w](-1)
\longrightarrow R\longrightarrow C\longrightarrow0.
\]

After sheafification, its first term is a length-one sheaf and its last term is the plane cubic $x^3=0$. The plane-cubic sequence and projective-space cohomology show that $H^1(Z_0,\mathcal O_{Z_0}(n))=0$ for $n\geq1$. They also show that the degree-$n$ piece in (10.2) maps isomorphically to $H^0(Z_0,\mathcal O_{Z_0}(n))$. Thus

\[
H^1(\mathbb P^3,\mathcal I_0(n))
=H^2(\mathbb P^3,\mathcal I_0(n))=0
\quad(n\geq1).
\]

For a flat family over a local Artinian $k$-algebra $B$, its ideal sheaf is $B$-flat too, by the ideal sequence. Filter $B$ by powers of its maximal ideal. The successive ideal-sheaf quotients are copies of $\mathcal I_0$, tensored with those finite-dimensional coefficient spaces. The displayed vanishing and the cohomology exact sequences show inductively that positive-degree ideal sections lift and have zero first and second cohomology. Freeness follows at each small extension $B\to B^\prime$ whose kernel $V$ is annihilated by the maximal ideal. The section sequence has kernel $V\otimes_k H^0(\mathcal I_0(n))$ and surjects onto the sections over $B^\prime$. Inductively lift a basis from those sections; its products with $V$ generate the entire kernel, by the displayed tensor identification. The resulting map from a free $B$-module is surjective, and equality of lengths makes it an isomorphism. The same argument applies to the quotient sections. Thus positive-degree sections commute with every Artinian base change.

It follows that these deformations are identified with their saturated homogeneous ideals. Three quadratic generators and one cubic generator lift the displayed generators of $I_0$. In every higher degree they still generate, by Nakayama applied to the finite module of sections in that degree. Conversely a homogeneous quotient with these free graded pieces and saturated ideal defines the required flat projective family. This explains why the following calculation determines the Hilbert scheme, rather than only an affine piece of its curves.

**The flat family.** Choose five coordinate parameters $s,t,p,q,r$ and write

\[
\begin{gathered}
X=x+sw,\qquad Y=y+tw,\\
Z=z+px+qy+rw.
\end{gathered}
\]

This triangular coordinate change is invertible over every parameter ring. Choose six more parameters $a_0,a_1,a_2,\ell_0,\ell_1,h$, and put

\[
A=a_0w+a_1Y+a_2X,
\qquad L=\ell_0w+\ell_1Y.
\]

These eleven parameters form $\mathbf a$. Over $k[\mathbf a,\beta,c_1,c_2,c_3,c_4]/J$, use the four forms

\[
\begin{aligned}
F_1={}&ZX+\beta AX-\beta LY,\\
F_2={}&ZY-\beta X(X+hw),\\
F_3={}&Z^2+c_4Zw+\beta AZ\\
&-\beta^2L(X+hw),\\
F_4={}&X^3+AXY-LY^2+hX^2w\\
&+c_1Xw^2+c_2Yw^2\\
&+c_3Zw^2+c_3c_4w^3.
\end{aligned}
\tag{10.3}
\]

Here and below the coefficients $a_i,\ell_i,h,\beta,c_i$ have degree zero; $X,Y,Z,w$ have degree one. We verify flatness explicitly. Order the monomials first by weights $(1,1,2,0)$ on $(X,Y,Z,w)$, then by total degree, then lexicographically with $Z>X>Y>w$. The leading monomials of the four monic forms are

\[
ZX,\qquad ZY,\qquad Z^2,\qquad X^3.
\]

Write $F=(F_1,F_2,F_3,F_4)$. The columns of the following coefficient matrix $M$ record reductions of the four generating monomial relations:

\[
\begin{gathered}
M_1=\begin{pmatrix}
-\beta(X+hw)\\
-Z-c_4w-\beta A\\
Y\\
0
\end{pmatrix},\\
M_2=\begin{pmatrix}
Z+c_4w\\
\beta L\\
-X\\
0
\end{pmatrix}.
\end{gathered}
\]

\[
\begin{gathered}
M_3=\begin{pmatrix}
-Y\\
X\\
0\\
\beta
\end{pmatrix},\\
M_4=\begin{pmatrix}
-X(X+hw)-c_1w^2\\
-c_2w^2-AX+LY\\
-c_3w^2\\
Z
\end{pmatrix}.
\end{gathered}
\]

Before imposing $J$, their four residues are

\[
\begin{aligned}
(FM)_1={}&\beta c_4wX(X+hw),\\
(FM)_2={}&\beta c_4w(AX-LY),\\
(FM)_3={}&\beta w^2(c_1X+c_2Y+c_3Z+c_3c_4w),\\
(FM)_4={}&\beta w^2\bigl[c_2X(X+hw)\\
&-c_1(AX-LY)\\
&-c_3\{AZ-\beta L(X+hw)\}\bigr].
\end{aligned}
\]

They vanish modulo $J$. In each column, after its two leading terms cancel, all other products have strictly smaller monomial than their least common multiple. The four leading relations are those for the pairs $(F_2,F_3)$, $(F_1,F_3)$, $(F_1,F_2)$ and $(F_1,F_4)$. The relations for the other two pairs are generated by these: pass from $ZY$ or $Z^2$ to $ZX$ and then to $X^3$. Thus every critical cancellation reduces to zero. Equivalently the usual monic-division proof of the standard-basis criterion applies: a relation of minimal leading monomial would reduce by one of these four relations to smaller leading monomial, a contradiction. This proof works over the coefficient ring, including its zero divisors; all leading coefficients are $1$.

It follows that (10.2), with $X,Y,Z$ in place of $x,y,z$, is a basis of every positive-degree quotient piece. Multiplication by $w$ stays injective, proving saturation on every base change. The forms therefore give a flat Hilbert family over the stated parameter scheme, not just over its reduced locus. Its specialization at the origin is $Z_0$.

**The tangent space.** Put $R=S/I_0$. A first-order perturbation of the four generators is a tuple

\[
(u,v,t,d)\in R_2^3\oplus R_3.
\]

Changing a generator by a multiple of $I_0$ has already been removed by using $R$. The first syzygies of $I_0$ are generated by

\[
\begin{gathered}
(y,-x,0,0),\quad(z,0,-x,0),\\
(0,z,-y,0),\quad(x^2,0,0,-z).
\end{gathered}
\]

For a monomial ideal these are checked directly from least common multiples; the remaining two pair relations follow from them. The tangent conditions are consequently

\[
\begin{gathered}
yu-xv=0,\quad zu-xt=0,\\
zv-yt=0,\quad x^2u-zd=0.
\end{gathered}
\tag{10.4}
\]

Expanding in (10.2) gives all solutions. The middle two equations force the $w^2$ coefficients of $u,v$ to vanish and force $t$ to be a scalar multiple of $zw$. The first equation then gives

\[
\begin{aligned}
u={}&\alpha x^2+\delta xy+\rho xw+\sigma zw,\\
v={}&\tau x^2+\alpha xy+\delta y^2+\rho yw+\nu zw,\\
t={}&\kappa zw.
\end{aligned}
\]

The last equation says precisely that the $w^3$ coefficient of $d$ vanishes. There are six coefficients in $u,v$, one in $t$, and nine in $d$: the tangent dimension is $16$.

Differentiating (10.3) realizes all of them. The coordinate changes $p,q,r,s,t$ account for the six coefficients in $u,v$, together with $\beta$; $c_4$ supplies the remaining coefficient in the third generator. In the cubic, $a_0,a_1,a_2,\ell_0,\ell_1,h,c_1,c_2,c_3$ supply its nine permitted monomials. The derivative of $r$ also contributes $2zw$ to the third generator, and the derivative of $s$ contributes $3x^2w$ to the fourth; subtract the corresponding $c_4$ and $h$ directions. These subtractions divide by neither $2$ nor $3$. Hence the parameter family induces an isomorphism on tangent spaces in every characteristic.

**Why all four equations are necessary.** The existence of the family proves flatness on the proposed base; it does not yet exclude a larger deformation base. For that we compute four independent primary obstructions. If the syzygies of (10.4) are lifted to second order, changing the second-order terms of the generators changes their residual tuple by the image of

\[
\begin{gathered}
\partial:R_2^3\oplus R_3\longrightarrow R_3^3\oplus R_4,\\
\partial(u,v,t,d)=\begin{pmatrix}
yu-xv\\
zu-xt\\
zv-yt\\
x^2u-zd
\end{pmatrix}.
\end{gathered}
\]

Thus every linear functional killing this image detects a necessary obstruction. Write $[m]v_i$ for the coefficient of the monomial $m$ in the $i$th residual. The following four functionals kill $\operatorname{im}\partial$:

\[
\begin{aligned}
\lambda_1(v)&=[xw^2]v_1+[zw^2]v_3,\\
\lambda_2(v)&=[yw^2]v_1-[zw^2]v_2,\\
\lambda_3(v)&=[zw^2]v_1,\\
\lambda_4(v)&=[x^2w]v_3.
\end{aligned}
\]

For example, the first two sums cancel the $w^2$ coefficients of the perturbations $v,u$, respectively. The third is zero because multiplication by $x$ or $y$ never produces $zw^2$ in $R$; the fourth is zero because neither $zv$ nor $yt$ can contain $x^2w$.

Set the eleven $\mathbf a$ directions to zero for the calculation. Use the tentative generators

\[
\begin{gathered}
zx,\qquad zy-\beta x^2,\qquad z^2+c_4zw,\\
x^3+c_1xw^2+c_2yw^2+c_3zw^2+c_3c_4w^3.
\end{gathered}
\]

Lifting the four original syzygies gives, modulo cubic parameter terms, the residual tuple

\[
\begin{gathered}
-\beta(c_1xw^2+c_2yw^2+c_3zw^2),\qquad0,\\
-\beta c_4x^2w,\qquad-\beta c_2x^2w^2.
\end{gathered}
\]

One can check it by adding $-\beta$ times the fourth generator to the first relation, $c_4w$ times the first generator to the second, $\beta x$ times the first and $c_4w$ times the second to the third, and $c_1w^2,c_2w^2,c_3w^2$ times the first three to the fourth. Applying the functionals gives

\[
-\beta c_1,\quad-\beta c_2,\quad-\beta c_3,\quad-\beta c_4.
\tag{10.5}
\]

Changing first-order lifts of a relation does not change these obstruction classes: their difference is an original syzygy, whose pairing with a tangent perturbation is zero modulo $I_0$ by (10.4). Second-order changes were already killed by the functionals. The four products in (10.5) are therefore independent necessary quadratic equations.

**The completed local ring.** Let $H$ be the completed Hilbert local ring. The tangent calculation gives a surjection from the formal power-series ring

\[
T=k[[\mathbf a,\beta,c_1,c_2,c_3,c_4]]
\longrightarrow H.
\]

The family gives $H\to T/J$, inducing the specified tangent isomorphism. Lift the images of the sixteen formal coordinates back to $T$. They define an automorphism of $T$, because their linear part is invertible; the inverse is constructed recursively by degree. Using that automorphism to choose the presentation, write $H=T/K$ with $K\subset J$ and unchanged tangent coordinates.

Now compute the four obstruction functionals on the full sixteen-parameter first-order deformation. Their quadratic equations vanish on the flat family $T/J$, so they lie in the four-dimensional space spanned by the products $\beta c_i$. Restricting to $\mathbf a=0$ gives (10.5), which is a basis of that space. Necessity of the equations therefore says that the degree-two initial part of $K$ is all of $J_2$. In particular each generator of $J$ belongs to $K+\mathfrak m^3$, where $\mathfrak m$ is the maximal ideal of $T$.

Since $K\subset J$ and $J$ is generated by those four quadratic monomials,

\[
J\cap\mathfrak m^3=\mathfrak mJ.
\]

Consequently $J=K+\mathfrak mJ$. The finite $T$-module $J/K$ equals its maximal-ideal multiple, so Nakayama gives $J=K$. This proves (10.1) to every order; no assertion that vanishing quadratic obstructions usually suffices has been made.

**The branches and their geometric meaning.** In the formal power-series ring,

\[
J=(\beta)\cap(c_1,c_2,c_3,c_4).
\]

Both ideals are prime. The quotients are power-series rings in $15$ and $12$ variables, and their sum gives the $11$-variable intersection. Their tangent spaces have the corresponding dimensions and sum to all sixteen directions. Thus the formal branches are smooth and meet transversely, although their union is singular.

On the branch $c_i=0$, the three quadrics are the minors of

\[
\begin{pmatrix}
X&\beta L&Z\\
Y&Z+\beta A&\beta(X+hw)
\end{pmatrix}.
\]

Where $\beta$ is invertible, the cubic generator follows from the quadrics. This branch contains smooth twisted cubics: set $\beta=1$, $A=0$, $L=w$ and $h=0$. The equations are the rational normal cubic parametrized by

\[
[w:X:Z:Y]=[s^3:st^2:s^2t:t^3].
\]

Smoothness is open, so the generic curve of this irreducible parameter branch is a smooth twisted cubic, and its origin lies in their closure.

On the branch $\beta=0$, take $c_4\ne0$. The quadrics are $ZX,ZY,Z(Z+c_4w)$. They support a plane cubic in $Z=0$ and the separate point $[X:Y:Z:w]=[0:0:-c_4:1]$. Restriction of $F_4$ to the plane is an arbitrary cubic in the chart where the $X^3$ coefficient is $1$: its nine other coefficients are $a_2,a_1,-\ell_1,h,a_0,-\ell_0,c_1,c_2,c_3c_4$. The fourth generator vanishes at the separate point. The monomial basis proves the Hilbert polynomial $3t+1$, so there is no further residual part. Generically this is a plane cubic with a disjoint point. The entire branch, including the origin, lies in the closure of that locus. This identifies the two formal branches claimed in the theorem. $\square$

For comparison, Heinrich–Skjelnes–Stevens, Appendix A, Lemma A.8 and Remarks A.9–A.10, give the boundary calculation. The proof above obtains the completed local ring from a monic flat family and four explicit obstruction functionals. Theorem 10.2 supplies the global step by classifying the three fixed ideals and excluding every invariant closed locus on which the conclusions could fail; the local calculation at $Z_0$ alone would not supply it.

### Three fixed ideals suffice for the global classification

We now account for every point of the Hilbert scheme. The projective parameter space and its triangular coordinate action make this possible without a separate list of all cubic curves.

**Theorem 10.2 (the two components).** Over an algebraically closed field $k$ of any characteristic, $\operatorname{Hilb}^{3t+1}_{\mathbb P^3_k}$ is reduced and has exactly two irreducible components. The closure $H$ of the smooth twisted cubics is smooth, rational, projective and $12$-dimensional. The closure $H'$ of plane cubics with a disjoint point is smooth, rational, projective and $15$-dimensional. Their scheme-theoretic intersection $D$ is smooth, irreducible, rational and $11$-dimensional.

At every closed point of $D$, the completed local ring of the whole Hilbert scheme has the form (10.1). Its two component tangent spaces span the $16$-dimensional tangent space and intersect in the tangent space of $D$. The Hilbert scheme is singular precisely along $D$.

**Proof.** All closures of loci in this proof have their reduced induced structure. The orbit calculation above shows that $H$ is irreducible of dimension $12$. For $H'$, choose a plane, a cubic in it and a point outside the cubic. This is an irreducible parameter space of dimension

\[
3+9+3=15.
\]

The union is a flat family of polynomial $3t+1$. For a general member, its plane cubic and its isolated point are uniquely recovered from the scheme. Thus its image has dimension $15$, and $H'$ is irreducible of that dimension. Both loci and their closures are invariant under projective coordinate changes.

**A projective fixed-point argument.** Let $B$ be the group of invertible triangular changes of the four variables, allowing each variable to acquire a linear combination of the preceding ones in the order $x,y,z,w$. We will use this elementary fact:

> Every nonempty closed $B$-invariant subset of the Hilbert scheme contains a $B$-fixed point.

The closed Grassmannian construction in Theorem 4.1 is equivariant: take one sufficiently large degree $m$, use the quotient of $S_m$, then its Plücker embedding. The ordered monomials of $S_m$ give a triangular matrix for every element of $B$. The induced representation on the exterior power, or its dual according to the projective convention, is triangular too. Consequently the ambient projective representation has a complete invariant vector-space flag.

For a nonempty invariant closed subset $Y$, choose the first vector space $V_i$ of that flag whose projectivization meets $Y$. Then $Y\cap\mathbb P(V_i)$ is projective and lies entirely in the affine complement of $\mathbb P(V_{i-1})$. Give this intersection its reduced structure. Being affine and proper over $k$, it is finite: its coordinate algebra is finite-dimensional by [proper coherent cohomology, Corollary 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-QC/proper-morphisms-and-coherent-direct-images.html#5-finite-cohomology-and-global-functions). The irreducible group $B$, a product of a torus with an affine space as a variety, cannot move a point through a nontrivial finite orbit. Thus this intersection contains a fixed $k$-point. This proves the fact without a characteristic-zero triangularization theorem.

**All possible fixed ideals.** A fixed saturated homogeneous ideal is monomial, since the diagonal torus has distinct characters on distinct monomials. We first show that $w$ is a nonzerodivisor modulo such an ideal $I$. If a counterexample existed, choose a monomial $w^rM\notin I$, with $M$ not divisible by $w$, for which $w^{r+1}M\in I$. Substitute $w+tx$, then $w+ty$, then $w+tz$. In each substitution the coefficient of $t^{r+1}$ belongs to $I$, because the ideal is fixed and $k$ is infinite. Hence

\[
\begin{gathered}
x^{r+1}M,\ y^{r+1}M\in I,\\
z^{r+1}M,\ w^{r+1}M\in I.
\end{gathered}
\]

Every monomial of sufficiently large degree is divisible by one of those four powers. Saturation would give $M\in I$, a contradiction. Thus no minimal monomial generator involves $w$, and

\[
I=J\,k[x,y,z,w],\qquad J\subset k[x,y,z].
\]

The one-dimensional monomial support of $k[x,y,z]/J$ can contain only the $z$-axis. Indeed its irreducible components are coordinate axes. If it contained the $x$-axis, invariance under $y\mapsto y+tx$ would put an entire plane in the support. If it contained the $y$-axis, use $z\mapsto z+ty$. Either contradicts dimension one. Therefore $\sqrt J=(x,y)$.

Put $K=J:z^\infty$. It is generated by monomials in $x,y$. The quotient $K/J$ is finite-dimensional: powers of $x,y$ annihilate it, as does one power of $z$, by finite generation and the definition of the colon ideal. Thus $k[x,y]/K$ has length $3$, the leading coefficient of our Hilbert polynomial. The three possible downward-closed sets of three standard monomials in two variables are

\[
\{1,x,x^2\},\qquad\{1,x,y\},\qquad\{1,y,y^2\}.
\]

The first is excluded: its ideal contains $y$, so invariance under $y\mapsto y+tx$ would also put $x$ in the ideal. The other two give

\[
K=(x,y)^2\quad\hbox{or}\quad K=(x,y^3).
\]

After adjoining $w$, their Hilbert polynomials are respectively $3n+1$ and $3n$. The finite-dimensional graded module $K/J$, tensored with $k[w]$, adds the constant $\dim_k(K/J)$ to that polynomial. Hence the first case forces $J=K$, and the second forces $\dim_k(K/J)=1$.

In the second case the single omitted monomial must be a minimal generator of $K$: a proper divisor in $K$ would otherwise belong to $J$ and force that monomial back into $J$. The possibilities are $x$ and $y^3$, and multiplication by every variable must kill their classes. We have proved that the complete fixed-point list is

\[
\begin{aligned}
J_A&=(x^2,xy,y^2),\\
J_N&=(x^2,xy,xz,y^3),\\
J_P&=(x,y^4,y^3z).
\end{aligned}
\tag{10.6}
\]

All three are fixed under the triangular group, by direct substitution. The argument used no binomial-coefficient division; it also excludes additional fixed ideals in characteristics two and three.

**The local scheme at $J_A$.** Here

\[
S/J_A=k[z,w]\oplus xk[z,w]\oplus yk[z,w]
\]

as a graded $k[z,w]$-module, with the last two generators in degree one. Sheafifying on the supporting line shows that its homogeneous pieces equal global sections in every nonnegative degree. A tangent perturbation of $(x^2,xy,y^2)$ is a tuple $(u,v,t)\in(S/J_A)_2^3$. The two generating syzygies give

\[
yu-xv=0,\qquad yv-xt=0.
\]

In each perturbation, separate its quadratic part in $z,w$ from the part in $(x,y)\cdot k[z,w]_1$. The equations kill all three pure $z,w$ parts. They impose no condition on the remaining four coefficients in each perturbation, since $(x,y)^2=0$. Thus the Hilbert tangent dimension is $12$ in every characteristic.

This point belongs to $H$. An explicit flat degeneration has equations

\[
\begin{gathered}
x^2-\tau yw,\qquad xy-\tau^2zw,\\
y^2-\tau xz.
\end{gathered}
\]

Their leading monomials are $x^2,xy,y^2$ when $x,y$ have weight two and $z,w$ weight one. With $F_i$ denoting the three displayed quadrics, the two critical identities are

\[
\begin{aligned}
yF_1-xF_2&=-\tau wF_3,\\
xF_3-yF_2&=-\tau zF_1.
\end{aligned}
\]

They prove that the monomial quotient basis is free over $k[\tau]$; multiplication by $w$ also proves saturation. For $\tau\ne0$, replacing $z,w$ by $\tau z,\tau w$ gives the rational normal cubic equations. Thus the closed point $J_A$ lies on the $12$-dimensional irreducible closed set $H$. Its local Hilbert dimension is at least $12$ and its tangent dimension is exactly $12$, so the local ring is regular. The unique local component has the same dimension as $H$, so $H$ is an irreducible component of the Hilbert scheme. Over our algebraically closed field, $J_A$ is a smooth point of that component alone.

**The local scheme at $J_P$.** This point is a plane cubic with a length-one contribution at a point on it. There is a sheaf exact sequence

\[
0\longrightarrow k_P\longrightarrow\mathcal O_Z
\longrightarrow\mathcal O_C\longrightarrow0,
\]

where $C$ is $x=y^3=0$ and $P=[0:0:0:1]$. Plane-cubic cohomology gives

\[
h^0(Z,\mathcal O_Z(n))=3n+1\qquad(n\geq1).
\]

In degree one a basis is $y,z,w$ together with the torsion section $y^3/w^2$, extended by zero away from $P$. It is regular because $y^3z=y^4=0$. In degrees at least three, global sections equal the homogeneous quotient pieces; their usual monomial bases already have dimension $3n+1$.

Use the generators $(x,y^4,y^3z)$. Their first syzygies are generated by

\[
(-y^4,x,0),\qquad(-y^3z,0,x),\qquad(0,z,-y).
\]

A tangent homomorphism sends them to

\[
(a,b,c)\in H^0(\mathcal O_Z(1))
\oplus H^0(\mathcal O_Z(4))^2.
\]

The first two relations impose no condition, and the third is $zb-yc=0$. Each degree-four section space has dimension $13$. In degree five, the image of $(b,c)\mapsto zb-yc$ is precisely the span of all standard monomials except $w^5$, so has dimension $15$. Therefore the tangent dimension is

\[
4+2\cdot13-15=15.
\]

The extra degree-one torsion section is essential; using only homogeneous linear polynomials would give an incorrect tangent dimension.

This point lies on $H'$. To see the flat specialization, let $C_\tau$ be the plane cubic with ideal $(x,y^3+\tau w^3)$ and keep $P$ fixed. Map its ideal sheaf surjectively to $\mathcal O_P$ by sending the generator $x$ to zero and the cubic generator to $1$, using $w$ to trivialize the twists at $P$. Its Koszul relation maps to zero, so the map exists over the whole parameter line. The kernel is an ideal sheaf defining $Z_\tau$, and

\[
0\longrightarrow\mathcal O_{P\times\mathbb A^1}
\longrightarrow\mathcal O_{Z_\tau}
\longrightarrow\mathcal O_{C_\tau}\longrightarrow0
\]

proves flatness. At $\tau=0$ its ideal is $J_P$. For $\tau\ne0$, the point is disjoint from the cubic and the family is their union. Thus the local Hilbert dimension at $J_P$ is at least $15$; its tangent dimension is $15$, so its local ring is regular. This makes $H'$ an irreducible component as well, and $J_P$ lies on it alone. The components are distinct: the $15$-dimensional $H'$ cannot pass through the $12$-dimensional local Hilbert scheme at $J_A$.

**The local scheme at $J_N$.** Permute the variables by $Z=x$, $X=y$, $Y=z$. Theorem 10.1 applies. Its finite-type parameter family has an isomorphism on completed local rings at the origin and hence is étale there, by the completion criterion proved in Section 9. Its two actual parameter branches map into $H$ and $H'$ by the geometric identifications in that theorem. They have different dimensions and give the two local components. In this étale neighbourhood, the reduced component pullbacks are exactly $c_i=0$ and $\beta=0$: étale pullback of a component is a union of components, and the dense generic loci distinguish these two. Thus $H,H'$ are smooth here, their intersection is smooth of dimension $11$, and the whole local Hilbert ring is reduced. There is no third local component.

**Why there are no other components or nilpotents.** The three local calculations give an open neighbourhood of each fixed point contained in $H\cup H'$. If the complement of this union were nonempty, its closure would be a nonempty invariant closed subset. The fixed-point argument would put one of (10.6) in that closure, contradicting those neighbourhoods. Thus the underlying Hilbert scheme is $H\cup H'$. These are its two distinct irreducible components, as already distinguished at $J_A,J_P$.

The nilradical is a coherent ideal on this Noetherian Hilbert scheme. If nonzero, its support would be a nonempty invariant closed subset and contain a fixed point. All three local Hilbert rings are reduced, so this is impossible. Hence the whole Hilbert scheme is reduced, and it is the scheme-theoretic union of the reduced $H,H'$.

Apply the same fixed-point argument to the nonsmooth locus of $H$. This is a closed invariant subset of the projective $H$. Its only possible fixed points are $J_A,J_N$, where we have proved smoothness; $J_P$ lies on $H'$ alone. Thus $H$ is smooth everywhere. The argument for $H'$ uses $J_N,J_P$ and is identical. For $D=H\cap H'$, the only possible fixed point is $J_N$. Its local intersection is smooth, so the nonsmooth locus of $D$ is empty. In particular $D$ is reduced. Each irreducible component of $D$ is invariant, since $B$ is irreducible and cannot permute its finitely many components. Each would therefore contain $J_N$. The regular local ring there has only one component, so $D$ is irreducible, of dimension $11$.

At any closed point of $D$, the reduced union gives the local-ring fibre product

\[
\mathcal O_{H\cup H'}
=\mathcal O_H\times_{\mathcal O_D}\mathcal O_{H'}.
\]

After completion the same identity holds, by exactness of Noetherian completion. The three schemes are smooth of dimensions $12,15,11$. Choose eleven formal coordinates on $D$, lift them on both components, and extend by one and four normal coordinates respectively. These choices are possible because a closed immersion between smooth schemes identifies its completed quotient with the power-series ring in the quotient coordinates. The fibre product is then exactly (10.1): a series is a common series in the eleven coordinates, plus a multiple of the one normal coordinate, plus a series in the other four normal coordinates with zero common constant term. Products between the two normal ideals vanish. This proves the transverse tangent statement and shows that the singular locus is precisely $D$.

**Rationality.** For a general point of $H'$, let the plane equation be $l$ and the isolated point be $P$, outside that plane. Its three-dimensional space of quadrics is $l\cdot I_P(1)$: a quadratic vanishing on a plane cubic must restrict to zero on the plane. The common linear factor recovers the plane; the three residual linear forms recover $P$; and restriction of the cubic ideal to the plane recovers the cubic equation up to scalar. On fixed coefficient charts these are rational operations, obtained by common-factor calculation and row reduction. They give an actual rational inverse, including in positive characteristic. Thus the rational $15$-dimensional parameter space used to define $H'$ is birational to $H'$.

For $H$, use the $12$-parameter branch $c_i=0$ of (10.3). It parametrizes the entire $12$-dimensional formal branch in Theorem 10.1 and its generic curve is a smooth twisted cubic, so its image is dense in $H$. On the open $\beta\ne0$, all its parameters are recovered rationally from the two normalized quadrics $F_1,F_2$. These are the unique reduced quadrics with leading monomials $zx,zy$ in the monomial order used above; their coefficients are read from the quadratic ideal by row reduction. Denote their coefficients by $u_m=[m]F_1$, $v_m=[m]F_2$. The inverse is

\[
\begin{aligned}
s&=u_{zw},\qquad t=v_{zw},\\
\beta&=-v_{x^2},\qquad p=v_{xy},\\
q&=v_{y^2},\qquad r=v_{yw}-qt.
\end{aligned}
\]

\[
\begin{aligned}
a_2&=(u_{x^2}-p)/\beta,\\
a_1&=(u_{xy}-q)/\beta,\\
\ell_1&=-u_{y^2}/\beta,\\
h&=(pt-v_{xw})/\beta-2s,\\
a_0&=(u_{xw}-r-ps)/\beta\\
&\quad-a_1t-2a_2s,\\
\ell_0&=(qs-u_{yw})/\beta\\
&\quad+a_1s-2\ell_1t.
\end{aligned}
\]

The equalities follow by expanding the two quadrics in $x,y,z,w$. Division uses $\beta$ only, so the inverse works in every characteristic. Hence $H$ is rational.

Finally choose a plane, a point in it and a plane cubic singular at that point. This rational incidence space has dimension $5+6=11$: the plane and point contribute five, and value and two local first derivatives impose three independent linear conditions on the ten cubic coefficients. This statement includes characteristic three; the value condition is imposed separately. Lift the plane cubic to an ambient cubic vanishing to order at least two at the point, and take the ideal generated by that lift and the plane equation times the three linear equations of the point. Such a lift exists by lifting the two plane linear coordinates vanishing at the point. Any two such lifts differ by the plane equation times a quadric vanishing at the point: their first normal derivatives agree because both vanish to order two. That difference is already in the ideal, so the scheme is independent of the lift. In coordinates it is $(ZX,ZY,Z^2,F)$ with $F\in(X,Y)^2$. On the chart where the $X^3$ coefficient is nonzero it is precisely the common branch of (10.3). Its image is therefore dense in $D$. The quadratic ideal recovers its common linear factor, the plane, and the three-dimensional point ideal; restriction to the plane recovers the cubic up to scalar. These recoveries are rational on the indicated coefficient chart. The incidence space is consequently birational to $D$, proving its rationality. Projectivity of the components follows because they are closed in the projective Hilbert scheme. $\square$

This proves the all-characteristic classification stated in Proposition A.1 and Remark A.2 of Heinrich–Skjelnes–Stevens. The proof uses the explicit local equations, three fixed ideals, and invariant closed loci; the generic orbit dimension alone would not give any of the boundary conclusions.

## 11 Exercises with complete solutions

**Exercise 1.** Determine \(\operatorname{Quot}^{P}_{\mathcal O^r/\operatorname{Spec}k/k}\) when \(P\) is constant. Include the impossible values.

**Solution.** The projective scheme here is a point, so the Hilbert polynomial of a fibre is its vector-space dimension. A quotient on a test scheme \(T\) is a finitely presented flat module \(G\) of constant rank \(q=P\), with a surjection \(\mathcal O_T^r\to G\). Finitely presented flat modules are locally free. Thus the functor is exactly \(\operatorname{Grass}_q(k^r)\) if \(q\) is an integer with \(0\leq q\leq r\). The endpoint values give a single point. If \(P\) is nonconstant, a nonintegral constant, a negative integer, or an integer greater than \(r\), no quotient exists over a nonempty field-valued test scheme, and the representing scheme is empty. The empty test scheme has its usual unique map to the empty scheme.

**Exercise 2.** Prove that the Hilbert scheme of degree-\(d\) hypersurfaces in \(\mathbb P^n\), for \(n,d\geq1\), is a projective space. Explain its dual convention and check arbitrary families.

**Solution.** A subscheme with polynomial \(P_d\) has rank-one ideal. On a factorial affine chart, taking the greatest common divisor of generators shows that its double dual is principal. Globally this double dual is \(\mathcal O(-e)\), with a quotient supported in codimension at least two. Comparing the next coefficient of the ideal polynomial gives \(e=d\); in dimension one the ideal is already invertible. The residual quotient then has zero polynomial, so is zero. Thus the field-valued ideal is \(\mathcal O(-d)\).

For a flat Hilbert family, the fibrewise Cartier criterion makes its ideal \(I\) invertible. The fibres of \(I(d)\) are trivial with one global section and no higher cohomology. Consequently \(N=p_*I(d)\) is a line bundle, formation commutes with every base change, and evaluation identifies \(p^*N\) with \(I(d)\). The inclusion in \(\mathcal O(d)\) gives a subline of \(H^0(\mathcal O(d))\otimes\mathcal O_T\), with locally free cokernel since the fibre equation is nonzero. Conversely any such subline evaluates to a locally principal ideal with a nonzero equation on every fibre. The Cartier criterion makes its quotient flat, of the required polynomial. These inverse constructions give

\[
\operatorname{Hilb}^{P_d}_{\mathbb P^n}
=\mathbb P\bigl(H^0(\mathcal O(d))^\vee\bigr).
\]

The dimension is \(\binom{n+d}{n}-1\). The dual appears because \(\mathbb P(W)\) records quotient lines of \(W\), whereas an equation is a subline of the section space.

**Exercise 3.** Show \(\operatorname{Hilb}^d_C=\operatorname{Sym}^d C\) for a smooth separated finite-type curve. Start with \(d=2\), including a double point.

**Solution.** The sum of the \(d\) graph divisors gives an invariant family on \(C^d\), hence a morphism from its symmetric quotient. For a pair of distinct points it simply forgets their order. At a double point, choose a local parameter \(u\). A deformation over an Artinian local \(k\)-algebra \(R\) is a free rank-two quotient with basis \(1,u\), hence has its unique equation

\[
u^2+a_1u+a_2=0,\qquad a_1,a_2\in\mathfrak m_R.
\]

It follows that the completed Hilbert ring is \(k[[a_1,a_2]]\). The completed symmetric-square ring is \(k[[u_1,u_2]]^{\mathfrak S_2}=k[[e_1,e_2]]\), in every characteristic. The divisor map sends \(a_1\) to \(-e_1\) and \(a_2\) to \(e_2\), so gives an isomorphism on these completions.

For a general divisor \(\sum d_i p_i\), idempotents lift across nilpotent ideals and split its Artinian deformation into the distinct support clusters. Each cluster is a free quotient with basis \(1,u_i,\ldots,u_i^{d_i-1}\) and one monic relation of degree \(d_i\). Its \(d_i\) coefficients independently belong to \(\mathfrak m_R\). The symmetric quotient has the same completed ring, using elementary symmetric functions separately in each cluster. These identifications respect the divisor morphism. The morphism is therefore étale at all geometric closed points. Its geometric points are in bijection because a finite-colength ideal in a discrete valuation ring is a unique power of its maximal ideal. Étaleness, geometric injectivity and surjectivity give an isomorphism, which descends from an algebraic closure. Section 7 proves the quotient construction and the formal symmetric-function assertions used here.

**Exercise 4.** Compute \(\operatorname{Hilb}^2_{\mathbb A^2}\) and prove that it is smooth of dimension four, without restricting the characteristic.

**Solution.** In the open where \(1,x\) is a basis, a quotient has unique relations \(x^2=a+bx\) and \(y=c+dx\), with \(a,b,c,d\) arbitrary. These relations conversely give the free algebra \(R[x]/(x^2-bx-a)\) and a surjection from \(R[x,y]\). Thus this open is \(\mathbb A^4\). There is a second \(\mathbb A^4\) where \(1,y\) is a basis. They cover: on a field fibre, if neither \(x\) nor \(y\) is independent from \(1\), both are scalars and cannot generate a two-dimensional algebra. The first basis changes to the second exactly when \(d\) is invertible, since its determinant is \(d\). Substitution yields

\[
\begin{gathered}
a'=d^2a-c^2-bcd,\\
b'=2c+bd,\qquad c'=-c/d,\qquad d'=1/d.
\end{gathered}
\]

The corresponding formula with primes inverted returns \(a,b,c,d\), so these identify the two basis opens. Smoothness and dimension four hold on both charts and hence globally. In characteristic two only the summand \(2c\) vanishes; the chart and its invertible transition remain valid.

**Exercise 5.** Prove that the Grassmannian morphism for \(\operatorname{Quot}^P\) is a closed immersion. Identify where uniformity, flattening, and properness enter.

**Solution.** Choose the common \(m\) of Lemma 2.1 and put \(V=f_*E(m)\), \(r=P(m)\). On \(H=\operatorname{Grass}_r(V)\) let \(U\) be the kernel of its universal quotient. Form

\[
F=\operatorname{coker}\bigl(p^*U\otimes L^{-m}\to E_H\bigr).
\]

Flattening with polynomial \(P\) represents the permitted pullbacks of \(F\) by a locally closed subscheme \(H_P\). For any desired quotient \(E_T\to G\), proper flat cohomology makes \(p_*G(m)\) a rank-\(r\) vector bundle. The map \(V_T\to p_*G(m)\) is onto, because its fibre is onto by the uniform vanishing of \(H^1(K_t(m))\), and Nakayama kills its finite cokernel. This defines its Grassmannian point.

Its kernel \(U_T\) has fibre \(H^0(K_t(m))\). Uniform generation therefore makes the evaluation \(p^*U_T\otimes L^{-m}\to K_T\) surjective: its finite cokernel has zero fibre everywhere. It follows that the induced candidate \(F_T\) is exactly \(G\), so the Grassmannian point factors through \(H_P\). Conversely, on \(H_P\), the quotient of \(V\) by \(U\) maps onto \(p_*F(m)\); both are locally free of rank \(r\), so this is an isomorphism. The two constructions are inverse on arbitrary test schemes. Hence \(\operatorname{Quot}^P\to H\) is a locally closed immersion, including all its infinitesimal structure.

For a discrete valuation ring, saturating the generic kernel inside \(E_R\) gives a coherent quotient that is torsion-free over \(R\), hence flat. Its polynomial is constant, and any flat extension has that same saturated kernel. The Noetherian valuative criterion gives properness. A proper locally closed immersion into the separated Grassmannian is closed. Thus flattening gives the locally closed part of the argument; properness removes the possibility of missing boundary points. Finally the Grassmannian determinant is very ample, and its restriction is \(\det p_*G(m)\).

**Exercise 6.** Let \(k\) have characteristic two. On \(U=\operatorname{Spec}k[x,y]\), let the generator of \(\mathbb Z/2\mathbb Z\) act by

\[
\sigma(x)=x,\qquad\sigma(y)=y+x.
\]

Compute the invariant ring and the quotient map. Base-change the quotient by the closed subscheme \(x=0\) of its target. Determine the action and its categorical quotient on that base change, and decide whether the base-changed original quotient is still categorical.

**Solution.** Put \(z=y^2+xy\). It is invariant, and the presentation

\[
\begin{gathered}
k[x,y]\simeq k[x,z][Y]/(Y^2+xY-z),\\
y\longleftrightarrow Y
\end{gathered}
\]

makes the source algebra free with basis \(1,y\) over \(k[x,z]\). In particular the coefficient ring embeds. Every element is uniquely \(f(x,z)+y g(x,z)\), and its difference from its translate is \(xg(x,z)\). The polynomial ring \(k[x,z]\) is a domain, so invariance is equivalent to \(g=0\). Thus the invariant ring is \(k[x,z]\), and the quotient sends \((x,y)\) to \((x,y^2+xy)\). It is finite locally free of degree two.

After imposing \(x=0\), the source is \(\operatorname{Spec}k[y]\), the action is trivial, and the base-changed morphism is

\[
\operatorname{Spec}k[y]\longrightarrow\operatorname{Spec}k[z],
\qquad z\longmapsto y^2.
\]

The invariant ring is now all of \(k[y]\). Its categorical quotient is the identity of \(\operatorname{Spec}k[y]\), whereas the displayed morphism is not categorical: the invariant function \(y\) is not a polynomial in \(y^2\). Every geometric fibre still has exactly one point, and the morphism is finite and universally closed. Those properties alone do not recover invariant functions or categorical initiality. The target base change is not flat, since multiplication by the nonzero element \(x\) becomes zero in \(k[x,z]/(x)\). The flat base-change assertion of the theorem is therefore consistent with this example.

## 12 What this lesson does not prove

The uniform regularity, projective flattening, Grassmannian representation and Plücker results are proved in the preceding lessons. The foundational inputs used here are the following, with their precise scope. The curve affine-neighbourhood and arbitrary-base relative Cartier assertions are proved in Lemmas 7.A–7.B; their construction is independent of the Quot representability theorem.

- Proper pushforward of a finitely presented sheaf flat over an arbitrary base is locally computed by a finite complex of finite locally free modules, compatibly with base change, in the proper finitely presented setting: the full proof is [Perfect tensor pushforwards over an arbitrary base](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-AS/moduli-stacks-are-algebraic.html#native-spaces-perfect-lemma-base-change-tensor-perfect) [Stacks, Tag 0A1H]. Its vanishing consequences were derived in *Flattening stratifications*.
- [Faithfully flat descent, Theorem 2.5, Proposition 3.1 and Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-DFG/faithfully-flat-descent.html#2-recovering-a-module-from-a-cocycle) proves descent for modules, their finite-presentation and flatness properties, and quasi-coherent sheaves on arbitrary schemes [Stacks, Tag 023R]. Descent of finite presentation, properness and flatness for morphisms is [Descending properties of schemes and morphisms, Theorem 2.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-DFG/AG-DFG-03.html#2-checking-a-morphism-on-an-fpqc-covering-of-its-target) [Stacks, Tags 02L0–02L2]. The sheaf argument in Section 1 applies these results to kernels.
- The Noetherian discrete-valuation criterion for properness is [Proper morphisms and the valuative criterion, Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-MO/proper-morphisms-and-valuative-criteria.html#5-why-discrete-valuation-rings-suffice-over-a-noetherian-base) [Stacks, Tag 0208]. We use it only for the finite-type separated morphism over a Noetherian base obtained above.
- The finite-extension algebra lemma of Section 9 proves Artin–Tate [comparison: Stacks, Tag 00IS]. [Completion, Theorems 3.1–3.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-CA/completion.html#3-noetherian-exactness-tensoring-and-flatness) proves exactness, flatness, faithful flatness for local completion, and Noetherianity [Stacks, Tags 00MB–00MC]. [Étale morphisms and their local structure, Lemma 1.2 and Theorem 4.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-FSE/etale-morphisms-and-their-local-structure.html#4-the-topology-and-the-open-immersion-criterion) proves the flat-unramified and open-immersion criteria [Stacks, Tags 02GV, 02LC and 05W5]; Section 7 above spells out their use after the completed-local-ring calculation. The effect of completion on the invariant rings and its use in the curve and surface morphisms were explained above.
- Lemma 7.A proves finite-set affine neighbourhoods, the affine-or-projective assertion, and point-removal affineness on regular curves over every field [Stacks, Tag 0A27]. The equation and flat-closed-family forms of the relative fibrewise Cartier criterion, with openness and arbitrary base change, are proved in Lemma 7.B [Stacks, Tag 062Y]. Also \(\operatorname{Pic}(\mathbb P^n_k)=\mathbb Z\) for \(n\geq1\) is [Weil divisors and the class group, Theorem 4.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-MO/weil-divisors-and-the-class-group.html#4-affine-and-projective-space) [Stacks, Tag 0BXJ].
- For a separated finitely presented morphism \(X\to S\) and an arbitrary quasi-coherent source \(E\), the general Quot functor is an algebraic space; when \(E\) is finitely presented, it is locally of finite presentation. The Hilbert functor is a separated algebraic space locally of finite presentation. These are proved in [Moduli stacks are algebraic, Theorem 6.2 and Corollary 6.3](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-AS/moduli-stacks-are-algebraic.html#6-quotients-and-closed-subschemes), including all parameter schemes and proper-support conditions. Their Stacks comparisons are Tags 09TU and 0D01. The projective construction in Theorem 4.1 does not use these general algebraicity results; the general surface example does use the Hilbert-space theorem.
- More generally, let \(X\to S\) be a proper morphism of finite presentation of algebraic spaces, let \(E\) be finitely presented, and let \(L\) be relatively ample. For a fixed polynomial \(P\), the algebraic space \(\operatorname{Quot}^{P,L}_{E/X/S}\) is proper over \(S\) [Stacks, Tag 0DPC]. The base need not be Noetherian. Theorem 4.3 proves this general properness statement, by projective embedding, exact polynomial rescaling and finite-presentation descent to a Noetherian coefficient ring. Theorem 4.1 supplies the projective scheme used in that proof.
- The finite-group quotient theorem in Section 9 proves existence, finiteness, separatedness, finite type, invariant functions and categorical initiality, with flat base change and no characteristic restriction. It uses the finite-inertia construction in [Quotient stacks and Deligne–Mumford stacks, Section 6.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-AS/quotient-and-dm-stacks.html#6-1-finite-inertia-and-the-coarse-space). The finite-piece prerequisite is proved in Affine descent, Zariski Main and recognition of spaces, Section D3 and Lemma E4.3; proper quasi-finite finiteness is [Zariski's Main Theorem, Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-MO/zariskis-main-theorem.html#5-properness-and-normality). The two-point Hilbert identification is then proved by its explicit local rings. These are programme proof routes; Keel–Mori remains the historical comparison.
- Theorems 10.1–10.2 prove the entire twisted-cubic classification in every characteristic: both components, their smoothness and rationality, the reduced Hilbert scheme, the smooth irreducible intersection and its transverse local equations. The three fixed ideals exhaust all possibilities by the projective triangular-flag argument and saturation. Proper affine finiteness in that argument is the exact coherent-cohomology result linked there. The tangent calculations retain the planar torsion section, and both boundary specializations are flat. The cubic-surface degree and tangent assertion is proved in the later tangent–obstruction lesson.

The fixed-polynomial projectivity theorem has been proved with a possibly nonflat coherent source. The general algebraic-space theorem does not by itself imply projectivity, and the coproduct over all polynomials need not be of finite type.

## References

- Grothendieck, *Techniques de construction et théorèmes d'existence en géométrie algébrique IV: les schémas de Hilbert*, Séminaire Bourbaki, Exposé 221, §§3–4. [Original text](https://www.numdam.org/item/SB_1960-1961__6__249_0/).
- Nitsure, *Construction of Hilbert and Quot schemes*, §§3–5. [Author's paper](https://arxiv.org/abs/math/0504590).
- The Stacks project: [Quot and Hilbert spaces](https://stacks.math.columbia.edu/tag/082L), particularly Tags 09TU and 0D01; [properness criterion](https://stacks.math.columbia.edu/tag/0208); [relative Cartier criterion](https://stacks.math.columbia.edu/tag/062Y). The tagged results are read in the AI Integrated Stacks Project edition.
- Keel and Mori, *Quotients by groupoids*, Corollary 1.2, Proposition 5.1 and Lemma 6.3. [Author's paper](https://arxiv.org/abs/alg-geom/9508012).
- Heinrich, Skjelnes and Stevens, *The space of twisted cubics*, Épijournal de Géométrie Algébrique **5** (2021), Article 10, Appendix A. [Published paper](https://epiga.episciences.org/7539).