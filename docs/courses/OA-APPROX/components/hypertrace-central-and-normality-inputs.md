# Central and normality inputs for hypertraces

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. New original exposition: public domain (CC0), to the extent of rights held. The notices on the retained programme proofs and linked human works remain in force.*

These constructions supply the center, spectral and topology inputs of Hypertraces and finite injective algebras, throughout its arbitrary finite and semifinite scope. Hilbert spaces and central partitions can have arbitrary cardinality. Inner products in the formulas below are linear in the second variable.

The complete projection and trace arguments are [PC0–7 and FCT0–7](central-finite-trace-inputs.md). They prove polar decomposition, arbitrary orthogonal sums, central comparison, finite cancellation, the finite-join theorem, central tiles, and existence, faithfulness and full ultraweak continuity of the normalized center-valued trace. Their scalar and coefficient inputs are the retained CF1–10 and CP1–6; their full spectral input is SF/SB0–6. The faithful representation and inverse topology argument is ST1–2.

We will also use the complete [commutative character construction](finite-cp-models-tensor-and-unitization-inputs.md#fcp3), including existence and norm separation, and the [scalar GNS and concrete matrix constructions](scalar-gns-and-matrix-cstar-norms.md). All the statements invoked below have their complete proofs at these locators.

<a id="hyp0"></a>
## HYP0. Finite restrictions of an order-normal trace

Let \(N\subseteq B(H)\) be concrete, and let \(\tau:N_+\to[0,\infty]\) be an additive, positively homogeneous, faithful tracial weight preserving bounded increasing positive suprema. If \(e\in N\) is a projection with \(0<\tau(e)<\infty\), then
\[
 f(x)=\tau(x)\quad(x\in(eNe)_+)
\]
extends to a bounded positive linear functional on \(eNe\), and \(f/\tau(e)\) is a faithful ultraweakly continuous tracial state on the whole corner.

Indeed \(0\le x\le\|x\|e\) makes \(f(x)\) finite and at most \(\|x\|\tau(e)\). Define \(f(a-b)=f(a)-f(b)\) on the self-adjoint part. If \(a-b=a'-b'\), then \(a+b'=a'+b\); additivity makes the two proposed values equal. Additivity and real homogeneity follow on this real space, and its complexification is linear on the corner. It is positive. Positive-functional Cauchy–Schwarz gives
\[
 |f(x)|^2\le f(e)f(x^*x)\le \tau(e)^2\|x\|^2,
 \qquad \|f\|=f(e)=\tau(e).
\]
Faithfulness is inherited on positive elements. The trace identity for the weight gives \(f(x^*x)=f(xx^*)\) for every corner element. The hermitian sesquilinear form
\[
 B(x,y)=f(x^*y)-f(yx^*)
\]
therefore has zero diagonal. Complex polarization gives \(B=0\); put \(x=a^*,y=b\) to obtain \(f(ab)=f(ba)\).

For the topology assertion, take a bounded increasing net in the positive corner. Its strong supremum in \(N\) is still supported by \(e\), so it is also its corner supremum. The order-normality assumption on \(\tau\) thus gives order normality of the bounded functional \(f\). The complete **bounded-functional theorem NF1–4** in the retained normality proof now gives \(f\in(eNe)_*\). Its scope is any bounded order-normal positive functional on any concrete von Neumann algebra; faithfulness and countability of the given representation are not premises.

Here is the exact content of that theorem used at this step. NF1 constructs the support corner of the functional. NF2 constructs an actual faithful vector-series state on that corner. NF3 proves uniform absolute continuity on its positive unit ball: a summable sequence defines a closed nonnegative form; its spectral cutoffs and order normality give the required uniform estimate. NF4 applies complex Hahn–Banach to the graph \(x\mapsto(x,\pi(x)\Omega)\) and approximates the functional in norm by actual normal vector coefficients. CP6's norm-closed concrete predual then gives membership in the predual. The full closed-form representation used there is FF4; its graph inclusion and the operator \(jj^*\) prove that representation. The normal GNS representation is used only for the already explicit vector-series state, with the complete ST coefficient proof. Consequently this route does not assume its order-to-topology conclusion as a premise.

The retained NF proof uses first-variable-linear inner products. Conjugating the displayed coefficients gives the second-variable convention here, for example \(x\mapsto\langle\eta,\pi(x)\Omega\rangle\); all norm, positivity and continuity statements are identical.

This proves the topology assertion needed in (TC4) of the finite-trace corner construction. Normality of the entire bounded corner state has been supplied, together with its positivity, trace law, faithfulness and exact normalization. The zero algebra needs no nonzero finite-trace projection or normalization.

<a id="hyp1"></a>
## HYP1. The full finite homogeneous decomposition

Let \(M\) be any finite von Neumann algebra, \(Z=Z(M)\), and \(T:M\to Z\) the normal faithful center-valued trace constructed in FCT0–7. Let \(z_a\) be the join of the central supports of all abelian projections. A projection \(e\) is abelian when \(eMe\) is commutative.

The beginning of FCT3 proves that every nonzero projection below \(z_a\) contains a nonzero abelian projection. To recall its precise reason, a polar bridge to an abelian projection produces an abelian subprojection. If no bridge exists, PC2 makes the central supports orthogonal; a nonzero projection below their join cannot be orthogonal to all of them.

For a nonzero abelian \(e\), FCT3 constructs a central partition of \(c(e)\) into pieces \(w_n\), \(n\ge1\), on which
\[
 w_n=e_{1,n}+\cdots+e_{n,n},
 \qquad e_{i,n}\sim ew_n.
\]
The construction first successively places copies of central cuts of \(e\) in the residual. The residual central supports decrease. A nonzero projection in their intersection would give infinitely many orthogonal copies of one nonzero projection, contradicting finiteness by FCT2. Their successive differences are the required \(w_n\). This includes all finite sizes and can have nonzero pieces at unboundedly many sizes.

For clarity we give the complete matrix identification on such a nonzero piece \(w\) of size \(n\). Choose \(v_i\) with
\[
 v_i^*v_i=e_1,\quad v_iv_i^*=e_i,\quad v_1=e_1,
 \qquad E_{ij}=v_iv_j^*.
\]
Orthogonality of the \(e_i\)'s gives \(E_{ij}E_{kl}=\delta_{jk}E_{il}\), \(E_{ij}^*=E_{ji}\), and \(\sum_iE_{ii}=w\). By PC4, compression \(z\mapsto ze_1\) is a normal \*-isomorphism from \(Zw\) onto \(Z(e_1Me_1)=e_1Me_1\), with normal inverse. Define
\[
 \Psi:M_n(Zw)\longrightarrow Mw,\qquad
 \Psi([z_{ij}])=\sum_{i,j}z_{ij}E_{ij}.
\]
The matrix-unit identities prove that \(\Psi\) is a unital \*-homomorphism. Given \(x\in Mw\), each \(v_i^*xv_j\) is in \(e_1Me_1\), so has the unique form \(z_{ij}e_1\). The finite identity resolutions show \(x=\sum_{i,j}v_i(v_i^*xv_j)v_j^*=\Psi([z_{ij}])\). These same corner compressions prove injectivity. The complete C\*-norm and matrix-order results give isometry and order preservation in both directions. Normality of \(\Psi\) follows from its finite sum of fixed multiplications; normality of its inverse follows from the corner compressions and PC4's inverse topology. Thus this is the full normal homogeneous matrix realization.

Choose a maximal disjoint family of central units carrying such finite homogeneous realizations. If their sum missed a nonzero central part of \(z_a\), that part would contain an abelian projection and the preceding construction would supply a further nonzero homogeneous unit. Hence they fill \(z_a\). Group the units by their finite size. For a fixed size, take the bounded strong-star central sums of their matrix units; PC1 gives these sums and multiplication passes to their uniformly bounded strong limits. They again satisfy every matrix-unit relation. Their first diagonal projection is abelian, since its corner is the product of the abelian corners on the disjoint central units. The matrix realization just proved therefore assembles the whole size-\(n\) part into \(M_n(Zz_n)\). This works for an arbitrary number of central units.

On \(M(1-z_a)\) there is no nonzero abelian projection. The pair construction and maximality argument in FCT3 halve every nonzero central unit into equivalent complementary projections. Repeated halving and transport give coherent divisions into \(2^m\) equivalent orthogonal projections for every \(m\). FCT3 also proves that every projection is an arbitrary orthogonal sum of central tiles. These are exactly the decomposition, halving and monic-projection assertions used in the hypertrace lesson.

Finally on a homogeneous size-\(n\) part, center linearity and traciality give
\[
 T(E_{ii})=w/n,\qquad T(E_{ij})=0\ (i\ne j),\qquad
 T(\Psi([z_{ij}]))=\frac1n\sum_i z_{ii}.
\]
For the off-diagonal assertion use \(E_{ii}E_{ij}=E_{ij}\) and \(E_{ij}E_{ii}=0\). The diagonal values are equal by equivalence and sum to \(T(w)=w\).

<a id="hyp2"></a>
## HYP2. Exact spectral thresholds and central matrix ranks

The full retained spectral proof SF/SB0–6 constructs the spectral measure of a bounded self-adjoint operator on an arbitrary Hilbert space and proves that its bounded Borel functions belong to the given von Neumann algebra. In particular, for \(a\ge0\),
\[
 p_\delta=1_{[\delta,\infty)}(a)\in M,\qquad
 \delta p_\delta\le a,\qquad
 p_\delta\uparrow s(a)\quad(\delta\downarrow0).
\]
These formulas follow on the spectral representation from the corresponding pointwise scalar inequalities. If \(a\ne0\), some \(p_\delta\) is nonzero: otherwise the squared-integral representation of \(\|a\xi\|\) is zero for every vector. If \(a\) is in a projection corner, every strictly positive threshold lies in that corner. If \(a\) is central, its spectral projections are central, by the unitary covariance and commutant test in SB6.

For a positive contraction and an integer \(N\ge1\), the projections
\[
 1_{[k/N,(k+1)/N)}(a)\quad(0\le k<N),
 \qquad 1_{\{1\}}(a)
\]
are pairwise orthogonal and sum to the identity of its algebra. On the \(k\)-th piece the operator lies between \(k/N\) and \((k+1)/N\). The endpoint piece has value exactly one. These are the precise central cuts used in AVG.

Every bounded self-adjoint \(a\) has uniform finite spectral-step approximants. Partition a compact interval containing its spectrum into half-open intervals of length at most \(\varepsilon\), treating the final endpoint separately, and choose a scalar from each interval. The resulting finite sum \(\sum_jt_j1_{I_j}(a)\) has distance at most \(\varepsilon\) from \(a\), by the spectral norm formula. For \(a\ge0\), the scalars can be nonnegative. Thus agreement of bounded linear maps on all projections implies agreement on the entire self-adjoint part and then, by complex linearity, on the entire algebra.

Here is the complete central-rank step in AVG. Let \(P\in M_n(Z)\) be a projection and put \(D=\sum_iP_{ii}\in Z\). For every character \(\chi\) of \(Z\), the matrix \([\chi(P_{ij})]\) is a numerical self-adjoint projection, so \(\chi(D)\in\{0,\ldots,n\}\). The complete character proof cited above supplies these characters and their separation property. Therefore
\[
 \prod_{k=0}^n(D-k1)=0.
\]
Define the Lagrange polynomials
\[
 z_k=\prod_{\substack{0\le j\le n\\j\ne k}}
                \frac{D-j1}{k-j}.
\]
Characters take the values zero or one on each \(z_k\), exactly according to the numerical rank. Character separation verifies \(z_k=z_k^*=z_k^2\), \(z_kz_l=0\) for \(k\ne l\), \(\sum_kz_k=1\), and \(D=\sum_kkz_k\). On the central piece \(z_k\), HYP1's trace formula gives \(T(Pz_k)=(k/n)z_k\). The standard first-\(k\)-coordinate projection has the same center-valued trace. FCT7 therefore makes the two projections equivalent, and FCT2 extends the implementing partial isometry to a unitary of that finite corner. This proves the whole constant-rank unitary reduction, including \(k=0,n\) and \(n=1\). Zero central pieces are omitted.

<a id="hyp3"></a>
## HYP3. The wider semifinite corner passage

PC6 proves that finite joins, and hence finite orthogonal sums, of Murray–von Neumann finite projections are finite. Finiteness of a projection is equivalent to finiteness of its corner: if a proper subprojection is equivalent to the corner unit, its implementing partial isometry is a nonunitary isometry in that corner, and conversely. Every such corner can act on an infinite-dimensional Hilbert space.

Under the projection-semifiniteness hypothesis, every nonzero residual projection contains a nonzero finite projection. A maximal orthogonal family of these finite projections therefore fills the identity. Its finite partial sums increase strongly to one, by the squared-norm tail estimate for orthogonal families in PC1. Each sum is finite by PC6. These are exactly the corners used by Corollary 6.3, with its original arbitrary index sets.

The separate finite-trace construction starts instead from a specified faithful normal semifinite scalar trace. In its finite-ideal convention, if \(p x=0\) for every \(x\) in the ultraweakly dense finite ideal, continuity of fixed multiplication gives \(pN=0\). Thus every nonzero projection has a nonzero element \(px\) of that form. The trace identity gives
\[
 0<\tau((px)(px)^*)=\tau(x^*px)\le\tau(x^*x)<\infty.
\]
A positive threshold from HYP2 supplies a nonzero \(q\le p\) of finite trace. The order definition of semifiniteness supplies the finite positive element directly and gives the same threshold argument. A maximal orthogonal family of these finite-trace projections fills one by the same residual argument. Every nonempty finite partial sum \(e\) has \(0<\tau(e)<\infty\). HYP0 supplies the actual faithful ultraweakly continuous tracial state on its whole corner.

Corner injectivity and the arbitrary increasing-corner approximation are proved in full by Lemmas 6.1–6.2 of the main lesson. Compression \(x\mapsto exe\) is normal completely positive and contractive at every matrix size. Its uniformly bounded strong-star convergence to \(x\) gives convergence on every concrete series-vector functional by CP's finite-head and summable-tail estimate. Choose one corner for a prescribed finite list of tests, then choose its finite-dimensional model. The two errors add. This proves both original corner passages at their different stated hypotheses, including the zero algebra and empty test lists.

<a id="hyp4"></a>
## HYP4. Finite spectral integrals and the whole scope

All integrals in Lemma 1.2 and the threshold part of Theorem 2.1 are finite step integrals. Restrict the two positive finite-rank operators to the finite-dimensional sum of their ranges; this subspace reduces both. Their finite spectral resolutions, including zero eigenvalues, give the nonnegative overlaps \(w_{sv}=\operatorname{Tr}(e_sf_v)\). A threshold changes only at one of the finitely many numbers \(s^2,v^2\). The indicator integrals are therefore ordinary finite sums of interval lengths; the values at the finitely many endpoints do not change them. This proves the exact integration convention used in the displayed spectral-overlap identities and all eight whole solutions.

The threshold contradiction also takes place on this finite partition. If the squared commutator-error sum were at least \(\varepsilon^2\) times the rank on every open interval having nonzero rank, integrating would contradict the displayed strict bound and the rank integral one. Thus one interval has the strict reverse inequality, and any interior threshold there gives the required nonzero finite-rank projection. The proof never requires a simultaneous eigenbasis for the two positive operators.

The three original figures retain their precise roles: the finite-trace corner diagram describes the sum of the two approximation errors, the spectral-overlap curve samples the exact parameter family in Example 1.3, and the cyclic-rounding array samples the uniform counting argument in AVG. Their full arguments remain in the main lesson.

The original whole scope includes prescribed normal traces in DEN and SC, arbitrary normal central supports and products in SUP, and possibly singular tracial states in ALL and Lemma 3.1. The latter conclusion uses the uniform-in-matrix-size norm averaging proof AVG. Its passage through arbitrary central products takes place in operator norm before evaluating the state, so it also applies to singular states. These distinctions, both semifinite conventions, and every original solved exercise are retained.

## Human comparisons and terms

Claire Anantharaman and Sorin Popa's author-hosted [draft](https://idpoisson.fr/anantharaman/publications/IIun.pdf) supplies the finite sign-support, prescribed-trace convexity, spectral-overlap and finite-product-vector method comparisons at Theorem 7.3.7, Theorem 10.2.9, Proposition 10.3.3, Theorem 10.3.4, Lemma 13.1.11 and Theorem 13.4.2. The local matrix and corner proofs supply their complete hypotheses and prerequisite routes.

Jesse Peterson's [2020 author notes](https://math.vanderbilt.edu/peters10/teaching/spring2020/OperatorAlgebras.pdf), Sections 5.1–5.2 and Chapters 5–6, provide projection-comparison and finite-trace context. The retained PC/FCT proofs establish the full arbitrary-center statements used here. Hiai's [author notes, version 1](https://arxiv.org/pdf/2004.02383v1), Definition 7.1 and Theorem 7.2, state broader weight normality criteria; HYP0 uses the separately proved bounded-functional theorem NF1–4.

These links provide freely readable mathematical comparisons. They grant no licence to adapt or redistribute the human text. All human works retain their own terms.
