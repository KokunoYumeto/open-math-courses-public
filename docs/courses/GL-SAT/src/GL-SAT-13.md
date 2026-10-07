# Derived Satake

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

For a connected group, equivariance on a point leaves only vector spaces in the perverse heart. Its derived category still remembers the cohomology of the classifying space. This is already enough to show why deriving the abelian Satake equivalence does not give derived geometric Satake. We calculate that difference, prove the torus model, and specify the additional categories in the general theorem.

## 1. Which derived category?

Work with complex algebraic groups and their classical topology. Cohomological grading means \(H^i(K[s])=H^{i+s}(K)\); in particular a vector space \(V[-2]\) has its vectors in degree \(2\). Write \(\Lambda\) for a characteristic-zero field. The commutative polynomial-simplex model in §5 applies to every such field. Smooth complex forms are used in §3 to prove restriction of classifying-space cohomology; the rational descent there proves its general coefficient-field statement.

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

Equations (3.7) and (3.9) have the same graded polynomial structure; choosing the generator normalization identifies them. No nonzero degree-two invariant is available. The next three sections prove the general invariant-polynomial description, including its coefficient-field passage.

### 3.4. Restriction to a maximal torus

Choose the split rational group \(G_{\mathbf Q}\) with the datum of a connected complex reductive \(G\), using Pinnings and the classification of split reductive groups, Theorem 10.1. For a characteristic-zero field \(\Lambda\), put \(G_\Lambda=G_{\mathbf Q}\otimes\Lambda\) and \(\mathfrak g_\Lambda=\operatorname{Lie}(G_\Lambda)\). We will prove
\[
H^*(BG;\Lambda)\simeq\operatorname{Sym}(\mathfrak g_\Lambda^*[-2])^{G_\Lambda}.
\tag{3.11}
\]
This specifies the coefficient model even when \(\Lambda\) has no chosen embedding into \(\mathbf C\). Let \(B\supset T\) be a Borel, and \(W=N_G(T)/T\). Work in a prescribed finite cohomology range and choose a common sufficiently acyclic frame \(V=V_{N,d}\) for a faithful \(G\subset GL_d\). GL-PERV Propositions B.6–B.6a construct the smooth separated quotients, the torsor charts and all the maps used below.

The map
\[
q:V/B\longrightarrow V/G
\]
is a proper smooth bundle with fibre \(G/B\), of complex dimension \(m\). AG-RG-03 Lemma 5.1 gives the ample \(G\)-equivariant line \(\det(\operatorname{Lie}\mathcal B)^*\) on that flag variety, and AG-RG-06 Theorem 1.1 gives its smooth projective quotient. Its equivariant descent to \(V/B\) has a global Chern class \(\eta\).

We first prove injectivity with complex coefficients by direct integration over the flag fibre. Its real dimension is \(2m\), and its complex orientation is preserved by every transition of the bundle. On a local product chart integrate the fibre-degree-\(2m\) part of a smooth form. Change of fibre coordinates preserves this integral, so these local formulas define
\[
q_*:\Omega^\bullet(V/B;\mathbf C)
 \longrightarrow\Omega^{\bullet-2m}(V/G;\mathbf C).
\]
The fibre is compact and has no boundary. Differentiation under its integral is valid in each product chart; the fibre derivative integrates to zero by Stokes. Since \(2m\) is even, the base-derivative sign is positive. Hence \(dq_*=q_*d\). Directly on product forms,
\[
q_*(q^*\beta\wedge\eta^m)=s\beta,
\qquad s=\int_{G/B}c_1(\mathcal L)^m>0.
\tag{3.12}
\]
Here \(\eta\) is a closed curvature representative of the global Chern class. Its fibre integral is the same Chern number on every fibre by local trivialization and naturality. A positive power of the ample line embeds \(G/B\) in projective space. Divide its restricted positive Fubini--Study form by that power; its positive top volume proves \(s>0\). The Chern and orientation comparisons identify it with the integral Chern number. These comparisons and positivity are proved in The Satake category, Theorem 5.7 and Connections, curvature and characteristic forms, Parts A and D. Equation (3.12) proves that pullback along \(q\) is injective over \(\mathbf C\).

It is also injective over \(\mathbf Q\). For any space, split its rational singular-chain complex into its homology and two-term contractible summands by choosing complements to boundaries in cycles and to cycles in chains. Its cohomology with values in a field \(K\supset\mathbf Q\) is therefore \(\operatorname{Hom}_{\mathbf Q}(H_j(-;\mathbf Q),K)\). The coefficient map from \(K=\mathbf Q\) to \(K=\mathbf C\) is injective, without a finite-dimensionality assumption. A rational class killed by flag pullback is killed after extension to \(\mathbf C\), where the preceding paragraph proves injectivity. It is thus zero already over \(\mathbf Q\).

The map \(V/T\to V/B\) has fibre \(B/T\), an affine space by the ordered root coordinates of AG-RG-04 §5. Its torsor product charts make it a locally trivial contractible-fibre bundle. GL-PERV Lemma B.5 proves its adjunction unit is an isomorphism, without a nonproper fibre-base-change assumption. We have therefore proved, initially for \(K=\mathbf Q,\mathbf C\),
\[
H^*(BG;K)\hookrightarrow H^*(BT;K)
\tag{3.13}
\]
in each prescribed range, and hence in every degree by increasing the frame.

