# Equivariant perverse sheaves and perverse sheaves on stacks

*Written and reconstructed by GPT-6.1 Sol and GPT-6 Astra (OpenAI) in Codex, Ultra setting, October 2026. Checked by the AI writer; independent review is not claimed. Public domain (CC0).*

Scaling the affine line preserves its two orbits, the punctured line and the origin. A perverse sheaf can be constant on both and still fail to carry the scaling action. The obstruction lies in how its nearby and vanishing cycles are attached. We begin with that distinction between an action and an orbit stratification, then organize the same data through stabilizers, quotient stacks and finite-dimensional resolution models.

Our earlier tools are the smooth-pullback theorem in [Affine morphisms, Artin vanishing and perverse cohomology](affine-morphisms-artin-vanishing-and-perverse-cohomology.md), the boundary characterization of [Intermediate extensions and intersection complexes](intermediate-extensions-and-intersection-complexes.md), and the gluing diagrams in Nearby and vanishing cycles. The explicit topological diagrams below concern complex varieties with a characteristic-zero coefficient field \(\Lambda\). Geometric étale statements use \(\overline{\mathbb Q}_\ell\), with \(\ell\) invertible on the base. We distinguish the algebraic ground field from the coefficient field. Group actions are by smooth finite-type algebraic groups; additional connectedness hypotheses are stated separately. Frobenius structures are extra data, not part of the geometric classification.

## 1. An action on a perverse sheaf

Write \(p,a:G\times X\to X\) for projection and action, and \(e:X\to G\times X\) for the identity section. A **strongly equivariant perverse sheaf** is a perverse \(P\) with an isomorphism \(\alpha:p^*P\to a^*P\) satisfying \(e^*\alpha=1\). Its cocycle says that the map from the fibre at \(x\) to that at \(ghx\) agrees with the composite through \(hx\). The same equation is imposed on the sheaf isomorphisms over \(G^2\times X\). A morphism must commute with these action maps. Denote this category by \(\operatorname{Perv}_G(X)\).

These conditions carry information even for a point. If a finite group acts on a point, \(P\) is a vector space and \(\alpha\) is its representation. For \(G=\mathbb Z/2\), a trivial line and a sign line become the same vector space after forgetting the action, but their identity linear map is not equivariant.

Connected groups behave differently in the perverse heart.

**Theorem 1.1.** Suppose \(G\) is connected. The forgetful functor \(\operatorname{Perv}_G(X)\to\operatorname{Perv}(X)\) is fully faithful. An underlying perverse sheaf admits an action if and only if \(p^*P\) and \(a^*P\) are isomorphic; when it does, the normalized action is unique.

**Proof.** Put \(g=\dim G\). Both maps are smooth of relative dimension \(g\), since \((h,x)\mapsto(h,hx)\) identifies the action map with a projection. The connected-fibre smooth-pullback theorem gives
\[
\operatorname{Hom}(P,Q)
 \xrightarrow{\sim}
\operatorname{Hom}(p^*P[g],p^*Q[g]).                         \tag{1.1}
\]
The identity section is an inverse on these Hom groups. Given an isomorphism \(\beta:p^*P\to a^*P\), its restriction \(b=e^*\beta\) is an automorphism of \(P\). Precomposing with \(p^*b^{-1}\) normalizes it. If two normalized isomorphisms are given, their quotient is an automorphism of \(p^*P\) restricting to the identity; (1.1) makes that quotient the identity.

Apply the same argument to projection from \(G^2\times X\). The two proposed cocycle maps are isomorphisms between the same normalized smooth pullbacks and restrict to the identity at \((1,1)\). Their quotient is the identity by connected-fibre full faithfulness. This proves the cocycle rather than assuming it from the initial isomorphism. Finally conjugate \(a^*f\) by the two action maps for any \(f:P\to Q\). The result and \(p^*f\) have the same identity-section restriction. Equation (1.1) makes them equal, exactly the compatibility required of an equivariant morphism. \(\square\)

The theorem says that an action, when it exists, is a property of the perverse object. It does not assert existence for every object, or full faithfulness in the derived category. Both limitations will occur concretely below.

## 2. Stabilizers and the gluing obstruction

### One orbit and its simple extensions

Take an orbit \(O=G/H\), with its torsor quotient. Pull an equivariant local system back along \(G\to O\). Transport from the base point \(H\) trivializes this pullback, so the remaining information is how the stabilizer acts on its fibre \(V\). An automorphism of the constant local system varies locally constantly on \(H\). The identity component therefore acts trivially, and the cocycle becomes a representation of the finite geometric component group. Conversely a representation supplies the locally constant torsor descent maps; their cocycle gives the descended local system and its action. Intertwiners descend in exactly the same way. Thus
\[
\operatorname{Loc}_G(G/H)
 \simeq\operatorname{Rep}_\Lambda(\pi_0H).                    \tag{2.1}
\]
One may construct the inverse using the finite étale component cover \(G/H^\circ\to G/H\). This argument uses local-system descent along the torsor. In positive characteristic it requires fppf descent when \(H\) is nonsmooth; it does not treat \(G\to O\) as smooth in that case. The complex linear quotients needed for the resolution models have the explicit construction in Appendix B, Proposition B.6a. General finite-characteristic quotient and descent prerequisites retain their separate scope.

For a connected stabilizer, (2.1) gives one irreducible equivariant local system, namely \(\Lambda\). It says nothing of that kind about all local systems without equivariance. There is also no assumption that \(G\) itself is simply connected.

Suppose \(G\) is connected and there are finitely many orbits. The simple equivariant perverse objects are precisely
\[
\operatorname{IC}(\overline O,E),\qquad
 E\text{ irreducible in }\operatorname{Rep}_\Lambda(\pi_0H_O), 
                                                               \tag{2.2}
\]
extended by zero from their closed supports. Here is the proof. Smooth base change for restriction and extension transports the equivariance to the image defining intermediate extension. The resulting object has neither a boundary subobject nor a boundary quotient. These are two conditions: for the boundary inclusion \(i\), both \({}^pH^0i^!\) and \({}^pH^0i^*\) vanish. An equivariant subobject restricts to a sub-local system of \(E\). Irreducibility, together with the two boundary conditions, makes that subobject zero or the whole IC.

For the converse, the underlying perverse category has finite length, and the exact faithful forgetful functor detects strict subobjects. Hence the equivariant category has finite length too. Let \(P\) be equivariantly simple and choose an orbit open in its support. Its restriction is a local system in shift \([d]\), where \(d=\dim O\). Finite-group representations in characteristic zero are semisimple: average any projection onto an invariant subspace over the group to obtain an invariant projection. Choose an irreducible summand \(E\) of that restriction. By adjunction its inclusion gives a nonzero map from the perverse !-extension of \(E[d]\) to \(P\). Simplicity makes it surjective, so its restriction shows that \(P|_O=E[d]\). The adjunction map from \(P\) to the perverse *-extension is nonzero and therefore injective. The image of their composite is the intermediate extension; thus \(P\) is the object in (2.2). If several orbits were initially maximal in the support, this argument on one of them forces its closure to be all the support. Restriction to the dense orbit proves uniqueness of the two parameters.

### Scaling a line

For the two-stratum complex line, use the cycle diagram
\[
V\xrightarrow{u}W\xrightarrow{v}V,
\qquad T_\psi=1+vu,\qquad T_\phi=1+uv,                 \tag{2.3}
\]
with both displayed monodromies invertible. The group \(\mathbb G_m\) acts by multiplication on the coordinate. A full turn of the group parameter rotates the punctured normal coordinate once. The cycle transport identities from the preceding lesson identify its actions on nearby and vanishing cycles with \(T_\psi\) and \(T_\phi\), respectively. An equivariant isomorphism identifies this action family with a constant family. Its two transports must therefore be identities, giving
\[
vu=0,\qquad uv=0.                                           \tag{2.4}
\]
Reversing the chosen trivialization inverts both transports and gives the same conditions.

These conditions suffice as well. Define an odd operator \(q\) on the graded space \(V\oplus W\) by \(q|_V=u\), \(q|_W=v\). Equation (2.4) is \(q^2=0\). Choose homogeneous lifts of a homogeneous basis of \(\operatorname{im}q\), and extend that basis inside \(\ker q\). Each lift and its image form a two-term chain; each extra kernel vector forms a one-term chain. The four possible graded chains give the following complete list.

| \((V,W;u,v)\) | Object on the affine line |
| --- | --- |
| \((\Lambda,0;0,0)\) | \(\Lambda_{\mathbb A^1}[1]\) |
| \((0,\Lambda;0,0)\) | \(i_*\Lambda\) |
| \((\Lambda,\Lambda;1,0)\) | \(j_!\Lambda_{\mathbb G_m}[1]\) |
| \((\Lambda,\Lambda;0,1)\) | \(Rj_*\Lambda_{\mathbb G_m}[1]\) |

Here \(i\) is the origin and \(j\) is its complement. Each object carries an action: the open constant system is equivariant, and its two extensions are equivariant by base change; the constant and supported objects are equivariant directly. Their direct sums establish sufficiency. The endomorphism ring of each displayed diagram is the scalar field, so all four are indecomposable, and the chain decomposition supplies every object.

The distinction from an orbit stratification can now be seen in three dimensions. Take \(V=\Lambda\), \(W=\Lambda e_1\oplus\Lambda e_2\), and set
\[
u(1)=e_1,\qquad v(e_1)=0,\qquad v(e_2)=1.
\]
Then \(vu=0\), while \(uv\) sends \(e_2\) to \(e_1\). Its square is zero, so \(1+uv\) is invertible, but it is not the identity. This is a valid perverse diagram, constant on its two strata, without the scaling action. Its composition factors are the two equivariant simples. Consequently the equivariant heart, although a full subcategory when the group is connected, need not contain extensions formed in the larger heart.

For the geometric étale analogue, an equivariant object has constant restriction to the open homogeneous orbit by (2.1). The tame cycle construction with that constant restriction gives the same two transport conditions and the same four extension objects. This uses the precise étale cycle and gluing prerequisites of the preceding lesson. A tame generator by itself does not classify arbitrary wild local systems on a punctured trait.

## 3. The normalization on a stack

On a smooth variety of dimension \(d\), a local system becomes perverse in shift \([d]\). For a stack, the corresponding shift must account for the dimension of the chart used to see it. Let \(u:U\to\mathcal Y\) be a smooth chart of relative dimension \(r_u\). Define
\[
K\in{}^pD^{\le0}(\mathcal Y)
 \quad\Longleftrightarrow\quad
u^*K[r_u]\in{}^pD^{\le0}(U),                                \tag{3.1}
\]
and make the same definition for the lower bound. A locally constant relative dimension means that the shift is taken separately on its open-and-closed constant pieces. Smoothness and surjectivity, without a connected-fibre condition, suffice for this test.

The ambient category here has **coherent smooth derived descent**: its objects, morphism spaces and higher identifications are recovered from a smooth atlas and its entire nerve. Constructible pullback, localization and the other used operations belong to that input. Laszlo–Olsson and Liu–Zheng provide the étale formalism. Arinkin and coauthors formulate enhanced limits of sheaf categories, using an affine-diagonal convention and !-pullbacks; smooth purity converts their convention to the *-pullbacks here, including the twists. The Betti argument requires the analogous constructible descent. Descent of separate ordinary cohomology sheaves does not supply this enhanced input.

**Theorem 3.1.** With these operations and coherent descent, (3.1) defines the perverse t-structure, independently of the atlas. Normalized chart pullback commutes with its truncations:
\[
u^*({}^p\tau^{\le a}K)[r_u]
 \simeq{}^p\tau^{\le a}(u^*K[r_u]).                         \tag{3.2}
\]
There is an analogous lower-truncation identity. Use bounded constructible objects on finite-type stacks. On a locally finite-type stack the appropriate category is \(D^b_{c,\mathrm{loc}}\): constructibility and boundedness on each finite-type chart, with no imposed uniform bound across all charts.

