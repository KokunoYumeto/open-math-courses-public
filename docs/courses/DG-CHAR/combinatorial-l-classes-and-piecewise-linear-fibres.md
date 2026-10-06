# Combinatorial L-classes and piecewise linear fibres

*Written and self-checked by the writing AI, GPT-6.1 Sol (OpenAI), at Ultra. Independently authored text dedicated under CC0. No independent AI review is recorded.*

A generic fibre of a piecewise linear map has a signature even when its source is only a rational homology manifold. We prove that this signature is independent of the generic value and of the map's homotopy representative. Sphere maps then determine unique rational L-classes, and stabilization removes the dimension restriction. Six original graded exercises have complete solutions.

This chapter proves the generic-fibre and stable-range construction, its sphere stabilization, and the duality and approximation results used here. The [smooth-comparison companion](smooth-fibres-triangulation-comparison-and-lens-spaces.md) proves compatibility with tangent L-classes for a given smooth triangulation and supplies the lens-space application. [The triangulation companion](smooth-triangulations-and-the-integral-pl-obstruction.md) proves existence, relative extension and the precise integral-refinement obstruction.

The exact proved prerequisites are [Thom and Euler classes](thom-classes-and-euler-classes.md) for singular excision, products, coefficient comparisons and right cap; [Frame fields](frame-fields-and-primary-obstructions.md) for degree classification, first Hurewicz, homotopy extension and the full cellular comparison; [Homotopy fibres](homotopy-fibres-and-the-serre-spectral-sequence.md) for filtered chains and relative CW compression; [Rational homotopy](rational-homotopy-and-the-hurewicz-range.md) for sphere finiteness with its complete proof; [Manifold duality](manifold-duality-the-diagonal-and-wu-classes.md) for the exact cap boundary convention; [Characteristic numbers](characteristic-numbers-and-projective-product-independence.md) for integral Newton identities; [The signature theorem](multiplicative-sequences-and-the-signature-theorem.md) for the full rational form algebra and universal multiplicative sequences; and [Odd-prime operations](odd-prime-reduced-powers-and-wu-classes.md) for normalization and the realization comparison. The actual complete used proofs, coefficients and dimension conditions were checked.

## A. Generic simplicial fibres and their local homology

The coefficient field in this chapter is \(\mathbb Q\). A locally finite simplicial complex \(K\) is a **rational homology \(n\)-manifold without boundary** if
\[
H_j(K,K-\{x\};\mathbb Q)=
\begin{cases}\mathbb Q&j=n,\\0&j\ne n,\end{cases}
\tag{A.1}
\]
at every point \(x\). This definition is a statement about local homology; it does not assert that a neighbourhood is a Euclidean ball. Compactness makes such a locally finite complex finite: finitely many local neighbourhoods, each meeting only finitely many simplices, cover it.

We first prove the local product assertion needed for generic fibres. Neither a differentiable implicit-function theorem nor a PL transversality theorem is assumed.

**Lemma A.1 — Product over an open target simplex.** Let \(K,L\) be locally finite simplicial complexes, let \(f:K\to L\) be a simplicial map, let \(V\) be the interior of a simplex \(\sigma=[w_0,\ldots,w_s]\) of \(L\), and choose \(y=\sum_j t_j w_j\in V\), with each \(t_j>0\). There is a homeomorphism
\[
f^{-1}(V)\longrightarrow V\times f^{-1}(y)
\tag{A.2}
\]
whose first coordinate is \(f\). This assertion concerns the open simplex, with no claim over its closed boundary.

**Proof.** For a point \(x\in f^{-1}(V)\), every vertex in the support of its barycentric coordinates maps to one of the \(w_j\)'s. Indeed all coordinate contributions are nonnegative, and a contribution at another target vertex would put \(f(x)\) outside \(\sigma\). Write \(c_v\) for these source coordinates and
\(s_j=\sum_{f(v)=w_j}c_v\).
Every \(s_j\) is positive, because \(f(x)\) is in the interior. Define
\[
x_y=\sum_j\sum_{f(v)=w_j}\frac{t_j}{s_j}c_v v.
\tag{A.3}
\]
Its coordinates are nonnegative and sum to \(\sum_jt_j=1\). It has the same support as \(x\), so remains in its source simplex, and its image is \(y\). Send \(x\) to \((\sum_j s_jw_j,x_y)\).

Conversely, for \(y'=\sum_j s_jw_j\in V\) and a point \(z\in f^{-1}(y)\), multiply every coordinate of \(z\) at a vertex mapping to \(w_j\) by \(s_j/t_j\). The resulting point has the same source support and image \(y'\). These two coordinate rules are inverse. They agree on common source faces and are continuous on each simplex, since their denominators are positive on the indicated open set. The weak simplex topology gives global continuity; for a locally finite complex it can also be checked in a finite union of simplices near every point. This proves the homeomorphism. ∎

**Lemma A.2 — Removing an ordinary local factor.** If \(Z\) is Hausdorff, \(V\) is an open \(s\)-simplex, and \(v\in V,z\in Z\), then
\[
H_j(V\times Z,(V\times Z)-\{(v,z)\};\mathbb Q)
\cong H_{j-s}(Z,Z-\{z\};\mathbb Q).
\tag{A.4}
\]
The isomorphism uses the positive local generator of the oriented \(V\).

**Proof.** The punctured product is
\((V-\{v\})\times Z\ \cup\ V\times(Z-\{z\})\).
Both punctured factors are open. Thus the full relative external-chain product comparison of the Thom chapter applies to this union. It identifies the pair's chains up to chain homotopy with
\[
C_*(V,V-\{v\};\mathbb Q)\otimes
C_*(Z,Z-\{z\};\mathbb Q).
\]
The first complex has homology \(\mathbb Q\) only in degree \(s\), by the proved local ball/sphere calculation. Splitting cycles and boundaries in a vector-space complex gives an actual chain homotopy equivalence with \(\mathbb Q[s]\). Tensoring that equivalence gives (A.4), with its generator and shift specified. This includes \(s=0\). ∎

**Proposition A.3 — Generic fibre local homology.** Suppose \(K\) is a compact rational homology \(n\)-manifold, \(L\) is a triangulated \(s\)-sphere and \(f:K\to L\) is simplicial. For every point \(y\) in the interior of a top-dimensional target simplex, \(f^{-1}(y)\) is a compact finite polyhedron satisfying (A.1) in dimension \(n-s\), or it is empty.

**Proof.** The fibre is closed in the compact complex, hence compact. In each source simplex its defining equations fix the sums of coordinates in the vertex groups of Lemma A.1. The solution is either empty or a convex polytope, specifically a product of scaled simplices. Its faces are the intersections with source faces. These finitely many polytopes can be triangulated compatibly: choose a barycentre in every nonempty face and use the simplices indexed by strictly nested face chains. Induction in face dimension proves this triangulation by coning the already triangulated boundary to the barycentre; convexity makes these cones cover the face with disjoint interiors. The choices on a shared face are identical. Thus the fibre is a finite polyhedron.

At a fibre point, Lemma A.1 identifies its neighbourhood in \(K\) with a neighbourhood in \(V\times f^{-1}(y)\). Relative excision identifies their point-local homology, and Lemma A.2 removes \(V\). Condition (A.1) on \(K\) gives exactly one copy of \(\mathbb Q\) in fibre degree \(n-s\), zero elsewhere. If \(s>n\), this required group would be in a negative degree, which cannot occur, so every such fibre is empty. ∎

These results prove the local-homology part of the generic-fibre construction. Orientation, duality, equality of the signatures in different target simplex interiors and their homotopy additivity require further proofs below; local product alone does not establish them.

## B. Recovering Pontryagin classes from the L-classes

The first formulas \(L_1=p_1/3\) and \(L_2=(7p_2-p_1^2)/45\) suggest recursive recovery of the \(p_i\)'s. We need a proof that the coefficient of \(p_i\) is nonzero for **every** \(i\), not an extrapolation from these examples.

**Lemma B.1 — Every indecomposable L-coefficient is positive.** In the rational polynomial \(L_j(p_1,\ldots,p_j)\), the coefficient \(c_j\) of the term \(p_j\) is strictly positive. Thus
\[
L_j=c_jp_j+R_j(p_1,\ldots,p_{j-1})
\tag{B.1}
\]
and each \(p_j\) is uniquely expressible as a rational polynomial in \(L_1,\ldots,L_j\).

**Proof.** All series here are formal over \(\mathbb Q\). Set
\(F(s)=s\cot s=s\cos s/\sin s\),
where cancellation of the leading \(s\) makes the quotient a well-defined even series with constant term one. The formal derivative identities for sine and cosine give
\[
sF'=F-F^2-s^2.
\tag{B.2}
\]
Write \(F=1-\sum_{j\geq1}b_js^{2j}=1-B\). Comparing coefficients gives
\[
(2j+1)b_j=\mathbf1_{j=1}
 +\sum_{\substack{a+b=j\\a,b\geq1}}b_a b_b.
\tag{B.3}
\]
It follows that \(b_1=1/3>0\). For \(j>1\) the sum contains \(b_1b_{j-1}>0\), and all other terms are nonnegative by induction, so \(b_j>0\).

If \(f(t)=\sqrt t/\tanh\sqrt t\) is the formal L-series, substitution into its sine/cosine definitions gives \(f(-s^2)=F(s)\). This identity needs no choice of a complex square root: the coefficients of \(\sinh s/s\) and \(\cosh s\) become those of \(\sin s/s\) and \(\cos s\) under \(s^2\mapsto-s^2\). Since
\(\log(1-B)=-\sum_{m\geq1}B^m/m\),
every coefficient of \(s^{2j}\) in \(\log F\) is strictly negative; the term \(m=1\) already contributes \(-b_j\), and all other terms are nonpositive. Hence the coefficient \(\lambda_j\) of \(t^j\) in \(\log f(t)\) has sign \((-1)^{j-1}\) and is nonzero.

In formal roots \(z_a\), the multiplicative-sequence theorem gives
\[
\log L(p)=\sum_a\log f(z_a)
 =\sum_{j\geq1}\lambda_j\sum_a z_a^j.
\]
The integral Newton identity already proved in Characteristic numbers, (2.3), says the power sum of weight \(j\) has coefficient \((-1)^{j-1}j\) on \(p_j\), with all remaining terms in lower \(p\)'s. Exponentiating the logarithm adds in weight \(j\) only products of smaller positive weights; they involve no \(p_j\). Thus
\(c_j=(-1)^{j-1}j\lambda_j>0\).
This proves (B.1). Solve it recursively:
\[
p_j=c_j^{-1}\bigl(L_j-R_j(p_1,\ldots,p_{j-1})\bigr).
\]
Starting at \(p_1=3L_1\), induction supplies both existence and uniqueness of the rational polynomial expressions. The argument proves the required nonvanishing directly; it makes no unproved assertion about Bernoulli-number signs. ∎

## C. Sphere maps detect the rational cohomology in the required range

We prove the precise comparison used later. The input is a **finite** CW complex \(X\) of dimension \(n\), and \(k\geq2\) satisfies
\[
n<2k-1.
\tag{C.1}
\]
The positive integral generator of \(H^k(S^k;\mathbb Z)\) is \(u\). The full prerequisites are the degree classification in [Frame fields](frame-fields-and-primary-obstructions.md), LemmaB.1; its arbitrary-CW cellular coefficient comparison, LemmaG.1; the relative compression and cell-dimension proofs in [Homotopy fibres](homotopy-fibres-and-the-serre-spectral-sequence.md), SectionB; and sphere finiteness with its actual proof in [Rational homotopy](rational-homotopy-and-the-hurewicz-range.md), TheoremH.3.

### C.1. The group operation and degree maps

Let \(\pi^k(X)=[X,S^k]\), taking unbased homotopy classes. We construct its abelian group structure under (C.1). First suppose \(X\) connected and choose a vertex. Since the target is simply connected, these classes coincide with based classes: a path moves a vertex value to the basepoint by homotopy extension; the vertex path in a homotopy between based maps is a loop, whose null-homotopy and homotopy extension make that homotopy based. Treat the finitely many components separately otherwise.

**Lemma C.1 — The wedge comparison.** For every finite number \(a\) of factors, the inclusion
\[
\bigvee_{j=1}^a S^k\longrightarrow\prod_{j=1}^a S^k
\tag{C.2}
\]
induces a bijection on homotopy classes of maps from \(X\).

**Proof.** Give each sphere its one-vertex, one-\(k\)-cell structure. The product has cells indexed by the chosen positive cells in a subset of its factors. The wedge consists of its zero-cell and single-factor cells. Every remaining cell has dimension at least \(2k\). The pair is therefore \((2k-1)\)-connected by the full cell-dimension argument in homotopy SectionB.2. Relative compression moves every map of \(X\) into the wedge. It also moves a homotopy, whose source pair \((X\times I,X\times\partial I)\) has dimension at most \(n+1<2k\), into the wedge while fixing its endpoints. Thus the induced map is surjective and injective. The same proof permits fixing chosen source vertices. ∎

For \(f,g:X\to S^k\), lift the pair map \((f,g)\) uniquely up to homotopy to the two-sphere wedge and then fold its two copies by their positive identity maps. Define \(f+g\) by this composition. Lemma C.1 makes it well defined. The three-factor version proves associativity: both parenthesizations lift the same triple of coordinates, and their final fold is the identity on each copy. Permuting the two factors and then folding gives the same map, proving commutativity. The constant map is an identity, since a lift of \((f,0)\) lies explicitly in its first wedge copy.

To prove the inverse rule, let \(R:S^k\to S^k\) be a coordinate reflection fixing the basepoint, of degree \(-1\). The map \((1,R):S^k\to S^k\times S^k\) has a wedge lift obtained by pinching the sphere into two positive spheres and applying \(R\) to the second copy. Its two coordinate maps have degrees \(1,-1\), hence are homotopic to \(1,R\) by the complete degree theorem. Folding has degree zero, and is null-homotopic by that same theorem. Composing this lift with \(f\) gives a lift of \((f,Rf)\). Thus \(Rf\) is the inverse of \(f\). We have proved an abelian group, with all its axioms.