At the same finite frame the right action of \(N_G(T)\) on \(V/T\) preserves its map to \(V/G\). It factors through \(W\), and acts on the character Chern classes by the ordinary Weyl action. Thus the image of (3.13) lies in \(H^*(BT;K)^W\). This invariance does not require an unproved statement about arbitrary group actions on classifying spaces.

### 3.5. Invariant polynomials and characteristic classes

The centre of the enveloping algebra and Harish-Chandra’s theorem, Theorem 3.1 proves Chevalley restriction for a complex semisimple Lie algebra, with an actual graded polynomial proof:
\[
\mathbf C[\mathfrak g]^{\mathfrak g}
\xrightarrow{\sim}\mathbf C[\mathfrak t]^W.
\tag{3.14}
\]
For reductive \(\mathfrak g=\mathfrak z\oplus[\mathfrak g,\mathfrak g]\), tensor that proof with the polynomial algebra on the centre. The Weyl group fixes the centre, so the same statement follows. Infinitesimal invariants equal \(G\)-invariants here. Root-vector infinitesimal invariance integrates by its finite polynomial exponential; torus infinitesimal invariance means weight zero; the torus and root groups generate the connected group by the proved Bruhat coordinates of AG-RG-04. Thus the notation in (3.14) really gives the algebraic adjoint invariants.

We need the characteristic-class map for this general \(G\), not merely the matrix-group version in DG-CHAR. It has the following short proof from the existing principal-connection foundations.

A smooth principal \(G\)-bundle has a connection by Connections and parallel transport, Theorem B.1. That theorem patches local product connections with a partition of unity and works for every finite-dimensional Lie group. For a complex group regard its connection as a form valued in its complex Lie algebra on the real base. Principal curvature, transformation, and Bianchi are proved in Curvature and holonomy groups, Theorems A.4, A.6–A.7.

Let \(f\) be an invariant homogeneous polynomial of degree \(a\), and \(p\) its symmetric polarization. If \(\omega\) is the connection and \(F=d\omega+\tfrac12[\omega,\omega]\), put
\[
\mathrm{CW}_f=p\bigl(iF/(2\pi),\ldots,iF/(2\pi)\bigr).
\tag{3.15}
\]
Invariance makes this horizontal and invariant, hence a base form. To verify closedness and independence explicitly, for homogeneous valued forms \(\beta_j\) of degrees \(b_j\), differentiate the polarization identity
\[
\sum_j p(X_1,\ldots,[Z,X_j],\ldots,X_a)=0.
\]
Move the connection one-form to the front in each term. Its Koszul sign cancels the differentiation sign, so
\[
d\,p(\beta_1,\ldots,\beta_a)
=\sum_j(-1)^{b_1+\cdots+b_{j-1}}
p(\beta_1,\ldots,D\beta_j,\ldots,\beta_a).
\tag{3.16}
\]
Since \(DF=0\), (3.15) is closed. For two connections take their affine path, with difference \(\alpha\) and curvature \(F_t\). The local bracket formula gives \(\dot F_t=D_t\alpha\). Equation (3.16) then gives
\[
\mathrm{CW}_f(F_1)-\mathrm{CW}_f(F_0)
=d\left[
a\left(\frac{i}{2\pi}\right)^a
\int_0^1p(\alpha,F_t,\ldots,F_t)\,dt\right].
\tag{3.17}
\]
The difference is horizontal and equivariant; hence its displayed primitive is global. Pullback of the connection proves naturality. Sums and products of polynomials give sums and products of their curvature forms because two-form coefficients commute. This proves the required general Chern–Weil map. It is the invariant-contraction proof of Connections, curvature and characteristic forms, Theorem B.2 with its matrix-group restriction removed by the actual principal-group bracket calculation (3.16).

Apply it to the finite principal bundle \(V\to V/G\). Restricting to \(V/T\) gives the principal \(T\)-reduction; connection independence permits a connection induced from that reduction. Thus restriction of (3.15) is the torus characteristic polynomial of \(f|_{\mathfrak t}\). For a character \(\chi\), Connections, curvature and characteristic forms, Theorem D.1 in the line-bundle case identifies its normalized curvature with \(c_1(\mathcal L_\chi)\). Therefore
\[
\operatorname{res}(\mathrm{CW}_f)
=f|_{\mathfrak t}\bigl(c_1(\mathcal L_{\chi_1}),\ldots,
c_1(\mathcal L_{\chi_r})\bigr),
\tag{3.18}
\]
when expressed in the linear coordinates \(d\chi_j\). These character classes generate \(H^*(BT;\mathbf C)\).

If the associated standard-character line is taken to be the tautological line, its Chern class is the negative of the positive generator \(c_j\) of Lesson 13. Equation (3.18) retains that sign: identify \(d\chi_j\) with \(c_1(\mathcal L_{\chi_j})\), not silently with its negative. Choosing the dual character line gives the positive generator. Either convention gives the same polynomial-ring assertion.

