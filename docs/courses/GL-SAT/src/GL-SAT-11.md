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

We will prove the following assertion, without using a general IC stalk-parity theorem:
\[
\text{(S): every object of }\operatorname{Sat}_G(\Lambda)
\text{ is a finite direct sum of simple objects.}
\tag{1.3}
\]
Lesson 10, Theorem 9.1 supplies a finite connected reductive quotient \(H_G\to R_G\) carrying every simple IC. Sections 7–8 identify its dual root datum and centre. Section 8 then removes the remaining kernel by the vanishing of IC self-extensions, proving (S) and the full classical equivalence. The Levi functor, rank-one characters and quotient identification are established before this semisimplicity argument. Section 8.7 then uses the geometric parity inputs proved in Lesson 06 to conclude ordinary IC stalk and costalk parity over every characteristic-zero coefficient field.

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
\qquad V_{\omega^\vee}=\Lambda,\quad
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
(n-2j)\omega^\vee,\qquad 0\le j\le n,
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
j\alpha^\vee,\qquad -n\le j\le n,
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

### 3.4. Rank-one Levi groups with their central torus

Let \(M\) be a connected complex reductive group whose roots are \(\{\pm\alpha\}\), with torus lattice \(L\). Its adjoint quotient
\[
q:M\longrightarrow M/Z(M)\simeq PGL_2
\tag{3.11}
\]
identifies the two root groups. This is the adjoint and rank-one construction proved in AG-RG-03, Theorem 1.1, Proposition 5.2 and Theorem 7.1. For a dominant \(\lambda\in L\), set \(m=\langle\alpha,\lambda\rangle\). The quotient sends \(\lambda\) to \(m\omega^\vee\), and \(\alpha^\vee\) to \(2\omega^\vee\).

The induced map of Schubert closures
\[
Z^M_\lambda\longrightarrow Z^{PGL_2}_{m\omega^\vee}
\tag{3.12}
\]
is a stratum-preserving homeomorphism of their classical spaces. Here are the lifting and injectivity checks. The map \(M(O)\to PGL_2(O)\), for \(O=\mathbb C[[t]]\), is onto. The fibre over an \(O\)-point is a torsor under the smooth affine diagonalizable group \(Z(M)\). Its special fibre has a complex point. Formal smoothness lifts it successively over \(O/t^n\), as in the affine lifting proof of Lesson 3, §7.5. The torsor is affine of finite presentation, so a compatible system of its points gives an \(O\)-point by evaluation on finitely many coordinate generators. This includes a centre with finite components; characteristic zero makes those components smooth.

The orbit-closure theorem makes the labels of the source
\(\lambda-j\alpha^\vee\), for \(0\le j\le\lfloor m/2\rfloor\). Their target labels are \((m-2j)\omega^\vee\), exactly the orbit labels of the target. Integral-frame surjectivity gives surjectivity on each orbit. The orbit stabilizers are also exact preimages under \(M(O)\to PGL_2(O)\): the positive and negative root-coordinate conditions are identical, and the whole central kernel stabilizes every modification. Thus each orbit map is bijective. Equivalently, two lifts differ by a central coweight; within the same component their difference also belongs to \(\mathbb Z\alpha^\vee\), whose intersection with the central lattice is zero, since \(\langle\alpha,\alpha^\vee\rangle=2\).

The finite-pole and frame-coordinate construction of Lesson 6, §7.3, places (3.12) in a finite separated target stage. Its source is complex projective by Lesson 2. A continuous bijection from that compact source to the Hausdorff target is a homeomorphism. It preserves stratum dimensions, and the identified upper root coordinate identifies the semi-infinite slices, with weight map \(\nu\mapsto\langle\alpha,\nu\rangle\omega^\vee\). The IC and standard-object constructions are determined by these stratified classical spaces. Consequently the \(PGL_2\) calculation gives
\[
F^M_{\lambda-j\alpha^\vee}(IC^M_\lambda)=\Lambda
\quad(0\le j\le m),
\qquad F^M_\nu(IC^M_\lambda)=0
\text{ for other }\nu.
\tag{3.13}
\]
The same spaces occur for \(\Delta^M_\lambda\), so exact faithful weights identify \(\Delta^M_\lambda=IC^M_\lambda\). In each component the labels are totally ordered. The extension calculation of §3.3 therefore also proves semisimplicity for this rank-one Levi, including its central torus. Formula (3.13) is the precise character statement needed below. None of this identifies Grassmannian quotient functors on arbitrary parameter rings; (3.12) concerns the classical spaces supporting the sheaves.

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
These are exactly the weights of \(\bigwedge^k\Lambda^n\). Its basis vectors \(v_{i_1}\wedge\cdots\wedge v_{i_k}\) have those distinct characters. The elementary matrices act by replacing one index with another when permitted. They connect every subset to \(\{1,\ldots,k\}\), so any nonzero invariant subspace, first decomposed into torus weights, contains all basis vectors. Thus this representation is simple, with highest weight \(\lambda\). After the quotient identification proved in §7 below, the IC corresponds to \(\bigwedge^k\) of the standard representation. Equations (4.1)–(4.3) are direct geometric calculations.

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