The construction is natural under precomposition. Also
\[
h:\pi^k(X)\longrightarrow H^k(X;\mathbb Z),\qquad
h([f])=f^*u
\tag{C.3}
\]
is a homomorphism: on the wedge, the folded generator is the sum of the two pulled-back coordinate generators. The cohomology of the wedge in degree \(k\) is its two free cell generators, so this equality follows by its restriction to each copy.

**Lemma C.2 — A degree-\(d\) target map acts as multiplication by \(d\).** If \(\delta_d:S^k\to S^k\) has degree \(d\), postcomposition by \(\delta_d\) on \(\pi^k(X)\) is multiplication by \(d\).

**Proof.** For \(d>0\), pinch a sphere into \(d\) positively oriented copies and fold. Its degree is \(d\), so it is homotopic to \(\delta_d\). The pinch has each coordinate projection of degree one. Composing with \(f\), Lemma C.1 therefore identifies it with the unique wedge lift of the \(d\)-tuple \((f,\ldots,f)\). Its fold represents the sum of \(d\) copies of \(f\). Degree zero gives the null map by degree classification, and negative degrees use the reflection inverse just proved. ∎

We will also use the resulting statement on ordinary homotopy groups of the sphere in dimensions \(j<2k-1\). For \(j\geq1\), the group operation just constructed on \([S^j,S^k]\) agrees with its usual homotopy group operation. Indeed the usual source pinch followed by \(f\vee g\) is a wedge lift of \((f,g)\): its coordinate collapses are based degree-one maps of \(S^j\), hence homotopic to the identity by the degree theorem. Folding gives the usual concatenation class. For \(j=1\) both groups are zero because \(k\geq2\). Thus the target degree map acts on \(\pi_j(S^k)\) as multiplication by \(d\) in every required degree.

### C.2. A rational telescope and a one-group replacement

**Theorem C.3 — Rational cohomotopy comparison.** Under (C.1), (C.3) induces a natural isomorphism
\[
\pi^k(X)\otimes_{\mathbb Z}\mathbb Q
\ \xrightarrow{\ \cong\ }\ H^k(X;\mathbb Q).
\tag{C.4}
\]
In particular, rational cohomology is spanned by the classes \(f^*u\), and every element in the kernel of (C.3) is torsion in the cohomotopy group. Here the natural comparison \(H^k(X;\mathbb Z)\otimes\mathbb Q\cong H^k(X;\mathbb Q)\) uses the finite free cellular cochain complex: tensoring it with the flat module \(\mathbb Q\) preserves its cycles and boundaries, and the full cellular comparison identifies both cohomologies with their singular versions.

**Proof: the telescope.** If \(n<k\), cellular compression makes every map to \(S^k\) null-homotopic and cellular cohomology makes the target zero, so assume \(n\geq k\). Form the mapping telescope
\[
S^k\xrightarrow{\delta_{2!}}S^k
\xrightarrow{\delta_{3!}}S^k
\xrightarrow{\delta_{4!}}\cdots ,
\tag{C.5}
\]
using based cellular degree maps. A mapping cylinder has its usual CW structure, with the cylinder cells of each sphere cell and the target sphere cells; these structures glue to a CW telescope \(T\). Its continuous height coordinate is bounded on every compact subset. Consequently every map from a compact sphere, every sphere homotopy, every map from the finite complex \(X\), and every such homotopy lies in a finite subtelescope. Each finite subtelescope deformation retracts onto its last sphere, by the mapping-cylinder retraction. Therefore
\[
\pi_j(T)=\varinjlim \pi_j(S^k),\qquad
[X,T]=\varinjlim [X,S^k].
\tag{C.6}
\]
The transition maps are the actual degree maps of (C.5). For based homotopy groups, use the telescope's basepoint spine to identify each stage basepoint with the first one. The cylinder retractions preserve this spine, so the displayed comparison is also the based comparison; its simply connected targets introduce no path ambiguity.

For \(j\leq n<2k-1\), Lemma C.2 identifies their maps on homotopy groups with multiplication by their degrees. The sphere connectivity and finiteness theorem say the groups are zero below \(k\), \(\mathbb Z\) at \(k\), and finite for \(k<j\leq n\). Every element in one of these finite groups is eventually killed: some later factorial degree is divisible by its order. At \(k\), the direct limit is \(\mathbb Q\). More explicitly, if \(D_m\) is the product of the first \(m\) degrees, the generator at stage \(m\) represents \(1/D_m\). Every positive integer divides some \(D_m\), so these fractions form all of \(\mathbb Q\). Thus
\[
\pi_j(T)=
\begin{cases}\mathbb Q&j=k,\\0&1\leq j\leq n,\ j\ne k.\end{cases}
\tag{C.7}
\]
Likewise, for the abelian group \(A=\pi^k(X)\), (C.6) and Lemma C.2 identify
\[
[X,T]=\varinjlim(A\xrightarrow{2!}A\xrightarrow{3!}\cdots)
=A\otimes\mathbb Q.
\tag{C.8}
\]
The algebraic identification sends a stage-\(m\) element \(a\) to \(a/D_m\). Common denominators prove surjectivity; a fraction that is zero means \(a\) is torsion, and a sufficiently late factorial kills it, proving injectivity. This is the localization/tensor comparison already proved in the coefficient foundations, and needs no finite-generation hypothesis on \(A\).

**Proof: removing the unused higher groups.** For \(j=n+1,n+2,\ldots\), attach a \((j+1)\)-cell for each element of the current \(\pi_j\), using cellular representatives. The cell-dimension theorem preserves every lower group and maps the old \(\pi_j\) onto the new one. Each old representative now bounds its attached disk, so the new \(\pi_j\) is zero. At the union \(Y\), compact sphere maps and homotopies have finite CW carriers and lie in a finite construction stage; this proves that the fixed lower groups stay fixed and all the higher groups are zero. This is the complete cell-killing argument of rational SectionF.4, applied here without a finite-generation assumption. We obtain a CW complex with exactly one positive homotopy group, \(\pi_k(Y)=\mathbb Q\).

The pair \((Y,T)\) has no relative cells in dimensions at most \(n+1\). Relative compression on \(X\) and its endpoint-fixed homotopies consequently gives
\[
[X,T]\xrightarrow{\ \cong\ }[X,Y].
\tag{C.9}
\]

**Proof: the cellular cohomology classification.** We supply the needed classification of maps into \(Y\), rather than referring to a representation theorem. By its \((k-1)\)-connectivity, homotopy extension and cellular compression make a map \(X\to Y\) constant on \(X^{k-1}\). On each positive \(k\)-cell it then determines an element \(a_e\in\pi_k(Y)=\mathbb Q\), giving a cellular \(k\)-cochain \(a\). An attaching \((k+1)\)-sphere has image in \(Y\) whose first Hurewicz class is \((\delta a)\) on that cell. To verify this, collapse \(X^{k-1}\), express the attaching sphere in the oriented relative \(k\)-cell generators, and evaluate their incidence coefficients; this is exactly the full relative-chain definition of the cellular differential in Frame fields, LemmaG.1. The first Hurewicz isomorphism detects its homotopy class. Hence extension across that cell is equivalent to \(\delta a=0\). All later cells extend since every \(\pi_j(Y)\) for \(j>k\) is zero. Every cellular cocycle is therefore realized by a map.