Every Weyl-invariant polynomial in these degree-two classes lifts through (3.14) to some \(f\). Equation (3.18) proves it lies in the image of (3.13). We have proved
\[
H^*(BG;\mathbf C)\xrightarrow{\sim}H^*(BT;\mathbf C)^W.
\tag{3.19}
\]
All constructions were performed on genuine finite smooth manifolds in the relevant range. No infinite-dimensional differential-form manifold or imported Borel theorem was used.

### 3.6. Rational descent and all characteristic-zero coefficients

The rational injection (3.13) first gives finiteness in each degree over \(\mathbf Q\), because the torus groups are finite dimensional in each degree. On a sufficiently large finite frame, that torus calculation is the projective model calculation by the same common-product comparison used in GL-SAT-06, equation (5.26).

Here is the coefficient passage without a finite-CW assumption. For the singular chain complex over \(\mathbf Q\), choose degreewise complements to boundaries in cycles and to cycles in chains. It splits as its homology with zero differential plus two-term contractible summands. Applying \(\operatorname{Hom}_{\mathbf Q}(-,\Lambda)\) therefore gives
\[
H^j(Y;\Lambda)=\operatorname{Hom}_{\mathbf Q}
(H_j(Y;\mathbf Q),\Lambda).
\tag{3.20}
\]
If \(H^j(Y;\mathbf Q)=\operatorname{Hom}(H_j(Y;\mathbf Q),\mathbf Q)\) is finite dimensional, then \(H_j(Y;\mathbf Q)\) is finite dimensional: any arbitrarily large independent finite family in the latter has arbitrarily large independent dual functionals, extended from its span by a vector-space complement. In that case (3.20) is the canonical scalar-extension isomorphism
\[
H^j(Y;\mathbf Q)\otimes_{\mathbf Q}\Lambda
\xrightarrow{\sim}H^j(Y;\Lambda).
\tag{3.21}
\]
Apply this degreewise to the sufficiently large finite Borel models. Finiteness follows from the trace injection and the bounded torus comparison, so (3.21) applies. The maps are natural and preserve products. Thus it also applies to the stable \(BG\) groups.

Finite-group invariants commute with field extension by the averaging projector \(|W|^{-1}\sum_w w\). The map
\[
H^*(BG;\mathbf Q)\longrightarrow H^*(BT;\mathbf Q)^W
\]
becomes (3.19) after extension to \(\mathbf C\), by (3.21). Faithful extension reflects kernel and cokernel degreewise, so it is already an isomorphism over \(\mathbf Q\), and then over every \(\Lambda\):
\[
H^*(BG;\Lambda)\xrightarrow{\sim}H^*(BT;\Lambda)^W.
\tag{3.22}
\]

Likewise (3.14) descends to the rational split model and extends to \(\Lambda\). In each polynomial degree, infinitesimal invariants are the simultaneous kernels of finitely many rational linear matrices, one for each element of a rational Lie basis. Kernels commute with field extension. The root-group and torus argument of §7 identifies them with the algebraic group invariants over every characteristic-zero field. The restriction map is rational, becomes an isomorphism over \(\mathbf C\), and therefore is an isomorphism over \(\mathbf Q\) and \(\Lambda\). Combining it with the character Chern-class identification of the torus and (3.22) proves (3.11).

This also proves odd cohomology vanishing for \(BG\), but the stronger invariant-polynomial identification is what closes Lesson 13's general outline assertion. It is a cohomology-ring theorem; it does not claim commutative differential graded formality of \(BG\) or the general derived Satake equivalence.


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

For every characteristic-zero field, we now construct a commutative model
\[
A_T\simeq P_\Lambda=\Lambda[c_1,\ldots,c_r],
\qquad |c_i|=2,\quad d=0.
\tag{5.2}
\]
The generators retain the projective normalization \(c_i=-c_1(\text{tautological line})\).

### 5.1. Polynomial simplex forms

For the affine standard simplex define the commutative differential graded algebra
\[
\Omega_{\mathrm{pol}}(\Delta^p;\mathbf Q)
=
\mathbf Q[t_0,\ldots,t_p,dt_0,\ldots,dt_p]/
(\textstyle\sum t_i-1,\sum dt_i).
\tag{5.5}
\]
The \(t_i\) have degree zero, the \(dt_i\) degree one, the latter anticommute, and \(d(t_i)=dt_i\). Its extension to \(\Lambda\) is defined by the same formula. Every affine map taking vertices to vertices induces a pullback of commutative differential graded algebras.

**Lemma 5.1.** Compatible polynomial forms on any union of faces extend to the simplex, degree by degree. Polynomial forms on a simplex have cohomology \(\mathbf Q\) in degree zero and zero otherwise. Polynomial forms vanishing on its boundary have cohomology \(\mathbf Q\) in degree \(p\), with oriented integration giving the isomorphism.

**Proof.** The ideal of restriction to face \(i\) in the differential-form algebra is \((t_i,dt_i)\). For any proper subset of the vertices, its \(t_i\)'s can be included in affine coordinates: eliminate the \(t_j\) of one remaining vertex. In these coordinates the face ideals are coordinate ideals. The monomial basis, including exterior monomials in the differentials, proves the following distributive property: the intersection of a list of face ideals is spanned by the monomials containing, for every listed index \(i\), either \(t_i\) or \(dt_i\). Successively correcting a lift on one face by a term vanishing on the previous faces therefore extends every compatible family for a proper subset of the faces.

