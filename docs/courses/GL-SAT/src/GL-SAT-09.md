# Tannakian categories

*Written by GPT-6.1 Sol (OpenAI), October 2026. Public domain (CC0).*

A group can be recovered from the linear transformations that act compatibly on all its representations. The compatibility includes every subobject and every tensor product. We construct the coordinate Hopf algebra from those finite-dimensional constraints, prove the reconstruction over all parameter algebras, and then translate generation properties into properties of the group.

A rigid symmetric monoidal category has an associative tensor product, a unit, a coherent symmetry, and evaluation and coevaluation maps satisfying the two duality triangles for every object. A neutral fibre functor is an exact faithful linear functor to finite-dimensional vector spaces that preserves the tensor product, unit and ordinary symmetry. No semisimplicity is included in this definition.

The preceding fusion lesson constructs these tensor and symmetry hypotheses for the classical Satake heart with characteristic-zero coefficients. Convolution and rigidity proves its duality triangles. We first prove reconstruction for an arbitrary field and arbitrary category satisfying the neutral hypotheses; identifying the resulting Satake group requires additional geometry.

## 1. The neutral hypotheses and reconstruction statement


Let \(k\) be a field. Let \(\mathcal C\) be an essentially small, \(k\)-linear abelian category with a symmetric monoidal structure, unit \(\mathbf1\), and duals for every object. Assume \(\operatorname{End}(\mathbf1)=k\). Let
\[
\omega:\mathcal C\longrightarrow\operatorname{Vect}^{\mathrm{fd}}_k
\]
be faithful, exact, \(k\)-linear, and strong symmetric monoidal. We construct a commutative Hopf algebra \(B\), prove that
\[
\mathcal C\simeq\operatorname{Comod}^{\mathrm{fd}}_B
   =\operatorname{Rep}^{\mathrm{fd}}_k(\operatorname{Spec}B),
\tag{1}
\]
and prove, for every commutative \(k\)-algebra \(R\), including rings with nilpotents,
\[
\operatorname{Hom}_{k\text{-alg}}(B,R)
 =\operatorname{Aut}^{\otimes}(R\otimes_k\omega).
\tag{2}
\]
No semisimplicity, characteristic restriction, finite tensor generator, or previously reconstructed group is assumed.

We first forget the tensor product. Exactness and faithfulness imply that \(\omega\) reflects zero objects, monomorphisms, epimorphisms, and isomorphisms: apply it to the appropriate kernel and cokernel. For any \(X,Y\), it embeds \(\operatorname{Hom}(X,Y)\) into \(\operatorname{Hom}_k(\omega X,\omega Y)\), so Hom spaces are finite dimensional. Every strict chain of subobjects of \(X\) gives a strict chain of subspaces of \(\omega X\). In particular every object has finite length, and an intersection of any family of subobjects of one object equals an intersection of finitely many members. To see the last statement, choose a finite intersection whose image has least dimension; intersecting any additional member cannot reduce that dimension, hence does not change the subobject.

For a finite vector space \(W\), the copower \(W\otimes_k X\) exists. Choose a basis to form a finite sum of copies of \(X\); the universal property
\(\operatorname{Hom}(W\otimes X,Y)=\operatorname{Hom}_k(W,\operatorname{Hom}(X,Y))\)
makes this construction independent of its basis. Exactness of finite sums and of \(\omega\) identifies its image with \(W\otimes\omega X\).

## 2. The finite algebra attached to one object

Fix \(X\), put \(V=\omega X\), and set \(H_X=V^*\otimes X\). Its image is canonically \(\operatorname{End}_k(V)\). Define
\[
A_X=\{a\in\operatorname{End}_k(V):
 a^{\oplus n}(\omega Y)\subset\omega Y
 \text{ for every }n\ge0\text{ and }Y\subset X^{\oplus n}\}.
\tag{3}
\]
It is a finite dimensional unital algebra: preserving subspaces is stable under sums, scalars, compositions, and the identity.

These constraints are images of actual subobject conditions. For \(Y\subset X^{\oplus n}\), compose evaluation with the quotient to obtain
\[
H_X\otimes_k\omega Y\longrightarrow X^{\oplus n}/Y.
\]
Choosing a basis of \(\omega Y\) turns it into one map from \(H_X\) to a finite sum of this quotient. Its kernel has image precisely the endomorphisms preserving \(\omega Y\). Intersect these kernels. The finite-length observation makes the intersection an actual subobject \(P_X\subset H_X\), and exactness gives
\[
\omega P_X=A_X.
\tag{4}
\]

There is a useful intrinsic description: \(P_X\) is the smallest subobject of \(H_X\) whose image contains \(1_V\). Such a smallest subobject \(Q\) exists by finite intersections; the intersections still contain \(1_V\). Since \(1_V\in A_X\), we have \(Q\subset P_X\). Conversely, regard \(Q\subset H_X\) as a subobject of a finite copower of \(X\). Every \(a\in A_X\) preserves \(\omega Q\) under its diagonal action. In the identification \(\omega H_X=\operatorname{End}(V)\), that action is left composition. Consequently \(a=a1_V\in\omega Q\), so \(A_X\subset\omega Q\). A subspace containment between images of subobjects reflects to containment of subobjects: the composite to the quotient has zero image under the faithful functor. Thus \(P_X\subset Q\), proving the description.

Right composition by \(a\in A_X\) defines a morphism \(H_X\to H_X\) by its action on the coefficient space \(V^*\). It preserves \(P_X\), because its image under \(\omega\) maps \(A_X\) to \(A_Xa\subset A_X\), and the quotient test just used detects this factorization. The multiplication and identity relations are checked by \(\omega\). Hence \(P_X\) is a right \(A_X\)-module object with image the right regular module.

Let \(\mathcal C_X\) be the full subcategory consisting of subquotients of finite sums of \(X\). It is closed under finite sums, kernels, and cokernels. Thus it is abelian with exact inclusion in \(\mathcal C\). We do not assert it is closed under every extension in \(\mathcal C\).

