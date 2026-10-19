# Abelian varieties

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A proper group scheme has no room for a function to escape to infinity. That simple observation becomes rigidity: a family of maps cannot start by collapsing a whole proper fibre and then vary freely. For abelian varieties it forces commutativity and controls line bundles under addition. The theorem of the cube turns that control into a quadratic formula for multiplication, from which the degree of the torsion schemes follows.

We work over an arbitrary field, including imperfect fields and positive characteristic. We prove a relative theorem of the cube on a connected parameter scheme, so its proof retains nilpotent parameters. The Picard identity component, its normalized Poincaré bundle, the ample dual map and Poincaré reducibility are proved in6.11–6.20. Cohomology and base change, elementary properties of ample line bundles and faithfully flat descent are prerequisites.

## 1. Proper groups that remain integral

An **abelian variety** over \(k\) is a group scheme \(A/k\) whose underlying scheme is proper and geometrically integral. In particular it is of finite type and separated. Write \(0\) for its identity and \(g=\dim A\). Commutativity and projectivity will be consequences of this definition.

**Lemma 1.1. Constants and field extension.** An abelian variety remains an abelian variety after every field extension. If \(X/k\) is a proper geometrically integral scheme, then

\[
\Gamma(X,\mathcal O_X)=k,\qquad
\Gamma(X\times_k\operatorname{Spec}R,\mathcal O)=R
\tag{1}
\]

for every \(k\)-algebra \(R\).

**Proof.** Group operations and their identities base change. Properness and geometric integrality are preserved by field extension, proving the first assertion.

Proper coherent cohomology makes \(\Gamma(X,\mathcal O_X)\) finite-dimensional over \(k\). Over an algebraic closure, this algebra is a domain because the scheme is integral; a finite-dimensional domain over an algebraically closed field is that field. Flat base change for \(H^0\) therefore gives

\[
\Gamma(X,\mathcal O_X)\otimes_k\overline k
=\Gamma(X_{\overline k},\mathcal O)=\overline k.
\]

The left side has dimension \(\dim_k\Gamma(X,\mathcal O_X)\) over \(\overline k\), so that dimension is one and the unit map from \(k\) is an isomorphism. Every \(k\)-algebra is flat as a \(k\)-module. Applying the same flat base-change statement to \(R\) proves the second formula. The formulas also give \(p_*\mathcal O_{X\times Y}=\mathcal O_Y\) for any \(k\)-scheme \(Y\), by checking on its affine opens. \(\square\)

The last base-change calculation only requires \(X\) proper and \(H^0(X,\mathcal O_X)=k\); geometric integrality supplied that condition here.

**Proposition 1.2. Smoothness and projectivity.** Every abelian variety is smooth and projective over its field.

**Proof.** Over an algebraic closure, \(A\) is reduced and of finite type. The reduced-group smoothness theorem over a perfect field, proved in *Lie algebras and smoothness of group schemes*, makes it smooth there. Smoothness descends through the faithfully flat field extension, so \(A/k\) is smooth. This argument uses geometric reducedness and therefore applies equally to imperfect \(k\).

The quasi-projectivity theorem proved in *Group schemes over a field* supplies a locally closed immersion \(A\hookrightarrow\mathbf P^N_k\). Since \(A\) is proper and the target is separated, this morphism is proper: its graph is closed, and projection from \(A\times\mathbf P^N\) to \(\mathbf P^N\) is proper. A proper locally closed immersion is a closed immersion. Thus \(A\) is projective. \(\square\)

If \(g=0\), geometric integrality makes \(A\) a single geometrically reduced point; its \(k\)-rational identity then identifies it with \(\operatorname{Spec}k\). We will keep this case explicit when discussing multiplication. *Comparison locators:* [Stacks, Tags 03RO, 0BFA–0BFC].

### Translation makes the tangent bundle constant

**Proposition 1.3. Invariant tangent vectors and differential forms.** If \(A/k\) is an abelian variety of dimension \(g\), then

\[
\begin{gathered}
T_{A/k}\simeq\mathcal O_A\otimes_kT_{A,0},\\
\Omega^r_{A/k}\simeq\mathcal O_A\otimes_k\bigwedge^rT_{A,0}^{\vee}.
\end{gathered}
\]

In particular its canonical bundle is trivial. Every global vector field and every global differential form is translation invariant.

**Proof.** On \(A\times A\), differentiate addition in its second variable at \(A\times\{0\}\). This gives an \(\mathcal O_A\)-linear map from the constant bundle with fibre \(T_{A,0}\) to \(T_{A/k}\). Its fibre at a geometric point \(a\) is \(d(t_a)_0\), an isomorphism with inverse \(d(t_{-a})_a\). The determinant therefore vanishes nowhere, proving that the bundle map is an isomorphism. Translation composition shows its compatibility with every translation, including translations by points over a test scheme. Dualizing and taking exterior powers gives the form-bundle formula. Finally \(H^0(A,\mathcal O_A)=k\), by Lemma 1.1, so every global section of a constant bundle has constant coefficients. This proves all the invariance assertions. \(\square\)

**Corollary 1.4. No rational curves.** Every morphism \(\mathbf P^1_k\to A\) is constant.

**Proof.** We may extend \(k\) to an algebraic closure: constancy there implies constancy over \(k\), by descent of equality with the constant map at the rational point \(\infty\). Suppose first that a morphism \(f\) has a nonzero differential. Proposition 1.3 supplies a global form on \(A\) whose pullback is nonzero at a point where \(df\ne0\). But \(\Omega^1_{\mathbf P^1}\simeq\mathcal O(-2)\) has no global section. This is a contradiction.

In characteristic zero, a nonconstant rational function has nonzero differential, so a nonconstant \(f\) has nonzero differential. In characteristic \(p\), if \(df=0\), all rational coordinate functions of \(f\) lie in \(k(t^p)\): writing a rational function in the basis \(1,t,\ldots,t^{p-1}\) over \(k(t^p)\) proves that this field is exactly the kernel of \(d/dt\). Thus the rational map factors through \(t\mapsto t^p\) on \(\mathbf P^1\). The resulting rational map to \(A\) extends to a morphism, because the local ring at every missing point is a DVR and \(A\) is proper. Repeat if its differential is still zero. For a fixed nonconstant coordinate function of degree \(d\), each factorization divides its degree by \(p\); therefore this process terminates. It produces a nonconstant morphism with nonzero differential, already ruled out. \(\square\)

### Ampleness over imperfect fields

**Proposition 1.5. Ampleness and the ground field.** On a proper finite-type scheme over a field, the tensor product of ample line bundles is ample, and an ample line bundle restricts to an ample bundle on every closed subscheme. A line bundle is ample if and only if it becomes ample over an algebraic closure. If a proper scheme becomes projective over an algebraic closure, it is projective over the original field.

**Proof.** Choose a common power of two ample bundles that makes both very ample. Their two embeddings, followed by the Segre embedding, give an embedding defined by products of sections of their tensor product. This subsystem generates that product and separates points and tangent vectors. Lemma 1.6, which applies to any proper scheme, shows that its full system also embeds. This proves the tensor-product assertion. Restricting an embedding to a closed subscheme proves the restriction assertion: the restricted sections form an embedding subsystem of the complete space of sections.

Field extension preserves these embeddings. Conversely, suppose \(L_{\bar k}^n\) is very ample. Proper coherent cohomology and field base change give
\[
H^0(X_{\bar k},L_{\bar k}^n)
=H^0(X,L^n)\otimes_k\bar k.
\]
The evaluation map downstairs is surjective because it becomes surjective after the faithfully flat field extension. Its morphism to projective space becomes a closed immersion, so it is a closed immersion by faithfully flat descent of closed immersions. Thus \(L\) is ample.

For the last assertion choose an ample bundle \(N\) on \(X_{\bar k}\). Its finitely many transition functions and their inverse and cocycle identities descend to \(X_K\) for a finite extension \(K/k\). This follows by taking a finite affine trivializing cover and descending its finitely presented opens, functions and identities; all coefficients used belong to a finite extension. The descended bundle is ample by the assertion just proved, applied over \(K\). The finite locally free projection \(p:X_K\to X\), of rank \(r=[K:k]\), has the norm line
\[
\operatorname{Nm}_p(N)=\det(p_*N)\otimes\det(p_*\mathcal O_{X_K})^{-1}.
\]
Here \(p_*N\) is locally free of rank \(r\). On an affine base the invertible module over its finite locally free algebra is finite projective over the base, as a summand of a finite sum of that algebra; its fibre dimension is \(r\). It can locally be trivialized as a rank-one module over the algebra on inverse images of base opens. Indeed on a finite Artin fibre every invertible module is free, by its product decomposition into local algebras and Nakayama. Lift a generator. Its cokernel has closed image in the base under the finite map and misses the chosen point; remove that image. The resulting surjection between rank-one algebra modules is an isomorphism. These base opens cover \(X\). In such a trivialization the norm transition is the determinant of multiplication by the transition unit on the rank-\(r\) algebra. Determinants are multiplicative, so this agrees with the displayed determinant-line definition.

Over \(\bar k\), the algebra \(K\otimes_k\bar k\) is a product of local Artin algebras. Write \(\ell_\sigma\) for their lengths and \(N_\sigma\) for the corresponding residue-field conjugate bundles on \(X_{\bar k}\). A multiplication operator on a local Artin algebra has determinant equal to the \(\ell_\sigma\)-th power of its residue: a composition series proves this by triangular matrices. Consequently
\[
\operatorname{Nm}_p(N)_{\bar k}
\simeq\bigotimes_\sigma N_\sigma^{\otimes\ell_\sigma}.
\]
Every \(N_\sigma\) is ample, so their product is ample. Field descent of ampleness makes the norm ample on \(X\). This proves projectivity, including inseparable extensions; no assumption that \(k\) is perfect is needed. \(\square\)

**Lemma 1.6. The point-and-tangent closed-immersion criterion.** Let \(X/k\) be proper of finite type, and let a generated finite-dimensional system of sections define \(f:X\to\mathbf P^N_k\). If it separates all geometric points and all nonzero tangent directions at geometric points, then \(f\) is a closed immersion.

**Proof.** Extend the field to an algebraic closure. Point separation makes every fibre contain at most one point, so \(f\) is quasi-finite. The morphism is proper, because its source is proper and its target separated. The already-proved proper quasi-finite theorem, [Zariski's main theorem](../../AG-MO/src/zariskis-main-theorem.md), Theorem 5.1, makes it finite. At a point the injective tangent map makes the fibre's cotangent space zero. Its finite local algebra has residue field \(k\) and maximal ideal equal to its square; Nakayama makes that maximal ideal zero. Thus every nonempty fibre has length one. At a target local ring in the image, \(1\) generates the finite module \(f_*\mathcal O_X\) modulo the maximal ideal. Nakayama makes the unit map \(\mathcal O_{\mathbf P^N}\to f_*\mathcal O_X\) surjective there. Outside the image its target is zero, so it is surjective there as well. These surjections say exactly that \(f\) is a closed immersion. Closed immersions descend by faithfully flat ideal descent, proving the assertion over \(k\). This argument uses no ampleness theorem for abelian varieties. \(\square\)

## 2. Rigidity of maps

The local assertion below needs no connectedness assumption on the parameter scheme. Connectedness and a separated target supply its global form.

**Theorem 2.1. Rigidity.** Let \(X/k\) be a nonempty proper scheme with \(H^0(X,\mathcal O_X)=k\), let \(Y/k\) be a scheme, and let \(f:X\times_kY\to Z\) be a morphism.

If the fibre over a point \(y_0\in Y\) maps to a single point of \(Z\), there is an open neighbourhood \(U\) of \(y_0\) and a morphism \(h:U\to Z\) with

\[
f|_{X\times U}=h\circ\operatorname{pr}_U.
\tag{2}
\]

If in addition \(Y\) is connected and \(Z\) is separated over \(k\), this factorization holds over all of \(Y\), and \(h\) is unique.

**Proof.** Choose an affine open \(V\subset Z\) containing the fibre's image. The closed subset \((X\times Y)\setminus f^{-1}(V)\) has closed image under the proper projection to \(Y\). Its image misses \(y_0\). Remove that image to obtain \(U\), so that \(f(X\times U)\subset V\).

For an affine open \(U'=\operatorname{Spec}R\subset U\), formula (1), in its \(H^0(X)=k\) form, identifies the ring map defining \(f:X\times U'\to V\) with a ring map \(\Gamma(V,\mathcal O_V)\to R\). This gives the required \(h\) on \(U'\). These maps agree on overlaps: their pullbacks agree, and the projection \(X\times U'\to U'\) is faithfully flat. They glue, proving the local assertion. In particular the factorization is an equality of morphisms even for a nonreduced \(U\).

For the global assertion, on \(X\times X\times Y\) consider the two maps

\[
(x,x',y)\longmapsto f(x,y),\quad f(x',y).
\]

Their equalizer \(E\) is closed because \(Z\) is separated. Projection \(q:X\times X\times Y\to Y\) is flat, of finite presentation and surjective, hence open. Consequently

\[
C=Y\setminus q\bigl((X\times X\times Y)\setminus E\bigr)
\tag{3}
\]

is closed. Its points are exactly the points whose fibre is contracted. To check this set-theoretic description, extend the residue field to an algebraic closure and compare any two geometric points of \(X\). If every pair has equal image, the image is a single point. The affine-open argument just given then makes the contraction a scheme-theoretic factorization through the residue-field point.

At every point of \(C\), the local assertion supplies a neighbourhood on which all fibres are contracted. Thus \(C\) is also open. It contains \(y_0\), and connectedness gives \(C=Y\). The local factorizations now cover \(Y\) and glue uniquely by faithful flatness of \(X\times Y\to Y\). This proves both existence and uniqueness. \(\square\)

The connectedness condition cannot be omitted from the global assertion. Take \(X=\mathbf P^1\), let \(Y\) be two disjoint points, and use the constant map to \(\mathbf P^1\) on the first component of \(X\times Y\) and the identity on the second. One fibre is contracted but no global factorization exists. The separatedness condition was used to close the equalizer in (3).

**Corollary 2.2. Commutativity.** The group law of an abelian variety is commutative.

**Proof.** Initially write the group law multiplicatively. Its commutator morphism is

\[
c:A\times A\longrightarrow A,\qquad
c(x,y)=xyx^{-1}y^{-1}.
\]

Use the second copy of \(A\) as \(X\) and the first as the connected parameter \(Y\). For \(x=0\), this map is constant at \(0\). Theorem 2.1 makes \(c\) independent of \(y\). Evaluating at \(y=0\) shows that the remaining map is also constantly \(0\). The equality of morphisms \(c=0\) proves commutativity on every test scheme. \(\square\)

We henceforth write addition. For every integer \(n\), multiplication is the homomorphism \([n]:A\to A\).

**Corollary 2.3. Morphisms are translations of homomorphisms.** For abelian varieties \(A,B/k\), every morphism \(f:A\to B\) has the unique form

\[
f=t_b\circ u,\qquad b=f(0)\in B(k),
\tag{4}
\]

where \(u:A\to B\) is a group homomorphism and \(t_b\) is translation by \(b\).

**Proof.** Replace \(f\) by \(u=t_{-f(0)}\circ f\), so \(u(0)=0\). Consider

\[
v(x,y)=u(x+y)-u(x)-u(y).
\]

It is zero for \(y=0\). Rigidity makes it independent of \(x\); its value at \(x=0\) is zero as well. Hence \(v=0\), exactly the homomorphism identity. The condition at \(0\) determines \(b\), then \(u\), proving uniqueness. \(\square\)

*Comparison locators:* [Stacks, Tag 0BFD] for commutativity and [Stacks, Tag 0AH8] for the local proper-fibre argument. The proof above supplies the explicit global rigidity statement.

### Maps from products and rational maps

**Corollary 2.4. The origin determines the law; maps out of products split.** There is at most one abelian-variety structure on a proper variety \(X\) with a prescribed rational identity \(e\). If \(V,W/k\) are proper geometrically integral schemes with rational points \(v_0,w_0\), and \(h:V\times W\to A\) satisfies \(h(v_0,w_0)=0\), then uniquely

\[
h(v,w)=f(v)+g(w),\quad f(v_0)=g(w_0)=0.
\]

**Proof.** The identity morphism between two proposed structures sends origin to origin. Corollary 2.3 makes it a homomorphism, which says that the two multiplication morphisms agree; the inverse morphisms then agree as well. For the second assertion put \(f(v)=h(v,w_0)\), \(g(w)=h(v_0,w)\). The difference \(h-f-g\) is zero on both coordinate slices. Apply Theorem 2.1 with \(V\) as the proper factor and \(W\) as the connected parameter. The difference factors through \(W\), and evaluation at \(v_0\) makes it zero. Restriction to the slices proves uniqueness. The equalities are scheme identities and survive all base changes. \(\square\)

For example \(\operatorname{Hom}(A_1\times A_2,B_1\times B_2)\) is the group of \(2\times2\) matrices whose \(ji\)-entry belongs to \(\operatorname{Hom}(A_i,B_j)\). Indeed restrict a homomorphism to the two factor inclusions, then use additivity; composing two maps gives the usual matrix multiplication with composition in the entries. General morphisms additionally have the unique translation specified in Corollary 2.3.

**Theorem 2.5. Rational maps from a smooth source extend.** Let \(V/k\) be a smooth variety and \(A/k\) an abelian variety. Every rational map \(f\colon V\dashrightarrow A\) extends uniquely to a morphism on \(V\).

**Proof.** We first work over an algebraically closed field, on one irreducible smooth component. Let \(U\) be the maximal domain of \(f\). At a codimension-one point the source local ring is a DVR, so properness of \(A\) extends the rational map over that ring. Its finitely many affine coordinates spread the extension to a neighborhood. Thus \(V\setminus U\) has codimension at least two.

On \(U\times U\) form \(F(v,w)=f(v)-f(w)\), and let \(W\subset V\times V\) be its maximal domain. We prove that \(W\) contains the diagonal. Fix a closed diagonal point \(x=(v,v)\), and choose an affine neighborhood \(H\subset A\) of the origin. The map \(F\) takes the dense defined part of the diagonal to the origin, so its inverse image of \(H\) is a nonempty, hence dense, open of the integral product. Pull back generators of the coordinate algebra of \(H\) to rational functions on \(V\times V\). This uses functions on the affine open, and does not assume that \(F\) is dominant.

If all these rational functions belong to the regular local ring \(\mathcal O_{V\times V,x}\), their algebraic relations hold there and define a morphism to \(H\). The map spreads to a neighborhood of \(x\), giving \(x\in W\). Otherwise one of these functions has a polar prime divisor \(D\) through \(x\). To justify this implication, the regular local ring is a UFD by [Regular local rings](../../AG-CA/src/regular-local-rings.md), Theorem 5.3: write the rational function as a reduced fraction and take an irreducible denominator. Shrinking near \(x\) makes that prime divisor a component of its nonregular locus. It misses the part of the diagonal in \(U\), because there \(F\) is the constant origin and is \(H\)-valued.

A local equation of \(D\) therefore restricts to a nonzero function on the regular integral diagonal: if the restriction were zero, \(D\) would contain its dense part in \(U\). The restriction vanishes at \(x\). Its zero set on the diagonal has codimension one by the one-equation dimension theorem. But this zero set is contained in the diagonal copy of \(V\setminus U\), which has codimension at least two. This contradiction proves \(x\in W\). All closed diagonal points are in \(W\); its closed complement therefore misses the entire diagonal.

Put \(W_0=W\cap(V\times U)\). Projection \(p:W_0\to V\) on the first coordinate is smooth and surjective. Its fibre at a geometric point \(v\) is an open of the second copy of \(V\) containing \(v\), intersected with the dense \(U\), so it is nonempty. On this faithfully flat cover define
\[
g(v,u)=F(v,u)+f(u).
\]
It equals \(f(v)\) where the latter is defined. The two pullbacks of \(g\) to \(W_0\times_VW_0\), an open of the smooth reduced \(V\times U\times U\), agree on the dense open with first coordinate in \(U\). Separatedness of \(A\) makes them equal everywhere. The proved faithfully flat descent of morphisms in [Quotients and torsors](quotients-and-torsors.md), Section 1, descends \(g\) to the required morphism on \(V\). Density and separatedness give uniqueness.

Over an arbitrary field, apply this argument to the irreducible smooth components after algebraic closure; their disjoint open-and-closed decomposition lets the extensions glue. Uniqueness gives the descent identities even on a possibly nonreduced double field extension. More explicitly, the original dense open \(U\subset V\) is universally schematically dense: on an affine regular component, a principal open contained in \(U\) is defined by a nonzerodivisor, and its multiplication map stays injective after tensoring with any \(k\)-algebra. An ideal vanishing on \(U\) after such a base change is therefore zero. The equalizer ideals of the two proposed extensions consequently vanish on the whole double extension, so faithfully flat descent applies. This proves existence and uniqueness over \(k\). \(\square\)

The preceding argument is the field form of the difference-map proof already given in [Néron models](neron-models.md), Theorem 2.2. Its use of an affine neighborhood of the identity fixes the unnecessary function-field-injectivity assumption in the mapped proof.

## 3. Cohomology detects trivial line bundles

We next isolate the technical steps for the cube. They are useful because fibrewise triviality alone can miss a deformation over a base with nilpotents.

We use the following cohomology-and-base-change prerequisite [Stacks, Tag 0B91]: if \(p:W\to B\) is proper, flat and of finite presentation and \(\mathcal L\) is a line bundle, then \(Rp_*\mathcal L\) is perfect, and its derived pullback to any \(T\to B\) computes \(R(p_T)_*\mathcal L_T\). Locally on an affine base a perfect object is represented by a bounded complex of finite free modules.

**Lemma 3.1. A complex adapted to one fibre.** Near any point \(b\) one can choose that free complex \(P^\bullet\) so that its differentials vanish after tensoring with \(\kappa(b)\), and

\[
\operatorname{rank}P^i
=\dim_{\kappa(b)}H^i(W_b,\mathcal L_b).
\tag{5}
\]

In particular it has no terms in negative degrees.

**Proof.** Start with a bounded free representative near \(b\). If a differential has a nonzero matrix entry modulo the prime of \(b\), invert that entry on a smaller neighbourhood. Row and column operations then put a unit in a separate \(1\times1\) block. The relation \(d^2=0\) lets one clear the preceding and following maps in that block. It splits off the contractible complex \(R\xrightarrow{1}R\), which can be deleted without changing the represented object.

Repeat. Each deletion lowers the sum of the finite ranks, so the procedure stops after finitely many steps. All remaining differential entries vanish at \(b\). The residue-field complex now has zero differentials, so its terms are its cohomology groups; base change gives (5). Negative fibre cohomology is zero, hence the corresponding free terms have rank zero. All the inversions and basis changes used only finitely many entries and take place on one neighbourhood. \(\square\)

This is the elementary cancellation underlying [Stacks, Tag 0BCD].

**Lemma 3.2. Universal constants in an integral proper family.** If \(p:W\to B\) is proper, flat and of finite presentation with geometrically integral fibres, then

\[
\mathcal O_T\xrightarrow{\sim}
(p_T)_*\mathcal O_{W_T}
\tag{6}
\]

for every \(T\to B\).

**Proof.** Lemma 1.1 gives \(H^0(W_b,\mathcal O)=\kappa(b)\). Apply Lemma 3.1 to \(\mathcal O_W\). On a neighbourhood of \(b\), its complex starts

\[
R\xrightarrow{d^0}P^1\longrightarrow\cdots .
\]

The unit morphism \(\mathcal O_B\to Rp_*\mathcal O_W\) is represented by a map of complexes from \(R\) in degree zero. Its degree-zero coefficient is nonzero at \(b\), since the unit spans \(H^0(W_b,\mathcal O)\). Shrink so that this coefficient is a unit. The chain-map identity \(d^0a=0\) then forces \(d^0=0\). It follows after every scalar extension that degree-zero cohomology is the base ring, with its given unit map. Arbitrary derived base change gives (6), locally and hence globally. \(\square\)

*Comparison locator:* [Stacks, Tag 0E0L].

**Lemma 3.3. The local product assertion.** Let \(X,Y\to B\) be proper, flat morphisms of finite presentation with geometrically integral fibres, and let \(x:B\to X\), \(y:B\to Y\) be sections. Suppose a line bundle \(\mathcal L\) on \(W=X\times_BY\) is trivial on \(X\times y(B)\) and \(x(B)\times Y\). If \(\mathcal L_b\) is trivial for one \(b\in B\), then \(\mathcal L\) is trivial over \(W_U\) for some open neighbourhood \(U\) of \(b\).

**Proof.** Work on an affine neighbourhood \(\operatorname{Spec}R\). Apply Lemma 3.1 simultaneously to

\[
C=R(p_W)_*\mathcal L,\qquad
D=R(p_X)_*\mathcal O_X,\qquad
F=R(p_Y)_*\mathcal O_Y.
\]

The degree-zero terms are \(R,R,R\). The first differentials of \(D,F\) are zero, by the unit argument in Lemma 3.2. Trivialize the two restrictions of \(\mathcal L\). Pullback of sections then gives derived morphisms \(C\to D\) and \(C\to F\). Since the source complex is bounded and free, these morphisms are represented by actual maps of complexes on the affine base.

After passing to \(\kappa(b)\), choose a trivialization of \(\mathcal L_b\). The two degree-one maps become the restrictions

\[
H^1(X_b\times Y_b,\mathcal O)
\longrightarrow
H^1(X_b,\mathcal O)\oplus H^1(Y_b,\mathcal O),
\tag{7}
\]

possibly multiplied on each summand by a nonzero scalar from the chosen trivializations. Map (7) is an isomorphism. Indeed the field Künneth formula [Stacks, Tag 0BED] decomposes its source as

\[
\bigl(H^1(X_b,\mathcal O)\otimes H^0(Y_b,\mathcal O)\bigr)
\oplus
\bigl(H^0(X_b,\mathcal O)\otimes H^1(Y_b,\mathcal O)\bigr).
\]

The two \(H^0\)'s are \(\kappa(b)\). Restriction by the sections is the identity on the corresponding summand and zero on the other, because a point has no positive-degree coherent cohomology.

Consequently the combined matrix

\[
B:C^1\longrightarrow D^1\oplus F^1
\]

has a full-column minor which is a unit at \(b\). Shrink to make that minor invertible; then \(B\) is split injective. The chain-map equations give

\[
B\,d_C^0=(d_D^0a,d_F^0a')=0.
\]

Thus \(d_C^0=0\). A basis vector of \(C^0=R\) now determines a global section of \(\mathcal L\) whose restriction to \(W_b\) is a nonzero constant multiple of a trivializing section.

Its zero scheme is closed in \(W\), and has closed image in \(B\) by properness. That image misses \(b\). Removing it makes the section nowhere vanishing, so it trivializes \(\mathcal L\). Every step works over \(R\) itself, retaining its nilpotents. \(\square\)

*Comparison locator:* [Stacks, Tag 0BF3], whose product assertion we have proved here.

**Lemma 3.4. A closed fibre locus.** For \(p:W\to B\) as in Lemma 3.2, and a line bundle \(\mathcal L\), the set

\[
C(\mathcal L)=\{b\in B:\mathcal L_b\simeq\mathcal O_{W_b}\}
\tag{8}
\]

is closed.

**Proof.** On a proper integral fibre, \(\mathcal L_b\) is trivial exactly when both \(\mathcal L_b\) and \(\mathcal L_b^{-1}\) have a nonzero section. For if \(s,t\) are such sections, their product is a nonzero section of \(\mathcal O_{W_b}\): integrality prevents it from vanishing identically. By Lemma 1.1 it is a nonzero scalar, so both sections are invertible.

The conditions \(h^0(\mathcal L_b)\geq1\) and \(h^0(\mathcal L_b^{-1})\geq1\) are closed. One can see the required upper semicontinuity directly in a free cohomology complex starting in degree zero: if its degree-zero rank is \(r\), then

\[
h^0_b=r-\operatorname{rank}(d^0\otimes\kappa(b)).
\]

The condition \(h^0_b\geq1\) is the vanishing of the \(r\times r\) minors of \(d^0\); for \(r=0\) the locus is empty. Such complexes exist locally by Lemma 3.1. The intersection of these two closed conditions is (8). \(\square\)

This lemma concerns a closed set of points; the next proof separately establishes local triviality on the actual base scheme.

### The closed locus of relative triviality

**Theorem 3.5. Maximal relative triviality over an arbitrary parameter scheme.** Let \(X/k\) be a proper geometrically integral variety, \(Y\) any \(k\)-scheme, and \(L\) a line bundle on \(X\times_kY\). There is a closed subscheme \(Y_0\subset Y\) such that, for every \(T\to Y\),
\[
\begin{gathered}
T\to Y\text{ factors through }Y_0\\
\Longleftrightarrow\quad L_T\simeq p_T^*N\\
\text{for a line bundle }N\text{ on }T.
\end{gathered}
\]
Formation of this closed subscheme commutes with every base change. Its universal line is \(p_{Y_0,*}(L|_{X\times Y_0})\).

**Proof.** Suppose first that \(X\) has a rational point \(x\) and \(Y=\operatorname{Spec}R\) is Noetherian. Normalize by replacing \(L\) with \(L'=L\otimes p^*(x^*L)^{-1}\); it has a canonical trivialization on the section \(x\). The fibres where \(L'\) is trivial form a closed set. Indeed they are exactly those where both \(L'\) and its inverse have nonzero sections. On the geometrically integral proper fibre, the product of two such sections is a nonzero constant, hence both sections are invertible. The upper-semicontinuity proof by matrix minors in [Semicontinuity and Grauert's theorem](../../AG-QC/src/semicontinuity-and-grauerts-theorem.md), Theorem 1.1, makes both nonzero-section loci closed.

At a point of this set, the complete proper-family Grothendieck-complex proof in [Base change and the Grothendieck complex](../../AG-QC/src/base-change-and-the-grothendieck-complex.md), Theorem 3.2, gives finite free nonnegative complexes for \(L'\) and \(L'^{-1}\), computing cohomology after every base change. Cancel their unit differential blocks as in the existing Lemma 3.1. Their degree-zero terms have rank one, since the two fibres are trivial and the constants of \(X\) are \(k\). Evaluation at \(x\) is a derived map to \(R\) in degree zero. Since the source complex is finite projective, it has a representing chain map. Its degree-zero coefficient is a unit at the selected point, because evaluation on its trivial fibre is an isomorphism. Shrink so that both evaluation coefficients are units.

Cut out the entries of the degree-zero differential in **both** complexes. On the resulting closed subscheme \(Z\), their basis elements lift to sections \(\sigma\) and \(\tau\) of \(L'\) and \(L'^{-1}\), with invertible values on \(x\). Their product is a global function on \(X\times Z\). Constants and flat \(k\)-base change give \(p_{Z,*}\mathcal O_{X\times Z}=\mathcal O_Z\), including when \(Z\) has nilpotents. The product is therefore the pullback of its invertible value at \(x\). Hence both sections are everywhere invertible, and \(L'\) is trivial.

Conversely, if a base change \(T\) makes \(L'\) a pullback from \(T\), its restriction on \(x\) makes that base line trivial. Its sections then evaluate isomorphically onto \(\mathcal O_T\). In each of the two base-changed complexes, this evaluation is multiplication by the specified unit on \(\ker d^0_T\subset\mathcal O_T\). Surjectivity forces \(d^0_T=0\). Thus such a base change factors through \(Z\), and precisely those base changes do. The local closed subschemes just constructed have identical functors on overlaps and glue, together with the empty subscheme on the complement of the fibre-trivial closed set. This proves the assertion for Noetherian affine \(Y\).

No Noetherian hypothesis on \(Y\) is necessary. On an arbitrary affine \(\operatorname{Spec}R\), the finite presentation data of the line bundle on the fixed finite-type \(X_R\) descend to a finitely generated \(k\)-subalgebra \(R_0\subset R\). One can check this on a finite affine cover: descend its finitely many trivializing principal opens, transition units and their inverses, the identities showing that those opens cover, and the cocycle identities. Enlarging \(R_0\) contains all finitely many coefficients and identities. The descended sheaf is a line bundle; the product projection is flat because the base is a field. The Noetherian construction over \(R_0\) computes its defining functor after **every** algebra base change by Theorem 3.2. Its pullback to \(R\) consequently represents exactly the required functor, not just its field-valued points. These closed subschemes glue on arbitrary affine covers of \(Y\).

Finally \(X\) need not have a rational point. A closed point gives a finite faithfully flat field extension \(K/k\) over which it has one. Construct the closed subscheme on \(Y_K\). The property that \(L_T\) is pulled back from \(T\) is faithfully flat local for this field extension. To verify this, let \(E=p_{T,*}L_T\). It is quasi-coherent, and the flat-base-change theorem, proved in [Base change and the Grothendieck complex](../../AG-QC/src/base-change-and-the-grothendieck-complex.md), Theorem 2.1, gives \(E_K=p_{T_K,*}L_{T_K}\). If the latter bundle is pulled back from a line \(N_K\), the constants calculation identifies \(E_K=N_K\), and the evaluation \(p_{T_K}^*E_K\to L_{T_K}\) is an isomorphism. Faithfully flat module descent makes \(E\) a line bundle, and faithful flatness makes the evaluation downstairs an isomorphism. This proves the claimed locality without a separability assumption on \(K/k\).

The two base changes of the constructed closed subscheme to \(Y_{K\otimes_kK}\) therefore represent the same functor and are identical. Descent of their quasi-coherent ideals, proved in [Quotients and torsors](quotients-and-torsors.md), Section 1, gives a closed subscheme \(Y_0\subset Y\). Its characterization and universal line follow from the evaluation argument. This also proves arbitrary base-change compatibility and uniqueness. \(\square\)

## 4. The theorem of the cube and the square

**Theorem 4.1. Relative cube.** Let \(S\) be a scheme. Let \(X,Y\to S\) be proper, flat morphisms of finite presentation with geometrically integral fibres and sections \(x,y\). Let \(Z\to S\) have connected underlying space. Suppose a line bundle \(\mathcal L\) on \(X\times_SY\times_SZ\) is trivial on

\[
x(S)\times_SY\times_SZ,\qquad
X\times_Sy(S)\times_SZ,
\]

and is trivial on the fibre \(X\times_SY\times_S\operatorname{Spec}\kappa(z_0)\) for at least one \(z_0\in Z\). Then \(\mathcal L\) is trivial.

**Proof.** Apply the preceding lemmas after base change from \(S\) to \(Z\). The fibre-trivial locus (8) is closed by Lemma 3.4. At each of its points, Lemma 3.3 supplies an open neighbourhood on which \(\mathcal L\) itself is trivial. Thus that locus is also open. It is nonempty by \(z_0\), so connectedness makes it all of \(Z\).

Choose these neighbourhoods as an open cover of \(Z\), with trivializations of \(\mathcal L\) over their inverse images. The ratios on overlaps are units on the product family. By Lemma 3.2, those units come uniquely from the overlaps in \(Z\); the same is true of their inverses. Their cocycle therefore glues a line bundle \(\mathcal N\) on \(Z\) with

\[
\mathcal L\simeq p_Z^*\mathcal N.
\]

Pull back along \(x\times y\times\operatorname{id}_Z\). The left side is trivial by the slice hypotheses, and the right side is \(\mathcal N\). Hence \(\mathcal N\) and then \(\mathcal L\) are trivial. This proves the relative statement, including nonreduced and non-Noetherian parameter schemes. \(\square\)

*Comparison locator:* [Stacks, Tag 0BF4].

For an abelian variety, let \(m_I:A^3\to A\) add the coordinates indexed by \(I\). Let \(p:A^3\to\operatorname{Spec}k\) be the structure map. The pullback \(0^*L\) is a one-dimensional \(k\)-vector space, viewed as a line bundle on the point.

**Corollary 4.2. The cube on an abelian variety.** For every line bundle \(L\) on \(A\), the line bundle

\[
\begin{aligned}
\mathcal C(L)={}&m_{123}^*L
\otimes m_{12}^*L^{-1}
\otimes m_{13}^*L^{-1}
\otimes m_{23}^*L^{-1}\\
&\otimes m_1^*L\otimes m_2^*L\otimes m_3^*L
\otimes p^*(0^*L)^{-1}
\end{aligned}
\tag{9}
\]

is trivial.

**Proof.** If any coordinate is zero, terms in (9) cancel in pairs, including the last constant line. Thus all three coordinate-zero slices are trivial. Apply Theorem 4.1 with \(X=Y=Z=A\), the identity sections in the first two factors, and \(z_0=0\) in the third. The required properness, geometric integrality and connectedness were established above. \(\square\)

Choosing a trivialization of \(0^*L\) gives the usual seven-term identity

\[
m_{123}^*L\otimes m_1^*L\otimes m_2^*L\otimes m_3^*L
\simeq m_{12}^*L\otimes m_{13}^*L\otimes m_{23}^*L.
\tag{10}
\]

Formula (9) keeps track of the constant line before that choice. *Comparison locator:* [Stacks, Tag 0BFE].

**Corollary 4.3. The square.** For \(a,b\in A(k)\),

\[
t_{a+b}^*L\otimes L\simeq t_a^*L\otimes t_b^*L.
\tag{11}
\]

The same assertion holds for points over any field extension of \(k\).

**Proof.** Pull (9) back by \(A\to A^3\), \(z\mapsto(z,a,b)\). Its varying factors are exactly those of (11); the others are the constant lines \(L_a,L_b,L_{a+b},L_0\). They are one-dimensional vector spaces over the field and therefore trivial line bundles on \(A\). Choosing their trivializations yields (11). Base change gives the assertion over every extension field. \(\square\)

Equivalently, the rule \(a\mapsto[t_a^*L\otimes L^{-1}]\) is additive into the group of line-bundle isomorphism classes. This conclusion needs no construction of a Picard scheme. Over a general test scheme the constant factors in (9) must be retained; the field-point formula alone does not remove them canonically.

### The constant lines in a family version of the square

**Proposition 4.4. Canonical normalized cube and the relative square.** The eight-factor bundle \(\mathcal C(L)\) in Corollary 4.2 has a unique trivialization whose value at \((0,0,0)\) is the canonical cancellation identification with \(k\). This trivialization agrees with the cancellation identifications on the three coordinate-zero faces and commutes with pullback by homomorphisms of abelian varieties.

For a \(k\)-scheme \(T\), \(a,b\in A(T)\), and \(p:A_T\to T\), there is consequently an isomorphism

\[
t_{a+b}^*L_T\otimes L_T\simeq
t_a^*L_T\otimes t_b^*L_T\otimes p^*B_L(a,b),
\]

where

\[
\begin{aligned}
B_L(a,b)&=(a+b)^*L\otimes(a^*L)^{-1}\\
&\quad\otimes(b^*L)^{-1}\otimes(0_T^*L).
\end{aligned}
\]

The class of \(B_L(a,b)\) in \(\operatorname{Pic}(T)\) is symmetric and additive in each argument.

**Proof.** Corollary 4.2 gives a trivialization. Its ambiguity is a unit in \(H^0(A^3,\mathcal O)=k\), so its specified value at the origin determines it uniquely. Its restriction to a coordinate face and the cancellation trivialization have the same value at the origin; constants on that face show that they agree. Pullback by a homomorphism preserves the origin value and therefore preserves the trivialization.

Pull back the normalized cube along \(A_T\to A^3\), \(z\mapsto(z,a,b)\). Its varying factors are those in the displayed relative square. The remaining factors are exactly the pullbacks of \(L_{a+b}^{-1},L_a,L_b,L_0^{-1}\). Moving them to the other side gives the formula. Finally apply the same cube to \((a,b,c):T\to A^3\); cancellation gives

\[
B_L(a+b,c)\simeq B_L(a,c)\otimes B_L(b,c).
\]

Symmetry is immediate from the expression for \(B_L\), so the other additivity follows too. These calculations retain the lines on \(T\), and are valid when \(T\) has nilpotents. \(\square\)

There is also a linear part of the integer-pullback formula. For any line bundle \(M\), set \(M_+=M\otimes[-1]^*M\), \(M_-=M\otimes([-1]^*M)^{-1}\). Inversion fixes \(M_+\) and takes \(M_-\) to its inverse. Theorem 5.1 therefore gives \([n]^*M_-=M_-^{\otimes n}\), while \(M^{\otimes2}=M_+\otimes M_-\). No division by two in the Picard group is being asserted.

### A scheme that records translation invariance

The normalized two-variable bundle is

\[
\Lambda_0(L)=m^*L\otimes p_1^*L^{-1}\otimes p_2^*L^{-1}
\otimes p^*(0^*L).
\]

It has its cancellation trivialization along either origin slice. Keeping the last factor makes the normalization independent of a chosen basis of \(L_0\).

**Lemma 4.5. The translation kernel, with nilpotents.** There is a closed subgroup scheme \(K(L)\subset A\) characterized, for every \(k\)-scheme \(T\), by

\[
\begin{gathered}
a\in K(L)(T)\\
\Longleftrightarrow\quad t_a^*L_T\otimes L_T^{-1}\simeq p_T^*N\\
\text{for a line bundle }N\text{ on }T.
\end{gathered}
\]

Necessarily \(N\simeq a^*L\otimes(0_T^*L)^{-1}\). Formation of \(K(L)\) commutes with every base change. If \(L\) is ample, \(K(L)\) is finite.

**Proof.** Apply Theorem 3.5 to the normalized bundle \(\Lambda_0(L)\) on \(A\times A\), with the second factor as parameter. Since its restriction on the origin section is canonically trivial, being pulled back from the parameter is equivalent to being trivial. This constructs the closed scheme \(K(L)\), with all its test-scheme nilpotents, and gives a universal trivialization along \(A\times K(L)\). The full general construction in Theorem 3.5 proves this rather than assuming a Picard scheme.

Pulling \(\Lambda_0(L)\) back along \(1_A\times a\) shows that its triviality is equivalent to the displayed condition; restriction to the origin gives the formula for \(N\). The relative square makes the condition stable under addition and inversion, proving the subgroup assertion on every test scheme. Its universal characterization also proves base-change compatibility.

For finiteness we may extend to an algebraic closure. Put \(B=(K(L)_{\mathrm{red}})^0\). The reduced identity component of a group over a perfect field is smooth, and the connected-group results in the earlier lessons make \(B\) an abelian subvariety. The restriction of \(\Lambda_0(L)\) to \(B\times B\) is trivial. Pulling it back along \(x\mapsto(x,-x)\) says that \(L|_B\otimes[-1]^*(L|_B)\) is a constant line bundle. If \(L\) is ample, this tensor product is ample. A trivial line bundle cannot be ample on a positive-dimensional proper integral scheme: all its sections are constant, and all maps furnished by its powers are constant. Thus \(\dim B=0\), so \(K(L)\) has dimension zero. Being a closed subscheme of the proper finite-type \(A\), it is finite. \(\square\)

The construction in Theorem 3.5 also proves the usual see-saw assertion for a proper geometrically integral \(X\) with a rational point and a **reduced** parameter scheme: if two line bundles on \(X\times T\) have isomorphic fibres and isomorphic restrictions on that section, normalize their quotient along the section. The same local degree-zero complex has all entries of \(d^0\) zero at every residue field. Reducedness makes those entries zero. Its lifted section trivializes the quotient. Fibrewise triviality alone on a nonreduced parameter is insufficient; Theorem 4.1 used the two slices to remove that deformation obstruction. This assertion uses reducedness of the actual base scheme, rather than merely of its geometric fibres.

### Fibres, effective divisors, and ampleness

**Proposition 4.6. Connected fibres are translates.** Let \(k\) be algebraically closed, \(A/k\) an abelian variety, and \(f:A\to Y\) a morphism to a separated \(k\)-scheme of finite type. Let \(F_a\) be the reduced connected component containing \(a\) of \(f^{-1}(f(a))\). Then \(F_0\) is an abelian subvariety and \(F_a=a+F_0\).

**Proof.** A proper reduced connected scheme over an algebraically closed field has \(H^0(\mathcal O)=k\): its ring of global functions is a finite reduced connected \(k\)-algebra, hence \(k\). Apply Theorem 2.1 to the restriction of \(f\circ m\) to \(F_a\times A\). Its fibre at parameter \(0\) is contracted; hence \(f(z+F_a)\) is a point for every \(z\). Taking \(z=b-a\) shows \(b-a+F_a\subset F_b\), because this is a connected reduced subset of the correct fibre containing \(b\). Taking \(a=0\) and then \(b=0\) gives the two inverse inclusions, so \(F_a=a+F_0\).

If \(a\in F_0(k)\), its fibre component is \(F_0\), hence \(a+F_0=F_0\). This proves closure under addition and inverses on geometric points. The scheme \(F_0\times F_0\) is reduced over the perfect field, so the equations for the closed immersion \(F_0\subset A\) vanish identically under addition; inversion is treated similarly. Thus \(F_0\) is a reduced closed subgroup scheme. The smoothness and connected-group results used in Lemma 4.5 make it a proper geometrically integral smooth group, hence an abelian subvariety. \(\square\)

For a simple abelian variety this implies that every morphism is constant or finite onto its image: the connected reduced fibres have dimension either \(g\) or zero, and in the latter case the proper morphism to its closed scheme-theoretic image is quasi-finite, hence finite.

**Proposition 4.7. An effective bundle has a generated square.** If \(H^0(A,L)\ne0\), then \(L^{\otimes2}\) is globally generated. Under this effectivity hypothesis, moreover,

\[
L\text{ ample}\quad\Longleftrightarrow\quad K(L)\text{ finite}.
\]

**Proof.** Work over an algebraic closure; global generation and ampleness descend by field extension. Let \(D\) be the divisor of a nonzero section of \(L\). For any point \(y\), choose \(a\) outside the two proper closed subsets defined by \(y+a\in D\) and \(y-a\in D\). The square gives \(t_a^*L\otimes t_{-a}^*L\simeq L^2\), and the product of the translated sections does not vanish at \(y\). Thus the evaluation map is surjective at every closed point, hence everywhere.

Let \(f:A\to\mathbf P(H^0(L^2)^\vee)\) be its morphism and \(B=F_0\) as in Proposition 4.6. Suppose \(B\) is positive-dimensional. Since \(f\circ t_b=f\) for \(b\in B(k)\), every divisor in \(|L^2|\) is invariant under every such translation. Apply this to \(2D\), the divisor of the square of the chosen section: equality \(2t_b^*D=2D\) of Weil divisors implies \(t_b^*D=D\), so \(b\in K(L)(k)\). Reducedness of \(B\) then gives \(B\subset K(L)\). If \(K(L)\) is finite this is impossible. Hence the fibres of \(f\) are zero-dimensional; \(f\) is finite. For every coherent \(F\) on \(A\), finite pushforward and the projection formula identify \(H^i(A,F\otimes L^{2n})\) with \(H^i(\mathbf P,f_*F(n))\). Serre vanishing kills these for \(i>0\) and large \(n\). The cohomological ampleness criterion in [Serre's theorems on projective schemes](../../AG-QC/src/serres-theorems-on-projective-schemes.md), Theorem 4.1, makes \(L^2\), and therefore \(L\), ample. The reverse implication is Lemma 4.5. \(\square\)

Over an algebraically closed field define the **reduced divisor stabilizer** \(H(D)_{\mathrm{red}}\) by the translations preserving \(D\) as a divisor. It is the reduced closed subgroup of \(K(L)\) cut out by fixing the line of its section in the projective action described below. The proof just given shows \(F_0\subset H(D)_{\mathrm{red}}^0\subset K(L)_{\mathrm{red}}^0\). Conversely, for \(C=K(L)_{\mathrm{red}}^0\), the restriction of \(\Lambda_0(L)\) to \(A\times C\) is trivial. Choose a translate \(D+a\) not containing \(C\); such a translate exists since a fixed point of \(C\) can be kept outside \(D+a\). It supplies a nonzero section of \(L|_C\), because \(a\in A(k)\) and \(t_a^*L|_C\simeq L|_C\) up to a constant line. The anti-diagonal identity gives \([-1]^*(L|_C)\simeq(L|_C)^{-1}\), so the inverse bundle also has a nonzero section. Their product is a nonzero constant, proving \(L|_C\) trivial. All sections of \(L^2|_C\) are consequently constant multiples of one trivialization. Thus \(f(C)\) is a point, and \(C\subset F_0\). We have proved

\[
F_0=H(D)_{\mathrm{red}}^0=K(L)_{\mathrm{red}}^0.
\]

In particular an effective divisor has finite reduced stabilizer if and only if its line bundle is ample. The adjective effective is essential: the inverse of an ample bundle has finite translation kernel as well, and is not ample in positive dimension.

## 5. Multiplication pulls back quadratically

**Theorem 5.1. The integer formula.** For every line bundle \(L\) on \(A\) and every integer \(n\),

\[
[n]^*L\simeq
L^{\otimes n(n+1)/2}\otimes
([-1]^*L)^{\otimes n(n-1)/2}.
\tag{12}
\]

Negative tensor powers mean powers of the dual line bundle. If \(L\) is **symmetric**, meaning \([-1]^*L\simeq L\), this reduces to

\[
[n]^*L\simeq L^{\otimes n^2}.
\tag{13}
\]

**Proof.** Work in the additive group of line-bundle isomorphism classes. Set \(F_n=[n]^*[L]\), \(l=[L]\), and \(i=[-1]^*[L]\). Then \(F_0=0\), since pullback by the constant map is a trivializable constant line, and \(F_1=l\).

Pull the cube back along \(x\mapsto(x,x,-x)\). Its three-coordinate sum is \(x\), its two nonzero pair sums are \(2x\) and the two constant zeros, and its individual sums are \(x,x,-x\). Cancellation gives

\[
F_2=3l+i.
\]

Next pull back along \(x\mapsto(x,x,[n-1]x)\). This gives, for every \(n\),

\[
F_{n+1}+2l+F_{n-1}=F_2+2F_n,
\quad\text{hence}\quad
F_{n+1}-2F_n+F_{n-1}=l+i.
\tag{14}
\]

For \(n\geq0\), the initial conditions and this recurrence uniquely determine

\[
F_n=\frac{n(n+1)}2\,l+\frac{n(n-1)}2\,i.
\]

One verifies the initial conditions directly; each of the two quadratic coefficients has second difference one. This proves (12) for nonnegative \(n\).

For \(n=-m<0\), pull the formula for \(m\) back by \([-1]\). That operation exchanges \(l\) and \(i\), giving the same formula with \(n=-m\). If \(L\) is symmetric, the two coefficients sum to \(n^2\), proving (13). \(\square\)

*Comparison locator:* [Stacks, Tag 0BFF].

Projectivity supplies an ample line bundle \(H\). The line bundle

\[
N=H\otimes[-1]^*H
\tag{15}
\]

is ample and symmetric: inversion is an automorphism and exchanges its two factors. This choice lets us use (13) without assuming that a given ample line bundle is symmetric.

### Why the third power always embeds

The next proof needs the Euler polynomial, finite étale torsor characters and Serre vanishing. We give the multivariable refinement and the torsor calculation explicitly.

**Lemma 5.2. Finite differences of Euler characteristic.** Let \(X\) be proper over a field, \(F\) coherent with support dimension at most \(d\), and \(M_1,\ldots,M_r\) line bundles. The function
\[
(a_1,\ldots,a_r)\longmapsto
\chi(X,F\otimes M_1^{a_1}\otimes\cdots\otimes M_r^{a_r})
\]
is a rational-coefficient polynomial of total degree at most \(d\), for all integer exponents. In particular, tensoring \(F\) by a finite-order line bundle preserves its Euler characteristic.

**Proof.** We use the actual coherent-filtration and generic-lattice proofs in [Coherence of higher direct images under proper morphisms](../../AG-QC/src/proper-morphisms-and-coherent-direct-images.md), Lemma 1.2 and Theorem 2.2, and the Euler additivity proved in [Euler characteristics and Hilbert polynomials](../../AG-QC/src/euler-characteristics-and-hilbert-polynomials.md), Proposition 1.1. Here is the finite-difference argument, including the multivariable step.

Let \(G_d\) be the subgroup of the Grothendieck group of coherent sheaves generated by sheaves with support dimension at most \(d\), and put \(G_{-1}=0\). Tensoring by a line bundle \(M\) defines an operator \(T_M\). We claim
\[
(T_M-1)G_d\subset G_{d-1}.
\]
Filter a sheaf into nonzero ideals \(I\) on integral closed subschemes \(V\), as in the cited complete filtration proof. On \(V\), the generic lines of \(I\) and \(I\otimes M\) are isomorphic. The extension-across-a-closed-complement lemma gives a common coherent ideal \(E\subset I\) and an injection \(E\to I\otimes M\) agreeing with that generic isomorphism. The injectivity follows because a generically zero kernel inside an ideal of a domain is zero. Both quotients are supported on proper closed subsets of \(V\). Subtracting the two exact-sequence classes gives
\[
[I\otimes M]-[I]=[Q']-[Q]\in G_{\dim V-1}.
\]
Add the filtration factors to prove the claim.

The commuting operators \(T_{M_j}-1\) therefore kill \([F]\) after any \(d+1\) applications. Thus every mixed difference of total order \(d+1\) of the displayed integer-valued function vanishes, at every integer argument. Repeated one-variable Newton expansion gives, for nonnegative arguments,
\[
\sum_{|\alpha|\le d}
\bigl(\Delta_1^{\alpha_1}\cdots\Delta_r^{\alpha_r}f\bigr)(0)
\prod_{j=1}^r\binom{a_j}{\alpha_j}.
\]
Terms with \(|\alpha|>d\) vanish by the operator calculation. This is a polynomial of total degree at most \(d\). The finite-difference equation in each coordinate determines values backward as well as forward, so the same polynomial gives the function at negative arguments. This proves the assertion for all integers.

If \(M^e\simeq\mathcal O_X\), the polynomial \(\chi(F\otimes M^a)\) is periodic with period \(e\). Its difference with its translate by \(e\) is zero at every integer and hence is the zero polynomial. A nonconstant polynomial has a nonzero translated difference, so this polynomial is constant. Its values at zero and one prove the final assertion. \(\square\)

**Lemma 5.3. Euler characteristic under prime-to-characteristic multiplication.** For an abelian variety \(A\) of dimension \(g\), any line bundle \(M\), and any positive integer \(n\) prime to the characteristic,
\[
\chi([n]^*M)=n^{2g}\chi(M).
\]

**Proof.** Extend the field to an algebraic closure; the affine Čech base-change proof preserves Euler characteristic. Theorems 6.1–6.2 of the existing lesson make \(q=[n]\) a finite étale torsor under the constant abelian group \(G=A[n](k)\), of order \(r=n^{2g}\) and exponent dividing \(n\). Indeed
\[
\begin{gathered}
A\times G\longrightarrow A\times_{q,A,q}A,\\
(a,h)\longmapsto(a,a+h)
\end{gathered}
\]
is an isomorphism, with inverse taking the difference of the two coordinates. The order \(r\) is invertible in \(k\), which contains all \(n\)-th roots of unity.

The character idempotents
\[
e_\eta=\frac1r\sum_{h\in G}\eta(h)^{-1}t_h
\]
split \(q_*\mathcal O_A\) into eigensheaves \(E_\eta\). On an étale cover trivializing the torsor, this is the character decomposition of functions on \(G\): each eigenspace has rank one, its character function is invertible, and multiplication identifies \(E_\eta\otimes E_\theta\) with \(E_{\eta\theta}\). These statements descend from the cover. Thus the eigensheaves are line bundles, \(E_1=\mathcal O_A\), and \(E_\eta^{\otimes n}\simeq\mathcal O_A\). There are exactly \(r\) of them: a finite abelian group of exponent dividing \(n\) is a product of cyclic groups, and each cyclic factor has as many characters as elements over this field.

Finite pushforward has no higher direct images. The projection formula and Lemma 5.2 consequently give
\[
\begin{aligned}
\chi(q^*M)&=\chi(M\otimes q_*\mathcal O_A)\\
&=\sum_\eta\chi(M\otimes E_\eta)\\
&=r\chi(M).
\end{aligned}
\]
Field descent proves the original statement. \(\square\)

**Lemma 5.4. Vanishing in an ample quadrant.** On a projective scheme over a field, for two ample bundles \(P,Q\) and a coherent sheaf \(F\),

\[
H^i(X,F\otimes P^a\otimes Q^b)=0\quad(i>0, a,b\ge M)
\]

for some \(M\).

**Proof.** Choose a common positive power making \(P,Q\) very ample, and embed \(X\) in a product \(\mathbf P^u\times\mathbf P^v\). Deal separately with the finitely many residue classes of the two exponents, pushing forward the corresponding twists of \(F\). It suffices to prove the assertion for a coherent sheaf \(G\) on this product with twists \(\mathcal O(a,b)\).

The Segre bundle \(\mathcal O(1,1)\) is very ample. The finite-generation-by-twists proof in [Serre's theorems on projective schemes](../../AG-QC/src/serres-theorems-on-projective-schemes.md), Proposition 1.2, applied to its Segre embedding, gives a surjection \(E\to G\), where \(E\) is a finite sum of \(\mathcal O(-c,-c)\), with coherent kernel \(J\). The standard product charts form a finite affine cover with affine intersections, so their Čech complex gives a uniform bound above which all quasi-coherent cohomology is zero. Descend on \(i\), for **all** coherent sheaves simultaneously. The claim is true above this bound. In the segment

\[
\begin{gathered}
H^i(E(a,b))\longrightarrow H^i(G(a,b))\\
\longrightarrow H^{i+1}(J(a,b)),
\end{gathered}
\]

the right group vanishes for \(a,b\) sufficiently large by induction. The left group vanishes when both exponents exceed all the \(c\)'s, by the projective-space cohomology calculation. Here its product use is justified directly: the two-direction Čech complex of the standard product cover is the tensor product over the field of the two standard section complexes. Its bi-intersections are affine, so the acyclic-cover comparison computes cohomology with this total complex. A complex of vector spaces splits as its cohomology with zero differential and contractible pairs, by choosing complements to cycles and boundaries. Tensoring such pairs remains contractible. Hence only the tensor products of the two factor cohomologies survive, in degree zero for these nonnegative twists. This proves the step for \(i>0\). A maximum over the finitely many cohomology degrees and residue classes finishes the proof. \(\square\)

**Proposition 5.5. Euler homogeneity and sections of an ample line bundle.** If \(g>0\), every line bundle \(M\) on a \(g\)-dimensional abelian variety satisfies
\[
\chi(M^a)=a^g\chi(M)\qquad(a\in\mathbf Z).
\]
If \(L\) is ample, then
\[
\begin{gathered}
H^i(A,L)=0\quad(i>0),\\
h^0(A,L)=\chi(L)>0.
\end{gathered}
\]
The degree \(d(L)\), defined as \(g!\) times the leading coefficient of its Hilbert polynomial, is therefore \(g!\chi(L)\). When \(L\) is very ample, this is its projective degree. In dimension zero, \(A=\operatorname{Spec}k\), and every line bundle has \(h^0=\chi=1\) and no higher cohomology.

**Proof.** Fix an integer \(n\ge2\) prime to the characteristic, and put
\[
\begin{gathered}
F(a,b)=\chi(M^a\otimes([-1]^*M)^b),\\
C=\frac{n^2+n}{2},\quad D=\frac{n^2-n}{2}.
\end{gathered}
\]
Lemma 5.2 makes \(F\) a rational-coefficient polynomial of total degree at most \(g\). Apply Lemma 5.3 to every line bundle \(M^a\otimes([-1]^*M)^b\). The integer-pullback formula, also applied after inversion, gives
\[
F(Ca+Db,Da+Cb)=n^{2g}F(a,b).
\]
This holds for all integer \(a,b\), so it is an identity of polynomials over \(\mathbf Q\).

Write \(u=a+b\) and \(v=a-b\). The transformation on the left sends \(u\) to \(n^2u\) and \(v\) to \(nv\). If a coefficient of \(u^iv^j\) is nonzero, the identity requires \(2i+j=2g\), while the total-degree bound requires \(i+j\le g\). These two conditions force \(i=g,j=0\). Consequently
\[
F(a,b)=c(a+b)^g,\qquad c=F(1,0)=\chi(M).
\]
Taking \(b=0\) proves Euler homogeneity. The change of variables takes place over \(\mathbf Q\), where Euler polynomial coefficients lie, and requires no division by two in \(k\). It is valid in characteristic two.

For an ample \(L\), [Euler characteristics and Hilbert polynomials](../../AG-QC/src/euler-characteristics-and-hilbert-polynomials.md), Theorem 3.1, proves that \(\chi(L^a)\) has degree \(g\) and positive leading coefficient. The formula just proved makes that coefficient precisely \(\chi(L)\), proving its strict positivity and the degree assertion.

For arbitrarily large positive integers \(n\) prime to the characteristic, Theorem 6.1 gives a finite locally free \([n]\) of degree \(n^{2g}\), invertible in \(k\). The trace divided by this degree splits \(\mathcal O_A\to[n]_*\mathcal O_A\). By the projection formula, \(L\) is a direct summand of \([n]_*[n]^*L\); hence \(H^i(A,L)\) is a direct summand of \(H^i(A,[n]^*L)\). The integer formula gives
\[
[n]^*L=L^{n(n+1)/2}\otimes([-1]^*L)^{n(n-1)/2}.
\]
Both bundles on the right are ample, so Lemma 5.4 kills its positive-degree cohomology for large \(n\). This proves vanishing in every characteristic. Thus \(h^0(L)=\chi(L)>0\). The dimension-zero assertion follows from the existing identification of \(A\) with \(\operatorname{Spec}k\). \(\square\)

**Corollary 5.6. The finite-flat Euler comparison needed below.** If \(q:A\to B\) is a finite locally free homomorphism of abelian varieties of rank \(r\), and \(M\) is ample on \(B\), then
\[
\chi(A,q^*M)=r\chi(B,M).
\]

**Proof.** The finite surjection makes the dimensions equal, say \(g\). Its direct image \(E=q_*\mathcal O_A\) is a vector bundle of rank \(r\). The generic-lattice proof in [Coherence of higher direct images](../../AG-QC/src/proper-morphisms-and-coherent-direct-images.md), Lemma 2.1, embeds \(I^{\oplus r}\) in \(E\), for a nonzero coherent ideal \(I\subset\mathcal O_B\), with smaller-dimensional quotient. The sequence comparing \(I\) with \(\mathcal O_B\) also has smaller-dimensional quotient. Euler-polynomial degree bounds therefore give
\[
[a^g]\chi(B,E\otimes M^a)
=r[a^g]\chi(B,M^a).
\]
Finite pushforward and projection identify the left polynomial with \(\chi(A,(q^*M)^a)\). Proposition 5.5 makes the two degree-\(g\) coefficients \(\chi(A,q^*M)\) and \(\chi(B,M)\), respectively. This proves the equality. For \(g=0\), both varieties are the rational point and \(r=1\). No étaleness, reduced kernel or separability hypothesis on \(q\) was used. \(\square\)

**Lemma 5.7. Reduced representatives.** Over an algebraically closed field, every effective divisor on \(A\) is linearly equivalent to an effective divisor with no repeated prime components.

**Proof.** Write \(D=\sum_i m_iD_i\) with distinct reduced prime divisors. For each \(m_i\ge2\), replace \(m_iD_i\) by

\[
\begin{gathered}
(D_i+a_{i1})+\cdots+(D_i+a_{i,m_i}),\\
\sum_j a_{ij}=0.
\end{gathered}
\]

The square makes this divisor linearly equivalent to \(m_iD_i\). Its parameters form \(A^{m_i-1}\). For any pair of its summands, their parameter difference maps surjectively to \(A\): for two summands with \(m_i=2\) it is multiplication by \(2\), surjective by Theorem 6.1 even in characteristic two; for \(m_i\ge3\) it is a surjective sum of independent coordinates. The translations fixing a prime divisor form a proper closed set: if every translation fixed it, translating one of its points to a point outside it would be impossible. Thus equality of two of these prime translates is a proper closed condition. Equality with a fixed prime divisor, or with a translate chosen for another \(i\), is also a proper closed condition on the product of parameter spaces. Avoid the finitely many such conditions in this irreducible parameter space. Keep the \(m_i=1\) summands fixed. The resulting sum has distinct prime components, each with coefficient one. \(\square\)

Here the closedness assertions can be checked without a Hilbert scheme. For a moving Cartier divisor, choose a sufficiently high fixed very ample twist. Relative Serre vanishing and generation identify its ideal, universally, with the evaluation image of a vector subbundle of the fixed space of global sections. Equality with another ideal is equality of those subbundles, a closed condition on their Grassmannian. This also gives the closed stabilizer scheme when needed; it retains infinitesimal parameters.

**Lemma 5.8. Openness of the reduced members needed here.** On a smooth projective variety \(X\) of positive dimension \(g\) over an algebraically closed field, the reduced divisors in a nonzero complete linear system form an open subset of its projective parameter space.

**Proof.** Write \(T=\mathbf P(H^0(X,L))\). On \(X\times T\), the universal section locally has equation \(f\). The locus defined by \(f=0\) and all components of its differential along \(X\) is closed: changing a local trivialization multiplies \(f\) by a unit, and changes its differential by that unit modulo \(f\). Denote this closed scheme by \(Z\). It is proper over \(T\), since \(X\) is projective. Its geometric fibre is exactly the nonsmooth locus of the corresponding divisor, by the smooth local-coordinate criterion.

We spell out the field assertion used here. If \(K/k\) is a finitely generated field extension of transcendence degree \(d\) over a perfect field, then \(\dim_K\Omega_{K/k}=d\). In characteristic zero this follows by choosing a transcendence basis and differentiating the finite separable extension, as proved in [Kähler differentials](../../AG-CA/src/kahler-differentials.md), Lemma 6.1 and Theorem 6.2. In characteristic \(p\), choose any transcendence basis and put \(F=k(t_1,\ldots,t_d)\). If \([K:F]=h\), Frobenius gives \([K^p:F^p]=h\), whereas \([F:F^p]=p^d\). The tower formula yields \([K:K^p]=p^d\). Successively adjoin elements not in the preceding field over \(K^p\). Each adjunction has degree \(p\), since its \(p\)-th power is already there, so this gives \(d\) elements \(z_1,\ldots,z_d\) whose monomials with exponents less than \(p\) form a basis of \(K/K^p\). Since \(k\subset K^p\), differentiating these unique expressions proves that their differentials span \(\Omega_{K/k}\). The coordinate derivatives are well-defined derivations: multiplication reduces exponents using \(z_i^p\in K^p\), whose derivatives are zero. They send \(z_i\) to the standard coordinate vectors and prove independence. Thus the differential dimension is indeed \(d\). At the generic point of an integral \(d\)-dimensional variety the local ring is its function field. The already-proved differential smoothness criterion, [Smooth algebras over a field and the Jacobian criterion](../../AG-CA/src/smooth-algebras-over-a-field-and-the-jacobian-criterion.md), Theorem 2.1, now proves generic smoothness, and its open-locus proof gives a dense smooth open.

A divisor on a smooth variety is reduced if and only if this fibre has dimension at most \(g-2\). For a reduced divisor apply this generic smoothness argument to every prime component; the nonsmooth locus has smaller dimension. For a nonreduced divisor, a repeated prime component is contained in the nonsmooth locus: in a regular local trivialization, differentiating a multiple factor leaves its prime factor in every derivative. The equivalence also follows directly from unique factorization in regular local rings, supplied by [Regular local rings](../../AG-CA/src/regular-local-rings.md), Theorem 5.3. Thus it includes reducible divisors and characteristic-\(p\) repeated factors. In dimension one the condition means that \(Z_t\) is empty.

We verify openness without assuming a general geometric-reducedness openness theorem. Fix \(t_0\) with a reduced divisor. Embed \(X\) in a projective space. If \(g>1\), choose \(g-1\) hyperplanes whose common linear space \(W\) misses \(Z_{t_0}\). Choose them successively to avoid the finitely many current maximal components, then to avoid the final finite set; this works over the infinite algebraically closed field. The closed subset \(Z\cap(W\times T)\) has closed image under the proper projection and its image misses \(t_0\). On the complementary open \(U\), every \(Z_t\) misses \(W\), so its dimension is at most \(g-2\). Indeed a nonempty projective scheme of dimension at least \(g-1\) cannot miss the intersection of \(g-1\) hyperplanes: its affine cone has dimension at least \(g\), and successively imposing these linear equations leaves dimension at least one by the principal ideal theorem, hence a point other than the cone vertex. If \(g=1\), remove the closed image of \(Z\) itself. In either case every \(t\in U\) has reduced divisor. Taking these neighborhoods at all reduced members proves the assertion. \(\square\)

**Lemma 5.9. The complete translated system has no stabilizer.** Let \(L\) be ample over an algebraically closed field. The only subgroup scheme whose translations preserve every divisor in \(|L|\) is the identity subgroup. The same holds if only the reduced members are required to be preserved.

**Proof.** On \(K(L)\), triviality of \(\Lambda_0(L)\) says that the isomorphisms between \(t_a^*L\) and \(L\) form a \(\mathbf G_m\)-torsor. With composition they form a group \(G(L)\). Each isomorphism acts linearly on \(V=H^0(A,L)\ne0\); changing it by a scalar changes its action by that scalar. Thus there is a morphism \(K(L)\to\operatorname{PGL}(V)\). Let \(H\) be its kernel. It is finite by Lemma 4.5, and represents exactly the translations preserving all members of \(|L|\).

Over \(H\), the action of \(G(L)\) consists of scalar matrices. Dividing an isomorphism by its scalar yields the unique isomorphism inducing the identity on \(V\). This operation is regular: the scalar can be recovered from any chosen nonzero section and any coordinate where it is nonzero. It is independent of the initial lift. It therefore gives a group splitting over \(H\), or equivalently an \(H\)-linearization of \(L\) fixing every global section.

The global finite quotient theorem in [Quotients and torsors](quotients-and-torsors.md), Theorem 5.2, applies to translations by \(H\), because a finite orbit in the projective \(A\) lies in an affine open by Lemma 5.4 there. It yields a finite locally free torsor \(q:A\to B=A/H\) of degree \(r=\operatorname{rank}H\). Finite type descends through this covering. The diagonal of \(B\) is closed: its pullback along \(A\times A\to B\times B\) is the closed relation \(A\times H\), and closed immersions descend by ideal descent. Commutativity descends the group law. The quotient is proper: any closed subset after any base change has closed image in the base because its inverse image in the proper \(A\) does, and \(q\) is surjective. It is geometrically integral: its geometric underlying space is an irreducible image of \(A\), and \(\mathcal O_B\hookrightarrow q_*\mathcal O_A\) makes it geometrically reduced. Thus \(B\) is an abelian variety.

Module descent at the beginning of [Quotients and torsors](quotients-and-torsors.md) descends the linearized line bundle to \(M\) on \(B\), and identifies its sections with the invariant sections upstairs. Our linearization fixes all sections, so \(H^0(B,M)=V\). The bundle \(M\) is ample. One direct check uses determinant norms: choose a section of a sufficiently high very ample power \(L^a=q^*M^a\) avoiding the finite fibre over a given point. Its norm is a section of \(M^{ar}\) nonvanishing there. The inverse image of its nonvanishing open is a principal open in the affine open \(A_s\): its defining function is \(q^*\operatorname{Norm}(s)/s^r\), the ratio of two sections of the same line bundle. It is therefore an invariant affine open. The affine effective quotient theorem, Theorem 4.3 of [Quotients and torsors](quotients-and-torsors.md), makes its quotient affine; its represented quotient is precisely the norm's nonvanishing open in \(B\), by the uniqueness of the sheaf quotient. These opens cover \(B\), proving ampleness.

Apply Propositions 5.5 and 5.6 to \(L=q^*M\) and \(M\). Their higher cohomology vanishes, so
\[
\begin{aligned}
h^0(A,L)&=\chi(A,L)\\
&=r\chi(B,M)=r\,h^0(B,M).
\end{aligned}
\]
The two nonzero spaces of sections were equal, so \(r=1\). A finite rank-one group scheme with an identity is the identity subgroup. Thus \(H=1\).

Lemma 5.7 supplies a reduced member of \(|L|\), and Lemma 5.8 proves that the reduced members form a nonempty open subset of \(\mathbf P(V)\). Choose a projective frame in that open. Such a choice exists: the open conditions that all frame points lie in the chosen open and that the first \(\dim V\) lines form a basis and the last line has every basis coefficient nonzero have nonempty intersection in the irreducible product of projective spaces. The scheme stabilizer of a projective frame is the identity in \(\operatorname{PGL}(V)\): fixing its basis lines makes a representative matrix diagonal, and fixing the final line makes all diagonal entries equal, over every test ring. Consequently a subgroup fixing all reduced members lies in \(H=1\), including its infinitesimal directions. If \(\dim V=1\), \(\operatorname{PGL}(V)\) is already trivial. \(\square\)

**Theorem 5.10. The second and third powers.** Over every field, an ample line bundle \(L\) on an abelian variety has \(L^2\) globally generated and \(L^n\) very ample for every \(n\ge3\).

**Proof.** For \(\dim A=0\), \(A=\operatorname{Spec}k\), and every power of every line bundle is trivial and embeds this point in \(\mathbf P^0\). Otherwise work over an algebraic closure; generation and the closed-immersion property of the morphism defined by the complete space of sections descend faithfully flatly. Proposition 5.5 makes \(L\) effective, and Proposition 4.7 generates \(L^2\).

We first prove that \(|L^3|\) separates distinct points \(P,Q\). Put \(h=Q-P\ne0\). Lemma 5.9 supplies a reduced \(D\in|L|\) with \(D+h\ne D\). There is \(R\in D\) with \(R+h\notin D\). Indeed otherwise \(D+h\) would be supported inside \(D\); these reduced divisors have the same positive hyperplane degree, so prime-component inclusion would force equality. Put \(a=P-R\). Then \(D+a\) contains \(P\) and misses \(Q\). Choose \(b\) so that \(D+b\) and \(D-a-b\) also miss \(Q\). The excluded choices are two proper closed subsets of \(A\). The square gives

\[
(D+a)+(D+b)+(D-a-b)\sim3D.
\]

This member contains \(P\) and misses \(Q\).

Now let \(0\ne v\in T_{A,P}\), and translate it to the invariant vector field \(\delta\) on \(A\). If \(\delta\) were tangent to every reduced member of \(|L|\), then it would lie in the Lie algebra of their common stabilizer, contrary to Lemma 5.9. To check this implication precisely, on an affine chart write a reduced member as \(f=0\). Tangency on its dense smooth locus says \(\delta(f)=0\pmod f\) on that locus, hence everywhere on this reduced divisor. Thus \(\delta(f)\in(f)\). The automorphism \(1+\epsilon\delta\) over \(k[\epsilon]/\epsilon^2\) preserves its ideal, which is exactly the infinitesimal stabilizer condition.

Consequently some reduced \(D\in|L|\) has a smooth point \(R\) where \(\delta\) is not tangent. Translate by \(a=P-R\), and choose \(b\) so that the other two translated divisors miss \(P\). The same displayed triple sum has a simple zero at \(P\) with nonzero derivative on \(v\). It separates that tangent direction. A further generic choice of \(a,b\) makes all three translates miss a given point, so \(|L^3|\) has no base points.

Generation, point separation and tangent separation now imply a closed immersion by the independently proved Lemma 1.6.

For every \(n\ge3\), replace the triple sum by

\[
\sum_{j=1}^n(D+a_j),\qquad \sum_{j=1}^n a_j=0.
\]

Keep the first translate that supplied point or tangent separation. The remaining parameters form \(A^{n-2}\), with the last parameter determined by the sum constraint. Each of their coordinate maps to \(A\), including that last sum map, is surjective. Requiring any remaining divisor to contain the tested point is therefore a proper closed condition. Avoid their finite union. Only the first divisor then contributes a zero at the tested point; the others are units there, preserving its separation or its nonzero first derivative. For generation, use the full zero-sum parameter space \(A^{n-1}\) and avoid the analogous conditions for all divisors. The square identifies the resulting divisor with \(nD\) for the original \(D\in|L|\). The same closed-immersion argument proves very ampleness for every \(n\ge3\). \(\square\)

The divisor notation above denotes **pushforward** translation \(D+a\). It corresponds to \(t_{-a}^*L\). Using \(t_a^*D\) instead moves the origin to \(-a\); keeping this sign prevents a point-separation error in a translation-based proof.

### How much projective space is necessary

**Theorem 5.11. The dimension obstruction.** A positive-dimensional abelian variety of dimension \(g\) cannot embed in \(\mathbf P^{2g-1}\). If \(g\ge3\), it cannot embed in \(\mathbf P^{2g}\) either.

**Proof.** We give the required degree and self-intersection calculation directly with vector bundles and finite resolutions. Write \(K_0(X)\) for the ring generated by vector bundles, with relation \([E]=[E']+[E'']\) for a short exact sequence and multiplication induced by tensor product. Euler characteristic is an additive homomorphism from this ring to \(\mathbf Z\). For a vector bundle set \(\lambda_t(E)=\sum_j[\bigwedge^jE]t^j\). An exterior-power filtration of a short exact sequence has successive quotients \(\bigwedge^aE'\otimes\bigwedge^{j-a}E''\); consequently \(\lambda_t(E)=\lambda_t(E')\lambda_t(E'')\). This defines the same operation for formal differences by division of power series with constant term one. These definitions require no intersection-theory theorem.

Suppose \(i:A\hookrightarrow\mathbf P^m\) is an embedding and put \(L=i^*\mathcal O(1)\). Necessarily \(m\ge g\). Both schemes are smooth, so this is a regular immersion: at a geometric closed point, the regular-local quotient theorem in [Regular local rings](../../AG-CA/src/regular-local-rings.md), Proposition 1.4, makes its ideal a regular sequence of length \(m-g\); these local generators persist on neighborhoods and descend to the original field. The normal bundle \(N\) has rank \(r=m-g\). The tangent-normal sequence, Proposition 1.3 and the projective-space Euler sequence give
\[
[N]=(m+1)[L]-(g+1)[\mathcal O_A].
\]
The Euler sequence itself is obtained by differentiating homogeneous coordinates: \(\mathcal O\to\mathcal O(1)^{m+1}\) sends \(1\) to the coordinate tuple, and its quotient is the tangent bundle on each standard chart. In particular
\[
\begin{aligned}
\lambda_t(N)&=\frac{(1+[L]t)^{m+1}}{(1+t)^{g+1}}\\
&=(1+t)^r\sum_{j=0}^{m+1}\binom{m+1}{j}\\
&\qquad\cdot([L]-1)^j\frac{t^j}{(1+t)^j}.
\end{aligned}
\]
The coefficient of \(t^{r+1}\) is
\[
\binom{m+1}{r+1}([L]-1)^{r+1}.
\]
Indeed all terms with \(j\le r\) are polynomials in \(t\) of degree at most \(r\), while the \(j=r+1\) term contributes its constant denominator coefficient. Since a rank-\(r\) bundle has zero \((r+1)\)-st exterior power, this class vanishes. Multiply by \([L]^a\) and take Euler characteristic. By Proposition 5.5 this gives
\[
\binom{m+1}{r+1}\Delta^{r+1}\bigl(a^g\chi(L)\bigr)=0
\qquad(a\in\mathbf Z).
\]
If \(m<2g\), then \(r+1\le g\), and this finite difference is a nonzero polynomial: its leading coefficient is
\(\chi(L)g(g-1)\cdots(g-r)>0\). The integer binomial coefficient is positive as well. This contradiction proves \(m\ge2g\).

It remains to analyze \(m=2g\). We first justify the finite resolution used in the numerical comparison. By the proved Serre graded-module construction, the coherent sheaf \(i_*\mathcal O_A\) on \(\mathbf P^m\) is the sheafification of a finite graded module over \(S=k[X_0,\ldots,X_m]\). Such a module has a finite graded free resolution. Here is a proof of the finiteness: choose minimal homogeneous generators, then minimal homogeneous generators of every kernel. Noetherianity makes each set finite, giving a graded free resolution \(F_\bullet\) with every differential entry in \(S_+=(X_0,\ldots,X_m)\). Minimality follows by lifting a basis modulo \(S_+\); graded Nakayama proves surjectivity because a finite graded module is bounded below. The Koszul complex of the variables resolves \(k=S/S_+\) in length \(m+1\): adjoining one variable forms the cone of multiplication by that variable, a nonzerodivisor on the preceding quotient. The double complex formed from this Koszul resolution and \(F_\bullet\) computes \(\operatorname{Tor}^S(M,k)\) in either direction. Thus its Tor is zero above \(m+1\), whereas \(F_\bullet\otimes_S k\) has zero differentials. Its terms in those degrees must be zero, so \(F_\bullet\) terminates. Sheafification gives a finite resolution by sums of twists of \(\mathcal O_{\mathbf P^m}\).

Let \(T=[\mathcal O_{\mathbf P^m}(-1)]\). The alternating class of that resolution is a Laurent polynomial \(p(T)\). The Koszul complex of the \(m+1\) coordinates is exact on projective space, because on every standard chart one coordinate is a unit. It gives \((1-T)^{m+1}=0\) in \(K_0(\mathbf P^m)\). Reduce the Laurent polynomial as
\[
p(T)=\sum_{s=0}^{m}b_s(1-T)^s.
\]
All \(b_s\) are integers: negative powers of \(T=1-(1-T)\) also have integer Taylor coefficients to this finite order. The projective-space cohomology calculation and the binomial difference identity give, for every integer \(a\),
\[
\begin{aligned}
\chi\bigl((1-T)^s\otimes\mathcal O(a)\bigr)
&=\sum_{j=0}^s(-1)^j\binom{s}{j}\\
&\qquad\cdot\binom{a-j+m}{m}\\
&=\binom{a+m-s}{m-s}.
\end{aligned}
\]
The left side for \(p(T)\) is \(\chi(A,L^a)=\chi(L)a^g\). The polynomials on the right have distinct degrees \(m-s\). With \(m=2g\), comparison therefore gives
\[
b_s=0\quad(s<g),\qquad b_g=g!\chi(L)=:d>0.
\]
This also proves directly that \(d\) is the usual projective degree: taking \(g\) generic hyperplane differences of the Hilbert polynomial leaves this constant length. The hyperplanes can be chosen successively as nonzerodivisors on the smooth, hence Cohen–Macaulay, variety until the intersection is zero-dimensional; the multiplication exact sequences compute its length as that difference. A field extension to an infinite field preserves all these numerical quantities.

Restrict the finite resolution to \(A\) and take its alternating Euler characteristic. Its terms give
\[
\begin{aligned}
\chi\bigl(i^*p(T)\bigr)
&=d\,\chi\bigl((1-L^{-1})^g\bigr)\\
&\quad+\sum_{s>g}b_s\,\chi\bigl((1-L^{-1})^s\bigr)\\
&=d^2.
\end{aligned}
\]
In fact Proposition 5.5 gives
\[
\chi\bigl((1-L^{-1})^s\bigr)
=\chi(L)\sum_{j=0}^s(-1)^j\binom{s}{j}(-j)^g,
\]
which is \(g!\chi(L)=d\) for \(s=g\) and zero for \(s>g\).

There is a second computation of the same restricted complex. The local Koszul resolution of the regular immersion shows that its homology sheaves are \(\bigwedge^jN^\vee\): after restriction, all equations in the Koszul differential become zero. Change of generators acts by the corresponding exterior powers on the conormal module, so these local identifications glue. Euler additivity for a finite complex consequently gives
\[
\chi\bigl(i^*p(T)\bigr)=\chi\bigl(\lambda_{-1}(N^\vee)\bigr).
\]
The dual of the normal-bundle class is
\([N^\vee]=(2g+1)[L^{-1}]-(g+1)\).
In the preceding power-series computation replace \(L\) by \(L^{-1}\) and \(r\) by \(g\), and sum the coefficients of degrees zero through \(g\) with alternating signs. Terms indexed by \(j<g\) vanish at \(t=-1\), since they contain the polynomial factor \((1+t)^{g-j}\); the \(j=g\) term remains. Hence
\[
\lambda_{-1}(N^\vee)
=\binom{2g+1}{g}(1-L^{-1})^g.
\]
Its Euler characteristic is \(\binom{2g+1}{g}d\). Comparing the two computations gives
\[
\begin{gathered}
d^2=\binom{2g+1}{g}d,\\
d=\binom{2g+1}{g},\qquad g!\mid d.
\end{gathered}
\]

The final divisibility fails for every \(g\ge3\). For \(g=3,4,5,6,7\), the binomial coefficients are respectively \(35,126,462,1716,6435\), none divisible by the respective factorial. For \(g=8\), \(\binom{17}{8}=24310<8!=40320\). The ratio \(R_g=\binom{2g+1}{g}/g!\) satisfies
\[
\frac{R_{g+1}}{R_g}
=\frac{(2g+3)(2g+2)}{(g+1)^2(g+2)}<1\quad(g\ge3),
\]
as expansion reduces the inequality to \(g^3-5g-4>0\). Thus \(0<R_g<1\) for every \(g\ge8\), also preventing divisibility. This proves the second obstruction. \(\square\)

In dimension one the possible degree in \(\mathbf P^2\) is \(3\); in dimension two the necessary degree in \(\mathbf P^4\) is \(10\). The degree calculation is a necessary condition, not an existence construction of those surfaces.

## 6. The degree and étaleness of multiplication

**Theorem 6.1. Finite locally free multiplication.** If \(d\) is a nonzero integer, then

\[
[d]:A\longrightarrow A
\]

is finite, surjective and locally free of degree \(d^{2g}\). In particular

\[
A[d]=\ker[d]
\]

is finite locally free over \(k\) of rank \(d^{2g}\).

**Proof.** Choose \(N\) as in (15). Theorem 5.1 gives \([d]^*N\simeq N^{d^2}\), an ample line bundle.

We first show that every geometric fibre is zero-dimensional. If a fibre had positive dimension, it would contain an integral projective curve \(C\): take a positive-dimensional irreducible component and successively cut by hyperplanes until its dimension is one. The pullback of \(N\) to that curve is trivial, because \([d]\) is constant on the fibre. On the other hand \(N^{d^2}|_C\) is ample and therefore has positive degree. The trivial line bundle has degree zero, a contradiction.

The morphism \([d]\) is proper, as a morphism between proper schemes with separated target. Its zero-dimensional fibres make it quasi-finite, and a proper quasi-finite morphism is finite. After extending to an algebraic closure, its closed image has dimension \(g\), since a finite morphism preserves the dimension of its source and image. The target is irreducible of dimension \(g\); a proper closed subset has smaller dimension. Thus the image is all of \(A\), proving surjectivity, which descends to \(k\).

For flatness, again work over an algebraic closure. At every closed point of the source and its image, the two local rings are regular of dimension \(g\), since \(A\) is smooth. The source ring is Cohen–Macaulay, and the local fibre has dimension zero. The local dimension equality therefore satisfies miracle flatness [Stacks, Tag 00R4], so \([d]\) is flat at every closed point. The flat locus of this finite-presentation morphism is open. Any nonempty complement on a scheme of finite type over the algebraically closed field has a closed point, so the complement is empty. Flatness descends, and finite flatness of finite presentation is finite local freeness.

Let its rank be \(r\), constant because \(A\) is connected. We compute \(r\) with Hilbert polynomials. For a finite morphism, pushforward is exact and the projection formula gives

\[
\chi(A,N^{d^2m})
=\chi\bigl(A,[d]_*\mathcal O_A\otimes N^m\bigr).
\tag{16}
\]

Here \([d]_*\mathcal O_A\) is a vector bundle of rank \(r\). For any rank-\(r\) vector bundle \(E\) on an integral projective \(g\)-fold, the leading coefficient of \(\chi(E\otimes N^m)\) is \(r\) times that of \(\chi(N^m)\). To verify this, take \(t\) large enough that \(E\otimes N^t\) is globally generated, and choose \(r\) sections forming a basis at the generic point. They give an injection

\[
(N^{-t})^{\oplus r}\longrightarrow E
\]

with cokernel supported in dimension less than \(g\). Injectivity follows because the source is torsion-free on the integral scheme and the map is generically injective. The cokernel's Hilbert polynomial has degree less than \(g\), and replacing \(m\) by \(m-t\) does not change the leading coefficient. This proves the assertion. In dimension zero the cokernel is zero and the assertion is the same rank calculation.

Write the positive leading coefficient of \(\chi(N^m)\) as \(c\), so its degree is \(g\). The two sides of (16) have leading coefficients \(c\,d^{2g}\) and \(rc\). Thus \(r=d^{2g}\). Finally the fibre over \(0\), namely \(A[d]\), inherits this rank by base change. \(\square\)

*Comparison locators:* [Stacks, Tag 0BFG] and the general degree calculation [Stacks, Tag 0BEX]. The proof uses the Hilbert-polynomial leading term, so it does not require a Riemann–Roch formula for abelian varieties.

**Theorem 6.2. The étaleness criterion.** If \(g>0\), then \([d]\) is étale exactly when \(d\) is invertible in \(k\). For \(d\ne0\), the same criterion holds for the finite group scheme \(A[d]\). If \(g=0\), every \([d]\), including \([0]\), is the identity of \(\operatorname{Spec}k\).

**Proof.** For \(d\ne0\), Theorem 6.1 supplies finite flatness. The differential at the identity is

\[
\operatorname{Lie}([d])=d\,\operatorname{id}_{\operatorname{Lie}(A)}.
\tag{17}
\]

Indeed the tangent group law adds tangent vectors, as proved in the Lie-algebra lesson; induction and inversion give (17) for every integer. Translation identifies the differential at any geometric point with that at \(0\).

If \(d\) is invertible, these differentials are isomorphisms. The relative cotangent module vanishes at every geometric closed point, hence everywhere by Nakayama and finite type. Thus \([d]\) is unramified; finite flat unramified morphisms are étale.

If \(d=0\) in \(k\) and \(g>0\), (17) is zero on a nonzero \(g\)-dimensional tangent space, so \([d]\) is not unramified at \(0\) and cannot be étale. The left exactness of the Lie functor gives

\[
\operatorname{Lie}(A[d])=\ker\operatorname{Lie}([d])
=\operatorname{Lie}(A)
\]

in this case. A finite étale scheme over a field has zero tangent space, so \(A[d]\) is not étale either. In the invertible case it is an étale base change of \([d]\).

The integer \(d=0\) gives a constant morphism; if \(g>0\), its fibre over \(0\) is \(A\), so it is not étale. If \(g=0\), Section 1 identifies \(A\) with the trivial group scheme, proving the stated exception. \(\square\)

*Comparison locator:* [Stacks, Tag 0BFH], which assumes a nonzero abelian variety. The dimension-zero exception must also be retained when using a summary of the torsion properties.

Over an algebraically closed field, the surjectivity in Theorem 6.1 makes \(A(k)\) a divisible abelian group: every point has a \(d\)-division point for every \(d\geq1\). Surjectivity on points follows because every nonempty finite fibre over that field has a rational point.

### Quotients by finite schematic subgroups

**Proposition 6.3 (finite quotients of abelian varieties).** Let \(K\hookrightarrow A\) be a finite subgroup scheme. The fppf quotient \(Q=A/K\) is an abelian variety. The quotient map \(q:A\to Q\) is finite locally free and surjective, of rank \(\dim_k k[K]\), and

\[
K\times_k A\xrightarrow{\sim}A\times_Q A,
\qquad (h,a)\longmapsto(a,a+h).
\tag{I.1}
\]

Its kernel is exactly \(K\). These assertions commute with arbitrary field extension.

**Proof.** The translation action is schematically free: the inverse to the map into its relation recovers \(h\) as the difference of the two coordinates. Thus \(K\times A\rightrightarrows A\) is an equivalence relation, with its two projections finite locally free. Each orbit is a finite set. Projectivity of \(A\), and *Quotients and torsors*, Lemma 5.4, put every such set in an affine open. The full finite-quotient theorem in that lesson, Theorem 5.2, therefore represents the fppf quotient by a scheme \(Q\), supplies a finite locally free surjection \(q\), and proves (I.1).

Since \(A\) is commutative, addition and inversion induce operations on the quotient sheaf. Representability makes these scheme morphisms; their identities follow from the sheaf identities. Its identity fibre is \(K\), by (I.1).

We check the geometric properties needed for our definition of an abelian variety. The quotient is of finite type over \(k\). On a quotient affine chart its rings have the form \(C\subset B\), with \(B\) finite over \(C\) and of finite type over \(k\). Here is the needed finite-type argument. Take \(C\)-module generators \(b_1,\ldots,b_s\) of \(B\), including \(1\), and \(k\)-algebra generators of \(B\). Put in a \(k\)-subalgebra \(C_0\subset C\) the finitely many coefficients expressing the algebra generators and all products \(b_i b_j\) in those module generators. Their \(C_0\)-span is a subalgebra containing the algebra generators, hence is all of \(B\). Consequently \(B\) is finite over the Noetherian finite-type algebra \(C_0\); its submodule \(C\) is finite over \(C_0\), so \(C\) is of finite type over \(k\).

The inverse image of \(\Delta_Q\) under the faithfully flat finite map \(q\times q\) is the closed relation \(A\times_QA\subset A\times A\): it is the inverse image of \(K\) under the difference map. Closed immersions descend faithfully flatly, by the ideal/module descent in *Quotients and torsors*, its opening descent section. Thus \(Q\) is separated. For any \(k\)-scheme \(T\) and closed subset \(Z\subset Q_T\), its inverse image in \(A_T\) is closed and has the same image in \(T\), since \(q_T\) is surjective. That image is closed by properness of \(A\). Thus \(Q\) is universally closed and hence proper.

After any field extension \(L/k\), the surjection \(A_L\to Q_L\) makes \(Q_L\) irreducible. It also makes \(Q_L\) reduced: on an affine open \(V\subset Q_L\), faithful flatness injects \(\Gamma(V,\mathcal O)\) into \(\Gamma(q_L^{-1}V,\mathcal O)\), a reduced ring because \(A_L\) is integral. Therefore \(Q\) is geometrically integral, and is an abelian variety. The finite locally free rank of \(q\) is the rank of its identity fibre \(K\), because \(Q\) is connected. Finally the quotient sheaf and the relation both commute with field extension; uniqueness of their representing scheme gives the base-change assertion. \(\square\)

This proposition includes infinitesimal subgroup schemes. It does not replace \(K\) by its reduced points.

### Recognizing an isogeny and measuring its kernel

**Theorem 6.4 (equivalent isogeny criteria).** For a homomorphism \(f:A\to B\) of abelian varieties the following conditions are equivalent:

1. \(f\) is surjective and its schematic kernel is finite;
2. \(f\) is surjective and \(\dim A=\dim B\);
3. \(\ker f\) is finite and \(\dim A=\dim B\);
4. \(f\) is finite, locally free and surjective.

A map satisfying them is an **isogeny**. Its degree is

\[
\deg f=[k(A):f^*k(B)]
=\operatorname{rank}_{\mathcal O_B}f_*\mathcal O_A
=\dim_k k[\ker f].
\tag{I.2}
\]

It is a torsor under \(\ker f\), and \(B\simeq A/\ker f\) as fppf sheaves and schemes.

**Proof.** First suppose \(K=\ker f\) is finite. Proposition 6.3 gives \(q:A\to Q=A/K\). The homomorphism \(f\) factors uniquely through \(\bar f:Q\to B\). Its kernel as an fppf sheaf is trivial: lift a section of \(Q\) locally to \(A\), and if its image in \(B\) is zero, that lift belongs to \(K\). A group homomorphism with trivial sheaf kernel is a monomorphism. The map \(\bar f\) is quasi-compact and has reduced source. *Group schemes over a field*, Proposition 5.8, therefore makes it a closed immersion. Thus every homomorphism with finite kernel factors as a finite locally free quotient followed by a closed immersion.

If \(f\) is also surjective, that closed immersion has full image in the reduced scheme \(B\); its defining ideal is zero. Hence \(Q\simeq B\), proving condition 4 and equal dimensions. If instead \(\dim A=\dim B\), finiteness of \(q\) gives \(\dim Q=\dim A\). A proper closed subset of the integral variety \(B\) has smaller dimension, so the closed immersion again has full image and is an isomorphism. This proves the implications from conditions 1 and 3.

Now suppose condition 2 holds. Dominance embeds \(k(B)\) into \(k(A)\). The dimension/transcendence-degree formula makes this an algebraic finitely generated extension, hence finite. Every affine chart of the generic fibre has a finitely generated \(k(B)\)-domain inside this finite field extension; all its elements are algebraic, so this chart is the spectrum of a finite field extension. The generic fibre is therefore zero-dimensional. Choose a point of that fibre and extend the field to its residue field. Translation by its lift identifies the generic fibre after that extension with the base change of \(\ker f\). Thus the kernel is zero-dimensional. Dimension is unchanged by field extension here: tensor a finite Noether normalization with the larger field, retaining its injective finite inclusion. The kernel's underlying set is finite, since it is Noetherian and zero-dimensional. It is a closed subscheme of the projective \(A\), so Lemma 5.4 of *Quotients and torsors* gives one affine open containing it. Its affine algebra has a finite Noether normalization by a polynomial ring of the same dimension; in dimension zero that ring is \(k\). Thus its algebra is finite-dimensional, \(\ker f\) is finite, and condition 1 follows.

Condition 4 gives a finite identity fibre and equal dimensions, so implies conditions 1 and 3. The torsor assertion follows from the schematic identity

\[
A\times K\simeq A\times_B A,
\qquad(a,h)\mapsto(a,a+h),
\]

whose inverse is difference of coordinates. Since \(f\) is an fppf covering, this also identifies its sheaf quotient with \(B\).

For the degree, the rank of \(f_*\mathcal O_A\) is constant on the connected \(B\). At its generic point it is the dimension of \(k(A)\) over \(k(B)\); at its rational identity it is the vector-space dimension of the coordinate algebra of \(K\). This proves (I.2). \(\square\)

*Exact algebra providers for the dimension step:* *Krull dimension and Noether normalization*, Corollary 3.2, Lemma 4.1 and Theorem 4.2. They supply normalization, strict dimension drop and the affine-domain dimension formula; the preceding paragraph gives the zero-dimensional specialization explicitly. The separate workflow record binds this provider text and the exact used statements.

**Corollary 6.5 (composition and cancellation).** Isogenies are preserved by field extension and composition, and

\[
\deg(gf)=\deg(g)\deg(f).
\tag{I.3}
\]

If \(u:W\to A\) and \(v:B\to C\) are isogenies and \(h_1,h_2:A\to B\) are homomorphisms such that \(vh_1u=vh_2u\), then \(h_1=h_2\).

**Proof.** Finite locally free surjections have the stated permanence properties. Their ranks multiply: locally a rank-\(a\) module over a rank-\(b\) finite locally free algebra has rank \(ab\) over the base. This proves the degree formula by (I.2).

Since \(u\) is faithfully flat, descent of morphisms cancels it. Thus \(h_1-h_2\) factors through \(\ker v\). A morphism from \(A\) to any finite affine \(k\)-scheme is induced by a map of its algebra into \(\Gamma(A,\mathcal O_A)=k\), by Lemma 1.1 of the current lesson, and is therefore constant. This particular constant is zero because it is a homomorphism. Hence \(h_1=h_2\). \(\square\)

### A finite group scheme is killed by its rank

The next lemma makes the reverse isogeny argument valid for nonreduced kernels. Counting only geometric points would give the wrong integer.

**Lemma 6.6 (rank annihilates a finite commutative group scheme).** If \(H/k\) is finite and commutative of rank \(d\), then \([d]_H=0\) as a scheme morphism.

**Proof.** Put \(D=k[H]\), a \(d\)-dimensional algebra, and

\[
S^d(D)=(D^{\otimes d})^{\mathfrak S_d}.
\]

We first construct a canonical algebra map \(\nu:S^d(D)\to k\) from the determinant norm. Choose a vector-space basis \(e_1,\ldots,e_d\). For a multi-index \(\alpha\) with \(|\alpha|=d\), let \(s_\alpha\) be the sum of the distinct basis tensors with \(\alpha_i\) occurrences of \(e_i\). These orbit sums form a basis of the invariant space, in every characteristic. Expand

\[
\det m_{\sum_i T_i e_i}=\sum_{|\alpha|=d}n_\alpha T^\alpha,
\qquad\nu(s_\alpha)=n_\alpha,
\tag{I.4}
\]

where \(m_a\) is multiplication by \(a\) on \(D\). This prescription is independent of the basis: it is characterized by

\[
\nu(a^{\otimes d})=\det(m_a)
\]

as a polynomial identity after every scalar extension. The coefficients of the universal vector \(a=\sum T_i e_i\) recover every \(\nu(s_\alpha)\).

To verify multiplicativity without division by \(d!\), take independent universal vectors \(a=\sum T_i e_i\) and \(b=\sum U_i e_i\). The identities

\[
\begin{gathered}
(ab)^{\otimes d}=a^{\otimes d}b^{\otimes d},\\
\det(m_{ab})=\det(m_a)\det(m_b).
\end{gathered}
\]

and coefficient comparison in \(T^\alpha U^\beta\) give
\(\nu(s_\alpha s_\beta)=\nu(s_\alpha)\nu(s_\beta)\).
Also \(\nu(1^{\otimes d})=1\). Thus \(\nu\) is an algebra map. Its construction commutes with scalar extension. It is unchanged by any algebra automorphism \(\sigma\) of \(D\), because \(m_{\sigma(a)}=\sigma m_a\sigma^{-1}\) has the same determinant; comparing coefficients proves invariance on all symmetric tensors.

Commutativity of \(H\) makes the iterated addition map \(H^d\to H\) symmetric. Its comorphism \(\Delta_d:D\to D^{\otimes d}\) lands in \(S^d(D)\). The composite \(\nu\Delta_d\) defines a point \(c\in H(k)\).

Let \(R\) be any \(k\)-algebra and \(h\in H(R)\). Translation by \(h\) is an automorphism of the finite free \(R\)-algebra \(D_R\), so the determinant norm point is invariant under simultaneous translation of its \(d\) factors. On the other hand, adding the translated factors adds \([d]h\) to their sum. Applying these two descriptions to \(\nu_R\Delta_d\) gives

\[
c_R+[d]h=c_R.
\]

Cancellation in \(H(R)\) gives \([d]h=0\). This holds for every \(R\), including rings with nilpotents, and proves the scheme identity. \(\square\)

**Theorem 6.7 (reverse isogeny).** If \(f:A\to B\) is an isogeny of degree \(d\), there is a unique homomorphism \(f':B\to A\) with

\[
f'f=[d]_A,\qquad ff'=[d]_B.
\tag{I.5}
\]

It is an isogeny. Consequently being isogenous over \(k\) is an equivalence relation on abelian varieties over \(k\).

**Proof.** Lemma 6.6 applied to \(\ker f\) shows that \([d]_A\) is invariant under its translations. The quotient property of Theorem 6.4 gives a unique \(f'\) with \(f'f=[d]_A\). It is a homomorphism because that identity can be checked after the faithfully flat cover \(f\times f\) of \(B\times B\). Now

\[
ff'f=f[d]_A=[d]_Bf.
\]

Cancelling the faithfully flat \(f\) gives the second identity. The first identity and surjectivity of \([d]_A\), proved in Theorem 6.1, make \(f'\) surjective. Its source and target have equal dimension, so Theorem 6.4 makes it an isogeny. Uniqueness already came from the quotient property. Reflexivity uses the identity, transitivity composition, and symmetry \(f'\). Every map is defined over the same field \(k\); this does not assert that an isogeny over an extension descends. \(\square\)

### Separable and infinitesimal parts

**Theorem 6.8 (separable and radicial criteria).** Let \(f:A\to B\) be an isogeny, with schematic kernel \(K\).

- The following are equivalent: \(k(A)/k(B)\) is separable; \(f\) is étale; \(K\) is étale; and \(\operatorname{Lie}(f)\) is an isomorphism.
- The following are equivalent: \(k(A)/k(B)\) is purely inseparable; \(f\) is radicial; and \(K\) is connected.

Here radicial means universally injective. A connected finite group scheme over a field is geometrically connected, because its rational identity is its sole point and its residue field is \(k\).

**Proof of the first row.** A finite locally free map is étale exactly when its relative differential sheaf is zero. If the function-field extension is separable, its differential module vanishes at the generic point, so the étale locus is a nonempty open. Over an algebraic closure this open contains a rational point. Translating that point to every other rational point preserves the homomorphism and its local differentials, so \(f\) is étale at all rational points. A nonempty closed support of its coherent relative differential sheaf would have a rational closed point; hence the support is empty. Étaleness descends to \(k\). Conversely an étale generic fibre has a separable function-field extension.

If \(f\) is étale, its identity fibre \(K\) is étale. If \(K\) is étale, the torsor description identifies the base change of \(f\) by its own fppf cover with the projection \(A\times K\to A\); that projection is étale, so \(f\) is étale by descent. Finally translation identifies all tangent maps with the map at the identity. Smoothness and equal dimensions make that map an isomorphism exactly when the relative cotangent space is zero there; Nakayama and the same translation argument give the étale criterion. The cotangent and finite-flat-unramified criteria are supplied by *Étale morphisms and their local structure*, Sections 1-2; their exact programme provider is recorded separately.

For the second row, if \(K\) is connected then \(k[K]\) is an Artinian local ring with residue field \(k\): the identity supplies that residue field and its kernel is nilpotent. Its scalar extension to any field remains local, with nilpotent augmentation ideal. Every geometric fibre of \(f\) is a translate of this group scheme after an algebraically closed extension, hence has exactly one point. This makes \(f\) universally injective: two points in any base-changed fibre would yield two distinct geometric points after a common algebraically closed extension. Conversely a radicial map has a singleton geometric identity fibre, so \(K\) is connected. At the generic point, the finite field extension must then be purely inseparable: its number of embeddings into an algebraic closure of the base field is its separable degree, and distinct embeddings give distinct points of the geometric generic fibre. A singleton fibre forces that degree to be one.

It remains to prove that a purely inseparable function-field extension forces connectedness. Let \(K^0\) be its identity component. *Group schemes over a field*, Theorems 2.3 and 3.1, prove that \(K^0\) is an open and closed geometrically connected subgroup and \(K/K^0=\pi_0(K)\) is finite étale. Proposition 6.3 factors \(f\) as

\[
A\xrightarrow{q}C=A/K^0\xrightarrow{h}B.
\tag{I.6}
\]

The map \(q\) has connected kernel, hence is radicial by the argument just given. The kernel of \(h\), calculated as an fppf sheaf, is \(K/K^0\); thus \(h\) is an isogeny with étale kernel. The first row makes \(k(C)/k(B)\) separable. As a subextension of the assumed purely inseparable extension \(k(A)/k(B)\), it must be trivial. Its degree is one, so \(K/K^0\) has rank one and \(K=K^0\). This proves the missing implication. \(\square\)

**Corollary 6.9 (canonical factorization).** Every isogeny has a factorization (I.6) into a radicial isogeny followed by an étale isogeny. It is unique up to a unique isomorphism of the intermediate abelian variety commuting with the maps. Moreover

\[
\deg q=\operatorname{rank}K^0,
\qquad\deg h=\operatorname{rank}\pi_0(K),
\qquad
\#K(\overline k)=\deg h.
\tag{I.7}
\]

**Proof.** Existence and degrees were proved above. In any other factorization \(f=h'q'\), the connected kernel of \(q'\) lies in \(K^0\). Conversely the map from \(K^0\) to the étale kernel of \(h'\) is zero: over an algebraic closure a connected scheme has constant image in a discrete finite scheme, and the identity determines that constant. Thus \(\ker q'=K^0\). Both intermediate schemes represent \(A/K^0\), giving the unique isomorphism. Over \(\overline k\), each component of \(K\) is an Artinian local scheme with one point, and components are indexed by \(\pi_0(K)(\overline k)\); this proves the last formula. \(\square\)

**Corollary 6.10 (torsion invariants under isogeny).** In characteristic \(p>0\), geometric \(p\)-rank is unchanged by arbitrary field extension. If \(A,B\) are isogenous over \(k\), they have the same geometric \(p\)-rank. For every \(\ell\ne\operatorname{char}k\), an isogeny induces an injection \(T_\ell(A)\to T_\ell(B)\) with cokernel killed by its degree. It is an isomorphism if \(\ell\) does not divide that degree, and becomes an isomorphism after tensoring with \(\mathbf Q_\ell\).

**Proof.** The finite algebra of \(A[p]_{\overline k}\) is a product of Artinian local algebras, each with residue field \(\overline k\) and nilpotent maximal ideal. After any algebraically closed extension \(\Omega/\overline k\), each factor still has nilpotent augmentation ideal and residue field \(\Omega\), so stays local and contributes exactly one point. The number of geometric points is therefore unchanged. For an arbitrary extension \(L/k\), choose an algebraic closure of \(L\) and embed \(\overline k\) into it over \(k\); the argument proves the field-extension assertion.

Let \(d=\deg f\). The kernel of the map on \(p^r\)-torsion points has at most \(d\) elements, by (I.2). Formula (24) of the current lesson therefore gives

\[
p^{r f_A}/d\le p^{r f_B}.
\]

Letting \(r\) grow gives \(f_A\le f_B\). The reverse isogeny of Theorem 6.7 gives the opposite inequality.

On Tate modules the two composites of \(f\) and \(f'\) are multiplication by \(d\). Theorem 7.2 makes the modules free over the domain \(\mathbf Z_\ell\), so multiplication by the nonzero integer \(d\) is injective. This proves injectivity of \(T_\ell(f)\). Its cokernel is killed by \(d\), because \(T_\ell(f)T_\ell(f')=d\). If \(d\) is a unit in \(\mathbf Z_\ell\), this cokernel is zero; after tensoring with \(\mathbf Q_\ell\) it is zero in every case. All maps commute with the Galois action by their definition over \(k\). \(\square\)

### 6.11. The Picard scheme and the dual variety

Let \(A/k\) be an abelian variety of dimension \(g\), over any field. All functor assertions below include test schemes with nilpotents. Projectivity is Theorem1.5 of the existing lesson. The full scheme construction used below is [Relative divisors and the existence of the Picard scheme, Theorem8.1](../../AG-HP/src/relative-divisors-and-the-existence-of-the-picard-scheme.md). Its projective, flat, geometrically integral hypotheses apply to \(A/k\); its representing scheme commutes with every base change. The square-zero tangent calculation is [The structure of the Picard scheme, Proposition2.1](../../AG-HP/src/the-structure-of-the-picard-scheme.md#2-the-square-zero-sequence-and-the-tangent-space). The component results are the already proved Theorems2.2–2.3 in [Group schemes over a field](group-schemes-over-a-field.md).

#### Cohomology without a general Hopf-algebra classification

**Lemma 6.11. The coherent cohomology bialgebra.** Put \(H=\bigoplus_{i\ge0}H^i(A,\mathcal O_A)\). It is a finite-dimensional connected graded-commutative and graded-cocommutative bialgebra, with counit in degree zero. It vanishes in degrees greater than \(g\). Every degree-one element is primitive.

**Proof.** The complete projective finiteness proof in [Serre's theorems on projective schemes](../../AG-QC/src/serres-theorems-on-projective-schemes.md) makes each cohomology group finite-dimensional. The affine-cover comparison in [Čech cohomology](../../AG-QC/src/cech-cohomology.md) computes these groups by an ordered Čech complex: intersections in a finite affine cover of a separated scheme are affine, and affine quasi-coherent higher cohomology vanishes. Its cup construction and comparison with sheaf cohomology are given in [Cohomology of sheaves on ringed spaces](../../AG-QC/src/cohomology-of-sheaves-on-ringed-spaces.md).

Here is the Künneth calculation in this situation. Use two finite affine covers of \(A\). The rectangular double Čech complex on their product has terms the tensor products over \(k\) of the two Čech terms. Resolve first in one cover and then in the other. Affine acyclicity shows that its total complex computes the cohomology of \(A\times A\). Over a field, every complex splits, as a complex of vector spaces, into its cohomology with zero differential and two-term identity complexes: choose complements to boundaries in cycles, and complements to cycles in each term; the differential identifies the latter with the next boundaries. Tensoring a two-term identity complex remains contractible, by its explicit contraction. Thus total cohomology is

\[
H^n(A\times A,\mathcal O)=
\bigoplus_{i+j=n}H^i(A,\mathcal O_A)\otimes_kH^j(A,\mathcal O_A).
\tag{D.1}
\]

This is the cross-product map on Čech cocycles, so is independent of the choices and functorial under morphisms. The total differential and the interchange of two factors use the sign \((-1)^{ij}\). Cup product is the pullback of cross product by the diagonal. It is consequently associative and graded commutative. Pullback by the addition \(m:A\times A\to A\), followed by (D.1), is a comultiplication compatible with cup product. Associativity and commutativity of \(m\) give coassociativity and graded cocommutativity. The zero section gives its counit. Proper geometric integrality gives \(H^0=k\), by Lemma3.2 of the existing lesson.

The vanishing above dimension can also be seen directly here. Extend the field faithfully flatly to an algebraic closure; the finite Čech complex commutes with this extension. Choose a projective embedding of \(A\). Successively choose \(g+1\) hyperplanes with no common intersection on \(A\): at each stage avoid the finitely many components of the preceding intersection, whose dimension drops by one; after \(g\) choices avoid its finitely many points. The complements of these hyperplanes in \(A\) are affine and cover it. Their Čech complex has no terms above degree \(g\), proving the vanishing. Faithful flatness returns it to \(k\).

Finally, in degree one the only summands of \(H\otimes H\) have bidegrees \((1,0)\) and \((0,1)\). The two counit identities make the comultiplication of \(u\in H^1\) exactly \(u\otimes1+1\otimes u\). Thus \(u\) is primitive. \(\square\)

**Lemma 6.12. The degree-one bound and its equality case.** Let \(H\) be any connected nonnegatively graded, graded-commutative bialgebra over a field, with \(H^i=0\) for \(i>g\). Then \(\dim H^1\le g\). If \(\dim H^1=g\), cup product gives an isomorphism of bialgebras

\[
\bigwedge H^1\simeq H,
\tag{D.2}
\]

with every element of \(H^1\) primitive. This includes characteristic two.

**Proof.** Every degree-one element is primitive, by the counit calculation above. If \(u_1,\ldots,u_n\) are independent, the component of the iterated comultiplication of \(u_1\cdots u_n\) in \((H^1)^{\otimes n}\) is the sum of their permutation tensors, with the Koszul signs. These tensors are independent after extending the \(u_i\) to a basis; each occurs with coefficient \(1\) or \(-1\), both nonzero in every characteristic. Thus the product is nonzero. Taking \(n=g+1\) would contradict the degree bound. This proves \(\dim H^1\le g\).

Suppose equality, and choose a basis \(u_1,\ldots,u_g\). In characteristic different from two, graded commutativity gives \(u_i^2=0\). In characteristic two \(u_i^2\) is primitive, since the two middle terms in its comultiplication cancel. If \(u_i^2\ne0\), the product

\[
u_i^2\prod_{j\ne i}u_j
\]

has degree \(g+1\), so is zero. Its iterated comultiplication component with degrees \((2,1,\ldots,1)\) is \(u_i^2\) in the first factor tensored with the signed sum of permutation tensors of the other \(g-1\) basis elements. Primitivity makes these the only terms in that component. It is nonzero, a contradiction. This also covers \(g=1\), when the degree-two element itself is zero; \(g=0\) is immediate. Hence all basis squares vanish.

There is now a bialgebra map \(\bigwedge H^1\to H\). Its degree-\(n\) component is injective: the iterated comultiplication followed by projection to \((H^1)^{\otimes n}\) sends distinct wedge basis elements to permutation sums with disjoint tensor supports. Write \(E\subset H\) for this exterior sub-bialgebra and \(\omega=u_1\cdots u_g\ne0\).

If \(H\ne E\), choose the smallest degree \(d\) for which an element \(x\in H^d\) has nonzero class in \(H^d/E^d\). All lower-degree pieces of \(H\) equal those of \(E\). Therefore

\[
\begin{gathered}
\Delta x=x\otimes1+1\otimes x+
\sum_{0<i<d}w_i,\\
w_i\in E^i\otimes E^{d-i}.
\end{gathered}
\]

The product \(\omega x\) is zero by degree. In \(\Delta(\omega x)\), take bidegree \((g,d)\) and project the second factor to \(H^d/E^d\). Every term with \(w_i\), or with \(x\otimes1\), has its second factor in \(E^d\) and disappears. From \(1\otimes x\) only the term \(\omega\otimes1\) of \(\Delta\omega\) has the required bidegree. The resulting tensor is \(\omega\otimes[x]\ne0\). This contradicts \(\Delta(\omega x)=0\). Thus \(H=E\), proving (D.2). No division by a factorial or Hopf classification theorem was used. \(\square\)

**Example 6.13. The general bialgebra wording needs correction.** The tensor-product assertion in AV ChapterVI6.12, if read as an assertion about all graded-commutative bialgebras without cocommutativity, is false. Over \(\mathbf Q\) let

\[
\begin{gathered}
H=\bigwedge(x,y)\otimes\mathbf Q[z],\\
|x|=|y|=1,\qquad |z|=2,
\end{gathered}
\]

make \(x,y\) primitive, and put

\[
\Delta z=z\otimes1+1\otimes z+x\otimes y.
\]

These formulas extend as an algebra map to the graded tensor product. They are coassociative: both iterates of \(\Delta z\) are the three copies of \(z\), plus \(x\otimes y\otimes1\), \(x\otimes1\otimes y\), and \(1\otimes x\otimes y\). The degree-zero projection is a counit. But its comultiplication is not graded cocommutative, since the graded flip takes the last term to \(-y\otimes x\). Any connected graded bialgebra generated by one homogeneous element has that element primitive: there are no smaller positive-degree pieces in which a reduced comultiplication could lie. Such a bialgebra is graded cocommutative, and so is any tensor product of them. Therefore the displayed bialgebra cannot be their tensor product as bialgebras. An underlying-algebra classification is a different assertion. Lemma6.12 supplies the precise full bialgebra statement needed for the abelian variety here.

**Example 6.14. Properness is needed for the coherent bound.** The source's unrestricted group-variety wording in ChapterVI6.15 is also false. For an elliptic curve \(E/k\), the smooth connected group \(E\times\mathbf G_a\) has dimension two, but

\[
H^1(E\times\mathbf A^1,\mathcal O)
=H^1(E,\mathcal O_E)\otimes_k k[t]
\]

has infinite dimension. The equality follows from the same finite affine Čech cover of \(E\), tensoring with \(k[t]\); the line has no higher affine cohomology. Lemmas6.11–6.12 apply to the proper abelian variety, and avoid this defect.

#### The representing dual and its universal bundle

**Theorem 6.15. The Picard identity component is an abelian variety.** The fppf Picard functor of \(A\) is represented by a separated locally finite-type scheme \(P\). Its identity component \(A^t=P^0\) is an abelian variety of dimension \(g\). For every ample line bundle \(L\) on \(A\), the translation map

\[
\varphi_L:A\longrightarrow A^t,
\qquad
a\longmapsto[t_a^*L\otimes L^{-1}]
\tag{D.3}
\]

is an isogeny, with the finite schematic kernel \(K(L)\) of Lemma4.5. Moreover \(h^1(A,\mathcal O_A)=g\).

**Proof.** Representability and its arbitrary-base-change assertion are the exact Theorem8.1 cited above. The scheme group law comes from tensor product. The field component theorem makes \(P^0\) open, of finite type, and geometrically irreducible. Proposition2.1 of the Picard-structure lesson computes

\[
T_0P=H^1(A,\mathcal O_A).
\tag{D.4}
\]

Its proof uses transition functions \(1+\varepsilon a_{ij}\) on a square-zero thickening, modulo the changes \(1+\varepsilon b_i\) of trivialization. Thus it retains the full infinitesimal scheme structure.

The normalized bundle

\[
\Lambda_0(L)=m^*L\otimes p_1^*L^{-1}
\otimes p_2^*L^{-1}\otimes L_0
\tag{D.5}
\]

on \(A\times A\), rigidified on the second factor's origin, represents the map (D.3) on every test scheme. The square identity makes it a group homomorphism. Its connected source and origin value put its image in \(P^0\). Lemma4.5 proves that its kernel on all test schemes is \(K(L)\), and proves this closed kernel finite for ample \(L\).

The map is proper, since its source is proper over \(k\) and its target separated. Its geometric fibres, when nonempty, are translates of the finite kernel, hence zero-dimensional. It is quasi-finite and thus finite by the proper finite-fibre theorem, already used in Theorem6.1. Its closed image has dimension \(g\). On the other hand (D.4) and Lemmas6.11–6.12 give

\[
g\le\dim P^0\le\dim T_0P
=h^1(A,\mathcal O_A)\le g.
\tag{D.6}
\]

The middle inequality holds because translation identifies the geometric local dimensions with that at the identity, and local dimension is at most embedding dimension. These arguments work after every field extension. The image's closed support is therefore all of the geometrically irreducible \(P^0\).

Over an algebraic closure, (D.6) says the Noetherian local ring at the identity has dimension equal to embedding dimension, so is regular. Over that perfect field it is smooth. Translating by geometric points makes every closed point smooth; the open smooth locus contains them all and hence all points of the finite-type scheme. Smoothness descends to \(k\). The dominant quasi-compact reduced-target homomorphism theorem, [Group schemes over a field](group-schemes-over-a-field.md), Proposition5.6, now makes \(\varphi_L\) faithfully flat. Thus it is a finite faithfully flat isogeny.

Properness of \(P^0\) follows without assuming properness of arbitrary Picard components. For any \(T\), a closed set in \(P^0_T\) has closed inverse image in \(A_T\); its image in \(T\) is closed because \(A\) is proper. Surjectivity of \(A_T\to P^0_T\) identifies this image with the original closed set's image. Thus \(P^0\) is universally closed; finite type and separation make it proper. It is smooth and geometrically integral, hence an abelian variety, and Theorem1.5 gives its projectivity. Equality throughout (D.6) proves the final assertion. \(\square\)

**Corollary 6.16. The full coherent cohomology algebra.** Over every field,

\[
H^\bullet(A,\mathcal O_A)=
\bigwedge H^1(A,\mathcal O_A),\qquad
h^i(A,\mathcal O_A)=\binom gi.
\tag{D.7}
\]

The isomorphism preserves cup product, addition's comultiplication, and all field extensions. **Proof.** Theorem6.15 gives the equality case of Lemma6.12, applied to Lemma6.11. The Čech cross products and cup maps used there commute with field extension. \(\square\)

**Proposition 6.17. The normalized Poincaré bundle.** There is a line bundle \(\mathcal P_A\) on \(A\times A^t\), rigidified to be trivial on \(\{0\}\times A^t\) and \(A\times\{0\}\). It represents the universal algebraically trivial line bundle and is unique with these compatible rigidifications. For any \(T/k\), maps \(T\to A^t\) correspond to its pullbacks, modulo base line bundles, or equivalently to their rigidifications at the origin of \(A_T\).

**Proof.** On each affine \(T\), a finite affine Čech equalizer and flatness over the field give \((p_T)_*\mathcal O_{A_T}=\mathcal O_T\); Lemma3.2 gives the starting \(H^0(A,\mathcal O_A)=k\). Thus an automorphism of a line bundle on \(A_T\) is multiplication by a unit from \(T\). If it respects its origin rigidification, that unit is one.

Any bundle can be rigidified by tensoring with the inverse of its restriction to \(0_T\). Two bundles with the same relative Picard class have unique rigidification-preserving local isomorphisms. These isomorphisms automatically satisfy descent cocycles. Faithfully flat descent for line bundles therefore makes rigidified isomorphism classes an fppf sheaf, equal to the relative Picard sheaf. Apply its representing property to the identity of \(P\); this constructs the universal rigidified bundle. Restrict to \(A\times P^0\). At the origin of \(P^0\) it represents the trivial class; the origin rigidification uniquely trivializes that slice, compatibly at \((0,0)\). Uniqueness follows from the same automorphism calculation. This proof uses every test scheme, including nonreduced ones. \(\square\)

**Proposition 6.18. Pullback defines the dual homomorphism.** A homomorphism \(f:A\to B\) induces \(f^t:B^t\to A^t\) by pullback of line bundles. Identity, composition and arbitrary field extension satisfy

\[
(gf)^t=f^t g^t,\qquad
(\operatorname{id}_A)^t=\operatorname{id}_{A^t}.
\tag{D.8}
\]

**Proof.** Pullback of the normalized universal bundle gives a rigidified family on \(A\times B^t\), so representability gives an actual scheme morphism. Tensor product and pullback commute, making it a group homomorphism on all test schemes. Its connected source and origin value put it in \(A^t\). The asserted identities are identities of pullback functors, and thus of representing maps. The base-change assertion is the Picard representing theorem and the uniqueness of rigidified families. \(\square\)

**Theorem 6.19. Algebraic triviality and addition of dual maps.** For a normalized line bundle \(M\) representing any \(T\)-point of \(A^t\),

\[
m^*M\simeq p_1^*M\otimes p_2^*M
\quad\text{on }A_T\times_T A_T,
\tag{D.9}
\]

compatibly with the origin rigidifications. Consequently \((f+g)^t=f^t+g^t\) for all homomorphisms with the same source and target.

**Proof.** Apply (D.5) to the universal normalized \(\mathcal P_A\), with its parameter \(A^t\). This produces a morphism

\[
F:A\times A^t\longrightarrow A^t,
\qquad(a,M)\longmapsto\varphi_M(a).
\]

To justify the indicated codomain, the representing map starts in \(P\); its connected source and zero origin value put it in \(P^0\). Its source and target are abelian varieties. Corollary2.3 of the existing lesson makes every origin-preserving morphism between them a homomorphism. Its restrictions to both axes are zero: \(\varphi_M(0)=0\), and the trivial bundle has zero translation map. Decompose \((a,M)=(a,0)+(0,M)\). Thus \(F=0\) as a scheme morphism.

The bundle (D.5) is rigidified along the second \(A\)-factor's origin. The zero representing map therefore makes it the trivial rigidified bundle, by Proposition6.17; there is no residual parameter-line ambiguity. For normalized \(M\), (D.5) is precisely (D.9). Pull back the universal statement to every \(T\). In particular it retains nilpotents. For \(f,g:C\to A\), pull (D.9) back by \((f,g)\). This identifies \((f+g)^*M\) with \(f^*M\otimes g^*M\); representability gives the equality of dual maps.

For ordinary field-valued bundles, membership in \(P^0\) is exactly algebraic equivalence to zero. A connected parameter family connecting a bundle to the trivial bundle maps into the Picard scheme and stays in its identity component. Conversely the Poincaré family on the connected variety \(P^0\) connects its point to its origin. Thus the terminology in this theorem agrees with the usual definition by connected parameter families. \(\square\)

**Theorem 6.20. Poincaré reducibility over the given field.** If \(i:C\hookrightarrow A\) is an abelian subvariety, there is an abelian subvariety \(D\subset A\), defined over \(k\), such that \(C\times D\to A\) by addition is an isogeny. In particular, for an isogeny-generating quotient \(q\colon J\twoheadrightarrow B\) of an abelian variety, an abelian subvariety of \(J\) maps isogenously onto \(B\).

**Proof.** Choose an ample \(L\) on \(A\). Restriction \(i^t:A^t\to C^t\) is Proposition6.18. Set \(u=i^t\varphi_L\). On \(C\), the normalized bundle formula (D.5) gives

\[
u i=\varphi_{i^*L}:C\longrightarrow C^t.
\]

The restriction of an ample bundle to the closed subvariety is ample, so Theorem6.15 makes this an isogeny. Thus \(u\) is surjective, and is faithfully flat by the reduced-target homomorphism theorem. Its fibres have dimension \(g-\dim C\). Define \(D=(\ker u)^0_{\mathrm{red}}\). Theorem8.8 of the existing lesson proves that this reduction is an abelian subvariety over \(k\), even when \(k\) is imperfect. It has that fibre dimension. The schematic intersection \(C\cap D\) is contained in the finite kernel of \(u i\). Hence addition \(C\times D\to A\) has finite kernel. It is proper with finite fibres, and has full-dimensional closed image. Geometric integrality of \(A\) makes that image all of \(A\). The same homomorphism theorem makes it faithfully flat, so it is an isogeny.

For the quotient statement take \(C=(\ker q)^0_{\mathrm{red}}\), whose dimension is \(\dim J-\dim B\), and the complement \(D\) just constructed. Its intersection with \(\ker q\) is finite: the kernel's finitely many components are translates of its identity component, and the latter has underlying reduction \(C\), while \(C\cap D\) is zero-dimensional. Consequently \(q|_D\) has finite kernel and \(\dim D=\dim B\). Properness, full-dimensional image and the reduced-target homomorphism theorem make \(D\to B\) an isogeny. All operations were performed over \(k\). \(\square\)

#### Source scope and credit

Edixhoven, van der Geer and Moonen, *Abelian Varieties*, preliminary version with 8 February2012 chapter footers, ChapterVI6.1–6.20, provides the comparison. The two scope corrections above preserve the source's actual bialgebra and nonproper-group wording rather than silently using them at false generality. The bounded bialgebra argument, Picard smoothness proof and ample isogeny construction are independently expressed here. The representing scheme and tangent calculation retain their exact existing programme providers. Poincaré's reducibility theorem is included as the complete specific input needed for the semistable-reduction argument. Biduality, the general structure of the Néron–Severi group, Fourier transforms and the precise Cartier-dual kernel of a general dual isogeny are separate mathematical statements; no proof of them is claimed by this supplement.

### Complex uniformization and lattices

*Independently written and self-checked by GPT-6.1 Sol (OpenAI), in Codex at Ultra effort, 5 October 2026. This supplement is CC0 1.0. Existing provider lessons retain their own component notices and human-source credits.*

A complex abelian variety is a compact complex Lie group with a full lattice in its tangent space. The following proofs describe its exponential, every homomorphism, isogeny degrees and rational lattice commensurability.

#### The bounded analytic input

The analytic inputs below have complete programme proof providers.

The following statements are the inputs actually used.

1. Complex analytic spaces and analytification, Lemma 2.2 and Theorem 3.2 give holomorphic inverse and implicit functions, the analytification of a reduced complex variety, and functoriality for maps and products. Its Proposition 5.2 proves compactness of a projective variety's analytification. Theorem 4.1 identifies completed local rings and proves faithful flatness; Proposition 5.1 proves exactness, faithfulness and internal-Hom compatibility for coherent modules.
2. Local tools for bundles and transport, Lemma 2.A and Theorem 2.1 prove the local ODE theorem with smooth dependence on initial values, initial time and finite-dimensional parameters. This includes the norm Taylor estimates for the path-space integral operator, the inverse of its linearized fixed-point operator and all mixed time derivatives. Its Lemma 2.2 proves global existence of invariant equations on each finite time interval. Its Section 1 proves the contraction and smooth inverse-function results used there. The flow proof does not require the separately licensed partition-of-unity passages in Section 3.
3. Serre's comparison theorems and Chow's theorem, Theorem 3.1 gives coherent cohomological GAGA for projective reduced complex varieties. Its Theorem 6.2 algebraizes every holomorphic map between such varieties, uniquely. The actual proof uses Theorem 6.1 (Chow), Theorems 5.2 and 4.1 (coherent algebraization and full faithfulness), Lemma 5.1 (analytic generation) and Theorem 3.1, including its explicit comparison for twists.
4. The GAGA lesson's analytic vanishing provider is Claude's Theorems A and B on Stein manifolds, Theorem 4.1: all coherent analytic sheaves and every positive cohomological degree on a complex manifold with a smooth strictly plurisubharmonic exhaustion. Its analytic finiteness provider is Claude's Finiteness on compact complex spaces, Theorem 2.1: all coherent sheaves on compact complex spaces, in every degree. These are independent analytic arguments, not consequences assumed from GAGA. Their proofs use local coherent resolutions, the weighted bar-partial estimates, coherent section topologies, compact restriction maps, Schwartz's perturbation theorem and an exhaustion argument; the exact preceding bodies and their hashes are recorded in the intake.
5. The local analytic construction uses the bridge's Oka Theorem 2.1, local parametrization Theorem 4.1, Nullstellensatz Theorem 5.1 and dimension Theorem 5.4, and Cartan coherence Theorem 1.1 and Theorem 3.2. Their proof bodies were read, including the primitive-element/discriminant construction and the argument giving generators on a neighbourhood, rather than merely at one stalk.
6. Formal functions, Theorem 5.2 proves that a proper map with finite fibres over a locally Noetherian base is finite. It is used in the graph argument, with the exact completion comparison above.

The current GAGA structure-sheaf calculation also uses the existing Laurent series and homogeneous projections, Theorems 2–5. Their complete product estimates, extension on every \(\Omega_N\), homogeneous decomposition and signed contraction were read in Sections 2–4. That existing unit retains CC BY-SA 4.0, including its separately credited Lebl v1.9 Laurent component.

Here is the finite graph step, specifying why an analytic isomorphism of graphs suffices. If \(h:X^{\mathrm{an}}\to Y^{\mathrm{an}}\) is holomorphic and \(X,Y\) are reduced projective complex varieties, its graph is a closed reduced analytic subset of \((X\times Y)^{\mathrm{an}}\). Chow gives a reduced algebraic graph \(Z\subset X\times Y\). The proper first projection \(p:Z\to X\) has one point in each closed fibre, and those fibres are zero-dimensional. The proper fibre-dimension theorem makes all fibres zero-dimensional: a nonempty closed locus of positive-dimensional fibres would have a closed point. Thus \(p\) is finite by Formal functions 5.2.

At a closed point \(x\) let \(A=\mathcal O_{X,x}\) and \(B=(p_*\mathcal O_Z)_x\). The finite \(A\)-algebra \(B\) has one maximal ideal \(\mathfrak n\), because the closed fibre has one point. The quotient \(B/\mathfrak m_A B\) is an Artinian local algebra, so \(\mathfrak n^s\subset\mathfrak m_A B\) for some \(s\); also \(\mathfrak m_A B\subset\mathfrak n\). The two adic topologies are therefore cofinal. Exact finite-module completion gives \(B\otimes_A\widehat A=\widehat B\). The analytic graph isomorphism and the local analytic completion comparison identify \(\widehat A\to\widehat B\) with an isomorphism. Faithful flatness of \(A\to\widehat A\) makes \(A\to B\) an isomorphism. The coherent kernel and cokernel vanish at every closed point, hence everywhere. Since a finite map is the relative spectrum of its direct-image algebra, \(p\) is an isomorphism. The second projection composed with \(p^{-1}\) algebraizes \(h\). Uniqueness follows from uniqueness of its reduced graph. This is exactly the reduced projective scope needed below; it assumes neither arbitrary-proper nor nonreduced GAGA.

The preceding provider identification is a bounded point-of-use check. The foundational results on which the analytic courses rest are not proved here. For example the L² proof still uses Lebesgue integration, distributional calculus, mollifier approximation and Hilbert-space representation, and the Fréchet proof uses Baire and the stated algebraic completion results. Their programme locators remain explicit prerequisites.

#### The exponential and the quotient

**Lemma 6.21 (the invariant exponential).** Let G be a connected compact complex Lie group whose group law is commutative. Write V=T_0G, with its complex vector-space structure. There is a unique holomorphic homomorphism

\[
\operatorname{Exp}_G:(V,+)\longrightarrow G
\]

with derivative the identity at zero. It is surjective and a local biholomorphism; its kernel is discrete.

**Proof.** Regard V as a real tangent space. For v∈V put

\[
X_v(a)=(dL_a)_0v,\qquad L_a(b)=a+b.
\]

This is a smooth vector field, depending smoothly and real-linearly on v. The complete parameter-dependent local-flow theorem in Section 1 applies in each chart. A finite cover by smaller charts with compact closures supplies uniform short existence intervals for a fixed v; hence its integral curve extends for every real time on compact G. Alternatively the invariant-equation lemma gives the same extension by repeatedly translating one identity chart, on every finite time interval. For v in a neighbourhood of a fixed v_0 those short intervals can be chosen uniformly: the coordinate bounds for X_v and its position derivatives are uniform on a compact parameter neighbourhood. Finitely many such intervals cover [0,1], and composition of their smooth solution maps proves that

\[
\begin{gathered}
E(v)=\gamma_v(1),\qquad\gamma_v(0)=0,\\
\gamma_v'(t)=X_v(\gamma_v(t)).
\end{gathered}
\]

is smooth in v. This justifies dependence before differentiating a solution.

Uniqueness and time rescaling give γ_(sv)(t)=γ_v(st), including negative s, and translating a solution gives γ_v(t+t_0)=γ_v(t)+γ_v(t_0). For v,w, differentiate the curve γ_v(t)+γ_w(t). The differential of addition at (a,b), applied to (ξ,η), is

\[
(dL_b)_a\xi+(dL_a)_b\eta.
\]

Here commutativity identifies right and left translations. Substitution of the two invariant derivatives consequently gives X_(v+w) at their sum. The sum curve starts at zero, so uniqueness gives γ_(v+w)(t)=γ_v(t)+γ_w(t). In particular E(v+w)=E(v)+E(w).

The equality E(sv)=γ_v(s) gives (dE)_0(v)=γ_v'(0)=v. Since E is already smooth, this identifies its differential as a linear map, not just separate formal directional derivatives. Differentiating E(v+h)=E(v)+E(h) yields

\[
(dE)_v=(dL_{E(v)})_0.
\tag{CL.1}
\]

Every translation is holomorphic, so (CL.1) is complex-linear. In local complex coordinates E is C¹ and complex-differentiable in each variable: its real derivative is complex-linear. It is therefore holomorphic under the bridge's definition (continuous and holomorphic separately in each variable). The holomorphic inverse-function theorem makes E a local biholomorphism near zero and then, by translation, everywhere.

Its image contains an open neighbourhood of zero, and is an open subgroup. Every other coset is open too. Connectedness makes the image all of G. Local injectivity at zero makes ker E discrete. Finally, if another holomorphic homomorphism has identity derivative, its differential along t↦tv makes its image curve solve the same invariant initial-value equation. Uniqueness gives that homomorphism equal to E for every v. □

**Lemma 6.22 (discrete subgroups and compactness).** Let W be a finite-dimensional real vector space and Γ⊂W a discrete additive subgroup. If r=dim_R span_R Γ, then Γ has a Z-basis γ_1,…,γ_r that is real-linearly independent. The quotient W/Γ is compact precisely when span_R Γ=W.

**Proof.** Discreteness at zero supplies ε>0 such that no nonzero element of Γ has norm less than ε. Differences of elements of Γ also belong to Γ, so distinct elements have this uniform separation. In particular a compact subset meets Γ in finitely many points: cover it by finitely many balls of diameter less than ε. The same separation shows Γ is closed, because a convergent sequence of its elements is eventually constant.

Choose real-linearly independent δ_1,…,δ_r∈Γ spanning span_R Γ and put Δ=ΣZδ_i. Reducing the real coordinates of any element of Γ modulo integers puts a representative of its class modulo Δ in the compact parallelepiped Σ[0,1]δ_i. Thus Γ/Δ is finite. If N is its order, then

\[
N\Delta\subset N\Gamma\subset\Delta.
\]

A subgroup H⊂Z^r is free of rank at most r. For a direct proof induct on r: its projection to the first coordinate is either zero, reducing to r−1, or aZ for a>0. Choose h∈H projecting to a; subtraction of an integer multiple of h identifies H as the direct sum Zh⊕ker(projection). Induction applies to the kernel. Applying this to NΓ⊂Δ shows it has a free basis. Since it contains NΔ, its rational span is all Δ⊗Q, so its rank is r. In Δ-coordinates its r basis vectors form an integer matrix of nonzero rational determinant, hence of nonzero real determinant. They are real-linearly independent. Multiplication by N identifies Γ with NΓ; dividing those basis vectors by N gives the asserted basis of Γ. This also treats r=0, when Γ=0.

If the real span is W, the closed parallelepiped of this basis maps onto W/Γ, so the quotient is compact. If the span is proper, choose a nonzero real-linear functional ℓ:W→R vanishing on it. It descends to a continuous surjection W/Γ→R. A compact space cannot have R as its continuous image, proving the converse. □

**Theorem 6.23 (uniformization of a complex abelian variety; full CX.1).** If A/C is an abelian variety of dimension g and V_A=T_0A^an, then the invariant exponential gives

\[
0\longrightarrow\Lambda_A\longrightarrow V_A
\xrightarrow{\operatorname{Exp}_A}A^{\mathrm{an}}\longrightarrow0,
\qquad A^{\mathrm{an}}\simeq V_A/\Lambda_A,
\tag{CL.2}
\]

where Λ_A has a real-linearly independent Z-basis of length 2g. The exponential is a holomorphic covering homomorphism with derivative the identity.

**Proof.** The existing abelian-variety proofs give smoothness, commutativity, projectivity and H⁰(A,O_A)=C. The holomorphic implicit-function theorem applied to its smooth affine charts makes A^an a complex manifold of dimension g; analytification carries its group operations to holomorphic operations and respects their identities. Projective compactness makes A^an compact.

Cohomological GAGA in degree zero gives H⁰(A^an,O)=C. A connected component of a manifold is open, because a sufficiently small coordinate ball is connected; it is also closed. If the manifold were disconnected, the function equal to one on one component and zero on its complement would be a nonconstant global holomorphic function. Thus it is connected. Lemma 6.21 applies, with discrete kernel Λ_A.

For clarity, the quotient in (CL.2) is an analytic quotient, not merely a set bijection. Choose a ball U in V_A small enough that its difference set meets Λ_A only at zero and the exponential is a biholomorphism on U. Its translates give charts on V_A/Λ_A; changes between representatives are translations by lattice vectors and are holomorphic. The quotient is Hausdorff, since Λ_A is a closed subgroup, and is second countable because the open quotient map takes a countable basis to a basis. The induced map to A^an is bijective, and on these charts a local biholomorphism. Its inverse local maps agree by bijectivity, giving the analytic isomorphism. Compactness and Lemma 6.22 now give rank_Z Λ_A=dim_R V_A=2g. □

The exponential and lattice are canonical for the specified tangent space and derivative. Choosing a lattice basis is not canonical. When g=0, V_A=0, Λ_A=0 and A is the one-point group; every assertion above includes this case.

#### Homomorphisms, isogenies and rational lattices

**Theorem 6.24 (all homomorphisms).** For complex abelian varieties A_1,A_2 the derivative gives a bijection

\[
\operatorname{Hom}_{\mathbf C\text{-groups}}(A_1,A_2)
\ \simeq\
\{u\in\operatorname{Hom}_{\mathbf C}(V_1,V_2):
u(\Lambda_1)\subset\Lambda_2\}.
\tag{CL.3}
\]

The same correspondence, before algebraization, identifies holomorphic group homomorphisms of their analytic tori with the displayed linear maps. It respects addition and composition.

**Proof.** Let f be a holomorphic group homomorphism and u=(df)_0. Its derivative is complex-linear. Differentiating f(a+b)=f(a)+f(b) with respect to b at zero gives

\[
(df)_a(dL_a)_0v=(dL_{f(a)})_0u(v).
\]

Thus f carries γ_v to the invariant curve with initial velocity u(v). Uniqueness of that curve proves

\[
f\operatorname{Exp}_{A_1}
=\operatorname{Exp}_{A_2}u.
\tag{CL.4}
\]

Applying (CL.4) to a lattice vector gives uΛ_1⊂Λ_2. Surjectivity of the first exponential makes f uniquely determined by u.

Conversely a complex-linear u satisfying this inclusion induces the well-defined homomorphism

\[
\begin{gathered}
\bar u:V_1/\Lambda_1\longrightarrow V_2/\Lambda_2,\\
v+\Lambda_1\longmapsto u(v)+\Lambda_2.
\end{gathered}
\]

It is holomorphic: in a small quotient chart, use a lift to V_1, apply u and the second quotient map. Its derivative is u. Theorem 6.2 of the exact projective GAGA provider gives a unique algebraic morphism f with analytification \bar u. It preserves zero. Its two addition composites A_1×A_1→A_2 have the same analytification; uniqueness in that same theorem, applied to the reduced projective product, makes them equal as algebraic morphisms. Hence f is an algebraic group homomorphism. Every algebraic homomorphism analytifies, so this proves the claimed bijection. Differential and (CL.4) prove compatibility with addition and composition. □

**Theorem 6.25 (the isogeny criterion and its degree).** For f and u as in 6.24, f is an isogeny exactly when u is an isomorphism. In this case

\[
\ker f(\mathbf C)
\simeq u^{-1}\Lambda_2/\Lambda_1
\simeq\Lambda_2/u\Lambda_1,
\qquad
\deg f=[\Lambda_2:u\Lambda_1].
\tag{CL.5}
\]

The first identification sends v+Λ_1 to Exp_(A_1)(v); the second is induced by u.

**Proof.** The existing isogeny criterion, Theorem 6.4 of the abelian-varieties lesson, makes an isogeny finite locally free, surjective and of equal dimensions. Its function-field extension in characteristic zero is separable. The exact first row and proof of Theorem 6.8 then make it étale and make its identity tangent map an isomorphism. Thus u is invertible.

Conversely assume u invertible. Every target torus point has a representative w∈V_2, and the class of u^−1(w) maps to it. Hence f is surjective on complex points. Its algebraic image is closed, by properness; a proper closed subset of a finite-type complex variety misses a closed complex point. Its image is therefore the whole target. The dimensions agree, so Theorem 6.4 makes f an isogeny.

Both uΛ_1 and Λ_2 are full lattices and uΛ_1⊂Λ_2. Reduction modulo a parallelepiped of the first lattice, exactly as in Lemma 6.22, gives finite index. Formula (CL.4) identifies the kernel point classes with u^−1Λ_2/Λ_1. The indicated u identifies this finite group with Λ_2/uΛ_1. The characteristic-zero étaleness just proved makes the finite schematic kernel étale. Over C its coordinate algebra is a product of copies of C, one for each kernel point. By the degree formula in Theorem 6.4 its vector-space dimension equals deg f, proving the index formula. This explains explicitly why the analytic point count computes the schematic degree here. □

**Theorem 6.26 (rational commensurability; full CX.2).** With isogeny defined over C,

\[
A_1\sim_{\mathbf C}A_2
\quad\Longleftrightarrow\quad
\exists\,u:V_1\xrightarrow{\sim}V_2\text{ complex-linear such that }
u(\Lambda_1\otimes_{\mathbf Z}\mathbf Q)
=\Lambda_2\otimes_{\mathbf Z}\mathbf Q.
\tag{CL.6}
\]

Rational spans are taken inside the underlying additive complex vector spaces. Equivalently uΛ_1 and Λ_2 have finite-index intersection in each.

**Proof.** If f is an isogeny, 6.25 gives the required isomorphism u and finite index uΛ_1⊂Λ_2; tensoring with Q gives equality of rational spans. The reverse-isogeny theorem already proved in the lesson ensures that this use agrees with the symmetric isogeny relation.

Conversely choose \(u\) as on the right. Choose lattice bases \(\lambda_{1,j},\lambda_{2,j}\). Write each \(u(\lambda_{1,j})\) as a rational linear combination of the second basis. There are finitely many coefficients. A positive integer \(n\) clearing all their denominators gives \(nu(\Lambda_1)\subset\Lambda_2\). The map \(nu\) is still a complex-linear isomorphism, so 6.24 algebraizes it and 6.25 makes it an isogeny. No integrality of the original \(u\) was assumed.

For the intersection formulation, equality of rational spans also supplies m>0 with mΛ_2⊂uΛ_1. Thus uΛ_1∩Λ_2 contains both n(uΛ_1) and mΛ_2 and has finite index in each. Conversely a finite-index inclusion becomes equality after tensoring with Q, so a finite-index intersection gives equality of both rational spans. This proves the equivalence. □

In particular, for every nonzero integer n,

\[
A[n](\mathbf C)
=n^{-1}\Lambda_A/\Lambda_A
\simeq\Lambda_A/n\Lambda_A
\simeq(\mathbf Z/|n|\mathbf Z)^{2g},
\qquad \deg[n]=|n|^{2g}.
\tag{CL.7}
\]

The middle isomorphism is multiplication by n, and the last uses any lattice basis. When g=0 the group is trivial and the degree is one. These conclusions do not assert that every abstract compact complex torus is projectively embeddable: algebraization in 6.24 is applied to the given abelian varieties, whose projectivity has already been proved.

#### Source credit and scope

The analytic bridge is independently written by Claude Opus 5.5 (Anthropic), with its CC0 declaration. Self-checked by the writing AI. The existing Laurent unit retains CC BY-SA 4.0 and its credited Jiri Lebl v1.9 component. These component terms remain attached to their exact companion readings.

The proofs use the smooth parameter ODE theorem and GAGA for reduced projective complex varieties. They do not assert algebraization for arbitrary proper or nonreduced spaces, or projectivity of every abstract compact complex torus. The analytic inputs retain their explicitly stated integration, distributional, Hilbert-space and Baire prerequisites. Bibliographic comparison does not substitute for those proofs.

### Biduality, isogeny kernels and the Picard component group

This independently written supplement is dedicated to CC0 1.0. It compares
the Edixhoven–van der Geer–Moonen preliminary *Abelian Varieties*,
Chapter VII, with the existing programme proofs. The sixteen results below continue the duality proofs. The base field is arbitrary, including
imperfect fields. Functor assertions concern all schemes over the field,
including schemes with nilpotents.

Write \(P_A=\operatorname{Pic}_{A/k}\) and \(A^t=P_A^0\). A bundle on \(A_T\)
is **normalized** if its restriction to \(0_T\) is trivialized. Tensoring
with the inverse of that restriction normalizes any bundle without changing
its relative Picard class. All universal bundles below carry this
normalization. The normalized difference bundle is

\[
\Lambda_0(L)=m^*L\otimes p_1^*L^{-1}\otimes p_2^*L^{-1}
                 \otimes \pi^*e^*L .
\tag{DU.1}
\]

For an unnormalized \(L\), write \(\Lambda(L)\) for the formula without
its last factor. Thus \(\Lambda(L)=\Lambda_0(L)\otimes\pi^*e^*L^{-1}\).

The proof order matters. 6.30–6.32 prove that \(\varphi_L=0\) is equivalent
to \([L]\in P_A^0\), using coherent cohomology and the already constructed
dual. 6.34 then proves that descended character bundles belong to \(P_B^0\).
Only after this do we prove the exact dual-isogeny kernel and biduality.
Neither torsion-freeness of Néron–Severi nor biduality is used in that bridge.

#### Earlier inputs

The current *Abelian varieties* lesson, results 6.11–6.20, supplies the
smooth representing Picard identity component of dimension \(\dim A\),
its normalized universal Poincaré bundle \(\mathcal P_A\), pullback dual
maps, addition of dual maps, and
\(m^*M=p_1^*M\otimes p_2^*M\) for normalized \(M\) in \(A^t(T)\).
Its results 2.3, 3.2, 3.5, 4.4–4.5, 5.1 and 6.1–6.9 give rigidity,
universal constants, maximal relative triviality, the square and cube
identities, finite ample translation kernels, the integer pullback formula,
finite multiplication and isogeny properties. Results 8.3–8.11 give
invariant differentials and Frobenius/Verschiebung. Finite Cartier duality,
including equality of ranks and its all-test scheme character functor,
is proved in *Group schemes, actions and Hopf algebras*, Theorem 3.1.

We use the actual proofs in AG-HP, [*Hilbert and Quot schemes*](../../AG-HP/src/hilbert-and-quot-schemes.md), Theorem 4.1
and Corollary 4.2, for the full Hilbert scheme; AG-QC, [*Base change and
the Grothendieck complex*](../../AG-QC/src/base-change-and-the-grothendieck-complex.md), Lemma 3.1 and Theorem 3.2, for a bounded finite
projective complex computing proper flat-sheaf cohomology after every base
change; and AG-DFG, [*Faithfully flat descent*](../../AG-DFG/src/faithfully-flat-descent.md), Theorems 2.5, 5.1 and 6.2,
for modules and morphisms. The component-group construction is already
proved in *Group schemes over a field*, Theorems 2.3 and 3.1. The proper
quasi-finite theorem remains the separately owned AG-MO, [*Zariski's Main
Theorem*](../../AG-MO/src/zariskis-main-theorem.md), Theorem 5.1. Exact observed revisions and hashes are retained
in the companion workflow record.

#### Homomorphisms in families

**Lemma 6.27 (the Hom scheme and its étale homomorphism subgroup).**
For projective \(k\)-schemes \(X,Y\), the scheme-morphism functor
\(\underline{\operatorname{Hom}}_{\rm Sch}(X,Y)\) is represented by a
separated scheme locally of finite type. For abelian varieties \(A,B\),
its group-homomorphism subfunctor \(\underline{\operatorname{Hom}}(A,B)\)
is represented by a separated étale commutative group scheme.

**Proof.** Use the full Hilbert scheme of \(X\times Y\), with universal
flat projective closed subscheme \(Z\). Graphs are exactly the families
for which \(Z\to X_T\) is an isomorphism. This is an open condition on
the parameter, as follows. On one finite-type Hilbert chart \(H\),
at a parameter where the geometric fibre projection is an isomorphism,
its non-quasi-finite locus is closed in \(Z\) and misses that fibre.
Projectivity of \(Z/H\) lets us remove its closed image in \(H\).
The projection is now proper quasi-finite, hence finite. Its coherent
algebra map \(\mathcal O_{X_H}\to g_*\mathcal O_Z\) has zero cokernel
on that fibre. Nakayama and removal of the proper image of that support
make it surjective. The kernel \(I\) now has zero fibre: flatness of
\(\mathcal O_Z\) over \(H\) makes tensoring this surjection sequence
exact on the left. Nakayama and properness of \(X/H\) remove the
kernel's support as well. The projection is an isomorphism on this
open neighbourhood. Conversely every graph lands there. Applying
this to the universal Noetherian charts represents graphs on arbitrary
\(T\): factorization through an open is detected on points. Projection
to \(Y_T\) recovers the map, with graph-taking as its inverse.

The conditions \(f(0)=0\) and \(f(a+a')=f(a)+f(a')\) are equalizers of
maps into the separated schemes representing maps from a point and
from \(A^2\) to \(B\). They cut out a closed subscheme of the graph
locus. Addition on \(B\) represents its commutative group law.

After algebraic closure, a tangent vector at the zero homomorphism
is a dual-number morphism reducing to zero. It differs from zero by
a derivation with values in \(\operatorname{Lie}(B)\otimes\mathcal O_A\).
Global sections of this sheaf are \(\operatorname{Lie}(B)\), since
\(H^0(A,\mathcal O_A)=k\). Its value at \(0_A\) must be zero, so the
derivation is zero. Translation in the Hom group identifies all its
geometric tangent spaces with this one. At a closed point of a
finite-type chart, \(\mathfrak m/\mathfrak m^2=0\); Nakayama makes
the local ring a field of dimension zero. Over an algebraically
closed field it is smooth of relative dimension zero. The étale
locus is open and a nonempty complement in a finite-type chart
has a closed point. Thus the whole scheme is étale. Descent returns
this conclusion to \(k\). \(\square\)

**Lemma 6.28 (translation maps for arbitrary parameter schemes).**
A line bundle \(L\) on \(A_T\) defines a homomorphism
\(\varphi_L:A_T\to A_T^t\) by (DU.1). It depends only on its relative
Picard class, is additive under tensor product, and commutes with
every change of \(T\). It therefore defines a group-scheme homomorphism

\[
\varphi:P_A\longrightarrow
          \underline{\operatorname{Hom}}(A,A^t).
\tag{DU.2}
\]

It is zero on \(P_A^0\). On a connected nonempty parameter scheme,
if one fibre is the zero homomorphism, the whole family is zero.

**Proof.** Formula (DU.1) is normalized on the first \(A\)-factor,
with parameter the second \(A\)-factor times \(T\). Representability
defines the map to \(P_A\). Connected geometric fibres of the second
\(A\), and the origin's zero value, place it in \(P_A^0\).
Replacing \(L\) by \(L\otimes\pi_T^*N\) leaves (DU.1) unchanged.
Tensor product and base change commute with the formula.

For the group identity we retain nilpotents as follows. The same
descent construction as result 6.17 supplies the rigidified universal
bundle on \(A\times P_A\), before restriction to \(P_A^0\).
The whole \(P_A\) is smooth: after algebraic closure each component
has a rational point and is a translate of the smooth \(P_A^0\).
On this reduced universal parameter scheme, the two addition maps
agree on every geometric fibre, by the square theorem. Their closed
equalizer has ideal vanishing on every point of the reduced source
\(A^2\times P_A\), hence has zero ideal. The universal map is a
homomorphism; pulling back proves this on arbitrary \(T\).

6.27 represents the resulting family by (DU.2). Result 6.19 makes
its restriction to \(P_A^0\) zero as a scheme morphism. The identity
section of an étale separated group scheme over \(k\) is open and
closed. Thus the zero locus in \(T\) is open and closed, and if
\(T\) is connected and has one zero fibre it is all of \(T\).
This includes nilpotents and needs no local-Noetherian hypothesis.
\(\square\)

**Corollary 6.29 (triviality and integer identities).**
For any \(T\) and \(L\) on \(A_T\), these are equivalent:
\(\varphi_L=0\); \(\Lambda(L)=p_2^*M\) for a bundle \(M\) on \(A_T\);
\(\Lambda(L)=\pi^*N\) for a bundle \(N\) on \(T\).
Then \(N=e^*L^{-1}\) and \(M=\pi_T^*N\). For connected nonempty
\(T\), these are equivalent to zero \(\varphi_{L_t}\) at one point.

For normalized \(L\) with \(\varphi_L=0\),
\(m^*L=p_1^*L\otimes p_2^*L\) compatibly on the two axes.
For \(f,g:Y\to A_T\), this gives
\([(f+g)^*L]=[f^*L\otimes g^*L]\) in the relative Picard group.
For every integer \(n\), \([n]^*L=L^n\) with normalization.

**Proof.** A zero representing map makes the rigidified family (DU.1)
trivial. If its unnormalized version is \(p_2^*M\), restriction to
\(\{0\}\times A_T\) gives \(M=\pi_T^*e^*L^{-1}\). This proves the
equivalences and identifications. 6.28 gives the fibre criterion.
Pull back the normalized addition identity by \((f,g)\).
Induction gives the formula for positive integers; its zero case
and restriction along \((1,-1)\) give zero and negative integers.
The source's condition “at some \(t\)” requires nonempty \(T\):
on the empty scheme the first conditions are vacuous but no point
exists. \(\square\)

#### The noncircular Picard criterion

**Lemma 6.30 (acyclicity of a nontrivial homogeneous bundle).**
If \(M\) is a nontrivial line bundle on \(A/k\) with \(\varphi_M=0\),
then \(H^q(A,M)=0\) for every \(q\).

**Proof.** Normalizing over a field changes only a constant
one-dimensional factor. 6.29 gives \([-1]^*M=M^{-1}\).
A nonzero section of \(M\) would give one of \(M^{-1}\).
Their product is a nonzero constant: it is nonzero at the generic
point of integral \(A\), and \(H^0(\mathcal O_A)=k\).
They are then nowhere zero, contradicting nontriviality of \(M\).
Thus \(H^0(A,M)=0\).

Choose the smallest higher degree \(q\) with nonzero cohomology,
if one exists. The composite \(A\to A^2\to A\),
\(a\mapsto(a,0)\mapsto a\), induces the identity through
\(H^q(A^2,m^*M)\). But \(m^*M=M\boxtimes M\), and the finite
affine double Čech complex over the field gives

\[
\begin{gathered}
H^q(A^2,M\boxtimes M)
\\
=\bigoplus_{i+j=q}H^i(A,M)\otimes H^j(A,M).
\end{gathered}
\]

Every summand vanishes: one index is zero, or one positive index
is smaller than \(q\). The identity factors through zero, a
contradiction. \(\square\)

**Lemma 6.31 (the precise cohomology comparison).**
For \(p:A\times S\to S\), Noetherian \(S\), and an invertible
\(E\), a bounded finite projective complex on each affine base
computes proper cohomology after every base change. Consequently:
if all fibre cohomology vanishes on an open, all \(R^qp_*E\) vanish
there; if all \(R^qp_*E\) vanish, all fibre cohomology vanishes.
The two projection Čech filtrations on \(A^2\) give the corresponding
Leray spectral sequences.

**Proof.** The sheaf is flat over \(S\). The actual Grothendieck-complex
proof gives a finite projective replacement of its bounded flat Čech
complex, retaining tensor comparison for every module. At a local
parameter point, trivialize the projective terms. An invertible
entry in a differential splits off a two-term identity complex:
clear its row and column, using \(d^2=0\). Repetition leaves a
complex with all differentials zero over the residue field.
If that fibre cohomology vanishes in all degrees, every remaining
term has zero residue fibre, hence is zero by Nakayama. The complex
is contractible near the point. This proves the first assertion.

A bounded acyclic complex of projectives is split exact: start at
its last term, split the surjection onto it and proceed downwards.
Every residue-field tensor is then acyclic, proving the second.
Finally take affine covers in both factors and filter the double
Čech computation either way. Affine acyclicity computes the direct
images at the first cohomology step; the next computes their
cohomology. The bounded filtrations give the spectral sequences.
We have proved the flat-sheaf facts needed here, without importing
a base-change assertion with its flatness hypotheses suppressed.
\(\square\)

**Theorem 6.32 (the exact translation-map kernel).**
There is an equality of subgroup schemes

\[
\ker\bigl(P_A\xrightarrow{\varphi}
       \underline{\operatorname{Hom}}(A,A^t)\bigr)=P_A^0.
\tag{DU.3}
\]

Thus on every \(T\), \(\varphi_L=0\) exactly when its normalized
class is a \(T\)-point of \(A^t\).

**Proof.** First work over an algebraically closed field, and choose
an ample normalized \(L\). If \(\varphi_M=0\), we show
\(M=t_a^*L\otimes L^{-1}\) for some \(a\in A(k)\). Put

\[
E=\Lambda_0(L)\otimes p_2^*M^{-1}\quad\hbox{on }A^2.
\]

Its fibre at a first-coordinate point \(a\) has class
\(t_a^*L\otimes L^{-1}\otimes M^{-1}\).
If no translate equals \(M\), each is nontrivial and homogeneous:
the difference from \(L\) belongs to \(A^t\), on which \(\varphi\)
is zero by result 6.19, and \(\varphi_M=0\).
6.30–6.31 give \(R^qp_{1*}E=0\) for every \(q\).
The first Leray computation makes \(H^n(A^2,E)=0\) for all \(n\).

For the other projection the fibre at \(b\) has class
\(t_b^*L\otimes L^{-1}\), with only a constant \(M^{-1}|_b\) factor.
Outside the finite \(K(L)\) this is nontrivial and homogeneous.
6.30–6.31 therefore support every coherent \(R^qp_{2*}E\)
on the finite set underlying \(K(L)\). Such a sheaf is killed
by a power of its finite-support ideal, by finite generation
on finitely many affine charts. It is a pushforward from a
finite Artinian scheme. Its positive cohomology is zero and
its global sections detect whether it is zero. The second
Leray sequence thus identifies
\(H^n(A^2,E)=H^0(A,R^np_{2*}E)\).
All left sides vanish, so all \(R^np_{2*}E=0\).
6.31 now makes every fibre acyclic. At \(b=0\) the fibre is
the trivial bundle up to a constant factor and has nonzero
\(H^0\), a contradiction. The claimed translate exists.
Every geometric kernel point therefore lies in \(P_A^0\).

By 6.27–6.28 the kernel is open and closed in \(P_A\), a union
of whole components, containing \(P_A^0\) as a scheme.
Over the algebraic closure every other nonempty component has
a rational point, which the preceding proof excludes from the
kernel. Thus the open subschemes are equal. Equality descends
faithfully flatly to \(k\). Equality of representing schemes
proves the assertion on every \(T\), including its nilpotents.
\(\square\)

#### Descent characters and the exact isogeny kernel

**Proposition 6.33 (equivariant descent and the character calculation).**
Let \(p:X\to Y\) be an fpqc torsor under a group scheme \(K/S\).
Quasi-coherent modules on \(Y\) are equivalent to quasi-coherent
modules on \(X\) with compatible \(K\)-linearization. The equivalence
preserves finitely presented and finite locally free modules.
In the locally Noetherian situation this gives the coherent version.
If \(K\) is finite locally free and commutative, and
\((X_T\to T)_*\mathcal O_{X_T}=\mathcal O_T\) universally, then
line bundles \(M\) on \(Y_T\) with \(p_T^*M\simeq\mathcal O_{X_T}\)
are canonically classified by characters \(K_T\to\mathbf G_{m,T}\),
compatibly with every change of \(T\).

**Proof.** The torsor identity \(K\times X=X\times_YX\)
converts a linearization into an isomorphism between the two
pullbacks to the equality relation. Its action identity is the
descent cocycle on the triple fibre product. The actual faithfully
flat module-descent theorem gives the equivalence and its inverse.
Finite presentation and finite local freeness descend.

Explicitly, a compatible linearization is
\(\lambda:p_2^*F\xrightarrow{\sim}\rho^*F\), with
\(\lambda_{gh}=\rho_h^*\lambda_g\circ\lambda_h\) on every test
scheme. The unit identity follows from this cocycle and invertibility.
For locally free \(F\), applying the symmetric-algebra construction
to the dual identifies it with a fibrewise linear lifting of the
action on \(X\) to the geometric bundle \(\mathbf V(F^\vee)\).
Pulling back its linear maps recovers \(\lambda\); the two
constructions are inverse and their action identities agree.

Choose \(\alpha:p_T^*M\simeq\mathcal O_{X_T}\).
Transport its canonical descent linearization across \(\alpha\).
It becomes multiplication by an invertible function on
\(K_T\times X_T\). Universal constants make it the pullback
of a unit on \(K_T\), namely a morphism
\(\chi:K_T\to\mathbf G_m\). The cocycle reads
\(\chi(h+h')=\chi(h)\chi(h')\).
Another \(\alpha\) differs by a unit from \(T\), which is
translation invariant, and leaves \(\chi\) unchanged.
Conversely use \(\chi\) as the linearization of the trivial
line and descend it. The constructions are inverse, with
tensor product corresponding to character multiplication.
They use the scheme equality relation and commute with
every base change. \(\square\)

The torsor hypothesis is essential. Source IV4.28 defines an
fppf quotient as a represented orbit sheaf, and IV4.31 obtains
the torsor relation under freeness. Thus VII7.2 needs this
freeness hypothesis: its assertion for arbitrary actions is false. For the trivial
\(\mathbf G_m\)-action on \(\operatorname{Spec}k\), its quotient
map is the identity, but equivariant lines have every integer
weight. Pullback from the quotient has only weight zero.
The torsor reading, used for isogenies, is the corrected
descent theorem. Over arbitrary non-Noetherian bases we use
quasi-coherent and finitely presented modules, rather than
assume every pullback preserves coherence.

**Theorem 6.34 (Cartier-dual kernel without a circular Picard input).**
For an isogeny \(f:A\to B\), with finite schematic kernel \(K\),
its dual \(f^t:B^t\to A^t\) is an isogeny and there is a canonical
isomorphism

\[
\delta_f:\ker f^t\xrightarrow{\;\sim\;}K^D,
\qquad \deg f^t=\deg f.
\tag{DU.4}
\]

It commutes with every field extension and holds on all test
schemes, not merely on geometric points.

**Proof.** The existing isogeny theorem identifies \(f\) with
the finite locally free \(K\)-torsor \(A\to A/K=B\).
Universal constant functions on \(A_T\) apply to every \(T\).
For a normalized class in the Picard pullback kernel,
\(f_T^*M\) is the trivial normalized bundle.
6.33 associates its descent character and identifies the
whole Picard pullback kernel with the character functor of \(K\).

We must show the converse character construction lands in
\(B^t\). Let \(M_\chi\) be the descended character line on
\(B_T\). Translation by \(a\in A(U)\) on the trivial line
of \(A_U\) commutes with its \(K_U\)-linearization: \(A\)
is commutative and \(\chi(h)\) is independent of the
\(A\)-coordinate. Descent gives
\(t_{f(a)}^*M_\chi\simeq M_\chi\).
The identity of \(A\) trivializes the identity fibre of the
descended line, providing its normalization.
Apply this translation comparison to the universal \(a\).
Its representing map \(\varphi_{M_\chi}:B_T\to B_T^t\)
becomes zero on the fpqc cover \(A_T\to B_T\), and is
therefore zero. 6.32, proved before the dual-kernel theorem
and biduality, puts \(M_\chi\) in \(B^t(T)\).
The full character functor is exactly \(\ker f^t(T)\).
Universal constants make the character independent of
trivialization; normalization removes base-line ambiguity.

Finite Cartier duality represents it by \(K^D\), whose
coordinate module is the vector-space dual of \(k[K]\).
Its rank equals that of \(K\), including local nonreduced
kernels. The dual homomorphism has finite kernel; its
source and target have equal dimension by the dual-variety
theorem. Properness and finite fibres make it finite,
and its full-dimensional closed image is the geometrically
integral target. The reduced-target homomorphism theorem
makes it faithfully flat. Its degree is its kernel rank,
giving (DU.4). All constructions commute with field
extension. \(\square\)

The character in (DU.4) is the scalar of the transported descent
linearization for \(a\mapsto a+h\). This fixes the sign of
the evaluation pairing \(e_f(h,M)=\delta_f(M)(h)\).
It is perfect because its second factor is the full Cartier
character scheme, including nilpotent parameters in both factors.

#### The bidual and symmetric translation maps

**Proposition 6.35 (pullback and symmetry).**
For \(f:A\to B\) and a line bundle \(M\) on \(B\),

\[
\varphi_{f^*M}=f^t\varphi_M f.
\tag{DU.5}
\]

If \(f\) is an isogeny and \(M\) has finite translation kernel,
then \(f^*M\) does too, and
\(\operatorname{rank}K(f^*M)=(\deg f)^2\operatorname{rank}K(M)\).
The normalized Poincaré bundle, viewed as a family on \(A^t\)
with parameter \(A\), defines a homomorphism
\(\kappa_A:A\to A^{tt}\). For every \(L\) on \(A\),

\[
\varphi_L=\varphi_L^t\kappa_A.
\tag{DU.6}
\]

**Proof.** Pull back translation:
\(t_a^*f^*M=f^*t_{f(a)}^*M\).
The normalized family identifies the representing maps on
all tests, proving (DU.5). A finite-kernel translation map
is an isogeny, since its source and target have equal
dimension. 6.34 and degree multiplication give the rank formula.

The switched Poincaré family is trivial at parameter \(0_A\).
Its connected parameter puts its map in \(P_{A^t}^0\).
It preserves the origin, so rigidity makes it a homomorphism.
Universality with normalization gives

\[
(\operatorname{id}_A\times\varphi_L)^*\mathcal P_A
       =\Lambda_0(L)\quad\hbox{on }A^2.
\]

The right side is invariant under switching coordinates:
addition is commutative and the inverse factors interchange.
Restrict at a \(T\)-valued point in either coordinate.
One restriction represents \(\varphi_L\); the other is
pullback of the switched Poincaré family and represents
\(\varphi_L^t\kappa_A\). This proves (DU.6), with compatible
axis normalizations and no scalar ambiguity. \(\square\)

**Theorem 6.36 (canonical biduality).**
The homomorphism \(\kappa_A:A\to A^{tt}\) is an isomorphism,
natural in \(A\):

\[
f^{tt}\kappa_A=\kappa_B f.
\tag{DU.7}
\]

For a finite-kernel line bundle \(L\), the schematic group
\(K(L)\) is isomorphic to its Cartier dual. With biduality
as the identification, every \(\varphi_L\) is symmetric.

**Proof.** Choose ample \(L\). Formula (DU.6) puts
\(\ker\kappa_A\) in the finite \(K(L)\).
Dimensions of \(A\) and \(A^{tt}\) agree. Properness,
finite fibres and full image dimension, followed by the
reduced-target homomorphism theorem, make \(\kappa_A\)
an isogeny. 6.34 gives
\(\deg\varphi_L^t=\deg\varphi_L\), so degree multiplication
in (DU.6) gives \(\deg\kappa_A=1\).
A finite locally free algebra of rank one is the base
ring: locally its unit has nonzero residue and generates
the rank-one module by Nakayama. The unit map is then
an isomorphism. This degree-one isogeny is an isomorphism.

The normalized bundle equality

\[
(f\times\operatorname{id}_{B^t})^*\mathcal P_B
 =(\operatorname{id}_A\times f^t)^*\mathcal P_A
       \quad\hbox{on }A\times B^t
\]

defines the pullback dual. Switch factors and represent
the resulting family on \(B^t\); this is (DU.7).
It proves naturality on all tests and under field extension.
There is also the triangle identity
\(\kappa_A^t\kappa_{A^t}=\operatorname{id}_{A^t}\).
Indeed the defining switched-family identity is
\((\operatorname{id}_{A^t}\times\kappa_A)^*\mathcal P_{A^t}
=s^*\mathcal P_A\). Combine it with the same identity for \(A^t\)
and the pullback-dual identity for \(\kappa_A\). On \(A\times A^t\)
these give
\((\operatorname{id}_A\times\kappa_A^t\kappa_{A^t})^*\mathcal P_A
=\mathcal P_A\), with both normalizations. Universality therefore
gives the triangle identity.
Finally \(\kappa_A\) restricts to
\(\ker\varphi_L\simeq\ker\varphi_L^t\), by (DU.6).
6.34 identifies the latter with \(K(L)^D\).
This proves the schematic self-duality. \(\square\)

**Corollary 6.37 (duality on Hom and torsion).**
Pullback gives an isomorphism of étale group schemes
\(\underline{\operatorname{Hom}}(A,B)\to
\underline{\operatorname{Hom}}(B^t,A^t)\), with inverse
\(g\mapsto\kappa_B^{-1}g^t\kappa_A\).
For every integer \(n\), \([n]_A^t=[n]_{A^t}\);
for \(n\ne0\),

\[
A[n]^D=A^t[n].
\tag{DU.8}
\]

**Proof.** Pullback of the universal bundle defines duality
for families of homomorphisms over every \(T\).
Multiplication of normalized bundles in \(B^t(T)\)
proves addition of those maps. Composition reverses,
and (DU.7) proves the inverse formula.
For the second inverse composite, use
\(g^{tt}\kappa_{B^t}=\kappa_{A^t}g\) and the triangle identities;
the dual of \(\kappa_B^{-1}g^t\kappa_A\) becomes
\(\kappa_A^t g^{tt}(\kappa_B^t)^{-1}
=\kappa_A^t\kappa_{A^t}g=g\).
Addition, the zero map and inversion give the integer
identity. Apply 6.34 to \([n]_A\), whose finite locally
free kernel is \(A[n]\) and whose dual is \([n]_{A^t}\).
This includes noninvertible \(n\). For \(n=0\) the dual
map identity holds but its kernel is nonfinite unless
\(A=0\). \(\square\)

#### Néron–Severi and the arithmetic distinction

**Theorem 6.38 (torsion and the integer criterion).**
For a line bundle \(L\) on \(A\), or a normalized family
over any \(T/k\), the following assertions hold.

1. If \(L^n\) belongs to \(A^t(T)\) for a nonzero integer
   \(n\), then so does \(L\). Thus torsion bundles are
   algebraically trivial.
2. \(L\otimes([-1]^*L)^{-1}\) belongs to \(A^t(T)\).
3. \(L\) belongs to \(A^t(T)\) exactly when
   \([n]^*L=L^n\) as relative Picard classes for every
   integer \(n\), or for one \(n\notin\{0,1\}\).

**Proof.** Additivity gives
\(\varphi_{L^n}=n\varphi_L=\varphi_L[n]_A\).
Every nonzero integer multiplication, after base change,
is faithfully flat and surjective, even if its differential
is zero. A zero composite makes \(\varphi_L=0\);
6.32 proves (1).

Formula (DU.5) with \(f=[-1]\), and 6.37, give
\(\varphi_{[-1]^*L}=(-1)\varphi_L(-1)=\varphi_L\).
The difference in (2) has zero translation map.
This is the correct sign computation: there are two
minus signs. 6.32 proves (2).

6.29 proves the forward implication in (3).
The assumed equality for \(n\notin\{0,1\}\) gives
\(n^2\varphi_L=n\varphi_L\), by formula (DU.5) and 6.37.
Thus \(\varphi_L[n(n-1)]_A=0\).
The integer \(n(n-1)\) is nonzero; cancel its fpqc
multiplication cover and apply 6.32.
This includes negative integers and the characteristic
prime, and does not replace an isogeny by its tangent
map. \(\square\)

**Theorem 6.39 (the component group and its embedding).**
The component group \(N_A=P_A/P_A^0\) is étale and fits
into an exact sequence of fppf sheaves

\[
0\longrightarrow A^t\longrightarrow P_A
 \longrightarrow N_A\longrightarrow0.
\tag{DU.9}
\]

Multiplication by every nonzero integer on \(N_A\) has
trivial schematic kernel. Integer pullback on \(N_A\)
is multiplication by \(n^2\). There is a monomorphism
of étale group schemes

\[
N_A\hookrightarrow
\underline{\operatorname{Hom}}_{\rm sym}(A,A^t),
\quad [L]\longmapsto\varphi_L.
\tag{DU.10}
\]

Two bundles have the same translation map exactly when
they are algebraically equivalent.

**Proof.** The actual component theorem applies to the
locally finite-type Picard group, giving (DU.9), with
surjectivity as sheaves. 6.32 identifies the translation
map kernel with the same identity component, so its
quotient embeds in the Hom scheme. 6.35's symmetry
formula and biduality make these maps symmetric.
Symmetric homomorphisms are the closed equalizer of
\(h\) and \(h^t\kappa_A\) in the étale Hom scheme.
This gives (DU.10) on every test scheme.

A torsion section of \(N_A(T)\) locally lifts to a
Picard section. 6.38(1) puts its lift in \(P_A^0\);
its component is therefore zero already on \(T\).
Formula (DU.5) gives
\(\varphi_{[n]^*L}=n^2\varphi_L\).
Injectivity in (DU.10) gives the quadratic action.
6.32 equates equality of the maps with equality modulo
\(P_A^0\). The connected Poincaré family equates that
with algebraic equivalence over an algebraically closed
field. Testing there descends because \(P_A^0\)
commutes with field extension. \(\square\)

For a separable closure \(k_s\), the étale \(N_A\) is
determined by its discrete geometric component group
and continuous Galois action; hence
\(N_A(k)=N_A(k_s)^{\operatorname{Gal}(k_s/k)}\).
Purely inseparable extension does not change components
of an étale scheme, so \(N_A(k_s)\) is the geometric
Néron–Severi group. Every component of \(P_{A,k_s}\)
has a \(k_s\)-point: it is smooth, and an étale chart
of a nonempty smooth scheme has a nonempty finite
separable fibre over a suitable \(k_s\)-point.
Rigidification at \(0_A\) represents that point by
an actual bundle.

Over \(k\), origin rigidification gives
\(\operatorname{Pic}(A)=P_A(k)\), but \(P_A(k)\to N_A(k)\)
need not be onto. A rational component is an \(A^t\)-torsor;
its class has an actual bundle representative exactly
when that torsor has a \(k\)-point. The quotient of
actual \(k\)-bundles by algebraic equivalence therefore
embeds in \(N_A(k)\), without necessarily equalling all
Galois-invariant geometric classes.

These are the Chapter VII7.24–7.26 component, torsion,
quadratic-action and injectivity assertions. The general
theorem of the base and uniform proper-family bounds
are separate AG-HP inputs, explicitly imported there.
No finite-generation proof or uniform bound follows
merely from (DU.10). The later surjectivity onto
symmetric homomorphisms, source XI11.3, is distinct.

#### The other mapped Chapter VII consequences

**Proposition 6.40 (Hodge cohomology and integer weights).**
For \(g=\dim A\), cup product gives natural identifications

\[
H^q(A,\Omega^p_{A/k})
 =\bigwedge\nolimits^q\operatorname{Lie}(A^t)
   \otimes\bigwedge\nolimits^p\operatorname{Lie}(A)^\vee.
\tag{DU.11}
\]

The Hodge number is \(\binom gp\binom gq\), and \([n]^*\)
acts as multiplication by \(n^{p+q}\).

**Proof.** Translation trivializes differentials:
\(\Omega^1=\operatorname{Lie}(A)^\vee\otimes\mathcal O_A\);
take exterior powers. The proved coherent cup theorem
identifies \(H^q(\mathcal O_A)\) with
\(\bigwedge^qH^1(\mathcal O_A)\), and the square-zero
Picard calculation identifies the degree-one space
with \(\operatorname{Lie}(A^t)\).
The differential of \([n]\) on \(A\) is \(n\), giving
\(n^p\) on invariant \(p\)-forms. Pullback on
\(H^1(\mathcal O_A)\) is the derivative of the
pullback dual \([n]_{A^t}\), namely \(n\).
Exterior powers give \(n^q\). Multiply the factors.
The cup maps and field extensions preserve every
identification. \(\square\)

**Theorem 6.41 (Hodge–de Rham degeneration over every field).**
The spectral sequence
\(E_1^{p,q}=H^q(A,\Omega^p_{A/k})\Rightarrow
H_{\rm dR}^{p+q}(A/k)\) degenerates at \(E_1\).
There is a natural exact sequence

\[
0\longrightarrow\operatorname{Lie}(A)^\vee
\longrightarrow H_{\rm dR}^1(A/k)
\longrightarrow\operatorname{Lie}(A^t)\longrightarrow0.
\tag{DU.12}
\]

**Proof.** Filter the total Čech–de Rham complex by
form degree. Its finite covers and bounded form complex
give a convergent spectral sequence with finite filtration.
Cross product is multiplicative with total-degree
Koszul signs; addition supplies the coproduct.
6.40 and the coherent cup theorem identify the total
\(E_1\)-algebra and coproduct with the exterior algebra on

\[
\begin{gathered}
V=H^1(A,\mathcal O_A)\oplus H^0(A,\Omega^1_{A/k}),\\
\dim V=2g,
\end{gathered}
\]

whose degree-one generators are primitive.
For the first summand this is the coherent counit
calculation. For invariant forms it follows by pulling
back along addition and its additive differential.
The product Künneth isomorphism at \(E_1\) is the
double Čech computation over the field and the
direct-sum decomposition of forms on \(A^2\).

Assume all earlier differentials vanish. The \(r\)-page
is still this exterior algebra, and the product's
\(r\)-page its tensor square. Functoriality makes
\(d_r\) a coderivation:
\(\Delta d_r=(d_r\otimes1+1\otimes d_r)\Delta\),
with the total-degree sign in the second tensor term.
It is also a cup-product derivation. It therefore
sends a primitive degree-one element to a primitive
element of total degree two.

No nonzero such primitive exists, including in
characteristic two. In a basis \(v_i\), the reduced
coproduct of \(\sum_{i<j}c_{ij}v_iv_j\) is
\(\sum_{i<j}c_{ij}(v_i\otimes v_j-v_j\otimes v_i)\).
The tensor basis detects every coefficient separately,
even when minus equals plus. Thus \(d_r\) vanishes
on \(V\); the derivation rule makes it zero everywhere.
Induction proves degeneration. This replaces the
source's overly broad bialgebra-classification wording
by the actual exterior algebra and corrects its
differential formula: it is a coderivation, not
\(d_r\otimes d_r\).
The degree-one filtration gives (DU.12); no canonical
splitting is asserted. \(\square\)

**Proposition 6.42 (Frobenius and Verschiebung are dual).**
In characteristic \(p\), under the canonical identification
\((A^t)^{(p)}=(A^{(p)})^t\),

\[
F_{A/k}^t=V_{A^t/k},
\qquad V_{A/k}^t=F_{A^t/k}.
\tag{DU.13}
\]

**Proof.** Picard representability and arbitrary base
change give the displayed identification, including
when Frobenius on \(k\) is not an isomorphism.
Let \((M,\alpha)\) be a normalized bundle representing
an element of \(A^t(T)\).
Relative Frobenius of the Picard scheme sends it to
its Frobenius-twisted bundle on \(A_T^{(p/T)}\);
this is Cartesian base change along absolute
Frobenius of the parameter. Pulling it back by
\(F_{A_T/T}\) is absolute Frobenius pullback on
\(A_T\). Transition functions become their \(p\)-th
powers, giving \(M^p\) with normalization \(\alpha^p\).
This calculation holds on every \(T\), including
nilpotents. Consequently

\[
F_{A/k}^tF_{A^t/k}=[p]_{A^t}.
\]

The proved defining Verschiebung identity reads
\(V_{A^t/k}F_{A^t/k}=[p]_{A^t}\).
Cancel the fpqc isogeny \(F_{A^t/k}\) to get the
first equality. Dualize and apply natural biduality
with its base-change compatibility to get the second.
No inverse field Frobenius identifying \(A^{(p)}\)
with \(A\) was used. \(\square\)

#### Source credit and scope

The proofs discharge mapped Chapter VII7.1–7.2 with
the torsor/coherence scope correction; 7.4–7.6;
7.8–7.12; 7.14–7.17; 7.19; 7.21–7.23; 7.25–7.30;
and 7.34. Adjacent 7.3, 7.7, 7.13, 7.18, 7.20,
7.24 and 7.32–7.33 supply their actual prerequisites
and definitions. General proper-scheme Néron–Severi
finiteness and uniform family bounds remain separately
owned AG-HP inputs; Chapter XI's surjectivity onto
symmetric homomorphisms is not inferred from an
injection. The non-abelian surface example VII7.31
and other unmapped chapters are not added to this
bounded proof assignment.

Comparison source: Bas Edixhoven, Gerard van der Geer
and Ben Moonen, *Abelian Varieties*, preliminary version,
Chapter VII with 8 February 2012 footers, printed
pages 98–111,
[author-hosted PDF](https://van-der-geer.nl/AV.pdf).
6.32 expands the cohomological argument attributed to
Mumford in that chapter; 6.31 gives its exact
flat-sheaf and tensor hypotheses. 6.41 supplies the
exterior-algebra version of the degeneration argument
attributed there to Oda. These mathematical credits
do not import their books or papers as unwritten
proof providers.

## 7. Torsion points and Tate modules

Fix a separable closure \(k_s\) and its absolute Galois group \(\Gamma\).

**Theorem 7.1. Torsion of invertible order.** If \(n\geq1\) is invertible in \(k\), then

\[
A[n](k_s)\simeq(\mathbf Z/n)^{2g}
\tag{18}
\]

as abstract abelian groups. The isomorphism is generally not canonical and does not assert that the Galois action is trivial.

**Proof.** The finite group scheme \(A[n]\) is étale of rank \(n^{2g}\). Over the separably closed field, a finite étale algebra is a product of copies of \(k_s\). Thus its group of points has exactly \(n^{2g}\) elements.

First take \(n=\ell^r\), with \(\ell\) a prime invertible in \(k\), and \(r\geq1\). Put \(H=A[\ell^r](k_s)\). It is a finite abelian group killed by \(\ell^r\), so its elementary-divisor decomposition is

\[
H\simeq\bigoplus_{i=1}^a\mathbf Z/\ell^{b_i},
\qquad 1\leq b_i\leq r.
\]

Its subgroup killed by \(\ell\) is exactly \(A[\ell](k_s)\), of size \(\ell^{2g}\). Every summand contributes \(\ell\), so \(a=2g\). The size of \(H\) is \(\ell^{2gr}\); hence \(\sum_i b_i=2gr\). There are \(2g\) terms, each at most \(r\), so every \(b_i=r\).

For general \(n=\prod_\ell\ell^{r_\ell}\), the elementary Chinese-remainder idempotents in \(\mathbf Z/n\) decompose the killed-by-\(n\) group into its \(\ell\)-primary subgroups. Those are \(A[\ell^{r_\ell}](k_s)\): the idempotents project onto them and their sum is one. The prime-power result and the Chinese remainder theorem prove (18). \(\square\)

In particular the cardinality alone at one composite \(n\) would not have determined the group; the degree calculation for its prime divisors is the additional input.

For a prime \(\ell\) invertible in \(k\), define

\[
T_\ell(A)=\varprojlim_r A[\ell^r](k_s),
\tag{19}
\]

with transition maps multiplication by \(\ell\). It is a \(\mathbf Z_\ell\)-module.

**Theorem 7.2. The Tate module.** There is an isomorphism

\[
T_\ell(A)\simeq\mathbf Z_\ell^{\,2g}.
\tag{20}
\]

The action of \(\Gamma\) is continuous for the inverse-limit topology and defines, after choosing a basis, a continuous homomorphism

\[
\rho_{A,\ell}:\Gamma\longrightarrow
\mathrm{GL}_{2g}(\mathbf Z_\ell).
\tag{21}
\]

**Proof.** The transition map \(P_{r+1}\to P_r\), where \(P_r=A[\ell^r](k_s)\), is surjective. Given a point in \(P_r\), its fibre under \([\ell]\) is a nonempty finite étale scheme over \(k_s\), and therefore has a \(k_s\)-point. Any such lift is killed by \(\ell^{r+1}\).

Choose a basis \(v_{1,1},\ldots,v_{2g,1}\) of \(P_1\). Recursively lift each \(v_{i,r}\) to \(v_{i,r+1}\) with \(\ell v_{i,r+1}=v_{i,r}\). These lifts form a basis at every level. To prove it, Theorem 7.1 identifies \(P_{r+1}\) as a free \(\mathbf Z/\ell^{r+1}\)-module of rank \(2g\). Multiplication by \(\ell^r\) induces an isomorphism

\[
P_{r+1}/\ell P_{r+1}\xrightarrow{\sim}P_1.
\]

The chosen lifts map to the original basis in \(P_1\). Nakayama over the local ring \(\mathbf Z/\ell^{r+1}\) makes them generators; their number and the equal finite cardinalities make the resulting map from the free module an isomorphism.

In these compatible bases the transition maps send a coordinate modulo \(\ell^{r+1}\) to its reduction modulo \(\ell^r\), because \(\ell v_{i,r+1}=v_{i,r}\). Taking inverse limits proves (20).

The Galois action on each \(P_r\) factors through a finite quotient: the finite étale scheme splits over a finite separable extension. It commutes with multiplication by \(\ell\), so acts on the inverse limit. Stabilizers of each finite-level tuple are open, exactly the continuity condition for (21) with its \(\ell\)-adic topology. \(\square\)

## 8. What changes in characteristic \(p\)

Suppose \(\operatorname{char}k=p>0\). The group scheme \(A[p]\) still has rank \(p^{2g}\), but its geometric points can be far fewer.

**Theorem 8.1. The point bound.** The geometric kernel of \([p]\) has at most \(p^g\) points.

**Proof.** Extend to an algebraically closed field; neither geometric points nor \(g\) change. The case \(g=0\) is immediate. Let \(K\) be the function field of the target \(A\), and \(L\) that of the source of \([p]\). Theorem 6.1 gives \([L:K]=p^{2g}\), where \(K\) is embedded by \([p]^*\).

By (17) and translations, the differential of \([p]\) vanishes everywhere. Thus its function-field image lies in \(L^p\): over the perfect ground field a function has zero differential exactly when it is a \(p\)-th power [Stacks, Tag 031W].

The smooth \(g\)-dimensional function field \(K\) has a \(p\)-basis \(t_1,\ldots,t_g\): the \(p^g\) monomials \(\prod t_i^{e_i}\), \(0\leq e_i<p\), form a basis over \(K^p\). This follows from the correspondence between \(p\)-bases and bases of \(\Omega_{K/k}\) [Stacks, Tags 07P1–07P2]. Adjoining their \(p\)-th roots gives a purely inseparable extension \(K^{1/p}/K\) of degree \(p^g\). Since each \([p]^*t_i\) has a \(p\)-th root in \(L\), it embeds as an intermediate field

\[
K\subset E\simeq K^{1/p}\subset L,\qquad
[E:K]=[L:E]=p^g.
\tag{22}
\]

We make the point count on an actual open fibre, rather than only on the function fields. On a nonempty affine open \(U=\operatorname{Spec}R\) in the target, shrink so that the \(t_i\) are regular and their chosen roots are regular on \([p]^{-1}(U)=\operatorname{Spec}B\). This is possible because \([p]\) is finite: the closed locus where any of the finitely many source rational functions is not regular has proper closed image, missing the generic point.

There is then a factorization

\[
\operatorname{Spec}B\longrightarrow
\operatorname{Spec}C\longrightarrow\operatorname{Spec}R,
\quad
C=R[u_1,\ldots,u_g]/(u_i^p-t_i).
\tag{23}
\]

The ring \(C\) is free over \(R\) on the \(p^g\) bounded monomials. Its map to \(B\) is injective: it is injective after passage to \(K\) by (22), and \(C\) is \(R\)-free. Thus \(C\) is a domain with fraction field \(E\). The extension \(B/C\) is finite, since a finite list of \(R\)-module generators of \(B\) also generates it over \(C\).

After one more shrinking of \(U\), \(B\) is free of rank \(p^g\) over \(C\). Here is a concrete justification. Choose an \(E\)-basis from \(B\); clearing the finitely many denominators expressing module generators gives a nonzero \(c\in C\) for which \(B_c\) is free of that rank. The determinant \(N_{C/R}(c)\) is nonzero, since multiplication by \(c\) is invertible over the fraction field. On \(D(N_{C/R}(c))\subset U\), the adjugate formula makes \(c\) a unit in \(C\), so this target shrinking suffices.

For every algebraically closed residue field, the second map in (23) has exactly one point in its fibre: each equation \(u_i^p=t_i\) has a unique root. The first map has at most \(p^g\) points over that point, because its fibre algebra has vector-space dimension \(p^g\). Therefore \([p]\) has at most \(p^g\) points over a closed point of this nonempty \(U\).

All closed-point fibres of \([p]\) have the same number of points. It is surjective, and a preimage of a point translates the kernel isomorphically to that fibre. The count over \(U\) consequently gives the same bound for the kernel. \(\square\)

*Comparison locator:* [Stacks, Tag 0C0Y].

The **\(p\)-rank** \(f\) of \(A\) is defined by

\[
A[p](\overline k)\simeq(\mathbf Z/p)^f.
\]

Such an \(f\) exists because the group is finite and killed by \(p\); Theorem 8.1 gives \(0\leq f\leq g\). More generally

\[
A[p^r](\overline k)\simeq(\mathbf Z/p^r)^f.
\tag{24}
\]

To prove it, multiplication by \(p\) surjects from \(A[p^{r+1}](\overline k)\) onto \(A[p^r](\overline k)\), using divisibility of \(A(\overline k)\). Its kernel is \(A[p](\overline k)\), so induction gives cardinality \(p^{fr}\). An elementary-divisor decomposition at level \(r\) has \(f\) summands, as seen by taking its killed-by-\(p\) subgroup. Each exponent is at most \(r\), and their sum is \(fr\); all are therefore \(r\). This proves (24). It describes geometric points and does not identify the nonreduced finite group scheme.

### Frobenius retains the infinitesimal kernel

Let \(\operatorname{char}k=p>0\). Write

\[
A^{(p)}=A\times_{\operatorname{Spec}k,F_k}\operatorname{Spec}k.
\]

The relative Frobenius \(F_{A/k}:A\to A^{(p)}\) has the ring formula
\(b\otimes c\mapsto c b^p\), as in *Lie algebras and smoothness*, Section 6. The twist remains part of the notation over imperfect fields.

**Theorem 8.2.** Relative Frobenius is a radicial isogeny of degree \(p^g\), where \(g=\dim A\). Its kernel is a connected finite group scheme whose underlying scheme has coordinate algebra

\[
k[A[F]]\simeq
k[t_1,\ldots,t_g]/(t_1^p,\ldots,t_g^p).
\tag{F.1}
\]

The isomorphism in (F.1) describes the scheme and a choice of parameters; it does not assert that its Hopf algebra is the product Hopf algebra of \(\alpha_p^g\).

**Proof.** Over an algebraically closed extension, raising coordinates to their \(p\)-th powers is injective on points, and the identity maps to the identity of the twist. Thus the geometric identity fibre has no other point. Its underlying space over \(k\) is consequently just the rational identity and lies in any affine neighbourhood of that point. Choose such a neighbourhood \(U=\operatorname{Spec}R\), generated by functions \(x_1,\ldots,x_s\) vanishing there. Its augmentation ideal \(\mathfrak m\) is generated by those functions. The entire identity fibre of relative Frobenius is therefore

\[
\operatorname{Spec}R/(x_1^p,\ldots,x_s^p).
\tag{F.2}
\]

Its augmentation ideal is nilpotent, and the bounded monomials in the \(x_i\)'s span a finite-dimensional algebra. Thus the kernel is finite and connected, with sole point the identity. The twist is an abelian variety of the same dimension; criterion 3 of Theorem 6.4 makes \(F_{A/k}\) an isogeny, and Theorem 6.8 makes it radicial.

Choose \(x_1,\ldots,x_g\) whose classes are a basis of \(\mathfrak m/\mathfrak m^2\). Smoothness makes \(R_{\mathfrak m}\) regular of dimension \(g\). Its completion, with its already given coefficient field \(k\), is \(k[[t_1,\ldots,t_g]]\), with \(t_i\mapsto x_i\). The complete proof of this regular equal-characteristic specialization is [Coefficient rings and the Cohen structure theorem](../../AG-CA/src/coefficient-rings-and-cohen-structure.md), Corollary 6.2; [Completion](../../AG-CA/src/completion.md), Theorems 3.3 and 4.1, preserve the dimension, regularity and Artinian quotients. The prescribed coefficient field \(k\) works in that proof because it already splits the residue map.

In this power-series ring every remaining \(x_j\) has zero constant term. Its \(p\)-th power belongs to \((t_1^p,\ldots,t_g^p)\), since raising a series to its \(p\)-th power multiplies every exponent by \(p\). Hence (F.2), whose Artinian ring agrees with its local completion, becomes the algebra in (F.1). The monomials \(t_1^{a_1}\cdots t_g^{a_g}\), \(0\le a_i<p\), form a basis. Its dimension is \(p^g\), proving the degree by (I.2). \(\square\)

### Constructing Verschiebung over arbitrary fields

We give a smooth-field construction. It avoids imposing perfectness on the answer and proves the auxiliary differential assertion used in the construction.

**Lemma 8.3 (zero differential factors through Frobenius).** Suppose \(X\) is an abelian variety over \(k\) in characteristic \(p\), and \(u:X\to Y\) is a morphism whose map on differentials \(u^*\Omega_{Y/k}\to\Omega_{X/k}\) is zero. There is a unique \(v:X^{(p)}\to Y\) such that \(u=vF_{X/k}\).

**Proof.** First extend to an algebraically closed field \(L\). The smooth standard chart at the generic point gives an étale map from a nonempty open of \(X_L\) to affine \(g\)-space: regard the free coordinates as the base variables, leaving a square invertible Jacobian in the remaining variables. Its nonempty open image is dense, and its generic fibre is finite étale. Thus its free coordinates give a separating transcendence basis \(t_1,\ldots,t_g\) of the function field \(M/L\), and \(M\) is finite separable over \(E=L(t_1,\ldots,t_g)\). To see the differential calculation explicitly, \(E/E^p\) is purely inseparable of degree \(p^g\), with basis the bounded monomials in the \(t_i\)'s. The extension \(M^p/E^p\) is separable of degree \([M:E]\). A purely inseparable and a separable field extension are linearly disjoint: at each purely inseparable simple step, a new root of \(T^{p^r}-a\) cannot appear in a separable extension unless it was already in the base. Hence

\[
\begin{gathered}
[EM^p:E]=[M:E],\quad EM^p=M,\\
[M:M^p]=p^g.
\end{gathered}
\]

Those same monomials form an \(M^p\)-basis of \(M\). The derivations \(\partial/\partial t_i\) on \(E\) extend uniquely to \(M\): differentiating the separable minimal polynomial of an algebraic generator solves for its derivative because its polynomial derivative is nonzero. Expanding an element in the bounded-monomial basis now shows

\[
\ker(d:M\to\Omega_{M/L})=M^p.
\tag{F.3}
\]

Indeed the extended derivations kill \(M^p\), and differentiation of that basis forces every coefficient of a monomial with any positive exponent to be zero.

For an affine open \(V\subset Y_L\), all pullbacks of its functions to \(u^{-1}V\) have zero differential, and so lie in \(M^p\). Their unique \(p\)-th roots are regular on \(u^{-1}V\): a root is integral over each local ring there, and those rings are integrally closed because \(X_L\) is smooth. The exact normality provider is *Smooth morphisms*, Theorem 2.1. Thus every pulled-back function belongs to the image of the relative-Frobenius map on these open structure sheaves. Over the perfect \(L\), that image is precisely the \(p\)-th powers, with the scalar action accommodated by the twist. Additivity and multiplicativity, and injectivity of Frobenius on reduced local rings, make the inverse images a ring map to the corresponding open in \(X_L^{(p)}\). Relative Frobenius is a universal homeomorphism, so these opens cover and the resulting morphisms glue. This constructs \(v_L\).

8.2 supplies finite faithful flatness of \(F_{X/k}\). Thus two proposed factors are equal as soon as their compositions with \(F_{X/k}\) are equal; the same cancellation works after every scalar extension. The two pullbacks of \(v_L\) to \(L\otimes_k L\) both compose with the base-changed Frobenius to \(u\), so they agree, including any nilpotents in that tensor product. Descent of morphisms along the faithfully flat field extension gives \(v\) over \(k\) and proves uniqueness. \(\square\)

**Theorem 8.4 (Verschiebung).** For every abelian variety \(A/k\) in characteristic \(p\), there is a unique isogeny

\[
V_{A/k}:A^{(p)}\longrightarrow A
\]

such that

\[
V_{A/k}F_{A/k}=[p]_A,
\qquad F_{A/k}V_{A/k}=[p]_{A^{(p)}}.
\tag{F.4}
\]

It has degree \(p^g\). For a homomorphism \(a:A\to B\),

\[
aV_{A/k}=V_{B/k}a^{(p)}.
\tag{F.5}
\]

The constructions commute with arbitrary field extension.

**Proof.** The differential of \([p]\) is zero at the identity, by (17) of the current lesson, and therefore everywhere by translation. Lemma 8.3 applied to \([p]\) gives the unique \(V\) with the first identity. It is a homomorphism: compose its proposed addition identity with the fppf cover \(F\times F\), where it becomes the homomorphism identity for \([p]\). Surjectivity of \([p]=VF\) makes \(V\) surjective. Since the two dimensions agree, Theorem 6.4 makes it an isogeny. Degrees multiply, so

\[
\deg V=\frac{\deg[p]}{\deg F}=p^g.
\]

The equality \(FVF=F[p]=[p]F\) and faithful flatness of \(F\) give the second identity. For (F.5), compose both sides with \(F_{A/k}\) and use functoriality of relative Frobenius; both composites are \(a[p]_A\). Cancel \(F_{A/k}\). Arbitrary base change preserves relative Frobenius and the displayed identities; the same uniqueness proves base-change compatibility. \(\square\)

For \(r\ge1\), set

\[
\begin{gathered}
F_A^{[r]}=F_{A^{(p^{r-1})}/k}\cdots F_{A/k},\\
F_A^{[r]}:A\to A^{(p^r)},\\
V_A^{[r]}=V_{A/k}\cdots V_{A^{(p^{r-1})}/k},\\
V_A^{[r]}:A^{(p^r)}\to A.
\end{gathered}
\]

The brackets distinguish these composites from powers of an endomorphism of an unchanged variety. Induction using (F.4) gives

\[
V_A^{[r]}F_A^{[r]}=[p^r]_A,
\qquad F_A^{[r]}V_A^{[r]}=[p^r]_{A^{(p^r)}},
\qquad \deg F_A^{[r]}=\deg V_A^{[r]}=p^{rg}.
\tag{F.6}
\]

For example, the first identity at \(r+1\) is
\(V_A V_{A^{(p)}}^{[r]}F_{A^{(p)}}^{[r]}F_A
=V_A[p^r]_{A^{(p)}}F_A=[p^{r+1}]_A\);
the second follows by the corresponding reversed calculation.

**Consequence 8.5 (the geometric point bound).** The factorization \([p]=VF\) gives another proof that \(\#A[p](\overline k)\le p^g\). Frobenius is bijective on geometric points, so it identifies \(A[p](\overline k)\) with \(\ker V(\overline k)\). The latter is a finite scheme of rank \(p^g\), hence has at most \(p^g\) points. This complements, and does not replace, the function-field proof of Theorem 8.1 already present in the lesson.

**Example 8.6 (a separable closure need not contain the geometric \(p\)-torsion).** Over \(k=\mathbf F_2(t)\), take

\[
E:\quad y^2+xy=x^3+t,
\qquad O=(0:1:0).
\]

The affine derivatives are \(y+x^2\) and \(x\), whose simultaneous zero \((0,0)\) is off the curve. At its unique point at infinity the homogeneous \(Z\)-derivative is one. Thus the projective cubic is smooth. Its tangent line at \(O\) is \(Z=0\), which cuts the cubic with multiplicity three, so \(O\) is a rational flex and Theorem 9.0 supplies the abelian group law. The vertical-line involution is \((x,y)\mapsto(x,y+x)\), hence is inversion. Its nonidentity fixed point has

\[
x=0,\qquad y^2=t.
\]

There is exactly one such geometric point, \((0,\sqrt t)\), and it is not defined over \(k_s\): \(\sqrt t\) has a purely inseparable degree-two minimal polynomial over \(k\), so cannot belong to a separable algebraic extension. Therefore \(E[2](k_s)=\{O\}\), while \(E[2](\overline k)\simeq\mathbf Z/2\). The connected-étale sequence of \(E[2]\) need not split over \(k_s\); the nonidentity section of its split étale quotient has no lift there. This is why formula (24) uses an algebraic closure.

### Torsion points and thick torsion schemes

**Theorem 8.7 (density at every prime).** Let \(\ell\) be any prime. The collection of subschemes

\[
A[\ell^r]\hookrightarrow A,\qquad r\ge0,
\]

is scheme-theoretically dense: no proper closed subscheme of \(A\) contains all of them. If \(\ell\ne\operatorname{char}k\), their geometric points are Zariski dense in \(A_{\overline k}\), and their underlying spaces are dense in \(A\). If \(\ell=\operatorname{char}k\), those topological assertions need not hold.

**Proof for \(\ell\ne\operatorname{char}k\).** Extend to an algebraic closure and put \(T=\bigcup_r A[\ell^r](\overline k)\). It is a subgroup. Let \(D\) be its reduced Zariski closure. It is a subgroup scheme, as follows without replacing scheme identities by unsupported point identities. Translation by an element of \(T\) preserves \(T\), and hence \(D\). For any \(y\in D(\overline k)\), the closed set \(\{x:x+y\in D\}\) contains \(T\), and hence contains \(D\). Therefore addition sends all rational points of \(D\times D\) into \(D\). The product is reduced over the algebraically closed field, and rational points are dense, so every equation of \(D\) pulls back to zero. Addition thus factors scheme-theoretically through \(D\). Inversion is handled in the same way, and the identity lies in \(D\).

The identity component \(D^0\) is a proper connected reduced group scheme over a perfect field. Theorem 2.3 and Proposition 4.1 of *Group schemes over a field*, and the reduced-group smoothness theorem of the Lie lesson, make it an abelian subvariety. Put \(h=\dim D^0\), and let \(N\) be the finite number of components of \(D\). A component containing an \(\ell^r\)-torsion point is translated by that point into \(D^0\), and this identifies its \(\ell^r\)-torsion points with \(D^0[\ell^r](\overline k)\). Theorems 6.1 and 7.1, applied to \(A\) and \(D^0\), give

\[
\ell^{2rg}=\#A[\ell^r](\overline k)
\le N\ell^{2rh}.
\]

Letting \(r\) grow forces \(h=g\). Thus \(D^0=A\), since a proper closed subset of the integral \(A\) has smaller dimension. This proves geometric topological density. Its image under the surjective field-extension projection is dense downstairs. If a closed subscheme \(Z\subset A\) contains every \(A[\ell^r]\), then \(Z_{\overline k}\) contains that dense set. Its ideal is zero on the reduced \(A_{\overline k}\), so \(Z_{\overline k}=A_{\overline k}\); faithful flatness gives \(Z=A\).

**Proof for \(\ell=p=\operatorname{char}k\).** By (F.6), \(A[F_A^{[r]}]\subset A[p^r]\). In the affine identity chart of 8.2 the Frobenius kernel is defined by

\[
(x_1^{p^r},\ldots,x_s^{p^r})\subset R.
\]

Suppose a closed subscheme \(Z\) contains all of these kernels, and let \(J\subset R\) define \(Z\cap U\). Localizing at the identity gives

\[
J R_{\mathfrak m}\subset
(x_1^{p^r},\ldots,x_s^{p^r})R_{\mathfrak m}
\subset\mathfrak m^{p^r}R_{\mathfrak m}
\quad\text{for every }r.
\tag{D.1}
\]

The completion map is injective by [Completion](../../AG-CA/src/completion.md), Theorem 3.2. In its power-series description from 8.2, a nonzero series has a least total degree and therefore cannot belong to all powers of the maximal ideal. Hence the intersection on the right of (D.1) is zero. Thus \(JR_{\mathfrak m}=0\). The affine ring \(R\) is a domain, so its localization at \(\mathfrak m\) is injective and \(J=0\). Therefore the ideal sheaf of \(Z\) is zero on a nonempty open subset of the integral \(A\). Any local section of that ideal is then zero: it vanishes at the generic point and a local ring of an integral scheme injects into its function field. Thus \(Z=A\), proving scheme-theoretic density.

If the \(p\)-rank is zero, formula (24) gives just the identity as a geometric point of each \(A[p^r]\). On a positive-dimensional variety this singleton is not topologically dense. It is the increasing infinitesimal thickness that supplies the scheme-theoretic conclusion. \(\square\)

The distinction is also visible in the sheaf map
\(\mathcal O_A\to\prod_r i_{r*}\mathcal O_{A[p^r]}\).
For \(p\)-rank zero it is zero on any open disjoint from the identity, and is not injective there. This does not contradict the global closed-subscheme assertion of 8.7: such a global ideal cannot agree with these arbitrarily deep identity jets on an integral variety.

### A source correction that the torsion calculation detects

The point-count statements do not classify the finite torsion group scheme. For a concrete check, use the supersingular characteristic-two cubic \(E:y^2+y=x^3\) from Example 9.2 of the current lesson. Its only geometric two-torsion point is its identity, so its \(2\)-rank is zero. Theorem 6.2 gives

\[
\dim\operatorname{Lie}(E[2])=1.
\]

On the other hand, \(\alpha_2\times\alpha_2\) has tangent-space dimension two, as is immediate from its ring \(k[u,v]/(u^2,v^2)\) and augmentation ideal. Thus

\[
E[2]\not\simeq\alpha_2\times\alpha_2
\]

as group schemes, although both have rank four and one geometric point. The product decomposition asserted in Remark I.7.4 of Milne's 2008 version would give precisely that false isomorphism when \(g=1\) and \(p\)-rank zero. Its valid geometric point bound is retained; the displayed group-scheme decomposition is not used. Likewise (F.1) is an isomorphism of underlying schemes with chosen parameters, and carries no claim about the comultiplication.

### Reduced connected subgroups over imperfect fields

**Theorem 8.8.** If \(H\hookrightarrow A\) is any closed subgroup scheme, then its identity component \(H^0\) is open and closed and geometrically irreducible, and \((H^0)_{\mathrm{red}}\) is an abelian subvariety over \(k\). In particular its reduction is geometrically reduced even when \(k\) is imperfect.

**Proof.** The component assertions are *Group schemes over a field*, Theorem 2.3. Replace \(H\) by \(H^0\), and put \(D=H_{\mathrm{red}}\), for now viewed only as a reduced closed subscheme. Over \(\overline k\), the reduced connected subgroup \((H_{\overline k})_{\mathrm{red}}\) is an abelian subvariety by the perfect-field reduced-group results used in 8.7.

Choose a prime \(\ell\ne\operatorname{char}k\). For every \(r\), the scheme \(H[\ell^r]\) is a closed subscheme of the finite étale scheme \(A[\ell^r]\), and is itself finite étale: a quotient of a finite product of finite separable fields is a product of some of those fields. It is reduced, hence its inclusion in \(H\) factors through \(D\). Over \(\overline k\), it equals the \(\ell^r\)-torsion of \((H_{\overline k})_{\mathrm{red}}\). Indeed both are reduced closed subschemes of the split finite étale \(A[\ell^r]_{\overline k}\), and have exactly the same points. 8.7 therefore makes the union of their underlying spaces dense in \(|H|=|D|\).

For any affine open \(U=\operatorname{Spec}C\subset D\), let \(E_r\) be the algebra of \(U\cap H[\ell^r]\), allowing the zero algebra for an empty intersection. It is finite étale over \(k\). Density and reducedness make

\[
C\longrightarrow\prod_{r\ge0} E_r
\tag{D.2}
\]

injective: a function zero on those schemes vanishes at a dense set of points, and is zero in the reduced ring \(C\). Let \(L/k\) be a finite field extension. Tensoring (D.2) with the flat \(k\)-module \(L\) preserves injectivity. Since \(L\) is finite-dimensional, tensoring with it commutes with this product: choosing a finite \(k\)-basis turns both sides of that comparison into the same finite direct sum of \(\prod_r E_r\). Thus

\[
C\otimes_k L\hookrightarrow\prod_r(E_r\otimes_k L).
\]

Every factor on the right is reduced, because finite étale algebras remain finite étale after extension. Hence \(C\otimes_k L\) is reduced for every finite \(L/k\).

If \(C\otimes_k\overline k\) had a nonzero nilpotent, its finitely many coefficients would lie in a finite subextension \(L/k\). The injective map from \(C\otimes L\) to \(C\otimes\overline k\) would exhibit the same nonzero nilpotent already over \(L\), a contradiction. Consequently \(D\) is geometrically reduced. Geometric irreducibility of \(H\) now makes \(D\) geometrically integral. Over \(\overline k\), it is exactly the reduced subgroup \((H_{\overline k})_{\mathrm{red}}\); descent of the equations for addition, inverse and identity makes \(D\) a subgroup over \(k\). It is proper as a closed subscheme of \(A\), so is an abelian variety under our definition. \(\square\)

### Verschiebung over an arbitrary base and its Cartier dual

This section concerns flat **commutative** group schemes over an arbitrary \(\mathbf F_p\)-scheme. Commutativity is an essential hypothesis from the definition preceding source (5.19). The finite-duality assertion has the additional hypothesis finite locally free. No existence of the whole symmetric-power quotient of an arbitrary scheme is presumed.

**Lemma 8.9 (the flat-module trace calculation).** Let \(R\) be an \(\mathbf F_p\)-algebra and \(M\) an \(R\)-module. Set

\[
\begin{gathered}
T_p(M)=M^{\otimes_Rp},\\
I_p(M)=T_p(M)^{\mathfrak S_p},\\
N(t)=\sum_{\sigma\in\mathfrak S_p}\sigma t.
\end{gathered}
\]

There is a natural \(R\)-linear map

\[
\phi_M:M\otimes_{R,F_R}R\longrightarrow I_p(M)/N(T_p(M)),
\qquad m\otimes r\longmapsto r[m^{\otimes p}].
\tag{V.1}
\]

If \(M\) is flat, this map is an isomorphism.

**Proof.** In expanding \((m+n)^{\otimes p}\), every mixed orbit has multiplicities \(j,p-j\), with \(0<j<p\), and its orbit sum is \(N\) of a representative divided by \(j!(p-j)!\), a unit in \(R\). These mixed terms vanish in the quotient. Also \((am)^{\otimes p}=a^p m^{\otimes p}\). These two facts prove the additivity and Frobenius-balanced relation needed for (V.1).

If \(M\) is free, choose a basis. Its tensor-word basis is permuted by \(\mathfrak S_p\), so invariant tensors have a basis of sums of distinct words in each orbit. The trace of a representative is its orbit sum multiplied by the order of its stabilizer. For a mixed word that order is a product of factorials of integers strictly less than \(p\), hence a unit; for a constant word it is \(p!=0\). Thus the trace quotient is free on the classes \(e^{\otimes p}\) of constant words, exactly the basis supplied by the Frobenius twist. This proves the assertion for free modules, including infinite bases.

We supply the flat-module passage explicitly. Consider the category of maps \(R^n\to M\), for finite \(n\), with arrows given by compatible linear maps. It is filtered. Direct sum gives a common recipient for two objects. For parallel arrows with difference matrix \(A:R^m\to R^n\) and an object \(f:R^n\to M\) satisfying \(fA=0\), write \(m_i=f(e_i)\). Flatness, applied to the kernel of \(A^{\mathrm t}:R^n\to R^m\), gives

\[
(m_i)_i=\sum_{j=1}^N v_j\otimes z_j,
\qquad v_j\in\ker A^{\mathrm t},\ z_j\in M.
\]

Indeed tensoring its kernel–image–target exact sequences with \(M\) identifies that kernel with the kernel after tensoring. Let \(u:R^n\to R^N\) have the rows \(v_j^{\mathrm t}\), and let \(g:R^N\to M\) send its basis to \(z_j\). Then \(f=gu\) and \(uA=0\), so this arrow equalizes the original pair. The colimit of these free modules is \(M\): every element comes from a map \(R\to M\), and an element of a finite free module mapping to zero is killed in a later object by the same construction with its single-column relation matrix. Thus every flat module is a filtered colimit of finite free modules, with a proof given here rather than an unproved Lazard citation.

Filtered colimits of modules are exact: a representative of a zero colimit element becomes zero at a later stage, which proves exactness element by element. They commute with finite tensor products, by the universal multilinear maps and the diagonal cofinality of a filtered index. Invariants under this finite group are the kernel of the map to the finite direct sum of the differences \((\sigma-1)\), and therefore commute with these colimits; so do the trace map and its cokernel. The Frobenius twist also commutes with colimits. Taking the colimit of the free-module isomorphisms proves (V.1). \(\square\)

For a flat \(R\)-algebra \(C\), put \(J=N(T_p(C))\subset I_p(C)\). It is an ideal, since \(N(st)=sN(t)\) for invariant \(s\). The map (V.1) is now an algebra isomorphism

\[
C^{(p/R)}\xrightarrow{\sim} I_p(C)/J:
\qquad c\otimes r\longmapsto r[c^{\otimes p}],
\tag{V.2}
\]

because pure tensors preserve products and units. This construction is functorial. Invariants and traces commute with flat base change by the kernel calculation; hence the affine symmetric quotient and (V.2) commute with flat base change. This proves the exact module and affine assertions needed for source (5.16)–(5.17).

**Theorem 8.10 (arbitrary-base Verschiebung).** Let \(S\) be an \(\mathbf F_p\)-scheme and \(G\) a flat commutative \(S\)-group scheme. There is a natural homomorphism

\[
V_{G/S}:G^{(p/S)}\longrightarrow G,
\qquad V_{G/S}F_{G/S}=[p]_G.
\tag{V.3}
\]

The construction commutes with flat base change. For abelian varieties over fields it agrees with 8.4. No finite-type, smoothness, or perfectness hypothesis is imposed on \(G\) or \(S\).

**Proof.** Work over an affine \(T=\operatorname{Spec}R\subset S\) and an affine \(U=\operatorname{Spec}C\subset G_T\). Flatness of \(G\) makes \(C\) a flat \(R\)-module. The finite constant group \(\mathfrak S_p\) acts on the affine \(U_T^p\); its invariant quotient is \(Q_U=\operatorname{Spec}I_p(C)\). The exact scheme-target categorical property is [Quotients and torsors, Proposition 11.1](quotients-and-torsors.md#11-categorical-and-geometric-quotients), using its Sections 1–3. The iterated group addition \(U_T^p\to G_T\) is invariant because \(G\) is commutative, so it induces \(Q_U\to G_T\). Restrict it to the closed subscheme cut out by \(J\). Via (V.2), this is a morphism

\[
v_U:U^{(p/T)}\longrightarrow G_T.
\]

The diagonal \(U\to U_T^p\) kills \(J\), since multiplication of a trace has the factor \(p!\). The composite of its restriction with (V.2) is relative Frobenius, as checked on \(c\otimes r\mapsto rc^p\). Iterated addition of the diagonal is \([p]\); hence \(v_UF_{U/T}=[p]|_U\).

These local maps glue. For an affine open \(W\subset U\), naturality of the tensor, trace and diagonal constructions and uniqueness of the categorical quotient factor make the map from \(W^{(p/T)}\) the restriction of \(v_U\). On an overlap of two affine opens, cover the overlap by affine opens \(W\) and apply this observation twice. For an open change of affine base, the same comparison follows from flat-base-change compatibility. The opens \(U^{(p/T)}\) cover \(G^{(p/S)}\), so we obtain \(V\) and (V.3).

Naturality for a homomorphism \(a:G\to H\) follows locally from naturality of the tensor construction and from \(a\) commuting with iterated addition; cover the source near a point by an affine open mapped into an affine open of the target. Thus \(aV_G=V_Ha^{(p)}\). Projections show \(V_{G\times G}=V_G\times V_G\). Apply naturality to the homomorphism \(m:G\times G\to G\), which is a homomorphism precisely because \(G\) is commutative. It gives \(m(V_G\times V_G)=V_Gm^{(p)}\), the homomorphism identity. The identity section is preserved by the same construction, and inverse follows. Flat-base-change compatibility was already proved on the affine opens. For an abelian variety, relative Frobenius is faithfully flat by 8.2, so the identity \(VF=[p]\) and uniqueness in 8.4 identify the two constructions. \(\square\)

The proof uses affine symmetric quotients only near repeated points and glues the Frobenius-twisted opens. It consequently establishes the arbitrary-base group theorem even when a whole quotient \(G_S^p/\mathfrak S_p\) has not been shown to be a scheme. The source's global symmetric-power notation for an arbitrary scheme needs its own quotient-existence hypotheses; it is not an additional theorem supplied by this argument.

**Theorem 8.11 (Cartier duality).** If \(G/S\) in 8.10 is finite locally free, there are canonical twist identifications for which

\[
(V_{G/S})^D=F_{G^D/S},
\qquad V_{G/S}=(F_{G^D/S})^D.
\tag{V.4}
\]

**Proof.** Finite locally free commutative Cartier duality over every base, including its tensor-dual and bidual identifications, is proved in [Group schemes, actions and Hopf algebras, Theorem 3.1](group-schemes-actions-and-hopf-algebras.md#3-finite-groups-and-their-character-partners). Work locally over \(R\), with the Hopf algebra \(C\) free on \(e_1,\ldots,e_n\), and let \(C^\vee\) have the dual basis. The comorphism of \(V\) is the iterated comultiplication followed by the trace-quotient map:

\[
C\xrightarrow{\Delta_p}I_p(C)\longrightarrow C^{(p/R)}.
\tag{V.5}
\]

The second map sends mixed orbit sums to zero and \(e_i^{\otimes p}\) to \(e_i\otimes1\). The canonical identification

\[
(C^\vee)^{(p/R)}\simeq(C^{(p/R)})^\vee
\]

sends \(\varphi\otimes r\) to the functional \(c\otimes s\mapsto sr\,\varphi(c)^p\); a basis verifies it is an isomorphism, and finite projective localization makes it canonical and compatible with overlaps.

For any symmetric tensor, pairing with \(\varphi^{\otimes p}\) gives zero on every mixed orbit sum: its orbit has size \(p!/\prod_j\alpha_j!\), divisible by \(p\), and each of its words has the same pairing. On a constant word \(e_i^{\otimes p}\), its value is \(\varphi(e_i)^p\). Therefore transposing (V.5) sends

\[
\varphi\otimes r\longmapsto r\varphi^p\in C^\vee,
\]

where the power is convolution, the multiplication on the dual Hopf algebra. This is exactly the ring formula for relative Frobenius on \(G^D\). It proves the first identity. Biduality and compatibility of finite duality with base change prove the second. Local computations glue because all their identifications are natural. The proof includes nilpotent rings \(R\) and requires no separability. \(\square\)

## 9. Elliptic curves make the difference visible

An **elliptic curve** is a one-dimensional abelian variety. We now construct the group law on a smooth plane cubic with a chosen rational flex. The construction includes coincident points and tangent lines, and proves the identities as identities of morphisms, so they hold on families with nilpotent parameters as well.

**Lemma 9.0a. Point classes on a cubic.** Let \(C\) be a smooth plane cubic over an algebraically closed field. If two points \(P,Q\) have linearly equivalent degree-one divisors, then \(P=Q\).

**Proof.** First \(C\) is integral. A reducible cubic has a line component and a remaining degree-two component; their equations have a common point over the algebraically closed field, because the latter restricts to a positive-degree homogeneous polynomial on that line. At that point the derivative of their product vanishes. A repeated component similarly contradicts smoothness. Thus the cubic is irreducible and reduced.

There is a nowhere vanishing regular differential on \(C\), in every characteristic. Write its homogeneous equation as \(F(X,Y,Z)=0\). On \(Z\ne0\), put \(x=X/Z\), \(y=Y/Z\) and \(f(x,y)=F(x,y,1)\). On the opens where the indicated denominator is a unit, set

\[
\omega=\frac{dx}{f_y}=-\frac{dy}{f_x}.
\]

The equality follows from \(df=f_xdx+f_ydy=0\), and the smooth-curve differential module shows that each expression is a regular generator on its open. Those opens cover this affine chart: if both partials vanished, Euler's homogeneous identity on \(F=0\) would also force \(F_Z=0\), contrary to smoothness. No division by the characteristic or by the degree is involved.

On \(Y\ne0\), use the cyclic coordinates \(u=Z/Y\), \(v=X/Y\), with equation \(g(u,v)=F(v,1,u)\), and take \(du/g_v=-dv/g_u\). On the overlap with \(Z\ne0\), we have \(u=1/y\), \(v=x/y\) and \(g_v=y^{-2}f_x\). Hence \(du/g_v=-dy/f_x\), proving that these generators agree. The same cyclic calculation on \(X\ne0\) completes the gluing. Thus \(\omega\) is globally regular and nowhere vanishing.

If \(P\ne Q\) and \((P)-(Q)\) were principal, its defining rational function \(h\) would give a nonconstant morphism \(f:C\to\mathbf P^1\) with a single simple pole at \(Q\). The local extension to a morphism is explicit: the regular local ring of a smooth curve is a DVR, so at each point either \(h\) or \(h^{-1}\) is regular. These expressions give its two projective charts and agree on their overlap.

Here is the finiteness argument in this particular projective-curve situation. The graph embeds \(C\) as a closed subscheme of \(\mathbf P^2\times\mathbf P^1\), so \(f\) is projective and proper. Its fibres are finite: the inverse image of a point is a proper closed subset of the integral curve, hence has dimension zero and finitely many points. At each closed target point, choose a linear form on \(\mathbf P^2\) not vanishing at any point of that fibre. Such a form exists over the infinite algebraically closed field. The image of its zero section on \(C\) is closed by properness and misses the chosen target point. On an affine neighbourhood \(V=\operatorname{Spec}A\) avoiding this image, the whole inverse image lies in the affine chart where the linear form is nonzero. It is closed in \(\mathbf A^2\times V\), and therefore is affine, say \(\operatorname{Spec}B\). These neighbourhoods cover the target, since a nonempty closed subset of \(\mathbf P^1\) has a closed point.

Every element \(b\in B\) is integral over \(A\). For if a nonzero \(b\) were not integral, then \(b^{-1}\) would be a nonunit of \(A[b^{-1}]\): an equation making it a unit would, after multiplication by a power of \(b\), give a monic equation for \(b\). Choose a maximal ideal containing \(b^{-1}\), and a valuation ring of \(k(C)\) dominating the resulting local domain. Its existence is proved in *Valuation rings and the valuative criterion of separatedness*, Theorem 2.1. The generic point map to \(C\) extends to this valuation ring: scale its three homogeneous coordinates so that all lie in the valuation ring and one is a unit; the equation of \(C\) continues to hold. Its composite to \(V\) is the given map because the two maps agree generically and \(V\) is separated. Thus it factors through \(f^{-1}(V)=\operatorname{Spec}B\), which puts \(b\) in the valuation ring. This contradicts \(b^{-1}\) being in its maximal ideal. Therefore \(B/A\) is integral. It is of finite type, so finitely many algebra generators satisfy monic equations; their bounded powers span a finite \(A\)-module. Hence \(f\) is finite.

It is flat, since its finite coordinate module over each target DVR is torsion-free and hence free. Its fibre at infinity has length one, so its finite flat rank is one. The unit map to a finite locally free algebra of rank one is an isomorphism, as can be checked on its residue fields and then by Nakayama. The curve would therefore be isomorphic to \(\mathbf P^1\).

But \(\mathbf P^1\) has no nonzero regular differential. On its affine chart such a differential is \(h(t)dt\) with polynomial \(h\); under \(t=1/u\), every nonzero such expression has a pole at \(u=0\). This contradicts the differential \(\omega\) just constructed. Hence \(P=Q\). \(\square\)

**Theorem 9.0. The cubic group law.** Let \(C/k\) be a smooth plane cubic with a rational flex \(O\). There is a commutative group-scheme structure on \(C\) with identity \(O\). If a line cuts out the divisor \((P)+(Q)+(R)\), counting multiplicities, then \(P+Q+R=O\). For geometric points,

\[
[(P+Q)-(O)]=[(P)-(O)]+[(Q)-(O)]
\]

in the group of degree-zero divisor classes. More precisely, for every field extension \(L/k\) and \(P,Q\in C(L)\), the divisor \((P)+(Q)-(P+Q)-(O)\) is principal over \(L\) itself. The group law is a morphism on \(C\times_k C\), including the diagonal; its scheme identities remain valid after every base change.

**Proof.** Smoothness implies geometric integrality by the preceding irreducibility argument after extending the field. The curve is smooth, projective and one-dimensional. It remains to construct the operations and verify their identities.

**Secants across the diagonal.** Put \(B=C\times_k C\), and denote its two universal points by \(P,Q\). For distinct points their joining line has coefficients given by the three minors of their homogeneous coordinate vectors, or equivalently by \(\det(P,Q,-)\). These are locally sections of one invertible sheaf on \(B\). Their common ideal is the diagonal ideal: the analogous minors define the diagonal of \(\mathbf P^2\), whose pullback to \(C\times C\) is exactly the diagonal of the closed immersion \(C\to\mathbf P^2\).

The diagonal of a smooth curve is an effective Cartier divisor. Divide the three coefficients by a local equation of this divisor. The quotients generate the unit ideal, since the original coefficients generate the diagonal ideal. Thus they define a morphism from \(B\) to the dual projective plane; changes of local equation multiply all three by the same unit, so the maps glue. Its value on the diagonal is the tangent line: the divided coordinate differences are precisely the first derivatives of the curve's immersion. We have obtained a universal secant-or-tangent line \(\ell\), without choosing a slope or omitting vertical lines.

**The residual point in families.** In \(C\times B\), the equation of \(\ell\) cuts out a relative divisor \(D\). The two graphs \(\Gamma_P,\Gamma_Q\) are Cartier divisors, and its section vanishes on both. The equation is divisible by their product, including where \(P=Q\). Here is a local check at such an intersection. Choose an étale parameter on the smooth curve; near the triple diagonal the graph ideals have equations \(a=t-p\), \(b=t-q\). Their difference defines the diagonal in the parameter base. In particular \(a,b\) form a regular sequence. If an element divisible by \(a\) also belongs to \((b)\), reducing modulo \(b\) and using that \(a\) is a non-zero-divisor there proves divisibility by \(ab\). Away from their intersection the same assertion is immediate. These local factorizations give a global residual divisor

\[
D-\Gamma_P-\Gamma_Q.
\]

On every geometric fibre the line meets the cubic in length three: restriction of its homogeneous cubic equation to the line is a nonzero degree-three polynomial on \(\mathbf P^1\). It is nonzero because an integral cubic has no line component. The two graph divisors remove length two, with multiplicity when they coincide. The residual divisor therefore has length one on every geometric fibre.

It is the graph of a section \(r:B\to C\). To justify this family assertion, a residual zero of length one on a smooth curve has a nonzero derivative in a curve parameter. The étale-coordinate criterion consequently makes the residual divisor étale over \(B\). Its geometric fibres each consist of one reduced point. The diagonal of this étale morphism is an open immersion; it contains every geometric point of the fibre product, and therefore is an isomorphism. Thus the morphism is a monomorphism. It is also a surjective étale covering, so its unique local sections descend and give an inverse. It is an isomorphism to \(B\), as asserted. This proves that the third-intersection point is a morphism, also for tangents and flexes. All these statements concern the universal family over \(B\); their pullbacks apply to every test scheme.

Define \(i(P)=r(P,O)\) and \(m(P,Q)=i(r(P,Q))\). Both are morphisms over \(k\). We prove that they are inversion and addition.

The principal-divisor formula already holds over the field of definition. For \(P,Q\in C(L)\), put \(R=r(P,Q)\) and \(S=i(R)\). The secant-or-tangent line \(\ell_{P,Q}\) and the line \(\ell_{R,O}\) are defined over \(L\) by the morphism just constructed. Their respective intersection divisors are \((P)+(Q)+(R)\) and \((R)+(O)+(S)\). The quotient of their linear equations, restricted to \(C_L\), is a nonzero rational function with divisor

\[
\operatorname{div}\bigl(\ell_{P,Q}/\ell_{R,O}\bigr)
=(P)+(Q)-(S)-(O).
\]

The restrictions are nonzero because the cubic has no line component. This computation includes repeated points and coincident lines; in the latter case the quotient is constant and the divisor is zero. It proves principality over \(L\), without a descent assertion about divisor classes. After identifying \(m\) with addition, it is the promised formula with \(S=P+Q\).

**Divisor classes give the identities.** Work over an algebraic closure for this verification. Every line section is linearly equivalent to the hyperplane divisor. The tangent line at the flex \(O\) cuts out \(3(O)\), so for every pair of points

\[
(P)+(Q)+(r(P,Q))\sim3(O),\qquad
(R)+(O)+(i(R))\sim3(O).
\]

Subtracting these identities gives

\[
[(m(P,Q))-(O)]=[(P)-(O)]+[(Q)-(O)],\qquad
[(i(P))-(O)]=-[(P)-(O)].
\]

By Lemma 9.0a the map \(P\mapsto[(P)-(O)]\) is injective. Associativity and commutativity of divisor-class addition therefore prove those identities for \(m\) on every geometric triple or pair. The zero class proves the identity law for \(O\), and the second formula proves the inverse law for \(i\). They also prove the asserted principal-divisor relation and the line rule.

Finally these are identities of morphisms. The sources \(C\), \(C^2\) and \(C^3\) are geometrically reduced schemes of finite type, and the target is separated. The closed equalizer of two of the morphisms contains every geometric point; on affine charts its equations consequently lie in the nilradical, which is zero. Thus the morphisms agree after the algebraic closure and hence over \(k\). Identities of scheme morphisms persist after arbitrary base change, including bases with nilpotents. The resulting smooth projective geometrically integral group curve is an abelian variety. \(\square\)

*Comparison and credit:* Milne, *Algebraic Groups*, Chapter 2c, records the cubic group-law construction. The proof above supplies the secant family, residual section, injective point classes and all scheme identities internally; it does not assume representability of a Picard scheme or an elliptic group law in order to construct this one.

**Example 9.1. Four points of order dividing two.** Let \(\operatorname{char}k\ne2\), and let \(f(x)\) be a separable cubic. The smooth projective curve with affine equation

\[
E:y^2=f(x)
\]

has a unique point \(O=[0:1:0]\) at infinity, a rational flex. Its affine partial derivatives are \(2y\) and \(-f'(x)\); a common zero on the curve would be a repeated root of \(f\), so none exists. The homogeneous \(Z\)-partial is nonzero at \(O\), proving smoothness there as well. A smooth plane cubic is geometrically integral: distinct positive-degree components in the geometric plane would meet and make the curve singular. The vertical line through \((x,y)\) meets the cubic at \((x,y),(x,-y),O\). Thus inversion is \((x,y)\mapsto(x,-y)\). An affine point is killed by two exactly when \(y=0\). Over \(\overline k\) these are the three distinct points \((r_i,0)\) at the roots of \(f\). Together with \(O\) they give

\[
E[2](\overline k)\simeq(\mathbf Z/2)^2.
\tag{25}
\]

The group is killed by two and has four elements, which proves the isomorphism directly. It is also the \(g=1,n=2\) instance of (18).

**Example 9.2. Ordinary and supersingular in characteristic two.** Over an algebraically closed field of characteristic two consider

\[
E_{\mathrm{ord}}:y^2+xy=x^3+1,\qquad
E_{\mathrm{ss}}:y^2+y=x^3.
\tag{26}
\]

Both are smooth projective cubics with the flex \(O=[0:1:0]\) at infinity. For the first, the homogeneous equation is

\[
F=Y^2Z+XYZ+X^3+Z^3=0.
\]

On the affine chart \(Z=1\), its partial derivatives in \(x,y\) are \(y+x^2,x\). A singular point would have \(x=y=0\), which does not lie on the curve. At infinity the equation forces \(X=0\), and \(F_Z\) is nonzero at \(O\). For the second cubic the homogeneous equation is \(Y^2Z+YZ^2+X^3=0\); its three partial derivatives are \(X^2,Z^2,Y^2\), which cannot all vanish at a projective point.

In each equation a vertical line's two affine intersections are exchanged by

\[
(x,y)\longmapsto(x,y+x)\quad\text{on }E_{\mathrm{ord}},
\qquad
(x,y)\longmapsto(x,y+1)\quad\text{on }E_{\mathrm{ss}}.
\]

The third intersection is \(O\), so these are the inverse maps. In the first curve an affine point fixed by inversion has \(x=0\), then \(y^2=1\), giving the unique point \((0,1)\). Its two-torsion has two geometric points including \(O\), hence \(p\)-rank one. In the second curve no affine point is fixed, so its two-torsion has only \(O\), hence \(p\)-rank zero.

An elliptic curve is called **ordinary** when its \(p\)-rank is one and **supersingular** when it is zero. These two cases exhaust the possibilities by \(f\leq g=1\). The computations in (26) realize both. Theorem 6.1 nevertheless gives rank four for both finite group schemes \(E[2]\); the point counts two and one record different nonreduced structures.

**Example 9.3. Products.** If \(A=E_1\times\cdots\times E_g\), then it is an abelian variety: smoothness, properness and geometric integrality are preserved in this finite product, and the group law is coordinatewise. Its torsion schemes and point groups are the corresponding products. In positive characteristic its \(p\)-rank is the sum of the elliptic \(p\)-ranks. In characteristic two, taking \(f\) copies of the first curve in (26) and \(g-f\) of the second realizes every point count \(2^f\), \(0\leq f\leq g\), while the kernel rank remains \(2^{2g}\).

### Weierstrass calculations in characteristics two and three

Start with a smooth projective Weierstrass cubic with origin \(O=(0:1:0)\):

\[
y^2+a_1xy+a_3y=x^3+a_2x^2+a_4x+a_6.
\tag{W.1}
\]

The chord-and-tangent law and its scheme-level associativity are the current lesson's Theorem 9.0. A vertical line cuts \(P\), the point \((x,-y-a_1x-a_3)\), and \(O\); consequently that second point is \(-P\).

**Proposition 9.4 (characteristic two).** In characteristic two the geometric \(2\)-rank is zero precisely when \(a_1=0\). If \(a_1\ne0\), the sole nonidentity geometric point of order two has

\[
\xi=a_3/a_1,
\qquad \eta^2=\xi^3+a_2\xi^2+a_4\xi+a_6.
\tag{W.2}
\]

If \(a_1=0\), then \(a_3\ne0\); over an algebraically closed field the cubic is isomorphic, with origin, to \(Y^2+Y=X^3\).

**Proof.** Inversion fixes an affine point precisely when \(a_1x+a_3=0\). If \(a_1\ne0\), this gives one \(x\)-coordinate and the square equation in (W.2) has exactly one root over an algebraic closure. Thus the geometric two-torsion has two points. If \(a_1=a_3=0\), the affine derivatives of the equation are \(x^2+a_4\) and zero. Choose a root of \(x^2+a_4\), then a square root of the right side of (W.1); the resulting point is singular. Smoothness excludes this case. If \(a_1=0\), therefore \(a_3\ne0\), inversion has no affine fixed point, and the geometric two-torsion consists only of \(O\). This proves the rank assertion and corrects the missing zero in the source's sentence about \(a_1,a_3\).

For the normal form, extend to an algebraic closure. Choose \(u\ne0\) with \(u^3=a_3\) and substitute \(x=u^2X\), \(y=u^3Y\). The equation becomes

\[
Y^2+Y=X^3+b_2X^2+b_4X+b_6.
\]

Choose a root \(r\) of \(r^4+r+b_4^2+b_2=0\), and put \(b=r^2+b_4\). Then \(b^2=r+b_2\). Substitute \(X=W+r\) and \(Y=Z+bW+c\). The coefficients of \(W^2\) and \(W\) cancel. Choose \(c\) with \(c^2+c=r^3+b_2r^2+b_4r+b_6\); the constant cancels too. The result is \(Z^2+Z=W^3\). All substitutions are invertible projective Weierstrass changes and preserve \(O\). The scalar choices in this proof are made only over an algebraic closure, so this is not a normal-form assertion over an imperfect ground field. \(\square\)

**Proposition 9.5 (characteristic three).** Complete the square in (W.1), obtaining

\[
y^2=x^3+b_2x^2+b_4x+b_6.
\tag{W.3}
\]

Then \(E\) is ordinary precisely when \(b_2\ne0\). In that case its two nonidentity geometric three-torsion points are \((\xi,\pm\eta)\), with

\[
4b_2\xi^3+4b_2b_6-b_4^2=0,
\qquad \eta^2=\xi^3+b_2\xi^2+b_4\xi+b_6.
\tag{W.4}
\]

**Proof.** The substitution \(y\mapsto y+(a_1x+a_3)/2\) is allowed in characteristic three, and gives \(b_2=a_2+a_1^2/4\), \(b_4=a_4+a_1a_3/2\), \(b_6=a_6+a_3^2/4\). If \(b_2=b_4=0\), a root of \(x^3+b_6\) with \(y=0\) is singular; hence those two coefficients cannot both vanish.

A nonidentity point \(P\) has \(3P=0\) exactly when its tangent cuts the cubic three times at \(P\), because the third tangent intersection is \(-2P\). A point with \(y=0\) is two-torsion and cannot also be nonzero three-torsion. At \(P=(\xi,\eta)\) with \(\eta\ne0\), the tangent slope is

\[
m=(2b_2\xi+b_4)/(2\eta).
\]

Set \(x=\xi+t\), \(y=\eta+mt\). The linear term of the equation cancels; its remaining terms are \(t^2(m^2-b_2)-t^3\). It is a triple tangent precisely when

\[
4b_2\eta^2=4b_2^2\xi^2+4b_2b_4\xi+b_4^2.
\tag{W.5}
\]

Substituting (W.3) reduces this to (W.4). If \(b_2=0\), (W.5) would force \(b_4=0\), already excluded; there is no nonidentity three-torsion. If \(b_2\ne0\), the first equation of (W.4) has exactly one geometric solution \(\xi\). Its right side in the square equation is nonzero: otherwise (W.5) also gives \(2b_2\xi+b_4=0\), producing a singular point. The two roots \(\pm\eta\) are consequently distinct and nonzero. This proves the count and the rank assertion. \(\square\)

For instance \(y^2=x^3+x^2+t\) over \(\mathbf F_3(t)\) is smooth: an affine singular point would require \(y=x=0\), which is off the curve, and the infinity derivative is nonzero. Its nonidentity geometric three-torsion has \(\xi^3=-t\), so its separable closure does not contain those points. This is the characteristic-three version of 8.6, with the twist and the algebraic closure still essential.

### An explicit infinitesimal action and a varying family

**Theorem 9.6 (the characteristic-two quotient).** Over any field \(k\) of characteristic two let

\[
E:\quad Y^2Z+YZ^2=X^3,
\qquad O=(0:1:0).
\tag{Q.1}
\]

Its Frobenius kernel is isomorphic to \(\alpha_2\). The following formulas define its translation action, and its quotient is the relative Frobenius \(E\to E^{(2)}\), with \(E^{(2)}\simeq E\) through this equation over \(\mathbf F_2\).

**Proof.** The cubic is smooth, as follows directly from its three partial derivatives, and \(O\) is a flex. Use the two affine charts

\[
\begin{gathered}
U=\operatorname{Spec}k[x,y]/(x^3+y^2+y),\\
W=\operatorname{Spec}k[w,z]/(w^3+z^2+z).
\end{gathered}
\]

They are \(Z\ne0\) and \(Y\ne0\); on the overlap \(w=x/y\), \(z=1/y\). Write \(\alpha_2=\operatorname{Spec}k[\epsilon]/(\epsilon^2)\). On the charts define

\[
x\longmapsto x+\epsilon,\quad y\longmapsto y+\epsilon x^2;
\qquad
w\longmapsto w+\epsilon,\quad z\longmapsto z+\epsilon w^2.
\tag{Q.2}
\]

On \(U\) this is \(a\mapsto a+\epsilon D(a)\), where \(D(x)=1\), \(D(y)=x^2\). The derivative of the relation is \(x^2+x^2=0\), and \(D^2=0\) on the generators, hence on the algebra. Since the characteristic is two, \(D^2\) is a derivation; these checks prove the relation and the group-action identity for \(\epsilon+\epsilon'\), including the cross term \(\epsilon\epsilon'D^2\). On the overlap

\[
\begin{gathered}
D(x/y)=(y+x^3)/y^2=1,\\
D(1/y)=x^2/y^2=w^2,
\end{gathered}
\]

so the formulas glue. The second chart has the same verification.

Put \(\xi=x^2\), \(\eta=y^2\). The invariant algebra on \(U\) is exactly

\[
B=k[\xi,\eta]/(\xi^3+\eta^2+\eta).
\tag{Q.3}
\]

Here is a full ring check. There are inverse isomorphisms

\[
\begin{gathered}
k[x,y]/(x^3+y^2+y)\simeq B[x]/(x^2-\xi),\\
y=\eta+\xi x.
\end{gathered}
\]

Indeed \(y^2=\eta^2+\xi^3=\eta\), and \(y^2+y=\xi x=x^3\); conversely the original relation gives \(y=y^2+x^3\). Thus the algebra is free over \(B\) with basis \(1,x\), and \(D(b+cx)=c\). Its invariant elements are exactly \(B\). On the second chart the same calculation uses \(w^2,z^2\). The invariant-chart maps glue to relative Frobenius and identify the target with the equation (Q.1).

They also prove schematic freeness, rather than just the absence of fixed geometric points. In the relation algebra \(A\otimes_BA\), the two copies of \(x\) have difference \(\epsilon\) with \(\epsilon^2=0\), and their \(y\)'s have difference \(\epsilon x^2\). Consequently

\[
\alpha_2\times E\xrightarrow{\sim}E\times_{E^{(2)}}E.
\tag{Q.4}
\]

The two free rank-two chart extensions make the map an fppf cover, so (Q.4) proves it represents the quotient.

It remains to identify the action as translations; equality of the quotient map alone would not prove this. The difference morphism

\[
\delta:\alpha_2\times E\longrightarrow E,
\qquad (h,a)\longmapsto \rho(h,a)-a
\]

lands in \(K=\ker F\), because \(F\) is a homomorphism and \(F\rho(h,a)=F(a)\). This is a scheme identity. For every \(k\)-algebra \(R\),

\[
\Gamma(E_R,\mathcal O_{E_R})=R.
\]

To verify this even with nilpotents in \(R\), take a finite affine cover of the separated \(E\), with affine intersections. Its degree-zero Čech kernel is \(k\), by Lemma 1.1. Tensoring the kernel diagram with the flat \(k\)-module \(R\) gives the displayed equality. A morphism from \(E_R\) to an affine \(R\)-scheme is determined by global functions and therefore factors through the projection to \(\operatorname{Spec}R\). Apply this with \(R=k[\epsilon]/(\epsilon^2)\) and the affine \(K_R\). Thus \(\delta(h,a)=i(h)\), where \(i(h)=\rho(h,O)\). Evaluating (Q.4) over the fibre of \(F(O)\) makes \(i:\alpha_2\to K\) an isomorphism. The action identity now makes \(i\) a group homomorphism, and \(\rho(h,a)=a+i(h)\) on every test scheme. This proves the required translation assertion. \(\square\)

**Lemma 9.7 (the finite Hom lemma needed for the family).** If \(E\) is an elliptic curve and \(B\) is an abelian variety over a field, then \(M=\operatorname{Hom}_k(E\times E,B)\) is a finitely generated torsion-free abelian group.

**Proof.** Choose a symmetric ample line bundle \(L\) on \(B\): from an ample \(L_0\), take \(L_0\otimes[-1]^*L_0\). Let \(i_1,i_2:E\to E\times E\) be the two factors and define

\[
Q(f)=\deg (fi_1)^*L+\deg (fi_2)^*L.
\tag{Q.5}
\]

Each summand is nonnegative, and is positive for a nonconstant map. For completeness, take a very ample power of \(L\). Its coordinate sections on the curve have an effective zero divisor of nonnegative degree. If that degree were zero, a nonzero section would be nowhere zero and all its section ratios would be constant, by Lemma 1.1; the map to projective space would be constant. A homomorphism constant on \(E\) is zero. Since \(f(x,y)=f(x,0)+f(0,y)\), this proves \(Q(f)>0\) for \(f\ne0\).

Pull the cube formula (9) back along \((f,g,-g)\), first on each copy of \(E\). Since \(L\) is symmetric, it gives the parallelogram identity

\[
Q(f+g)+Q(f-g)=2Q(f)+2Q(g).
\tag{Q.6}
\]

The integer formula (13) gives \(Q(nf)=n^2Q(f)\). These identities make

\[
\langle f,g\rangle=\tfrac12\bigl(Q(f+g)-Q(f)-Q(g)\bigr)
\]

a symmetric biadditive form with \(Q(f)=\langle f,f\rangle\). To verify additivity, also write it as \(B(x,y)=(Q(x+y)-Q(x-y))/4\). The parallelogram identities for \((x+y,z)\) and \((x-y,z)\) give \(B(x+z,y)+B(x-z,y)=2B(x,y)\). Interchanging \(x,z\), and using \(B(z-x,y)=-B(x-z,y)\), gives \(B(x+z,y)-B(x-z,y)=2B(z,y)\). Adding proves additivity in the first variable, and symmetry gives it in the second. Positivity of \(Q(mf+ng)\) for integer \(m,n\), then for rational coefficients after clearing denominators, gives \(\langle f,g\rangle^2\le Q(f)Q(g)\) by the discriminant of the resulting quadratic polynomial. Hence \(\|f\|=\sqrt{Q(f)}\) satisfies the triangle inequality and every nonzero \(f\) has norm at least one. In particular \(M\) has no torsion.

For every integer \(n>1\) prime to the characteristic, restriction injects

\[
M/nM\hookrightarrow
\operatorname{Hom}_k\bigl((E\times E)[n],B[n]\bigr).
\tag{Q.7}
\]

Indeed a homomorphism zero on the schematic \(n\)-torsion factors uniquely through the fppf quotient \([n]:E\times E\to E\times E\), by 6.4, and is therefore \(n\) times another homomorphism. The target in (Q.7) is finite: after an algebraic closure its finite étale groups are constant finite groups, and a map over \(k\) is determined by that geometric restriction.

There are only finitely many \(f\) with \(\|f\|\le R\). Choose an integer \(n>2R\) prime to the characteristic. Two such elements in the same coset modulo \(nM\) differ by \(nh\); its norm is at most \(2R\), while a nonzero \(nh\) has norm at least \(n\). Thus they are equal, and (Q.7) bounds their number.

Finally fix one such integer \(n>1\) and finitely many representatives of \(M/nM\), with largest norm \(C\). Choose \(R\) with \((R+C)/n<R\). For any \(f\) with norm greater than \(R\), write \(f=r+nh\) using a chosen representative. Then \(\|h\|\le(\|f\|+C)/n<\|f\|\). Induction on the nonnegative integer \(Q(f)\) expresses every \(f\) using the representatives and the finite set with norm at most \(R\). This proves finite generation. All uses of the cube and multiplication formulas keep their existing anchors; no general Rosati or Tate-isogeny theorem is imported. \(\square\)

**Theorem 9.8 (the quotient family).** Let \(E/k\) be an elliptic curve in characteristic \(p\) with a specified group-scheme isomorphism \(E[F]\simeq\alpha_p\), and put \(A=E\times E\). Nonzero pairs \((\lambda,\mu)\) define finite subgroup schemes

\[
H_{(\lambda:\mu)}=
\operatorname{image}\bigl(\alpha_p\xrightarrow{(\lambda,\mu)}
\alpha_p^2\simeq A[F]\bigr).
\tag{Q.8}
\]

Their parameter is \(\mathbf P^1\). They form a finite locally free subgroup \(H\subset A\times\mathbf P^1\) of rank \(p\). Its quotient is a proper smooth group scheme over \(\mathbf P^1\) whose geometric fibres are abelian surfaces, and the maps on those fibres are isogenies of degree \(p\). For a fixed parameter \(s\in\mathbf P^1(k)\), only finitely many \(t\in\mathbf P^1(k)\) have \(A/H_t\simeq A/H_s\). The same finiteness holds geometrically, so the family is not geometrically isotrivial.

**Proof.** A Hopf endomorphism of \(k[\epsilon]/(\epsilon^p)\) must send \(\epsilon\) to a primitive element with zero constant term. In degree \(j\), \(1<j<p\), the coefficient of \(\epsilon\otimes\epsilon^{j-1}\) in its comultiplication is \(j\) times its degree-\(j\) coefficient, so that coefficient vanishes. Thus the primitive elements are precisely \(c\epsilon\), and \(\operatorname{End}(\alpha_p)=k\), with composition the product of scalars. A nonzero pair in (Q.8) is a closed immersion because one coordinate is an isomorphism. Two pairs have the same image precisely when they differ by a nonzero scalar. The zero pair has no such embedding and is excluded.

On the chart \(\lambda\ne0\), write \(t=\mu/\lambda\) and embed \(\alpha_p\) by \(\epsilon\mapsto(\epsilon,t\epsilon)\). On \(\mu\ne0\), write \(s=\lambda/\mu\) and use \(\epsilon'\mapsto(s\epsilon',\epsilon')\). On the overlap the change is \(s=t^{-1}\), \(\epsilon'=t\epsilon\). These glue the height-one additive group of the tautological line bundle \(\mathcal O(-1)\), with local algebra \(\mathcal O[\epsilon]/(\epsilon^p)\), into the constant \(A[F]\). This proves closedness and finite local freeness of rank \(p\), including at \(t=0\) and infinity.

The translation relation on \(A\times\mathbf P^1\) has finite locally free projections. The scheme \(A\times\mathbf P^1\) is projective over \(k\), so every finite orbit has an affine neighbourhood by *Quotients and torsors*, Lemma 5.4. Its Theorem 5.2 gives the scheme quotient \(Y\) and a finite locally free fppf cover \(q:A\times\mathbf P^1\to Y\) of rank \(p\). The invariant projection to \(\mathbf P^1\) descends. Addition and inverse descend because \(H\) is a subgroup of the commutative group. Finite type follows from the coefficient argument in 6.3, and separatedness and universal closedness over \(\mathbf P^1\) follow by the same relation and proper-cover argument there. Thus \(Y\) is proper. Flatness over \(\mathbf P^1\) descends along \(q\): on local rings the tensor of a test injection with \(\mathcal O_Y\) becomes injective after the faithfully flat extension to \(\mathcal O_{A\times\mathbf P^1}\), which is flat over the base. Finite type over the Noetherian base gives finite presentation. Base change of the effective quotient identifies each geometric fibre with \(A/H_t\); 6.3 makes it an abelian surface and therefore smooth. The fibrewise smoothness criterion for a flat morphism of finite presentation, [Smooth morphisms, Theorem 3.1](../../AG-FSE/src/smooth-morphisms.md#3-from-smooth-fibres-to-a-smooth-family), now gives smoothness of \(Y\to\mathbf P^1\). This proves the stated family assertion; it does not assume a global symmetric-power construction or a moduli-space representability theorem.

Fix \(B=A/H_s\). Whenever \(A/H_t\simeq B\), compose such an isomorphism with \(q_t\) to obtain \(f_t\in M=\operatorname{Hom}_k(A,B)\). If an isomorphism was initially taken just as a variety isomorphism, translate its image of zero to zero; the rigidity consequence for origin-preserving maps in Corollary 2.3 makes it a group isomorphism. Every \(\ker f_t=H_t\) lies in \(A[p]\). If \(f_t-f_u=ph\) in \(M\), their restrictions to the entire scheme \(A[p]\) agree, since \(ph|_{A[p]}=h[p]|_{A[p]}=0\). Their kernels inside that scheme are consequently equal, so \(H_t=H_u\) and \(t=u\). Lemma 9.7 makes \(M/pM\) finite. The parameter set for this fixed isomorphism class injects into that finite set.

The same argument over \(\overline k\) proves that every geometric isomorphism class has only finitely many parameters. Since \(\mathbf P^1(\overline k)\) is infinite, the family cannot become constant after a field extension. In characteristic two, 9.6 supplies an explicit \(E\) satisfying the hypothesis over every ground field, so gives a fully explicit instance of the family. \(\square\)

### Realizing geometric torsion ranks

The source's remark (5.25)(ii) asks for every field \(k\) of characteristic \(p\), not only algebraically closed fields. The following coefficient proof settles all primes over algebraically closed fields, supplies ordinary elliptic curves over every prime field, and supplies supersingular curves over every prime field with \(p=2,3\), \(p\equiv3\pmod4\), or \(p\equiv2\pmod3\). The missing prime-field case is stated after the proof.

**Lemma 9.9 (the coefficient criterion).** Let \(p\) be odd, \(h=(p-1)/2\), and \(E:y^2=f(x)\) a smooth cubic over a field of characteristic \(p\). If \(c\) is the coefficient of \(x^{p-1}\) in \(f(x)^h\), then \(E\) has geometric \(p\)-rank zero if \(c=0\), and one if \(c\ne0\).

**Proof.** Extend to an algebraic closure; \(c=0\) is unchanged by that faithful extension. Homogenize the equation to \(G=Y^2Z-f_h(X,Z)\) in \(\mathbf P^2\). The hypersurface exact sequence identifies \(H^1(E,\mathcal O_E)\) with the one-dimensional \(H^2(\mathbf P^2,\mathcal O(-3))\), since the higher structure-sheaf cohomology of projective space vanishes. The exact provider is [Cohomology of projective space, Lemma 2.1 and Theorem 2.2](../../AG-QC/src/cohomology-of-projective-space.md#2-negative-exponents-determine-cohomology). A basis of the latter group is the Laurent class \(1/(XYZ)\).

In that description Frobenius sends this class to

\[
\frac{G^{p-1}}{(XYZ)^p}.
\tag{R.1}
\]

To check the factor \(G^{p-1}\), lift a Čech one-cocycle on \(E\) to the structure sheaf on the projective affine cover. Its coboundary is \(G\) times a two-cochain. Taking \(p\)-th powers makes the coboundary \(G^p\) times that cochain's \(p\)-th power; dividing by \(G\) in the connecting map gives (R.1). The Laurent cohomology calculation kills terms unless each of \(X,Y,Z\) has negative exponent; since the total degree is \(-3\), the surviving term has all three exponents \(-1\). Thus the scalar is the coefficient of \(X^{p-1}Y^{p-1}Z^{p-1}\) in \(G^{p-1}\).

To obtain the \(Y\)-exponent \(p-1=2h\), select \(h\) factors \(Y^2Z\) and \(h\) factors \(-f_h\). The binomial coefficient is \(\binom{p-1}{h}=(-1)^h\) in the field; it cancels the sign of \((-f_h)^h\). The required remaining coefficient of \(X^{2h}Z^h\) in \(f_h^h\) is exactly \(c\). Frobenius on \(H^1(\mathcal O_E)\) is therefore zero precisely when \(c=0\).

We justify the link with the torsion rank. The genus-one identification \(E\simeq\operatorname{Pic}^0(E)\), with \(P\mapsto\mathcal O(P-O)\), is proved as a functor on all test schemes in [The Picard functor and the Picard scheme of a curve, Proposition 5.1 and Section 8](../../AG-HP/src/the-picard-functor-and-the-picard-scheme-of-a-curve.md#8-three-examples-of-the-comparison). Pullback by relative Frobenius on those Picard schemes gives \(v:E^{(p)}\to E\). On a divisor \(F(P)-F(O)\), pullback is \(p(P-O)\); equality on geometric points of these reduced curves gives \(vF=[p]\), so 8.4 identifies \(v=V\).

The tangent of that Picard functor is \(H^1(\mathcal O)\), proved with transition functions \(1+\epsilon a_{ij}\) in [The structure of the Picard scheme, Section 2](../../AG-HP/src/the-structure-of-the-picard-scheme.md#2-the-square-zero-sequence-and-the-tangent-space). Pullback of those transitions proves directly that \(dV\) is relative-Frobenius pullback on \(H^1(\mathcal O)\); its vanishing is the vanishing just calculated. If it is nonzero, 6.8 makes the degree-\(p\) isogeny \(V\) étale, so its kernel has \(p\) geometric points. If it is zero, the function-field extension of a degree-\(p\) map cannot be separable (its generic differential would then be invertible), hence is purely inseparable and 6.8 makes it radicial. Its kernel then has one point. Since \(F\) is bijective on geometric points and \([p]=VF\), these are precisely the two geometric point counts of \(E[p]\). \(\square\)

**Proposition 9.10 (proved realization cases).** For every prime \(p\) there are ordinary and supersingular elliptic curves over \(\overline{\mathbf F}_p\). There is an ordinary elliptic curve over \(\mathbf F_p\). There is also a supersingular elliptic curve over \(\mathbf F_p\) whenever \(p=2,3\), \(p\equiv3\pmod4\), or \(p\equiv2\pmod3\). Over any field containing both such curves, every pair \(0\le f\le g\) is realized by an abelian variety of dimension \(g\) and \(p\)-rank \(f\).

**Proof.** For odd \(p\) consider the smooth Legendre cubic \(y^2=x(x-1)(x-\lambda)\), with \(\lambda\ne0,1\). Its coefficient in 9.9 is

\[
(-1)^h H_p(\lambda),
\qquad H_p(T)=\sum_{i=0}^{h}\binom hi^2T^i.
\tag{R.2}
\]

This follows by expanding \((x-1)^h(x-\lambda)^h\) and taking its \(x^h\)-coefficient. The polynomial has degree \(h>0\), leading coefficient one, \(H_p(0)=1\), and

\[
H_p(1)=\binom{2h}{h}=\binom{p-1}{h}=(-1)^h\ne0.
\]

The middle equality follows by comparing the \(T^h\)-coefficient in \((1+T)^h(1+T)^h\). Thus it has a root away from zero and one over an algebraic closure, giving a supersingular elliptic curve. A nonroot away from those two points gives an ordinary curve there. For \(p\ge5\), there are \(p-2>h\) allowed elements of \(\mathbf F_p\), so at least one is a nonroot; this supplies an ordinary curve already over the prime field.

For \(p=3\), the curves \(y^2=x^3+x^2+1\) and \(y^2=x^3-x\) are smooth and have respectively rank one and zero by 9.5. For \(p=2\), use \(y^2+xy=x^3+1\) and \(y^2+y=x^3\); smoothness follows from their partial derivatives, and 9.4 gives the two ranks.

For \(p\ge5\) with \(p\equiv3\pmod4\), take \(y^2=x^3-x\). Its coefficient in 9.9 is the \(x^{2h}\)-coefficient of \(x^h(x^2-1)^h\), which is zero because \(h\) is odd. If \(p\equiv2\pmod3\), take \(y^2=x^3-1\). Its powers have only exponents divisible by three, whereas \(p-1\) is not divisible by three, so that coefficient is zero. Both cubics are smooth in the indicated characteristics.

If \(E_0,E_1\) over the chosen field have ranks zero and one, put \(A=E_1^f\times E_0^{g-f}\), with the zero-dimensional product the point. Products preserve properness and geometric integrality and add dimensions. Their schematic \(p\)-torsion is the product, so their geometric point counts multiply and their ranks add. Thus \(\dim A=g\) and its \(p\)-rank is \(f\). Field-extension invariance is already proved in 6.10. \(\square\)

### Prime-field supersingular curves and every geometric p-rank

The following proof supplies the prime-field case left open by Proposition9.10. Its scalar analytic inputs are the proved [Cauchy, power-series and maximum-modulus results](../../foundations-of-von-neumann-algebras/src/cauchy-s-theorem-for-cycles-and-its-consequences.md#OA-FND-CT-02), Lemma0.1 and Theorems2.1–2.3,3.1–3.7. Only their scalar statements are used.

Here are the residue and strict-maximum consequences used below. If a meromorphic function has finitely many poles inside a polygon and no poles on its boundary, remove small disjoint squares around them. Triangulate the remaining polygonal region into triangles avoiding the poles. Cauchy's theorem on the triangles cancels all internal edges. At a pole expand its Laurent series, obtained from its local power-series factorization and the inverse series of its nonvanishing unit. Integrating each monomial around its small square gives zero except the exponent \(-1\), whose integral is \(2\pi i\) by the index calculation. Thus the outer integral is \(2\pi i\) times the sum of residues. For \(f'/f\), local factorization \(f=(z-a)^m u\), with \(u(a)\ne0\), makes that residue \(m\), negative at a pole; this proves the argument principle used on a fundamental parallelogram. A slight polygonal perturbation avoids its finitely many boundary zeros and poles.

Finally an interior maximum of \(|f|\) forces local constancy. Cauchy's mean-value formula on a small circle makes its average equal to the central value. Equality in the triangle inequality, with every modulus bounded by the central modulus, forces every value on that circle to equal the central value. Its nonconstant Taylor coefficients are therefore zero by the same integral formula. The identity theorem extends this constancy on a connected domain. This applies in an ordinary chart or a finite-rotation quotient chart of the compact modular domain. These are the precise analytic consequences used in the next proofs.

#### Lattices, cubic coordinates, and a modular function

**Lemma 9.14 (the needed lattice construction).** For a lattice \(\Lambda\subset\mathbf C\), there is a smooth pointed plane cubic whose analytic space is \(\mathbf C/\Lambda\). A linear map \(z\mapsto az\) with \(a\Lambda\subset\Lambda\) gives an algebraic endomorphism of that cubic, with differential \(a\), degree \([\Lambda:a\Lambda]\), and composition corresponding to multiplication of the scalars. For \(\Lambda_\tau=\mathbf Z+\mathbf Z\tau\), \(\operatorname{Im}\tau>0\), its invariant is the holomorphic modular function

\[
j(\tau)=\frac{E_4(\tau)^3}{\Delta(\tau)},\qquad
\Delta=\frac{E_4^3-E_6^2}{1728},
\tag{S.1}
\]

where, for \(q=e^{2\pi i\tau}\),

\[
E_4=1+240\sum_{n\ge1}\sigma_3(n)q^n,\qquad
E_6=1-504\sum_{n\ge1}\sigma_5(n)q^n.
\tag{S.2}
\]

In particular \(j\in q^{-1}+\mathbf Z[1/6][[q]]\), with a convergent expansion near the cusp.

**Proof.** Define

\[
\begin{aligned}
\wp(z)={}&z^{-2}\\
&+\sum_{\lambda\in\Lambda\setminus\{0\}}
\big((z-\lambda)^{-2}-\lambda^{-2}\big),\\
G_r={}&\sum_{\lambda\ne0}\lambda^{-r}
\quad(r\ge4\text{ even}).
\end{aligned}
\]

The number of lattice points in an annulus of integral radius is \(O(n)\). Hence \(\sum|\lambda|^{-r}\) converges for \(r>2\); on a fixed bounded set the subtracted summand in \(\wp\) is \(O(|\lambda|^{-3})\). The series and its derivatives converge normally away from lattice points. The lattice sums also converge normally as \(\tau\) varies on a compact subset of the upper half-plane: the real-linear map \((m,n)\mapsto m\tau+n\) has smallest singular value bounded below by a positive constant on that compact set. Pairing opposite lattice points makes \(\wp\) even. Reindexing its absolutely convergent derivative makes \(\wp'\) periodic. Therefore \(\wp(z+\omega)-\wp(z)\) is constant for a basis period \(\omega\); evaluating at \(-\omega/2\) and using evenness makes that constant zero. Thus \(\wp\) is periodic too.

Its Laurent expansion at zero is

\[
\wp=z^{-2}+3G_4z^2+5G_6z^4+O(z^6).
\]

Set \(g_2=60G_4\), \(g_3=140G_6\). The elliptic function
\(\wp'^2-4\wp^3+g_2\wp+g_3\) has no pole, by this expansion. A holomorphic periodic function is bounded on a fundamental parallelogram and hence constant by Liouville's theorem; its constant term here is zero. Consequently

\[
\wp'^2=4\wp^3-g_2\wp-g_3.
\tag{S.3}
\]

For a nonzero meromorphic periodic function, the argument principle on a slightly translated fundamental parallelogram says that the numbers of zeros and poles agree: opposite boundary integrals of its logarithmic derivative cancel. The function \(\wp'\) has one triple pole on the torus, and vanishes at its three distinct nonzero half-periods, by oddness and periodicity. These are therefore its only zeros, all simple. Their three \(\wp\)-values are distinct, since otherwise \(\wp-e\), with its single double pole, would have two zeros each of order at least two. These values are the roots of \(4X^3-g_2X-g_3\). The roots are distinct, so
\(g_2^3-27g_3^2\ne0\).

Equation (S.3) gives the map to the smooth cubic
\(y^2=4x^3-g_2x-g_3\). At zero its local projective parameter \(-2x/y\) equals \(z+O(z^5)\), so it extends to the point at infinity. The zeros-and-poles calculation makes \(\wp\) a degree-two map to \(\mathbf P^1\): its two inverse points are \(z\) and \(-z\), with the usual multiplicity at half-periods. The value of \(\wp'\) distinguishes these points away from them. Thus the map to the cubic is bijective. It has nonzero derivative: away from zeros of \(\wp'\) use \(x\); at such a zero use \(y\), since the zero is simple; at infinity use \(-2x/y\). It is therefore a biholomorphism.

An even meromorphic function on the torus factors meromorphically through \(\wp\). At a half-period a local parameter is negated by \(z\mapsto-z\), and an even Laurent series is a series in its square, so there is no failure of meromorphic descent at a branch point. A meromorphic function on \(\mathbf P^1\) is rational: subtract its finitely many finite principal parts and its polynomial principal part at infinity, then use Liouville. Dividing an odd function by \(\wp'\) makes it even. Every meromorphic function on the torus is consequently of the form
\(R(\wp)+\wp'S(\wp)\), with rational \(R,S\). The functions \(\wp(az)\) and \(\wp'(az)\) are periodic when \(a\Lambda\subset\Lambda\); thus the induced pointed map is algebraic. Corollary 2.3 makes it a group homomorphism. Its derivative is \(a\), and its analytic fibres have \([\Lambda:a\Lambda]\) points, without ramification when \(a\ne0\), proving the degree assertion.

The cubic law agrees with addition of torus parameters. Indeed its pullback is a holomorphic group law on the torus. Lift it locally to the complex plane on \(\mathbf C^2\); the two derivatives are single-valued entire functions, periodic in both variables. Boundedness on the product of two parallelograms and Liouville in each variable make them constant. The identity conditions make both constants one and the additive constant zero modulo \(\Lambda\). This proves the assertion globally. In particular \(z\mapsto nz\) is the algebraic map \([n]\).

Scaling the lattice scales \(g_2,g_3\) with weights \(-4,-6\). The cubic invariant
\(1728g_2^3/(g_2^3-27g_3^2)\) is therefore unchanged by homothety, and is holomorphic in \(\tau\) because the denominator never vanishes. Changing an oriented integral basis of \(\Lambda_\tau\) gives \(\Lambda_{\gamma\tau}=(c\tau+d)^{-1}\Lambda_\tau\), so the function is invariant under \(\mathrm{SL}_2(\mathbf Z)\).

Here are the Fourier calculations, to include the local-integrality input. The cotangent partial fraction identity

\[
\pi\cot\pi z=z^{-1}+\sum_{n\ge1}\frac{2z}{z^2-n^2}
\]

follows by integrating \(\pi\cot\pi w/(w^2-z^2)\) on squares with vertical sides at half-integers and horizontal sides of height tending to infinity. Cotangent is uniformly bounded on those boundaries, while the denominator has quadratic growth; the boundary integral tends to zero and the residues give the identity. Comparing its Laurent coefficients with the Taylor series of sine and cosine gives \(\zeta(4)=\pi^4/90\), \(\zeta(6)=\pi^6/945\). On the upper half-plane the geometric-series identity is
\(\pi\cot\pi z=-\pi i(1+2\sum_{r\ge1}e^{2\pi irz})\).
Differentiating \(k-1\) times gives, for even \(k\ge4\),

\[
\sum_{n\in\mathbf Z}(z+n)^{-k}
=\frac{(2\pi i)^k}{(k-1)!}\sum_{r\ge1}r^{k-1}e^{2\pi irz}.
\]

Split the lattice sum into its \(m=0\) terms and its pairs with \(m>0\). The latter double this identity with \(z=m\tau\). Regrouping the absolutely convergent double series by \(n=mr\) gives
\(G_4=(\pi^4/45)E_4\) and \(G_6=(2\pi^6/945)E_6\), with (S.2). Thus

\[
g_2^3-27g_3^2=\frac{64\pi^{12}}{27}(E_4^3-E_6^2),
\]

which proves (S.1). The coefficient of \(q\) in (E_4^3-E_6^2) is \(720+1008=1728\). Accordingly \(\Delta=q(1+q\mathbf Z[1/6][[q]])\), and inversion proves the claimed convergent expansion of \(j\). Full integrality at 2 and 3 is unnecessary here. \(\square\)

#### The one modular-polynomial argument we need

**Lemma 9.15 (algebraicity and p-integrality at the chosen lattice).** Let \(p\ge5\) be prime and \(\tau=i\sqrt p\). Then \(j(\tau)\) is algebraic and integral over \(\mathbf Z[1/6]\).

**Proof.** First an invariant holomorphic function on the upper half-plane with a finite-order pole at the cusp is a polynomial in \(j\). Its convergent Laurent expansion has finitely many negative powers. Since \(j=q^{-1}+O(1)\), subtract multiples of successive powers of \(j\) to remove them. The remaining invariant function is holomorphic at the cusp and is constant. To justify the last assertion, every orbit has a representative in

\[
\{\tau:|\operatorname{Re}\tau|\le1/2,\ |\tau|\ge1\}.
\]

One obtains it by maximizing \(\operatorname{Im}(\gamma\tau)=\operatorname{Im}\tau/|c\tau+d|^2\) over primitive integer pairs ((c,d)), whose denominators form a discrete set with only finitely many bounded values, and then translating the real part. Maximality prevents \(|\tau|<1\), because inversion would increase the imaginary part. The truncated region is compact; the portion at large height is compactified by the disk coordinate \(q\). Side identifications give a compact quotient. At a finite stabilizer its holomorphic invariant functions have convergent series in a local quotient coordinate: linearize the finite cyclic stabilizer by averaging a local parameter, then take its order-th power. Thus the bounded function attains a maximum in a holomorphic chart of this compact connected quotient and is constant by the maximum principle.

The index-\(p\) sublattices of \(\Lambda_\tau\) are precisely

\[
\mathbf Z+\mathbf Zp\tau,\qquad
p\mathbf Z+\mathbf Z(\tau+a)\quad(0\le a<p).
\]

Indeed reduction modulo \(p\Lambda_\tau\) identifies them with the (p+1) lines in \(\mathbf F_p^2\). Form

\[
\big(Y-j(p\tau)\big)\prod_{a=0}^{p-1}
\big(Y-j((\tau+a)/p)\big).
\tag{S.4}
\]

Changing a basis permutes these sublattices, so each coefficient is invariant. It is holomorphic in \(\tau\) and has a finite-order pole at the cusp: use the expansions in (q^{1/p}) of its finitely many factors. By the preceding argument there is a polynomial \(\Phi_p(X,Y)\in\mathbf C[X,Y]\) for which (S.4) equals \(\Phi_p(j(\tau),Y)\).

In fact its coefficients lie in \(\mathbf Z[1/6]\). Each coefficient of the product expansion belongs to \(\mathbf Z[1/6,\zeta_p]\); a cyclotomic automorphism \(\zeta_p\mapsto\zeta_p^u\) permutes the indices \(a\) and fixes it. These are all \(p-1\) automorphisms: the polynomial \(1+T+\cdots+T^{p-1}\) is irreducible because its translate by 1 is Eisenstein at \(p\), and its roots are precisely the primitive \(p\)-th roots. An invariant coefficient is rational by averaging its expression in powers of \(\zeta_p\): the sum of \(\zeta_p^{um}\) over \(1\le u<p\) is \(p-1\) if \(p\mid m\) and \(-1\) otherwise. It is also integral over \(\mathbf Z[1/6]\); a rational number integral over that ring has no prime in its denominator other than 2 or 3, by clearing a monic equation and comparing valuations. Thus they belong to \(\mathbf Z[1/6]\). Translation \(\tau\mapsto\tau+1\) permutes the factors as well; its invariance eliminates fractional powers of \(q\). Subtracting the successive leading powers of \(j\) in the polynomial construction preserves \(\mathbf Z[1/6]\) at each step. The constant remainder lies in that ring too. This proves the assertion about \(\Phi_p\).

Put \(D_p(X)=\Phi_p(X,X)\). As \(\operatorname{Im}\tau\to\infty\), its first factor is asymptotic to \(-q^{-p}\), and each of the other \(p\) factors is asymptotic to \(q^{-1}\), since \(p>1\). Hence

\[
D_p(j(\tau))\sim-q^{-2p}.
\]

As \(j(\tau)\sim q^{-1}\), the nonzero polynomial \(D_p\) has degree \(2p\) and leading coefficient \(-1\). Finally, at \(\tau=i\sqrt p\) we have \(\tau/p=-1/\tau\), and invariance under inversion gives \(j(\tau/p)=j(\tau)\). The factor \(a=0\) in (S.4) vanishes on the diagonal. Thus \(j(\tau)\) is a root of the monic polynomial \(-D_p\in\mathbf Z[1/6][X]\), proving both claims. No class-field or class-polynomial theorem is involved. \(\square\)

#### Algebraic descent of the specific endomorphism

For characteristic different from 2 and 3, the pointed short cubic
\(y^2=x^3+Ax+B\) has

\[
j=1728\frac{4A^3}{4A^3+27B^2}.
\tag{S.5}
\]

Two such smooth cubics over an algebraically closed field have the same invariant exactly when they are pointed-isomorphic. If \(AB A'B'\ne0\), equality gives \(r^3=s^2\), with \(r=A'/A\), \(s=B'/B\). Choose \(u\) with \(u^2=s/r\); then \(u^4=r\), \(u^6=s\), and scaling coordinates gives the isomorphism. When \(A=0\) or \(B=0\), use a sixth or fourth root respectively. Conversely these scalings preserve (S.5).

**Lemma 9.16 (a number-field endomorphism).** For \(p\ge5\) there are an elliptic curve \(E\) over a number field \(L\) and an endomorphism \(\alpha\) over \(L\) such that

\[
j(E)=j(i\sqrt p),\qquad
\alpha^2=[-p],\qquad
\deg\alpha=p,
\tag{S.6}
\]

and \(\alpha^*\omega=\sqrt{-p}\,\omega\) for every invariant differential after choosing the embedding \(L\hookrightarrow\mathbf C\) used in the construction.

**Proof.** The lattice \(\mathbf Z+\mathbf Z\sqrt{-p}\) is preserved by multiplication by \(\sqrt{-p}\). Its matrix in this basis is
\(\left(\begin{smallmatrix}0&-p\\1&0\end{smallmatrix}\right)\), of determinant \(p\). Lemma 9.14 gives the corresponding algebraic endomorphism over \(\mathbf C\), with the degree, differential and square in (S.6).

Lemma 9.15 makes its invariant \(J\) algebraic. There is a smooth short cubic over \(\overline{\mathbf Q}\) with that invariant: for \(J\ne0,1728\) use

\[
A=-\frac{3J}{J-1728},\qquad B=-\frac{2J}{J-1728};
\tag{S.7}
\]

for \(J=0\) use \(A=0,B=1\), and for \(J=1728\) use \(A=1,B=0\). The calculation (S.5) checks each case. It is pointed-isomorphic over \(\mathbf C\) to the lattice cubic. Transport \(\alpha\) to it.

We prove that this transported map is defined over \(\overline{\mathbf Q}\). Its kernel \(H\) is contained in \(E[p]\), because \(\alpha^2=[-p]\). The latter is finite étale over \(\overline{\mathbf Q}\), by Theorems 6.1 and 6.3. All its complex points are algebraic: their coordinates belong to finite algebras over the algebraically closed field \(\overline{\mathbf Q}\). Thus \(H\) is a subgroup defined over \(\overline{\mathbf Q}\).

For any \(\sigma\in\operatorname{Aut}(\mathbf C/\overline{\mathbf Q})\), the maps \(\alpha\) and \(\alpha^\sigma\) have the same kernel and degree. The quotient universal property of Theorem 6.6 gives
\(\alpha^\sigma=b_\sigma\alpha\) for a pointed automorphism \(b_\sigma\) of \(E\). Both differentials are \(\sqrt{-p}\), which is fixed by \(\sigma\); hence \(db_\sigma=1\).

A pointed automorphism of a smooth short cubic in characteristic zero is a scaling \(x\mapsto u^2x\), \(y\mapsto u^3y\). Here is the coordinate justification. The functions with poles only at \(O\) are the polynomial coordinate ring of its affine complement. Using the cubic equation, write them uniquely as \(a(x)+yb(x)\). The pole orders of \(x,y\) are 2 and 3; the leading orders in these two summands have different parity. It follows that the spaces with pole bound 2 and 3 have respective bases \(1,x\) and \(1,x,y\). An automorphism must therefore send \(x\) to \(u^2x+r\) and \(y\) to \(u^3y+sx+t\); comparing the cubic equation first eliminates the terms involving \(y\), then its (x^2) term eliminates \(r\). Its differential is \(u^{-1}\), so differential one forces the identity. Consequently \(\alpha^\sigma=\alpha\) for every \(\sigma\).

The fixed field of all these automorphisms is \(\overline{\mathbf Q}\): a transcendental element can be included in a transcendence basis, moved in its rational function field, and the resulting isomorphism extended to algebraic closures. The last extension follows by successively adjoining a root of the transported minimal polynomial, or by Zorn's lemma. In unique rational expressions for the pullbacks of \(x,y\), use the basis \(1,y\) over \(\mathbf C(x)\) and monic polynomial denominators. Invariance makes every coefficient fixed, hence algebraic. Only finitely many coefficients occur. They, the equation coefficients and \(\sqrt{-p}\) belong to one number field \(L\). All identities in (S.6) are already identities of rational maps and so hold over \(L\). \(\square\)

#### Good models and extension, with the local arguments included

**Lemma 9.17 (a place and a smooth model).** The curve and endomorphism in 9.16 can be defined over a number field \(L\) with a discrete valuation ring \(R\subset L\), of residue characteristic \(p\), such that \(E\) has a smooth projective plane-cubic model \(\mathcal E/R\) with its origin section.

**Proof.** We first recall explicitly why such a place is available. In a number field \(L\), choose an integral rational basis \(\beta_i\). The ring \(\mathcal O_L\) of algebraic integers is contained in the trace-dual lattice of \(\sum\mathbf Z\beta_i\): for \(x\in\mathcal O_L\), each \(\operatorname{Tr}(x\beta_i)\) is an integer. The trace pairing is nondegenerate in characteristic zero, so this dual is a finite-rank lattice. Hence \(\mathcal O_L\) is finite over \(\mathbf Z\) and Noetherian. It is integrally closed, by transitivity of integrality. The trace assertions follow by embedding \(L\) into a splitting field: the trace is a sum of conjugates, is an algebraic integer, and is rational; a rational algebraic integer is an integer. Nondegeneracy follows, for example, from the invertible Vandermonde matrix on the distinct roots of a primitive element's separable minimal polynomial.

The ideal \(p\mathcal O_L\) is proper, since \(1/p\) is not integral. Choose a maximal ideal \(\mathfrak p\) containing it. Every nonzero prime of \(\mathcal O_L\) is maximal: for nonzero \(x\) in it, the nonzero constant term of the monic characteristic polynomial of multiplication by \(x\) is an integer in \(x\mathcal O_L\); the quotient by that integer is finite. Thus \(R=(\mathcal O_L)_{\mathfrak p}\) is a normal Noetherian local domain of dimension one.

For completeness, such a ring is a DVR. Choose \(0\ne a\in\mathfrak m\). Since \(\sqrt{(a)}=\mathfrak m\), finite generation gives \(\mathfrak m^n\subset(a)\). With \(n\) least, choose \(b\in\mathfrak m^{n-1}\setminus(a)\); then \(z=b/a\notin R\) but \(z\mathfrak m\subset R\). If \(z\mathfrak m\subset\mathfrak m\), write multiplication by \(z\) on a finite generating list of \(\mathfrak m\) as a matrix with entries in \(R\). Its monic characteristic polynomial annihilates each generator, by the adjugate identity. A nonzero generator and cancellation in the fraction field make this polynomial vanish at \(z\), proving integrality over \(R\), a contradiction. Therefore \(z\mathfrak m=R\) and \(\mathfrak m\) is principal, say generated by \(\varpi\). A nonzero element cannot be divisible by all powers of \(\varpi\): the ascending principal ideals generated by its successive quotients would stabilize by Noetherianity and make \(\varpi\) a unit. Thus every nonzero element is a unit times a unique power of \(\varpi\), proving the DVR assertion.

The invariant \(J\) is integral over \(\mathbf Z[1/6]\) by 9.15, hence belongs to \(R\) for any such place with \(p\ge5\). Choose a root \(\lambda\) of

\[
256(T^2-T+1)^3-JT^2(1-T)^2=0.
\tag{S.8}
\]

After a finite extension of \(L\), include this root and retain a place above \(p\). The polynomial has leading coefficient 256, a unit of the new valuation ring, so \(\lambda\) is integral there. Reduction of (S.8) excludes both \(\bar\lambda=0\) and \(\bar\lambda=1\). Therefore

\[
\mathcal E:\quad y^2=x(x-1)(x-\lambda)
\tag{S.9}
\]

is a smooth projective cubic over that ring: its three finite roots stay distinct and \(2\) is a unit, while the partial derivative at its point at infinity is a unit. To compute its invariant, shift \(x\) by \((1+\lambda)/3\). Its short-cubic coefficient is \(A=-(\lambda^2-\lambda+1)/3\), and direct substitution gives \(4A^3+27B^2=-\lambda^2(1-\lambda)^2\). Formula (S.5) consequently gives

\[
j=\frac{256(\lambda^2-\lambda+1)^3}{\lambda^2(1-\lambda)^2}=J.
\]

Thus its generic fibre is geometrically pointed-isomorphic to the curve in 9.16. Such an isomorphism uses finitely many algebraic coefficients; extend \(L\) once more to include them and transport \(\alpha\). This proves the assertion. The elementary valuation argument also proves integrality of \(\lambda\): if its valuation were negative, the leading term of its monic equation would have strictly smaller valuation than every other term and could not cancel. \(\square\)

We need the group law over this DVR, not just on its fibres. The construction in Theorem 9.0 works relatively as follows. On \(\mathcal E\times_R\mathcal E\), the minors of the two universal coordinate vectors generate the ideal of the diagonal. The diagonal of a smooth relative curve is Cartier. Dividing the minors by its local equation gives a secant-or-tangent line everywhere. On the pulled-back curve this line cuts a divisor of fibre degree three. Remove the two universal graph divisors: near their intersection smooth parameters give equations \(t-u,t-v\), a regular sequence, so vanishing on both implies divisibility by their product. The residual divisor has length one on every fibre. At such a simple residual zero its derivative in a curve parameter is a unit, so it is étale over the parameter base, with one-point geometric fibres; it is consequently the graph of a section. Reflecting that residual point by the line through the origin constructs addition and inverse as morphisms over \(R\). Their group identities hold on the generic fibre by Theorem 9.0, and hence everywhere: the powers of the smooth flat model are flat over the domain \(R\), and equality to a separated target on the generic fibre kills the defining equalizer ideal, since it is \(R\)-torsion. This supplies the smooth proper group scheme \(\mathcal E/R\) needed below.

**Lemma 9.18 (extension over a good model).** If \(\mathcal E/R\) is (S.9) and \(K=\operatorname{Frac}R\), every homomorphism \(u:E_K\to E_K\) extends uniquely to a homomorphism \(\mathcal E\to\mathcal E\).

**Proof.** We give the translation argument, including the enlargement used to find sections. First pass to the completion \(\widehat R\). Its uniformizer remains \(\varpi\), and every nonzero completed element has a first nonzero \(\varpi\)-adic digit, so \(\widehat R\) is a DVR. Write the finite residue field as \(\mathbf F_q\). Construct a tower \(R_1=\widehat R\subset R_2\subset\cdots\) of complete DVRs with the same uniformizer and residue fields \(\mathbf F_{q^{n!}}\): at step \(n\), lift a monic irreducible polynomial of degree \(n+1\) over the residue field and adjoin a root. Its quotient ring is finite free and complete, its reduction is a field, and its maximal ideal is generated by \(\varpi\). The polynomial is irreducible over the fraction field: coefficients of any monic factors would be integral as symmetric expressions in its integral roots and hence would belong to the normal DVR, contradicting irreducibility of the reduction. Thus the quotient is a domain and is a DVR by division by \(\varpi\); its derivative is a unit because finite fields are perfect. Choosing roots in an algebraic closure gives the stated inclusions. Put \(R'=\bigcup_nR_n\). It is a DVR: all nonzero elements have integral valuations and every nonzero ideal contains an element with least valuation. Its residue field is \(\overline{\mathbf F}_q\), since every finite extension degree divides some \(n!\). It is henselian, since the coefficients of a polynomial and an initial residue root belong to some finite stage, where the usual Newton iteration lifts a simple root in the complete DVR. In that iteration \(a_{n+1}=a_n-f(a_n)/f'(a_n)\) and the error valuation at least doubles, proving convergence and the root assertion. Completion and these extensions are faithfully flat over \(R\): they are torsion-free modules over a PID, hence flat (each finite subset lies in a free finite submodule, and filtered unions preserve exactness); the maps are local and their residue fields are nonzero, so flatness is faithful. Their completion inclusion is injective by the ascending-ideal argument in 9.17.

The homomorphism on the generic fibre defines a rational map on \(\mathcal E_{R'}\). At the generic point \(\eta_s\) of its special fibre, the local ring is a DVR with uniformizer \(\varpi\): the fibre is integral and smooth, and its generic-point local ring modulo \(\varpi\) is a field. Properness of the projective target extends the rational map to this local ring. This instance of the valuative criterion is elementary: scale the three homogeneous coordinates so they are integral and one is a unit; the homogeneous cubic equation continues to hold. The extension spreads to an open neighbourhood by clearing finitely many denominators in an affine target chart. Consequently the map is defined on an open \(U\) containing its entire generic fibre and a dense open of its special fibre. The omitted special-fibre points form a finite set.

For any special point \(x\), choose a residue point \(a\) with both \(a\in U_s\) and \(x-a\in U_s\). This is possible because the algebraically closed residue field is infinite, the smooth cubic has infinitely many points, and the forbidden sets are finite. The point \(a\) lifts to a section \(\widetilde a\) over \(R'\). On the affine chart of (S.9), one of its two equation derivatives is nonzero; lift the other coordinate arbitrarily and use the preceding simple-root Hensel calculation. At infinity use its origin section. Since the special value is in \(U\), the section lies wholly in \(U\); an open subset of the spectrum of a DVR containing its closed point contains its generic point as well.

On the translate \(U+\widetilde a\), define

\[
v(z)=u(z-\widetilde a)+u(\widetilde a).
\tag{S.10}
\]

This is a morphism and agrees generically with \(u\), because the latter is a homomorphism. The translate contains \(x\). These translates and \(U\) cover the model, and their maps glue: on overlaps they agree on the generic fibre, so separatedness and flatness give equality as above. The addition identity and origin identity likewise extend from the generic fibre, proving the homomorphism assertion over \(R'\).

Uniqueness follows from that same argument. The two pullbacks of the extension to \(R'\otimes_R R'\) consequently agree: the base-changed model is flat over \(R\), and they agree after inverting \(\varpi\). To descend this particular projective-target morphism, pull back \(\mathcal O_{\mathbf P^2}(1)\) and its three coordinate sections. Equality of the two maps supplies the canonical descent datum on that line bundle and those sections. On affine source charts, the module-descent lemma and affine-descent corollary in the opening section of *Quotients and torsors* descend the module and sections; the descended module is invertible because that can be checked faithfully flat locally. They glue on chart overlaps by uniqueness. Generation by the three sections and the homogeneous cubic equation can also be checked after faithful scalar extension. Thus they define the descended morphism to \(\mathcal E\). No extension theorem for good reduction or complex multiplication is being assumed. \(\square\)

#### Radicial reduction, prime-field descent, and the full realization theorem

**Theorem 9.19 (supersingular curves over the prime field).** For every prime \(p\equiv1\pmod {12}\) there is a supersingular elliptic curve over \(\mathbf F_p\).

**Proof.** Such a prime is at least 13. Apply 9.16–9.18 to obtain a smooth model and an extended endomorphism \(\alpha\). Its square is \([-p]\) on the model, since this holds generically and the model is flat with separated target. Let \(E_s\) and \(\beta\) be the special fibre and the reduced endomorphism. Then

\[
\beta^2=[-p]_{E_s}.
\tag{S.11}
\]

The pullback of a generator of the invariant differentials is multiplication by an element \(a\in R\). On the generic fibre it is \(\sqrt{-p}\), by 9.16; hence \(a^2=-p\). It reduces to zero. Thus \(d\beta=0\) at the origin and, by translation, everywhere.

The map \(\beta\) cannot be constant, since its square is the nonconstant multiplication map \([-p]\). It is therefore a finite surjective map of smooth projective curves: its proper fibres are finite, and proper quasi-finite morphisms are finite. Its degree satisfies

\[
(\deg\beta)^2=\deg[-p]=p^2
\]

by Theorem 6.1, so \(\deg\beta=p\). A degree-\(p\) function-field extension with zero differential is inseparable and hence purely inseparable. Theorem 6.8 makes \(\beta\) radicial. Equivalently apply Lemma 8.3 to factor it as

\[
E_s\xrightarrow{F_{E_s/k_s}}E_s^{(p)}
\xrightarrow{b}E_s.
\tag{S.12}
\]

Frobenius has degree \(p\) by Theorem 8.2; hence \(b\) has degree one. A finite degree-one map between smooth curves is an isomorphism: its coordinate inclusions are integral and birational, and the normal target is integrally closed. This also proves radiciality directly. Equation (S.11) now makes \([p]\) radicial, so its geometric kernel has only the origin. The special fibre has geometric \(p\)-rank zero.

The isomorphism \(E_s^{(p)}\simeq E_s\) in (S.12) forces

\[
j(E_s)^p=j(E_s).
\tag{S.13}
\]

Indeed the \(j\)-formula commutes with Frobenius twisting. The roots of \(T^p-T\) in any characteristic-\(p\) field are exactly the elements of its prime field: all \(p\) prime-field elements are roots and the polynomial has degree \(p\). Thus \(j_0=j(E_s)\) belongs to \(\mathbf F_p\), even though the intermediate residue field \(k_s\) may be larger.

Use (S.7) with \(J=j_0\) to write a smooth cubic over \(\mathbf F_p\); use \(y^2=x^3+1\) at \(j_0=0\), or \(y^2=x^3+x\) at \(j_0=1728\). Formula (S.5) shows that its invariant is \(j_0\). It becomes pointed-isomorphic to \(E_s\) over an algebraic closure, by the coordinate proof preceding 9.16. The finite torsion schemes then have the same geometric points, so this **prime-field** cubic is supersingular. The explicit equations are used for descent of the curve; we make no claim that the intermediate endomorphism itself descends to \(\mathbf F_p\). \(\square\)

**Theorem 9.20 (every dimension and p-rank over every characteristic-p field).** Let \(k\) be any field of characteristic \(p>0\), including an imperfect field. For each pair of integers \(0\le f\le g\) there is an abelian variety over \(k\) of dimension \(g\) and geometric \(p\)-rank \(f\).

**Proof.** Proposition 9.10 gives an ordinary elliptic curve \(E_1\) over every prime field. It gives a supersingular curve \(E_0\) over the prime field for \(p=2,3\), for \(p\equiv3\pmod4\), and for \(p\equiv2\pmod3\). Every prime \(p\ge5\) is congruent to 1, 5, 7 or 11 modulo 12; 9.19 supplies precisely the remaining class 1. Thus both curves are available over \(\mathbf F_p\) for every prime.

Base-change them along the canonical inclusion \(\mathbf F_p\hookrightarrow k\) and set

\[
A=(E_1)_k^{\,f}\times_k(E_0)_k^{\,g-f}.
\tag{S.14}
\]

For \(g=0\) take \(\operatorname{Spec}k\). Products of proper geometrically integral groups are proper geometrically integral groups, and dimensions add, so \(A\) is an abelian variety of dimension \(g\). On an algebraic closure the schematic kernel of multiplication by \(p\) is the product of the kernels in the factors. The ordinary factors have \(p\) geometric points and the supersingular factors one. Hence \(\#A[p](\overline k)=p^f\), which is exactly geometric \(p\)-rank \(f\). Field-extension invariance is also Theorem 6.10 of the current lesson. There is no rational-point or perfect-field requirement in this calculation. This proves source (5.25)(ii) with its full ground-field quantifier. \(\square\)

#### Comparison, scope and source credit

The source statement is Edixhoven–van der Geer–Moonen, *Abelian Varieties*, Chapter V, remark (5.25)(ii), in the preliminary edition with 8 February 2012 footers. The coefficient and other prime-field arguments of the preceding supplement remain useful and unchanged.

The analytic ingredients, the lattice construction and the endomorphisms of complex elliptic curves, are treated in J. S. Milne, [*Elliptic Curves*](https://www.jmilne.org/math/Books/EC2.pdf), second edition, Chapter III, §§2–3. The modular polynomial is treated in Don Zagier, [*Elliptic Modular Forms and Their Applications*](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/978-3-540-74119-0_1/fulltext.pdf), §6.1, equations (77)–(79) and Proposition 24. Here we prove only the needed prime-degree diagonal polynomial and use \(\mathbf Z[1/6]\), which suffices for the remaining primes. The number-field, good-model and extension arguments are written out, rather than importing class fields, a CM reduction classification, Tate's theorem, quaternionic classification or a global existence theorem. The theorem of Honda and Tate gives another route to these existence results; see Kirsten Eisenträger's notes [*The theorem of Honda and Tate*](https://math.stanford.edu/~conrad/vigregroup/vigre04/hondatate.pdf). The proof above does not use it.

No source prose, source figures or distinctive lesson organization is reproduced. These are proofs of established results, not a claim of new mathematical research.

### The sharp curve example and a two-factor warning

**Lemma 9.11. The curve Riemann–Roch and duality inputs.** A smooth proper geometrically integral curve \(C/k\) is projective. Put \(g_C=h^1(C,\mathcal O_C)\). For every line bundle \(M\),
\[
\begin{gathered}
\chi(C,M)=\deg M+1-g_C,\\
H^1(C,M)^\vee\simeq H^0(C,\Omega^1_{C/k}\otimes M^{-1}),
\end{gathered}
\]
and \(\deg\Omega^1_{C/k}=2g_C-2\).

**Proof.** Proper coherent cohomology is finite by the complete proof in [Coherence of higher direct images under proper morphisms](../../AG-QC/src/proper-morphisms-and-coherent-direct-images.md), Theorem 4.1. The constants are \(k\): their finite algebra becomes a finite reduced connected algebra over an algebraic closure, hence that algebraically closed field; affine Čech field base change then makes its dimension over \(k\) equal to one.

Line-bundle cohomology on this curve is zero above degree one, without a projectivity assumption. To see this, embed \(M\) in its sheaf \(\mathcal K_M\) of rational sections. The latter is flasque: its sections on every nonempty open are the same generic one-dimensional vector space. Its quotient is the direct sum, over closed points \(P\), of the principal-part skyscraper sheaves \(\mathcal K_M/M_P\). Indeed any local rational section has only finitely many poles, and every open of a Noetherian curve is quasi-compact. Conversely a principal part at one point is represented by a rational section near that point; shrink away its other finitely many poles and glue its quotient class to zero on the complement of that point. Finite tuples glue in the same way. Restrictions of these direct sums are projections onto subsets of the points, hence surjective. The quotient is therefore flasque as well. This length-one flasque resolution proves \(H^q(C,M)=0\) for \(q>1\), so \(\chi(M)=h^0(M)-h^1(M)\).

A line bundle on the regular integral curve has a nonzero rational section. Its valuations at closed points, whose local rings are DVRs, give a divisor \(D=\sum_P n_PP\) of finite support and identify \(M\simeq\mathcal O_C(D)\). Finiteness follows by writing the rational section in finitely many affine trivializations: each nonzero numerator or denominator has only finitely many zeros on a Noetherian integral curve. The point sequence
\[
0\longrightarrow M(-P)\longrightarrow M
\longrightarrow M|_P\longrightarrow0
\]
changes Euler characteristic by \([k(P):k]\). Additivity, iterated for positive or negative coefficients, gives
\[
\begin{aligned}
\chi(M)&=\chi(\mathcal O_C)+\sum_Pn_P[k(P):k]\\
&=1-g_C+\deg D.
\end{aligned}
\]
This proves the first formula. It also proves independence from the rational section: a principal divisor gives an isomorphic structure sheaf and has degree zero. Thus this degree agrees with the ordinary divisor degree in every characteristic, including inseparable residue fields.

We establish projectivity before applying projective duality. Choose any closed point \(P\). For \(a\) sufficiently large, the first formula makes
\(\chi(\mathcal O_C(aP))=1-g_C+a[k(P):k]>1\).
Since \(h^0\ge\chi\), there is a nonconstant rational function with poles bounded by \(aP\). The rational map it gives to \(\mathbf P^1\) extends at every closed point by the DVR valuative criterion for the proper target, and hence is a morphism. It is proper and has zero-dimensional fibres: otherwise the integral curve would be a fibre and the function constant. Thus it is finite by the proper quasi-finite theorem. The pullback of \(\mathcal O_{\mathbf P^1}(1)\) is ample: its two standard nonvanishing opens are finite inverse images of affine opens, hence affine, and the affine-nonvanishing criterion proved in [Group schemes over a field](group-schemes-over-a-field.md), Lemma 6.1, applies. A sufficiently high power embeds the proper \(C\), proving projectivity.

We now apply the full projective Cohen–Macaulay duality construction in [Dualizing sheaves and Serre duality for projective schemes](../../AG-QC/src/dualizing-sheaves-and-serre-duality-for-projective-schemes.md), Theorems 4.1–4.2. Their proofs construct the dualizing sheaf
\[
\omega_C^\circ
=\mathcal E xt^{N-1}_{\mathbf P^N}
   (\mathcal O_C,\mathcal O_{\mathbf P^N}(-N-1))
\]
for an embedding \(C\hookrightarrow\mathbf P^N\), and prove
\(\operatorname{Hom}(M,\omega_C^\circ)=H^1(C,M)^\vee\)
and the all-degree duality by ambient projective-space duality. These are proved earlier theorems, rather than an omitted curve-duality assertion.

Here is the required identification with differentials, so it is not assumed from a smooth-duality citation. Write \(I\) for the ideal of the immersion. By the regular-local quotient theorem, its local equations are a regular sequence of length \(N-1\). Their Koszul resolution gives
\[
\omega_C^\circ
\simeq\mathcal O_{\mathbf P^N}(-N-1)|_C
      \otimes\bigl(\det(I/I^2)\bigr)^{-1}.
\]
The calculation glues: a change of generators changes the final Koszul term by its determinant, exactly the transition of the displayed inverse determinant. Since \(C\) and projective space are smooth, the conormal sequence is
\[
0\longrightarrow I/I^2\longrightarrow
\Omega^1_{\mathbf P^N/k}|_C\longrightarrow
\Omega^1_{C/k}\longrightarrow0.
\]
For example, after algebraic closure, its first map has rank \(N-1\) at every closed point because the quotient tangent space of the smooth curve has dimension one; Nakayama and faithful flat descent prove injectivity on the original curve. Taking determinants and using the dual Euler sequence
\(\det\Omega^1_{\mathbf P^N/k}=\mathcal O(-N-1)\)
identifies \(\omega_C^\circ\) with \(\Omega^1_{C/k}\). This proves the stated cohomology formula.

Duality with \(M=\mathcal O_C\), and then with \(M=\omega_C^\circ\), gives
\[
h^0(\omega_C^\circ)=g_C,\qquad h^1(\omega_C^\circ)=1.
\]
Its Euler characteristic is \(g_C-1\). Applying the first formula to this line bundle yields \(\deg\omega_C^\circ=2g_C-2\), as claimed. This also proves the full usual curve Riemann–Roch equality
\(h^0(M)-h^0(\Omega^1_{C/k}\otimes M^{-1})=\deg M+1-g_C\).
\(\square\)

**Example 9.12. Why the cube, rather than the square.** Let \(E/k\) be a smooth proper geometrically integral genus-one curve with \(O\in E(k)\). Lemma 9.11 makes its canonical bundle trivial: it has a nonzero canonical section, and that section has a degree-zero effective zero divisor, hence no zeros. The same proved lemma gives, for every line bundle \(M\) of positive degree \(d\),

\[
h^0(E,M)=d,\qquad H^1(E,M)=0.
\]

The inverse of a positive-degree line bundle has no section, because a nonzero section would give an effective divisor of negative degree. For \(d\ge3\), and any length-two subscheme \(Z\) after an algebraic closure, the line bundle \(M(-Z)\) has positive degree, so \(H^1(M(-Z))=0\). The exact restriction sequence makes \(H^0(M)\to H^0(Z,M|_Z)\) surjective. The same argument for a length-one subscheme gives generation. Lemma 1.6 turns these point and tangent restrictions into a closed immersion. This proves very ampleness for every \(d\ge3\), including \(d=3\), in every characteristic. For \(d=2\), the length-one restriction argument still gives generation, so the two-dimensional complete space of sections gives a map to \(\mathbf P^1\), which cannot embed a genus-one curve; for \(d=1\), one section cannot generate an embedding. Thus \(M\) is very ample exactly when \(d\ge3\), and ample exactly when \(d>0\), since its third power then embeds. Conversely a very ample power has positive degree: a hyperplane through a point but not containing the curve cuts out a nonempty effective divisor. Thus a nonpositive-degree bundle cannot be ample.

In particular \(\mathcal O_E(2O)\) is generated and gives a degree-two morphism to \(\mathbf P^1\), while \(\mathcal O_E(3O)\) embeds in \(\mathbf P^2\) as a cubic. The existing pointed-cubic construction supplies its group law. This corrects the off-by-one thresholds, and the \(\mathbf P^3\) typo for three sections, in Milne's Example I.6.5.

For completeness the genus-one input also produces the cubic. Choose \(x\in H^0(2O)\setminus H^0(O)\) and \(y\in H^0(3O)\setminus H^0(2O)\). Their pole orders are exactly two and three. The seven functions \(1,x,y,x^2,xy,x^3,y^2\) lie in the six-dimensional \(H^0(6O)\). Their unique relation has nonzero coefficients of both \(x^3\) and \(y^2\), since the remaining pole orders are distinct and smaller than six. Rescale \(x,y\): if the relation reads \(a y^2=b x^3+\cdots\), replacing both variables by \((b/a)\) times themselves makes the two leading coefficients equal. It becomes a generalized Weierstrass equation

\[
y^2+a_1xy+a_3y=x^3+a_2x^2+a_4x+a_6.
\]

The already-proved very ampleness of \(3O\) embeds \(E\) by \(1,x,y\). Its image has degree \(\deg(3O)=3\), and the displayed nonzero cubic relation therefore cuts out that image. At \(O\), multiply the three sections by a local parameter cubed: their orders are \(3,1,0\), so the image is \([0:1:0]\) in the coordinate order \([x:y:1]\). The line at infinity cuts out \(3O\), making \(O\) a flex. Thus the existing pointed-cubic theorem shows that every such genus-one curve is an abelian variety. Conversely Proposition 1.3 makes the canonical bundle of a one-dimensional abelian variety trivial; Lemma 9.11 gives \(2g_E-2=0\), so it has genus one.

**Example 9.13. Two origin slices do not determine a bundle on two factors.** On \(E\times E\) let

\[
M=\mathcal O(\Delta-E\times\{O\}-\{O\}\times E).
\]

It is trivial on both origin slices. To check this, the diagonal meets either slice once at \(O\), the opposite slice contributes the same point, and the slice's own normal bundle is constant: its normal direction is the tangent line \(T_{E,O}\). For \(P\ne O\), restriction to \(\{P\}\times E\) is \(\mathcal O_E(P-O)\). This is nontrivial: a trivialization would give a rational function with one simple pole and one simple zero, hence a degree-one map \(E\to\mathbf P^1\), contradicting the point-class injectivity already proved in Lemma 9.0a. Thus \(M\) is nontrivial although both origin slices are trivial. The third slice in the cube is substantive.

## 10. Equivalent definitions and families

**Proposition 10.1. Sixteen definitions.** Choose one property from each row:

| Properness | Connectedness | Smoothness or reducedness |
|---|---|---|
| proper or projective | connected, geometrically connected, irreducible or geometrically irreducible | smooth or geometrically reduced |

A \(k\)-group scheme with those three chosen properties is an abelian variety, and every abelian variety has all the listed properties.

**Proof.** Every combination implies the weakest one: proper, connected and geometrically reduced. Properness gives finite type. The connected-group results of *Group schemes over a field* give geometric irreducibility for a connected group scheme; together with geometric reducedness this is geometric integrality. Thus the weakest combination already gives our definition.

Conversely an abelian variety is proper and geometrically integral, hence satisfies all four connectedness properties and geometric reducedness. Proposition 1.2 gives projectivity and smoothness. This proves the assertion for all \(2\cdot4\cdot2=16\) choices. \(\square\)

*Comparison locators:* [Stacks, Tags 03RP and 0H2U]. In the multiplication criteria of the summary, the trivial abelian variety has the dimension-zero exception from Theorem 6.2.

An **abelian scheme** over \(S\) is a smooth proper commutative \(S\)-group scheme of finite presentation with geometrically connected fibres. Each fibre is an abelian variety: it is proper, smooth and geometrically connected, so Proposition 10.1 applies over its residue field. Abelian varieties are the case \(S=\operatorname{Spec}k\). This is the family notion used in *Néron models*, where the extension across a missing special fibre is governed by a mapping property.

## 11. Exercises

**Exercise 1 (easy): remove the translation.** Use rigidity to prove that every morphism of abelian varieties is a homomorphism followed by a unique translation.

**Exercise 2 (medium): two-torsion on a cubic.** For \(y^2=f(x)\), with \(f\) a separable cubic and \(\operatorname{char}k\ne2\), compute the four geometric points of \(E[2]\), and determine their abstract group.

**Exercise 3 (medium): extract the square.** Pull the cube back along \(z\mapsto(z,a,b)\), \(a,b\in A(k)\). Identify every varying and constant factor, and deduce the theorem of the square.

**Exercise 4 (medium): symmetric multiplication.** Prove formula (12) from the cube and deduce (13). Construct a symmetric ample line bundle from an arbitrary ample line bundle.

**Exercise 5 (hard): recover the torsion group.** Prove \(A[n](k_s)\simeq(\mathbf Z/n)^{2g}\) for invertible \(n\), using the degrees of multiplication for the prime divisors of \(n\). Explain why the order at a single \(n\) is insufficient by itself.

**Exercise 6 (hard): compatible Tate bases.** Prove surjectivity of the transition maps in (19), construct compatible bases, and deduce that the Galois action on \(T_\ell(A)\) is continuous.

**Exercise 7 (medium): the missing connectedness hypothesis.** Give a proper geometrically integral \(X\) and a disconnected \(Y\) for which one fibre of \(X\times Y\to Z\) is contracted but the morphism does not globally factor through \(Y\). Locate the step of the rigidity proof that fails.

**Exercise 8 (hard): why nilpotent parameters survive the cube proof.** In Lemma 3.3, write down the equation between the degree-zero differentials and degree-one restriction matrices. Explain why an invertible minor forces a section to lift over the entire local base ring, and how properness turns it into a local trivialization of the family.

**Exercise 9 (medium): equal length, unequal point counts.** Check the smoothness and inverse maps of the two cubics (26). Compute their geometric two-torsion points and compare with the ranks of their two-torsion schemes.

**Exercise 10 (hard): higher \(p\)-power points.** Assuming the point bound and surjectivity of every \([d]\), prove (24). Determine the \(p\)-rank of a product and verify the dimension-zero exception to the étaleness criterion.

### Further exercises on isogenies and density

**Exercise 11.** Let \(f:A\to B\) be an isogeny of degree \(d\) and let \(g=\dim A\). Compute the degree of the reverse isogeny in 6.7. What happens when \(g=0\)?

**Exercise 12.** Explain why an étale isogeny of degree \(d\) has exactly \(d\) geometric kernel points, whereas an arbitrary isogeny may have fewer. Give the relevant characteristic-\(p\) example.

**Exercise 13.** Prove that two homomorphisms \(A\to B\) agreeing on \(A[\ell^r](\overline k)\) for every \(r\), where \(\ell\ne\operatorname{char}k\), are equal over \(k\). State the correct replacement if \(\ell=\operatorname{char}k\).

## 12. Complete solutions

**Solution 1.** Set \(b=f(0)\), and \(u=t_{-b}\circ f\). It satisfies \(u(0)=0\). The morphism \(v(x,y)=u(x+y)-u(x)-u(y)\) is zero on \(A\times\{0\}\). The source factor \(A\) is proper with \(H^0(A,\mathcal O)=k\), the parameter factor is connected, and the target is separated. Rigidity therefore makes \(v\) independent of \(x\). Its restriction to \(\{0\}\times A\) is also zero, so \(v=0\). This is the homomorphism identity for \(u\), and \(f=t_b\circ u\). Any homomorphism sends \(0\) to \(0\), so evaluation determines \(b\) and then \(u\) uniquely.

**Solution 2.** The point at infinity is \(O\). On an affine vertical line the two intersections are \((x,y)\) and \((x,-y)\), and the third is \(O\); the line rule makes them inverses. A finite point of order dividing two therefore satisfies \(y=-y\). Since two is invertible, this means \(y=0\). The curve equation then gives precisely the three points at the distinct roots of \(f\). There are four points including \(O\), all killed by two. An abelian group killed by two is a vector space over \(\mathbf F_2\); its size four gives dimension two and group \((\mathbf Z/2)^2\). No root coincidence is possible because \(f\) is separable.

**Solution 3.** Along \((z,a,b)\), the pullback of (9) is

\[
t_{a+b}^*L\otimes(t_a^*L)^{-1}
\otimes(t_b^*L)^{-1}\otimes L
\otimes
(L_{a+b})^{-1}\otimes L_a\otimes L_b\otimes(L_0)^{-1},
\]

where the last four factors mean constant line bundles on \(A\). The cube says the product is trivial. Each constant factor is a one-dimensional \(k\)-vector space and hence has a basis; trivializing them yields

\[
t_{a+b}^*L\otimes L\simeq t_a^*L\otimes t_b^*L.
\]

The calculation also shows the exact correction factors if \(a,b\) are families over a more general base, where those lines need not have chosen global bases.

**Solution 4.** In line-bundle classes write \(F_n=[n]^*[L]\), \(l=[L]\), \(i=[-1]^*[L]\). The substitution \((x,x,-x)\) gives \(F_2=3l+i\). The substitution \((x,x,[n-1]x)\) gives

\[
F_{n+1}-2F_n+F_{n-1}=l+i.
\]

With \(F_0=0,F_1=l\), the unique solution for nonnegative integers is

\[
F_n=\frac{n(n+1)}2l+\frac{n(n-1)}2i.
\]

For negative integers pull back by inversion, which exchanges \(l,i\). If \(L\) is symmetric, \(i=l\), and the total coefficient is \(n^2\). Given any ample \(H\), inversion preserves ampleness and the tensor product of ample line bundles is ample. Thus \(H\otimes[-1]^*H\) is ample; inversion exchanges its two factors, making it symmetric.

**Solution 5.** Finite étaleness gives \(|A[d](k_s)|=d^{2g}\) for every invertible positive divisor \(d\) of \(n\). For \(n=\ell^r\), decompose the killed-by-\(\ell^r\) group as \(\bigoplus_{i=1}^a\mathbf Z/\ell^{b_i}\), \(1\leq b_i\leq r\). Its killed-by-\(\ell\) subgroup is \(A[\ell](k_s)\), so \(a=2g\). Its total order gives \(\sum b_i=2gr\). The upper bounds on the \(2g\) terms force \(b_i=r\) for every \(i\). Chinese-remainder primary decomposition gives the general \(n\) result.

For comparison, a group of order \(\ell^4\) killed by \(\ell^2\) could be \((\mathbf Z/\ell^2)^2\), \(\mathbf Z/\ell^2\oplus(\mathbf Z/\ell)^2\), or \((\mathbf Z/\ell)^4\). The total order and exponent bound alone do not distinguish them. Their killed-by-\(\ell\) subgroup sizes do, which is why the lower-order degree information is needed.

**Solution 6.** Given \(x\in A[\ell^r](k_s)\), the fibre of \([\ell]\) over \(x\) is nonempty and finite étale. It has a \(k_s\)-point \(y\); since \(\ell y=x\), it is killed by \(\ell^{r+1}\). This proves surjectivity. Choose a basis at level one and recursively lift it through these maps.

At level \(r+1\), multiplication by \(\ell^r\) identifies \(P_{r+1}/\ell P_{r+1}\) with \(P_1\), by the already-proved free structure of \(P_{r+1}\). The compatible lifts map to the original basis there. Nakayama makes them generators over \(\mathbf Z/\ell^{r+1}\); a generating map from a free module of the same rank is bijective here because the two finite sets have equal cardinalities. The coordinates reduce under the transition maps, so the limit is \(\mathbf Z_\ell^{2g}\).

At each finite level the Galois action factors through the finite Galois group of a splitting field for the finite étale torsion scheme. The kernels of all these finite-level actions are open in \(\Gamma\). They are the preimages of the congruence neighbourhoods of the identity in \(\mathrm{GL}_{2g}(\mathbf Z_\ell)\), proving continuity.

**Solution 7.** Take \(X=\mathbf P^1_k\), \(Y=\operatorname{Spec}k\amalg\operatorname{Spec}k\), and \(Z=\mathbf P^1_k\). On the first component let the map be constant at a rational point, and on the second let it be the identity. The first fibre is contracted and the second is not, so no map from \(Y\) can recover it by projection. In (3) the contracted-fibre locus is the first open and closed component. It is nonempty but is not all of \(Y\); the connectedness step is exactly what fails.

**Solution 8.** Represent the three derived pushforwards by free complexes \(C,D,F\) adapted to the fibre. Their degree-zero terms are the base ring \(R\), and the unit sections make \(d_D^0=d_F^0=0\). Let \(a,a'\) be the degree-zero maps of restriction and \(B=(b,b')\) the combined degree-one map. The chain equations are

\[
B\,d_C^0=(d_D^0a,d_F^0a')=(0,0).
\]

Künneth makes \(B\) injective after reduction to the residue field. Inverting a full-column minor makes \(B\) split injective over \(R\), so \(d_C^0=0\) over \(R\), including any nilpotents. The basis of \(C^0\) therefore lifts the trivializing fibre section to a genuine section of \(\mathcal L\). Its zero scheme has closed image under the proper product family and misses the chosen point. Removing that image makes the lifted section invertible on the whole inverse image of an open neighbourhood. This supplies local triviality on the scheme, rather than merely at its reduced points.

**Solution 9.** For \(y^2+xy=x^3+1\), the affine partials \(y+x^2,x\) would both vanish only at \((0,0)\), which is off the curve. Its unique point at infinity is \(O\), where the homogeneous \(Z\)-partial is nonzero. For \(y^2+y=x^3\), the homogeneous partials are \(X^2,Z^2,Y^2\), with no common projective zero. Both curves are smooth.

The vertical-line involutions are \(y\mapsto y+x\) and \(y\mapsto y+1\), respectively. They preserve the equations and exchange the two finite intersections on the line; their third intersection is \(O\), so they give inversion. The first involution fixes exactly the affine point \((0,1)\), while the second fixes no affine point. Including \(O\) gives two and one geometric two-torsion points. In both cases \(g=1,d=2\), so Theorem 6.1 gives finite locally free rank \(2^2=4\). Hence the ranks agree while the \(p\)-ranks are one and zero.

**Solution 10.** Over \(\overline k\), surjectivity of \([p]\) gives a \(p\)-division point of any \(p^r\)-torsion point, and such a lift is killed by \(p^{r+1}\). Thus

\[
0\longrightarrow A[p](\overline k)
\longrightarrow A[p^{r+1}](\overline k)
\xrightarrow{p}A[p^r](\overline k)
\longrightarrow0
\]

is exact. If the first group has size \(p^f\), induction gives size \(p^{fr}\) at level \(r\). The elementary-divisor decomposition of that level has exactly \(f\) factors, counted by its killed-by-\(p\) subgroup. Each exponent is at most \(r\), and their sum is \(fr\), so all exponents are \(r\). This proves (24).

Products have coordinatewise kernels and point groups, so their \(p\)-ranks add. Finally a zero-dimensional abelian variety is \(\operatorname{Spec}k\). Its group is trivial and every multiplication is its identity, an étale map regardless of whether \(d\) is invertible. The positive-dimensional hypothesis in the converse of Theorem 6.2 is therefore necessary.

### Solutions on isogenies and density

**Solution 11.** Since \(f'f=[d]_A\), degree multiplication and Theorem 6.1 give \(\deg(f')d=d^{2g}\). Thus \(\deg(f')=d^{2g-1}\) when \(g>0\). In dimension zero both varieties are the trivial group \(\operatorname{Spec}k\); the unique isogeny has degree \(d=1\) and so does its reverse. The formula still evaluates to one, but there is no nontrivial degree to choose.

**Solution 12.** A finite étale algebra over an algebraically closed field is a product of copies of that field. Its number of factors is its vector-space dimension \(d\), so the kernel has exactly \(d\) points. For general kernels the factors may be local Artinian algebras of length greater than one; their lengths sum to \(d\), while the number of points counts only the factors. Relative Frobenius on a positive-dimensional \(A\) has degree \(p^g\) and a connected kernel with just one geometric point, by 8.2.

**Solution 13.** Over \(\overline k\), the equalizer is a closed subscheme, because \(B\) is separated. Its defining ideal vanishes on the dense torsion point set from 8.7; reducedness of \(A_{\overline k}\) makes that ideal zero. Faithful flatness then descends equality. For the characteristic prime, require equality of the restrictions as scheme morphisms on every \(A[p^r]\). Their schematic density makes the same equalizer all of \(A\). Equality on points alone is insufficient when the \(p\)-rank is zero: the zero map and the identity of a positive-dimensional supersingular elliptic curve agree on all those torsion points but differ as morphisms.

## What this lesson does not prove

The construction of the elliptic-curve group law from a smooth plane cubic and its rational flex is proved in Lemma 9.0a and Theorem 9.0, including the rational-function divisor formula over every extension field and the scheme identities in families. Its line rule supplies the inversion and torsion computations. We also prove the smoothness and all torsion calculations of the chosen cubics. The point-class argument gives its own projective-curve finiteness proof; its valuation-ring domination input is the full internal proof in *Morphisms of schemes*, *Valuation rings and the valuative criterion of separatedness*, Theorem 2.1. The remaining elementary ring input is that a finite torsion-free module over a DVR is free.

The general cohomology-and-base-change theorem for proper flat finite-presentation families and perfect complexes is a prerequisite [Stacks, Tag 0B91], as are field Künneth [Stacks, Tag 0BED], flat base change for coherent cohomology [Stacks, Tag 02KH], the elementary Hilbert-polynomial and ampleness results, and miracle flatness [Stacks, Tag 00R4]. The Hilbert-polynomial support-degree statement was also checked in AI Integrated Stacks Project, Tag 0HDJ. The field-theoretic \(p\)-basis facts used in Section 8 have locators [Stacks, Tags 031W and 07P1–07P2]. Their role and hypotheses are identified at the points of use. Lemmas 3.1–3.4 supply the additional local and global line-bundle arguments rather than importing the theorem of the cube.

The earlier course proofs of smoothness, quasi-projectivity and connected-group structure are used explicitly. Results6.11–6.42 construct the dual and its Poincaré bundle, prove Poincaré reducibility, complex uniformization and lattice homomorphisms, the all-test Picard criterion, exact Cartier-dual isogeny kernels, canonical biduality, torsion-free Néron–Severi components and their symmetric-Hom embedding, Hodge–de Rham degeneration and Frobenius/Verschiebung duality over arbitrary fields. General proper-scheme Néron–Severi finiteness and uniform family bounds, surjectivity onto all symmetric homomorphisms and the complete classification of nonreduced \(p\)-torsion have separate proof scopes.

## References

The Stacks Project, read in **AI Integrated Stacks Project**, Groupoid Schemes, Section 0BF9, Tags 03RO, 0BFA–0BFH, 0C0Y, 03RP and 0H2U; More on Morphisms, Tag 0BF4 and the comparison product lemma 0BF3, together with the proper-fibre lemma 0AH8. Cohomology and algebra prerequisites are cited individually above. AI Integrated Stacks Project is an AI-integrated edition; its additions have not been reviewed by the official Stacks maintainers. The cited material was checked at published revision 565b10e987aba5969b21145a0833f42d69f96790.

J. S. Milne, *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*, corrected edition dated 5 October 2021, Cambridge University Press, 2022: Chapter 2c for the cubic examples, and Chapter 8e for anti-affine groups and abelian varieties. [Author's edition](https://www.jmilne.org/math/Books/iAG2022.pdf).

The finite-kernel, separability and factorization results correspond to Bas Edixhoven, Gerard van der Geer and Ben Moonen, *Abelian Varieties*, preliminary version, Chapter V, §§1-3, especially (5.2)-(5.13), (5.15), (5.20)-(5.25) and (5.30)-(5.31). The chapter footer dates this source section 8 February 2012. The finite-kernel recognition also corresponds to J. S. Milne, *Abelian Varieties*, version 2.0, title dated 16 March 2008, Part I, Proposition 7.1; its Theorem 7.2 and Remark 7.3 are already supplied by Theorems 6.1-7.2 in the current lesson. The correction above concerns the actual displayed formula in that exact version's Remark 7.4. Direct reading editions: [Edixhoven-van der Geer-Moonen](https://van-der-geer.nl/AV.pdf), [Milne](https://www.jmilne.org/math/CourseNotes/AV.pdf).

The proof organization here is independent. 6.3-6.4 use the programme's effective finite quotient and closed-monomorphism results rather than importing general miracle flatness. 6.6 supplies the needed finite-rank annihilator by a determinant calculation on symmetric tensors. 8.3-8.4 use smoothness, differentials and faithfully flat descent; the arbitrary-base Verschiebung construction and finite Cartier-duality theorem of source (5.16)-(5.19) are now supplied by 8.9-8.11. 8.7 proves both density conclusions and retains the failure of topological density at the characteristic prime. Exact source-result decisions and inherited algebraic prerequisites are recorded in the accompanying workflow JSON.

The characteristic-two and characteristic-three computations, infinitesimal translation action, quotient family and flat-module Verschiebung construction correspond to Edixhoven, van der Geer and Moonen, Chapter V (5.16)-(5.19) and (5.26)-(5.29). The coefficient calculation and Proposition 9.10 prove the stated realization cases of (5.25)(ii); Theorems9.19–9.20 now supply the prime-field case and realize every p-rank over every field of positive characteristic. The exposition, trace calculation, explicit action verification and finite-Hom argument are independently written. These additions retain CC0 1.0.

### Source credit and exact prerequisite boundary

Related treatments are Edixhoven–van der Geer–Moonen, *Abelian Varieties*, preliminary version, Chapters 1–2 and Chapter 9, items 9.11–9.12 and 9.18, and Milne, *Abelian Varieties*, version 2.0, Part I §§1 and 5–6. Proposition 4.6 follows Edixhoven–van der Geer–Moonen in attributing their Proposition 2.20 to Nori. The cube and square results are credited to Weil at the cube proof, and the projective-space obstruction to Barth and Van de Ven. The general third-power result is Lefschetz's theorem; neither of these treatments contains its full proof. Akhil Mathew's notes of Xinwen Zhu's lectures, [*Algebraic geometry*](https://www.math.uchicago.edu/~amathew/232b.pdf) (Harvard, spring 2012), Theorem 2.10, state it without proof.

The exact retained lesson inputs are Lemma 1.1, Proposition 1.2, Theorem 2.1, Lemmas 3.1–3.4, Theorem 4.1 and its square/cube corollaries, Theorem 5.1, Theorems 6.1–6.2, and the pointed-cubic Theorem 9.0 and Lemma 9.0a. Earlier group lessons supply connected components, reduced-group smoothness over a perfect field, finite translation quotients, finite-set affine neighborhoods, the affine-nonvanishing ampleness criterion, and faithfully flat descent. The exact read files, result anchors and hashes are recorded in the accompanying workflow.

The new arguments close their additional inputs as follows. Lemmas 5.2–H1 and Proposition 5.5 prove Euler homogeneity, positivity and effectivity using the earlier fully proved coherent-filtration, Euler-polynomial and Serre theorems. Corollary 5.6 proves the needed finite-flat Euler comparison by generic lattices. Lemma 5.8 proves the particular reduced-member openness needed for Lemma 5.9, including the perfect-field generic-smoothness calculation. Theorem 5.11 proves its degree and restricted-resolution calculation using exterior-power identities and its explicit finite graded-resolution proof. Lemma 9.11 proves the curve formulas and identifies the canonical sheaf with differentials; it binds the actual earlier full projective duality proofs, rather than treating curve duality as a missing assertion. Theorem 2.5 supplies rational-map extension, and Theorem 3.5 supplies maximal relative triviality for arbitrary proper geometrically integral \(X\) and arbitrary \(Y\), including nilpotents and inseparable point extensions.

The numerical degree statement is expressed by the Hilbert polynomial and projective degree. General algebraic Riemann–Roch and a general Chow-ring intersection construction are not required for the proofs above. The deeper Picard, duality and semistable-reduction results have their own proof scopes.

The added exposition is independently written and uses the user-selected CC0 1.0 dedication.