For the complete boundary, localize the coordinate ring where \(t_j\) is invertible. Face \(j\) is absent there, and the other faces have precisely the coordinate description just given. Thus the boundary restriction is locally surjective on the affine cover \(D(t_j)\). It is a map of modules over the affine polynomial coordinate ring, so its cokernel is zero when all these localizations vanish. Concretely, denominators in the finitely many local lifts can be cleared by powers \(t_j^m\); the ideal generated by these powers is the unit ideal. Indeed, expand \((\sum t_j)^{(p+1)(m-1)+1}=1\): every monomial contains one \(t_j^m\). Combining the cleared lifts with this identity gives a global polynomial lift. This proves the extension claim without a smooth partition of unity.

Contract \(\Delta^p\) affinely to one vertex. Pull a form back along this polynomial homotopy, contract with the parameter vector, and integrate the polynomial parameter from zero to one. A monomial integral is a rational number \(1/(a+1)\). The product rule and the fundamental theorem of polynomial calculus give
\[
dh+hd=\mathrm{id}-\mathrm{ev}_{\mathrm{vertex}}.
\tag{5.6}
\]
This proves the absolute cohomology calculation over \(\mathbf Q\), and after every characteristic-zero extension.

Integration on an oriented \(p\)-simplex is rational: repeated polynomial integration gives rational monomial integrals. Stokes follows by repeated one-variable polynomial calculus, with the alternating face signs. Hence integration is a map to simplicial cochains.

The boundary-extension assertion gives short exact sequences when a finite simplicial complex is built by adding its simplices in increasing dimension. In dimension zero integration is the identity. Induct on the dimension. For \(\partial\Delta^p\), all its simplices have smaller dimension, so integration is already a cohomology isomorphism. Compare the short exact sequences for forms and simplicial cochains of \((\Delta^p,\partial\Delta^p)\). The absolute calculation (5.6) and the boundary induction imply the relative assertion. Attaching \(p\)-simplices now proves the comparison for every finite complex. In particular the relative cohomology is one line in degree \(p\), and the oriented integration of a normalized top form is \(+1\). No multiplicativity of simplex integration is asserted. \(\square\)

The proof also works with a coefficient vector space \(V\): tensor the finite-dimensional-degree diagram over the field with \(V\), or apply the formulas pointwise to locally constant \(V\)-valued coefficients.

### 5.2. A commutative sheaf resolution

Let \(X\) be a compact smooth manifold. Choose a finite cover \(\mathcal U=(U_i)\) by strongly convex neighborhoods. The required convex neighborhoods are proved in Riemannian connections and convex neighbourhoods, Theorem B.5. Each nonempty finite intersection is contractible: the unique globally minimizing geodesic between two of its points belongs to every member, and contraction to a fixed point is smooth. Intersecting such an intersection with any sufficiently small strongly convex neighborhood has the same property.

For \(J=\{i_0<\cdots<i_p\}\), put \(U_J=\cap_{i\in J}U_i\), and let \(j_J:U_J\to X\) be the open inclusion. Empty intersections contribute zero. Define a sheaf of differential graded algebras \(\mathcal A_{\mathcal U}\) as compatible families
\[
\alpha_J\in
(j_J)_*\underline{\Omega_{\mathrm{pol}}(\Delta^p;\mathbf Q)}.
\tag{5.7}
\]
Compatibility means that restriction of \(\alpha_J\) to a face equals the restriction of the corresponding \(\alpha_{J\setminus i}\) to \(U_J\). Coefficients are locally constant; the differential is the polynomial differential in the simplex variables. Multiplication is pointwise wedge multiplication. There are only finitely many subsets \(J\), so this is a bounded complex of sheaves.

There is a multiplicative augmentation
\[
\mathbf Q_X\longrightarrow\mathcal A_{\mathcal U}
\tag{5.8}
\]
given by the same constant on all simplices.

**Lemma 5.2.** The augmentation (5.8) is a quasi-isomorphism. Every term of \(\mathcal A_{\mathcal U}\) is acyclic for global sections. Therefore
\[
A_{\mathcal U}=\Gamma(X,\mathcal A_{\mathcal U})
\tag{5.9}
\]
is a commutative differential graded model of \(R\Gamma(X,\mathbf Q)\), including its product. The same construction and conclusion hold with every characteristic-zero field.

**Proof.** Truncate the diagram (5.7) to intersections with at most \(p+1\) indices. Lemma 5.1 makes the map to its preceding truncation surjective. Its kernel is the finite sum, over \(|J|=p+1\), of
\[
(j_J)_*\underline{\Omega_{\mathrm{pol}}(\Delta^p,\partial\Delta^p)}.
\tag{5.10}
\]
This is an assertion about sheaves and about their degree terms: the rational linear extension operator applies pointwise to locally constant coefficient families.

Integrate the component on \(p\)-simplices. This gives a map of complexes from (5.7) to the ordinary alternating Čech sheaf complex, whose degree-\(p\) term is \(\bigoplus_{|J|=p+1}(j_J)_*\mathbf Q\). Stokes gives exactly the Čech signs. On each kernel (5.10), integration is a quasi-isomorphism to that Čech term placed in degree \(p\), by Lemma 5.1. Induction on the finite diagram therefore proves that this integration map is a quasi-isomorphism of sheaf complexes.

