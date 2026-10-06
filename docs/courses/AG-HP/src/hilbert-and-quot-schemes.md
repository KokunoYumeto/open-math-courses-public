# Hilbert and Quot schemes

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A sheaf quotient can be recovered from enough of its sections, provided the meaning of “enough” is uniform across the family. A Grassmannian records a quotient of the resulting finite module of sections. It does not by itself ensure that the induced sheaf has the desired Hilbert polynomial or is flat. Flattening supplies those conditions, and a valuation argument closes the resulting locally closed subscheme. This is the construction of the projective Quot scheme.

We give the construction over a Noetherian base with a coherent source, allowing that source and its module of sections to be nonflat. The test schemes are arbitrary. We then construct finite-point Hilbert schemes by explicit algebra charts and calculate the two-point scheme of the affine plane.

The prerequisites are the representability and Plücker proofs in *Grassmannians*, the uniform kernel theorem in *Regularity and bounded families*, and the projective flattening theorem in *Flattening stratifications*. We also use the proper flat cohomology input [Stacks, Tag 0A1H], with its arbitrary-base consequences proved in the latter lesson, and the Noetherian discrete-valuation criterion for properness [Stacks, Tag 0208]. The corrected partial-coefficient strengthening discussed in the regularity lesson is not needed for the construction.

## 1 Quotients and their families

Let \(f:X\to S\) and let \(E\) be quasi-coherent on \(X\). The functor \(\operatorname{Quot}_{E/X/S}\) assigns to an \(S\)-scheme \(T\) the equivalence classes of surjections

\[
E_T\twoheadrightarrow G,
\]

where \(G\) is finitely presented, flat over \(T\), and has support proper over \(T\). Two quotients are equivalent if there is an isomorphism of their targets respecting the surjections. Equivalently, their kernels are equal. An automorphism respecting a surjection is the identity. Pullback preserves surjectivity, finite presentation and flatness, and proper support remains proper after base change, so this defines a functor.

The Hilbert functor is the special case \(E=\mathcal O_X\). A submodule \(I\subset\mathcal O_{X_T}\) is an ideal, and its quotient is \(\mathcal O_Z\) for the corresponding closed subscheme \(Z\subset X_T\). Thus

\[
\operatorname{Hilb}_{X/S}(T)=
\{Z\subset X_T\text{ closed}\mid Z\to T
\text{ is proper, flat and of finite presentation}\}.
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
[Z_i,Z_j]=0,\qquad f_a(Z_1,\ldots,Z_n)=0,
\qquad m_j(Z_1,\ldots,Z_n)e_1=e_j.
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
a'=d^2a-c^2-bcd,\qquad b'=2c+bd,
\qquad c'=-c/d,\qquad d'=1/d.
\]

These changes are inverse to the analogous changes with primed variables. They are valid in every characteristic, including characteristic two. Both charts are smooth affine four-spaces, so the glued scheme is smooth of dimension four. \(\square\)

At a double point the parameter \(d\) records a tangent direction of finite slope. The other chart records the missing vertical direction. The collision is therefore a point of a projective line of possible tangent directions, rather than a single undifferentiated diagonal point.

## 7 A smooth curve: unordered divisors are the Hilbert scheme

**Theorem 7.1.** Let \(C\) be a smooth separated curve of finite type over a field \(k\), with all components of dimension one. Then

\[
\operatorname{Hilb}^d(C)\simeq\operatorname{Sym}^d(C)=C^d/\mathfrak S_d.
\]

This is an isomorphism of schemes, in every characteristic. Both schemes are smooth of dimension \(d\), component by component.

**Proof.** We give the scheme-theoretic argument, since a bijection of divisors over algebraically closed fields would not prove the theorem.

