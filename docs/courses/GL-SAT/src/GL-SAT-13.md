# Derived Satake

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

For a connected group, equivariance on a point leaves only vector spaces in the perverse heart. Its derived category still remembers the cohomology of the classifying space. This is already enough to show why deriving the abelian Satake equivalence does not give derived geometric Satake. We calculate that difference, prove the torus model, and specify the additional categories in the general theorem.

## 1. Which derived category?

Work with complex algebraic groups and their classical topology. Cohomological grading means \(H^i(K[s])=H^{i+s}(K)\); in particular a vector space \(V[-2]\) has its vectors in degree \(2\). Write \(\Lambda\) for a characteristic-zero field. The explicit commutative differential-form model in §5 uses \(\Lambda=\mathbf R\) or \(\mathbf C\). The integral topological calculations, and their characteristic-zero scalar extensions, are identified separately.

There are two constructions to distinguish:

- \(D^b(\mathrm{Sat}_G)\), the bounded derived category of the abelian perverse category;
- \(D^b_{L^+G,c}(\mathrm{Gr}_G)\), the Borel equivariant constructible category, with bounded underlying complexes and finite Schubert support.

In the second category, equivariance includes the compatible derived data on all levels of the action nerve. Equivalently one uses finite-dimensional sufficiently acyclic free-action models, in the range of degrees under consideration. Equivariant perverse sheaves and perverse sheaves on stacks, Theorem B.9 constructs those bounded models and their comparisons. Its §4 calculates the first extra class for \(\mathbf G_m\). An isomorphism on the first action product, with a cocycle on the second, describes heart equivariance; it does not replace the full derived construction.

On each finite model, bounded-below injective complexes and their Hom complexes give the enhancement used for derived sections. Sheaves of modules and their derived categories, Theorem 6.1 and Lemmas 6.2–6.3 prove resolution existence and the quasi-isomorphism comparison of those Hom complexes. Their differential is \(d(f)=d_Jf-(-1)^{|f|}fd_I\), and composition satisfies the graded product rule by expansion. The bounded model comparisons are taken in the degree range under consideration. The explicit compatible torus construction is given in §5; no general enhanced-descent theorem is inferred from triangulated full faithfulness alone.

Mapping objects retain these complexes and composition; cones are homotopy cones. Thus \(R\operatorname{Hom}(A,B)\), and not just its cohomology groups, is part of the construction. A **perfect** module over a differential graded algebra is an object obtained from finite sums of shifts of the free module by finitely many cones and direct summands. Equivalently it belongs to the smallest idempotent-complete stable subcategory containing that free module. This definition does not require the algebra to be concentrated in degree zero.

## 2. The unit sees a classifying space

The base point \(e=t^0\) is fixed by \(L^+G\). Its unit sheaf is \(\mathbf1=i_*\Lambda_e\). Closed extension is fully faithful also in the equivariant derived category: in every free-action model it is closed extension along the corresponding closed subspace, and the ordinary identity \(i^*i_*=1\) identifies the unit and counit. It is compatible with the transition models. Hence

\[
R\operatorname{Hom}_{L^+G}(\mathbf1,\mathbf1)
 \simeq R\Gamma(BL^+G,\Lambda).
\tag{2.1}
\]

Indeed on a model of the point quotient the object is the constant sheaf. Its derived endomorphisms are the sections of its coefficient-resolution complex. Products are cup products, because composition of constant-sheaf endomorphisms is the product in that resolution. This proves (2.1) as an endomorphism algebra, rather than only an equality of dimensions.

Evaluation at \(t=0\) induces

\[
L^+G\longrightarrow G,
\tag{2.2}
\]

with constant loops as its section. Its kernel is contractible in the coefficient topology of formal jets. Explicitly \(g(t)\mapsto g(st)\), \(0\leq s\leq1\), fixes constant loops and at \(s=0\) is \(g(0)\). Substitution preserves the defining polynomial equations of \(G\) and the group product. On each jet quotient it is polynomial in the jet coordinates and \(s\); the maps are compatible under truncation. On the inverse-limit topology it is therefore continuous. The kernel is contracted to its identity.

This induces the classifying-space comparison at each bounded model and in each fixed cohomological degree. One can also check it on the bar nerve: the maps on its degree-\(r\) spaces are the corresponding maps on \((L^+G)^r\) and \(G^r\), and the contraction respects faces and degeneracies because it is a group homomorphism at each parameter. Realizing the homotopy gives the same comparison. Consequently

\[
\boxed{\ \operatorname{Ext}^*_{D^b_{L^+G,c}(\mathrm{Gr}_G)}
 (\mathbf1,\mathbf1)=H^*(BG,\Lambda).\ }
\tag{2.3}
\]

The jet construction of The Satake category, §2 supplies the finite algebraic quotients used here; their successive kernels are vector groups in the classical topology. Equation (2.3) is a topological Borel computation. It is not a claim that the algebraic loop quotient functor is unchanged on nonreduced rings.

## 3. Two classifying-space calculations

### 3.1. A circle and a degree-two generator

The group \(\mathbf C^\times\) retracts to its unit circle by \(z\mapsto z|z|^{-s}\). A model of the circle's universal bundle is

\[
S^\infty\longrightarrow\mathbf {CP}^\infty.
\tag{3.1}
\]

Here the unit vectors have finitely many nonzero complex coordinates, with the weak topology from their finite spheres. This space is contractible. If \(S\) inserts a zero first coordinate, the normalized vector \((1-s)v+sS(v)\) never vanishes: for \(s>0\), use the last nonzero coordinate of \(v\) in its new shifted position. This deforms \(v\) to \(S(v)\). The latter is orthogonal to the first coordinate vector, so the path \(\cos(\pi s/2)S(v)+\sin(\pi s/2)e_0\) contracts it to \(e_0\). The homotopies are continuous at every finite stage and on products with the compact parameter interval. The compact-exhaustion product proof is in Grassmannians and classifying maps, Lemma 2.1. Coordinate charts of projective space give local trivializations of (3.1).