By the all-test-algebra reconstruction in Lesson 9, it induces a homomorphism \(H_M\to H_G\) restricting to the identity on the specified weight torus. After the full equivalence is proved in §8 for both groups, this is the usual Levi inclusion, up to the root-frame choices. The following final identification is not an input to the quotient proof of §7. To check closed immersion, every \(M\)-simple occurs in a constant term. For an \(M\)-dominant \(\mu\), take \(\lambda=\mu^+\) for \(G\). The extremal weight \(\mu\) of \(V_\lambda\) occurs once. A weight strictly above it in the \(M\)-positive-root direction would have larger squared length: \(\mu\) is \(M\)-dominant, so
\(\|\mu+\beta\|^2=\|\mu\|^2+2(\mu,\beta)+\|\beta\|^2>\|\mu\|^2\)
for nonzero \(\beta\in Q_M^{\vee,+}\). All weights lie in the convex hull of \(W_G\lambda\), and have length at most \(\|\lambda\|=\|\mu\|\). Hence that line is an \(M\)-highest line of character \(\mu\). Semisimplicity for \(M\) puts \(IC^M_\mu\) in the constant term as a constituent. Lesson 9, Theorem 8.1 then proves the closed immersion. A closed reductive subgroup containing the same maximal torus is generated by that torus and its root subgroups: the proved Bruhat coordinates supply this statement. Its roots are exactly the coroots in \(M\), so its image is the indicated standard Levi. Identifying its individual root frames requires the compatible pinning choices.

## 7. The dual root datum of the finite quotient

Use the connected reductive quotient \(R_G\) of Lesson 10, Theorem 9.1. All its simples are precisely the IC representations, and its closed maximal torus is the split torus \(\widehat T\), by Lesson 10, §9.2. Thus it is split. This section identifies \(R_G\) before proving (S) for the entire heart. The ordinary highest-weight theory used here is proved in Finite-dimensional Lie theory, §7, and integrated and descended in The isomorphism theorem and construction of split groups, §§6,10.

For clarity, the module bridge gives every dominant integral weight of the split group, not just the fundamental representations used in its construction. Pull such a weight back along the central isogeny from a central torus times the simply connected semisimple group. Its semisimple part is a sum of fundamental dominant weights. The corresponding tensor product of the constructed fundamental modules has its one-dimensional top line at that sum. Complete reducibility and the finite highest-weight presentation give a Lie-simple constituent generated by that line; the Lie-stability lemma AG-GS-01, Lemma 5.21 makes it stable under the connected semisimple group. Tensor its pulled-back central character. All its weights differ from the pulled-back highest weight by roots, so the finite central kernel acts trivially on every weight space. Faithfully flat central-quotient descent therefore gives the desired simple module of the original group. Conversely the highest-weight and lowering proof gives a dominant integral top weight for every simple. The rational presentations preserve these modules and their weight dimensions over every characteristic-zero field.

### 7.1. Vertices of the IC weight polytope

Lemma 1.1 puts every IC weight in \(\operatorname{conv}(W_G\lambda)\). Here is the convexity check. For a real functional \(\ell\), move \(\ell\) to the dominant chamber. Its maximum on a Weyl orbit is its value on the dominant representative, by successively reflecting across negative walls. If \(\nu^+\le\lambda\), pairing with that dominant functional gives
\(\max_w\ell(w\nu)\le\max_w\ell(w\lambda)\).
Every separating functional therefore places \(\nu\) in this convex hull. The separation fact follows by taking the nearest point of the compact convex hull in a Euclidean norm: its difference from an outside point strictly separates that point.

Every \(w\lambda\) actually occurs as an IC weight. The slice \(S_{w\lambda}\cap Z_\lambda\) is nonempty, since it contains \(t^{w\lambda}\), and it misses every boundary orbit. Indeed an intersection with a boundary closure \(Z_\mu\) would contract into \(t^{w\lambda}\in Z_\mu\), forcing \(\lambda\le\mu<\lambda\), by the orbit-closure theorem. Hence the IC is the constant shifted sheaf throughout this slice. The dimension theorem and top compact-cohomology calculation of Lesson 5 give
\[
F_{w\lambda}(IC_\lambda)
=H_c^{d_\lambda+h_G(w\lambda)}
 (S_{w\lambda}\cap Z_\lambda,\Lambda)\ne0;
\tag{7.1}
\]
the degree displayed is twice the slice dimension, and each nonempty top-dimensional component has its nonzero orientation class. Thus
\[
\operatorname{conv}\{\nu:F_\nu(IC_\lambda)\ne0\}
=\operatorname{conv}(W_G\lambda).
\tag{7.2}
\]
This proves the vertices without claiming the interior multiplicities, identifying standard and IC objects, or using (S).

### 7.2. Identifying the Weyl group

The cocharacter of \(\widehat T\) given by \(2\rho_G\) is regular for \(R_G\), by the highest-space argument of Lesson 10, §§7.3,9.2, with the sign reversed. Choose its positive chamber. Lemma 1.1 makes \(\lambda\) the highest weight of the simple \(R_G\)-representation \(H(IC_\lambda)\). The set of dominant integral weights of \(R_G\) is therefore exactly the original dominant coweights of \(G\).

For any simple highest-weight representation of a reductive group, the vertices of its weight polytope are the Weyl orbit of its highest weight. Here is the part of that assertion needed: every weight is obtained by subtracting positive simple roots, so any dominant functional is maximized at the highest weight; applying Weyl representatives proves the same in every chamber and supplies every Weyl translate. The separating-functional argument just used then identifies the convex hull. For a regular highest weight the orbit points are distinct vertices, since a functional in its chamber has that unique maximizer.

