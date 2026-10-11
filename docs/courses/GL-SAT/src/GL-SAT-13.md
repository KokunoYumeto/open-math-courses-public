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

## Appendix A. Arithmetic Ext purity and the formal generator category

This appendix proves the purity and formality steps for the actual spherical generators. It does not identify their full graded Ext category with the dual Lie-algebra model; that further comparison is needed for (8.1). We work over \(\overline{\mathbf F}_q\), with finite \(E/\mathbf Q_\ell\), \(\ell\nmid q\), and a chosen \(a\in E\) with \(a^2=q\). The coefficient \(E(1/2)\) has geometric Frobenius \(a^{-1}\). Write \(A_\lambda=I_\lambda(d_\lambda/2)\) for the normalized geometric IC with its specified split Weil structure.

The finite rational coefficient operations and trace orientations are proved in Semi-infinite orbits and weight functors, Appendices O–Q, with the supported section comparisons in The Satake category, Lemmas A.1.1.1–A.1.2.1. The split Tate stalk and costalk operators are proved in Consequences and examples, Theorem C.3.1.1. The free [Equivariant Satake category and Kostant–Whittaker reduction, §§6.5–6.6](https://arxiv.org/abs/0707.3799v4) supplies the formality context; the algebraic and geometric arguments used below are proved here.

### A.1. Arithmetic classifying-space cohomology

We use actual finite free-frame models in every prescribed degree range. Their algebraic construction is the one in Equivariant perverse sheaves and perverse sheaves on stacks, Propositions B.6–B.8. Here is the constant-adic acyclicity calculation needed to use the same frames in this characteristic.

For \(V_{N,r}\) consisting of \(r\) independent columns in \(k^N\), successive column-forgetting maps have, on minor charts, fibre
\(\mathbf A^{r-1}\times(\mathbf A^{N-r+1}\setminus0)\).
Relative zero-section localization and the supported vector trace give
\[
 H^j(\mathbf A^d\setminus0,E)=
 \begin{cases}E,&j=0,\\ E(-d),&j=2d-1,\\0,&\text{otherwise}.\end{cases}
\tag{A.1.1}
\]
Indeed the zero section has supported coefficient \(E(-d)[-2d]\), obtained by composing the \(d\) coordinate section comparisons. The ordinary coefficient of affine space is \(E\), by the relative affine-line calculation iterated \(d\) times. The localization triangle then gives exactly (A.1.1). Its maps are the zero-section class and the trace, so are Frobenius compatible. This calculation is relative on the trivializing charts. For a pulled-back admissible coefficient complex the same localization triangle tensors with that complex, by the actual section comparisons and proper projection maps of Lesson 5 Q; it gives the same unit range. The units for successive column projections are therefore isomorphisms through degree \(2(N-r)\); their cones start above that range, and left t-exact ordinary direct image preserves that bound under composition. This proves the needed stable-range comparison. It does not compare arbitrary sheaves merely by their pointwise fibres.

All quotient and flag maps below are algebraic maps on these free frames. Quotients are obtained by the finite homogeneous-space and torsor charts in the cited construction; only its topological acyclicity calculation has been replaced by (A.1.1). Increasing \(N\) increases the proved coefficient range. Equivalently their mapping and cohomology comparisons can be computed on the whole action nerve; the frame units identify those comparisons in each fixed range.

**Theorem A.1.1.1.** If \(L/\mathbf F_q\) is split connected reductive, then \(H^{2j+1}(BL,E)=0\), every \(H^{2j}(BL,E)\) is finite dimensional, and its actual Frobenius is \(q^j\operatorname{id}\). The same holds for a split group \(H=U\rtimes L\) whose \(U\) has the affine ordered coordinates of a split unipotent group.

**Proof.** For a split torus \(T\), use the product of the \(r\) projective-space frame models. The split affine cells of each projective space and their oriented cycle classes give
\[
 H^{2j}(BT,E)=E(-j)^{b_j},\qquad
 H^{2j+1}(BT,E)=0.
\tag{A.1.2}
\]
This is the actual scalar operator, by Lesson 12 C.1.1.1, rather than an inference from a trace. For \(U\), every level \(U^s\) of the group nerve is an affine space. Its ordinary constant cohomology is \(E\) in degree zero. The augmented nerve of these constant complexes contracts by the degeneracy maps: insertion of the identity gives the contracting homotopy in positive simplicial degrees. Consequently \(R\Gamma(BU,E)=E\). The same relative calculation on torsor charts identifies the unit \(E\to R(BH\to BL)_*E\), so \(BH\) has the same groups and operators as \(BL\).

Take a split Borel \(B\subset L\). The map \(V/B\to V/L\) of a sufficiently large common frame is smooth proper with fibre \(L/B\), of dimension \(m\). There is an ample \(L\)-linearized flag line, as proved in AG-RG-03 Lemma 5.1. Let \(\eta\) be its descended Kummer first Chern class. Structural trace and projection give
\[
 \pi_*(\eta^m\cup\pi^*x)=s x,\qquad
 s=\int_{L/B}c_1(\mathcal L)^m\in\mathbf Q_{>0}.
\tag{A.1.3}
\]
We justify that scalar in the adic setting. A positive power \(\mathcal L^d\) gives a projective embedding. Choose \(m\) hyperplanes meeting its smooth image transversally in finitely many reduced points after a finite separable field extension. Such hyperplanes exist: the incidence of a point and a hyperplane containing its projective tangent space has dimension smaller than the hyperplane parameter space; proper projection makes its bad image closed. Apply this argument successively to the smooth intersections. The final intersection is nonempty and finite, by the projective dimension theorem used in the flag construction. The divisor section comparisons identify the product of their Kummer classes with the supported class of those points. Each rational point has trace one. Thus the top trace is their positive number divided by \(d^m\). The supported products and trace commute with that field extension; this is the displayed nonzero rational scalar already over the original field.

Smooth proper base change identifies the same fibre scalar on every geometric fibre of the finite frame. Hence \(\pi_*(\eta^m)\) is \(s\) times its unit section. Projection proves (A.1.3). Its classes lie in \(H^{2m}(-,E(m))\), and trace is correspondingly twisted, so this left inverse commutes with Frobenius. Since \(s\ne0\) in the characteristic-zero coefficient field, flag pullback is injective. The successive affine root coordinates of \(B/T\) identify \(H^*(BB,E)=H^*(BT,E)\), using the same ordinary affine-line unit. In each stable range we have therefore obtained
\[
 H^*(BL,E)\hookrightarrow H^*(BT,E).
\tag{A.1.4}
\]
The right side is finite dimensional in each degree, zero in odd degree, and has exactly the scalar in (A.1.2). Its Frobenius-stable subspace has that same scalar. This proves the theorem, including the unipotent extension case. ∎

### A.2. Pure equivariant Ext from actual restrictions

**Theorem A.2.1.1.** For any two normalized spherical IC generators, every finite-dimensional group
\[
 \operatorname{Ext}^n_{L^+G}(A_\lambda,A_\mu)
\tag{A.2.1}
\]
has Frobenius with sole eigenvalue \(a^n\). A Jordan part is allowed in this assertion. The proof applies to all original split connected reductive groups, using their actual sufficiently large jet action.

**Proof.** Fix a finite closed union containing both supports, and a sufficiently large jet level. Its orbit stabilizers are connected and have split reductive Levi quotient with split unipotent radical: the constant parabolic and the remaining root and torus coefficients are the actual stabilizer coordinates of Lessons 4 §2 and 6 §§1–2. The classifying-space groups of every stabilizer consequently have the actual scalar \(a^p\) in degree \(p\), by A.1.

On an orbit \(S\) of dimension \(d\), put \(K=i_S^*A_\lambda\), \(L=i_S^!A_\mu\). The ordinary cohomology fibres of \(K\) in degree \(u\) and \(L\) in degree \(v\) have actual scalar operators \(a^u,a^v\), by Lesson 12 C.3.1.1 and its dual costalk comparison. For the exceptional restriction this includes the stratum normalization: the point's additional exceptional pullback contributes \([-2d](-d)\), so dividing its scalar by \(q^d=a^{2d}\) gives precisely \(a^v\) on the orbit fibre. Equivariance transports these fibres over the whole orbit; connected stabilizers leave their cohomology systems constant, by Lesson 6 B.1.

The action-nerve mapping complex on this orbit has its ordinary hypercohomology spectral sequence. At a point, complexes of finite-dimensional vector spaces split into their cohomology and contractible pairs. Thus its degree-\(t\) fibre Hom is
\[
 \bigoplus_u\operatorname{Hom}_E(H^uK,H^{u+t}L)
\tag{A.2.2}
\]
with sole scalar \(a^t\). No splitting of the full equivariant objects is being asserted. The cohomology local systems of this fibre Hom are constant on the classifying space of the connected stabilizer. The nerve spectral sequence consequently has terms \(H^p(BH,E)\) tensored with (A.2.2). Each term of total degree \(n=p+t\) has scalar \(a^n\).

A differential has total degree one and commutes with Frobenius. It is zero, since its source and target have distinct sole eigenvalues \(a^n,a^{n+1}\). More explicitly, an intertwiner between finite generalized eigenspaces with distinct eigenvalues is zero: apply the relatively prime annihilating polynomials and their Bézout identity. The orbit Ext groups thus have a finite filtration whose degree-\(n\) quotients all have eigenvalue \(a^n\). They are finite dimensional. The bounded fibre degree range and the finiteness of \(H^p(BH)\) give the required convergence.

Finally order the finitely many orbits so that the successive unions are closed. Source localization triangles give a finite filtration of the global mapping complex with terms
\(R\operatorname{Hom}_S(i_S^*A_\lambda,i_S^!A_\mu)\).
All triangles and maps are the actual equivariant coefficient maps and commute with Frobenius. Its spectral sequence has the same degree and eigenvalue property, so again every differential is zero. A finite extension of generalized \(a^n\)-eigenspaces is still a generalized \(a^n\)-eigenspace: a product of their annihilating polynomials annihilates the extension. This proves (A.2.1). It does not turn such an extension into a split scalar Frobenius module. ∎

### A.3. Minimal models and a nonresonant automorphism

We spell out the algebra used to pass from these groups to mapping complexes. A minimal \(A_\infty\) category has graded Hom spaces and operations \(m_r\) of degree \(2-r\), with \(m_1=0\). Suspend the Hom spaces by an operator \(s\) of degree \(-1\). On their tensor coalgebra of composable words, these operations are the components of a degree-one coderivation \(b\), with \(b^2=0\). All signs below are the tensor Koszul signs. A coalgebra map is determined by its components on single-output words. It is invertible whenever its first component is invertible, by induction on word length.

**Lemma A.3.1.1.** A differential graded category over a field has a minimal \(A_\infty\) model on its cohomology Hom spaces, with its ordinary binary composition. A quasi-equivalence or an equivalence of enhanced objects induces an \(A_\infty\) equivalence of these models.

**Proof.** On each Hom complex choose representatives for cohomology, complements to boundaries in cycles, and complements to cycles. This gives maps \(i,p,h\) with
\[
 pi=1,\qquad dh+hd=1-ip,\qquad
 h^2=hi=ph=0.
\tag{A.3.1}
\]
On words the tensor maps \(I,P\) give a contraction for the tensor differential \(d_0\). Its homotopy is the signed sum
\[
 H_r=\sum_{j=1}^r(ip)^{\otimes(j-1)}
                 \otimes h\otimes1^{\otimes(r-j)}.
\tag{A.3.2}
\]
Expanding \(d_0H_r+H_rd_0\) telescopes to \(1-(ip)^{\otimes r}\). The same side conditions give \(H^2=HI=PH=0\). Its coproduct identity is
\(\Delta H=(H\otimes1+IP\otimes H)\Delta\), verified by dividing the sum at each cut of a word.

Let \(\delta\) be the coderivation for the original binary product. It lowers word length by one. Define
\[
 I_\infty=(1+H\delta)^{-1}I,\qquad
 P_\infty=P(1+\delta H)^{-1},\qquad
 b_H=P\delta(1+H\delta)^{-1}I.
\tag{A.3.3}
\]
The inverses here are finite geometric sums on every fixed word, not analytic limits. The recursion \(I_\infty=I-H\delta I_\infty\), its counterpart for \(P_\infty\), and (A.3.1) give
\((d_0+\delta)I_\infty=I_\infty b_H\),
\(P_\infty(d_0+\delta)=b_HP_\infty\),
and \(P_\infty I_\infty=1\).
To check these identities, substitute the recursions, use \(d_0H+Hd_0=1-IP\), and collect terms containing \((d_0+\delta)^2=0\). At word length \(r\) the leftover terms have smaller word length and vanish inductively, starting with \(r=1\). The same coproduct identity for \(H\), applied to those recursions and to the coderivation identity for \(\delta\), proves that \(I_\infty,P_\infty\) are coalgebra maps and \(b_H\) is a coderivation. Applying \(P_\infty\) and \(I_\infty\) to the square-zero identity gives \(b_H^2=0\). Its first component is zero and its second is \(p\,m_2(i\otimes i)\), the cohomology product.

For a dg functor \(f\), the map \(P_\infty f I_\infty\) is an \(A_\infty\) functor with first component \(H(f)\). If that component is invertible, the word-length recursion constructs its coalgebra inverse, which also commutes with the coderivations. Changing the choices uses the same construction on the identity of the original category, so gives an equivalence between the models. Closed homotopy equivalences of enhanced objects give the same conclusion after adjoining those objects to one dg category. Units are preserved on cohomology; equivalently the construction can be normalized at identity arguments using the side conditions in (A.3.1). This is sufficient for the unital finite-cone and retract envelopes. ∎

**Theorem A.3.1.2.** Let \(\mathcal C\) be a minimal \(A_\infty\) category with degreewise finite-dimensional Hom spaces. Suppose it has an \(A_\infty\) automorphism \(F\) fixing its objects, such that the first component on every degree-\(n\) Hom space has sole eigenvalue \(a^n\), where \(a\) is not a root of unity. Then an \(A_\infty\) change of coordinates with first component the identity sends \(\mathcal C\) to its ordinary graded cohomology category, with all \(m_r=0\) for \(r>2\). Jordan parts of \(F_1\) are permitted.

**Proof.** First linearize \(F\). Suppose its components from arity two through arity \(r-1\) have already been removed. Conjugate by a coalgebra change of coordinates whose only new component is \(g_r\), of unsuspended degree \(1-r\). At arity \(r\) its new component is
\[
 F_r+g_rF_1^{\otimes r}-F_1g_r.
\tag{A.3.4}
\]
For a tuple of input degrees \(n_1,\ldots,n_r\), the output of \(g_r\) has degree \(\sum n_i+1-r\). The operator on that finite-dimensional Hom block
\[
 g\longmapsto gF_1^{\otimes r}-F_1g
\tag{A.3.5}
\]
is invertible. Indeed its two commuting multiplication operators have respective sole eigenvalues \(a^{\sum n_i}\) and \(a^{\sum n_i+1-r}\); their difference is nonzero for \(r>1\). Subtract those scalars to obtain commuting nilpotent operators. Their difference is nilpotent, by its binomial expansion. The inverse of the nonzero scalar plus that nilpotent operator is a finite geometric polynomial. Solve (A.3.5) uniquely to make (A.3.4) zero.

There are possibly infinitely many degree tuples, but a graded multilinear cochain is their product of finite Hom blocks. The inverse just described is applied componentwise. It requires no uniform bound on the Jordan sizes. Iterating in \(r\) gives a change of coordinates: every component on a fixed word has stabilized after finitely many steps. The new automorphism has only \(F_1\).

It commutes with the transformed coderivation. For \(r>2\), the transformed \(m_r\) has output degree \(\sum n_i+2-r\). Thus the equation
\[
 F_1m_r=m_rF_1^{\otimes r}
\tag{A.3.6}
\]
intertwines generalized eigenspaces with distinct sole eigenvalues \(a^{\sum n_i+2-r}\) and \(a^{\sum n_i}\). The same invertibility calculation forces \(m_r=0\). The binary product is unchanged by a coordinate change with linear term the identity, and its two eigenvalues agree. This proves the assertion. The construction did not assume a weight decomposition on the original cochain spaces, or semisimplicity of their Frobenius action. ∎

### A.4. The actual arithmetic generator envelope

Let \(\mathcal E_G\) be the graded category with objects \(A_\lambda\) and actual morphisms \(\operatorname{Ext}^*_{L^+G}(A_\lambda,A_\mu)\), with their genuine Yoneda composition and zero differential. Let \(\operatorname{Perf}(\mathcal E_G)\) denote the idempotent-complete finite-cone envelope of its represented modules.

**Theorem A.4.1.1.** The geometric bounded finite-support spherical derived category, with the actual rational-adic coefficient enhancement, is equivalent to \(\operatorname{Perf}(\mathcal E_G)\). It is the category of its actual graded Ext generators; no dual Lie-algebra identification or monoidal upgrade is asserted by this theorem.

**Proof.** On finite jet and free-frame diagrams take the compatible coefficient resolutions used in the rational-adic enhancements of Lesson 5 P–Q and Lesson 12 N. Their Hom complexes and composition give the enhanced generator category. At each coefficient level the underlying injective-resolution existence and comparison are proved in Sheaves of modules and their derived categories, Theorem 6.1 and Lemmas 6.2–6.3. Compatible cartesian action-nerve diagrams retain the equivariant data. Increasing the frame compares these complexes in each required degree range by the pulled-coefficient unit calculation of A.1; none of the action levels is discarded. Increasing a sufficient jet level has the same property: its kernel is split unipotent with \(R\Gamma(BU,E)=E\), so the corresponding nerve unit identifies mapping complexes. The finite model thus defines the same generator enhancement at every sufficient level.

Arithmetic Frobenius pullback is an exact equivalence of these coefficient sites, and hence gives a dg functor on the resolution enhancement. Each chosen Weil structure identifies its generator with its pullback by a closed enhanced homotopy equivalence. Adjoin the pullback representatives when necessary, apply A.3.1.1, and identify them with the original labels. This gives an \(A_\infty\) automorphism of the minimal generator category whose first component is precisely the actual Frobenius on Ext. By A.2 its sole eigenvalue in degree \(n\) is \(a^n\), and \(a\) is not a root of unity. A.3.1.2 therefore makes this category equivalent to \(\mathcal E_G\).

For completeness, the generators and their finite envelope really give the bounded category. Bounded perverse truncations express any bounded finite-support object by finitely many cones of its perverse cohomology objects. The geometric spherical heart is semisimple with simples \(A_\lambda\), proved in Lessons 6 B.1 and 11 C–D. Each perverse cohomology object is a finite sum of those simples. Retracts remain bounded and finite supported, as their ordinary and perverse cohomology are retracts of the corresponding finite objects.

Enhanced Yoneda is fully faithful on the generators: evaluation of a represented module at its representing object gives its mapping complex, with exactly the original composition. Its comparison extends in the first argument and then the second through shifts and finite cones, because Hom from or into a cone is the corresponding mapping cone. It extends through retracts by taking the images of their commuting projectors. Its essential image is therefore exactly the finite-cone and retract envelope of the represented modules. A quasi-equivalence of the generator categories gives the same comparisons on every such construction, again in both variables. Applying the preceding formality equivalence proves the theorem.

The remaining step toward (8.1) is an actual composition-preserving identification of \(\mathcal E_G\) with the free dual-group polynomial generators. Compatibility with convolution and change to complex coefficients also need their own enhanced comparisons. This theorem supplies neither merely from a list of Ext dimensions. ∎

![Orbit restriction scalars give actual Ext purity; enhanced Frobenius gives the formal generator category without discarding Jordan parts](assets/arithmetic-ext-to-formal-generators.png)

Theorems A.1.1.1–A.2.1.1 and A.3.1.2–A.4.1.1 give every group, map, degree and nonresonance condition displayed. The last box is the actual graded Ext category; its further dual Lie-algebra identification is a separate requirement. Editable SVG source.

### A.5. Why a one-sided weight inequality is insufficient

**Proposition A.5.1.1.** The condition \(H^n_j(D)=0\) for \(j<n\) on a bigraded dg algebra does not in general give a dg morphism, even after inverting quasi-isomorphisms, from its diagonal cohomology algebra into \(D\) inducing the inclusion of that diagonal.

**Proof.** Over a characteristic-zero field let
\[
 D=\bigwedge(a,b,c),\quad |a|=|b|=|c|=1,\quad
 da=db=0,\quad dc=ab,
 \qquad w(a)=w(b)=1,\quad w(c)=2.
\tag{A.5.1}
\]
The differential preserves inner weight. A direct basis calculation gives
\[
 H^0=k,\quad H^1=k[a]\oplus k[b],\quad
 H^2=k[ac]\oplus k[bc],\quad H^3=k[abc],
\tag{A.5.2}
\]
of weights \(0,1,3,4\) respectively. Thus every weight is at least its cohomological degree. Its diagonal algebra is \(k\oplus k[a]\oplus k[b]\), with all positive products zero.

In \(D\), the triple Massey product \(\langle[a],[a],[b]\rangle\) has the unique value \([ac]\), up to the chosen overall sign convention, and is nonzero. Indeed \(a^2=0\), \(ab=dc\), so a defining pair of primitives is \(0,c\). Its resulting cycle is \(ac\). The possible indeterminacy is \(aH^1+H^1b=0\), since all those products are either zero or the boundary \(ab\). No boundary has an \(ac\) component. In the diagonal algebra the same triple product has only value zero.

We recall the exact invariance needed here. A dg map sends cycles and defining primitives to a defining system, hence sends its value into the target product. A quasi-isomorphism also preserves the entire product: lift the three cycle classes; whenever a required product is exact, lift its primitive after correcting its differential by a boundary, using the isomorphisms on cohomology. The difference between two such corrections is a cycle and changes the value by precisely the displayed indeterminacy. Applying the same argument in the reverse direction proves equality of the product sets. Along any zigzag representing a map in the localization, zero in a defined product therefore propagates through forward dg maps and inverse quasi-isomorphisms. A morphism inducing the diagonal inclusion would send the zero triple value to the nonzero singleton \([ac]\), a contradiction.

In contrast, if all cohomology is on the diagonal, the familiar truncation proof is valid. Define
\(U^n_j=D^n_j\) for \(n<j\), \(U^j_j=\ker(d:D^j_j\to D^{j+1}_j)\), and \(U^n_j=0\) for \(n>j\).
This is a subalgebra: equality in the product degree bound forces both factors to be closed diagonal elements. Its map to diagonal cohomology is multiplicative. Full diagonal purity makes both the inclusion and that projection quasi-isomorphisms, weight by weight. In (A.5.1) the projection kills the nonzero classes \(ac,bc,abc\), so is not a quasi-isomorphism. This identifies exactly the missing hypothesis. ∎

![The explicit exterior algebra satisfies the one-sided weight bound but has a nonzero Massey product and off-diagonal cohomology](assets/one-sided-weight-massey-obstruction.png)

Proposition A.5.1.1 and Exercises A.6.1–A.6.3 compute the full differential, cohomology, weight obstruction and enhanced-automorphism condition. A degree bound on cohomology alone does not create the required chain comparison. Editable SVG source.

### A.6. Exercises

**Exercise A.6.1 (medium).** In the algebra (A.5.1), compute every differential on its eight exterior basis elements. Verify both the one-sided weight inequality and its failure to imply diagonal formality.

**Solution.** On \(1,a,b\) the differential is zero; on \(c\) it is \(ab\). The product rule gives \(d(ab)=0\), \(d(ac)=-aab=0\), \(d(bc)=-bab=0\), and \(d(abc)=ab\,ab=0\). Thus the only nonzero differential is \(c\mapsto ab\). The classes and weights are exactly (A.5.2); every weight is at least the degree, while \(ac,bc,abc\) are off the diagonal. The triple product from A.5 is nonzero and cannot be imported from the square-zero diagonal algebra. This calculation tests a chain-level obstruction rather than a parity count.

**Exercise A.6.2 (medium).** For an arity-\(r\) coordinate change \(g_r\) and an arity-\(r\) operation \(m_r\), compute the two nonresonance exponents. Allow nontrivial Jordan blocks and give the inverse used in the first equation.

**Solution.** The output degrees are \(\sum n_i+1-r\) and \(\sum n_i+2-r\). Their Frobenius eigenvalue ratios to the input product are therefore \(a^{1-r}\) and \(a^{2-r}\). The first is different from one for every \(r>1\), and the second for every \(r>2\). On a fixed finite Hom block (A.3.5) is \(sI+N\), where \(s=a^{\sum n_i}-a^{\sum n_i+1-r}\ne0\) and \(N\) is nilpotent, after identifying the commuting input and output multiplications. Its inverse is \(s^{-1}\sum_{j=0}^{M-1}(-N/s)^j\) for any \(M\) with \(N^M=0\). The same argument forces the higher operation to vanish. No diagonalization of the Jordan blocks was used.

**Exercise A.6.3 (advanced).** Let \(H=k1\oplus kx\oplus ky\), with \(|x|=1,|y|=2\), all products of positive-degree elements zero, and \(m_3(x,x,x)=y\) as the only higher operation on such arguments. Verify this defines a minimal strictly unital \(A_\infty\) algebra. Show that the graded automorphism \(F_1(x)=ax,F_1(y)=a^2y\), with \(a\ne0,1\), cannot lift to an \(A_\infty\) automorphism.

**Solution.** In the reduced bar coalgebra the suspended positive generators have degrees zero and one. Its only nonzero coderivation component replaces three consecutive \(sx\)'s by \(sy\). Two overlapping replacements give zero because a replacement inserts \(sy\); two disjoint replacements cancel in the square, since the coderivation has odd degree. Hence \(b^2=0\). Extending the ordinary unit with all higher operations containing it zero gives the unital identities: a unit in a binary vertex removes that vertex, and the two adjacent removals have opposite Koszul signs. On positive inputs the binary products are zero, so there are no remaining mixed binary terms. This proves the stated identities.

For an automorphism's arity-three equation on \(x,x,x\), the terms involving \(F_2\) and binary products are zero: \(F_2(x,x)\) has degree one, hence is a multiple of \(x\), whose product with \(x\) is zero. Thus the equation is \(a^2y=a^3y\), impossible for \(a\ne0,1\). A graded cohomology automorphism alone is therefore insufficient for formality. The enhanced Frobenius lift in A.4 is an essential input.

This appendix leaves the dual Lie-algebra Ext computation, its convolution compatibility, and the renormalized, singular-support and factorization enhancements as actual further proof requirements.

## Appendix B. The polynomial generators and their full Kostant restriction

Let \(R\) be the prescribed split connected reductive coefficient group over a characteristic-zero field \(E\), with its actual torus, character lattice and centre. Eventually \(R=\widehat G\); none of the constructions below replaces it by its adjoint quotient. We prove the algebraic generator comparison needed for (8.1). The remaining geometric comparison must identify these modules and their composition with actual equivariant cohomology.

Write \(\mathfrak r=\operatorname{Lie}R\), \(T\subset B\), \(\mathfrak t=\operatorname{Lie}T\), \(r=\dim T\), and \(N=|\Phi^+|\). Choose a nondegenerate invariant form to identify \(\mathfrak r\) with \(\mathfrak r^*\); the derivative formulation below also describes the resulting action directly on the coadjoint space. Every linear coordinate of \(A=E[\mathfrak r^*]=\operatorname{Sym}(\mathfrak r)\) has degree two. Nilpotent means nilpotent in a faithful algebraic module; the toral centre's Jordan component is semisimple and its nilpotent component is zero. Geometric orbit arguments may be checked after algebraic closure. The polynomial maps and the smooth descent diagrams constructed below are defined over \(E\), and their verified identities descend faithfully flatly to it.

The root and torus groups and their full schemes are proved in Root groups and the rank-one subgroups, §§2–5. We use Complete reducibility, Theorems 4.1 and 5.1, [Representations of \(sl_2\)](../RT-LIE/RT-LIE-05.html), and Chevalley restriction, Theorem 3.1, with the coefficient descent of §3 above. The classical highest-weight and character statements are also available from Identifying the dual group, Theorem B.4.1.1. The free [Equivariant Satake category and Kostant–Whittaker reduction, §§2.6 and 4.1](https://arxiv.org/abs/0707.3799v4) gives the restriction problem; we prove its polynomial, regular-locus and morphism assertions here.

### B.1. Polynomial invariants and the sum of their degrees

**Lemma B.1.1.1.** The algebra \(E[\mathfrak t]^W\) is polynomial on \(r\) homogeneous generators of degrees \(d_1,\ldots,d_r>0\), and
\[
 \sum_i(d_i-1)=N.
\tag{B.1.1}
\]

**Proof.** First take the semisimple part and its auxiliary simply connected torus \(T_{\rm sc}\), whose character lattice is the full weight lattice. This auxiliary torus is only used to prove a statement about the linear Weyl action. It does not replace \(R\) in any representation or centralizer comparison.

The invariant Laurent algebra \(E[T_{\rm sc}]^W\) is polynomial in the fundamental characters \(\chi_{\omega_i}\). Indeed its orbit sums have one basis element for each dominant weight. The product \(\prod_i\chi_{\omega_i}^{n_i}\) has highest weight \(\sum_i n_i\omega_i\) with coefficient one and only lower weights. Induction on the positive root height expresses every orbit sum as a polynomial in these characters. The induction terminates: a strictly lower dominant weight has strictly smaller nonnegative height. Algebraic independence follows by taking a maximal dominant weight among the finitely many monomials in a proposed relation; its coefficient cannot be supplied by a lower monomial. These are exactly the finite highest-weight and tensor arguments already proved in Lesson 11.

Complete the torus quotient at the image of the identity. Its invariant algebra completes to a formal power-series ring in \(\chi_{\omega_i}-\dim V_{\omega_i}\). Its fibre over that point has only the identity as a geometric point: a finite-group invariant separates two distinct finite orbits, by prescribing values on their finite point sets and averaging. The Laurent algebra is finite over its invariants, because each coordinate and its inverse satisfy their monic orbit polynomials. Thus completing at that invariant ideal is the same as completing the torus algebra at the identity; the two ideals have cofinal powers.

Invariants commute with this completion. To verify this, let \(I\) be an ideal of the invariant algebra. The averaging projector is linear over that algebra, so \(I^nE[T_{\rm sc}]\cap E[T_{\rm sc}]^W=I^n\). It also lifts an invariant class modulo \(I^n\) by averaging any lift. Taking the inverse limit proves the claim.

Formal logarithms of a character basis identify the completed torus with the formal vector space \(\mathfrak t_{\rm sc}\), equivariantly for \(W\): the characteristic-zero series \(\log(q_i)\) has inverse \(\exp(z_i)\), and logarithms turn multiplication of characters into addition. Hence \(E[[\mathfrak t_{\rm sc}]]^W\) is a regular power-series algebra on \(r_{\rm ss}\) variables.

For clarity this implies polynomiality of the graded invariant algebra, rather than merely a formal statement. Let \(C=E[\mathfrak t_{\rm sc}]^W\), with positive ideal \(\mathfrak m\). It is finitely generated: the coefficients of the orbit polynomials of a linear coordinate basis generate a Noetherian algebra over which the polynomial ring is finite; its invariant submodule is therefore finite over that algebra. The degree filtration and the \(\mathfrak m\)-adic filtration are cofinal, since the degrees of a finite homogeneous generating set are positive and bounded. Its completion is consequently the invariant formal series just calculated. Thus \(\dim_E\mathfrak m/\mathfrak m^2=r_{\rm ss}\). Choose a homogeneous basis and representatives \(f_i\). Induction on degree generates \(C\) from them: a positive homogeneous element modulo their linear span is in \(\mathfrak m^2\), whose factors have smaller positive degrees. The \(f_i\) are algebraically independent, because the fraction field of \(C\) has transcendence degree \(r_{\rm ss}\), by the finite integral extension to the polynomial ring. A relation among \(r_{\rm ss}\) generators would lower that transcendence degree. Adjoining the centre's linear coordinates proves polynomiality for all \(R\).

Finally averaging the trace of \(W\) on symmetric powers gives
\[
 \prod_i(1-t^{d_i})^{-1}
       =\frac1{|W|}\sum_{w\in W}\det(1-tw)^{-1}.
\tag{B.1.2}
\]
This identity follows by diagonalizing each finite-order \(w\) and multiplying its geometric series; it is an identity of formal power series. Put \(u=1-t\). On the left the first two Laurent coefficients are
\((\prod d_i)^{-1}u^{-r}(1+\frac12\sum(d_i-1)u+\cdots)\).
On the right the identity contributes \(|W|^{-1}u^{-r}\), and each reflection contributes \((2|W|)^{-1}u^{1-r}\). All other elements contribute lower pole orders. There are precisely \(N\) reflections: the root hyperplanes are the chamber walls and all their translates; a reflection's generic fixed point must lie on one of them, since a point off them has trivial chamber stabilizer. There is one reflection per positive root. Comparing these two coefficients proves \(\prod d_i=|W|\) and (B.1.1). For a torus \(W=1\), all degrees are one and the same assertion is immediate. ∎

### B.2. A polynomial Kostant slice with its positive grading

Choose pinned root vectors \(e_i,f_i\) with \([e_i,f_i]=\alpha_i^\vee\). Let
\[
 h=2\rho^\vee=\sum_i c_i\alpha_i^\vee,\qquad
 e=\sum_i e_i,\qquad f=\sum_i c_i f_i.
\tag{B.2.1}
\]
The \(c_i\) are positive integers, because \(2\rho^\vee\) is the sum of the positive coroots. The actual cocharacter \(2\rho^\vee\) belongs to the original coroot lattice.

**Theorem B.2.1.1.** The affine slice \(\Sigma=e+\mathfrak r^f\) is mapped isomorphically by the adjoint quotient
\[
 \chi:\mathfrak r^*\longrightarrow
       \mathfrak b=\operatorname{Spec}E[\mathfrak r^*]^R.
\tag{B.2.2}
\]
This is a polynomial isomorphism with a polynomial inverse on every parameter algebra. Under the slice action
\[
 t\cdot x=t^2\operatorname{Ad}_{h(t^{-1})}x,
\tag{B.2.3}
\]
its coordinate weights are \(2d_i\). Every slice point is regular.

**Proof.** The simple-root relations give \([e,f]=h,[h,e]=2e,[h,f]=-2f\). On the adjoint module, complete reducibility gives \(sl_2\) summands of highest weights \(2m_i\): all \(h\)-weights are even root heights. Each summand has one weight-zero line, and \(\mathfrak r_0=\mathfrak t\). There are therefore \(r\) summands, allowing \(m_i=0\) on the centre. Since \(\dim\mathfrak r=2N+r\),
\[
 \sum_i m_i=N.
\tag{B.2.4}
\]
The lowest lines form \(\mathfrak r^f\), with slice weights \(2(m_i+1)>0\).

We check an invertible differential at \(x_*=e+f\). The principal triple acts through an actual \(SL_2\) homomorphism into \(R\): in a faithful module its rank-one representation integrates by the polynomial highest-weight formulas, Theorem 2.1 and Proposition 2.2, and the two root-group images are the polynomial exponentials of \(e\) and \(f\), contained in the original positive and negative unipotent groups. These root groups generate \(SL_2\). Its determinant-one matrix \(\left(\begin{smallmatrix}1&-1/2\\1&1/2\end{smallmatrix}\right)\) conjugates the diagonal generator to \(e+f\). Hence \(x_*\) is conjugate to \(h\) and is regular semisimple.

The kernel of \(d\chi\) at a regular semisimple point is its orbit tangent space. Indeed the differential of \(R\times\mathfrak t_{\rm reg}\to\mathfrak r\) is \([\mathfrak r,x]+\mathfrak t=\mathfrak r\), and the finite Weyl quotient is étale off its reflecting hyperplanes. Here are the required checks. If \(w\) fixes a regular vector over any characteristic-zero field, its rational fixed subspace has no root identically zero, since that vector witnesses this. A rational real point of that subspace can therefore be chosen outside every root hyperplane. Its chamber stabilizer is trivial, so \(w=1\). Now prescribe any first jet at a regular geometric point \(x\), multiplied by \(|W|\), and prescribe zero first jets at all other orbit points. The squared maximal ideals of these distinct points are comaximal, so the Chinese remainder theorem gives a polynomial with these jets. Averaging it gives an invariant with the chosen differential at \(x\). Thus the quotient differential is surjective, and it is an isomorphism since both smooth spaces have dimension \(r\), by B.1. Maps between smooth schemes, Lemma 3.A proves étaleness. This establishes the quotient differential assertion used here.

The space \(\mathfrak r^f\) is transverse to that orbit at \(x_*\). Use the invariant form. The orthogonal complement of the orbit tangent is \(\mathfrak r^{x_*}\). In an \(sl_2\) summand \(\operatorname{Sym}^{2m}\), its weight-zero line after the rotation sending \(h\) to \(e+f\) has nonzero highest coefficient: rotating \(X^mY^m\) gives a nonzero multiple of \((Y^2-X^2)^m\). It therefore pairs nondegenerately with the lowest line. On each multiplicity space the invariant pairing is nondegenerate, and the same nonzero scalar multiplies it. This proves the transversality, including the central summands. Thus \(d(\chi|_\Sigma)\) is invertible at \(x_*\).

Choose the homogeneous generators from B.1 and Chevalley restriction. The restricted polynomial \(p_i|_\Sigma\) has slice weight \(2d_i\), because the quotient is invariant under conjugation and \(p_i\) has ordinary polynomial degree \(d_i\). Its Jacobian determinant has weight
\(2\sum_i d_i-2\sum_i(m_i+1)=0\), by (B.1.1) and (B.2.4). All slice variable weights are positive. Hence this determinant is a constant, nonzero by the preceding differential calculation.

At the slice origin \(e\) its linear part is an invertible graded map. Consequently the two multisets \(d_i\) and \(m_i+1\) agree. This gives a polynomial inverse without an unproved general assertion about constant Jacobians. Order the common positive weights. In a block of weight \(d\), the quotient coordinates are an invertible linear combination of the variables of weight \(d\), plus polynomials in variables of strictly smaller weights. A nonlinear monomial of total weight \(d\) can only contain such smaller weights. Solve these finite blocks in order. This constructs the inverse polynomial, also on nonreduced parameter algebras.

Finally every element has centralizer dimension at least \(r\): regular semisimple elements form a dense open, and the corresponding rank bound on \(\operatorname{ad}x\) is the vanishing of polynomial minors. Choose an \(h\)-homogeneous complement to \(\ker\operatorname{ad}e\). For \(x=e+v\in\Sigma\), the highest nonzero \(h\)-weight of a vector in that complement has nonzero image under \(\operatorname{ad}e\), with weight two higher. All \([v,-]\) terms have at most its original weight. They cannot cancel that term. Thus \(\operatorname{ad}x\) has rank at least \(\dim\mathfrak r-r\), and the opposite inequality just proved makes it equal. The regular minor is invertible locally on the whole slice, so the centralizer Lie kernel is a vector bundle there. ∎

### B.3. Regular fibres and the full centralizer scheme

**Lemma B.3.1.1.** Every nilpotent element of a reductive Lie algebra in characteristic zero belongs to the nilpotent radical of a Borel. The nilpotent locus is irreducible of dimension \(\dim\mathfrak r-r\), and its regular elements form one orbit.

**Proof.** Jordan decomposition and its preservation in faithful modules for the semisimple summand are proved in The Killing form and Cartan's criteria, Theorem 6.2 and Complete reducibility, Theorem 5.1. The central torus acts diagonally in an algebraic module; its component is semisimple and commutes with those Jordan parts. This gives the stated reductive version. For a nilpotent \(n\), its finite polynomial exponential is an actual additive subgroup of \(R\). One can check containment schematically: the right-invariant derivation associated with \(n\) preserves the Hopf ideal of the closed group \(R\); every Taylor coefficient of a defining equation on \(\exp(tn)\) is therefore zero. The exponential is polynomial because the represented \(n\) is nilpotent.

This additive group has a fixed point on the projective flag variety \(R/B\), constructed in The flag scheme and the Weyl group, Theorem 1.1. Here is the needed fixed-point argument. A nonconstant additive orbit map from \(\mathbf A^1\) into a projective variety is represented by polynomial homogeneous coordinates after trivializing its pulled-back line on \(E[t]\). Homogenizing to their largest degree extends it to \(\mathbf P^1\), with a defined value at infinity. Translation equivariance holds on the dense affine line and therefore on the entire projective line by separatedness. Infinity is fixed by every translation, so its image is fixed. A constant orbit already provides a fixed point. Thus \(n\) lies in a conjugate Borel Lie algebra. In a faithful weight-triangular module its torus part would give diagonal eigenvalues. Nilpotence makes all of them zero, and the faithful torus weights span its Lie dual. Hence that part is zero.

It follows that the proper incidence map \(R\times^B\mathfrak n\to\mathfrak r\) covers the nilpotent locus. Its source is an irreducible vector bundle of dimension \(2N=\dim\mathfrak r-r\), so its image is irreducible and has dimension at most that number. Supporting field geometry, Theorem G.3.4 and Theorem G.4.2 proves smoothness of each characteristic-zero finite-type stabilizer and local closedness of its orbits. The principal \(e\) therefore has group centralizer dimension \(r\), by the \(sl_2\) Lie calculation of B.2, so its orbit has exactly that dimension. The bound is an equality. Any regular nilpotent orbit has the same dimension and is open in the irreducible nilpotent locus, so must be the same orbit. For the openness assertion, a constructible orbit contains a nonempty open of its closure; translating that open covers the orbit and makes the whole orbit open in its closure. Two distinct full-dimensional orbits would give disjoint nonempty opens of the same irreducible variety. ∎

**Theorem B.3.1.2.** Each regular quotient fibre has exactly one geometric orbit. The map
\[
 p:R\times\Sigma\longrightarrow\mathfrak r_{\rm reg},
           \qquad(g,\sigma)\longmapsto\operatorname{Ad}_g\sigma
\tag{B.3.1}
\]
is smooth surjective. The closed group scheme
\[
 J=\{(\sigma,g)\in\Sigma\times R:
                              \operatorname{Ad}_g\sigma=\sigma\}
\tag{B.3.2}
\]
is smooth over \(\Sigma\), has relative dimension \(r\), and is commutative. Its fibres need not be connected. It includes the full original \(Z(R)\).

**Proof.** Write a geometric element \(x=s+n\) in Jordan form, with commuting semisimple and nilpotent parts. The semisimple part lies in a torus. This can also be seen directly in a faithful module: in a diagonal basis the formal exponential of \(s\) has character exponents. Distinct exponential series are linearly independent by their derivative Vandermonde matrix. Its algebraic closure is therefore the torus defined by the integral character relations whose derivative on \(s\) is zero; the same Hopf-ideal Taylor argument places that torus in \(R\). Maximal-torus conjugacy is proved in Tori, maximal tori and their conjugacy.

Let \(D\) be the torus just obtained. Its character relation lattice is exactly the integral characters whose derivative at \(s\) is zero; this lattice is saturated, since the characteristic is zero. In a faithful diagonal module two weights restrict to the same character of \(D\) exactly when their eigenvalues on \(s\) agree. Commuting with \(s\) means preserving precisely these equal-eigenvalue blocks, while commuting with the universal \(D\)-action means preserving exactly its character blocks. The two matrix conditions are therefore identical over every parameter algebra. Intersecting with the original closed group gives the scheme equality \(C_R(s)=C_R(D)\). Centralizers of subtori, Theorem 2.2 proves that this is a smooth connected reductive group. Choose an integral cocharacter of \(D\) outside the finitely many hyperplanes for roots nontrivial on \(D\); an integral point exists because its cocharacter lattice spans the rational vector space. Its zero roots are exactly those with \(\alpha(s)=0\). Weyl conjugation makes this cocharacter dominant. The positive/negative cocharacter limits and the Levi construction of The flag scheme and the Weyl group, §1 identify the centralizer as the corresponding root Levi \(L\). In particular its rank is the original \(r\), and its roots are precisely \(\alpha(s)=0\). This proves the full centralizer assertion without dropping any component or infinitesimal equation.

The centralizer of \(x\) is \(C_L(n)\), since a commuting operator preserves the polynomial Jordan parts. Thus \(x\) is regular exactly when \(n\) is regular in that Levi. B.3.1.1 applies to the Levi. Invariant polynomials have the same values on \(s+n\) and \(s\): put \(n\) in a Levi Borel radical and contract it to zero with its positive coroot cocharacter, fixing \(s\). Chevalley restriction and finite-orbit separation for \(W\) determine the semisimple conjugacy class from these values. The single regular nilpotent orbit of its Levi determines the remaining regular orbit. This proves uniqueness of a regular orbit in a quotient fibre.

B.2 gives a slice point for every quotient value, and every slice point is regular. The map (B.3.1) is consequently geometrically surjective. At a slice point, \(d\chi|_{\mathfrak r^f}\) is an isomorphism, so \(d\chi\) has rank \(r\). Invariance places the orbit tangent in its kernel; both have dimension \(\dim\mathfrak r-r\), so they are equal. Conjugation gives the same equality at every regular point. The orbit and slice tangents therefore make the differential of (B.3.1) surjective everywhere. The differential criterion of Lemma 3.A cited in B.2 gives actual smooth surjectivity, of relative dimension \(r\).

Base changing this map along the slice gives \(J\). This is the full scheme centralizer, because equality of two quotient values forces their slice coordinates to be equal by the polynomial inverse of B.2, even over nonreduced rings. More explicitly the actual descent relation is
\[
 (R\times\Sigma)\times_{\mathfrak r_{\rm reg}}(R\times\Sigma)
       \simeq R\times J,
\tag{B.3.3}
\]
with right multiplication by the centralizer on the first factor. Thus \(J\) is smooth over \(\Sigma\). Its generic fibre is a torus. The two multiplication maps on \(J\times_\Sigma J\) agree there and hence everywhere: its affine coordinate algebra is flat over the integral slice, so is torsion free and injects into its generic localization. Every coordinate difference therefore vanishes already on the whole source. This proves commutativity as a scheme identity. Central elements satisfy (B.3.2). No special fibre has been replaced by its identity component. ∎

### B.4. The extension across the missing locus

**Proposition B.4.1.1.** The nonregular complement in \(\mathfrak r\) has codimension at least two. Restriction of polynomial functions to the regular locus is an isomorphism, and the same is true for maps between free bundles.

**Proof.** Use the finitely many root Levi types for semisimple centralizers. If a type \(L\) has semisimple rank \(s\), its semisimple centralizer parameters have dimension \(r-s\). Its nilpotent locus has dimension \(\dim L-r\), by B.3.1.1. The corresponding Jordan stratum is covered by
\(R\times^L(Z(\mathfrak l)_{\rm reg}\times\mathcal N_L)\),
of dimension at most \(\dim R-s\). If \(s\ge2\), this already gives codimension at least two. If \(s=0\), all elements are regular. If \(s=1\), its derived Lie algebra is \(sl_2\), whose nonzero nilpotents have centralizer dimension one and whose only nonregular nilpotent is zero. The bad stratum in this case has dimension at most
\(\dim R-(r+2)+(r-1)=\dim R-3\).
The finite union of these bounds proves the assertion. This dimension argument concerns geometric Jordan strata; the regular scheme and its centralizers are the full smooth schemes of B.3.

Let a regular function on this open locus be \(u/v\) in reduced form in the polynomial fraction field. If an irreducible factor divided \(v\), its height-one generic point would be in the regular locus, since the missing set has codimension at least two. Regularity there would force cancellation of that factor, a contradiction. Thus \(v\) is a unit and the function is polynomial. Uniqueness follows from density. Apply this coefficientwise to maps between finite free bundles. ∎

### B.5. Exact Kostant restriction and full free-module morphisms

Let \(p_1,\ldots,p_r\) be the chosen invariants. Their differentials on the coadjoint space give sections \(\zeta_i\) of the stabilizer Lie bundle. Equivalently they are gradients under the invariant form. The differentials have rank \(r\) on the slice, and invariance makes their values commute with the slice element. Hence they form the entire \(\operatorname{Lie}J\) bundle. B.3 makes this an abelian bundle. Put
\[
 \mathcal B=\operatorname{Sym}_{E[\Sigma]}(\operatorname{Lie}J)
       =E[p_1,\ldots,p_r,z_1,\ldots,z_r],
 \qquad |p_i|=2d_i,\quad |z_i|=2d_i-2.
\tag{B.5.1}
\]
The tangent-bundle underlying algebra is thus supplied with the displayed deformation grading. In the Hom notation below the superscript records the degree of a homogeneous module map between these coherent graded objects.

**Theorem B.5.1.1.** For an \(R\)-equivariant coherent sheaf \(F\) on \(\mathfrak r^*\), restriction to \(\Sigma\), with the stabilizer Lie action, gives an exact functor \(\kappa(F)\) to coherent \(\mathcal B\)-modules. On the free generators \(A\otimes V\) it gives
\[
 M(V)=E[\Sigma]\otimes V,\qquad
 z_i\cdot v=\rho_V(\zeta_i)v.
\tag{B.5.2}
\]
It is fully faithful on these generators, including all homogeneous morphism degrees:
\[
 \operatorname{Hom}^*_{A,R}(A\otimes V,A\otimes W)
       \xrightarrow{\sim}
 \operatorname{Hom}^*_{\mathcal B}(M(V),M(W)).
\tag{B.5.3}
\]
The comparison preserves actual composition and the prescribed full group.

**Proof.** Pullback to \(R\times\Sigma\) along the smooth surjection \(p\) is exact. Equivariance identifies it with the pullback of \(F|_\Sigma\) along the faithfully flat projection to the slice. Consequently restriction to the slice is exact on equivariant coherent sheaves, even though an arbitrary closed restriction is not flat. The residual action of \(J\) gives its Lie action, hence the module over its symmetric algebra. It is coherent: it is already finite over the Noetherian base \(E[\Sigma]\). This proves exactness and (B.5.2).

A \(\mathcal B\)-linear map between the displayed modules is a polynomial family \(\phi_\Sigma\) commuting with \(\operatorname{Lie}J\). On the geometric generic fibre \(J\) is a torus. Commuting with its Lie action implies commuting with its full torus action: rational torus modules split into actual characters, and distinct characters have distinct derivatives in characteristic zero. This retains characters differing on finite centres as well.

It follows that \(\phi_\Sigma\) commutes with the full \(J\) everywhere. The required coordinate equalities hold on the generic fibre of the smooth flat group scheme \(J\); its torsion-free coordinate algebra makes them hold as scheme equations on the whole \(J\). Define the family on \(R\times\Sigma\) by
\(\rho_W(g)\phi_\Sigma(\sigma)\rho_V(g)^{-1}\).
Full \(J\)-equivariance makes it compatible with the actual relation (B.3.3). Faithfully flat descent gives an \(R\)-equivariant free-bundle map on \(\mathfrak r_{\rm reg}\). B.4 extends its coefficients uniquely to polynomials on all of \(\mathfrak r\). Equivariance extends too, because its two matrix formulas agree on the dense \(R\times\mathfrak r_{\rm reg}\). Restriction reverses this procedure, proving (B.5.3). All steps are functorial matrix equalities, so preserve composition.

For the grading, give a vector in \(V\) its principal \(h\)-weight, in addition to any specified external grading. The gradient identity under (B.2.3) is
\[
 \zeta_i(t\cdot\sigma)
   =t^{\,2(d_i-1)}\operatorname{Ad}_{h(t^{-1})}\zeta_i(\sigma).
\tag{B.5.4}
\]
Its root component of \(h\)-weight \(b\) has coefficient degree \(2(d_i-1)-b\), while its action raises a vector's principal degree by \(b\). Thus its total operator degree is exactly \(2d_i-2\), as in (B.5.1). An equivariant homogeneous polynomial map of degree \(k\) similarly satisfies
\(\phi(t\cdot\sigma)=t^k\rho_W(h(t^{-1}))\phi(\sigma)\rho_V(h(t))\).
The coefficient and principal-degree changes cancel to give degree \(k\). Conversely decompose the unique polynomial extension into its finitely many homogeneous parts. Their restriction preserves these degrees; faithfulness forces every part of a different degree to be zero. This proves the graded comparison, not just the ungraded Hom equality.

There is also the coefficient tensor comparison
\[
 M(V)\otimes_{E[\Sigma]}M(W)\simeq M(V\otimes W),
\tag{B.5.5}
\]
where \(z_i\) acts primitively as \(z_i\otimes1+1\otimes z_i\). This follows directly from the differential of the representation tensor product. Its associativity and unit are those of that tensor product. A derived convolution or symmetry comparison requires its own enhancement and the conventions of Lesson 8; (B.5.5) is the stated coefficient-level comparison. ∎

![The actual polynomial Kostant slice gives smooth full-centralizer descent and unique polynomial extension of all free-generator morphisms](assets/kostant-slice-descent.png)

Lemmas and Theorems B.1.1.1–B.5.1.1 prove the slice inverse, smooth maps, full scheme relation, codimension bound, grading and composition shown. The invariant-ring argument and positive-weight inverse provide actual polynomial maps over every parameter algebra. Editable SVG source.

### B.6. Rank one: full operators, morphisms and centre

**Proposition B.6.1.1.** For \(R=SL_2\) use the trace form \(B(X,Y)=\operatorname{tr}(XY)\), the invariant \(p(X)=\frac12\operatorname{tr}(X^2)\), and
\[
 X(c)=\begin{pmatrix}0&1\\c&0\end{pmatrix},\qquad
 E[\Sigma]=E[c],\qquad \mathcal B=E[c,z],\quad |c|=4,\ |z|=2.
\tag{B.6.1}
\]
The unit, standard and adjoint generators have respectively \(z\)-actions \(0,X(c),T=\operatorname{ad}X(c)\). For the adjoint basis \((e,h,f)\) of degrees \(2,0,-2\),
\[
 T=\begin{pmatrix}0&-2&0\\-c&0&1\\0&2c&0\end{pmatrix},
 \qquad T^3=4cT.
\tag{B.6.2}
\]
The two unit-adjoint Hom modules are freely generated over \(E[c]\) in degree two by
\[
 i=(1,0,c)^{\mathsf t},\qquad \ell=(c,0,1).
\tag{B.6.3}
\]
Their actual compositions are
\[
 \ell i=2c,\qquad i\ell=2cI-\tfrac12T^2,\qquad Ti=\ell T=0.
\tag{B.6.4}
\]
The adjoint endomorphism algebra is \(E[c,T]/(T^3-4cT)\), and the standard one is \(E[c,X]/(X^2-cI)\).

**Proof.** The chosen invariant's gradient under the trace form is \(X\), so these are exactly the operators in (B.5.2). Applying the brackets to \(e,h,f\) gives the three columns of (B.6.2); multiplying gives its relation. The vector \(f\) is cyclic over \(E[c]\): the columns \(f,Tf,T^2f\) have determinant \(2\). Thus a commuting endomorphism is uniquely a polynomial of degree at most two in \(T\), determined by its value on that cyclic vector. There are no denominators or extra endomorphisms at \(c=0\). For the standard module the vector \(v_-\) is cyclic with columns \(v_-,Xv_-\) of determinant \(-1\), proving its endomorphism algebra.

Solving \(Ti=0\) and \(\ell T=0\) gives (B.6.3) as the entire free Hom modules. Their grades follow from the displayed basis degrees and \(|c|=4\). Direct multiplication gives (B.6.4), with the stated trace normalization. These are the full compositions supplied by B.5, not their dimensions.

The full universal centralizer is
\[
 J=\operatorname{Spec}E[c,u,v]/(u^2-cv^2-1),
 \qquad g=\begin{pmatrix}u&v\\cv&u\end{pmatrix}.
\tag{B.6.5}
\]
Every commuting matrix has this form, by the same cyclic-vector calculation, and the equation is its actual determinant-one condition. At \(c=0\) it is \(\mu_2\times\mathbf G_a\), with additive coordinate \(v/u\). This fibre has two components and retains the original centre.

Globally there is no nonzero map from the unit to the standard Kostant module: \(X(c)\) has zero kernel over the domain \(E[c]\). At \(c=0\) its Lie-action kernel is one dimensional, but the central element \(-I\) acts on that line by \(-1\), so there is still no map from the unit commuting with the full centralizer group. Fibrewise Lie commutation alone would lose precisely this condition; the generic-to-flat-group argument in B.5 does not. The unit–adjoint block descends to \(PGL_2\); the standard generator in this example belongs to the stated \(SL_2\). ∎

![The SL2 Kostant generators have explicit composition constants and retain the full finite centre on the nilpotent fibre](assets/sl2-kostant-compositions.png)

Proposition B.6.1.1 and Exercises B.7.2–B.7.3 compute the exact operators, cyclic bases, products, scheme equations and nilpotent coefficients. The full centralizer condition distinguishes fibrewise Lie commutation from the global morphism theorem. Editable SVG source.

### B.7. Exercises

**Exercise B.7.1 (medium).** Verify the positive-weight inverse argument on \(F(u,v)=(u,v+u^2)\), with weights \(2,4\). Evaluate it on \(E[\epsilon]/(\epsilon^3)\), with \(u=\epsilon,v=\epsilon^2\), retaining every coefficient.

**Solution.** The two target coordinates have weights \(2,4\); its linear blocks are both the identity and its only nonlinear term uses the smaller weight. The inverse is \((u,w)\mapsto(u,w-u^2)\). At the specified parameter \(F(\epsilon,\epsilon^2)=(\epsilon,2\epsilon^2)\), and the inverse recovers \(\epsilon^2\). Passing to its point would erase that quadratic coefficient. The argument uses the positive-weight triangular blocks proved in B.2, not a general claim that any constant-Jacobian polynomial map is invertible.

**Exercise B.7.2 (advanced).** For \(SL_3\), take \(e=E_{12}+E_{23}\), \(f=2(E_{21}+E_{32})\), and slice \(X=e+uf+vf^2\). Compute its quotient coordinates, the centralizer Lie basis, and the full centre of the nilpotent group fibre.

**Solution.** The matrix is
\[
 X=\begin{pmatrix}0&1&0\\2u&0&1\\4v&2u&0\end{pmatrix}.
\tag{B.7.1}
\]
Multiplication gives \(\frac12\operatorname{tr}X^2=4u\) and \(\frac13\operatorname{tr}X^3=\det X=4v\). Its quotient inverse is \(u=p_2/4,v=p_3/4\), with degrees four and six. The columns \(e_3,Xe_3,X^2e_3\) have determinant \(-1\), on every parameter algebra. Hence every commuting matrix is \(aI+bX+dX^2\). Its trace-zero part has basis \(X\) and \(X^2-\frac{8u}{3}I\), of operator degrees two and four, respectively. These are the gradients of the two chosen invariants under the trace form.

At \(u=v=0\), \(X^3=0\) and \(\det(aI+bX+dX^2)=a^3\). The group equation is therefore \(a^3=1\). Its centre factor is the whole \(\mu_3\); after dividing by \(a\), logarithm coordinates \(b/a\) and \(d/a-b^2/(2a^2)\) give the two additive factors. Thus the full regular nilpotent centralizer is \(\mu_3\times\mathbf G_a^2\), with three geometric components in characteristic zero. B.3 never assumed this fibre connected.

**Exercise B.7.3 (advanced).** At \(c=\epsilon\in E[\epsilon]/(\epsilon^2)\), verify that
\[
 \begin{pmatrix}1+\epsilon/2&1\\
                 \epsilon&1+\epsilon/2\end{pmatrix}
\tag{B.7.2}
\]
is an actual \(SL_2\) centralizer point. Explain the difference between the nilpotent fibre's Lie-action Hom and the global free-module Hom.

**Solution.** It has the form (B.6.5) with \(u=1+\epsilon/2,v=1\), and \(u^2-\epsilon v^2=1\) exactly. Multiplying with \(X(\epsilon)\) on either side gives the same matrix; its infinitesimal coefficient is retained by the scheme equation. At \(c=0\), the standard module has a nonzero vector killed by \(z=X(0)\), so its Lie-action Hom from the unit has dimension one. Its \(-I\) action makes the full group Hom zero. Over \(E[c]\) the determinant of \(X(c)\) is the nonzero polynomial \(-c\), so its kernel and the global free-module Hom are zero. Formation of that kernel does not commute with this specialization. There is no contradiction with the global fully faithful restriction theorem.

These proofs construct the full algebraic polynomial generators and their faithful restriction, with their precise grading and composition. Identifying these restriction modules with geometric equivariant cohomology, and proving geometric full faithfulness and enhanced convolution compatibility, remain the next steps toward the derived equivalence.

## Appendix C. Contracting loop charts and an integral cohomology criterion

We construct opposite-loop open charts over every parameter algebra, prove their actual contraction comparison, and give a cell criterion for equivariant Ext to equal graded module Hom. The criterion requires surjectivity to the fixed-point stalks. Section C.9 proves a sufficient weight implication with its compact-support estimate stated explicitly as a hypothesis.

The earlier geometric proofs are Lesson 1, Theorem 2.C and Lemma 2.0, Lesson 2, Lemma 2.1, Theorem 3.1 and Lemma 7.2, Lesson 6, Lemmas A.1.1.1–A.1.2.1, and Lesson 5, §§O–P and Q.1. These provide the root coordinates, lattice families, affine homogeneous-quotient hull, global supported Kummer class, trace and affine-line propagation used below. Free reading is [Ginzburg, *Pointwise purity, derived Satake, and Symplectic duality*, arXiv:2508.15958v2](https://arxiv.org/abs/2508.15958v2), §§4.1–4.2. The proofs here specify the actual integral maps.

### C.1. Orthogonal supports give integral Hom vanishing

Let \(S=E[u_1,\ldots,u_r]\), \(Q=\operatorname{Frac}(S)\), and let \(A\) be a commutative \(S\)-algebra. Suppose

\[
 Q\otimes_S A=\prod_{x\in\Xi}Q
\]

for a finite set \(\Xi\). Write \(e_x\) for its orthogonal idempotents. Let \(M,N\) be finite \(A\)-modules. Assume their localizations have disjoint idempotent supports and that \(N\) is \(S\)-torsion free.

**Lemma C.1.1.1.** Then \(\operatorname{Hom}_A(M,N)=0\).

**Proof.** Let \(e\) be the sum of the idempotents supporting \(QM\), so \(e\) acts as the identity there and as zero on \(QN\). For an \(A\)-linear map \(f\), its localization is \(QA\)-linear. For every \(m\in QM\),

\[
 Qf(m)=Qf(em)=eQf(m)=0.
\]

For each \(m\in M\), this says that \(f(m)\) is killed by a nonzero element of \(S\). Torsion freeness of \(N\) makes \(f(m)=0\). Thus \(f=0\). No denominator has been used to construct a global map, and no surjectivity is inferred from localization. The same proof applies in every homogeneous map degree. ∎

This is the exact role of fixed-point localization in the geometric criterion: disjoint supports kill cross terms integrally because their targets are free over \(H_T^*(\mathrm{pt})\). The proof does not say that an arbitrary rational morphism extends.

### C.2. Two module filtrations give the required left-exact Hom row

Keep \(S,A,Q\). Let \(P,F\) be \(A\)-modules, together with exact sequences

\[
 0\longrightarrow P_c\xrightarrow{a}P\xrightarrow{b}P_Z\longrightarrow0,
 \qquad
 0\longrightarrow P_!\xrightarrow{c}P\xrightarrow{d}P_U\longrightarrow0,
\]

\[
 0\longrightarrow F_Z\xrightarrow{i}F\xrightarrow{j}F_U\longrightarrow0.
\]

Assume \(P_c,P_U,F_U\) have localized support on a subset \(\Xi_U\), whereas \(P_!,P_Z,F_Z\) have support in its complement. Assume \(F_Z\) and \(F_U\) are \(S\)-torsion free. In geometry these are the compact open, ordinary open and closed restriction sequences; their exactness is a separate geometric assertion.

**Lemma C.2.1.1.** Every \(g:P\to F\) induces a unique \(A\)-linear map

\[
 \beta(g):P_U\longrightarrow F_U,
 \qquad \beta(g)d=jg.
\]

Moreover the sequence

\[
 0\longrightarrow\operatorname{Hom}_A(P_Z,F_Z)
 \xrightarrow{\alpha}\operatorname{Hom}_A(P,F)
 \xrightarrow{\beta}\operatorname{Hom}_A(P_U,F_U)
\]

is exact, where \(\alpha(f)=ifb\). Surjectivity of \(\beta\) is not an assumption or a conclusion of this lemma.

**Proof.** Lemma C.1.1.1 gives

\[
 \operatorname{Hom}_A(P_!,F_U)=
 \operatorname{Hom}_A(P_c,F_Z)=
 \operatorname{Hom}_A(P_Z,F_U)=0.
\]

The first equality makes \(jgc=0\), so the quotient universal property for \(d\) gives the unique map \(\beta(g)\). Since \(b\) is surjective and \(i\) is injective, \(\alpha\) is injective. For \(f:P_Z\to F_Z\), the composite \(ji=0\) makes \(\beta\alpha(f)=0\).

Conversely suppose \(\beta(g)=0\). Then \(jg=0\), so \(g=i\widetilde g\) for a unique map \(\widetilde g:P\to F_Z\). The second displayed Hom vanishing gives \(\widetilde ga=0\). Hence \(\widetilde g=fb\) for a unique \(f:P_Z\to F_Z\), and \(g=\alpha(f)\). This proves exactness without applying an unjustified exactness assertion to a Hom functor. ∎

### C.3. A surjective upper comparison supplies all lower lifts

Consider a commutative diagram whose top row is short exact and whose bottom row is the row of C.2:

\[
\begin{array}{ccccccccc}
0&\to&E_Z&\xrightarrow{s}&E&\xrightarrow{t}&E_U&\to&0\\
 &&\downarrow h_Z&&\downarrow h&&\downarrow h_U\\
0&\to&H_Z&\xrightarrow{\alpha}&H&\xrightarrow{\beta}&H_U.
\end{array}
\]

**Lemma C.3.1.1.** If \(h_Z\) and \(h_U\) are isomorphisms, then \(h\) is an isomorphism and \(\beta\) is surjective.

**Proof.** To prove injectivity, let \(h(e)=0\). Commutativity and injectivity of \(h_U\) give \(t(e)=0\), so \(e=s(z)\). Then \(0=\alpha h_Z(z)\). Injectivity of \(\alpha\) and \(h_Z\) gives \(z=0\), hence \(e=0\).

For surjectivity, choose \(g\in H\). Lift \(\beta(g)\) through the isomorphism \(h_U\) to \(u\in E_U\), and through the surjection \(t\) to \(e\in E\). Then

\[
 \beta(g-h(e))=0.
\]

Exactness of the lower row gives \(g-h(e)=\alpha(z')\). Lift \(z'\) through \(h_Z\), giving \(z\). Commutativity now gives

\[
 g=h(e+s(z)).
\]

Thus \(h\) is surjective. For any \(v\in H_U\), lift it through \(h_U\) and \(t\) as above; commutativity gives \(v=\beta(h(e))\), proving surjectivity of \(\beta\). ∎

This is the complete induction chase needed for the actual cohomology map. Its top row must come from the actual geometric restriction triangle. Weights may force its connecting maps to vanish, but weight purity alone does not prove the separate module-filtration surjectivity used in C.2.

### C.4. A complete two-fixed-point example

Let

\[
 S=E[u],\quad |u|=2,\qquad
 A=S[h]/(h(h-u)),\quad |h|=2.
\]

It is free over \(S\) with basis \(1,h\). Over \(Q\) its two characters are \(h=0\) and \(h=u\), with idempotents

\[
 e_0=1-h/u,\qquad e_\infty=h/u.
\]

They satisfy \(e_0^2=e_0\), \(e_\infty^2=e_\infty\), \(e_0e_\infty=0\) and sum to one, directly from \(h^2=uh\). For the rank-one modules \(S_0,S_\infty\) carrying these respective characters,

\[
 \operatorname{Hom}_A(S_0,S_\infty)=0=
 \operatorname{Hom}_A(S_\infty,S_0).
\]

Indeed a map is multiplication by \(a\in S\), and commutation with \(h\) requires \(ua=0\). The polynomial domain makes \(a=0\).

At \(u=0\), both specialized modules are \(E\) with trivial \(h\)-action over \(E[h]/h^2\), so their specialized-module Hom is \(E\). The specialization of the global Hom remains zero. This computes the failure of Hom to commute with this base change. It explains why one cannot forget the equivariant parameter and infer the desired geometric full faithfulness from specialized module dimensions.

### C.5. Euler classes and cellular fixed-point localization

Let \(k\) be algebraically closed, let \(\ell\) be invertible in \(k\), and let \(E/\mathbf Q_\ell\) be finite. Let \(T\) be a split torus with character basis \(\chi_1,\ldots,\chi_r\). Put

\[
 S=H_T^*(\operatorname{Spec}k,E)=E[u_1,\ldots,u_r],
 \qquad |u_i|=2,\qquad Q=\operatorname{Frac}(S).
 \tag{C.5.1}
\]

The notation for the polynomial variables suppresses their coefficient lines, rather than changing the maps: \(c_1(\chi_i)\) lies in \(H_T^2(\mathrm{pt},E(1))\). A degree-\(2d\) Euler action therefore has its actual domain \(M(-d)[-2d]\). Every restriction and cup product below retains that line.

Here is the finite model of (C.5.1). Choose the right action on
\(P_m=(\mathbf A^{m+1}\setminus0)^r\) so that the associated \(\chi_i\)-line over \(B_m=(\mathbf P^m)^r\) is \(\mathcal O(1)\) on its \(i\)-th factor. The closed affine paving and affine trace give projective-space cohomology in even degrees only. The \(a\)-fold hyperplane intersection has positive trace \(1\) on \(\mathbf P^a\); hence the powers of its Kummer class give its basis. Products of those intersections give

\[
 H^*(B_m,E)=E[u_1,\ldots,u_r]/(u_1^{m+1},\ldots,u_r^{m+1}).
 \tag{C.5.2}
\]

Equivalently this follows by applying the same affine-cell induction to the product, with its coordinate hyperplane classes. Its monomials are paired with the complementary coordinate linear subvarieties; their intersection matrix is the identity. The trace and section orientations are the actual comparisons proved in Lesson 6, A.1.1.1–A.1.2.1, and Lesson 5, O–P. The restriction of (C.5.2) stabilizes in each fixed degree. This proves (C.5.1). For \(\alpha=\sum a_i\chi_i\), additivity of the Kummer connecting homomorphism on line-bundle transition units gives
\(c_1(\alpha)=\sum a_i u_i\).

**Lemma C.5.1.1.** If \(V=\bigoplus_{j=1}^d k_{\alpha_j}\) is a \(T\)-representation with every \(\alpha_j\ne0\) and \(d>0\), then the nonzero polynomial

\[
 e_T(V)=\prod_{j=1}^d\alpha_j\in S
 \tag{C.5.3}
\]

annihilates \(H_T^*(V\setminus0,K)\) and \(H_{T,c}^*(V\setminus0,K)\) for every actual equivariant bounded constructible \(K\) there.

**Proof.** Over \(B_m\), the associated vector bundle is the sum of the character lines \(L_{\alpha_j}\). On its total space the \(j\)-th coordinate zero divisor has its global supported Kummer class. Lesson 6, Lemma A.1.2.1, proves that forgetting support gives \(c_1(L_{\alpha_j})\), with the section trace and all transition units fixed.

Take the cup product of these supported classes. Cup product with supports lands in the intersection of their supports: this is the tensor product of the localization counits, followed by multiplication of the constant coefficient objects. Their common support is the zero section. Forgetting support gives the product of the pulled-back line classes. Restriction to the complement of the zero section is consequently zero. Thus \(e_T(V)=0\) in the equivariant constant-coefficient cohomology of \(V\setminus0\).

The action of a constant-coefficient cohomology class on \(K\) is its representing map tensored with \(1_K\), followed by the unit evaluation. A zero class therefore acts by zero on both ordinary and compact images; projection formula makes this the \(S\)-action just specified. This argument applies at every finite \(B_m\) and hence in each stable degree. Finally each \(\alpha_j=\sum a_{ij}u_i\) is a nonzero linear polynomial: its integral character is nonzero and \(E\) has characteristic zero. The polynomial domain makes their product nonzero. No weight bound or stalk-surjectivity assertion has been used. ∎

Let \(X\) be a proper finite-type \(T\)-scheme with a finite closed filtration whose successive strata are \(T\)-equivariantly isomorphic to such representations \(V_\lambda\); zero-dimensional strata are allowed. Let \(P\subset X\) be the reduced closed union of the origins of those cells, and suppose these are all its geometric fixed points. We use the actual closed point immersion \(i:P\to X\), without replacing a possibly larger nonreduced fixed-point scheme by a statement about its moduli functor.

**Theorem C.5.2.1.** For every actual equivariant bounded constructible \(F\), restriction induces

\[
 QH_T^*(X,F)\xrightarrow{\sim}
 \bigoplus_{x\in P}QH_T^*(x,i_x^*F).
 \tag{C.5.4}
\]

For the constant object this is an algebra isomorphism
\(QH_T^*(X,E)=\prod_{x\in P}Q\). It is the localization map that gives the idempotents in Lemma C.1.1.1.

**Proof.** Remove \(P\) from each term of the closed filtration. Its successive strata are the punctured \(V_\lambda\), with an empty stratum when \(V_\lambda=0\). Lemma C.5.1.1 kills the localized equivariant compact cohomology of each stratum. The closed–open compact-support triangles and exactness of \(Q\otimes_S-\) therefore kill that of \(X\setminus P\), by finite induction.

Apply equivariant cohomology to
\[
 j_!j^*F\longrightarrow F\longrightarrow i_*i^*F
 \longrightarrow .
 \tag{C.5.5}
\]
At each classifying approximation the base \(B_m\) is proper, and properness of \(X\) identifies the first image with the relative compact image of its open complement. Its localization is zero by the preceding induction. The second arrow thus gives (C.5.4). The finite support \(P\) is a disjoint union of points, so its image is the displayed direct sum. For the constant object, restriction preserves units and cup products, and each point has the ring \(S\); this proves the algebra assertion.

In particular a complex supported on one closed union of cells has localized module supported on the corresponding fixed points. Applying Lemma C.1.1.1 to modules with disjoint such supports and torsion-free targets gives integral Hom vanishing. The theorem supplies no assertion that rational maps lift to global maps. ∎

### C.6. An opposite-loop chart over every parameter algebra

Let \(O_R=R[[t]]\), \(F_R=R((t))\), and
\[
 L^{--}H(R)=
 \ker\bigl(H(R[t^{-1}])\xrightarrow{t^{-1}=0}H(R)\bigr).
 \tag{C.6.1}
\]
This includes negative coefficients in the nilradical of \(R\). We first work with \(H=GL_n\).

The bounded lattice scheme of Lesson 2, §2, represents lattices
\[
 t^NO_R^n\subset L\subset t^{-N}O_R^n
\]
whose finite quotient \(L/t^NO_R^n\) is a locally direct summand of
\(t^{-N}O_R^n/t^NO_R^n\). On its index-zero rank stratum that quotient has rank \(nN\). The nonnegative-power projection gives the map of finite vector bundles
\[
 \bar\pi_+:L/t^NO_R^n\longrightarrow
 O_R^n/t^NO_R^n.
 \tag{C.6.2}
\]
Let \(\Omega_N\) be its determinant-invertible open. On other rank strata use the empty open.

**Theorem C.6.1.1.** The opens \(\Omega_N\) are compatible under increasing \(N\). Their union \(\Omega\) is the image of the open immersion
\[
 L^{--}GL_n\longrightarrow\operatorname{Gr}_{GL_n},
 \qquad h\longmapsto hO^n.
 \tag{C.6.3}
\]
For every \(R\), a lattice in \(\Omega_N(R)\) has a unique representative
\[
 h=1+\sum_{j=1}^N h_jt^{-j},
 \qquad
 h^{-1}=1+\sum_{j=1}^N k_jt^{-j}.
 \tag{C.6.4}
\]

**Proof.** For \(L\in\Omega_N(R)\), the full projection
\(\pi_+:L\to O_R^n\) is an isomorphism of \(R\)-modules. Indeed an element in its kernel maps to zero under (C.6.2), hence belongs to \(t^NO_R^n\), where projection is the identity. For a prescribed power series \(f\), lift its class modulo \(t^N\) through (C.6.2), and correct the remaining positive tail by an element of \(t^NO_R^n\subset L\). This proves surjectivity.

Let \(l_i\) be the unique inverse images of the standard constant vectors. Their columns give a matrix \(h=1+\sum_{j=1}^N h_jt^{-j}\). All its columns belong to \(L\), so \(hO_R^n\subset L\).

We must prove invertibility over \(R[t^{-1}]\); a field-point factorization alone would not suffice. At every prime of \(R\), pass to its residue field \(\kappa\). The bounded lattice construction commutes with this passage, as does the inverse of (C.6.2). The matrix \(\bar h\) has determinant a polynomial in \(t^{-1}\) with constant coefficient \(1\), so it is invertible over \(\kappa((t))\). The inclusion \(\bar hO_\kappa^n\subset L_\kappa\), whose latter index is zero, gives
\[
 \operatorname{val}_t(\det\bar h)\ge0.
\]
This is the field lattice index calculation proved by elementary divisors in Lesson 1, Lemma 2.0: the difference is the nonnegative length of their quotient. On the other hand a polynomial in \(t^{-1}\) with constant coefficient \(1\) has valuation at most zero, and valuation zero precisely when all its other coefficients vanish. Therefore \(\det\bar h=1\).

Write \(\det h=1+b\), with \(b\) a negative polynomial. Every coefficient of \(b\) vanishes at every prime, hence is nilpotent. To see the last assertion directly, a nonnilpotent element would remain nonzero in its localization and a prime of that nonzero localization would avoid it. There are finitely many coefficients. If their nilpotence exponents are \(a_1,\ldots,a_s\), their ideal has zero power \(1+\sum(a_i-1)\), by the pigeonhole principle for its monomials. Thus \(b\) is nilpotent and
\[
 (1+b)^{-1}=1-b+b^2-\cdots
\]
is a finite negative polynomial. The adjugate formula now gives \(h^{-1}\in GL_n(R[t^{-1}])\), with value \(1\) at infinity.

For a finite negative matrix \(a\) define \(T_a(f)=\pi_+(af)\) on \(O_R^n\). Multiplication by another negative matrix keeps every discarded strictly negative term strictly negative. Consequently
\[
 T_aT_b=T_{ab}.
 \tag{C.6.5}
\]
In particular \(T_h^{-1}=T_{h^{-1}}\). Thus \(\pi_+:hO_R^n\to O_R^n\) is an isomorphism. Since it is also an isomorphism on \(L\), their inclusion is equality. Now \(t^NO_R^n\subset hO_R^n\) implies \(h^{-1}t^NO_R^n\subset O_R^n\); every entry of the negative polynomial \(h^{-1}\) has pole order at most \(N\). This proves (C.6.4).

Conversely a negative loop with its inverse bounded by \(N\) defines a bounded lattice. Formula (C.6.5) proves that its projection is an isomorphism, hence that (C.6.2) is an isomorphism. Its columns are recovered by the prescribed unique constant inverse images, proving uniqueness. The constructions commute with every ring map.

At a larger bound, (C.6.2) adds the same positive-power quotient to both sides, with identity as its induced map. The determinant-invertible conditions are therefore compatible. The finite negative matrices and their inverses in (C.6.4) are represented by affine schemes with their polynomial inverse equations. The preceding natural inverses identify them with \(\Omega_N\). Their union is exactly the ind-open \(\Omega\), which proves the asserted open immersion as a statement about the entire functor. ∎

For a connected reductive \(G/k\), choose the faithful closed embedding \(G\hookrightarrow H=GL(V)\) of Lesson 2, Lemma 7.2. That lemma proves that the actual fppf quotient \(H/G\) is an open subscheme of an affine finite-type scheme \(A\); it keeps the original \(G\), including its centre.

**Theorem C.6.2.1.** The natural map
\[
 L^{--}G\longrightarrow\operatorname{Gr}_G
 \tag{C.6.6}
\]
is an open immersion. Its image is the inverse image of \(\Omega\) under \(\operatorname{Gr}_G\to\operatorname{Gr}_H\).

**Proof.** On an fppf cover, a point of that inverse image is represented by \(g\in G(F_R)\). Theorem C.6.1.1 supplies the unique matrix factorization
\[
 g=hk,\qquad h\in L^{--}H(R),\quad k\in H(O_R).
 \tag{C.6.7}
\]
The equality \(g\in G(F_R)\) gives equality of right cosets \(kG=h^{-1}G\) in \((H/G)(F_R)\).

Compose their maps with the open immersion \(H/G\subset A\). A function of the affine hull evaluated on \(h^{-1}G\) lies in \(R[t^{-1}]\); evaluated on \(kG\) it lies in \(R[[t]]\). Their common value lies in
\[
 R[t^{-1}]\cap R[[t]]=R\quad\text{inside }R((t)),
 \tag{C.6.8}
\]
an equality of coefficient series for every ring, including nonreduced rings. Evaluation at \(t^{-1}=0\) is the identity coset because \(h^{-1}(\infty)=1\). Hence every affine-hull coordinate is the corresponding constant identity-coset coordinate. The immersion into \(A\) makes the entire quotient map that constant map. The fiber of the quotient torsor over the identity coset is precisely \(G\); therefore \(h^{-1}\in G(R[t^{-1}])\), and then \(k=h^{-1}g\in G(O_R)\). The latter can also be tested on the closed equations of \(G\), since \(O_R\to F_R\) is injective.

No passage from a formal section to a polynomial section has been asserted without proof: (C.6.8) proves it coordinate by coordinate in the fixed affine hull.

Two negative representatives of the same Grassmannian point differ by a positive loop. In the matrix embedding their ratio belongs to both \(H(R[t^{-1}])\) and \(H(R[[t]])\), so is constant, and its value at infinity is \(1\). They are equal. This uniqueness makes the local negative representatives descend: their finitely many matrix coefficients agree on overlaps, their inverse equations and the equations of \(G\) descend, and the pole bound can be taken on each bounded lattice stage. Thus (C.6.6) identifies the full negative-loop functor with the specified ind-open inverse image. ∎

### C.7. The exact contracting action on a Schubert support

For \(\lambda\in X_*(T)\), translate the preceding chart:
\[
 U_\lambda=t^\lambda L^{--}G\,K/K,\qquad K=L^+G.
 \tag{C.7.1}
\]
It is open and contains \(t^\lambda K\). Its negative coordinates carry the monoid action
\[
 a_s(t^\lambda h(t^{-1})K)
 =t^\lambda h(st^{-1})K,\qquad s\in\mathbf A^1.
 \tag{C.7.2}
\]

**Proposition C.7.1.1.** Formula (C.7.2) is an actual \(\mathbf A^1\)-action on \(U_\lambda\), commuting with \(T\), whose zero endomorphism is the constant map to \(t^\lambda K\). On \(s\ne0\) it agrees with
\[
 a_s(gK)=\lambda(s)\,g(s^{-1}t)K.
 \tag{C.7.3}
\]
It preserves \(U_\lambda\cap X\) for every closed finite union \(X\) of Iwahori cells stable under \(T\) and rotation, with its full scheme structure. In particular this holds for finite spherical Schubert supports.

**Proof.** In a bounded chart, both \(h\) and \(h^{-1}\) are polynomial matrices in \(t^{-1}\) with value \(1\) at infinity. Substitution \(t^{-1}\mapsto st^{-1}\) preserves the inverse equations, the equations of \(G\), and the pole bounds. Thus it defines a regular map over every parameter algebra. Double substitution is multiplication of the parameters and substitution at zero is the identity matrix. This proves the monoid laws and the stated zero map.

The left \(T\)-action in these coordinates is conjugation on \(h\), because \(T\) commutes with \(t^\lambda\) and its constant loops lie in \(K\). It commutes with substitution. Finally
\[
 \lambda(s)(s^{-1}t)^\lambda=t^\lambda
\]
for invertible \(s\), giving (C.7.3) exactly. There is no missing cocharacter or rotation sign.

An Iwahori is preserved by rotation and normalized by \(T\). Their actions therefore preserve each labelled cell and any closed union. To extend this assertion from invertible \(s\) to the whole monoid, test its closed defining equations on an affine chart of \(\mathbf A^1\times(U_\lambda\cap X)\). They vanish after inverting \(s\). Multiplication by \(s\) is injective on \(R[s]\) for every coordinate ring \(R\), so they vanish already before that localization. This proves preservation with nilpotents retained.

For the raw spherical IC, its dense spherical-orbit system is the constant rank-one system with its prescribed shift. The action (C.7.3) preserves that orbit and this system. Smooth normalized pullback and the no-boundary characterization of intermediate extension extend this isomorphism uniquely to the IC. Restriction to the identity parameter is the identity, and the two composites on \(\mathbb G_m^2\) agree because they agree on the dense orbit; uniqueness proves the unit and cocycle. These are the genuine heart action comparisons of Lesson 6, B.2.3.1, and preserve the coefficient and Tate lines. The same actual action is inherited by restriction to any stable closed cell union and then to its contracting chart. ∎

![The determinant-invertible lattice projection constructs an actual negative-loop chart and its contraction while retaining nilpotent parameters](assets/negative-loop-chart.png)

Theorems C.6.1.1–C.6.2.1 and Proposition C.7.1.1 give the open condition, normalized inverse, affine-hull coefficient intersection and exact cocharacter/rotation formula. Exercise C.11.1 displays the nonreduced torus chart. Editable SVG source.

### C.8. Contraction gives the actual restriction and counit

Let \(f:Y\to B\) be separated of finite type, with a closed section \(z:B\to Y\). Suppose a monoid action \(a:\mathbf A^1_B\times_B Y\to Y\) is over \(B\), is the identity at \(1\), restricts to a group action on \(\mathbb G_m\), and has \(a_0=zf\). Write \(U=Y\setminus z(B)\).

**Theorem C.8.1.1.** For an actual naively \(\mathbb G_m\)-equivariant bounded constructible \(F\), the restriction unit and exceptional counit induce
\[
 Rf_*F\xrightarrow{\sim}z^*F,\qquad
 z^!F\xrightarrow{\sim}Rf_!F.
 \tag{C.8.1}
\]
They also hold for finite cones, shifts and direct summands of such objects. In particular the first is the fixed-stalk comparison on a contracting chart, including its finite torus classifying approximations.

**Proof.** We give the action-graph argument for this precise hypothesis, rather than treating the more restricted projective-bundle statement of Lesson 5, Q.2.2.1, as a general contraction theorem. Use that lesson's actual ordinary smooth comparison Q.1.1.1 and affine-line propagation Q.1.3.1–Q.1.3.2, whose proofs apply to the trivial-action base \(B\).

Let \(j:U\to Y\), put \(F_0=j_!j^*F\), and put \(C=Rf_*F_0\). Set
\[
 Q_Y=1_{\mathbf A^1}\times f,\quad
 q:\mathbf A^1_B\to B,\quad
 r(s,y)=(s,a_s(y)),\quad
 D=R(Q_Y)_*r^*p_Y^*F_0.
 \tag{C.8.2}
\]
The maps \(Q_Yr\) and \(Q_Y\) are equal. Over \(\mathbb G_m\), \(r\) is an isomorphism, so ordinary smooth comparison and equivariance give \(D|_{\mathbb G_m}=q^*C|_{\mathbb G_m}\).

The inverse image of \(U\) under the action is exactly \(\mathbb G_m\times U\): invertible parameters act by automorphisms fixing the section, whereas zero maps into the section. Pullback of open extension by zero and the chosen equivariance isomorphism consequently give
\[
 r^*p_Y^*F_0
 \simeq j_{Y,!}j_Y^*p_Y^*F_0,
 \tag{C.8.3}
\]
where \(j_Y:\mathbb G_m\times Y\to\mathbf A^1\times Y\). Ordinary image composition and the affine-line calculation Q.1.3.1 imply
\[
 Rq_*D
 =Rf_*R(p_Y)_*j_{Y,!}j_Y^*p_Y^*F_0=0.
 \tag{C.8.4}
\]
Q.1.3.2, applied with the already established constant form on \(\mathbb G_m\), now gives \(D|_0=0\). Localization identifies \(D\) with extension by zero of its restriction to \(\mathbb G_m\). This inference uses the affine-line calculation, not ordinary nonproper base change at zero.

The ordinary adjunction unit for \(r\), followed by image composition \(Q_Yr=Q_Y\), gives
\[
 \beta:q^*C\longrightarrow D.
 \tag{C.8.5}
\]
It is invertible over \(\mathbb G_m\). Extend its inverse by zero to obtain \(\gamma:D\to q^*C\). The endomorphism \(\gamma\beta\) of \(q^*C\) is the identity at \(1\) and zero at \(0\). Affine-line propagation Q.1.3.1 therefore gives \(C=0\). Apply \(Rf_*\) to the support triangle
\[
 F_0\longrightarrow F\longrightarrow z_*z^*F
 \longrightarrow .
\]
Its specified second arrow is the restriction map, so this proves the first isomorphism of (C.8.1).

Verdier duality preserves naive equivariance: on the smooth group parameter its two equal orientation lines cancel, as proved in Q.1.4.1. Apply the first isomorphism to \(D_YF\) and dualize. The actual dual exchanges and supported adjunction of Lesson 5, P.3, identify the resulting map as the section counit \(z^!F\to Rf_!F\), with its original trace normalization. Finally the two arrows are natural transformations of exact functors. Their isomorphism loci are closed under finite cones, shifts and direct summands. ∎

### C.9. The precise weight implication for stalk surjectivity

This section is a conditional weight lemma. Its hypothesis is the compact-support upper weight estimate:

\[
 \text{if every }H^b(K_{\bar y})\text{ has weights }\le v+b,
 \quad
 H_c^n(Y_{\bar k},K)\text{ has weights }\le v+n.
 \tag{W\_c}
\]

Here \(Y\) is finite type over a finite field, \(K\) is a mixed bounded constructible complex, and the assertion is required also on the finite classifying approximations being used. This hypothesis is separate from parity and from the statements proved in §§1–8.

**Lemma C.9.1.1.** Assume \((W_c)\). Let \(X\) be proper over \(\mathbf F_q\), with a split torus action. Let \(P\) be an actual equivariant mixed complex, let \(x\) be a rational fixed point, and suppose:

- the stalks of \(D_XP\) have upper complex weight \(-w\);
- every \(H^b(P_x)\) is pure of weight \(w+b\);
- \(x\) has an open neighborhood with an actual contracting action commuting with \(T\), and \(P\) has the equivariance of Theorem C.8.1.1.

Then the actual restriction \(H_T^n(X,P)\to H_T^n(x,P_x)\) is surjective in every degree. The assertion keeps Frobenius and the coefficient lines, and does not require Frobenius semisimplicity.

**Proof.** Work at \(B_m=(\mathbf P^m)^r\). Write \(X_m=X\times^T P_m\), \(U_m\) for the associated contracting neighborhood, \(Z_m=X_m\setminus U_m\), and \(P^{(m)}\) for the descended complex. Theorem C.8.1.1 over the base \(B_m\) identifies the ordinary image from \(U_m\) with that of the fixed section.

The cohomology sheaves on that section are the constant \(H^b(P_x)\)-systems: the connected torus acts trivially on each ordinary cohomology system of a point, since its action is an isomorphism of constant systems on connected \(T\) and is the identity at \(1\). The associated systems consequently descend with identity transitions. By (C.5.2), their base degree \(a\) has weight \(a\). The section spectral sequence thus has total-degree-\(n\) terms of weight \(w+n\). Its differentials raise total degree by one and commute with Frobenius, so are zero between these disjoint weights. Its finite filtration makes degree \(n\) pure of weight \(w+n\), without asserting that the filtration splits as a Frobenius representation.

The descended dual \(D_{X_m}P^{(m)}\) has upper complex weight \(-w\). Locally it is \(D_XP\) times the smooth base dualizing complex \(E(\dim B_m)[2\dim B_m]\); the shift and Tate line cancel in the complex weight convention. Restriction to \(Z_m\) preserves the stated stalk upper bound. Actual supported duality gives
\[
 H_{Z_m}^{n+1}(X_m,P^{(m)})
 =
 H_c^{-n-1}(Z_m,i_{Z_m}^*D_{X_m}P^{(m)})^\vee.
 \tag{C.9.1}
\]
Hypothesis \((W_c)\) makes the right side have weights at least \(w+n+1\). The localization boundary from \(H^n(U_m,P^{(m)})\), pure of weight \(w+n\), is therefore zero. A Frobenius-linear map between finite-dimensional representations with disjoint eigenvalue weights is zero even for nontrivial Jordan blocks: over a splitting extension its source and target primary eigenvalue factors are disjoint, and the coprime minimal polynomials force the map to vanish.

The localization long exact sequence now gives surjectivity from \(X_m\) to \(U_m\), hence to the section. Passing to a stable approximation in each degree proves the assertion. Every used arrow was restriction, duality, or a localization boundary, so the result concerns the actual restriction map. ∎

### C.10. A cell criterion for the actual Ext-to-Hom isomorphism

Let \(X\) have the proper finite linear \(T\)-cell filtration of §5. Let \(A=H_T^*(X,E)\). For actual equivariant bounded constructible objects \(P,Q\), assume:

1. On every cell \(C\), the cohomology sheaves of \(i_C^*P\) and \(i_C^!Q\) are geometrically constant and are concentrated, respectively, in two fixed parities \(\eta_P,\eta_Q\).
2. For every cell origin \(x\), the actual map \(H_T^*(X,P)\to H_T^*(x,P_x)\) is surjective.
3. Restriction from each cell to its origin identifies \(H_T^*(C,i_C^*P)\) with \(H_T^*(x,P_x)\).

The third condition also follows from the linear cell contraction whenever that contraction has the indicated actual equivariance. The theorem does not assert that stalk parity supplies the second condition.

**Theorem C.10.1.1.** Under these hypotheses, equivariant cohomology induces an isomorphism
\[
 h:\operatorname{Ext}_{D_T(X)}^*(P,Q)
 \xrightarrow{\sim}
 \operatorname{Hom}_A^*(H_T^*(X,P),H_T^*(X,Q)).
 \tag{C.10.1}
\]
For a family satisfying these conditions for its pairs, the isomorphisms preserve identities and actual Yoneda composition.

**Proof.** We prove a strengthened statement simultaneously for every term \(X'\) of the closed filtration: the comparison for \((i_{X'}^*P,i_{X'}^!Q)\) is an isomorphism with the original \(A\)-linear Hom, and its Ext module is finite free over \(S\), concentrated in parity \(\eta_Q-\eta_P\). The empty term starts the induction. For a last open cell \(u:C\to X'\) and closed complement \(v:Z\to X'\), set \(E'=i_{X'}^*P\) and \(F'=i_{X'}^!Q\).

The smaller pair is exactly \((i_Z^*P,i_Z^!Q)\), by composition of the respective restrictions. Its cell hypotheses are inherited. The original surjection to any origin in \(Z\) factors through \(H_T^*(Z,i_Z^*P)\), so the recursive source has the required origin surjectivity. Every module action throughout this strengthened induction is through the original \(A\).

First record the cell calculation. A geometrically constant equivariant cohomology system on \(C\) is the constant coefficient system with its vector space: connected \(T\) gives identity on its cohomology, as in C.9. Equivariant cohomology of the constant object on the representation \(C\) is \(S\), and its compact cohomology is \(S(-d)[-2d]\), by the vector-bundle contraction and smooth trace. A complex whose cohomology lies in one parity splits in the geometric equivariant derived category into these shifted constant systems. Indeed each Postnikov attaching obstruction is an odd Ext between constant systems, whereas \(H_T^*(C,E)=S\) has no odd degrees. This proves the assertion inductively through its finite cohomology range. No splitting of Frobenius representations is needed.

Thus ordinary and compact cell cohomology are finite free \(S\)-modules of their specified parity. Between the two cell complexes, the actual Ext-to-cohomology map is the usual matrix map with entries in \(S\); it is an isomorphism. To check this without depending on a splitting choice, check constant shifted summands: cup multiplication sends an Ext entry \(a\in S\) to multiplication by \(a\). Finite direct sums give the matrix assertion, and naturality makes the conclusion independent of the chosen summand presentations. The action of \(A\) on these modules factors through \(H_T^*(C,E)=S\). That map is onto, since the base inclusion \(S\to A\) restricts to the identity. Hence their \(A\)-linear Hom equals their \(S\)-linear Hom.

Next use compact open–closed induction for the *restrictions of \(P\). All terms have parity \(\eta_P\), so the connecting maps of degree one are zero. This proves finite freeness and the exact first filtration of C.2,
\[
 0\to H_{T,c}^*(C,u^*E')\to H_T^*(X',E')
 \to H_T^*(Z,v^*E')\to0.
 \tag{C.10.2}
\]
The properness of \(X'\) identifies ordinary and compact images here. Freeness follows by lifting a basis of the free cell or quotient module to split each \(S\)-module extension.

Similarly, closed-costalk induction for \(F'\) uses \(v^!F'\), whose costalk parity is inherited by composition of exceptional restrictions. The open cell terms have parity \(\eta_Q\). It proves freeness and
\[
 0\to H_T^*(Z,v^!F')\to H_T^*(X',F')
 \to H_T^*(C,u^*F')\to0.
 \tag{C.10.3}
\]

Hypotheses 2–3 supply surjectivity
\(H_T^*(X',E')\to H_T^*(C,u^*E')\). In fact the surjection from \(X\) to the cell origin factors through this map and then through the isomorphism in hypothesis 3. The supported triangle and surjectivity in every degree consequently give
\[
 0\to H_T^*(Z,v^!E')\to H_T^*(X',E')
 \to H_T^*(C,u^*E')\to0.
 \tag{C.10.4}
\]
This step uses no unproved exceptional-parity assertion for \(i_{X'}^*P\).

The three sequences (C.10.2)–(C.10.4) are exactly those of C.2. Identify their localized supports separately. For the compact open and ordinary open modules \(P_c,P_U,F_U\), the cup action factors through
\[
 A\longrightarrow H_T^*(C,E)=S
 \longrightarrow H_T^*(x,E)=S,
 \tag{C.10.6}
\]
where \(x\) is the last cell origin. After localization this is the character of that origin in \(\prod_{y\in P}Q\), so these modules are supported there, or are zero. For \(P_!,P_Z,F_Z\), apply Theorem C.5.2.1 to their actual closed extensions from \(Z\) into the proper original \(X\); their localized supports lie among the complementary origins. This does not assert vanishing boundary stalks for an ordinary open direct image. The target modules in C.2 are free by (C.10.3) and the cell calculation. Lemmas C.1–C.2 therefore give the actual left-exact Hom row.

Apply \(\operatorname{RHom}(-,F')\) to
\(u_!u^*E'\to E'\to v_*v^*E'\to\).
Closed and open adjunction identify its two outer terms with
\[
 \operatorname{Ext}_{D_T(Z)}^*(v^*E',v^!F'),
 \qquad
 \operatorname{Ext}_{D_T(C)}^*(u^*E',u^*F').
 \tag{C.10.5}
\]
By the strengthened induction and the cell calculation they are finite free \(S\)-modules, concentrated in parity \(\eta_Q-\eta_P\). The degree-one connecting maps are zero, giving the genuine short exact upper Ext row. Its free cell quotient has a homogeneous \(S\)-basis; lifting that basis splits the sequence as \(S\)-modules. The middle Ext module is therefore finite free with the same parity, proving this part of the strengthened assertion. Freeness has been proved from the Ext sequence, rather than inferred from a Hom submodule of free modules.

Its maps and the lower Hom maps form the commutative diagram of C.3: the closed arrow is the counit on the target and unit on the source, and the open arrow is actual restriction. Applying cohomology gives precisely the factorization defining \(\alpha,\beta\) in C.2.

The outer comparison maps are isomorphisms by the induction and cell calculation. Lemma C.3.1.1 makes the middle comparison an isomorphism, and also proves the lower row surjective. The empty union starts the induction. At \(X'=X\) this is (C.10.1).

Finally \(h\) is induced by the actual cohomology functor. Its map on a composite of derived morphisms is the composite of its maps, with the ordinary grading and shift convention; it sends an identity to an identity. Thus the theorem preserves Yoneda products, rather than only computing their dimensions. ∎

![Euler localization kills cross-Hom terms, and the actual Ext row lifts every integral module morphism under the cell criterion](assets/localized-support-lifting.png)

Lemma C.5.1.1 and Theorem C.5.2.1 prove the displayed Euler annihilation and localized algebra. Lemmas C.1–C.3 give the exact Hom row and integral lifting. Theorem C.10.1.1 verifies those rows and composition under its stated fixed-point restriction hypotheses. Localization is used to prove vanishing; the upper Ext surjection supplies the lifts. Editable SVG source.

### C.11. Three solved exercises

**Exercise C.11.1 (basic).** Describe \(\Omega_1\) for \(GL_1\), and compute its contraction over \(R=k[\epsilon]/\epsilon^2\).

**Solution.** The lattice quotient is the line generated by \(1+at^{-1}\) in \(t^{-1}O/tO\). Its positive projection is the isomorphism sending that vector to \(1\). Multiplication by \(t\) preserves the line precisely when
\[
 a=a(1+at^{-1}),\qquad a^2=0.
\]
Thus the chart is \(\operatorname{Spec}k[a]/a^2\), with normalized negative loop \(1+at^{-1}\) and inverse \(1-at^{-1}\). Over the stated dual numbers, \(a=b\epsilon\) with arbitrary \(b\in k\). The monoid sends \(a\) to \(sa\). Its zero map is the identity lattice, but the chart itself has its nonzero tangent direction. This verifies both the sign and retention of the nilpotent parameter in C.6–C.7.

**Exercise C.11.2 (intermediate).** For \(T=\mathbb G_m\), compute the annihilating Euler polynomial for
\(V=k_\chi\oplus k_{2\chi}\). Compute the localized support of a closed-extension point module inside a two-fixed-point proper cell scheme.

**Solution.** With \(u=c_1(\chi)\), the character-line calculation gives \(e_T(V)=u(2u)=2u^2\), of degree \(4\), with coefficient twist \(E(2)\). It is nonzero over the characteristic-zero field \(E\), also when the geometric characteristic is two; the integral character \(2\chi\) has not become a zero coefficient in \(E\). Lemma C.5.1.1 kills both images from \(V\setminus0\) after inverting \(u\).

In the ring \(A=S[h]/h(h-u)\) of §4, the point modules have localized supports \(e_0=1-h/u\) and \(e_\infty=h/u\), respectively. Each idempotent acts as identity on its own point module and zero on the other. Thus C.1 gives their integral cross-Hom vanishing. At \(u=0\) their specialized-module Hom is instead \(E\), exactly as computed in §4; this does not contradict localization or prove that Hom commutes with specialization.

**Exercise C.11.3 (advanced).** Let \(X=\mathbf P^1\), with affine open \(j:C=\mathbf A^1_\alpha\to X\) and its nonzero \(T\)-weight \(\alpha\). Show that \(F=j_!E_C\) has even ordinary cell restrictions, while \(H_T^*(X,F)\to H_T^*(C,E)\) is not onto. Explain the relevance to recursive closed restriction of an IC.

**Solution.** Its open restriction is \(E_C\) in degree zero and its closed ordinary restriction is zero. Both satisfy even ordinary parity. Properness gives
\[
 H_T^*(X,F)=H_{T,c}^*(C,E)=S(-1)[-2],
 \qquad H_T^*(C,E)=S.
\]
The restriction map is multiplication by the character Euler class
\[
 S(-1)[-2]\xrightarrow{\alpha}S.
 \tag{C.11.1}
\]
To determine this actual arrow, the zero-section orientation maps
\(S(-1)[-2]\) to the compact cohomology of the line. Its composite with the line trace is the identity by Lesson 6 A.1.1.1, hence is the compact orientation isomorphism. Forgetting compact support and restricting to the zero section sends that class to \(c_1(k_\alpha)=\alpha\), by A.1.2.1. This proves (C.11.1) with its trace normalization.

The map is injective and its cokernel is \(S/(\alpha)\), so it is not onto. The localization boundary places this cokernel in odd supported cohomology at infinity. Thus ordinary parity does not imply exceptional parity or open-restriction surjectivity.

For a recursively restricted source \(i_{X'}^*P\), its ordinary cell restrictions are inherited from \(P\), but its exceptional restriction to a smaller closed union is \(v^!i_{X'}^*P\); it need not be the exceptional restriction of \(P\) to that union in the original space. The common-parity theorem for the original IC therefore does not prove the missing condition 2 of C.10. The weight lemma C.9 supplies a distinct sufficient implication only under its explicitly stated hypothesis \((W_c)\).

### C.12. Restriction from the whole Grassmannian

The exact earlier proof inputs are Lesson 1, Theorem 2.C, Lesson 2, Theorem 7.1 and Lemmas 7.10-7.12, Lesson 4, Theorem 3.5 and section 5, and Lesson 5, Lemma Q.1.2.1 and the closed-open triangles of Appendices O-P. They supply the root-coordinate recursion, full bounded stages, closure and component classification, and normalized affine-line trace. The restriction and inverse-limit argument are proved below.

Continue over an algebraically closed field \(k\), with the original connected reductive group \(G\), maximal torus \(T\), and Borel \(B\). The coefficient field \(E\) has characteristic zero and residue characteristic different from that of \(k\). Put
\[
 \Lambda=X_*(T),\qquad Q^\vee=\mathbb Z\Phi^\vee,\qquad
 \Pi=\Lambda/Q^\vee,\qquad S=H_T^*(\mathrm{pt},E).
\]
The quotient \(\Pi\) includes the free directions contributed by the centre. We use the actual full bounded stages \(Y_N\) of Lesson 2, Theorem 7.1 and §7.6, with their original scheme structures. Ordinary cohomology on this countable ind-presentation means derived compatible sections on those stages. We will compute that complex explicitly below. In particular, we will prove that its restriction to a finite support is onto; this assertion is not built into the definition.

#### C.12.1. Cells of bounded dimension in one component

Let \(I\subset G(k[[t]])\) be the inverse image of \(B\) under evaluation at zero. For a root \(\alpha\), set \(r(\alpha)=0\) for \(\alpha>0\), and \(r(\alpha)=1\) for \(\alpha<0\).

**Lemma C.12.1.1.** The \(I\)-orbit \(C_\lambda=It^\lambda K/K\), for \(\lambda\in\Lambda\), is a \(T\)-linear affine cell of dimension
\[
 d_I(\lambda)=
 \sum_{\alpha\in\Phi}
       \max\bigl(0,\langle\alpha,\lambda\rangle-r(\alpha)\bigr).
 \tag{C.12.1}
\]
It is contained in the actual negative-loop open \(U_\lambda\) of C.7. Its contraction there acts on the coordinate indexed by \((\alpha,n)\) as
\[
 c_{\alpha,n}\longmapsto
       s^{\langle\alpha,\lambda\rangle-n}c_{\alpha,n},
 \qquad
 r(\alpha)\le n<\langle\alpha,\lambda\rangle.
 \tag{C.12.2}
\]
In each fixed class \(\kappa\in\Pi\), only finitely many such cells have \(d_I(\lambda)\le D\), for every integer \(D\).

**Proof.** The ordered root-coordinate and height argument of Lesson 1, Theorem 2.C, applies to \(I/(I\cap t^\lambda Kt^{-\lambda})\) as follows. In the big-cell coordinates of \(I\), conjugation by \(t^{-\lambda}\) changes the \(\alpha\)-coordinate exponent \(n\) to \(n-\langle\alpha,\lambda\rangle\). The integral big-cell test in that theorem shows that the conjugated element is integral exactly when each root coordinate has valuation at least \(\langle\alpha,\lambda\rangle\). The torus arc is unchanged. Thus the stabilizer has root thresholds
\[
 \max\bigl(r(\alpha),\langle\alpha,\lambda\rangle\bigr),
\]
and contains every torus arc.

Here is the coefficient split needed for this quotient. Place first the finitely many coefficients with
\(r(\alpha)\le n<\langle\alpha,\lambda\rangle\), and then the common coefficients at or above both thresholds. Each set is closed under addition whenever the sum is a real affine root. Two of the first set cannot sum to a positive imaginary degree: for opposite roots their exponents have sum at least one, while the two strict upper inequalities would make that sum negative. Common coefficients and their opposite-root torus corrections stay in the common set.

Use the positive integral affine height from the proof of Theorem 2.C to reorder these products. A commutator changes only coefficients of larger height. Opposite-root interchanges have denominator \(1+uv\) with \(uv\in tR[[t]]\); its inverse is the convergent geometric series, and its torus correction is common. At each height recover the next coefficient uniquely by subtracting the already known corrections. At any bounded height these operations and their inverses are polynomial in finitely many coefficients. This proves, over every test algebra \(R\), the unique factorization into the displayed first coefficients and a stabilizer element. The quotient is their affine space, giving (C.12.1). The refined Cartan decomposition in the same theorem identifies these cells, without repetitions, as the cells of the Grassmannian.

A representative of this affine space is an ordered product of
\(u_\alpha(c_{\alpha,n}t^n)t^\lambda\). Move \(t^\lambda\) to the left. All remaining factors have exponent
\(n-\langle\alpha,\lambda\rangle<0\), are polynomial in \(t^{-1}\), and have value one at infinity. Their product is an actual element of \(L^{--}G(R)\). This proves the claimed inclusion in \(U_\lambda\), including its scheme structure. Substitution \(t^{-1}\mapsto st^{-1}\) gives (C.12.2); every displayed exponent of \(s\) is positive. Constant \(T\) conjugation multiplies this coordinate by the character \(\alpha\). Therefore these are linear \(T\)-coordinates, and the two actions commute.

For a positive root put \(m=\langle\alpha,\lambda\rangle\). Its pair with \(-\alpha\) contributes
\[
 \max(0,m)+\max(0,-m-1)
 =
 \begin{cases}m,&m\ge0,\\-m-1,&m<0.\end{cases}
\]
Consequently
\[
 |\langle\alpha,\lambda\rangle|\le d_I(\lambda)+1.
 \tag{C.12.3}
\]
Fix a representative \(\lambda_0\) of \(\kappa\). Then \(\lambda-\lambda_0\in Q^\vee\). The simple-root pairings give an injective real linear map on the real span of the coroots: its matrix in the simple-coroot basis is the invertible finite Cartan matrix, as proved by the positive definite root-space form in Lesson 1, Theorem 2.C. Inequality (C.12.3) bounds all these pairings, so it bounds \(\lambda-\lambda_0\) in that real vector space. A bounded set meets the free lattice \(Q^\vee\) in finitely many elements, by expressing it in an integral basis. This proves finiteness. If \(G\) is a torus, \(Q^\vee=0\) and each class has exactly one cell; the same argument includes this case. ∎

#### C.12.2. The full stages and reduced Schubert exhaustion

Write \(\operatorname{Gr}_\kappa\) for the component with class \(\kappa\). The classification and local constancy of this class were proved in Lesson 4, §5, for the original group and in every geometric characteristic.

**Lemma C.12.2.1.** Each component has a nested sequence of projective reduced Schubert varieties \(Z_j\) such that every reduced bounded stage \(Y_{N,\kappa,\mathrm{red}}\) is contained in some \(Z_j\), and every \(Z_j\) is contained in some full bounded stage. The actual restrictions
\[
 R\Gamma_T(Y_{N,\kappa},E)\longrightarrow
 R\Gamma_T(Y_{N,\kappa,\mathrm{red}},E)
 \tag{C.12.4}
\]
are multiplicative quasi-isomorphisms, compatible with all transitions.

**Proof.** Choose a dominant \(\lambda_0\) in the class \(\kappa\); reflecting any representative to a dominant one preserves its class, since
\(s_\alpha\lambda-\lambda=-\langle\alpha,\lambda\rangle\alpha^\vee\).
Put
\[
 \eta=\sum_{\alpha>0}\alpha^\vee,\qquad
 \lambda_j=\lambda_0+j\eta,\qquad
 Z_j=\overline{\operatorname{Gr}^{\lambda_j}}_{\mathrm{red}}.
\]
Each simple-coroot coefficient of \(\eta\) is positive: the positive coroots have nonnegative coefficients, and the corresponding simple coroot occurs among them. A simple reflection permutes all positive coroots except its own simple coroot, which it makes negative. Hence
\(s_i\eta=\eta-2\alpha_i^\vee\), so
\(\langle\alpha_i,\eta\rangle=2\). Thus every \(\lambda_j\) is dominant and \(\lambda_j\le\lambda_{j+1}\). Lesson 4, Theorem 3.5 proves that the \(Z_j\) are nested and projective.

If \(\mu\) is any dominant coweight of class \(\kappa\), then
\(\lambda_0-\mu\) has integral simple-coroot coefficients. Adding \(j\eta\), whose coefficients are all positive, makes them all nonnegative for sufficiently large \(j\). Thus \(\mu\le\lambda_j\). For a torus the class has only \(\mu=\lambda_0\), and the sequence is constant.

We now check the full bounded stages. They are \(K\)-stable: an integral matrix and its inverse preserve both bounding lattices in the faithful representation used in Lesson 2. By its Lemma 7.10 only finitely many dominant Cartan coweights occur in \(Y_N\). A Cartan orbit which occurs is wholly contained there, and so is its reduced closure, because \(Y_N\) is a closed stage. Their finite union, with reduced structure, equals \(Y_{N,\mathrm{red}}\). Indeed their geometric points cover it by Cartan decomposition, over every algebraically closed extension of \(k\). Equality of closed supports in a common bounded stage gives equality of their radical ideals, hence equality of the reduced closed subschemes. In the component \(\kappa\), choose \(j\) dominating all these finitely many coweights. The closure theorem gives the required inclusion into \(Z_j\). Conversely every finite-type Schubert variety has a finite lattice bound, as in the projectivity proof of Lesson 4, and therefore lies in a full \(Y_N\).

This is an exhaustion statement about the reductions. For the actual cohomology comparison let \(i:Y_{\mathrm{red}}\to Y\) be any of the closed reductions. Its open complement is empty. The closed–open triangle proved in Lesson 5, Appendices O–P, is therefore the actual unit isomorphism
\[
 E_Y\xrightarrow{\ \sim\ }i_*i^*E_Y=i_*E_{Y_{\mathrm{red}}}.
\]
Apply equivariant global sections. This proves (C.12.4). The map is the pullback of constants, so it preserves the unit, cup product, and pullbacks along stage inclusions. The reduction is \(T\)-stable: a product of a reduced \(k\)-scheme with the smooth split torus is reduced, so its action factors through the reduction. The same closed–open argument applies on each finite Borel approximation and is compatible with those approximations.

No nilpotent Grassmannian family has been removed from the moduli construction. For example, \(1+\epsilon t^{-1}\) in the torus chart of C.11.1 does not factor through its reduced point. The comparison just proved identifies constant cohomology through an actual closed restriction. It does not identify the two functors of points. ∎

#### C.12.3. Surjective restrictions and the inverse limit

**Theorem C.12.3.1.** Let \(X\) be a proper closed finite union of Iwahori cells in \(\operatorname{Gr}_G\), with reduced structure, or a \(T\)-stable closed nilpotent thickening with that reduction. Then the actual restriction of graded rings
\[
 H_T^*(\operatorname{Gr}_G,E)\longrightarrow H_T^*(X,E)
 \tag{C.12.5}
\]
is onto. In a single component, each fixed cohomological degree stabilizes along the sequence of Lemma C.12.2.1 and is finite dimensional over \(E\). No stabilization across all components is asserted.

**Proof.** First let \(X\subset Y\) be two projective reduced finite cell unions, and set \(U=Y\setminus X\). Their cells admit filtrations by closed unions with one affine cell at each step. To see this, the closure of an \(I\)-orbit is \(I\)-stable and its boundary has strictly smaller dimension. It is a union of the finitely many cells of \(Y\), by the refined Cartan decomposition. Put all boundary cells before a cell in the order. At each step the new union is the preceding closed union together with that cell's closure, so is closed. Since \(X\) is already a closed cell union, its cells may be put first. The remaining order gives a closed-cell filtration of \(U\).

By Lemma C.12.1.1, a cell of dimension \(d\) is a \(T\)-representation of dimension \(d\). Its finite Borel approximation is a rank-\(d\) vector bundle \(v:V\to B_m\). Iterate the actual affine-line trace of Lesson 5, Lemma Q.1.2.1, on a trivializing open to obtain \(Rv_!E_V=E_{B_m}(-d)[-2d]\). The comparison is the smooth trace, with its given normalization, so these local comparisons agree under the vector-bundle transition maps. Equivalently the trace cone vanishes on every trivializing open and hence vanishes globally. Passing to the compatible finite Borel approximations gives the compact cell cohomology
\[
 H_{T,c}^q(C,E)=S^{q-2d}(-d).
 \tag{C.12.6}
\]
Here \(S^a=0\) for \(a<0\) or \(a\) odd. Applying the compact closed–open triangle successively to the filtrations proves that the compact cohomology of \(U,X,Y\) is even and finite free over \(S\). More explicitly, the odd groups vanish by induction; the resulting exact sequence in even degrees has free cell quotient, and lifting its homogeneous basis splits it as a graded \(S\)-module. On \(X,Y\), properness identifies compact and ordinary cohomology.

Now use the compact triangle for \(U\subset Y\) with closed complement \(X\). Its boundary from \(H_T^q(X)\) goes to \(H_{T,c}^{q+1}(U)\). For even \(q\) the latter vanishes, and for odd \(q\) all ordinary groups vanish. We obtain the actual graded exact sequence
\[
 0\longrightarrow H_{T,c}^*(U,E)
 \longrightarrow H_T^*(Y,E)
 \longrightarrow H_T^*(X,E)
 \longrightarrow0.
 \tag{C.12.7}
\]
In particular restriction is onto. It is the pullback of constants and therefore is a ring map; a chosen module splitting is not being used as its definition.

Fix a component and a degree bound \(q\ge0\). By Lemma C.12.1.1 there are only finitely many cells in that component of dimension at most \(q/2\). The exhaustion in Lemma C.12.2.1 puts all of them in some \(Z_{j_0}\). For \(j'\ge j\ge j_0\), every cell in \(Z_{j'}\setminus Z_j\) has \(2d>q\). Formula (C.12.6) and its filtration show that this complement's compact cohomology vanishes in degrees at most \(q\). Sequence (C.12.7) consequently makes restriction an isomorphism in all those degrees. Each stabilized group is finite dimensional over \(E\), since a finite free graded \(S\)-module with finitely many homogeneous generators has finite dimensional homogeneous pieces.

For completeness, compute the derived compatible-section complex, so an inverse-limit term is not omitted. Write \(C_j=R\Gamma_T(Z_j,E)\) and \(f_j:C_{j+1}\to C_j\) for restriction. Derived compatible sections on this tower are the homotopy fibre
\[
 R\!\varprojlim_j C_j
 =
 \operatorname{fib}\left(
  \prod_{j\ge0}C_j
   \xrightarrow{\,1-\mathrm{shift}\,}
  \prod_{j\ge0}C_j\right),
 \quad
 (a_j)\longmapsto(a_j-f_j(a_{j+1})).
 \tag{C.12.8}
\]
Formula (C.12.8) specifies the derived compatible-section complex used here, with its canonical maps to the stages. It is invariant under componentwise quasi-isomorphisms: products of \(E\)-vector spaces are exact, so a product of quasi-isomorphisms is a quasi-isomorphism; the two products and their fibre consequently preserve such a replacement. Cohomology of the products is the product of cohomology. The fibre's long exact sequence therefore gives
\[
 0\longrightarrow
 \operatorname{coker}\!\left(1-\mathrm{shift}:
       \prod_j H_T^{q-1}(Z_j)\to\prod_j H_T^{q-1}(Z_j)\right)
 \longrightarrow H^q(R\!\varprojlim_j C_j)
 \longrightarrow\varprojlim_j H_T^q(Z_j)
 \longrightarrow0.
 \tag{C.12.9}
\]
The cokernel is zero. Indeed all the cohomological restriction maps are onto by (C.12.7). For a prescribed sequence \((b_j)\), choose \(a_0=0\) and successively choose \(a_{j+1}\) with \(f_j(a_{j+1})=a_j-b_j\). This solves \((1-\mathrm{shift})a=b\) in each homogeneous degree. Thus the canonical map in (C.12.9) identifies cohomology with the ordinary inverse limit.

Apply the same calculation directly to the full bounded presentation. By C.12.2.1 its reduction maps are compatible quasi-isomorphisms; its reduced stages are finite Schubert unions. The preceding cell argument and (C.12.7) show that their cohomological transitions are onto. Thus (C.12.9) also identifies cohomology of derived compatible sections on the full \(Y_{N,\kappa}\) with the ordinary limit of their graded cohomology. These ordinary limits agree canonically with the limit over \(Z_j\): for each stage in either system choose a containing stage in the other and restrict a compatible family. Independence of this choice follows by restricting from a common larger stage; the two resulting operations are inverse by the same argument. This proves the comparison on cohomology without assuming a separate derived cofinality theorem.

Cup products are compatible at every stage, and the canonical projection of derived compatible sections to a stage preserves them. One may define their product on a sheaf-cochain model before taking compatible sections; compatibility says exactly that restricting a product restricts both factors. The canonical map in (C.12.9) therefore identifies this product with the product of compatible homogeneous classes, not merely with an abstract isomorphic algebra.

If a finite \(X\) lies in \(Z_m\), choose a lift of a homogeneous class in \(H_T^q(X)\) to \(H_T^q(Z_m)\) using (C.12.7). Choose successive lifts to \(Z_{m+1},Z_{m+2},\ldots\) by the same surjectivity, and define the earlier classes by restriction. This is a compatible homogeneous class, and (C.12.9) realizes it in \(H_T^q(\operatorname{Gr}_\kappa)\). This proves (C.12.5) in one component.

For the full Grassmannian, the component classification gives a disjoint union indexed by \(\Pi\). Compatible sections give a degreewise product
\[
 H_T^q(\operatorname{Gr}_G,E)
       =\prod_{\kappa\in\Pi}H_T^q(\operatorname{Gr}_\kappa,E).
 \tag{C.12.10}
\]
One can verify this on the bounded presentation: each stage meets only finitely many classes by Lesson 2, Lemma 7.10, and enlarging stages covers every class. Thus a compatible family is exactly a family of compatible classes on all components. A finite \(X\) meets finitely many components. Lift its class in each of them as above and use zero in the others. This proves the global surjectivity, even when the centre contributes infinitely many classes.

Finally, for a nilpotent thickening \(X\) the actual closed restriction to \(X_{\mathrm{red}}\) is the multiplicative isomorphism proved in C.12.2.1. Its composite with (C.12.5) is the already proved surjection onto that reduction, so restriction onto \(X\) is onto as well. ∎

**Corollary C.12.3.2.** For complexes \(P,Q\) supported on such an \(X\), the actual whole-Grassmannian action gives
\[
 \operatorname{Hom}_{H_T^*(\operatorname{Gr}_G)}^*
       \bigl(H_T^*(X,P),H_T^*(X,Q)\bigr)
 =
 \operatorname{Hom}_{H_T^*(X)}^*
       \bigl(H_T^*(X,P),H_T^*(X,Q)\bigr).
 \tag{C.12.11}
\]
Whenever the hypotheses of C.10 hold on \(X\), its comparison theorem therefore holds with the whole Grassmannian cohomology ring.

**Proof.** Both module actions factor through actual restriction to \(H_T^*(X)\): cup product with a supported complex first restricts the constant class to its support. If a homogeneous map commutes with the whole-Grassmannian action, lift any homogeneous class of \(H_T^*(X)\) using C.12.3.1. Commutation with that lift is commutation with the given class. Conversely commutation with every support class implies commutation with their restrictions. These are the same maps, with the same degrees and compositions. The last assertion is now exactly C.10 applied to this equality; no stalk-surjectivity hypothesis has been supplied by the corollary. ∎

#### C.12.4. Two exercises on the component qualification

**Exercise C.12.4.1 (basic).** Compute the ring in (C.12.10) for \(G=\mathbb G_m\). Explain why the full Grassmannian does not have finite dimensional degree-zero cohomology, despite degreewise stabilization on each component.

**Solution.** Here \(\Lambda=\Pi=\mathbb Z\), \(Q^\vee=0\), and each reduced component is one point \(t^n\). Its full stages may retain the nilpotents displayed in C.11.1, but C.12.2.1 identifies their constant cohomology with that point's cohomology. With \(u=c_1(\chi)\),
\[
 H_T^*(\operatorname{Gr}_{\mathbb G_m},E)
      =\prod_{n\in\mathbb Z}^{\mathrm{degreewise}}E[u].
 \tag{C.12.12}
\]
The superscript specifies the graded ring: in each degree one takes the product of that degree's vector spaces, with componentwise multiplication. It is not a direct sum of component rings. In degree zero it is \(\prod_{n\in\mathbb Z}E\), which is infinite dimensional. Restriction to finitely many components is the product projection and is onto. Each individual component is already stable at its reduced point, in every degree.

**Exercise C.12.4.2 (intermediate).** For \(G=PGL_2\), choose the coweight coordinate \(n\in\mathbb Z\) with \(\langle\alpha,n\rangle=n\). List the dimensions of the cells \(n=-2,-1,0,1,2\) and the classes in which they lie. Why does dimension zero not identify the two components?

**Solution.** The coroot is \(2\), so \(\Pi=\mathbb Z/2\mathbb Z\). Formula (C.12.1) is
\[
 d_I(n)=\max(0,n)+\max(0,-n-1).
\]
The listed dimensions are \(1,0,0,1,2\), respectively; their classes are \(0,1,0,1,0\). Thus both components contain a zero-dimensional cell. In the odd component the point \(n=-1\) is the closed cell of the minimal orbit \(\mathbf P^1\), while its other cell, at \(n=1\), has dimension one. In the even component \(n=0\) is the base point. The locally constant coroot class, not dimension, separates them. Within either class, the inequality \(|n|\le d_I(n)+1\) bounds the coweight labels of cells of bounded dimension.

### C.13. Finite jets, constant-group restriction and actual mapping complexes

The earlier proof inputs are Lesson 1, Theorem 2.C, Lesson 2, Theorem 7.1, and Lesson 5, Lemmas Q.1.1.1-Q.1.2.1. The finite-jet generator enhancement is Theorem A.4.1.1 above. The full quotient schemes and the actual coefficient and mapping-complex comparisons are proved here.

Let \(H_m\) be the algebraic group with
\[
 H_m(R)=G(R[t]/t^{m+1}),\qquad m\ge0,
\]
so \(H_0=G\). Constant loops give a section \(G\to H_m\) of evaluation. We work on a finite \(G(k[[t]])\)-stable closed support \(X\) contained in a full bounded stage \(Y_N\). The quotient-stack notation below denotes the actual action-nerve constructible category, or its finite free-frame models, with the maps of those presentations. The enhancements and coefficient comparisons used in A.4 are retained.

#### C.13.1. The whole finite-jet quotient

**Lemma C.13.1.1.** Evaluation has kernel
\[
 U_m=\ker(H_m\longrightarrow G)\simeq\mathbf A^{m\dim G}
 \tag{C.13.1}
\]
as a scheme, over every parameter algebra. Multiplication identifies \(H_m=U_m\rtimes G\), and right quotient by the constant group identifies \(H_m/G\) with the actual scheme \(U_m\). More generally,
\[
 U_{n,m}=\ker(H_n\longrightarrow H_m)
      \simeq\mathbf A^{(n-m)\dim G}\quad(n\ge m).
 \tag{C.13.2}
\]
The arc action on \(Y_N\), and hence on \(X\), factors through \(H_m\) whenever \(m+1\ge2N\).

**Proof.** The ordered big cell of Lesson 1, Theorem 2.C is a principal open containing the identity, with coordinates
\(U^-TU^+\). Any finite jet equal to the identity modulo \(t\) lies in this open: its defining function has an invertible constant term, hence is invertible modulo \(t^{m+1}\), on every algebra \(R\). Its negative and positive root coordinates are uniquely
\(\sum_{j=1}^m a_{\alpha,j}t^j\). Choose a character basis for the original split torus. Each of its coordinates is uniquely
\[
 1+\sum_{j=1}^m b_{i,j}t^j.
\]
These expressions are units; their inverses are the finite geometric series in the nilpotent ideal \((t)\). Every displayed coefficient is arbitrary in \(R\). There are \(m(|\Phi|+\operatorname{rank}T)=m\dim G\) coefficients. The big-cell multiplication and inverse coordinate maps give (C.13.1) on arbitrary test algebras. This includes every central torus coordinate.

For the kernel in (C.13.2), impose equality to the identity modulo \(t^{m+1}\) instead. Uniqueness of the same big-cell coordinates sets precisely their coefficients of degrees at most \(m\) to zero; their coefficients of degrees \(m+1,\ldots,n\) are arbitrary. This proves (C.13.2), retaining the full kernel schemes.

For \(h\in H_m(R)\), let \(g_0=h(0)\). The unique expression \(h=u g_0\), with \(u=h g_0^{-1}\in U_m(R)\), proves the semidirect product. Under right multiplication by \(a\in G(R)\), the expression \(h h(0)^{-1}\) is unchanged, because \((h a)(h(0)a)^{-1}=h h(0)^{-1}\). Thus it gives the quotient map and its section \(u\mapsto u\), identifying the whole right quotient with \(U_m\).

The map \(G(R[[t]])\to H_m(R)\) is onto. After dividing a given jet by its constant value, its big-cell coordinates have the displayed form. Extend the root polynomials to formal series and the torus coordinates to the same units in \(R[[t]]\). Their product, times the constant value, is a lift. This argument also proves surjectivity \(H_n(R)\to H_m(R)\), by using the same expressions modulo \(t^{n+1}\).

Finally take the faithful matrix embedding and the full lattice bounds from Lesson 2. A matrix \(h=1+t^{m+1}A(t)\), and its inverse, have this congruence form in that embedding. For every bounded lattice \(L\) and every \(\ell\in L\),
\[
 h\ell-\ell\in t^{m+1-N}R[[t]]^{\dim V}
       \subset t^N R[[t]]^{\dim V}\subset L
 \qquad(m+1\ge2N).
\]
Thus \(hL\subset L\), and the inverse inclusion follows from \(h^{-1}\). The associated-lattice closed immersion of the full Grassmannian in Lesson 2 identifies equality of these lattices with equality of the Grassmannian points, on every algebra. The entire congruence kernel therefore acts as identity on the full \(Y_N\), including its nilpotent parameters. Surjectivity onto \(H_m\) makes the action factor through that finite jet group. ∎

#### C.13.2. Restriction to the constant group

**Theorem C.13.2.1.** For an \(H_m\)-action on \(X\), let
\[
 p:[X/G]\longrightarrow[X/H_m]
\]
be induced by inclusion of the constant group. For every constructible coefficient complex \(F\) on the target, its actual ordinary unit is an isomorphism
\[
 F\xrightarrow{\ \sim\ }Rp_*p^*F.
 \tag{C.13.3}
\]
Consequently restriction gives canonical isomorphisms
\[
 \begin{gathered}
 R\Gamma_{H_m}(X,F)\xrightarrow{\sim}R\Gamma_G(X,p^*F),\\
 R\operatorname{Hom}_{H_m}(P,Q)
      \xrightarrow{\sim}R\operatorname{Hom}_G(p^*P,p^*Q).
 \end{gathered}
 \tag{C.13.4}
\]
They preserve units, cup actions, shifts, composition and, for Weil objects, the actual Frobenius operators.

**Proof.** Pull \(p\) back along the smooth action atlas \(X\to[X/H_m]\). The resulting map is
\[
 X\times(H_m/G)\longrightarrow X.
\]
Indeed an isomorphism between two trivial \(H_m\)-torsors is an element \(h\); the equality of their maps to \(X\) determines the second point as \(h^{-1}x\), and its change by a constant \(G\)-element divides \(h\) on the right. Lemma C.13.1.1 identifies this quotient with \(U_m\), an affine space. Thus the pulled-back map is an actual product affine-space projection, and the pulled coefficient is the pullback of \(F|_X\).

Iterate the ordinary affine-line unit of Lesson 5, Lemma Q.1.2.1. Its \(m\dim G\) iterations show that the ordinary unit on this product projection is an isomorphism, for every such pulled coefficient. Ordinary smooth base change, with its actual counit-transpose comparison in Lesson 5, Lemma Q.1.1.1, identifies this map with the pullback of (C.13.3). Smooth descent is conservative on the action presentation: if a cone restricts to zero on its atlas, every level of its cartesian nerve diagram is zero, so the cone is zero. This proves (C.13.3); no nonproper arbitrary-fibre comparison is used.

Apply global sections to its actual unit. Composition of ordinary images identifies the target with \(R\Gamma_G(X,p^*F)\), giving the first map of (C.13.4). For the second, derived adjunction gives
\[
 R\operatorname{Hom}_G(p^*P,p^*Q)
 =
 R\operatorname{Hom}_{H_m}(P,Rp_*p^*Q).
\]
Under this equality the restriction map is precisely the map induced by the unit of \(Q\). Formula (C.13.3) makes it an isomorphism. This argument needs no asserted internal-Hom pullback formula for singular constructible complexes.

Restriction is a functor on the actual coefficient presentations, so it preserves identities, shifts and composition. Pullback preserves multiplication of constant cochains and their action on pulled coefficients, giving the cup and coefficient-ring compatibility. Every map used is an actual unit, pullback, ordinary-image comparison or adjunction, defined over the ground field. If the objects have Weil structures, naturality therefore intertwines those structures and the resulting Frobenius operators. A choice of affine coordinates was used to test the unit, not to define it. ∎

#### C.13.3. Increasing the jet level

**Lemma C.13.3.1.** Suppose the action on \(X\) factors through \(H_m\), and let \(n\ge m\). For the quotient-stack map \(q:[X/H_n]\to[X/H_m]\), the actual unit is an isomorphism
\[
 F\xrightarrow{\ \sim\ }Rq_*q^*F.
 \tag{C.13.5}
\]
Thus increasing a sufficient jet level preserves all mapping complexes between objects defined at that level. In the finite-jet spherical generator enhancement of A.4, the restriction maps in C.13.2 consequently identify the actual \(G(k[[t]])\)-equivariant generator mapping complexes with their constant-\(G\) restrictions.

**Proof.** The kernel \(V=U_{n,m}\) acts trivially on \(X\). Pulling \(q\) back along the action atlas gives \(X\times BV\to X\): a lift of a trivial \(H_m\)-torsor exists as the trivial \(H_n\)-torsor, and its automorphisms over that torsor are exactly \(V\). This describes the entire quotient stack, retaining all its automorphisms.

Every level \(V^s\) of the group nerve is an affine space, by C.13.1.1. For the coefficient pulled from \(X\), the actual ordinary affine-line units give
\[
 F|_X\xrightarrow{\sim}
 R(\operatorname{pr}_X:X\times V^s\to X)_*
                  \operatorname{pr}_X^*(F|_X).
\]
These units commute with faces and degeneracies, since all of those maps preserve the projection to \(X\). The augmented cosimplicial complex of the constant diagrams on the left has identity face and degeneracy maps. Its normalized complex is \(F|_X\) in degree zero and zero in positive simplicial degrees: in degree \(s>0\) a normalized element is in the kernel of a degeneracy which is the identity. The same computation can be made in any bounded coefficient-resolution range and then in the full bounded-below total complex; the affine-space units are quasi-isomorphisms at each level, and the first-quadrant degree filtration makes them a quasi-isomorphism on totalizations. It follows that the ordinary image of the pulled coefficient on \(X\times BV\) is exactly \(F|_X\), with the displayed unit.

Descent on the action atlas, or on the compatible free-frame diagrams of A.1, identifies this comparison with (C.13.5). To spell out the ordinary-image calculation, inverse image of the target atlas computes the fibre groupoid just described; its cartesian nerve has the projections \(X\times V^s\to X\). Ordinary image on that presentation is their cosimplicial totalization. Thus the comparison is a calculation on the actual presentation, not an inference from the cohomology of individual geometric fibres. Conservativity of that presentation proves (C.13.5).

Global sections and the same derived-adjunction argument as in C.13.2 give cohomology and mapping-complex isomorphisms. The composition \(G\to H_n\to H_m\) is the original constant inclusion. Hence these isomorphisms commute with the constant-group restrictions. The generator enhancement of A.4 is formed from these action and coefficient presentations at sufficient jet levels; the units just proved identify its mapping complexes at every larger level with those at the chosen finite level, and then with (C.13.4). All identifications are the actual restriction functors and retain their compositions and Frobenius structures. This proves the stated generator comparison. It does not assert that every \(G\)-equivariant constructible object on \(X\) comes from an \(H_m\)-equivariant object. ∎

#### C.13.4. Two finite-jet exercises

**Exercise C.13.4.1 (basic).** Compute \(U_2\) for \(G=\mathbb G_m\), including its multiplication, over an arbitrary parameter algebra. Explain why its trivial constant cohomology does not mean it is the trivial group scheme.

**Solution.** Its units are \(1+at+bt^2\) modulo \(t^3\). Multiplication is
\[
 (a,b)(a',b')=(a+a',\,b+b'+aa'),
 \qquad
 (a,b)^{-1}=(-a,\,a^2-b).
 \tag{C.13.6}
\]
Thus the scheme is \(\mathbf A^2\), with a genuine group law in every characteristic. Its ordinary constant cohomology is \(E\) by two affine-line units; the relative nerve calculation in C.13.3 makes \(R\Gamma(BU_2,E)=E\). Neither comparison identifies its points or its group law with those of the trivial group. In particular all \(a,b\), including nilpotent parameters, remain in the quotient scheme \(H_2/G\).

**Exercise C.13.4.2 (intermediate).** For \(G=GL_2\), describe \(U_1\) and determine a sufficient jet level for action on a lattice stage with bounds \(t^N O^2\subset L\subset t^{-N}O^2\).

**Solution.** Every point of \(U_1\) is uniquely \(1+tA\) modulo \(t^2\), with \(A\in M_2(R)\); its inverse is \(1-tA\), and the group law is addition of \(A\). Hence \(U_1\) is the four-dimensional additive matrix scheme. For the bounded lattice stage, a congruence \(h=1+t^{m+1}A(t)\) changes any lattice vector by an element of \(t^{m+1-N}O^2\). This is inside \(t^NO^2\subset L\) when \(m+1\ge2N\), and the inverse congruence gives equality of lattices. Therefore \(H_m\) acts for \(m\ge\max(0,2N-1)\). This is a sufficient uniform bound; it is not claimed to be the minimum for each individual lattice.

### C.14. The flag basis and actual torus-to-group comparison

We use the proved invariant-degree identities of Lemma B.1.1.1 above, the actual Euler and trace comparisons of C.5 and Lesson 6 A.1, and the finite-jet comparisons of C.13. The additional commutative-algebra and flag-coordinate proofs are linked at their point of use. Every change-of-group map below is restriction followed by the specified cup action.

Keep the original split connected reductive \(G/k\), with \(k\) algebraically closed, and \(E/\mathbb Q_\ell\) finite, with \(\ell\) invertible in \(k\). Write
\[
 S=\operatorname{Sym}_E(X^*(T)\otimes_{\mathbb Z}E),
 \qquad R=S^W,\qquad N=|\Phi^+|.
\]
A character has polynomial degree one and cohomological degree two. Its Chern class retains its coefficient twist \(E(1)\). Thus a homogeneous class of polynomial degree \(a\) gives the action \(F(-a)[-2a]\to F\). We suppress those lines only when writing graded coefficient rings.

#### C.14.1. The finite coinvariant algebra

**Lemma C.14.1.1.** Choose homogeneous polynomial generators \(f_1,\ldots,f_r\) of \(R\), of polynomial degrees \(d_i\), as in B.1.1.1. Put \(C=S/(f_1,\ldots,f_r)\). Then
\[
 \dim_E C=|W|,\qquad C^{>N}=0,\qquad
 \operatorname{Soc}(C)=C^N\simeq E,
 \quad N=\sum_i(d_i-1).
 \tag{C.14.1}
\]
Every nonzero ideal of \(C\) meets this socle. If \(b_1,\ldots,b_{|W|}\) are homogeneous lifts of an \(E\)-basis of \(C\), then they form an \(R\)-basis of \(S\). They may be chosen with \(b_1=1\).

**Proof.** B.1.1.1 proves polynomiality, the sum of the degrees, and \(\prod_i d_i=|W|\), for this Weyl action including its central fixed space. The polynomial ring \(S\) is finite over \(R\): each coordinate \(x_j\) satisfies the monic orbit polynomial \(\prod_{w\in W}(Z-wx_j)\), whose coefficients are invariant. Reducing powers by these finitely many monic equations expresses \(S\) as a finite \(R\)-module. Hence \(C\) is finite dimensional. Its positive ideal \(\mathfrak n_C\) is nilpotent by its finite positive grading, and \(C/\mathfrak n_C=E\); it is therefore local.

The list \(f_1,\ldots,f_r\) is a system of parameters in \(S_{(x_1,\ldots,x_r)}\). A polynomial ring over a field is Cohen–Macaulay by Regular sequences, depth and Cohen–Macaulay modules, Theorem 5.3. Its Corollary 4.3 proves that this parameter list is regular. It is regular already in the graded polynomial ring: a nonzero homogeneous element of a successive homogeneous quotient stays nonzero on localizing at \((x_1,\ldots,x_r)\). Indeed multiplication by a polynomial with nonzero constant term has nonzero least-degree component on such an element. A homogeneous annihilator in a kernel would consequently contradict local regularity.

The successive multiplication sequences for this regular list give
\[
 \operatorname{Hilb}_C(z)
 =\frac{\prod_i(1-z^{d_i})}{(1-z)^r}
 =\prod_i(1+z+\cdots+z^{d_i-1}).
 \tag{C.14.2}
\]
Its degree is \(N\), its top coefficient is one, and its value at one is \(|W|\).

We also prove that no smaller-degree socle is hidden. The Koszul complex on a regular sequence is a free resolution of its quotient: start with the two-term injective multiplication complex, and tensor the next such complex; its cone has cohomology only the next quotient because the next multiplication is injective. This induction applies to both the coordinate sequence \(x_1,\ldots,x_r\) resolving \(E\), and \(f_1,\ldots,f_r\) resolving \(C\).

Compute their balanced \(\operatorname{Tor}_r^S(E,C)\) using these two resolutions. Equality of the computations follows by taking their finite double tensor complex: resolve one factor first by rows and then the other by columns, using the just proved acyclicity of their free resolutions. In the coordinate Koszul complex tensored with \(C\), its top cycles are precisely the elements of \(\operatorname{Soc}(C)\), with their polynomial degrees increased by \(r\); there is no incoming top boundary. In the \(f\)-Koszul complex tensored with \(E\), every differential is zero because every \(f_i\) has positive degree. Its top term is one line of polynomial degree \(\sum_i d_i=N+r\). Thus the socle is exactly one line in degree \(N\), proving (C.14.1).

Every nonzero ideal meets it. Given a nonzero element in that ideal, take the largest power of the nilpotent maximal ideal whose product with the generated ideal is nonzero. Any nonzero element of that product is killed by the maximal ideal and belongs to the socle.

Finally the lifts \(b_j\) generate \(S\) over \(R\) by induction on polynomial degree: reduce an element modulo \((f_i)\) in the chosen basis, and express the remainder as \(\sum_i f_i a_i\), with each \(a_i\) of smaller degree. The free graded \(R\)-module on these lifts has Hilbert series
\(\operatorname{Hilb}_R(z)\operatorname{Hilb}_C(z)=\operatorname{Hilb}_S(z)\), by (C.14.2). The resulting surjection is a bijection in each finite dimensional homogeneous degree. It is therefore the required free basis. The unique degree-zero basis class is one. All these arguments include the torus case, where the \(d_i\) are one and \(C=E\). ∎

#### C.14.2. Chern classes on the flag variety

Let \(F=G/B\). Use the associated line convention
\[
 \mathcal L_\chi=G\times^B k_\chi,\qquad
 (g,z)\cdot b=(gb,\chi(b)^{-1}z).
\]
At \(n_wB\) its \(T\)-character is \(w\chi\). The root-coordinate Bruhat proof in Root data and Weyl groups, Theorems 6.2 and 8.1, and the smooth projective quotient of The flag scheme and the Weyl group, Theorem 1.1, give a closed affine paving of \(F\) indexed by \(W\), and the \(T\)-fixed points \(n_wB\). Its tangent characters there are \(-w\alpha\), for \(\alpha>0\). Put \(\delta=\prod_{\alpha>0}(-\alpha)\in S^N\).

**Theorem C.14.2.1.** The actual Chern map gives an isomorphism
\[
 C\xrightarrow{\sim}H^*(F,E),\qquad
 [\chi]\longmapsto c_1(\mathcal L_\chi).
 \tag{C.14.3}
\]
The class \(c(\delta)\) has trace \(|W|\), with coefficient line \(E(N)\). In particular the images \(c(b_j)\) of C.14.1 form a homogeneous basis of flag cohomology.

**Proof.** Bruhat root coordinates are linear for the constant torus and have nonzero weights. The closed-cell trace induction of C.12.3 proves that \(H_T^*(F,E)\) is finite free over \(S\), in even degrees. The same induction without the torus proves that ordinary flag cohomology has one generator for each cell, in its compact degree \(2d\), with twist \(-d\).

The actual forgetful restriction gives
\[
 H_T^*(F,E)\otimes_S E\xrightarrow{\sim}H^*(F,E).
 \tag{C.14.4}
\]
Here is the comparison, rather than a general assertion that base change commutes with Hom. At each finite torus model choose a point of \(B_m\) with a frame; pulling back gives \(F\). On each cell the compact trace comparison is \(S(-d)[-2d]\to E(-d)[-2d]\), so is exactly augmentation of its coefficient ring. The compact cell rows are short exact with free cell quotient, both equivariantly and ordinarily. Tensoring the former with \(E\) remains exact because that quotient is free. Induction in the comparison of these rows proves (C.14.4), with its actual pullback. It also proves multiplicativity, since pullback of constants preserves cup product.

For any homogeneous \(f\in R\), the equivariant Chern class \(c_T(f)\) restricts at \(n_wB\) to \(w(f)=f\). The base class \(f\in S\) has those same restrictions. C.5.2.1 says that their difference is zero after localization. Freeness over the polynomial domain \(S\) says that a class killed by a nonzero denominator is zero already. Thus
\[
 c_T(f)=\pi^*f.
 \tag{C.14.5}
\]
When \(f\) has positive degree, (C.14.4) sends the right side to zero. This proves that the ordinary Chern map factors through \(C\).

Compute the trace of \(c(\delta)\) with its actual orientation. At a fixed point \(p=n_wB\), a translated root chart is an affine neighbourhood with coordinate tangent characters \(-w\alpha\). Compose its coordinate zero-section comparisons from Lesson 6, A.1.1.1–A.1.2.1. The supported point class has restriction
\[
 e_p=\prod_{\alpha>0}(-w\alpha)=w\delta
\]
at \(p\), and zero restriction at the other fixed points. Its structural trace is one by composition of the section and structural trace counits. After inverting \(S\setminus0\), C.5.2.1 therefore expresses any equivariant class \(a\) as the sum of these supported point classes with coefficients \(a|_p/e_p\). Applying trace gives
\[
 \int_F a=\sum_{w\in W}\frac{a|_{n_wB}}{w\delta}.
 \tag{C.14.6}
\]
This identity is in the localized coefficient ring and retains the twists; the supported classes, self-intersections and trace defined it. For \(a=c_T(\delta)\), every fraction is one. Its degree-normalized trace is consequently \(|W|\). The trace is constant in degree zero, so its localized equality is its integral equality. Forgetful pullback and trace compatibility give the same number for \(c(\delta)\). It is nonzero in \(E\), regardless of the geometric characteristic.

Thus \([\delta]\) is nonzero in \(C^N\), and generates its socle by C.14.1. If the Chern map had a nonzero kernel ideal, that ideal would meet this socle and would kill \(c(\delta)\), which has nonzero trace. Its kernel is therefore zero. Both sides of (C.14.3) have dimension \(|W|\), the right side by its closed affine paving. The map is onto as well. ∎

#### C.14.3. Relative flag decomposition and restriction

For a finite-type \(G\)-scheme \(X\) and actual equivariant bounded constructible complexes, write \(\operatorname{res}\) for restriction of the action presentation to \(T\). Cohomology of quotient stacks is computed in fixed ranges by the actual free frames of A.1. Write \(a_j=\deg b_j\).

**Theorem C.14.3.1.** Actual restriction identifies \(H_G^*(\mathrm{pt},E)\) with \(R=S^W\). For every \(G\)-equivariant \(F,P,Q\) on \(X\), the maps
\[
 \begin{gathered}
 H_G^*(X,F)\otimes_R S
       \xrightarrow{\sim}H_T^*(X,\operatorname{res}F),\\
 \operatorname{Ext}_G^*(P,Q)\otimes_R S
       \xrightarrow{\sim}
       \operatorname{Ext}_T^*(\operatorname{res}P,\operatorname{res}Q)
 \end{gathered}
 \tag{C.14.7}
\]
send \(x\otimes s\) to \(s\cup\operatorname{res}(x)\). They retain the shifts and coefficient twists specified above. The Ext comparison preserves identities and Yoneda composition under this scalar extension.

**Proof.** First compare \(T\subset B\). Ordered root coordinates identify \(B/T\) with the full affine scheme of the unipotent radical. On a smooth action atlas, the map \([X/T]\to[X/B]\) is the product projection with this fibre. The iterated ordinary affine-line unit and Lemma Q.1.1.1, followed by conservative descent on the atlas, give the actual unit isomorphism, exactly as in C.13.2. This proves the corresponding cohomology and mapping-complex comparisons by adjunction. It keeps the action presentations, rather than replacing them by an arbitrary fibre calculation.

Now consider the proper smooth flag map
\[
 p:[X/B]\longrightarrow[X/G].
\]
Its pullback to the action atlas is \(X\times F\to X\). On \([X/B]\) the character lines from \(BB\) give the actual classes \(c(b_j)\). Compose the adjunction unit of a target coefficient \(K\) with cup action by these classes to define
\[
 \Phi_K:
 \bigoplus_j K(-a_j)[-2a_j]\longrightarrow Rp_*p^*K.
 \tag{C.14.8}
\]
On the atlas, proper base change and projection identify the target with \(K|_X\otimes R\Gamma(F,E)\). The pulled classes are the flag classes of C.14.2.1, so their basis makes this displayed map an isomorphism. One can verify the product coefficient identity by the same compact-cell trace filtration used in C.14.4; its arrows are the proper pullback and projection comparisons. Conservativity on the action atlas proves (C.14.8) globally. In particular this decomposition concerns the actual unit and global character classes, not only the fibre dimensions.

Apply global sections for cohomology. For mapping complexes use derived adjunction:
\[
 R\operatorname{Hom}_B(p^*P,p^*Q)
 =R\operatorname{Hom}_G(P,Rp_*p^*Q).
\]
Inserting (C.14.8) gives the direct sum of the shifted and twisted \(G\)-mapping complexes. Its \(j\)-th map is cup action by \(b_j\) after actual restriction. No internal-Hom pullback formula is needed.

It remains to identify the coefficient ring used in (C.14.7). Apply this decomposition with \(X=\mathrm{pt}\). Since \(b_1=1\), the actual map \(H_G^*(\mathrm{pt})\to S\) is injective: it is the first summand of the resulting basis decomposition. Its image lies in \(S^W\). Indeed, on a common free \(G\)-frame the right action of \(N_G(T)\) on the quotient by \(T\) preserves its projection to the quotient by \(G\); it factors through \(W\) and transforms character lines by the Weyl action. Pullback from the quotient by \(G\) is invariant under these actual maps.

The flag decomposition and (C.14.2) give, degree by degree,
\[
 \operatorname{Hilb}_{H_G^*(\mathrm{pt})}(z)
 =\frac{\operatorname{Hilb}_{S}(z)}
        {\sum_j z^{a_j}}
 =\prod_i(1-z^{d_i})^{-1}
 =\operatorname{Hilb}_{R}(z).
 \tag{C.14.9}
\]
There are no odd groups: a degree-zero basis summand would otherwise produce an odd group in \(S\), which has none. The same summand proves finiteness of every degree. Thus the invariant inclusion has equal dimensions in each degree and is onto \(R\). It is a ring map, so identifies the coefficient rings multiplicatively.

Lemma C.14.1.1 makes \(S=\bigoplus_j Rb_j\). Therefore the cohomology and Ext direct-sum comparisons just constructed are precisely (C.14.7). Restriction is an actual functor and cup coefficients have even degrees, so
\[
 (s\cup\operatorname{res}u)\circ
 (t\cup\operatorname{res}v)
 =st\cup\operatorname{res}(u\circ v).
 \tag{C.14.10}
\]
There is no odd coefficient sign. Identities map to identities. This proves the asserted composition compatibility; it does not claim a monoidal enhancement from graded Ext alone. All maps are defined over the ground field and intertwine Weil structures when supplied. ∎

#### C.14.4. Weyl descent of actual morphisms

Let \(A_G=H_G^*(X,E)\), \(A_T=H_T^*(X,E)\), and \(M_G=H_G^*(X,P)\), \(N_G=H_G^*(X,Q)\). The actual \(G\)-equivariances give a Weyl action on their torus restrictions: representatives in the normalizer conjugate the torus action, and the action cocycle identifies the pulled coefficients. Representatives differing by \(T\) give the same map on equivariant cohomology and Ext, by that cocycle. These are semilinear actions over \(S\).

**Corollary C.14.4.1.** These actions yield
\[
 \begin{gathered}
 \operatorname{Ext}_G^*(P,Q)
       =\operatorname{Ext}_T^*(\operatorname{res}P,\operatorname{res}Q)^W,\\
 \operatorname{Hom}_{A_G}^*(M_G,N_G)
       =\operatorname{Hom}_{A_T}^*(M_G\otimes_R S,N_G\otimes_R S)^W.
 \end{gathered}
 \tag{C.14.11}
\]
The maps are actual restriction and scalar extension, and retain composition. If the comparison of C.10 holds for the torus restrictions of \(P,Q\) on \(X\), it therefore holds for their \(G\)-equivariant Ext and \(A_G\)-module Hom. For a sufficiently large finite jet action, C.13 gives the same assertion for the original spherical generator Ext.

**Proof.** C.14.3 identifies each torus group with scalar extension from \(R\), and identifies \(A_T=A_G\otimes_R S\) as rings: the multiplication comparison is the restriction and cup map. Under these identifications \(W\) acts trivially on the \(G\)-factor and ordinarily on \(S\), since all restricted classes came from a \(G\)-presentation.

For every \(R\)-module \(L\), the invariant part of \(L\otimes_R S\) is exactly \(L\). To prove this without a flat Hom-base-change assertion, average the \(W\)-action using \(|W|^{-1}\sum_w w\). This projector is \(R\)-linear on \(S\) with image \(R\), and is the identity on that submodule. On \(L\otimes_R S\) its image is therefore \(L\otimes_R R=L\); this inclusion is injective because the same projector splits it. Apply this first to the Ext scalar extension to get the first equation.

For an \(A_T\)-linear invariant map \(h\) in the second line, \(h(m\otimes1)\) is invariant and hence belongs to the canonically embedded \(N_G\). It defines a homogeneous map \(h_0:M_G\to N_G\). Applying the actual restriction of each \(a\in A_G\) proves \(h_0\) is \(A_G\)-linear. Every other value of \(h\) is determined by \(S\)-linearity:
\(h(m\otimes s)=s\,h_0(m)\). Conversely scalar extension of an \(A_G\)-linear map gives such an invariant \(A_T\)-linear map. These inverse constructions preserve composition. They require neither projectivity of \(M_G\) nor a claim that arbitrary Hom commutes with specialization.

Finally the cohomology comparison map of C.10 is natural under these normalizer maps, because it applies actual cohomology to actual morphisms. Its Weyl invariants therefore give the comparison of the first and second lines of (C.14.11). The finite-jet and constant-group restriction of C.13 identifies the original generator Ext with this one, preserving the coefficient action and composition. The hypotheses of C.10, including its stalk-surjectivity requirement, remain required. ∎



**Corollary C.14.4.2.** On the full Grassmannian, constant cohomology satisfies
\[
 H_G^*(\operatorname{Gr}_G,E)\otimes_R S
       \xrightarrow{\sim}H_T^*(\operatorname{Gr}_G,E).
 \tag{C.14.12}
\]
For every finite closed \(G(k[[t]])\)-stable support \(X\) whose reduction is a union of Iwahori cells, actual restriction \(H_G^*(\operatorname{Gr}_G)\to H_G^*(X)\) is onto. The comparison of C.10, when its stalk hypotheses hold, therefore identifies the original spherical generator Ext with module Hom over the whole \(G\)-equivariant Grassmannian ring.

**Proof.** Use the original full bounded stages \(Y_N\); they are \(G\)-stable by the matrix-bound argument of C.12.2. C.14.3 applies at every such stage and commutes with its restriction maps. Its decomposition has the fixed finite basis \(b_j\), independent of \(N\). Finite direct sums and fixed shifts commute with the two products and their fibre in the derived compatible-section model (C.12.8). Thus the same flag decomposition holds for derived compatible sections on the full bounded presentation. The canonical cohomology map gives (C.14.12), with the same actual cup products and Weyl action.

Under this comparison \(W\) acts on the scalar factor \(S\) alone. Averaging as in C.14.4 identifies its invariants with \(H_G^*(\operatorname{Gr}_G)\), also for degreewise products over all components. The restriction in C.12.3 is a Weyl-equivariant surjection for this \(G\)-stable \(X\). Given an invariant target class, lift it by that surjection and average the lift; the averaged class is an invariant lift. Hence the \(G\)-restriction is onto. Reduction and the actual closed-restriction unit retain the assertion for the stated nilpotent support structures.

Consequently an \(H_G^*(X)\)-module map between supported cohomology modules is exactly a map linear over the whole ring: lift each homogeneous support class through the surjection, as in C.12.3.2. Combine this equality with C.14.4.1 and the actual jet comparison of C.13. The result retains composition and the original group and components. The unconditional stalk-surjectivity input, geometric identification of these modules with Appendix B, and enhanced convolution remain separate requirements. ∎

#### C.14.5. Two change-of-group exercises

**Exercise C.14.5.1 (basic).** For the rank-one Weyl action \(u\mapsto-u\) compute \(R,C\), a free \(R\)-basis of \(S\), and the invariant part of \(L\otimes_R S\) for an arbitrary \(R\)-module \(L\).

**Solution.** With polynomial degree \(|u|=1\), \(S=E[u]\), \(R=E[u^2]\), \(C=E[u]/(u^2)\), and \(S=R\oplus Ru\). Thus \(L\otimes_R S=L\oplus Lu\); its Weyl action is \((a,b)\mapsto(a,-b)\). Since two is invertible in \(E\), its invariants are exactly the first copy \(L\), including when \(L\) has \(u^2\)-torsion. The quotient \(C\) has its one-dimensional socle generated by \(u\). This verifies both the free basis and the averaging argument without a torsion-free hypothesis on \(L\).

**Exercise C.14.5.2 (intermediate).** For \(G=SL_2\), let \(\chi(\operatorname{diag}(z,z^{-1}))=z\) and \(u=c_1(\chi)\). Determine the sign of \(\mathcal L_\chi\) on \(G/B=\mathbf P^1\) in our associated-line convention, and check the tangent-root trace.

**Solution.** The upper Borel fixes the line spanned by \(e_1\). The map \([g,z]\mapsto z\,ge_1\) identifies \(\mathcal L_\chi\) with the tautological line: replacing \((g,z)\) by \((gb,\chi(b)^{-1}z)\) leaves that vector unchanged. Therefore \(c(u)=-h\), where \(h=c_1(\mathcal O(1))\) has trace one. The positive root is \(\alpha=2\chi\), and \(\delta=-\alpha=-2u\); hence \(c(\delta)=2h\), with trace \(2=|W|\). At the two fixed points the tangent Euler classes are \(-2u\) and \(2u\), respectively. Formula (C.14.6) for \(c_T(\delta)\) sums two fractions equal to one. This checks the sign and also retains the nonprimitive integral root character.

### C.15. Relative tame boundary comparison with complete coefficients

Let \(Y_0\) be smooth and integral over a finite field of characteristic \(p\), let \(p_0:\overline X_0\to Y_0\) be a smooth proper curve, and let \(D_0\subset\overline X_0\) be a Cartier divisor finite étale over \(Y_0\). Write \(j:U_0=\overline X_0\setminus D_0\hookrightarrow\overline X_0\) and \(i:D_0\hookrightarrow\overline X_0\). Fix a finite extension \(E/\mathbb Q_\ell\), with \(\ell\ne p\), valuation ring \(O\), and uniformizer \(\pi\). Let \(L\) be a lisse \(E\)-sheaf of rank \(r\ge1\). Tameness means that the finite reductions of a stable lattice are tame at the generic boundary DVRs. All comparisons below concern the actual ordinary extension \(j_*L=\mathcal H^0Rj_*L\).

The local finite-cover input has a complete earlier proof: Specialization and tame ramification, Theorem 2.3, identifies tame covers along a regular Cartier divisor with finite Kummer covers after passage to a strict local scheme. The coefficient inputs are The pro-étale site and l-adic complexes, Theorem 7.10 and Corollary 7.11, and Semi-infinite geometry and MV weight functors, M.6.2.1 and O.2.1.1. Their completed pullback and ordinary-image proofs retain the actual coefficient comparisons. We use them rather than commuting an infinite inverse limit with an ordinary étale stalk.

#### C.15.1. The boundary invariant and its geometric fibre

**Lemma C.15.1.1.** The actual restriction comparison
\[
 (j_*L)|_{\overline X_{\bar y}}
       \longrightarrow j_{\bar y,*}(L|_{U_{\bar y}})
 \tag{C.15.1}
\]
is an isomorphism for every geometric \(\bar y\to Y_0\). At a geometric point \(d\) of the boundary its completed fibre is \(V^{I_d}\), where \(V\) is the local fibre of \(L\) and \(I_d\) is tame inertia. This statement uses the full \(E\)-system.

**Proof.** Locally along \(D_0\) there is a relative parameter \(z\) with \(D_0=(z)\). Indeed, trivialize its Cartier ideal near a point. Since \(D_0\to Y_0\) is étale, the image of \(dz\) generates the relative cotangent line along \(D_0\). After restricting to a smaller open, \((p_0,z)\) is étale over \(\mathbb A^1_{Y_0}\): the differential is invertible and both sides are smooth of the same relative dimension. Thus \(z\) has valuation one also on each geometric curve fibre.

The total space and divisor are regular. For the strict henselization \(A\) at \(d\), Theorem 2.3 just cited says that every finite tame cover of \(\operatorname{Spec}A[1/z]\) is a disjoint union of
\[
 \operatorname{Spec}A[1/z,t]/(t^m-z),\qquad (m,p)=1.
 \tag{C.15.2}
\]
Each displayed cover is connected: the valuation at the prime \((z)\) gives the degree \(m\) root-uniformizer calculation in that theorem. Its automorphisms are \(t\mapsto\zeta t\), for \(\zeta\in\mu_m(A)\); strict henselianity supplies these roots of unity. A common multiple of two exponents dominates both covers. Maps and automorphisms are determined by these root equations, so this describes the finite tame cover category, including its morphisms. Its pointed automorphism group is
\(I_d=\varprojlim_{(m,p)=1}\mu_m=\widehat{\mathbb Z}^{(p')}(1)\).

Pull the equations to the strict local curve at the same geometric point. They remain connected Kummer covers of exactly degree \(m\), because the pulled parameter still has valuation one. The same description supplies every finite tame cover there and the same root maps between covers. Consequently restriction induces the identical tame inertia group and the identical action on every pulled finite coefficient fibre. This assertion applies to the entire compatible tower; no single finite cover is asserted to trivialize that tower.

There is a global stable lattice on each connected component of \(U_0\). Indeed \(U_0\) is smooth and hence geometrically unibranch. The cited Corollary 7.11 identifies its coefficient representation with a continuous representation of the profinite étale fundamental group. Its image is compact. The translates of a basis lattice lie in one larger lattice by compactness, and their \(O\)-span is a finite torsion-free \(O\)-module containing the starting lattice. It is a stable lattice. Let \(M\) be its local fibre and \(M_n=M/\pi^nM\).

Finite ordinary extension at \(d\) has degree-zero fibre \(M_n^{I_d}\). To see this directly, a finite section on the punctured strict local scheme is exactly a fibre vector fixed by the finite covering action. The Kummer comparison therefore identifies this fibre and its restriction to the curve fibre, with the actual restriction map.

Now apply O.2.1.1 to the lattice sheaf and M.6.2.1 to its geometric-point pullback. The complete fibre of its ordinary derived image is the coherent derived limit of the finite derived-image fibres. They are in degrees \(\ge0\); hence the degree-zero Milnor sequence has zero \(\varprojlim^1\mathcal H^{-1}\) term and gives
\[
 \mathcal H^0(d_O^*Rj_*L_O)
       =\varprojlim_n M_n^{I_d}
       =M^{I_d}.
 \tag{C.15.3}
\]
The last equality follows because compatible fixed vectors are precisely fixed vectors in \(M=\varprojlim_nM_n\). It is an inverse-limit assertion, not an assertion about reduction of \(M^{I_d}\).

Here \(d_O^*\) denotes actual completed ringed pullback; degree-zero cohomology is taken after that pullback. Actual rational ordinary image and actual rational pullback are the localizations of these integral constructions, by O.2.1.1 and M.6.2.2. Localization is exact. Choose a dense tame generator \(\tau\), and let \(T\) act on \(M\). Continuity makes invariance under \(\tau\) equivalent to invariance under \(I_d\), since the stabilizer equation is closed. Thus
\[
 M^{I_d}\otimes_O E
   =\ker(T-1:M\to M)\otimes_O E
   =\ker(T-1:V\to V)=V^{I_d}.
 \tag{C.15.4}
\]
Finite-level restriction was the same Kummer action, so its coherent limit and localization identify the actual map (C.15.1) with the identity on this invariant fibre. On the open curve it is already the identity. Ordinary rational inverse image is exact on constructible sheaves. On a lisse stratum the locally free \(E\)-coefficient model pulls back to the same degree-zero model. The finite closed-open filtration and the actual identities \(g^*i_*=i'_*g^*\), \(g^*j_!=j'_!g^*\) of M.6.1.2 extend this conclusion to the entire constructible sheaf, because those extensions and finite extensions of sheaves are exact. Closed restriction also has the coefficient identity M.3.4. Geometric fibres detect an isomorphism, using this finite stratal coefficient description. Therefore (C.15.1) is an isomorphism of ordinary sheaves. ∎

#### C.15.2. A finite logarithmic coefficient

On \(\mathbb G_m\) define a rank-\(n\) logarithmic system \(\operatorname{Log}_n\) with basis \(e_0,\ldots,e_{n-1}\) and \(Je_i=e_{i-1}\), \(Je_0=0\). Its tame inertia action is
\[
 a\longmapsto\exp(aJ),\qquad a\in\mathbb Z_\ell(1),
 \tag{C.15.5}
\]
after choosing a generator of the Tate line. The remaining prime-to-\(p\) inertia factors act trivially.

This is an actual complete coefficient system. The basis \(l_i=i!e_i\) is an \(O\)-lattice, and
\[
 \exp(aJ)l_i=\sum_{k=0}^{i}\binom{i}{k}a^k l_{i-k}.
 \tag{C.15.6}
\]
Its matrices are integral and continuous, so every finite reduction is a finite continuous action. The compatible \(\ell\)-power root covers of the coordinate construct this action geometrically. The integral classification in Theorem 7.10 and completion of its finite reductions construct the lattice sheaf; rationalization gives \(\operatorname{Log}_n\).

There is a Weil structure with geometric Frobenius \(Fe_i=q^ie_i\). For completeness, the root covers based at the section \(1\in\mathbb G_m\) give the Kummer quotient of its arithmetic fundamental group. Its geometric subgroup is \(\widehat{\mathbb Z}^{(p')}(1)\), and the section splits the projection to \(\widehat{\mathbb Z}\). Arithmetic Frobenius acts on roots of unity by \(q\), so geometric Frobenius conjugates inertia by \(q^{-1}\). The diagonal action just defined has \(FJF^{-1}=q^{-1}J\) and therefore respects that semidirect-product relation. It extends continuously to the arithmetic group: \(q\) is an \(\ell\)-adic unit, so its integer powers have finite images in every congruence quotient and extend to \(\widehat{\mathbb Z}\). This also proves continuity on the integral lattice (C.15.6). Thus \(J:\operatorname{Log}_n\to\operatorname{Log}_n(-1)\) is an actual Weil morphism. The inclusions \(e_i\mapsto e_i\) give compatible inclusions \(\operatorname{Log}_n\hookrightarrow\operatorname{Log}_{n+1}\).

On a parameter chart, pull this system back by \(z\) and put
\[
 B_n=\mathcal H^0i^*Rj_*(L\otimes z^*\operatorname{Log}_n),
 \qquad \mathcal N=-1\otimes J:B_n\to B_n(-1).
 \tag{C.15.7}
\]
These are constructible rational sheaves and actual morphisms by O.2.1.1 and M.6. In particular \(B_1=i^*j_*L=:B\).

**Lemma C.15.2.1.** If \(n\ge r\), the completed geometric fibre of \(B_n\) is the generalized eigenvalue-one part \(V_1\) of tame monodromy on \(V\). Under this identification \(\mathcal N\) is \(N=\log(T|_{V_1})\), with its Tate twist. The actual inclusion \(B\hookrightarrow B_n\) identifies \(B\) with \(\ker\mathcal N\). These identifications commute with geometric curve fibres, inclusions in \(n\), and Frobenius.

**Proof.** Normalize the chosen \(\ell\)-component of \(\tau\) to one. Lemma C.15.1.1 applied to the tensor coefficient gives the fibre
\(\ker(T\otimes\exp J-1)\). The primary decomposition for the polynomial \(T\) separates \(V_1=\ker(T-1)^r\) from its complementary primary parts. On each other part, after a finite splitting field, the eigenvalues of \(T\otimes\exp J\) are the eigenvalues of \(T\), none equal to one. Its difference from one is invertible there, and faithful scalar extension proves that the invariant kernel has no such part over \(E\).

On \(V_1\) the finite logarithm \(N=\log T\) is nilpotent, with \(N^r=0\), and
\[
 T\otimes\exp J=\exp(N\otimes1+1\otimes J).
\]
For a nilpotent operator \(A\), \(\exp A-1=A\,h(A)\), where \(h(0)=1\); the polynomial \(h(A)\) is invertible by a finite geometric series. Hence the required kernel is \(\ker(N\otimes1+1\otimes J)\).

There is an explicit inverse pair
\[
 \Psi_n:V_1\xrightarrow{\sim}(B_n)_d^{\mathrm{comp}},
 \qquad
 \Psi_n(v)=\sum_{i=0}^{n-1}(-N)^iv\otimes e_i,
 \tag{C.15.8}
\]
and extraction of the coefficient of \(e_0\). Indeed a tensor \(\sum v_i\otimes e_i\) is in the kernel exactly when \(Nv_i+v_{i+1}=0\) for \(i<n-1\) and \(Nv_{n-1}=0\). These equations determine all coefficients from \(v_0\), and the last equation is automatic for \(n\ge r\). The formulas also show that the inclusion for \(n\to n+1\) is an isomorphism on these kernels: its last new coefficient is \((-N)^nv=0\).

The coefficient of \(e_0\) in \(-1\otimes J\) applied to (C.15.8) is \(-v_1=Nv\). Thus \(\mathcal N\) corresponds to \(N\). Its kernel consists exactly of tensors \(v\otimes e_0\) with \(Nv=0\); this is the actual map from \(B_1\). Equality of the completed fibres proves the claimed sheaf kernel identity. The logarithmic system is tame, so C.15.1.1 applies to it and gives the geometric fibre compatibility of all these actual maps.

At a closed boundary point of residue cardinality \(q_d\), Frobenius preserves \(V_1\). Conjugation acts on tame inertia by its invertible \(q_d^{-1}\)-power automorphism; it therefore preserves the subrepresentation on which inertia is unipotent. Taking the finite logarithm there gives \(FNF^{-1}=q_d^{-1}N\). The logarithmic coefficient has \(Fe_i=q_d^ie_i\). Consequently
\[
 F\Psi_n(v)=\sum_i(-q_d^{-1}N)^iFv\otimes q_d^ie_i
           =\Psi_n(Fv).
 \tag{C.15.9}
\]
This verifies the Frobenius action and the sign in (C.15.7). No semisimplicity of Frobenius and no finite cover killing all the monodromy of \(L\) were assumed. ∎

#### C.15.3. Actual monodromy subsheaves after one base restriction

**Theorem C.15.3.1.** After replacing \(Y_0\) by a dense open, \(B=i^*j_*L\) is lisse and has a finite increasing filtration by actual lisse subsheaves whose completed geometric fibres are the monodromy filtration induced on \(V^{I_d}\), centred at zero on the unipotent part \(V_1\). Its formation commutes with geometric curve fibres. For a Weil \(L\), the filtration is Frobenius stable. Thus both relative comparisons required in Weights, purity and semisimplicity over finite fields, Appendix D, Lemma D2, hold for this tame curve family on that dense open.

**Proof.** Cover the boundary by finitely many parameter opens of \(\overline X_0\), as in C.15.1. On each boundary open the single sheaf \(B_r\) of C.15.7 is constructible. Choose a dense open in each of its irreducible components on which it is lisse; this is the finite stratification in the definition of rational constructibility. The closure in \(D_0\) of each discarded subset contains no generic point of a component of \(D_0\). There are only finitely many charts. Since \(D_0\to Y_0\) is finite, the images of these closures are closed; they omit the generic point of \(Y_0\), because a proper closed subset of a finite dominant component cannot dominate an integral base. Delete their finite union from \(Y_0\). Every \(B_r\) on the restricted charts is now lisse.

An actual morphism between two lisse finite-dimensional \(E\)-systems is locally its fixed coefficient matrix. Its kernel and image are lisse systems: they are the corresponding invariant subspaces under the local representation, and the representation classification constructs their inclusions and quotient. Exactness on fibres follows from exact linear algebra over \(E\). Apply this to \(\mathcal N\) and its powers, retaining Tate twists. Lemma C.15.2.1 identifies \(B=\ker\mathcal N\), so \(B\) is lisse as well.

For \(k\le0\) define on such a chart
\[
 B_{\le k}
   =\ker\mathcal N\ \cap\
       \operatorname{im}\bigl(\mathcal N^{-k}(-k):
                         B_r(-k)\longrightarrow B_r\bigr);
 \qquad B_{\le k}=B\quad(k\ge0).
 \tag{C.15.10}
\]
The superscript is the nonnegative integer power \(-k\); the parenthesized twist brings its target back to \(B_r\). These are actual lisse subsheaves of the same \(B\). They are zero for \(k<-(r-1)\), so only finitely many terms differ. Kernels, images and intersections are exact on the lisse fibres, and C.15.2.1 identifies their fibres with
\[
 \ker N\cap\operatorname{im}N^{-k}\quad(k\le0).
 \tag{C.15.11}
\]

Here is the linear algebra identifying this filtration. For a nilpotent \(N\), set
\[
 M_kV_1=
  \sum_{a=0}^{r-1}
       \bigl(\ker N^{a+1}\cap\operatorname{im}N^{a-k}\bigr),
 \tag{C.15.12}
\]
where an image with exponent \(\le0\) means the whole space. Kernels and images make this formula independent of a choice of Jordan basis. On a chain \(v_0,\ldots,v_{h-1}\) with \(Nv_i=v_{i-1}\), its term indexed by \(a\) is spanned by
\[
 v_0,\ldots,v_{\min(a,h-1-\max(a-k,0))},
\]
with the term zero when this upper index is negative. Maximizing this upper index shows that \(v_i\) enters exactly when \(2i-(h-1)\le k\). Thus the successive chain grades are \(-(h-1),-(h-3),\ldots,h-1\). It follows directly that \(NM_k\subset M_{k-2}\), and \(N^b\) takes the grade-\(b\) vectors bijectively to the grade-\(-b\) vectors, with the twist \((-b)\). This is the centred monodromy filtration of Appendix A of the weights lesson, written with the convention for negative exponents.

The invariant part of this chain is its bottom line \(Ev_0\), of grade \(-(h-1)\). It belongs to \(\operatorname{im}N^{-k}\) precisely when \(h-1\ge -k\). Taking direct sums of the chains proves
\[
 M_kV_1\cap\ker N=
 \begin{cases}
  \ker N\cap\operatorname{im}N^{-k},&k\le0,\\
  \ker N,&k\ge0.
 \end{cases}
 \tag{C.15.13}
\]
Consequently (C.15.10) has exactly the required invariant monodromy fibres. Possible non-unipotent primary parts contribute no invariant vectors by C.15.2.

It remains to glue the chart constructions. Two equations for the same regular divisor differ by a unit: \(z'=uz\). On a strict local scheme every prime-to-\(p\) root cover of \(u\) is finite étale and splits. Compatible roots can be chosen successively for the \(\ell\)-power tower. Therefore its Kummer character is trivial on local inertia. The character of \(z'\) and that of \(z\) have the same valuation-one inertia character. Different choices of fibre frame conjugate the monodromy matrix; changing the Tate generator rescales \(N\) by a nonzero scalar. Neither operation changes the intrinsic subspace \(M_kV_1\cap V^{I_d}\). Both chart constructions are subsheaves of the actual common sheaf \(B\), with these same subspaces in every completed geometric fibre. On a common lisse trivializing cover their inclusions are the same subspaces in a constant coefficient module. Hence the subsheaves agree on overlaps and glue uniquely.

The same matrix argument, together with the actual comparison C.15.1 and the tensor comparison C.15.2, proves that these subsheaves restrict to the corresponding filtration on every geometric curve fibre. The operators are Weil morphisms with their twists, and Frobenius scales \(N\) by \(q_d^{-1}\). Their kernels and images, and therefore the glued filtration, are Frobenius stable.

Lemma C.15.1 proves the first comparison in weights Appendix D, and the actual finite filtration just constructed proves its second comparison. This supplies that relative tame input. The compact-support estimate additionally requires the other pointwise weight and induction inputs of that lemma; C.9 continues to state its weight hypothesis. ∎

#### C.15.4. Two complete-coefficient exercises

**Exercise C.15.4.1 (basic).** On a geometric base of characteristic different from \(3\), let a tame pro-\(3\) generator act on \(M=\mathbb Z_3\) by \(T=4\). Compare \(M^I/3M^I\) and \((M/3M)^I\), and compute the compatible inverse limit of all the finite invariant modules.

**Solution.** The action \(a\mapsto4^a\) on \(\mathbb Z_3\) is continuous for \(a\in\mathbb Z_3\), since \(4=1+3\); its finite reductions are finite Kummer actions. Invariance on \(M\) is \(3v=0\), so \(M^I=0\). Modulo \(3\), the action is the identity, and \((M/3M)^I=\mathbb F_3\). These two modules therefore differ. At level \(3^n\), the invariant vectors are the multiples of \(3^{n-1}\). The transition from level \(n+1\) to \(n\) sends every such vector to zero. Their inverse limit is zero, in agreement with \(M^I\), and the rational invariant space is zero as well. This example explains why (C.15.3) uses the compatible complete tower and (C.15.4) uses exact localization of a kernel.

**Exercise C.15.4.2 (intermediate).** Let \(N\) have a length-three chain \(v_0,v_1,v_2\) and a length-one chain \(w\), with \(Nv_2=v_1\), \(Nv_1=v_0\), \(Nv_0=Nw=0\). Compute the rank-four logarithmic reconstruction and the induced invariant filtration. Check it for \(F(v_0)=q^{-1}v_0\), \(F(v_1)=v_1\), \(F(v_2)=qv_2\), \(F(w)=w\).

**Solution.** Since \(N^3=0\), the reconstruction is
\[
 \Psi_4(v)=v\otimes e_0-Nv\otimes e_1+N^2v\otimes e_2;
\]
its \(e_3\) coefficient is zero. The cancellation equations in C.15.2 show that it is a bijection onto the tensor invariant kernel, and \(-1\otimes J\) induces \(N\). The invariant space is \(B=Ev_0\oplus Ew\). Intersecting it with the images of \(N\) and \(N^2\) gives
\[
 B_{\le-3}=0,\qquad
 B_{\le-2}=B_{\le-1}=Ev_0,\qquad
 B_{\le0}=Ev_0\oplus Ew.
\]
Thus its nonzero grades are a one-dimensional grade \(-2\) and a one-dimensional grade \(0\); grade \(-1\) is zero. Directly on each basis vector, \(FNF^{-1}=q^{-1}N\). Formula (C.15.9) then verifies the logarithmic Frobenius comparison. The bottom lines have eigenvalues \(q^{-1}\) and \(1\), of weights \(-2\) and \(0\), respectively. This is a linear coefficient example; the calculation does not assert the existence of a global pure system with these prescribed local data.

### C.16. Stalk surjectivity from wall fibres and parity

We now prove the stalk-surjectivity input of C.10 directly for the actual spherical IC generators. The proof uses the rootwise resolution charts, supported character Chern classes, and the general IC parity already established in Reconstruction and the dual reductive group, Theorem C.4.1.1. In particular the weight hypothesis of C.9 is not an input to this application.

Let \(k\) be algebraically closed, let \(\ell\ne\operatorname{char}k\), and let \(E/\mathbb Q_\ell\) be finite. Fix \(T\subset G\), the Iwahori \(I\) whose constant Borel is \(B\), and \(S=H_T^*(\mathrm{pt},E)\). All equivariant maps in this section are in the actual geometric rational theory. Write \(\operatorname{Fl}_G=LG/I\).

#### C.16.1. A global class lifts the open wall-fibre term

For an affine-wall word \(s_1\cdots s_a\), start with a normalizer torsor \(n_\omega I\) and form the partial Bott–Samelson varieties \(\mathcal B_a\). Let \(f_a:\mathcal B_a\to\operatorname{Fl}_G\) be endpoint multiplication and \(F_a(y)=f_a^{-1}(yI)\). They are proper fibres; their reduced affine pavings and actual coefficient comparison are proved by the wall induction in Lesson 11, Lemma C.2.1.1. That induction also applies to a word which is not reduced.

**Lemma C.16.1.1.** For every word and every normalizer endpoint \(yI\), actual restriction is onto:
\[
 H_T^*(\mathcal B_a,E)\twoheadrightarrow H_T^*(F_a(y),E).
 \tag{C.16.1}
\]
The coefficient comparison includes nilpotent fibre structures.

**Proof.** Induct on \(a\). At length zero the fibre is empty or a point, so the assertion holds. For the last wall \(s=s_a\), let \(v\) be the shorter of \(y,ys\). Forgetting the last factor identifies \(F_a(y)\) with
\(f_{a-1}^{-1}(n_vP_s/I)\), inside \(\mathcal B_{a-1}\). A last wall step to \(yI\) is uniquely determined by its preceding endpoint on that wall line; this is the quotient equality of the two wall charts in Affine Grassmannians as ind-projective moduli spaces, Proposition 7.7 and Lemmas 7.8–7.9.

The wall line \(C=n_vP_s/I\simeq\mathbf P^1\) has closed endpoint \(vI\), and open chart
\(c\mapsto x_{v(a_s)}(c)vsI\), with origin \(vsI\). Put
\(\beta=\operatorname{grad}(v(a_s))\in X^*(T)\); it is a nonzero finite root. Conjugation gives \(h\,x_{v(a_s)}(c)h^{-1}=x_{v(a_s)}(\beta(h)c)\). Thus left multiplication by that root section identifies the closed and open fibre parts, \(T\)-equivariantly, with
\[
 Z=F_{a-1}(v),\qquad
 U=\mathbb A^1_\beta\times F_{a-1}(vs).
 \tag{C.16.2}
\]
The affine coordinate has weight \(\beta\), and \(T\) acts ordinarily on the second factor. Finite proper affine pavings give even free \(S\)-cohomology of both preceding fibres, by compact cell localization and the equivariant vector-line trace of C.5. Nilpotent invariance retains their actual coefficients. Consequently localization on the proper \(F_a(y)\) gives, in every degree,
\[
 0\to H_T^{n-2}(F_{a-1}(vs),E)(-1)
   \xrightarrow{\iota_U}H_T^n(F_a(y),E)
   \longrightarrow H_T^n(F_{a-1}(v),E)\to0.
 \tag{C.16.3}
\]
Here the first identification is the actual line trace for \(U\), not an ordinary pushforward along a nonproper map.

We need a class on \(\mathcal B_{a-1}\) that lifts every first term. Choose \(\chi\in X^*(T)\) with
\(m=\langle\chi,\operatorname{grad}(a_s)^\vee\rangle\ne0\).
Such a character exists because the finite coroot is nonzero. A character of \(I\), obtained by its constant torus quotient, gives an endpoint associated line \(\mathcal L_\chi\) on every partial resolution: descend the one-dimensional representation along its endpoint \(I\)-torsor. The actual torsor and its transition maps are part of the contracted-product construction in Lesson 2. Left \(T\)-multiplication commutes with this right descent and linearizes the line.

On \(C\), the associated-line convention of C.14.5.2 gives degree \(-m\). Indeed the wall's determinant-one root homomorphism identifies the line with the rank-one associated line of character \(z^m\), whose transition is that of \(\mathcal O(-m)\). This holds also for the affine wall, whose finite coroot is the torus homomorphism in those same charts. Its two fixed weights are \(\bar v\chi\) and \(\overline{vs}\chi\); their difference is \(m\beta\). Bars denote the finite Weyl parts, because translations commute with the constant torus. Therefore the global class
\[
 d=\frac{\bar v\chi-c_1^T(\mathcal L_\chi)}{m}
       \in H_T^2(\mathcal B_{a-1},E(1))
 \tag{C.16.4}
\]
restricts on the wall to zero at \(vI\), to \(\beta\) at \(vsI\), and has trace one.

This restricted class is the supported point class of \(vsI\). Its Euler restriction is \(\beta\) and its trace is one by C.5 and the normalized supported cup comparison in Lesson 6 A.1. At the other endpoint it is zero. These two restrictions determine a class on \(C\): localization is injective after passing to \(\operatorname{Frac}(S)\), and \(H_T^*(C,E)\) is free over \(S\) by its two cells. Thus equality descends integrally over \(S\). Division here is by the nonzero coefficient integer \(m\) in \(E\), never by \(\beta\).

Pull this supported class to \(F_a(y)\). This is a Cartier pullback: on the open product its equation is the regular affine coordinate \(c\), and on \(Z\) it is a unit. Hence the pulled supported Kummer class forgets to the ordinary pullback of the class just identified on \(C\). Its support is the zero section
\(\{0\}\times F_{a-1}(vs)\subset U\), disjoint from \(Z\). On this product the pulled class is the supported class of the zero of \(\mathbb A^1_\beta\), tensored with the constant second coefficient. The actual supported cup construction of C.5 therefore gives, for every global class \(b\) on \(\mathcal B_{a-1}\),
\[
 (d\cup b)|_{F_a(y)}
      =\iota_U\bigl(b|_{F_{a-1}(vs)}\bigr),
 \tag{C.16.5}
\]
where \(b\) has the degree and Tate twist specified in (C.16.3). To verify its normalization, restrict to \(U\): the supported point class followed by the affine-line trace is the identity, so its compact class is precisely the orientation generator. On \(Z\) its support is empty. Forgetting that support and then extending from \(U\) is exactly \(\iota_U\). These are maps of coefficients and cup products, so the equality retains the actual restriction maps.

Induction lifts any first-term class in (C.16.3) to such a \(b\). Equation (C.16.5) lifts its image to a class on \(\mathcal B_{a-1}\). Induction also lifts any class of the right-hand term to a class on \(\mathcal B_{a-1}\). Given a middle class, first lift its right-hand restriction, subtract that lift, and then lift the remaining first-term class by (C.16.5). Thus restriction from \(\mathcal B_{a-1}\) to \(F_a(y)\), under the forgetful identification, is onto. Pullback along the last projective-line bundle \(\mathcal B_a\to\mathcal B_{a-1}\) gives precisely those restrictions in (C.16.1). This completes induction. ∎

#### C.16.2. Equivariant parity lifts the two dense-cell identities

**Lemma C.16.2.1.** On a finite union of linear Iwahori cells, if \(A\)'s ordinary cell restrictions and \(B'\)'s exceptional cell restrictions have constant cohomology of the same parity, then
\[
 \operatorname{Hom}_{D_T}(A,B'[2b+1])=0.
 \tag{C.16.6}
\]
In particular, a flag IC and its rootwise resolution image, both of point and dual-point parity equal to the dimension of their dense cell, admit actual \(T\)-equivariant derived maps \(u,v\) with \(vu=1\).

**Proof.** The constant-system cell calculation is the first part of the proof of C.10. Connected \(T\) acts trivially on a geometrically constant cohomology sheaf. Ordered root parameters identify the cell with a linear \(T\)-space; its equivariant constant Ext ring is \(S\), which has only even degrees. Successive Postnikov attaching maps between cohomology of one parity are odd and therefore zero. Each bounded restriction consequently splits in the geometric \(T\)-equivariant category as a finite sum of shifted constant systems. Between the two restrictions every odd Hom vanishes.

Apply closed-open localization. Its open Hom and the closed Hom from \(i^*A\) to \(i^!B'\) inherit these same hypotheses by composition of ordinary and exceptional restrictions, respectively. Induction on the finite cells gives (C.16.6). This uses only the cell calculation, not the stalk-surjectivity hypothesis or conclusion of C.10.

For the last assertion let \(J\) be the raw IC of the flag Schubert support, \(R=Rf_*E[d]\) its resolution image, and \(j\) its dense cell. Both restrictions there are \(E[d]\). For each direction, the triangle
\(i_*i^!B'\to B'\to Rj_*j^*B'\)
has identity-lifting obstruction
\(\operatorname{Hom}_{D_T}(i^*A,i^!B'[1])\), zero by (C.16.6). Lift the two dense-cell identities to \(u:J\to R\) and \(v:R\to J\). Their composite is the identity on that cell. An underlying endomorphism of the perverse IC with zero dense restriction has boundary-supported image, excluded by middle extension. Thus the underlying composite is \(1\). Forgetting equivariance is faithful on degree-zero morphisms between perverse objects: these are morphisms of equivariant heart objects with a descent compatibility, so a zero underlying morphism is zero. Hence \(vu=1\) in the actual equivariant derived category. ∎

#### C.16.3. Pass from a flag stalk to a Grassmannian stalk

**Theorem C.16.3.1.** For every raw spherical \(I_\lambda\), every finite proper support containing its Schubert support, and every torus fixed point \(x\), the actual map
\[
 H_T^*(X,I_\lambda)\twoheadrightarrow
             H_T^*(x,(I_\lambda)_x)
 \tag{C.16.7}
\]
is onto. It holds in every allowed geometric characteristic, over the original finite \(E\).

**Proof.** A point outside the support has zero target. Closed image identifies the cohomology and the other stalks with those on \(X_\lambda=\overline{\operatorname{Gr}}^\lambda\), so take this support. The projection
\[
 q:\widetilde X_\lambda=
       \operatorname{Fl}_G\times_{\operatorname{Gr}_G}X_\lambda
       \longrightarrow X_\lambda
 \tag{C.16.8}
\]
is an actual smooth proper \(G/B\)-bundle of relative dimension \(N=\dim G/B\). The actual moduli interpretation in Beauville–Laszlo gluing and the moduli interpretation, Theorem 3.1, supplies the universal disc torsor; restrict it at \(t=0\) to get an actual \(G\)-torsor over \(X_\lambda\). Here \(I\) is the preimage of \(B\) under evaluation \(K^+=G(k[[t]])\to G\), with the whole congruence kernel. Thus adding an \(I\)-frame modulo \(I\) is exactly adding a flag in that restricted torsor. Its quotient by \(B\) is (C.16.8). On the smooth surjective torsor cover it is the product with the proved smooth projective \(G/B\); smoothness and properness descend. The same associated-line descent gives its \(T\)-linearized character lines.

The minimal right finite-Weyl representative \(w_\lambda\) of the dense Grassmannian cell has length \(d_\lambda\). Its right coset has unique longest element \(w_\lambda w_0\) of length \(d_\lambda+N\): appending the finite longest word successively adds its positive inversions to the inversion set of the minimal representative. Ordered root coordinates of Lesson 1 identify that flag cell as the dense cell of the inverse-image bundle. The preimage is irreducible, since it is a flag bundle over the irreducible \(X_\lambda\); properness of the flag Schubert closure and density identify it with that closure. Thus it has the rootwise resolution for a reduced word of \(w_\lambda w_0\).

Put \(J=q^*I_\lambda[N]\). This is the raw IC of \(\widetilde X_\lambda\). One can check this assertion by the middle-extension characterization: on the inverse image of the dense spherical orbit it is the constant system in degree \(d_\lambda+N\). Smooth pullback shifted by \(N\) is perverse t-exact, and smooth ordinary base change and its dual exceptional comparison preserve the strict boundary stalk and costalk inequalities, with each boundary-stratum dimension increased by \(N\). These are the actual smooth comparison and duality maps of Lesson 5 O.4 and P.3. Refining the dense smooth orbit to its dense flag cell gives the same IC.

Theorem C.4.1.1 of Lesson 11 gives point and dual-point parity \(d_\lambda\) for \(I_\lambda\). Smooth pullback and shift give parity \(d_\lambda+N\) for \(J\). Its ordinary and dual cohomology on each Iwahori cell are constant: the inherited Iwahori action and the ordered root section trivialize these systems, just as in the proof of Lesson 11 C.2.3.1. Duality on a smooth cell converts dual-point parity into exceptional cell parity without changing it, since its shift is even.

The flag resolution image has that same parity. Its proper fibres have the affine pavings (C.16.2); proper base change gives ordinary parity, and proper duality on the smooth source gives dual parity. The root sections also give its constant cell cohomology. Lemma C.16.2.1 therefore makes \(J\) a \(T\)-equivariant derived retract of this image. Lemma C.16.1.1 and actual proper base change make the resolution image's cohomology-to-fixed-stalk map onto. Naturality of restriction carries this surjection to the retract: inject a \(J\)-stalk class into the resolution stalk, lift it globally there, and project the global lift back to \(J\). Consequently
\[
 H_T^*(\widetilde X_\lambda,q^*I_\lambda)
       \twoheadrightarrow H_T^*(y,(I_\lambda)_x)
 \tag{C.16.9}
\]
for each fixed flag \(y\) above \(x\), after removing the common shift \(N\). Such flags exist explicitly as the normalizer flags \(t^\mu n_wI\) above \(x=t^\mu K^+\).

Finally compare the image of (C.16.9) with that of (C.16.7). The character Chern basis of C.14, with degrees \(2a_j\) and \(b_1=1\), gives an actual relative flag comparison
\[
 \bigoplus_j I_\lambda(-a_j)[-2a_j]
       \xrightarrow{\sim}Rq_*q^*I_\lambda,\qquad
       (c_j)\longmapsto\sum_j b_j\cup q^*c_j.
 \tag{C.16.10}
\]
Its proof is the same actual basis map as C.14.3: on the smooth trivializing \(G\)-torsor cover, proper and smooth comparison identify its fibre map with the proved basis of \(H^*(G/B,E)\); those fibres detect an isomorphism. The globally descended Chern classes make these local maps one map. Apply it on the finite \(T\)-classifying approximations to retain its equivariant assertion.

At \(y\), each \(b_j\) restricts to its character polynomial \(b_j|_y\in S\), with its Tate line. Restriction of a global class in (C.16.10) is therefore
\[
 \sum_j(b_j|_y)\,\operatorname{res}_x(c_j)
    =\operatorname{res}_x\!\left(\sum_j(b_j|_y)c_j\right).
 \tag{C.16.11}
\]
All terms have the same total degree and twist. This is a downstairs lift of every upstairs restriction value, by \(S\)-linearity of the actual restriction. Conversely the summand \(b_1=1\) contains every downstairs value. The two images agree. Surjectivity in (C.16.9) proves (C.16.7). ∎

#### C.16.4. The geometric generator comparison is unconditional

**Corollary C.16.4.1.** Let \(P=I_\lambda\), \(Q=I_\mu\), let \(G\subset L^+G\) be the constant subgroup, and put
\[
 A_G=H_G^*(\operatorname{Gr}_G,E),\qquad
 M_G=H_G^*(X,P),\qquad N_G=H_G^*(X,Q)
\]
on any sufficiently large finite proper spherical support \(X\). There is an actual comparison isomorphism
\[
 \operatorname{Ext}_{L^+G}^*(P,Q)
       \xrightarrow{\sim}\operatorname{Hom}_{A_G}^*(M_G,N_G).
 \tag{C.16.12}
\]
It retains identities and Yoneda composition. It is the geometric generator morphism comparison; identification of the modules with the Kostant presentation and an enhanced convolution equivalence require further arguments.

**Proof.** On the Iwahori cells of \(X\), the ordinary restrictions of \(P\) and exceptional restrictions of \(Q\) have constant cohomology in parities \(d_\lambda\) and \(d_\mu\), respectively. This is Lesson 11 C.4.1.1, the root-section constancy, and the even smooth-cell duality shift. Theorem C.16.3.1 supplies exactly hypothesis 2 of C.10. The constant-system cell comparison with its origin supplies hypothesis 3, by the cell calculation of C.10. Thus that theorem proves the actual torus comparison, with its composition.

C.12 identifies linearity over the finite-support ring with linearity over the whole torus Grassmannian ring, using the proved actual restriction surjection. C.13 identifies the original spherical generator Ext with sufficiently large finite-jet Ext and then constant-group Ext. C.14 supplies the actual flag scalar extension and Weyl descent, including the whole-\(\operatorname{Gr}\) restriction surjection. Taking the Weyl-invariant maps of the torus comparison therefore gives exactly (C.16.12), with the original \(A_G\)-actions. All arrows in those results are actual restrictions, cup actions, adjunctions, or scalar extensions; their established composition compatibility gives the asserted Yoneda compatibility. This application used C.16.3 rather than the conditional general weight lemma C.9. ∎

#### C.16.5. Two supported-class exercises

**Exercise C.16.5.1 (basic).** On the \(SL_2\) wall line, use the root character \(\chi=\alpha\), whose coroot pairing is \(2\). Express the normalized class of the open origin in terms of \(c=c_1^T(\mathcal L_\alpha)\). Compute its fixed restrictions and trace, including geometric characteristic two.

**Solution.** The two line weights are \(\alpha\) and \(-\alpha\), and its ordinary degree is \(-2\). Therefore \(d=(\alpha-c)/2\) restricts to zero at the closed endpoint and to \(\alpha\) at the open origin. Its trace is \(-(-2)/2=1\). The two-cell ring is \(S[d]/(d(d-\alpha))\), and \(c=\alpha-2d\). In characteristic two the coefficient field still has characteristic zero; for the primitive torus character \(u\), \(\alpha=2u\) is nonzero in \(S\), and division by \(2\) is permitted in \(E\). No reduced replacement of the geometric central kernel is made.

**Exercise C.16.5.2 (intermediate).** Suppose a proper flag-line bundle has actual basis comparison \(Rq_*q^*P=P\oplus P(-1)[-2]\), given by \(1,h\). At a fixed flag \(y\) over \(x\), write \(h|_y=a\in S^2(1)\). Show directly that upstairs stalk surjectivity implies downstairs stalk surjectivity.

**Solution.** Any homogeneous upstairs class is \(q^*m_0+h\cup q^*m_1\), with the shifted degree and twist for \(m_1\). Its restriction is \(\operatorname{res}_x(m_0)+a\operatorname{res}_x(m_1)=\operatorname{res}_x(m_0+a m_1)\). Thus every upstairs restriction value already has a downstairs lift. The first basis summand gives the converse inclusion of images. Equality of these images proves the implication. It uses the actual cup basis and \(S\)-linearity, with no assertion that arbitrary module Hom commutes with specialization.

### C.17. The actual equivariant cohomology tensor functor

Continue over algebraically closed \(k\), finite \(E/\mathbb Q_\ell\), and \(\ell\ne\operatorname{char}k\). To distinguish the coefficient ring from the dual group of Appendix B, write
\[
 R_0=H_G^*(\mathrm{pt},E)=S^W,\qquad
 S=H_T^*(\mathrm{pt},E),\qquad
 \mathfrak m=R_{0,>0}.
 \tag{C.17.1}
\]
C.14 identifies these actual coefficient rings and makes \(S\) finite free and faithfully flat over the positive graded polynomial ring \(R_0\). For a genuine spherical perverse \(P\), set \(\omega_G(P)=H_G^*(X,P)\), independent of the sufficiently large proper support \(X\), and \(\omega(P)=H^*(X,P)\). The module grading is cohomological.

The full Satake equivalence and general rational IC parity were proved in Reconstruction and the dual reductive group, B.4.1.1 and C.4.1.1. We use its corrected symmetric structure. The tensor symmetry on the graded modules below is the ordinary flip; the base ring has only even degrees. The unadjusted fusion symmetry instead corresponds to the usual Koszul flip.

#### C.17.1. Free modules and actual augmentation

**Lemma C.17.1.1.** Actual forgetting of equivariance induces a natural isomorphism
\[
 \omega_G(P)\otimes_{R_0}E\xrightarrow{\sim}\omega(P).
 \tag{C.17.2}
\]
The module \(\omega_G(P)\) is finite graded free over \(R_0\). A homogeneous basis of \(\omega(P)\) can be lifted to a homogeneous \(R_0\)-basis; this choice is not asserted to be canonical. Its basis degrees are the actual ordinary cohomology degrees.

**Proof.** First take \(P\) supported on one component. Semisimplicity makes it a finite sum of raw IC objects, all with that component's parity: \(h_G(\alpha_i^\vee)=2\), so dimension parity is constant modulo \(Q^\vee\). On each Iwahori cell its ordinary cohomology is constant and has this parity by Lesson 11 C.4.1.1 and the root-section comparisons. The equivariant constant-system splitting in C.10 therefore computes compact cell cohomology as its shifted coefficient space tensored with \(S\), with the affine trace's degree and Tate line.

Proper compact-cell localization has zero degree-one connecting maps. Consequently all its sequences are short exact, its equivariant terms are finite free over \(S\), and the ordinary sequences have exactly the same basis degrees. The actual cell forget map is
\[
 H_{T,c}^*(C,i_C^*P)\otimes_S E
       \xrightarrow{\sim}H_c^*(C,i_C^*P).
 \tag{C.17.3}
\]
This is the vector-space coefficient map and the same orientation trace on both sides. Induct through the finite closed cell filtration. Tensoring each equivariant sequence with \(E=S/S_{>0}\) stays exact because its quotient is free; the ordinary sequence and (C.17.3) then identify the middle map. Since \(X\) is proper, this proves
\[
 H_T^*(X,P)\otimes_S E=H^*(X,P)
 \tag{C.17.4}
\]
through actual forgetting. It also proves, degree by degree,
\(\operatorname{Hilb}_{H_T(P)}=\operatorname{Hilb}_S\operatorname{Hilb}_{\omega(P)}\), allowing finite Laurent degree shifts.

C.14.3 gives \(H_T(P)=\omega_G(P)\otimes_{R_0}S\) by actual restriction and cup product. Forgetting the torus and the group are compatible with the same coefficient augmentation. Tensor this comparison with \(E\) over \(S\) and use (C.17.4) to get (C.17.2).

Put \(M=\omega_G(P)\). It is a finite \(R_0\)-module: C.14.4 makes it the invariant submodule of the finite \(R_0\)-module \(H_T(P)\), and \(R_0\) is Noetherian. It is bounded below in degree because it embeds there. Choose homogeneous lifts of a basis of \(M/\mathfrak mM=\omega(P)\), giving a map \(L\to M\) from the finite graded free module \(L\) with those degrees. Its cokernel is finite graded, bounded below, and has zero reduction modulo \(\mathfrak m\). Such a cokernel is zero: a lowest nonzero homogeneous degree could not be generated by elements of strictly positive degree acting on lower degrees. Thus \(L\to M\) is onto.

Let \(b_j\) be the homogeneous \(R_0\)-basis of \(S\), of degrees \(2a_j\), from C.14. Then
\[
 \operatorname{Hilb}_{H_T(P)}
   =\operatorname{Hilb}_M\sum_jz^{2a_j},\qquad
 \operatorname{Hilb}_S
   =\operatorname{Hilb}_{R_0}\sum_jz^{2a_j}.
 \tag{C.17.5}
\]
Together with the preceding cell calculation, these equalities give
\(\operatorname{Hilb}_M=\operatorname{Hilb}_{R_0}\operatorname{Hilb}_{\omega(P)}=\operatorname{Hilb}_L\).
Each degree is finite dimensional; the surjection with equal dimensions is therefore an isomorphism in every degree. This proves freeness without a polynomial-module classification theorem.

For several components, use their finitely many supporting component projectors and apply the argument to each summand. Actual augmentation and naturality are preserved by these direct sums; bases still need not be chosen naturally. ∎

#### C.17.2. The relative external cup map

**Lemma C.17.2.1.** Let \(P,Q\) be such spherical objects on proper supports \(X,Y\), with diagonal constant-group action on \(X\times Y\). Actual external cup gives an isomorphism
\[
 H_G^*(X,P)\otimes_{R_0}H_G^*(Y,Q)
       \xrightarrow{\sim}
 H_G^*(X\times Y,P\boxtimes Q).
 \tag{C.17.6}
\]
It retains the actual coefficient maps, associativity, and the graded external-product signs.

**Proof.** On the quotient product over \(BG\), the two structural coefficient maps from \(R_0\) agree. Thus the ordinary external cup map is balanced over \(R_0\), defining (C.17.6). Construct it on the finite classifying models; its action-nerve and model comparisons are those of C.13–C.14.

First restrict to \(T\). On two cells, split the bounded constant-parity coefficient complexes as in C.10. The external cup map is an isomorphism on constant shifted coefficients: the product vector-bundle trace is the iterated trace, so it identifies the two compact orientations, retaining the Tate lines. Finite sums give the same statement for the cell coefficients.

Induct through the closed cell filtrations of \(X\) and \(Y\). All compact localization sequences are short exact by their component parities, and every equivariant term is free over \(S\). Tensoring one such sequence with the other term is exact. The corresponding compact product-cell sequence is the same actual localization sequence under external tensor and proper-support image. The cell isomorphism and induction therefore identify its middle map. Repeating in the two variables proves
\[
 H_T(P)\otimes_S H_T(Q)
       \xrightarrow{\sim}H_T(P\boxtimes Q).
 \tag{C.17.7}
\]
Finite component decompositions handle objects of different component parities.

By C.14.3, scalar extension of (C.17.6) from \(R_0\) to \(S\) is exactly (C.17.7). Its kernel and cokernel vanish after this extension. Faithful flatness of \(S/R_0\) makes them vanish before extension, proving (C.17.6). The maps were actual cup and tensor maps throughout. Associativity and the external Koszul symmetry can be checked on those maps before descent, so the result retains them. ∎

#### C.17.3. Canonical transport of a complex along affine parameters

**Lemma C.17.3.1.** Let \(Z\) be separated of finite type over \(k\), and let \(p:\mathbb A^r\times Z\to Z\). A bounded rational constructible \(K\) is in the essential image of actual \(p^*\) if every ordinary \(\mathcal H^nK\) is isomorphic to \(p^*L_n\) for a constructible sheaf \(L_n\) on \(Z\). For such \(K\), the actual counit and every section restriction give isomorphisms
\[
 p^*Rp_*K\xrightarrow{\sim}K,\qquad
 Rp_*K\xrightarrow{\sim}s^*K .
 \tag{C.17.8}
\]
They are natural and commute with restriction along affine parameter maps over \(Z\). For an arbitrary base change \(g:Z'\to Z\), the ordinary-image comparison for a complex in this essential image is also an isomorphism.

**Proof.** Iterating Semi-infinite geometry and MV weight functors, Lemma Q.1.2.1, gives the actual unit \(C\xrightarrow{\sim}Rp_*p^*C\) for every bounded rational constructible \(C\). Derived adjunction consequently makes \(p^*\) fully faithful on these complexes. Rational pullback is t-exact on constructible objects: on a lisse coefficient stratum its finite free model stays in the same degrees, and the actual closed-open pullback identities of Lesson 5 M.6 extend this assertion through the finite stratification.

Induct on the finite ordinary cohomology range of \(K\). The first truncation is a shifted \(p^*L_n\). Suppose the lower truncation is \(p^*C\). The next attaching map has the form
\[
 p^*L_{n+1}[-n-1]\longrightarrow p^*C[1].
 \tag{C.17.9}
\]
Full faithfulness lifts it uniquely to a map on \(Z\). Its cone, with the truncation shift, constructs a complex on \(Z\) pulling back to the next truncation. Thus \(K\) is pulled back from some bounded constructible \(C'\). Actual ordinary image is constructible by Lesson 5 O.2.1.1, and the unit identifies \(Rp_*K\) with \(C'\). The adjunction identity makes its displayed counit an isomorphism. Pull that counit along a section to obtain the second map in (C.17.8).

For a parameter map \(f:\mathbb A^b\times Z\to\mathbb A^r\times Z\) over \(Z\), \(f^*p^*C'\) is the same pullback of \(C'\). The unit, counit and their pasting identities therefore give the same comparisons for the two projections. For a base change \(g\), the pulled complex is \(p'^*g^*C'\). Its ordinary image is \(g^*C'\) through the affine-space unit. Under the two unit identifications the actual map \(g^*Rp_*p^*C'\to Rp'_*p'^*g^*C'\) is the identity of \(g^*C'\): transpose it under the right adjunction and use the counit identity. Naturality then proves the assertion for \(K\) and its morphisms. This proves both compatibilities. It did not replace a cohomology-sheaf comparison by an arbitrarily chosen derived splitting; the actual counit supplies the canonical complex map. ∎

#### C.17.4. Convolution and the corrected symmetry over the coefficient ring

**Theorem C.17.4.1.** The functor \(\omega_G\) takes the genuine rational Satake heart to finite graded free \(R_0\)-modules. It is exact and faithful and has canonical tensor comparisons
\[
 \omega_G(P)\otimes_{R_0}\omega_G(Q)
       \xrightarrow{\sim}\omega_G(P*Q).
 \tag{C.17.10}
\]
They preserve associativity, units, all finite ordered fusion block comparisons, and the corrected ordinary symmetric constraint. Actual augmentation (C.17.2) is the ordinary Satake cohomology tensor comparison. The functor preserves rigid duals:
\[
 \omega_G(P^\vee)=
       \operatorname{Hom}_{R_0}(\omega_G(P),R_0)
 \tag{C.17.11}
\]
with the dual grading. This is a statement about the actual graded cohomology tensor functor; a dual-Lie-algebra identification or a monoidal dg equivalence is not inferred from it.

**Proof.** Use the ordered moving-chain construction on the affine line from Fusion and the symmetric tensor structure, C.1–C.6, with unshifted factors \(P_1,\ldots,P_r\). Its map \(a_r:Y_r\to B_r=\mathbb A^r\) is proper, its coefficient \(A_r\) has the finite product charts of that lesson, and its full-collision fibre is the actual convolution chain. Constant \(G\) acts on all away frames diagonally; this commutes with the translated coordinates \(z-x_i\) and the genuine formal-coordinate coefficient comparisons. Thus the source, coefficient and endpoint maps have a genuine constant-\(G\) action.

Use the actual action nerve retained in C.13: its classifying-group level is \(Z_n=G^n\), its source level is \(Z_n\times Y_r\), and its base level is \(Z_n\times B_r\). The coefficient at that level is the pullback of \(A_r\), with the genuine action identifications on the faces. Put
\[
 K_{r,n}=R(\mathrm{id}_{Z_n}\times a_r)_*
                  \operatorname{pr}_{Y_r}^*A_r .
\]
The map being pushed forward is proper. Its product-base-change comparison identifies this complex with the pullback of \(K_{r,0}=Ra_{r,*}A_r\) from \(B_r\). Lesson 8 C.4.1.1 proves that every \(\mathcal H^qK_{r,0}\) is constant, with the specified external-product normalization, full coefficients and all degrees. Thus every \(\mathcal H^qK_{r,n}\) is pulled from \(Z_n\). This uses a proved cohomology-sheaf statement and proper base change; no derived splitting has yet been chosen.

For \(p_n:B_r\times Z_n\to Z_n\), Lemma C.17.3.1 supplies the actual complex comparison
\[
 K_{r,n}\xleftarrow{\sim}
 p_n^*Rp_{n,*}K_{r,n}.
 \tag{C.17.12}
\]
These maps retain the nerve, including its higher comparisons. A face or degeneracy induces a map \(g:Z_n\to Z_b\). Equivariance and the group action give the cartesian coefficient comparison for its proper source diagrams; the action face is cartesian because multiplication by the specified group element is an invertible map of the fibre. Proper base change gives the corresponding map between the \(K\)'s. The base-change part of C.17.3.1 applies to these pulled complexes and makes the ordinary-image and counit square commute. Its adjunction proof identifies this with the actual comparison, including its compositions. Consequently (C.17.12) is an isomorphism of the complete cartesian nerve diagrams, not merely a collection of isomorphisms on their cohomology groups.

Restrict that diagram to a chosen all-distinct point and to the full collision. Proper base change identifies the two restrictions with the action-nerve complexes for the equivariant proper cohomology of the external product and the convolution. Both are the diagram \(Rp_{n,*}K_{r,n}\), through the same counit. Taking actual derived equivariant sections therefore gives a canonical isomorphism of their equivariant cohomology complexes: it applies the existing derived totalization to an isomorphism of the whole diagram, with no interchange of cohomology and an infinite limit. The coefficient maps from the constant nerve diagram of \(E\) commute with the counit and external cup. Thus it is \(R_0\)-linear. Its cohomology followed by the external cup isomorphism (C.17.6) gives (C.17.10).

For three or more factors, use this same construction on \(\mathbb A^r\times Z_n\) at every nerve level. A block collision repeats coordinates and commutes with the projection to \(Z_n\). Lemma C.17.3.1 makes all corresponding section maps restrictions of the same counit. The actual proper block and unit maps are those proved in Lesson 8 C.3 and C.6, and are constant-\(G\)-equivariant by their bundle and away-frame constructions. Their comparisons, coefficients and cocycles therefore give the same maps on the nerve. They give the associator, unitors, and every ordered block compatibility in (C.17.10), without choosing different paths for different parenthesizations.

On the distinct open, the unadjusted permutation is the derived external shuffle. Its cohomology sign is \((-1)^{ab}\) on degrees \(a,b\), by Lesson 8 C.5. Naturality of the same counit transports this sign to a collision. For objects on components of parities \(\epsilon_P,\epsilon_Q\), Lemma C.17.1.1 shows that every degree of their equivariant cohomology has these parities, since \(R_0\) is even. The corrected Satake symmetry multiplies the geometric shuffle by \((-1)^{\epsilon_P\epsilon_Q}\). The two signs cancel, giving the ordinary flip on the graded \(R_0\)-modules. Finite component decompositions retain all permutation and braid equations.

Forgetting \(G\) uses the same coefficient, proper pullback, counit and external cup maps. Hence (C.17.2) specializes (C.17.10) to the ordinary cohomology tensor comparison, with its proved component adjustment. Semisimplicity of the genuine Satake heart makes every short exact sequence split, so this additive functor is exact. Its augmentation is the faithful ordinary fibre functor; therefore it is faithful. Freeness was proved in C.17.1.

Finally the full genuine Satake equivalence of Lesson 11 B.4.1.1 supplies its rigid evaluation and coevaluation maps. Applying the established monoidal comparisons retains their two triangle identities. Thus \(\omega_G(P^\vee)\) is a dual of the finite graded free \(\omega_G(P)\); evaluation identifies that dual with the graded \(R_0\)-linear Hom into \(R_0\). This proves (C.17.11). ∎

#### C.17.5. Two coefficient-functor exercises

**Exercise C.17.5.1 (basic).** In rank one, let \(S=E[u]\), \(|u|=2\), \(R_0=E[p]\), \(p=u^2\), and suppose the actual ordinary cohomology has basis degrees \(-2,0,2\). Determine the free equivariant module's Hilbert series and explain why a basis modulo \((p)\) determines a free basis after lifting.

**Solution.** The torus Hilbert series is
\[
 \frac{z^{-2}+1+z^2}{1-z^2}.
\]
The basis \(1,u\) of \(S/R_0\) has degree polynomial \(1+z^2\). Division gives the group-equivariant series
\[
 \frac{z^{-2}+1+z^2}{1-z^4}.
\]
Lift the three homogeneous vectors modulo \((p)\). The induced map
\(R_0[2]\oplus R_0\oplus R_0[-2]\to M\)
is onto by the lowest-degree argument in C.17.1. Source and target have the displayed same finite dimension in each degree, so its kernel is zero. This proves freeness, while allowing different choices of lifts.

**Exercise C.17.5.2 (intermediate).** Suppose \(P,Q\) have odd component parity. Compute the unadjusted and corrected exchange on homogeneous classes in \(\omega_G(P)\otimes_{R_0}\omega_G(Q)\). Explain why the affine-parameter complex comparison remains compatible with a further collision of three ordered factors.

**Solution.** All coefficient degrees of \(R_0\) are even, so all degrees from \(P,Q\) stay odd. The unadjusted external exchange sends \(a\otimes b\) to \(-b\otimes a\). The corrected component scalar is also \(-1\), giving \(b\otimes a\), the ordinary flip. For three factors, write \(K_n=p_n^*C_n\) via the actual counit on \(\mathbb A^3\times G^n\). Both orders of two successive block merges are restrictions of this same pulled complex along maps over \(G^n\); their restrictions and counits compose identically. They commute with every nerve face and degeneracy. Proper block comparisons therefore give the same equivariant cohomology tensor map, with the ordered shuffle sign already accounted for. No independent derived splitting is chosen at a diagonal.

### C.18. A graded tensor trivialization and its Lie operators

Keep \(R_0\) from C.17.1, and write \(H=\widehat G_E\) for the split dual reductive group of Reconstruction and the dual reductive group, B.4.1.1. In this section \(H\) is over the characteristic-zero coefficient field \(E\), independently of the characteristic of the geometric field \(k\). A grading has its ordinary tensor symmetry, as in C.17. The ordinary cohomology functor, denoted \(\omega\), retains its grading.

#### C.18.1. Algebraizing an equivariant lift

**Lemma C.18.1.1.** Let \(R=E[p_1,\ldots,p_s]\), with every \(|p_i|>0\), and let \(\mathfrak m=(p_1,\ldots,p_s)\). Let \(P\to\operatorname{Spec}R\) be a smooth affine morphism of finite presentation, equipped with an algebraic \(\mathbb G_m\)-action extending the degree action on \(R\). Every fixed \(E\)-point \(x\) over the origin extends to a \(\mathbb G_m\)-equivariant section. This section need not be unique.

**Proof.** The case \(s=0\) is the given fixed point, so assume \(s>0\). Put \(R_n=R/\mathfrak m^n\). We construct compatible equivariant sections \(\sigma_n:\operatorname{Spec}R_n\to P\), starting with \(x\) at \(n=1\). The ideal
\[
 I_n=\mathfrak m^n/\mathfrak m^{n+1}
 \subset R_{n+1}
 \tag{C.18.1}
\]
is square zero and is annihilated by \(\mathfrak m\).

First any \(\sigma_n\) has a lift without imposing equivariance. Its image is the single topological point \(x\). Use the standard smooth chart at that point from Smooth morphisms, Proposition 1.1:
\[
 \bigl(R[X_1,\ldots,X_b]/(F_1,\ldots,F_c)\bigr)_{h\Delta},
 \qquad
 \Delta=\det(\partial F_i/\partial X_j)_{i,j\le c}.
 \tag{C.18.2}
\]
Lift the values of the \(X_j\) arbitrarily to \(R_{n+1}\). The errors \(F_i\) lie in \(I_n\). The displayed Jacobian matrix is invertible there: its reduction is a unit, and units lift across nilpotent ideals by the finite geometric inverse. Correct the first \(c\) values by the solution of the linear system whose right side is minus those errors. Taylor expansion has no terms of order two because \(I_n^2=0\), so all equations now vanish. The localization elements remain units. This gives a lift on the chart and hence on \(P\).

Write \(A=\mathcal O(P)\). The difference between two lifts is an \(R\)-derivation \(A\to I_n\); conversely adding such a derivation to one lift gives another. Since \(\mathfrak mI_n=0\), the derivation factors through the relative cotangent space at \(x\). Thus the lift set is a nonempty affine space under
\[
 D_n=\operatorname{Hom}_E
       (\Omega_{A/R}\otimes_A E_x,I_n).
 \tag{C.18.3}
\]
This is finite dimensional. The action of \(\mathbb G_m\) on this affine space is algebraic and its linear part is the natural action on \(D_n\): use finitely many homogeneous generators of \(A\) and the finite-dimensional graded algebra \(R_{n+1}\) to write its values and equations.

Every nonempty affine space with such an action has a fixed point. Here is the argument over \(E\). After choosing an origin, write the action as \(v\mapsto\rho(t)v+c(t)\). Its group law says \(c(tu)=c(t)+\rho(t)c(u)\). Therefore
\[
 (v,a)\longmapsto(\rho(t)v+a\,c(t),a)
\]
is a rational linear representation on \(D_n\oplus E\), with trivial quotient \(E\). A rational \(\mathbb G_m\)-representation is a direct sum of its integer weights: expand its coaction in the Laurent monomials \(t^j\), and coassociativity makes their coefficients mutually orthogonal projectors with sum one. The weight-zero projector applied to any vector mapping to \(1\) still maps to \(1\), because the quotient has weight zero. It therefore gives a fixed vector \((v,1)\). The corresponding lift is equivariant. This constructs \(\sigma_{n+1}\) extending the specified \(\sigma_n\).

The inverse limit gives a graded \(R\)-algebra map \(A\to\widehat R=\varprojlim R_n\). It is polynomial rather than merely formal. Indeed, if \(d=\min_i|p_i|\), then \(\mathfrak m^n\) has no part of degree less than \(nd\). A compatible homogeneous value of weight \(j\ge0\) stabilizes in the finite-dimensional space \(R_j\) once \(nd>j\); a negative weight has value zero. Choose finitely many homogeneous \(R\)-algebra generators of \(A\). Each of their values consequently lies in \(R\). Every relation vanishes in all \(R_n\), hence in \(R\), since \(\bigcap_n\mathfrak m^n=0\) by the same degree argument. These values define a graded map \(A\to R\) splitting the structural map and specializing to \(x\). Its corresponding section proves the lemma. ∎

#### C.18.2. The tensor-isomorphism torsor, constructed from regular functions

**Lemma C.18.2.1.** Let \(R\) be a commutative \(E\)-algebra. Let \(\mathcal C=\operatorname{Rep}_E(H)\), with its ordinary forgetful functor \(\omega_0\), and let
\[
 F:\mathcal C\longrightarrow\operatorname{Mod}_R
\]
be an exact \(E\)-linear symmetric tensor functor taking finite-dimensional representations to finite free \(R\)-modules. The tensor-isomorphism functor
\[
 \mathcal P(B)=
 \operatorname{Isom}^{\otimes}
  (B\otimes_R F,\ B\otimes_E\omega_0),
 \qquad R\to B,
 \tag{C.18.4}
\]
is represented by a faithfully flat, smooth affine \(H_R\)-torsor of finite presentation.

**Proof.** Extend \(F\) to filtered unions by their module colimits. This extension is exact: filtered colimits of module sequences are exact, and each element of a kernel or image is already represented at a finite stage. Tensor products commute with these colimits.

Give \(O=E[H]\) the left regular action \(h\cdot f(g)=f(h^{-1}g)\). It is a union of finite-dimensional subrepresentations. To see this directly, expand a function's coaction in a finite linearly independent set in its second tensor factor; coassociativity shows that the span of its first coefficients is stable. Set
\[
 A=F(O).
 \tag{C.18.5}
\]
Its multiplication and unit come from those of the equivariant algebra \(O\).

The algebra \(A\) is finitely presented over \(R\). Choose finitely many algebra generators of \(O\) and a finite-dimensional stable space \(U\subset O\) containing them. The kernel of \(\operatorname{Sym}_E U\to O\) is a finitely generated ideal, by Noetherian and Artinian rings, Theorem 2.1. Choose a finite-dimensional stable space \(D\) in that kernel containing ideal generators. The equivariant sequence
\[
 (\operatorname{Sym}U)\otimes D
   \longrightarrow\operatorname{Sym}U
   \longrightarrow O\longrightarrow0
 \tag{C.18.6}
\]
is exact at the last two terms. Since \(E\) has characteristic zero, symmetric powers are the images of the usual averaging projectors on tensor powers. Exactness and the symmetric tensor comparisons therefore give
\[
 A=\operatorname{Sym}_R F(U)/(F(D)).
 \tag{C.18.7}
\]
The modules \(F(U),F(D)\) are finite free, so this is a finite presentation.

It is faithfully flat. Finite representations of \(H\) are semisimple by the full genuine Satake equivalence and semisimplicity proved in Lesson 11 B.4.1.1. Thus \(O\) is the union of finite semisimple subrepresentations, and \(A\) is the filtered colimit of their finite free images, so is flat. The invariants of the left regular action on \(O\) are exactly \(E\): an invariant regular function has the same value as at the identity on every test point, by left translation. On each finite subrepresentation containing \(E\), semisimplicity gives the canonical projection onto its invariant summand; there are no maps from a nontrivial simple to the trivial representation. These projections agree on overlaps and give an \(H\)-equivariant retraction \(O\to E\). Applying \(F\) makes \(R\) a module direct summand of \(A\). For every \(R\)-module \(M\), \(M\to A\otimes_R M\) consequently has a retraction. Flatness is therefore faithful.

The equivariant scheme isomorphism
\[
 H\times H\longrightarrow H\times H,\qquad
 (g,h)\longmapsto(g,g^{-1}h)
 \tag{C.18.8}
\]
changes diagonal left translation into left translation on the first factor and trivial action on the second. Applying \(F\) to its coordinate map gives an algebra isomorphism
\[
 A\otimes_R A\simeq A\otimes_E E[H].
 \tag{C.18.9}
\]
Its right \(H\)-coaction comes from right translation on \(O\), which commutes with left translation. The identity, multiplication and inverse equations in (C.18.8) show that (C.18.9) is precisely the torsor comparison \(P\times H_R\simeq P\times_R P\), for \(P=\operatorname{Spec}A\). Together with faithful flatness this gives an \(H_R\)-torsor.

We check that it represents (C.18.4), rather than relying on a torsor identification alone. For a representation \(V\), the vector-valued function
\[
 v\longmapsto\bigl(g\longmapsto g^{-1}v\bigr)
 \tag{C.18.10}
\]
is an equivariant map \(V\to O\otimes_E\omega_0(V)\), with trivial action on the second factor. Multiplication by \(O\) extends it to the equivariant isomorphism
\[
 O\otimes V\simeq O\otimes\omega_0(V),\qquad
 f(g)v\longmapsto f(g)g^{-1}v.
 \tag{C.18.11}
\]
Its inverse uses \(gv\). Applying \(F\) gives \(A\otimes_R F(V)\simeq A\otimes_E\omega_0(V)\). Substituting an algebra map \(A\to B\) gives the isomorphisms of (C.18.4). The equation \(g^{-1}(v\otimes w)=g^{-1}v\otimes g^{-1}w\) proves their tensor compatibility, and the identity representation proves unit compatibility. They are natural in \(V\).

Conversely extend a tensor isomorphism to \(O\) by filtered unions and compose it with evaluation at the identity to obtain an algebra map \(A\to B\). Naturality applied to (C.18.10) recovers its isomorphism on every \(V\). Applied to \(O\), (C.18.11) and the coordinate counit recover the original algebra map. The two constructions are inverse on every \(B\), proving representability.

Finally \(P\to\operatorname{Spec}R\) is smooth. Its geometric fibre over any point has a point, since it is a nonzero finitely generated algebra over an algebraically closed field; The Nullstellensatz and Jacobson rings, Theorem 1.3, proves that the residue field of a maximal ideal is that field. Choosing such a point in the torsor comparison identifies that fibre with the smooth group \(H\). The morphism is flat and finitely presented, and has smooth geometric fibres, so Smooth morphisms, Theorems 2.1 and 3.1, makes it smooth. This completes the construction. ∎

#### C.18.3. A tensor basis for actual equivariant cohomology

**Theorem C.18.3.1.** There exists a graded \(R_0\)-linear symmetric tensor isomorphism
\[
 \tau_P:\omega_G(P)\xrightarrow{\sim}
           R_0\otimes_E\omega(P)
 \tag{C.18.12}
\]
natural in the genuine rational Satake heart. It specializes at the coefficient origin to the actual augmentation of C.17.2. The grading on the right is the sum of the coefficient grading and the ordinary cohomology grading. This simultaneous tensor choice is not asserted to be canonical.

**Proof.** Identify the heart with \(\operatorname{Rep}_E(H)\) by Lesson 11 B.4.1.1 and its specified ordinary fibre functor. C.17 supplies the exact symmetric tensor functor \(F=\omega_G\) with finite free values. Forget the gradings temporarily and apply C.18.2. Its tensor-isomorphism torsor is smooth, affine and finitely presented over \(R_0\).

The gradings of \(F(V)\) and \(R_0\otimes\omega(V)\) give semilinear algebraic \(\mathbb G_m\)-actions covering the positive coefficient-degree action on \(\operatorname{Spec}R_0\). The ordinary grading of \(\omega\) is a tensor automorphism family, hence a cocharacter of \(H=\operatorname{Aut}^{\otimes}(\omega)\) by the all-test-algebra reconstruction of Lesson 11. These two graded actions act by conjugation on the tensor-isomorphism functor. This is an algebraic action on its representing scheme: (C.18.10)–(C.18.11) express it on the finite generating coefficient spaces in (C.18.7); the degree actions and the ordinary cocharacter are algebraic there. Tensor and naturality equations are preserved.

Actual augmentation gives an \(E\)-point of this torsor over the origin. It is fixed, because C.17.2 and its tensor comparison preserve the ordinary grading. By C.14 the coefficient ring is a polynomial ring in strictly positive homogeneous degrees. Lemma C.18.1.1 therefore extends that point to an equivariant section. Its corresponding tensor isomorphism preserves the gradings: equivariant module maps for \(\mathbb G_m\) preserve the weight projectors of the coaction. It is precisely (C.18.12), and its origin value is the specified augmentation. ∎

#### C.18.4. Tensor derivations in dual Lie-algebra coordinates

Fix one \(\tau\) from C.18.12, and let \(\vartheta:\mathbb G_m\to H\) be the ordinary cohomology grading cocharacter. A tensor derivation of degree \(j\) means a natural family of \(R_0\)-linear degree-\(j\) maps \(d_P:\omega_G(P)\to\omega_G(P)\) such that \(d_{\mathbf1}=0\) and, under C.17.10,
\[
 d_{P*Q}=d_P\otimes1+1\otimes d_Q.
 \tag{C.18.13}
\]
The formula is the ordinary tensor formula for the corrected symmetry.

**Lemma C.18.4.1.** Under \(\tau\), such families are exactly elements of \(R_0\otimes_E\mathfrak h\), where \(\mathfrak h=\operatorname{Lie}H\). A family of degree \(j\) is an element of total degree \(j\), with the coefficient grading on \(R_0\) and the \(\operatorname{Ad}\vartheta\)-weight grading on \(\mathfrak h\). Commutators of families correspond to Lie brackets.

**Proof.** Work first without gradings and set \(B=R_0[\epsilon]/(\epsilon^2)\). The maps \(1+\epsilon d_P\) are invertible with inverse \(1-\epsilon d_P\). Naturality, the unit condition and (C.18.13) say exactly that they are a tensor automorphism of the base-changed ordinary fibre functor, reducing to the identity over \(R_0\). By the same all-test-algebra reconstruction,
\[
 \ker\bigl(H(B)\to H(R_0)\bigr)
     =\mathfrak h\otimes_E R_0
 \tag{C.18.14}
\]
as an additive first-order group. Explicitly a coordinate map \(E[H]\to B\) reducing to the identity's counit has the form \(f\mapsto e(f)+\epsilon\,\delta(f)\). Multiplicativity says
\(\delta(fg)=e(f)\delta(g)+e(g)\delta(f)\);
thus \(\delta\) is a linear functional on the cotangent space at the identity with values in \(R_0\). That cotangent space is finite dimensional, so these functionals are exactly \(\mathfrak h\otimes_E R_0\). This also proves the asserted equality without a field-point restriction.

For \(\xi\) so obtained, its action in \(V\) is the differential of the representation \(H\to GL(V)\). Coordinate comultiplication on a tensor product gives the sum of the two differentials, proving the converse and (C.18.13). These actions recover every \(d_P\) by (C.18.14).

Give \(\epsilon\) degree \(-j\). Requiring \(1+\epsilon d\) to preserve the grading is exactly requiring \(d\) to have degree \(j\). A vector \(x\in\mathfrak h\) of \(\operatorname{Ad}\vartheta\)-weight \(w\) sends \(\omega(V)^n\) into \(\omega(V)^{n+w}\), by differentiating the conjugation equation for \(\vartheta\). Hence \(a x\), for homogeneous \(a\in R_0\), acts in degree \(|a|+w\). The weight decomposition of \(\mathfrak h\) proves the total-degree assertion. Differentials of representations carry the Lie bracket to the matrix commutator, proving its compatibility on all objects; the coordinate first-order description makes these families faithful on \(\mathfrak h\). ∎

In particular, a geometric cup operator can be put into these coordinates once its actual tensor derivation formula has been proved. C.18.4 does not assume that formula for an arbitrary class. Identifying the specific cup operators, their normalizations and their Kostant-slice coordinates remains the next step.

#### C.18.5. Two graded-section exercises

**Exercise C.18.5.1 (basic).** Let \(R=E[p]\), \(|p|=4\), and
\[
 A=R[x,y,z]/(y-x^2-p),\qquad
 |x|=2,\quad |y|=4,\quad |z|=-2.
\]
Find every graded section through the origin of \(\operatorname{Spec}A\to\operatorname{Spec}R\). Explain why the presence of a negative coordinate does not obstruct C.18.1.

**Solution.** The ring is \(R[x,z]\), so the map is smooth and the origin is fixed. A graded value of \(x\) must be in \(R_2=0\), and a graded value of \(z\) in \(R_{-2}=0\). Thus \(x=z=0\), and the relation forces \(y=p\). This is the unique graded section. In the formal construction all negative-degree values are zero; every fixed nonnegative degree stabilizes to its finite polynomial part. Negative weights on the total space therefore cause no formal-series obstruction.

**Exercise C.18.5.2 (intermediate).** Let \(H=SL_2\), \(R=E[p]\) with \(|p|=2\), and let the standard representation have basis \(v_+,v_-\) of degrees \(1,-1\). Show that a tensor trivialization with fixed augmentation can still be nonunique.

**Solution.** For every \(a\in E\), the \(SL_2(R)\)-matrix
\[
 g_a(p)=
 \begin{pmatrix}1&0\\ap&1\end{pmatrix}
 \tag{C.18.15}
\]
acts by \(v_+\mapsto v_++ap\,v_-\), \(v_-\mapsto v_-\). The added term has degree \(2-1=1\), so the matrix is graded, and at \(p=0\) it is the identity. Its determinant is one and its inverse is \(g_{-a}\). More intrinsically, for \(\vartheta(t)=\operatorname{diag}(t,t^{-1})\),
\[
 \vartheta(t)g_a(t^2p)\vartheta(t)^{-1}=g_a(p).
\]
Applying any representation proves its compatibility with that representation's semilinear degree action. These group elements therefore give graded natural tensor automorphisms on all representations. Composing a trivialization with \(g_a\) preserves its specified augmentation, while distinct \(a\)'s already act differently on the standard representation. ∎

### C.19. The determinant cup operator is a regular Lie element

Fix the closed faithful representation \(\rho:G\hookrightarrow GL(V)\) used in Loop groups and the affine Grassmannian, Theorem 7.1 and Lemmas 7.2–7.12. Its finite-stage closed embeddings retain nilpotents in every geometric characteristic. Write \(b=\dim_kV\), \(O_A=A[[t]]\), and \(F_A=A((t))\), for a parameter algebra \(A\). The coefficient field remains the finite characteristic-zero extension \(E/\mathbb Q_\ell\). The representation's integral torus weights will be used over \(E\); no trace-form nondegeneracy over \(k\) is assumed.

#### C.19.1. Relative determinants on the full lattice functor

**Lemma C.19.1.1.** The formula
\[
 \mathscr D_\rho(L)=
 \det_A(L/t^NO_A^b)^{-1}\otimes
 \det_A(O_A^b/t^NO_A^b)
 \tag{C.19.1}
\]
defines a line bundle on \(\operatorname{Gr}_G\), independent of a sufficiently large bound \(N\), on the full scheme functor. It has genuine positive-loop equivariance and a canonical equivariant trivialization at the unit lattice. For three commensurable lattices its relative version has associative isomorphisms
\[
 \mathscr D(L_2,L_0)=
 \mathscr D(L_1,L_0)\otimes
 \mathscr D(L_2,L_1).
 \tag{C.19.2}
\]
Determinants may be retained as graded lines: \(\det M\) has integer degree \(\operatorname{rk}M\), and their interchange has the sign prescribed by these degrees.

**Proof.** Lesson 2 Lemma 2.1 makes every bounded lattice quotient finite projective over \(A\). In particular \(L/t^NO_A^b\) is finite projective: it is the kernel of the quotient between the finite bounding window and its projective quotient by \(L\), so that exact sequence splits over \(A\). This argument is valid before reduction and after every base change.

For a finite projective module \(M\), define \(\det M=\bigwedge^{\operatorname{rk}M}M\) separately on its open-and-closed rank loci. If \(0\to M'\to M\to M''\to0\) is exact with all terms finite projective, a local splitting and an ordered basis give \(\det M=\det M'\otimes\det M''\). A second splitting changes the concatenated basis by a block triangular matrix of determinant one. Thus the comparison is independent of that splitting and glues. For a longer filtration the two successive comparisons both concatenate the same ordered bases, proving associativity. Interchanging two blocks has wedge sign \((-1)^{\operatorname{rk}M'\operatorname{rk}M''}\), explaining the graded-line convention.

If a common lower lattice \(U\) is replaced by \(U'\subset U\), the exact sequences for both lattices add the same determinant \(\det(U/U')\). In the relative ratio
\[
 \mathscr D(L_i,L_j)=
       \det(L_i/U)^{-1}\otimes\det(L_j/U)
 \tag{C.19.3}
\]
these extra factors cancel by their evaluation. The filtration calculation proves compatibility for successive smaller \(U'\). Any two bounds have a smaller common bound, so this gives a choice-free relative line. Cancellation of the middle determinant proves (C.19.2), with the indicated ordering and graded interchanges. Its three-factor associativity is the same cancellation and ordered-basis equality. This constructs (C.19.1) on every finite window and identifies its restrictions through all transitions.

A positive integral matrix preserves \(O_A^b\) and \(t^NO_A^b\). It acts on both finite quotients and hence on their determinant ratio. The action law is the determinant action law, and the bound comparisons are equivariant. On a fixed window the action factors through a sufficiently deep genuine jet quotient, since a matrix congruent to one modulo \(t^{2N}\) acts trivially on \(t^{-N}O_A^b/t^NO_A^b\). At \(L=O_A^b\), evaluation of the two identical determinant factors gives the canonical unit frame, also preserved by that action. All these maps commute with base change. Descent through the full faithful-representation lattice charts therefore gives the stated line on \(\operatorname{Gr}_G\), with its actual equivariance. ∎

#### C.19.2. The moving line and independent-disc factorization

**Lemma C.19.2.1.** On every ordered moving chain \(Y_r\to\mathbb A^r\) of Fusion and the symmetric tensor structure, C.1–C.6, there is a constant-\(G\)-equivariant determinant line of its last bundle relative to the standard bundle. On the distinct-point locus it is the ordered tensor product of the individual \(\mathscr D_\rho\)'s. On the full collision it is the pullback of (C.19.1) by the convolution endpoint. All ordered block, bound and unit comparisons agree with (C.19.2), on every parameter algebra.

**Proof.** In the affine coordinate write
\[
 f(t)=\prod_{i=1}^r(t-a_i),\qquad u=f(t).
 \tag{C.19.4}
\]
The monic construction of Lesson 8 §1 identifies the completed disc ring with a finite free \(A[[u]]\)-algebra, with basis \(1,t,\ldots,t^{r-1}\). The associated last \(V\)-bundle lattice \(L\) and standard lattice \(L_0\) have common finite bounds \(f^ML_0\subset L\subset f^{-M}L_0\). That lesson's operator-kernel and quotient calculation gives finite projective \(A\)-modules \(L/f^ML_0\) and \(L_0/f^ML_0\). Their determinant ratio is therefore a line on the full finite moving scheme. Smaller common lower lattices give the same canonical comparisons proved in C.19.1. It descends through the actual formal-frame charts; the away frame fixes the standard lattice. The construction is constant-\(G\)-equivariant.

On the distinct-point locus the ideals \((t-a_i)\) are pairwise comaximal. CRT and completion identify the disc ring with the product of the individual completed discs. Locally on the \(i\)-th disc, the other factors of \(f\) are units, so \(f^ML_0=(t-a_i)^ML_0\) as a submodule. Both finite quotients are the corresponding ordered direct sums. The exact determinant direct-sum maps of C.19.1 identify their relative ratio with the product of the individual relative lines, including its graded interchange signs.

For a separated collection of blocks the same CRT argument uses their monic block polynomials. When labels inside a block collide, its polynomial becomes a power of \(t-a\). The corresponding lower lattice is \((t-a)^{M|\text{block}|}L_0\), which is just a larger bound in C.19.1. Thus its specialization is the single-disc line on the actual last bundle. If all labels collide, this is the convolution endpoint's line. Regrouping a chain compares its successive relative lattices by (C.19.2); associativity of determinant filtrations and of CRT makes those comparisons agree before and after further collisions. The empty chain has \(L=L_0\), with its specified unit frame. No section displacement or infinitesimal lattice direction has been discarded. ∎

#### C.19.3. The actual primitive cup map

Set
\[
 c_\rho=c_1(\mathscr D_\rho)
       \in H_G^2(\operatorname{Gr}_G,E(1)).
 \tag{C.19.5}
\]
This notation means the compatible actual Kummer classes on the bounded stages; its action on a supported object is computed on that support.

**Theorem C.19.3.1.** Cup with \(c_\rho\) gives a natural degree-two operator
\[
 d_{\rho,P}:\omega_G(P)\longrightarrow\omega_G(P)(1)
 \tag{C.19.6}
\]
with its displayed Tate line. Its actual tensor rule is
\[
 d_{\rho,P*Q}
   =d_{\rho,P}\otimes1+1\otimes d_{\rho,Q}
 \tag{C.19.7}
\]
under C.17.10. It is zero on the unit and retains all ordered block comparisons. After choosing \(\tau\) in C.18.12 it corresponds to an element
\[
 \xi_\rho\in R_0\otimes_E\mathfrak h\otimes_E E(1)
 \tag{C.19.8}
\]
of total degree two.

**Proof.** The Kummer connecting map is additive on line tensors and negates inverse lines. At each finite coefficient level this follows by multiplying or inverting the frame transitions and their root cocycles in the actual exact coefficient sequence; the connecting map is a homomorphism. The completed coefficient construction of The Satake category and IC sheaves, A.1–A.2, retains those same maps and their inverse-limit homotopies. Thus the equality is for the actual complete class, with no interchange of invariants and reductions. It holds also on the equivariant nerve because the line comparisons are equivariant.

On \(Y_r\), cup with the moving line is a morphism \(A_r\to A_r(1)[2]\). Proper image gives the same morphism of each \(K_{r,n}\) on \(\mathbb A^r\times G^n\) in C.17.12. That complex is in the essential image of the affine pullback. The full faithfulness proved in C.17.3 therefore lifts this morphism uniquely to \(Rp_{n,*}K_{r,n}\to Rp_{n,*}K_{r,n}(1)[2]\). Its natural counit square commutes. Those lifts commute with every action face and degeneracy by the actual base-change and adjunction comparisons of that lemma. Consequently the operator commutes with the complete nerve transport and its derived sections.

At a distinct-point section, C.19.2 and Kummer additivity make this the sum of the external individual cup maps. At a collision it is the convolution endpoint cup map, by proper base change and the line specialization. The external cup map of C.17.2 identifies those two descriptions under C.17.10, proving (C.19.7). Its degree is even, so no external Koszul sign enters this sum. The same proof for \(r\) factors and their block maps proves the ordered block compatibility. The unit frame makes its Kummer class zero on the unit. Tensoring a class with an object commutes with every coefficient morphism, proving naturality.

Apply C.18.4 to this tensor derivation. To keep its coefficient line, choose temporarily a nonzero vector in \(E(1)\) and divide the operator by that vector; the lemma gives its unique Lie element. Changing the vector rescales that element inversely, so their tensor is the well-defined (C.19.8). This proves the Tate-valued assertion and its total degree. ∎

#### C.19.4. Fixed-point characters and localized projectors

List the torus weights \(\chi_1,\ldots,\chi_b\) of \(V\), with multiplicity, and define
\[
 B_\rho(\lambda,\mu)
    =\sum_{j=1}^b
          \langle\chi_j,\lambda\rangle
          \langle\chi_j,\mu\rangle,\qquad
 \psi_\lambda=\sum_j\langle\chi_j,\lambda\rangle\chi_j.
 \tag{C.19.9}
\]
The pairing is regarded on the integral coweight lattice and then over \(E\).

**Lemma C.19.4.1.** The constant-\(T\) character of \(\mathscr D_\rho\) at \(t^\lambda\) is \(\psi_\lambda\). The pairing \(B_\rho\) is Weyl invariant and nondegenerate over \(E\), including the entire central torus, and \(\psi_\lambda\ne\psi_\mu\) for distinct coweights. Put \(Q=\operatorname{Frac}S\). On a proper spherical support \(X\), the actual restriction identifies
\[
 Q\otimes_S H_T^*(X,P)
   \simeq
 \bigoplus_{t^\lambda\in X^T}
     Q\otimes_S H_T^*(t^\lambda,i_\lambda^*P).
 \tag{C.19.10}
\]
There \(d_{\rho,P}\) is scalar cup with \(c_1(\psi_\lambda)\) on the \(\lambda\)-summand. Its localized Lagrange polynomials are the projectors onto those summands.

**Proof.** In a weight basis, \(t^\lambda V(O)\) has \(j\)-th lattice \(t^{\langle\chi_j,\lambda\rangle}O\). At a large bound \(N\), the first quotient in (C.19.1) has \(N-\langle\chi_j,\lambda\rangle\) vectors of character \(\chi_j\), and the second has \(N\). The determinant inverse cancels the \(N\) terms and leaves precisely \(\langle\chi_j,\lambda\rangle\chi_j\). This proves the character and hence its actual Kummer restriction.

Lesson 2 Lemma 7.10 proves that these weights generate \(X^*(T)\), including detection of non-smooth finite kernels. On the real coweight space the Gram sum in (C.19.9) is strictly positive on every nonzero vector. Its matrix is integral, with nonzero rational determinant; it therefore stays nondegenerate over the characteristic-zero field \(E\), also when \(k\) has positive characteristic. Normalizer conjugation permutes the weight multiset, proving Weyl invariance. Nondegeneracy makes \(\lambda\mapsto\psi_\lambda\) injective, so distinct coweights give distinct nonzero differences as linear elements of \(S\).

To prove (C.19.10) for these coefficients, remove the fixed points from the finite Iwahori-cell filtration of \(X\). On each cell the constant-parity restrictions split equivariantly as in C.10. Its punctured linear cell has localized compact cohomology zero by the supported Euler proof C.5.1: every root weight is a nonzero polynomial in \(S\), and their product becomes invertible in \(Q\). Finite sums and shifts retain this vanishing. Closed–open induction gives \(QH_{T,c}^*(X\setminus X^T,P)=0\). Since \(X\) is proper, its actual localization triangle now gives (C.19.10). Cup with the line restricts on a point to its character class, so acts by the asserted scalar.

Choose a Tate vector only to write those scalars as \(\nu_\lambda\in S^2\). For the finitely many fixed labels, the polynomial
\[
 \prod_{\mu\ne\lambda}
       \frac{d_\rho-\nu_\mu}{\nu_\lambda-\nu_\mu}
 \tag{C.19.11}
\]
has value one on the \(\lambda\)-summand and zero on every other summand. All denominators are nonzero in \(Q\). These are therefore exactly its actual localized projectors; they sum to one and are mutually orthogonal. Each ratio has total degree zero, and a change of Tate vector cancels in it. This proves the claim without extending a polynomial identity from ordinary fixed-point stalk dimensions. ∎

#### C.19.5. A nonzero top cup power on the actual IC object

**Lemma C.19.5.1.** Let \(X=\overline{\operatorname{Gr}}^\lambda\) have dimension \(d=h_G(\lambda)\). Then
\[
 c_\rho^d:H^{-d}(X,IC_\lambda)
             \longrightarrow H^d(X,IC_\lambda)(d)
 \tag{C.19.12}
\]
is nonzero. This is the actual ordinary cup map; no hard Lefschetz theorem for singular IC objects is used.

**Proof.** For \(d=0\), \(X\) is its point support and the assertion is the identity, so assume \(d>0\). On its fixed component and a sufficiently large finite window, C.19.1 is the inverse determinant of the tautological subbundle times a constant line. It is therefore the pullback of the Plücker \(\mathcal O(1)\) under the finite closed embedding of Lesson 2 Theorem 7.1. In particular it is very ample on \(X\).

Let \(U\simeq\mathbb A^d\) be the dense Iwahori cell and \(i:Z=X\setminus U\to X\). There exists an actual \(T\)-equivariant map
\[
 u:E_X[d]\longrightarrow IC_\lambda
 \tag{C.19.13}
\]
restricting to the identity on \(U\). Here is its lifting proof. On every cell of \(Z\), the ordinary restriction of \(E_Z[d]\) is constant in parity \(d\), and the exceptional restriction of \(i^!IC_\lambda\) is constant in that same parity by Lesson 11 C.4.1.1. On a cell, the constant-system equivariant Ext ring is the even polynomial ring \(S\), as proved in C.10. Thus their odd Ext vanishes. Induct on the closed cell filtration using the source ordinary and target exceptional restrictions, as in C.16.2; the two outer odd Ext groups are zero, so the middle odd group is zero. In particular
\(\operatorname{Ext}_T^1(E_Z[d],i^!IC_\lambda)=0\).
The target localization triangle
\[
 i_*i^!IC_\lambda\to IC_\lambda
       \to Rj_*E_U[d]\to i_*i^!IC_\lambda[1]
\]
therefore lifts the ordinary open unit to (C.19.13). No costalk-parity assertion for the constant sheaf on the singular \(X\) is needed.

Raw Verdier self-duality gives \(DIC_\lambda=IC_\lambda(d)\). Dualize \(u\) and untwist to obtain
\[
 v:IC_\lambda\longrightarrow\omega_X(-d)[-d].
 \tag{C.19.14}
\]
On \(U\) these two maps have the actual constant unit and smooth orientation normalizations.

We supply the finite linear-section argument for their top trace. Embed \(X\) by this very ample line in \(\mathbb P^M\). A general ordered \(d\)-tuple of hyperplanes has finite nonempty intersection with \(X\), entirely inside \(U\), and transverse there. For the avoidance and transversality assertions, a fixed point imposes one independent condition on each hyperplane. The incidence over \(Z\), of dimension at most \(d-1\), has dimension at most \(dM-1\). Over a smooth point of \(U\), hyperplane derivatives surject onto the cotangent space because the map is an immersion. A dependent \(d\)-tuple of derivatives is cut out by a nonzero determinant; its incidence again has dimension at most \(dM-1\). The closures of the images of these two incidences consequently miss a nonempty open in the \(dM\)-dimensional hyperplane parameter space. The dimension bound follows on each component by injection of function fields into those of its dominating incidence component.

Nonemptiness of the projective intersection also has an elementary proof. The homogeneous coordinate domain of the affine cone has dimension \(d+1\); away from its vertex its affine charts are line charts times \(\mathbb G_m\). Krull dimension and Noether normalization, Theorem 4.2 and Corollary 4.4, make its vertex maximal ideal have height \(d+1\). An ideal generated by the \(d\) hyperplane forms cannot have that vertex as its only prime, by Dimension theory of Noetherian local rings, Theorem 3.1. If its projective zero set were empty, localization at every degree-one coordinate would be zero; every such coordinate would be nilpotent in the quotient, making the vertex its only prime. This contradiction proves nonemptiness. A tuple outside the two incidence images thus has a nonempty finite reduced intersection \(Z'\subset U\).

Each hyperplane section has the global supported Kummer class of its divisor, whose forget-support image is \(c_1(\mathscr D_\rho)\). This is the relative class and orientation construction of Lesson 6 A.1–A.2, pulled from the ambient hyperplane line. Their supported product has support in \(Z'\). At each of those points the \(d\) independent parameters give the iterated normalized section class, of trace \(1\). On that support \(u\) and \(v\) are precisely the constant identity and smooth orientation. Therefore actual supported cup, forget support and proper trace give
\[
 \operatorname{Tr}\bigl(v(d)\,c_\rho^d\,u(1)\bigr)
      =|Z'|\ne0
      \quad\text{in }E.
 \tag{C.19.15}
\]
Here \(u(1)\) is the image of the constant global section in degree \(-d\); the notation \(v(d)\) retains the displayed Tate cancellation. All point traces have the same positive Kummer normalization. The coefficient field has characteristic zero, so this positive integer is nonzero even in bad geometric characteristic. The composite factors through (C.19.12), proving the lemma. ∎

#### C.19.6. The regularity of the geometric Lie element

**Theorem C.19.6.1.** Choose a Tate vector and a graded tensor trivialization in C.18.12 to express (C.19.8) as an \(R_0\)-valued Lie element. Its origin value is a regular principal nilpotent, and every geometric value is regular. This assertion holds for the full dual reductive group, including its centre. Identifying its adjoint quotient with the specified coefficient coordinates, and identifying all higher Kostant-gradient operators, are additional steps.

**Proof.** The ordinary cohomology grading cocharacter is \(\vartheta=2\rho_G\) in the dual torus, by the weight degrees and dual-root identification of Lesson 11 B.1–B.4. Degree two in C.18.4 implies
\[
 \xi_\rho(0)=\sum_i a_i e_i,
 \tag{C.19.16}
\]
where \(e_i\) are the simple positive root vectors of \(H\). Indeed the Cartan has grading zero, the simple roots have grading two, and a positive root of height at least two has grading at least four; negative roots have negative grading. At the origin every positive-degree coefficient vanishes, leaving exactly the degree-two root spaces.

If the derived root system is empty, every Lie element of the torus is regular, so the conclusions already hold. Otherwise choose a strictly dominant integral highest \(H\)-weight \(\lambda\) in the root lattice; it corresponds to an allowed \(G\)-coweight. For example \(2\rho_H\) has this property. On \(\omega(IC_\lambda)\), the degrees \(-d,d\), with \(d=\langle2\rho_G,\lambda\rangle\), are its one-dimensional lowest and highest weight spaces, of weights \(w_0\lambda,\lambda\). This is the full highest-weight and weight-degree theorem of Lesson 11.

Every simple-root coefficient in (C.19.16) is nonzero. Suppose \(a_i=0\). Every monomial in its \(d\)-th power then raises the lowest weight by a sum of simple roots omitting \(\alpha_i\). It cannot reach the highest weight. To check that the latter difference uses every simple root, take a reduced word \(w_0=s_{i_1}\cdots s_{i_N}\). Telescoping gives
\[
 \lambda-w_0\lambda
   =\sum_{k=1}^N
       \langle\lambda,\alpha_{i_k}^{\vee}\rangle
       s_{i_1}\cdots s_{i_{k-1}}\alpha_{i_k}.
\]
The inversion roots in this reduced word are all positive roots: at each prefix, a simple reflection permutes the positive roots other than its simple root, so the inverse inversion set gains exactly the new positive prefix root; for the longest element that set is the entire positive system. All displayed coefficients are positive by strict dominance. In particular their simple-root coefficients include each simple root with a positive coefficient. The reduced-word and inversion-root facts have the complete root proof in Finite-dimensional Lie theory, §5. Therefore the hypothesized missing \(a_i\) makes the map from degree \(-d\) to degree \(d\) zero. Actual augmentation identifies that map with the ordinary \(c_\rho^d\) of C.19.12, contradicting C.19.5.1.

The simple characters are a basis of the character lattice of the adjoint torus. Their nonzero values can therefore rescale every \(a_i\) to one, over an algebraic closure or by the split adjoint torus itself. Thus \(\xi_\rho(0)\) is adjoint-conjugate to the principal \(e=\sum_i e_i\), proved regular in B.2. The central summand is zero at the origin and adds its full rank to the centralizer, so causes no exception.

For global regularity, C.18.4 gives the precise homogeneous identity
\[
 \xi_\rho(t\cdot p)
     =t^2\operatorname{Ad}_{\vartheta(t^{-1})}\xi_\rho(p).
 \tag{C.19.17}
\]
The nonregular locus is closed by the minors of the centralizer matrix and is invariant under conjugation and nonzero scalar multiplication, as in B.3. Its inverse image in \(\operatorname{Spec}R_0\) is therefore a closed subset stable under the positive grading action. If it had a geometric point \(p\), the map \(t\mapsto t\cdot p\) would extend to \(\mathbb A^1\), with value the coefficient origin at zero. Closedness would put that origin in the nonregular inverse image. This contradicts the principal origin value just proved. The inverse image is empty, so every geometric value is regular. ∎

![Relative determinant cancellation, the actual collision cup sum, and the principal-origin regularity argument](assets/determinant-cup-regularity.png)

The common lower lattice retains the full finite quotients. The moving line transports its degree-two Tate-valued cup map through the collision. Its nonzero top IC cup power forces every simple-root coefficient at the origin, and positive grading propagates regularity. Proofs C.19.1.1–C.19.6.1. The disc symbols and the final grading arrow are schematics of those proved comparisons. Editable SVG source.

#### C.19.7. Two determinant-operator exercises

**Exercise C.19.7.1 (basic).** Take \(G=\mathbb G_m\) and its identity character representation. Compute the determinant character and primitive cup action on the point-supported object at label \(n\), and compare labels \(n,m,n+m\).

**Solution.** For \(N>|n|\), the two ranks in (C.19.1) are \(N-n,N\), so their character difference is \(n\chi\). If \(u=c_1(\chi)\), the action on its module \(S\) is multiplication by \(nu\), with its Tate line. Labels add under convolution, and \((n+m)u=nu+mu\) is exactly (C.19.7). At label zero the line has its canonical unit frame and the operator is zero. These supported cohomology objects use the reduced points, while the line was constructed on the full torus Grassmannian including its nilpotent directions. Integrally the operator \(nu\) alone does not recover the degree-zero label operator \(n\) by division by \(u\); that division requires localization.

**Exercise C.19.7.2 (intermediate).** Take \(G=GL_2\), its standard representation, and the minuscule \(P=E_{\mathbb P^1}[1]\). Choose a Tate vector for the scalar formulas. Let \(u_1,u_2\) be the two character classes and \(\sigma_1=u_1+u_2,\sigma_2=u_1u_2\). Compute the determinant cup matrix and its normalized rank-one companion form.

**Solution.** At the support \(tO^2\subset L\subset O^2\), the tautological line is \(L/tO^2\). Formula (C.19.1) is its inverse times \(\det(k^2)\). If its class is \(a\), put \(x=\sigma_1-a\). The relative flag Chern-basis calculation of C.14 gives
\[
 H_T^*(\mathbb P^1,E)=
    S[a]/((a-u_1)(a-u_2))
   =S[x]/(x^2-\sigma_1x+\sigma_2).
\]
The two fixed values of \(x\) are \(u_1,u_2\), agreeing with (C.19.9). The invariant basis \(1,x\) descends through C.14 to the \(R_0=E[\sigma_1,\sigma_2]\)-basis of \(H_G^*(P)\), in degrees \(-1,1\). Actual cup with \(x\) has matrix
\[
 \begin{pmatrix}0&-\sigma_2\\1&\sigma_1\end{pmatrix}.
 \tag{C.19.18}
\]
Set \(y=x-\sigma_1/2\) and \(c=\sigma_1^2/4-\sigma_2\). In the ordered homogeneous basis \((y,1)\), of degrees \(1,-1\), the matrix becomes
\[
 \frac{\sigma_1}{2}I+
       \begin{pmatrix}0&1\\c&0\end{pmatrix}.
 \tag{C.19.19}
\]
The second matrix is the rank-one Kostant companion, with \(c\) of degree four; the scalar part retains the full \(GL_2\) centre. At the coefficient origin its raising map is nonzero and its square is zero. The eigenvalues are \(u_1,u_2\), and their difference is nonzero after localization. The basis change is graded and has determinant a unit. These are actual cup matrices on this geometric module; they do not identify all higher operators for a general group.

### C.20. Fixed-point weights and the actual Kostant quotient

Retain the coefficient rings, full dual group \(H\), faithful representation \(\rho\), and actual determinant cup element of Sections 17–19. In this section choose one nonzero vector of \(E(1)\) for the scalar Lie and polynomial formulas. The conclusions with their Tate lines follow by undoing that choice. Write
\[
 L=X_*(T_G)=X^*(T_H),\qquad
 \mathfrak t_G=X_*(T_G)\otimes E,\qquad
 \mathfrak t_H=\operatorname{Hom}_{\mathbb Z}(L,E).
 \tag{C.20.1}
\]
The trace pairing from C.19.4 defines the isomorphism
\[
 \beta_\rho:\mathfrak t_G\longrightarrow\mathfrak t_H,\qquad
 \lambda(\beta_\rho(u))
     =\sum_{\chi\text{ a weight of }V_\rho}
           \langle\chi,\lambda\rangle\,\chi(u).
 \tag{C.20.2}
\]
Multiplicities occur in this sum. It is \(W\)-equivariant and invertible, including on the centre, by C.19.4. The cohomological degree of a linear coordinate is two. Thus \(\beta_\rho\) identifies the positively graded quotient bases. We first check which multiplicities occur in the localized geometric operator.

![Compact attracting-slice localization, invariant trace tests and the adapted graded frame](assets/geometric-kostant-quotient.png)

The first panel concerns the reduced cohomological support of the finite attracting scheme: invertible character coordinates kill its punctured compact image only after extension to \(Q\). The second uses the resulting actual weight multiplicities to test every invariant polynomial and then descends along the injective coefficient map. The third shows the full smooth conjugation scheme and the precise grading sign that permits a polynomial section through the identity. Proofs C.20.1.1–C.20.4.1 establish these maps; Exercise C.20.5.2 explains why adapting the rational pinning matters. Editable SVG source.

#### C.20.1. Compact attraction computes the fixed-point rank

**Lemma C.20.1.1.** For a raw spherical \(P=IC_\lambda\), supported on a finite projective Schubert variety \(X\), and any torus label \(\mu\), there is an actual restriction isomorphism
\[
 Q\otimes_S H_{T,c}^*(S_\mu\cap X,P)
       \xrightarrow{\ \sim\ }
 Q\otimes_S H_T^*(t^\mu,i_\mu^*P),
 \qquad Q=\operatorname{Frac}S.
 \tag{C.20.3}
\]
An empty slice gives zero on both sides. In particular
\[
 \dim_E F_\mu(IC_\lambda)
       =\sum_j\dim_E H^j(i_\mu^*IC_\lambda).
 \tag{C.20.4}
\]
Under the full Satake equivalence, this is the multiplicity of weight \(\mu\) in \(V_\lambda\).

**Proof.** The finite projective lattice embedding is \(T\)-equivariant. Choose a strictly dominant constant cocharacter \(\gamma\) which does not annihilate any nonzero difference of the finitely many ambient weights. Such an integral choice exists: the strictly dominant rational cone is open, and finitely many proper rational hyperplanes cannot cover it. The root-parameter calculation of Lesson 5, §7, equation (7.1), applies to this \(\gamma\). Its positive root powers contract every point of \(S_\mu\) to \(t^\mu\); the proved Iwasawa partition and uniqueness of a limit show that this is precisely the corresponding attracting locus.

Here is a finite coordinate realization sufficient for localization. Choose an eigen-coordinate \(z_0\) nonzero at the fixed point in the projective embedding. Its chart is \(T\)-stable. If \(\eta_i\) is the weight of the ratio \(z_i/z_0\), attraction to this point sets the negative \(\gamma\)-weight ratios to zero and the zero-weight ratios to their point values. The remaining ratios \(x_i\) have \(\langle\eta_i,\gamma\rangle>0\). Intersecting these equations with the closed equations of \(X\) gives a closed affine attracting scheme \(A\), with distinguished origin. The description holds on every parameter algebra: an equivariant polynomial path has coordinate \(s^{\langle\eta_i,\gamma\rangle}x_i\); a negative power belongs to \(R[s]\) only when its coefficient is zero, including for nilpotent coefficients. The underlying reduced locus is \(S_\mu\cap X\), by the preceding partition. Actual closed-reduction comparison in C.12 and Lesson 5 O.4.2.1 identifies their cohomology and compact images, so we may use this finite scheme.

The finitely many invariant opens \(D(x_i)\) cover \(A\setminus\{t^\mu\}\). Each \(\eta_i\) is a nonzero character. On \(D(x_i)\) the function \(x_i\) is an invertible equivariant section of the line with character \(\eta_i\), up to the harmless inverse convention for the function action. Its first Chern class is therefore zero on that open. This is an actual equivariant line trivialization: after tensoring by the inverse character, the section has weight zero and gives the trivial frame on the whole action nerve. The Kummer cocycle of that frame is zero. Consequently the nonzero linear class \(c_1(\eta_i)\), or its negative, acts by zero on the compact equivariant cohomology of any restricted coefficient complex there.

The same argument works on every intersection in this finite open cover. Localization to \(Q\) therefore kills all these compact cohomology modules. The compact Mayer–Vietoris triangle follows from the two extension-by-zero maps and their overlap, checked on stalks; induction on the number of opens gives
\[
 Q\otimes_S H_{T,c}^*(A\setminus\{t^\mu\},P)=0.
 \tag{C.20.5}
\]
The compact image of the actual open–closed triangle
\(j_!j^*P\to P\to i_{\mu*}i_\mu^*P\)
now gives exactly (C.20.3). Localization is flat, so this conclusion preserves the specified restriction map.

To compute its two ranks, form the genuine \(T\)-equivariant compact image of \(P|_A\) on the point. Its underlying complex is concentrated in degree \(h_\mu=\langle2\rho_G,\mu\rangle\), with coefficient \(F_\mu(P)\), by Lesson 5, Theorem Q.4.2.1. A complex with one ordinary cohomology sheaf is canonically that sheaf shifted. The equivariant point sheaf here is constant: its action matrix is a degree-zero section on the connected torus, hence is a constant matrix, and the identity section forces that matrix to be the identity. Its cocycle is consequently the constant cocycle. Taking equivariant cohomology gives
\[
 H_{T,c}^*(A,P)=S\otimes_E F_\mu(P)[-h_\mu].
 \tag{C.20.6}
\]
This computation uses the actual compact image object, whose construction on the action nerve commutes with the smooth atlas comparisons; it does not assert nonproper ordinary base change.

At the fixed point, the ordinary stalk of \(IC_\lambda\) has one parity by Lesson 11 C.4.1.1. Its finite equivariant ordinary tower splits as in C.10: an attaching map between constant even-separated terms belongs to an odd group of \(S\), which is zero. Thus its equivariant cohomology is a free \(S\)-module of rank \(\sum_j\dim H^j(i_\mu^*P)\). Comparing ranks in (C.20.3) proves (C.20.4). Finally the full weight identification in Lesson 11 B.1–B.4 identifies \(F_\mu(IC_\lambda)\) with the \(\mu\)-weight space of \(V_\lambda\). This proves the last assertion. ∎

#### C.20.2. Traces test every invariant polynomial

**Lemma C.20.2.1.** Let \(H\) be the original split connected reductive group in characteristic zero, with its full character lattice \(L\). In each positive polynomial degree \(n\), the functions
\[
 x\longmapsto\operatorname{tr}_{V_\lambda}(x^n),
 \qquad \lambda\in L\text{ dominant},
 \tag{C.20.7}
\]
span \(E[\mathfrak h]^H_n\). No change to a simply connected cover is required.

**Proof.** First work on \(\mathfrak t_H\). Integral linear forms \(\mu\in L\) span its linear dual. Their \(n\)-th powers span all degree-\(n\) polynomials, because
\[
 n!\,\ell_1\cdots\ell_n
    =\sum_{J\subset\{1,\ldots,n\}}
          (-1)^{n-|J|}
          \left(\sum_{j\in J}\ell_j\right)^n.
 \tag{C.20.8}
\]
Expansion proves this identity: any monomial omitting an index cancels in the subset sum, and the sole monomial using every index has coefficient \(n!\). Choose the \(\ell_j\) from an integral basis and use linearity. Averaging over the finite Weyl group therefore shows that the invariant polynomials are spanned by
\(\sum_{\mu\in W\lambda}\mu^n\)
for dominant \(\lambda\in L\), with distinct orbit elements.

The formal character of \(V_\lambda\) is the orbit sum of \(\lambda\), with coefficient one, plus a finite combination of orbit sums of strictly lower dominant weights. This is the highest-weight theorem of Lesson 11: the extremal weights \(W\lambda\) have multiplicity one, and all other weights differ from \(\lambda\) by positive-root sums. This triangular relation can be inverted using only representations of the original group. To see termination, pair the dominant weights with the sum of positive coroots of the derived group. The resulting nonnegative integers strictly decrease under a strict dominance drop. All terms keep the same central character. For a torus there are no lower terms. Thus induction expresses every orbit sum as a finite linear combination of these full-group characters.

Apply the linear operation \(e^\mu\mapsto\mu^n\) to that character identity. The character of \(V_\lambda\) becomes the torus restriction of (C.20.7), because a torus Lie element acts by the scalar \(\mu(x)\) on its \(\mu\)-weight space. Hence those trace functions span the torus invariants. Chevalley restriction and its full reductive centre, including the descent to every characteristic-zero coefficient field proved in §3 of this lesson, identify the latter with \(E[\mathfrak h]^H\). The trace polynomials are themselves conjugation invariant, so the spanning assertion follows. ∎

#### C.20.3. The quotient is the trace-pairing coordinate map

**Theorem C.20.3.1.** The actual geometric element satisfies, for every invariant polynomial \(f\),
\[
 f(\xi_\rho)=f(\beta_\rho(u))
       \quad\text{in }R_0=E[\mathfrak t_G]^W.
 \tag{C.20.9}
\]
Here the right side denotes restriction of \(f\) to \(\mathfrak t_H\), followed by \(\beta_\rho\). Thus its adjoint quotient is the specified isomorphism of the coefficient base with \(\mathfrak h/\!/H\).

**Proof.** Extend the actual cup action and its graded tensor trivialization to \(S\), and then to \(Q\). C.19.4 gives the actual fixed-point decomposition and projectors. On the block at \(\mu\) the determinant cup element acts by
\[
 \nu_\mu(u)=\mu(\beta_\rho(u)).
 \tag{C.20.10}
\]
These eigenvalues are distinct for distinct labels, since \(\beta_\rho\) is an isomorphism. Lemma C.20.1.1 identifies the dimension of that block with \(\dim V_\lambda[\mu]\). Consequently, for every \(n>0\),
\[
 \operatorname{tr}_{V_\lambda}(\xi_\rho^n)
       =\sum_\mu\dim V_\lambda[\mu]\,
                         \mu(\beta_\rho(u))^n
       =\operatorname{tr}_{V_\lambda}(\beta_\rho(u)^n)
       \quad\text{in }Q.
 \tag{C.20.11}
\]
The first trace is taken on the finite free module \(\omega_G(IC_\lambda)\); under C.18 it is precisely the represented Lie action on \(R_0\otimes V_\lambda\). The actual torus restriction and fixed-point projectors computed its trace, rather than substituting an abstract module with the same rank.

Lemma C.20.2.1 gives (C.20.9) for homogeneous invariant polynomials of positive degree. Constants agree as well, and finite sums handle every polynomial. Both sides lie in \(R_0\). Its inclusion into \(S\), and into \(Q\), is injective by C.14, so the equality already holds in \(R_0\). Since \(\beta_\rho\) is invertible and \(W\)-equivariant, its map on the two invariant polynomial rings is an isomorphism. This proves the precise quotient statement over every coefficient parameter algebra, including nonreduced ones. ∎

#### C.20.4. A rational pinning and a graded conjugation

**Theorem C.20.4.1.** Adapt the pinning of \(H\) to the nonzero simple coefficients of \(\xi_\rho(0)\). Let
\(\sigma_\rho:\mathfrak h/\!/H\to\mathfrak h_{\mathrm{reg}}\)
be the resulting Kostant section. There is a graded tensor trivialization, with the same actual augmentation as C.18, in which the determinant cup element is exactly
\[
 \sigma_\rho\!\left(\beta_\rho(u)\bmod W\right).
 \tag{C.20.12}
\]
The construction preserves the original full dual group and centre. It need not give a conjugation to an arbitrarily prescribed old pinning over \(E\).

**Proof.** By C.19.6 write \(e_\rho=\xi_\rho(0)=\sum_i a_i e_i\), with every \(a_i\in E^\times\). Set
\[
 e_i^\rho=a_i e_i,\qquad
 f_i^\rho=a_i^{-1}f_i,\qquad
 f_\rho=\sum_i c_i f_i^\rho .
 \tag{C.20.13}
\]
Their principal triple has the same \(h=2\rho_H^\vee\) and cocharacter \(\vartheta\) as B.2. These are a full rational pinning, not a claim about an \(H(E)\)-conjugator. Indeed the simple characters form a basis on the adjoint torus, so the tuple \((a_i)\) gives an \(E\)-point there. After a finite extension it lifts to the original split torus: in character bases, Smith normal form reduces the lift to finitely many equations \(z^m=a\), all with \(a\ne0\). The corresponding extensions are separable in characteristic zero. Two lifts differ by the centre and hence give the same conjugation on \(H\). The resulting conjugation automorphism and its inverse descend to \(E\); the matrix coefficients agree on the two overlap projections, so affine faithful-flat descent supplies the descended maps. Denote this automorphism by \(\phi_\rho\). It fixes the torus, the centre, \(\vartheta\), and every invariant polynomial. The last assertion can be tested after that finite extension, where it is ordinary inner conjugation, and then descends injectively.

Apply \(\phi_\rho\) to the complete proofs of B.2–B.3. The adapted slice is
\(\Sigma_\rho=e_\rho+\ker\operatorname{ad}f_\rho\).
Its quotient is the same polynomial isomorphism on all parameter algebras; its positive action is still \(t^2\operatorname{Ad}_{\vartheta(t^{-1})}\). Its inverse defines \(\sigma_\rho\). The full map
\(H\times\Sigma_\rho\to\mathfrak h_{\mathrm{reg}}\)
is smooth surjective. In the torus case \(\phi_\rho\) is the identity and the slice is all of \(\mathfrak h\); the argument includes it.

Let \(B=\operatorname{Spec}R_0\), and put
\(s(p)=\sigma_\rho(\beta_\rho(p)\bmod W)\).
Consider the affine scheme of finite presentation
\[
 P=\{(p,g)\in B\times H:
                 \operatorname{Ad}_g s(p)=\xi_\rho(p)\}.
 \tag{C.20.14}
\]
It is the base change of the preceding smooth surjection along \(\xi_\rho:B\to\mathfrak h_{\mathrm{reg}}\). To check this scheme equality, the base change initially has a variable slice point \(\sigma\). Applying the quotient to its defining equality forces \(\sigma=s(p)\), by (C.20.9) and the polynomial inverse on the full slice. This argument holds for every parameter algebra. Thus \(P\to B\) is smooth surjective. Its fibres retain the full centralizer, including its centre and all components.

Homogeneity of \(\xi_\rho\) and of the slice gives the algebraic action
\[
 t\cdot(p,g)
    =\bigl(t\cdot p,\,
            \vartheta(t^{-1})g\vartheta(t)\bigr)
       \quad\text{on }P.
 \tag{C.20.15}
\]
Substitution in (C.20.14) proves this identity, including its sign: both \(s(t\cdot p)\) and \(\xi_\rho(t\cdot p)\) equal \(t^2\operatorname{Ad}_{\vartheta(t^{-1})}\) of their values at \(p\). The point \((0,1)\) is fixed, since \(s(0)=e_\rho=\xi_\rho(0)\). The base coordinates have positive weights. Lemma C.18.1.1 therefore gives an actual polynomial equivariant section \(g:B\to H\) through the identity, by its finite-order lifts and homogeneous stabilization. No field-point lifting or merely formal section is substituted.

If \(\tau\) is the former tensor trivialization, replace it on each representation by \(g^{-1}\tau\). The represented group action is a natural tensor automorphism on every test algebra. Equation (C.20.15) makes the new frame graded; its identity value at the origin retains the actual augmentation. Finally
\(\operatorname{Ad}_{g^{-1}}\xi_\rho=s\)
is exactly (C.20.12). The higher primitive operators still have to be constructed and identified with the centralizer gradients. ∎

#### C.20.5. Two quotient and pinning exercises

**Exercise C.20.5.1 (basic).** For \(GL_2\) with its standard trace pairing, recover the two adjoint-quotient coordinates from the actual matrix C.19.18. Check that the centre survives the comparison.

**Solution.** Here \(\beta_\rho\) is the identity on the two diagonal coordinates. The matrix has trace \(\sigma_1\), determinant \(\sigma_2\), and squared trace invariant \(\operatorname{tr}(\xi_\rho^2)=\sigma_1^2-2\sigma_2\). Hence its characteristic polynomial is \(z^2-\sigma_1z+\sigma_2\), exactly the polynomial of the diagonal pair \((u_1,u_2)\). The central scalar in C.19.19 is \(\sigma_1/2\); it is retained by this quotient map. Trace and squared trace generate the same invariant algebra as trace and determinant since \(2\) is invertible in \(E\).

**Exercise C.20.5.2 (intermediate).** In \(SL_2\) over a characteristic-zero coefficient field \(E\), let \(a\in E^\times\). Determine when \(aE_{12}\) is conjugate to \(E_{12}\) by an \(SL_2(E)\)-matrix. Construct its adapted principal triple even when that conjugator does not exist.

**Solution.** Any such conjugator preserves the unique kernel line \(Ee_1\), so has the form
\(\left(\begin{smallmatrix}z&b\\0&z^{-1}\end{smallmatrix}\right)\).
Its conjugation sends \(E_{12}\) to \(z^2E_{12}\). A conjugator exists exactly when \(a\) is a square in \(E^\times\). For any \(a\ne0\), however, the vectors \(e_a=aE_{12}\), \(f_a=a^{-1}E_{21}\), and \(h=\operatorname{diag}(1,-1)\) satisfy \([e_a,f_a]=h\), \([h,e_a]=2e_a\), and \([h,f_a]=-2f_a\). They define the adapted slice \(e_a+Ef_a\) with the same invariant quotient. Its adjoint-torus rescaling descends over \(E\) even if its original-torus lift requires adjoining a square root. This is the precise distinction used in C.20.4.

### C.21. Higher primitive cup operators and the generator modules

Keep the adapted graded tensor frame of C.20.4. Choose a Tate vector as in C.20 for scalar formulas. For a homogeneous coefficient class \(q\in R_0\) of polynomial degree \(d\geq1\), its cohomological degree and natural twist are \(2d\) and \(E(d)\). We construct a cup class of degree \(2d-2\), with twist \(E(d-1)\). Its normalization will be a directional derivative, including in polynomial degree one.

![The fixed-point curve sign, actual higher gradients and the whole-ring generator morphism comparison](assets/higher-cup-kostant-modules.png)

The first panel is the exact torus-fixed calculation on the curve, with its negative lattice degree and trace normalization. The second uses the full framed moving torsor to obtain the primitive operator before identifying its gradient. The third displays the two coefficient descents that recover linearity over every whole-Grassmannian class. Here the diagram abbreviation \(B_{\mathrm{op}}\) denotes the polynomial operator algebra \(\mathcal B_\rho\), while the inverse trace form is \(B_H\). Proofs C.21.1.1–C.21.5.1 supply the maps; the coherent Hom uses the deformation grading of B.5. Editable SVG source.

#### C.21.1. The inverse trace form on the full dual Lie algebra

**Lemma C.21.1.1.** There is a nondegenerate \(H\)-invariant symmetric bilinear form \(B_H\) on \(\mathfrak h\) whose restriction to \(\mathfrak t_H\) is
\[
 B_H(v,w)=B_\rho(\beta_\rho^{-1}v,\beta_\rho^{-1}w).
 \tag{C.21.1}
\]
For \(f=q\circ\beta_\rho^{-1}\), regarded as an invariant polynomial on \(\mathfrak h\) by Chevalley restriction, its gradient satisfies
\[
 \lambda\!\left(\nabla_{B_H}f(\beta_\rho(u))\right)
                  =D_\lambda q(u)\qquad(\lambda\in L).
 \tag{C.21.2}
\]

**Proof.** The displayed Cartan form is nondegenerate and \(W\)-invariant by C.19.4. It is orthogonal between distinct derived simple components, and between the derived Cartan and the centre. Indeed a reflection fixes the other component and the centre, while negating its simple coroot; invariance makes the pairing with that coroot zero. The simple coroots span the derived Cartan.

On one simple component, compare this form with the Cartan restriction of the Killing form. Its Cartan matrix is the root Gram form \(\sum_{\alpha}\alpha\otimes\alpha\): these roots span the rational Cartan dual, and the real Gram form is positive definite. Its determinant is therefore a nonzero rational number, hence remains nonzero over every characteristic-zero \(E\). The Killing form is invariant by the trace-of-a-commutator identity. Distinct root spaces pair only when their roots are opposite, by Cartan invariance. For a normalized root pair its value is \(K(e_\alpha,f_\alpha)=K(\alpha^\vee,\alpha^\vee)/2\), again nonzero by that rational Gram calculation. This also verifies nondegeneracy on the full simple Lie ideal. The comparison endomorphism commutes with every reflection. A reflection's negative eigenspace is its simple-coroot line, so the endomorphism has some scalar on each such line. For adjacent simple coroots, the formula \(s_i(\alpha_j^\vee)=\alpha_j^\vee-m_{ij}\alpha_i^\vee\), with \(m_{ij}\ne0\), forces their scalars to agree. The connected simple Dynkin diagram makes the comparison a single scalar. That scalar is nonzero by nondegeneracy. Extend by this scalar times the Killing form on each simple Lie ideal, and by the prescribed form on the centre. This constructs the required full nondegenerate invariant form; neither a central direction nor a simple factor is discarded. Invariance for the algebraic group follows from the same torus and root-exponential argument as §3: a Lie-invariant polynomial tensor is torus-invariant and root-group-invariant, and those subgroups generate \(H\).

Put \(v=\beta_\rho(u)\), and let \(b=\beta_\rho^{-1}\nabla_{B_H}f(v)\) in the Cartan. The gradient lies there: invariant gradients are fixed by the torus stabilizing \(v\), so this holds on the dense regular Cartan and then as a polynomial identity on the entire Cartan. For \(x\in\mathfrak t_G\), the gradient definition gives
\[
 B_\rho(b,x)
    =B_H(\nabla f(v),\beta_\rho(x))
    =df_v(\beta_\rho(x))
    =dq_u(x).
 \tag{C.21.3}
\]
By C.20.2, \(\lambda(\beta_\rho(b))=B_\rho(\lambda,b)\). Substituting \(x=\lambda\) in (C.21.3) proves (C.21.2). The equality extends from the regular Cartan to all its points because both sides are polynomials. ∎

#### C.21.2. A framed characteristic class and its primitive cup map

**Theorem C.21.2.1.** There is a compatible actual whole-Grassmannian equivariant class
\[
 z_q\in H_G^{2d-2}(\operatorname{Gr}_G,E(d-1)).
 \tag{C.21.4}
\]
Its cup maps on the spherical cohomology modules are natural and \(R_0\)-linear, vanish on the tensor unit, and satisfy
\[
 z_q|_{\omega_G(P*Q)}
      =z_q|_{\omega_G(P)}\otimes1
           +1\otimes z_q|_{\omega_G(Q)}
 \tag{C.21.5}
\]
under the actual tensor comparison C.17. The class is linear in \(q\). The construction uses the full lattice and moving-chain functors before taking their cohomological supports.

**Proof.** Use \(\mathbb P^1\) with modification point \(0\). The full gluing equivalence of Lesson 3, Proposition 2.1 and Theorem 3.1, gives on \(\mathbb P^1\times\operatorname{Gr}_G\) the universal right \(G\)-torsor \(\mathcal P\), with its specified frame off \(0\). This assertion can be read stage by stage: pull back to the local loop-frame covers, glue the disc torsor to the framed trivial torsor on the complement, and descend along the exact change-of-frame maps. The gluing equivalence includes morphisms, so these transitions satisfy the cocycle on the full parameter algebras. A framed automorphism which is the identity off \(0\) is the identity: on a local trivialization its defining functions vanish after inverting the curve parameter, which is a nonzerodivisor on the flat torsor. Thus there is no residual automorphism ambiguity in this descent.

The constant \(G\)-action is retained. Let \(\mathcal P_{\mathrm{ref}}\) be the trivial curve torsor with its diagonal constant-\(G\) equivariance. Its characteristic class is the base class \(q\); its ordinary bundle being trivial does not make its equivariant class zero. Characteristic classes here mean actual pullback from the \(G\)-torsor classifying nerve: the element \(q\in H_G^{2d}(\mathrm{pt},E(d))\) pulls back along each torsor's classifying map. The off-point frame gives a specified isomorphism of these torsors there.

We spell out how that frame supplies a supported class, rather than choosing a lift of a vanishing restriction. In the completed derived mapping models of Lesson 5, M.6 and Lemma P.1.3.1, use the relative-cone construction of Lesson 6 A.2 and represent \(q\) by a closed cochain. Write \(F_b,F_r\) for its two classifying pullback chain maps. On the complement \(U\) the framed torsor isomorphism gives a chain homotopy \(K\) with
\[
 (F_b-F_r)|_U=dK+Kd.
 \tag{C.21.6}
\]
It is the ordinary nerve prism: in a string of composable transition arrows insert the isomorphism in each possible position and take the alternating sum. All inner faces cancel in pairs; the two remaining end faces are the two classifying maps. This verifies (C.21.6) directly. On a common trivializing cover the formula is finite in every nerve degree. Refining that cover preserves the formula, and the same prism for change of cover identifies its augmentations. Étale descent and the completed inverse limits retain these finite identities. Hence it defines the specified homotopy in the genuine equivariant enhancement, with all action faces and degeneracies.

In the relative complex
\(\operatorname{Cone}(C(\mathbb P^1\times X)\to C(U))[-1]\)
of any finite stage, use the pair
\[
 c_q=\big((F_b-F_r)q,Kq\big),\qquad
       d(c,u)=(dc,c|_U-du).
 \tag{C.21.7}
\]
It is closed by (C.21.6). Replacing \(q\) by \(q+dv\) changes it by the relative boundary of \(((F_b-F_r)v,Kv)\), since
\(Kdv=(F_b-F_r)v|_U-dKv\).
Thus its supported class is well defined and linear in the original cohomology class. The construction commutes with parameter pullback, change of frame and the constant-\(G\) nerve maps through their actual prism homotopies.

Let \(\pi:\mathbb P^1\times X\to X\). Forget the support in (C.21.7), and apply the actual smooth proper curve trace of Lesson 5, Theorems P.2.3.1–P.2.4.1, with the Kummer orientation normalized in Lesson 6 A.1.1. Define
\[
 z_q=-\pi_*\bigl(q(\mathcal P)-q(\mathcal P_{\mathrm{ref}})\bigr).
 \tag{C.21.8}
\]
The minus sign belongs to the lattice convention and is checked below. This trace lowers degree by two and twist by one, proving the degree in (C.21.4). The supported construction remains available to compare sums of modifications. Proper base change and the trace comparisons make these classes compatible on every finite stage and on all action-nerve levels. C.12 identifies these compatible classes with an actual class of the whole ind-Grassmannian, including all its component products.

For primitivity, construct the same framed relative class on \(\mathbb P^1\times Y_r\) for the full moving ordered chain of Lesson 8. Its support is the union of the graphs of the moving points. Off the diagonals those graphs are disjoint. Cochains supported on a finite disjoint union split as the direct sum of the individual support complexes: the corresponding closed support functor is the sum of their extension-by-zero functors, an equality checked on stalks. On the open obtained by deleting the other graphs, the full gluing and CRT comparison of Lesson 8 C.1–C.6 identifies the last framed torsor with the single input modification. Consequently the prism class restricts to that input's prism class on each support summand. Curve trace then gives the sum of the input \(z_q\)'s.

On a full collision the last framed torsor is the endpoint pullback of \(\mathcal P\); its off-point frame is the endpoint frame. Proper curve base change therefore identifies the same moving class with the endpoint pullback of (C.21.8). These statements concern the actual maps on the full families and their nilpotent parameters.

Cup with the moving class gives the actual morphism of the moving coefficient complex, shifted by \(2d-2\) and twisted by \(d-1\). Take its proper image on the full action nerve as in C.17.4. The canonical affine counits of C.17.3 transport this morphism to the base: both its source and its shifted target belong to the fully faithful essential image. Thus its lift is unique. Restriction to distinct sections is the sum just proved, and restriction to collision is the endpoint cup map. All finite block maps, action faces and degeneracies commute with those counits. Derived sections and the actual external cup comparison give (C.21.5). This repeats the morphism-level transport of C.19.3 with its actual higher degree and twist. At the zero modification the framed torsors are identical; their prism difference is zero, proving the unit assertion. ∎

#### C.21.3. The fixed-point derivative and the lattice sign

**Lemma C.21.3.1.** Restriction to a torus point is
\[
 z_q|_{t^\lambda}=D_\lambda q(u)\in S,
       \qquad \lambda\in L.
 \tag{C.21.9}
\]
The natural twist of this equality is \(E(d-1)\).

**Proof.** At \(t^\lambda\) the universal bundle has its torus reduction. For a character \(\chi\), its associated line on the curve is
\[
 \mathcal O_{\mathbb P^1}
       (-\langle\chi,\lambda\rangle\,0)\otimes k_\chi,
 \tag{C.21.10}
\]
where \(k_\chi\) denotes the geometric character line. The negative sign is exactly the full lattice gluing convention of Lesson 3, §3. Its equivariant first Chern class is
\(\chi(u)-\langle\chi,\lambda\rangle h\),
where \(h=c_1(\mathcal O(1))\).

The curve has trivial \(T\)-action. Its affine-line and point filtration, with the normalized supported point class of Lesson 6 A.1 and the compact affine trace, gives the two actual ordinary basis classes \(1,h\). Above degree two its ordinary cohomology is zero, so \(h^2=0\); the trivial equivariant action tensors this calculation with \(S\). Equivalently this is the relative projective Chern basis of C.14 for the trivial rank-two bundle. The actual trace gives
\[
 H_T^*(\mathbb P^1)=S[h]/(h^2),\qquad
             \pi_*h=1,\quad\pi_*1=0.
 \tag{C.21.11}
\]
The reference line has class \(\chi(u)\). Restriction of \(q\) along the torus classifying map is its actual polynomial in the character Chern classes, by C.14. Hence the two curve characteristic classes differ by
\[
 q(u-\lambda h)-q(u)
          =-D_\lambda q(u)\,h.
 \tag{C.21.12}
\]
Expansion of each polynomial monomial proves the equality, since \(h^2=0\). Taking the negative trace in (C.21.8) proves (C.21.9). The trace removes the \(E(1)\) of \(h\), leaving exactly \(E(d-1)\). No character, coefficient variable or lattice index is inverted. ∎

#### C.21.4. The higher operators are the full centralizer gradients

**Theorem C.21.4.1.** Let \(q_1,\ldots,q_r\) be homogeneous polynomial generators of \(R_0\), of degrees \(d_i\), and put \(f_i=q_i\circ\beta_\rho^{-1}\) on the dual adjoint quotient. In the adapted frame C.20.4, the actual \(z_q\)-operator is
\[
 \nabla_{B_H}(q\circ\beta_\rho^{-1})
           \bigl(\sigma_\rho(\beta_\rho(u)\bmod W)\bigr).
 \tag{C.21.13}
\]
In particular the \(z_{q_i}\) act by the entire basis of the full centralizer Lie bundle in B.5. They give the geometric module \(\omega_G(IC_\lambda)\) exactly the Kostant presentation
\[
 M(V_\lambda)=R_0\otimes_E V_\lambda,\qquad
 z_{q_i}\cdot v=
       \rho_{V_\lambda}(\nabla_{B_H}f_i(\sigma_\rho))v,
             \quad |z_{q_i}|=2d_i-2.
 \tag{C.21.14}
\]
The polynomial algebra
\(\mathcal B_\rho=R_0[z_{q_1},\ldots,z_{q_r}]\)
embeds in the actual whole equivariant cohomology ring; equality with that whole ring is not asserted.

**Proof.** Theorem C.21.2.1 and C.18.4 express cup with \(z_q\) as a homogeneous Lie element \(\eta_q\) of total degree \(2d-2\), retaining the Tate line. Cups of these even-degree classes commute with the determinant cup. Reconstruction identifies their commutator with \([\eta_q,\xi_\rho]\), so that bracket is zero. Thus in the adapted slice frame \(\eta_q\) is a section of the full centralizer Lie bundle.

Extend to the fraction field \(Q\) of \(S\) and then to an algebraic closure of \(Q\). The vector \(\beta_\rho(u)\) is regular semisimple: its root values are nonzero linear polynomials, since \(\beta_\rho\) is invertible. C.20.3 and B.3 identify \(\xi_\rho\) with its geometric adjoint orbit. Choose a conjugator taking it to \(\beta_\rho(u)\). The corresponding \(\eta_q\) then belongs to \(\mathfrak t_H\).

In every \(V_\lambda\), the eigenvalues of this Cartan vector \(\beta_\rho(u)\) distinguish its distinct weights. Therefore its \(\mu\)-weight blocks are precisely the transported actual fixed-point blocks of C.19.4. Actual cup restriction and C.21.9 show that \(\eta_q\) acts on such a block by \(D_\mu q(u)\). Lemma C.21.1.1 gives exactly the same scalar for the gradient in (C.21.13). The weights of a faithful \(H\)-representation span its full character lattice by the all-kernel argument of Lesson 2, Lemma 7.10. Decomposing that representation into its genuine simple modules proves that these scalar equalities determine the Cartan Lie element, including its centre. The two elements agree over the extended fraction field.

Invariant gradients are equivariant under \(H\), by invariance of \(B_H\) and the chain rule. Conjugating back consequently identifies \(\eta_q\) with the gradient at the slice point. Both are sections of the finite free module \(R_0\otimes_E\mathfrak h\). Its injection into the extended fraction-field module makes this equality hold already over \(R_0\), proving (C.21.13) on every parameter algebra.

The \(f_i\) are polynomial generators of the dual invariant ring by C.20.2. Their differentials form the cotangent basis of the quotient along the polynomial slice isomorphism. B.5 therefore makes their gradients the entire Lie-centralizer basis, with the specified total degrees. This proves the actual action and grading in (C.21.14). The full centre supplies its degree-zero gradient operators when \(d_i=1\).

For completeness these actual cup classes have no polynomial relation over \(R_0\). A relation would act as zero on every \(IC_\lambda\), and hence on every localized fixed-point block. Each label \(\mu\in L\) occurs: its dominant Weyl translate has that extremal weight with multiplicity one, and C.20.1 supplies the corresponding nonzero block. At the generic regular Cartan the map
\[
 \mu\longmapsto(D_\mu q_1(u),\ldots,D_\mu q_r(u))
 \tag{C.21.15}
\]
extends to an invertible linear map over \(Q\); equivalently the quotient differentials are independent there, as checked in B.2. The integral lattice \(L\) is polynomially dense in its affine space: in a lattice basis, repeated one-variable infinite-root arguments prove this for the integer grid. Its image under that invertible map is equally dense. The proposed relation, evaluated at (C.21.15), is therefore the zero polynomial in its operator variables over \(Q\). Injectivity \(R_0\to Q\) makes every coefficient zero already over \(R_0\). This proves the claimed embedding. It leaves the whole ring's degreewise component products intact. ∎

#### C.21.5. Morphisms over the actual whole cohomology ring

**Theorem C.21.5.1.** For two spherical IC generators, actual cup linearity gives
\[
 \operatorname{Hom}_{H_G^*(\operatorname{Gr}_G)}^*
       (\omega_G(IC_\lambda),\omega_G(IC_\mu))
   =\operatorname{Hom}_{\mathcal B_\rho}^*
       (M(V_\lambda),M(V_\mu)).
 \tag{C.21.16}
\]
Consequently C.16 and B.5 give an actual composition-preserving graded comparison
\[
 \operatorname{Ext}_{L^+G}^*(IC_\lambda,IC_\mu)
     \xrightarrow{\ \sim\ }
 \operatorname{Hom}_{A,H}^*
       (A\otimes V_\lambda,A\otimes V_\mu),
       \qquad A=E[\mathfrak h^*],
 \tag{C.21.17}
\]
with the deformation grading and full group of B.5. This is the geometric generator module and morphism comparison. An enhanced monoidal equivalence and dg formality remain separate requirements.

**Proof.** Write \(A_G=H_G^*(\operatorname{Gr}_G)\). Since the \(z_{q_i}\) are actual cup classes, every \(A_G\)-linear map is \(\mathcal B_\rho\)-linear. Conversely let \(F\) be \(\mathcal B_\rho\)-linear. The section \(\xi_\rho=\sigma_\rho\) commutes with itself and hence belongs to the full Lie-centralizer bundle. Its basis from C.21.4 writes it as an \(R_0\)-linear combination of the gradient operators. Thus \(F\) commutes with the actual determinant operator.

Extend \(F\) along the actual scalar comparison \(R_0\to S\) of C.14, then to \(Q\). The determinant eigenvalues \(\mu(\beta_\rho(u))\) distinguish labels, so \(F_Q\) preserves each fixed-point block. Every class of the whole \(A_T=H_T^*(\operatorname{Gr}_G)\) acts on that block by its scalar restriction at \(t^\mu\). This follows from the actual fixed-point restriction isomorphism of C.19.4, which is a module map for those whole classes. The scalar is the same on source and target blocks. Hence \(F_Q\) commutes with every such cup class.

The underlying source and target torus cohomology modules are finite free over \(S\) by C.17. A matrix commutator which becomes zero over \(Q\) is already zero over \(S\). In particular \(F\otimes_{R_0}S\) commutes with the restrictions of every class of \(A_G\). The faithful flatness of \(S/R_0\) makes the original commutator zero. Thus \(F\) is \(A_G\)-linear, proving (C.21.16). This uses scalar actions on the actual generic blocks, not a polynomial presentation of the whole ind-Grassmannian cohomology.

C.16.4 identifies the left side with the original finite-jet spherical generator Ext, through the actual cup comparison preserving Yoneda composition. C.21.4 identifies the right side with the exact modules of B.5, using \(B_H\) to identify the coadjoint coordinates and using the adapted pinning automorphism from C.20.4. Both preserve the original full group. B.5 then gives the right side of (C.21.17), including its specified grading and composition. Composing these isomorphisms proves (C.21.17). None of these graded Hom isomorphisms asserts a dg lift or eliminates higher composition obstructions. ∎

#### C.21.6. Two derivative and centre exercises

**Exercise C.21.6.1 (basic).** For \(G=\mathbb G_m\), take \(R_0=E[u]\), label \(n\), and \(q=u^d\). Compute \(z_q\), including \(d=1\), and check primitivity on labels \(n,m\).

**Solution.** The curve line at that label has class \(u-nh\), with \(h^2=0\). Thus \(-\pi_*((u-nh)^d-u^d)=dn\,u^{d-1}\). Its degree is \(2d-2\), with twist \(E(d-1)\). At \(d=1\) it is the degree-zero label operator \(n\), obtained without dividing by \(u\). At label \(n+m\) its value is \(d(n+m)u^{d-1}=dn u^{d-1}+dm u^{d-1}\), the actual tensor rule.

**Exercise C.21.6.2 (intermediate).** For \(G=GL_2\), use \(q_1=u_1+u_2\) and \(q_2=u_1u_2\). On the standard minuscule module with determinant cup matrix \(M\) of C.19.18, compute the two higher operators and verify the polynomial relation expressing \(M\) in their span.

**Solution.** The two labels are \((1,0)\) and \((0,1)\). Their \(q_1\)-derivatives are both one, while their \(q_2\)-derivatives are respectively \(u_2,u_1\). Therefore the two operators are \(I\) and \(\sigma_1I-M\). Equality holds over \(R_0\): localization computes their two distinct eigenspaces, and finite freeness descends the matrix equality. Explicitly \(M=\left(\begin{smallmatrix}0&-\sigma_2\\1&\sigma_1\end{smallmatrix}\right)\), so \(z_{q_2}=\left(\begin{smallmatrix}\sigma_1&\sigma_2\\-1&0\end{smallmatrix}\right)\). The standard trace form gives \(\nabla q_1=I\) and \(\nabla q_2(X)=(\operatorname{tr}X)I-X\), exactly these matrices. Finally \(q_{\rho,2}=\tfrac12(u_1^2+u_2^2)=q_1^2/2-q_2\) has gradient \(X\), and its actual derivative operator is \(\sigma_1 z_{q_1}-z_{q_2}=M\). The degree-zero central operator is essential to this integral formula.

### C.22. Tensor generators, their enhanced envelope and arithmetic purity

For the arithmetic statements in this section work over \(k=\overline{\mathbf F}_q\), with finite characteristic-zero coefficient field \(E\) containing \(a\) such that \(a^2=q\). The underlying split group and all the rootwise constructions descend to the finite field. Taking a square power of its prime field makes \(a\) a rational integer, if that is needed to keep the original coefficient field. Let \(A_\lambda\) denote the raw geometric IC with its canonical Weil map multiplied by \(a^{-d_\lambda}\). This is a normalization of the Weil map; it changes neither the underlying geometric object nor its cohomological shift. In the statements not mentioning Frobenius, retain the general geometric coefficient scope of C.21.

Write
\[
 A=\operatorname{Sym}_E(\mathfrak h[-2]).
 \tag{C.22.1}
\]
Thus each linear polynomial has cohomological degree two and the differential is zero. Put a representation \(V\) in degree zero in the free equivariant dg module \(F_V=A\otimes V\). On slice restriction, its grading is the coefficient-plus-principal grading proved in B.5. The notation \(\operatorname{Perf}^H(A)\) means the finite shift, cone and retract envelope of these free modules, exactly as in §8.1.

![Actual tensor generators, their arithmetic enhanced envelope and the locally finite weight model](assets/tensor-generators-weight-model.png)

The first panel distinguishes the actual graded tensor comparison from the enhanced arithmetic equivalence of finite envelopes. The second records the normalized IC Weil maps \(A_\lambda\), the identity action on multiplicities and the sole Ext eigenvalues; the diagram's IC labels denote those same normalized maps. The third gives the strict, locally finite hypothesis and the exact weight-versus-degree truncation. The target keeps the full \(H\), with polynomial coordinates in cohomological degree two. Proofs C.22.1.1–C.22.4.1 establish these maps. Exercise C.22.5.2 shows why cohomological purity alone does not authorize a termwise locally finite replacement. Editable SVG source.

#### C.22.1. The actual tensor comparison on every generator morphism

**Theorem C.22.1.1.** Let \(\mathcal E_G^\oplus\) be the graded category of spherical perverse objects, with their actual spherical Ext as morphisms and the corrected Satake convolution symmetry. The comparisons of C.21 extend to a graded symmetric monoidal equivalence
\[
 \Phi:\mathcal E_G^\oplus\xrightarrow{\ \sim\ }\mathcal F_H,
       \qquad P\longmapsto F_{\omega(P)},
 \tag{C.22.2}
\]
where \(\mathcal F_H\) has the free modules \(F_V\), their genuine graded \(A,H\)-linear Hom, and tensor over \(A\). For homogeneous generator morphisms \(b,c\),
\[
 \Phi(b*c)=\Phi(b)\otimes_A\Phi(c).
 \tag{C.22.3}
\]
This is a comparison of the actual graded tensor operations. It does not yet identify the enhanced convolution functor.

**Proof.** Semisimplicity of the geometric spherical heart makes every object a finite sum of IC generators. Thus C.21.5 extends by matrices to a fully faithful graded functor with the displayed objects. Every finite-dimensional representation of the original \(H\) is a finite sum of its true simple modules, by Lesson 11, so these objects give its whole target.

The required naturality is for derived morphisms, rather than just degree-zero maps in the heart. Choose common finite supports and jet bounds for \(b:P\to P'[n]\) and \(c:Q\to Q'[m]\). Genuine equivariant pullback and descent give their external map on the full moving ordered chain. Its target is the moving coefficient for \(P',Q'\), shifted by \(n+m\). The proper images of both coefficient complexes lie in the affine pullback essential image of C.17.3, since the proved constant-cohomology property is unchanged by shifts. The actual affine counits therefore transport this map uniquely on every action-nerve level, including the action face, and on all finite block diagrams.

At distinct points its derived sections are the actual external product map. At collision they are the actual convolution map. The external cup comparison in C.17.2 is functorial for these coefficient maps: its construction uses the tensor of representatives, the projection comparison and composed proper counits; each commutes with a coefficient morphism, with the usual tensor sign. Therefore
\[
 \omega_G(b*c)=\omega_G(b)\otimes_{R_0}\omega_G(c)
 \tag{C.22.4}
\]
under the actual tensor isomorphism C.17.4. In particular the argument did not require an arbitrarily chosen lift of a morphism to fusion.

There is no hidden odd sign on the unshifted generator category. Distinct component supports have zero Ext. Within one component the IC dimensions have the same parity, since a simple coroot changes the dimension height by two. Their star and costalk cell coefficients thus have matching parity. The actual comparison C.16, with the even coefficient ring of C.10, makes their odd Ext zero. Homogeneous nonzero \(b,c\) have even degrees. The shifted finite envelope will use the usual dg signs.

The frame of C.20.4 is tensor on objects and on the heart. Substituting it in (C.22.4) makes the slice module map the coefficient tensor of the two maps in C.21. This equals restriction of their coherent tensor product: on every slice point it is literally the matrix tensor product over the common coefficient ring. The full faithfulness in B.5 makes the inverse polynomial extension equal to that coherent tensor map, proving (C.22.3).

The same tensor frame carries the associator, unit and corrected symmetry on the heart to the usual associator, unit and flip of representations. These are the degree-zero structural maps in the graded category. The genuine finite-set comparisons of C.17 preserve every pentagon, unit and permutation identity, and B.5 preserves their compositions. Hence all diagrams for a graded symmetric monoidal functor commute. This proves (C.22.2) with its actual structural maps. ∎

#### C.22.2. The enhanced arithmetic free-generator envelope

**Theorem C.22.2.1.** At the stated arithmetic coefficients and geometric base, there is an equivalence of enhanced categories
\[
 D^b_{L^+G,\mathrm{sph}}(\operatorname{Gr}_G,E)
       \xrightarrow{\ \sim\ }\operatorname{Perf}^H(A)
 \tag{C.22.5}
\]
sending every IC generator to \(A\otimes V_\lambda\). The left category has bounded, finite-supported objects. This theorem does not assert that the chosen enhanced equivalence is monoidal, or that it has been transferred to complex coefficients.

**Proof.** The actual arithmetic formality and generator envelope A.4 identify the left side with the finite-cone and retract envelope of the graded Ext category with zero differential. Its hypotheses are the split finite-field geometry, the actual IC stalk/costalk Frobenius of Lesson 12 C.3, and the enhanced Frobenius lift in A.4. The nonresonance proof A.3 permits its Jordan parts. C.22.1 identifies that formal graded category, including composition, with \(\mathcal F_H\).

We check that its envelope is the asserted dg module envelope, rather than invoking an ordinary coherent derived category in its place. For a rational \(H\)-equivariant dg \(A\)-module \(M\),
\[
 \operatorname{Hom}_{A,H}^\bullet(F_V,M)
         =(V^\vee\otimes_E M)^H .
 \tag{C.22.6}
\]
Invariants of rational \(H\)-modules are exact in characteristic zero. For an arbitrary rational module this follows from the finite-dimensional proof: an element and a chosen lift lie in finite-dimensional \(H\)-stable spans, and complete reducibility splits the resulting finite image. An invariant image vector consequently has an invariant lift. Applying this to the cycles and boundaries in an acyclic dg module proves that (C.22.6) is acyclic whenever \(M\) is acyclic. Thus each \(F_V\) computes its derived Hom directly.

In particular the actual dg Hom between two free objects is
\[
 \operatorname{Hom}_{A,H}^\bullet(F_V,F_W)
       =(A\otimes V^\vee\otimes W)^H
 \tag{C.22.7}
\]
with differential zero, the very graded category \(\mathcal F_H\). There are no extra rational group cohomology terms. Its enriched Yoneda comparison is an isomorphism on these free generators, with their actual composition. In each variable it extends through shifts and cones by the corresponding mapping-cone identity, and through retracts by the image of a commuting idempotent. This proves an enhanced equivalence of its finite envelope with the finite shift, cone and retract subcategory of equivariant dg \(A\)-modules. That subcategory is our definition of \(\operatorname{Perf}^H(A)\).

Composing this equivalence with A.4 and C.22.1 gives (C.22.5), with the specified generator images. Although C.22.1 is monoidal on the graded generators, the formality coordinate change in A.4 was constructed for composition. A comparison of the enhanced convolution bifunctor and its coherent structural maps is still needed to make this chosen equivalence monoidal. ∎

#### C.22.3. Scalar Frobenius on ordinary IC cohomology and tensor multiplicities

**Theorem C.22.3.1.** The actual normalized ordinary cohomology of \(A_\lambda\) has scalar Frobenius
\[
 F|_{H^n(\operatorname{Gr}_G,A_\lambda)}
                        =a^n\operatorname{id}.
 \tag{C.22.8}
\]
For any finite convolution word \(P=A_{\lambda_1}*\cdots*A_{\lambda_r}\), every multiplicity space in its canonical geometric isotypic decomposition
\[
 P=\bigoplus_\nu A_\nu\otimes_E M_\nu(P),
        \qquad M_\nu(P)=\operatorname{Hom}_{\mathrm{Perv}}(A_\nu,P),
 \tag{C.22.9}
\]
has the identity Frobenius. Consequently every degree-\(n\) Ext between normalized convolution words has sole eigenvalue \(a^n\), with Jordan parts allowed. Associators, units and the corrected permutations on these words retain their actual arithmetic structures.

**Proof.** The rootwise source \(\mathcal B_\lambda\) of Lesson 11 C.2.1 is an iterated wall projective-line bundle, beginning with a point, defined over \(\mathbf F_q\). On each last line choose the global character line of C.16.1, whose fibre degree is a nonzero integer \(-m\). The class
\(-c_1(\mathcal L)/m\)
has fibre trace one. The coefficient field has characteristic zero, so this division is allowed even when the geometric wall central kernel is nonsmooth.

For a wall projection \(p\), its classes \(1,-c_1(\mathcal L)/m\) give the actual proper-image comparison
\[
 E\oplus E(-1)[-2]\xrightarrow{\ \sim\ }Rp_*E.
 \tag{C.22.10}
\]
Indeed on every geometric fibre \(\mathbb P^1\) they give its two independent normalized basis classes; actual proper base change checks the cone at those fibres. The line and divisor transitions are defined over the finite field. Kummer Frobenius sends its untwisted degree-two class to \(q\) times that class. Thus (C.22.10) is compatible with the two displayed Frobenius scalars.

Iterate (C.22.10). Products of its degree-two classes give an actual basis of \(H^{2j}(\mathcal B_\lambda,E)\), on which Frobenius is \(q^j\) times the identity, and the odd groups vanish. For the raw resolution image \(B_\lambda=Rf_{\lambda*}E[d_\lambda]\), its ordinary degree-\(n\) cohomology therefore has scalar \(q^{(n+d_\lambda)/2}\).

Use the actual underlying IC retractions \(I_\lambda\xrightarrow{u}B_\lambda\xrightarrow{v}I_\lambda\), with \(vu=1\) and both dense restrictions the identity, proved in Lesson 11 C.4.2. The compression proof of Lesson 12 C.2 applies also to ordinary cohomology on this proper support. Here is its required transport. If \(s:X\to\operatorname{Spec}k\) is the support map, the field square \(s\sigma_X=\sigma_ks\), actual proper base change and pullback composition identify \(R\Gamma(X,\sigma_X^*K)\) with the pullback of \(R\Gamma(X,K)\) to the geometric field point. Field pullback on its coefficient-module category is canonically the identity, naturally for every underlying derived map.

The composite \(v\alpha_{B_\lambda}\sigma^*u\) is the canonical raw IC Weil map: it has the same identity on the dense cell, and intermediate extension excludes an endomorphism with boundary-supported image. With the just-specified global transport, its degree-\(n\) action is therefore
\[
 H^n(v)\,F_{B_\lambda}\,H^n(u)
         =q^{(n+d_\lambda)/2}\operatorname{id}.
 \tag{C.22.11}
\]
No separate arithmetic equivariance of \(u,v\) was assumed. Multiplication of the Weil map by \(a^{-d_\lambda}\) gives (C.22.8).

The actual ordinary cohomology tensor comparison of Lesson 8 and C.17 is arithmetic-compatible: all its gluing, proper maps, normalization traces and external cup maps descend to the finite field. Hence the degree-\(n\) cohomology of \(P\) also has scalar \(a^n\), as a tensor of the scalars in (C.22.8).

The geometric semisimple heart gives the canonical evaluation isomorphism (C.22.9). It is arithmetic-equivariant when \(M_\nu(P)\) has the conjugation action defined by the two Weil maps. Frobenius fixes the labels, since their rootwise data are split. Applying \(H^n\) gives a direct sum of \(H^n(A_\nu)\otimes M_\nu(P)\). For each occurring \(\nu\), choose \(n\) with \(H^n(A_\nu)\ne0\); such an \(n\) exists by the proved faithfulness of total cohomology. On this summand the two scalar formulas force
\(a^n(1\otimes F_{M_\nu})=a^n1\).
Tensoring with a nonzero finite-dimensional vector space is faithful, so \(F_{M_\nu}=1\), proving the assertion even against a possible Jordan part.

Decompose both convolution words by (C.22.9). Their actual Ext is the finite sum of IC Ext tensored with coefficient Hom between identity-Frobenius multiplicities. A.2 gives its sole eigenvalue \(a^n\). The structural maps mentioned in the theorem were actual finite-field fusion maps in Lesson 8; normalization uses the same scalar on every ordered input. They consequently retain their descended arithmetic structures under this isotypic description. ∎

#### C.22.4. A multiplicative truncation when the cochain action is locally finite

**Theorem C.22.4.1.** Let \(C\) be a dg category, dg algebra, or diagram of complexes over \(E\), with a strict chain automorphism \(F\), fixing every object in the category case. Suppose \(F\) is locally finite on every cochain vector, all its eigenvalues are among \(a^w\) for integers \(w\), and \(a\) is not a root of unity. Suppose
\[
 H^n(C)\text{ has sole eigenvalue }a^n.
 \tag{C.22.12}
\]
Its composition and specified degree-zero multilinear structure maps commute strictly with \(F\). Then there is a natural multiplicative zigzag
\[
 C\ \longleftarrow\ D(C)\
                 \longrightarrow\ H^*(C)
 \tag{C.22.13}
\]
of quasi-isomorphisms, retaining the ordinary graded structure. For a strictly \(F\)-equivariant higher operation of degree \(-r<0\), its restriction to \(D(C)\) lands in \(D(C)\) and its projection to \(H^*(C)\) is zero. The locally finite and strict cochain hypotheses in this statement must be verified before applying it to an enhanced geometric diagram.

**Proof.** Local finiteness means that each vector lies in a finite-dimensional \(F\)-stable space. Primary decomposition there, followed by its unique compatible inclusions, gives the canonical direct sum
\[
 C=\bigoplus_{w\in\mathbb Z}C_w,\qquad
 C_w=\{x:(F-a^w)^N x=0\text{ for some }N\}.
 \tag{C.22.14}
\]
Distinct integer weights have distinct eigenvalues. The differential preserves these subspaces. Products add their weights: on finite-dimensional primary spaces the tensor automorphism has sole eigenvalue \(a^{w+v}\), since its remaining part is a polynomial without constant term in commuting nilpotent operators. Every \(F\)-equivariant multilinear map therefore sends input weights to their sum.

Define, in cohomological degree \(n\),
\[
 D(C)^n=
   \bigoplus_{w>n}C_w^n
       \ \oplus\
   \ker(d:C_n^n\to C_n^{n+1}).
 \tag{C.22.15}
\]
Weights below \(n\) are omitted. This is a subcomplex. If \(w>n+1\), the differential remains in the full \(w\)-summand; if \(w=n+1\), it lands in the diagonal cycle term; the differential of a diagonal cycle is zero. For a fixed weight \(w\) it is exactly the good subcomplex truncation \(\tau_{\leq w}C_w\). Equation (C.22.12) says that \(H^n(C_w)=0\) for \(n\ne w\), so its inclusion into \(C_w\) is a quasi-isomorphism. Direct sums of vector-space complexes are exact, proving the left arrow in (C.22.13).

The right arrow takes a diagonal cycle to its cohomology class and every term of weight \(w>n\) to zero. It is a chain map: an off-diagonal differential can reach the diagonal only as an ordinary boundary. On the sole weight-\(w\) cohomology group it is its defining quotient map, so it too is a quasi-isomorphism.

If two inputs have weights at least their degrees, their product has that property. When both weights equal the degrees, both inputs are cycles and the degree-zero chain product is a cycle. Thus (C.22.15) is closed under composition and the degree-zero chain structure maps. The right arrow preserves them: any strict weight excess on an input leaves an excess on the output, and on diagonal cycles it is ordinary cohomological composition. Units lie in degree and weight zero, and are retained. These observations also prove naturality in strictly \(F\)-equivariant chain maps.

Tensor comparisons are compatible as well. There is a natural product map \(D(C)\otimes D(C')\to D(C\otimes C')\); both paths to \(C\otimes C'\) are the inclusion of the same tensor of cochains. Tensoring quasi-isomorphisms over a field preserves them, even for unbounded complexes: an acyclic vector-space complex has a contracting homotopy by complements to its cycles, and tensoring that homotopy contracts its tensor with any complex. The two inclusion maps are quasi-isomorphisms, so this product comparison is one. The same multiplication of representatives proves its associative and permutation identities.

Finally an operation of degree \(-r\) sends inputs of degrees \(n_i\) and weights \(w_i\ge n_i\) to output degree \(\sum n_i-r\) and weight \(\sum w_i\). For \(r>0\) that output has strictly larger weight than degree. It belongs to the full off-diagonal term of \(D(C)\), and its cohomology projection is zero. Restriction thus retains any supplied operation identities; projection kills their negative-degree terms. Jordan parts have been retained throughout by primary spaces, not discarded by diagonalization. ∎

#### C.22.5. Two cochain-model exercises

**Exercise C.22.5.1 (intermediate).** Let \(C=E[x,z]\otimes\Lambda(y)\), with \(|x|=|z|=2,|y|=1\), \(dy=z\) and \(dx=dz=0\). Give all three generators weight two and let \(F\) act by \(a^2\) on them. Compute \(D(C)\) and its map to cohomology.

**Solution.** The polynomial generators give diagonal cycle monomials \(x^i z^j\); the monomials \(yx^i z^j\) have weight one above their cohomological degree. These exhaust the basis, so \(D(C)=C\). Their differentials are \(x^i z^{j+1}\). Thus every monomial containing \(z\) is a boundary, the odd terms have no cycles, and \(H^*(C)=E[x]\). The right arrow sends \(x\) to \(x\), \(z,y\) to zero. It is multiplicative and retains the weight-two class of \(x\). The calculation demonstrates why diagonal boundaries are killed, while an off-diagonal primitive is retained until the projection.

**Exercise C.22.5.2 (advanced).** In degrees zero and one take \(C^0=C^1=E[t,t^{-1}]\), differential multiplication by \(t-a\), and chain automorphism multiplication by \(t\). Compute its cohomology and show why taking the locally finite subspace of each term is not a valid replacement.

**Solution.** The differential is injective in the Laurent polynomial domain and has cokernel \(E\), by evaluation at \(t=a\). Thus \(H^0=0\), and \(H^1=E\) with Frobenius \(a=a^1\), exactly diagonal purity. Yet every nonzero Laurent polynomial has linearly independent translates among sufficiently many powers of \(t\): a finite polynomial relation among them would contradict the domain property. There is no nonzero locally finite vector in either term. Taking those termwise subspaces gives the zero complex and loses \(H^1\). A geometric application must construct a compatible derived locally finite model, rather than making that termwise substitution from cohomological purity alone.

## 11. Scope and free reading

The proved statements are the unit self-Ext formula (2.3), the general invariant-polynomial classifying-space ring in §3, the torus symmetric tensor model over every characteristic-zero field in §5, the two Koszul endomorphism calculations and generated-category equivalences in §6, and the compactness distinction in §7. The five exercises use those proofs. Appendix A proves arithmetic stabilizer cohomology, actual equivariant Ext purity, minimal-model transfer, nonresonant Frobenius formality and the actual spherical generator envelope; it also proves the one-sided-weight counterexample. Appendix B proves the polynomial Kostant slice, the full smooth universal centralizer, extension across the nonregular locus, exact equivariant coherent restriction and a composition-preserving graded comparison on every free dual polynomial generator. Its rank-one and rank-two examples retain finite centres and nilpotent parameter algebras. Appendix C proves cellular Euler localization, opposite-loop open charts on all parameter algebras, their actual contraction comparison, and the integral Ext-to-Hom cell criterion preserving composition. Its general weight implication retains its explicit compact-support hypothesis. C.12–C.16 instead prove actual whole-Grassmannian restriction, finite-jet and constant-group comparison, Weyl descent and unconditional spherical IC stalk surjectivity, giving the original generator Ext-to-module-Hom map. C.17–C.20 construct the actual graded cohomology tensor functor, an augmentation-preserving tensor frame, the full determinant cup operator, its regularity and actual adjoint quotient. C.21 constructs the higher primitive cup operators, identifies all full centralizer gradients and geometric Kostant modules, and proves the actual graded generator morphism comparison with composition. C.22 proves the actual graded symmetric tensor comparison and enhanced arithmetic finite-envelope equivalence, scalar normalized IC cohomology and identity tensor multiplicities, and a multiplicative weight model under explicit strict locally finite cochain hypotheses. The enhanced monoidal upgrade, its compatible cochain model, complex coefficient comparisons, and the renormalized, singular-support and factorization theorems of §8 remain necessary.

Free further reading:

- [Luigi Lunardon, *Some remarks on Dupont contraction*, arXiv:1807.02517](https://arxiv.org/abs/1807.02517), for polynomial simplex forms and simplicial comparisons.

- [Bezrukavnikov–Finkelberg, *Equivariant Satake category and Kostant–Whittaker reduction*, arXiv:0707.3799v4](https://arxiv.org/abs/0707.3799v4), Theorem 5 and §6.6.
- [Arinkin–Gaitsgory, *Singular support of coherent sheaves, and the geometric Langlands conjecture*, arXiv:1201.6343v4](https://arxiv.org/abs/1201.6343v4), §§12.2–12.5.
- [Campbell–Raskin, *Langlands duality on the Beilinson–Drinfeld Grassmannian*, arXiv:2310.19734v2](https://arxiv.org/abs/2310.19734v2), §§5.7, 6.3, 6.6 and 8.10.
- [Gaitsgory–Raskin, *Proof of the geometric Langlands conjecture II: Kac–Moody localization and the FLE*, arXiv:2405.03648v3](https://arxiv.org/abs/2405.03648v3), §§1.5–1.8 and Appendix E.

The proofs from earlier programme lessons are linked at the points where they are used. The reading list does not replace any of them.
