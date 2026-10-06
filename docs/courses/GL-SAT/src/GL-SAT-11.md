# The Mirković–Vilonen theorem: identifying the dual group

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Public domain (CC0).*

The weight functors identify a torus in the reconstructed group. To identify its roots, one must also determine the integral steps along a rank-one weight string. A chamber alone does not determine those steps: the roots of \(SL_2\) and \(PGL_2\) have different divisibilities in their character lattices. We keep that distinction throughout the argument.

We work with classical constructible sheaves on the complex affine Grassmannian, with coefficients in an arbitrary characteristic-zero field \(\Lambda\). Fix \(T\subset B\subset G\), and put
\[
L=X_*(T),\qquad Q^\vee=\sum_i\mathbb Z\alpha_i^\vee,
\qquad h_G(\nu)=\langle2\rho_G,\nu\rangle.
\tag{1.1}
\]
The simple objects are \(IC_\lambda\), for dominant \(\lambda\in L\). Lesson 10 reconstructs a geometrically connected affine group \(H_G\), with a closed maximal split torus
\(\widehat T=D_\Lambda(L)\). Its character lattice is \(L\), and
\[
H(IC_\lambda)_\nu=F_\nu(IC_\lambda).
\tag{1.2}
\]
The tensor comparison in (1.2) is the actual canonical comparison of Lesson 10, §5.

Some conclusions below have the following explicit hypothesis:
\[
\text{(S): every object of }\operatorname{Sat}_G(\Lambda)
\text{ is a finite direct sum of simple objects.}
\tag{1.3}
\]
Lesson 6, Proposition 5.2 proves (S) from its IC stalk and costalk parity hypothesis (P). The general proof of (P) remains outside the results established there. Whenever (S) is assumed here, the resulting theorem is conditional on that hypothesis. The Levi functor, rank-one simple characters and minuscule weight calculations will not require it.

## 1. The largest weight and the component of a simple object

**Lemma 1.1.** For every dominant \(\lambda\), the largest \(h_G\)-weight of \(H(IC_\lambda)\) is \(\lambda\), its weight space is one dimensional, and every nonzero weight \(\nu\) satisfies
\[
\nu^+\le\lambda,\qquad \nu-\lambda\in Q^\vee.
\tag{1.4}
\]
Here \(\nu^+\) is the dominant representative in the original Weyl group of \(G\).

**Proof.** If \(S_\nu\) meets the support \(Z_\lambda\), contraction puts \(t^\nu\) in that closed support. Lesson 4, Theorem 3.5 and §5 gives both assertions in (1.4). For a dominant functional \(2\rho_G\),
\[
h_G(\nu)\le h_G(\nu^+)\le h_G(\lambda).
\]
The second inequality is strict when \(\nu^+\ne\lambda\), since \(2\rho_G\) pairs positively with each simple coroot. The first is strict unless \(\nu\) is already dominant: move to the dominant chamber by reflections in walls with negative pairing; every nontrivial move increases this functional. Thus equality occurs only at \(\nu=\lambda\).

Lesson 5, §9 proves that \(S_\lambda\cap Z_\lambda\) is a dense open irreducible subset of dimension \(d_\lambda=h_G(\lambda)\). Its intersection with the open Schubert orbit is again dense and irreducible. There \(IC_\lambda=\Lambda[d_\lambda]\), whose top compact cohomology is \(\Lambda\), by the oriented top-degree calculation of Lesson 5, §20. Each boundary orbit has dimension at most \(d_\lambda-2\). The strict IC stalk bound and the semi-infinite dimension formula give compact cohomology on its slice only in degrees at most \(h_G(\lambda)-2\). The closed–open triangle therefore identifies this top group with \(F_\lambda(IC_\lambda)\). This proves the asserted one-dimensional line. \(\square\)

The opposite extreme is also one dimensional:
\(F_{w_0\lambda}(IC_\lambda)=\Lambda\), by Lesson 10, §1. Neither extreme calculation assumes semisimplicity.

**Corollary 1.2.** A one-dimensional representation of \(H_G\) on which \(\widehat T\) acts trivially is trivial.

**Proof.** It is simple, hence corresponds to some \(IC_\lambda\). Its one-dimensional lowest weight has character \(w_0\lambda\). Triviality on \(\widehat T\) forces \(\lambda=0\), and the simple object is the tensor unit. \(\square\)

## 2. Levi constant terms

For a standard parabolic \(P=M U\), choose a cocharacter central in \(M\), positive on the roots of \(U\), and zero on the roots of \(M\). The corresponding attracting correspondence is
\[
\operatorname{Gr}_G\xleftarrow{\ i\ }\operatorname{Gr}_P
\xrightarrow{\ q\ }\operatorname{Gr}_M.
\tag{2.1}
\]
The normalized constant term on component \(\kappa\in\pi_1(M)=L/Q_M^\vee\) is
\[
\operatorname{CT}_P(A)|_\kappa
=\bigl(Rq_!i^*A\bigr)|_\kappa[d_P(\kappa)],
\qquad
d_P(\kappa)=\langle2\rho_G-2\rho_M,\nu\rangle,
\quad [\nu]=\kappa.
\tag{2.2}
\]
This is well defined: \(2\rho_G-2\rho_M\) annihilates the coroots of \(M\). The shift is part of the functor.

The proof of its perverse, exact and tensor properties is given below after the explicit rank-one calculations. For \(M=T\), (2.2) is already the proved functor
\[
\operatorname{CT}_B(A)=\bigoplus_{\nu\in L}F_\nu(A)\otimes\delta_\nu
\tag{2.3}
\]
from Lesson 10, §§4–5. In particular it is an exact symmetric tensor functor without (S).

## 3. Rank one: finite quotients and all simple characters

We first identify finite reductive quotients of the reconstructed affine groups. This determines every simple representation, but it does not by itself rule out extensions in the full category.

### 3.1. The group \(PGL_2\)

Write \(L=\mathbb Z\omega^\vee\), with the positive coroot \(\alpha^\vee=2\omega^\vee\). The minuscule Schubert variety is \(\mathbb P^1\), and
\(A=IC_{\omega^\vee}=\Lambda_{\mathbb P^1}[1]\). Its two semi-infinite slices are an affine line and a point. Thus
\[
V=H(A),\qquad \dim V=2,
\qquad V_{\omega^\vee}=\Lambda,quad
V_{-\omega^\vee}=\Lambda.
\tag{3.1}
\]
The object \(A\) is simple, so \(V\) is absolutely simple by Lesson 10, §7.2. Its determinant has trivial \(\widehat T\)-character, hence is trivial by Corollary 1.2. Let \(R\) be the schematic image of
\(H_{PGL_2}\to SL(V)\). It is a connected smooth algebraic group: its coordinate Hopf algebra is the finitely generated algebra of matrix coefficients, the map to its spectrum is faithfully flat by Lesson 9, §7, and characteristic-zero smoothness is Lie algebras and smoothness, Theorem 4.3.