The integral computation

\[
H^*(\mathbf {CP}^n,\mathbf Z)
 =\mathbf Z[c]/(c^{n+1}),\qquad |c|=2,
\tag{3.2}
\]

is proved in Gysin sequence and projective splitting, Theorem 3.2. Briefly, the unit-circle bundle of the tautological line has total space \(S^{2n+1}\). Its Gysin sequence says that multiplication by its Euler class is an isomorphism between consecutive even cohomology groups below the top degree. The cell decomposition has one cell in degrees \(0,2,\ldots,2n\) and none elsewhere; thus there are no further groups, and the powers of the class generate. The class \(c=-c_1(\gamma)\) evaluates to \(+1\) on the complex-oriented projective line. Compatibility of the inclusions and stabilization in every fixed degree give

\[
H^*(B\mathbf G_m,\Lambda)=\Lambda[c],\qquad |c|=2.
\tag{3.3}
\]

There is one group in every nonnegative even degree and no odd group. The universal-coefficient passage has no torsion term, since the integral cell homology is free. For a split torus of rank \(r\), take products of these bundle models. The chain product comparison and the same free even cell groups give

\[
H^*(BT,\Lambda)=\Lambda[c_1,\ldots,c_r],\qquad |c_i|=2.
\tag{3.4}
\]

### 3.2. \(SL_2\) and a degree-four generator

The maximal compact subgroup of \(SL_2(\mathbf C)\) is \(SU_2\), which is the group of unit quaternions. Polar decomposition gives a deformation to it: write \(g=up\), with \(u\) unitary of determinant one and \(p\) positive Hermitian of determinant one, then use \(up^{1-s}\). For the right quotient, \(gSU_2\mapsto gg^*\) identifies the quotient with the positive Hermitian determinant-one matrices; its inverse is the coset of the positive square root. The matrix logarithm identifies that space with the vector space of traceless Hermitian matrices, so it is contractible. The locally trivial associated bundle \(EG/SU_2\to EG/G\) has that fibre. Its homotopy sequence and the weak-equivalence cohomology comparison identify the classifying-space cohomology rings. Those two results, including their proofs, are Homotopy fibres and the Serre spectral sequence, Theorems C.2 and B.4.

A universal unit-quaternion bundle is

\[
S^\infty_{\mathbf H}\longrightarrow\mathbf {HP}^\infty.
\tag{3.5}
\]

The same shift and normalization contraction proves that its total space is contractible. The quaternionic projective charts are the charts of one-dimensional right quaternionic subspaces, and their unit frames give local trivializations. For the finite space \(\mathbf {HP}^n\), normalize the last nonzero homogeneous coordinate to one. Its strata are affine quaternionic spaces of dimensions \(0,1,\ldots,n\). The closed filtration by \(\mathbf {HP}^j\) therefore attaches one real cell in every degree \(4j\). The characteristic map is the projectivization of \((z,\sqrt{1-\|z\|^2})\) on the closed quaternionic ball; on the boundary it lies in the preceding projective space. Compactness and the projective chart inverse show that the attachment quotient is the stated space. Thus its additive integral cohomology is \(\mathbf Z\) in degrees \(0,4,\ldots,4n\), with no other groups.

Let \(Q\) be the tautological quaternionic line, viewed as an oriented real rank-four bundle. Its sphere bundle is \(S^{4n+3}\). The rank-four Gysin sequence, proved in Gysin sequence and projective splitting, Theorem 1.1, now makes multiplication by \(e(Q)\) an isomorphism from degree \(4j\) to degree \(4j+4\) for \(0\leq j<n\): the intervening sphere groups vanish. Hence

\[
H^*(\mathbf {HP}^n,\mathbf Z)
 =\mathbf Z[e]/(e^{n+1}),\qquad |e|=4.
\tag{3.6}
\]

Under \(SU_2\subset GL_2(\mathbf C)\), this is a complex rank-two bundle with trivial determinant. Its top Chern class is its real Euler class, with the complex orientation; the identity is proved in Chern classes and the integral universal ring, equation (1.2). Choosing that orientation sets \(e=c_2\). Passing to the limit gives

\[
\boxed{\ H^*(BSL_2,\Lambda)=\Lambda[c_2],\qquad |c_2|=4.\ }
\tag{3.7}
\]

In particular

\[
\operatorname{Ext}^2(\mathbf1,\mathbf1)=0,
\qquad
\operatorname{Ext}^4(\mathbf1,\mathbf1)=\Lambda
\quad(G=SL_2).
\tag{3.8}
\]

### 3.3. The invariant polynomial in this example

Write a trace-zero matrix as \(M=\begin{pmatrix}z&x\\y&-z\end{pmatrix}\). Its invariant quadratic polynomial is \(p(M)=z^2+xy=-\det M\). Every conjugation-invariant polynomial is a polynomial in \(p\). To prove this, restrict to \(\operatorname{diag}(z,-z)\). A Weyl representative exchanges the diagonal entries, so the restriction is an even polynomial \(f(z)=g(z^2)\). Matrices with \(p\ne0\) have distinct eigenvalues and are conjugate to such a diagonal matrix, over an algebraic closure. A change of eigenbasis may be rescaled to determinant one, so conjugation by \(SL_2\) suffices. Subtract \(g(p)\). The invariant difference vanishes on this dense open set, hence is the zero polynomial. Density follows because \(p\) is a nonzero polynomial in the integral polynomial ring.