Two normalized maps with cochains \(a_0,a_1\) are homotopic precisely when \(a_1-a_0=\delta b\) for a cellular \((k-1)\)-cochain \(b\). Construct the homotopy constant below dimension \(k-1\). On the cylinder of each \((k-1)\)-cell, the endpoints and side are constant; its collapsed boundary gives a \(k\)-sphere, on which any chosen value \(b_e\in\mathbb Q=\pi_k(Y)\) can be realized. On a \(k\)-cell cylinder the remaining obstruction is
\[
a_1-a_0-\delta b.
\tag{C.10}
\]
The signs are fixed by the ordinary prism convention
\(\partial P+P\partial=f_{1\#}-f_{0\#}\):
evaluation of a cocycle on its oriented cell generators gives exactly the endpoint difference minus evaluation on the side prisms. Those side evaluations are the cellular incidence differential \(\delta b\). The first Hurewicz isomorphism again detects this obstruction. If it is zero fill the cylinder; all higher cylinders fill because their boundary dimensions exceed \(k\). This proves sufficiency. For necessity, first make a given homotopy constant on the cylinders of \(X^{k-2}\), relative to its already normalized endpoints. Their relative dimension is at most \(k-1\), so connectivity and homotopy extension permit this normalization. The remaining \((k-1)\)-cell cylinders then have the prism values \(b_e\) just described, and the same boundary identity gives (C.10). Homotopy extension and weak topology justify the assembled maps and homotopies on all characteristic disks.

There is a class \(\upsilon\in H^k(Y;\mathbb Q)\) evaluating as the identity on \(\pi_k(Y)=H_k(Y;\mathbb Z)=\mathbb Q\). The first Hurewicz theorem and the coefficient theorem give this class uniquely, since all the lower positive homology groups vanish. The cellular values just calculated show that \(f\mapsto f^*\upsilon\) is precisely the bijection
\[
[X,Y]\xrightarrow{\ \cong\ }H^k(X;\mathbb Q).
\tag{C.11}
\]
It is natural under maps of the finite source complexes: it is actual cohomology pullback, rather than only a count of cell choices.

Finally identify the comparison itself. The inclusion of the stage-\(m\) sphere into \(Y\) sends its homotopy generator to \(1/D_m\), so pulls \(\upsilon\) back to \(u/D_m\). Thus the composite of (C.8), (C.9) and (C.11) sends \(a/D_m\) to \(h(a)/D_m\). This is exactly (C.4). It is a homomorphism because (C.3) is one; its proved bijectivity gives the claimed group isomorphism. No finite-kernel assertion was needed or inferred from rational tensoring. ∎

### C.3. The unique functional on cohomology

**Corollary C.4.** Under (C.1), every homomorphism
\(\sigma:\pi^k(X)\to\mathbb Z\) determines one and only one rational-linear functional
\[
\sigma_{\mathbb Q}:H^k(X;\mathbb Q)\longrightarrow\mathbb Q
\quad\text{with}\quad \sigma_{\mathbb Q}(f^*u)=\sigma([f]).
\tag{C.12}
\]

**Proof.** A homomorphism to \(\mathbb Z\) kills torsion. Thus \(\sigma\otimes1\) is well defined on \(\pi^k(X)\otimes\mathbb Q\); transport it across (C.4). Equivalently, assign \(\sigma(a)/d\) to \(h(a)/d\). If two such fractions represent the same cohomology class, their difference represents a torsion cohomotopy element by (C.4), whose signature is zero. The assignment is therefore well defined. Those fractions span all rational cohomology, proving uniqueness. ∎

For a compact rational homology \(n\)-manifold and \(k=n-4i\), condition (C.1) is exactly \(4i<(n-1)/2\). The later fibre-signature argument must still supply the homomorphism \(\sigma\) and the rational Poincaré pairing; this comparison alone does not assert either one.

## D. Duality for finite rational homology manifolds

We need duality for the polyhedra in Section A, whose links can be rational homology spheres without being spheres. Here is a chain proof over \(\mathbb Q\). It also proves the boundary version used by a homotopy of generic fibres.

### D.1. Links, orientations and the boundary condition

For a simplex \(\sigma\) of a finite complex \(K\), its **link** consists of the simplices \(\eta\) disjoint from \(\sigma\) for which \(\sigma\cup\eta\) is a simplex of \(K\). Include the empty face. Reduced homology uses the augmented convention: the empty link has one copy of \(\mathbb Q\) in degree \(-1\), and no other group.

**Lemma D.1 — Local homology is link homology with the correct shift.** If \(x\) is in the interior of a \(p\)-simplex \(\sigma\), then
\[
H_j(K,K-\{x\};\mathbb Q)
 \cong\widetilde H_{j-p-1}(\operatorname{lk}_K\sigma;\mathbb Q).
\tag{D.1}
\]

**Proof.** Points near \(x\) have positive coordinates at every vertex of \(\sigma\). The sum \(t\) of those coordinates is positive. Divide them by \(t\) to obtain a point of \(\operatorname{int}\sigma\); the remaining coordinates, divided by \(1-t\) when it is nonzero, give a point of the link. The outside height is \(1-t\), and at height zero its link coordinate is irrelevant. Restricting the normalized \(\sigma\)-coordinate to a small open neighbourhood of \(x\) and the height to \([0,\epsilon)\) gives an actual homeomorphism with
\[
V^p\times \operatorname{cone}_{[0,\epsilon)}
          (\operatorname{lk}_K\sigma).
\]
The coordinate rules and their inverse agree on all faces. The empty-link case means the cone consists only of its apex. Lemma A.2 removes \(V\). The cone is contractible and its punctured cone retracts onto the link by changing the positive height to a fixed height. The exact sequence of this pair therefore identifies its local homology with the reduced link homology shifted by one. Excision gives (D.1). ∎

Consequently the local condition (A.1) is equivalent to every \(p\)-simplex link having the rational reduced homology of \(S^{n-p-1}\). In particular, \(K\) is pure of dimension \(n\): a maximal \(p\)-simplex has empty link, so (D.1) forces \(p=n\). A codimension-one face has a zero-dimensional link with reduced \(H_0=\mathbb Q\), hence belongs to exactly two top simplices.

For the boundary version, a finite pair \((K,M)\), with \(M\) a subcomplex, is a **rational homology \(n\)-manifold with boundary** in the following precise sense. Off \(M\) it satisfies (A.1); at every point of \(M\) its ordinary point-local homology is zero in every degree; and \(M\) is a rational homology \((n-1)\)-manifold without boundary. By (D.1), links of interior simplices are rational spheres, links of boundary simplices in \(K\) are rationally acyclic, and their links in \(M\) are rational spheres of one lower dimension. These are local homology hypotheses, with no collar or Euclidean half-ball assumption.

This pair is pure of dimension \(n\). To check the only possible issue, a maximal simplex in \(M\) has dimension \(n-1\) by purity of \(M\); it cannot also be maximal in \(K\), since its empty \(K\)-link would have nonzero reduced homology. An extension to a maximal \(K\)-simplex is therefore outside \(M\) and has dimension \(n\). Every other maximal simplex is already interior and has that dimension. An interior \((n-1)\)-face belongs to two top simplices, and a boundary \((n-1)\)-face belongs to one: its \(K\)-link is a nonempty acyclic finite set.

Fix one total ordering of the vertices and use its induced orientation for every simplex. Write \([\tau:\sigma]\in\{0,1,-1\}\) for the simplicial boundary coefficient of \(\sigma\) in \(\tau\). An **orientation** here is a choice of top-simplex signs \(\epsilon_\rho\in\{1,-1\}\) for which
\[
c=\sum_{\dim\rho=n}\epsilon_\rho\rho,
\qquad \partial c\in C_{n-1}(M;\mathbb Q).
\tag{D.2}
\]
For a closed complex take \(M=\varnothing\). Thus the two contributions at each interior codimension-one face cancel. This is the usual coherent simplex orientation. On a triangulated oriented manifold, restricting its local orientation to the top-simplex interiors gives these signs; the elementary oriented-face boundary formula gives their cancellation. We use (D.2) as the explicit orientation datum also for homology manifolds.

At every interior point \(c\) has a nonzero local class. Indeed, around a \(p\)-simplex, its link chain is the sum of its incident top-link simplices with coefficients equal to the nonzero signed incidences in (D.2). Its boundary is zero by the same face cancellation. It is nonzero as a top-dimensional chain and cannot be a boundary, since the link has no higher-dimensional simplices. Its homology group has dimension one by (D.1), so it is a generator. This identifies the fundamental class \([K,M]=[c]\) and its coherent positive local values. At a boundary top face the coefficient of \(\partial c\) is \(1\) or \(-1\), since there is exactly one incident top simplex. The same link argument in \(M\), using \(\partial^2c=0\), shows that \(\partial c\) is its fundamental cycle. We give \(M\) this boundary orientation and thus have
\[
\partial[K,M]=[M].
\tag{D.3}
\]
In smooth half-ball coordinates it is the outward-normal-first convention, by the usual boundary of an oriented simplex. The arguments below use the explicit identity (D.3).

### D.2. Dual blocks and their relative generators

Let \(K'\) be the barycentric subdivision. Write \(b_\tau\) for the barycentre of a simplex \(\tau\). Its simplices are strictly increasing face chains. The **closed dual block** of a \(p\)-simplex \(\sigma\) is the order complex
\[
D_\sigma=\{\sigma\leq\tau_0<\cdots<\tau_a\}.
\]
Here \(\sigma\leq\tau_0\) allows a face chain to start at a proper coface. The boundary block \(\dot D_\sigma\) consists of the chains all of whose faces are proper cofaces of \(\sigma\). Thus
\[
D_\sigma=b_\sigma*\dot D_\sigma,
\qquad
\dot D_\sigma\cong(\operatorname{lk}_K\sigma)'.
\tag{D.4}
\]
The latter identification sends the proper coface \(\sigma\cup\eta\) to the nonempty link face \(\eta\) and preserves inclusion. In particular \(D_\sigma\) is a cone. The cone pair and its exact sequence give
\[
H_j(D_\sigma,\dot D_\sigma;\mathbb Q)=
\begin{cases}
\mathbb Q&j=n-p,\quad \sigma\notin M,\\
0&\text{otherwise}.
\end{cases}
\tag{D.5}
\]
For a top simplex its boundary block is empty and (D.5) says \(H_0(\{b_\sigma\})=\mathbb Q\). For a boundary simplex its link is acyclic, so its cone pair has zero homology in every degree.

The following explicit chain fixes both the generator and all incidence signs. For an interior \(p\)-simplex put
\[
z_\sigma=
\sum_{\sigma=\tau_p<\tau_{p+1}<\cdots<\tau_n}
 \epsilon_{\tau_n}
 \prod_{j=p}^{n-1}[\tau_{j+1}:\tau_j]\,
 [b_{\tau_p},b_{\tau_{p+1}},\ldots,b_{\tau_n}],
\tag{D.6}
\]
where every face in the flag has its indicated dimension. Orient a barycentric simplex in its displayed, increasing-dimension order.

**Lemma D.2 — The dual incidence identity.** For interior \(\sigma\),
\[
\partial z_\sigma=
\sum_{\substack{\tau>\sigma\\\dim\tau=p+1}}
[\tau:\sigma]z_\tau.
\tag{D.7}
\]
Moreover \(z_\sigma\) represents a generator in (D.5).

**Proof.** Delete a vertex of a flag in (D.6). Deleting its first vertex has boundary sign \(+1\). After grouping by \(\tau_{p+1}\), its coefficient is precisely \([\tau_{p+1}:\sigma]\) times (D.6) for that coface. Every coface of an interior simplex is interior, because \(M\) is a subcomplex.

Deleting a vertex strictly between the first and last leaves a gap of two face dimensions. Summing over its possible intermediate faces gives
\[
\sum_{\tau_j}
[\tau_{j+1}:\tau_j][\tau_j:\tau_{j-1}]=0,
\]
the coefficient of \(\tau_{j-1}\) in \(\partial^2\tau_{j+1}\). All other factors and the deletion sign are shared, so these terms cancel.

Deleting the last vertex gives the coefficient of a fixed \((n-1)\)-face in \(\partial c\), times the earlier flag factors and its common deletion sign. That face contains the interior \(\sigma\), so is outside \(M\); (D.2) makes its coefficient zero. These three kinds of deletion prove (D.7). If \(p=n\), \(z_\sigma=\epsilon_\sigma[b_\sigma]\) has zero boundary, which is also (D.7).

Equation (D.7) lies in \(\dot D_\sigma\), so \(z_\sigma\) is a relative cycle. Its top flag coefficients are nonzero. There are no chains of dimension above \(n-p\) in \(D_\sigma\), and no chains of dimension \(n-p\) in \(\dot D_\sigma\). Consequently it is not a relative boundary. Since (D.5) has dimension one, it is a generator. ∎

Filter \(K'\) by subcomplexes
\[
F_q=\bigcup_{\dim\sigma\geq n-q}D_\sigma
 \quad(0\leq q\leq n),\qquad F_{-1}=\varnothing.
\tag{D.8}
\]
The first stage is the set of top-simplex barycentres and the last is all of \(K'\). At stage \(q\) add the blocks for the \((n-q)\)-simplices. Two distinct new blocks intersect only in their boundary blocks, and their intersection with \(F_{q-1}\) is exactly their boundary block. This follows directly from the face-chain description: a chain that contains one of the new minimal faces cannot contain another of the same dimension.

On simplicial relative chains there is therefore an exact direct-sum decomposition
\[
C_*(F_q,F_{q-1};\mathbb Q)
 =\bigoplus_{\dim\sigma=n-q}
   C_*(D_\sigma,\dot D_\sigma;\mathbb Q).
\tag{D.9}
\]
Indeed a barycentric simplex not already in \(F_{q-1}\) has a unique minimal face of dimension \(n-q\), which places it in exactly one summand; its boundary either retains that face or is killed in the relative quotient. Simplicial-to-singular comparison for these finite pairs identifies the same relative homology. Its proof uses the dimension filtration: each relative simplex is sent to its singular disk generator; excision gives the disk relative groups; the pair exact sequences induct on the finite skeleta. This is the constant-coefficient specialization of the full relative-cell comparison in [Frame fields](frame-fields-and-primary-obstructions.md), LemmaG.1, also proved for realizations in [Odd-prime powers](odd-prime-reduced-powers-and-wu-classes.md), SectionI.4. Thus (D.9) proves the required relative splitting without assuming a collar of a dual-block boundary.

### D.3. Identifying the duality map with right cap

Put \(B_q=C^{n-q}(K,M;\mathbb Q)\), the relative simplicial cochains reindexed as a chain complex, and give it differential
\[
d_B a=(-1)^q\delta a,\qquad a\in B_q.
\tag{D.10}
\]
It is a differential since \(\delta^2=0\); its homology is the ordinary relative cohomology in degree \(n-q\). Set
\[
\gamma_p=(-1)^{\,n(n+1)/2+np-p(p-1)/2}.
\tag{D.11}
\]
The exponent is an integer, \(\gamma_n=1\), and
\(\gamma_p=(-1)^{n-p}\gamma_{p+1}\).
For the cochain \(\sigma^*\) evaluating as one on an interior oriented \(p\)-simplex and as zero on the other \(p\)-simplices, define
\[
\Phi(\sigma^*)=\gamma_p z_\sigma.
\tag{D.12}
\]
Equation (D.7) and the displayed relation between the \(\gamma\)'s show that \(\partial\Phi=\Phi d_B\), including the precise signs.

**Lemma D.3 — This chain map is an isomorphism on homology.** The map (D.12) gives
\[
H^p(K,M;\mathbb Q)\cong H_{n-p}(K;\mathbb Q).
\tag{D.13}
\]

**Proof.** Filter \(B\) by its terms of chain degree at most \(q\), and filter the target simplicial chain complex by (D.8). The map preserves filtration. At the first relative-homology page, the source has one basis vector in chain degree \(q\) for each interior \((n-q)\)-simplex and has zero homology in every other chain degree. Equations (D.5) and (D.9) give exactly the same description for the target. The induced map sends each basis vector to the nonzero generator \(\gamma_pz_\sigma\), so is an isomorphism on that page.

Apply the fully proved filtered-chain construction in [Homotopy fibres](homotopy-fibres-and-the-serre-spectral-sequence.md), TheoremA.1. Isomorphism on one page gives isomorphism on its next page by taking kernels and images of the commuting differentials. Induction gives isomorphism on the limiting page and thus on every successive quotient of the homology filtrations. Both filtrations have only the \(n+1\) stages in (D.8). The short exact sequences for successive stages show by induction that the homology map itself is an isomorphism: surjectivity lifts first in the quotient and then in the preceding stage; injectivity moves a zero-image element to the preceding stage and uses its injectivity. This proves (D.13), with no splitting assumption about the filtration. ∎

We must still identify (D.13) with the actual cup-product duality map. Recall the right cap convention from the Thom chapter:
\[
R_a[v_0,\ldots,v_m]
 =a([v_{m-p},\ldots,v_m])[v_0,\ldots,v_{m-p}],
 \qquad |a|=p.
\]
Its full boundary identity, proved in manifold (1.3), is
\[
\partial R_a t=R_a\partial t+(-1)^{m-p}R_{\delta a}t,
\qquad t\in C_m.
\tag{D.14}
\]
Since \(a\) vanishes on \(M\), \(R_a\partial c=0\). Hence \(a\mapsto R_a c\) is another chain map from (D.10), now into the original simplicial chains. Compose it with subdivision to obtain
\[
\Psi(a)=\operatorname{Sd}(R_a c)\in C_*(K';\mathbb Q).
\tag{D.15}
\]
Subdivision commutes with boundary by its simplex-coning proof, so (D.14) proves \(\partial\Psi=\Psi d_B\).

**Lemma D.4 — The two maps are chain homotopic.** Equations (D.12) and (D.15) induce the same homology map.

**Proof.** For a basis cochain \(\sigma^*\), both outputs are carried in the subdivided closed star of \(\sigma\). Formula (D.6) is carried there. In \(R_{\sigma^*}c\), every contributing top simplex contains \(\sigma\), and all its retained faces lie in that closed star. A closed star is a cone: it is \(\sigma*\operatorname{lk}\sigma\), and coning chains to any fixed vertex of \(\sigma\) gives an augmented contraction. Its subdivision has the same vanishing reduced homology, by the just-proved simplicial comparison, so every augmented cycle there can be filled.

Construct a homotopy \(H_q:B_q\to C_{q+1}(K')\) in increasing chain degree \(q\). In degree zero, \(\sigma\) is a top simplex. Its \(\Phi\)-value is \(\epsilon_\sigma[b_\sigma]\), because \(\gamma_n=1\). Its \(\Psi\)-value is \(\epsilon_\sigma[v_0]\), where \(v_0\) is that simplex's first vertex. The difference has augmentation zero and lies in its closed star, so fill it there to define \(H_0(\sigma^*)\).

Suppose the lower-degree homotopy is defined. For a degree-\(q\) basis cochain \(a=\sigma^*\), the residual
\[
\Phi(a)-\Psi(a)-H_{q-1}(d_Ba)
\]
is a \(q\)-cycle: applying boundary and the previously established homotopy identity cancels its first two derivatives, and \(d_B^2=0\) cancels the last remaining term. Each basis cochain in \(d_Ba\) is a coface \(\tau\) of \(\sigma\). Its closed star is contained in the closed star of \(\sigma\), so the entire residual is still carried in that contractible star. For \(q>0\) fill it there and use that filling as \(H_q(a)\). Extend linearly. This gives in every degree
\[
\Phi-\Psi=\partial H+H d_B.
\tag{D.16}
\]
The construction also covers the last degree, since a cycle above the star's dimension is zero and has the zero filling. ∎

The simplicial comparison used above preserves the cap formula exactly on affine simplex generators: restricting a singular cochain to their terminal faces is its simplicial cochain, and their retained front faces are the same affine simplices. It induces an isomorphism in cohomology by the rational coefficient theorem applied to the proved homology comparison. Thus every singular cohomology class can be compared through that restriction.

We also compare the two subdivision chain maps explicitly. Let \(J,J'\) send the chosen oriented simplex generators of \(K,K'\) to their affine singular simplices. The maps \(J'\operatorname{Sd}\) and \(\operatorname{Sd}_{\rm sing}J\) are chain maps carried in each original simplex and agree on augmentations. They can differ when the chosen order reverses a subdivided simplex, since a reversed singular parametrization is not literally the negative singular chain. Construct their homotopy on the original simplex basis in increasing dimension. In dimension zero their difference is zero. Having defined the homotopy on faces, subtract its value on the boundary from the difference on the current simplex. The residual is a cycle in that simplex: its boundary cancels by the already established face identity and \(\partial^2=0\). In positive dimension the standard-simplex augmented contraction proved in the Thom chapter fills it there. Use that filler as the homotopy value and extend linearly. Faces lie in the same original simplex, so every step has the stated carrier and the induction gives the full chain-homotopy identity. It preserves subcomplexes as well.

Singular subdivision is itself chain homotopic to the identity by the full prism/coning proof in the Thom chapter. Therefore \(J'\operatorname{Sd}\) and \(J\) induce the same homology map. Consequently (D.15) represents precisely the singular right cap with \([c]\). Lemmas D.3–D.4 prove an isomorphism for that actual map, rather than merely for a choice of groups with the same ranks.

**Theorem D.5 — Rational Poincaré and Lefschetz duality.** For a finite oriented rational homology \(n\)-manifold pair satisfying D.1's boundary conditions, right cap with (D.2) gives isomorphisms
\[
\begin{aligned}
H^p(K,M;\mathbb Q)&\xrightarrow{\cong}H_{n-p}(K;\mathbb Q),\\
H^p(K;\mathbb Q)&\xrightarrow{\cong}H_{n-p}(K,M;\mathbb Q).
\end{aligned}
\tag{D.17}
\]
The pairing
\[
H^{n-p}(K,M;\mathbb Q)\times H^p(K;\mathbb Q)
 \longrightarrow\mathbb Q,\qquad
(y,a)\longmapsto\langle y\smile a,[K,M]\rangle
\tag{D.18}
\]
is perfect. In particular, when \(M\) is empty this is the usual perfect closed Poincaré pairing.

**Proof of the remaining assertions.** All groups are finite dimensional: the finite simplicial chain complexes compute their singular homology, and the rational coefficient theorem computes cohomology as its vector-space dual. The first map of (D.17) was just proved. Its evaluation identity is
\[
\langle a,R_yc\rangle=\langle a\smile y,c\rangle.
\tag{D.19}
\]
Thus the pairing with factor order \(a,y\) is perfect. Graded commutativity switches it to (D.18) by the fixed invertible sign \((-1)^{p(n-p)}\).

For an absolute cocycle \(a\), (D.14) shows \(R_ac\) is a relative cycle modulo \(M\). Changing either representative changes it by a relative boundary, again by (D.14). Its evaluation against relative \(y\) is \(\langle y\smile a,c\rangle\). Relative cohomology is the full dual of relative homology, and (D.18) is perfect, so this second right-cap map is an isomorphism. This proves both its existence and its identification in (D.17). ∎

### D.4. The signature of a rational homology boundary

For a finite closed oriented rational homology \(4i\)-manifold \(F\), define \(\sigma(F)\) as the signature of the symmetric perfect form
\[
(x,y)\longmapsto\langle x\smile y,[F]\rangle
\quad\text{on }H^{2i}(F;\mathbb Q).
\tag{D.20}
\]
The finite-dimensional form proofs in [The signature theorem](multiplicative-sequences-and-the-signature-theorem.md), SectionA, apply over this same field. In dimension zero this is the signed point count. Use zero signature in dimensions not divisible by four, and for the empty space.

**Theorem D.6 — Boundary vanishing.** If \((K,M)\) is a finite oriented rational homology \((4i+1)\)-manifold with boundary as defined in D.1, then \(\sigma(M)=0\).

**Proof.** Put \(m=2i\), let \(j:M\to K\) be inclusion, and let
\(\delta:H^m(M;\mathbb Q)\to H^{m+1}(K,M;\mathbb Q)\)
be the pair connecting map. For \(x\in H^m(M;\mathbb Q)\), extend a representing cocycle to an absolute cochain \(X\) on \(K\). This can be done simplex by simplex, because boundary simplices are a subset of the singular-simplex basis. Then \(\delta X\) is a relative cocycle representing \(\delta x\). For an absolute cocycle \(A\) representing \(a\in H^m(K;\mathbb Q)\), the cup differential identity and (D.3) give
\[
\begin{aligned}
\langle\delta x\smile a,[K,M]\rangle
 &=\langle\delta(X\smile A),c\rangle\\
 &=\langle X\smile A,\partial c\rangle\\
 &=\langle x\smile j^*a,[M]\rangle.
\end{aligned}
\tag{D.21}
\]
Hence the image \(L=\operatorname{im}j^*\) is equal to its orthogonal complement in the perfect middle form on \(M\). One inclusion follows because \(\delta j^*=0\). For the other, if \(x\) pairs to zero with every \(j^*a\), (D.21) and the perfect relative–absolute pairing (D.18) imply \(\delta x=0\); the pair exact sequence then puts \(x\) in \(L\).

Nondegeneracy gives \(\dim L+\dim L^\perp=\dim H^m(M;\mathbb Q)\), so \(L=L^\perp\) is an isotropic half. The signature chapter's full diagonalization and isotropic-half proof, LemmaA.2, gives zero signature. This includes \(i=0\), when it says the induced signed boundary points sum to zero. Every step used the local homology and chain orientation conditions stated here, with no smooth collar assumption. ∎

## E. Finite PL refinements and relative approximation

A map of finite polyhedra is **piecewise linear**, abbreviated PL, if there are finite triangulations on which its restriction to each source simplex is affine in Euclidean realization coordinates. Changes of triangulation in this section are PL changes. A continuous homeomorphism is not assumed PL. In particular, the lemmas here do not by themselves prove smooth-compatible triangulation of a manifold.

### E.1. Refinements that make a PL map simplicial

**Lemma E.1 — Common refinements and map triangulation.** Two finite PL triangulations of the same polyhedron have a common subdivision. A single PL map of finite polyhedra can be made simplicial by subdivisions of its source and target, refining any prescribed finite PL subdivisions there.

**Proof.** Work first in a fixed finite Euclidean realization. Cut every simplex by the finitely many affine hyperplanes containing the facets of the simplices in either triangulation, including hyperplanes defining their lower-dimensional affine hulls. The nonempty intersections are convex polytopes. Take all of their faces, identifying a shared face only once. This gives a finite polyhedral complex subdividing both triangulations. Choose a point in the relative interior of every face and cone its already triangulated boundary to that point, in increasing face dimension. Convexity shows these cones cover the face with intersections exactly their shared faces. The choices are shared on the overlaps, so this produces a common triangulation.

For a PL identification between different realizations, cut first into its finitely many affine pieces and perform the same construction there and in their images. Pulling back target affine cuts is again an affine cut on a source piece. Thus the preceding argument applies to the common abstract polyhedron as well.

For a PL map \(f:P\to Q\), start with its affine source pieces and all their faces, and their convex image polytopes. Cut the target simplices by the affine hulls and facet hyperplanes of all these image polytopes. Then each image is a union of the resulting target cells. Cut each source piece by the inverse images of all these target cuts. The nonempty source cells \(A\) map onto target cells \(B\), including cells of smaller dimension: explicitly the cells are the nonempty intersections with \(f^{-1}(B)\), and each target cell included in an image has its full preimage there. A face of a cut source cell is an original source face further intersected with inverse images of target faces. Since the images of all original source faces were included among the cuts, its image is again a target cell. Include all source and target faces.

Choose the target interior point \(b_B\) in every target face \(B\). For each source face \(A\) with \(f(A)=B\), choose an interior point \(a_A\) with \(f(a_A)=b_B\). Such a point exists for a surjective affine map of convex polytopes. To see this directly, the average \(a_0\) of all source vertices is an interior point. Its image \(b_0\) is interior in \(B\), since an affine supporting functional attaining its minimum at \(b_0\) would attain that minimum at every source vertex and hence everywhere in \(B\). If \(b_0=b_B\) use \(a_0\). Otherwise, because \(b_B\) is interior, extend the segment from \(b_0\) through \(b_B\) a little to \(b_1\in B\). Lift \(b_1\) to \(a_1\in A\). Express \(b_B=(1-t)b_0+tb_1\) with \(0<t<1\); its lift \((1-t)a_0+ta_1\) is interior, since its positive \(a_0\) contribution keeps every defining nonconstant face inequality strict.

Triangulate both complexes by their face-chain cones at these chosen points. A nested source face chain maps to a weakly nested target face chain. Repeated image faces give repeated vertices and are simply removed from the image chain. Consequently each source simplex maps affinely to a target simplex, with its vertices sent to the chosen target vertices. This makes the actual map \(f\) simplicial, without altering its values.

The cutting construction can incorporate finitely many prescribed source and target PL subdivisions by using their common refinements at its start. This proves the stated single-map refinement assertion. ∎

**Lemma E.2 — The compatible prism triangulation.** Give the vertices of a finite complex \(P\) one total order. The prisms \(\sigma\times I\) have a compatible finite triangulation. For \(\sigma=[v_0,\ldots,v_p]\), its top simplices are
\[
[(v_0,0),\ldots,(v_j,0),(v_j,1),\ldots,(v_p,1)]
\quad(0\leq j\leq p).
\tag{E.1}
\]

**Proof.** If a point of the prism has source coordinates \(\lambda_i\) and height \(t\), choose \(j\) so that
\[
\sum_{i>j}\lambda_i\leq t\leq\sum_{i\geq j}\lambda_i.
\]
Use the lower vertices for \(i<j\), the upper vertices for \(i>j\), and split the coefficient \(\lambda_j\) between its two copies with upper part \(t-\sum_{i>j}\lambda_i\). This writes the point in the indicated simplex, with nonnegative coefficients summing to one. An equality at one of the inequalities is exactly its shared face with an adjacent prism simplex. Zero source coordinates give the same construction on a source face, because the order is inherited. Thus the prisms fit compatibly. ∎

We will also need a PL retraction
\[
P\times I\longrightarrow P\times\{1\}\ \cup\ A\times I
\tag{E.2}
\]
for a subcomplex \(A\subset P\). Here is its construction. Process the source simplices outside \(A\) in decreasing dimension. In the prism of a maximal remaining \(\sigma=[v_0,\ldots,v_p]\), remove the simplex with \(j=p\) in (E.1) together with its free bottom face. Then remove the simplex with \(j=p-1\) together with its now free face shared with the first one, and continue down to \(j=0\). The removed simplices leave exactly the top and side faces of this prism. The bottom face is free because its larger source cofaces outside \(A\) were already processed; no coface in \(A\) can contain a simplex outside \(A\). All intermediate shared faces are free for the same reason. After all source simplices have been processed, the remaining subcomplex is the union in (E.2).

Each elementary removal has a PL retraction. If a simplex \(T=v*\tau\) has free facet \(\tau\), its remaining faces are \(v*\partial\tau\). Insert an interior point \(b\) of \(\tau\), triangulate \(T\) by the cones with vertices \(v,b\) and a face of \(\partial\tau\), and send \(b\) to \(v\), fixing every vertex on \(v*\partial\tau\). This defines an affine map on each of those simplices onto the remaining faces, fixes those faces pointwise and thus glues to the identity outside \(T\). If \(\tau\) is a vertex, the same construction is just the constant map from its edge to the other vertex. A straight homotopy inside \(T\) is a deformation retraction fixing the remaining faces. Composing these finitely many PL retractions, with common refinements from Lemma E.1 when needed, proves (E.2). This is a proved finite PL homotopy-extension retraction, not a collar assumption on \(A\).

### E.2. Relative approximation and fixed-endpoint homotopies

**Lemma E.3 — Relative PL approximation.** Let \(P,Q\) be finite polyhedra and \(A\subset P\) a subpolyhedron. If \(F:P\to Q\) is continuous and its restriction to \(A\) is PL, then \(F\) is homotopic relative to \(A\) to a PL map agreeing there exactly with \(F\).

**Proof.** Choose triangulations with \(A\) a subcomplex. The full finite simplicial approximation proof in [Frame fields](frame-fields-and-primary-obstructions.md), LemmaA.1, supplies a simplicial approximation \(g\) and its straight homotopy from \(F\), after source subdivision. Its actual carrier property is that \(F(x)\) and \(g(x)\) lie together in a target simplex for every \(x\).

On \(A\), both endpoint maps \(F|_A\) and \(g|_A\) are PL. Refine \(A\) into polyhedral cells on which both maps are affine and each of their images lies in a single minimal target face. At a relative interior point of any such source cell, each affine image lies in the relative interior of its minimal image face: if a target vertex coordinate vanishes at an interior point, its nonnegative affine value vanishes on the entire cell. The carrier property therefore implies the two minimal image faces span a common target simplex. Both entire cell images lie in that simplex.

Triangulate these cells and use the prism triangulation (E.1). Send a bottom vertex to its \(F\)-value and a top vertex to its \(g\)-value, extending affinely on the prism simplices. The common carrier just proved keeps each image in \(Q\). This gives a PL homotopy
\[
b:A\times I\to Q,\qquad b_0=F|_A,\quad b_1=g|_A.
\]
It is homotopic relative to its endpoints to the original straight homotopy on \(A\): interpolate their values inside their shared target simplex on each source prism. These interpolations agree on common faces.

Define the PL map on \(P\times\{1\}\cup A\times I\) to be \(g\) on the first part and \(b\) on the second. They agree on the intersection. Compose with (E.2). Its restriction \(h\) to \(P\times\{0\}\) is PL and equals \(F\) on \(A\); the composite is a homotopy from \(h\) to \(g\) whose restriction to \(A\) is \(b\).

For clarity, the homotopy from \(F\) to \(h\) can be made relative to \(A\), not only unrestricted. The original homotopy \(F\to g\) can first be changed to have restriction exactly \(b\), fixing both endpoints: apply the already proved CW homotopy extension property to
\((P\times I,P\times\partial I\cup A\times I)\)
and the just-constructed interpolation on \(A\). Concatenate this modified homotopy with the reverse of \(h\to g\). On \(A\) it traverses \(b\) forward and backward. This loop of paths contracts to its constant initial value by continuously shortening the maximum parameter of \(b\), keeping its two endpoint values fixed. Apply homotopy extension to the same pair once more to extend this contraction. At its final stage the full homotopy \(F\to h\) is constant on \(A\). The homotopy-extension proof being used is the explicit disk-cylinder retraction in Frame fields, SectionE, (E.1), followed by its cellwise extension; every pair here is a finite CW pair after the prism triangulation. This proves the relative assertion. ∎

In particular, two homotopic PL maps \(f,g:P\to Q\) have a **PL homotopy with exactly those endpoints**. Apply Lemma E.3 to a continuous homotopy on \(P\times I\), with the subpolyhedron \(P\times\partial I\); its endpoint restrictions are already PL. Lemma E.1 can then make that homotopy simplicial, while retaining its endpoint subcomplexes and the actual endpoint maps. No redefinition of the homotopy classes at the ends is required.

### E.3. Moving points in a PL sphere

Our target sphere is the boundary of a \((k+1)\)-simplex, with its usual PL structure and positive orientation. Any subdivision or PL reparametrization represents the same finite polyhedron.

**Lemma E.4 — The point movement needed for generic fibres.** Let \(U_1,U_2\) be nonempty open subsets of this PL \(k\)-sphere, \(k\geq1\). There are points \(y_i\in U_i\) and an orientation-preserving PL homeomorphism \(u\) homotopic to the identity with \(u(y_1)=y_2\).

**Proof.** Choose \(y_i\) in the interiors of standard top-dimensional facets, since the union of these interiors is dense. Inside one such facet, small neighbourhoods have affine Euclidean charts. Distinct standard facets meet in a codimension-one face. At an interior point of that face, flatten their two adjacent half-simplex neighbourhoods linearly onto the opposite sides of a Euclidean hyperplane, using the same affine coordinates on the shared face. This is a PL chart. A path from \(y_1\) to \(y_2\) can therefore be chosen within the union of facet interiors and these codimension-one charts, crossing a shared face at an interior point. Cover this compact path by finitely many charts, and subdivide its parameter interval until each consecutive pair of points lies in one chart and in the interior of a convex polytope contained in that chart.

For two such points \(a,b\) inside a convex polytope \(B\), triangulate \(\partial B\), cone it first to \(a\) and then to \(b\), and send the cone vertex \(a\) to \(b\) while fixing the boundary vertices. Each cone simplex maps affinely to the corresponding cone simplex. Both conings cover \(B\) with the same boundary incidences, so this is a PL homeomorphism of \(B\), equal to the identity on its boundary. Extend it by the identity outside \(B\). Lemma E.1 provides a common refinement at that boundary, so the extension is PL on the sphere.

It is isotopic to the identity: replace \(b\) by \(a_t=(1-t)a+tb\) in the same cone formulas. Every \(a_t\) is interior in \(B\), so each stage is a homeomorphism and the family is continuous. This also shows it preserves orientation. Compose the finitely many such supported homeomorphisms along the chosen path. Their composition takes \(y_1\) to \(y_2\), is PL and is homotopic to the identity by concatenating their isotopies. ∎

The open-set formulation is enough: each generic fibre has a whole target simplex interior on which its oriented homeomorphism type is constant. It avoids assuming an unproved chart theorem for an arbitrary triangulated topological sphere. Only the stated standard PL sphere and its PL subdivisions are used.

## F. Fibre signatures and the stable-range L-class

Let \(K\) be a finite closed oriented rational homology \(n\)-manifold. Take the target \(S^k\) with its positive standard PL orientation, and put \(d=n-k\). A **generic value** of a PL map means a point outside the lower-dimensional skeleton of a target triangulation making that map simplicial. Such values form an open dense subset. The signature results below concern \(d=4i\); the fibre-dimension and orientation constructions also apply to other nonnegative \(d\).

### F.1. Induced orientation, including a homotopy boundary

**Lemma F.1 — Oriented generic fibres.** For a PL map \(f:K\to S^k\), a generic fibre \(F_y=f^{-1}(y)\) is a finite closed oriented rational homology \(d\)-manifold, or empty. The induced convention is **fibre first, target last**:
\[
\text{orientation of }K
 =\text{orientation of }F_y\ \times\
   \text{positive local orientation of }S^k.
\tag{F.1}
\]
For a PL homotopy \(h:I\times K\to S^k\) from \(f\) to \(g\), the generic fibre is a rational homology \((d+1)\)-manifold pair with boundary, oriented by the same convention using \(I\times K\). Its induced boundary is
\[
\partial h^{-1}(y)=g^{-1}(y)\ \sqcup\ (-f^{-1}(y)).
\tag{F.2}
\]

**Proof of the closed assertion and orientation.** Lemma E.1 makes \(f\) simplicial. Proposition A.3 supplies the finite polyhedron and its local rational homology. In a top source simplex that maps onto the target top simplex, the fibre polytope has dimension \(d\). Give it the ordinary linear orientation determined by (F.1). This rule can be checked in the actual product coordinates of Lemma A.1: reorder those coordinates to fibre first and target last, and use the relative cross product to remove the positive target local generator.

These top-polytope orientations induce coherent signs on their triangulations. Across an internal triangulation face they cancel by the ordinary boundary of an oriented convex polytope. A shared facet of two different fibre polytopes lies in a codimension-one source face which still maps onto the full target simplex. Indeed the defining positive vertex-group sums impose \(k\) independent affine conditions on that source face; its fibre has dimension \(\dim(\text{source face})-k\), so a \(d-1\) facet has source dimension \(n-1\). That face has two incident top source simplices. Their boundary orientation contributions cancel by the orientation cycle of \(K\).

In the product coordinates over the open target simplex, this is exactly the cancellation of the fibre facet contributions. The product boundary formula is
\[
\partial(a\times b)=(\partial a)\times b+(-1)^{|a|}a\times\partial b.
\tag{F.3}
\]
There is no local target boundary in its open simplex. Thus the first summands must cancel, with the same fibre-first convention on both sides. This proves the top fibre signs satisfy (D.2) with empty boundary. Lemma D.1 then shows their top cycle has a generator at every local point. It is the induced orientation in (F.1), not merely a sign choice on its smooth part.

For two values in the same target simplex interior, the fibre homeomorphism in (A.3) rescales the source coordinates in each vertex group by positive constants. Interpolating the positive target coordinates joins it to the identity in those product coordinates, so it preserves this induced orientation. It is affine on each fibre polytope. Therefore the oriented fibre type, and its signature when defined, is constant throughout that open simplex.

**Proof of the homotopy assertion.** The finite prism triangulation makes \(I\times K\) a polyhedron with its endpoint subcomplexes. Give it the ordered product orientation with \(I\) first. It has the rational homology boundary conditions of D.1. In its interior this follows from the interval version of Lemma A.2. At an endpoint the local interval pair
\(([0,\epsilon),[0,\epsilon)-\{0\})\)
has zero homology in every degree: both spaces are contractible and their nonempty inclusion induces the same \(H_0\). The relative chain product therefore makes every ordinary local homology group at an endpoint zero. Its endpoint subcomplexes are copies of \(K\) and have the required closed local homology. Formula (F.3) gives their fundamental cycle as \(K\) at time one minus \(K\) at time zero.

By Lemma E.1 make the actual homotopy simplicial, retaining its endpoint subcomplexes. Lemma A.1 preserves source support, so its local product homeomorphism also preserves these subcomplexes. The fibre meets them exactly in the endpoint fibres. At an interior fibre point, Lemma A.2 gives the closed local homology in dimension \(d+1\). At an endpoint fibre point, the same removal of the target local factor gives zero ordinary local homology in every degree. The endpoint fibres separately have the closed local homology of dimension \(d\), by Proposition A.3. Thus this fibre pair satisfies every boundary hypothesis of D.1.

The oriented top-polytope construction above applies now with ambient boundary. Every interior facet cancels; each boundary facet has one incident top polytope and carries its induced boundary sign. To check that sign, in a product orientation write the outward interval direction first, then the endpoint fibre tangent orientation, and then the target orientation. Removing the last target factor gives exactly the outward-first orientation of the fibre boundary. In \(I\times K\), the endpoint signs are \(+\) at one and \(-\) at zero. This proves (F.2). If endpoint fibres or the full fibre are empty the same statements hold with their zero cycles. ∎

### F.2. Independence of generic value and homotopy

**Theorem F.2 — Generic signature invariance (MS20.3–20.4).** Suppose \(d=4i\geq0\) and \(k\geq1\). The integer \(\sigma(f^{-1}(y))\) is the same for all generic values of any PL representative \(f\), independent of its PL triangulations and of its homotopy class representative. Denote it by \(\sigma(f)\). Every continuous map has a PL representative, so this defines an integer on continuous homotopy classes as well.

**Proof: equality at common generic values.** If PL maps \(f,g\) are homotopic, Lemma E.3 supplies a PL homotopy with the exact endpoints. Triangulate it and its endpoint subcomplexes. For every value generic for this common triangulation, Lemma F.1 gives the oriented rational homology boundary (F.2). Theorem D.6 and direct-sum additivity of the middle form give
\[
0=\sigma(h^{-1}(y)\text{ boundary})
 =\sigma(g^{-1}(y))-\sigma(f^{-1}(y)).
\tag{F.4}
\]
This proves the equality on an open dense set, before asserting constancy between different target simplices.

**Proof: constancy for one map.** Fix two target top-simplex interiors \(V_1,V_2\) for \(f\). Lemma F.1 makes the fibre signature constant on each, with respective values \(a_1,a_2\). By Lemma E.4 choose \(y_j\in V_j\) and an orientation-preserving PL homeomorphism \(u\), homotopic to the identity, taking \(y_1\) to \(y_2\). The map \(uf\) is PL and homotopic to \(f\). Its fibre signature on \(u(V_1)\) is \(a_1\), because its fibre sets are those of \(f\) at \(u^{-1}(y)\), and \(u\) preserves the last orientation factor in (F.1).

The intersection \(u(V_1)\cap V_2\) is a nonempty open neighbourhood of \(y_2\). Choose a point there avoiding all the finitely many lower-dimensional skeleta used to triangulate \(f\), \(uf\) and their PL homotopy. Their union has empty interior: each of its simplices has lower affine dimension in a top-dimensional target simplex, and finitely many such pieces cannot contain an open set. At the chosen point (F.4) gives \(a_1=a_2\). Thus every target simplex has the same generic signature.

The same common-generic-value argument now proves full homotopy invariance for two maps, using their established individual constancy. A further triangulation does not change any actual fibre or its orientation at a common generic point, so it does not change the integer. Every continuous map has a PL representative by the finite approximation lemma; two choices are continuously homotopic and hence have PL-homotopic representatives by Lemma E.3. This proves all assertions. ∎

The word generic is essential here. A fibre over a lower-dimensional target face need not have the closed local homology or the dimension required by (D.20).

### F.3. Additivity and the unique stable-range class

Assume now \(k\geq2\) and \(n<2k-1\), so Section C has constructed the abelian group \(\pi^k(K)\).

**Proposition F.3 — Signature is a cohomotopy homomorphism.**
\[
\sigma:\pi^k(K)\longrightarrow\mathbb Z
\tag{F.5}
\]
is a homomorphism when \(n-k=4i\).

**Proof.** Lift a pair of maps to the two-sphere wedge as in Lemma C.1. Choose a PL representative \(a:K\to S^k\vee S^k\) by finite approximation. Its two coordinate projections \(f',g'\) are PL representatives of the original maps; the wedge collapse and fold are PL on their standard sphere complexes. The fold composite represents their sum.

For \(y\) different from the wedge basepoint, its fold fibre is exactly the disjoint union of \(f'^{-1}(y)\) and \(g'^{-1}(y)\). On a neighbourhood of the first fibre the fold equals \(f'\), and on a neighbourhood of the second it equals \(g'\); the two sets are disjoint. The identities on the two positively oriented sphere copies make their induced orientations agree. Choose \(y\) also generic for all three maps, which is possible by avoiding their finite lower skeleta and the basepoint. The form of this disjoint union is their orthogonal direct sum. Therefore
\(\sigma(f'+g')=\sigma(f')+\sigma(g')\).
Homotopy invariance identifies these integers with the original classes. A constant map has an empty fibre at a generic value different from its image, so has signature zero. This proves (F.5). ∎

**Theorem F.4 — The stable-range rational L-class (MS20.6).** For
\[
4i<\frac{n-1}{2},
\tag{F.6}
\]
there is a unique class \(\ell_i(K)\in H^{4i}(K;\mathbb Q)\) satisfying
\[
\big\langle \ell_i(K)\smile f^*u,[K]\big\rangle
 =\sigma(f)
\quad\text{for every }f:K\to S^{n-4i}.
\tag{F.7}
\]
It is preserved by PL homeomorphisms.

**Proof.** Set \(k=n-4i\). Condition (F.6) is exactly \(n<2k-1\); it also ensures \(k\geq2\). Proposition F.3 and Corollary C.4 give a unique rational-linear functional \(\sigma_{\mathbb Q}\) on \(H^k(K;\mathbb Q)\) taking \(f^*u\) to \(\sigma(f)\). Theorem D.5's perfect closed pairing identifies the dual of this cohomology group with \(H^{n-k}(K;\mathbb Q)=H^{4i}(K;\mathbb Q)\). It gives the unique \(\ell_i\) in (F.7). In particular the proof uses all sphere-pullback classes spanning rational cohomology, rather than only some chosen maps.

For an orientation-preserving PL homeomorphism \(\lambda:K'\to K\), the actual fibre homeomorphism \(\lambda^{-1}(f^{-1}(y))\to f^{-1}(y)\) preserves the induced orientation. Hence its signature is equal, and \(\lambda_*[K']=[K]\). Pullback of (F.7) and uniqueness give \(\ell_i(K')=\lambda^*\ell_i(K)\).

Reversing the orientation on one component negates both its fundamental class and every fibre signature contribution from that component, so leaves the defining class unchanged. Maps and cohomology split over the finitely many components, and their fibre forms split as direct sums. Thus the same conclusion holds for any PL homeomorphism, with its componentwise orientation changes accounted for. ∎

This theorem is presently in the strict range (F.6). The extension to all indices by products with spheres, and comparison with smooth tangent L-classes, require the further arguments below.

### F.4. The generic fibre represents the pulled-back sphere class

The following identity supplies a useful compatibility for those arguments. It is also a check on the order in (F.1).

**Lemma F.5 — Fibre cap and evaluation.** For \(k\geq1\), \(d=n-k\geq0\), a PL map \(f\), and its oriented generic fibre inclusion \(j:F_y\to K\), one has
\[
j_*[F_y]=R_{f^*u}[K]\in H_d(K;\mathbb Q).
\tag{F.8}
\]
Consequently, for \(a\in H^d(K;\mathbb Q)\),
\[
\langle a\smile f^*u,[K]\rangle
 =\langle j^*a,[F_y]\rangle.
\tag{F.9}
\]

**Proof.** A positive generator of \(H^k(S^k,S^k-\{y\};\mathbb Q)\) maps to \(u\). The local cone/ball computation proves this: the corresponding positive local top homology generator is the restriction of the sphere fundamental class, so the coefficient theorem evaluates the relative generator as one on that restriction and its absolute image as one on the sphere. Pull it back to the pair \((K,K-F_y)\).

Excision restricts this pair near \(F_y\) to the open product of Lemma A.1, reordered as \(F_y\times V\), where \(y\in V\). The class is the last-factor local generator \(1\times u_y\). The relative fundamental class on this product is
\([F_y]\times\mu_y\), with \(\mu_y\in H_k(V,V-\{y\};\mathbb Q)\) positive. To verify this identification, relative chain products give
\[
H_n(F_y\times V,F_y\times(V-\{y\});\mathbb Q)
 \cong H_d(F_y;\mathbb Q)\otimes\mathbb Q\mu_y.
\]
The image of \([K]\) on this pair has the induced positive local values prescribed by (F.1). A top homology class of \(F_y\) is determined by its values at the interiors of its finitely many top simplices: its simplicial representative is a top cycle, with no chains above that degree, and each such local restriction detects that simplex's coefficient. The two indicated classes therefore agree. This verifies the relative fundamental comparison without a tubular-neighbourhood theorem.

Right cap by \(1\times u_y\) removes exactly the last factor and sends this relative product class to \([F_y]\) at a point of \(V\). Here is its sign check at chains. Use normalized singular cochains, whose comparison and Alexander–Whitney compatibility are proved in odd-prime LemmaG.1, a coefficient-independent normalization argument. In the shuffle cross product of a degree-\(d\) fibre simplex and a degree-\(k\) target simplex, the evaluated last \(k\) vertices project to a nondegenerate target simplex only for the shuffle with all fibre steps first and all target steps last. Every other projection has a repeated vertex and has zero value under the normalized \(u_y\). This remaining shuffle has sign \(+1\); its retained front face is the fibre simplex at the first target vertex. The local generator evaluates as one on \(\mu_y\). Moving that vertex to \(y\) inside the contractible \(V\) changes the fibre inclusion by a homotopy. Thus the resulting cap class is its fundamental class included at \(y\).

Cap naturality, excision's small-chain comparison, and the relative pullback show that this local computation gives exactly the absolute right cap \(R_{f^*u}[K]\) after inclusion in \(K\). If \(F_y\) is empty, the pullback relative class lives in the zero pair \((K,K)\), so both sides are zero. Finally evaluate \(a\) and use the already proved right-cap identity \(\langle a,R_bc\rangle=\langle a\smile b,c\rangle\). This gives (F.9). ∎

## G. Stabilization beyond the cohomotopy range

Section F defines \(\ell_i(K)\) only when \(4i<(n-1)/2\). We now prove an extension for every finite closed oriented rational homology manifold and every \(i\geq0\). The construction is independent of an auxiliary sphere's dimension and has the expected signature normalization.

Products of finite polyhedra are finite polyhedra: products of their simplices are convex polytopes, their intersections are common product faces, and face-chain coning gives a compatible finite triangulation. For \(K^n\times S^m\), a sphere chart and Lemma A.2 give the local rational homology in dimension \(n+m\). Its orientation is the ordered product orientation, with \(K\) first. The chain product and its boundary formula give its coherent top-simplex orientation and fundamental class
\[
[K\times S^m]=[K]\times[S^m].
\tag{G.1}
\]
This can also be checked by triangulating each oriented simplex product: the shuffle simplices cover it, interior facets cancel in pairs, and its boundary facets are exactly (F.3).

### G.1. A localized degree-one product map

**Lemma G.1 — Product suspension with the same generic fibre.** Let \(f:K^n\to S^k\) be PL, where \(k\geq1\), \(d=n-k\geq0\), and let \(m\geq1\). There is a PL map
\[
F:K\times S^m\longrightarrow S^{k+m}
\tag{G.2}
\]
for which
\[
F^*U=f^*u\times v,
\tag{G.3}
\]
with \(u,v,U\) the positive sphere generators. On a nonempty open subset of its target its fibres are oriented homeomorphic to a generic fibre of \(f\). In particular, if \(d\) is divisible by four then \(\sigma(F)=\sigma(f)\).

**Proof of the PL product map.** Choose a generic target simplex interior for \(f\), and a positive affine chart there. Choose also a positive chart of \(S^m\). Inside their ordered product chart choose two concentric homothetic \((k+m)\)-simplices, an inner \(D_0\) and an outer \(D_1\), with \(D_0\subset\operatorname{int}D_1\). Denote \(N=k+m\). Triangulate \(S^N\) as the boundary of an \((N+1)\)-simplex, and pick one facet \(T\), with the complement the cone \(b*\partial T\) from its opposite vertex \(b\).

Define \(q:S^k\times S^m\to S^N\) to take \(D_0\) affinely and positively onto \(T\), and the complement of \(\operatorname{int}D_1\) constantly to \(b\). On the annulus between the two homothetic simplices, use its face prisms: a face of \(D_0\) and its corresponding face of \(D_1\) bound a convex truncated cone, subdivided into the staircase simplices of its face prism. Send the inner face vertices to the corresponding vertices of \(\partial T\) and the outer face vertices to \(b\), and extend affinely on that subdivision. Each image lies in the corresponding cone face of \(b*\partial T\). The rules agree on common faces and on the two annulus boundaries. This defines a continuous PL map \(q\).

For completeness, that staircase subdivision gives genuine straight simplices in each truncated cone. Put the common centre at zero, write the inner scale as \(a\in(0,1)\), and normalize a chosen outer facet by its affine supporting equation \(\lambda(u)=1\), with \(\lambda\) linear. The projective map
\[
(u,t)\longmapsto \frac{a\,u}{1-(1-a)t}
\quad (u\text{ in that facet},\ 0\leq t\leq1)
\]
takes its ordinary prism bijectively onto the truncated cone between the scales \(a\) and \(1\). The denominator is positive. It takes lines to lines, and convex combinations to convex combinations with positive rescaled coefficients. Hence it takes each simplex in (E.1) onto the straight convex hull of its corresponding inner and outer vertices, preserving the common-face intersections and the covering. The inverse uses \(r=\lambda(x)\), \(u=x/r\) and \(t=(1-a/r)/(1-a)\), so is continuous. Use this map only to verify the straight triangulation; the definition of \(q\) is the affine vertex map on each resulting simplex. The same construction agrees on adjacent outer facets and their subfaces.

Every point of \(\operatorname{int}T\) has exactly one preimage under \(q\), in \(\operatorname{int}D_0\), with positive local orientation. Formula (F.9), applied to this map between equal-dimensional oriented manifolds with \(a=1\), gives
\(\langle q^*U,[S^k\times S^m]\rangle=1\).
Field Künneth makes \(H^{k+m}(S^k\times S^m;\mathbb Q)\) the one-dimensional space generated by \(u\times v\), whose evaluation on the product fundamental class is one. Hence
\[
q^*U=u\times v.
\tag{G.4}
\]

Set \(F=q(f\times1)\). It is PL by common refinements of its finitely many affine pieces. Pulling back (G.4) gives (G.3). For \(z\in\operatorname{int}T\), write its unique preimage as \((y,t)\) in \(D_0\). Then
\[
F^{-1}(z)=f^{-1}(y)\times\{t\}.
\]
All such \(y\) lie in the one chosen generic simplex interior for \(f\). The derivative of the affine \(D_0\to T\) preserves the ordered target orientation \(S^k,S^m\). With the product source ordered \(K,S^m\), the fibre-first convention has factor order \(F_y,S^k,S^m\), so its fibre orientation is exactly that of \(f^{-1}(y)\). Thus these fibres have the asserted oriented type. Theorem F.2's established generic constancy supplies the signature statement after avoiding any additional skeleton from a triangulation of the composite. ∎

### G.2. Restriction of stable-range classes

**Lemma G.2 — Restriction under a sphere factor.** Suppose a finite closed rational homology manifold \(P^N\) satisfies \(4i<(N-1)/2\), and \(s\geq1\). If \(j:P\to P\times S^s\) includes any slice, then
\[
j^*\ell_i(P\times S^s)=\ell_i(P).
\tag{G.5}
\]
If \(s>4i\), the stronger identity is
\[
\ell_i(P\times S^s)=\operatorname{pr}_P^*\ell_i(P).
\tag{G.6}
\]

**Proof.** Both spaces are in the strict range. Field Künneth decomposes the larger class uniquely as
\[
\ell_i(P\times S^s)=\alpha\times1+\beta\times v_s,
\]
where \(\alpha\in H^{4i}(P;\mathbb Q)\), and
\(\beta\in H^{4i-s}(P;\mathbb Q)\); a negative degree means zero. The slice restriction is \(\alpha\), independently of its point since the sphere is path connected.

Put \(k=N-4i\). For every PL \(f:P\to S^k\), Lemma G.1 gives the product map \(F:P\times S^s\to S^{k+s}\), with pullback \(f^*u\times v_s\) and the same signature. Equation (F.7) on the larger product therefore gives
\[
\begin{aligned}
\sigma(f)
 &=\big\langle(\alpha\times1+\beta\times v_s)
          \smile(f^*u\times v_s),[P]\times[S^s]\big\rangle\\
 &=\langle\alpha\smile f^*u,[P]\rangle.
\end{aligned}
\tag{G.7}
\]
The \(\beta\) term is zero since \(v_s^2=0\) for positive-dimensional spheres. The other term has no cup/external-product sign: its first class has sphere degree zero. The positive \(v_s\) evaluates as one. Theorem F.4's uniqueness now forces \(\alpha=\ell_i(P)\), proving (G.5). If \(s>4i\), the group for \(\beta\) is zero, giving (G.6). ∎

### G.3. Choice independence and normalization

For arbitrary \(K^n\) choose a positive integer \(m\) with
\[
m>4i,\qquad 4i<\frac{n+m-1}{2}.
\tag{G.8}
\]
Such integers exist. Field Künneth says that projection gives an isomorphism
\[
H^{4i}(K;\mathbb Q)\xrightarrow{\cong}
 H^{4i}(K\times S^m;\mathbb Q)
\]
because its other sphere summand has degree \(4i-m<0\). Define the unrestricted \(\ell_i(K)\) to be the slice pullback of the already constructed strict-range class on this product.

**Theorem G.3 — Stabilized rational L-classes.** This definition is independent of \(m\), the slice point and the positive sphere triangulation. It agrees with Theorem F.4 wherever that theorem applies, is preserved by PL homeomorphisms, and has
\[
\ell_0(K)=1,\qquad \ell_i(K)=0\quad(4i>n).
\tag{G.9}
\]
For a finite closed oriented rational homology \(4i\)-manifold,
\[
\langle\ell_i(K),[K]\rangle=\sigma(K).
\tag{G.10}
\]

**Proof of choice independence.** Slice point independence follows from path homotopy in the sphere. Let \(m,m'\) be two integers satisfying (G.8), and let \(\alpha_m,\alpha_{m'}\) be their slice classes. On
\(K\times S^m\times S^{m'}\),
apply (G.6) first with base \(K\times S^m\), which is in strict range, and added sphere \(S^{m'}\), whose dimension exceeds \(4i\). Its class is
\(\operatorname{pr}_K^*\alpha_m\).
Apply it instead with base \(K\times S^{m'}\) and added sphere \(S^m\). Swapping the two sphere factors is a PL homeomorphism. Theorem F.4's orientation-independent PL invariance identifies the second ordered product's class with that of the first, even when the swap changes the product orientation by \((-1)^{mm'}\). Its class is therefore also
\(\operatorname{pr}_K^*\alpha_{m'}\).
Restrict to any \(K\)-slice in the double product to obtain \(\alpha_m=\alpha_{m'}\).

Lemma G.2 gives agreement with the strict-range class if the base \(K\) itself lies in that range. Changing a sphere's PL triangulation or applying a PL homeomorphism to \(K\) gives a product PL homeomorphism; Theorem F.4 and pullback to slices show invariance. Thus all indicated choices have been removed.

**Proof of the zero and unit assertions.** The degree vanishing in (G.9) follows from the finite simplicial cohomology complex of dimension \(n\). For a strict-range base of dimension \(N\) and \(i=0\), the target dimension is \(N\). Its generic fibres are signed zero-manifolds. Lemma F.5, evaluated with \(a=1\), says their signed count is \(\langle f^*u,[K]\rangle\). This is their signature by (D.20). The unique class of Theorem F.4 is consequently the degree-zero unit \(1\). Apply this to a product satisfying (G.8) and pull back to \(K\) to obtain \(\ell_0(K)=1\), also in dimensions zero and one.

**Proof of the top normalization.** When \(n=4i\), choose \(m>4i+1\). The product lies in the strict range. Its projection to \(S^m\) has generic fibre \(K\) with its original orientation, because the source order is \(K,S^m\). Equation (F.7) gives
\[
\big\langle\operatorname{pr}_K^*\ell_i(K)
      \smile\operatorname{pr}_{S^m}^*v,
      [K]\times[S^m]\big\rangle
 =\sigma(K).
\]
The first factor is pulled back from \(K\) by (G.8), and \(v\) evaluates as one. Product evaluation proves (G.10). Disconnected spaces and signed zero-dimensional components are included because the forms and fundamental classes split over their components. ∎

**Corollary G.4 — The fibre formula beyond the strict range.** For every PL \(f:K^n\to S^{n-4i}\) with \(n-4i\geq1\), the unrestricted class satisfies (F.7).

**Proof.** Choose \(m\) satisfying (G.8). Apply Lemma G.1 to \(f\); the larger product lies in strict range, so its defining pairing evaluates to \(\sigma(f)\). Its L-class is \(\operatorname{pr}_K^*\ell_i(K)\) by the definition and Künneth. Equation (G.3) and product evaluation reduce that pairing to the left side of (F.7) on \(K\). ∎

Finally define rational combinatorial Pontryagin classes recursively by
\[
\mathfrak p_j(K)
 =c_j^{-1}\bigl(\ell_j(K)
       -R_j(\mathfrak p_1(K),\ldots,\mathfrak p_{j-1}(K))\bigr),
\tag{G.11}
\]
where \(c_j>0\) and \(R_j\) are proved in Lemma B.1. All terms have degree \(4j\), the recursion is unique, and every operation is rational cohomology addition or multiplication. Theorem G.3 therefore makes these classes PL invariants. Their identification with \(p_j(TK)\) when the PL space comes from a smooth manifold uses the smooth comparison theorem proved in [the comparison companion](smooth-fibres-triangulation-comparison-and-lens-spaces.md), with existence supplied in [the triangulation companion](smooth-triangulations-and-the-integral-pl-obstruction.md). No topological-homeomorphism invariance is asserted here.

## H. Six graded exercises with solutions

**Exercise H.1 — Easy: an actual fibre polytope.** Map the six vertices of \(\Delta^5\) to the vertices \(w_0,w_1,w_2\) of \(\Delta^2\), in groups of sizes \(2,3,1\). Describe the fibre over \(y=t_0w_0+t_1w_1+t_2w_2\), with every \(t_j>0\). Write the homeomorphism between its fibre and the fibre at another such \(y'\). Explain why replacing the target open simplex by its closed simplex would invalidate the product assertion.

**Solution.** The source barycentric coordinates in the three groups have respective fixed sums \(t_0,t_1,t_2\). Each group is a scaled simplex, giving the product
\[
t_0\Delta^1\times t_1\Delta^2\times t_2\Delta^0.
\]
Its dimension is \(1+2+0=3=5-2\). To change to \(y'\), multiply each coordinate in group \(j\) by \(t'_j/t_j\). These positive multipliers preserve the source support and all face incidences, and the inverse multipliers give the inverse homeomorphism.

At the target vertex \(w_0\), the second and third sums become zero. Its fibre is just \(\Delta^1\), with dimension one. It is not homeomorphic to the three-dimensional product at an interior value. Thus a product over the entire closed target simplex would have unequal fibre types. The positive denominators and the open-simplex qualification in Lemma A.1 have real content.

**Exercise H.2 — Easy: the strict range and its repair.** For \(i=1\), does Theorem F.4 apply in dimensions \(n=9\) and \(n=10\)? For an arbitrary \(K^n\), express the two integer requirements on the auxiliary sphere dimension in (G.8). Find the least permitted \(m\) for \(n=4\), \(i=1\).

**Solution.** At \(n=9\), the inequality is \(4<4\), which fails. At \(n=10\), it is \(4<9/2\), which holds. In integer form (G.8) is
\[
m\geq4i+1,\qquad n+m\geq8i+2.
\]
Hence the least positive integer allowed is
\(\max(1,4i+1,8i+2-n)\).
For \(n=4,i=1\), this is \(\max(1,5,6)=6\). The resulting product has dimension ten and the positive cohomology degree four is smaller than the sphere dimension six, exactly the two facts used in stabilization.

**Exercise H.3 — Medium: a torsion kernel is sufficient.** Let \(A\) be an abelian group, \(V\) a rational vector space, and \(h:A\to V\) a homomorphism inducing \(A\otimes\mathbb Q\cong V\). Prove that every homomorphism \(s:A\to\mathbb Z\) has a unique rational-linear extension to \(V\). Does this hypothesis alone imply that \(\ker h\) is finite?

**Solution.** If \(a\) is torsion, then \(s(a)\) is torsion in \(\mathbb Z\), hence zero. Localizing \(s\) therefore gives the well-defined map \(A\otimes\mathbb Q\to\mathbb Q\), with \(a/d\mapsto s(a)/d\). Transport it across the given isomorphism. The elements \(h(a)/d\) span \(V\), so the extension is unique.

For a direct verification, an equality \(h(a)/d=h(b)/e\) says \(ea-db\) has zero rationalization. Localization says some nonzero integer kills it, so \(s(ea-db)=0\); the prescribed rational values agree. No finiteness of the torsion subgroup was used.

Take \(A=\mathbb Z\oplus\bigoplus_{j\geq1}\mathbb Z/2\) and \(h(a,t)=a\in\mathbb Q\). Then \(A\otimes\mathbb Q\cong\mathbb Q\), but the kernel is the infinite direct sum of order-two groups. This shows exactly why rational comparison proves the sufficient torsion-kernel assertion without proving a finite kernel.

**Exercise H.4 — Medium: inspect the dual chains on a circle.** Orient the boundary of \([0,1,2]\) by
\[
c=[1,2]-[0,2]+[0,1].
\]
Compute the three vertex dual chains \(z_0,z_1,z_2\) in (D.6). Verify (D.7) at vertex zero and identify the sum of their phased chains with positive subdivision of \(c\).

**Solution.** Write \(b_i\) for a vertex barycentre and \(b_{ij}\) for an edge barycentre. The incidence of its initial vertex in an increasing ordered edge is \(-1\), and that of its terminal vertex is \(+1\). Thus
\[
\begin{aligned}
z_0&=-[b_0,b_{01}]+[b_0,b_{02}],\\
z_1&=[b_1,b_{01}]-[b_1,b_{12}],\\
z_2&=-[b_2,b_{02}]+[b_2,b_{12}].
\end{aligned}
\]
Their respective edge dual zero-chains are
\(z_{01}=[b_{01}]\), \(z_{02}=-[b_{02}]\), and
\(z_{12}=[b_{12}]\).
At vertex zero,
\[
\partial z_0=-[b_{01}]+[b_{02}]
 =[01:0]z_{01}+[02:0]z_{02},
\]
as required.

For \(n=1,p=0\), (D.11) gives \(\gamma_0=-1\). Hence \(-z_0-z_1-z_2\) is the sum of the paths
\([b_0,b_{01}]-[b_1,b_{01}]\),
\(-[b_0,b_{02}]+[b_2,b_{02}]\), and
\([b_1,b_{12}]-[b_2,b_{12}]\).
Each is the positive subdivision of its signed original edge: the second segment of an increasing edge is the negative of the reversed segment from its terminal vertex to its barycentre. Their sum is therefore \(\operatorname{Sd}c\). This verifies the global orientation phase as well as the local incidence.

**Exercise H.5 — Medium: boundary duality in dimension one.** For the positive interval \(W=[0,1]\), describe its induced boundary middle form, the restriction image \(L\subset H^0(\partial W;\mathbb Q)\), and \(L^\perp\). Verify its zero signature directly. Explain why this does not say that every boundary cohomology class extends.

**Solution.** In the basis given by the points zero and one, the boundary fundamental cycle is \([1]-[0]\). The cup-evaluation form is
\[
b((x_0,x_1),(y_0,y_1))=-x_0y_0+x_1y_1.
\]
The interval's degree-zero classes are constants, so restriction has image
\(L=\mathbb Q(1,1)\).
A vector \((x_0,x_1)\) is orthogonal to this image exactly when
\(-x_0+x_1=0\), giving \(L^\perp=L\). It is an isotropic one-dimensional half of the nondegenerate two-dimensional form. Its diagonal entries \(-1,1\) give signature zero directly. A class such as \((1,0)\) is not constant and does not extend; the connecting map detects precisely that failure. This is the lowest-dimensional case of (D.21).

**Exercise H.6 — Hard: stabilization and recursive Pontryagin recovery.** Reprove independence of the two sphere dimensions \(m,m'\) in (G.8), accounting for the orientation of their interchange. Then express \(\mathfrak p_1,\mathfrak p_2\) in terms of \(\ell_1,\ell_2\). State what further theorem is needed to identify these formal PL invariants with smooth tangent Pontryagin classes.

**Solution.** Both \(K\times S^m\) and \(K\times S^{m'}\) lie in strict range, and both sphere dimensions exceed \(4i\). Lemma G.2 on the double product gives its L-class as the pullback of the class on \(K\times S^m\), and hence as \(\operatorname{pr}_K^*\alpha_m\). Applying the same lemma with the two spheres interchanged gives \(\operatorname{pr}_K^*\alpha_{m'}\). The sphere interchange is PL and changes the ordered product orientation by \((-1)^{mm'}\). Theorem F.4 is independent of orientation choice, because changing a component orientation negates both sides of its defining fibre-signature pairing. It therefore identifies the two larger classes despite that sign. Pullback to a \(K\)-slice gives \(\alpha_m=\alpha_{m'}\).

The proved first multiplicative-sequence formulas give
\[
\ell_1=\frac{\mathfrak p_1}{3},\qquad
\ell_2=\frac{7\mathfrak p_2-\mathfrak p_1^2}{45}.
\]
Solving them, in order, yields
\[
\mathfrak p_1=3\ell_1,\qquad
\mathfrak p_2=\frac{45\ell_2+9\ell_1^2}{7}.
\]
The denominator seven is legitimate over \(\mathbb Q\). Lemma B.1 gives the analogous invertible leading coefficient in every degree, so this recursion always works. Their identification with \(p_j(TM)\) uses the smooth comparison
\(\ell_j(K)=t^*L_j(p(TM))\)
for a compatible smooth triangulation \(t:K\to M\), proved in [the comparison companion](smooth-fibres-triangulation-comparison-and-lens-spaces.md). [the triangulation companion](smooth-triangulations-and-the-integral-pl-obstruction.md) supplies existence in the stated smooth scope. Formal inversion and PL invariance alone would not establish that comparison.

## I. The construction for a homology manifold with boundary

Let \((K,M)\) be a finite oriented rational homology \(n\)-manifold pair with the full boundary conditions of Lemma D.1. In particular, \(M\) is its rational homology \((n-1)\)-manifold boundary, and \([K,M]\) is the coherent relative fundamental class constructed there. We give the relative extension mentioned in Milnor's 1957 notes, Chapter XVI, Section 4.

### I.1. Relative sphere maps

For \(k\geq2\) and \(n<2k-1\), let \(\pi^k(K,M)\) be homotopy classes of maps
\[
f:(K,M)\longrightarrow(S^k,*),
\]
with homotopies fixed at the basepoint on \(M\). This is a natural abelian group, and pullback of the positive sphere generator gives a natural isomorphism
\[
\pi^k(K,M)\otimes\mathbb Q
 \xrightarrow{\cong}H^k(K,M;\mathbb Q).
\tag{I.1}
\]

**Proof.** Collapsing the subcomplex \(M\) gives a finite CW complex \(K/M\) of dimension at most \(n\), with the collapsed point as basepoint. If \(M\) is empty, use \(K\) with a disjoint basepoint instead. Maps and homotopies of the indicated pairs are exactly based maps and based homotopies of this quotient. Its positive reduced cohomology is the relative cohomology: the quotient cellular complex consists of the cells outside \(M\), with precisely the relative attaching incidences. The full simplicial/singular cellular comparison in Section C identifies this calculation with singular relative cohomology.

Every step of C.1–C.3 permits fixing the source basepoint. The relative wedge comparison therefore gives the abelian group; the factorial telescope and the cellular cocycle classification give (I.1), with the same pulled-back generator, rather than an unspecified vector-space isomorphism. Homotopy extension at the quotient basepoint supplies the based homotopies used in that argument. All of these constructions commute with maps of pairs. ∎

### I.2. The relative fibre functional

Suppose \(i\geq0\), \(k=n-4i\geq2\), and \(n<2k-1\). A PL map of pairs as above has a closed oriented rational homology \(4i\)-manifold as its fibre over every generic value away from \(*\), or an empty fibre. Its signature defines a homomorphism
\[
\sigma_i:\pi^k(K,M)\longrightarrow\mathbb Z.
\tag{I.2}
\]
There is a unique class \(\ell_i(K,M)\in H^{4i}(K;\mathbb Q)\) satisfying
\[
\langle \ell_i(K,M)\smile f^*u,[K,M]\rangle
 =\operatorname{sign}f^{-1}(y).
\tag{I.3}
\]
The notation records the boundary pair; the class itself is in absolute cohomology.

**Proof.** Use E.3 to make any continuous pair map PL while keeping its boundary value fixed. The generic fibre avoids \(M\), and is compact because \(K\) is compact. At each of its points the ambient local homology is the interior copy of \(\mathbb Q[n]\). The exact product calculation A.1–A.3 gives its local homology in degree \(4i\). Orient its top polytopes with the fibre-first, target-last convention of F.1; the ambient relative fundamental chain supplies the same coherent signs at every interior point.

For a pair homotopy, the vertical boundary \(I\times M\) maps to the basepoint. Thus a generic fibre in \(I\times K\) misses that vertical boundary. Its only boundary is the terminal fibre minus the initial fibre, with the order and orientations of F.1. The full local boundary calculation and Theorem D.6 give equal endpoint signatures. E.3 provides the required PL homotopy relative to the fixed boundary.

To compare two generic values, choose the target-point isotopy in E.4 inside \(S^k-\{*\}\). This is possible because that punctured sphere is connected and has the same local convex charts used in E.4; a compact path can be covered by finitely many smaller chart balls avoiding \(*\). The resulting PL homeomorphism is the identity at \(*\), has positive orientation and is homotopic to the identity while fixing \(*\). The common-generic-value argument of F.2 now applies to maps of pairs. It proves value independence, as well as independence of subdivisions and representatives.

The wedge lift can also be chosen relative to \(M\). Away from the wedge point, the folded generic fibre is the oriented disjoint union of its two coordinate fibres. Signature is their sum. A constant map has empty such fibre. This proves (I.2).

A homomorphism to \(\mathbb Z\) kills torsion, so (I.1) extends this functional uniquely to \(H^k(K,M;\mathbb Q)\). The perfect absolute/relative pairing of Theorem D.5 represents it by exactly one absolute degree-\(4i\) class. This is (I.3). Reversing an ambient component orientation reverses both its fibre signatures and \([K,M]\); hence the class is independent of that orientation choice. PL homeomorphisms of boundary pairs preserve the construction by pulling back the pair maps and the local orientations. ∎

### I.3. Stabilization and the relative cap formula

The relative construction extends uniquely to every dimension by the same sphere stabilization:
\[
\ell_i(K,M)=j^*\ell_i(K\times S^s,M\times S^s),
\qquad s>4i,\quad n+s\geq8i+2.
\tag{I.4}
\]
Here \(j(x)=(x,z)\) for any fixed sphere point. This expression is independent of \(s\), \(z\), subdivisions and the chosen orientations. It agrees with Section G when \(M\) is empty. For \(n-4i\geq1\), every PL pair map to \(S^{n-4i}\) satisfies the unrestricted fibre identity (I.3). Its fibre class is characterized by
\[
f^*u\frown[K,M]=[f^{-1}(y)]
 \quad\hbox{in }H_{4i}(K,M;\mathbb Q),
\tag{I.5}
\]
where the right side is the image of the closed fibre's fundamental class.

**Proof.** First compare a strict-range pair and its product with \(S^s\), \(s\geq1\). Choose the supported degree-one product map of G.1 so that its support lies in a ball disjoint from \(\{*\}\times S^s\). Composing it with \(f\times1\) gives a pair map: the entire new boundary still maps to the basepoint. A generic value in its positive target facet has exactly the same oriented fibre as \(f\). Its pulled-back generator is \(f^*u\times v\), with \(v[S^s]=1\). The relative external-chain product, followed by the rational coefficient theorem, gives the relative Künneth decomposition. The corresponding absolute decomposition writes the product L-class as
\[
\alpha\times1+\beta\times v,
\qquad
\alpha\in H^{4i}(K;\mathbb Q),\quad
\beta\in H^{4i-s}(K;\mathbb Q).
\]
Evaluation against every class \(f^*u\times v\) gives \(\alpha=\ell_i(K,M)\), using (I.1), (I.3) and the perfect pairing. If \(s>4i\), the group containing \(\beta\) is zero. Thus in that case the full product class is the pullback of the original class.

For two allowed dimensions \(s,s'\), apply this product calculation to the double product and then restrict to a \(K\)-slice. Interchanging the spheres changes the ordered orientation by \((-1)^{ss'}\); orientation independence in I.2 cancels this sign. Both restrictions coincide, proving independence in (I.4). Changing \(z\) is a homotopy of slice inclusions. If the original pair was already in strict range, the same calculation proves agreement with I.2. Empty boundary recovers the identical closed construction.

For a map below strict range, use the supported product map with \(s\) as in (I.4). Its unchanged generic fibre and generator \(f^*u\times v\) give (I.3) after product evaluation. Degree \(4i>n\) gives the zero class automatically; \(i=0\) gives the unit by the signed zero-dimensional fibre count. No sphere map of degree zero is needed for either statement.

For (I.5), take a small target ball at \(y\) disjoint from the basepoint. The relative sphere generator pulls back to the supported class on \((K,K-f^{-1}(y))\). Since \(M\subset K-f^{-1}(y)\), it also determines the given class in \(H^k(K,M)\). The local product and normalized shuffle calculation in F.5 take cap with the ambient local generator to the positive fibre generator. Their signs are the same fibre-first, target-last signs; the boundary is outside the support. Coherence of the relative fundamental chain identifies these local generators with the fibre's fundamental class. Finally the natural map to \(H_{4i}(K,M)\) gives (I.5). ∎

## J. Local chains from oriented links

Gaifullin's local-formula approach uses the combinatorial link at each simplex. We prove its chain criterion directly. In this section a **combinatorial manifold** has sphere links, with the indicated compatible PL orientations; this is a more specific input than the rational homology manifolds of Sections A–I. Include the empty face in simplicial joins and use augmented chains when describing their orientations.

### J.1. The complex of oriented links

For \(q\geq1\), let \(T_q\) be the abelian group generated by oriented combinatorial \((q-1)\)-spheres, modulo orientation-preserving isomorphism and
\[
[-L]=-[L].
\]
Put \(T_0=\mathbb Z\), with the oriented empty sphere as its generator. The vertex-link differential and oriented join are
\[
\partial_T[L]=\sum_{v\in V(L)}[\operatorname{lk}_L v],
\qquad [L][R]=[L*R].
\tag{J.1}
\]
For \(q=1\) the first expression is zero: the two points of the oriented zero-sphere have opposite empty-link signs. These operations are well defined and obey
\[
\partial_T^2=0,\qquad
[L][R]=(-1)^{qr}[R][L],\qquad
\partial_T([L][R])=(\partial_T[L])[R]+(-1)^q[L]\partial_T[R]
\tag{J.2}
\]
when \(L\) and \(R\) have degrees \(q,r\).

**Proof.** Encode the sphere orientation by its coherent augmented top cycle. For an oriented simplex \(\sigma\), orient its link so that concatenating the ordered vertices of \(\sigma\) and a top link simplex has the ambient top-simplex sign. Isomorphisms preserve this rule; reversing the ambient orientation reverses every induced link orientation. Thus (J.1) respects the defining relations.

In the double differential, each edge with vertices \(v,w\) contributes the link obtained first at \(v\), then at \(w\), and the link obtained in the reverse order. Their concatenations differ by the transposition of \(v,w\), so the induced orientations are opposite and the two terms cancel. At the last augmented degree, the empty-link signs give the same cancellation. This proves \(\partial_T^2=0\).

Concatenating the top cycles orients a join. To check that it is a PL sphere, first use the given PL sphere identifications in the two factors; joining their simplicial refinements gives a PL identification with the join of two simplex boundaries. Realize those simplices \(P,Q\) about the origin in complementary vector spaces. If \(\mu_P,\mu_Q\) are their piecewise linear gauges, their convex free sum is
\[
R=\{(x,y):\mu_P(x)+\mu_Q(y)\leq1\}.
\]
The boundary is the join: a join point with parameter \(t\) and boundary points \(a,b\) maps to \((ta,(1-t)b)\). On each join of boundary facets this map is affine in the join barycentric coordinates, and its inverse is unique except at the two collapsed ends, exactly as in the definition of a join. Hence it is a PL homeomorphism.

For completeness, the boundary of \(R\) is PL homeomorphic to the boundary of a simplex containing the same origin. Intersect their finite face cones to form a common polyhedral fan, then triangulate that fan compatibly by choosing one interior ray in every face cone and using its face chains. Cut each simplicial cone by the two polytope boundaries. Each cut is a simplex in its containing facet, with corresponding vertices on the same rays. Map those vertices to each other and extend affinely. The simplices cover both boundaries, their intersections are their common faces, and the inverse uses the same face data. This is the required PL homeomorphism. Thus the join is a combinatorial sphere.

Concatenation is associative, with the empty sphere as unit. Swapping the two ordered vertex blocks has sign \((-1)^{qr}\), because their respective lengths are \(q,r\). This proves supercommutativity.

A vertex of \(L\) has link \((\operatorname{lk}_L v)*R\) with that ordered orientation. For a vertex of \(R\), moving its first vertex past the \(q\) vertices of a top \(L\)-simplex gives the sign \((-1)^q\); its link is \(L*(\operatorname{lk}_R v)\) with that sign. Summing these two sets of vertices gives the Leibniz identity. The opposite signs at the two vertices of a zero-sphere also verify the degree-one edge case. ∎

Set \(T^q=\operatorname{Hom}(T_q,\mathbb Q)\), and define
\[
(\delta f)([L])=(-1)^q\sum_{v\in V(L)}f([\operatorname{lk}_L v]).
\tag{J.3}
\]
Then \(\delta^2=0\) by (J.2). If a sphere has an orientation-reversing automorphism, its generator satisfies \(2[L]=0\), so every rational-valued \(f\) vanishes on it. Dualizing the join gives a bilinear functional on \(T_q\times T_r\), that is, an element of \(\operatorname{Hom}(T_q\otimes T_r,\mathbb Q)\). This target is available without a finite-generation assumption.

### J.2. The exact local-chain criterion

For a closed oriented combinatorial \(m\)-manifold \(K\) and \(f\in T^q\), \(q\geq1\), \(m\geq q\), define
\[
f_\sharp(K)=\sum_{\dim\sigma=m-q}
 f([\operatorname{lk}_K\sigma])\,\sigma.
\tag{J.4}
\]
Orient each \(\sigma\) arbitrarily, with the induced link orientation of J.1. Changing that orientation changes both factors' signs, so the summand is unambiguous. The chain identity, with these explicit conventions, is
\[
\partial f_\sharp(K)=(-1)^m(\delta f)_\sharp(K).
\tag{J.5}
\]
In particular, \(f_\sharp(K)\) is a cycle for every such \(K\) if and only if \(\delta f=0\). For \(q\geq2\), changing \(f\) by a coboundary changes every cycle by a boundary, and hence gives the same cohomology class under Poincaré duality.

**Proof.** Put \(d=m-q\). For \(d\geq1\), fix an oriented \((d-1)\)-simplex \(\tau\). Its \(d\)-dimensional cofaces are \(\sigma=\tau\cup\{v\}\), indexed by the vertices of \(\operatorname{lk}_K\tau\). Let \(\epsilon=[\sigma:\tau]\). With \(\sigma\) ordered as \([v,\tau]\), \(\epsilon=1\). Moving \(v\) through the \(d\) vertices of \(\tau\) compares \([v,\tau,\rho]\) with \([\tau,v,\rho]\). Therefore, in general,
\[
[\operatorname{lk}_K\sigma]
 =\epsilon(-1)^d
 [\operatorname{lk}_{\operatorname{lk}_K\tau}v].
\]
The coefficient of \(\tau\) in the left side of (J.5) is thus
\[
(-1)^d\sum_v f([\operatorname{lk}_{\operatorname{lk}_K\tau}v])
 =(-1)^{d+q}(\delta f)([\operatorname{lk}_K\tau])
 =(-1)^m(\delta f)([\operatorname{lk}_K\tau]).
\]
This proves the identity at every simplex. For \(d=0\), the ordinary boundary of a zero-chain is zero and the right side has no simplices in its negative dimension, so both sides are zero.

If \(\delta f=0\), (J.5) proves the cycle assertion. Conversely, let \(L\) be any oriented combinatorial \(q\)-sphere, and take the closed \((q+1)\)-sphere \(K=L*S^0\). Orient it so that the link of the positive suspension vertex is \(L\). The coefficient at that vertex in (J.5) is \((-1)^{q+1}(\delta f)([L])\). Universal vanishing of the boundary therefore forces \(\delta f\) to vanish on every generator. This proves the converse.

For \(f'=f+\delta h\), \(h\in T^{q-1}\), equation (J.5) gives
\[
f'_\sharp(K)-f_\sharp(K)=(-1)^m\partial h_\sharp(K).
\]
The homology classes coincide. The perfect duality proved in D.5 assigns a unique degree-\(q\) cohomology class to each of them, so those classes coincide too. ∎

The cohomology class defined by an arbitrary cocycle in (J.3) can be tested against the L-classes already constructed. In degree four it computes the first rational Pontryagin class precisely when, for every complementary class \(a\),
\[
\langle a,[f_\sharp(K)]\rangle
 =\langle 3\ell_1(K)\smile a,[K]\rangle.
\tag{J.6}
\]
The equivalence follows from the perfect pairing and \(\mathfrak p_1=3\ell_1\); the cycle criterion by itself does not supply this normalization.

### J.3. Graph paths and rational coefficients

The passage from cycle values to an edge cochain in the bistellar-move method has a useful purely algebraic form. Let \(G\) be a connected graph, possibly infinite and with loops or multiple edges. Let \(\tau\) be an involution fixing a base vertex \(o\), and let
\[
c:H_1(G;\mathbb Q)\longrightarrow\mathbb Q
\]
satisfy \(c(\tau_*z)=-c(z)\). All individual chains have finite support. Choose paths \(p_v\) from \(o\) to each vertex \(v\), with \(p_o=0\), and put
\[
\xi_v=\tfrac12(p_v+\tau_*p_{\tau v}).
\tag{J.7}
\]
Then \(\partial\xi_v=v-o\), \(\xi_{\tau v}=\tau_*\xi_v\), and for an oriented edge \(e:v\to w\),
\[
h(e)=c(e+\xi_v-\xi_w)
\tag{J.8}
\]
is an anti-invariant rational edge cochain representing \(c\). Its cohomology class is independent of the paths.

**Proof.** The two boundaries in (J.7) are both \(v-o\), since \(\tau o=o\). Applying \(\tau\) proves its equivariance. The argument of \(c\) in (J.8) is a cycle, so it lies in the stated domain. Reversing an edge reverses that cycle; applying \(\tau\) applies \(\tau_*\) to it. Thus (J.8) defines an anti-invariant cochain. A graph has no two-cells, so every edge cochain is a cocycle. On a finite cycle \(z\), the coefficients of the path terms at each vertex cancel because \(\partial z=0\). Consequently \(h(z)=c(z)\), as required.

For another family \(\xi'_v\) with the same boundaries, put \(t_v=\xi'_v-\xi_v\); each \(t_v\) is a cycle. The change in (J.8) is \(c(t_v)-c(t_w)=-d a(e)\), where \(a(v)=c(t_v)\) and \(d a(e)=a(w)-a(v)\). It is a coboundary. This proves path independence and includes loops and an infinite graph, since every evaluated chain remains finite. ∎

More generally, if a complexity-decreasing recursion reaches \(o\) and chooses finitely many edges \(\beta_j:v\to v_j\), an averaged choice is
\[
\xi_v=\frac1r\sum_{j=1}^r(\xi_{v_j}-\beta_j).
\tag{J.9}
\]
Induction proves \(\partial\xi_v=v-o\): each summand has boundary \((v_j-o)-(v_j-v)=v-o\). The decreasing recursion and finite branching make each \(\xi_v\) a finite rational chain. Rational coefficients must be retained throughout this averaging step. Decomposition of a resulting rational cycle into integral elementary-cycle generators gives rational coefficients in that decomposition. Choosing single paths instead keeps those paths integral; (J.8)'s independence proof still applies. This explains the coefficient convention needed in Gaifullin's Section 6 algorithm.

## Sources and contributions

John Milnor's [1957 lectures, with notes by James Stasheff](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/milnorcc.pdf), Chapter XVI, Sections 1–4, develop the generic-fibre construction and credit René Thom for the combinatorial characteristic classes. The complete duality, approximation, rational comparison and stabilization proofs above supply the steps compressed in that source. Its smooth-triangulation comparison is developed in the two linked companions.

Alexander A. Gaifullin's [2009 paper](https://arxiv.org/html/0912.3933v1), Sections 2 and 4–6, develops the oriented-link complex and the bistellar-move approach to local Pontryagin formulae. Section J gives complete independent proofs of the chain criterion and graph-cochain steps used here. The paper credits Norman Levitt and Colin Rourke for local existence results, Udo Pachner for the bistellar-equivalence theorem, and Victor M. Buchstaber and G. I. Sharygin for the acknowledged problem suggestion and discussion. Its explicit first-Pontryagin formula and its global classification of local cocycles are further results in the cited work.

The chapter's exposition, expanded proofs and six exercise solutions were independently written and self-checked by the named writing AI. The cited human mathematical contributions retain their attribution; no source prose or figures have been imported.