The group \(R\) is reductive. A connected normal unipotent subgroup has a nonzero fixed vector in \(V\), by Diagonalizable groups and reductivity, Lemma 2.A. Normality makes its fixed space \(R\)-stable; simplicity makes it all of \(V\), and faithfulness makes the subgroup trivial. A proper connected reductive subgroup of \(SL_2\) is a torus or the trivial group: its maximal torus has rank at most one; if it has a root, its rank-one root subgroups and torus already have dimension three, hence fill \(SL_2\), by Roots and reductive groups of rank one, §§2–3. A torus cannot act irreducibly on a two-dimensional space over an algebraic closure. Therefore
\[
H_{PGL_2}\twoheadrightarrow SL_2.
\tag{3.2}
\]
This identification also holds over \(\Lambda\): the weight torus has diagonal action \(\operatorname{diag}(z,z^{-1})\), and the image after algebraic closure is the whole closed subgroup \(SL(V)\).

The representation \(\operatorname{Sym}^nV\) of \(SL_2\) is absolutely simple in characteristic zero. Its standard monomials give weights
\[
(n-2j)\omega^\vee,qquad 0\le j\le n,
\tag{3.3}
\]
each once. For completeness, the usual raising and lowering operators send consecutive monomials to nonzero multiples of their neighbours. A nonzero invariant subspace is stable under the torus and contains a weight vector; successive raising reaches the highest monomial, and successive lowering then reaches every monomial. This proves simplicity. Inflating along the faithfully flat map (3.2) preserves simplicity. Its lowest weight is \(-n\omega^\vee\), so the unique simple label is \(n\omega^\vee\), by Lesson 10, §7.2 and its lowest-weight formula. Consequently
\[
H(IC_{n\omega^\vee})\simeq\operatorname{Sym}^nV,
\tag{3.4}
\]
with the characters (3.3), without assuming (S). All simple objects thus factor through (3.2).

Section 3.3 below proves (S) for this rank-one category without a general IC parity theorem. Every object then factors through this quotient, and (3.2) is an isomorphism: every matrix coefficient of every object belongs to the quotient Hopf algebra, and these coefficients generate the reconstructed Hopf algebra. Thus
\[
\operatorname{Sat}_{PGL_2}(\Lambda)\simeq\operatorname{Rep}_\Lambda(SL_2).
\tag{3.5}
\]

### 3.2. The group \(SL_2\)

Now \(L=\mathbb Z\alpha^\vee\). The first nontrivial Schubert closure is the projective quadratic cone of Lesson 6, §7. Its rational link calculation proves
\(A=IC_{\alpha^\vee}=\Lambda_{Z_{\alpha^\vee}}[2]\). The slices are \(\mathbb A^2,\mathbb A^1,\mathrm{pt}\), giving
\[
V=H(A),\qquad
V_{\alpha^\vee}=V_0=V_{-\alpha^\vee}=\Lambda,
\qquad\dim V=3.
\tag{3.6}
\]
Rigidity of Lesson 7, §8 and the identity \(A^\vee=A\) give a nondegenerate invariant bilinear form on \(V\). Since \(\operatorname{Hom}(A,A^\vee)\) is one dimensional, transposing this form multiplies it by a scalar whose square is one. It is symmetric or alternating. An alternating nondegenerate form has even dimension: in odd dimension its skew matrix has determinant equal to its own negative. Thus the form is symmetric. Its determinant character is trivial by Corollary 1.2.

The schematic image \(R\) therefore lies in \(SO(V)\). It is connected, smooth and reductive by the same faithful-simple argument as above. In a weight basis its quadratic form is \(c z^2+bxy\), with \(b,c\ne0\): opposite weight lines pair, and their self-pairings vanish by torus invariance. Scale the form by \(c^{-1}\) and replace one of \(x,y\) by \((b/c)\) times itself. This identifies its orthogonal group with that of \(z^2+xy\), without taking square roots.

Here is the group identification needed. The adjoint action of \(SL_2\) on
\(\left(\begin{smallmatrix}z&x\\y&-z\end{smallmatrix}\right)\)
preserves its determinant \(-z^2-xy\). Over every coefficient algebra a matrix commuting with the three matrices \(E,F,H\) is scalar: commuting with \(H=\operatorname{diag}(1,-1)\) kills the off-diagonal entries since two is invertible, and commuting with \(E\) makes the two diagonal entries equal. The kernel is therefore exactly \(\mu_2\). The quotient \(PGL_2=SL_2/\mu_2\), proved by the central-quotient construction in Root data, Weyl chambers and the Bruhat decomposition, §7, embeds as a closed subgroup by Group schemes over a field, Theorem 5.9. Its differential is injective because a trace-zero scalar is zero, and both the source Lie algebra and the orthogonal Lie algebra have dimension three. The latter assertion follows by writing its equation \(X^{\mathsf t}J+JX=0\): multiplication by the invertible Gram matrix identifies its solutions with the three-dimensional space of skew matrices. The same linearization and translations show that the orthogonal group is smooth of dimension three. The image of \(PGL_2\) is consequently its identity component: a closed subgroup of the same dimension contains that component, which is irreducible for a connected smooth group.

A torus acting faithfully in a three-dimensional orthogonal space has rank at most one. Its characters pair as \(\chi,-\chi\), with the remaining character zero, and hence span a lattice of rank at most one. Since \(R\) acts irreducibly, it is not a torus; a connected reductive group of rank one with a root has dimension three, by the rank-one root construction of Roots and reductive groups of rank one, §§7–8. Thus \(R\) is that same orthogonal identity component, giving
\[
H_{SL_2}\twoheadrightarrow PGL_2.
\tag{3.7}
\]
The simple \(PGL_2\)-representations are \(\operatorname{Sym}^{2n}\) of the two-dimensional \(SL_2\)-representation: its central \(-1\) acts as \((-1)^{2n}=1\). Their weights in the quotient torus lattice are
\[
j\alpha^\vee,qquad -n\le j\le n,
\tag{3.8}
\]
each once. The same inflation and lowest-weight argument identifies them with \(H(IC_{n\alpha^\vee})\). Section 3.3 proves (S) for this category too, so (3.7) is an isomorphism, and
\[
\operatorname{Sat}_{SL_2}(\Lambda)\simeq\operatorname{Rep}_\Lambda(PGL_2).
\tag{3.9}
\]

The integral root normalization is visible already in these quotients. For \(PGL_2\), the dual root is \(2\omega^\vee\), the original coroot. For \(SL_2\), it is \(\alpha^\vee\), again the original coroot; the original root is twice the primitive character and becomes the coroot of the dual adjoint group.

![Rank-one weight strings with their integral root steps](assets/GL-SAT-11-rank-one-strings.svg)