Thus, for every regular dominant integral \(\lambda\),
\[
W_{R_G}\lambda=W_G\lambda.
\tag{7.3}
\]
This equality of orbits determines the groups as linear transformations, not merely their orders. Fix \(u\in W_{R_G}\). For every such \(\lambda\), some \(w\in W_G\) satisfies \((u-w)\lambda=0\). A finite union of proper rational subspaces cannot contain all lattice points in an open rational cone: choose independent integral vectors inside that cone, take their large positive integral combinations, and observe that a nonzero product of linear forms cannot vanish on every positive integer grid, by induction on its variables. Therefore one \(u-w\) is identically zero. The reverse argument is identical. Hence
\[
W_{R_G}=W_G\quad\text{on }L.
\tag{7.4}
\]

### 7.3. The integral rank-one step

The dominant chambers agree: their dominant lattice points agree, and every rational point in either closed rational cone has an integral multiple there. Thus a simple reflection of \(R_G\) is the corresponding simple reflection \(s_i\) of \(G\). Its one-dimensional negative eigenspace in \(L_\mathbb R\) is the line through \(\alpha_i^\vee\). Write its positive simple root as \(\beta_i=c_i\alpha_i^\vee\), \(c_i>0\).

Choose a sufficiently regular dominant integral \(\lambda\), with
\(m=\langle\alpha_i,\lambda\rangle\ge2\). Let \(M_i\) be the standard rank-one Levi for \(\alpha_i\), and take the component of its exact constant term containing \(\lambda\):
\[
Q=\operatorname{CT}_{P_i}(IC_\lambda)
 \big|_{[\lambda]\in L/\mathbb Z\alpha_i^\vee}.
\tag{7.5a}
\]
Theorem 6.1 and (6.2) identify its weights with the original weights on \(\lambda+\mathbb Z\alpha_i^\vee\). This line meets the polytope (7.2) precisely in the edge \([\lambda,s_i\lambda]\). To check this, choose a functional zero on \(\alpha_i^\vee\) and positive on every other simple coroot. For a Weyl-orbit point its difference from \(\lambda\) is a nonnegative combination of simple coroots, so a maximizer has the form \(\lambda-c\alpha_i^\vee\). A Weyl-invariant positive definite inner product makes every orbit point have length \(\|\lambda\|\). The quadratic equation \(\|\lambda-c\alpha_i^\vee\|^2=\|\lambda\|^2\) has exactly the two solutions \(c=0,m\), by the reflection formula. Hence the maximizing face has just the vertices \(\lambda,s_i\lambda\). In semisimple rank one the whole segment is that face, and a central direction merely translates it.

Every simple composition factor of \(Q\) has its highest weight on this edge, by Lemma 1.1 for \(M_i\) and exactness of its weight functors. Its highest line at \(\lambda\) is one dimensional. Among these factors only \(IC^{M_i}_\lambda\) can contain weight \(\lambda\): a smaller \(M_i\)-dominant label on the edge has no weight larger than itself in the \(\alpha_i^\vee\) direction. Thus \(IC^{M_i}_\lambda\) occurs exactly once. Formula (3.13) and exact weights now force every weight
\[
\lambda-j\alpha_i^\vee,\qquad 0\le j\le m
\tag{7.5}
\]
to occur in \(IC_\lambda\). Conversely a weight on that edge has difference from \(\lambda\) on the line \(\mathbb R\alpha_i^\vee\); Lemma 1.1 puts that difference in \(Q^\vee\), making the coefficient integral because the simple coroots form a basis of that lattice. The segment restricts it to \(0\le j\le m\). Thus (7.5) is exactly the set of edge weights. This argument retains the integral step even when \(\alpha_i^\vee\) is nonprimitive in \(L\).

The rank-one highest-weight calculation for \(R_G\) gives exactly
\(\lambda-r\beta_i\), for \(0\le r\le\langle\beta_i^\vee,\lambda\rangle\), on the same edge. Other lowering operators cannot remain on that edge: positive simple roots are independent, and all their coefficients in a lowering word are nonnegative. The first positive step in (7.5) is \(\alpha_i^\vee\); equality of the two finite weight sets forces \(c_i=1\). This is the same integral distinction computed explicitly in §3, rather than a conclusion from equal ranks. Consequently \(\beta_i=\alpha_i^\vee\). Comparing the identical reflection formulas
\[
s_i\nu=\nu-\langle\alpha_i,\nu\rangle\alpha_i^\vee
=\nu-\langle\beta_i^\vee,\nu\rangle\beta_i
\]
gives \(\beta_i^\vee=\alpha_i\). Weyl conjugation gives all roots and coroots. The root datum is
\[
\bigl(X^*(\widehat T),\Phi(R_G),X_*(\widehat T),\Phi(R_G)^\vee\bigr)
=\bigl(X_*(T),\Phi(G)^\vee,X^*(T),\Phi(G)\bigr).
\tag{7.6}
\]

**Theorem 7.1.** There is an isomorphism
\(R_G\simeq\widehat G_\Lambda\), carrying the specified weight torus and positive chamber to those of the split group with dual root datum. For the semisimple IC tensor subcategory \(\mathcal S_G\) of Lesson 10, it induces
\[
\mathcal S_G\simeq\operatorname{Rep}_\Lambda(\widehat G),
\qquad IC_\lambda\longmapsto V_\lambda,
\qquad F_\nu(IC_\lambda)\longmapsto(V_\lambda)_\nu.
\tag{7.7}
\]
In particular the weights and their multiplicities are those of the irreducible highest-weight representation \(V_\lambda\).