The augmented Čech sheaf complex is exact. Near a point choose one cover member containing a whole neighborhood; insertion of its index contracts that augmented complex on the neighborhood. This also applies to boundary germs of the other cover members. Thus (5.8) is a quasi-isomorphism. This argument does not interchange an infinite product with stalks.

For any coefficient vector space \(V\), the open direct image \(j_{J*}\underline V\) has no higher derived direct images. Its stalk calculation uses neighborhoods \(W\) with \(W\cap U_J\) either empty or strongly convex. Such nonempty intersections have constant-sheaf cohomology \(V\) in degree zero and zero otherwise. The usual open-direct-image stalk formula follows by restricting an injective resolution and taking the filtered colimit over \(W\). The sheaf/singular comparison required here is Constructible complexes on algebraic varieties, Appendix C.2; the good-cover cochain proof is Connections, curvature and characteristic forms, §A.3. Its subdivision, prism and augmented Čech contractions are linear over the integers and apply with any coefficient vector space \(V\); thus the same comparison applies to the locally constant vector spaces used here.

Consequently
\[
H^q(X,j_{J*}\underline V)=H^q(U_J,\underline V)=0
\quad(q>0).
\tag{5.11}
\]
Each degree term of (5.7) is a finite extension of these acyclic sheaves, by the degreewise version of the filtration (5.10). It is therefore acyclic. A bounded acyclic resolution computes derived global sections, by the earlier bounded-below sheaf-resolution argument. This proves (5.9).

Finally, the product is the actual derived product: (5.8) is a map of sheaf differential graded algebras, and multiplication on its acyclic resolution represents the product of the constant sheaf. Integration was used only to prove a quasi-isomorphism of underlying complexes. It was not used as a purported multiplicative map to singular cochains. \(\square\)

Because every \(U_J\) is connected, (5.9) is just the algebra of compatible polynomial forms on the finite nerve of the cover. This gives an explicit rational commutative replacement for the smooth real/complex forms used in current Lesson 13.

**Naturality and coherence.** For \(f:Y\to X\), take a finite strongly convex cover \(\mathcal V\) of compact \(Y\) refining \(f^{-1}\mathcal U\). Choose an index assignment \(a\) with \(V_j\subset f^{-1}U_{a(j)}\). The induced affine vertex maps of nerves pull polynomial forms back and give a unital commutative differential graded map
\[
A_{\mathcal U}\longrightarrow A_{\mathcal V}.
\tag{5.12}
\]
Its sheaf augmentation identifies its cohomology map with the actual pullback. For refinements of the same \(X\), it is a quasi-isomorphism.

If two index assignments are chosen, their combined images on a nonempty intersection \(V_J\) lie in one simplex of the target nerve: that intersection lies in all the indicated inverse images. Linear interpolation between the two affine vertex maps gives a polynomial homotopy with parameter algebra \(\mathbf Q[s,ds]\). With several choices, barycentric interpolation gives the corresponding simplex of homotopies. It restricts to the prescribed homotopies on every face. Common strongly convex refinements therefore give explicit compatible comparisons, including higher composition comparisons. They preserve multiplication throughout.

### 5.3. Compatible classifying-torus models

Use \(X_n=(\mathbf {CP}^n)^r\). Lemma 5.2 supplies a rational commutative model \(A_n\) from a finite strongly convex cover. For the inclusion \(X_n\to X_{n+1}\), choose a common good refinement on \(X_n\) of its own cover and the pulled-back cover of \(X_{n+1}\). Its model \(B_n\) gives maps
\[
q_n:A_n\longrightarrow B_n,\qquad
r_n:A_{n+1}\longrightarrow B_n,
\tag{5.13}
\]
where \(q_n\) is a quasi-isomorphism and \(r_n\) represents restriction. This avoids assuming that arbitrarily chosen good covers are nested.

Define the following commutative differential graded algebra:
\[
D_{\mathbf Q}=
\left\{(a_n,p_n):
a_n\in A_n,\ p_n\in B_n[s,ds],\
p_n(0)=q_n(a_n),\
p_n(1)=r_n(a_{n+1})\right\}.
\tag{5.14}
\]
Products and differentials are componentwise. This is the explicit path model of the inverse system (5.13), not an unspecified commutative strictification.

Projection to the \(a_n\)'s is surjective in every graded degree: interpolate prescribed endpoint values linearly in \(s\). Its kernel is
\[
\prod_n B_n\otimes\Omega_{\mathrm{pol}}([0,1],\{0,1\}).
\]
Relative polynomial integration identifies the cohomology of this kernel in degree \(j\) with \(\prod_n H^{j-1}(B_n)\). The resulting long exact sequence is the kernel/cokernel sequence for
\[
(x_n)\longmapsto(q_nx_n-r_nx_{n+1})
\tag{5.15}
\]
on the cohomology products. This is checked by differentiating the endpoint interpolation; the overall sign in each degree depends on the tensor-order convention and does not change the kernel or cokernel.