*Each dot is a one-dimensional weight space. The first row uses the generator \(\omega^\vee\) and root step \(2\omega^\vee\); the second uses \(\alpha^\vee\) and root step \(\alpha^\vee\). These are the exact characters proved in (3.3) and (3.8), not a common rescaling of one character lattice. The free comparison source is Mirković–Vilonen, §7; the proofs are §§3.1–3.2 above.*

### 3.3. The whole rank-one category is semisimple

First transfer the lattice-slice calculation of Lesson 5, §19 to all the rank-one labels. A projective lattice class in the \(PGL_2\) parity component of \(n\) has exactly one lattice representative of determinant index \(n\): multiplication by \(t^a\) changes the index by \(2a\), and scalar units preserve the lattice. The projected-frame morphism takes the projective \(GL_2\) closure of type \((n,0)\) bijectively onto the \(PGL_2\) closure of type \(n\omega^\vee\), preserving its orbit strata. It is a continuous map from a compact complex projective space to a Hausdorff finite target stage, so it is a homeomorphism. For \(SL_2\), use determinant-zero type \((m,-m)\). Every lattice with that index has a determinant-one frame: multiply one basis vector by the inverse of its determinant unit. The same orbitwise morphism and compact bijection identify its closure with type \(m\alpha^\vee\). These are the finite-frame constructions of Lesson 6, §7.3, now applied at an arbitrary bound. The upper root coordinate is unchanged, so the semi-infinite slices are identified as well.

In the \(PGL_2\) case their labels are \((n-2i)\omega^\vee\), \(0\le i\le n\); in the \(SL_2\) case they are \((m-i)\alpha^\vee\), \(0\le i\le2m\). Each open-orbit slice is irreducible: Lesson 5, §19 gives the two extremes \(\mathbb A^n\) and a point, and the intermediate slices \(\mathbb G_m\times\mathbb A^{n-i-1}\). Its standard-object basis theorem, equation (20.3), makes every indicated weight space of \(\Delta_\lambda\) one dimensional, and all others zero. Sections 3.1–3.2 proved exactly the same character for \(IC_\lambda\), without semisimplicity. The canonical epimorphism
\(\Delta_\lambda\twoheadrightarrow IC_\lambda\)
is consequently an isomorphism: each exact weight functor gives a surjection of equal one-dimensional spaces, and their faithful direct sum kills its kernel. Hence
\[
\Delta_\lambda=IC_\lambda
\quad\text{for every rank-one label.}
\tag{3.10}
\]

We spell out how (3.10) controls extensions. On a closed support \(Y\) where \(O_\lambda\) is open, put
\(A=j_!\Lambda[d_\lambda]\) and \(K={}^p\tau_{\le-1}A\).
Right t-exactness of \(j_!\), proved in Gluing t-structures, Theorem 2.1, gives
\[
K\longrightarrow A\longrightarrow\Delta_\lambda
\longrightarrow K[1].
\]
For perverse \(Q\), applying \(\operatorname{Hom}(-,Q[1])\) injects
\(\operatorname{Hom}(\Delta_\lambda,Q[1])\)
into \(\operatorname{Hom}(A,Q[1])\). The preceding group is
\(\operatorname{Hom}(K[1],Q[1])=\operatorname{Hom}(K,Q)=0\),
by perverse orthogonality; no vanishing of \(\operatorname{Hom}(K,Q[1])\) is needed. If \(Q=IC_\mu\) is on the boundary, open adjunction makes the latter group zero. If \(\mu=\lambda\), it is \(H^1(O_\lambda,\Lambda)=0\), proved in Lesson 6, §4. Verdier self-duality of the ICs reverses the arguments and handles reverse containment. Different components have disjoint open-and-closed supports. Within either rank-one component the closures are totally ordered, so these cases exhaust all pairs.

An extension of two ICs is supported on the union of their supports. Its connecting map in the constructible derived category is zero by the preceding computation, so the identity of its quotient lifts to a section in the perverse heart. Full faithfulness of equivariance, Lesson 6, §2, makes this section spherical. All simple extensions therefore split, and finite-length induction splits every object. This proves (S) for both rank-one categories, completing the unconditional equivalences (3.5) and (3.9). No general IC parity theorem entered the argument.

## 4. Minuscule Grassmannians for \(GL_n\)

Let \(\lambda=(1^k,0^{n-k})\), \(0\le k\le n\), and \(d=k(n-k)\). Its lattice consists of
\(tO^n\subset M\subset O^n\), with \(O^n/M\) a \(k\)-dimensional quotient. Hence its closed orbit is \(\operatorname{Gr}(k,n)\), a smooth projective variety, and its IC is \(\Lambda[d]\).

Its torus fixed points correspond to subsets \(I=\{i_1<\cdots<i_k\}\) of \(\{1,\ldots,n\}\), with coweight
\(\nu_I=\sum_{i\in I}e_i\). Upper unipotent row reduction gives the semi-infinite intersection in this bounded minuscule locus as an affine cell. A quotient matrix with pivot columns \(i_j\) has a free entry in each nonpivot column to the right of its pivot. Row reduction removes entries in the other pivot columns, so the number of free entries is
\[
c_I=\sum_{j=1}^k(n-k+j-i_j).
\tag{4.1}
\]
These matrices parametrize the cell without relations: a pivot minor is one, and the remaining pivot conditions determine the reduced form uniquely. On the lattice side the containment \(tO^n\subset M\subset O^n\) makes these quotient coordinates constant modulo \(t\); the upper loop operations induce precisely these upper row operations. Thus the cells are the attracting strata used by the weight functors.

Compact cohomology of \(\mathbb A^{c_I}\) is \(\Lambda\) in degree \(2c_I\), and
\[
2c_I-d=\sum_{i\in I}(n+1-2i)=h_G(\nu_I).
\tag{4.2}
\]
Therefore every weight \(\nu_I\) occurs once, there are no other weights, and
\[
\dim H(IC_\lambda)=\binom nk.
\tag{4.3}
\]
These are exactly the weights of \(\bigwedge^k\Lambda^n\). Its basis vectors \(v_{i_1}\wedge\cdots\wedge v_{i_k}\) have those distinct characters. The elementary matrices act by replacing one index with another when permitted. They connect every subset to \(\{1,\ldots,k\}\), so any nonzero invariant subspace, first decomposed into torus weights, contains all basis vectors. Thus this representation is simple, with highest weight \(\lambda\). After the group identification proved under (S) in §7 below, the IC corresponds to \(\bigwedge^k\) of the standard representation. Equations (4.1)–(4.3) themselves are unconditional.

## 5. A precise criterion for detecting perversity

The following proof will also explain why Levi constant terms land in a perverse heart.