First, the required schemes exist and are finite type. A regular irreducible curve is either affine or projective [Stacks, Tag 0A27], and removing a closed point from a regular projective curve gives an affine open, as in the proof of that tag. Every finite set of points therefore has a common affine neighbourhood. There is even a finite cover sufficient for the length-\(d\) Hilbert functor: on a projective component choose \(d+1\) distinct closed points \(q_j\); any support of at most \(d\) points misses one of them and is contained in \(C\setminus\{q_j\}\). There are infinitely many closed points on a curve, so such a choice is possible. Smooth components are disjoint, and there are only finitely many of them; take the finitely many corresponding combinations of affine opens. Proposition 5.1 then gives a finite-type Hilbert scheme.

For the symmetric quotient, the invariant opens \(U^d\), with \(U\) a common affine neighbourhood of a finite set of points of \(C\), cover \(C^d\). On \(U^d=\operatorname{Spec}B\), use \(\operatorname{Spec}B^{\mathfrak S_d}\). Every element \(b\in B\) is integral over the invariant ring, since it satisfies \(\prod_\sigma(T-\sigma b)\). Finite generation of \(B\) makes this a finite ring extension; the invariant ring is finitely generated over \(k\) by the finite-extension form of the Artin–Tate lemma. Its geometric fibres are the finite orbits: invariant functions separate distinct finite orbits, by multiplying suitable separating functions and their translates. Images of invariant open subsets are open, because the finite quotient is closed and the complement is invariant. These affine quotients therefore glue, with their usual categorical universal property for invariant maps to schemes. This constructs \(\operatorname{Sym}^d C\).

Over \(C^d\), sum the \(d\) graph divisors in \(C\times C^d\). A graph of a section of a smooth relative curve is Cartier; locally its equation is a relative parameter. The sum is defined by the product of the graph ideals. On a geometric fibre it is the divisor consisting of the chosen points with their multiplicities. It is a relative effective Cartier divisor: the product remains a nonzerodivisor on every curve fibre, and the fibrewise Cartier criterion [Stacks, Tag 062Y] gives flatness. Its support is a finite union of graphs; hence the divisor is proper with finite fibres, and is finite locally free of degree \(d\). It defines an invariant map \(C^d\to\operatorname{Hilb}^d C\), and the categorical quotient gives

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
\widehat{\mathcal O}_{\operatorname{Sym}^d C,D}
=k[[u_{i,1},\ldots,u_{i,d_i}]]^{\prod_i\mathfrak S_{d_i}}
=k[[e_{i,1},\ldots,e_{i,d_i}]],
\]

where \(e_{i,j}\) is the \(j\)-th elementary symmetric polynomial in the \(i\)-th cluster. The final equality holds in every characteristic: apply the fundamental theorem of symmetric polynomials to each homogeneous degree of a symmetric series and pass to completion. Its weighted-degree topology agrees with the power-series topology, since all the weights \(j\) are positive. No averaging by the order of the group is used.

The sum-divisor morphism \(a\) takes \(a_{i,j}\) to \((-1)^j e_{i,j}\), by expanding \(\prod_l(u_i-u_{i,l})\). It is therefore an isomorphism of these completed local rings. The formal criterion for an étale morphism of finite-type schemes over a field makes \(a\) étale at each closed point. The non-étale locus is closed and, if nonempty, has a closed point, so \(a\) is étale everywhere. An étale morphism injective on geometric points is a universally injective open immersion; since it is also surjective on geometric points, it is an isomorphism. These are the standard étale and completion criteria recalled among the prerequisites below.

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

Now take any Hilbert family \(Z\subset\mathbb P(V)_T\) of this polynomial. Its fibres are Cartier divisors by the field argument. Since \(Z\to T\) is flat and finitely presented and projective space is flat and finitely presented, the fibrewise Cartier criterion [Stacks, Tag 062Y] makes \(Z\) a relative effective Cartier divisor. Its ideal \(I\) is invertible and flat over \(T\), with \(I(d)_t=\mathcal O\) on every fibre. Proper flat cohomology gives

\[
N=p_*I(d)
\]

locally free of rank one, compatible with base change. The evaluation \(p^*N\to I(d)\) is an isomorphism: it is so on every fibre, hence is surjective by Nakayama, and a surjection between invertible sheaves is an isomorphism. Pushing its inclusion in \(\mathcal O(d)\) to the base gives