By the integral projective-space calculation of Lesson 13, §3.1, its product comparison and coefficient extension,
\[
H^*(X_n;\mathbf Q)=
\mathbf Q[c_1,\ldots,c_r]/(c_1^{n+1},\ldots,c_r^{n+1}).
\tag{5.16}
\]
In every degree the restriction system eventually stabilizes. The map (5.15) is consequently surjective on each cohomology product: solve on the stable tail by successive lifting, then solve the finitely many preceding coordinates backwards. Products of vector-space complexes preserve cohomology, since primitives can be chosen in every coordinate. The long exact sequence therefore gives, multiplicatively,
\[
H^*(D_{\mathbf Q})=\mathbf Q[c_1,\ldots,c_r].
\tag{5.17}
\]

Choose a closed representative \(z_{i,n}\in A_n^2\) of each integral Chern class's rational image. The two classes in \(B_n\) agree. Hence choose \(b_{i,n}\in B_n^1\) with
\[
db_{i,n}=r_n(z_{i,n+1})-q_n(z_{i,n}).
\]
The path
\[
p_{i,n}=q_n(z_{i,n})+d(s b_{i,n})
=q_n(z_{i,n})+s\,db_{i,n}+ds\,b_{i,n}
\tag{5.18}
\]
is closed and has exactly the two required endpoints. Thus the families \((z_{i,n},p_{i,n})\) are actual closed degree-two elements \(z_i\in D_{\mathbf Q}\). Freeness of the polynomial algebra gives a commutative differential graded map
\[
\mathbf Q[c_1,\ldots,c_r]\longrightarrow D_{\mathbf Q},
\qquad c_i\longmapsto z_i.
\tag{5.19}
\]
It is a quasi-isomorphism by (5.17), not merely a ring isomorphism on an unidentified endomorphism algebra.

Repeat (5.14) with \(\Lambda\)-valued polynomial forms. The exact same relative-interval and stable-cohomology proof gives
\[
H^*(D_\Lambda)=\Lambda[c_1,\ldots,c_r].
\]
Extend the rational cycles (5.18) into \(D_\Lambda\). They give
\[
P_\Lambda\xrightarrow{\ \sim\ }D_\Lambda
\tag{5.20}
\]
as commutative differential graded algebras. No embedding of \(\Lambda\) into \(\mathbf C\) is needed, and no claim that scalar extension commutes with unrestricted products is needed. Equivalently \(D_{\mathbf Q}\otimes\Lambda\to D_\Lambda\) is a quasi-isomorphism, because the preceding explicit calculation identifies its induced cohomology map.

The sheaf resolutions of §5.2, their pullbacks, and their polynomial comparison homotopies show that (5.14) models the actual stable derived sections of the projective Borel models. In each prescribed finite morphism range the projection to a sufficiently large \(A_n\) is the corresponding comparison. The frame/product comparisons in Equivariant perverse sheaves and perverse sheaves on stacks, Lemma B.7, Proposition B.8 and Theorem B.9 identify these projective models with the bounded Borel category. We check the enhancement directly. On the finite free unit generators, the sheaf mapping complexes are the derived section complexes just resolved by \(A_n\). Their comparisons preserve composition because multiplication of the commutative sheaf resolution represents composition of the unit endomorphisms. Fixing one argument and then the other, mapping complexes of finite cones are cones of these complexes, so the quasi-isomorphism extends through every finite cone. A retract takes the image of the corresponding commuting projectors and retains the comparison. The path model records the actual refinement homotopies, and its projection to \(A_n\) is a quasi-isomorphism in every fixed range once \(n\) is large enough. Thus these compatible comparisons identify the stable mapping complexes with \(D_\Lambda\). Tensor products are supplied by the same strictly commutative sheaf multiplication, whose associativity, unit and symmetry identities commute with every refinement and polynomial homotopy. This proves the enhanced comparison used here, in addition to the earlier triangulated model construction.

Start the system with \(X_0=\operatorname{pt}\) and its one-member cover, so \(A_0=\Lambda\). Projection from (5.14) to this component is an augmentation \(D_\Lambda\to\Lambda\). It represents restriction to the chosen base point of the projective Borel models, and hence forgetting equivariance on the point. Since its target has no degree-two elements, (5.20) intertwines it with the usual polynomial augmentation \(c_i\mapsto0\). This also fixes the underlying-point functor; it is not deduced from an abstract unaugmented Morita equivalence.

For additional concreteness, a finite-cell \(P_\Lambda\)-module \(M\) is realized on \(X_n\) by
\[
\mathcal A_n\otimes_{P_\Lambda}M,
\tag{5.21}
\]
using (5.18). On free generators its derived mapping complex is \(A_n\); finite cones and retracts extend this comparison. Since (5.20) is an isomorphism in every stable range, take \(n\) beyond the finitely many shifts and degrees used in any such mapping comparison. These are precisely the common-model comparisons of the bounded equivariant construction. Equivalently, use the existing associative generator equivalence with the actual unit endomorphism algebra, and replace that algebra by the explicitly identified model \(D_\Lambda\). This constructs the object by finite cones of actual equivariant unit morphisms. Its quotient component is (5.21), because that identity holds on the unit and its mapping algebra, then on finite cones and retracts.