**Lemma 5.1.** Let \(C\) be a bounded, orbit-constructible, equivariant complex on a bounded part of \(\operatorname{Gr}_M\). Put
\[
\mathcal L^M_\nu(C)=R\Gamma_c(S^M_\nu,C)[h_M(\nu)].
\tag{5.1}
\]
Then \(C\) is perverse if and only if every \(\mathcal L^M_\nu(C)\) has cohomology only in degree zero.

**Proof.** The forward implication is Lesson 5, Theorem 17.1, applied to \(M\). The perverse cohomology objects of \(C\) are equivariant and have finite support. Their images under (5.1) are concentrated in degree zero. Apply (5.1) to the finite perverse truncation tower. Induction, or its finite spectral sequence, gives
\[
H^r\mathcal L^M_\nu(C)=F^M_\nu({}^pH^rC).
\tag{5.2}
\]
If the left side vanishes for all \(\nu\) and \(r\ne0\), the exact faithful direct sum of the weight functors, Lesson 10, §1 for \(M\), forces \({}^pH^rC=0\). Thus \(C\) is perverse. This uses neither semisimplicity nor a test of just the underlying dimensions. \(\square\)

## 6. Tensor constant terms and their signs

### 6.1. The attracting correspondence and its finite bounds

Factor the positive root group as \(N_G=U\rtimes N_M\), using the ordered root coordinates proved in Root data, Weyl chambers and the Bruhat decomposition, §5. Iwasawa decomposition, proved in Lesson 1, §6, puts every complex loop coset in \(U(F)M(F)K/K\). The chosen central cocharacter contracts the \(U\)-coordinates and leaves the \(M\)-coordinates fixed. Thus the fixed point locus is the classical locus \(\operatorname{Gr}_M\), and its attracting locus over a point \(mK_M\) is the locus represented by \(u mK\). These are precisely the maps (2.1). Indeed a point has a finite pole bound in each ordered root coordinate; scaling multiplies the outside-Levi coordinates by positive powers, while the inside-Levi coordinates have weight zero. Uniqueness of the limit in a separated finite projective stage identifies the attracting map with \(q\).

We also need the correspondence in families, rather than just this point classification. Choose a faithful closed embedding \(G\subset H=GL(V)\) and split \(V=\bigoplus_a V_a\) into central-cocharacter weights. Let \(P_H\) preserve the descending weight filtration. In a graph chart around a fixed subspace with weight-compatible pivots, the coordinate from a pivot of weight \(b\) to a complementary vector of weight \(a\) has weight \(a-b\). Lesson 5, §12 constructs attracting families by the rule \(c\mapsto c s^{a-b}\) for \(a-b\ge0\), and forces the coordinate to vanish otherwise. The lattice therefore has the filtration
\[
M_{\ge a}=M\cap(V_{\ge a}\otimes R((t))).
\tag{6.0}
\]
Its finite quotient has direct-summand graded pieces in the graph chart. Those pieces remain \(t\)-stable, and their inverse-image kernels are projective \(R[[t]]\)-lattices by Lesson 2, Lemma 2.1. Successive extensions split as modules. This gives a \(P_H\)-reduction on the disc, standard off the disc, whose associated graded is the attracting limit.

The map \(G/P\to H/P_H\) is a closed immersion. Schematically \(G\cap P_H=P\): a conjugation limit in \(H\) remains in the closed subgroup \(G\), since its equations vanish after inverting \(s\) and \(R[s]\to R[s,s^{-1}]\) is injective. Thus the quotient map is a monomorphism. The source is smooth projective by Automorphisms, forms and parabolic subgroups, Theorem 1.1. Its reduced proper image over \(\mathbb C\) is a single homogeneous orbit and is smooth: its nonempty smooth locus translates to every point. Zero-dimensional fibres make source and image have the same dimension, and the monomorphism on dual-number tests makes the differential injective, hence an isomorphism. The Jacobian criterion makes the map étale. The actual open-immersion proof in Étale morphisms and their local structure, Theorem 4.1 then makes it an isomorphism onto that closed image.

For an attracting \(G\)-modification, the \(P_H\)-flag just constructed lies in this closed \(G/P\)-subspace over the punctured disc. Its equations extend across the disc because multiplication by \(t\) is injective in \(R[[t]]\). It gives a unique \(P\)-reduction. Conversely, on local disc frames a \(P\)-reduction gives its attracting family by
\(u_\alpha(f_\alpha)\mapsto
u_\alpha(s^{\langle\alpha,\zeta\rangle}f_\alpha)\)
and leaves its Levi modification fixed. These inverse constructions have finite pole bounds, respect changes of frames, and descend. They identify the bounded attracting correspondence with (2.1), including parameter rings with nilpotents. Over a moving divisor, use \(f(t)=\prod_i(t-a_i)\) in place of \(t\): Lesson 8, §1 proves the needed finite free completed algebra, injectivity of multiplication by \(f\), and the projective stable-quotient lattice construction. The same filtration and closed flag equations apply to each graded piece. This supplies the actual relative correspondence used in §6.2.

All sheaf operations take place on finite supports. Embed a bounded proper support in the finite lattice Grassmannian of Lesson 8, §1, with its torus-equivariant Plücker embedding. Its fixed locus is closed and projective, and its attracting pieces are locally closed finite-type varieties obtained from the weight-coordinate charts of Lesson 5, §§12–16. The image of each piece lies in a bounded part of \(\operatorname{Gr}_M\). Only finitely many components meet the support. Consequently the classical constructibility and proper-support base-change proofs in Constructible complexes on algebraic varieties, H.2–H.4 and K.8 apply. The \(M(O)\)-action commutes with the central cocharacter and acts on both maps; restriction and proper-support pushforward therefore give an equivariant complex. Enlarging the bound gives the same functor by extension by zero and composition. These statements concern the reduced classical loci needed for sheaves; they do not assert that nilpotent fixed-point functors are discrete.

The inverse image under \(q\) of \(S^M_\nu\) is \(S^G_\nu\): the factorization \(U\rtimes N_M\) gives both inclusions, with the same stabilizer quotient. The composition theorem for \(!\)-images now gives, for every bounded equivariant complex \(A\), an actual natural equality of normalized complexes
\[
\begin{aligned}
\mathcal L^M_\nu(\operatorname{CT}_P A)
&=R\Gamma_c(S^M_\nu,Rq_!i^*A)
   [h_M(\nu)+d_P([\nu])]\\
&=R\Gamma_c(S^G_\nu,A)[h_G(\nu)]
=\mathcal L^G_\nu(A).
\end{aligned}
\tag{6.1}
\]
Equivalently the diagram comes from the Cartesian torsor identity
\(\operatorname{Gr}_{B_G}
=\operatorname{Gr}_P\times_{\operatorname{Gr}_M}\operatorname{Gr}_{B_M}\).
A \(P\)-bundle and a Borel reduction of its Levi quotient give the inverse-image \(B_G\)-bundle, and extension and Levi quotient give the inverse construction, with the same punctured trivialization. This proves the identity on every base and the base-change maps used in (6.1).
For perverse \(A\), Lemma 5.1 makes \(\operatorname{CT}_P A\) perverse. A short exact sequence gives a distinguished triangle whose images are perverse, hence again a short exact sequence. Thus constant term is exact. The same root factorization for nested parabolics proves transitivity, because the component shifts add:
\(2\rho_G-2\rho_N=(2\rho_G-2\rho_M)+(2\rho_M-2\rho_N)\).
Associativity of composition of \(!\)-images makes the triple transitivity diagram commute.