**Proof.** The pinned isomorphism and existence theorems are proved in The isomorphism theorem and construction of split groups, Theorems 5.1 and 10.1. Choose frames in the simple root lines of the split \(R_G\), and use (7.6). Lesson 10, (9.3), and Lemma 1.1 give (7.7). The last assertion identifies the actual simple representation and its torus spaces, so it includes multiplicities. No semisimplicity of arbitrary perverse objects is assumed. \(\square\)

## 8. The centre, self-extensions and the whole Satake heart

### 8.1. A central lift of the quotient's centre

For the dual root datum the character group of the centre is
\[
X^*(Z(\widehat G))=L/Q^\vee=\pi_0(\operatorname{Gr}_G).
\tag{8.1}
\]
To prove the centre calculation, a central element centralizes the maximal torus, whose schematic centralizer is that torus by AG-RG-02, Theorem 2.2. An element of the torus is central exactly when every root character evaluates to one. The fppf word-generation proof in AG-RG-05, Lemma 4.1 shows that root subgroups and torus generate the group on arbitrary test algebras locally in the fppf topology. Thus the centre is schematically the kernel of all roots, the diagonalizable group with character lattice the quotient by their span; this is also the centre formula proved in AG-RG-03, §1. Use (7.6) for that span. On an irreducible highest-weight module, all weights differ from \(\lambda\) by dual roots, so its central character is \([\lambda]\). This matches the component containing its IC support. Equation (8.1) concerns the character group of the centre; it does not identify the component group with the centre as a scheme.

For \(PGL_2\), (8.1) is \(\mathbb Z/2\), the character group of \(\mu_2\subset SL_2\). The representation (3.3) has central sign \((-1)^n\). For \(SL_2\), the component group and the centre of its dual \(PGL_2\) are trivial. Its first nontrivial simple is the three-dimensional adjoint representation of §3.2.

The entire centre of \(R_G\), not just its identity component, lifts centrally to \(H_G\). Put \(C=D_\Lambda(L/Q^\vee)\). For every coefficient algebra \(A\) and \(c\in C(A)\), act on the cohomology of an object in component \(\delta\) by the scalar \(c(\delta)\). Component projectors are natural and components add under convolution, so these actions are natural tensor automorphisms on all objects. Every tensor automorphism commutes with those projectors and scalars. Thus they define a central homomorphism \(C\to H_G\), which is the usual closed inclusion \(C\subset\widehat T\subset H_G\). Under \(H_G\to R_G\), its restriction to the torus is unchanged. The root calculation above identifies its image with \(Z(R_G)\). In particular this is an isomorphism onto the full quotient centre, on all test algebras.

### 8.2. Every IC self-extension vanishes

**Lemma 8.1.** For every dominant \(\lambda\) and every characteristic-zero coefficient field,
\[
\operatorname{Ext}^1_{\operatorname{Sat}_G}
 (IC_\lambda,IC_\lambda)=0.
\tag{8.2}
\]

**Proof.** Work on \(Y=Z_\lambda\), with open orbit \(j:O_\lambda\hookrightarrow Y\). Put \(I=IC_\lambda\), \(A=j_!\Lambda[d_\lambda]\), \(\Delta={}^pH^0A\), and \(N={}^p\tau_{\le-1}A\). Right t-exactness of \(j_!\) gives
\(N\to A\to\Delta\to N[1]\).
Applying \(\operatorname{Hom}(-,I[1])\), perverse orthogonality \(\operatorname{Hom}(N,I)=0\) gives an injection
\[
\operatorname{Hom}(\Delta,I[1])
 \hookrightarrow\operatorname{Hom}(A,I[1])
 =H^1(O_\lambda,\Lambda)=0.
\tag{8.3}
\]
The equality uses open adjunction and \(j^!I=\Lambda[d_\lambda]\); the last vanishing is the complete orbit-cohomology proof of Lesson 6, §4.

The epimorphism \(\Delta\twoheadrightarrow I\) has boundary-supported kernel \(B\). The IC has no boundary-supported subobject, so \(\operatorname{Hom}(B,I)=0\). Apply \(\operatorname{Hom}(-,I[1])\) to \(B\to\Delta\to I\to B[1]\). It injects \(\operatorname{Hom}(I,I[1])\) into the zero group in (8.3). Every heart self-extension of \(I\) is supported on \(Y\); its connecting map is zero, and the quotient identity therefore lifts to a section in the perverse heart. Full faithfulness of spherical equivariance, Lesson 6, §2, makes this section spherical. This proves (8.2) without asserting \(\Delta=I\). \(\square\)

### 8.3. A centre-trivial module occurs in a simple endomorphism module

**Lemma 8.2.** Let \(R\) be a split connected reductive group over a characteristic-zero field \(k\). For every nonzero finite-dimensional \(R\)-module \(A\) on which \(Z(R)\) acts trivially, some simple \(V_\lambda\) admits a nonzero equivariant map
\[
\phi:A\longrightarrow\operatorname{End}_k(V_\lambda).
\tag{8.4}
\]