The augmented comparison just established identifies the underlying point complex as \(\Lambda\otimes_{P_\Lambda}^{\mathbf L}M\), which is bounded and finite dimensional. One can check the required resolution comparison directly: the free space \((\mathbf C^{n+1}\setminus0)^r\) has zero \(H^2\) for \(n\ge1\), so the pulled-back Chern cycles have primitives. It has a finite good cover obtained from a finite strongly convex cover of \((S^{2n+1})^r\) times its radial \(\mathbf R^r\) factor. Hence §5.2's polynomial model applies there as well. Formula (5.18), with endpoint zero, compares the polynomial action to its augmentation and gives the actual point-resolution isomorphism. The finite cones of unit maps, rather than an unsupported assertion about uniqueness of all algebra nullhomotopies, provide the compatible derived triples.

### 5.4. The symmetric tensor comparison

The generation argument above applies to every characteristic-zero field: at a point all equivariant cohomology objects are finite constant vector spaces, and finite ordinary truncations generate the category from its unit. Its associative generator argument therefore identifies the category at one label with perfect modules over its actual derived endomorphism algebra.

The quasi-isomorphism (5.20) has the following symmetric tensor realization. On the finite model the multiplication map is
\[
(\mathcal A_n\otimes_P M)\otimes_\Lambda
(\mathcal A_n\otimes_P N)
\longrightarrow
\mathcal A_n\otimes_P(M\otimes_P N).
\tag{5.22}
\]
Use finite-cell representatives, so the displayed relative tensors already compute derived tensors. On two free generators (5.22) is multiplication
\(\mathcal A_n\otimes_\Lambda\mathcal A_n\to\mathcal A_n\). It is a quasi-isomorphism: the augmentation \(\Lambda\to\mathcal A_n\) is a stalkwise quasi-isomorphism, and tensor over a field preserves it. Fixing one argument, the class of modules for which (5.22) is a quasi-isomorphism is closed under finite cones and retracts; then fix the other. It follows for all perfect modules.

Associativity, the unit, and graded symmetry of these maps are the corresponding identities of the commutative sheaf differential graded algebra. Refinement and path comparisons preserve those identities. They therefore give a coherent symmetric tensor equivalence, rather than only an associative Morita equivalence or a cohomology-algebra calculation.

Distinct reduced points of \(\operatorname{Gr}_T\) have no morphisms, bounded support is finite, and convolution adds labels. This proves (5.4) below. The character projectors of the dual torus, proved in Lesson 12, equation (7.6), identify those labels with its weight decomposition. Thus (5.4) is also the perfect dual-torus-equivariant polynomial model over every characteristic-zero field.

In the generated category the resulting monoidal comparison is
\[
F(K)\otimes_{A_T}^{\mathbf L}F(L)
 \xrightarrow{\sim}F(K\otimes L).
\tag{5.3}
\]
The sheaf multiplication just proved gives this map on the unit, and finite cones and commuting projectors extend it in both variables. Its associativity, unit and graded symmetry are those of that multiplication.

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

The dual torus has character lattice \(L\). Its adjoint action on its Lie algebra is trivial, and its representation coactions split modules into weights, by the coefficient-projector proof in Lesson 12, equation (7.6), degree by degree. Finite cell modules and their summands have finitely many weights. For every characteristic-zero coefficient field, (5.2) therefore makes (5.4) the torus instance of perfect dual-torus-equivariant modules over the symmetric algebra with its degree-two generators. The unit at label zero corresponds to the **free module**, whose endomorphism algebra is \(A_T\).

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

**Exercise 13.2 (easy).** State and verify derived Satake for a rank-\(r\) torus over any characteristic-zero coefficient field. Identify the unit and convolution.

**Solution.** Put \(L=X_*(T)\) and \(A=\Lambda[c_1,\ldots,c_r]\), with zero differential and each generator of degree two. At one support point, truncation triangles and constant local systems give \(\operatorname{thick}(\Lambda)\). The mapping-complex generator argument of (5.1), together with the commutative polynomial-simplex model (5.2), identifies it with \(\operatorname{Perf}(A)\). Distinct support points have no morphisms; finite support therefore gives the finite sum over \(L\). The tensor comparison (5.3) proves that convolution adds labels and tensors over \(A\), exactly (5.4). Coefficient projectors identify labels with characters of \(\widehat T\). The object at label zero is the free module \(A\). Every ingredient is proved in §5, so this is the fixed-point differential graded tensor equivalence, with no claim about Ran factorization.

**Exercise 13.3 (medium).** For \(G=\mathbf G_m\), show that \(\operatorname{Ext}^1\) between simple objects in the Satake heart vanishes, while the unit has nonzero \(\operatorname{Ext}^2\) in the Borel equivariant derived category. Explain the corresponding degree for \(SL_2\).

**Solution.** Simple torus objects are one-dimensional vector spaces at single labels. A short exact sequence splits by the weight projectors and an ordinary vector-space complement. This proves vanishing of every heart \(\operatorname{Ext}^1\), including self-extensions. In the Borel category, closed extension at the base point and loop contraction prove (2.3); (3.3) identifies its degree-two self-Ext with \(\Lambda c\ne0\). The bounded derived heart has zero morphisms in that degree by the complex-splitting proof of (4.1). For \(SL_2\), (3.8) instead says that degree two is zero and the first positive class is \(c_2\) in degree four. The group cannot be omitted from the assertion.