Every \(\omega Z\), \(Z\in\mathcal C_X\), has a natural left \(A_X\)-action. Present \(Z=Y/Y'\) with \(Y'\subset Y\subset X^{\oplus n}\), and use (3) to induce the diagonal action on its quotient. This is independent of the presentation, and every morphism commutes with it. Here is a direct check that avoids assuming fullness: for \(f:Z\to Z'\), its graph is a subobject of \(Z\oplus Z'\). Pull it back to subobjects of finite sums of \(X\); all these subobjects are preserved by (3). The induced action therefore preserves the graph, which is exactly commutation with \(\omega f\). Apply the same graph argument to identity maps between two presentations.

For a finite left \(A_X\)-module \(M\), form the object
\[
L_X(M)=P_X\otimes_{A_X}M
\tag{5}
\]
as the cokernel of the two action maps
\(P_X\otimes_k A_X\otimes_k M\rightrightarrows P_X\otimes_k M\).
It belongs to \(\mathcal C_X\), and exactness gives a natural isomorphism
\[
\omega L_X(M)=A_X\otimes_{A_X}M=M.
\tag{6}
\]
Comparison (6) is also \(A_X\)-linear: the left action on the first factor is \(b(a\otimes m)=ba\otimes m\), and multiplication sends this to \(bam\). Its inverse is \(m\mapsto1\otimes m\). Both maps are natural in every module homomorphism. In particular \(L_X\) is exact: apply \(\omega\) to the kernel and cokernel of the homology of the resulting finite sequence.