**Proof.** Complete reducibility is proved in Lesson 9, Theorem 10.1. Each irreducible summand of \(A\) has highest weight \(\gamma\) in the root lattice \(Q_R\), since its central character is trivial. Such a summand has a zero weight. Indeed the saturated-weight theorem of RT-LIE-14, Proposition 5.1 gives
\(\operatorname{Wt}V_\gamma=\operatorname{conv}(W_R\gamma)\cap(\gamma+Q_R)\).
The average of \(W_R\gamma\) is zero: it is Weyl invariant and lies in the root space, whose invariant subspace is zero because pairing with each simple coroot must vanish. Thus zero belongs to that polytope and coset. The same statement for a reductive group follows by retaining its fixed central character and applying the semisimple-root calculation; here that character is zero. Consequently \(A_0\ne0\). If \(R\) is a torus, the hypothesis makes all of \(A\) trivial, giving the conclusion directly.

The rational highest-weight presentations proved in RT-LIE-14, §4.5, and AG-RG-S06, §7, supply the split simple modules over \(\mathbb Q\) and every characteristic-zero field, with the same weight dimensions. Thus the saturated-weight statement just used and the character formula below apply over \(k\), although the RT-LIE proofs first present them over \(\mathbb C\).

Choose a sufficiently dominant integral \(\lambda\) so that \(\lambda+\nu\) is dominant for every weight \(\nu\) of \(A\). A large multiple of a strictly dominant root-lattice weight does this. The Weyl character formula, proved in RT-LIE-16, Theorem 2.1, implies
\[
\chi_\lambda\chi_A
 =\sum_\nu (\dim A_\nu)\chi_{\lambda+\nu}.
\tag{8.5}
\]
To verify the implication, write \(a_\eta=\sum_w\epsilon(w)e^{w\eta}\). Weyl invariance of the multiplicities of \(A\) gives
\[
a_{\lambda+\rho}\chi_A
 =\sum_\nu (\dim A_\nu)a_{\lambda+\rho+\nu}.
\]
Apply the character formula and cancel its nonzero denominator alternant in the group-algebra domain. If \(\rho\) is not in the character lattice, perform the calculation in the lattice enlarged by \(\rho\); the resulting characters belong to the original lattice. All \(\lambda+\nu\) are dominant, so there are no reflected terms or cancellations. Complete reducibility and independence of simple characters, by their highest monomials, identify the multiplicity of \(V_\lambda\) in \(A\otimes V_\lambda\) as \(\dim A_0>0\). An equivariant projection onto this constituent gives a nonzero map \(A\otimes V_\lambda\to V_\lambda\), equivalently (8.4). \(\square\)

### 8.4. Removing every finite-stage unipotent kernel

Work over the original coefficient field \(k=\Lambda\). By Lesson 9, §7, write \(k[H_G]\) as the union of finite Hopf subalgebras containing \(k[R_G]\). Their quotient groups give
\[
H_G\twoheadrightarrow S\twoheadrightarrow R_G,
\qquad U=\ker(S\to R_G).
\tag{8.6}
\]
Every simple \(S\)-module inflates to a simple \(H_G\)-module, hence factors through \(R_G\). A faithful \(S\)-module with a composition-series basis therefore embeds \(U\) into the upper unitriangular group, schematically, as proved in Lesson 10, §9.3. Cartier's theorem makes \(U\) smooth. Assume \(U\ne1\).

We give the needed unipotent quotient explicitly. In the strictly upper triangular matrix algebra, exponential and logarithm are the finite mutually inverse polynomials
\[
\exp X=\sum_{j=0}^{N-1}\frac{X^j}{j!},
\qquad
\log(1+X)=\sum_{j=1}^{N-1}\frac{(-1)^{j+1}}jX^j,
\quad X^N=0.
\tag{8.7}
\]
Check the next polynomial identity over an algebraic closure \(\overline k\). For \(u\in U(\overline k)\), each integral power \(u^n\) belongs to \(U\). Every defining polynomial of \(U\) therefore vanishes on \(\exp(z\log u)\) at infinitely many integers \(z\), hence identically. Its derivative at zero places \(\log u\) in \(\mathfrak u=\operatorname{Lie}U\). Since \(U_{\overline k}\) is reduced, this gives the scheme inclusion \(\log U_{\overline k}\subset\mathfrak u_{\overline k}\). Both have dimension \(\dim\mathfrak u\), by smoothness, and a proper closed subset of a vector space has smaller dimension. Thus they are equal. All polynomial maps are defined over \(k\), and faithful field extension detects their equality. Consequently \(\log U=\mathfrak u\) over \(k\), and \(U\) is geometrically connected.

The finite logarithm formula proved in RT-LIE-06, Lemma 7.2 shows that \(\exp\mathfrak u\) is a group. Reducing its displayed differential recurrence modulo \([\mathfrak u,\mathfrak u]\) gives
\[
\log(\exp X\exp Y)=X+Y
 \pmod{[\mathfrak u,\mathfrak u]}.
\tag{8.8}
\]
Indeed every correction term is a commutator, and the initial value at zero is zero. Consequently \(D=\exp[\mathfrak u,\mathfrak u]\) is a closed normal subgroup of \(S\), and the quotient map
\(U\to A=\mathfrak u/[\mathfrak u,\mathfrak u]\)
is a surjective vector-group homomorphism with kernel \(D\). Normality follows also schematically: conjugation by \(S\) preserves \(U\), its Lie algebra and its derived subspace, and commutes with the finite exponential. The strictly triangular Lie algebra is nilpotent, so its nonzero subalgebra \(\mathfrak u\) has nonzero abelianization; otherwise its lower central series would be constantly \(\mathfrak u\), contradicting nilpotence. Thus \(A\ne0\).