**Exercise 13.4 (medium).** For \(G=SL_2\), compare \(H^*(BG,\Lambda)\) with \(\operatorname{Sym}(\mathfrak g^*[-2])^G\). Do not assume the general characteristic-class theorem.

**Solution.** Polar decomposition and the quaternionic universal bundle reduce the first ring to \(H^*(\mathbf {HP}^{\infty},\Lambda)\). Its rank-four Gysin sequence gives the polynomial ring \(\Lambda[c_2]\) with generator of degree four, by (3.6)–(3.7). For the second ring, write \(p=z^2+xy\). Restriction of an invariant to diagonal trace-zero matrices is even by the Weyl interchange. Subtract its corresponding polynomial in \(p\); the difference vanishes on the dense distinct-eigenvalue locus and is zero. Thus (3.9) is \(\Lambda[p]\), with \(p\) of degree four when the linear coordinates have degree two. Sending \(p\) to \(c_2\) defines the graded algebra isomorphism. This computes the rings and a chosen isomorphism; a universal normalization in arbitrary rank is not being inferred.

**Exercise 13.5 (hard).** For \(A=\Lambda[c]\), \(|c|=2\), and \(B=\bigwedge(\epsilon)\), \(|\epsilon|=-1\), prove both derived endomorphism calculations and the corresponding generated-category equivalences. Why does this not equate all \(A\)-modules with all \(B\)-modules?

**Solution.** Write \(k\) for the augmentation object. Resolve \(k_A\) by \(P=A\otimes\bigwedge(e)\), \(|e|=1\), \(de=c\). Multiplication by \(c\) is injective, so the augmentation is a quasi-isomorphism. The closed contraction \(\iota_e\) has degree \(-1\), square zero, and its two classes give all of \(\operatorname{Hom}_A(P,k)\). The finite free comparison therefore proves \(R\operatorname{End}_A(k)\simeq B\).

Resolve \(k_B\) by \(Q=B[f]\), \(|f|=-2\), \(df=\epsilon\). Its positive pairs cancel since \(d(f^{n+1})=(n+1)\epsilon f^n\); the augmentation is a quasi-isomorphism. The increasing polynomial-degree filtration makes it semi-free, and the homotopy-lifting argument in §6 shows it computes derived Hom. The closed operator \(\partial_f\) has degree two. Its powers, followed by augmentation, give the dual basis to \(f^n\), with nonzero coefficients \(n!\). Thus \(\Lambda[c]\to\operatorname{End}_B(Q)\), \(c\mapsto\partial_f\), is a quasi-isomorphism. There is one basis element in each nonnegative even degree, without a completion.

The two generator mapping-complex arguments give \(\operatorname{thick}_A(k)\simeq\operatorname{Perf}(B)\) and \(\operatorname{thick}_B(k)\simeq\operatorname{Perf}(A)\). The second takes \(k_B\) to \(A\), while the free \(B\)-module goes to a different object. These equivalences specify their generated subcategories. In all \(B\)-modules, the same \(k_B\) fails compactness by the product-versus-sum calculation (7.1). It is compact in its own Ind-completion (7.2). There is also a direct failure of the first functor on all \(A\)-modules: the nonzero module \(A[c^{-1}]\) is sent to zero by \(R\operatorname{Hom}_A(k,-)\). Its Hom complex from \(P\) has differential multiplication by \(c\), now an isomorphism, and is contractible. Thus that functor is not faithful on all modules. Passing to larger categories without specifying the completion would invalidate the assertion.

## 11. Scope and free reading

The proved statements are the unit self-Ext formula (2.3), the general invariant-polynomial classifying-space ring in §3, the torus symmetric tensor model over every characteristic-zero field in §5, the two Koszul endomorphism calculations and generated-category equivalences in §6, and the compactness distinction in §7. The five exercises use those proofs. The general bounded, renormalized, singular-support and factorization theorems in §8 are stated here; their general proofs remain unfinished.

Free further reading:

- [Luigi Lunardon, *Some remarks on Dupont contraction*, arXiv:1807.02517](https://arxiv.org/abs/1807.02517), for polynomial simplex forms and simplicial comparisons.

- [Bezrukavnikov–Finkelberg, *Equivariant Satake category and Kostant–Whittaker reduction*, arXiv:0707.3799v4](https://arxiv.org/abs/0707.3799v4), Theorem 5 and §6.6.
- [Arinkin–Gaitsgory, *Singular support of coherent sheaves, and the geometric Langlands conjecture*, arXiv:1201.6343v4](https://arxiv.org/abs/1201.6343v4), §§12.2–12.5.
- [Campbell–Raskin, *Langlands duality on the Beilinson–Drinfeld Grassmannian*, arXiv:2310.19734v2](https://arxiv.org/abs/2310.19734v2), §§5.7, 6.3, 6.6 and 8.10.
- [Gaitsgory–Raskin, *Proof of the geometric Langlands conjecture II: Kac–Moody localization and the FLE*, arXiv:2405.03648v3](https://arxiv.org/abs/2405.03648v3), §§1.5–1.8 and Appendix E.

The proofs from earlier programme lessons are linked at the points where they are used. The reading list does not replace any of them.