Summing (6.1), and using the canonical weight injections of Lesson 5, §18 on both sides, supplies the natural ungraded comparison
\[
\gamma_A:H_M(\operatorname{CT}_P A)\xrightarrow{\sim}H_G(A).
\tag{6.2}
\]
The cohomological degree of the \(\nu\)-summand changes from \(h_G(\nu)\) to \(h_M(\nu)\); these degrees must not be identified.

### 6.2. A sheaf-level comparison through the collision

Use the proper two-point fusion complex \(\mathcal F_2\) of Lesson 8, §§2–4. Its fibre normalization is \(\mathcal F_2[-2]\): at distinct points it is \(A\boxtimes B\), and on the diagonal it is \(A*B\). On a bounded supported moving target, take relative positive hyperbolic restriction to the moving \(M\)-target and shift by \(d_P\) on each total \(M\)-component. Call the resulting total complex \(E\).

The geometry and constructibility are the same finite weight-coordinate construction as in §6.1; the base coordinates have weight zero. Proper-support base change proves that the restriction to a block stratum of the two-point base is the constant-term complex of the corresponding convolution, with the collective base shift \([2]\). By §6.1 that convolution's constant term is perverse. On the distinct-point open it is
\[
E|_{B^\circ}
=\operatorname{CT}_P(A)\boxtimes\operatorname{CT}_P(B)
   \boxtimes\Lambda_{B^\circ}[2],
\qquad B^\circ=\mathbb A^2\setminus\Delta.
\tag{6.3}
\]

Here are the costalk bounds, as well as the stalk bounds. Classical hyperbolic localization of Lesson 5, §§15–16, applied with the opposite central cocharacter, gives
\[
\mathbb D\bigl(Rq_!i^* C[d_P]\bigr)
\simeq Rq^-_!i^{-*}(\mathbb D C)[-d_P].
\tag{6.4}
\]
Indeed duality first gives \(Rq_*i^!\mathbb D C[-d_P]\); the negative-cocharacter Braden comparison identifies this with the opposite attracting \(!\)-image. It is the normalized opposite-parabolic functor. Its perversity is proved by (6.1) for the Borel with positive Levi roots and negative outside-Levi roots. The proper fusion complex has the dual fibre description proved in Lesson 8, §4, so the dual of \(E\) has perverse fibres with the same collective base shift \([2]\).

An orbit stratum in the diagonal target has dimension \(d_\mu+1\), whereas the stalk bound furnished by a perverse fibre and \([2]\) is at most \(-d_\mu-2\). It is strictly below the perverse boundary bound. Equation (6.4) gives the strict dual costalk bound. On the distinct-point strata the bounds are precisely the perverse bounds. Thus \(E\) is perverse and has no perverse subobject or quotient on the diagonal. The proved characterization of intermediate extension in Intermediate extensions and intersection complexes, §1 therefore gives
\[
E=j_{!*}(E|_{B^\circ}).
\tag{6.5}
\]
The right side is exactly the fusion complex for the two constant-term objects. Restrict (6.5) to the diagonal and remove \([2]\). It yields an isomorphism of perverse sheaves
\[
\phi^{\rm raw}_{A,B}:
\operatorname{CT}_P(A*B)
\xrightarrow{\sim}
\operatorname{CT}_P(A)*\operatorname{CT}_P(B).
\tag{6.6}
\]
This is a sheaf-level construction. It does not deduce an isomorphism from equality of total dimensions, nor assume that an arbitrary hyperbolic restriction commutes with nearby cycles.

### 6.3. Normalizing the tensor comparison

Fix the cochain shift map
\[
(C[a]\otimes D[b])\longrightarrow(C\otimes D)[a+b],
\qquad x\otimes y\longmapsto(-1)^{b|x|}x\otimes y,
\tag{6.7}
\]
where \(|x|\) is the degree before shifting. This is a chain map: the shifted differentials are \((-1)^a d_C\) and \((-1)^b d_D\); for the first term the exponent changes by \(b\) when \(x\) is differentiated, and for the second term the tensor differential uses \(|x|-a\). Both terms agree with the differential shifted by \(a+b\).

On \(\pi_1(M)\), define
\[
e_G(\kappa)=h_G(\nu)\pmod2,
\qquad d(\kappa)=d_P(\kappa),\qquad [\nu]=\kappa.
\tag{6.8}
\]
The first is well defined because \(2\rho_G\) pairs evenly with every \(M\)-coroot; the second is well defined integrally as already checked. Both are additive. At distinct points, (6.7) shows that the comparison (6.6), under (6.2) and the chosen total-cohomology comparisons, differs from the \(G\)-comparison on the pair of output components \((\kappa_1,\kappa_2)\) by
\[
\chi(\kappa_1,\kappa_2)
=(-1)^{e_G(\kappa_1)d(\kappa_2)}.
\tag{6.9}
\]
The unshifted first weight complex has degree \(h_G(\nu_1)\), and the second component shift is \(d(\kappa_2)\), exactly the two exponents in (6.7). The canonical localization maps of Lesson 10, §5.4 commute with these restriction and product maps, so this calculation compares the chosen tensor structures themselves. By (6.5) it also determines their diagonal comparison.

More explicitly, the relative version of the Cartesian Borel identity identifies the total-coweight complexes
\[
\mathscr W^M_\nu(\operatorname{CT}^{\rm rel}_P K_G)
\simeq\mathscr W^G_\nu(K_G)[d_P([\nu])],
\qquad K_G=\mathcal F_2[-2].
\tag{6.11}
\]
Lesson 10, §5 constructs these surviving weight sheaves as canonical local-system summands using two localization maps. Equation (6.11) supplies maps of those local systems, with fibre (6.2). On the distinct-point open their comparison is (6.7), with phase (6.9). Equality of maps of these local systems extends across the collision, because their base \(\mathbb A^2\) is connected and the summands are locally constant. This verifies the claimed comparison with the chosen \(H\)-tensor maps before applying the correction; intermediate-extension uniqueness alone would not identify arbitrary cohomology splittings.