The normal affine quotient theorem of AG-GS-04, Theorem 11.1d supplies the affine group
\[
E=S/D,\qquad 1\longrightarrow A\longrightarrow E
 \longrightarrow R_G\longrightarrow1.
\tag{8.9}
\]
The quotient sheaves satisfy \(E/A=(S/D)/(U/D)=S/U=R_G\): local lifts to \(S\) give precisely the same coset equivalence relation. Hence \(E\to R_G\) is an \(A\)-torsor. Conjugation on \(A\) factors through \(R_G\), since conjugation by \(U\) is trivial on its abelianization. Every additive polynomial over a characteristic-zero algebra is linear: its homogeneous part of degree \(d\) satisfies \(f(2x)=2f(x)\), forcing \((2^d-2)f_d=0\) for \(d\ne1\), and \(f(0)=0\). Thus this action is an ordinary rational linear representation, also on every coefficient algebra. The central lift of §8.1 maps centrally into \(S\), and maps isomorphically onto \(Z(R_G)\). Hence \(Z(R_G)\) acts trivially on \(A\), so Lemma 8.2 applies.

We next split (8.9), proving the splitting instead of assuming a Levi decomposition. The vector-group torsor \(E\to R_G\) has a regular section because \(R_G\) is affine. Here is the descent argument. Choose an affine faithfully flat trivializing cover, with coordinate algebra \(B\) over \(k[R_G]\). The difference of two local sections is an additive Čech cocycle with values in the free module underlying \(A\). Its Amitsur complex is exact: after tensoring with \(B\), multiplication in the extra tensor factor contracts the augmented complex; faithful flatness reflects exactness. The cocycle is therefore a coboundary. Correcting the local section by that coboundary gives a section over \(R_G\).

Normalize the section \(s\) at the identity. Its multiplication defect is a regular map \(c:R_G^2\to A\), defined by
\[
s(g)s(h)=c(g,h)s(gh).
\]
Associativity gives
\(g c(h,l)-c(gh,l)+c(g,hl)-c(g,h)=0\).
This regular two-cocycle is a coboundary, as follows. The left regular representation on \(k[R_G]\) is locally finite, by the finite-subcomodule proof of Lesson 9, §6. Every finite submodule is semisimple. Its invariant part consists of constants, since a left-invariant function has value \(f(g)=f(1)\). Projections onto that trivial isotypical part are unique and compatible on finite submodules. They give a normalized left-invariant functional
\[
\ell:k[R_G]\to k,\qquad \ell(1)=1.
\tag{8.10}
\]
For homogeneous regular cochains, take equivariant maps \(F:R_G^{n+1}\to A\), with differential the alternating deletion of variables. Define
\[
(hF)(g_0,\ldots,g_{n-1})
 =\ell_x F(x,g_0,\ldots,g_{n-1}).
\tag{8.11}
\]
Left invariance of \(\ell\) preserves equivariance: translating all the remaining variables translates \(x\) in the integration and acts on the value in \(A\). Expanding the alternating deletions cancels every term except \(\ell(1)F\), giving \(\delta h+h\delta=1\) in positive degree. The homogeneous cocycle corresponding to \(c\) is
\(F(g_0,g_1,g_2)=g_0c(g_0^{-1}g_1,g_1^{-1}g_2)\).
Applying (8.11) and returning to inhomogeneous cochains gives a regular \(b:R_G\to A\) with
\(c(g,h)=g b(h)-b(gh)+b(g)\).
Replace \(s(g)\) by \(-b(g)s(g)\). Its defect is zero. This is a group section, proving
\[
E\simeq A\rtimes R_G.
\tag{8.12}
\]

Choose the nonzero map \(\phi:A\to\operatorname{End}(V_\lambda)\) in Lemma 8.2. On \(V_\lambda\oplus V_\lambda\), let \(R_G\) act diagonally and let \(a\in A\) act by
\[
\begin{pmatrix}1&\phi(a)\\0&1\end{pmatrix}.
\tag{8.13}
\]
Linearity and equivariance of \(\phi\) verify the additive law and the semidirect-product conjugation law on all test algebras. This is a regular \(E\)-module and gives an extension of \(V_\lambda\) by itself. It is nonsplit: \(A\) acts trivially on both constituents but nontrivially on the middle module, whereas a direct sum of the constituents would have trivial \(A\)-action. Pullback along \(S\twoheadrightarrow E\) and \(H_G\twoheadrightarrow S\) preserves nonsplitting by full faithfulness of inflation in Lesson 9, Theorem 8.1. Reconstruction would therefore give a nonsplit IC self-extension, contradicting Lemma 8.1.

Thus \(U=1\) in every cofinal finite Hopf stage over \(\Lambda\). Each \(S\to R_G\) is an isomorphism, and their coordinate-algebra union gives \(H_G=R_G\). The contradiction and representation splitting were carried out over the original coefficient field; algebraic closure was used only to verify the polynomial logarithm identity. No additional equivalence between scalar-extended perverse hearts is needed.

**Theorem 8.3 (classical geometric Satake).** For a connected complex reductive \(G\) and any characteristic-zero field \(\Lambda\), the full Satake heart is semisimple, its reconstructed group is the split group with dual root datum, and
\[
\operatorname{Sat}_G(\Lambda)
 \simeq\operatorname{Rep}^{\mathrm{fd}}_\Lambda(\widehat G),
\qquad IC_\lambda\longmapsto V_\lambda,
\qquad F_\nu(IC_\lambda)\longmapsto(V_\lambda)_\nu.
\tag{8.14}
\]
This follows from \(H_G=R_G\), Theorem 7.1 and the proved complete reducibility of the reductive quotient. It proves (S) independently of general IC stalk and costalk parity.

