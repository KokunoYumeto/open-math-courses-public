# Determinants, ramification and Tate curves

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

This supporting reading contains the completed proofs from Lesson 8 used by the fundamental estimate: the Euler-product determinant identity, its finite-coefficient extensions, the Swan and curve Euler formulas, Tate uniformization, and the local Legendre calculations. The original section, theorem and exercise numbers are retained for those references.

The trace formula is proved in Lesson 7. Its curve conventions and intersection arguments are in Lesson 6 and Lesson 5. The full rationality and functional-equation lesson includes these proofs and the smooth-proper individual-factor result, using the later purity proof in Lesson 11.

## 1. Local factors and formal Euler products

Let \(k_0=\mathbf F_q\), \(k=\overline{\mathbf F}_q\), \(p=\operatorname{char}k_0\), and \(\ell\ne p\). Let \(E/\mathbf Q_\ell\) be finite. Schemes over \(k_0\) are separated and of finite type; \(X=X_0\times_{k_0}k\). A constructible \(E\)-sheaf \(\mathcal F_0\) means a constructible adic sheaf with an integral lattice, localized to \(E\), as in Lesson 1. It need not be lisse.

We use geometric Frobenius throughout. Write \(F\) for its action on \(H_c^i(X,\mathcal F)\), and \(F_x\) for geometric Frobenius over \(\kappa(x)\) acting on \(\mathcal F_{\bar x}\). If \(d_x=[\kappa(x):k_0]\), define

\[
L(X_0,\mathcal F_0,t)
=\prod_{x\in|X_0|}
\det_E(1-F_xt^{d_x}\mid\mathcal F_{\bar x})^{-1}
\quad\in1+tE[[t]].
\tag{1.1}
\]

This is a formal product. For each \(n\), there are finitely many closed points of degree at most \(n\): a point of degree \(d\) gives \(d\) points over \(\mathbf F_{q^d}\), whose set of rational points is finite. Thus only finitely many factors affect a specified coefficient. No analytic convergence or complex embedding is needed. The usual variable is \(t=q^{-s}\) when one later asks analytic questions.

For the constant sheaf,

\[
Z(X_0,t)=L(X_0,E,t)
=\prod_{x\in|X_0|}(1-t^{d_x})^{-1}\in1+t\mathbf Z[[t]].
\tag{1.2}
\]