\[
N\hookrightarrow\operatorname{Sym}^dV\otimes\mathcal O_T.
\]

This is a line subbundle. Its fibre is the nonzero equation line, so locally one coefficient is a unit and the inclusion splits with locally free cokernel. It is therefore exactly a \(T\)-point of \(\mathbb P((\operatorname{Sym}^dV)^\vee)\).

Conversely, a line subbundle \(N\) in this vector bundle evaluates as \(p^*N\otimes\mathcal O(-d)\to\mathcal O\). On every field fibre it is a nonzero equation in a polynomial ring, and hence a nonzerodivisor. Its zero scheme is locally principal with Cartier fibres, so the same criterion gives a relative effective Cartier divisor flat over \(T\). Its ideal sequence yields polynomial \(P_d\). The two constructions are inverse, including on arbitrary nonreduced test schemes, proving the proposition. \(\square\)

This parameter space is all hypersurfaces, not just the smooth locus. Smooth hypersurfaces form an open subfunctor inside it. The use of the dual in the parameter space is forced by the quotient convention: equations are sublines of the space of sections.

## 9 Two points on a smooth surface

The exceptional divisor of a blow-up records the extra information needed when two points meet: a tangent direction. This statement includes the scheme structure of the parameter space, and remains valid in characteristic two.

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

For a general separated surface, existence of the geometric categorical quotient \(Q=B/\mathfrak S_2\) as a separated algebraic space, and finiteness of \(B\to Q\), are the finite-group case of Keel–Mori, *Quotients by groupoids*, Corollary 1.2 and Lemma 6.3. Algebraicity of the Hilbert functor is [Stacks, Tag 0D01]. For a quasi-projective surface the quotient may instead be constructed from invariant affine neighbourhoods of finite orbits, exactly as in Section 7. The invariant family descends to a morphism \(q:Q\to\operatorname{Hilb}^2_S\).

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

The polynomial \(3t+1\) gives another useful warning about components. Over an algebraically closed field of any characteristic, the closure of the locus of twisted cubics in \(\operatorname{Hilb}^{3t+1}_{\mathbb P^3}\) is a smooth irreducible projective component of dimension \(12\). There is a second smooth component of dimension \(15\); their intersection is smooth of dimension \(11\), and the entire Hilbert scheme is singular there. We use this as a stated classification theorem: Heinrich–Skjelnes–Stevens, *The space of twisted cubics*, Proposition A.1 and Remark A.2. The latter supplies the characteristic-two and characteristic-three extension of the original Piene–Schlessinger theorem. The boundary classification is not needed for the existence proof above.

One can see the dimension of the open twisted-cubic locus directly. Every smooth rational normal cubic is the image of \(\mathbb P^1\) under its complete linear system \(\mathcal O(3)\), followed by a projective change of coordinates. Its stabilizer in \(\operatorname{PGL}_4\) is \(\operatorname{PGL}_2\): restriction gives an automorphism of the curve, and each such automorphism acts on \(H^0(\mathcal O(3))\); an element restricting to the identity fixes four independent evaluation vectors and their further linear combinations, so is scalar. The orbit dimension is \(15-3=12\). This calculation alone does not prove that its compactification is smooth; that is the content of the stated classification.

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
a'=d^2a-c^2-bcd,\qquad b'=2c+bd,
\qquad c'=-c/d,\qquad d'=1/d.
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

## 12 What this lesson does not prove

The uniform regularity, projective flattening, Grassmannian representation and Plücker results are proved in the preceding lessons. The foundational inputs used here are the following, with their precise scope.