### 8.5. The IC cycle basis after semisimplicity

Now, and only now, every standard perverse object equals its IC:
\[
\Delta_\lambda=IC_\lambda.
\tag{8.15}
\]
Indeed decompose \(\Delta_\lambda\) using Theorem 8.3. Its support excludes every simple not supported in \(Z_\lambda\). For smaller supports, perverse open adjunction gives
\(\operatorname{Hom}(\Delta_\lambda,IC_\mu)
=\operatorname{Hom}(\Lambda[d_\lambda],j^!IC_\mu)=0\).
For \(\mu=\lambda\) it is \(\Lambda\). Its semisimple decomposition therefore has exactly that one summand, proving (8.15).

The standard-object basis proved in Lesson 5, (20.3) now becomes an actual IC basis: the weight \(F_\nu(IC_\lambda)\) has the orientation classes of the top-dimensional components of \(S_\nu\cap O_\lambda\). Its nonzero support is exactly
\[
\{\nu\in\lambda+Q^\vee:\nu^+\le\lambda\},
\tag{8.16}
\]
by the nonemptiness criterion proved in Lesson 5, §§8–10. Thus the component counts equal the weight multiplicities in \(V_\lambda\), by (8.14). This transfer uses the proved standard–IC equality; it does not identify open-slice top cohomology with IC cohomology merely by deleting a boundary.

### 8.6. The choice of pinning

The reconstructed group with its fibre functor is intrinsic after the sign modification of Lesson 8 is fixed. An identification with a particular presentation of a Chevalley group requires a pinning. Equation (7.6) gives the based datum; choosing nonzero vectors in the simple root lines upgrades it to a unique pinned isomorphism by Theorem 5.1 cited above. Without those vectors the isomorphism is generally not unique: conjugation by the adjoint torus rescales them. For \(SL_2\), diagonal conjugation already displays this ambiguity. Over \(\Lambda\), the rescaling is an element of the adjoint torus; it need not lift to a point of the original torus.

The cycle basis provides one explicit geometric normalization. Take
\(\lambda_0=\sum_{\alpha>0}\alpha^\vee\), so
\(\langle\alpha_i,\lambda_0\rangle=2\) for every simple root. Ordinary highest-weight theory makes both
\(F_{\lambda_0}(IC_{\lambda_0})\) and
\(F_{\lambda_0-\alpha_i^\vee}(IC_{\lambda_0})\)
one dimensional: the latter is the first simple-root lowering space. By (8.15) and Lesson 5, (20.3), they have canonical generators from their unique oriented open-slice components; call these \(v_0,v_i\). The root line \(\mathfrak h_{\alpha_i^\vee}\) acts nontrivially from the second line to the first, by the rank-one raising–lowering formula. Define its frame \(E_i\) by
\[
E_i v_i=2v_0.
\tag{8.17}
\]
There is exactly one such frame. Characteristic-zero root parametrization, proved in Roots and reductive groups of rank one, Theorem 4.1, integrates it to a root-group pinning. Thus (8.17) and the fixed torus and Borel give a specified pinning over \(\Lambda\), and a unique pinning-preserving isomorphism with the pinned dual group. This proves a precise normalization by the cycle basis. Its comparison with a pinning defined by cup product with a first Chern class, or with the Weil-equivariant normalization of §9, requires a further comparison and is not asserted here.

### 8.7. All intersection complexes have parity

The geometric parity arguments have now all preceded their use. The Satake category, Lemma 5.6 proves the conditional tensor-generator statement by a minimum-norm lattice argument and a schematically faithful representation. Its Proposition 5.9 proves parity of every dominant-short-coroot IC by the actual cone neighborhood, ordinary flag-variety Lefschetz and the Gysin sequence. Lemma 5.10 proves parity under convolution with a parity IC, using equivariant derived retractions to ordinary Bott–Samelson pushforwards and explicit rank-one wall fibres. None of those geometric proofs uses the equivalence established here.

**Theorem 8.4 (classical IC parity).** For every connected reductive \(G/\mathbb C\), every characteristic-zero coefficient field \(\Lambda\), and every dominant \(\lambda\), the ordinary cohomology sheaves of both
\[
i_\mu^*IC_\lambda,\qquad i_\mu^!IC_\lambda
\]
vanish in degrees \(q\not\equiv\langle2\rho,\lambda\rangle\pmod2\), on every spherical orbit \(O_\mu\). The objects may have zero restriction to an orbit.

*Proof.* Theorem 8.3 supplies precisely the tensor equivalence hypothesized in Lemma 5.6: its reconstructed root datum is dual, and (8.14) identifies the IC objects with the corresponding irreducible highest-weight modules. Hence every IC is an actual summand of a finite sum of convolution words in the chosen minuscule and dominant-short-coroot ICs and their duals.

Each generating factor has parity. A minuscule support is a smooth closed flag variety; each short-coroot support has the cone chart proved in Proposition 5.9. Dual labels are \(-w_0\xi\), which preserve these two forms and their dimension parity. Apply Lemma 5.10 successively, from the rightmost factor of each word. This is the same unshifted convolution as in Lesson 07, whose finite frames and endpoints agree with the correspondence used in that lemma. Each word therefore has pure parity equal to the sum of its factors' component parities.