If \(a_d\) is the number of degree-\(d\) closed points and \(N_r=\#X_0(\mathbf F_{q^r})\), then

\[
N_r=\sum_{d\mid r}d\,a_d,\qquad
a_d=\frac1d\sum_{e\mid d}\mu(e)N_{d/e}.
\tag{1.3}
\]

The first identity partitions rational points by their closed point; the second is ordinary Möbius inversion. In particular,

\[
Z(X_0,t)=\exp\left(\sum_{r\ge1}N_r\frac{t^r}{r}\right)
\quad\text{in }\mathbf Q[[t]].
\tag{1.4}
\]

The integrality in (1.2) comes from the Euler product, not from the denominators in this exponential.

For a finite-dimensional vector space \(V\) and endomorphism \(A\),

\[
-t\frac{d}{dt}\log\det(1-tA)
=\sum_{r\ge1}\operatorname{Tr}(A^r)t^r.
\tag{1.5}
\]

To prove this, extend scalars to triangularize \(A\). Its determinant is the product of \(1-t\alpha_j\), and its power traces are \(\sum_j\alpha_j^r\), including multiplicity. Differentiating each factor proves the identity. This argument does not assume semisimplicity.

Applying (1.5) to (1.1), the coefficient of \(t^r\) is

\[
\sum_{d\mid r}d
\sum_{\substack{x\in|X_0|\\d_x=d}}
\operatorname{Tr}(F_x^{r/d}\mid\mathcal F_{\bar x}).
\tag{1.6}
\]

Each degree-\(d\) point gives \(d\) rational points after extension to \(\mathbf F_{q^r}\). Their stalk operators are conjugate to \(F_x^{r/d}\), by Lesson 3. Thus (1.6) is precisely the rational-point sum for that extension.

## 2. The cohomological expression

**Theorem 2.1.** For \(X_0,\mathcal F_0,E\) as above,

\[
L(X_0,\mathcal F_0,t)
=\prod_i
\det_E(1-tF\mid H_c^i(X,\mathcal F))^{(-1)^{i+1}}
\in E(t).
\tag{2.1}
\]

**Proof.** Lesson 7 gives finite-dimensional cohomology, vanishing outside a finite range, and, for every \(r\ge1\),

\[
\sum_{u\in X_0(\mathbf F_{q^r})}
\operatorname{Tr}(F_u\mid\mathcal F_{\bar u})
=\sum_i(-1)^i\operatorname{Tr}(F^r\mid H_c^i(X,\mathcal F)).
\tag{2.2}
\]

Here \(F_u\) refers to Frobenius over the extended field. Equations (1.5)–(1.6) show that \(t\,d\log/dt\) of both sides of (2.1) is the series with these coefficients. The quotient of the two sides belongs to \(1+tE[[t]]\) and has derivative zero. In characteristic zero its coefficients of every positive degree vanish, so it is \(1\). Both sides have constant term \(1\); this fixes the integration constant. The right side is a finite product of polynomials and their inverses. \(\square\)

Applying the same proof to a bounded constructible complex gives the local alternating determinant and the determinant on its compact-support hypercohomology. For an actual sheaf, (2.1) is the formulation used below.

### Coefficients with torsion

Power traces do not determine a determinant over a torsion ring. For example, in characteristic \(\ell\), the series \(1\) and \(1+t^\ell\) have the same logarithmic derivative. We will compare each coefficient directly, using symmetric powers of the coefficient complex and effective zero-cycles of the scheme.

Let \(A\) be a commutative Noetherian ring killed by a positive integer \(m\) prime to \(p\). The ring need not be finite, reduced or regular. Constructible \(A\)-modules have finitely generated stalks and are locally constant on a finite stratification. As before, \(D_{\mathrm{ctf}}\) additionally requires finite Tor amplitude. For a perfect complex \(C\) and its endomorphism \(u\), define
\[
\det(1-tu\mid C)=\prod_j\det(1-tu^j\mid P^j)^{(-1)^j},
\tag{2.3}
\]
where \(P\) is a bounded finite-projective representative and \(u^\bullet\) is a chain representative. Determinants on projective modules are defined on their determinant lines; the local definitions agree under a change of basis. We will also prove that (2.3) is independent of these representatives.

**Theorem 2.2 (the determinant formula with torsion coefficients).** For a separated finite-type \(X_0/\mathbf F_q\) and \(K_0\in D_{\mathrm{ctf}}(X_0,A)\), the compact-support complex is perfect over \(A\), and
\[
\prod_{x\in|X_0|}
\det(1-t^{d_x}F_x\mid K_{\bar x})^{-1}
=\det(1-tF\mid R\Gamma_c(X,K))^{-1}.
\tag{2.4}
\]
In particular this proves the formula for every finite commutative ring of order prime to \(p\). A noncommutative ring still has the additive trace of Lessons 4–7, but not the determinant in the commutative power-series ring used here.

We first establish the algebra and geometry needed to prove the theorem.

### Extending the additive trace to a Noetherian ring

**Lemma 2.3.** The perfectness and additive trace formula of Lesson 7 hold for the ring \(A\) above.

**Proof.** Consider first a locally constant sheaf \(M\) whose stalk is finite projective over \(A\). Its monodromy has finite image: a finite generating set has finite orbits under a continuous action of a profinite group on the discrete stalk, and the intersection of its open stabilizers fixes the module. A finite étale torsor \(\pi:V_0\to U_0\), with group \(G\), therefore trivializes \(M\). Put \(R=(\mathbf Z/m)[G]\). This is a finite ring of order prime to \(p\).

The regular local system \(P=\pi_*(\mathbf Z/m)\) is locally free of rank one as a right \(R\)-module, with the compatible left monodromy action. Choose the action convention so that
\(P\otimes_R M\) is the given sheaf. Lesson 7 applied to \(R^{\mathrm{op}}\) gives a perfect right-\(R\) complex \(C=R\Gamma_c(U,P)\) and its noncommutative Frobenius trace. The coefficient projection comparison gives
\[
R\Gamma_c(U,M)=C\otimes_R^{\mathbf L}M.
\tag{2.5}
\]
This comparison also holds when \(M\) is not perfect over \(R\). To see this directly, resolve an arbitrary left \(R\)-module by free modules in nonpositive degrees. On a compactification, extension by zero is exact and commutes with sums; global cohomology commutes with sums and has finite cohomological dimension for these torsion coefficients. Truncate the resolution from below. In each specified total degree the omitted terms have sufficiently negative degrees to contribute nothing, after allowing the fixed cohomological-dimension bound. The comparison for a bounded free complex follows by cones from the free-module case. Passing through these truncations proves (2.5). The same argument works on every geometric fibre for \(Rf_!\).

Each finite-projective right-\(R\) term of \(C\), tensored with \(M\), is a direct summand of a finite sum of \(M\)'s. It is therefore finite projective over \(A\). This proves perfectness. The map
\[
\phi_M:R/[R,R]\longrightarrow A,
\qquad r\longmapsto\operatorname{Tr}_A(r\mid M)
\]
is well defined by cyclicity. For a term which is a summand of \(R^h\), express its endomorphism using the corresponding idempotent matrix. Its \(A\)-trace after tensoring is \(\phi_M\) of its Hattori–Stallings trace: both are the sum of the diagonal traces on \(M^h\). Apply this degree by degree to \(C\). The finite-ring trace formula then becomes exactly the additive trace formula for \(M\), including its local stalk operators. All comparisons commute with Frobenius because the torsor is defined over \(\mathbf F_q\).

For completeness, this reduction also gives the finiteness input over \(A\). A finite-ring constructible \(Rf_!P\) has a finite stratification with finite cohomology modules. In the coefficient spectral sequence for (2.5), their \(R\)-Tor groups with \(M\) are finitely generated over \(A\), and carry the same locally constant descent data on a refinement of that stratification. In each total degree only finitely many rows occur. The projection formula and the torsion dimension bound give a common finite Tor interval. Thus the resulting cohomology is constructible over \(A\).

A bounded constructible finite-Tor complex admits a bounded representative by constructible flat sheaves. Here is the usual presentation argument. On each stratum, take finitely many generators of its finitely generated coefficient modules, trivialize their finite descent data on a finite étale covering, and push these free generators forward with proper support. Use open–closed extensions to assemble a finite constructible presentation. Repeat for the kernels and for a bounded-above resolution of the complex. Noetherianity preserves finite generation of the kernels. At an index beyond its uniform Tor interval the last kernel is flat, by the dimension-shifting Tor sequence on stalks; truncating there gives the bounded flat representative. Its stalks are finitely presented and flat, hence projective. These are also the constructible-presentation and extension-by-zero constructions of the preceding étale-cohomology lessons.

Stratify each term of this representative into the locally constant projective case just proved. Open–closed support sequences and the finite filtration by its degrees give compatible filtered complexes. Perfectness is preserved by their finite extensions, and the filtered trace additivity of Lesson 4 proves the trace formula for \(K_0\). This proves the lemma. \(\square\)

### Symmetric tensors of a complex

For a finite-projective module \(M\), write
\[
\Gamma^n M=(M^{\otimes n})^{\mathfrak S_n}.
\tag{2.6}
\]
This is the divided-power module, rather than the quotient symmetric power. For a free module with basis \(e_1,\ldots,e_r\), it is free on the orbit sums of tensors having each prescribed multiplicity \((a_1,\ldots,a_r)\), \(\sum a_i=n\). This description proves base-change compatibility and projectivity, first for free modules and then for direct summands. In particular, it introduces no division by \(n!\). Intrinsically it represents homogeneous polynomial laws of degree \(n\); that description extends \(\Gamma^n\) to arbitrary modules, while (2.6) remains valid for flat modules.

We require the nonadditive derived functor of \(\Gamma^n\). Here is the construction and the properties used below. A nonnegative cochain complex \(P\) corresponds to a cosimplicial module \(D(P)\); its degree-\(q\) term is
\[
D(P)^q=\bigoplus_{[q]\twoheadrightarrow[j]}P^j.
\]
For finite-projective terms one can construct it without choices by dualizing the usual simplicial denormalization of the chain complex \(P^\vee\). A monotone map between the indexing ordinals acts on the summands by its epi–mono factorization, with the boundary component supplied by the differential. The cosimplicial identities follow from the uniqueness of that factorization and \(d^2=0\). Normalization is
\(N(B)^q=\bigcap_i\ker(s^i:B^q\to B^{q-1})\), with differential \(\sum_i(-1)^id^i\). Successively subtracting the codegenerate components splits \(B^q\) into its normalized summand and the summands indexed by proper degeneracies. Applied to the displayed direct sum, this recovers \(P^q\) and its differential. Applied to any cosimplicial module, the same decomposition reconstructs it from its normalization. This proves the normalization–denormalization equivalence used here.

Define
\[
L\Gamma^n(P)=N\bigl(\Gamma^n(D(P))\bigr).
\tag{2.7}
\]
A cosimplicial homotopy consists of maps satisfying the face and degeneracy identities. Applying any functor to those maps preserves those identities; normalization turns the resulting homotopy into a chain homotopy by the alternating prism sum. Hence (2.7) preserves homotopy equivalences. A quasi-isomorphism between bounded projective complexes is a homotopy equivalence, since its bounded acyclic projective cone splits successively. Thus (2.7) defines a functor on perfect nonnegative complexes, including their endomorphisms. If \(P\) occupies degrees \([0,b]\), its image occupies \([0,nb]\). Indeed, dualize to normalized simplicial symmetric powers. A tensor monomial in simplicial degree \(q\) is degenerate unless the union of the cuts in its \(n\) indexing surjections contains every one of the \(q\) cuts. Each contributing summand has at most \(b\) cuts, so a nondegenerate term requires \(q\le nb\). The normalized terms are direct summands of finite-projective terms.

The same construction on flat sheaves, checked on stalks, defines \(L\Gamma^n\) for bounded complexes with nonnegative Tor amplitude. Independence from a bounded flat representative follows as well. We give the flat-module argument needed here. If \(M\) is flat and a finite column of elements \(m\) satisfies a matrix relation \(Bm=0\), tensor the kernel–image sequence of \(B\) with \(M\). Flatness says that \(m\) is a finite sum of columns in \(\ker B\), with coefficients in \(M\). Thus \(m=Cn\) for a finite matrix \(C\) with \(BC=0\).

Consider all maps from finite free modules to \(M\). Their category is filtered: a direct sum receives two such maps, and the displayed relation calculation coequalizes two parallel maps. Indeed, transpose their difference to obtain the matrix \(B\); factoring the column of target generators as \(Cn\) gives a map to a new finite free module whose composite kills that difference. Its colimit is \(M\). It is onto because every element defines a map from the rank-one free module. It is injective because an element in a stage which maps to zero supplies another finite matrix relation, and the same factorization kills it at a later stage. This proves the finite-free presentation theorem for flat modules without a finite-generation assumption.

Apply this argument degree by degree in a fixed finite interval. A finite collection of elements and differential images factors through finite free modules. Construct the next degree to include those images, and coequalize the finite \(d^2=0\) relations there; proceed to the upper end of the interval. The same procedure incorporates maps, their commutation equations and homotopy components. It expresses a bounded flat complex and maps between such complexes as ind-objects of bounded finite-projective complexes. A finite diagram lifts to a common stage, and its finite equations hold after a further stage.

An acyclic bounded flat complex is zero in the corresponding ind-derived category. To verify this, map any stage, a bounded finite-projective complex \(Q\), into the limit complex. The Hom-complex from \(Q\) to an acyclic complex is acyclic, so that chain map is null-homotopic. Its finitely many homotopy components lift to a later stage, where their finitely many equations hold. Thus every stage map becomes zero. Apply this observation to the cone of a quasi-isomorphism of bounded flat complexes. It is an isomorphism between the ind-derived objects. The construction (2.7), already a functor on bounded projective complexes and their homotopy classes, preserves this isomorphism; it also commutes with filtered colimits, as its orbit-sum construction and normalization do. This proves the required quasi-isomorphism invariance on flat complexes. It does not assume that a nonlinear functor takes a mapping cone to a mapping cone.

Two properties will be useful. For a split module sum,
\[
\Gamma^n(M'\oplus M'')=
\bigoplus_{a+b=n}\Gamma^aM'\otimes\Gamma^bM''.
\tag{2.8}
\]
For a short exact sequence of flat modules with flat quotient, the corresponding filtration has these tensor products as its graded pieces. Define it by the images of tensors having at least a specified number of factors in the submodule. It is functorial; a splitting gives exactly (2.8). This also proves the assertion when a flat quotient is not projective. Express that quotient as a filtered colimit of finite free modules by the presentation theorem above. Pull the sequence back to each such module; it splits. Express its flat kernel as a filtered colimit of finite free modules as well. A finite collection of transition maps and their equations factors at a common later stage by the same matrix-relation argument. Consequently the original sequence is a filtered colimit of split sequences, and divided powers, tensors and the finite filtration commute with that colimit. For constructible finite-projective stalks one can use the splitting directly. Applying this filtration degreewise to denormalizations and then normalizing gives the corresponding finite filtration of (2.7). The diagonal of a bisimplicial tensor complex computes the tensor product of its normalizations: the Alexander–Whitney map takes front and back faces, its inverse sums the signed shuffles, and their composite differs from the identity by the prism homotopy. These maps use integral coefficients. Thus its graded pieces are
\(L\Gamma^a(P')\otimes^{\mathbf L}L\Gamma^b(P'')\).

**Lemma 2.4 (the algebraic coefficient identity).** For a perfect nonnegative complex \(P\) and an endomorphism \(u\),
\[
\det(1-tu\mid P)^{-1}
=\sum_{n\ge0}\operatorname{Tr}(L\Gamma^n(u);L\Gamma^n(P))t^n.
\tag{2.9}
\]
The trace on the right is the alternating perfect-complex trace.

**Proof.** Denote the right side by \(D(P,u)\). The filtration above and tensor multiplicativity of trace show that
\(D(P,u)=D(P',u')D(P'',u'')\) for a compatible degreewise split short exact sequence. For \(M\) in degree zero, the identity is the usual complete-symmetric coefficient identity. To verify it over every ring, first take a free module and a universal matrix over \(\mathbf Z[z_{ij}]\). Each coefficient is a polynomial in its entries. Over its characteristic-zero fraction field a diagonalizable matrix gives both sides as \(\prod_i(1-\alpha_it)^{-1}\), so the polynomial identities hold in the universal ring and after every specialization. Adding a complementary projective summand with zero endomorphism gives the projective case.

Place the same \(M\) in degrees \(q,q+1\) with differential the identity. This complex is contractible, so its positive derived symmetric powers are zero. Its stupid filtration therefore gives
\(D(M[-q],u)D(M[-q-1],u)=1\).
Induction on \(q\) proves that a shift to degree \(q\) raises the degree-zero expression to \((-1)^q\). Apply the stupid filtration to \(P\). Its product is precisely (2.3) inverted, proving (2.9). Because the right side is invariant under a compatible homotopy equivalence, (2.3) has the same invariance for nonnegative complexes. Shift a general perfect complex into nonnegative degrees; its determinant is inverted for an odd shift. This proves invariance in general. The same degreewise filtration proves determinant multiplicativity for the compatible filtered complexes arising from support and coefficient sequences. \(\square\)

### Symmetric powers with external coefficients

Let \(X\) be quasi-projective over an algebraically closed field, and let \(\pi_n:X^n\to\operatorname{Sym}^nX\) be the finite quotient. For a flat sheaf \(M\), set
\[
\Gamma^n_{\mathrm{ext}}M
=\bigl(\pi_{n*}(M\boxtimes\cdots\boxtimes M)\bigr)^{\mathfrak S_n}.
\tag{2.10}
\]
At the cycle \(z=\sum_i a_ix_i\), with distinct geometric points \(x_i\), its stalk is
\[
(\Gamma^n_{\mathrm{ext}}M)_z
=\bigotimes_i\Gamma^{a_i}(M_{x_i}).
\tag{2.11}
\]
To verify this, the stalk of the finite pushforward is the sum over the ordered lifts of the cycle. Invariants on this transitive orbit are the invariants under its stabilizer \(\prod_i\mathfrak S_{a_i}\), giving the displayed formula. Flatness permits tensoring the successive invariant modules; their orbit-sum descriptions show that the result remains flat. Presentations by flat sheaves extend this to divided powers on arbitrary sheaves. Denormalization and normalization then give \(L\Gamma^n_{\mathrm{ext}}K\) for nonnegative finite-Tor complexes.

The stalk formula proves coefficient base change and base change of the scheme, and proves compatibility with closed restriction and open extension by zero. For the latter, a cycle outside \(\operatorname{Sym}^nU\) has a factor with zero stalk. Formula (2.8) gives a finite filtration for a coefficient sequence, whose graded pieces are
\[
v_{a,b*}\bigl(L\Gamma^a_{\mathrm{ext}}K'
\boxtimes^{\mathbf L}L\Gamma^b_{\mathrm{ext}}K''\bigr),
\qquad a+b=n,
\tag{2.12}
\]
where \(v_{a,b}\) is the finite map adding two effective cycles. These statements are assertions about the complexes and their filtrations, so they preserve coefficient endomorphisms.

Evaluation of compactly supported sections, followed by the external product, defines a natural comparison
\[
\kappa_n:L\Gamma^nR\Gamma_c(X,K)
\longrightarrow
R\Gamma_c(\operatorname{Sym}^nX,L\Gamma^n_{\mathrm{ext}}K).
\tag{2.13}
\]
Here are representatives on which to construct the map. Choose a projective compactification \(j:X\hookrightarrow\overline X\), and a bounded nonnegative flat representative of \(j_!K\). For a flat sheaf \(M\), its Godement resolution starts with the sheaf of products of its geometric stalks. Evaluation at each geometric point splits the augmentation on that stalk. Successive cokernels give an augmented resolution split at every stalk, functorially in \(M\). Its terms are acyclic for sections. Products of flat \(A\)-modules are flat because \(A\) is Noetherian: for a finite matrix relation \(Bm=0\) in a product, choose a fixed finite set of generators of \(\ker B\). Flatness in each factor expresses its components as combinations of those generators; collecting their coefficients gives the same expression in the product. The flatness criterion proved above applies. Filtered colimits of these products compute the stalks, so the Godement terms are flat. Their stalk-split successive quotients are flat too.

Truncate each Godement column at order \(N\), with \(N\) at least the cohomological dimension of \(\overline X\), using its kernel as the last term. Dimension shifting in the acyclic resolution gives \(H^i(\overline X,Z^N)=H^{i+N}(\overline X,M)=0\) for \(i>0\); thus that last term is acyclic too. The truncated column remains split at every stalk. Totalizing these finitely many columns gives a bounded nonnegative flat complex \(Q\), stalkwise homotopy equivalent to \(j_!K\), with every term acyclic for sections. Its sections are flat modules: for any flat acyclic term \(T\), the proper projection formula identifies
\[
\Gamma(\overline X,T)\otimes_A^{\mathbf L}V
=R\Gamma(\overline X,T\otimes_A\underline V)
\]
for an arbitrary module \(V\). The right side has no negative cohomology. Hence the left has no positive Tor, which proves flatness of \(\Gamma(\overline X,T)\). The sections of \(Q\) therefore form a bounded flat representative of \(R\Gamma_c(X,K)\).

Apply the external-product map of sections in each cosimplicial degree of \(D(Q)\), then take invariant symmetric tensors and normalize. Finite direct sums and normalization kernels commute with sections. This gives
\[
L\Gamma^n\Gamma(\overline X,Q)
\longrightarrow
\Gamma(\operatorname{Sym}^n\overline X,L\Gamma^n_{\mathrm{ext}}Q)
\longrightarrow
R\Gamma(\operatorname{Sym}^n\overline X,L\Gamma^n_{\mathrm{ext}}Q).
\]
At a cycle meeting the boundary, a stalk of \(Q\) is contractible, so the last coefficient complex has zero cohomology there. Its restriction on \(\operatorname{Sym}^nX\) is \(L\Gamma^n_{\mathrm{ext}}K\). Thus the final expression is the target of (2.13). If two prepared resolutions represent the same complex, resolve their maps by a common Godement resolution and use a truncation order large enough for both. Their section complexes are bounded flat quasi-isomorphic representatives; the quasi-isomorphism invariance proved for (2.7) identifies the resulting maps. Homotopies are preserved as well, so this construction descends through the derived-category roofs and is independent of representatives.

The same construction on a relative compactification gives the comparison for \(u:X\to Y\), with target on \(\operatorname{Sym}^nY\). Use the uniform proper-fibre dimension bound for the truncation; flatness of the direct-image terms follows stalkwise from the proper projection formula in the same way. The degreewise evaluation maps respect composition, tensor extension and the maps adding cycles. Their identities persist after normalization and passage through the common resolutions. This proves compatibility with composition, coefficient extension, base change and (2.12). Common compactification refinements and the boundary-stalk calculation prove independence of compactification. In degree zero for a point the map is the identity. Naturality with respect to the coefficient correspondence also proves Frobenius compatibility.

**Lemma 2.5 (symmetric Künneth).** The comparison (2.13) is an isomorphism for constructible finite-Tor \(K\) of nonnegative Tor amplitude and for the prime-to-characteristic torsion ring \(A\) above.

**Proof.** We give the reduction as well as its final curve argument. First reduce the coefficient ring, also for the relative form of (2.13), to its residue fields. Both comparisons commute with derived coefficient extension. Their stalk complexes are bounded and perfect: Lemma 2.3 and its fibrewise version give this for compact support, and the divided-power degree bound gives it for the source. A perfect cone whose tensor with every residue field is acyclic is zero. Locally over a local ring, cancel every invertible differential entry in a finite free representative; the remaining minimal complex has zero differential after tensoring with its residue field, so it has no terms. Localization at all primes proves the assertion. We may therefore work over a field \(a\) of positive characteristic \(\ell\ne p\).

Ordinary compact-support Künneth over this field follows from its \(\mathbf F_\ell\) version in the preceding course, even if \(a\) is infinite. Resolve tensor over \(a\) by the two-sided bar complex: its degree \(-r\) terms are \(E\otimes_{\mathbf F_\ell}a^{\otimes r}\otimes_{\mathbf F_\ell}K\), and its differential multiplies adjacent scalar factors or applies their actions. The insertion of the unit gives the usual contracting homotopy on the augmented free resolution, so this computes derived tensor over \(a\). The \(\mathbf F_\ell\) Künneth map applies to each term. Compact-support cohomology commutes with the sums and the totalizations here: its finite cohomological dimension lets one truncate sufficiently far to the left in each specified degree. The resulting map is Künneth over \(a\).

For a compatible short exact sequence of coefficient complexes, the filtrations (2.8) and (2.12) now show the following: if every \(\kappa_n\) is an isomorphism for two of the complexes, it is so for the third. Induct on \(n\). The interior graded pieces have indices \(a,b<n\); their comparisons are isomorphisms by the induction and ordinary compact-support Künneth. The two end pieces are the degree-\(n\) comparisons in question. Two of them and the filtered middle comparison determine the third by their cohomology long exact sequences. This proves the reduction without assuming that a nonlinear functor takes an arbitrary triangle to a triangle.

For the relative comparison, the finitely many points of a geometric cycle in a quasi-projective \(Y\) lie in an affine open: choose a hyperplane missing them in a projective embedding, and intersect its affine complement. Thus first work locally with an affine target. Use an affine locally closed stratification of \(X\) and the open–closed coefficient sequence to reduce to an affine source. Its morphism factors as a closed immersion into \(\mathbf A^r_Y\) followed by successive projections. The relative dimensions of these factors are at most one. Compatibility with composition reduces the theorem to such a map \(u\). Check at a geometric cycle of \(\operatorname{Sym}^nY\) and make its algebraically closed base-field extension. Restriction to the finite reduced union of the points in that cycle commutes with both sides. The source is then a finite disjoint union of schemes of dimension at most one. The direct-sum formula and ordinary Künneth reduce this to compact-support cohomology of a single curve, or a finite scheme, over an algebraically closed field.

Over \(a\), coefficient filtrations and the contractible two-term complex used in Lemma 2.4 reduce bounded complexes to sheaves in degree zero. For a constructible sheaf, stratify and trivialize its finite monodromy. If \(G\) is its finite image, take the cover corresponding to an \(\ell\)-Sylow subgroup. Its degree is prime to \(\ell\), so pullback followed by trace makes the original sheaf a direct summand of the pushforward of its pullback. A representation of an \(\ell\)-group in characteristic \(\ell\) has a filtration with trivial quotients. Indeed, a central element of order \(\ell\) has nilpotent \(g-1\); its nonzero kernel is stable, and induction on the quotient group produces a fixed vector, after which induction on dimension gives the filtration. The coefficient reduction and compatibility with a finite pushforward now reduce to constant coefficients on a finite cover of the curve. Nilpotent invariance, normalization, its finite exceptional set and a projective completion reduce this to a smooth connected projective curve \(C\) with constant \(\mathbf F_\ell\)-coefficients. The finite-set case is (2.11) itself.

Suppose first that \(C\) is a complex curve. Apply proper comparison to both \(C\) and \(\operatorname{Sym}^nC\). Theorem 7.2 of the preceding comparison lesson proves this in every dimension by a graph construction and induction from projective curves; thus comparison on the curve alone is not being assumed to compare its higher-dimensional symmetric powers. Exact analytification preserves the finite pushforward in (2.10), the stalk invariants and the flat divided-power construction. The comparison's external-product compatibility therefore identifies (2.13) with its topological counterpart. Triangulate the compact surface \(C^{\mathrm{an}}\). A closed simplex \(D\) and every nonempty intersection of its faces are contractible. Applying a contraction simultaneously to every point contracts \(\operatorname{Sym}^nD\). Consequently both sides of (2.13) for \(D\) are the coefficient field in degree zero, and the comparison is the identity on constants. Build the triangulated surface from its finitely many closed simplices. For a union of closed subcomplexes \(B\cup D\) use the exact coefficient sequence
\[
0\to a_{B\cup D}\to a_B\oplus a_D\to a_{B\cap D}\to0,
\]
with the sheaves extended by their closed embeddings. Its last map is the difference of restrictions. The stalk sequence is exact, including at an intersection. The nonlinear coefficient-filtration reduction already proved, inductively on the simplices and their faces, establishes every \(\kappa_n\) for the union. This proves the complex-curve case; it uses no averaging by \(n!\).

For an algebraically closed field of characteristic zero, descend the curve and the comparison to a finitely generated subfield, embed that field in \(\mathbf C\), and use the proper smooth and algebraically closed base-extension comparisons from the preceding course. They preserve the map (2.13), so the complex-curve case applies.

In characteristic \(p>0\), lift the smooth projective curve to a smooth projective curve \(\mathscr C\) over the complete Witt ring \(W(k)\). Theorem 8.1 of [Deformations of rings and schemes and the naive cotangent complex](course:AG-HP/deformations-of-rings-and-schemes-and-the-naive-cotangent-complex) supplies the smooth-chart gluing obstruction \(H^2(C,T_C)\otimes(p^r/p^{r+1})\). It is zero on a curve. That theorem applies to mixed-characteristic complete local coefficient rings as well as equal characteristic, so induction produces compatible flat smooth deformations over \(W(k)/p^r\). Theorem 5.1 of [Algebraization of formal schemes](course:AG-QC/algebraization-of-formal-schemes) applies: the closed fibre is projective, the base is complete Noetherian local, and \(H^2(C,\mathcal O_C)=0\). It gives a projective flat algebraization, using its explicit line-bundle lifting and fixed projective embedding construction. Smoothness holds along the closed fibre by the smooth charts. The nonsmooth locus is closed; its proper image in the local base would contain the closed point if nonempty. Hence that locus is empty and the algebraization is smooth.

Every \(\operatorname{Sym}^n\mathscr C\) is smooth and projective over \(W(k)\). In étale coordinates at a cycle, group its distinct support points in separate coordinate neighbourhoods. Each multiplicity group has the elementary symmetric coordinates of \(\operatorname{Sym}^a\mathbf A^1=\mathbf A^a\). The completed local ring has the corresponding independent symmetric parameters, so the finite-presentation smoothness criterion gives smoothness; no assumption that \(n!\) is invertible occurs. Proper smooth base change therefore identifies the cohomology of \(\mathscr C\) and of all its symmetric powers on the two geometric fibres. Their cohomology sheaves are locally constant. A bounded complex with finite locally constant cohomology over \(\mathbf F_\ell\) is étale locally a constant perfect complex: successively split its finite truncation triangles after killing their finitely many local extension classes. Applying the derived divided-power construction therefore preserves local constancy and coefficient compatibility. The comparison (2.13) is consequently an isomorphism on the special fibre if it is so on the geometric generic fibre. That fibre has characteristic zero, where it was just proved. This finishes the curve case and all the reductions. \(\square\)

The ordinary Künneth input is [Cohomological dimension and the Künneth formula](course:ag-etale-cohomology/cohomological-dimension-and-the-kunneth-formula), Theorem 9.1: compactify both factors and extend both coefficients by zero; their external product extends by zero on the product compactification, as is checked on stalks. Its one-proper-factor formula is then the required compact-support formula. The comparison input is [Comparison with singular cohomology](course:ag-etale-cohomology/comparison-with-singular-cohomology), Lemma 3.1 and §§5–9, including proper comparison on every symmetric power. Its projective-curve foundations now have written programme proofs: [Comparison with topology](course:AG-DFG/AG-DFG-08), Theorem 3.1, proves proper Riemann existence from coherent GAGA; [Serre's comparison theorems and Chow's theorem](course:AG-QC/serres-comparison-theorems-and-chows-theorem), Theorems 3.1, 4.1 and 5.2, prove projective coherent GAGA. Only their projective case is needed here. The GAGA lesson specifies its remaining analytic finiteness and vanishing prerequisites. Smooth specialization is supplied by [Smooth base change and local acyclicity](course:ag-etale-cohomology/smooth-base-change-and-local-acyclicity), Corollary 11.3 and Theorem 12.2. The deformation and formal-algebraization proofs are at the exact homes linked above. The symmetric-power construction, filtrations, reduction and final simplex argument have been supplied here.

### Comparing every coefficient of the Euler product

**Proof of Theorem 2.2.** Open–closed multiplicativity permits an affine stratification, so suppose first that \(X_0\) is affine; all its symmetric powers exist. Shift the coefficient complex into nonnegative Tor degrees. An odd shift inverts both sides of (2.4), so proving the formula there proves it in general.

Lemma 2.4 expands each local inverse determinant. The coefficient of \(t^n\) in their product is indexed by the effective zero-cycles of degree \(n\) on \(X_0\). Such a cycle gives a geometric cycle fixed by Frobenius in \(\operatorname{Sym}^nX\); each closed point of degree \(d\) contributes its entire orbit of \(d\) geometric points. The local operator on the stalk in (2.11) cyclically permutes the orbit factors and applies the stalk correspondence at each step. Its alternating trace is the trace of the resulting local Frobenius on the relevant derived symmetric power. One can check this statement directly by taking a finite scheme containing these finitely many closed points. There, global sections are an exact finite direct sum, (2.11) identifies its symmetric tensors with the sum over cycles, and the Frobenius matrix permutes the summands. Only its fixed summands contribute to the trace. The coefficient identity (2.9) for that finite direct sum then gives
\[
[t^n]L(X_0,K_0,t)
=\sum_{z\in\operatorname{Sym}^nX_0(\mathbf F_q)}
\operatorname{Tr}(F_z;(L\Gamma^n_{\mathrm{ext}}K)_z).
\tag{2.14}
\]
For any fixed \(n\) this finite scheme can include every closed point of degree at most \(n\), so the calculation proves (2.14) on \(X_0\). It also handles complexes and their signs, without guessing a permutation sign on ordinary tensor powers.

The right side of (2.4), expanded by (2.9), has coefficient
\[
\begin{aligned}
\operatorname{Tr}(L\Gamma^nF;L\Gamma^nR\Gamma_c(X,K))
&=\operatorname{Tr}(F;R\Gamma_c(\operatorname{Sym}^nX,
                 L\Gamma^n_{\mathrm{ext}}K))\\
&=\sum_{z\in\operatorname{Sym}^nX_0(\mathbf F_q)}
\operatorname{Tr}(F_z;(L\Gamma^n_{\mathrm{ext}}K)_z).
\end{aligned}
\tag{2.15}
\]
The first equality is the Frobenius-compatible isomorphism of Lemma 2.5. The second is Lemma 2.3's additive trace formula on the symmetric power. Its coefficient complex is constructible and of finite Tor amplitude by (2.11), the bounded-degree construction and its flat representatives. Thus every coefficient in (2.14) and (2.15) agrees in \(A\). This proves (2.4) in the affine case.

For a general separated finite-type scheme, choose a finite affine locally closed stratification as in Lesson 7. Its local Euler product is the product over the strata. Compact support has the compatible finite support filtration, so determinant multiplicativity from Lemma 2.4 gives the identical product for the cohomological side. This proves the theorem in general. Perfectness was Lemma 2.3. \(\square\)

This is the coefficient method of Deligne, *SGA 4½*, *Fonctions L modulo \(\ell^n\) et modulo \(p\)*, §§1–2, especially Theorem 2.2(a). The symmetric Künneth argument comes from Deligne, SGA 4, Exposé XVII, §§5.5.1–5.5.28. The proof above explains the nonlinear derived operation, the geometric reduction and the coefficient comparison; equality of logarithmic derivatives alone would leave the torsion theorem unproved.

### Artin–Schreier and symmetric powers in characteristic \(p\)

The divided-power algebra and the construction of (2.13) also apply to \(\mathbf F_p\). The geometric proof of Lemma 2.5 must change: proper smooth specialization with these coefficients is unavailable. We instead compare with coherent cohomology using Artin–Schreier.

**Lemma 2.6 (semilinear fixed vectors).** Let \(k\) be algebraically closed of characteristic \(p\), and let \(V\) be finite dimensional over \(k\), with a \(p\)-semilinear endomorphism \(\varphi\). Then
\[
V=(V^{\varphi=1}\otimes_{\mathbf F_p}k)\oplus V_{\mathrm{nil}},
\tag{2.16}
\]
where \(\varphi\) is nilpotent on the second summand. The functor of fixed vectors is exact on these semilinear spaces, and commutes with divided powers.

**Proof.** Since \(k\) is perfect, images and kernels of the powers of \(\varphi\) are \(k\)-subspaces. Choose \(r\) at which their dimensions stabilize. Their intersection is zero: \(\varphi\) is bijective on its stable image, so no nonzero element there is killed by a power. Dimensions give the direct sum of the stable image and kernel. This proves the unique invertible–nilpotent decomposition.

On the invertible summand of dimension \(s\), write \(\varphi(x)=Bx^{[p]}\) with \(B\) invertible. The equation \(\varphi(x)-x=c\) becomes
\(x_i^p-\sum_j(B^{-1})_{ij}x_j=(B^{-1}c)_i\).
The monic leading monomials \(x_i^p\) are relatively prime; polynomial division, with the overlap relations obtained by substituting these same equations in either order, leaves exactly the monomials with every exponent less than \(p\). Thus each fibre has length \(p^s\). Its Jacobian is \(-B^{-1}\), so it is reduced. Over the algebraically closed field it therefore consists of \(p^s\) points. In particular \(\varphi-1\) is surjective and its kernel is an \(s\)-dimensional \(\mathbf F_p\)-space.

An \(\mathbf F_p\)-basis of that kernel is independent over \(k\). In a shortest contrary relation, normalize one coefficient to \(1\), apply \(\varphi\), and subtract. Minimality forces all the other coefficients to satisfy \(c^p=c\), making the relation an \(\mathbf F_p\)-relation. Hence the fixed basis is a \(k\)-basis of the invertible summand. On the nilpotent summand, \(\varphi-1\) has inverse \(-\sum_{j<r}\varphi^j\) and no fixed vectors. This proves (2.16).

For an exact sequence, lift a fixed vector in its quotient. Its error under \(\varphi-1\) lies in the subspace; surjectivity of \(\varphi-1\) there corrects the lift. This proves exactness. Finally use (2.8) on (2.16). Each summand involving a positive divided power of \(V_{\mathrm{nil}}\) has nilpotent induced \(\varphi\), hence no fixed vectors. On the remaining summand the orbit-sum basis has scalar Frobenius, whose fixed coefficients are \(\mathbf F_p\). Its fixed module is exactly \(\Gamma^n_{\mathbf F_p}(V^{\varphi=1})\). \(\square\)

Algebraic closedness matters here. Over \(k=\mathbf F_3\), multiplication by \(-1\) is a bijective \(3\)-semilinear map with zero fixed space. Its second divided power is the identity and has nonzero fixed space. Thus a perfect field alone does not give (2.16), exactness of fixed vectors, or their compatibility with divided powers. The geometric application below takes place over an algebraic closure. This supplies the needed hypothesis in the auxiliary lemmas of SGA 4, XVII, §§5.5.36–5.5.37.

**Lemma 2.7 (symmetric Künneth for \(p\)-torsion).** The map (2.13) is an isomorphism for bounded constructible complexes over \(\mathbf F_p\), and over a finite extension of \(\mathbf F_p\).

**Proof.** The reductions of Lemma 2.5 still apply. Ordinary compact-support Künneth is Theorem 9.1 of the preceding Künneth lesson, on the two proper compactifications; that theorem allows characteristic torsion. The coefficient filtrations, factorization through relative curves, Sylow trace cover, trivial-quotient filtration and normalization therefore reduce to constant \(\mathbf F_p\) on a smooth projective curve over an algebraically closed field \(k\). We prove this case without a lift.

First establish the coherent analogue of symmetric Künneth. For a quasi-projective \(k\)-scheme \(Y\) and a quasi-coherent sheaf \(M\), define the coherent external divided power by invariants of the finite pushforward from \(Y^n\), taking external tensor over \(k\). On an affine \(Y=\operatorname{Spec}B\), with module of sections \(N\), its sections are \(\Gamma^n_kN\), and its base ring is \((B^{\otimes_k n})^{\mathfrak S_n}\). This description is functorial. All modules are flat over \(k\), so denormalization defines its derived operation on bounded nonnegative complexes.

The coherent comparison
\[
L\Gamma^n_kR\Gamma(Y,M)\longrightarrow
R\Gamma(\operatorname{Sym}^nY,L\Gamma^n_{\mathrm{ext,coh}}M)
\tag{2.17}
\]
is an isomorphism. Here is its affine reduction. A finite affine covering of the separated \(Y\) has affine intersections; its alternating Čech resolution expresses \(M\) by a finite complex of sums of \(j_*M|_U\), with \(U\) affine. The divided-power coefficient filtration and induction on its degree, exactly as for (2.12), permit this reduction through the finite resolution. The composition rule reduces each such term to the comparisons for \(U\to Y\) and \(U\to\operatorname{Spec}k\). To check the first, a finite cycle on \(Y\) has its support in an affine open \(Y_1\). The opens \(\operatorname{Sym}^nY_1\) cover the target. The intersection \(U\cap Y_1\) is affine, and both its symmetric power and that of \(Y_1\) are affine. Quasi-coherent higher direct images vanish for these affine maps. The comparison is therefore the module identity just described. The second map has affine source and target and is the same identity. Bounded complexes follow through their finite degree filtrations and the contractible two-term shift argument. This proves (2.17). In particular, for \(M=\mathcal O_Y\), its external divided power is \(\mathcal O_{\operatorname{Sym}^nY}\).

The exact Artin–Schreier sequence
\[
0\to\mathbf F_p\to\mathcal O_Y
\xrightarrow{\varphi-1}\mathcal O_Y\to0
\tag{2.18}
\]
holds on the étale site: an equation \(z^p-z=a\) gives an étale surjective cover, and its kernel is the constant \(\mathbf F_p\). For proper \(Y\), coherent cohomology is finite dimensional over \(k\). Lemma 2.6 makes \(\varphi-1\) surjective on each of its groups, so
\(H^i(Y,\mathbf F_p)=H^i(Y,\mathcal O_Y)^{\varphi=1}\).

This fixed-vector assertion is compatible with the derived divided-power operation, including its comparison map. To verify that point, represent the coherent cohomology complex by a bounded complex \(L\) of finite-dimensional \(k\)-spaces and its semilinear correspondence, and represent the finite étale groups by a bounded \(\mathbf F_p\)-complex \(P\). The map \(u:P\to L\) satisfies \(H^*(\varphi u)=H^*(u)\). Hence \(\varphi u-u=dH+Hd\), because complexes over a field split into cohomology and contractible terms. Solve \((\varphi-1)H_0=H\) termwise using Lemma 2.6 on the finitely many Hom components, and replace \(u\) by \(u-(dH_0+H_0d)\). It now satisfies \(\varphi u=u\). Exactness of fixed vectors says that \(P\to L^{\varphi=1}\) is a quasi-isomorphism. Denormalization, Lemma 2.6 and normalization consequently identify the fixed complex of \(L\Gamma^n_kL\) with \(L\Gamma^n_{\mathbf F_p}P\); fixed vectors commute with its cohomology as well. The preceding flat-invariance proof ensures independence of the representatives.

Apply this argument to \(Y=C\) and \(Y=\operatorname{Sym}^nC\). The coherent map (2.17) is Frobenius compatible, since its affine map is an external product of functions. Passing to fixed vectors identifies it with the étale map (2.13). Thus that map is an isomorphism. This proves the final curve case and all the reductions. Extension to a finite coefficient field commutes with the constructions and follows either by scalar extension on the constant case or by the same Sylow reduction. \(\square\)

### The trace formula with characteristic torsion

We need a different additive trace theorem before comparing coefficients of the Euler product. The geometric step is a coherent trace calculation on a curve.

**Lemma 2.8 (coherent curve trace).** Let \(k\) be algebraically closed, \(C/k\) smooth projective, \(f:C\to C\) have finitely many fixed points with \(1-df_x\ne0\), and let \(E\) be a vector bundle with \(u:f^*E\to E\). Then
\[
\sum_i(-1)^i\operatorname{Tr}(uf^*;H^i(C,E))
=\sum_{f(x)=x}\frac{\operatorname{Tr}(u_x)}{1-df_x}.
\tag{2.19}
\]
For the Frobenius correspondence of a curve over \(\mathbf F_q\), every denominator is \(1\).

**Proof.** Use coherent curve Serre duality, with its normalized trace \(H^1(C,\omega_C)\to k\). Its programme proof is [Dualizing sheaves and Serre duality for projective schemes](course:AG-QC/dualizing-sheaves-and-serre-duality-for-projective-schemes), Theorem 4.2. The local trace normalization follows from the one-equation resolution of a point: the class of \(dt/t\) is the counit of its closed immersion, and has trace \(1\). Composition of the closed-immersion and projective adjunctions proves this equality; their explicit computations are [The right adjoint of derived pushforward](course:AG-QC/the-right-adjoint-of-derived-pushforward), Proposition 1.1, Theorem 3.1 and §§4–5. Only bounded projective duality is needed for this argument.

On \(C\times C\), put \(B=p_1^*(E^\vee\otimes\omega_C)\otimes p_2^*E\). The diagonal has normal line \(T_C\), so its residue sequence is
\[
0\to B\to B(\Delta)\to\Delta_*\operatorname{End}(E)\to0.
\]
Let \(c_\Delta\in H^1(C\times C,B)\) be the boundary of the identity. Coherent Künneth follows from the tensor product of finite affine Čech complexes. Under it, \(c_\Delta\) is the identity kernel for Serre duality: if \(e_{ij}\) is a basis of \(H^i(C,E)\) and \(e_{ij}^\vee\) its trace-dual basis, its components are
\(\sum_{i,j}(-1)^i e_{ij}^\vee\otimes e_{ij}\).
Here is a check of this kernel identity on classes, including its sign. A vector bundle on a smooth curve embeds in its sheaf of rational sections. The quotient is the sum of its principal-part sheaves at the closed points. Both are acyclic: rational sections restrict identically on nonempty opens of an integral component, and each principal-part sheaf is a skyscraper. Thus this two-term resolution computes \(H^0\) as its kernel and \(H^1\) as its cokernel. Trivialize \(E\) at a point with parameter \(t\). The diagonal's local residue representative is \(dt_1/(t_1-t_2)\) times the identity matrix. Its two Laurent expansions are
\[
\frac1{t_1-t_2}=\sum_{m\ge0}t_2^m t_1^{-m-1},
\qquad
\frac1{t_1-t_2}=-\sum_{m\ge0}t_1^m t_2^{-m-1}.
\]
For a Laurent polynomial \(h(t_1)\), contraction and residue in \(t_1\) return, respectively, its nonnegative part and minus its principal part. Their difference is \(h(t_2)\). For a formal regular series the calculation holds coefficient by coefficient; for a principal part only finitely many negative terms occur. This computes the induced maps on both terms of the rational-section resolution. It is the identity on regular sections and principal-part classes, and therefore on its kernel and cokernel. Changes of frame preserve the identity matrix, so the computation glues. Interchanging the degree-one class with its dual introduces the Koszul sign \(-1\). Consequently the kernel has the displayed positive degree-zero and negative degree-one components. These two components exhaust the coherent Künneth decomposition and prove the asserted identity, using no analytic convergence.

Pull this residue sequence back to the graph \(t\mapsto(t,f(t))\), and contract with \(u\). The graph meets the diagonal transversely by \(1-df_x\ne0\). The pullback of \(c_\Delta\) is a class in \(H^1(C,\omega_C)\). Its trace, from the displayed Künneth expression, is the left side of (2.19). On the other hand it is the boundary of the principal parts
\(\operatorname{Tr}(u(t))\,dt/(t-f(t))\) at the fixed points. In the local parameter \(t-t(x)\), their residues are \(\operatorname{Tr}(u_x)/(1-df_x)\). Each residue boundary has exactly that trace by the point counit computation. Adding the finitely many boundaries proves (2.19). Frobenius has zero differential, giving the last assertion. The calculation also works component by component if Frobenius permutes connected components; nonfixed components contribute zero to either trace. \(\square\)

**Theorem 2.9 (additive trace modulo \(p\)).** For a separated finite-type \(X_0/\mathbf F_q\) and a bounded constructible complex over a finite field \(a\) of characteristic \(p\),
\[
\sum_{x\in X_0(\mathbf F_q)}\operatorname{Tr}_a(F_x;K_{\bar x})
=\operatorname{Tr}_a(F;R\Gamma_c(X,K)).
\tag{2.20}
\]

**Proof.** Start with \(a=\mathbf F_p\) and a local system \(G_0\) on an open \(U_0\) of a smooth projective curve \(C_0\). The coherent bundle \(G_0\otimes_{\mathbf F_p}\mathcal O_{U_0}\) carries its \(p\)-semilinear map \(\varphi\), acting on the structural factor. Extend it to a vector-bundle lattice \(Q_0\) on \(C_0\) so that \(\varphi(Q_0)\subset I Q_0\), where \(I\) is the ideal of the finite boundary. Such a lattice exists: choose any coherent locally free extension, and at each boundary parameter bound the poles of the matrix of \(\varphi\) by \(c\). Replacing that lattice by its \(t^n\)-multiple gives the bound \(np-c\ge n+1\) for large \(n\). Glue these finitely many modifications to the unchanged bundle on \(U_0\).

On \(C\) there is then an exact sequence
\[
0\to j_!G\to Q\xrightarrow{\varphi-1}Q\to0.
\tag{2.21}
\]
Its kernel on \(U\) is Artin–Schreier. Near the boundary a fixed section belongs to every power of its maximal ideal, since \(\varphi\) multiplies the exponent by \(p\) and contracts the lattice. Krull intersection makes it zero there. Surjectivity is étale local: in a free frame, the additive polynomial map \(x\mapsto Bx^{[p]}-x\) has Jacobian \(-1\), hence is étale. On each algebraically closed fibre its image is an open subgroup of the connected additive group, therefore the whole group. This gives an étale surjective map of sheaves. These verifications prove (2.21).

Let \(V_0^i=H^i(C_0,Q_0)\), finite dimensional over \(\mathbf F_q\). Write \(q=p^f\). On \(V^i=V_0^i\otimes k\), Lemma 2.6 makes \(\varphi-1\) surjective, so (2.21) identifies \(H^i_c(U,G)\) with its fixed vectors. The geometric Frobenius on these vectors is induced by the \(k\)-linear map \(T=(\varphi_0^f)\otimes1\), not by the semilinear extension of \(\varphi^f\). Indeed the absolute Frobenius pullback, followed by the structural correspondence, has this linear map after descent from \(\mathbf F_q\); on the fixed étale kernel its coefficient correspondence is the identity, as in Lesson 3. The maps commute with \(\varphi\). The stable nilpotent summand has nilpotent \(T\), hence zero trace, while on the stable summand (2.16) extends the matrix on fixed vectors. Consequently
\(\operatorname{Tr}_{\mathbf F_p}(F;H^i_c(U,G))=\operatorname{Tr}_{\mathbf F_q}(\varphi_0^f;V_0^i)\), viewed in \(k\).

Apply Lemma 2.8 to \(Q\), relative \(q\)-Frobenius and the linearization of \(\varphi_0^f\). At a boundary point the lattice contraction makes its fibre map zero. At an interior rational point its fibre trace is the trace on \(G_{\bar x}\). The coherent trace is therefore exactly (2.20). Finite points are immediate; normalization, a finite boundary and open–closed coefficient sequences extend this to every constructible sheaf on a curve. Finite cohomology truncations extend it to bounded complexes.

For affine \(X_0\), embed it as a closed subscheme of \(\mathbf A^r\) and push its coefficients through the closed embedding. Induct on \(r\), using projection \(\mathbf A^r\to\mathbf A^{r-1}\). At every rational point of the target, compact-support base change computes the Frobenius trace on the direct image by the already proved curve formula on its affine-line fibre. The inductive formula on the target and \(R\Gamma_c Rf_!=R\Gamma_c\) give (2.20). Compact-support constructibility and the finite degree bound keep the direct image bounded constructible; these are the exact preceding compact-support foundations. Finite affine stratification proves the separated finite-type case.

For a finite extension \(a/\mathbf F_p\), restriction of scalars gives the field trace of the proposed equality. To recover the equality itself, tensor with the rank-one constant-base local system whose geometric Frobenius is multiplication by each \(\lambda\in a^*\). The same formula after restriction of scalars says that the difference \(D\in a\) satisfies \(\operatorname{Tr}_{a/\mathbf F_p}(\lambda D)=0\) for every \(\lambda\). The finite separable field-trace pairing is nondegenerate, so \(D=0\). The twist exists because \(\lambda\) has finite order. This proves the theorem. \(\square\)

### Reduced characteristic-\(p\) coefficient rings

**Theorem 2.10.** Formula (2.4) also holds for a commutative Noetherian reduced ring \(A\) of characteristic \(p\), with \(K_0\in D_{\mathrm{ctf}}(X_0,A)\).

**Proof.** Compact-support perfection holds in this case too. The preceding compact-support course supplies finite generation with Noetherian torsion coefficients, without excluding characteristic torsion. Its projection formula and amplitude \([0,2\dim X]\) give a finite Tor interval for \(R\Gamma_c(X,K)\). A bounded complex with finitely generated cohomology and finite Tor amplitude over a Noetherian ring is perfect: take successive finite free presentations and truncate beyond that Tor interval; dimension shifting makes the last finite syzygy projective locally. This also proves coefficient-base-change compatibility of its perfect determinant. This use retains the explicit general-finiteness foundation in [Cohomology with compact support](course:ag-etale-cohomology/cohomology-with-compact-support), §12.

If \(A\) is a finite field, repeat the coefficient comparison (2.14)–(2.15), using Lemma 2.7 and Theorem 2.9. All its algebraic determinant steps work in characteristic \(p\); they involve no division. Thus (2.4) holds over finite fields of characteristic \(p\).

For general \(A\), descend the finite coefficient data to a finitely generated \(\mathbf F_p\)-subalgebra \(B\subset A\). The finite-presentation generators and compactness required for this step are proved in [Constructible sheaves and extension by zero](course:ag-etale-cohomology/constructible-sheaves-and-extension-by-zero), §§4–5, especially Lemma 5.2. Take a bounded constructible flat representative. Present each term by finite sums of the generators \(a_!A\) on finitely presented affine étale objects. A presentation map is specified by finitely many sections, each locally a finite list of coefficients on a finite covering. Include those coefficients in \(B\). Compactness and the finite equalizer description on a qcqs basis descend the differentials, their zero composites, and the Frobenius correspondence at a later stage.

Flatness must also descend; it does not follow from flatness after extension along the possibly nonflat \(B\to A\). Refine to a finite stratification and finite étale charts on which the finitely many presentation matrices \(D:A^s\to A^r\) are constant and their cokernels are projective. Each such matrix has a generalized inverse \(T\) with \(DTD=D\): split the surjection from \(A^r\) to its projective cokernel; its kernel is projective, so split the surjection from \(A^s\) to that kernel. Include the finitely many entries of \(T\) as well. Over \(B\), the same equation holds, \(DT\) is idempotent, and the image of \(D\) is the image of \(DT\). Its cokernel is therefore the projective image of \(1-DT\). This proves flatness at all stalks of the descended term, and its extension is the original cokernel presentation. The descended bounded flat complex \(K_B\) is consequently constructible and of finite Tor amplitude, and its derived extension is \(K\). The subring \(B\) is reduced because \(A\) is.

Every maximal residue field of \(B\) is finite. Moreover the intersection of its maximal ideals is zero: for any nonzero \(b\), choose a maximal ideal of the nonzero ring \(B[1/b]\). Zariski's lemma makes its residue field finite over \(\mathbf F_p\). The image of \(B\) in that finite field is a finite domain, hence a field, so the contracted ideal is maximal and does not contain \(b\). Here Zariski's lemma follows from the usual denominator argument: if a field finitely generated as an algebra had a positive transcendence basis, it would be finite integral over a localization of a polynomial ring at one element. That polynomial localization is not a field (choose an irreducible polynomial not dividing the denominator), whereas a ring over which a field is integral must be a field. The remaining algebraic generators give a finite extension.

Reduce each coefficient of the proposed equality in \(B[[t]]\) modulo every maximal ideal. Projection and perfectness identify the cohomological reduction with the coefficient-extended complex; the finitely many local factors contributing to that coefficient reduce in the same way. The finite-field case proves equality in every residue field. The zero intersection proves equality in \(B[[t]]\), and extension to \(A\) finishes the proof. \(\square\)

**Example 2.11 (nilpotents can destroy the formula).** Let
\(A=\mathbf F_2[\tau]/(\tau^2-1)=\mathbf F_2[\epsilon]/(\epsilon^2)\), with \(\epsilon=1+\tau\ne0\). The smooth projective completion of
\(Y_0:y^2+y=x^3\) is a plane cubic with its single point \(O\) at infinity. Its involution \(y\mapsto y+1\) makes \(Y_0\setminus\{O\}\to\mathbf A^1\) a finite étale double cover. Put \(M=\pi_*\mathbf F_2\), with the regular \(A\)-action. It is locally free of rank one over \(A\).

We compute its compact cohomology directly. The plane-cubic adjunction and coherent cohomology give \(H^1(Y,\mathcal O_Y)=k\) and \(\omega_Y=\mathcal O_Y\). Its generator as a differential is \(dx\). It is regular and nonzero on the affine curve, since the derivative of the equation with respect to \(y\) is \(1\). At infinity use \(t=x/y\), \(v=1/y\), where \(v+v^2=t^3\). Then \(dv=t^2dt\), and
\(dx=d(t/v)=(v+t^3)dt/v^2=dt\).
Thus \(dx\) is regular and nowhere zero there too.

Frobenius on \(H^1(Y,\mathcal O_Y)\) is zero. Represent a class by finitely many principal parts \(h_x\); rational functions form an acyclic sheaf, so these represent all such classes. Its Serre pairing with \(dx\) after Frobenius is the sum of the residues of \(h_x^2dx=d(xh_x^2)\), which are zero. The residue normalization was checked in Lemma 2.8. Perfectness of the pairing and its one-dimensional differential space give the assertion. Artin–Schreier (2.18) now gives \(H^0(Y,\mathbf F_2)=\mathbf F_2\) and zero in every positive degree: on \(H^0(\mathcal O_Y)=k\), \(z^2-z\) is onto with kernel \(\mathbf F_2\), and on \(H^1(\mathcal O_Y)\) it is \(-1\). The localization sequence at \(O\) therefore makes \(R\Gamma_c(Y\setminus\{O\},\mathbf F_2)=0\). Finite pushforward gives \(R\Gamma_c(\mathbf A^1,M)=0\) as an \(A\)-complex.

At \(x=0\), both points of the cover are rational and Frobenius on its regular stalk is \(1\). At \(x=1\), the two roots are in \(\mathbf F_4\) and Frobenius interchanges them, so its operator is \(\tau\). The additive local sum is \(1+\tau=\epsilon\ne0\), while the compact cohomological trace is zero. Equally, the coefficient of \(t\) in the Euler product is \(\epsilon\), whereas its cohomological determinant is \(1\). Reducedness in Theorem 2.10 cannot be removed.

Deligne's *Fonctions L modulo \(\ell^n\) et modulo \(p\)*, §§3–4, gives the Artin–Schreier lattice method and this counterexample. The coherent symmetric-power reduction is SGA 4, XVII, §§5.5.29–5.5.35. The proofs here include the semilinear hypothesis check, the affine coherent reduction, the curve residue trace and the reduced-ring descent. For a separate treatment of the coherent trace in every dimension, see Lenny Taelman, [*Sheaves and functions modulo p*](https://staff.science.uva.nl/l.d.j.taelman/beijing.pdf), Appendix A, Theorem A.4; its graph-duality proof gives the same denominator and alternating sign.

## 6. The tame Euler characteristic and the Legendre family

### Ramification and the Euler characteristic

Let \(C\) be a smooth projective connected curve over an algebraically closed field \(k\) of characteristic \(p\), let \(U=C-D\), and put \(s=\#D\). For a finite Galois covering \(V\to U\), write \(Y\to C\) for its normalized projective completion and \(G\) for its group. At a point \(y\) over \(x\in D\), its stabilizer \(D_y\) is its inertia group: the residue field is \(k\). If \(t\) is a uniformizer at \(y\), set

\[
i_y(\sigma)=v_y(\sigma(t)-t),\qquad
D_{y,i}=\{1\}\cup\{\sigma:i_y(\sigma)\geq i+1\}\quad(i\geq0).
\tag{6.a}
\]

These definitions do not depend on the uniformizer. Indeed a change \(t'=a_1t+a_2t^2+\cdots\), \(a_1\ne0\), changes \(\sigma(t)-t\) by a unit multiple plus terms of strictly greater valuation. The group \(D_{y,0}\) is \(D_y\); \(D_{y,1}\) is a \(p\)-group, and all \(D_{y,i}\), \(i\geq1\), are normal \(p\)-subgroups of \(D_y\). Here is the local reason. The leading coefficient \(\sigma(t)/t\bmod t\) embeds \(D_y/D_{y,1}\) into \(k^\times\); a finite subgroup of \(k^\times\) has order prime to \(p\). For \(i\geq1\), the coefficient of \(t^{i+1}\) in \(\sigma(t)-t\) embeds \(D_{y,i}/D_{y,i+1}\) into the additive group of \(k\). These groups terminate because a nonidentity automorphism has finite \(i_y\). Thus their successive orders are powers of \(p\).

For a representation \(M\) of \(D_y\) over a field of characteristic different from \(p\), its Swan conductor is

\[
\operatorname{Sw}_x(M)
=\sum_{i\geq1}\frac{|D_{y,i}|}{|D_y|}
\bigl(\dim M-\dim M^{D_{y,i}}\bigr).
\tag{6.b}
\]

Conjugating \(y\) conjugates the filtration and leaves this number unchanged. The usual finite-quotient convention is understood in (6.b): use a covering through which the local representation factors. Refining that covering does not change the number. One can verify this directly with ramification valuations: for a normal subgroup \(N\) and a nonidentity coset \(\bar\sigma\), the uniformizer-norm calculation gives
\(i_{D_y/N}(\bar\sigma)=|N|^{-1}\sum_{\tau\mapsto\bar\sigma}i_{D_y}(\tau)\).
For detail, let \(P(T)=\prod_{n\in N}(T-n(t))\), whose constant coefficient is, up to sign, a uniformizer \(w\) of the fixed field. Put \(h=v_{\mathrm{fix}}(\bar\sigma(w)-w)\). Expanding any integral element of that field in powers of \(w\) shows that the valuation upstairs of its \(\sigma\)-difference is at least \(|N|h\). Since \((\sigma P)(\sigma t)=0\), evaluate \(P-\sigma P\) at \(\sigma t\). Its constant term has valuation exactly \(|N|h\); every positive-degree term has larger valuation, because its coefficient has valuation at least \(|N|h\) and \(v(\sigma t)=1\). On the other hand \(P(\sigma t)=\prod_{n\in N}(\sigma t-n(t))\), so its valuation is the sum of the \(i\)-values over the coset. This proves the displayed identity. Consequently the Swan character of a quotient is the average of the Swan character over each coset, including the identity coset by the zero total sum of a Swan character. Pairing that identity with an inflated representation proves the claimed invariance. In particular, (6.b) is the normalized lower-filtration formula, not an unweighted sum of codimensions. It is zero for tame monodromy.

The Swan character just used has value \(-(i(\sigma)-1)\) at \(\sigma\ne1\), and value \(\sum_{\sigma\ne1}(i(\sigma)-1)\) at \(1\); hence its total sum is zero. Quotient compatibility also applies to representations of characteristic \(\ell\), even when \(\ell\) divides the group order. Indeed the local version of the projective class (6.e), with \(G=D_y\), has this character. Push that class along \(O[D_y]\to O[D_y/N]\). A summand of a free right module stays a summand of a free right module, so this pushforward is projective; its characteristic-zero character is the coset average, by the averaging projector onto \(N\)-coinvariants. The norm identity identifies it with the quotient's Swan character. Lemma 6.1 then identifies the two projective classes after reduction, and tensoring with any quotient representation gives equal conductors. Thus no lift of that modular representation or division by \(|D_y|\) in its coefficient field is required.

We need a small representation-theoretic fact because a finite monodromy group can have order divisible by \(\ell\). Its proof also explains why averaging over the whole group would be invalid here.

**Lemma 6.1 (detecting projective group modules).** Let \(a\) be a splitting field of characteristic \(\ell\) for a finite group \(G\), and let \(O\) be a complete discrete valuation ring with residue field \(a\), whose fraction field \(B\) has characteristic zero and splits \(G\). Finite projective \(a[G]\)-modules lift to \(O[G]\). Their lifted characters determine their classes in \(K_0(a[G])\otimes\mathbf Q\). A lifted projective character is zero on every element whose order is divisible by \(\ell\).

**Proof.** A finite projective is the image of an idempotent matrix. Idempotents lift successively across the powers of the maximal ideal: correct \(e^2-e\) by multiplying it by the inverse of \(2e-1\), whose square is congruent to \(1\); each correction squares the error. Completeness then gives an idempotent lift. Maps between the lifted projectives reduce surjectively, by their finite free splittings. This also lifts isomorphisms, since a map invertible after reduction is invertible over the complete ring. Consequently the isomorphism class of a projective lift is unambiguous.

Let \(S_i\) be the simple \(a[G]\)-modules and \(Q_i\) their indecomposable projective covers. These are all the generators of the projective Grothendieck group, by the decomposition of the semisimple quotient and lifting its primitive idempotents. For an element of order prime to \(\ell\), define \(\theta_i\) by lifting its eigenvalues, roots of unity, to \(O\) and taking their sum. These functions, the Brauer characters, are linearly independent over \(B\). To prove this, reduce an alleged relation whose coefficients are integral and at least one is a unit. Its reduction is a relation between the ordinary traces of the \(S_i\) on the prime-to-\(\ell\) elements. For any \(g\in G\), write \(g=g_{\ell'}g_\ell\) with commuting prime-to-\(\ell\) and \(\ell\)-power parts. On each eigenspace of \(g_{\ell'}\), the second factor is unipotent, so its trace gives the same trace as \(g_{\ell'}\). The relation therefore holds on all group elements and hence on their group algebra. But the trace forms of its simple modules are independent: on \(a[G]/\operatorname{rad}(a[G])=\prod_i\operatorname{End}_a(S_i)\), test a single matrix unit of diagonal trace \(1\) in one factor. This contradicts the unit coefficient. Normalizing valuations proves independence for every \(B\)-relation.

Let \(W_j\) run through the irreducible \(B[G]\)-modules, with invariant \(O\)-lattices \(L_j\). Such lattices are obtained by summing the translates of any lattice. Write \(d_{ji}\) for the composition multiplicity of \(S_i\) in \(L_j\bmod\mathfrak m\). Restricting the ordinary character of \(W_j\) to prime-to-\(\ell\) elements gives \(\sum_i d_{ji}\theta_i\), because their eigenspace projectors have denominator invertible in \(O\). The restrictions of all ordinary irreducible characters span all functions on the prime-to-\(\ell\) conjugacy classes: extend such a function by zero to the other conjugacy classes and use ordinary character orthogonality. That orthogonality follows by averaging a linear map over \(G\) in characteristic zero and applying Schur's lemma. Thus the matrix \((d_{ji})\) has full column rank.

For a lift \(\widetilde Q_i\), finite projectivity gives
\[
\dim_B\operatorname{Hom}_{B[G]}(\widetilde Q_i\otimes B,W_j)
=\dim_a\operatorname{Hom}_{a[G]}(Q_i,L_j\bmod\mathfrak m)
=d_{ji}.
\]
The first equality is base change for a summand of a finite free module; the second follows from exactness of \(\operatorname{Hom}(Q_i,-)\) and \(\operatorname{Hom}(Q_i,S_h)=a\) if \(h=i\), zero otherwise. Hence the lifted characters of the \(Q_i\) have the linearly independent columns \((d_{ji})\) as their ordinary-character coordinates. This proves injectivity of the character map, without assuming that simple modular representations themselves lift.

Finally restrict a projective lift to the cyclic subgroup generated by \(g\). Separate the eigenspaces for its prime-to-\(\ell\) part, using the integral projectors just described. Each is projective over the group ring of its cyclic \(\ell\)-power part. That ring is local: its reduction is \(a[T]/(T-1)^{\ell^e}\). A finite projective over it is free, by lifting a basis of its quotient and Nakayama's lemma. A nonidentity element of this \(\ell\)-group permutes the regular basis without fixed vectors and has trace zero. Multiplying by each prime-to-\(\ell\) eigenvalue proves the last assertion. \(\square\)

**Theorem 6.2 (Grothendieck–Ogg–Shafarevich).** Let \(\mathcal V\) be a rank-\(r\) lisse \(E\)-sheaf on \(U\), where \(E/\mathbf Q_\ell\) is finite and \(\ell\ne p\). Then

\[
\chi_c(U,\mathcal V)
=r(2-2g(C)-s)-\sum_{x\in D}\operatorname{Sw}_x(\mathcal V).
\tag{6.c}
\]

In particular, if all wild inertia acts trivially,

\[
\chi_c(U,\mathcal V)=r\chi_c(U,E)=r(2-2g(C)-s).
\tag{6.1}
\]

**Proof.** We first prove the formula for a finite-monodromy local system over a finite field \(a\) of characteristic \(\ell\ne p\). Enlarge \(a\) and its characteristic-zero coefficient ring to splitting fields; Euler characteristics and the dimensions of the wild invariant spaces do not change. Choose a connected finite étale \(G\)-torsor \(V\to U\) trivializing the sheaf, and let \(M\) be its stalk representation. The regular local system is a free rank-one right \(a[G]\)-local system. Its compact cohomology
\(P_a=R\Gamma_c(V,a)\) is consequently perfect as a right \(a[G]\)-complex by Lesson 4, Theorem 4.3. The coefficient projection formula there gives

\[
R\Gamma_c(U,\mathcal V)=P_a\otimes^L_{a[G]}M.
\tag{6.d}
\]

Use the same regular systems over \(O/\mathfrak m^n[G]\). Their compact cohomology has a common Tor interval \([0,2]\) and compatible reductions. The inverse-limit proof of the adic-sheaves lesson, Theorem 6.1, works here with finite projectives in place of finite free modules. More explicitly, decompose into indecomposable projectives and cancel each differential component invertible on their simple tops. The remaining differentials lie in the radical, so the multiplicities in a minimal complex are determined by reduction modulo that radical. They are fixed at the first level. Idempotent lifting and the lifting of maps between projectives, as in Lemma 6.1, identify successive models and homotopies; inverse limits of their matrices give a bounded projective \(O[G]\)-complex \(P\) with reduction \(P_a\). The radical topology is the \(\mathfrak m\)-adic topology since the radical modulo \(\mathfrak m\) is nilpotent. Thus all the completeness and boundedness arguments used in that lesson apply. Its underlying \(O\)-complex computes \(R\Gamma_c(V,O)\), including the deck transformations.

For each \(x\in D\), choose \(y\) above it and define a rational projective class

\[
S_x=\sum_{i\geq1}\frac{|D_{y,i}|}{|D_y|}
\bigl([O[G]]-[e_{y,i}O[G]]\bigr),\qquad
e_{y,i}=\frac1{|D_{y,i}|}\sum_{h\in D_{y,i}}h.
\tag{6.e}
\]

The idempotent exists over \(O\) because \(D_{y,i}\) is a \(p\)-group and \(\ell\ne p\). It follows that every term is projective. At a nonidentity \(\sigma\), the character of \(S_x\) is
\(-\sum_{y'\mapsto x,\ \sigma y'=y'}(i_{y'}(\sigma)-1)\): the regular character contributes zero, and the character of the right ideal \(e_{y,i}O[G]\) counts cosets fixed by \(\sigma\). Normality of \(D_{y,i}\) in \(D_y\), followed by the coefficient in (6.e), makes each level contribute \(-1\) at a fixed \(y'\) exactly when \(\sigma\in D_{y',i}\). At the identity its character is
\(\sum_{y'\mapsto x}\sum_{i\geq1}(|D_{y',i}|-1)\).

The completed curve \(Y\) is smooth, since a normal curve over the perfect \(k\) is smooth. A nonidentity deck transformation has no fixed points on \(V\). The curve fixed-point theorem, Theorem 4.1, therefore gives its alternating trace on \(Y\) as \(\sum_{\sigma y=y}i_y(\sigma)\). Localization subtracts the trace of its boundary permutation module, namely the number of fixed boundary points. Thus its trace on \(P\otimes B\) is \(\sum_{\sigma y=y}(i_y(\sigma)-1)\).

At the identity, the different formula and the canonical-divisor degree give the same character equality. For detail, the map \(f^*\omega_C\to\omega_Y\) has zero divisor the different. In a totally ramified completed local extension, its exponent is
\(\sum_{\sigma\ne1}i_y(\sigma)=\sum_{i\geq0}(|D_{y,i}|-1)\): the derivative of the Eisenstein polynomial of a uniformizer is \(\prod_{\sigma\ne1}(t-\sigma t)\), and generates the different. Taking degrees yields Riemann–Hurwitz, since \(\deg\omega=2g-2\), as proved by curve Riemann–Roch in Lesson 5, §2.3. Subtracting the number of points of \(Y-V\), and using \(\sum_{y\mapsto x}|D_y|=|G|\), yields
\[
\chi_c(V,a)=|G|\chi_c(U,a)
-\sum_{y\in Y-V}\sum_{i\geq1}(|D_{y,i}|-1).
\]
Together with the nonidentity computation, this says that the characters of the two projective classes in
\[
[P_a]=\chi_c(U,a)[a[G]]-\sum_{x\in D}(S_x\bmod\mathfrak m)
\quad\text{in }K_0(a[G])\otimes\mathbf Q
\tag{6.f}
\]
agree. On elements of order divisible by \(\ell\), both are zero by Lemma 6.1 and because none of the \(p\)-groups \(D_{y,i}\) contains such an element. Lemma 6.1 therefore proves (6.f).

Apply to (6.f) the additive functional sending a projective right module \(Q\) to \(\dim_a(Q\otimes_{a[G]}M)\). It is defined on all such projectives; \(M\) need not be projective as a group module. The regular module gives \(r\), and \(e_{y,i}a[G]\) gives \(\dim M^{D_{y,i}}\), by the averaging idempotent for that \(p\)-group. Equation (6.d) now gives exactly (6.c) for this local system.

Finally choose an invariant free \(O_E\)-lattice in the original \(E\)-sheaf. Such a lattice exists by compactness of the monodromy image: its bounded translates generate an invariant lattice. The adic perfect-complex recovery in the adic-sheaves lesson shows that the Euler characteristic over \(E\) equals that of its reduction modulo the maximal ideal. The latter has finite monodromy and was just treated. Wild inertia has finite image on the lattice: the kernel of reduction is a pro-\(\ell\) group, whereas wild inertia is pro-\(p\); successive congruence quotients are additive \(\ell\)-groups, so their intersection with a pro-\(p\) image is trivial. For each of its ramification subgroups the averaging projector has integral coefficients and the rank of its image is unchanged by reduction. Formula (6.b) therefore gives the same Swan conductor before and after reduction. This proves (6.c) and its tame specialization. \(\square\)

There is no tame codimension term in (6.c), because we use extension by zero and compact support. For \(j:U\hookrightarrow C\), the stalk of \(j_*\mathcal V\) at \(x\) is \(\mathcal V^{I_x}\). The support exact sequence therefore gives the distinct formula
\[
\chi(C,j_*\mathcal V)
=r\chi(C,E)-\sum_{x\in D}
\bigl(r-\dim\mathcal V^{I_x}+\operatorname{Sw}_x(\mathcal V)\bigr).
\tag{6.g}
\]
This is the Artin-conductor version. It follows from the proved compact-support formula by adding the boundary invariant spaces; it should not be substituted for (6.c).

Raynaud's Bourbaki exposé 286, §I.1 and §I.3, Theorem 1, and SGA 5, Exposé X, §7, Theorem 7.1, are the historical sources for these conductor and Euler characteristic statements. The projective-character argument above supplies the modular passage, including groups of order divisible by \(\ell\), within this lesson.

The Swan term can be computed explicitly for the character sheaves used later. For an Artin–Schreier cover \(z^p-z=s^{-m}\), \(m>0\), \(p\nmid m\), its degree is \(p\) and its point over \(s=0\) is totally ramified: an unramified place would make \(p\mid m\) by valuation of the equation. Upstairs \(v(s)=p\) and \(v(z)=-m\). Choose \(A,B\) with \(Ap-Bm=1\); then \(t=s^Az^B\) is a uniformizer and \(p\nmid B\). A nonzero translation \(z\mapsto z+a\) satisfies \(\sigma(t)/t=(1+a/z)^B\), giving \(i(\sigma)=m+1\). Thus every higher ramification group through level \(m\) is \(\mathbf F_p\), and the subsequent groups are trivial. A nontrivial rank-one character has Swan conductor \(m\) by (6.b). The additive character of \(x\) has conductor \(1\) at infinity and zero at \(0\); a Kummer twist is tame and changes neither higher group. The character of \(x+a/x\), \(a\ne0\), has conductor \(1\) at each of \(0,\infty\). Formula (6.c) therefore predicts Euler characteristics \(-1\) and \(-2\) on \(\mathbf G_m\). Section 7 retains direct covering calculations of the cohomology, tracing both this local correction and its Frobenius action.

### The Legendre family

Assume now that \(q\) is odd. Let \(U_0=\mathbf P^1_{k_0}-\{0,1,\infty\}\), and let \(f:\mathscr E_0\to U_0\) be the smooth projective elliptic family with affine equation

\[
y^2=x(x-1)(x-\lambda).
\tag{6.2}
\]

Proper and smooth base change make \(\mathcal V_0=R^1f_*E\) lisse of rank \(2\). Its finite integral levels are locally free of rank \(2\). At a closed point \(\lambda\) of degree \(d\), put
\(a_\lambda=q^d+1-\#\mathscr E_\lambda(\mathbf F_{q^d})\). Its local factor is

\[
\det(1-F_\lambda t^d\mid\mathcal V_{\bar\lambda})
=1-a_\lambda t^d+q^dt^{2d}.
\tag{6.3}
\]

Let \(\chi_Q\) be the quadratic character of \(\mathbf F_Q^\times\), extended by \(\chi_Q(0)=0\), where \(Q=q^r\). Counting the two possible \(y\)-coordinates and the point at infinity gives
\(a_\lambda=-\sum_x\chi_Q(x(x-1)(x-\lambda))\).
Summing over \(\lambda\ne0,1\), use
\(\sum_{\lambda\in\mathbf F_Q}\chi_Q(x-\lambda)=0\). The two excluded terms give

\[
\begin{aligned}
\sum_{\lambda\ne0,1}a_\lambda
&=\sum_x\chi_Q(x(x-1))\bigl(\chi_Q(x)+\chi_Q(x-1)\bigr)\\
&=-\chi_Q(-1)-1.
\end{aligned}
\tag{6.4}
\]

Indeed, for \(x\ne0,1\) the two summands reduce to \(\chi_Q(x-1)\) and \(\chi_Q(x)\). Their sums are \(-\chi_Q(-1)\) and \(-1\). Put \(\epsilon=\chi_q(-1)\); then \(\chi_Q(-1)=\epsilon^r\). Equations (1.6) and (6.4), with constant term \(1\), yield

\[
L(U_0,\mathcal V_0,t)=(1-t)(1-\epsilon t).
\tag{6.5}
\]

### Tate uniformization and local inertia

We prove the uniformization used in the degree interpretation. The parameter below is called \(Q\), to distinguish it from the finite-field cardinality \(q\).

**Theorem 6.3 (Tate uniformization).** Let \(K\) be complete for a nontrivial nonarchimedean absolute value, and let \(Q\in K\) satisfy \(0<|Q|<1\). There is an elliptic curve \(E_Q/K\) and a Galois-compatible isomorphism
\[
L^\times/Q^{\mathbf Z}\xrightarrow{\sim}E_Q(L)
\tag{6.h}
\]
for every finite extension \(L/K\). If \(K\) is discretely valued and an elliptic curve \(E/K\) has split multiplicative reduction, there is a unique such \(Q\in K\) with \(E\simeq E_Q\).

**Proof.** Define the convergent integral series
\[
s_m(Q)=\sum_{n\geq1}\frac{n^mQ^n}{1-Q^n},\qquad
a_4=-5s_3,\qquad a_6=-\frac{5s_3+7s_5}{12},
\tag{6.i}
\]
and put \(E_Q:y^2+xy=x^3+a_4x+a_6\). The expression for \(a_6\) is integral even in residue characteristics \(2,3\): \(12\) divides \(5n^3+7n^5\) for every integer \(n\). Modulo \(3\), use \(n^5\equiv n^3\); modulo \(4\), use \(n^2\equiv1\) for odd \(n\) and \(4\mid n^3\) for even \(n\). Thus (6.i) is interpreted through its integer coefficients, without dividing by a nonunit in \(K\). The same convention applies to integral series with a displayed rational expression below.

The Weierstrass invariants computed from this equation satisfy
\[
c_4=1+240s_3=1+O(Q),\quad
\Delta=Q+O(Q^2),\quad
j(Q)=Q^{-1}+744+O(Q).
\tag{6.j}
\]
For example use \(b_2=1\), \(b_4=2a_4\), \(b_6=4a_6\), \(b_8=a_6-a_4^2\) in
\(\Delta=-b_2^2b_8-8b_4^3-27b_6^2+9b_2b_4b_6\).
The coefficients of these series are integers. Hence \(\Delta\ne0\), and the equation is nonsingular over \(K\). Its reduced equation is \(y^2+xy=x^3\); the tangent cone at the node is \(y(y+x)\), with two distinct rational directions in every characteristic. Its reduction is split multiplicative.

For \(u\notin Q^{\mathbf Z}\), set
\[
X(u)=\sum_{n\in\mathbf Z}\frac{Q^nu}{(1-Q^nu)^2}-2s_1,
\qquad
Y(u)=\sum_{n\in\mathbf Z}\frac{(Q^nu)^2}{(1-Q^nu)^3}+s_1.
\tag{6.k}
\]
The terms tend to zero in both directions: for \(n\to+\infty\) they are bounded by positive powers of \(|Q|^n\), and for \(n\to-\infty\) rewrite each term in powers of \((Q^nu)^{-1}\). The convergence is uniform on closed annuli avoiding the poles. Index shifting proves \(Q\)-periodicity. Directly pairing the positive and negative indices gives
\[
X(u^{-1})=X(u),\qquad
Y(u^{-1})=-Y(u)-X(u),\qquad
u\frac{dX}{du}=2Y+X.
\tag{6.l}
\]
All three identities are identities of integral Laurent series, so the last one remains valid in characteristics \(2,3\).

Here are the elementary analytic facts needed for this construction. A meromorphic \(Q\)-periodic function has finitely many zeros and poles, counted with multiplicity, on the annulus \(|Q|\leq|u|\leq1\), with the two boundary circles identified. Its total zero order equals its total pole order. For the first assertion, convergent Laurent coefficients tend to zero at both boundary radii; only finitely many coefficients can occur on the lower Newton polygon between these radii. Factoring the associated finite distinguished polynomial gives the zeros and their multiplicities, and leaves a unit. This factorization can be seen directly by successive division by \(u-\alpha\); the remaining terms converge because the nonleading coefficients are strictly smaller at the given radius. Apply the same argument to a quotient of analytic functions for poles. The change of Newton-polygon slope across the annulus is the number of zeros minus poles. Periodicity identifies the slopes at its two boundaries, proving equality of the totals. Zeros on a boundary are counted once after identification. Over an algebraically closed complete extension these factorizations split; for functions defined over a finite extension the distinguished polynomials show that their zeros belong to an algebraic extension.

One also has the product condition
\[
\prod(\text{zero representatives})\big/
\prod(\text{pole representatives})\in Q^{\mathbf Z}.
\tag{6.m}
\]
For a direct proof, the product
\[
\Theta(u)=(1-u)\prod_{n\geq1}(1-Q^nu)(1-Q^n/u)
\]
converges locally uniformly on the punctured line, has simple zeros exactly at \(Q^{\mathbf Z}\), and satisfies \(\Theta(Qu)=-u^{-1}\Theta(u)\). Divide the function by the products of \(\Theta(u/u_j)\) for its zeros and multiply by those for its poles. The quotient has no poles or zeros. Its transformation law has the form \(h(Qu)=c\,h(u)\), with \(c\) equal to the reciprocal of the ratio in (6.m), because the zero and pole counts agree. Expand \(h\) as a Laurent series on the punctured line; the coefficient equation is \((Q^n-c)h_n=0\). Thus \(h\) is one Laurent monomial and \(c\in Q^{\mathbf Z}\), proving (6.m). In particular, a holomorphic periodic function is constant. This establishes the divisor facts used below through convergent Laurent series and their Newton polygons.

We verify the cubic identity, rather than importing a complex uniformization. At \(u=1+z\), pair the terms with indices \(n\) and \(-n\) in (6.k), and expand \((1-Q^nu)^{-1}\). The divisor-sum identities \(\sum_{n,m\geq1}m^rQ^{nm}=s_r\) give
\[
X=z^{-2}+z^{-1}+s_3z^2-s_3z^3+
\frac{11s_3+s_5}{12}z^4+O(z^5).
\tag{6.n}
\]
The coefficient \((11s_3+s_5)/12\) is integral by the same congruences as above. Use \(2Y=uX'-X\) over the universal characteristic-zero series ring to calculate the principal part and constant term of \(Y^2+XY-X^3\). They are respectively \(-5s_3(z^{-2}+z^{-1})\) and
\(6s_3-7(11s_3+s_5)/12=-(5s_3+7s_5)/12\).
All higher polar coefficients cancel. Therefore
\(Y^2+XY-X^3-a_4X-a_6\) is holomorphic and periodic, and its constant Laurent coefficient at \(1\) is zero. It is the zero function. This calculation is an equality of integral series, so reduction gives it over every \(K\), including characteristics \(2,3\). At each \(Q^n\) the map extends to the point at infinity \(O\), since \(X,Y\) have respective pole orders \(2,3\) and \(-X/Y\) is a local parameter of order one. Hence (6.k) defines a map \(\phi\) from the periodic quotient to \(E_Q\).

On a fundamental annulus, \(X\) has a single double pole and no other poles. Thus \(X-x\) has exactly two zeros counting multiplicities. They are interchanged by \(u\mapsto u^{-1}\), by (6.l). The corresponding \(Y\)-values are the two roots of the Weierstrass equation at \(x\). If they coincide, \(2Y+X=0\); the derivative identity in (6.l) then makes the \(X\)-zero double. Consequently every point of \(E_Q\) is obtained exactly once modulo \(Q^{\mathbf Z}\), also at a double root. At infinity the preimage is precisely \(Q^{\mathbf Z}\). These observations prove bijectivity over an algebraically closed complete extension.

For the group law, pull back a line through two finite points. Except in the vertical case it is a periodic function \(aX+bY+c\) with a triple pole at \(1\); its three zeros, counted with multiplicity, have product in \(Q^{\mathbf Z}\) by (6.m). The third intersection of the line with the cubic therefore has parameter \((uv)^{-1}\). Equation (6.l) identifies inversion with elliptic-curve negation, so the chord law gives \(\phi(u)+\phi(v)=\phi(uv)\). Tangencies are included by zero multiplicity; vertical lines and the origin follow from inversion and the extension at \(1\). Thus \(\phi\) is a group isomorphism with kernel \(Q^{\mathbf Z}\).

It is defined by convergent series with coefficients in \(K\), so it commutes with every automorphism over \(K\). The inverse images just constructed are algebraic by the distinguished-polynomial argument. They are separable: the pullback of the nonvanishing invariant differential \(dX/(2Y+X)\) is \(du/u\), by (6.l), and the same equality in a different local coordinate covers the zeros of \(2Y+X\). Thus \(\phi\) is a local isomorphism, including at \(1\), where the parameter was computed explicitly. For an \(L\)-rational point, its preimage class is Galois invariant. If \(\sigma(u)/u=Q^m\), invariance of absolute values gives \(|Q|^m=1\), hence \(m=0\). Its algebraic separable representative \(u\) is therefore fixed and belongs to \(L\). This proves (6.h) over every finite extension, not just over an algebraic closure.

It remains to identify a curve of split multiplicative reduction. An integral minimal equation with nodal special fibre has \(c_4\) a unit and \(v(\Delta)>0\), so \(|j(E)|>1\). Conversely these invariant conditions characterize a node. The formal series \(1/j(Q)=Q+O(Q^2)\) has an inverse in \(z\mathbf Z[[z]]\): determine its coefficients successively using its leading coefficient \(1\). This integral inverse converges for \(|z|<1\). With \(z=1/j(E)\), it gives a unique \(Q\in K\), \(0<|Q|<1\), satisfying \(j(Q)=j(E)\).

Two elliptic curves with this \(j\) are isomorphic over a separable extension. Their origin-preserving automorphisms are \(\{1,[-1]\}\), since \(j\) is neither \(0\) nor \(1728\); this follows by substituting the general change \(x\mapsto u^2x+r\), \(y\mapsto u^3y+s u^2x+t\) into a Weierstrass equation. The assertion includes characteristics \(2,3\), where the exceptional \(j\)-value is \(0\). Thus the descent obstruction of an isomorphism \(\alpha:E\to E_Q\) is a quadratic character. It is exactly the character interchanging the two branches of the node, as we now verify.

Compare the two minimal nodal equations after the finite extension defining \(\alpha\). Their \(c_4\)'s are units, and \(c_4\) changes by the fourth power of the scale, so \(u\) is a unit. We check that \(r,s,t\) are integral. If not, set \(N=\max\{-v(r)/2,-v(s),-v(t)/3\}>0\). After a further finite extension, compare the leading residues \(R,S,T\) in weights \(2N,N,3N\), assigning zero to any parameter of smaller pole order. At least one is nonzero. Comparing the five integral coefficient equations in weights \(N,2N,3N,4N,6N\) gives
\[
2S=0,\qquad 3R-S^2=0,\qquad 2T=0,\qquad
3R^2-2ST=0,\qquad R^3-T^2=0.
\]
Terms involving an original integral coefficient have smaller pole order and do not affect these equations. Outside residue characteristic \(2\), the first and third equations give \(S=T=0\), and the last gives \(R=0\). In characteristic \(2\), the fourth gives \(R=0\), the second gives \(S=0\), and the last gives \(T=0\). Both contradict the choice of \(N\). Thus the coordinate change and its inverse are integral, and reduce to an isomorphism of nodal cubics. On the normalization of a nodal cubic, the two preimages of the node are the two tangent directions. The involution \([-1]\) interchanges them, since on its nonsingular part \(\mathbf G_m\) it is inversion. If both nodes are split, Galois fixes each direction on each curve. The reduction of \(\sigma(\alpha)\alpha^{-1}\) cannot then interchange them. The quadratic character is trivial, and \(\alpha\) is defined over \(K\). This proves the converse and uniqueness. \(\square\)

For the geometric local fields \(k((s))\) in our example, this gives a direct description of the Tate module. A class \([u]\) is killed by \(\ell^n\) exactly when \(u^{\ell^n}=Q^b\); send it to \(b\bmod\ell^n\). Changing \(u\) by a power of \(Q\) changes \(b\) by a multiple of \(\ell^n\). The kernel is \(\mu_{\ell^n}\), and choosing compatible \(\ell^n\)-th roots of \(Q\) gives compatible lifts of \(1\). Taking inverse limits and tensoring with \(E\) yields

\[
0\longrightarrow E(1)\longrightarrow V_\ell(E_Q)
\longrightarrow E\longrightarrow0.
\tag{6.6}
\]

In this basis the off-diagonal Galois cocycle is
\(\sigma(Q^{1/\ell^n})/Q^{1/\ell^n}\in\mu_{\ell^n}\). Write \(Q=s^m u\), \(m>0\), with \(u\in k[[s]]^\times\). Each \(\ell^n\)-th root of \(u\) is in \(k[[s]]^\times\), by Hensel's lemma, whose derivative is a unit. The roots of \(s\) and all roots of unity are in tame extensions, since \(\ell\ne p\). Thus wild inertia is trivial, while tame inertia acts by
\(\begin{pmatrix}1&m t_\ell(\sigma)\\0&1\end{pmatrix}\).
The dual \(H^1\) representation is tame and unipotent. This proves the local input for the Legendre family, including its extension class; unipotent inertia need not have finite image.

Papikian, *Rigid analytic geometry and abelian varieties*, §2, Theorems 2.1–2.2 and pp.3–4, gives the analytic formulas, the arbitrary-complete-field formulation and the split multiplicative criterion. The proof here uses integral Laurent identities and nonarchimedean divisor calculations for the construction and descent.

At \(\lambda=0,1\), (6.2) has nodal multiplicative reduction: its discriminant is \(16\lambda^2(1-\lambda)^2\), and \(c_4=16(\lambda^2-\lambda+1)\) is a unit at each point. Over the geometric local field the node is split, so (6.6) applies. At infinity put \(s=1/\lambda\), \(x=u/s\), \(y=v/s^2\). The equation becomes

\[
v^2=s\,u(u-s)(u-1).
\tag{6.7}
\]

It is the quadratic twist by \(s\) of the family with parameter \(s\), which has multiplicative reduction at \(s=0\). The extension adjoining \(\sqrt{s}\) is tame because \(p\ne2\). An inertia element acting by \(-1\) on \(\sqrt{s}\) acts on this twisted \(H^1\) with both eigenvalues \(-1\), instead of the unipotent eigenvalues \(1\). Hence there are no inertia invariants there, even on the dual.

A global geometric section of \(\mathcal V^\vee\) would be invariant under this local inertia, so \(H^0(U,\mathcal V^\vee)=0\). Duality gives \(H_c^2(U,\mathcal V)=0\). Also \(H_c^0(U,\mathcal V)=0\): a nonzero section of a lisse sheaf on a connected curve cannot have proper support inside a nonproper curve. The sheaf is tame at all three boundary points. Equation (6.1) gives \(\chi_c=-2\), and therefore

\[
\dim H_c^1(U,\mathcal V)=2,\qquad
\det(1-tF\mid H_c^1(U,\mathcal V))=(1-t)(1-\epsilon t).
\tag{6.8}
\]

This explains the degree without assuming a Leray degeneration or a vanishing of top compact-support cohomology. If \(q\equiv3\pmod4\), the ground-field eigenvalues are \(1,-1\), although both square to \(1\) after a quadratic extension.

## Selected exercises with complete solutions

**Exercise 8.9 (medium).** For the Legendre local system, calculate \(\chi_c(U,\mathcal V)\) and \(\chi(\mathbf P^1,j_*\mathcal V)\). Show that its two compact degree-one classes come from the boundary, and identify their Frobenius eigenvalues.

**Solution.** The rank is \(2\), the genus is zero and there are three boundary points. All Swan terms vanish, so (6.c) gives \(\chi_c=-2\). The nodal Tate representations at \(0,1\) have one-dimensional invariant spaces, since their parameter valuations are \(2\) and their rational tame cocycles are nonzero. The twisted representation at infinity has none. Thus (6.g) gives \(\chi(\mathbf P^1,j_*\mathcal V)=2\cdot2-(1+1+2)=0\). Its degree-zero cohomology vanishes because inertia at infinity has no invariants; its degree-two cohomology is \(H_c^2=0\) by duality. Hence its degree-one cohomology also vanishes. The exact sequence \(0\to j_!\mathcal V\to j_*\mathcal V\to\mathcal B\to0\), where \(\mathcal B\) consists of the two boundary invariant lines, gives \(H^0(\mathcal B)\simeq H_c^1(U,\mathcal V)\). At \(0\) the reduced tangent equation is \(y^2=-x^2\), so its two branches are exchanged by Frobenius exactly when \(-1\) is a nonsquare; the boundary eigenvalue is \(\epsilon=\chi_q(-1)\). At \(1\) the tangent equation is \(y^2=(x-1)^2\), with rational branches and eigenvalue \(1\). In a split Tate curve the invariant line in the dual Tate module has eigenvalue \(1\); exchanging the branches twists it by the quadratic character. These give precisely the two factors in (6.8).

**Exercise 8.10 (medium).** For a split Tate curve over \(k((s))\), with \(Q=s^m u\), compare rational inertia with reduction modulo \(\ell\). Explain why reduction can change the tame invariant dimension without changing the Swan conductor.

**Solution.** The rational tame cocycle is \(m t_\ell\), so \(m>0\) makes the rational inertia image infinite and its invariant space one-dimensional. Its residual cocycle is zero if \(\ell\mid m\); in that case the residual inertia representation is trivial and its invariant space has dimension two. If \(\ell\nmid m\), its residual invariant space is one-dimensional. In every case wild inertia is trivial and the Swan conductor is zero. The averaging projectors used in Theorem 6.2 apply to higher ramification \(p\)-groups; they do not assert that invariants under tame \(\ell\)-power inertia commute with reduction. For the Legendre nodes \(m=2\), reduction modulo \(2\) illustrates this distinction.

## Sources and scope

The exact finite-coefficient determinant argument compares symmetric powers rather than inferring equality from power traces. The conductor proof includes the modular projective-character argument. The Tate proof includes its analytic construction, group law, descent and multiplicative criterion.

- [Deligne, La conjecture de Weil I](https://publications.ias.edu/sites/default/files/Number23.pdf), §§1–2, for the determinant and Frobenius conventions.
- [Milne, Lectures on Étale Cohomology](https://www.jmilne.org/math/CourseNotes/LEC.pdf), §§27 and29, for the canonical Euler-product formulation.
- [Raynaud, Caractéristique d'Euler-Poincaré d'un faisceau et cohomologie des variétés abéliennes](https://www.numdam.org/item/SB_1964-1966__9__129_0/), Bourbaki exposé286, §I.1 and §I.3, for the historical conductor and Euler formula.
- [Papikian, Rigid analytic geometry and abelian varieties](https://math.stanford.edu/~vakil/snowbird/mihranjun21.pdf), §2, Theorems2.1–2.2, for the Tate-curve comparison; the full construction used here is written above.

The explanatory prose is CC0 where stated. References retain their own terms; free access is not a reuse licence. This reading makes no claim that the general WeilII weight theorem or the remaining higher-dimensional pencil geometry has been proved.