Multiply (6.6) on each output pair by (6.9). Since \(\chi^2=1\), the resulting \(\phi_{A,B}\) makes (6.2) a monoidal natural isomorphism. Its associativity follows directly from
\[
\chi(\kappa_1,\kappa_2)
\chi(\kappa_1+\kappa_2,\kappa_3)
=\chi(\kappa_2,\kappa_3)
\chi(\kappa_1,\kappa_2+\kappa_3),
\tag{6.10}
\]
which is additivity in both variables. The zero component gives the unit. Three-point intermediate-extension uniqueness gives the associativity of the raw comparisons; (6.10) preserves it.

The symmetry is the modified symmetry of Lesson 8 on both groups. To verify it, apply the faithful functor \(H_M\) to the symmetry diagram. Under the monoidal comparison (6.2), it becomes the ordinary symmetry diagram for \(H_G\), proved in Lesson 10, §2. Thus the diagram commutes before applying \(H_M\) as well. This explicitly accounts for the shift signs; no equality of \(G\)- and \(M\)-component parities is assumed.

For nested Levi groups, write \(d_1=2\rho_G-2\rho_M\) and \(d_2=2\rho_M-2\rho_N\). Composition of the raw shift maps differs from the direct shift map by \((-1)^{d_1(\kappa_1)d_2(\kappa_2)}\). The ratio of the two products of (6.9) is the same sign, since \(e_G-e_M=d_1\) modulo two. They cancel. Thus the transitivity isomorphism of §6.1 is monoidal. The same computation and associativity of \(!\)-composition gives coherent triple transitivity.

**Theorem 6.1.** The normalized functor (2.2) is exact and symmetric monoidal, with the tensor comparison just specified. It preserves the fibre functor through (6.2), and is coherently transitive for nested Levi groups. No hypothesis (S) is used.

By the all-test-algebra reconstruction in Lesson 9, it induces a homomorphism \(H_M\to H_G\) restricting to the identity on the specified weight torus. Under (S) for both groups and their root identifications, this is the usual Levi inclusion, up to the root-frame choices. To check closed immersion, every \(M\)-simple occurs in a constant term. For an \(M\)-dominant \(\mu\), take \(\lambda=\mu^+\) for \(G\). The extremal weight \(\mu\) of \(V_\lambda\) occurs once. A weight strictly above it in the \(M\)-positive-root direction would have larger squared length: \(\mu\) is \(M\)-dominant, so
\(\|\mu+\beta\|^2=\|\mu\|^2+2(\mu,\beta)+\|\beta\|^2>\|\mu\|^2\)
for nonzero \(\beta\in Q_M^{\vee,+}\). All weights lie in the convex hull of \(W_G\lambda\), and have length at most \(\|\lambda\|=\|\mu\|\). Hence that line is an \(M\)-highest line of character \(\mu\). Semisimplicity for \(M\) puts \(IC^M_\mu\) in the constant term as a constituent. Lesson 9, Theorem 8.1 then proves the closed immersion. A closed reductive subgroup containing the same maximal torus is generated by that torus and its root subgroups: the proved Bruhat coordinates supply this statement. Its roots are exactly the coroots in \(M\), so its image is the indicated standard Levi. Identifying its individual root frames requires the compatible pinning choices.

## 7. The root datum under hypothesis (S)

This section assumes (S) for \(G\). Lesson 10, §9 then proves that \(H_G\) is a connected reductive algebraic group. Its closed maximal torus is the split torus \(\widehat T\), so the group is split. The ordinary highest-weight theory used here is proved in Finite-dimensional Lie theory, §7, and integrated and descended in The isomorphism theorem and construction of split groups, §§6,10.

### 7.1. All the weights, before their multiplicities

Write \(\Delta_\lambda={}^pH^0j_!\Lambda[d_\lambda]\) for the standard perverse object. Under (S),
\[
\Delta_\lambda=IC_\lambda.
\tag{7.1}
\]
Indeed perverse adjunction gives
\(\operatorname{Hom}(\Delta_\lambda,IC_\mu)
=\operatorname{Hom}(\Lambda[d_\lambda],j^!IC_\mu)\).
It is zero for \(\mu\ne\lambda\): smaller supports miss the open orbit, larger supports are excluded by the support of \(\Delta_\lambda\). Its value for \(\mu=\lambda\) is \(\Lambda\). A decomposition of \(\Delta_\lambda\) into simples consequently has exactly this one summand.

Lesson 5, §20 proves the standard-object basis from top compact cohomology of the open semi-infinite slice. The nonemptiness criterion of its §§8–10 and (7.1) give the exact support
\[
\{\nu:F_\nu(IC_\lambda)\ne0\}
=\{\nu\in\lambda+Q^\vee:\nu^+\le\lambda\}.
\tag{7.2}
\]
Every such weight has multiplicity the number of top-dimensional components of that open slice. No dual-group character formula is an input to (7.2).

The convex hull of (7.2) is \(\operatorname{conv}(W_G\lambda)\). It contains all \(W_G\lambda\). Conversely, for a real functional \(\ell\) on \(L_\mathbb R\), move \(\ell\) to the dominant chamber. Its maximum on a Weyl orbit is its value on the dominant representative, by successively reflecting across negative walls. If \(\nu^+\le\lambda\), pairing with that dominant functional gives
\(\max_w\ell(w\nu)\le\max_w\ell(w\lambda)\).
Every separating functional therefore places \(\nu\) in this convex hull. The finite-dimensional separation fact follows, for example, by taking the nearest point of the compact convex hull in a Euclidean norm: the difference to an outside point strictly separates it. This proves the assertion without a character formula.

### 7.2. Identifying the Weyl group

The cocharacter of \(\widehat T\) given by \(2\rho_G\) is regular for \(H_G\), by the highest-space argument of Lesson 10, §7.3, with the sign reversed. Choose its positive chamber. Lemma 1.1 makes \(\lambda\) the highest weight of the simple \(H_G\)-representation \(H(IC_\lambda)\). The set of dominant integral weights of \(H_G\) is therefore exactly the original dominant coweights of \(G\).

For any simple highest-weight representation of a reductive group, the vertices of its weight polytope are the Weyl orbit of its highest weight. Here is the part of that assertion needed: every weight is obtained by subtracting positive simple roots, so any dominant functional is maximized at the highest weight; applying Weyl representatives proves the same in every chamber and supplies every Weyl translate. The separating-functional argument just used then identifies the convex hull. For a regular highest weight the orbit points are distinct vertices, since a functional in its chamber has that unique maximizer.

Thus, for every regular dominant integral \(\lambda\),
\[
W_{H_G}\lambda=W_G\lambda.
\tag{7.3}
\]
This equality of orbits determines the groups as linear transformations, not merely their orders. Fix \(u\in W_{H_G}\). For every such \(\lambda\), some \(w\in W_G\) satisfies \((u-w)\lambda=0\). A finite union of proper rational subspaces cannot contain all lattice points in an open rational cone: choose independent integral vectors inside that cone, take their large positive integral combinations, and observe that a nonzero product of linear forms cannot vanish on every positive integer grid, by induction on its variables. Therefore one \(u-w\) is identically zero. The reverse argument is identical. Hence
\[
W_{H_G}=W_G\quad\text{on }L.
\tag{7.4}
\]