Take the summand \(IC_\lambda\). Restriction to its open-and-closed Grassmannian component discards all words in other components. Within its component their parity is \(d_\lambda\), since \(\langle2\rho,\alpha_i^\vee\rangle=2\) and component labels differ by the coroot lattice. Stalk and dual-stalk cohomology inherit that parity under the summand maps. Stratum duality contributes an even shift, so dual-stalk parity is exactly the claimed ordinary costalk parity. This proves the theorem over the given coefficient field. \(\square\)

The retraction argument also resolves the identity-lift criterion in Lesson 06, (5.9), for its rootwise resolutions: with IC parity now proved, equation (5.27) lifts the dense-cell identity to the actual equivariant derived inclusion, and its dual projection has identity composite. This supplies the required lift directly. The general relative-Lefschetz and intersection-form criteria in that lesson are alternative sufficient methods, and are not needed for this conclusion.

Thus (S), the full classical equivalence and the IC cycle basis are established before general (P). This proof order supplies both results without assuming parity in reconstruction or using semisimplicity to split an entire derived resolution complex.

## 9. Integral and Weil-equivariant versions: statements only

These variants are not inputs to any proof above. For a Noetherian commutative coefficient ring of finite global dimension, the integral theorem identifies the finite-support equivariant perverse category with finitely generated representations of the split group with dual root datum. Its exact source is Mirković–Vilonen, [the corrected arXiv version, Theorem 12.1 and §13, equation (13.1)](https://arxiv.org/html/math/0401222v5#S12). In the subcategory with free finite total cohomology, the representations have free finite underlying modules. General integral perverse objects need not be semisimple, and the rigid field-valued argument of §7 is not an integral proof. The corrected version includes Appendix B addressing a gap in the original integral group identification.

For a nonarchimedean local field \(E\) of residue characteristic \(p\) and \(\ell\ne p\), Fargues–Scholze construct an integral Satake category on the Fargues–Fontaine Grassmannian, with continuous Weil action on its fibre functor. Their [Theorem VI.11.1](https://arxiv.org/pdf/2102.13459v4) identifies its reconstructed group with the dual group over \(\mathbb Z_\ell\), equivariantly for the Weil group. The pinning has root lines identified with \(\mathbb Z_\ell(1)\), so the Weil action includes a cyclotomic twist as well as the based-datum action. Proposition VI.7.13 gives normalized constant terms; tensor compatibility is Proposition VI.9.6, not VI.7.13 alone. Proposition VI.12.1 identifies switching with the Chevalley involution up to conjugation by \(\widehat\rho(-1)\) in the adjoint group. These precise statements are not proved here or transferred to classical sheaves by citation.

## 10. Exercises and complete solutions

**Exercise 11.1 (easy).** Compute the weights and dimension of the IC of \(\operatorname{Gr}(k,n)\). Identify its representation.

**Solution.** Row reduction gives the cells (4.1), indexed by the \(k\)-element subsets \(I\). Equation (4.2) places their compact cohomology in the required weight degree. Thus the characters are \(\sum_{i\in I}e_i\), each once, and the dimension is \(\binom nk\). The elementary-matrix argument of §4 proves that \(\bigwedge^k\Lambda^n\) is simple with highest weight \((1^k,0^{n-k})\). Theorem 7.1 identifies the IC with that quotient representation; Theorem 8.3 identifies the whole heart. For \(k=0,n\), this gives respectively the unit and the determinant, both one dimensional.

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

**Exercise 11.5 (hard).** Deduce the roots and coroots of the reductive quotient before full semisimplicity, keeping the integral normalization.

**Solution.** Lemma 1.1 bounds all weights, while the boundary-free extremal-slice calculation (7.1) supplies every vertex \(W_G\lambda\). Ordinary highest-weight theory for the already proved reductive quotient gives vertices \(W_{R_G}\lambda\). The finite-union-of-subspaces argument of §7.2 identifies the two Weyl groups as lattice transformations. On the edge from \(\lambda\) to \(s_i\lambda\), exact rank-one Levi constant term has \(IC^{M_i}_\lambda\) as a constituent, because its highest line at \(\lambda\) has dimension one. Formula (3.13) forces all the steps in (7.5); the component condition excludes fractional steps. The ordinary lowering string has spacing the simple root \(\beta_i\), so equality of these finite edge sets gives \(\beta_i=\alpha_i^\vee\). Comparing reflection formulas gives \(\beta_i^\vee=\alpha_i\). Weyl conjugation gives all roots and coroots. This argument does not use \(\Delta_\lambda=IC_\lambda\); that equality is obtained later in (8.15).

## What this lesson does not prove

The general classical characteristic-zero Satake equivalence, full-heart semisimplicity, IC cycle basis and ordinary IC stalk and costalk parity are proved in §§7–8. Parity is concluded only after the equivalence, and is not its proof input. The integral and Weil-equivariant theorems of §9, comparison of the cycle-basis pinning with other geometric normalizations, and the rational-adic extension to other algebraically closed ground fields are stated or excluded explicitly and are not used as proof inputs.

The free reading for comparison is Mirković–Vilonen, [§§6–7, especially Remark 7.2, and the corrected integral discussion](https://arxiv.org/abs/math/0401222v5), and Zhu, [the affine-Grassmannian notes](https://arxiv.org/abs/1603.05593). The finite-stage kernel argument in §8 is written out with its actual earlier programme proofs; the corrected integral theorem is complementary reading, not an input replacing those arguments.