Place each linear coordinate on \(\mathfrak{sl}_2\) in degree two. Then \(p\) has degree four, and the calculation proves

\[
\operatorname{Sym}(\mathfrak{sl}_2^*[-2])^{SL_2}
 =\Lambda[p],\qquad |p|=4.
\tag{3.9}
\]

Equations (3.7) and (3.9) have the same graded polynomial structure; choosing the generator normalization identifies them. No nonzero degree-two invariant is available. The general invariant-polynomial description of \(H^*(BG)\) requires the general characteristic-class theorem; it is not needed for the two computations above.

## 4. Why the abelian equivalence cannot simply be derived

For a split torus, The Satake category and Consequences and examples, §7 prove that the heart is the category of finite supported graded vector spaces. Every short exact sequence splits weight by weight, by choosing a complement in each vector space. A bounded complex in this heart splits into its cohomology and contractible two-term complexes: choose complements to boundaries inside cycles and to cycles inside each term. Therefore

\[
\operatorname{Hom}_{D^b(\mathrm{Sat}_T)}
 (\mathbf1,\mathbf1[j])=0\quad(j\ne0).
\tag{4.1}
\]

For \(T=\mathbf G_m\), equation (2.3) instead gives a nonzero degree-two morphism in the Borel equivariant category. The two categories cannot be equivalent through a functor sending their units to one another. In degree one, both calculations give zero, so the difference is already compatible with a semisimple heart.

For \(SL_2\), the unconditional rank-one semisimplicity proof of Identifying the dual group, §3.3 gives the analogous vanishing in the derived heart, while (3.8) gives the extra degree-four Borel class. One must specify the group when asserting a nonzero higher self-Ext: its degree is two for a circle and four for \(SL_2\).

## 5. The torus category as perfect differential graded modules

Let \(\mathcal C_T\) be the bounded Borel equivariant category supported on one reduced point of \(\mathrm{Gr}_T\). In the classical coefficient models, it is generated by its constant object \(\Lambda\). To see this, \(BT\) is simply connected: the local trivial bundle with contractible total space has \(\pi_1(BT)=\pi_0(T)=0\). Thus each finite-dimensional local system is constant. This also follows in every sufficiently acyclic finite projective model, whose fundamental group is zero. The cohomology sheaves of an equivariant object on the point are such local systems on the model; its underlying bounded finite-dimensional complex gives only finitely many of them. Ordinary truncation triangles express it as finitely many extensions of shifts of finite sums of \(\Lambda\). Direct summands are retained. Consequently \(\mathcal C_T=\operatorname{thick}(\Lambda)\).

Put \(A_T=R\operatorname{Hom}(\Lambda,\Lambda)=R\Gamma(BT,\Lambda)\), retaining its differential graded algebra. The functor

\[
F=R\operatorname{Hom}(\Lambda,-):
\mathcal C_T\longrightarrow\operatorname{Perf}(A_T)
\tag{5.1}
\]

is an equivalence. Here is the generator proof. It sends \(\Lambda\) to the free module \(A_T\), and the comparison of mapping complexes is an isomorphism on that generator by the definition of \(A_T\). Fixing one argument, the objects for which the comparison is an isomorphism form a stable subcategory closed under direct summands, because both mapping functors turn triangles into triangles. First extend in the second argument, then in the first. This proves full faithfulness on the thick subcategory. Its image contains the free module and is closed under shifts, cones and summands; full faithfulness lifts an idempotent and its splitting. It is therefore all of \(\operatorname{Perf}(A_T)\). This is differential graded Morita equivalence on the generated category, proved here.

For \(\Lambda=\mathbf R\) or \(\mathbf C\), its algebra has the explicit commutative model

\[
A_T\simeq\Lambda[c_1,\ldots,c_r],\qquad |c_i|=2,
\quad d=0.
\tag{5.2}
\]

To justify the algebra assertion, use the finite models \(X_n=(\mathbf {CP}^n)^r\). On each factor choose the negative of the first Chern form of the tautological line, so that it represents \(c_i\). Orthogonal projection of the ordinary derivative in the trivial bundle defines its connection; projection commutes with the linear projective inclusions. Its forms are therefore compatible. The closedness, class identification and projective-line integral \(-1\) are proved in Connections, curvature and characteristic forms, Theorem D.1 and §D.3. Put \(D_n=\Omega^*(X_n;\Lambda)\), with wedge product, and \(D=\varprojlim D_n\). Sending \(c_i\) to those compatible closed forms defines a commutative differential graded algebra map \(\Lambda[c_1,\ldots,c_r]\to D\).