**Proof.** For a smooth surjective map of schemes \(f\) of relative dimension \(s\), the functor \(f^*[s]\) is t-exact and conservative. It reflects perverse bounds, since it takes every forbidden perverse cohomology object to the corresponding forbidden object upstairs; surjectivity detects whether that sheaf is zero. Given two atlases, compare their pullbacks on the fibre product and then on an étale scheme cover of that algebraic space. Relative dimensions add, so the two normalized tests agree.

To construct a truncation, first perform it on each normalized smooth chart. For a smooth chart map \(f:U\to V\), the transition is \(f^*[r_u-r_v]\); t-exactness makes the truncated objects compatible. Functorial truncation in the enhanced category gives their coherent identifications, and smooth descent produces a triangle downstairs with the required two bounds. The chartwise truncations remain constructible and bounded. A finite-type atlas supplies a common bound; for a locally finite-type stack the construction glues over its finite-type opens by uniqueness.

There is a useful check on that coherent step. In a Čech nerve, the face maps are smooth, whereas a degeneracy can be a nonsmooth diagonal. If \(s\) is a degeneracy and \(d\) its face retraction, then \(ds=1\). Pulling the truncated face identification along \(s\) gives the degeneracy identification; the normalization shifts cancel. The original descent identities and functoriality of truncation give all composition identities. Equivalently the truncation adjunction gives a contractible space of compatible choices. No t-exactness assertion is being made for a nonsmooth degeneracy on arbitrary complexes.

For orthogonality, suppose \(A\) satisfies the upper-zero bound and \(B\) the lower-one bound. On a normalized chart every nonnegative homotopy group of their mapping space is
\(\operatorname{Hom}(A[m],B)\) for \(m\ge0\), which is zero by the ordinary perverse t-structure there. The mapping space is therefore contractible. Its descent limit is contractible too, proving \(\operatorname{Hom}(A,B)=0\) downstairs. Shift stability is detected by the same chart tests. This proves the axioms and (3.2). \(\square\)

The atlas \(\operatorname{pt}\to BG\) has relative dimension \(g=\dim G\). A local system \(E\) on \(BG\) is therefore in the perverse heart with shift \([-g]\). The normalized pullback is \(E[-g][g]=E\). More generally the torsor atlas \(X\to[X/G]\) gives
\[
\operatorname{Perv}([X/G])\simeq\operatorname{Perv}_G(X),
\qquad K\longmapsto u^*K[g].                                \tag{3.3}
\]
To verify this equivalence, its first overlap is \(G\times X\), so a descent map is exactly the action isomorphism of Section 1. The second overlap gives its cocycle and the identity section gives its unit. Conversely these heart descent data, with their shift removed, descend \(P[-g]\); Theorem 3.1 detects perversity and recovers the morphisms. In particular \([G/H\,/G]=BH\). For smooth \(H\) of dimension \(h\), the stack shift \([-h]\) pulls to the orbit shift \([g-h]\). If \(H\) is nonsmooth, use an actual smooth atlas of \(BH\); its point map need not be smooth.

Appendix A gives the more general bounded admissible-perversity construction, including its excellent-base, principal-adic, Gorenstein-quotient and local cohomological boundedness hypotheses. The middle normalization is recovered there as a particular pointed-chart evaluation. Integral duality has its own exactness conditions and is not asserted to preserve the usual integral heart.

## 4. Finite models and the information beyond the heart

The complex linear case can be built from ordinary finite-dimensional spaces. Choose \(G\subset\operatorname{GL}_r\) and a full-rank frame space \(V_{N,r}\). Its projection over \(X\) is universally \(2(N-r)\)-acyclic. Appendix B proves this for arbitrary base sheaves, constructs the quotient \((V_{N,r}\times X)/G\), and constructs its torsor and comparison charts. A model object is a triple
\[
(A,B,\beta),\qquad
\beta:q^*B\xrightarrow{\sim}\pi^*A,
\]
on \(X\), the quotient, and their common torsor. The interval argument there proves that acyclicity exceeding the width of the ordinary cohomological interval permits comparison of maps, extensions and triangles. Common products of frames give coherent comparison functors. Enlarging the interval supplies the triangulated category \(D^b_{G,c}(X)\), its perverse t-structure and the identification of its heart with \(\operatorname{Perv}_G(X)\).

The shifts can be checked directly. If \(\pi\) has relative dimension \(d\), a triple with perverse \(A\) has \(B[d-g]\) perverse on the quotient, because
\(q^*(B[d-g])[g]\simeq\pi^*A[d]\). Appendix B first proves torsor descent by local sections, then recovers the action map from this identification by connected-fibre full faithfulness. That proof works for disconnected \(G\); it is \(\pi\), not the torsor map \(q\), whose connected fibres are needed for recovering the action.

A nonzero degree-two map is already visible in these models. Take \(G=\mathbb G_m\), \(X=\operatorname{pt}\), \(r=1\), and \(N\ge3\). The quotient is \(\mathbb P^{N-1}\), and the frame space \(\mathbb C^N\setminus0\) is at least four-acyclic. The triples with underlying complexes \(\Lambda\) and \(\Lambda[2]\) have quotient complexes with the same names. Their underlying degree-two map on a point is zero, but every class in
\(H^2(\mathbb P^{N-1},\Lambda)\) gives a quotient map whose pullback is zero by acyclicity. Thus it gives a morphism of triples. Conversely every such morphism has this form. Appendix B's full-faithfulness and comparison proofs identify this Hom group in the equivariant derived category with \(H^2(\mathbb P^{N-1},\Lambda)=\Lambda\). The last equality follows from the projective-space cohomology calculation of the first lesson. The heart is ordinary vector spaces, so its own \(\operatorname{Ext}^2\) is zero. This demonstrates the extra derived information without assuming a derived equivalence merely from a heart equivalence.

The stack formalism exhibits the same phenomenon through the universal line bundle. Its first Chern class restricts along the classifying map for \(\mathcal O(1)\) on \(\mathbb P^1\) to that bundle's nonzero degree-one class. Consequently
\[
\operatorname{Hom}_{D_c(B\mathbb G_m)}
(\Lambda[-1],\Lambda[-1]2)\ne0.                         \tag{4.1}
\]
The Tate symbol is omitted for Betti sheaves. This class becomes zero on the atlas point. The perverse heart consists of vector spaces shifted by \([-1]\), and is semisimple, so usual realization cannot identify its bounded derived category with \(D_c^b(B\mathbb G_m)\). The universal line bundle and its functorial Chern class are inputs to this stack version; the finite-model calculation above establishes its separate category-theoretic example directly.

There is a further distinction in larger sheaf categories. Arinkin and coauthors use the ind-completion of bounded constructible sheaves on quasi-compact schemes. On stacks, constructibility need not imply compactness: their Appendix D gives the constant object on \(B\mathbb G_m\) as an example. That compactness assertion is an additional formalism input here, not a consequence of the degree-two calculation. We define stack perversity by normalized chart tests, not by compactness.

## 5. Flags and Kazhdan–Lusztig formulas

Let \(G\) be connected reductive and \(B\) a Borel subgroup. Bruhat cells in \(G/B\) are indexed by \(w\in W\), with dimension \(\ell(w)\). Their stabilizers are \(B\cap wBw^{-1}\). The root-subgroup description writes this intersection using the common torus and the common positive root groups, all connected. Thus (2.2) supplies one simple equivariant object per cell, its constant-coefficient intersection complex. The root-subgroup and Bruhat geometry are Lie-theoretic prerequisites to this application.

A general IC stalk need not have rank one. In the complex setting the geometric Kazhdan–Lusztig theorem gives
\[
P_{y,w}(q)=\sum_{k\ge0}
 \dim H^{2k-\ell(w)}((\operatorname{IC}_w)_x)q^k,
\qquad x\in C_y,\quad y\le w,                                \tag{5.1}
\]
with vanishing in the other degrees. The partial-flag analogue uses the parabolic polynomial in the \(q\)-parameter convention. This theorem is retained as an unproved input: Kashiwara–Tanisaki's Theorem 5.4 gives the stronger rational Hodge statement with unshifted even stalk \(\mathbb Q(-k)\). Forgetting that structure and extending coefficients yields (5.1). Its proof and the relevant Hodge foundations are still required. The finite-field stalk in Exercise 5 will instead follow from its explicit small resolution and proper base change.

The representation-theoretic form also requires a precise convention. Let \(\mathfrak g\) be finite-dimensional complex semisimple, let \(\lambda\) be dominant integral, and set \(w\cdot\lambda=w(\lambda+\rho)-\rho\). For Verma modules \(M(\mu)\) and their simple quotients \(L(\mu)\), the regular-integral statement is
\[
[M(w\cdot\lambda):L(y\cdot\lambda)]
=\begin{cases}P_{w,y}(1),&w\le y,\\0,&w\not\le y.\end{cases}    \tag{5.2}
\]
This is the finite-dimensional specialization of Kashiwara–Tanisaki, *Kazhdan–Lusztig conjecture … III*, Theorem 1.1, equation (1.5). Here \(\lambda+\rho\) is strictly dominant, the integral Weyl group is the full \(W\), and imaginary-root conditions are absent. Its localization and Riemann–Hilbert proof belongs to the D-modules course's *The Kazhdan–Lusztig conjecture*; its exact programme proof and dependencies have not been verified here. The monodromic or equivariant conditions of the localization theorem must be retained.

In rank one the multiplicity computation can be proved without using the general theorem. With \([h,e]=2e\), \([h,f]=-2f\), \([e,f]=h\), the highest-weight module has basis \(v_n\), \(n\ge0\), and actions
\[
fv_n=v_{n+1},\quad hv_n=(\lambda-2n)v_n,\quad
ev_n=n(\lambda-n+1)v_{n-1},\qquad ev_0=0.                    \tag{5.3}
\]
The three commutator identities hold by substitution. Conversely reorder any word in \(e,f,h\) acting on a highest-weight generator by those commutators; it becomes a linear combination of powers of \(f\). The displayed representation has those powers as independent vectors, so it is the universal Verma module.

At \(\lambda=0\), the span of \(v_1,v_2,\ldots\) is the Verma module of highest weight \(-2\). In that latter module the coefficient of \(ev_n\) is \(-n(n+1)\), nonzero for every \(n>0\). Any nonzero submodule contains a weight vector: use a polynomial in the diagonal operator \(h\) to isolate one term of a nonzero finite linear combination. Repeated application of \(e\) then gives its highest-weight generator, and \(f\) generates the whole module. Hence \(M(-2)\) is simple. The quotient of \(M(0)\) by that submodule is the trivial line. We obtain
\[
\operatorname{ch}M(0)=\operatorname{ch}L(0)+\operatorname{ch}L(-2),
\qquad \operatorname{ch}M(-2)=\operatorname{ch}L(-2).
\]
Subtracting yields the character of the trivial module. For general \(W\), (5.2) instead supplies a finite triangular system, with diagonal entries one, determining simple characters from Verma characters.

### The Borel action on the projective line

For \(\operatorname{PGL}_2\), write the action as \(z\mapsto az+b\). The two orbits are \(\mathbb A^1\) and infinity. The open restriction is constant, by its connected stabilizer. In the coordinate \(w=1/z\), the torus acts by \(w\mapsto a^{-1}w\). Its full turn forces identity vanishing-cycle transport as well as identity nearby transport. Equation (2.4) applies, giving four indecomposables:
\[
\Lambda_{\mathbb P^1}[1],\quad i_*\Lambda,\quad
j_!\Lambda_{\mathbb A^1}[1],\quad Rj_*\Lambda_{\mathbb A^1}[1]. \tag{5.4}
\]
Affine-open exactness makes the last two perverse, and base change makes them equivariant. The additional three-vertex chain from the nonequivariant projective-line classification has nonzero \(uv\) and is excluded. Thus Bruhat constructibility alone cannot supply the strong equivariance used in a localization comparison. For \(\operatorname{SL}_2\), the normal torus character is \(-2\), so the required identity is \((1+uv)^2=1\). The open restriction gives \(vu=0\), hence \((uv)^2=0\); characteristic zero then gives \(2uv=0\) and the same classification.