### 7.3. The integral rank-one step

The dominant chambers agree, so a simple reflection of \(H_G\) is the corresponding simple reflection \(s_i\) of \(G\). Its one-dimensional negative eigenspace in \(L_\mathbb R\) is the line through \(\alpha_i^\vee\). Write its positive simple root as \(\beta_i=c_i\alpha_i^\vee\), \(c_i>0\).

Choose a sufficiently regular dominant integral \(\lambda\), with
\(m=\langle\alpha_i,\lambda\rangle\ge2\). The edge from \(\lambda\) to \(s_i\lambda\) has, by (7.2), exactly the weights
\[
\lambda-j\alpha_i^\vee,qquad 0\le j\le m.
\tag{7.5}
\]
To check the exactness, a point on that edge has difference from \(\lambda\) on the line \(\mathbb R\alpha_i^\vee\); membership in \(Q^\vee\) makes the coefficient integral because the simple coroots form a basis of that lattice. Conversely, for any such \(j\), all the other simple-root pairings stay nonnegative. If the \(i\)-pairing is negative, applying \(s_i\) replaces \(j\) by \(m-j\). The dominant representative is therefore
\(\lambda-\min(j,m-j)\alpha_i^\vee\le\lambda\), proving membership in (7.2).

The rank-one highest-weight calculation for \(H_G\) gives exactly
\(\lambda-r\beta_i\), for \(0\le r\le\langle\beta_i^\vee,\lambda\rangle\), on the same edge. Other lowering operators cannot remain on that edge: positive simple roots are independent, and all their coefficients in a lowering word are nonnegative. The first positive step in (7.5) is \(\alpha_i^\vee\); equality of the two finite weight sets forces \(c_i=1\). This is the same integral distinction computed explicitly in §3, rather than a conclusion from equal ranks. Consequently \(\beta_i=\alpha_i^\vee\). Comparing the identical reflection formulas
\[
s_i\nu=\nu-\langle\alpha_i,\nu\rangle\alpha_i^\vee
=\nu-\langle\beta_i^\vee,\nu\rangle\beta_i
\]
gives \(\beta_i^\vee=\alpha_i\). Weyl conjugation gives all roots and coroots. The root datum is
\[
\bigl(X^*(\widehat T),\Phi(H_G),X_*(\widehat T),\Phi(H_G)^\vee\bigr)
=\bigl(X_*(T),\Phi(G)^\vee,X^*(T),\Phi(G)\bigr).
\tag{7.6}
\]

**Theorem 7.1, conditional on (S).** There is an isomorphism
\(H_G\simeq\widehat G_\Lambda\), carrying the specified weight torus and positive chamber to those of the split group with dual root datum. It induces
\[
\operatorname{Sat}_G(\Lambda)\simeq\operatorname{Rep}_\Lambda(\widehat G),
\qquad IC_\lambda\longmapsto V_\lambda,
\qquad F_\nu(IC_\lambda)\longmapsto(V_\lambda)_\nu.
\tag{7.7}
\]
In particular the weights and their multiplicities are those of the irreducible highest-weight representation \(V_\lambda\).

**Proof.** The pinned isomorphism and existence theorems are proved in The isomorphism theorem and construction of split groups, Theorems 5.1 and 10.1. Choose frames in the simple root lines of the split \(H_G\), and use (7.6). Reconstruction of Lesson 9 and Lemma 1.1 give (7.7). The last assertion is an identification of the actual representation and its actual torus spaces, and therefore includes multiplicities. \(\square\)

## 8. Components, centres and the choice of pinning

For the dual root datum the character group of the centre is
\[
X^*(Z(\widehat G))=L/Q^\vee=\pi_0(\operatorname{Gr}_G).
\tag{8.1}
\]
To prove the centre calculation, an element of the torus is central exactly when every root character evaluates to one. The root subgroups and torus generate the group by the Bruhat decomposition proved in Root data, Weyl chambers and the Bruhat decomposition, §6. Thus the centre is the kernel of all roots, the diagonalizable group with character lattice the quotient by their span. Use (7.6) for that span. On an irreducible highest-weight module, all weights differ from \(\lambda\) by dual roots, so its central character is \([\lambda]\). This matches the component containing its IC support. Equation (8.1) concerns the character group of the centre; it does not identify the component group with the centre as a scheme.

For \(PGL_2\), (8.1) is \(\mathbb Z/2\), the character group of \(\mu_2\subset SL_2\). The representation (3.3) has central sign \((-1)^n\). For \(SL_2\), the component group and the centre of its dual \(PGL_2\) are trivial. Its first nontrivial simple is the three-dimensional adjoint representation of §3.2.

The reconstructed group with its fibre functor is intrinsic after the sign modification of Lesson 8 is fixed. An identification with a particular presentation of a Chevalley group requires a pinning. Equation (7.6) gives the based datum; choosing nonzero vectors in the simple root lines upgrades it to a unique pinned isomorphism by Theorem 5.1 cited above. Without those vectors the isomorphism is generally not unique: conjugation by the adjoint torus rescales them. For \(SL_2\), diagonal conjugation already displays this ambiguity. Over \(\Lambda\), the rescaling is an element of the adjoint torus; it need not lift to a point of the original torus.

Under (S), the cycle basis provides one explicit geometric normalization. Take
\(\lambda_0=\sum_{\alpha>0}\alpha^\vee\), so
\(\langle\alpha_i,\lambda_0\rangle=2\) for every simple root. Ordinary highest-weight theory makes both
\(F_{\lambda_0}(IC_{\lambda_0})\) and
\(F_{\lambda_0-\alpha_i^\vee}(IC_{\lambda_0})\)
one dimensional: the latter is the first simple-root lowering space. By (7.1) and Lesson 5, (20.3), they have canonical generators from their unique oriented open-slice components; call these \(v_0,v_i\). The root line \(\mathfrak h_{\alpha_i^\vee}\) acts nontrivially from the second line to the first, by the rank-one raising–lowering formula. Define its frame \(E_i\) by
\[
E_i v_i=2v_0.
\tag{8.2}
\]
There is exactly one such frame. Characteristic-zero root parametrization, proved in Roots and reductive groups of rank one, Theorem 4.1, integrates it to a root-group pinning. Thus (8.2) and the fixed torus and Borel give a specified pinning over \(\Lambda\), and a unique pinning-preserving isomorphism with the pinned dual group. This proves a precise normalization by the cycle basis. Its comparison with a pinning defined by cup product with a first Chern class, or with the Weil-equivariant normalization of §9, requires a further comparison and is not asserted here.