Here are the comparisons behind that assertion. On a coordinate ball, integration along the radial homotopy gives \(dh+hd=1-\mathrm{ev}_0\). Thus the augmented form sheaves resolve the constant real or complex sheaf. A subordinate partition of unity contracts their augmented Čech rows by insertion of its functions and summation. Connections, curvature and characteristic forms, §A.3, equations (A.7)–(A.12) proves this comparison and its multiplicative Čech complexes: the product of bidegrees \((p,q)\) and \((p',q')\) has sign \((-1)^{qp'}\). Through their common constants complex these are multiplicative quasi-isomorphisms, rather than a claim that simplex integration itself preserves products.

Restriction of forms from \(X_{n+1}\) to \(X_n\) is surjective. In charts adapted to the closed projective submanifold, extend coefficients in the normal coordinates; a partition and cutoff patch these local extensions. Consequently the map \(1-\mathrm{shift}\) on \(\prod_nD_n\) is degreewise surjective: choose its coordinates successively by lifting along the surjective restrictions. This gives the short exact sequence of complexes

\[
0\longrightarrow D\longrightarrow\prod_nD_n
 \xrightarrow{1-\mathrm{shift}}\prod_nD_n\longrightarrow0.
\]

Products of vector-space complexes commute with cohomology, since primitives can be chosen in every coordinate. The cohomology exact sequence therefore identifies \(H^j(D)\) with \(\varprojlim H^j(D_n)\) once \(1-\mathrm{shift}\) on the preceding cohomology products is surjective. The groups in every fixed degree eventually stabilize by (3.2)–(3.4); a stable tail has that surjectivity by recursive lifting, and the finitely many initial coordinates can be solved backwards. Thus the possible \(\varprojlim^1\) correction is zero. The polynomial-to-forms map is an isomorphism on every cohomology group, proving (5.2).

For completeness this also supplies compatible enhanced objects, not just a graded endomorphism calculation. A finite semifree \(D\)-module \(M\) gives on \(X_n\) the sheaf complex \(\Omega^\bullet_{X_n}\otimes_D M\). Its free generator is the de Rham resolution of the constant sheaf. For any finite construction and fixed morphism-degree range, take \(n\) beyond that range. The point-resolution triples and comparisons of Theorems B.7–B.9 in the equivariant lesson apply. Maps on the free generators are the just-computed stable form complexes; extending the comparison in both arguments through their finite cones proves full faithfulness. Truncation generation proves essential surjectivity. Retracts have cohomology sheaves equal to images of idempotents on finite constant local systems, and hence remain bounded and finite. This directly realizes the torus enhancement used in (5.1).

For the remaining tensor assertions of this section take \(\Lambda=\mathbf R\) or \(\mathbf C\); the preceding associative generator Morita assertion retains its stated characteristic-zero coefficients. The monoidal comparison is derived tensor over the commutative form algebra. For objects generated by the constant unit there is a natural map

\[
F(K)\otimes_{A_T}^{\mathbf L}F(L)
 \longrightarrow F(K\otimes L),
\tag{5.3}
\]

formed by multiplication and evaluation in the constant-sheaf endomorphism algebra. In the real or complex form model it is the inverse of the wedge-product comparison

\[
(\Omega^\bullet_{X_n}\otimes_D M)\otimes_\Lambda
(\Omega^\bullet_{X_n}\otimes_D N)
 \longrightarrow\Omega^\bullet_{X_n}\otimes_D(M\otimes_D N).
\]

That comparison is a quasi-isomorphism on the free generators, since the constant-to-forms augmentation is a stalkwise quasi-isomorphism. Exactness extends it through finite cones and summands in each argument. Wedge multiplication supplies its associativity, unit and graded symmetry directly. Equivalently (5.3) is an isomorphism first on the unit and then on its whole thick category. Thus (5.1) is a tensor equivalence with the derived tensor product; the commutative polynomial presentation uses the stated real or complex coefficients.

The reduced support of \(\mathrm{Gr}_T\) is indexed by \(L=X_*(T)\). Different supported points have no morphisms between them, as closed restriction detects; point convolution adds the labels. The full bounded finite-support torus statement is therefore

\[
D^b_{L^+T,c}(\mathrm{Gr}_T)
 \simeq\bigoplus_{\lambda\in L}^{\mathrm{finite}}
 \operatorname{Perf}(A_T),
\qquad
(M*N)_\gamma=\bigoplus_{\lambda+\mu=\gamma}
 M_\lambda\otimes_{A_T}^{\mathbf L}N_\mu.
\tag{5.4}
\]

The dual torus has character lattice \(L\). Its adjoint action on its Lie algebra is trivial, and its representation coactions split modules into weights, by the coefficient-projector proof in Lesson 12, equation (7.6), degree by degree. Finite cell modules and their summands have finitely many weights. For real or complex coefficients, (5.2) therefore makes (5.4) the torus instance of perfect dual-torus-equivariant modules over the symmetric algebra with its degree-two generators. The unit at label zero corresponds to the **free module**, whose endomorphism algebra is \(A_T\).

This is not a category of ordinary graded modules with all differentials discarded. Cones, derived tensor products and mapping complexes are essential. For example the cone of multiplication by \(c\), with the suitable shift, gives the perfect module \(\Lambda=A_{\mathbf G_m}/(c)\), while the unit remains \(A_{\mathbf G_m}\). The two objects have different endomorphism algebras.

## 6. The elementary Koszul dual pair

Let \(V\) be finite-dimensional, and put

\[
A=\operatorname{Sym}(V[-2]),\qquad d=0,
\qquad k=\Lambda=A/(V).
\tag{6.1}
\]

Choose a basis \(v_1,\ldots,v_r\), all in degree two. The differential graded module

\[
P=A\otimes\bigwedge(e_1,\ldots,e_r),
\qquad |e_i|=1,
\qquad d(e_i)=v_i
\tag{6.2}
\]

has the augmentation \(P\to k\). It is a finite semifree resolution. In one variable its differential maps \(a e\) to \(a v\). Multiplication by \(v\) in \(\Lambda[v]\) is injective, and its cokernel is \(\Lambda\); hence its cohomology is exactly the augmentation line. Tensor the one-variable resolutions over the field. Splitting complexes into cohomology and contractible summands, as in Lesson 12, Lemma 1.1, shows that their tensor has the same augmentation cohomology. Filtering by the number of exterior factors makes (6.2) semifree, because its differential lowers that number. Thus it computes derived Hom.

**Proposition 6.1.** As a differential graded algebra,

\[
R\operatorname{Hom}_A(k,k)
 \simeq B=\bigwedge(V^*[1]),
\qquad |\epsilon_i|=-1,
\qquad d=0.
\tag{6.3}
\]

**Proof.** The complex \(\operatorname{Hom}_A(P,k)\) has zero differential, since every \(v_i\) acts by zero on \(k\). Its basis is dual to the exterior basis of the \(e_i\); dualizing a degree-one generator gives degree \(-1\). To verify multiplication, let \(\iota_i\) be contraction with \(e_i\) on \(P\). It has degree \(-1\); \(\iota_i^2=0\), and \(\iota_i\iota_j=-\iota_j\iota_i\). Since \(d=\sum_i v_i\iota_i\), the graded commutator of \(d\) with each \(\iota_j\) is zero. These operators give a differential graded algebra map

\[
B\longrightarrow\operatorname{End}_A(P).
\]

Postcomposition with the augmentation is a quasi-isomorphism from \(\operatorname{End}_A(P)\) to \(\operatorname{Hom}_A(P,k)\): the finite semifree filtration makes \(\operatorname{Hom}_A(P,-)\) preserve quasi-isomorphisms. The images of the products of contractions are the dual exterior basis, with their exterior signs. Thus the algebra map induces an isomorphism in cohomology and proves (6.3). Changes of basis identify contractions with \(V^*\), so the result is independent of the chosen basis. \(\square\)

The negative degree in (6.3) is essential. For one variable the resolution has free generators in degrees zero and one. An \(A\)-linear map from its degree-one generator to the augmentation line has degree \(-1\), not degree \(+1\).

The reverse computation is equally explicit in characteristic zero. Resolve the augmentation line as a \(B\)-module by

\[
Q=B\otimes\Lambda[f_1,\ldots,f_r],
\qquad |f_i|=-2,
\qquad d(f_i)=\epsilon_i.
\tag{6.4}
\]

In one variable \(d(f^n)=n\epsilon f^{n-1}\). For \(n>0\) its coefficient is invertible, so all the negative-degree pairs contract and only the constant augmentation remains. Tensoring proves the assertion for every \(r\). Polynomial-degree filtration makes \(Q\) semifree. It is infinite, but still computes derived Hom: a nullhomotopy against an acyclic target is constructed successively on that filtration. On each new free generator, the already prescribed differential makes the obstruction a cycle; acyclicity supplies a primitive. The successive choices define a homotopy on the union. This proves that \(\operatorname{Hom}_B(Q,-)\) preserves quasi-isomorphisms.

The commuting operators \(\partial/\partial f_i\) are closed endomorphisms of degree two. Their products, followed by augmentation, evaluate on the polynomial monomials by the nonzero factorial coefficients. They therefore identify the polynomial algebra on these operators with the cohomology of \(\operatorname{Hom}_B(Q,k)\). As in the preceding proof, postcomposition with augmentation compares it with \(\operatorname{End}_B(Q)\). Consequently

\[
R\operatorname{Hom}_B(k,k)\simeq A.
\tag{6.5}
\]

There is no completed power series algebra in this calculation: in each fixed cohomological degree only finitely many monomials of the \(f_i\) occur, and their duals have that same finite degree. Characteristic zero was used in the factorial coefficients; this proof does not assert an identical divided-power statement in positive characteristic.

Applying the generator proof of §5 to these two augmentation objects gives the precise category statements

\[
\operatorname{thick}_A(k)\simeq\operatorname{Perf}(B),
\qquad
\operatorname{thick}_B(k)\simeq\operatorname{Perf}(A).
\tag{6.6}
\]

The second equivalence is \(R\operatorname{Hom}_B(k,-)\); the first is its corresponding \(A\)-module construction. These are statements about the specified generated subcategories. They do not identify all differential graded modules over \(A\) with all modules over \(B\).

Since \(B\) is nonpositive with \(H^0(B)=k\), a \(B\)-module with bounded finite-dimensional cohomology belongs to \(\operatorname{thick}_B(k)\). Its ordinary truncation triangles have cohomology objects that are finite sums of shifts of the augmentation module; the negative-degree elements act trivially on a single cohomology object. There are finitely many such triangles. Conversely a finite construction from \(k\) has bounded finite-dimensional cohomology. Thus the second category on the left of (6.6) is exactly the bounded coherent module category of this exterior algebra.

If \(\mathfrak h\) is a vector space placed in degree zero, the coordinate algebra of the derived self-intersection of the origin in \(\mathfrak h\) is

\[
\mathcal O(\operatorname{pt}\times_{\mathfrak h}^{\mathbf R}
 \operatorname{pt})
 =\Lambda\otimes^{\mathbf L}_{\operatorname{Sym}(\mathfrak h^*)}\Lambda
 \simeq\bigwedge(\mathfrak h^*[1]).
\tag{6.7}
\]

To prove it, resolve the origin over the degree-zero polynomial algebra by its ordinary Koszul complex, with free exterior generators in degree \(-1\) and differential equal to the coordinate functions. Tensoring with the origin kills that differential. Taking \(\mathfrak h=V\), (6.7) is precisely \(B\). Equations (6.5)–(6.6) explain why perfect modules with degree-two polynomial generators can also be expressed by coherent modules on this derived self-intersection.

For a torus, apply this independently at each weight label in (5.4), using the coefficient hypothesis of (5.2) for the polynomial presentation. Its spectral description can therefore use either perfect modules over \(\operatorname{Sym}(\widehat{\mathfrak t}[-2])\) or bounded coherent modules over \(\bigwedge(\widehat{\mathfrak t}^*[1])\), with the dual torus's weight decomposition. The latter algebra is the coordinate algebra of \(\operatorname{pt}\times^{\mathbf R}_{\widehat{\mathfrak t}}\operatorname{pt}\). Under the second equivalence in (6.6), its augmentation module corresponds to the free polynomial module, the Satake unit. Its product is the product transported from (5.4); this assertion does not replace that product by ordinary tensor over the exterior algebra.

## 7. What renormalization changes

For the exterior algebra \(B=\Lambda[\epsilon]\), \(|\epsilon|=-1\), the augmentation module \(k\) is not compact in the category of all differential graded \(B\)-modules. This can be checked from (6.4), rather than from terminology. Take the direct sum \(M=\bigoplus_{n\geq0}k[2n]\), all with trivial \(\epsilon\)-action. In degree zero a map from its resolution to \(M\) may assign the generator \(f^n\) any scalar in the \(n\)-th summand. Those choices are independent; the Hom differential is zero because \(\epsilon\) acts by zero. Thus

\[
\operatorname{Hom}_{D(B)}(k,M)=\prod_{n\geq0}\Lambda,
\qquad
\bigoplus_{n\geq0}\operatorname{Hom}_{D(B)}(k,k[2n])
 =\bigoplus_{n\geq0}\Lambda.
\tag{7.1}
\]

The natural direct-sum comparison is not surjective. This is exactly failure of compactness.

On the other hand \(k\) is a generator of the bounded coherent category \(\operatorname{thick}_B(k)\). If one **defines** its renormalized presentable category by

\[
\operatorname{Ind}(\operatorname{thick}_B(k)),
\tag{7.2}
\]

then that object is compact there: by the construction of Ind-completion, maps from an original object commute with filtered colimits. The equivalence (6.6) extends to

\[
\operatorname{Ind}(\operatorname{thick}_B(k))
 \simeq\operatorname{Ind}(\operatorname{Perf}(A)).
\tag{7.3}
\]

Its compact objects are exactly the original idempotent-complete perfect category. To see the last assertion, write an object as a filtered colimit of finite constructions; if the object is compact, its identity factors through one stage, making it a retract of that stage. These formulas give a concrete reason for specifying the completion in a derived Satake theorem. The full module category over the exterior algebra and (7.2) have different compactness behavior despite containing the same bounded coherent subcategory.

## 8. The general theorems and their categories

The following are external theorem statements. The proofs above establish their torus algebraic model and the unit calculations; they do not prove the general equivalences in this section. None of these statements is used to justify an earlier result or an exercise below.

### 8.1. The bounded equivariant theorem

Let \(G\) be a complex simply connected semisimple group and \(\widehat G\) its dual over an algebraically closed characteristic-zero coefficient field. [Bezrukavnikov–Finkelberg, Theorem 5, §2.7](https://arxiv.org/pdf/0707.3799v4#page=7) gives monoidal triangulated equivalences

\[
D^b_{G(O),c}(\mathrm{Gr}_G)
 \simeq\operatorname{Perf}^{\widehat G}
       (\operatorname{Sym}(\widehat{\mathfrak g}[-2])),
\qquad
D^b_{G(O)\rtimes\mathbf G_m,c}(\mathrm{Gr}_G)
 \simeq\operatorname{Perf}^{\widehat G}(U_\hbar^{[\ ]}).
\tag{8.1}
\]

On the right, equivariant perfect modules are generated by \(A\otimes V\), for finite-dimensional representations \(V\), under finite cones and summands. Both displayed algebras have differential zero. In the second, Lie generators and \(\hbar\) have degree two, and the relation is \(xy-yx=\hbar[x,y]\). The paper simplifies to simply connected \(G\) after §2.4; the reductive categorical formulation is given next. Equation (8.1) is a monoidal theorem, without an asserted factorization upgrade.

### 8.2. Ordinary and renormalized spherical categories

For a reductive group in characteristic zero, put

\[
\mathcal H_{\widehat G}
 =B\widehat G\times^{\mathbf R}_{\widehat{\mathfrak g}/\widehat G}
 B\widehat G
 =(\operatorname{pt}\times^{\mathbf R}_{\widehat{\mathfrak g}}
   \operatorname{pt})/\widehat G.
\tag{8.2}
\]

Write \(\mathrm{Sph}=D\text{-mod}(\mathrm{Gr}_G)^{G(O)}\), with its ordinary cocompletion. Let \(\mathrm{Sph}^{loc.c}\) consist of objects compact after forgetting equivariance, and define \(\mathrm{Sph}^{ren}=\operatorname{Ind}(\mathrm{Sph}^{loc.c})\). [Arinkin–Gaitsgory, §§12.3–12.5](https://arxiv.org/pdf/1201.6343v4#page=109) distinguish the following monoidal equivalences:

| Geometric category | Spectral category | Exact theorem |
| --- | --- | --- |
| \(\mathrm{Sph}^{loc.c}\) | \(\operatorname{Coh}(\mathcal H_{\widehat G})\) | Theorem 12.3.3 |
| \(\mathrm{Sph}^{ren}\) | \(\operatorname{IndCoh}(\mathcal H_{\widehat G})\) | Corollary 12.3.4 |
| \(\mathrm{Sph}\) | \(\operatorname{IndCoh}_{\mathrm{Nilp}}(\mathcal H_{\widehat G})\) | Theorem 12.5.3, Corollary 12.5.5 |
| \(\mathrm{Sph}^{c}\) | \(\operatorname{Coh}_{\mathrm{Nilp}}(\mathcal H_{\widehat G})\) | Corollary 12.5.5 |

Here Nilp constrains singular support in \(\widehat{\mathfrak g}^*/\widehat G\), rather than ordinary support in the underlying point quotient. Proposition 12.4.2 and Corollary 12.4.5 give the polynomial Koszul-dual presentation of all IndCoh. Remark 12.4.3 excludes compatibility of that presentation with factorization. The functors of §12.2.4 are \(\Xi:\mathrm{Sph}\to\mathrm{Sph}^{ren}\) and \(\Psi:\mathrm{Sph}^{ren}\to\mathrm{Sph}\), with \(\Xi\dashv\Psi\) and \(\Xi\) fully faithful. Renormalized compactness refers to \(\mathrm{Sph}^{loc.c}\).

### 8.3. Factorization is additional structure

For reductive \(G\) over an algebraically closed characteristic-zero field, [Campbell–Raskin, Theorem 6.6.1](https://arxiv.org/pdf/2310.19734v2#page=59) proves an equivalence

\[
\mathrm{Sat}_G:\mathrm{Sph}_G
 \xrightarrow{\sim}\mathrm{Sph}^{spec}_{\widehat G}
 \quad\text{in }\operatorname{AssocAlg}(\operatorname{FactCat}).
\tag{8.3}
\]

Both categories are renormalized. Proposition 6.3.2 specifies geometric renormalization; §5.7 specifies spectral renormalization using integrable factorization modules. Theorem 8.10.1 and Corollary 8.10.1.1 identify its one-point algebraic models. The QCoh formal-completion presentation there precedes passage to integrable objects and renormalization. Proposition 10.2.1 identifies QCoh with the tempered subcategory, rather than with all ordinary spherical objects. The spherical theorem (8.3) is unconditional; its proof is not supplied here.

The half-density convention is specified in [Gaitsgory–Raskin, §§1.5–1.7](https://arxiv.org/pdf/2405.03648v3#page=23):

\[
\mathrm{Sph}^{non\text{-}ren}_G
 =D\text{-mod}_{1/2}(L^+G\backslash LG/L^+G).
\tag{8.4}
\]

Renormalization ind-completes the objects compact after either forgetful functor to the Grassmannian. Theorem 1.7.2 gives the unique monoidal factorization equivalence with all IndCoh on the spectral Hecke category, compatible with the Casselman–Shalika action. Its one-point stack is the derived zero self-intersection over \(\widehat{\widehat{\mathfrak g}}_0/\widehat G\); that self-intersection agrees with (8.2). Appendix E constructs the Ran category. Example 1.7.4 sends \(\mathrm{IC}_\lambda\) to \(\mathrm{nv}(V^{-w_0\lambda})\), preserving its dual-weight convention. Remark 1.7.5 makes the half-density twist essential for factorization.

## 9. Reading the spectral expression

The notation in (8.2) can be understood without assuming the general theorem. For a vector space \(\mathfrak h\), its derived zero self-intersection has exterior coordinate algebra (6.7). Its underlying ordinary point does not describe all its functions: the negative cohomological degrees record the intersection's excess tangent directions. For an acting group, equivariance additionally records compatible action data. In the torus case the action on \(\mathfrak h=\widehat{\mathfrak t}\) is trivial, and coefficient projectors give exactly the weight labels in (5.4).

In this finite exterior-algebra example, coherent means bounded finite-dimensional cohomology, as proved in §6. IndCoh is its Ind-completion as in (7.2). Equation (7.1) explains why this differs from simply taking all modules over its coordinate algebra. In the general statement, singular support requires additional operators on derived morphisms. It is part of the external theorem in §8; no assertion that ordinary support or a point's set of coordinates determines it is needed for our calculations.

Likewise, factorization specifies compatible categories for moving finite collections of points, their products when the points are disjoint, and their behavior under collision. A one-point equivalence supplies only one part of that data. Fusion, §6 proves the classical collision product of perverse sheaves. It does not construct the derived spectral category on Ran. Thus (5.4) is a proved fixed-point torus tensor equivalence; (8.3) includes the further moving-point structure by its external theorem.

The relevance to geometric Langlands is a precise preview. Hecke correspondences act on sheaves on \(\operatorname{Bun}_G\), as described in Consequences and examples, §8. A general derived Satake equivalence expresses the local category of kernels for that action through \(\widehat G\). Constructing the global spectral action also requires those global correspondences and their derived descent. This lesson's torus calculation neither assumes nor proves that further action.

## 10. Exercises with complete solutions

**Exercise 13.1 (easy).** Compute \(H^*_{\mathbf G_m}(\operatorname{pt},\Lambda)\), including its product and odd degrees.

**Solution.** By definition this is \(H^*(B\mathbf G_m,\Lambda)\). The contraction and projective bundle model in §3.1 give \(B\mathbf G_m\simeq\mathbf {CP}^{\infty}\). There is one even cell in each nonnegative even degree. The finite Gysin calculation (3.2) proves that the positive generator \(c\) in degree two has powers generating all those groups. Their restrictions stabilize, and all odd groups are zero. Hence the answer is the polynomial algebra \(\Lambda[c]\), with \(|c|=2\), including its multiplication.

**Exercise 13.2 (easy).** State and verify derived Satake for a rank-\(r\) torus with real or complex coefficients. Identify the unit and convolution.

**Solution.** Put \(L=X_*(T)\) and \(A=\Lambda[c_1,\ldots,c_r]\), with zero differential and each generator of degree two. At one support point, truncation triangles and constant local systems give \(\operatorname{thick}(\Lambda)\). The mapping-complex generator argument of (5.1), together with the multiplicative form model (5.2), identifies it with \(\operatorname{Perf}(A)\). Distinct support points have no morphisms; finite support therefore gives the finite sum over \(L\). The tensor comparison (5.3) proves that convolution adds labels and tensors over \(A\), exactly (5.4). Coefficient projectors identify labels with characters of \(\widehat T\). The object at label zero is the free module \(A\). Every ingredient is proved in §5, so this is the fixed-point differential graded tensor equivalence, with no claim about Ran factorization.

**Exercise 13.3 (medium).** For \(G=\mathbf G_m\), show that \(\operatorname{Ext}^1\) between simple objects in the Satake heart vanishes, while the unit has nonzero \(\operatorname{Ext}^2\) in the Borel equivariant derived category. Explain the corresponding degree for \(SL_2\).

**Solution.** Simple torus objects are one-dimensional vector spaces at single labels. A short exact sequence splits by the weight projectors and an ordinary vector-space complement. This proves vanishing of every heart \(\operatorname{Ext}^1\), including self-extensions. In the Borel category, closed extension at the base point and loop contraction prove (2.3); (3.3) identifies its degree-two self-Ext with \(\Lambda c\ne0\). The bounded derived heart has zero morphisms in that degree by the complex-splitting proof of (4.1). For \(SL_2\), (3.8) instead says that degree two is zero and the first positive class is \(c_2\) in degree four. The group cannot be omitted from the assertion.

**Exercise 13.4 (medium).** For \(G=SL_2\), compare \(H^*(BG,\Lambda)\) with \(\operatorname{Sym}(\mathfrak g^*[-2])^G\). Do not assume the general characteristic-class theorem.

**Solution.** Polar decomposition and the quaternionic universal bundle reduce the first ring to \(H^*(\mathbf {HP}^{\infty},\Lambda)\). Its rank-four Gysin sequence gives the polynomial ring \(\Lambda[c_2]\) with generator of degree four, by (3.6)–(3.7). For the second ring, write \(p=z^2+xy\). Restriction of an invariant to diagonal trace-zero matrices is even by the Weyl interchange. Subtract its corresponding polynomial in \(p\); the difference vanishes on the dense distinct-eigenvalue locus and is zero. Thus (3.9) is \(\Lambda[p]\), with \(p\) of degree four when the linear coordinates have degree two. Sending \(p\) to \(c_2\) defines the graded algebra isomorphism. This computes the rings and a chosen isomorphism; a universal normalization in arbitrary rank is not being inferred.

**Exercise 13.5 (hard).** For \(A=\Lambda[c]\), \(|c|=2\), and \(B=\bigwedge(\epsilon)\), \(|\epsilon|=-1\), prove both derived endomorphism calculations and the corresponding generated-category equivalences. Why does this not equate all \(A\)-modules with all \(B\)-modules?

**Solution.** Write \(k\) for the augmentation object. Resolve \(k_A\) by \(P=A\otimes\bigwedge(e)\), \(|e|=1\), \(de=c\). Multiplication by \(c\) is injective, so the augmentation is a quasi-isomorphism. The closed contraction \(\iota_e\) has degree \(-1\), square zero, and its two classes give all of \(\operatorname{Hom}_A(P,k)\). The finite free comparison therefore proves \(R\operatorname{End}_A(k)\simeq B\).

Resolve \(k_B\) by \(Q=B[f]\), \(|f|=-2\), \(df=\epsilon\). Its positive pairs cancel since \(d(f^{n+1})=(n+1)\epsilon f^n\); the augmentation is a quasi-isomorphism. The increasing polynomial-degree filtration makes it semi-free, and the homotopy-lifting argument in §6 shows it computes derived Hom. The closed operator \(\partial_f\) has degree two. Its powers, followed by augmentation, give the dual basis to \(f^n\), with nonzero coefficients \(n!\). Thus \(\Lambda[c]\to\operatorname{End}_B(Q)\), \(c\mapsto\partial_f\), is a quasi-isomorphism. There is one basis element in each nonnegative even degree, without a completion.

The two generator mapping-complex arguments give \(\operatorname{thick}_A(k)\simeq\operatorname{Perf}(B)\) and \(\operatorname{thick}_B(k)\simeq\operatorname{Perf}(A)\). The second takes \(k_B\) to \(A\), while the free \(B\)-module goes to a different object. These equivalences specify their generated subcategories. In all \(B\)-modules, the same \(k_B\) fails compactness by the product-versus-sum calculation (7.1). It is compact in its own Ind-completion (7.2). There is also a direct failure of the first functor on all \(A\)-modules: the nonzero module \(A[c^{-1}]\) is sent to zero by \(R\operatorname{Hom}_A(k,-)\). Its Hom complex from \(P\) has differential multiplication by \(c\), now an isomorphism, and is contractible. Thus that functor is not faithful on all modules. Passing to larger categories without specifying the completion would invalidate the assertion.

## 11. Scope and free reading

The proved statements are the unit self-Ext formula (2.3), both classifying-space rings in §3, the torus tensor Morita model with the stated coefficients in §5, the two Koszul endomorphism calculations and generated-category equivalences in §6, and the compactness distinction in §7. The five exercises use those proofs. The general bounded, renormalized, singular-support and factorization theorems in §8 are precisely stated external results, whose proofs remain outside this lesson.

Free further reading:

- [Bezrukavnikov–Finkelberg, *Equivariant Satake category and Kostant–Whittaker reduction*, arXiv:0707.3799v4](https://arxiv.org/abs/0707.3799v4), Theorem 5 and §6.6.
- [Arinkin–Gaitsgory, *Singular support of coherent sheaves, and the geometric Langlands conjecture*, arXiv:1201.6343v4](https://arxiv.org/abs/1201.6343v4), §§12.2–12.5.
- [Campbell–Raskin, *Langlands duality on the Beilinson–Drinfeld Grassmannian*, arXiv:2310.19734v2](https://arxiv.org/abs/2310.19734v2), §§5.7, 6.3, 6.6 and 8.10.
- [Gaitsgory–Raskin, *Proof of the geometric Langlands conjecture II: Kac–Moody localization and the FLE*, arXiv:2405.03648v3](https://arxiv.org/abs/2405.03648v3), §§1.5–1.8 and Appendix E.

The proofs from earlier programme lessons are linked at the points where they are used. The reading list does not replace any of them.