## 6. The scope in geometric Langlands

In classical geometric Satake one first uses \(G(\mathcal O)\)-equivariant perverse sheaves with support in finite-dimensional closed pieces of the affine Grassmannian. Appropriate finite-dimensional quotients of the proalgebraic group act on those pieces; the bounded-support categories are then assembled. On classical \(\operatorname{Bun}_G\), the locally finite-type version of Section 3 supplies the stack normalization. The later ind-completion and singular-support conditions are further parts of geometric Langlands, not extra atlas tests proved here.

Fargues–Scholze has a different ambient geometry. Definition IV.1.1 concerns Artin v-stacks. Definition/Proposition VI.7.1 constructs the relative perverse t-structure for bounded local Hecke stacks; Proposition VI.7.2 gives full faithfulness on the heart after pullback to the affine Grassmannian. Proposition VI.4.1 handles suitable pro-unipotent kernels, and VI.4.2 gives conservativity of hyperbolic localization. We retain those results at their stated v-stack and relative-Hecke scope. Their foundations and proofs are further obligations; Theorem 3.1 does not replace their hypotheses by an arbitrary diamond atlas.

## 7. Exercises with solutions

### Exercise 1 — scaling and an orbit-constant counterexample

Classify the strongly \(\mathbb G_m\)-equivariant perverse sheaves on \(\mathbb A^1\). Give their four multiplicities in terms of a cycle diagram, and construct an orbit-constructible object which has no such action.

**Solution.** Write \(a=\operatorname{rank}u\) and \(b=\operatorname{rank}v\). Conditions (2.4) put \(\operatorname{im}u\) inside \(\ker v\) and \(\operatorname{im}v\) inside \(\ker u\). Choose lifts in \(V\) of a basis of \(\operatorname{im}u\), and lifts in \(W\) of a basis of \(\operatorname{im}v\). These form \(a\) chains from \(V\) to \(W\) and \(b\) chains in the reverse direction. Extend the image bases to bases of the two kernels; their remaining vectors have zero image. Thus the multiplicities of the !-extension, *-extension, constant IC and point sheaf are respectively
\[
a,\qquad b,\qquad \dim V-a-b,\qquad \dim W-a-b.
\]
The inclusions into the kernels prove that these integers are nonnegative. The ranks and dimensions are isomorphism invariants, so they determine the direct-sum type uniquely. For the counterexample, use the chain \(e_2\in W\mapsto1\in V\mapsto e_1\in W\mapsto0\). It has \(vu=0\) and \((uv)^2=0\), with \(uv\ne0\). Its two monodromies are invertible and its open local system is constant, so it is a valid orbit-constructible perverse object. The nonidentity vanishing transport prevents equivariance.

### Exercise 2 — the two actions on a line

For the trivial \(\mathbb Z/2\)-action on a point, classify the equivariant perverse sheaves and decide whether the forgetful functor is full.

**Solution.** Let \(s\) be the generator. Its action obeys \(s^2=1\). The idempotents \(e_+=(1+s)/2\) and \(e_-=(1-s)/2\) have sum one and product zero, giving \(V=\operatorname{im}e_+\oplus\operatorname{im}e_-\). On the first summand \(s\) is \(+1\), and on the second it is \(-1\). Intertwining maps preserve both summands. Hence every object is a direct sum of trivial and sign lines, with their two dimensions determining it. A map \(c\) from a trivial line to a sign line is equivariant only if \(c=-c\), thus only if \(c=0\). The underlying vector spaces have nonzero maps, which proves that forgetting is not full.

### Exercise 3 — two extensions at infinity

Classify the \(B\)-equivariant perverse sheaves on \(\mathbb P^1\) for the Borel of \(\operatorname{PGL}_2\), and compute the two nonsplit extensions of its simple objects.

**Solution.** The affine orbit and its stabilizer force a constant open system. At infinity the normal character has weight \(-1\), so the cycle diagram satisfies both zero-composite relations. Decomposition into the four graded chains therefore gives the list (5.4). The local diagrams globalize: identify their punctured-disc restriction with the restriction of the constant affine-line system and apply the earlier two-open descent theorem. This also identifies maps, so it gives the global classification, not only the local one. All four global extension objects carry the action by Section 5.

In the chain \(V\xrightarrow{1}W\xrightarrow0V\), the isolated \(W\)-vertex is a subobject and the quotient is the isolated \(V\)-vertex. Reversing the nonzero arrow reverses these roles. With \(i\) the point at infinity and \(j\) the affine-line inclusion, this gives
\[
0\longrightarrow i_*\Lambda\longrightarrow j_!\Lambda[1]
 \longrightarrow\Lambda_{\mathbb P^1}[1]\longrightarrow0,
\]
\[
0\longrightarrow\Lambda_{\mathbb P^1}[1]\longrightarrow Rj_*\Lambda[1]
 \longrightarrow i_*\Lambda\longrightarrow0.
\]
A split sum would have both arrows zero, while each displayed extension has rank one for one arrow. Rank is invariant under the two changes of basis, so neither sequence splits. The four multiplicities from Exercise 1 classify every direct sum.

### Exercise 4 — descent from a stabilizer

Recover the equivariant perverse category of a homogeneous orbit \(G/H\). Determine its simple objects and its shift on \(BH\) when \(H\) is smooth.

**Solution.** Fix the point \(H\) and a fibre \(V\). The action trivializes the pullback to \(G\). On \(G\times H\), two trivializations differ by the action of \(H\) on \(V\); being a map of constant local systems makes it locally constant on \(H\). The unit makes it trivial on \(H^\circ\), so it factors through \(\pi_0H\). Conversely an action of that finite group supplies the torsor descent cocycle. An intertwiner is exactly a compatible descent morphism. This proves the equivalence (2.1), with the fppf local-system descent hypothesis retained for nonsmooth stabilizers.

Equivariance on a single smooth orbit makes the cohomology lisse. The perverse stalk and costalk bounds there put it in the single local-system shift \([d]\), \(d=\dim(G/H)\). Thus the category is finite-dimensional representations of \(\pi_0H\) in that shift, and its simple objects are the irreducible representations. Averaging projections proves semisimplicity in the stated coefficient characteristic. When \(H\) is smooth, write \(h=\dim H\), \(g=\dim G\). On \(BH\) the corresponding local system has shift \([-h]\), since the orbit atlas adds \([g]\) and \(g-h=d\). Setting \(H=G\) gives the point orbit and the normalization of \(BG\). Setting \(H=1\) gives the free orbit, with quotient a point and ordinary vector spaces.

### Exercise 5 — a small resolution and the polynomial \(1+q\)

Over the algebraic ground field \(k\), fix the standard plane \(F_2\subset k^4\). Let
\[
X=\{W\in\operatorname{Gr}(2,4):\dim(W\cap F_2)\ge1\}.
\]
Compute its intersection-complex stalks and the normalized stalk polynomial at its singularity. Identify the corresponding partial-flag and full-flag labels.

**Solution.** The intersection condition says that projection \(W\to k^4/F_2\) has rank at most one. In Plücker coordinates it is \(p_{34}=0\). Substitution in the Grassmannian equation leaves
\(p_{13}p_{24}-p_{14}p_{23}=0\), a three-dimensional quadric cone in projective four-space. Its four nonzero partial derivatives are the four off-vertex coordinates with their signs. They vanish together precisely at the point with only \(p_{12}\ne0\), namely \(W=F_2\). This calculation works in every characteristic.

Keep track of the intersecting line rather than choosing it implicitly. Set
\[
Y=\{(L,W):L\subset F_2, \dim L=1, L\subset W\},\qquad f:Y\to X.
\]
For fixed \(L\), the possible \(W/L\) are lines in the three-dimensional vector space \(k^4/L\). Thus \(Y\) is a projective-plane bundle over \(\mathbb P(F_2)\), smooth of dimension three, and \(f\) is projective. Away from \(F_2\), the inverse sends \(W\) to \((W\cap F_2,W)\). This is a morphism because that kernel has constant rank one on the open set. Over \(F_2\) its fibre is \(\mathbb P^1\). The exceptional stratum has dimension zero and twice its fibre dimension is two, strictly below three. The small-map theorem therefore identifies \(Rf_*\Lambda_Y[3]\) with \(\operatorname{IC}_X\).

At every smooth point the stalk is \(\Lambda[3]\). At the vertex, proper base change and projective-line cohomology give exactly
\[
H^{-3}(i^*\operatorname{IC}_X)=\Lambda,\qquad
H^{-1}(i^*\operatorname{IC}_X)=\Lambda(-1).                    \tag{7.1}
\]
The remaining stalk groups vanish. In the étale setting duality gives \(D\operatorname{IC}_X=\operatorname{IC}_X(3)\). Dualizing the two groups after that twist puts the costalk in degrees one and three, with coefficients \(\Lambda(-2)\) and \(\Lambda(-3)\). In the Betti setting omit all Tate symbols. The normalization \(2k-3\) turns (7.1) into the polynomial \(1+q\).

Here are the permutation labels explicitly. For upper-triangular Bruhat cells in the Grassmannian, the two pivot indices \(i_1<i_2\) obey \(\dim(W\cap F_2)\ge1\) exactly when \(i_1\le2\). The largest allowable pair is \((2,4)\), with cell dimension \((2-1)+(4-2)=3\). Its minimal coset representative is \(2413\); the vertex has pair \((1,2)\) and representative \(1234\). The parabolic subgroup is generated by \(J=\{s_1,s_3\}\), so the partial-flag formula is \(P^{J,q}_{1234,2413}=1+q\).

The map from complete flags to planes has fibre \(\mathbb P^1\times\mathbb P^1\): choose a line in the plane and a line in the two-dimensional quotient. Its relative dimension is two. In the inverse image of the cell just found, choose the largest cell in each projective-line fibre. The resulting complete-flag permutation is the maximal element of its coset, obtained by multiplying \(2413\) by \(2143\), the longest element of \(W_J\). It is \(4231\), of length five. The projective bundle over the irreducible \(X\) is irreducible, so the closure of this dense cell is the entire inverse image, \(X_{4231}\). Over the vertex the largest fibre cell is \(2143\), of length two; its closure is the whole fibre \(X_{2143}\). Normalized smooth pullback shifts (7.1) by \([2]\), producing degrees \(-5,-3\). Equation (5.1) then yields \(P_{2143,4231}=1+q\). The resolution computed the stalks independently; the general theorem supplies their Kazhdan–Lusztig names.

## Appendix A. Admissible perversities and adic coefficients

The middle atlas shift is one member of a larger family. We describe the bounded constructible version, including the hypotheses needed by its proof. This also supplies the integral perverse truncations used in the preceding affine lesson.

Let the base \(S\) be a disjoint union of excellent, quasi-compact, finite-dimensional schemes admitting dimension functions. Fix a prime \(\ell\) invertible on \(S\). For adic coefficients take a commutative ring \(\Lambda\), complete for a principal ideal \(\mathfrak m=(\pi)\) generated by a non-zero-divisor, such that every \(\Lambda/\mathfrak m^{n+1}\) is an \(\ell\)-primary torsion, zero-dimensional Gorenstein ring. A complete discrete valuation ring of residue characteristic \(\ell\) is the basic example. Retain local \(\Lambda/\mathfrak m\)-boundedness: there is a smooth atlas by algebraic spaces such that every scheme étale and of finite presentation over an atlas piece has finite cohomological dimension for \(\Lambda/\mathfrak m\)-modules. The bound is allowed to depend on that scheme.