## 9. Integral and Weil-equivariant versions: statements only

These variants are not inputs to any proof above. For a Noetherian commutative coefficient ring of finite global dimension, the integral theorem identifies the finite-support equivariant perverse category with finitely generated representations of the split group with dual root datum. Its exact source is Mirković–Vilonen, [the corrected arXiv version, Theorem 12.1 and §13, equation (13.1)](https://arxiv.org/html/math/0401222v5#S12). In the subcategory with free finite total cohomology, the representations have free finite underlying modules. General integral perverse objects need not be semisimple, and the rigid field-valued argument of §7 is not an integral proof. The corrected version includes Appendix B addressing a gap in the original integral group identification.

For a nonarchimedean local field \(E\) of residue characteristic \(p\) and \(\ell\ne p\), Fargues–Scholze construct an integral Satake category on the Fargues–Fontaine Grassmannian, with continuous Weil action on its fibre functor. Their [Theorem VI.11.1](https://arxiv.org/pdf/2102.13459v4) identifies its reconstructed group with the dual group over \(\mathbb Z_\ell\), equivariantly for the Weil group. The pinning has root lines identified with \(\mathbb Z_\ell(1)\), so the Weil action includes a cyclotomic twist as well as the based-datum action. Proposition VI.7.13 gives normalized constant terms; tensor compatibility is Proposition VI.9.6, not VI.7.13 alone. Proposition VI.12.1 identifies switching with the Chevalley involution up to conjugation by \(\widehat\rho(-1)\) in the adjoint group. These precise statements are not proved here or transferred to classical sheaves by citation.

## 10. Exercises and complete solutions

**Exercise 11.1 (easy).** Compute the weights and dimension of the IC of \(\operatorname{Gr}(k,n)\). Under hypothesis (S), identify its representation.

**Solution.** Row reduction gives the cells (4.1), indexed by the \(k\)-element subsets \(I\). Equation (4.2) places their compact cohomology in the required weight degree. Thus the characters are \(\sum_{i\in I}e_i\), each once, and the dimension is \(\binom nk\). The elementary-matrix argument of §4 proves that \(\bigwedge^k\Lambda^n\) is simple with highest weight \((1^k,0^{n-k})\). Under (S), Theorem 7.1 identifies the IC with that representation. For \(k=0,n\), this gives respectively the unit and the determinant, both one dimensional.

**Exercise 11.2 (easy).** Explain the component–central-character correspondence, including the difference between a group and its character group.

**Solution.** Lesson 4 proves \(\pi_0\operatorname{Gr}_G=L/Q^\vee\). The dual roots are the original coroots, so imposing that they all be trivial on the dual torus gives the centre \(D(L/Q^\vee)\). Its character group is \(L/Q^\vee\). A simple highest-weight representation has all its weights in \(\lambda+Q^\vee\), so the centre acts by \([\lambda]\), the component label of \(IC_\lambda\). For \(PGL_2\), the label group is \(\mathbb Z/2\) and the centre scheme is \(\mu_2\); its nontrivial character acts by \(-1\) on the standard two-dimensional representation.

**Exercise 11.3 (medium).** Compute the weights of \(H(IC_{\alpha^\vee})\) for \(SL_2\) and explain its adjoint interpretation without using general semisimplicity.

**Solution.** The quadratic cone has IC \(\Lambda[2]\). Its three slices have dimensions \(2,1,0\), hence shifted compact degrees \(2,0,-2\) and coweights \(\alpha^\vee,0,-\alpha^\vee\). Each weight space is one dimensional. Self-duality produces a nondegenerate symmetric form because the dimension is odd, and the determinant is the unit by Corollary 1.2. Section 3.2 identifies its faithful simple image with the orthogonal identity component, hence \(PGL_2\), and the representation with its adjoint representation. Section 3.3 then proves rank-one semisimplicity from the standard-to-IC comparison and the extension computation, making the quotient the whole reconstructed group.

**Exercise 11.4 (medium).** For \(G=GL_2\) and diagonal \(T\), prove that normalized constant terms commute with convolution.

**Solution.** A torus Satake object is a finite \(L\)-graded vector space. Here \(L=\mathbb Z^2\), \(h_G(a,b)=a-b\), and the component shift in (2.2) is \(a-b\). Therefore its degree-zero stalk at \((a,b)\) is precisely \(F_{(a,b)}\). Lesson 10, §5 constructs the canonical maps
\[
F_{(a,b)}(P*Q)=
\bigoplus_{(u,v)+(x,y)=(a,b)}
F_{(u,v)}(P)\otimes F_{(x,y)}(Q).
\tag{10.1}
\]
Convolution for a torus adds lattice labels, so (10.1) is exactly the required isomorphism of torus objects. Its associativity, unit and ordinary modified symmetry are the three-point and sign calculations of the same proof. In particular, for the minuscule object of weight \((1,0)\), the constant term has the two lines \((1,0),(0,1)\); its square has dimensions \(1,2,1\) at \((2,0),(1,1),(0,2)\), agreeing with its convolution.

**Exercise 11.5 (hard).** Under (S), deduce the roots and coroots of the reconstructed group, keeping the integral normalization.

**Solution.** Lemma 1.1 labels the highest lines, and (7.1) identifies the standard-object weight support with that of the IC. Thus its polytope has vertices \(W_G\lambda\). Ordinary highest-weight theory gives vertices \(W_{H_G}\lambda\). The finite-union-of-subspaces argument of §7.2 makes the two Weyl groups equal as lattice transformations. On the edge from \(\lambda\) to \(s_i\lambda\), the geometric support consists exactly of (7.5); the rank-one lowering string for \(H_G\) has spacing its simple root \(\beta_i\). Equality of the finite sets makes \(\beta_i=\alpha_i^\vee\), not merely a rational multiple. Comparing their reflection formulas then makes \(\beta_i^\vee=\alpha_i\). Weyl conjugation gives all roots and coroots. The explicit two- and three-dimensional cases of §3 exhibit the two possible divisibilities of the rank-one root in its character lattice.

## What this lesson does not prove

The general classical Satake equivalence (7.7) is proved here under (S); the general IC parity input supplying (S) in Lesson 6 is still unproved. Rank-one semisimplicity and both full equivalences are proved separately in §3.3. The integral and Weil-equivariant theorems of §9, comparison of the cycle-basis pinning with other geometric normalizations, and the rational-adic extension to other algebraically closed ground fields are stated or excluded explicitly and are not used as proof inputs.

The free reading for comparison is Mirković–Vilonen, [§§6–7 and the corrected integral discussion](https://arxiv.org/abs/math/0401222v5), and Zhu, [the affine-Grassmannian notes](https://arxiv.org/abs/1603.05593). The proof maps and the conditional hypothesis above specify which assertions are actually established in this lesson.