- Proper pushforward of a finitely presented sheaf flat over an arbitrary base is locally computed by a finite complex of finite locally free modules, compatibly with base change, in the proper finitely presented setting [Stacks, Tag 0A1H]. Its vanishing consequences were derived in *Flattening stratifications*.
- Faithfully flat descent for quasi-coherent modules and quotients is [Stacks, Tag 023R]; descent of finite presentation, properness and flatness is [Stacks, Tags 02L0–02L2]. The sheaf argument in Section 1 applies these results to kernels.
- The Noetherian discrete-valuation criterion for properness is [Stacks, Tag 0208]. We use it only for the finite-type separated morphism over a Noetherian base obtained above.
- Artin–Tate [Stacks, Tag 00IS], flatness and faithful flatness of Noetherian completion [Stacks, Tags 00MB–00MC], and the étale open-immersion criteria [Stacks, Tags 02GV, 02LC and 05W5] are commutative-algebra and descent inputs. The effect of completion on the invariant rings and its use in the curve and surface morphisms were explained above.
- A smooth separated finite-type curve has affine neighbourhoods of finite sets: an irreducible regular curve is affine or projective, and removing a closed point from the latter is affine [Stacks, Tag 0A27]. Also \(\operatorname{Pic}(\mathbb P^n_k)=\mathbb Z\) for \(n\geq1\) [Stacks, Tag 0BXJ]. The relative fibrewise Cartier criterion is [Stacks, Tag 062Y].
- For a separated finitely presented morphism \(X\to S\) and a quasi-coherent source \(E\), the Quot functor above is an algebraic space [Stacks, Tag 09TU]; if \(E\) is finitely presented, it is locally of finite presentation over \(S\). The Hilbert functor is an algebraic space locally of finite presentation [Stacks, Tag 0D01]. These are Artin-style algebraicity theorems. Our projective scheme construction is independent of their proofs; the general surface example uses the Hilbert-space statement.
- More generally, let \(X\to S\) be a proper morphism of finite presentation of algebraic spaces, let \(E\) be finitely presented, and let \(L\) be relatively ample. For a fixed polynomial \(P\), the algebraic space \(\operatorname{Quot}^{P,L}_{E/X/S}\) is proper over \(S\) [Stacks, Tag 0DPC]. The base need not be Noetherian. This general statement is imported; Theorem 4.1 proves properness directly for the projective Noetherian scheme setting used in our construction.
- For a finite group acting on a separated finite-type scheme over a field, the geometric categorical quotient exists as a separated algebraic space and its quotient morphism is finite. This is the finite-group specialization of Keel–Mori, *Quotients by groupoids*, Corollary 1.2 and Lemma 6.3. Only existence outside the affine-neighbourhood situation is imported in Proposition 9.1; the identification with the two-point Hilbert space is proved here.
- The compactified twisted-cubic component and the other component, with the dimensions and intersection stated in Section 10, are Heinrich–Skjelnes–Stevens, *The space of twisted cubics*, Proposition A.1 and Remark A.2. We do not reproduce their boundary classification. The cubic-surface degree and tangent assertion is proved in the later tangent–obstruction lesson.

The fixed-polynomial projectivity theorem has been proved with a possibly nonflat coherent source. The general algebraic-space theorem does not by itself imply projectivity, and the coproduct over all polynomials need not be of finite type.

## References

- Grothendieck, *Techniques de construction et théorèmes d'existence en géométrie algébrique IV: les schémas de Hilbert*, Séminaire Bourbaki, Exposé 221, §§3–4. [Original text](https://www.numdam.org/item/SB_1960-1961__6__249_0/).
- Nitsure, *Construction of Hilbert and Quot schemes*, §§3–5. [Author's paper](https://arxiv.org/abs/math/0504590).
- The Stacks project: [Quot and Hilbert spaces](https://stacks.math.columbia.edu/tag/082L), particularly Tags 09TU and 0D01; [properness criterion](https://stacks.math.columbia.edu/tag/0208); [relative Cartier criterion](https://stacks.math.columbia.edu/tag/062Y). The tagged results are read in the AI Integrated Stacks Project edition.
- Keel and Mori, *Quotients by groupoids*, Corollary 1.2, Proposition 5.1 and Lemma 6.3. [Author's paper](https://arxiv.org/abs/alg-geom/9508012).
- Heinrich, Skjelnes and Stevens, *The space of twisted cubics*, Épijournal de Géométrie Algébrique **5** (2021), Article 10, Appendix A. [Published paper](https://epiga.episciences.org/7539).