Use the normalized constructible adic six-operation category, its ordinary constructible truncations, absolute purity on regular schemes, and its coherent smooth hyperdescent. Closed/open restriction, exceptional restriction, and the associated recollement must preserve the constructible category. These are ambient prerequisites. They hold in the enhanced formalism of Liu–Zheng with the stated base and coefficient conditions. An adic object is a coherently compatible derived system, not a sequence of underived sheaves. [The pro-étale site and ℓ-adic complexes](course:AG-LTF/the-pro-etale-site-and-l-adic-complexes#4-completion-remembers-a-complex) proves this coherent-system interpretation, completion and constructibility detection for its scheme and discrete-valuation-ring setting. It does not supply the higher-stack six operations and hyperdescent required here, or the broader Gorenstein coefficient generality just stated. All stalk and costalk symbols below mean the actual derived adic operations.

On a quasi-compact separated scheme \(U\) of finite type over \(S\), a **weak perversity** is an integer-valued function \(p\) such that \(\{x:p(x)\geq a\}\) is ind-constructible for every integer \(a\), meaning a union of constructible subsets. It is **admissible** if, for every point \(\eta\), some dense open subset of \(\overline{\{\eta\}}\) satisfies
\[
p(x)\leq p(\eta)+2\operatorname{codim}(x,\overline{\{\eta\}}).
\tag{A.1}
\]
Weakness implies \(p(x)\geq p(\eta)\) on a sufficiently small dense open of that closure: an ind-constructible set containing its generic point contains a constructible subset containing that point, and such a subset contains a dense open. We use locally bounded integer-valued admissible functions, with bounds on each such scheme chart.

For a geometric point \(\bar x\), take its strict localization \(U_{(\bar x)}\), and let \(i_{\bar x}:\bar x\to U_{(\bar x)}\) and \(j_{\bar x}:U_{(\bar x)}\to U\). Define
\[
\begin{aligned}
K\in{}^pD^{\leq0}(U)
&\Longleftrightarrow i_{\bar x}^*j_{\bar x}^*K\in D^{\leq p(x)}
\quad\text{for every }x,\\
K\in{}^pD^{\geq0}(U)
&\Longleftrightarrow i_{\bar x}^!j_{\bar x}^*K\in D^{\geq p(x)}
\quad\text{for every }x.
\end{aligned}
\tag{A.2}
\]
We work with bounded constructible objects, or with objects bounded on each finite-type chart. In particular the lower test is used with the locally bounded-below hypothesis present in the adic formalism. Replacing the adic costalk in (A.2) by a naive list of coefficient-level costalks is not an additional theorem.

**Proposition A.1.** Under these prerequisites, the cuts (A.2) define a bounded t-structure on the bounded constructible adic category of \(U\). Both perverse truncations preserve constructibility. The same argument applies to bounded constructible finite-coefficient complexes whenever the corresponding purity, ordinary truncation and recollement prerequisites hold.

**Proof.** We give the finite construction rather than using an unbounded existence theorem. By Noetherian induction it suffices to remove a dense open from each irreducible component. Nilpotents do not change the étale category. Excellence allows that open to be regular. Shrink it so that the cohomology of the given \(K\) is lisse, and so that, on each component with generic point \(\eta\),
\[
p(\eta)\leq p(x)\leq p(\eta)+2c_x,
\qquad c_x=\operatorname{codim}(x,U).
\tag{A.3}
\]
For lisse coefficients on this regular open, purity gives
\(i_{\bar x}^!K\simeq K_{\bar x}(-c_x)[-2c_x]\).
Consequently the ordinary truncation triangle at degree \(p(\eta)\) has first term in the upper cut of (A.2) and last term in its lower cut of degree one. The first term has stalk degrees at most \(p(\eta)\leq p(x)\). The last has costalk degrees at least \(p(\eta)+1+2c_x\geq p(x)+1\). Ordinary constructible truncation retains lisse cohomology on this open.

Let \(j:V\hookrightarrow U\) be this dense open, and \(i:Z\hookrightarrow U\) its closed complement. If \(A_V\to j^*K\to B_V\) is that triangle, form
\[
j_!A_V\longrightarrow K\longrightarrow G\xrightarrow{+1}.
\]
By induction the restricted perversity on the smaller-dimensional \(Z\) has truncations. Set \(C={}^p\tau^{\leq0}i^!G\), take the cone \(B\) of the counit-induced arrow \(i_*C\to G\), and take the fibre \(A\) of \(K\to G\to B\). The recollement octahedron gives
\[
j^*A=A_V,\quad j^*B=B_V,\quad
i^*A=C,\quad i^!B={}^p\tau^{\geq1}i^!G.
\tag{A.4}
\]
Closed restriction of the upper stalk test and transitivity of the costalk test give the required bounds on \(Z\). Thus \(A\to K\to B\) has upper zero and lower one. Every operation used is constructible by the specified prerequisites; the finite induction preserves boundedness.

Orthogonality can be proved by the same induction without assuming an ambient perverse t-structure. Given upper \(A\) and lower-one \(B\), choose a common dense regular open on which both have lisse cohomology. At its generic point their complexes have ordinary degrees at most \(p(\eta)\) and at least \(p(\eta)+1\). Shrink to keep these bounds throughout that open. Ordinary orthogonality gives \(\operatorname{Hom}(j^*A,j^*B)=0\). On the complement, \(i^*A\) and \(i^!B\) satisfy the corresponding opposite tests, so induction gives \(\operatorname{Hom}(i^*A,i^!B)=0\). Apply \(\operatorname{Hom}(-,B)\) to \(j_!j^*A\to A\to i_*i^*A\); both outside Hom groups vanish, hence so does \(\operatorname{Hom}(A,B)\).

Shift stability is immediate. Finally let \(\alpha\leq p\leq\beta\) on this chart. An ordinary complex in degrees at most \(\alpha\) is in the upper cut. An ordinary complex in degrees at least \(\beta\) is in the lower cut, since point exceptional restriction is ordinary left t-exact. Shifting any bounded complex puts it in either cut. This proves boundedness and completes the t-structure construction. \(\square\)

The factor \(2\) in (A.3) is essential for this proof. On a regular curve take \(p(\eta)=0\) and \(p(x)=2\) at every closed point. This is a weak admissible function: its positive level sets are unions of the constructible closed points, and (A.1) holds. Every nonempty open still contains closed points, so no dense open satisfies \(p(x)\leq p(\eta)+c_x\). The purity shift \(2c_x\), however, proves exactly the required lower bound. Thus the construction uses the admissibility inequality as stated, without imposing a stricter dense-open condition.

To pass to a higher Artin stack of finite geometric level, assign a function \(p_u\) to each pointed smooth scheme chart. For a smooth map of pointed charts \(f:(V,v,y)\to(U,u,x)\), set
\[
\delta=\dim_y f-\operatorname{trdeg}_{\kappa(x)}\kappa(y)
=\operatorname{codim}(y,V_x).
\]
A **perversity evaluation** requires
\[
p_u(x)\leq p_v(y)\leq p_u(x)+2\delta.
\tag{A.5}
\]
Require each chart function to be weak, admissible and locally bounded as above. Relative dimensions and residue-field transcendence degrees add for composed smooth charts, so \(\delta\) adds. The chart data include their compatibility with equivalences and common refinements; they are not values chosen independently on unrelated atlases.

Smooth pullback is t-exact for these *unshifted* chart cuts. The upper assertion follows from the first inequality in (A.5). For the lower assertion, smooth base change and purity on the smooth fibre give
\[
i_{\bar y}^!f^*K\simeq
\bigl(i_{\bar x}^!K\bigr)|_{\bar y}(-\delta)[-2\delta].
\tag{A.6}
\]
Indeed factor the fibre point through the generic point of a regular subvariety of dimension \(t=\operatorname{trdeg}_{\kappa(x)}\kappa(y)\). Its exceptional shift in the smooth \(r=\dim_y f\) fibre is \(-2(r-t)\); smooth base change identifies its coefficient with the displayed base costalk. This gives (A.6), including the twist. The lower bound after pullback is therefore \(p_u(x)+2\delta\), which is at least \(p_v(y)\). Both halves, hence their truncations, commute with the smooth transitions.

The coherent chartwise argument of Theorem 3.1 now constructs and descends these truncations, and its mapping-space proof gives orthogonality. For higher stacks one applies that argument inductively to the finite geometric level of the overlaps; an overlap is not silently replaced by an ordinary scheme groupoid. Smooth hyperdescent of the ambient enhanced category supplies the coherent data at each level. Its degeneracies are dealt with as explained in the proof of Theorem 3.1. Constructibility and local boundedness are detected on the scheme charts and retained by Proposition A.1. Thus the same cuts give the bounded constructible, or chartwise locally bounded constructible, perverse t-structure in this higher-stack formalism.

For a stack over a field \(k\), the middle evaluation is
\[
p_u(x)=-\operatorname{trdeg}_k\kappa(x)+r_u(x).
\tag{A.7}
\]
Its change under a smooth chart map is \(\delta\), within the interval (A.5). The inequality for the unshifted \(u^*K\) in (A.2) is precisely the ordinary middle inequality for \(u^*K[r_u]\), recovering (3.1). This explains the atlas shift and its compatibility with more general evaluations.

The integral construction is not an assertion that the usual integral perverse heart is self-dual. Already over a point, with \(\Lambda=\mathbf Z_\ell\),
\(R\operatorname{Hom}_\Lambda(\Lambda/\ell,\Lambda)\)
has its nonzero cohomology in degree one. It leaves the ordinary heart. Field duality, torsion-coefficient duality over a self-injective quotient ring, and adic Verdier duality have distinct exactness hypotheses. The locally bounded-below condition and the true adic costalk in (A.2) retain these distinctions.

## Appendix B. Torsor descent and finite resolution models

### B.1. Recovering the action in the heart

We now prove the comparison at the level of perverse sheaves. Work over the complex numbers with the field coefficients fixed above. The geometric data used below consist of varieties and algebraic torsors with étale local sections; the same arguments apply on étale charts of algebraic spaces once those charts and their sheaf operations are supplied. Smooth normalized pullback and its connected-fibre full faithfulness are Proposition 3.1 of the affine lesson. Effective étale descent, including descent of morphisms, is Proposition 4.1 of the perverse-t-structure lesson. Their precise operation prerequisites remain in force.

We first construct the torsor descent needed in the comparison. This avoids using descent on an unspecified derived category of stacks as a substitute for the argument.

**Lemma B.2 (torsor descent in the heart).** Let \(q:E\to Y\) be a smooth \(G\)-torsor, with \(g=\dim G\). Write \(r_1,r_2:E\times_YE\to E\) for the projections. The functor \(q^*[g]\) identifies \(\operatorname{Perv}(Y)\) with the category of pairs
\[
(F,\sigma),\qquad
F\in\operatorname{Perv}(E),\quad
\sigma:r_1^*F\xrightarrow{\sim}r_2^*F,              \tag{B.3}
\]
where \(\sigma\) is the identity on the diagonal and satisfies
\(r_{23}^*\sigma\circ r_{12}^*\sigma=r_{13}^*\sigma\) on the triple fibre product. Morphisms are perverse-sheaf morphisms compatible with \(\sigma\). Connectedness of \(G\) is not needed here.

**Proof.** Choose étale charts \(U_i\to Y\) with sections \(s_i:U_i\to E_i=E\times_YU_i\), and write \(F_i\) for the pullback of \(F\). Put
\[
L_i=s_i^*F_i[-g].                                  \tag{B.4}
\]
These are bounded constructible complexes. Pulling \(\sigma\) back along
\(e\mapsto(s_i(q_i(e)),e)\) gives an isomorphism
\(q_i^*L_i[g]\simeq F_i\). The normalized smooth pullback \(q_i^*[g]\) is t-exact and conservative, so it reflects perversity. Indeed it commutes with perverse cohomology, and each forbidden perverse cohomology object vanishes if its conservative pullback vanishes. Consequently \(L_i\) is perverse. This argument does not assert that the section pullback \(s_i^*\) is t-exact on arbitrary complexes.

Over \(U_i\times_YU_j\), pull \(\sigma\) back along the pair of sections \((s_i,s_j)\), then shift by \(-g\). This gives \(L_i\simeq L_j\). The diagonal and triple identities for \(\sigma\) give the identity and cocycle identities for these transition maps. Effective étale descent therefore constructs \(L\in\operatorname{Perv}(Y)\). The local isomorphisms \(q_i^*L_i[g]\simeq F_i\) agree on overlaps: that is the same triple identity applied to \((s_i,s_j,e)\). They give \(q^*L[g]\simeq F\), with its prescribed descent isomorphism.

A compatible morphism \(F\to F'\) pulls back to maps \(s_i^*F_i[-g]\to s_i^*F_i'[-g]\). Compatibility with \(\sigma\) makes these maps agree under the transition maps, so étale descent gives a morphism \(L\to L'\). It is unique, since the same local section calculation recovers every such morphism. Conversely pullback of a morphism on \(Y\) has the required compatibility. Applying the construction to \(F=q^*L[g]\) recovers \(L\) and its morphisms. This proves the equivalence. \(\square\)

Suppose now that \(G\) acts freely on a variety \(E\), that \(q:E\to Y=E/G\) is a torsor as in the lemma, and that
\(\pi:E\to X\) is an equivariant smooth surjection of pure relative dimension \(d\) with connected geometric fibres. These are hypotheses on a supplied resolution, rather than an assertion that every free quotient has already been constructed. Consider the category \(\mathcal T_\pi(X)\) of triples
\[
(A,B,\beta),\qquad
A\in\operatorname{Perv}(X),\quad B\in D_c^b(Y),\quad
\beta:q^*B\xrightarrow{\sim}\pi^*A.                 \tag{B.5}
\]
A morphism is a pair \((f:A\to A',h:B\to B')\) such that
\(\pi^*f\circ\beta=\beta'\circ q^*h\).
Every triple automatically satisfies
\[
B[d-g]\in\operatorname{Perv}(Y),\qquad
q^*(B[d-g])[g]\simeq\pi^*A[d].                     \tag{B.6}
\]
The right-hand side is perverse by smooth pullback, and the same reflection argument as in the lemma proves the assertion about \(B\).

**Proposition B.3 (comparison for a supplied resolution).** There is a canonical equivalence
\[
\mathcal T_\pi(X)\simeq\operatorname{Perv}_G(X)      \tag{B.7}
\]
whose underlying object on \(X\) is \(A\). The group \(G\) may be disconnected; the connected-fibre hypothesis is on \(\pi\).

**Proof.** A triple first determines the action on \(A\). Let \(a_E,p_E:G\times E\to E\) be action and projection. Since \(qa_E=qp_E\), the complex \(q^*B\) has its canonical action isomorphism. Transporting it through \(\beta\) gives
\[
\sigma_\beta=(a_E^*\beta)\circ(p_E^*\beta)^{-1}:
p_E^*\pi^*A\xrightarrow{\sim}a_E^*\pi^*A,          \tag{B.8}
\]
where the two pullbacks of \(q^*B\) are identified by that equality of maps. This isomorphism has a unit and satisfies the action cocycle. In a composite through three points, the intervening \(\beta^{-1}\beta\) cancels, leaving the same transport as the direct arrow.

We must descend the isomorphism to \(G\times X\). The two complexes \(p^*A[g]\) and \(a^*A[g]\) are perverse there: \(p\) is smooth of relative dimension \(g\), and \(a\) is its composite with the isomorphism \((h,x)\mapsto(h,hx)\). The map \(1_G\times\pi\) is smooth with connected nonempty geometric fibres and relative dimension \(d\). Its normalized pullback is fully faithful on these perverse objects. Thus \(\sigma_\beta\), with the common shift \(g+d\), is the pullback of a unique isomorphism
\(\alpha:p^*A\to a^*A\). Full faithfulness lifts the inverse as well, so the lifted map is indeed an isomorphism.

Restrict to the identity of \(G\). The pullback by \(\pi\) of \(e^*\alpha\) is the identity. Faithfulness on the perverse object \(A\) gives \(e^*\alpha=1_A\). To check the cocycle, compare its two composites on \(G^2\times X\). Their source and target become perverse after the common shift \(2g\). Pullback along \(1_{G^2}\times\pi\) is faithful on these shifted objects, and the composites become equal because \(\sigma_\beta\) satisfies the cocycle. They are therefore equal before pullback. We have obtained an actual object \((A,\alpha)\) of \(\operatorname{Perv}_G(X)\).

For a morphism of triples, compatibility with \(\beta,\beta'\) makes \(\pi^*f\) commute with the transported action isomorphisms. Faithfulness along \(1_G\times\pi\) then makes \(f\) commute with \(\alpha,\alpha'\). This defines a functor from the left side of (B.7) to the right side.

We construct its inverse using Lemma B.2. Start with \((A,\alpha)\). On \(E\), the object \(\pi^*A[d]\) is perverse. The torsor identification
\(G\times E\simeq E\times_YE\), \((h,e)\mapsto(e,he)\), turns the pullback of \(\alpha\), shifted by \(d\), into a descent isomorphism for this object. The action unit and cocycle are exactly the identities in (B.3). The lemma gives \(C\in\operatorname{Perv}(Y)\) and a compatible isomorphism
\(q^*C[g]\simeq\pi^*A[d]\). Set \(B=C[g-d]\) and shift the isomorphism by \(-d\). We obtain \(\beta:q^*B\simeq\pi^*A\), hence a triple. An equivariant morphism of the \(A\)'s gives a morphism of descent data; the morphism part of the lemma gives the required unique map of the \(B\)'s.

These constructions are inverse, including their morphisms. Starting with \((A,\alpha)\), the reconstructed action pulls back to the original one, and connected-fibre full faithfulness makes it equal to that original action. Starting with a triple, its transported descent datum is precisely the datum carried by \(B[d-g]\) through \(\beta[d]\). Uniqueness in Lemma B.2 recovers this object, its identification and every morphism. Those uniqueness statements also make the resulting unit and counit natural. This proves (B.7). \(\square\)

The connected-fibre hypothesis on \(\pi\) cannot be dropped. Take \(G=\mathbb Z/2=\{1,s\}\), \(X=Y=\operatorname{pt}\), and \(E=G\), with both \(q\) and \(\pi\) the map to a point. Set \(A=B=\Lambda\), and let \(\beta\) be multiplication by \(1\) on the component \(1\) and by \(2\) on the component \(s\). This is a triple, since \(\beta\) is invertible. Formula (B.8) gives multiplication by \(2\) for transport by \(s\) starting at \(1\), and by \(1/2\) for transport by \(s\) starting at \(s\). These are unequal in characteristic zero. They cannot be the pullback of a single map on the \(s\)-component of \(G\times X\). Thus an arbitrary disconnected resolution supplies triples which do not recover a group action on \(A\).

**Corollary B.4 (independence in the heart).** Two supplied resolutions satisfying the hypotheses of Proposition B.3 give canonically equivalent triple categories. The equivalences preserve the equivariant object on \(X\) and satisfy the composition compatibility for three or more resolutions.

**Proof.** Identify each triple category with \(\operatorname{Perv}_G(X)\) by the explicit construction above. For a fixed equivariant object, Lemma B.2 gives a unique descent object up to the unique isomorphism preserving its descent identification. Thus passing from one resolution to another and back has the canonical identity comparison. Two iterated comparisons have the same underlying equivariant object and identification; full faithfulness in Proposition B.3 gives a unique isomorphism between them. Every coherence diagram commutes because its two composites lift that same identity morphism.

This equivalence also agrees with the usual pullback between resolution models. If \(v:E'\to E\) is an equivariant map over \(X\), inducing \(\bar v:Y'\to Y\), pull a triple back to \((A,\bar v^*B,v^*\beta)\). It is a triple for \(\pi'\); its required perverse shift follows from (B.6) for \(\pi'\), so no t-exactness of \(\bar v^*\) is assumed. Its transported action is the pullback of the old one. The uniqueness in the lifting step of Proposition B.3 identifies its action on \(A\) with the same \(\alpha\). Consequently this pullback is the equivalence just constructed. The canonical composition maps of pullback preserve \(\alpha\), and hence have the asserted coherence. \(\square\)

The next subsection supplies acyclic free spaces, constructs their geometric quotients, and compares the bounded models. The derived construction retains its exact constructible-operation and descent prerequisites. Proposition B.3 and Corollary B.4 need only the smooth connected-fibre hypotheses on the given resolutions.

For the resolution definition and its derived scope, the freely readable primary reference is [Bernstein–Lunts, author-hosted Part I, §§1.9, 2 and 5](https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/luntz_ESF/3-derived-category-and-functors.pdf). [Baumann–Riche, Appendix A.1, Proposition A.2] treats the heart comparison. The argument here first constructs torsor descent by local sections and then recovers the action from the triple; both steps, their shifts and their morphisms have been written above. These references do not replace the geometric and operation prerequisites identified below.

### B.2. Acyclicity and bounded comparison

We next prove the acyclicity estimate, construct the quotient charts, and then use the adjunction unit to compare bounded derived models. Continue in the complex setting, with field coefficients. For a map \(f:Z\to Y\), say that \(f\) is **universally \(n\)-acyclic** if, after every base change under consideration, every sheaf \(M\) on the new base satisfies
\[
M\xrightarrow{\sim}f_*f^*M,\qquad
R^if_*f^*M=0\quad(1\le i\le n).                    \tag{B.9}
\]
The first isomorphism is the adjunction unit. Here sheaves need not be locally constant or constructible. The underlying topological spaces are Hausdorff; Proposition B.6a constructs the analytic quotient charts used here as locally trivial bundles of Hausdorff spaces. The bounded constructible operations, adjunctions and ordinary truncations are those of the first lesson. The constructible sheaf operations on the resulting algebraic spaces, or equivalently in the stated analytic setting on their local charts, retain these operation hypotheses.

**Lemma B.5 (a fibre calculation with arbitrary base coefficients).** Let \(F\) be a connected second countable manifold such that, for every coefficient vector space \(V\),
\(H^0(F,V)=V\) and \(H^i(F,V)=0\) for \(1\le i\le n\). A locally trivial bundle with fibre \(F\) is universally \(n\)-acyclic.

**Proof.** We prove the assertion for \(f:Y\times F\to Y\); restriction to trivializing opens will then prove the bundle assertion. For a connected open \(W\subset F\), sections of \(f^*M\) over \(U\times W\) are precisely sections of \(M\) over \(U\). Restrict along a fixed slice to construct one direction. On each fibre the sheaf is constant, so connectedness makes the original section agree with the pullback of its slice restriction at every stalk. This proves the other direction and its uniqueness. In particular \(f_*f^*M=M\). Applying this argument on a basis of connected \(W\)'s also proves that \(f^*\) preserves products of sheaves: the product comparison is an isomorphism on this product basis.

Let \(i_y:\{y\}\hookrightarrow Y\), and embed \(M\) by its germs into
\[
T(M)=\prod_{y\in Y}(i_y)_*M_y.                     \tag{B.10}
\]
The map is injective because a section with zero germ everywhere is zero. We show that \(f^*T(M)\) has zero higher direct images through degree \(n\). Write \(j_y:F\hookrightarrow Y\times F\) for the closed fibre. Product preservation and the stalk calculation for a closed fibre give
\(f^*T(M)=\prod_y(j_y)_*\underline{M_y}_F\).

Use the flabby cochain-sheaf resolution \(\mathcal C_F^\bullet(V)\) of a constant sheaf, constructed in Appendix C.2 of the first lesson. The product complex
\(\prod_y(j_y)_*\mathcal C_F^\bullet(M_y)\) is a flabby resolution of \(f^*T(M)\). To check exactness, take a product open \(U\times W\) with \(W\) a contractible coordinate ball. Its section complex is the product, over \(y\in U\), of the cochain-sheaf section complexes on \(W\). Each has cohomology \(M_y\) in degree zero and zero in higher degrees. Products of complexes of vector spaces preserve exactness, since coordinatewise surjections are surjective. This proves exactness on a basis and hence on stalks. Each term is flabby: closed direct image preserves flabbiness, and a product of surjective restriction maps is surjective. Thus this complex computes the derived direct image.

Over \(U\subset Y\), its direct-image section complex is
\(\prod_{y\in U}\Gamma(F,\mathcal C_F^\bullet(M_y))\). Its cohomology is the product of the groups \(H^i(F,M_y)\). The assumed fibre calculation proves (B.9) for \(T(M)\).

Set \(Q=T(M)/M\). Exactness of inverse image and the long exact direct-image sequence apply to
\(0\to f^*M\to f^*T(M)\to f^*Q\to0\).
Its degree-zero maps are the original maps \(M\to T(M)\to Q\), by the already proved unit isomorphism. Surjectivity onto \(Q\) gives \(R^1f_*f^*M=0\). For \(2\le i\le n\), the same sequence gives
\(R^if_*f^*M\simeq R^{i-1}f_*f^*Q\), because the adjacent higher images of \(T(M)\) vanish. Induction on \(i\), applied to all sheaves, proves the required vanishing for \(M\).

The calculation applies on every trivializing open of a bundle, so it proves (B.9) there and hence globally. Base change preserves these product trivializations, and the proof allowed arbitrary sheaves on the base. This gives the stated universality. \(\square\)

**Proposition B.6 (free frames and an explicit bound).** Suppose a complex linear algebraic group \(G\) is given as a closed subgroup of \(\operatorname{GL}_r\). Let
\[
V_{N,r}=\{A\in\operatorname{Mat}_{N\times r}(\mathbb C):
                  \operatorname{rank}A=r\},\qquad N\ge r.             \tag{B.11}
\]
It is smooth, connected and universally \(2(N-r)\)-acyclic over a point. The action \(h\cdot A=Ah^{-1}\) is free. Consequently \(V_{N,r}\times X\to X\), with the diagonal action, is an equivariant smooth universally \(2(N-r)\)-acyclic map of relative complex dimension \(Nr\).

**Proof.** The rank condition is the union of the open conditions that a specified maximal minor is invertible. Hence \(V_{N,r}\) is an open subvariety of affine \(Nr\)-space. Forgetting the last column maps it onto \(V_{N,r-1}\). Over a chart with a specified invertible \((r-1)\)-minor, complete the existing columns with the standard coordinate columns complementary to that minor. This gives an invertible matrix depending regularly on the existing frame. In these coordinates the last column is allowed precisely when its final \(N-r+1\) coordinates are not all zero. This constructs a local product with fibre
\[
\mathbb C^{r-1}\times(\mathbb C^{N-r+1}\setminus\{0\}).              \tag{B.12}
\]
Contract the first factor and retract the second radially to \(S^{2(N-r)+1}\). The cochain comparison, prism and hemisphere calculation of Appendix C.1–C.4 of the first lesson give \(H^0=V\) and zero cohomology in degrees \(1,\ldots,2(N-r)\), for any coefficient vector space \(V\). The same hemisphere calculation works with \(V\) in place of the one-dimensional coefficient field. These fibres are connected. Lemma B.5 applies to the displayed local products.

Compose the successive forgetful maps down to \(V_{N,0}=\operatorname{pt}\). All their acyclicity bounds are at least \(2(N-r)\). To justify composition, a map satisfying (B.9) has, for a sheaf \(M\), a unit cone in ordinary degrees at least \(n+1\). In a composite \(Z\xrightarrow fY\xrightarrow gW\), apply the left t-exact functor \(Rg_*\) to the unit cone for \(g^*M\). It still starts in degree \(n+1\). Together with the unit cone for \(g\), the composition of the two unit maps therefore induces an isomorphism through degree \(n\). This proves (B.9) for the composite. It works after every base change. Surjectivity and connectedness are also preserved here: a locally trivial bundle with connected base and connected fibre is connected, since the images of two complementary nonempty open-and-closed subsets would separate the base. Induction proves the assertions about \(V_{N,r}\).

If \(Ah^{-1}=A\), injectivity of the linear map \(A:\mathbb C^r\to\mathbb C^N\) gives \(h=1\). This proves freeness. Projection from \(V_{N,r}\times X\) is smooth of relative dimension \(Nr\), and is universally acyclic by the product case of Lemma B.5. With the diagonal action it is equivariant. \(\square\)

### B.3. The geometric quotient construction

The frame construction has a useful feature beyond freeness: the full general linear group acts on the frames, and its quotient is a Grassmannian. We will first take the quotient by the prescribed subgroup inside this frame bundle. We then attach the variety carrying the action. This produces actual geometric spaces and local sections for the comparisons below.

**Proposition B.6a (frame quotients and their charts).** Let \(G\subset H=\operatorname{GL}_r\) be a complex linear algebraic group, and let \(X\) be a separated finite-type complex variety with a \(G\)-action. Put \(V=V_{N,r}\). The quotient \(B=V/G\) is a smooth separated variety, and
\[
M_X=(V\times X)/G                                             \tag{B.12a}
\]
is a separated finite-type algebraic space. The maps \(V\to B\) and \(V\times X\to M_X\) are smooth \(G\)-torsors with étale-local sections. The same assertions hold with any nonempty finite product of frame spaces in place of \(V\). Equivariant maps induce maps of these quotients. For a projection removing one frame factor, the square formed with the two torsor maps is cartesian; on an étale cover of its target, the induced quotient map is projection from that frame factor.

Here algebraic spaces, rather than schemes, allow arbitrary separated \(X\); no equivariant ample line bundle on \(X\) is assumed. The scheme geometry used below is the Noetherian constructibility theorem of Quasi-finite morphisms and Chevalley's theorem, Theorem 4.2, and the smooth-coordinate and generic-smoothness theorems of Smooth morphisms, Theorems 4.1 and 6.1. The construction of the algebraic space from its relation, including descent of its diagonal, is given explicitly.

**Proof, first step: a finite-dimensional orbit for \(H/G\).** Write
\(A=\mathbb C[t_{ij},\det(t)^{-1}]\), and let \(I\) be the ideal defining \(G\) in \(H\). Choose finitely many generators of \(I\). There are integers \(m,d\) such that these generators and \(1\) belong to the finite-dimensional subspace
\[
W=\{\det(t)^{-m}P(t):\deg P\le d\}\subset A.
\]
Right translation \(R_hf(t)=f(th)\) preserves \(W\): it substitutes linear combinations for the matrix entries and multiplies the denominator by the scalar \(\det(h)^m\). These operators define an algebraic representation of \(H\). Set \(U=I\cap W\).

The scheme stabilizer of \(U\) is exactly \(G\). Indeed, for every complex algebra \(R\), an element of \(G(R)\) preserves the ideal of \(G_R\) by right translation, and hence preserves \(U_R\). Intersections commute with this base change because \(R\) is flat over the field \(\mathbb C\). Conversely, if \(h\in H(R)\) preserves \(U_R\), each chosen generator \(f\) satisfies \(R_hf\in I_R\). Evaluation at the identity gives \(f(h)=0\), so \(h\in G(R)\). This checks the stabilizer on arbitrary algebras, including those with nilpotents.

If \(G=H\), its quotient is a point. Otherwise \(u=\dim U>0\), and \(U\ne W\) because \(1\notin I\). In \(E=\bigwedge^uW\), take the line \(L=\bigwedge^uU\). It has the same stabilizer. To check this over a ring, choose a basis \(e_1,\ldots,e_u\) of \(U\), extend it to \(W\), and put \(w=e_1\wedge\cdots\wedge e_u\). Then
\[
U_R=\{v\in W_R:w\wedge v=0\}.
\]
This follows by expanding \(v\) in the basis: the coefficients outside \(U_R\) multiply distinct basis vectors in the exterior power. An automorphism preserving the line sends \(w\) to \(cw\) for a unit \(c\), so it preserves this kernel. Apply the same argument to its inverse to get equality. The converse follows by taking the determinant of its restriction to \(U_R\).

Consider the orbit \(O=H\cdot[L]\subset\mathbb P(E)\). Here is why it is locally closed. The image of the orbit map is constructible by the cited Noetherian Chevalley theorem. Its closure is irreducible, since \(H\) is irreducible. A dense constructible subset of an irreducible Noetherian space contains a nonempty open of that closure: in a finite union of locally closed pieces, one piece must have the full closure. Translate such an open by all \(h\in H(\mathbb C)\). The union is open in the orbit closure and contains exactly the orbit's closed points. Constructible subsets of a finite-type complex scheme are determined by their closed points, since every nonempty locally closed subset has such a point. Thus this union is the whole orbit. Give it its reduced locally closed scheme structure.

The action restricts to \(O\). One can check factorization on closed points here: \(H\times O\) is reduced, so a function vanishing at every closed point is zero; the preimage of the closed complement of the specified open has no closed points and is empty. Apply generic smoothness to \(O\to\operatorname{Spec}\mathbb C\). It gives a nonempty smooth open. Translations preserve smoothness and are transitive on the closed points, so every closed point of \(O\) is smooth. The nonsmooth locus is closed and has no closed points, hence is empty. The same argument, using generic smoothness for the dominant map \(H\to O\) and translations on source and target, proves that this orbit map is smooth everywhere. It is surjective by its construction.

The scheme stabilizer calculation identifies its relation explicitly:
\[
H\times G\xrightarrow{\sim}H\times_OH,
\qquad(h,g)\longmapsto(h,hg).                                \tag{B.12b}
\]
The inverse uses \(h^{-1}h'\); it belongs to \(G\) on every test algebra because \(h\) and \(h'\) send \(L\) to the same line. Consequently \(H\to O\) is the smooth torsor quotient \(H\to H/G\), with relative dimension \(g=\dim G\).

A smooth surjection here has étale-local sections for an explicit reason. At a closed point of a nonempty fibre, smooth coordinates factor a neighbourhood through an étale map to \(\mathbb A^g\) over the base. The coordinate values of that point lie in \(\mathbb C\). Pull the étale map back along the constant section with those values. The resulting étale neighbourhood maps to the original smooth source and supplies a section after base change. Its image is open and contains the chosen base point. Taking these neighbourhoods over closed base points covers the base, since its remaining closed complement would otherwise contain a closed point. This argument also applies to the later smooth torsors.

**Second step: put the orbit inside the frame bundle.** The column span map
\(V\to\operatorname{Gr}(r,N)\) is a Zariski-locally trivial right \(H\)-torsor. On a Grassmannian chart where one Plücker coordinate is nonzero, a plane has a unique matrix basis whose selected rows form the identity. Every frame of that plane is this basis multiplied by a unique \(h\in H\). These formulas give the chart and its inverse by matrix operations with the selected determinant inverted.

Replace each chart's factor \(H\) by \(O=H/G\). Changes of frame act by left multiplication on \(O\), so the resulting varieties glue over the Grassmannian. More concretely, the representation \(E\) gives an associated vector bundle. The \(H\)-stable closed orbit closure \(\overline O\subset\mathbb P(E)\) and its closed boundary \(\overline O\setminus O\) give closed subspaces of the associated projective bundle on every chart, agreeing on overlaps. Their difference is the glued variety \(B\). In particular it is separated and of finite type. Its charts are products of Grassmannian charts with the smooth variety \(O\), so \(B\) is smooth.

The map \(V\to B\) is locally the product with \(H\to O\). Hence it is smooth and surjective and has relation \(V\times G\simeq V\times_BV\). It represents the quotient sheaf, since a smooth surjection with the local sections just constructed is a cover and its fibres have exactly this relation. Choose an étale cover \(U_0\to B\) carrying a section \(s\) of \(V\). We can use a finite disjoint union of finite-type separated charts, because \(B\) is quasi-compact.

**Third step: attach \(X\) and prove representability.** Over \(U_0\), write a frame as \(v=s(u)h\). The invariant coordinate for the diagonal left action
\[
k\cdot(v,x)=(vk^{-1},kx)
\]
is \(z=hx\). Thus the local quotient is \(W_0=U_0\times X\). On \(U_0\times_BU_0\), let \(g_{ij}\) be defined by \(s_j=s_i g_{ij}\). The coordinates obey \(z_i=g_{ij}z_j\), and the equality \(g_{ij}g_{jk}=g_{ik}\) gives the cocycle. Set
\[
R_0=(U_0\times_BU_0)\times X,
\quad
s(i,j,z)=(j,z),\qquad t(i,j,z)=(i,g_{ij}z).          \tag{B.12c}
\]
Both maps are étale: one is base change of the cover and the other is that projection composed with an isomorphism. The unit, inverse and composition come respectively from the identity, \(g_{ij}^{-1}=g_{ji}\), and the cocycle. This is an equivalence relation as a functor, not merely on complex points. Its map to \(W_0\times_BW_0\) is a closed immersion: over \(U_0\times_BU_0\) it is the graph of the indicated automorphism of the separated variety \(X\).

Let \(M_X\) be the étale sheaf quotient by this relation. We verify the two conditions making it an algebraic space. First its diagonal over \(B\) is representable and closed. Given two maps \(T\to M_X\) with the same base map, an étale cover \(T'\to T\) lifts them to \(W_0\). Their equality locus there is the closed subscheme obtained by pulling back \(R_0\). On overlaps these closed subschemes agree as subfunctors: changing either lift by the equivalence relation does not change whether the pair is related. Their ideals therefore agree and descend.

For completeness, descent of these ideals uses the following elementary faithfully flat argument. Let \(A\to C\) be faithfully flat and \(J\subset C\) an ideal whose two extensions to \(C\otimes_AC\) agree. Put \(I=\ker(A\to C/J)\). Flatness identifies
\(IC=\ker(C\to(C/J)\otimes_AC)\). For \(j\in J\), equality of the two extended ideals makes \(1\otimes j\) zero in this last tensor product, so \(J\subset IC\). The reverse inclusion follows from the definition of \(I\). Uniqueness follows because \(A/I\to C/IC\) is injective. More generally the unit \(N\to N\otimes_AC\) is injective: after tensoring once more with \(C\) it has a left inverse given by multiplication of the two \(C\)-factors, and flatness and faithfulness detect the zero kernel. On affine pieces, a finite collection of affine étale covers gives such a faithfully flat product algebra. This proves descent and uniqueness of the ideals; the affine answers glue by uniqueness. We have constructed the closed equality subscheme of \(T\), proving the assertion about the diagonal.

It follows that \(W_0\to M_X\) is representable: for a scheme \(T\to M_X\), its fibre product is the pullback of that diagonal inside \(W_0\times_BT\). After an étale cover of \(T\) lifting to \(W_0\), this map is the base change of \(R_0\to W_0\). It is therefore étale and surjective, since these properties are local for the étale topology. This proves that \(M_X\) is an algebraic space with atlas \(W_0\). The same argument shows it is separated over \(B\); it is of finite type since its displayed finite-type atlas is quasi-compact. As \(B\) is separated over \(\mathbb C\), so is \(M_X\).

There is an invariant map \(V\times X\to M_X\), given in each chart by \((s(u)h,x)\mapsto(u,hx)\). Its pullback to \(W_0\) is
\[
G\times W_0\longrightarrow W_0,
\qquad (h,u,z)\longmapsto(u,z),
\]
with the corresponding point of \(V\times X\) equal to \((s(u)h,h^{-1}z)\). The group action sends \(h\) to \(hk^{-1}\). Thus this is a smooth torsor with a section, and the original map is a smooth \(G\)-torsor. These local formulas also identify \(M_X\) with the quotient of \(V\times X\), as asserted in (B.12a).

**Fourth step: products and comparison maps.** For
\(V_1\times\cdots\times V_a\times X\), apply the construction to \(V_1\) and the separated variety \(V_2\times\cdots\times V_a\times X\), carrying its diagonal action. This proves existence and the torsor assertion for every nonempty finite product.

An equivariant map between two such spaces descends to the quotient sheaves: apply it to a local lift, and equivariance makes different lifts equivalent. The descended map is unique, so composition is preserved. For the projection \(S=P\times_XR\to R\), the square
\[
\begin{array}{ccc}
S&\longrightarrow&R\\
\downarrow&&\downarrow\\
S/G&\longrightarrow&R/G
\end{array}                                                   \tag{B.12d}
\]
is cartesian. To check this, choose a local section of the torsor \(R\to R/G\). An orbit in \(S\) mapping to its base point has a unique representative whose image in \(R\) is that section: existence and uniqueness are precisely the torsor identity. This identifies both fibre products, compatibly on overlapping sections. In particular, if \(P=V_{N,r}\times X\), the lower map after this étale base change is \(V_{N,r}\times U\to U\). It is smooth of relative dimension \(Nr\).

Over \(\mathbb C\) these étale charts give analytic local sections. Indeed, the local coordinate description of an étale map has an invertible Jacobian, and the analytic inverse function theorem makes it a local analytic isomorphism. The quotient can equivalently be constructed by gluing the analytic products \(U\times X^{\mathrm{an}}\) with the displayed transition maps. The resulting space is Hausdorff: points over different base points separate in the Hausdorff base, and points over one base point separate in a common product neighbourhood. The torsors are locally trivial analytic bundles, and (B.12d) remains cartesian. Lemma B.5 and Proposition B.6 now make the lower projection universally \(2(N-r)\)-acyclic, with arbitrary base sheaf coefficients. This gives exactly the geometric maps used in the bounded-model comparison. \(\square\)

For example, with \(r=1\), \(G=\mathbb G_m\) and its weight-one action on \(X=\mathbb A^1\), the quotient is the tautological line bundle on \(\mathbb P^{N-1}\): the invariant map is \((v,z)\mapsto(\mathbb Cv,zv)\). For \(G=H\) and \(X\) a point, it is the Grassmannian itself. These examples check the right-frame/left-action convention in the construction. A disconnected \(G\) causes no change: connectedness in Proposition B.3 concerns the projection to \(X\), whose fibre is the connected frame space.

The stabilizer-line construction is also proved in Milne's freely available corrected *Algebraic Groups*, Theorem 4.27 and Lemma 4.28; its orbit quotient appears in Theorem 7.18. We used the explicit polynomial representation for \(\operatorname{GL}_r\), then the frame charts and the closed relation (B.12c) to construct the specific spaces required here. The proof does not construct quotients for arbitrary free actions. The remaining categorical inputs are constructible sheaf operations and descent on these algebraic spaces or their analytic charts, together with the precise operation compatibilities used below. Recursive verification of the cited scheme and analytic prerequisites is still required.

**Lemma B.7 (what an acyclic map preserves).** Let \(I=[a,b]\), write \(w=b-a\), and let \(f:Z\to Y\) be universally \(n\)-acyclic. If \(n\ge w\), then \(f^*:D_c^I(Y)\to D_c^I(Z)\) is fully faithful. Its essential image consists of the objects \(K\) for which the counit-induced map
\[
f^*\tau^{\le b}Rf_*K\longrightarrow K               \tag{B.13}
\]
is an isomorphism. Here direct image and the displayed truncation are assumed to preserve the specified constructible categories. If \(n>w\), pullback also identifies the \(\operatorname{Hom}(A,B[1])\) groups for \(A,B\in D_c^I(Y)\), reflects distinguished triangles with terms in \(D_c^I(Y)\), and has image in \(D_c^I(Z)\) closed under extensions and direct summands.

**Proof.** For a sheaf in ordinary degree \(j\), the unit cone begins in degree \(j+n+1\), by (B.9). The finite ordinary truncation triangles of \(B\in D_c^I(Y)\) therefore show that
\[
\operatorname{Cone}(B\longrightarrow Rf_*f^*B)
                 \in D^{\ge a+n+1}(Y).             \tag{B.14}
\]
At each step, the cones of the unit maps form an extension triangle, so this lower bound is preserved. For \(A\in D_c^I(Y)\), ordinary t-structure orthogonality makes maps from \(A\) to this cone and its shift by \(-1\) vanish when \(n\ge w\). Apply \(\operatorname{Hom}(A,-)\) to the unit triangle and use adjunction. This gives full faithfulness. If \(n>w\), the same argument with \(B[1]\) works because the lower bound in (B.14) decreases by one; it gives the assertion about degree-one Hom.

Put \(S_f(K)=\tau^{\le b}Rf_*K\). Left t-exactness of \(Rf_*\) puts this in \(D_c^I(Y)\). Equation (B.14) gives a natural isomorphism \(B\simeq S_f(f^*B)\). The adjunction identities show that (B.13) is its inverse after pullback when \(K=f^*B\). Conversely, if (B.13) is invertible, it explicitly writes \(K\) as the pullback of \(S_f(K)\). This proves the essential-image criterion. The criterion commutes with finite direct sums, so a direct summand of an object in the image also lies in the image.

For an extension triangle with outer terms \(f^*B_1,f^*B_2\), its connecting map lifts uniquely to \(B_2\to B_1[1]\) when \(n>w\). Complete that map to a triangle. Its middle object has ordinary cohomology in \(I\), by the cohomology sequence. Exactness of pullback identifies the pulled-back triangle with the given one, proving extension closure.

For reflection of triangles, let \(A_1\to A_2\to A_3\to A_1[1]\) have terms in \(D_c^I(Y)\), and suppose its pullback is distinguished. The cone \(C\) of its first arrow belongs to \(D_c^{[a-1,b]}(Y)\). The cone triangle after pullback is isomorphic to the given pulled-back triangle, through the identity on its first two terms. Since \(n>w\), full faithfulness applies on the enlarged interval \([a-1,b]\). It lifts this isomorphism \(f^*C\simeq f^*A_3\), its inverse and its compatibility with the other arrows. Thus the original diagram is isomorphic to a cone triangle and is distinguished. The unit/counit and interval arguments also hold in the ambient bounded-below category of all sheaves; constructibility is imposed when the resulting objects are used in \(D_c^I\). \(\square\)

The distinction between the two bounds is real. Projection \(\mathbb C^*\to\operatorname{pt}\) is universally \(0\)-acyclic, by Lemma B.5 and the circle calculation in the first lesson. For \(I=[0,0]\), it preserves morphisms between vector spaces. But \(\operatorname{Hom}(\Lambda,\Lambda[1])=0\) over the point, whereas after pullback this group is \(H^1(\mathbb C^*,\Lambda)=\Lambda\). Thus the bound \(n\ge w\) alone does not preserve extension classes.

We will use two locality consequences, and record their proofs. First, (B.9) descends along a surjection \(t:Y'\to Y\) with local sections: near any point choose a section, so the original map on that open is a base change of the pulled-back map. Unit isomorphisms and cohomology sheaf vanishing can be checked on these opens. Apply this also after an arbitrary base change to get universality. Second, for an acyclic \(f\), membership in the image in Lemma B.7 can be checked after such a \(t\). If the pullback of \(K\) is a pullback from \(Y'\), pull its presentation back along each local section to obtain a presentation of \(K\) on the corresponding open of \(Y\). On each open (B.13) is invertible. Ordinary direct image commutes with restriction to base opens, as does its derived functor by restriction of an injective resolution. Thus (B.13) is invertible globally. This argument requires no general descent assertion for arbitrary complexes.

**Proposition B.8 (comparison of bounded resolution models).** Let \(P\xrightarrow\pi X\) and \(R\xrightarrow\rho X\) be free \(G\)-spaces over \(X\) with geometric torsor quotients. Suppose \(\pi\) is universally \(n\)-acyclic with \(n>b-a\), and the quotient of \(S=P\times_XR\) is supplied too. In a resolution triple as in (B.5), now allow \(A\in D_c^I(X)\) in place of a perverse \(A\). Denote its category by \(\mathcal T_\pi^I(X)\), and similarly for \(\rho\). Pullback along \(S\to R\) gives an equivalence
\[
\mathcal T_\rho^I(X)\xrightarrow{\sim}
                         \mathcal T_{S\to X}^I(X). \tag{B.15}
\]
If both \(\pi\) and \(\rho\) satisfy the bound, both product projections give equivalences, hence a canonical comparison between their models.

**Proof.** Write \(Z=R/G\), \(W=S/G\), and \(v:S\to R\), \(\bar v:W\to Z\) for the induced maps. The square with vertical torsor maps and horizontal maps \(v,\bar v\) is cartesian. Indeed on a local section chart of \(R\to Z\), write \(R=G\times U\). Equivariance identifies \(S\) there with \(G\) times its restriction over \(\{1\}\times U\); this gives exactly \(S=R\times_ZW\). The identification glues because the maps are the original quotient maps. The map \(v\) is a base change of \(\pi\), and so is universally \(n\)-acyclic. The first locality consequence shows that \(\bar v\) is universally \(n\)-acyclic as well.

In every bounded triple the quotient complex lies in \(D_c^I\), since torsor pullback is conservative and exact for the ordinary t-structure. For a triple \((A,C,\gamma)\) on \(S\), its quotient complex \(C\) pulls back to \(v^*\rho^*A\). The second locality consequence, applied to \(\bar v\) and the torsor \(R\to Z\), shows that \(C\) comes from \(B\in D_c^I(Z)\). Lemma B.7 gives this \(B\), its identification \(\bar v^*B\simeq C\), and uniqueness on morphisms. Now \(\gamma\) is an isomorphism between the pullbacks by \(v\) of \(q_R^*B\) and \(\rho^*A\). Full faithfulness for \(v\) lifts it, and its inverse, uniquely to \(\beta:q_R^*B\simeq\rho^*A\). This constructs a triple on \(R\).

For a morphism on \(S\), full faithfulness for \(\bar v\) uniquely lifts its quotient component. Faithfulness for \(v\) makes the lifted component compatible with its map on \(X\). These constructions are inverse to pullback on both objects and morphisms, proving (B.15). If \(\rho\) is also sufficiently acyclic, exchange \(P\) and \(R\). \(\square\)

The comparisons are coherent. For three resolutions, pull the comparisons to their triple product. Each projection which removes one sufficiently acyclic factor gives an equivalence by Proposition B.8. There all comparisons are the same pullback identification. Full faithfulness then gives a unique comparison downstairs. On a product of four resolutions the same argument makes the two composites of these comparisons equal, proving the coherence identity. An actual map between two sufficiently acyclic resolutions gives this comparison too: factor it through its graph in their product. Pullback by the graph is inverse to pullback by the projection whose composite with that graph is the identity. This also identifies the natural composition maps.

**Theorem B.9 (derived construction from the frame quotients).** Let \(G\subset\operatorname{GL}_r\) and the separated complex variety \(X\) be as in Proposition B.6a. Use the bounded constructible operations and descent on its separated finite-type algebraic spaces. Proposition B.6a supplies the geometric quotient torsors, all finite products of frame models over \(X\), and the induced quotient maps. The bounded models above construct a triangulated category \(D_{G,c}^b(X)\), independent of the sufficiently acyclic resolutions. It has the perverse t-structure detected by its underlying object on \(X\). Its perverse heart is the equivariant heart of (3.3).

**Proof.** For each finite interval \(I\), choose \(N\) with \(2(N-r)>b-a\) and form \(\mathcal T_{V_{N,r}\times X}^I(X)\). Proposition B.8 identifies any two choices, with the just-proved coherence. If \(I\subset J\), choose a resolution sufficiently acyclic for \(J\). Its \(I\)-model is the full subcategory of its \(J\)-model on objects with underlying complex in \(I\). The comparisons preserve that complex, so these full embeddings are independent of the choices. Taking their increasing union defines objects and morphisms of \(D_{G,c}^b(X)\): each finite collection is represented in one sufficiently large interval and one sufficiently acyclic resolution. Coherence identifies different such representations.

Here is the triangulated structure, rather than an assumption that a category of triples is automatically triangulated. On a sufficiently acyclic resolution \(\pi:P\to X\), projection of a bounded triple to its quotient complex \(B\) is fully faithful. Given a map \(B\to B'\), its pullback and the two comparison isomorphisms give a map \(\pi^*A\to\pi^*A'\); Lemma B.7 lifts it uniquely to \(A\to A'\). Its image is exactly the quotient complexes whose pullback comes from \(X\).

For a morphism of triples, choose a larger interval containing its two underlying complexes and their cone, and choose a resolution acyclic for that interval. Take the cones of the two components. The compatibility square and the cone triangles give an isomorphism between their pullbacks: complete the two given isomorphisms to a morphism of cone triangles, and the cohomology sequence makes its third component an isomorphism. Thus the cone is again a triple. Define distinguished triangles by these componentwise cone triangles. Shifts are componentwise shifts.

All triangulated axioms can now be verified on a common sufficiently acyclic resolution. For a finite diagram, enlarge the interval to contain the cones and shifts appearing in the axiom. Projection to quotient complexes is fully faithful there. A triangle of triples whose quotient triangle is distinguished also has distinguished underlying triangle: pull it back to the resolution using its comparison isomorphisms, then apply triangle reflection in Lemma B.7. The identity and rotation axioms therefore follow from those of the quotient derived category. A filler for a morphism of triangles is obtained there and lifts by full faithfulness. For the octahedral axiom, form the usual octahedron for the two quotient morphisms and their composite; its cone vertices are triples by the preceding cone construction. Its arrows and commuting diagrams lift by full faithfulness, and its distinguished triangles reflect as just proved. Different cone choices are isomorphic through the identity on the first two terms, and this isomorphism lifts as well. Product comparison is an exact pullback on each component, so it preserves these triangles and the verification is independent of the model. This proves the claimed triangulated structure.

Finally impose perverse bounds on the underlying \(A\). For a smooth resolution of relative dimension \(d\), with \(g=\dim G\), its comparison isomorphism identifies \(\pi^*A[d]\) with \(q^*(B[d-g])[g]\). Both normalized pullbacks are t-exact and conservative, so \(A\) has a given perverse bound exactly when \(B[d-g]\) has it. Orthogonality follows by projecting morphisms to the quotient derived category and applying that perverse t-structure. For existence, first choose an interval containing \(A\) and its two perverse truncations, then a sufficiently acyclic resolution. Perverse truncation of \(B[d-g]\), followed by the shift \([g-d]\), is compatible with the truncation of \(A\), by normalized smooth t-exactness. It gives two triples and a componentwise distinguished truncation triangle. Shift stability holds on \(A\); hence these cuts form a t-structure. Its truncations are independent of the model by the orthogonality and uniqueness of a truncation triangle.

Every heart object is therefore represented by a triple with perverse \(A\). Proposition B.3 recovers its equivariant structure; Corollary B.4 makes this independent of the resolution and compatible with morphisms. Conversely an equivariant perverse \(A\) gives such a triple by that proposition, after choosing the resolution sufficiently acyclic for an interval containing \(A\). The constructions are inverse on objects and morphisms. This identifies the heart and completes the construction with the specified constructible-operation and descent inputs. \(\square\)

The free author-hosted Bernstein–Lunts Part I, §§1.9, 2 and 3.1, supplies the primary comparison for these definitions and the resolution approach. The arguments above include the arbitrary-base-sheaf calculation, the full-rank-frame bound, the bounded unit/counit criterion, the resolution comparison and the triangulated and perverse constructions. Proposition B.6a now supplies the actual geometric frame quotients, their torsor charts and their product comparison maps. The exact earlier operation foundations and the recursive prerequisites of its scheme and analytic steps remain to be verified; the existence of these spaces alone does not prove constructible descent or higher-stack operations.

## Exact prerequisites still required

The action and finite-orbit arguments use the earlier perverse smooth-pullback, finite-length, intermediate-extension and local-cycle constructions at their exact coefficient and geometric scope. The normalized atlas proof assumes coherent derived smooth descent and constructible operations; ordinary cohomology-sheaf descent alone is insufficient. For nonsmooth stabilizers in positive characteristic the local-system argument additionally requires fppf descent.

Appendix A retains the excellent base with dimension functions, locally bounded integer admissible perversity, principal complete adic coefficients with zero-dimensional Gorenstein quotients, local cohomological boundedness, regular purity, constructible recollement and enhanced higher smooth hyperdescent. It constructs the bounded perverse cuts after those operations exist. The scheme/DVR pro-etale completion provider has a smaller scope and does not discharge the full higher-stack formalism.

Appendix B constructs torsor heart descent, free-frame acyclicity, the actual complex quotient spaces and their product maps, bounded interval comparison, and the triangulated/perverse category. The quotient proof uses the specified Noetherian image and smooth-coordinate/generic-smoothness results and analytic inverse function theorem. Its ideal-descent argument is written locally. All recursive scheme, analytic and constructible-operation foundations must still be verified; this construction does not prove arbitrary free-action quotients or the positive-characteristic nonsmooth case.

The Bruhat/root geometry, full geometric Kazhdan-Lusztig theorem, general regular-integral Verma multiplicities and exact localization/Riemann-Hilbert comparison remain proof obligations. Section 5 proves the rank-one Verma calculation directly; Exercise 5 proves its particular IC stalks by a small resolution. The universal Chern class, stack compactness example and broader Satake, BunG and v-stack results retain their exact further inputs. Neither those examples nor a reference to a free text supplies the missing general proofs.

## References

- Y. Laszlo, M. Olsson, [*Perverse t-structure on Artin stacks*](https://www.cmls.polytechnique.fr/perso/laszlo/articleweb/faisceaux-pervers.pdf), author-hosted 16-page preprint of the 2009 publication; freely readable.
- Y. Liu, W. Zheng, [*Enhanced adic formalism and perverse t-structures for higher Artin stacks*](https://arxiv.org/abs/1404.1128v2), arXiv:1404.1128v2 (26 September 2017); freely readable supplied LaTeX and PDF.
- P. Baumann, S. Riche, [*Notes on the geometric Satake equivalence*](https://www.math.unistra.fr/~baumann/Satake-luminy.pdf), Appendix A.1, Proposition A.2.
- M. Kashiwara, T. Tanisaki, [*Parabolic Kazhdan–Lusztig polynomials and Schubert varieties*](https://arxiv.org/abs/math/9908153), Theorem 5.4 and Proposition 5.2.
- M. Kashiwara, T. Tanisaki, [*Kazhdan–Lusztig conjecture for symmetrizable Kac–Moody Lie algebras. III: Positive rational case*](https://arxiv.org/abs/math/9812053), Theorem 1.1, equation (1.5), and Theorems 1.2–1.3.
- D. Arinkin, D. Gaitsgory, D. Kazhdan, S. Raskin, N. Rozenblyum, Y. Varshavsky, [*The stack of local systems with restricted variation and geometric Langlands theory with nilpotent singular support*](https://arxiv.org/abs/2010.01906), Appendices C and D.
- L. Fargues, P. Scholze, [*Geometrization of the local Langlands correspondence*](https://arxiv.org/abs/2102.13459), Definition IV.1.1, Propositions VI.4.1–VI.4.2, and Definition/Proposition VI.7.1 through Proposition VI.7.4.
- A. Beilinson, J. Bernstein, P. Deligne, [*Faisceaux pervers*](https://publications.ias.edu/sites/default/files/Faisceaux%20pervers.pdf), Astérisque 100 (1982); freely readable IAS scan.
- J. S. Milne, [*Algebraic Groups*](https://www.jmilne.org/math/Books/iAG2022.pdf), freely available corrected 2022 author edition, Theorem 4.27, Lemma 4.28 and Theorem 7.18.