Evaluation defines \(P_X\otimes_{A_X}V\to X\), and its image is the regular-module multiplication isomorphism. Thus it is an isomorphism. For a subobject \(Y\subset X^{\oplus n}\), evaluation restricted to \(P_X\otimes_k\omega Y\) factors through \(Y\): its composite to \(X^{\oplus n}/Y\) has zero image by (3). It is balanced, so gives
\(L_X(\omega Y)\to Y\), an isomorphism by (6). For \(Y'\subset Y\), pass to the quotient, using exactness of \(L_X\). This gives an isomorphism
\[
L_X(\omega Z)\longrightarrow Z
\tag{7}
\]
for every \(Z\in\mathcal C_X\). The graph argument proves naturality: two proposed composites have the same image, so faithfulness makes them equal. Equations (6)–(7) prove an equivalence
\[
\mathcal C_X\simeq\operatorname{Mod}^{\mathrm{fd}}(A_X)
\tag{8}
\]
whose forgetful functor is \(\omega\). Fullness and essential surjectivity have both been proved, not assumed. Moreover \(L_X(A_X)=P_X\), and the equivalence gives \(\operatorname{Hom}_{\mathcal C_X}(P_X,Z)=\operatorname{Hom}_{A_X}(A_X,\omega Z)=\omega Z\). Thus \(P_X\) is a projective generator of this finite subcategory: finite module generators give epimorphisms from finite sums of \(P_X\). This says nothing about its projectivity in the entire category. Its object endomorphism ring is \(A_X^{\mathrm{op}}\), whereas the natural-endomorphism algebra in (9) is \(A_X\).

Natural endomorphisms of the forgetful functor on finite left \(A_X\)-modules are precisely left multiplication by elements of \(A_X\). Indeed naturality on the regular module with its right-multiplication maps makes an endomorphism left multiplication by its value at 1. The maps \(A_X\to M\), \(a\mapsto am\), then force its value on every \(M\). Therefore
\[
A_X=\operatorname{End}(\omega|_{\mathcal C_X}).
\tag{9}
\]

## 3. Compatible finite coalgebras

The subcategories \(\mathcal C_X\) are directed: \(\mathcal C_X\) and \(\mathcal C_Y\) lie in \(\mathcal C_{X\oplus Y}\). When \(\mathcal C_X\subset\mathcal C_{X'}\), restriction of (9) is an algebra homomorphism \(A_{X'}\to A_X\). It is surjective, as follows.

Under (8) for \(X'\), write \(V=\omega X\) and let \(D\) be the image of \(A_{X'}\) in \(\operatorname{End}(V)\). The module \(V\) is faithful over \(D\). If \(v_1,\ldots,v_d\) is a basis, the map
\[
D\longrightarrow V^{\oplus d},\qquad a\longmapsto(av_i)_i
\]
is injective and \(D\)-linear. Every finite \(D\)-module is a quotient of a finite sum of regular modules, so is a subquotient of a finite sum of \(V\). Conversely, every such subquotient is annihilated by the kernel \(A_{X'}\to D\). Hence \(\mathcal C_X\) corresponds exactly to all finite \(D\)-modules. Their natural-endomorphism algebra is \(D\), by the regular-module proof. Equation (9) identifies it with \(A_X\), proving surjectivity.

Dualize the finite algebras to coalgebras \(B_X=A_X^*\). The transition maps are injective coalgebra maps. Put
\[
B=\varinjlim_X B_X.
\tag{10}
\]
The left \(A_X\)-module structure on \(\omega Z\) is equivalent to a right \(B_X\)-coaction: for dual bases \(a_i,b_i\), the formula is
\(v\mapsto\sum_i a_i v\otimes b_i\).
Associativity and unit are precisely the coassociativity and counit equations. Compatibility under restriction makes these into \(B\)-coactions, defining a functor \(\mathcal C\to\operatorname{Comod}^{\mathrm{fd}}_B\).

Every finite \(B\)-comodule comes from one \(B_X\). Choose a vector-space basis and include its finitely many coaction coefficients in one stage; the counit and coassociativity equations already hold there because its inclusion into \(B\) is injective. Equivalence (8) supplies its object. For two objects, include both in one \(\mathcal C_X\); a \(B\)-comodule map is a \(B_X\)-comodule map, since the stage inclusion is injective. Fullness of (8) supplies the morphism. This proves the coalgebra version of (1).

## 4. Matrix coefficients and the tensor product

There is a presentation particularly suited to the tensor structure. Take the direct sum of \((\omega X)^*\otimes\omega X\) over a small skeleton, and impose the relations
\[
[\xi,\omega(f)v]_Y=[\xi\circ\omega(f),v]_X
\quad(f:X\to Y).
\tag{11}
\]
Denote the resulting vector space by \(Q\). For \(\mathcal C_X\) alone, the dual of this quotient is exactly the space of natural endomorphisms of its forgetful functor, by the pairing \(\xi(a_Xv)\). It is \(A_X\) by (9). Since a vector space with finite dimensional dual is finite dimensional (extend a basis and choose coordinate functionals), this coefficient quotient is canonically \(A_X^*=B_X\). The canonical map is evaluation on natural endomorphisms. Matrix coefficients of \(X\) span it: dualize the inclusion \(A_X\subset\operatorname{End}(\omega X)\).

Every finite collection of objects and morphisms in (11) lies in one of the directed \(\mathcal C_X\). Thus the global presentation is their filtered colimit, and identifies \(Q\) with \(B\). For a basis \(v_i\) and its dual \(\xi_i\), write \(b_{ij}=[\xi_i,v_j]_X\). The coalgebra formulas are
\[
\Delta(b_{ij})=\sum_h b_{ih}\otimes b_{hj},
\qquad\epsilon(b_{ij})=\delta_{ij}.
\tag{12}
\]
They agree with the dual-algebra construction and show directly that (11) respects the coalgebra operations.

Use the strong tensor isomorphisms of \(\omega\) to define
\[
[\xi,v]_X[\eta,w]_Y
  =[\xi\otimes\eta,v\otimes w]_{X\otimes Y}.
\tag{13}
\]
Relation (11) is respected in each variable by \(f\otimes1\) and \(1\otimes f\), so this is well defined. The coefficient of the unit is the multiplicative unit. Associativity follows from naturality for the associator and the strong monoidal compatibility of \(\omega\). The symmetry constraint and the ordinary vector-space interchange prove commutativity. Formula (12), applied to a tensor-product basis, proves that \(\Delta\) and \(\epsilon\) are algebra homomorphisms. Hence \(B\) is a commutative bialgebra.

Duality gives the antipode. Identify \(\omega(X^\vee)=(\omega X)^*\), and write \(\operatorname{ev}_v\) for evaluation at \(v\). Set
\[
S([\xi,v]_X)=[\operatorname{ev}_v,\xi]_{X^\vee}.
\tag{14}
\]
Naturality for the dual morphism makes this respect (11). The evaluation and coevaluation morphisms give, on a basis, respectively
\[
\sum_h S(b_{ih})b_{hj}=\delta_{ij}1,
\qquad
\sum_h b_{ih}S(b_{hj})=\delta_{ij}1.
\tag{15}
\]
To verify the first equation directly, evaluate the tensor coefficient on the invariant pairing \(X^\vee\otimes X\to\mathbf1\); contraction of the middle dual basis is \(\xi_i(v_j)\). The second follows by applying the invariant coevaluation \(\mathbf1\to X\otimes X^\vee\) and contracting the other pair. These are the two antipode identities, so \(B\) is a Hopf algebra. Formula (13) makes the equivalence in (1) symmetric monoidal; formula (14) makes it preserve duals.

## 5. The automorphism functor on every test algebra

Let \(R\) be any commutative \(k\)-algebra. A linear map \(\varphi:B\to R\) gives a natural \(R\)-linear endomorphism \(a_X\) of \(R\otimes\omega X\) through
\[
\xi(a_Xv)=\varphi([\xi,v]_X).
\tag{16}
\]
Conversely every such natural endomorphism defines a map from the coefficient direct sum, and naturality is exactly (11), so it descends uniquely to \(B\). This argument is over arbitrary \(R\), rather than a comparison of field-valued points.

Tensor compatibility and the unit condition say exactly that \(\varphi\) is a unital algebra homomorphism, by (13). For such a homomorphism the natural endomorphism is invertible: use the coefficients \(\varphi(S(b_{ij}))\) for its inverse and apply (15). Hence (16) gives (2). Compatibility with base change in \(R\) is immediate from the coefficient formulas. Therefore the affine group scheme \(G=\operatorname{Spec}B\) represents the tensor automorphism functor, and (1) is the requested neutral reconstruction theorem. The bijection respects group multiplication: matrix multiplication has entries \(\sum_h\varphi(b_{ih})\psi(b_{hj})\), exactly convolution through \(\Delta\); the inverse is represented by \(S\). A finite comodule coefficient matrix defines a morphism \(G\to GL(V)\), since its antipode matrix is the inverse and comultiplication is the group-law equation. Conversely a group-scheme representation has coefficient functions satisfying these equations and hence defines a coaction. The same coefficient equations identify morphisms. This proves the representation/comodule equality used in (1), including the tensor structures.

Reconstruction does not by itself make \(G\) reductive, connected, smooth, or of finite type. Those properties require additional categorical arguments in geometric Satake. Reconstruction alone must not be used to supply them.

## 6. Finite coefficients and generators

We need an elementary finiteness fact for arbitrary coalgebras. If \(A\) is a coalgebra and \(a\in A\), write \(\Delta(a)=\sum_i a_i\otimes b_i\) with the \(b_i\) linearly independent. Coassociativity shows that \(W=\operatorname{span}(a_i)\) satisfies \(\Delta(W)\subset W\otimes A\): project the first factor of the coassociativity identity to \(A/W\), and use independence in its third factor. Counitality puts \(a\) in \(W\). Sums of these subspaces put every finite subset in a finite-dimensional regular right subcomodule.

For a finite right comodule \(V\), choose a basis and write
\[
\rho(v_j)=\sum_i v_i\otimes c_{ij},\qquad
C(V)=\operatorname{span}_k\{c_{ij}\}.
\tag{17}
\]
The coefficient space is a finite subcoalgebra, since
\(\Delta(c_{ij})=\sum_h c_{ih}\otimes c_{hj}\) and \(\epsilon(c_{ij})=\delta_{ij}\).
The coaction gives an injective comodule map
\[
V\hookrightarrow V_{\mathrm{triv}}\otimes C(V)
          \simeq C(V)^{\oplus\dim V}.
\tag{18}
\]
Injectivity follows by applying the counit. The maps \(v\mapsto(\xi\otimes1)\rho(v)\), for a basis of \(V^*\), together give a surjective comodule map
\[
V^{\oplus\dim V}\twoheadrightarrow C(V).
\tag{19}
\]
Indeed their images span exactly the coefficients in (17).

Adapted bases give the following identities and containment:
\[
\begin{aligned}
C(V\oplus W)&=C(V)+C(W),\\
C(V\otimes W)&=\operatorname{span}_k(C(V)C(W)),\\
C(V^\vee)&=S(C(V)),\\
C(U)&\subset C(V)\quad\text{if }U\text{ is a subquotient of }V.
\end{aligned}
\tag{20}
\]
For the last assertion, put a subobject first in a basis. Its matrix is a diagonal block of the original matrix; the quotient matrix is the other diagonal block. The tensor identity follows by multiplying entries, and the dual identity follows from the inverse matrix (15).

Every element of a Hopf algebra \(A\) belongs to some \(C(V)\). Apply the preceding coalgebra construction to its regular comodule, choose a basis \(v_i\) of the resulting finite \(V\subset A\), and apply \(\epsilon\otimes1\) to \(\Delta(v_j)=\sum_i v_i\otimes c_{ij}\). It gives \(v_j=\sum_i\epsilon(v_i)c_{ij}\). Thus
\[
A=\bigcup_V C(V).
\tag{21}
\]
The union is directed by direct sums.

Call \(X\) a **tensor generator** if every object is a subquotient of a finite sum of tensor words in \(X,X^\vee\), including the empty word \(\mathbf1\).

**Theorem 6.1.** The reconstructed affine group \(G\) is of finite type over \(k\) if and only if \(\mathcal C\) has a tensor generator. Such a generator gives a closed immersion \(G\hookrightarrow GL(\omega X)\).

**Proof.** If \(X\) generates, (20)–(21) show that its coefficients and their antipodes generate the coordinate algebra \(B\). There are finitely many of them. The dual coefficients are entries of the inverse matrix, so they belong to the image of \(k[GL(\omega X)]\). This coordinate map is surjective, which proves the closed immersion and finite type.

Conversely suppose \(B\) is finitely generated as an algebra. Put a finite set of algebra generators in one finite regular subcomodule \(X\subset B\), using the coalgebra construction. The calculation proving (21) puts those generators in \(C(X)\). Thus \(B=k[C(X)]\). For any finite comodule \(M\), its finite coefficient space lies in the span of products of at most \(N\) entries from \(C(X)\), for some finite \(N\). By (20), this is
\[
C\left(\bigoplus_{r=0}^{N}X^{\otimes r}\right).
\]
Embedding (18) puts \(M\) in a finite sum of this coefficient comodule. Surjection (19) makes that coefficient comodule a quotient of a finite sum of the displayed tensor words. Taking the inverse image of \(M\) under this surjection exhibits it as a subquotient of those words. This proves tensor generation in every characteristic. \(\square\)

Call \(X\) an **additive generator** if every object is a subquotient of \(X^{\oplus n}\) for some finite \(n\).

**Theorem 6.2.** The affine group scheme \(G\) is finite over \(k\) if and only if \(\mathcal C\) has an additive generator.

**Proof.** If \(X\) is an additive generator, (20) puts every coefficient in the one finite space \(C(X)\); (21) therefore makes \(B=C(X)\) finite dimensional. Conversely if \(B\) is finite dimensional, its regular comodule is an object, and every finite comodule embeds in \(B^{\oplus\dim M}\) by its coaction. Thus \(B\) is an additive generator. Finite dimensionality of the coordinate algebra is exactly finiteness of the affine scheme over the field. This criterion concerns the scheme, including its nilpotents; it is not a count of rational points. \(\square\)

## 7. Why Hopf inclusions are faithfully flat

An injective homomorphism of arbitrary rings need not be flat. The group structure supplies the missing argument for commutative Hopf algebras.

**Lemma 7.1.** An inclusion \(B\subset A\) of commutative Hopf algebras over a field makes \(A\) faithfully flat as a \(B\)-module, without finite type or reducedness assumptions.

**Proof in finite type.** Write \(G=\operatorname{Spec}A\), \(H=\operatorname{Spec}B\), and \(K=\ker(G\to H)\). This is a closed finite-type subgroup, and is flat because its base is a field. We use two exact earlier programme results. Quotients and torsors, Theorem 11.1b proves that \(Q=G/K\) is a finite-type scheme and that \(p:G\to Q\) is an fppf \(K\)-torsor. Its initial algebraic-space quotient is supplied by the proved flat quotient theorem, Corollary 8.3; Theorem 11.1b's subsequent affine-neighbourhood construction proves the scheme assertion. Group schemes over a field, Theorem 5.9 proves that a quasi-compact monomorphism between locally finite-type field groups is a closed immersion, retaining nilpotents in every characteristic.

The induced \(j:Q\to H\) is a monomorphism on every test scheme. To check this, lift two cosets fppf locally to \(g_1,g_2\in G\). Equality of their images in \(H\) says that \(g_1^{-1}g_2\) lies in \(K\), so their cosets agree. Equality descends. Both groups are finite type, so the monomorphism is quasi-compact. The stated theorem makes \(j\) a closed immersion. Every equation of this closed subscheme pulls back to zero in \(A\), whereas \(B\to A\) is injective. Its defining ideal is therefore zero. Thus \(Q=H\), and \(G\to H\) is fppf. Equivalently \(A\) is faithfully flat over \(B\).

**Passage to arbitrary Hopf algebras.** Every commutative Hopf algebra is a filtered union of finitely generated Hopf subalgebras. Given a finite list of elements, the proof of (21) puts them in a finite coefficient coalgebra. Adjoin its finitely many entries and their antipodes. The formulas for their comultiplication, counit and antipode make the generated algebra a Hopf subalgebra. Here \(S^2=1\): applying the representing functor to any commutative test algebra makes \(S\) group inversion, whose square is the identity; taking the universal test algebra proves the algebra identity. Direct sums of finite coefficient comodules make these subalgebras directed.

Consider all pairs of finitely generated Hopf subalgebras \(B_0\subset B\), \(A_0\subset A\) with \(B_0\subset A_0\). They form a filtered system, and multiplication gives a \(B\)-module isomorphism
\[
\varinjlim_{(B_0,A_0)}B\otimes_{B_0}A_0\xrightarrow{\sim}A.
\tag{22}
\]
It is surjective because any element of \(A\) occurs in one \(A_0\). For injectivity take a representative \(\sum_i b_i\otimes a_i\) whose product sum is zero. Enlarge the pair so that all \(b_i\) also belong to its first algebra. In this stage the representative equals \(1\otimes\sum_i b_i a_i=0\). No injectivity of the transition tensor maps is required.

The finite-type proof makes \(A_0\) flat over \(B_0\), so each module \(B\otimes_{B_0}A_0\) is flat over \(B\). A filtered colimit of flat modules is flat: tensor commutes with that colimit, and an element and a relation making its image zero occur at a common stage. The stagewise preservation of a module injection then preserves it in the colimit. Thus (22) proves flatness of \(A/B\).

If a proper ideal \(I\subset B\) satisfied \(IA=A\), write \(1=\sum_i b_i a_i\) with \(b_i\in I\), and include all terms in one such pair. The ideal \((b_i)\subset B_0\) is proper, since its image lies in \(I\). Finite-type faithful flatness contradicts \(1\in(b_i)A_0\). Hence every proper ideal remains proper. For a nonzero \(B\)-module choose a nonzero element; its cyclic submodule is \(B/I\) for a proper ideal. Tensoring preserves its injection by flatness and keeps it nonzero by the ideal assertion. This is faithfulness, completing the proof. \(\square\)

## 8. Morphisms of groups from their representations

Let \(f:G\to H\) be a homomorphism of arbitrary affine group schemes over \(k\), and write \(u:B=k[H]\to A=k[G]\). Restriction of representations is the exact faithful tensor functor \(f^*\), obtained by composing a coaction with \(1\otimes u\).

**Theorem 8.1.** The following criteria hold over every field.

1. \(f\) is faithfully flat if and only if \(f^*\) is fully faithful and every \(G\)-subobject of a restricted \(H\)-representation is an \(H\)-subobject.
2. \(f\) is a closed immersion if and only if every finite-dimensional \(G\)-representation is a subquotient of a restricted \(H\)-representation.

In the first statement a subobject includes its specified inclusion into the representation. If one instead says that it is merely isomorphic to a restricted object, full faithfulness must lift that inclusion.

**Proof of the faithfully flat criterion.** Faithful flatness makes \(u\) injective. A linear map between two restricted comodules is a \(G\)-map exactly when its two coaction composites agree after applying \(u\). The injection \(V\otimes B\hookrightarrow V\otimes A\) detects that equality, so it is already an \(H\)-map. This proves full faithfulness. If \(W\subset V\) is \(G\)-stable, the composite
\[
W\longrightarrow V\otimes B\longrightarrow(V/W)\otimes B
\]
becomes zero after applying \(u\); the same injection shows that it was zero. Thus \(W\) is \(H\)-stable.

Conversely put \(I=\ker u\). It is a Hopf ideal, so \(\epsilon(I)=0\) and
\(\Delta(I)\subset I\otimes B+B\otimes I\).
Suppose \(0\ne a\in I\), choose a finite regular \(B\)-subcomodule \(V\subset B\) containing it, and put \(W=V\cap I\). After composing the second coaction factor with \(u\), the Hopf-ideal identity makes \(W\) a \(G\)-subobject of the restricted \(V\). To see this precisely, \((1\otimes u)\Delta(W)\) lies both in \(V\otimes A\) and in \(I\otimes A\); their intersection is \(W\otimes A\), since tensoring over a field is exact. The subobject hypothesis makes \(W\) a \(B\)-subcomodule, so \(\Delta(W)\subset W\otimes B\). Applying \(\epsilon\otimes1\) gives \(W=0\), because \(\epsilon(W)=0\). This contradicts \(a\in W\). Therefore \(u\) is injective; Lemma 7.1 proves faithful flatness. With inclusions specified, the subobject hypothesis also implies fullness directly by applying it to graphs of \(G\)-maps.

**Proof of the closed-immersion criterion.** If \(u\) is surjective, lift a basis of \(C(M)\) for a finite \(G\)-comodule \(M\) to \(B\). Put these lifts in a finite regular \(H\)-subcomodule \(V\subset B\). Then \(u(V)\subset A\) is a quotient of the restricted \(V\) and contains \(C(M)\). Embedding (18) gives
\[
M\hookrightarrow C(M)^{\oplus\dim M}
 \subset u(V)^{\oplus\dim M}.
\]
Taking its inverse image in \((f^*V)^{\oplus\dim M}\) exhibits the required subquotient. Conversely the coefficients of every subquotient of a restricted representation lie in \(u(B)\), by (20). If this covers every \(G\)-representation, (21) implies \(A=u(B)\). Thus the affine coordinate map is surjective, exactly the closed-immersion condition. \(\square\)

For any neutral category, finite sets of objects and their duals generate tensor subcategories whose coefficient Hopf algebras are finitely generated subalgebras of \(B\). Section 6 proves that their union is \(B\), and Lemma 7.1 now proves that all the corresponding transition morphisms of affine groups are faithfully flat. Thus the reconstructed group is an inverse limit of algebraic groups. Finite type, connectedness and reductivity remain additional properties to establish in an application.

## 9. Graded vectors, finite groups and the symmetry obstruction

### 9.1. Integer gradings reconstruct the multiplicative group

Let \(\mathcal C\) be finite-dimensional \(\mathbb Z\)-graded vector spaces, with degree-preserving maps, the usual tensor grading, and the ordinary symmetry. Let \(k(n)\) denote the one-dimensional object in degree \(n\). Every object is a finite direct sum of these, and \(k(n)\otimes k(m)=k(n+m)\).

For any test algebra \(R\), a natural endomorphism of the forgetful functor must act on the degree \(n\) summand by one scalar \(a_n\in R\). Indeed degree projections force preservation of each summand, and all linear maps within that summand force a scalar; maps from \(k(n)\) determine the same scalar for every object. The tensor and unit conditions give
\[
a_{n+m}=a_n a_m,\qquad a_0=1.
\]
Consequently \(a_1=u\in R^\times\), \(a_{-1}=u^{-1}\), and \(a_n=u^n\). Conversely these formulas give every tensor automorphism. The representing Hopf algebra is therefore
\[
k[z,z^{-1}],\qquad
\Delta(z)=z\otimes z,\quad\epsilon(z)=1,\quad S(z)=z^{-1}.
\tag{23}
\]
The coaction on a vector of degree \(n\) is \(v\mapsto v\otimes z^n\).

To verify the equivalence in the other direction, write any finite Laurent-polynomial coaction uniquely as \(\rho(v)=\sum_n p_n(v)\otimes z^n\), using only finitely many \(n\) for a fixed finite vector-space basis. Coassociativity says \(p_n p_m=0\) for \(n\ne m\) and \(p_n^2=p_n\); the counit says \(\sum_n p_n=1\). Thus their images give a finite grading. Morphisms commute with all these projectors, and tensor degrees add by (23). This proves \(\mathcal C=\operatorname{Rep}(\mathbb G_m)\). The line \(k(1)\) is a tensor generator, but no additive generator exists: a finite graded object has only finitely many degrees, whereas its subquotients and finite sums introduce no new degree.

The same calculation for an abelian group \(L\) gives the diagonalizable group \(D(L)=\operatorname{Spec}k[L]\), with \(\Delta(e^\ell)=e^\ell\otimes e^\ell\). It retains scheme structure in positive characteristic. For example \(L=\mathbb Z/p\mathbb Z\) in characteristic \(p\) gives \(\mu_p\), whose coordinate algebra \(k[z]/(z^p-1)\) is nonreduced.

### 9.2. A finite constant group

Let \(\Gamma\) be a finite abstract group and take its finite-dimensional \(k\)-representations with the usual forgetful functor. They are finite left modules over the finite algebra \(k\Gamma\). The regular module is an additive generator, because a basis of any module gives a surjection from a finite sum of regular modules. The natural-endomorphism calculation of §2 gives \(A=k\Gamma\). Its dual coefficient coalgebra is \(B=(k\Gamma)^*\), the vector space \(k^\Gamma\) of functions on \(\Gamma\).

An element \(g\in\Gamma\) acts on a tensor product by \(g\otimes g\). Dualizing this tensor rule makes multiplication in \(B\) pointwise. Multiplication of group elements gives
\[
\Delta(f)(g,h)=f(gh),\qquad
\epsilon(f)=f(1),\qquad S(f)(g)=f(g^{-1}).
\tag{24}
\]
Thus \(\operatorname{Spec}B\) is the constant group scheme consisting of one copy of \(\operatorname{Spec}k\) for each \(g\in\Gamma\). On a disconnected test algebra its points are locally constant choices of \(g\), as the mutually orthogonal idempotents of \(k^\Gamma\) specify. This is the full scheme reconstruction, not merely recovery of \(\Gamma\) on field-valued points. Nothing in the calculation divides by \(|\Gamma|\); it remains valid when the characteristic divides the group order.

### 9.3. Why super vector spaces require a different symmetry

Suppose \(\operatorname{char}k\ne2\). Super vector spaces are \(\mathbb Z/2\mathbb Z\)-graded spaces with the Koszul symmetry \(v\otimes w\mapsto(-1)^{|v||w|}w\otimes v\). Let \(E\) be the one-dimensional odd line. It is invertible, \(E\otimes E\simeq\mathbf1\), and its self-symmetry is \(-1_{E\otimes E}\).

If a symmetric fibre functor \(\omega\) to ordinary vector spaces existed, \(\omega E\) would be invertible there. Its dimension has square one, so it is a one-dimensional space. Ordinary interchange on its tensor square is the identity, whereas \(k\)-linearity sends the self-symmetry of \(E\) to minus the identity. Strong symmetric compatibility identifies these two maps, a contradiction in characteristic different from two. The usual forgetful functor is exact, faithful and tensor, but fails this symmetry condition.

In characteristic two this obstruction disappears: the Koszul signs equal one. The same graded category is then \(\operatorname{Rep}(\mu_2)\), by §9.1 with \(L=\mathbb Z/2\mathbb Z\). The characteristic hypothesis is essential. This example explains why the sign-adjusted symmetry of Lesson 8, §7 matters when ordinary cohomology becomes the Satake fibre functor.

## 10. Reductivity and the boundary of neutral reconstruction

### 10.1. The connected characteristic-zero dictionary

**Theorem 10.1.** Let \(G\) be a connected affine group scheme over a characteristic-zero field. Its finite-dimensional representation category is semisimple if and only if \(G\) is pro-reductive. Here this means that its canonical finite-type quotient groups are reductive, or equivalently that it is the inverse limit of those connected reductive algebraic groups with faithfully flat transition maps. For a finite-type connected group, the condition is simply reductivity.

**Proof.** First consider a connected finite-type affine group. The proved Cartier theorem, AG-GS-02, Theorem 4.3 makes it smooth. The complete smooth connected classification in AG-GS-01, Theorem 5.22 proves reductivity equivalent to exact invariants. Its characteristic-zero direction uses the proved Weyl complete-reducibility theorem and the central-isogeny structure of a reductive group. For the converse, the unipotent fixed-vector input can be supplied directly by AG-RG-01, Lemma 2.A: a unitriangular subgroup has a trivial-quotient flag on every representation, so every nonzero representation has a fixed vector. Normality then makes an irreducible representation trivial on the unipotent radical, and a faithful representation forces that radical to be trivial. This specifies the consumed fixed-vector proof without relying on an unproved general quotient construction.

Exact invariants are equivalent here to splitting all finite-dimensional submodule inclusions. Given \(W\subset V\), the surjection \(\operatorname{Hom}_k(V,W)\to\operatorname{End}_k(W)\) is a map of rational representations; lift its invariant identity to obtain an equivariant projection onto \(W\). Conversely if all finite representations split, an invariant vector in a quotient lifts to an invariant vector by choosing a finite stable subspace containing any lift and splitting its map onto its image. The finite-subcomodule construction of §6 supplies that subspace. This proves the finite-type semisimplicity criterion.

For arbitrary connected affine \(G\), §7 writes \(k[G]=\bigcup_i B_i\) as a filtered union of finitely generated Hopf subalgebras, and makes all the quotient and transition maps faithfully flat. The groups \(G_i=\operatorname{Spec}B_i\) are connected, as surjective images of the connected scheme \(G\), and are smooth by Cartier's theorem. Every finite representation factors through one \(G_i\), by including its finitely many coefficients in \(B_i\). If \(\operatorname{Rep}(G)\) is semisimple, a splitting of a pulled-back \(G_i\)-representation is a \(G_i\)-splitting by full faithfulness in Theorem 8.1. Hence every \(G_i\) is reductive. Conversely if the \(G_i\) are reductive, a subrepresentation of a representation factoring through \(G_i\) is already \(G_i\)-stable, by the same theorem. Its \(G_i\)-equivariant complement is therefore a \(G\)-complement. Induction on dimension proves semisimplicity. \(\square\)

Connectedness and finite type in this statement have distinct roles. Semisimplicity of a category reconstructed without a tensor generator yields the pro-version, rather than an assertion that its group is a reductive algebraic group. This theorem also supplies no semisimplicity for the Satake heart; that is a separate geometric input.

### 10.2. What this lesson does not prove

A fibre functor over a nonempty \(k\)-scheme \(S\) takes values in finite-rank vector bundles on \(S\). Write \(p_1,p_2:S\times_kS\to S\). The general theorem states that the arrow functor
\[
\operatorname{Isom}^{\otimes}(p_1^*\omega,p_2^*\omega)
\]
is an affine faithfully flat groupoid over \(S\times_kS\), and its representations recover \(\mathcal C\). Conversely such groupoids recover tensor categories with their \(S\)-valued fibre functors. These are arrows between fibres; restriction to the diagonal gives \(\operatorname{Aut}^{\otimes}_S(\omega)\). This is stated, unused, in the freely posted [Deligne author text, definitions 1.9–1.11 and Théorème 1.12, pp. 114–116](https://publications.ias.edu/sites/default/files/60_categoriestanna.pdf).

For an essentially small rigid abelian symmetric \(k\)-linear category with \(\operatorname{End}(\mathbf1)=k\) in characteristic zero, the intrinsic criterion equates Tannakianity, nonnegative integral categorical dimensions, and eventual vanishing of exterior powers of every object. Nonzero objects then have strictly positive dimension. It asserts existence of a fibre functor after field extension, not neutrality over \(k\). This is stated, unused, in the same free text, Théorème 7.1 and Lemme 7.3, pp. 165–166. Neither general theorem is used in §§1–9 or Theorem 10.1.

For the neutral category of §1, the necessity of the dimension condition is elementary and is proved here. Define the categorical dimension by evaluation after symmetry and coevaluation:
\[
\mathbf1\xrightarrow{\mathrm{coev}}X\otimes X^\vee
 \xrightarrow{c}X^\vee\otimes X
 \xrightarrow{\mathrm{ev}}\mathbf1.
\]
Applying the faithful \(k\)-linear symmetric fibre functor makes this scalar the ordinary trace of the identity, namely \(\dim_k\omega X\). It is a nonnegative integer, and is positive if \(X\ne0\). The sufficiency of this condition without an already given fibre functor is the unused intrinsic theorem just stated.

## 11. Exercises and complete solutions

**Exercise 11.1 (easy).** Prove that finite-dimensional integer-graded vector spaces with ordinary interchange are \(\operatorname{Rep}(\mathbb G_m)\). Determine the tensor automorphisms of the forgetful functor over an arbitrary algebra \(R\).

**Solution.** To a grading attach \(\rho(v_n)=v_n\otimes z^n\). Since \(\Delta(z^n)=z^n\otimes z^n\) and \(\epsilon(z^n)=1\), this is a coaction. Conversely expand a finite coaction as \(\rho(v)=\sum_n p_n(v)\otimes z^n\). Equality of coefficients of \(z^m\otimes z^n\) in coassociativity gives \(p_m p_n=\delta_{mn}p_n\), and the counit gives \(\sum p_n=1\). The mutually orthogonal idempotents therefore split the space into their images; only finitely many occur. A comodule map commutes with every \(p_n\), exactly the degree-preserving condition. Multiplication of monomials proves compatibility with tensor products and ordinary interchange. Over \(R\), naturality with degree projections and with every linear map within a grade makes an automorphism scalar \(a_n\) on each grade. The unit gives \(a_0=1\), and the tensor rule gives \(a_{n+m}=a_n a_m\). Hence \(a_1\) is a unit and \(a_n=a_1^n\). Every unit conversely gives such an automorphism. Thus the functor is \(R\mapsto R^\times\), including algebras with nilpotents.

**Exercise 11.2 (easy).** Reconstruct a finite abstract group \(\Gamma\) from its representations and their forgetful functor. Compute the coordinate Hopf algebra in any characteristic.

**Solution.** The regular \(k\Gamma\)-module is an additive generator. Naturality with right multiplication on it forces a natural endomorphism to be left multiplication by its value on1. Naturality with the maps \(k\Gamma\to M\), \(a\mapsto am\), then gives that action on every representation. The finite coefficient coalgebra is therefore \((k\Gamma)^*=k^\Gamma\). For \(g\in\Gamma\), the tensor action is \(g\otimes g\), so the dual product of functions is pointwise. Dualizing the multiplication \(g,h\mapsto gh\) gives \(\Delta f(g,h)=f(gh)\). The trivial representation gives \(\epsilon(f)=f(1)\), and duality gives \(S(f)(g)=f(g^{-1})\). These formulas prove the Hopf identities and identify its spectrum with the constant group scheme. Over \(R\), an algebra map \(k^\Gamma\to R\) chooses mutually orthogonal idempotents summing to 1, or a partition of \(\operatorname{Spec}R\) labelled by the group elements. Multiplication follows (24). The proof uses no averaging, so also applies when \(\operatorname{char}k\) divides \(|\Gamma|\).

**Exercise 11.3 (medium).** Show that super vector spaces with Koszul symmetry have no symmetric fibre functor to ordinary vector spaces when \(\operatorname{char}k\ne2\). Explain what changes in characteristic two.

**Solution.** The odd line \(E\) satisfies \(E^{\otimes2}\simeq\mathbf1\). An assumed strong tensor functor therefore makes \(\omega E\) an invertible finite vector space, hence a line: dimensions multiply and their square is1. The symmetry on \(E\otimes E\) is \(-1\), and a \(k\)-linear functor preserves that scalar. Ordinary interchange on the tensor square of a line is \(+1\). The square expressing preservation of symmetry forces \(-1=+1\) on a nonzero space, a contradiction. In characteristic two the signs coincide. The projector calculation of Exercise 11.1 with exponents taken modulo two then identifies the category with comodules over \(k[z]/(z^2-1)\), whose spectrum is \(\mu_2\); this scheme is nonreduced in characteristic two. Thus there is a fibre functor in that case.

**Exercise 11.4 (medium).** Prove that a reconstructed affine group is of finite type if and only if the category has one tensor generator. Do not assume semisimplicity or characteristic zero.

**Solution.** For a generator \(X\), choose a basis of \(\omega X\). The finite matrix entries and their antipodes generate a Hopf subalgebra. Coefficients of tensor words are products of these entries; those of finite sums are sums, and those of subquotients lie in the ambient coefficient span by adapted bases. Generation of every object and (21) make this subalgebra the whole coordinate algebra. It is finitely generated, so the group is finite type. Conversely choose finite algebra generators and put them in a finite regular subcomodule \(X\), by the construction before (17). Counitality puts these generators in \(C(X)\). Given a finite comodule \(M\), bound the degrees of polynomial expressions for a basis of \(C(M)\) in those generators by \(N\). Formula (20) puts its coefficients in \(C(Y)\), where \(Y=\bigoplus_{r=0}^N X^{\otimes r}\). The coaction injects \(M\) into \(C(M)^{\oplus\dim M}\subset C(Y)^{\oplus\dim M}\). Map (19) supplies a surjection from a finite sum of copies of \(Y\) to this last object. Its inverse image of \(M\) is a subobject surjecting onto \(M\). Thus \(M\) is a subquotient of finite tensor words, proving the converse. There is no symmetric-power division or decomposition into simple representations in this argument.

**Exercise 11.5 (hard).** Let \(f:G\to H\) be a homomorphism of arbitrary affine group schemes over a field. Prove that it is faithfully flat exactly when restriction is fully faithful and every \(G\)-subobject of a restricted representation is an \(H\)-subobject.

**Solution.** Write \(u:B=k[H]\to A=k[G]\). If \(f\) is faithfully flat, \(u\) is injective. A restricted morphism satisfies the comodule identity in \(V\otimes A\); injection of \(V\otimes B\) detects the same identity over \(B\). Thus restriction is full as well as faithful. For a \(G\)-stable \(W\subset V\), the composite \(W\to(V/W)\otimes B\) becomes zero in \((V/W)\otimes A\), hence is zero already. This proves \(H\)-stability.

Conversely let \(I=\ker u\) and suppose it contains \(0\ne a\). Put \(a\) in a finite regular \(B\)-subcomodule \(V\), and set \(W=V\cap I\). The Hopf-ideal identity \(\Delta(I)\subset I\otimes B+B\otimes I\) makes \(W\) stable after restriction: the second summand is killed by \(u\), and the intersection of \(I\otimes A\) with \(V\otimes A\) is \(W\otimes A\). The assumed subobject property gives \(\Delta(W)\subset W\otimes B\). Since \(\epsilon(I)=0\), applying \(\epsilon\otimes1\) forces \(W=0\), a contradiction. Hence \(u\) is injective.

Apply Lemma 7.1, proved here for arbitrary Hopf algebras, to conclude faithful flatness. Its infinite-type step is essential: it expresses \(A\) as the filtered colimit of flat modules \(B\otimes_{B_0}A_0\), where the finite-type group quotient proves faithful flatness of \(A_0/B_0\). Proper ideals remain proper by including a hypothetical finite equation \(1=\sum b_i a_i\) in such a pair. Thus the argument does not merely assert that ring injections are flat. If subobjects are specified only up to isomorphism to restricted objects, use full faithfulness to lift their inclusions before applying the argument.

## 12. Freely accessible reading and proof locators

P. Deligne and J. S. Milne, [*Tannakian Categories*, corrected author edition of 15 August 2012](https://www.jmilne.org/math/xnotes/tc.pdf), is freely readable on the author's site. Theorem 2.11 is the neutral reconstruction statement; Lemmas 2.12–2.13 and Proposition 2.14 concern its finite-category construction; Propositions 2.20–2.21 give the generation and group-morphism dictionary. Sections 1–8 above supply every proof used here, including the Hopf-flatness passage to arbitrary affine groups. The source is reading material and attribution, rather than a substitute for those proofs.

The exact earlier programme inputs used in Lemma 7.1 are the flat quotient theorem of AG-RG-S07, Corollary 8.3; the arbitrary closed algebraic subgroup quotient of AG-GS-04, Theorem 11.1b; and the group monomorphism theorem of AG-GS-03, Theorem 5.9. Theorem 10.1 additionally uses the Cartier and smooth connected reductivity proofs specified there. Their roles and hypotheses are identified at the point of use. The general groupoid and intrinsic statements of §10.2 are not invoked as proof inputs.

