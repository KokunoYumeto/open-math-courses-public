# Group schemes over a field

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

*The proofs in Section 2, Lemma 2.A through Corollary 2.H, were added by GPT-6 Astra (OpenAI) in Codex, Ultra setting, October 2026. CC0.*

Translation makes the topology of a group scheme unusually rigid. Connected pieces cannot branch into intersecting irreducible components, and the component containing the identity is itself a group. For groups of finite type, the remaining components form a finite étale group scheme. This retains arithmetic information: a component group need not be a constant group over the ground field.

We distinguish three levels of generality. A **group scheme over \(k\)** has no finiteness condition. A **locally algebraic** group scheme is locally of finite type over \(k\). An **algebraic group scheme** is of finite type over \(k\); smoothness is an additional condition. The first two sections treat arbitrary group schemes. The finite étale component group and quasi-projectivity carry their finite-type conditions explicitly. Section 7 also distinguishes finite-type orbit boundaries from topological transitivity without finiteness.

Prerequisites are schemes, flatness, connected components, field extensions, finite étale schemes and their Galois description, and basic dimension theory. The preceding lessons supply invariant differentials and smoothness. We will not use the general existence of quotients by closed subgroups in constructing the component group.

## 1. Open multiplication and a single component through each point

**Proposition 1.1.** Every group scheme over a field is separated. Multiplication is open. If \(U\subset G\) is open and \(T\to G\) is any morphism, the image of \(T\times_kU\to G\) under multiplication is open as well.

**Proof.** The rational identity \(e\) is a closed point, even without a finite-type condition. Indeed, if it specialized to \(y\), an affine neighbourhood of \(y\) would also contain \(e\). On that affine chart the evaluation map to \(k\) is surjective, so its kernel is maximal, and \(e\) has no distinct specialization there. Its scheme structure is a closed immersion, since the evaluation map is surjective. The separatedness criterion from *Group schemes, actions and Hopf algebras* now applies.

The shear \((g,h)\mapsto(gh,h)\) is an automorphism of \(G\times_kG\). It identifies multiplication with projection onto the first factor. A scheme over a field is universally open over that field, so this projection, and hence multiplication, is open.

For the last assertion, take any point of \(T\times_kU\) and extend the field so that its two coordinates are represented by rational points \(t,u\). Over that field, the image contains the open translate \(tU\). Projection from this field extension back to \(G\) is open. Its image supplies an open neighbourhood of the original image point contained in the image of \(T\times_kU\). Doing this at every point proves openness. \(\square\)

We write \(TU\) for that image, and similarly use \(UV\) and \(U^{-1}\). These denote images of scheme morphisms, so this notation includes points with arbitrary residue fields.

For arguments without finite type, the usual assertion that closed points are rational needs a replacement.

**Lemma 1.2. Large-field point detection.** For any scheme \(X/k\), there is an algebraically closed extension \(K/k\) such that \(X_K\) is Jacobson and every closed point of \(X_K\) is \(K\)-rational. Every nonempty locally closed subset then contains a \(K\)-rational point.

**Proof.** Fix an affine cover and an infinite cardinal \(\kappa\) bounding the numbers of algebra generators of all its coordinate rings. Choose algebraically closed \(K\) with \(|K|>\kappa\). The rings of the base-changed charts still have at most \(\kappa\) generators as \(K\)-algebras.

If a field \(L\) is generated as a \(K\)-algebra by at most \(\kappa\) elements, its vector-space dimension over \(K\) is at most \(\kappa\), because the finite monomials in those generators span it. If \(z\in L\) were transcendental over \(K\), the elements

\[
\frac1{z-c}\qquad(c\in K)
\]

would be linearly independent. For a finite alleged relation, multiply by the product of its denominators and evaluate the resulting polynomial at each \(c\); every coefficient must vanish. This contradicts the dimension bound. Thus \(L/K\) is algebraic, and algebraic closedness gives \(L=K\).

Consequently every maximal residue field of each chart is \(K\). For any prime \(\mathfrak p\) and any \(f\notin\mathfrak p\), apply the same argument to a maximal ideal of \((A/\mathfrak p)[1/f]\). Its residue map to \(K\) restricts to a surjective map \(A\to K\), whose maximal kernel contains \(\mathfrak p\) and avoids \(f\). Thus every prime is the intersection of maximal ideals containing it: the chart is Jacobson. This also shows that every nonempty locally closed subset has a rational point. Rational points are closed in the whole scheme by the affine-neighbourhood argument of Proposition 1.1. The assertions therefore hold globally. \(\square\)

<a id="gs03-algebraically-closed-products"></a>

We also use the elementary product fact that over an algebraically closed field, the product of reduced schemes is reduced, and the product of irreducible reduced schemes is irreducible. Here this includes schemes not of finite type. To check the affine domain case, first take finite-type domains \(A,B\). For nonzero \(f,g\in A\otimes_kB\), write their finite coefficient expansions in linearly independent elements of \(B\). Choose a rational point of \(\operatorname{Spec}A\) where neither coefficient list vanishes identically. Both specialized elements of \(B\) are nonzero, and their product is nonzero because \(B\) is a domain. A rational point of \(\operatorname{Spec}B\) detecting that product shows that \(fg\ne0\). Thus \(A\otimes B\) is a domain. Arbitrary domains are unions of their finite-type subalgebras; their tensor inclusions are injective over a field, so the conclusion persists. For reduced rings, embed each into the product of its domain quotients by minimal primes. Finite coefficient expansions show that the induced tensor maps are injective, and the domain case proves reducedness. Affine covers give the scheme statements.

**Theorem 1.3.** Every local ring of a group scheme over a field has a unique minimal prime. Every point lies on exactly one irreducible component. The component \(Z\) through the identity is geometrically irreducible.

**Proof.** First work over an algebraically closed field. If \(Z_1,Z_2\) are irreducible components through \(e\), equip them with their reduced closed structures. Their product is irreducible. Its multiplication image is contained in an irreducible component, and contains both \(Z_1\) and \(Z_2\), because multiplication by \(e\) is the identity. Maximality of irreducible components forces \(Z_1=Z_2\).

For any point \(x\), choose an algebraically closed field extension \(K\) containing its residue field and a rational lift \(x'\). Translation identifies the local ring at \(x'\) with the local ring at the identity upstairs. The local map \(\mathcal O_{G,x}\to\mathcal O_{G_K,x'}\) is faithfully flat. Uniqueness of the minimal prime descends: each minimal prime downstairs is the contraction of a minimal prime upstairs, by surjectivity on spectra and going down for flat maps. Distinct minimal primes would therefore require distinct minimal primes upstairs. This proves uniqueness in all local rings. Irreducible components through a point correspond to the minimal primes of its local ring, which proves the second assertion.

For geometric irreducibility, first extend to an algebraic closure. Every component of \(Z_{\overline k}\) dominates \(Z\): flatness contracts a minimal prime to a minimal prime. The projection is integral, so its image is closed and hence is all of \(Z\). Its fibre over the rational identity is the single point \(e_{\overline k}\), so every such component contains that point. They are components of \(G_{\overline k}\) as well: a larger component would project into an irreducible subset containing the maximal component \(Z\), and hence would still lie above \(Z\). Uniqueness through \(e_{\overline k}\) therefore leaves only one component of \(Z_{\overline k}\). Over an algebraically closed field irreducibility persists under further field extension, by the product/domain argument just given. This proves geometric irreducibility. \(\square\)

*References:* [Stacks, Tags 047K, 0B7N, 047L and 047M]. The field-extension point-detection argument is the content of [Stacks, Tag 0479].

### 1.4. Dense products over a zero-dimensional local base

**Lemma 1.4.** Let \(A\) be a zero-dimensional local ring with residue field \(k\), and let \(G\) be any \(A\)-group scheme. Then \(G\) is separated. If \(U,V\subset G\) are dense open subsets, the multiplication image of \(U\times_AV\) is all of \(G\). In particular an irreducible \(A\)-group scheme is quasi-compact. No flatness or finiteness condition on \(G\) is required.

**Proof.** Every element of the maximal ideal of \(A\) is nilpotent. Its extension to any \(A\)-algebra is a nil ideal: each element is a finite sum involving finitely many nilpotent generators. Thus \(G_k\to G\) and \(G_k\times_kG_k\to G\times_AG\) induce homeomorphisms on underlying spaces. A uniform nilpotence bound is unnecessary. The identity of \(G_k\) is closed by Proposition 1.1. Thus the identity section of \(G\) has closed image. On an affine neighbourhood \(\operatorname{Spec}B\) of that image, its evaluation map \(B\to A\) is surjective, since its composite with the structure map \(A\to B\) is the identity. The section is consequently a closed immersion. The identity-section criterion of *Group schemes, actions and Hopf algebras*, Proposition 6.1, proves separatedness.

For the dense-product assertion these same homeomorphisms reduce the question to \(A=k\). Take any point \(x\in G\), and extend to \(K=\kappa(x)\) with rational lift \(x_K\). The projection \(G_K\to G\) is open and surjective, so inverse images of dense opens are dense opens: every nonempty open upstairs projects to a nonempty open downstairs meeting the dense open. Hence \(U_K\) and \(x_K V_K^{-1}\) are dense opens of \(G_K\), and their intersection is nonempty. Choose a point in it and extend its residue field if necessary. It gives compatible field-valued points \(u\in U\), \(v\in V\) with \(u=xv^{-1}\), or \(x=uv\). Projecting back puts the original point \(x\) in the multiplication image. This proves the assertion over \(k\) and therefore over \(A\).

Finally, if \(G\) is irreducible, choose a nonempty affine open \(U\). It is dense, and the proved result makes \(U\times_AU\to G\) surjective. Its source is affine and quasi-compact, so its image \(G\) is quasi-compact. \(\square\)

**Corollary 1.5.** An immersion of group schemes over a zero-dimensional local ring is a closed immersion.

**Proof.** Reduction to the residue field gives a closed immersion by Proposition 5.2, hence a closed image. The nil-ideal homeomorphisms used in Lemma 1.4 show that the original immersion has closed image as well. An immersion with closed image is a closed immersion: its defining ideal on the open through which it factors glues with the unit ideal on the complement of its image. \(\square\)

### 1.6. Local rings and rational sections over an Artinian base

A Noetherian local ring is **Cohen–Macaulay** if it has a regular system of parameters. The needed commutative-algebra statements are [*Regular sequences, depth and Cohen–Macaulay modules*](../../AG-CA/src/regular-sequences-depth-and-cohen-macaulay-modules.md), Proposition 1.1, Corollary 4.3 and Corollary 5.2: flat extension preserves regular sequences, faithful flatness detects them, every parameter system of a Cohen–Macaulay ring is regular, and its prime localizations are Cohen–Macaulay. We use these exact statements, including their Noetherian hypotheses.

**Lemma 1.6.** A nonempty scheme locally of finite type over a local Artinian ring has a closed point with Cohen–Macaulay local ring. Every group scheme locally of finite type over a field has Cohen–Macaulay local rings at all points.

**Proof.** For the first assertion choose a nonempty affine chart \(\operatorname{Spec}B\), and induct on its finite dimension. The ring \(B\) is Noetherian and Jacobson: its reduction is a finite-type algebra over the residue field. If there is a zero-dimensional component, its point belongs to no other component and has zero-dimensional, hence Artinian and Cohen–Macaulay, local ring. Otherwise all components have positive dimension. A positive-dimensional Jacobson component has infinitely many closed points, so choose a maximal ideal which is not one of the finitely many associated primes of \(B\). Finite prime avoidance gives an element of this maximal ideal outside every associated prime. It is a nonunit nonzerodivisor \(b\).

The closed subset \(V(b)\) is nonempty and proper in every component. Dimension theory for finite-type algebras over a field, applied to the reduction, makes its dimension smaller. Induction supplies a closed point \(z\) at which \(B/(b)\) is Cohen–Macaulay. At \(z\), prepend \(b\) to a lifted regular parameter system of that quotient. The result is regular and has zero-dimensional quotient. The height theorem and the regular-sequence depth bound make its length equal to the local dimension, so it is a regular parameter system of \(B_z\). This proves the first assertion. The chosen point is closed in the whole scheme: its residue field is finite over the residue field of the base, and the same maximal-ideal argument on any affine neighbourhood of a proposed specialization proves closedness.

For the group assertion start with such a closed Cohen–Macaulay point \(x\). We record why finite field extension preserves and detects Cohen–Macaulayness at points lying above a closed point. For a finite extension \(K/k\), the local map \(R=\mathcal O_{G,x}\to S=\mathcal O_{G_K,x'}\) is faithfully flat, and its closed fibre is Artinian. Flat going down and incomparability for the finite integral projection give \(\dim S=\dim R\). A regular parameter system of \(R\) stays regular in \(S\), and its quotient is a localization of an Artinian finite extension of \(R\)'s parameter quotient, hence zero-dimensional. Conversely a parameter system of \(R\) has zero-dimensional quotient in \(S\); if \(S\) is Cohen–Macaulay, that list is regular there and faithful flatness detects its regularity in \(R\). The parameter criterion proves both directions.

For another closed point \(y\), take a finite extension containing both residue fields. The rational lifts of \(x\) and \(y\) differ by a translation. Their local rings are isomorphic, so the preceding preservation and descent make \(\mathcal O_{G,y}\) Cohen–Macaulay. Every point in an affine chart is a generalization of a closed point of that chart. Its local ring is a prime localization of the closed point's local ring, so the localization theorem gives the assertion at every point. \(\square\)

**Lemma 1.7. Lifting a fibrewise regular sequence.** Let \((A,\mathfrak m,k)\) be local Artinian and \(R\) a flat \(A\)-algebra. If the images of \(f_1,\ldots,f_d\in R\) form a regular sequence in \(\overline R=R/\mathfrak mR\), then the list is regular in \(R\), and each quotient \(R/(f_1,\ldots,f_i)\) is flat over \(A\). Finite generation of \(R\) is unnecessary.

**Proof.** First take one element \(f\). For any \(A\)-module \(M\), flatness identifies the factors in the finite \(\mathfrak m\)-adic filtration of \(M\otimes_AR\) with

\[
(\mathfrak m^jM/\mathfrak m^{j+1}M)
\otimes_k\overline R.
\]

Multiplication by \(f\) on each factor is multiplication by \(\overline f\), tensored with a vector space. It is injective. Induction up the finite filtration makes multiplication by \(f\) injective on \(M\otimes_AR\). For \(M=A\) this gives injectivity on \(R\). Put \(N=M\otimes_AR\). The exact sequence \(0\to R\xrightarrow{f}R\to R/fR\to0\), with the two copies of \(R\) flat, then has

\[
\begin{aligned}
\operatorname{Tor}_1^A(M,R/fR)&=\ker(f:N\to N),\\
&=0.
\end{aligned}
\]

Thus \(R/fR\) is flat over \(A\). Apply the same argument successively to the later quotients and their fibre sequences. Their last quotient is nonzero because its reduction is nonzero. This proves every assertion. \(\square\)

**Theorem 1.8. Artinian group local rings.** Let \(A\) be local Artinian and \(G/A\) flat and locally of finite type. Every local ring of \(G\) is Cohen–Macaulay. At a closed point \(x\), quotienting \(\mathcal O_{G,x}\) by any system of parameters gives a nonzero finite free \(A\)-algebra, with residue field \(\kappa(x)\).

**Proof.** The local special-fibre ring is Cohen–Macaulay by Lemma 1.6. Choose its regular parameter system and lift it to \(R=\mathcal O_{G,x}\). The maximal ideal of the base is nilpotent, so the fibre and total local ring have the same spectrum and dimension. Lemma 1.7 makes the lifted parameters a regular list with flat successive quotients. Its final quotient is zero-dimensional, proving that \(R\) is Cohen–Macaulay. This argument applies at every point.

At a closed point, any parameter system of \(R\) reduces to a parameter system in the special fibre, since the spectra are the same. That fibre is Cohen–Macaulay, so the reduced list is regular. Lemma 1.7 makes the quotient \(Q\) flat over \(A\). It is an Artinian local ring, being a zero-dimensional quotient of a Noetherian local ring. Its residue field \(\kappa(x)\) is finite over \(k\). The finite filtration by powers of its maximal ideal has finite-dimensional \(\kappa(x)\)-vector spaces as factors, so \(Q\) is finite as an \(A\)-module. A finite flat module over a local Artinian ring is free, as proved in *Diagonalizable groups*, Lemma 4.14. It is nonzero by local Nakayama, so its free rank is positive. Its residue field remains \(\kappa(x)\). \(\square\)

**Proposition 1.9. Finite-free rationalization.** Under the hypotheses of Theorem 1.8, take finitely many closed points of \(G\). There is a local Artinian finite free \(A\)-algebra \(A'\) such that every point of \(G_{A'}\) above those points is the image of an \(A'\)-section. Here an \(A'\)-section is a morphism \(\operatorname{Spec}A'\to G_{A'}\), not merely a rational point of its special fibre.

**Proof.** Choose a finite normal extension \(K/k\) containing the residue fields of the finitely many points, with the purely inseparable roots included. It can be lifted to a finite free local Artinian extension \(A_1/A\) with residue field \(K\). Indeed express \(K/k\) as a finite tower of simple extensions. At each step lift the coefficients of the monic minimal polynomial to the preceding ring and quotient its polynomial algebra by that monic polynomial. The quotient is free of the polynomial's degree; its reduction is the next field, so it is local Artinian. Iteration gives \(A_1\).

All points above the chosen points in \(G_{A_1}\) are rational over \(K\), and there are finitely many of them. List them as \(x_1,\ldots,x_r\). For each, Theorem 1.8 supplies a quotient \(Q_i\) of the local ring by a parameter system, finite free over \(A_1\), local Artinian and with residue field \(K\). Set

\[
A'=Q_1\otimes_{A_1}\cdots\otimes_{A_1}Q_r.
\]

It is finite free of positive rank over \(A_1\), hence over \(A\). Modulo the base maximal ideal, the tensor of the finite local \(K\)-algebras has nilpotent ideal given by the sum of their maximal ideals and quotient \(K\). Consequently \(A'\) is local Artinian with residue field \(K\). Each composite \(\mathcal O_{G_{A_1},x_i}\to Q_i\to A'\) defines a section after base change to \(A'\), through the point lying above \(x_i\). No further residue-field points appear in this nilpotent extension with the same residue field. The sections therefore include every point required in the assertion. \(\square\)

**Corollary 1.10. Smoothness over an Artinian ring.** For a flat, locally finite-type group scheme over local Artinian \(A\), the following are equivalent: \(G/A\) is smooth; its special fibre is geometrically reduced; its special fibre is geometrically reduced at the identity.

**Proof.** Smoothness gives geometric reducedness of every fibre. Conversely suppose the geometric special fibre is reduced at the identity. Over an algebraic closure, its reduction is a smooth subgroup by Proposition 4.1 and *Lie algebras and smoothness of group schemes*, Theorem 5.1. The nilradical of the locally Noetherian geometric fibre vanishes in its identity local ring, hence vanishes on a neighbourhood of that point. On that neighbourhood the subgroup inclusion is an isomorphism. Thus the geometric fibre is smooth at the identity. Translation makes it smooth at every rational point, and any nonempty closed complement of the smooth locus would contain a rational point. It is smooth everywhere; field descent gives a smooth special fibre over \(k\).

The Noetherian base makes local finite type into local finite presentation. With the assumed flatness, the exact fibrewise criterion in [*Smooth morphisms*](../../AG-FSE/src/smooth-morphisms.md), Theorem 3.1, now makes \(G/A\) smooth. Its proof uses finite-presentation Jacobian charts and flatness to remove the remaining kernel, so the infinitesimal base introduces no omitted lifting assumption. This proves the equivalences. \(\square\)

**Lemma 1.11. Relative flatness from the special fibre.** Let \(A\) be local Artinian, \(B\) an \(A\)-algebra, and \(M\) a \(B\)-module which is flat over \(A\). If \(M/\mathfrak mM\) is flat over \(B/\mathfrak mB\), then \(M\) is flat over \(B\). No finiteness hypotheses on \(B\) or \(M\) are required.

**Proof.** Put \(I=\mathfrak mB\). The surjection \(\mathfrak m\otimes_AB\to I\) gives a surjection \(\mathfrak m\otimes_AM\to I\otimes_BM\). Its composite with \(I\otimes_BM\to M\) is injective, since \(M\) is flat over \(A\). Surjectivity of the first map and injectivity of the composite make the second map injective. Thus \(\operatorname{Tor}_1^B(B/I,M)=0\).

For a module \(N\) killed by \(I\), choose a presentation with free \(B/I\)-module \(P\) and kernel \(K\). Tensoring \(0\to K\to P\to N\to0\) with \(M\) is the same as tensoring over \(B/I\) with \(M/IM\), so it retains the injection on the left. Also \(\operatorname{Tor}_1^B(P,M)=0\), by the previous vanishing and direct sums. The Tor sequence gives \(\operatorname{Tor}_1^B(N,M)=0\). Every \(B\)-module has a finite filtration by \(I^jN\), since \(I\) is nilpotent; its factors are killed by \(I\). The same Tor sequence, inductively up this filtration, gives the vanishing for every \(N\). The Tor flatness criterion proves the result. \(\square\)

**Corollary 1.12. Flatness propagates along an Artinian orbit.** Let \(G/A\) be any flat group scheme over local Artinian \(A\), let it act on any \(A\)-scheme \(X\), and choose a section \(x\in X(A)\). If the orbit map \(g\mapsto gx\) is flat at one point, it is flat everywhere. Neither scheme need be locally of finite type, and \(X\) need not be flat over \(A\).

**Proof.** Base change preserves flatness at the corresponding special-fibre point. For groups over a field, flatness of an orbit map at one point propagates to all points by common-residue-field extension and translation, as proved in Lemma 7.5. Thus the entire special-fibre orbit map is flat. At any point of \(G\), its local ring \(M\) is flat over \(A\); take \(B\) to be the target local ring. The quotients by \(\mathfrak m\) are the special-fibre local rings, so Lemma 1.11 makes \(M\) flat over \(B\). This holds at every point. \(\square\)

**Lemma 1.13. Detecting finiteness and immersions on a nilpotent base.** Let \(R\) be a ring, \(J\subset R\) an ideal with \(J^N=0\), and \(f:X\to Y\) a morphism of \(R\)-schemes. Write \(f_0\) for its base change to \(R/J\). Each of the properties locally of finite type, of finite type, immersion and closed immersion holds for \(f\) if and only if it holds for \(f_0\).

**Proof.** The forward implications are base change. For local finite type, take affine source and target charts with coordinate map \(C\to B\). If \(B/JB\) has finitely many algebra generators over \(C/JC\), lift them to \(B\), and let \(B'\) be the \(C\)-subalgebra they generate. Then \(B=B'+JB\), and \(JB'\subset B'\), because \(J\) comes from the base. Iterating gives \(B=B'+J^nB\) for every \(n\), hence \(B=B'\). This proves local finite type. Quasi-compactness of the morphism is unchanged by the nilpotent-base homeomorphisms, so the finite-type assertion follows too.

Suppose \(f_0\) a closed immersion. The inverse image of each affine target chart has affine special fibre. Affineness is invariant under a nilpotent thickening, by [*Infinitesimal lifting and invariance under thickenings*](../../AG-FSE/src/infinitesimal-lifting-and-invariance-under-thickenings.md), Proposition 1.2. Thus \(f\) is affine. On the chart its ring map satisfies \(B=\operatorname{im}C+JB\), and the same iteration, with no finite generation of this module assumed, gives \(B=\operatorname{im}C\). It is surjective, so \(f\) is a closed immersion. If \(f_0\) is an immersion, lift the open target through which it factors using the homeomorphism of target spaces. The image of \(f\) lies in that open; apply the closed-immersion case there. This proves the remaining assertion. \(\square\)

## 2. Connectedness, compactness and the identity component

### Connectedness after extending the ground field

A connected scheme can split after a field extension: \(\operatorname{Spec}\mathbb C\) is connected over \(\mathbb R\), whereas its base change to \(\mathbb C\) consists of two points. A rational point prevents this phenomenon. We prove that assertion without imposing finite type, quasi-compactness or separation on the scheme, and also prove the stronger version in which the residue field of a point has no new algebraic constants.

We use [Zariski's lemma](../../AG-CA/AG-CA-06.html#section-1), Theorem 1.3, and the [weak Nullstellensatz](../../AG-CA/AG-CA-06.html#section-2), Theorem 2.1, from *The Nullstellensatz and Jacobson rings*, together with the [Hilbert basis theorem](../../AG-CA/AG-CA-03.html#section-2), Theorem 2.1 of *Noetherian and Artinian rings*. Finite generation will be imposed on auxiliary rings containing a finite list of coefficients, not on the original scheme. Connected and irreducible spaces are nonempty.

<a id="gs03-idempotents-and-base-extension"></a>

**Lemma 2.A. Open and closed pieces.** Idempotents in \(\Gamma(X,\mathcal O_X)\) correspond bijectively to open-and-closed subsets of any scheme \(X\). For a field extension \(F/k\), the projection \(X_F\to X\) is surjective; restriction of functions from an affine chart to its base change is injective.

**Proof.** A function satisfying \(e^2=e\) has germ zero or one at every point: in a local ring either \(e\) or \(1-e\) is a unit, and \(e(1-e)=0\). Thus \(D(e)\) and \(D(1-e)\) form a complementary open partition. Conversely the functions one and zero on a complementary open partition glue to a unique global idempotent. These operations are inverse and commute with restriction.

For a point \(x\in X\), the fibre of the projection is \(\operatorname{Spec}(\kappa(x)\otimes_k F)\). This tensor product is a nonzero ring, because it is the tensor product of two nonzero vector spaces over a field and its identity is nonzero. It has a maximal ideal and hence a point. The projection is therefore surjective. On an affine chart, \(A\to A\otimes_k F\) is injective: a \(k\)-basis of \(A\) stays linearly independent after scalar extension. This also proves that equality of functions can be checked after field extension. \(\square\)

<a id="gs03-algebraically-closed-clopen-descent"></a>

**Lemma 2.B. Algebraically closed ground fields.** Suppose \(k\) is algebraically closed and \(F/k\) is any field extension. For every \(k\)-algebra \(A\), scalar extension gives a bijection on idempotents. Consequently, for every \(k\)-scheme \(X\), inverse image gives a bijection on open-and-closed subsets of \(X\) and \(X_F\). Connectedness and irreducibility of \(X\) are both preserved by extension to \(F\).

**Proof.** First recall explicitly the domain argument used in Section 1. If \(R,S\) are finite-type domains over \(k\) and \(u,v\ne0\) lie in \(R\otimes_k S\), expand both in finite linearly independent lists of elements of \(S\). Choose one nonzero coefficient from each expansion. Their product is nonzero in \(R\). The weak Nullstellensatz applied to the localization at that product gives a \(k\)-valued point of \(\operatorname{Spec}R\) where both expansions remain nonzero. Their specialized product is nonzero in \(S\), so \(uv\ne0\). Arbitrary domains are directed unions of finite-type subalgebras, and their tensor inclusions are injective over \(k\). Hence the tensor product of any two domains over an algebraically closed field is a domain.

Now let \(R\) be a finite-type \(k\)-algebra. Its spectrum has finitely many irreducible components: the Hilbert basis theorem makes it Noetherian, and a minimal closed subset failing to be a finite union of irreducible closed sets would split into two smaller closed subsets, a contradiction. Write these components as \(V(\mathfrak p_1),\ldots,V(\mathfrak p_n)\). Form the finite graph whose vertices are these components and whose edges mean nonempty intersection. The unions belonging to graph components are precisely the connected components of \(\operatorname{Spec}R\). Each such union is connected by successively adjoining intersecting connected sets, and distinct unions are disjoint closed sets whose finite union is the whole space, so each is also open.

After tensoring with \(F\), each \((R/\mathfrak p_i)\otimes_k F\) is a domain by the preceding paragraph. These irreducible closed subsets still cover the spectrum. Indeed, the product of the finitely many \(\mathfrak p_i\) is contained in the nilradical, and every element of the extended nilradical is nilpotent: any such element uses only finitely many nilpotent generators. Every prime upstairs therefore contains one of the extended \(\mathfrak p_i\). Intersections are preserved exactly, since

\[
(R/(\mathfrak p_i+\mathfrak p_j))\otimes_k F
\]

is nonzero exactly when \(R/(\mathfrak p_i+\mathfrak p_j)\) is nonzero. Thus the same graph computes the connected components upstairs. Its component unions, and therefore all clopen subsets and idempotents, come from \(R\).

For an arbitrary \(A\), an idempotent of \(A\otimes_k F\) involves finitely many elements of \(A\). Let \(R\subset A\) be the \(k\)-subalgebra they generate. The inclusion \(R\otimes_k F\hookrightarrow A\otimes_k F\) is injective, so the same element is already idempotent in \(R\otimes_k F\). The finite-type case supplies an idempotent of \(R\), and hence of \(A\), producing it. Injectivity follows from Lemma 2.A.

Apply this affine assertion on every chart of \(X\). The resulting idempotents agree on overlaps: cover an overlap by affine opens and use injectivity after extension. They therefore glue. This proves clopen descent and the connectedness assertion without assuming that \(X\) has a finite affine cover.

For irreducibility, suppose \(X\) is irreducible. Every nonempty affine chart has a coordinate ring with exactly one minimal prime. Its reduced quotient is a domain, whose tensor product with \(F\) is a domain by the first paragraph. The kernel introduced by passing to the reduction is a nil ideal even after tensoring, so the base-changed chart is irreducible. Any two nonempty affine charts of \(X\) intersect, and their inverse images intersect by surjectivity. These irreducible open subsets cover \(X_F\), which is therefore irreducible. \(\square\)

<a id="gs03-purely-inseparable-homeomorphism"></a>

**Lemma 2.C. Purely inseparable extensions.** If \(L/k\) is an algebraic purely inseparable extension, then \(X_L\to X\) is a homeomorphism for every \(k\)-scheme \(X\).

**Proof.** In characteristic zero the extension is trivial. In characteristic \(p>0\), put \(B=A\otimes_k L\) on an affine chart. For each \(b\in B\), there is a power \(q=p^r\) such that \(b^q\) belongs to the embedded copy of \(A\): expand \(b\) as a finite sum and take a common purely inseparable exponent for its coefficients. A prime of \(B\) over \(\mathfrak p\subset A\) must therefore contain \(b\) exactly when \(b^q\in\mathfrak p\). There is at most one such prime, and there is at least one by Lemma 2.A. Moreover, \(D_B(b)\) is the inverse image of \(D_A(b^q)\). The continuous bijection is thus open on basic opens and is a homeomorphism. The affine assertions agree on overlaps. \(\square\)

<a id="gs03-separable-closure-test"></a>

**Proposition 2.D. Testing geometric properties over a closure.** A \(k\)-scheme is geometrically connected if and only if it becomes connected over a separable closure \(k_s\). It is geometrically irreducible if and only if it becomes irreducible over an algebraic closure \(\bar k\).

**Proof.** The forward implications are part of the definitions. The extension \(\bar k/k_s\) is algebraic purely inseparable, so connectedness over \(k_s\) gives connectedness over \(\bar k\) by Lemma 2.C. Given any field extension \(F/k\), choose a common field extension \(\Omega\) of \(F\) and \(\bar k\): take a maximal quotient of the nonzero ring \(F\otimes_k\bar k\), into which both fields inject. Lemma 2.B makes \(X_\Omega\) connected whenever \(X_{\bar k}\) is connected. Its surjective projection onto \(X_F\) then makes \(X_F\) connected. This proves the first assertion. The same argument, using preservation of irreducibility in Lemma 2.B and the fact that a continuous image of an irreducible space is irreducible, proves the second. \(\square\)

<a id="gs03-galois-clopen-descent"></a>

**Lemma 2.E. Galois descent of a clopen partition.** Let \(L/k\) be a possibly infinite Galois extension, with group \(\Gamma\). A \(\Gamma\)-invariant open-and-closed subset of \(X_L\) is the inverse image of a unique open-and-closed subset of \(X\). On the inverse image of any affine open of \(X\), every clopen subset has a finite orbit under \(\Gamma\).

**Proof.** We first justify the field fact, also for an infinite extension. Fix an algebraic closure \(\Omega\) containing \(L\). A \(k\)-embedding \(\tau:E\to\Omega\), with \(k\subseteq E\subseteq L\), extends to \(L\): order its extensions to intermediate fields by inclusion. A chain has the union embedding as an upper bound, so a maximal extension exists by Zorn's lemma. If its domain \(M\) is not \(L\), take \(a\in L\setminus M\). Applying the embedding to the coefficients of the minimal polynomial of \(a\) gives an irreducible polynomial over the image of \(M\). Choose a root in \(\Omega\). Evaluation at that root extends the embedding to \(M(a)\), a contradiction. Thus the maximal domain is \(L\).

When \(L/k\) is normal, this extension maps \(L\) onto \(L\). Indeed, every element of \(L\) is a root of a polynomial over \(k\) that splits in \(L\); the embedding sends the finite set of distinct roots of that polynomial injectively into itself and therefore permutes that set. It follows both that its image is contained in \(L\) and that every element of \(L\) is in its image. If \(a\in L\setminus k\), its minimal polynomial has degree greater than one and, by separability, has a distinct root \(b\in L\). The embedding \(k(a)\to L\) sending \(a\) to \(b\) therefore extends to an element of \(\Gamma\) moving \(a\). This proves that the fixed field of \(\Gamma\) is exactly \(k\).

On \(\operatorname{Spec}A\), the clopen subset corresponds to an idempotent \(e\in A\otimes_k L\). Invariance of the subset gives invariance of \(e\), by uniqueness in Lemma 2.A. Expand \(e\) in a finite \(k\)-linearly independent list in \(A\). Invariance says that every coefficient in \(L\) is fixed by \(\Gamma\), and hence belongs to \(k\). Thus \(e\) lies in \(A\), where it is idempotent by injectivity.

These descended idempotents agree on all overlaps, again by checking after field extension on affine subopens. They glue, and surjectivity gives uniqueness of the descended subset. Finally, any idempotent on an affine chart uses finitely many coefficients in \(L\). Adjoin all the roots of their minimal polynomials over \(k\). Normality puts these finitely many roots in \(L\), and separability makes their splitting field \(E/k\) finite Galois. The subgroup fixing \(E\) fixes the idempotent. Its index is finite, since restriction embeds its coset set into the finite set of automorphisms of \(E/k\). Hence the orbit of the corresponding subset is finite. \(\square\)

<a id="gs03-geometrically-connected-morphism-criterion"></a>

**Theorem 2.F. A connected scheme receiving a geometrically connected scheme.** Let \(f:T\to X\) be a morphism of \(k\)-schemes. If \(T\) is geometrically connected and \(X\) is connected, then \(X\) is geometrically connected.

**Proof.** Set \(L=k_s\). Suppose that \(X_L=U\amalg V\) is a partition into two nonempty clopen subsets. The nonempty connected scheme \(T_L\) maps into one of them; rename them so that \(f_L(T_L)\subset U\). Set

\[
B=\bigcup_{\sigma\in\Gamma}\sigma(V),
\qquad A=X_L\setminus B=\bigcap_{\sigma\in\Gamma}\sigma(U).
\]

The set \(B\) is open. On the inverse image of an affine chart \(W\subset X\), Lemma 2.E says that the translates of \(V\cap W_L\) form a finite family. Thus \(B\cap W_L\) is also closed in \(W_L\). These charts cover \(X_L\), so \(B\) is globally closed and \(A\) is clopen. This local finiteness argument does not assert that there are only finitely many translates on all of \(X_L\).

Both sets are \(\Gamma\)-invariant. The set \(B\) contains \(V\), so is nonempty. Since \(f\) is defined over \(k\), its base-changed image is \(\Gamma\)-invariant. Its containment in \(U\) therefore puts it in every \(\sigma(U)\), hence in \(A\); this makes \(A\) nonempty. Lemma 2.E descends this partition to a nontrivial clopen partition of \(X\), contradicting connectedness. Thus \(X_{k_s}\) is connected, and Proposition 2.D proves the theorem. \(\square\)

<a id="gs03-relative-constants-geometric-irreducibility"></a>

**Proposition 2.G. No new algebraic constants.** Let \(K/k\) be any extension of fields such that every element of \(K\) algebraic over \(k\) belongs to \(k\). Then \(\operatorname{Spec}K\) is geometrically irreducible over \(k\). Neither finite generation nor separability of \(K/k\) is required.

**Proof.** Every monic irreducible \(P\in k[t]\) stays irreducible over \(K\). Indeed, the coefficients of a proper monic factor in \(K[t]\) are elementary symmetric expressions in some roots of \(P\), counted with multiplicity, in an algebraic closure of \(K\). They are algebraic over \(k\), hence belong to \(k\), which would give a proper factor over \(k\).

We recall the elementary primitive-element argument needed for finite separable extensions. Over an infinite field, if \(E=k(a,b)\) is finite separable, it has \([E:k]\) distinct embeddings in a normal closure: at each step of a tower an embedding extends in exactly as many ways as the number of distinct roots of the separable minimal polynomial. Choose \(c\in k\) outside the finitely many values for which two distinct embeddings take the same value on \(a+cb\). If the embeddings agree on \(b\), they disagree on \(a\), so they impose no forbidden value. Then \(a+cb\) has at least \([E:k]\) distinct conjugates, and therefore generates \(E\). Induction handles finitely many generators. Over a finite field, \(E\) is finite and \(E^\times\) is cyclic: its exponent \(m\) is attained by an element, by multiplying commuting elements with the largest prime-power orders; every element is a root of \(t^m-1\), so \(|E^\times|\le m\), forcing equality. A generator of \(E^\times\) also generates \(E\) as a field.

Consequently, for every finite separable extension \(E/k\), write \(E=k[t]/(P)\) with \(P\) monic irreducible. The first paragraph gives

\[
K\otimes_k E\cong K[t]/(P)
\]

as a field. Tensor inclusions are injective, so \(K\otimes_k k_s\) is the directed union of these fields and is itself a field. The passage from \(k_s\) to \(\bar k\) is purely inseparable; Lemma 2.C shows that \(\operatorname{Spec}(K\otimes_k\bar k)\) still has one point. It is irreducible, although it need not be reduced. Proposition 2.D now proves geometric irreducibility over \(k\). \(\square\)

<a id="gs03-connected-point-geometric-connectedness"></a>

**Corollary 2.H. A point with no new algebraic constants.** Let \(X\) be a connected \(k\)-scheme. If it has a point \(x\) such that \(k\) is algebraically closed in \(\kappa(x)\), then \(X\) is geometrically connected. In particular a connected scheme with a \(k\)-rational point is geometrically connected.

**Proof.** Proposition 2.G makes \(T=\operatorname{Spec}\kappa(x)\) geometrically irreducible, and hence geometrically connected. Apply Theorem 2.F to its canonical morphism \(T\to X\). For a rational point the residue field is \(k\), which satisfies the hypothesis. \(\square\)

The rational-point condition cannot be replaced by merely having a closed point: \(\operatorname{Spec}\mathbb C\) over \(\mathbb R\) has a closed point, but its residue field introduces the new algebraic constant \(i\). Nor does Proposition 2.G assert geometric reducedness. Connectedness, irreducibility and reducedness are distinct properties.

*References:* The Stacks project authors, in the AI Integrated Stacks Project edition, [geometrically connected schemes](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/varieties.tex), including the results indexed by Tags 0387, 056R and 04KV; [geometrically irreducible field extensions](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/algebra.tex), Tag 037P. The proofs above are independently written; the source authors retain credit for the cited results.

**Lemma 2.1.** An irreducible group scheme over a field is quasi-compact.

**Proof.** Theorem 1.3 makes it geometrically irreducible. Enlarge the field as in Lemma 1.2; quasi-compactness of this extension will imply quasi-compactness downstairs, since the projection is surjective. Choose a nonempty affine open \(U\).

For every rational point \(g\), irreducibility gives \(gU\cap U\ne\varnothing\). After making a residue-field extension if necessary, a point in the intersection writes \(g=u_1u_2^{-1}\). Thus the image \(UU^{-1}\) contains every rational point. It is open by Proposition 1.1. Its closed complement has no closed point, so Lemma 1.2 makes that complement empty. The morphism \(U\times U\to G\), \((u_1,u_2)\mapsto u_1u_2^{-1}\), is therefore surjective on underlying spaces. Its source is affine and quasi-compact. Its image \(G\) is quasi-compact. \(\square\)

**Theorem 2.2.** A connected group scheme over a field is irreducible.

**Proof.** By [Corollary 2.H](#gs03-connected-point-geometric-connectedness), a connected scheme with a rational point is geometrically connected. Thus a large algebraically closed extension preserves connectedness. It suffices to prove irreducibility there.

Let \(Z\) be the unique irreducible component through \(e\), with reduced structure. Multiplication preserves it: the image of the irreducible product \(Z\times Z\) is in a component and contains \(Z\). Inversion also preserves it, since it fixes \(e\). The product is reduced, so these set-theoretic containments give factorization through the reduced closed scheme \(Z\). Thus \(Z\) is a subgroup. Lemma 2.1 makes it quasi-compact.

Suppose there is another component \(Z'\). Theorem 1.3 makes \(Z\cap Z'=\varnothing\). Choose a quasi-compact open \(U\) containing \(Z\) and disjoint from \(Z'\), using a finite affine cover of the quasi-compact set \(Z\) inside its open complement. The image \(W=ZU\) is open and quasi-compact, contains \(Z\), and is saturated under multiplication by \(Z\), since \(Z(ZU)=ZU\).

Any component \(C\) meeting \(W\) has a rational point \(g\) in that intersection, by Lemma 1.2. Translation and uniqueness give \(C=Zg\); saturation then puts all of \(C\) in \(W\).

We claim \(W\) is closed. Because \(G\) is separated, its quasi-compact open immersion \(W\to G\) is quasi-compact on affine charts. On an affine chart, write \(W\) as a finite union of basic opens \(D(f_i)\). A point \(\mathfrak p\) in the closure of \(D(f_i)\) admits a prime \(\mathfrak q\subset\mathfrak p\) avoiding \(f_i\): otherwise \(f_i\) would be nilpotent in the localization at \(\mathfrak p\), and some neighbourhood of \(\mathfrak p\) would miss \(D(f_i)\). Hence every point of the closure of \(W\) is a specialization of a point of \(W\). Its irreducible component meets \(W\), so by the preceding paragraph is entirely in \(W\). This proves the claim.

Moreover \(W\) misses \(Z'\). If it met \(Z'\), a rational point in the intersection would lift, after field extension, to a product \(zu\) with \(z\in Z\), \(u\in U\). The component of \(zu\) is the same as that of \(u\), since multiplication by \(Z\) preserves each coset component. It would force \(Z'\cap U\ne\varnothing\), contrary to the choice of \(U\). Thus \(W\) is a nonempty proper open and closed subset, contradicting connectedness. \(\square\)

*References:* [Stacks, Tags 0B7P–0B7Q].

We use the canonical scheme structure on a connected component of a scheme: it is the unique structure for which its inclusion is a flat closed immersion [Stacks, Tags 04PW–04PX]. Connected components are closed under generalization as well as specialization, which is the criterion for this structure. A further part of that criterion says that every scheme morphism whose set-theoretic image lies in this closed subset factors through its canonical structure. It allows us to retain nilpotents in a component rather than replace the component by its reduction.

**Theorem 2.3. Identity component.** Every group scheme \(G/k\) has a canonical normal subgroup \(G^0\), whose underlying space is the connected component of \(e\). Its inclusion is a flat closed immersion; it is geometrically irreducible and quasi-compact. Formation of \(G^0\) commutes with extension of the field. If \(G\) is locally algebraic, \(G^0\) is also open.

**Proof.** Give the component of \(e\) its canonical flat closed structure. The identity factors through it. Inversion preserves its underlying connected component. Since it is connected and has a rational point, [Corollary 2.H](#gs03-connected-point-geometric-connectedness) makes it geometrically connected. Its product with itself is connected, and the multiplication image contains \(e\), so lies in that component. The factorization criterion for flat closed immersions therefore restricts multiplication and inverse to it. The group identities restrict too, since the inclusion is a monomorphism. It is a connected group scheme, so Theorem 2.2 makes it irreducible; Theorem 1.3 makes it geometrically irreducible; Lemma 2.1 makes it quasi-compact.

For a field extension \(K/k\), \(G^0_K\) is connected and contains \(e_K\). Conversely, the connected component of \(e_K\) in \(G_K\) projects into the connected component of \(e\) in \(G\). The flat closed factorization criterion puts it inside \(G^0_K\). These two containments, with uniqueness of the canonical flat closed structure, prove base-change compatibility.

Conjugation by any field-valued point preserves the connected component of the identity after that field extension. Thus the morphism \(G\times G^0\to G\), \((g,h)\mapsto ghg^{-1}\), has set-theoretic image in \(G^0\). The same factorization criterion proves normality schematically, on all test schemes.

Finally, for \(G\) locally of finite type, every affine chart is Noetherian. Its finitely many irreducible components are pairwise disjoint by Theorem 1.3, so each is open as well as closed in that chart. Thus the components of \(G\) are locally open. The identity component, already irreducible, is open. \(\square\)

The openness condition matters. Let \(C=\prod_{j\geq1}\mathbf Z/2\) with its profinite topology, and let \(B\) be the union of the rings \(k^{(\mathbf Z/2)^n}\), under pullback from the finite projection maps. Its Hopf algebra represents the inverse limit of those finite constant group schemes. A prime of \(B\) selects a compatible component of every finite product, so \(\operatorname{Spec}B\) has underlying space \(C\). Basic opens specify finitely many coordinates. Connected components are individual points, and the identity point is not open, because no finite list of coordinates isolates it. Hence \(G^0\) in this example is a flat closed copy of \(\operatorname{Spec}k\) that is not an open subgroup. Theorem 2.3 includes this example.

### 2.4. Components over an Artinian ring

**Proposition 2.4.** Let \(A\) be a local Artinian ring and \(G/A\) a group scheme locally of finite type. Its identity component is an open and closed normal subgroup \(G^0\), of finite type over \(A\), with geometrically irreducible special fibre. Every component of \(G\) is open and closed and of finite type over \(A\). The assertion does not require \(G\) to be flat. For any homomorphism of local Artinian rings \(A\to A'\), formation of \(G^0\) commutes with this base change. Every automorphism of the group \(G_T\), for any \(A\)-scheme \(T\), preserves \(G^0_T\).

**Proof.** Put \(k=A/\mathfrak m\). The nilpotent closed immersion \(G_k\to G\) is a homeomorphism. Theorem 2.3 and local Noetherianity show that the irreducible components of \(G_k\) are disjoint open and closed subsets. Their inverse images consequently give open and closed subschemes of \(G\). The component containing the identity has a geometrically irreducible special fibre. Multiplication, inverse and conjugation preserve that component on underlying spaces, as can be checked after reduction to the field. Factorization through an open subscheme then restricts these morphisms and proves the subgroup and normality assertions.

We check that every component \(C\) is quasi-compact; local finite type then makes it of finite type over \(A\). Choose a closed point of a nonempty affine open in \(C_k\). Its residue field is finite over \(k\). Choose a finite normal extension \(K/k\) containing that residue field, including its inseparable part. Every point above the chosen point is then \(K\)-rational, and there are only finitely many such points. Each component of \((C_k)_K\) maps onto \(C_k\): its generic point contracts to the generic point by flatness, and the projection is integral, so its image is closed. It therefore contains a point of that finite fibre. A component containing a rational point is a translate of \((G_k)^0_K\), hence is quasi-compact by Theorem 2.3. There are finitely many of these components and they cover \((C_k)_K\). This proves its quasi-compactness, then that of \(C_k\) by surjective projection, and then that of \(C\) by the homeomorphism.

For \(A\to A'\), the new special fibre is the old special fibre extended to the residue field of \(A'\). Theorem 2.3 identifies its identity component with the base change of \((G_k)^0\). Unique open subscheme structures give \((G_{A'})^0=G^0_{A'}\). More generally, on each field fibre over \(T\), an automorphism preserves the identity component. The same open-factorization argument, applied to the automorphism and its inverse, proves preservation of \(G^0_T\). \(\square\)

The characteristic-subgroup assertion also strengthens Theorem 2.3 over a field, without local finite type. Indeed, for a group automorphism \(\phi:G_T\to G_T\), field fibres put the image of \(G^0_T\) in \(G^0_T\). Its inclusion is a flat closed immersion, so the factorization criterion used in Theorem 2.3 factors \(\phi\) through it. Applying this to \(\phi^{-1}\) gives equality. Normality is the special case of inner automorphisms.

## 3. Turning finitely many components into an étale group

Assume in this section that \(G\) is of finite type. Over an algebraic closure \(\overline k\), it has finitely many open and closed components. Every component is a translate of \(G^0_{\overline k}\): choose a rational point on it and use translation and uniqueness. Multiplication and inverse give a group structure on the finite set of components,

\[
C=\pi_0(G_{\overline k}).
\]

This group structure is independent of the chosen points, because \(G^0\) is normal.

Let \(k^s\) be a separable closure and \(\Gamma=\operatorname{Gal}(k^s/k)\). Purely inseparable extension does not change the underlying components, so \(C\) is also the component set over \(k^s\). The descent action of \(\Gamma\) is by group automorphisms. It is continuous: the finitely many open and closed components descend to a finite separable extension, so an open subgroup of \(\Gamma\) fixes all of them. This is also [Stacks, Tags 038D–038E].

The equivalence between finite étale \(k\)-schemes and finite continuous \(\Gamma\)-sets now gives a finite étale scheme \(E\). The multiplication, inverse and identity on \(C\) are equivariant, so descend to group-scheme operations on \(E\). Denote it by \(\pi_0(G)\).

**Theorem 3.1.** There is a canonical homomorphism \(q:G\to\pi_0(G)\) and an exact sequence of fppf sheaves of groups

\[
1\longrightarrow G^0\longrightarrow G
\xrightarrow{q}\pi_0(G)\longrightarrow1.
\tag{1}
\]

The map \(q\) is faithfully flat and of finite presentation. Formation of this sequence commutes with field extension. It is universal for homomorphisms from \(G\) to finite étale group schemes.

**Proof.** Choose a finite separable extension on which the components of \(G\) are all geometrically connected and individually defined. The component-labelling map sends each open and closed component to its label in the constant scheme \(C\). It is a morphism, respects multiplication, and is compatible with the descent data. Descent gives \(q\). This construction also proves it is canonical.

Over \(\overline k\), the identity fibre is exactly \(G^0_{\overline k}\), with its open and closed scheme structure. Thus its schematic kernel downstairs is \(G^0\). Every fibre upstairs is a nonempty translate of \(G^0_{\overline k}\); mapping such a component to a point over a field is flat. Consequently \(q_{\overline k}\) is flat and surjective. These properties descend. Finite type over a field and the finite étale target also make \(q\) of finite presentation. It is therefore an fppf cover. Its sheaf map is surjective, and the kernel calculation proves (1); surjectivity here does not claim surjectivity on \(k\)-rational points.

For any field extension, geometric component sets and their descent actions identify in the construction, and Theorem 2.3 identifies the kernels. This gives base-change compatibility.

Finally let \(f:G\to F\) be a homomorphism with \(F\) finite étale. Over \(\overline k\), its target is discrete, so \(f\) is constant on each connected component. The resulting map \(C\to F(\overline k)\) is a group homomorphism compatible with descent. It gives a unique homomorphism \(\pi_0(G)\to F\) through which \(f\) factors. Uniqueness can also be checked after the faithfully flat cover \(q\). \(\square\)

**Example 3.2. Roots of unity over \(\mathbf Q\).** Factorization gives

\[
\mu_{3,\mathbf Q}
=\operatorname{Spec}\mathbf Q
\amalg\operatorname{Spec}\mathbf Q(\zeta_3).
\]

The identity component is the first factor, with the trivial group structure. The whole group is finite étale, so \(\pi_0(\mu_3)=\mu_3\). It is not constant over \(\mathbf Q\): its two nonidentity geometric points are interchanged by conjugation. Thus the two irreducible components over \(\mathbf Q\) become three components over \(\overline{\mathbf Q}\), and the second original irreducible component is not geometrically irreducible. Geometric irreducibility in Theorem 2.3 belongs specifically to \(G^0\).

For \(\mu_p\) in characteristic \(p\), the coordinate ring \(k[u]/(u^p)\) has one point. Thus \(G^0=\mu_p\) and \(\pi_0(G)=1\); the identity component includes its nilpotent structure.

## 4. Reduction and its limits

**Proposition 4.1.** Over a perfect field, \(G_{\mathrm{red}}\) is a closed subgroup of any group scheme \(G\). If \(G\) is locally algebraic, this subgroup is smooth.

**Proof.** A reduced scheme over a perfect field is geometrically reduced [Stacks, Tag 020I]. Thus \(G_{\mathrm{red}}\times_kG_{\mathrm{red}}\) is reduced. Every morphism from a reduced scheme to \(G\) factors through \(G_{\mathrm{red}}\), because nilpotent functions pull back to zero. Apply this to multiplication on that product, to inversion on \(G_{\mathrm{red}}\), and to the identity from \(\operatorname{Spec}k\). The group identities are inherited through the closed immersion. For a locally algebraic group, its reduction is also locally of finite type, and the perfect-field smoothness theorem of the preceding lesson applies. \(\square\)

Here is a counterexample to the subgroup assertion when perfectness is removed. It records an effect different from a reduced group failing to be smooth.

**Example 4.2. The reduced locus is not stable under multiplication.** Over \(k=\mathbf F_p(a)\), let

\[
B=k[x,y,z]/(x^p-ay^p,\ z^p).
\]

Define multiplication on triples by

\[
(x,y,z)(x',y',z')
=(x+x',\,y+y',\,z+z'+xy'-yx').
\tag{2}
\]

The last extra term is bilinear. Bilinearity gives its cocycle identity

\[
c(v,w)+c(v+w,u)=c(w,u)+c(v,w+u),
\]

which proves associativity. The identity is \((0,0,0)\), and the inverse is \((-x,-y,-z)\), since \(c(v,v)=0\). The equation \(x^p-ay^p=0\) is preserved by addition. Moreover

\[
(xy'-yx')^p
=x^py'^p-y^px'^p=0
\]

in the product algebra, using both copies of the first equation. Hence (2) also preserves \(z^p=0\), and defines a group scheme.

The algebra \(H=k[x,y]/(x^p-ay^p)\) is a domain by the inseparable valuation argument in *Lie algebras and smoothness of group schemes*. Since \(B=H[z]/(z^p)\), its nilradical is exactly \((z)\). Its reduction is the locus \(z=0\). But multiplying two universal points of that locus produces last coordinate

\[
xy'-yx'\ne0\quad\text{in }H\otimes_kH.
\]

Nonvanishing follows from the free basis \(x^ix'^j\), \(0\leq i,j<p\), over \(k[y,y']\): the two displayed terms have different basis indices and nonzero coefficients. Thus the reduction is not a subgroup. The calculation works also in characteristic two, where the two signs coincide but the basis terms remain distinct.

For an algebraic group over any field, smoothness is equivalent to geometric reducedness: if it is smooth its field extensions are reduced; if its algebraic-closure extension is reduced, the perfect-field theorem makes that extension smooth and smoothness descends. Reducedness over \(k\) alone is weaker.

**Example 4.3. Reduction need not be normal over a perfect field.** In characteristic \(p\), let \(G=\alpha_p\rtimes\mathbf G_m\), where scalars act on the additive coordinate. Its law is \((u,c)(v,d)=(u+cv,cd)\). Over a perfect field its reduction is the subgroup \(\{(0,c)\}\simeq\mathbf G_m\). On the universal test algebra \(k[u,c,c^{-1}]/(u^p)\), conjugation gives

\[
(u,1)(0,c)(-u,1)=((1-c)u,c).
\]

The first coordinate is nonzero in this algebra. Thus conjugation does not preserve the reduced subgroup. Reducedness and the subgroup property in Proposition 4.1 do not imply normality.

**Example 4.4. A smooth identity in the reduction can mislead.** Over \(k=\mathbf F_p(a)\), the kernel of the additive polynomial \(T^{p^2}-aT^p\) is a finite group scheme. The two factors \(T^p\) and \(T^{p(p-1)}-a\) are relatively prime. The second is irreducible over \(k\), by Eisenstein at \(a\) in \(\mathbf F_p[a][T]\). Thus its reduced scheme is the disjoint union of the rational identity and the spectrum of that inseparable field extension. Its reduction is étale at the identity. After algebraic closure, however, the additive polynomial is the \(p\)-th power of \(T^p-a^{1/p}T\), and the original kernel is nonreduced. Smoothness of the reduction at the identity cannot replace geometric reducedness of the original group in the smoothness criterion.

## 5. Closed subgroups, centrality and a manageable open subgroup

**Proposition 5.1.** If a homomorphism \(\psi:H\to G\) of group schemes over a field has open set-theoretic image \(S\), then that image is also closed.

**Proof.** Translation by every field-valued image point preserves \(S\), after the field extension in question. This follows from multiplying the lift in \(H\), and applies to inverse translation too. Let \(Z=G\setminus S\) with reduced closed structure. The image \(ZS\) is open by Proposition 1.1.

It is contained in \(Z\). Otherwise, after extending the residue fields to choose compatible lifts, a product \(zs\) with \(z\notin S\) and \(s\in S\) would be in \(S\); multiplying by a lifted inverse of \(s\) would put \(z\) in \(S\), a contradiction. Conversely \(Z\subset ZS\), because the identity belongs to \(S\). Hence \(ZS=Z\), and \(Z\) is open. Its complement \(S\) is closed. \(\square\)

**Proposition 5.2.** An immersion of group schemes over a field is a closed immersion.

**Proof.** Closedness can be checked after extending to an algebraic closure, because the field projection is an fpqc quotient map. Reduce source and target there without changing their topological spaces. By Proposition 4.1 they remain groups. Let \(L\) be the reduced closed scheme on the closure of the immersed image. The closure of the product of two subsets of schemes over a field is the product of their closures [Stacks, Tag 047B]. Thus continuity of multiplication puts \(L\times L\) in \(L\) set-theoretically; inversion preserves it too. These products are reduced, so the maps factor schematically through the reduced \(L\). It is a subgroup.

An immersion has locally closed image, which is open in its closure. Apply Proposition 5.1 to the induced homomorphism into \(L\). Its dense open image is also closed, hence equals \(L\). The original image is therefore closed. An immersion with closed image is a closed immersion, and descent gives the result over the original field. \(\square\)

*References:* [Stacks, Tags 047R–047T].

Centrality must be tested after all base changes. We define \(Z(G)(T)\) to consist of \(g\in G(T)\) whose conjugation automorphism of \(G_T\) is the identity.

**Proposition 5.3.** This centre functor is represented by a closed subgroup of \(G\).

**Proof.** The commutator morphism \(G\times G\to G\) has a closed identity fibre, by separatedness. Choose an affine chart \(U=\operatorname{Spec}A\) in the first factor and any affine chart \(V=\operatorname{Spec}B\) in the second. Its identity fibre on \(U\times V\) is defined by an ideal \(J\subset A\otimes_kB\). Choose a \(k\)-basis \((b_\lambda)\) of \(B\). Every equation in \(J\) has a unique finite expansion \(\sum a_\lambda\otimes b_\lambda\). Let \(I_U\subset A\) be the ideal generated by all such coefficients, for all equations and all charts \(V\).

For any \(A\)-algebra \(R\), the commutator of its parameter point with the universal point of every \(V_R\) is the identity exactly when every equation maps to zero in \(R\otimes B\). Independence of the basis says precisely that all its coefficients vanish in \(R\), or \(I_U R=0\). These universal points test identity of the conjugation morphism on the affine cover of \(G_R\). Thus \(\operatorname{Spec}(A/I_U)\) represents the centre functor over \(U\), on every base change.

The coefficient ideals commute with localization in \(A\), since both the equation ideal and its finite coefficient expansions do. They therefore agree on overlaps and glue to a closed subscheme of \(G\). Central elements are closed under multiplication and inverse on every test scheme, so it is a closed subgroup. \(\square\)

This coefficient proof requires no finite-dimensional coordinate ring. In particular it gives the assigned closed-centre result for locally algebraic groups [Stacks, Tag 0BF8].

**Proposition 5.4.** Every group scheme over a field has an open and closed subgroup containing \(e\) which is a countable union of affine opens.

**Proof.** Choose a quasi-compact open neighbourhood \(U\) of \(e\), and replace it by \(U\cap U^{-1}\). Separatedness keeps this intersection quasi-compact, and now \(U^{-1}=U\). Each image \(U^n\) under \(n\)-fold multiplication is open and quasi-compact. Their union \(G'\) is stable under multiplication and inverse: the set-theoretic assertion follows by lifting points to a common residue-field extension and concatenating or reversing their factors in \(U\). Since the union is open, this restricts the group morphisms to it. Proposition 5.1 makes it closed as well. Each \(U^n\), being quasi-compact and open, has a finite affine cover. Taking these covers for all positive integers \(n\) gives a countable affine cover of \(G'\). \(\square\)

The conclusion concerns this identity-containing subgroup [Stacks, Tag 047U]. The whole group need not have a countable affine cover: for an uncountable abstract group \(\Lambda\), the constant scheme \(\coprod_{\lambda\in\Lambda}\operatorname{Spec}k\) has only finite quasi-compact affine opens, and a countable union of them cannot cover its uncountably many points.

For a locally algebraic \(G\), the dimension lemma in *Lie algebras and smoothness of group schemes*, Lemma 3.1, proves that every irreducible component has the same finite dimension \(d=\dim G^0\). This follows from translation over an algebraic closure and invariance of dimension under field extension. At every closed point the local ring has dimension \(d\); this assertion concerns closed points, since the local ring at a generic point can have dimension zero. In particular \(d\leq\dim_k\operatorname{Lie}(G)\), with equality precisely for smooth \(G\), by that lesson's Theorem 3.2 [Stacks, Tag 045X].

### 5.5. Products of generic points

**Lemma 5.5. Generic factorization.** Let \(G\) be any group scheme over a field. Every point of \(G\) is the multiplication image of a point of \(G\times G\) whose two projections are generic points of irreducible components. No quasi-compactness or finite-type hypothesis is required.

**Proof.** For \(x\in G\), extend the base field to \(K=\kappa(x)\), so that \(x\) has a rational lift \(x_K\). Over \(K\), the fibre of multiplication at \(x_K\) is isomorphic to \(G_K\) by

\[
g\longmapsto(x_Kg^{-1},g).
\]

The second projection is the identity in this identification, and the first is inversion followed by translation. Both are isomorphisms, so a generic point of any component of this fibre projects to generic points of components of \(G_K\). A field-extension projection is flat. Going down therefore contracts a minimal prime to a minimal prime, so it sends these generic points to generic points of components of \(G\). Projecting the chosen point of the fibre to \(G\times_kG\) gives the required factorization of \(x\). \(\square\)

**Proposition 5.6. Quasi-compact dominant homomorphisms.** A quasi-compact dominant homomorphism \(f:G\to H\) of group schemes over a field is surjective on underlying spaces. If \(H\) is reduced, \(f\) is faithfully flat. The groups need not be affine, quasi-compact over the field, locally of finite type, or smooth. Dominant means that the image is dense; it need not initially be schematically dominant.

**Proof.** First, a quasi-compact dominant morphism of schemes hits every generic point of its target. To prove this, take an affine target neighbourhood \(\operatorname{Spec}A\) of such a point, with minimal prime \(\mathfrak p\), and a finite affine cover \(\operatorname{Spec}B_i\) of its inverse image. If the fibre over \(\mathfrak p\) were empty, each \(B_i\otimes_A\kappa(\mathfrak p)\) would be zero. The local ring \(A_{\mathfrak p}\) has its maximal ideal as nilradical, so every element of that ideal is nilpotent. It follows that \(B_i\otimes_AA_{\mathfrak p}=0\): the vanishing of the residue algebra would otherwise express \(1\) as a finite sum of multiples of nilpotent elements, itself nilpotent. For each \(i\), some \(s_i\notin\mathfrak p\) therefore vanishes in \(B_i\). Their product \(s\notin\mathfrak p\) vanishes on the full inverse image. The morphism's image in this affine neighbourhood is contained in \(V(s)\), contradicting density because \(D(s)\) is a nonempty open neighbourhood of \(\mathfrak p\). This proves the generic-point assertion.

Now take \(h\in H\) and apply Lemma 5.5 to find \(u\in H\times H\) mapping to \(h\), with generic projections \(\alpha,\beta\). Both fibres of \(f\) over those projections are nonempty. After extension to \(\kappa(u)\), they remain nonempty, and their product over this field is nonempty. Indeed choose residue fields of points in the two factors; their tensor product over the field is nonzero and has a prime. Consequently \(u\) has a lift \(v\in G\times G\) under \(f\times f\). The multiplication image of \(v\) maps to \(h\), proving surjectivity.

Suppose \(H\) reduced. At a generic point \(\alpha\), its local ring is a field, so \(f\) is flat at every point over \(\alpha\). Choose one such point \(g\). To transport flatness to an arbitrary \(z\in G\), take a common field extension \(K\) containing copies of \(\kappa(g)\) and \(\kappa(z)\); one can obtain it from a prime quotient of their nonzero tensor product over the base field. This gives rational lifts \(g_K,z_K\) in \(G_K\). Flatness at \(g\) survives this base change. Put \(a=z_Kg_K^{-1}\). Left translation by \(a\) on \(G_K\) and by \(f(a)\) on \(H_K\) intertwine \(f_K\). Their local-ring maps are isomorphisms, so \(f_K\) is flat at \(z_K\).

The local ring of \(G_K\) at \(z_K\) is faithfully flat over the local ring of \(G\) at \(z\). It is flat over the original target local ring as well, by the just-proved flatness and flat field base change on \(H\). Faithfully flat descent of module flatness makes \(f\) flat at \(z\). Explicitly, tensor any injection of target modules with the source local ring, and then with this faithfully flat extension; the final map is injective, so its preceding kernel is zero. Since \(z\) was arbitrary, \(f\) is flat everywhere. Together with surjectivity this is faithful flatness. \(\square\)

**Example 5.7. Two necessary hypotheses.** Quasi-compactness cannot be omitted in Proposition 5.6. Over \(k=\mathbf C\), map the constant group scheme \(\mathbf Q_k\) to \(\mathbf G_a\) by the usual inclusion of rational numbers. This is a group-scheme homomorphism, defined on each open and closed copy of \(\operatorname{Spec}k\). Its image is dense, because a nonzero polynomial has only finitely many roots, but it misses every irrational complex point. The morphism is not quasi-compact: the inverse image of the affine target is an infinite disjoint union of points.

Reducedness of the target is needed for the flatness conclusion. In characteristic \(p\), the identity inclusion \(1\to\alpha_p\) is quasi-compact and surjective on underlying spaces, since the target has one point. Its local ring map is \(A=k[t]/(t^p)\to k\). It is not flat: for \(I=(t)\subset A\), the nonzero module \(I\otimes_Ak=I/tI\) maps to zero under \(I\otimes_Ak\to A\otimes_Ak\). Thus the map fails to preserve this injection. Topological dominance alone does not prove faithful flatness for a nonreduced target.

### 5.8. Schematic images over a field

**Proposition 5.8.** A quasi-compact homomorphism \(f:G\to H\) of arbitrary group schemes over a field has a closed schematic image \(J\subset H\) which is a subgroup scheme. The factor \(G\to J\) is quasi-compact, schematically dominant and surjective. If \(G\) is reduced, then \(J\) is reduced and \(G\to J\) is faithfully flat. In particular a quasi-compact monomorphism with reduced source is a closed immersion. In characteristic zero, every quasi-compact group monomorphism is a closed immersion.

**Proof.** Both groups are separated by Proposition 1.1, so \(f\) is separated, hence quasi-separated. The finite affine-cover argument of *Group schemes, actions and Hopf algebras*, Lemma 4.4, applies to this quasi-compact, quasi-separated morphism. In particular \(f_*\mathcal O_G\) is quasi-coherent, and its formation commutes with flat base change. Set

\[
\mathcal I=\ker(\mathcal O_H\longrightarrow f_*\mathcal O_G),
\qquad J=V(\mathcal I).
\]

This is a quasi-coherent ideal. The induced map \(q:G\to J\) has injective structure-sheaf map, and is quasi-compact: on the affine cover of \(J\) obtained by intersecting it with affine opens of \(H\), its inverse images are the original quasi-compact inverse images. Flat base change preserves the injective structure-sheaf map, by flat base change for direct image and exactness of flat tensor product.

The map \(q\times q\) is schematically dominant. Factor it as \(G\times G\to G\times J\to J\times J\); each map is a flat base change of \(q\), because all schemes over a field are flat. The composite of schematically dominant maps is schematically dominant. The group identity
\(f\circ m_G=m_H\circ(f\times f)\) now makes \(m_H|_{J\times J}\) factor through \(J\): the pullback of every equation of \(J\) vanishes after the schematically dominant map \(G\times G\to J\times J\), so vanishes already on \(J\times J\). Inversion is treated in the same way, and the identity factors through \(J\) because it is the image of the identity of \(G\). Thus \(J\) is a subgroup.

Schematic dominance implies topological dominance. If a nonempty open of \(J\) missed the image, its nonzero structure sheaf would map injectively to zero on that open, which is impossible. Proposition 5.6 therefore makes \(q\) surjective. If \(G\) is reduced, the ring of sections on every open of \(G\) is reduced. Hence the kernel of the structure-sheaf map is radical on affine charts of \(H\), so \(J\) is reduced. Proposition 5.6 then gives faithful flatness.

If \(f\) is a monomorphism, so is \(q\). A faithfully flat quasi-compact monomorphism is an isomorphism: it is an fpqc cover with \(G\times_JG=G\), and the identity map on this cover descends to an inverse \(J\to G\). Descent of morphisms is the sheaf property of schemes, as in *Quotients and torsors*, Section 1. Thus \(f\) is a closed immersion. Finally, arbitrary characteristic-zero group schemes are geometrically reduced by *Lie algebras and smoothness of group schemes*, Theorem 4.4 and its complete Appendix A. The reduced-source case proves the last assertion. \(\square\)

The reduced-source hypothesis here concerns this proof of faithful flatness. Proposition 5.6 and Example 5.7 still distinguish topological dominance from schematic dominance when the target is nonreduced.

### 5.9. Locally finite-type monomorphisms

**Theorem 5.9.** A quasi-compact monomorphism between group schemes locally of finite type over a field is a closed immersion, in every characteristic, including nonreduced groups. More generally the same assertion holds over a local Artinian ring, with no flatness assumption on either group.

**Proof over a field.** Closed immersions descend under a field extension, so first work over an algebraic closure. Take the closed schematic image \(J\subset H\) of \(f:G\to H\) from Proposition 5.8. The factor \(q:G\to J\) is quasi-compact and schematically dominant. Reductions are group schemes over this perfect field. The reduced map is still a quasi-compact monomorphism, so Proposition 5.8 makes it a closed immersion. Its underlying image is the image of \(f\), which is the entire space of \(J\). Its reduced schematic image is consequently \(J_{\mathrm{red}}\), and

\[
G_{\mathrm{red}}\xrightarrow{\sim}J_{\mathrm{red}}.
\]

For an affine open \(V\subset J\), its inverse image is quasi-compact and locally Noetherian, with reduction isomorphic to the affine \(V_{\mathrm{red}}\). On a finite affine cover its nilradical is nilpotent; the largest of these finitely many bounds gives a nilpotent thickening globally. The affineness theorem used in Lemma 1.13 therefore makes \(q^{-1}V\) affine. Write its ring map as \(C\to B\). It is of finite type, since the source and target are locally of finite type over the field and this source chart is quasi-compact. Choose finitely many algebra generators \(b_i\). The reduction isomorphism writes each as \(b_i=c_i+n_i\), with \(c_i\) in the image of \(C\) and \(n_i\) nilpotent. Thus each generator satisfies a monic equation \((T-c_i)^{N_i}=0\); the finitely many bounded monomials span \(B\) over \(C\). It is a finite \(C\)-module.

Monomorphy gives \(B\otimes_CB\simeq B\) by multiplication. At a prime of \(C\), the finite fibre algebra is nonzero, since \(q\) is surjective. Its vector-space dimension \(r\) therefore satisfies \(r^2=r\), so \(r=1\) and the scalar map from the residue field is an isomorphism. The finite module \(\operatorname{coker}(C\to B)\) has zero fibre at every prime; local Nakayama makes it zero. Hence the ring map is surjective. Schematic dominance makes it injective as well, so \(q\) is an isomorphism. This proves the closed-immersion assertion over the algebraic closure, and faithfully flat descent proves it over the original field.

**Proof over the Artinian base.** Base change to the residue field preserves quasi-compactness, local finite type and monomorphy. The field result makes this base change a closed immersion. Lemma 1.13 detects closed immersions on the nilpotent special fibre, proving the assertion over the original base. \(\square\)

Example 5.7 shows why the quasi-compact hypothesis remains necessary even for reduced locally finite-type groups: the rational-number inclusion is a nonclosed monomorphism.

### 5.10. Closed images and dimensions over an Artinian ring

**Theorem 5.10.** Let \(A\) be local Artinian and \(f:G\to H\) a quasi-compact homomorphism of group schemes locally of finite type over \(A\). Its topological image is closed. The connected components of that image are irreducible and all have the same finite dimension. Moreover

\[
\dim G=\dim f(G)+\dim\ker f.
\]

Neither group is assumed flat over \(A\). The kernel is the represented scheme-theoretic kernel. Dimensions ignore nilpotents; the assertion about the image concerns its underlying closed subset.

**Proof.** The special-fibre homeomorphisms identify the source, target, kernel and image with their counterparts over the residue field. Over that field, Proposition 5.8 constructs the closed schematic image \(J\subset H\), with \(f:G\to J\) surjective. Thus the underlying image is \(|J|\). Since \(J\) is a locally finite-type group, Proposition 2.4 gives irreducible connected components, and *Lie algebras and smoothness of group schemes*, Lemma 3.1, gives their common finite dimension. The special-fibre homeomorphisms prove these topological assertions over \(A\).

For the formula extend the residue field to an algebraic closure. Schematic images in Proposition 5.8 commute with this flat base change, and the surjection to \(J\) remains surjective. Dimensions are invariant under field extension by the dimension result used in Lemma 3.1. We can therefore work over the algebraic closure. Take the reduced source \(G_{\mathrm{red}}\) and its closed schematic image \(J_{\mathrm{red}}\). They have the same underlying spaces as \(G\) and \(J\): the reduced image is reduced, and its underlying image is all of \(J\). Proposition 5.8 makes

\[
q:G_{\mathrm{red}}\longrightarrow J_{\mathrm{red}}
\]

faithfully flat. It is locally of finite type, and its local rings at the identities are Noetherian. The exact local formula in [*Flatness criteria, dimension and the flat locus*](../../AG-FSE/src/flatness-criteria.md), Theorem 3.1, gives

\[
\begin{aligned}
\dim\mathcal O_{G_{\mathrm{red}},e}
&=\dim\mathcal O_{J_{\mathrm{red}},e}\\
&\quad+\dim\mathcal O_{\ker q,e}.
\end{aligned}
\]

All three schemes are locally finite-type groups over this field. Their dimensions equal their identity local-ring dimensions, by Lemma 3.1 of the Lie-algebra lesson. The kernels of \(q\) and \(f\) have the same underlying space: reduction removes only nilpotents in the source, and both fibres impose the same identity point in the target. Thus their dimensions agree. This proves the displayed formula over the algebraic closure, and dimension invariance and the special-fibre homeomorphisms prove it over \(A\). \(\square\)

## 6. Why every algebraic group scheme is quasi-projective

This result concerns the underlying scheme, including its nilpotents. The proof first produces an ample line bundle on a smooth connected group. A finite Frobenius map then handles nilpotents in positive characteristic.

For a section \(s\) of an invertible sheaf \(L\), write \(X_s\) for its nonvanishing open. Recall that \(L\) is ample when the opens \(X_s\), allowing sections of positive powers of \(L\), form a basis of affine opens. For a finite-type scheme over a field, existence of an ample invertible sheaf is equivalent to quasi-projectivity [Stacks, Tags 01Q3, 01VT].

**Lemma 6.1.** Let \(X\) be quasi-compact and quasi-separated. If sections of an invertible sheaf \(L\) have affine nonvanishing opens covering \(X\), then \(L\) is ample. If \(f:Y\to X\) is finite and \(L\) is ample, then \(f^*L\) is ample.

**Proof.** Take a covering section \(s\). Inside the affine \(X_s\), principal opens \(D(a)\), for \(a\in\Gamma(X_s,\mathcal O_X)\), form a neighbourhood basis. Localization of sections of an invertible sheaf on a quasi-compact, quasi-separated scheme gives

\[
a=t/s^m,\qquad t\in\Gamma(X,L^{\otimes m}),
\]

for some \(m\geq0\) [Stacks, Tag 01PW]. The section \(ts\) of \(L^{\otimes(m+1)}\) vanishes outside \(X_s\), and inside \(X_s\) its nonvanishing locus is \(D(a)\). Thus these affine nonvanishing opens of powers of \(L\) form a basis, proving ampleness.

For the second assertion, choose finitely many affine nonvanishing opens of sections of positive powers of \(L\) covering \(X\). Replace their sections by powers to make their degrees a common positive integer \(N\). The inverse images are affine because \(f\) is finite, and they cover \(Y\). The first assertion makes \(f^*L^{\otimes N}\) ample. Nonvanishing opens of its powers are also those of powers of \(f^*L\), so \(f^*L\) is ample. \(\square\)

We will use three precise results about line bundles as prerequisites, rather than import a theorem about algebraic groups.

- On a Noetherian separated scheme, if \(U\) is dense affine and the local rings outside \(U\) are UFDs, its complement is the support of an effective Cartier divisor [Stacks, Tag 0BCW]. Regular local rings are UFDs [Stacks, Tag 0AG0].
- If \(X\) is a normal variety and \(V\) is a nonempty open subscheme of affine space, the restrictions of any invertible sheaf on \(X\times V\) at two rational points of \(V\) are isomorphic [Stacks, Tag 0BEH].
- If \(X_K\) has an ample invertible sheaf for a field extension \(K/k\), then \(X\) has an ample invertible sheaf [Stacks, Tag 0BDC].

**Theorem 6.2.** Every algebraic group scheme over a field is quasi-projective.

**Proof for a smooth connected group over an algebraically closed field.** Such a group \(G\) is an irreducible smooth variety by Theorem 2.3. Its local rings are regular, so the first prerequisite supplies an effective Cartier divisor \(D\) with nonempty affine complement \(U=G\setminus D\). The case \(D=0\), where \(G\) itself is affine, is included. For any finite list \(w_1,\ldots,w_n\in G(k)\), the complement of

\[
D w_1^{-1}\cup\cdots\cup D w_n^{-1}
\]

is affine: it is the intersection of the translated affine opens \(Uw_i^{-1}\), and finite intersections of affine opens in a separated scheme are affine.

Let \(d=\dim G\). Smoothness supplies a nonempty affine open chart \(W_0\subset G\) with an étale map to \(\mathbf A^d_k\). It is dominant and generically finite. After restricting to a nonempty principal open \(V\subset\mathbf A^d_k\), we may arrange that

\[
\pi:W\longrightarrow V
\]

is finite étale of a constant degree \(n>0\), where \(W\) remains a nonempty open in \(G\). Here is the finiteness step: over the generic point the coordinate algebra is finite; each of its finitely many algebra generators satisfies a monic equation over the fraction field. Inverting the finitely many denominators in these equations makes every generator integral over the base algebra, so the restricted algebra is finite. Étaleness is preserved by restriction.

On \(G\times W\), pull back \(D\) along \((g,w)\mapsto gw\), obtaining an effective Cartier divisor \(\mathcal D\). Multiplication is flat, since its shear identifies it with a projection over a field, so this pullback is indeed Cartier. Take the norm of this divisor along the finite étale map

\[
1\times\pi:G\times W\longrightarrow G\times V.
\]

We describe this norm directly. Étale locally on \(V\), the degree-\(n\) cover is a disjoint union of \(n\) copies of the base. Tensor the \(n\) line bundles of the pulled-back divisors, and multiply their canonical sections. Permutation of the sheets does not change this construction, so the line bundle and section descend to \(G\times V\). A product of nonzerodivisors is a nonzerodivisor; hence the descended section defines an effective Cartier divisor \(E\).

At \(v\in V(k)\), write \(\pi^{-1}(v)=\{w_1,\ldots,w_n\}\). The fibre construction is exactly

\[
E_v=\sum_{i=1}^n D w_i^{-1}.
\tag{3}
\]

In particular the restricted section is regular, and its nonvanishing locus \(G\setminus E_v\) is affine by the preceding intersection argument.

Every \(g\in G(k)\) avoids some \(E_v\). The bad set

\[
\{w\in W:gw\in D\}
\]

is proper closed in the irreducible \(W\): the open \(gW\) cannot be contained in the proper divisor support of \(D\). Its dimension is less than \(d\). Its image under the finite map \(\pi\) is closed and also has dimension less than \(d\), so it does not fill \(V\). Choose a rational \(v\) outside this image. Every point of its fibre is good, and (3) implies \(g\notin E_v\). For \(d=0\), the bad set is empty and the same conclusion holds.

Apply the second prerequisite to the invertible sheaf \(\mathcal O(E)\) on the normal variety \(G\times V\). All \(\mathcal O(E_v)\) have one isomorphism class; choose a representative \(L\) on \(G\). After choosing these isomorphisms, their canonical sections give sections \(s_v\) of \(L\). Their nonvanishing opens are the affine \(G\setminus E_v\), and cover all rational points of \(G\). They cover the scheme: otherwise their closed complement, nonempty in a finite-type scheme over an algebraically closed field, would have a rational point. Lemma 6.1 makes \(L\) ample.

**Passage to an arbitrary algebraic group.** First still assume \(k\) algebraically closed. There are finitely many open and closed components, all translated copies of \(G^0\). In characteristic zero, Lesson 2 makes \(G^0\) smooth, so the case just proved applies.

In characteristic \(p>0\), put \(H=(G^0)_{\mathrm{red}}\). It is a smooth connected group by Proposition 4.1. Choose \(r\) so large that \(n^{p^r}=0\) for every local section of the nilradical of \(G^0\). Such a uniform exponent exists because the scheme is Noetherian and quasi-compact. Relative Frobenius then factors as

\[
G^0\xrightarrow{f}H^{(p^r)}
\lhook\joinrel\longrightarrow(G^0)^{(p^r)}.
\tag{4}
\]

The factorization is schematic: the pullback of the nilradical of the twisted target sends a nilpotent \(n\) to \(n^{p^r}=0\). The map \(f\) is finite. On an affine chart over the perfect field \(k\), relative Frobenius is finite because each algebra generator is integral over the subalgebra of its \(p^r\)-th powers, and the monomials with exponents less than \(p^r\) span a finite module. Factoring this finite ring map through the quotient defining \(H^{(p^r)}\) preserves finiteness.

The target of \(f\) is smooth connected and hence has an ample line bundle. Its finite pullback is ample by Lemma 6.1. Thus \(G^0\), including its nilpotents, is quasi-projective.

Choose an ample line bundle on each of the finitely many components of \(G\). They combine into an invertible sheaf on \(G\). Sections on one component extend by zero on the others; their affine nonvanishing opens give a basis on the disjoint union. This sheaf is ample.

Finally, for general \(k\), apply this result to \(G_{\overline k}\). The third prerequisite descends existence of an ample invertible sheaf to \(G\). Finite type and Tag 01VT turn it into an immersion in some projective space. This proves quasi-projectivity over \(k\). \(\square\)

The argument proves the assigned result, not just its reduced or smooth case [Stacks, Tag 0BF7]. Neither the finite Frobenius step nor the descent step requires affineness of \(G\).

## 7. Orbits and their boundaries

For Theorem 7.1 and Example 7.2, \(k\) is algebraically closed, \(G\) is a smooth algebraic group, and \(X\) is a variety, meaning an integral separated finite-type \(k\)-scheme, equipped with a \(G\)-action. For \(x\in X(k)\), the **orbit map** is

\[
a_x:G\longrightarrow X,\qquad g\longmapsto gx.
\]

Its schematic stabilizer \(G_x\) is the fibre of this map over \(x\). It is a closed subgroup, but need not be smooth. We first establish the geometry of the orbit without assuming existence of a quotient \(G/G_x\).

<a id="gs03-smooth-identity-component"></a>

**Lemma 7.0. Components of a smooth algebraic group.** Let \(k\) be algebraically closed and let \(G/k\) be a smooth finite-type group scheme. Its irreducible components are pairwise disjoint open and closed integral subschemes. The component \(G^0\) containing the identity is the identity connected component, is a subgroup, and every component is \(gG^0\) for some \(g\in G(k)\).

**Proof.** Smooth finite-type schemes have regular local rings by [*Smooth algebras over a field and the Jacobian criterion*, Theorem 2.1](../../AG-CA/src/smooth-algebras-over-a-field-and-the-jacobian-criterion.md#2-the-criterion-and-its-open-locus). A regular local ring is a domain by [*Regular local rings*, Theorem 1.1](../../AG-CA/src/regular-local-rings.md#1-coordinates-graded-rings-and-regular-quotients), whose full initial-form argument is [*Regular sequences, depth and Cohen–Macaulay modules*, Theorem 6.1](../../AG-CA/src/regular-sequences-depth-and-cohen-macaulay-modules.md#6-regular-local-rings-and-complete-intersections). Thus a point of \(G\) lies on a unique irreducible component: the components through it correspond to the minimal primes of its local ring, which has just the prime \((0)\) as its minimal prime. The Noetherian scheme \(G\) has finitely many components. Disjointness then makes each component open as well as closed. With its open subscheme structure it is smooth and reduced, and irreducibility makes it integral.

Let \(C\) be the component through \(e\in G(k)\). The [product proof preceding Theorem 1.3](#gs03-algebraically-closed-products) makes \(C\times_kC\) irreducible. The multiplication morphism \(C\times_kC\to G\) has irreducible image containing \(e\), so its image lies in \(C\). Because \(C\subset G\) is open, this is a scheme-theoretic factorization through \(C\). Inversion also preserves \(C\), since it is an automorphism fixing \(e\). The restricted multiplication \(C\times_kC\to C\), inversion \(C\to C\), and identity \(\operatorname{Spec}k\to C\) satisfy the group identities, as their composites with the open immersion into \(G\) do. Consequently \(C\) is a subgroup scheme. It is connected, and the disjoint open and closed component decomposition shows that no larger connected subset contains it. Therefore \(C=G^0\).

Every component has a \(k\)-rational point by the Nullstellensatz applied to a nonempty finite-type affine open. For such a point \(g\), left translation \(t_g:G\to G\) is a \(k\)-scheme automorphism and sends the component containing \(e\) isomorphically onto the component containing \(g\). Thus this component is \(gG^0\), including its open subscheme structure. \(\square\)

**Theorem 7.1. Closed orbit lemma.** The set-theoretic image \(O_x\) of \(a_x\) is locally closed and has a canonical reduced locally closed scheme structure. Every orbit in \(\overline{O_x}\setminus O_x\) has strictly smaller dimension than \(O_x\). Consequently an orbit of minimum dimension is closed, every nonempty closed invariant subvariety contains a closed orbit, and every orbit closure contains a closed orbit.

**Proof.** Chevalley's theorem makes \(O_x\) constructible. In its reduced closure \(Y=\overline{O_x}_{\mathrm{red}}\), this dense constructible set contains a dense open subset \(U\). Translation by any \(g\in G(k)\) preserves \(O_x\) and \(Y\). Therefore

\[
V=\bigcup_{g\in G(k)}gU
\]

is open in \(Y\) and contained in \(O_x\). It contains every rational point of \(O_x\). Indeed, choose a rational \(u\in U\); both \(u\) and any rational \(y\in O_x\) have lifts in \(G(k)\), since a nonempty finite-type fibre over \(k\) has a rational point. Some \(g\in G(k)\) sends \(u\) to \(y\).

The difference \(O_x\setminus V\) is constructible. If it were nonempty, it would have a rational point, contradicting what we just proved. Thus \(O_x=V\), proving local closedness. Equip it with the reduced open structure in \(Y\).

The action restricts to this orbit scheme, not merely to its rational points. To check this, first use rational points to see that the image of \(G\times O_x\) lies in \(Y\) and avoids \(Y\setminus O_x\); a nonempty inverse image of that boundary would have a rational point. Both \(G\) and \(O_x\) are reduced over the perfect field \(k\), so their product is reduced by [the product proof preceding Theorem1.3](#gs03-algebraically-closed-products). The equations of \(Y_{\mathrm{red}}\) therefore vanish on it, and the action factors through \(Y\), then its open \(O_x\). The same argument makes \(Y\) invariant.

By [Lemma7.0](#gs03-smooth-identity-component), write the finitely many components of \(G\) as \(g_iG^0\). The images of \(G^0\) under \(a_x\) have irreducible closure \(Y_0\), because \(G^0\) is irreducible. The closure \(Y\) is the finite union of the translates \(g_iY_0\). These irreducible closed sets all have the same dimension \(d\); the distinct ones are exactly its irreducible components. The dense open \(O_x\subset Y\) has dimension \(d\).

Its boundary is proper closed in every component of \(Y\), hence has dimension strictly less than \(d\). It is invariant. Every orbit through a point of the boundary is contained in the boundary, so has dimension less than \(d\). This proves the dimension assertion.

Orbit dimensions are nonnegative integers. If a minimum-dimensional orbit had a nonempty boundary, a rational point in that boundary would give an orbit of smaller dimension. Thus it is closed. Apply the same argument among the orbits of any nonempty closed invariant subvariety, or of \(Y\), to obtain the remaining statements. \(\square\)

The same proof works for a reduced separated finite-type \(X\) with several components. The word “variety” only simplifies its presentation.

**Example 7.2. An orbit map with inseparable differential.** In characteristic \(p\), let \(\mathbf G_m\) act on itself by \(g\cdot x=g^p x\). There is a single orbit over an algebraically closed field. Its reduced orbit scheme is the smooth \(\mathbf G_m\), but its orbit map at \(1\) is \(g\mapsto g^p\), whose differential is zero and whose stabilizer is \(\mu_p\). Thus smoothness of the acting group does not make every stabilizer, or every orbit map, smooth.

### 7.3. Transitivity without a finiteness assumption

In this subsection the field \(k\), group scheme \(G\), and \(G\)-scheme \(X\) are arbitrary. We call the action **topologically transitive** when

\[
\begin{aligned}
\Phi&\colon G\times_kX\longrightarrow X\times_kX,\\
(g,x)&\longmapsto(gx,x).
\end{aligned}
\]

is surjective on underlying spaces. This condition is preserved by field extension. It does not assert that \(\Phi\) is flat or that \(X\) is a torsor. For example the trivial group acting on \(\alpha_p\) satisfies this condition, since both sides have one underlying point.

**Lemma 7.3. Tensor products of fields and normality.** If \(k\) is perfect and \(E,K\) are extensions of \(k\), every local ring of \(E\otimes_kK\) is a normal domain. Normality descends under a faithfully flat map of local rings.

**Proof.** Write \(E\) as the filtered union of its finitely generated subfields \(E_i\). Over a perfect field each \(E_i\) has a separating transcendence basis: it is finite separable over a purely transcendental field. Equivalently, it is a localization of a smooth \(k\)-algebra, by the field-theoretic criterion in [The Stacks Project, Tag 037X]. Its tensor product with \(K\) is a localization of a smooth \(K\)-algebra. Such an algebra has regular, hence normal, local rings. At a fixed prime of \(E\otimes_kK\), the corresponding local ring is the filtered colimit of these normal local domains. The transition maps are local and flat, hence faithfully flat and injective. An integral fraction and its monic equation involve only finitely many elements; they occur at one stage, where normality puts the fraction in that stage's local ring. The colimit is consequently a normal domain.

For descent, let \(R\to B\) be local and faithfully flat, with \(B\) a normal domain. Injectivity first makes \(R\) a domain. If \(a/b\) is integral over \(R\), it is integral over \(B\), and therefore lies in \(B\). The class of \(a\) in \(R/bR\) becomes zero in \(B/bB\). Faithful flatness detects this vanishing, so \(a\in bR\) and \(a/b\in R\). This proves normality of \(R\). \(\square\)

**Theorem 7.4. Local structure of a transitive space.** Suppose the action is topologically transitive. After extension to the perfect closure \(k^{\mathrm{perf}}\), the reduction of \(X\) has normal local rings. Over any extension field, every point of \(X\) lies on exactly one irreducible component. A component containing a \(k\)-rational point is geometrically irreducible.

If \(C\) is a reduced irreducible component of \((X_{k^{\mathrm{perf}}})_{\mathrm{red}}\), with generic point \(\eta\), and \(L\) is the algebraic closure of \(k\) in \(\kappa(\eta)\), then \(C\) is canonically an \(L\)-scheme and is geometrically irreducible over \(L\).

**Proof.** First let \(k\) be perfect. Reduction of \(G\) and \(X\) preserves the action and the surjectivity condition: their products are reduced over a perfect field, and their reductions have the same underlying spaces. We may thus work with reduced schemes. Pick a generic point \(\eta\) of any component and a point \(z\) of \(X\). Choose a point of \(X\times X\) projecting to \((z,\eta)\), and a preimage \(\gamma\) under \(\Phi\). With \(K=\kappa(\gamma)\), this gives rational points \(g,\eta',z'\) satisfying \(g\eta'=z'\). The local ring at \(\eta'\) is a localization of \(\kappa(\eta)\otimes_kK\), since \(\mathcal O_{X,\eta}=\kappa(\eta)\). It is normal by Lemma 7.3. Translation by \(g\) makes the local ring at \(z'\) normal. Its local map from \(\mathcal O_{X,z}\) is faithfully flat, so Lemma 7.3 descends normality to \(z\).

For general \(k\), pass to its perfect closure and reduce. That field extension is a universal homeomorphism. The local domain assertion above gives a unique component through each point, and the homeomorphism transfers this topological conclusion to \(X\). Repeating the argument after any field extension proves the geometric pointwise assertion.

Let \(C\) contain a rational point \(x\). Over an algebraic closure, each component of \(C_{\overline k}\) dominates \(C\) by flat going down. The projection is integral, so that component maps onto \(C\) and contains a point over \(x\). There is only one point over the rational \(x\), and it lies on a unique component of \(X_{\overline k}\). Components of \(C_{\overline k}\) are components of \(X_{\overline k}\), since the image of a larger component would be contained in the same maximal component of \(X\). Hence \(C_{\overline k}\) is irreducible. Irreducibility persists under further extension of the algebraically closed field by the product fact proved before Theorem 1.3. This gives geometric irreducibility over \(k\).

For the final assertion, the local rings of the reduced component \(C\) equal those of the reduced ambient scheme at its points: its defining minimal prime vanishes in the ambient local domain. They are therefore normal. Every \(\ell\in L\) is integral over every affine coordinate ring of \(C\), because it is algebraic over the ground field, and belongs to their common fraction field \(\kappa(\eta)\). Normality puts \(\ell\) in every one of these rings. These inclusions agree on overlaps and define the canonical \(L\)-structure. The field \(L\) contains \(k^{\mathrm{perf}}\) and is perfect.

Write \(F=\kappa(\eta)\). For any finite extension \(L'/L\), choose a primitive element and its irreducible polynomial \(P\). A monic factor of \(P\) over \(F\) has coefficients algebraic over \(L\), being symmetric expressions in its roots. They must lie in \(L\), by the definition of \(L\), so \(P\) stays irreducible. Thus \(F\otimes_LL'\) is a field. Taking the union gives a domain \(F\otimes_L\overline L\). Over the algebraically closed \(\overline L\), the product/domain argument preceding Theorem 1.3 shows that it remains a domain under every further field extension. Embedding an arbitrary extension of \(L\) into such an algebraically closed common extension proves that \(F\otimes_LK\) is a domain for every \(K/L\). Each affine coordinate ring of \(C\) embeds in \(F\), so its extension embeds in this domain. Intersections of nonempty affine opens remain nonempty after field extension. Their union \(C_K\) is therefore irreducible. \(\square\)

In particular the reduction of any group scheme over a perfect field is geometrically normal, without finite type: the theorem applied to its translation action gives normality, and the perfect-field geometric normality criterion of [The Stacks Project, Tag 037Y] gives preservation under every field extension.

**Lemma 7.5. Flatness of orbit maps.** For a group over a field acting on any scheme, flatness of the orbit map of a rational point at one point implies flatness everywhere. Consequently, under topological transitivity, the orbit map \(G_K\to X_K\) is flat whenever \(X_K\) is reduced. Here \(K\) is any extension field over which the chosen point is rational.

**Proof.** Take one source point where flatness is known. Over a common extension of its residue field and that of any other source point, both have rational lifts. Left translation on the group carries one lift to the other and intertwines their orbit maps with the corresponding action automorphism of the target. Flatness is preserved by this field base change and by these isomorphisms. Faithfully flat descent along the local field-extension map, exactly as in Proposition 5.6, proves flatness at the other source point.

For the consequence, transitivity makes the orbit map surjective, by taking the fibre of \(\Phi_K\) over its second coordinate. A generic reduced target local ring is a field, so the map is flat at every point above a generic point. The first assertion applies. \(\square\)

**Proposition 7.6. Saturation and connected components.** Under topological transitivity, for every open \(U\subset X\), the image \(G^0U\) is open and is the union of the irreducible components whose generic points belong to \(U\). If \(U\) is retrocompact, meaning its intersection with every affine open of \(X\) is quasi-compact, this saturation equals \(\overline U\) and is open and closed. An irreducible transitive space is quasi-compact. If \(X\) is quasi-separated, each connected component is irreducible. A component containing a rational point \(x\) is the surjective image of \(G^0\) under \(g\mapsto gx\).

**Proof.** The assertions about underlying spaces can be checked after passage to the perfect closure and reduction. Work there first. The saturation is open: it is the union, over field-valued points of \(G^0\), of the images of the open translates of \(U\) under the open field projections to \(X\). The group \(G^0\) preserves every component \(Z\). Indeed \(G^0\times Z\) is irreducible, its action image contains \(Z\) by the identity, and maximality of \(Z\) places the whole image in \(Z\).

Suppose \(\eta\), the generic point of \(Z\), belongs to \(U\), and let \(z\in Z\). Put \(K=\kappa(z)\). The orbit map at \(z_K\) is flat by Lemma 7.5. Let \(\omega\) be the generic point of \(G^0_K\). Its image \(t\) is in \(Z_K\). Choose a generic component point \(\beta\) of \(Z_K\) generalizing \(t\). Flat going down lifts \(\beta\) to a generalization of \(\omega\). Since \(\omega\) is already a generic point of a component of \(G_K\), it has no proper generalization; therefore \(t=\beta\). Its projection to \(Z\) is \(\eta\), again by flat going down, so \(t\in U_K\). Over the residue field of \(\omega\) we have \(\omega z\in U\), hence \(z\in G^0U\). Conversely every component meeting \(U\) has its generic point in \(U\), and component preservation gives the other containment. This proves the component description.

For retrocompact \(U\), its intersection with an affine chart is a finite union of basic opens. A point in the closure of such a union is a specialization of one of its points: in a localization at that point, a basic-open defining element which is not nilpotent avoids some prime. Choose a minimal prime below that prime. It is the generic point of a component meeting \(U\). Thus \(\overline U\) is the union of precisely the components just described, and equals the open saturation. If \(X\) is irreducible, a nonempty affine \(U\) has saturation all of \(X\). The source \(G^0\times U\) is quasi-compact, so its surjective image \(X\) is quasi-compact.

Now suppose \(X\) quasi-separated. An affine open is retrocompact. Fix a component with generic point \(\eta\). The closures of its affine neighbourhoods are open and closed, so contain the connected component of \(\eta\). Their intersection is \(\overline{\{\eta\}}\). To see this, for a point outside that closure choose an affine open \(V\) containing it and missing \(\eta\). Its saturation \(\overline V\) misses \(\eta\), by the component description. An affine neighbourhood of \(\eta\) inside the open complement of \(\overline V\) has closure still missing that point. Hence the connected component of \(\eta\) equals its irreducible component. These arguments descend through the homeomorphism, proving the statements over the original field too.

Finally let that component \(C\) contain a rational \(x\). Give \(C\) the canonical flat closed structure, obtained as the intersection of the clopen neighbourhoods just used; its local rings are the ambient local rings at its points. Theorem 7.4 makes it geometrically irreducible. It is preserved by \(G^0\). After perfect closure and reduction, flatness of the full orbit map and going down show that the generic point \(\omega\) of \(G^0\) maps to the generic point \(\eta\) of \(C\). For any \(z\in C\), the preceding orbit argument gives, after a field extension, \(a\in G^0\) with \(az\) lying above \(\eta\). The fibre of \(G^0\to C\) above \(\eta\) is nonempty; it remains nonempty after extension to the residue field of \(az\). Choose a further lift \(b\in G^0\) with \(bx=az\). Then \(z=(a^{-1}b)x\). Descent of this underlying-space surjectivity proves the last assertion. \(\square\)

**Example 7.7. An inseparable constant field which does not act.** Let \(k=\mathbf F_p(a)\) and

\[
X=\operatorname{Spec}A,\qquad
A=k[t]/(t^{p^2}-a^p).
\]

Translation by \(G=\alpha_{p^2}\) makes \(X\) a \(G\)-torsor: on \(X\times X\) the difference \(u=s-t\) satisfies \(u^{p^2}=0\), and \((u,t)\mapsto(t+u,t)\) is the inverse of the difference map. The map to the field is faithfully flat, since \(A\) is finite free and nonzero. The unique underlying point has residue field \(L=k(a^{1/p})\), the full algebraic constant field of its generic point. Nevertheless \(X\) admits no \(L\)-scheme structure compatible with \(k\).

Such a structure would supply \(z\in A\) with \(z^p=a\). Put \(k_0=\mathbf F_p(a^p)\) and \(y=t^p\). Expanding \(z\) in the basis \(1,t,\ldots,t^{p^2-1}\) shows that \(z^p\) belongs to the embedded subring

\[
B=k_0[y]/(y^p-a^p)\subset A.
\]

The elements \(1,y,\ldots,y^{p-1}\) are linearly independent over \(k\), by the displayed basis of \(A\). Therefore \(B\cap k=k_0\). But \(a\notin k_0\), so \(z^p=a\) is impossible. This proves the assertion. The reduction \(X_{\mathrm{red}}=\operatorname{Spec}L\) does have the \(L\)-structure. The field-structure conclusion of Theorem 7.4 is consequently stated for the reduced component after perfect closure; topological transitivity alone does not give that conclusion for a nonreduced component over an imperfect field. This corrects that unrestricted assertion in [Gabriel, SGA 3, Exposé VI A].

**Example 7.8. Connected over the ground field.** The constant group \(\mathbf Z/2\) over \(\mathbf R\) acts on \(X=\operatorname{Spec}\mathbf C\) by conjugation. It is a torsor: \(\mathbf C\otimes_{\mathbf R}\mathbf C\simeq\mathbf C\times\mathbf C\), with the two projections describing the identity and conjugation. The space \(X\) is connected and irreducible over \(\mathbf R\), but its group's identity component is trivial and cannot act transitively on \(X\times_{\mathbf R}X\), which has two points. The component's natural constant field is \(\mathbf C\); over that field \(X\times_{\mathbf C}X=X\), and the trivial group does act transitively. This explains the rational-point condition in the last assertion of Proposition 7.6.

**Lemma 7.9. Components under arbitrary field extension.** Let \(Y/k\) be irreducible, and let \(K/k\) be any field extension. Each irreducible component of \(Y_K\) maps onto \(Y\), without any finiteness hypothesis on the scheme or the extension.

**Proof.** Choose a transcendence basis \(T\) for \(K/k\), and put \(L=k(T)\). The scheme \(Y_L\) is irreducible. On an affine chart this follows by reducing its coordinate ring to a domain: polynomial extension and localization preserve a domain, and the nilradical remains nil after these operations. Intersections of nonempty charts remain nonempty after the faithfully flat field extension, so the assertion is global. The extension \(K/L\) is algebraic. The projection \(Y_K\to Y_L\) is flat and integral. Flat going down maps the generic point of a component to the generic point of \(Y_L\). The component is closed, and its integral projection has closed image, so that image is the whole \(Y_L\). Finally \(Y_L\to Y\) is surjective. Composing proves the assertion. \(\square\)

**Theorem 7.10. The canonical separable constant field.** Let \(X\) be a quasi-separated topologically transitive \(G\)-scheme, and let \(C\) be a connected component, with its canonical flat closed structure. Write \(\eta\) for its generic point, and let \(E\) be the separable algebraic closure of \(k\) in \(\kappa(\eta)\). Then \(C\) has a canonical \(E\)-scheme structure, is geometrically irreducible over \(E\), and the morphism

\[
G^0_E\times_EC\longrightarrow C\times_EC
\]

given by \((g,x)\mapsto(gx,x)\) is surjective. No finite-type or reducedness condition is imposed. Example 7.7 prevents replacing this separable field by the full algebraic closure of \(k\) in the generic residue field for a nonreduced component.

**Proof.** Proposition 7.6 makes \(C\) irreducible. Its canonical flat closed structure can be described explicitly. Intersect the clopen neighbourhoods of its generic point constructed in that proposition. On an affine chart take the sum of their clopen defining ideals. Their quotients are flat and form a filtered system, so the resulting quotient is flat. Its underlying subset is \(C\); at points of \(C\) all the clopen ideals have zero stalk, so its local rings are the ambient local rings. This construction also shows uniqueness and the factorization property already used in Theorem 2.3.

First take a finite separable subextension \(E_i/k\) of \(E\). The finite étale projection \(C_{E_i}\to C\) has finitely many irreducible components. Indeed every component maps onto \(C\) by Lemma 7.9, so has a point over \(\eta\); that fibre is a finite scheme. The components are pairwise disjoint by Theorem 7.4, applied to \(X_{E_i}\), and the flat closed inclusion of \(C_{E_i}\) gives it the same local rings as that ambient scheme at its points. Thus these finitely many components are clopen.

In the generic fibre, the chosen embedding \(E_i\hookrightarrow\kappa(\eta)\) selects the factor \(\kappa(\eta)\) of the finite étale algebra \(\kappa(\eta)\otimes_kE_i\). Let \(D_i\) be the component containing that point. It is a clopen finite étale \(C\)-scheme, of rank one at \(\eta\). Rank is locally constant, and \(C\) is connected, so its rank is one everywhere. A finite étale algebra of rank one is the base algebra: its unit map is an isomorphism on all residue fields and therefore on a neighbourhood of every point, by the determinant criterion for rank-one bundles. Hence \(D_i\to C\) is an isomorphism. Its inclusion into \(C_{E_i}\) is the graph of an \(E_i\)-structure on \(C\).

This structure is uniquely determined by the generic embedding. Any other such graph is a clopen section of the finite étale projection, and its generic point selects the same component \(D_i\); it is therefore the same graph. The structures for finite subextensions consequently agree on overlaps. Taking their union gives the canonical \(E\)-structure.

Put \(F=\kappa(\eta)\). The field \(E\) is separably algebraically closed in \(F\), since a separable algebraic extension of \(E\), which is itself separable algebraic over \(k\), is separable algebraic over \(k\). A nontrivial monic factor over \(F\) of an irreducible separable polynomial over \(E\) would have coefficients separably algebraic over \(E\), as symmetric expressions in its roots. Such coefficients in \(F\) must lie in \(E\), a contradiction. Therefore \(F\otimes_EE'\) is a field for every finite separable extension \(E'/E\). Passage to the separable closure gives a domain; subsequent purely inseparable extension to an algebraic closure preserves irreducibility by the universal homeomorphism of spectra. Over an algebraically closed field, irreducibility persists under further extension, by the product argument before Theorem 1.3. Faithfully flat projection from an algebraically closed common extension proves that \(F\otimes_EK\) has irreducible spectrum for every \(K/E\).

For an affine coordinate ring \(B\) of \(C\), its reduced domain embeds into \(F\). After tensoring with \(K\), it embeds into \(F\otimes_EK\). A subring of a ring whose nilradical is prime also has prime nilradical: nilpotence is reflected by an injective ring map. Hence that extended reduced domain has irreducible spectrum. The nil ideal of \(B\) stays nil after tensoring over a field, so \(B\otimes_EK\) is irreducible too. Intersections of nonempty affine opens stay nonempty under faithful field extension. Thus \(C_K\) is irreducible, proving geometric irreducibility over \(E\).

The \(G^0\)-action is \(E\)-linear. For each finite \(E_i/k\), compare the two maps \(G^0\times_kC\to\operatorname{Spec}E_i\) obtained from the action and projection. Their equality locus is clopen, because the diagonal of a finite étale scheme is clopen. It contains \(e\times C\). Its source is irreducible, since \(G^0\) is geometrically irreducible, so the equality locus is the whole source. This proves equality of the morphisms, including nilpotent tests. It holds for every finite subfield and hence for \(E\).

Finally extend \(E\) to a field \(K\). The closed subscheme \(C\times_EK\subset C\times_kK\) is the intersection of the clopen diagonal factors for all finite \(E_i\). It is flat and closed, by the same filtered-quotient construction. A component of \(X_K\) containing a point of this subset projects into the unique component \(C\) downstairs, so lies in \(C\times_kK\). Its connectedness keeps it in every one of those clopen factors. Since \(C\times_EK\) is irreducible, it is precisely that component, with its canonical structure. For any point of \(C\), extend to its residue field, viewed as an \(E\)-extension, and take its rational lift. Proposition 7.6 makes its component the surjective orbit of \(G^0\) over that field. These are the fibres of the displayed morphism over its second coordinate, so it is surjective. \(\square\)

### 7.11. Finite-type components and orbit dimensions

**Theorem 7.11.** Let \(A\) be local Artinian with residue field \(k\). Let \(G/A\) and the nonempty \(G\)-scheme \(X/A\) both be locally of finite type, and suppose

\[
G\times_AX\longrightarrow X\times_AX,
\qquad (g,x)\longmapsto(gx,x)
\]

surjective. Every connected component of \(X\) is open, irreducible and of finite type over \(A\), and all components have the same dimension. Over an algebraic closure \(\overline k\), let \(x\) be any closed point of \(X_{\overline k}\) and \(F\subset G_{\overline k}\) its scheme-theoretic stabilizer. The common component dimension is

\[
\dim G-\dim F.
\]

No flatness of \(G\) or \(X\) is assumed. The local-finite-type hypothesis on \(X\) is part of the statement.

**Proof.** The special-fibre homeomorphism reduces the topological assertions to \(k\). The finite-type assertion will lift by Lemma 1.13. First work over \(\overline k\). Replace \(G\) and \(X\) by their reductions. The reduced group acts on the reduced scheme: the product is reduced over this perfect field, so the action factors through the reduction. Transitivity persists, since these reductions have the same underlying spaces, also after the product. Write \(G'\) and \(X'\) for these reduced schemes.

Theorem 7.4 says that every point of \(X'\) belongs to exactly one irreducible component. On a Noetherian affine chart there are finitely many components. Removing all except the one through a chosen point gives an open neighbourhood contained in that component. Thus the components are open as well as closed, and they are the connected components. A locally Noetherian scheme is quasi-separated, because an intersection of two affine opens is an open subset of a Noetherian affine and is therefore quasi-compact.

For a component \(C'\), choose a closed point \(x\) of a nonempty affine chart in it. It is rational over \(\overline k\). Proposition 7.6 makes the orbit of \(x\) under \((G')^0\) surject onto \(C'\). The identity component is of finite type by Proposition 2.4, so its image is quasi-compact. As \(C'\) is locally of finite type, it is of finite type. Any two rational points of \(X'\) differ by a group element: their orbit fibre is a nonempty locally finite-type scheme over an algebraically closed field, and hence contains a rational point. Translation carries their components to one another, so all these components have the same dimension.

Return to \(k\). Theorem 7.4 and the same Noetherian-chart argument make the components downstairs irreducible and clopen. For a component \(C\), choose a component \(D\) of \(C_{\overline k}\). Lemma 7.9 gives a surjection \(D\to C\). The component \(D\) is one of the finite-type components just proved. Its image \(C\) is quasi-compact, hence finite type. The map is integral, so \(\dim C=\dim D\); this also descends the common dimension. Lifting each clopen component through the special-fibre homeomorphism gives the components of \(X/A\). Their finite type follows from Lemma 1.13.

For the formula, work again over \(\overline k\) with the reductions. The orbit map \(G'\to X'\) is surjective and flat by Lemma 7.5. Its restriction to \((G')^0\to C'\) is flat and surjective. Apply the local dimension formula of *Flatness criteria, dimension and the flat locus*, Theorem 3.1, at the identity and \(x\). At the closed point \(x\), the target local-ring dimension equals \(\dim C'\). This is the finite-type field formula in [*Krull dimension and Noether normalization*](../../AG-CA/src/krull-dimension-and-noether-normalization.md), Theorem 6.1; the residue-field transcendence degree is zero. The fibre at the identity has the same underlying space as \(F\cap G_{\overline k}^0\). This subgroup contains \(F^0\), so its identity local-ring dimension equals \(\dim F\), by the homogeneous-dimension lemma. The source identity local-ring dimension is \(\dim G\). Hence the local flat formula gives \(\dim C'=\dim G-\dim F\), and the preceding descent proves the assertion. \(\square\)

A nonempty one-point affine scheme with an infinitely generated nilpotent coordinate algebra illustrates why \(X\) must be locally of finite type here. The trivial group acts topologically transitively on it, because both products have one underlying point, but that scheme need not be of finite type.

### 7.12. Schematic orbit immersions

The orbit proof of Theorem 7.1 uses a smooth group and the reduced structure on the orbit. We now retain the whole scheme structure. The following elementary generic argument is the additional ingredient.

**Lemma 7.12. Generic recognition of a monomorphism.** Let \(f:Y\to X\) be a finite-type monomorphism between Noetherian schemes, and let \(Z\subset X\) be its schematic image. There is an open \(V\subset Z\), containing every generic point of \(Z\), for which \(f^{-1}(V)\to V\) is an isomorphism. No reducedness assumption is made.

**Proof.** We first check two algebraic facts. A nonempty finite-type monomorphism \(T\to\operatorname{Spec}F\), with \(F\) a field, is an isomorphism. Choose a closed point in a nonempty affine chart of \(T\); its residue field \(L\) is finite over \(F\). The base change \(T_L\to\operatorname{Spec}L\) has a section. A monomorphism with a section is an isomorphism: composing the section with the map gives the identity, since both this composite and the identity have the same image under the monomorphism. Isomorphisms descend along the faithfully flat extension \(L/F\). This proves the fact, including the absence of nilpotents in \(T\).

A finite monomorphism is a closed immersion. Indeed, on an affine target write it as \(\operatorname{Spec}B\to\operatorname{Spec}C\), with \(B\) finite over \(C\). Over each residue field its fibre is either empty or the spectrum of that same field, by the first fact. Thus \(C\to B\) is surjective after tensoring with every residue field. Its cokernel is a finite \(C\)-module; Nakayama at each prime makes that cokernel zero. The ring map is surjective, as claimed.

The ideal of the schematic image is quasi-coherent: \(f\) is quasi-compact and separated, and quasi-coherent direct image and its kernel have this property. The factorization \(Y\to Z\) is schematically dominant, and this remains so on open restrictions. Its topological image is dense in \(Z\). By the Noetherian Chevalley theorem, this image is constructible, so it contains every generic point of \(Z\). The same theorem applies to closed subsets of \(Y\). The exact provider is *Quasi-finite morphisms and Chevalley*, Theorem 4.2; its dense-constructible criterion is Theorem 3.1.

Fix a generic point \(\eta\) of \(Z\). Remove all other irreducible components and choose an affine neighbourhood \(\operatorname{Spec}C\) of \(\eta\). This neighbourhood has irreducible underlying space. There is a unique point \(y\) over \(\eta\), and the fibre is \(\operatorname{Spec}\kappa(\eta)\), by the first fact. Choose an affine neighbourhood \(W=\operatorname{Spec}B\) of \(y\) inside its inverse image. The closed complement of \(W\) in that inverse image has constructible image missing \(\eta\). Its closure is a proper closed subset: a dense constructible subset of an irreducible Noetherian space contains its generic point. Shrinking the target to a principal neighbourhood of \(\eta\) disjoint from this closure makes its entire inverse image a principal open of \(W\). We may therefore assume that the restricted map is the affine finite-type map \(\operatorname{Spec}B\to\operatorname{Spec}C\).

Put \(\mathfrak p=\eta\) and \(R=C_{\mathfrak p}\). Since \(\mathfrak p\) is minimal and \(C\) is Noetherian, \(R\) is a local Artinian ring. Its maximal ideal \(\mathfrak m\) has some power \(\mathfrak m^N=0\), and

\[
(B\otimes_C R)/\mathfrak m(B\otimes_C R)
\simeq\kappa(\eta).
\]

Choose finitely many algebra generators \(b_j\) of \(B\otimes_C R\). Their residues lift to elements \(r_j\in R\). Each \(b_j-r_j\) lies in \(\mathfrak m(B\otimes_C R)\), so \((b_j-r_j)^N=0\). Consequently every generator is integral over \(R\), and this algebra is finite over \(R\). Clearing the finitely many denominators in their monic equations gives \(s\in C\setminus\mathfrak p\) for which \(B_s\) is finite over \(C_s\). The resulting finite monomorphism is a closed immersion by the second fact. Schematic dominance makes \(C_s\to B_s\) injective as well as surjective, hence an isomorphism. Taking the union of these neighbourhoods for the finitely many generic points proves the lemma. The inverses agree on overlaps because they invert the same monomorphism. \(\square\)

**Theorem 7.13. The orbit with its full scheme structure.** Let \(k\) be any field, let \(G/k\) be a finite-type group scheme, and let \(G\) act on a finite-type \(k\)-scheme \(X\). For \(x\in X(k)\), let \(H=G_x\) be the schematic stabilizer. The fppf quotient \(Q=G/H\) is a finite-type scheme, and its canonical map

\[
i:Q\longrightarrow X,\qquad gH\longmapsto gx
\]

is an immersion. If \(X\) is quasi-projective, so is \(Q\). These assertions commute with every extension of \(k\). Neither \(G\) nor \(H\) is required to be smooth or reduced; \(G\) need not be affine.

**Proof.** The point \(x\) is a closed immersion \(\operatorname{Spec}k\to X\). Its inverse image under the orbit map \(a:G\to X\) is the closed subgroup \(H\). Theorem 11.1b of *Quotients and torsors* represents \(Q\) as a finite-type scheme, and gives the fppf torsor \(p:G\to Q\). The map \(a\) descends to \(i\). If two quotient sections have the same image in \(X\), lift both fppf locally to \(g,g'\in G\). Equality of their images says \(g^{-1}g'\in H\), so their quotient sections agree. Sheaf descent proves that \(i\) is a monomorphism on all test schemes.

Let \(Z\subset X\) be the schematic image of \(i\), equivalently of \(a\). For the equivalence, a function vanishes after pullback to \(Q\) precisely when it vanishes after the faithfully flat pullback to \(G\). The schematic image commutes with extension of the ground field: quasi-coherent direct image for a quasi-compact separated map commutes with flat base change, and flatness preserves its kernel. This is the exact direct-image result in *Group schemes, actions and Hopf algebras*, Lemma 4.4.

The action preserves \(Z\) schematically. To see this, form the automorphism

\[
G\times_kX\longrightarrow G\times_kX,
\qquad(g,z)\longmapsto(g,gz).
\]

The schematic image of \(1_G\times i\) is \(G\times_kZ\), by flat base change. Equivariance gives a commuting square with the analogous automorphism of \(G\times_kQ\). Thus this automorphism of \(G\times_kX\), and its inverse, preserve \(G\times_kZ\). Restricting it proves the required action on \(Z\).

Extend scalars to an algebraic closure \(\overline k\). Lemma 7.12 gives a nonempty open \(V\subset Z_{\overline k}\) over which \(i_{\overline k}\) is an isomorphism. Pick a rational point \(q_0\) in its inverse image. Every rational point \(q\in Q(\overline k)\) lifts to a rational point of \(G_{\overline k}\): its nonempty fppf fibre is finite type over the algebraically closed field. The action of \(G(\overline k)\) on \(Q(\overline k)\) is therefore transitive. In particular some element sends \(q_0\) to any prescribed \(q\).

Translate \(V\) by all these elements and put

\[
W=\bigcup_{g\in G(\overline k)}gV
\subset Z_{\overline k}.
\]

Each restriction \(i_{\overline k}^{-1}(gV)\to gV\) is an isomorphism by equivariance, and their inverses agree on overlaps. Their inverse images contain every rational point of \(Q_{\overline k}\). The complement is closed; if nonempty it would have a rational point, since it is finite type. Thus these inverse images cover the whole scheme. We obtain an isomorphism \(Q_{\overline k}\simeq W\), with the original scheme structures throughout.

Here is the descent of the open image. Set \(O=|i(Q)|\subset|Z|\). Images of morphisms commute with base change as subsets: points over two given residue fields have a common lift because their tensor product over the base residue field is nonzero. Hence the inverse image of \(O\) in \(Z_{\overline k}\) is \(W\). The projection \(Z_{\overline k}\to Z\) is open and surjective. For openness, every principal open on an affine chart is defined over some finite extension \(K/k\); its image agrees with the image of that principal open in \(Z_K\). The finite free projection \(Z_K\to Z\) is open by the following direct calculation. On a chart with ring \(C\), multiplication by \(b\in C\otimes_kK\) has a characteristic polynomial of degree \([K:k]\). Over a residue field, \(D(b)\) has a point precisely when \(b\) is not nilpotent in that finite-dimensional algebra. This is equivalent to some nonleading characteristic coefficient being nonzero: nilpotence gives the polynomial \(T^{[K:k]}\), and its converse follows from Cayley–Hamilton. Thus the image of \(D(b)\) is the union of the principal opens of those coefficients, and is open.

It follows that \(O\), the image of the open \(W\), is open in \(Z\). The map \(Q\to O\) becomes an isomorphism after faithfully flat extension to \(\overline k\), and is therefore an isomorphism. Its inverse descends uniquely as a morphism, by the fpqc sheaf property for schemes. Consequently \(i\) is the composite of the open immersion \(O\subset Z\) with the closed immersion \(Z\subset X\).

If \(X\) immerses into \(\mathbf P^n_k\), compose its immersion with \(i\). This exhibits \(Q\) as quasi-projective. Finally, the stabilizer, the quotient sheaf and its torsor relation, and immersions all commute with field extension. The stated scheme and quasi-projectivity conclusions persist. \(\square\)

The construction of the component group and the smooth orbit proof earlier in this lesson remain independent of quotient existence. Theorem 7.13 uses the later quotient theorem after those arguments; that theorem uses those earlier results, not Theorem 7.13.

**Example 7.14. An orbit can be a nonreduced closed subscheme.** In characteristic \(p>0\), let \(\alpha_p\) act on \(\mathbf A^1_k\) by addition, and take \(x=0\). The schematic stabilizer is trivial: on every test algebra the equality \(u+0=0\) forces \(u=0\). Thus \(G/H=\alpha_p\), and its orbit immersion is

\[
\operatorname{Spec}k[u]/(u^p)
\hookrightarrow\operatorname{Spec}k[t],
\qquad t\longmapsto u.
\]

The underlying orbit is the single point \(0\), but its ideal is \((t^p)\), not \((t)\). Replacing the schematic orbit by that reduced point would destroy the quotient and its monomorphism. In particular the word “variety” in an orbit statement must not silently impose reducedness when the acting group is allowed to be nonreduced.

## 8. Finite groups over a perfect field

A finite étale group scheme is the same as a finite abstract group with a continuous action of \(\operatorname{Gal}(k^s/k)\) by group automorphisms. This follows by applying the finite étale/Galois equivalence to multiplication, inverse and identity; all must be equivariant. Continuity says that an open subgroup acts trivially on this finite group.

A finite group scheme is **infinitesimal** if it becomes a one-point scheme over an algebraic closure. Its coordinate ring is then a finite local algebra with nilpotent augmentation ideal and residue field \(k\).

**Theorem 8.1.** Let \(k\) be perfect and \(G/k\) finite. Its connected group \(G^0\) is infinitesimal. The restriction \(G_{\mathrm{red}}\to\pi_0(G)\) is an isomorphism, giving a canonical subgroup section \(s:\pi_0(G)\to G\). Conjugation by this section gives an isomorphism

\[
G^0\rtimes\pi_0(G)\xrightarrow{\ \sim\ }G,\qquad
(h,c)\longmapsto h\,s(c).
\tag{5}
\]

**Proof.** Proposition 4.1 makes \(G_{\mathrm{red}}\) a smooth finite subgroup. A finite smooth scheme over a field is finite étale, since its relative dimension is zero. Over \(\overline k\), the reduction of each connected finite component is a single reduced point. Thus \(G_{\mathrm{red}}\to\pi_0(G)\) is a bijection between finite étale schemes on geometric points. The finite étale/Galois equivalence makes it an isomorphism over \(k\), and its inverse followed by inclusion supplies \(s\). It is a group homomorphism.

The finite connected \(G^0\) is geometrically connected by Theorem 2.3, so its finite geometric fibre has one point. Its coordinate ring is local Artinian. Its residue extension of \(k\) is finite purely inseparable, since a separable residue extension would split into more than one geometric point. Perfectness makes that residue field \(k\). The unique maximal ideal is therefore the augmentation ideal, and is nilpotent. This is the stated infinitesimal structure.

Define \(\alpha_c(h)=s(c)h\,s(c)^{-1}\). Normality of \(G^0\) makes this an action of \(\pi_0(G)\) by group automorphisms. The multiplication in the semidirect product is

\[
(h,c)(h',c')=(h\,\alpha_c(h'),\,cc').
\]

Formula (5) respects this multiplication. Its inverse on every test scheme is

\[
g\longmapsto\bigl(g\,s(q(g))^{-1},\,q(g)\bigr).
\tag{6}
\]

The first factor has \(q\)-image the identity, so it factors schematically through the kernel \(G^0\). Formulas (5) and (6) are mutually inverse morphisms; their equalities hold on all test schemes, including those with nilpotents. \(\square\)

This need not be a direct product: the étale part can act nontrivially on the infinitesimal part. For example, for \(p>2\), the constant group \(\mathbf F_p^\times\) acts on \(\alpha_p\) by scalar multiplication. The resulting finite group has underlying scheme \(\alpha_p\times\mathbf F_p^\times\) and law

\[
(u,c)(v,d)=(u+cv,cd).
\]

Its identity component is \(\alpha_p\), its component group is the constant \(\mathbf F_p^\times\), and these factors do not commute.

For \(\mu_p/\mathbf F_p\), the coordinate \(u=t-1\) gives \(\mathbf F_p[u]/(u^p)\). The augmentation ideal \((u)\) is nilpotent. Thus \(\mu_p\) is connected infinitesimal, its component group is trivial, and (5) reduces to \(G=G^0\).

## 9. Two geometric examples

### Orthogonal groups

Let \(\operatorname{char}k\ne2\) and \(n\geq1\). On \(k^n\) use \(q(v)=v^{\mathsf T}v\) and \(b(v,w)=v^{\mathsf T}w\). Define

\[
O_n(R)=\{g\in\mathrm{GL}_n(R):g^{\mathsf T}g=I\},
\qquad SO_n=\ker(\det:O_n\to\mu_2).
\]

The target \(\mu_2\) is the constant group \(\{1,-1\}\), since \(2\) is invertible. The determinant fibres are open and closed. For a vector \(v\) with \(q(v)\ne0\), reflection in its perpendicular hyperplane is

\[
r_v(w)=w-\frac{2b(w,v)}{q(v)}v.
\tag{7}
\]

It fixes \(v^\perp\), sends \(v\) to \(-v\), and has determinant \(-1\). Formula (7) depends regularly on \(v\) on the irreducible open

\[
P=\{v\in\mathbf A^n:q(v)\ne0\}.
\]

**Proposition 9.1.** The group \(SO_n\) is smooth and geometrically irreducible. Thus \(O_n\) has two geometric components, \(O_n^0=SO_n\), and \(\pi_0(O_n)\) is the constant \(\mathbf Z/2\).

**Proof.** Work first over an algebraic closure. Every orthogonal transformation is a product of at most \(2n\) reflections. To prove this, choose a nonisotropic \(v\). For \(g\in O_n(k)\),

\[
q(gv-v)+q(gv+v)=4q(v)\ne0.
\]

If \(q(gv-v)\ne0\), direct substitution in (7) shows \(r_{gv-v}(gv)=v\). Otherwise \(q(gv+v)\ne0\), and \(r_{gv+v}(gv)=-v\); applying \(r_v\) next sends it to \(v\). After at most two reflections, the transformation fixes \(v\). It restricts to an orthogonal transformation of the nondegenerate space \(v^\perp\); induction on dimension proves the bound.

For determinant \(1\), the number of reflections in such a product is even. Inserting pairs \(r_w r_w=1\) pads it to exactly \(2n\). Consequently the morphism

\[
P^{2n}\longrightarrow SO_n,\qquad
(v_1,\ldots,v_{2n})\longmapsto r_{v_1}\cdots r_{v_{2n}}
\]

contains every rational point of \(SO_n\) in its image. Its source is irreducible; its image closure is therefore irreducible. Rational points are dense in this finite-type scheme over an algebraically closed field, so that closure is the whole underlying space of \(SO_n\). This proves irreducibility.

Smoothness can be checked near the identity by the Cayley transform. Let \(X\) vary over skew-symmetric matrices with \(\det(I+X)\ne0\). Then

\[
g=(I-X)(I+X)^{-1}
\tag{8}
\]

satisfies \(g^{\mathsf T}g=I\). Its determinant is \(1\), because
\(\det(I-X)=\det((I-X)^{\mathsf T})=\det(I+X)\). Conversely, on the open \(\det(I+g)\ne0\) in \(SO_n\),

\[
X=(I-g)(I+g)^{-1}
\]

is skew-symmetric and inverts (8). These identities are polynomial identities after the displayed determinants are inverted, so apply to arbitrary \(k\)-algebras. This open neighbourhood of the identity is an open in the vector space of skew-symmetric matrices, and is smooth. Translation gives smoothness at every rational point. The complement of the smooth locus is closed and, if nonempty, has a rational point; hence \(SO_n\) is smooth everywhere.

The fixed reflection \(r_{e_1}\) translates \(SO_n\) isomorphically onto the determinant-\(-1\) fibre. Thus these two fibres are exactly the geometric components, and both are smooth. Descending smoothness and using Theorems 2.3 and 3.1 gives all assertions over the original field. \(\square\)

The reflection \(r_{e_1}\) also provides a subgroup section of the determinant map. Hence

\[
O_n\simeq SO_n\rtimes\mathbf Z/2.
\]

Here \(n\geq1\) is essential: \(O_0\) is the trivial group and has one component.

### Matrix conjugacy

Let \(k\) be algebraically closed. The smooth group \(\mathrm{GL}_n\) acts on the affine space \(M_n\) by conjugation. A matrix is semisimple when it is diagonalizable over \(k\).

**Proposition 9.2.** A conjugacy orbit in \(M_n\) is closed if and only if its matrices are semisimple.

**Proof.** If \(A\) is semisimple, list its distinct eigenvalues as \(\lambda_1,\ldots,\lambda_r\), with multiplicities \(m_1,\ldots,m_r\). Put

\[
f(T)=\prod_{i=1}^r(T-\lambda_i),\qquad
P(T)=\prod_{i=1}^r(T-\lambda_i)^{m_i}.
\]

The equations \(f(B)=0\) and \(\det(TI-B)=P(T)\), by equality of coefficients, define a closed subset of \(M_n\). Since \(f\) has distinct roots, any rational matrix satisfying \(f(B)=0\) is diagonalizable, and its characteristic polynomial prescribes these multiplicities. It is therefore conjugate to \(A\). Conversely every conjugate satisfies the equations. By Theorem 7.1 the orbit is constructible; any nonempty constructible difference between this closed set and the orbit would have a rational point. There is none, so the orbit is this closed set.

If \(A\) is not semisimple, put it in Jordan form. In a block of size \(r\), conjugation by

\[
\operatorname{diag}(t^{r-1},t^{r-2},\ldots,t,1),\qquad t\ne0,
\]

multiplies every entry on the superdiagonal by \(t\). Applying this to all blocks gives conjugates \(A(t)=S+tN\), where \(S\) is the diagonal matrix of eigenvalues and \(N\ne0\) is the block nilpotent part. The polynomial family extends to \(t=0\), giving the semisimple matrix \(S\). It lies in the orbit closure but is not conjugate to \(A\), because diagonalizability is invariant under conjugation. Thus the orbit is not closed. \(\square\)

This example shows concretely how a boundary orbit can have smaller dimension: deleting a nilpotent Jordan part enlarges the centralizer and reduces the conjugacy orbit. The closed orbit lemma ensures existence of a closed orbit in a closure; here the explicit degeneration identifies one.

## 10. Exercises

The first five exercises address the core computations and theorems. Exercises 6–11 test the distinctions that prevent incorrect extensions of those theorems.

**Exercise 1 — Easy: arithmetic components.** For \(G=\mu_{3,\mathbf Q}\), compute \(G^0\) and \(\pi_0(G)\). Describe the Galois action on geometric components. Then make the same computations for \(\mu_p\) over \(\mathbf F_p\). Explain why the number of irreducible components over the ground field does not by itself determine the component group.

**Exercise 2 — Medium: orthogonal components.** Let \(n\geq1\) and \(\operatorname{char}k\ne2\). Compute \(O_n^0\) and \(\pi_0(O_n)\), and construct a group-scheme section of the component map. Explain the roles of the reflection parameter space and the Cayley transform. What changes for \(n=0\)?

**Exercise 3 — Medium: geometric reducedness.** Prove that an algebraic group scheme \(G/k\) is smooth if and only if \(G_{\overline k}\) is reduced. Show why “\(G\) is reduced” cannot replace geometric reducedness, using \(x^p-ay^p=0\) over \(\mathbf F_p(a)\).

**Exercise 4 — Medium: open images.** Let \(\psi:H\to G\) be a homomorphism of algebraic group schemes with open image \(S\). Prove that \(S\) is closed, carefully accounting for points whose residue fields differ from \(k\). Deduce that an open subgroup is closed. Does this imply that \(\psi\) is surjective on \(k\)-rational points of \(S\)?

**Exercise 5 — Hard: a closed orbit.** Let a smooth algebraic group act on a variety over an algebraically closed field. Prove that each orbit is locally closed, that every orbit in its boundary has smaller dimension, and that its closure contains a closed orbit. Use matrix conjugation to exhibit a nonclosed orbit and a closed orbit in its boundary.

**Exercise 6 — Hard: failure of reduction as a subgroup.** Over \(k=\mathbf F_p(a)\), use the equations
\[
x^p-ay^p=0,\qquad z^p=0
\]
and law (2) to construct an affine group whose reduction is not a subgroup. Verify associativity, the equations, the inverse, the nilradical and the nonvanishing obstructing reduced multiplication. Include characteristic two.

**Exercise 7 — Medium: finite splitting need not commute.** For \(p>2\), define \(G=\alpha_p\rtimes\mathbf F_p^\times\) by the law in Section 8. Compute \(G^0\), \(G_{\mathrm{red}}\), and \(\pi_0(G)\). Give the isomorphism and inverse in (5)–(6) explicitly, and show that \(G\) is not commutative.

**Exercise 8 — Hard: the limits of general topology.** For the inverse limit of the constant groups \((\mathbf Z/2)^n\), show that its identity component is not open. For an uncountable constant group \(\Lambda\), show that its group scheme has no countable affine cover. Explain why these examples agree with Theorem 2.3 and Proposition 5.4.

**Exercise 9 — Hard: components without flatness.** Let \(A=k[\epsilon]/(\epsilon^2)\), and give \(H=\operatorname{Spec}A[x]/(\epsilon x)\) the additive group law. Show that it is not flat over \(A\). For \(G=H\times(\mathbf Z/2)_A\), identify its components and check Proposition 2.4, including base change to \(k\).

**Exercise 10 — Hard: image and inseparability.** Over a characteristic-\(p\) field, compute the schematic image, kernel and differential of \(F:\mathbf G_a\to\mathbf G_a\), \(x\mapsto x^p\). Prove faithful flatness directly from its coordinate algebra. Explain why the closed-monomorphism conclusion of Proposition 5.8 does not make \(F\) an isomorphism. Contrast it with the dense map \(\mathbf Q_{\mathbf C}\to\mathbf G_{a,\mathbf C}\) in Example 5.7.

**Exercise 11 — Hard: constants in a thick point.** Take \(k=\mathbf F_2(a)\) and \(X=\operatorname{Spec}k[t]/(t^4-a^2)\). Prove that \(X\) is an \(\alpha_4\)-torsor and geometrically irreducible. Compute its residue field and show that it has no compatible action of that residue field as scalars. Compute its reduction after perfect closure and explain which conclusion of Theorem 7.4 applies.

## 11. Solutions

**Solution 1.** The factorization
\[
T^3-1=(T-1)(T^2+T+1)
\]
has relatively prime factors over \(\mathbf Q\). The second is irreducible. Thus \(\mu_3\) is the disjoint union of the identity point \(\operatorname{Spec}\mathbf Q\) and \(\operatorname{Spec}\mathbf Q(\zeta_3)\). The identity component is the trivial group. All three roots over \(\overline{\mathbf Q}\) are simple, so \(\mu_3\) is finite étale and its component map is the identity: \(\pi_0(\mu_3)=\mu_3\).

The three geometric components have group law given by multiplication of roots. Complex conjugation fixes \(1\) and exchanges \(\zeta_3,\zeta_3^2\), so this group scheme is not the constant group of order three over \(\mathbf Q\). The two ground-field components are Galois orbits of the three geometric ones; they are not themselves a group of order two.

In characteristic \(p\), write \(u=T-1\). Then
\[
T^p-1=u^p,\qquad
\mathcal O(\mu_p)=\mathbf F_p[u]/(u^p).
\]
This local algebra has a single point with residue field \(\mathbf F_p\), and the same remains true over an algebraic closure. Hence \(\mu_p^0=\mu_p\), while \(\pi_0(\mu_p)=1\). The nilpotent identity neighbourhood contributes no extra geometric component.

**Solution 2.** Determinant defines a homomorphism \(O_n\to\mu_2=\{1,-1\}\). Its two fibres are open and closed, and both are nonempty: \(I\) has determinant \(1\), while
\[
r=\operatorname{diag}(-1,1,\ldots,1)
\]
has determinant \(-1\). Also \(r^2=I\), so the map from the constant \(\mathbf Z/2\) sending its generator to \(r\) is a group-scheme section.

To see there are no further geometric components, extend to an algebraic closure. For nonisotropic \(v\), the reflection \(r_v\) has determinant \(-1\). The reflection induction in Proposition 9.1 expresses every determinant-\(1\) matrix as an even product of at most \(2n\) reflections; adjoining cancelling pairs makes it a product of exactly \(2n\). The irreducible open parameter space \(P^{2n}\) therefore maps onto all rational points of \(SO_n\). Its image closure is irreducible and contains the dense rational points, so \(SO_n\) is irreducible.

The Cayley transform identifies the identity neighbourhood \(\det(I+g)\ne0\) with an open of the vector space of skew-symmetric matrices, giving smoothness at \(I\). Translations and density of rational points give smoothness throughout \(SO_n\). Multiplication by \(r\) identifies the other determinant fibre with \(SO_n\). These are exactly the two geometric components. Consequently \(O_n^0=SO_n\), and the component map is determinant with \(\pi_0(O_n)=\mathbf Z/2\). Its section gives \(O_n=SO_n\rtimes\mathbf Z/2\), with action \(h\mapsto rhr^{-1}\).

For \(n=0\), there is only the empty identity matrix with determinant \(1\). The group, its identity component and its component group are all trivial.

**Solution 3.** A smooth scheme over a field is geometrically regular and therefore geometrically reduced. This proves the forward implication. Conversely, suppose \(G_{\overline k}\) is reduced. It is a reduced algebraic group over the perfect field \(\overline k\); Lesson 2 proves it smooth. Smoothness descends along the faithfully flat extension \(k\subset\overline k\), so \(G\) is smooth over \(k\).

For the proposed replacement, take
\[
H=\operatorname{Spec}k[x,y]/(x^p-ay^p),
\qquad k=\mathbf F_p(a),
\]
with addition in \(x,y\). It is a subgroup of \(\mathbf G_a^2\), since its defining polynomial is additive. The element \(a\) is not a \(p\)-th power in \(\mathbf F_p(a,y)\): its valuation at the prime \(a\) is \(1\), whereas a \(p\)-th power has valuation divisible by \(p\). Hence \(X^p-a\) is irreducible there, and substitution \(X=x/y\) shows that \(x^p-ay^p\) is irreducible in \(k(y)[x]\). Being monic in \(x\), it gives a domain in \(k[x,y]\). Thus \(H\) is reduced.

Its dimension is one, since its coordinate ring is finite integral over \(k[y]\). At the identity, the equation has no linear term, so its tangent space has dimension two. The smoothness criterion of Lesson 2 shows it is not smooth. Over \(k(a^{1/p})\), the equation becomes
\[
(x-a^{1/p}y)^p=0,
\]
so its base change is visibly nonreduced. This is the precise obstruction.

**Solution 4.** The complement \(Z=G\setminus S\) is closed. Give it the reduced scheme structure. The image of \(Z\times S\) under multiplication is open by Proposition 1.1, because its second factor is open.

That image equals \(Z\). For the containment in \(Z\), suppose a product of a point in \(Z\) with a point in \(S\) landed in \(S\). Extend the residue fields to a common field on which these points and lifts of the two image points to \(H\) are defined. The product of one lifted image point with the inverse of the other lies in \(H\); its image would be the original point of \(Z\), contradicting that this point is outside the image. Conversely multiplying by the identity, which belongs to \(S\), gives every point of \(Z\). Thus \(Z\) is open. Therefore \(S\) is closed.

Applying this to the inclusion of an open subgroup proves it closed. Rational surjectivity does not follow: the homomorphism \(\mathbf G_{m,\mathbf Q}\to\mathbf G_{m,\mathbf Q}\), \(t\mapsto t^2\), is surjective as a scheme morphism and has open closed image the entire target, but \(2\in\mathbf Q^\times\) has no rational preimage. The scheme-point argument permits extension of residue fields; it cannot be replaced by a calculation solely in \(G(k)\).

**Solution 5.** Fix a rational \(x\) and let \(O\) be the image of its orbit map. Chevalley makes \(O\) constructible, so it contains a dense open \(U\) in its reduced closure \(Y\). Each translate \(gU\), for \(g\in G(k)\), is open in \(Y\) and contained in \(O\). Their union contains every rational point of \(O\): a rational point of an orbit lifts to a rational point of \(G\), and the rational points of \(O\) form the ordinary \(G(k)\)-orbit. A nonempty constructible difference between \(O\) and that union would contain a rational point, which is impossible. The union equals \(O\), proving local closedness.

The finitely many components \(g_iG^0\) of \(G\) give the closure as a union of translates of the irreducible closure of \(G^0x\). All those components have one dimension \(d=\dim O\). The boundary \(Y\setminus O\) is closed, invariant, and proper in each component; hence its dimension is less than \(d\). Any orbit in it also has dimension less than \(d\).

Choose an orbit of least dimension in \(Y\), possible because dimensions are nonnegative integers and \(Y\) has rational points. If its boundary were nonempty, the boundary would have a rational point with an orbit of smaller dimension. This contradiction proves that chosen orbit closed. Its closure is contained in \(Y\), which is closed in \(X\), so it is closed in \(X\) as well.

For a concrete example in \(M_2\), let
\[
J=\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix}.
\]
For \(t\ne0\), conjugation by \(\operatorname{diag}(t,1)\) gives \(\lambda I+tE_{12}\). The limit at \(t=0\) is \(\lambda I\), which is not conjugate to \(J\). Thus the orbit of \(J\) is not closed. The singleton orbit \(\{\lambda I\}\) is closed and belongs to its boundary.

**Solution 6.** Write \(v=(x,y)\) and \(c(v,w)=xy'-yx'\). Bilinearity gives
\[
c(v,w)+c(v+w,u)=c(w,u)+c(v,w+u),
\]
so the two ways to multiply three triples have identical last coordinate; the first two coordinates associate by addition. The identity is \((0,0,0)\), and \(c(v,-v)=0\) gives inverse \((-x,-y,-z)\).

The equation \(x^p-ay^p=0\) is preserved by sums. In the product coordinate algebra,
\[
c(v,w)^p=x^py'^p-y^px'^p
=a y^py'^p-y^p a y'^p=0.
\]
Consequently \((z+z'+c(v,w))^p=0\), and multiplication preserves the other defining equation. The inverse preserves both equations too. These calculations prove the group laws over every test algebra.

By the irreducibility argument in Solution 3, \(H=k[x,y]/(x^p-ay^p)\) is a domain. In \(B=H[z]/(z^p)\), the ideal \((z)\) is nilpotent and its quotient is reduced, so it is exactly the nilradical. The reduction is \(z=0\).

Multiplication of its two universal points has last coordinate \(xy'-yx'\). The ring \(H\otimes_kH\) is free over \(k[y,y']\) with basis
\[
\{x^ix'^j:0\leq i,j<p\},
\]
because each monic degree-\(p\) equation reduces a distinct variable. The term \(xy'\) has basis index \((1,0)\) and coefficient \(y'\), whereas \(yx'\) has index \((0,1)\) and coefficient \(y\). They cannot cancel. In characteristic two the minus is plus, but these are still distinct basis indices. Thus the multiplication does not factor through \(z=0\), and the reduction is not a subgroup.

**Solution 7.** On any test algebra \(R\), the first coordinate consists of \(u\in R\) with \(u^p=0\); the second belongs to the constant étale group \(\mathbf F_p^\times\). The law
\[
(u,c)(v,d)=(u+cv,cd)
\]
preserves \(u^p=0\), since \(c^p=c\) on each constant component and \(v^p=0\). Associativity follows by expanding the first coordinate to \(u+cv+cdw\). The identity is \((0,1)\), and the inverse is \((-c^{-1}u,c^{-1})\).

The underlying finite scheme has one connected component \(\alpha_p\) for each \(c\). Thus
\[
G^0=\{(u,1)\}\simeq\alpha_p,\qquad
G_{\mathrm{red}}=\{(0,c)\}\simeq\mathbf F_p^\times,
\qquad \pi_0(G)=\mathbf F_p^\times.
\]
The component map is \((u,c)\mapsto c\), and its section is \(c\mapsto(0,c)\). The multiplication map from the semidirect product sends \((u,c)\) to \((u,1)(0,c)=(u,c)\); its inverse takes \((u,c)\) to that same pair, since
\[
(u,c)(0,c^{-1})=(u,1).
\]
Conjugation by \((0,c)\) sends \((u,1)\) to \((cu,1)\).

Choose \(c\ne1\) and the universal \(u\) in \(\mathbf F_p[u]/(u^p)\). Then \((0,c)(u,1)=(cu,c)\) differs from \((u,1)(0,c)=(u,c)\). Hence \(G\) is not commutative, despite the two individual factors being commutative.

**Solution 8.** In the ring
\[
B=\underset{n}{\operatorname{colim}}\,k^{(\mathbf Z/2)^n},
\]
every prime ideal selects exactly one factor at each finite level. These choices must be compatible, so points of \(\operatorname{Spec}B\) identify with sequences in \(\prod_{j\geq1}\mathbf Z/2\). A basic open fixes finitely many initial coordinates. Two distinct sequences differ at a finite level, where a clopen partition separates them; hence every connected subset is a singleton. The identity component is therefore the all-zero sequence, with the canonical flat closed structure \(\operatorname{Spec}k\) given by evaluation at that sequence.

No basic open isolates it, because after any finite string of zeros one may choose a later nonzero coordinate. Its component is not open. The scheme is not locally of finite type, so this does not contradict the conditional openness in Theorem 2.3.

For the constant group scheme \(\coprod_{\lambda\in\Lambda}\operatorname{Spec}k\), any affine open is quasi-compact. The point components form an open cover, so quasi-compactness makes an affine open meet only finitely many of them. A countable union of such opens contains at most countably many points; it cannot cover uncountable \(\Lambda\). Proposition 5.4 only supplies a countably covered open and closed subgroup containing the identity. In this example the trivial subgroup already has all those properties. Neither example contradicts the corrected general statements.

**Solution 9.** Addition preserves \(\epsilon x=0\), since \(\epsilon(x+y)=0\) on the product. Negation preserves it too. Write \(B=A[x]/(\epsilon x)\). As an \(A\)-module it is the direct sum of \(A\) in degree zero and copies of \(k\) in every positive degree. The injection \((\epsilon)\to A\) becomes, after tensoring with \(B\), the multiplication map

\[
B/\epsilon B\longrightarrow B,\qquad \overline b\longmapsto\epsilon b.
\]

Its nonzero element \(\overline x\) maps to zero. Thus \(B\) is not flat. Its special fibre is \(k[x]\), whose spectrum is irreducible. The nilpotent-base homeomorphism makes \(H\) irreducible as well. The constant group of order two is two disjoint open and closed copies of \(\operatorname{Spec}A\), in every characteristic. Consequently \(G\) has exactly two components, both isomorphic to \(H\), and \(G^0=H\times\{0\}\). It is open, closed, normal and of finite type over \(A\), with special fibre \(\mathbf G_a\), although it is not flat over \(A\). Base change to \(k\) gives \(G_k^0=\mathbf G_a\times\{0\}\), precisely the base change asserted in Proposition 2.4. That proposition's flat closed immersion of the component into the group comes here from a clopen inclusion; it does not assert flatness of the component over the base.

**Solution 10.** The coordinate map is \(k[y]\to k[x]\), \(y\mapsto x^p\). It is injective, so the schematic image is the whole target. Each polynomial in \(x\) has a unique expansion in the free basis \(1,x,\ldots,x^{p-1}\) over \(k[x^p]\). Thus the morphism is finite locally free of positive rank \(p\), hence faithfully flat. The kernel is \(\operatorname{Spec}k[x]/(x^p)=\alpha_p\); its nontrivial points on nilpotent test algebras show that \(F\) is not a monomorphism. The tangent substitution \(x=b\epsilon\) gives \(x^p=0\), so its differential is zero. None of these assertions require perfection of the field. The rational image consists of \(k^p\), which can be smaller than \(k\), even though the scheme morphism is surjective.

The rational-number inclusion has a different failure: its source is reduced and the map is a monomorphism, but it is not quasi-compact. Its dense image is not a closed immersion. Hence it does not satisfy the quasi-compact hypothesis in Proposition 5.8. The finite Frobenius map satisfies quasi-compactness but does not satisfy the monomorphism hypothesis.

**Solution 11.** On the product of two copies, \((s-t)^4=s^4-t^4=0\), and addition \((u,t)\mapsto(t+u,t)\) inverts the difference map. The coordinate algebra is free of rank four over \(k\), so this proves the faithfully flat torsor assertion. Its defining polynomial is \((t^2-a)^2\), and \(t^2-a\) is irreducible: the valuation of \(a\) is odd, whereas that of a square in \(\mathbf F_2(a)\) is even. The sole point has residue field \(L=k(a^{1/2})\).

Put \(k_0=\mathbf F_2(a^2)\). For \(z=c_0+c_1t+c_2t^2+c_3t^3\), its square lies in the two-dimensional \(k_0\)-span of \(1,t^2\), since \(t^4=a^2\). This span intersects the constants \(k\) in \(k_0\), by independence of \(1,t,t^2,t^3\) over \(k\). Thus no \(z\) has square \(a\), and no \(k\)-compatible map \(L\to k[t]/(t^4-a^2)\) exists.

Over an algebraic closure the equation is \((t-a^{1/2})^4=0\), so the base change has one point. Further field extensions preserve that one-point space, proving geometric irreducibility. Over the perfect closure \(K\), the reduction is \(\operatorname{Spec}K\), with normal local ring \(K\). This is exactly the normality and reduced-component field conclusion of Theorem 7.4. It gives no incompatible field structure on the original thick point.

## Appendix A. Quasi-compact approximation and infinite groups

All group schemes in this
appendix are over a field, unless a different base is stated. Quasi-compact
does not mean locally of finite type. Quotient means the fpqc sheaf quotient.

The main statements are SGA 3, VI A 6.5–6.8 and 6.10, together with the
infinite-affine assertion at 5.4.3. Perrin's 1975 thesis, Part I, Chapters
III–V, and his 1976 article explain the approximation method. The proofs here
spell out its algebra, the nonreduced step, its component step, and the
transfinite rational-point argument. The characteristic-zero proof already in
AG-GS-02 Appendix A remains a distinct useful proof.

### Exact previously proved inputs

The following are mathematical inputs, with their precise scope. Their file
hashes and source-reading evidence are retained in the companion workflow
record.

* AG-GS-01, Lemmas 4.4 and 5.1: flat base change for global sections/direct
  image on quasi-compact quasi-separated schemes, and finite-dimensional
  subcomodules of a comodule over a coalgebra.
* AG-GS-03, Theorem 2.3: the identity component is a geometrically irreducible,
  quasi-compact, flat closed normal subgroup; its local ring at the identity
  is the original local ring, and its formation commutes with field extension.
  The flat closed component has the canonical component structure, so its
  defining ideal vanishes in local rings at points of that component.
  Propositions 5.2, 5.6 and 5.8 prove closedness of subgroup immersions,
  surjectivity of quasi-compact dominant homomorphisms, and the closed schematic
  image. Proposition 5.6 proves faithful flatness when the target is reduced.
* AG-GS-04, Theorems 11.1b and 11.1d and Corollary 11.10: quotients of
  finite-type groups by closed subgroups, affine quotients by normal subgroups
  of affine finite-type groups, and faithful-flat/closed-image factorization
  for finite-type field groups. These statements include nonreduced groups
  and arbitrary fields. Theorem A.2 and Corollary A.3 prove the affine,
  saturated, finitely generated nilpotent quotient step without finite type
  on the covering groups. Lemma 11.19 supplies affine neighbourhoods
  of finite sets in a finite-type field group; Theorem 5.5 descends its
  finite-field torsor data under precisely this finite-set hypothesis.
* AG-GS-02, Lemmas A.6–A.8: the finite row-echelon coefficient construction,
  descent of a finitely generated generic equivalence ideal to a finitely
  generated quotient field, and realization of a strict rational group law.
  In A.6 below the characteristic-zero restrictions in A.2, the field-test
  argument in A.9, and the smooth-model step in A.8 are replaced explicitly.
* Bootstrap theorem, Theorem 4.1, is the flat, locally finitely presented equivalence
  relation quotient theorem used in the proof of AG-GS-02 Lemma A.7. The
  relation at that point is of finite type, so this is its stated scope.
* AG-MO, *Limits and Noetherian approximation*, Theorem 1.1, Lemmas 2.1–2.3,
  Theorems 3.2 and 4.1–4.2: existence of limits with affine transitions,
  descent of quasi-compact opens and finite-presentation objects, maps,
  identities and fixed closed immersions. These are finite-data statements,
  not an assertion that an unspecified infinite collection descends at once.
* [Faithfully flat descent](../../AG-DFG/src/faithfully-flat-descent.md), Theorems 2.5, 5.1, 6.2 and 7.1:
  effective descent of modules, ideals, morphisms, affine schemes, and affine
  morphisms. AG-GS-07 Lemma 6.9 is the strict-law translation-sheaf provider
  used in the rational-group realization.

We also use the proper quasi-finite theorem over arbitrary bases, [Zariski’s Main Theorem](../../AG-MO/src/zariskis-main-theorem.md), Theorem 5.1. Its exact transitive proof provider is
recorded separately: the preceding relative integral-completion theorem is
supplied there by Stacks Tag 03GW, with its finite-piece input Tag 02LN.
This is a separately owned general scheme theorem, rather than a Perrin
assertion used in place of the following group arguments.

### 1. The affine case, including arbitrary Hopf algebras

**Lemma A.1 (faithful flatness of a Hopf inclusion).** Let \(B\subset A\)
be an inclusion of commutative Hopf algebras over \(k\). There is no dimension
or finite-generation assumption. Then \(A\) is faithfully flat over \(B\).
Every affine group is an inverse limit of affine finite-type groups, with
faithfully flat affine projections and transitions.

**Proof.** First recall, with the construction, that a commutative Hopf algebra
is the union of its finitely generated Hopf subalgebras. A finite list belongs
to a finite-dimensional subcomodule \(W\) of the regular comodule. If
\(\Delta(w_j)=\sum_iw_i\otimes a_{ij}\), coassociativity and the counit give

\[
\Delta(a_{ij})=\sum_\ell a_{i\ell}\otimes a_{\ell j},
\qquad w_j=\sum_i\epsilon(w_i)a_{ij}.
\]

The algebra generated by the finitely many \(a_{ij}\) and their antipodes is
a Hopf subalgebra containing the list. The antipode has square one because
the algebra is commutative. Taking larger finite lists makes this system
filtered.

Fix a finitely generated Hopf subalgebra \(B_0\subset B\). The Hopf
subalgebras \(A_j\subset A\) which contain \(B_0\) form a filtered family
with union \(A\). The map of finite-type groups
\(\operatorname{Spec}A_j\to\operatorname{Spec}B_0\) is schematically
dominant. The finite-type factorization theorem just listed makes it
faithfully flat, including when \(B_0\) is nonreduced. Thus \(A\), a filtered
colimit of flat \(B_0\)-modules, is flat over \(B_0\).

Here is the passage from all \(B_0\) to \(B\). In the finite-relations
criterion for flatness, a relation \(\sum b_ra_r=0\) in \(A\), with finitely
many \(b_r\in B\), has its coefficients in one \(B_0\). Flatness over that
\(B_0\) expresses the tuple \((a_r)\) as finite sums of tuples whose
\(B_0\)-coefficient vectors satisfy the same linear relation. These same
expressions prove the criterion over \(B\). Hence \(A\) is flat over \(B\).
The corresponding homomorphism of affine groups is quasi-compact and
schematically dominant; in particular it is dominant. AG-GS-03 Proposition
5.6 gives surjectivity, without a reducedness assumption for that part of
the proposition. Flatness and surjectivity give faithful flatness.

Apply this to each finitely generated Hopf subalgebra of \(A\), and to their
inclusions. Spectra convert their filtered union into the asserted inverse
limit. Each projection is an affine fpqc morphism. \(\square\)

We will repeatedly use this elementary limit-flatness test. If
\(Y=\varprojlim Y_i\) has affine transitions, and a fixed morphism \(X\to Y\)
has flat composites \(X\to Y_i\), it is flat. On a target chart its ring is
\(R=\varinjlim R_i\). An affine source chart mapping into it is flat over
each relevant \(R_i\); the finite-relations argument in the preceding proof
makes it flat over \(R\). If the composites are surjective, then \(X\to Y\)
is dominant: a nonempty open contains a nonempty basic open pulled back
from one stage, which its surjective composite meets. When this morphism is
a quasi-compact group homomorphism, Proposition 5.6 supplies its
surjectivity. This test does not require that the target be reduced.

**Lemma A.2 (normal quotients of an already approximated group).** Suppose
\(G=\varprojlim G_i\), with \(G_i\) finite-type groups, faithfully flat
projections, and eventually affine faithfully flat transitions. If
\(N\subset G\) is closed and normal, then \(G/N\) is a quasi-compact group
scheme. If \(G\) is affine, \(G/N\) is affine. Formation of this quotient
commutes with arbitrary extension of the field, and its quotient map is
fpqc.

**Proof.** Discard an initial segment so all transitions are affine. Let
\(N_i\) be the closed schematic image of \(N\to G_i\). It is a normal
subgroup. For normality, lift a conjugating section of \(G_i\) fpqc locally
to \(G\); pullback of its conjugation equations to the schematically
dominant \(N\to N_i\) makes them vanish, also after this flat base change.
The image of \(N_j\to N_i\) is all \(N_i\); the finite-type factorization
theorem makes this map faithfully flat. Put \(Q_i=G_i/N_i\).

The map \(Q_j\to Q_i\) is faithfully flat: a section of \(Q_i\) lifts
locally to \(G_i\), then to \(G_j\), and equality of lifts is the usual
kernel relation. Its kernel is

\[
K_{ji}/(K_{ji}\cap N_j),\qquad K_{ji}=\ker(G_j\to G_i).
\]

Indeed a representative in \(G_j\) whose image is in \(N_i\) can be
multiplied by a local lift from \(N_j\) to put it in \(K_{ji}\).
The group \(K_{ji}\) is affine since \(G_j\to G_i\) is affine. Its normal
finite-type quotient in the displayed formula is affine. Thus
\(Q_j\to Q_i\), an fpqc torsor under that affine kernel, is affine by
descent of affine morphisms. The limit \(Q=\varprojlim Q_i\) exists and is
quasi-compact and separated. In the affine case it is affine.

Each \(G\to Q_i\) is faithfully flat. The limit-flatness test proves that
\(q:G\to Q\) is flat and dominant. It is quasi-compact because its source
is quasi-compact and its target separated. Proposition 5.6 therefore makes
it surjective. Its kernel is \(N\). To check the scheme structure, a
function in the ideal of \(N\) on an affine chart of the limit occurs at a
finite stage; its vanishing on \(N\) puts it in the schematic-image ideal
of that stage. Conversely all those ideals vanish on \(N\). Their union
after pullback is consequently exactly the ideal of \(N\). This also
proves \(N=\varprojlim N_i\), with the latter interpreted as the closed
subscheme inside \(G\).

For every group homomorphism with kernel \(N\), the maps
\((g,n)\mapsto(g,gn)\) and \((g,g')\mapsto(g,g^{-1}g')\) identify
\(G\times N\) and \(G\times_QG\) on every test scheme. Since \(q\) is
fpqc, this identifies \(Q\) with the quotient sheaf. It also proves the
base-change assertion by pulling back the torsor relation and cover.
\(\square\)

There is no circularity between A.1 and A.2: A.1 uses only the
finite-type faithful-flat image theorem; A.2 then supplies all infinite
affine normal quotients.

**Lemma A.3 (affine torsors over an algebraically closed field).** If
\(k\) is algebraically closed and \(A\) is any affine \(k\)-group, every
fpqc \(A\)-torsor over \(k\) has a \(k\)-point.

**Proof.** The torsor \(T\) is affine, by affine fpqc descent. Write its
structure Hopf algebra as a union of finite-type Hopf subalgebras, and
well-order a set of these subalgebras whose union is the whole algebra.
Let \(B_\alpha\) be the Hopf algebra generated by the subalgebras preceding
the ordinal \(\alpha\). Thus \(B_0=k\), successor algebras are generated
by finitely many elements over their predecessor, and at a limit ordinal
\(B_\lambda=\varinjlim_{\alpha<\lambda}B_\alpha\). Put
\(A^\alpha=\operatorname{Spec}B_\alpha\), and
\(K_\alpha=\ker(A\to A^\alpha)\).

The contracted torsor \(T_\alpha=T/K_\alpha\) exists as an affine scheme:
on an fpqc trivializing cover it is \(A^\alpha\), and its translated
descent datum descends affinely. Its quotient map is a torsor under
\(K_\alpha\). A.1 makes each
\(A^{\alpha+1}\to A^\alpha\) faithfully flat, so
\(T_{\alpha+1}\to T_\alpha\) is faithfully flat. It is of finite type,
because the successor Hopf algebra has finitely many algebra generators
over \(B_\alpha\). The fibre over a \(k\)-point is therefore a nonempty
finite-type \(k\)-scheme and has a \(k\)-point by the Nullstellensatz.
At a limit ordinal the affine schemes satisfy
\(T_\lambda=\varprojlim_{\alpha<\lambda}T_\alpha\): check after the same
fpqc trivialization, where this is the Hopf-algebra union. Compatible
\(k\)-points give a \(k\)-point of that limit.

Start with the unique point of \(T_0\). Transfinite recursion chooses a
lift at every successor and takes the compatible point at every limit.
At the last union stage \(K_\alpha=1\) and \(T_\alpha=T\). We obtain a
point of \(T\) over the original \(k\). This argument does not assert that
an arbitrary inverse system of nonempty sets has nonempty inverse limit;
its successor fibres have finite type and its limit stages are handled
explicitly. \(\square\)

### 2. Generic quotients in every characteristic

For the next three results first assume \(k\) algebraically closed.

**Lemma A.4 (primary generic rings in arbitrary characteristic).** A
geometrically irreducible group scheme has primary local rings: every zero
divisor in each local ring is nilpotent. A dense open in it, or in any finite
power of it, is universally schematically dense in a constant family.

**Proof.** A zero-dimensional local \(k\)-algebra \(Q\), with nil maximal
ideal \(\mathfrak n\), is the filtered union of Artinian local subalgebras
with finitely generated residue field over \(k\). For a finite list take
the finite-type subalgebra \(C\subset Q\) it generates, set
\(\mathfrak p=C\cap\mathfrak n\), and localize at \(\mathfrak p\).
Every element of \(C\setminus\mathfrak p\) is a unit in \(Q\), so the
map \(C_\mathfrak p\to Q\) is injective. The reduction of \(C\) is a
domain in the residue field of \(Q\), hence \(\mathfrak p\) is the unique
minimal prime. The Noetherian local ring \(C_\mathfrak p\) is
zero-dimensional and Artinian. Its residue field is
\(\operatorname{Frac}(C/\mathfrak p)\), finitely generated over \(k\).

Such an Artinian subalgebra has a coefficient field in every characteristic
here. The residue field has a separating transcendence basis over the
perfect \(k\). Lift that basis; nonzero rational denominators are units.
The remaining finite extension is separable. Lift a primitive element and
correct its separable minimal polynomial by Newton's formula
\(a\mapsto a-p(a)/p'(a)\); the error is squared at each step and hence
vanishes after finitely many steps in the nilpotent maximal ideal. This
embeds the residue field into the Artinian algebra.

For two such Artinian local algebras with coefficient fields \(E_1,E_2\),
their tensor product is free over the domain \(E_1\otimes_kE_2\). This
tensor product is a domain since \(k\) is algebraically closed, by the
finite-coefficient domain-product proof preceding AG-GS-03 Theorem 1.3.
The augmentation onto that domain has nilpotent kernel. If an element has
nonzero residue \(d\), it becomes a unit after inverting \(d\). It cannot
annihilate a nonzero element in a free module over the domain. Thus every
zero divisor has nilpotent residue-zero part. Tensoring the injective
filtered subalgebra maps over \(k\) is injective; a putative zero-divisor
relation lies in one finite stage. Consequently \(Q_1\otimes_kQ_2\) is
primary for arbitrary zero-dimensional local \(Q_1,Q_2\).

Let \(\eta\) be the generic point of the group \(G\) and
\(Q=\mathcal O_{G,\eta}\). The multiplication map
\(\operatorname{Spec}(Q\otimes Q)\to G\) is flat: generic-local-spectrum
inclusions are flat and multiplication is a projection after a group
automorphism. It is surjective by the generic-pair argument of AG-GS-03
Lemma 5.5. At every point it gives a faithfully flat local inclusion into
a localization of the primary ring \(Q\otimes Q\). A subring of a
primary ring is primary. This proves the local assertion. An affine open
is irreducible; an element outside its minimal prime is nonnilpotent in
every local ring and therefore regular. Its generic localization is
injective, so every dense open is schematically dense.

Repeat after extending to an algebraic closure of any residue field to
get the same fibre assertion for a constant family. The proof of
AG-GS-02 Lemma A.3 now applies without its characteristic restriction:
on a finite affine cover, a dense fibre open contains a principal open
whose defining element is regular in nearby fibres. Multiplication by
that element, on each finite coefficient space, is a finite matrix of
full column rank in every fibre. Its maximal minors generate the unit
ideal, and a linear combination of their adjugate left inverses proves
injectivity after every parameter-algebra change. This proves universal
schematic density. It also proves that equality of finitely many rational
functions on a fibrewise dense quasi-compact domain is given by finitely
many coefficient equations on the parameter. \(\square\)

**Lemma A.5 (finite normal stabilizers).** If \(G\) is geometrically
irreducible and quasi-compact, there is a filtered decreasing family of
closed normal subgroups \(N_i\), of finite presentation as closed
subschemes of \(G\), with scheme intersection \(1\). A cofinal part of
the family consists of affine groups.

**Proof.** For a finite list of rational functions \(f_r\), impose, on
every parameter scheme, the universal equations

\[
f_r(xny)=f_r(xy)
\tag{Q.1}
\]

on their common rational-function domain, with independent universal outer
variables \(x,y\). Its fibres are dense opens in the irreducible \(G^2\),
and its domain is quasi-compact by separatedness and quasi-compactness.
A.4 and finite coefficient expansion give a closed subscheme defined by
a locally finitely generated ideal. The two successive insertions of
\(n,n'\) prove closure under product, and substitution of \(xn^{-1}\)
for \(x\) proves closure under inverse. Substitution of \(xg,g^{-1}y\)
proves normality. Universal schematic density justifies all substitutions
on common domains, including over nonreduced parameter schemes. Thus
these are closed normal subgroup schemes of finite presentation.

An element satisfying all lists acts trivially on all affine coordinates
of an affine identity neighbourhood \(U\). On
\(U_T\cap n^{-1}U_T\) its translation and the identity agree as maps to
\(U_T\). This open is fpqc over \(T\), since every field fibre is a
nonempty intersection of two opens in an irreducible group. Cancellation
there, then fpqc descent, gives \(n=1\). Thus the scheme intersection is
the identity. The complement of \(U\) is quasi-compact; the finite
intersection property for the decreasing closed supports shows that some
\(N_i\) lies in \(U\). It is closed in the affine \(U\), hence affine,
and every smaller subgroup is affine as well. \(\square\)

**Lemma A.6 (integral approximation, with the inseparable relation
retained).** If \(P\) is geometrically integral and quasi-compact, and
\(N\subset P\) is closed, normal and of finite presentation, then
\(P/N\) is a smooth finite-type group. Consequently \(P\) is an inverse
limit of smooth finite-type groups with eventually affine faithfully flat
transitions and projections.

**Proof.** Set \(K=k(P)\). Restrict the closed action relation to its two
generic object coordinates. It is a finitely generated equivalence ideal
\(I\subset K\otimes_kK\). The actual proof in AG-GS-02 Lemma A.7 is
characteristic independent: its finite coefficient descent, monic Gröbner
generic-freeness argument, finite-type flat relation quotient, dense affine
open, and equalizer calculation give a finitely generated field
\(F\subset K\) with

\[
(K\otimes_kK)/I=K\otimes_FK,
\qquad F=\{a\in K:a\otimes1=1\otimes a\}.
\tag{Q.2}
\]

Retain the entire ring in (Q.2). In positive characteristic it need not
be reduced; replacing it by its field-valued points loses the equations
needed for the next argument.

For \(f\in F\), let \(c_1,\ldots,c_m\in K\) be the canonical
row-echelon left coefficients of \(\Delta f\), as in AG-GS-02 Lemma A.6. Let
\(D=K\otimes_FK\), with its two maps \(\alpha,\beta:K\to D\).
These are the universal pair in the generic relation. Normality says that
multiplying that pair by an independent universal point of \(P\) on the
right preserves the relation. Therefore

\[
(\alpha\otimes1)(\Delta f)=(\beta\otimes1)(\Delta f)
\tag{Q.3}
\]

as rational functions over the parameter algebra \(D\). Here is why
coefficient comparison is valid over this possibly nonreduced ring.
Both maps \(K\to D\) are faithfully flat, since \(K/F\) is a field
extension. The coefficient construction is a kernel on finite-dimensional
coefficient spaces. Tensoring with \(D\) preserves that kernel. The
chosen nonzero pivot entries from \(K\) remain units, so its same
row-echelon basis remains a basis with the prescribed pivot positions.
Denominators are universally regular: their finite coefficient expansions
have a nonzero coefficient from \(K\), which remains a unit under either
embedding, and the field partner has geometrically integral fibres.
The matrix argument in A.4 proves regularity over \(D\). Localizing at
the two denominators is therefore injective. Equality (Q.3) identifies
the two row-echelon bases and gives
\(\alpha(c_r)=\beta(c_r)\) in \(D\), for every \(r\).
The field equalizer in (Q.2) puts every \(c_r\) in \(F\).

Left multiplication treats the right coefficients in exactly the same
way. The coefficient intersection identity of AG-GS-02 Lemma A.6 then puts
\(\Delta f\) in \(\operatorname{Frac}(F\otimes_kF)\). Applying
inversion to the universal generic relation proves that inversion
preserves \(F\), too. Thus \(F\) carries a rational group law; its
universal translations are birational, because their inverse formulas
are the restricted group formulas. Since \(k\) is perfect, every
finitely generated field \(F/k\) is separably generated. A separating
transcendence basis followed by a separable primitive element and inversion
of its discriminant gives a smooth affine model of \(F\). This replaces
the characteristic-zero smooth-model sentence in AG-GS-02 Lemma A.8. The rest of
that lemma's strict-law construction and translation-chart gluing applies
unchanged, and supplies a smooth finite-type group \(Q\) with field \(F\).

For completeness, the rational map \(P\dashrightarrow Q\) extends to a
homomorphism without a finite-type assumption on \(P\). On a nonempty
affine domain \(V\) where it is defined, the difference map
\(V^2\to P\), \((a,b)\mapsto ab^{-1}\), is fpqc: it is flat and
quasi-compact, and each geometric fibre is nonempty by irreducibility.
On it set \(q(a,b)=q(a)q(b)^{-1}\). On its overlap the equality of these
values is the rational group identity on an open of the integral \(P^3\);
separatedness of \(Q\) extends it over that overlap. Descent gives
\(q:P\to Q\) and the group identities. It is dominant and hence
faithfully flat by Proposition 5.6, since \(Q\) is reduced.

Its kernel is \(N\) schematically. The relations \(R_N\) and
\(P\times_QP\) have flat projections to the integral \(P\) and the same
restriction (Q.2) at both generic object coordinates. For a flat module
over a domain, localization at the fraction field is injective. Thus each
relation is schematically dense in its restriction to the first generic
coordinate, then to the second; the second step is still flat after the
first flat generic-point base change. They are the schematic closure of
the same generic relation in \(P^2\), and are equal. Their identity
fibres give \(N=\ker q\). Hence \(Q=P/N\).

Apply this to A.5's cofinal affine normal subgroups. Every quotient map
is an affine fpqc torsor under its affine kernel. Transition maps have
affine kernel, the finite-type normal quotient of one affine stabilizer
by the next, and are therefore affine fpqc torsors. The limit exists.
The canonical map from \(P\) to it is flat and dominant by the limit
test, surjective by Proposition 5.6, and a monomorphism because the kernel
is the intersection \(1\). An fpqc monomorphism is an isomorphism: its
cover and equality relation make it the quotient by the identity relation.
This proves the approximation. \(\square\)

### 3. Nonreduced connected groups

**Lemma A.7 (semidirect approximation).** If \(A\) is affine, \(P\) is
already approximated as in A.2, and \(P\) acts on \(A\) by group
automorphisms, then \(A\rtimes P\) is also approximated in that form.

**Proof.** Global sections of a quasi-compact separated \(k\)-scheme commute
with flat scalar extension. Applying the finite affine-cover equalizer twice
gives
\(\Gamma(X\times Y,\mathcal O)=\Gamma(X,\mathcal O)\otimes_k
\Gamma(Y,\mathcal O)\). Thus the global sections of the group
\(A\rtimes P\) form a Hopf algebra, and its action on the affine \(A\)
makes \(k[A]\) a comodule. Any finite list in \(k[A]\) belongs to a
finite-dimensional subcomodule \(W\).

Take its matrix coefficients for the restriction to translations by
\(A\). They generate, with their antipodes, a finite-type Hopf subalgebra
\(B\subset k[A]\), containing the original list by evaluating the
translation at the identity. It is stable under \(P\): the identity
\(p\ell_ap^{-1}=\ell_{p(a)}\) expresses the transformed translation
matrix as its conjugate by the matrix for \(p\) on \(W\). Each transformed
coefficient is consequently a linear combination, over \(\Gamma(P)\),
of the original matrix coefficients and their antipodes. This proves
stability schematically, not only on field points.

Write \(A_B=\operatorname{Spec}B\). The action
\(P\times A_B\to A_B\) factors through some finite-type quotient
\(P_i\): it is a map from an inverse limit with affine transitions to
an affine finite-presentation target. The action, unit and automorphism
identities involve finitely many maps and equalities, and hence hold at
one later stage. This gives the finite-type semidirect product
\(A_B\rtimes P_i\). Enlarge the finite list and the index together to
obtain a filtered system of these semidirect products. The projections
are faithfully flat: their underlying scheme maps are the product of
the faithfully flat \(A\to A_B\) of A.1 and \(P\to P_i\). Their
transitions are affine on the cofinal affine part of the \(P_i\)-system.
Taking the limit recovers the action and the underlying \(A\times P\),
and therefore the semidirect group. \(\square\)

**Lemma A.8 (connected finite-equation quotient and approximation).**
Let \(k\) be perfect and \(G\) connected. If \(N\subset G\) is affine,
closed, normal, and its immersion is of finite presentation, then \(G/N\)
is a finite-type group and \(G\to G/N\) is an affine fpqc torsor. Every
connected group over \(k\) has the approximation stated in SGA VI A 6.5(i).

**Proof.** We may first extend the perfect field to an algebraic closure;
the descent back to \(k\) is explained below. Put \(P=G_{\mathrm{red}}\).
It is a geometrically integral subgroup and is quasi-compact. A.6
approximates it. A.7 approximates \(N\rtimes P\). Its multiplication
homomorphism to \(G\) has closed normal kernel
\(J\simeq N\cap P\), via \(a\mapsto(a^{-1},a)\). A.2 therefore
represents

\[
L=(N\rtimes P)/J.
\]

The induced \(L\to G\) is a monomorphism of fpqc sheaves: equal local
products differ by exactly \(J\). It is quasi-compact, since \(L\) is
quasi-compact and \(G\) is separated. As sheaves,
\(L/N=P/(N\cap P)\); the latter is a finite-type group by A.6, since
\(N\cap P\to P\) is of finite presentation.

We prove that \(L\to G\) is of finite presentation; this is the step
which supplies a *finite* nilpotence bound. Let \(Y=G/N\) as a sheaf and
\(X=L/N\), the just-proved finite-type scheme. Equality of two
\(Y\)-sections defined over a ring \(R_i\) is detected at a finite stage
of a filtered algebra system \(R_j\) with colimit \(R\). Choose a common
faithfully flat affine cover at stage \(i\) on which they lift to \(G\).
Their equality says the difference belongs to \(N\). The finitely
presented closed immersion \(N\subset G\), on a finite affine cover
and finite principal refinement, gives finitely many equations for that
condition. Their vanishing over the colimit occurs at some stage \(j\).
The base-changed cover is still faithfully flat, so equality descends
there. No finite presentation of the cover or of \(G\) was used.

Now a \(G\)-section defined over \(R_i\) lies in \(L(R)\) precisely
when its class in \(Y(R)\) lies in \(X(R)\). A section of the finite-type
scheme \(X\) descends to a finite stage. The preceding equality test
then makes its equality with the original \(Y\)-class hold at a later
stage. Membership in \(L\) consequently descends to a finite stage.
For an affine chart \(W\subset L\) mapping into an affine chart
\(V\subset G\), membership in \(W\), rather than merely \(L\), also
descends: the stage lift's inverse image of \(W\) is a quasi-compact
open in the affine parameter scheme, and if its pullback covers the
limit, a finite principal-cover unit-ideal identity makes it cover a
later stage. The lift is unique because \(L\to G\) is a monomorphism.
Thus the functor of the affine map \(W\to V\) commutes with filtered
algebra colimits. The actual algebraic converse, AG-MO Lemma 3.1, proves
its coordinate algebra finitely presented: factor its identity through
one finite presentation and quotient by the finite differences between
its generators and their images under that retraction. These charts,
and quasi-compactness and separatedness, prove that \(L\to G\) is of
finite presentation.

This monomorphism is a closed immersion. Here no arbitrary group
monomorphism theorem is being assumed. The reduced source \(P\to L\)
is closed by AG-GS-03 Proposition 5.8. It is surjective on spaces: a
geometric point of \(L\) is locally a product \(np\), and the geometric
point \(n\) belongs to \(P\). Hence \(P\subset L\), like \(P\subset G\),
is a closed immersion with nil ideal and is a universal homeomorphism.
The two such maps show that \(L\to G\) is a universal homeomorphism.
Being finitely presented, universally closed and a monomorphism, it is
proper and quasi-finite. The exact proper quasi-finite theorem listed
above makes it finite. A finite monomorphism is closed: on a target
local ring its finite coordinate module has fibre either zero or the
residue field, generated by \(1\). Nakayama makes the ring map
surjective at every localization, hence globally. This proves the claim.

The ideal of \(L\subset G\) is now locally finitely generated, consists
of nilpotents because \(P\subset L\), and is nilpotent with one bound
on a finite affine cover. The affine group \(N\) preserves this ideal
since \(L\) is a subgroup containing it. Its quotient \(L/N=X\) is
finite type. The proved nilpotent quotient step, AG-GS-04 Corollary A.3,
constructs \(G/N\) as a finite-type scheme and \(G\to G/N\) as its
fpqc \(N\)-torsor. The group law descends since \(N\) is normal. The
torsor is affine since \(N\) is affine.

Apply this construction to A.5's cofinal affine stabilizers. Transition
maps are affine faithfully flat torsors under their affine normal
quotients. Their limit receives a flat dominant quasi-compact
homomorphism from \(G\), so it is surjective by Proposition 5.6. Its
kernel is \(1\), so it is an isomorphism. This proves connected
approximation over an algebraically closed field.

For a general perfect \(k\), use the stabilizer functors defined over
\(k\), whose finite equations descend as explained in the next
paragraph. The finite-type quotient \(Q_{\bar k}\) and its group law
have models over some finite subextension \(E/k\): their presentations,
overlap maps and group identities involve finitely many coefficients.
The map \(G_{\bar k}\to Q_{\bar k}\) also descends to that finite
extension, by the finite-presentation target and the quasi-compact
quasi-separated source. Enlarge \(E\) once for its homomorphism
identities. The resulting \(q_E:G_E\to Q_E\) is faithfully flat by
faithfully flat descent from \(\bar k/E\). Its kernel is \(N_E\):
the two closed ideals agree after the same faithfully flat extension,
so agree already over \(E\). Therefore \(Q_E\) is the quotient sheaf
over \(E\). Its canonical \(E/k\) descent datum is effective by
AG-GS-04 Theorem 5.5, since the finite-type group \(Q_E\) has affine
neighbourhoods of finite sets by Lemma 11.19. The group operations,
affineness of the torsor map and its equality relation descend as
well. This proves the assertion over \(k\), without presuming
effectivity of arbitrary scheme descent. \(\square\)

For arbitrary \(k\), including imperfect \(k\), the same connected
finite-equation quotient holds. Extend to the perfect closure \(k^{\rm
perf}\). The preceding proof constructs the quotient there. A canonical
descent datum under a purely inseparable field extension preserves every
open affine chart: the two projections of its tensor-square base are
universal homeomorphisms, and on the diagonal their isomorphism is the
identity. Each chart therefore descends effectively by affine fpqc
descent; their intersections and gluing maps descend as well. Finite
type, the group law, and the affine torsor descend. Applying this to
the stabilizers constructed over \(k\) gives connected approximation
over every field. The properties of those stabilizers are detected over
an algebraic closure by their finite coefficient equations; they are
not chosen only upstairs and then presumed to descend.

More explicitly, for a finite list of rational functions defined over
\(k\), define its stabilizer functor by (Q.1) over \(k\). After an
algebraic closure it is the closed finite-presentation subgroup proved
in A.5. The definition is invariant under both scalar projections
and their composition, even on the nonreduced tensor-square of the
field extension, because equality was tested universally in constant
families. Thus its defining ideal carries an effective fpqc descent
datum. Descent of ideals and finite generation represents the original
functor by a closed finite-presentation subgroup over \(k\). The
intersection and affineness arguments use the original affine identity
chart over \(k\). This establishes the needed finite kernels over the
original field rather than relying on descent of an arbitrary chosen
subgroup upstairs.

### 4. The component quotient and the general group

**Lemma A.9 (the possibly infinite component quotient).** If \(G\) is
quasi-compact, the quotient \(\Pi=G/G^0\) is affine and pro-étale: an
inverse limit of finite étale groups, with affine faithfully flat
transitions and projections. Its quotient map is fpqc. Its finite
quotient kernels pull back to a decreasing family of open and closed
normal subgroups \(C_i\subset G\), with \(G^0=\varprojlim C_i\).

**Proof.** Define the algebra

\[
R=\ker\bigl(\Gamma(G,\mathcal O_G)
\rightrightarrows\Gamma(G^0\times G,\mathcal O)\bigr),
\qquad \Pi=\operatorname{Spec}R.
\tag{Q.4}
\]

Flat scalar extension commutes with this kernel. Enlarge the field so
every component has a rational point: choose one residue field from
each geometric component and embed these in a common extension. This
is used only to check the component quotient, not the fixed-base
rational-point conclusion. Each component is then a translate of
\(G^0\). An invariant function is constant on each component. Moreover
it is constant in a neighbourhood of every point: the canonical flat
closed component has the same local ring at that point as \(G\), so
the difference from that constant vanishes in that local ring. A
finite subcover of the quasi-compact \(G\) shows that each invariant
function takes only finitely many values. Thus \(R\) is the algebra
of locally constant functions, generated by the characteristic
idempotents of clopen component-saturated sets.

Clopen saturated sets separate different components, by the component
separation proof in AG-GS-03 Theorem 2.2. Consequently the map
\(p:G\to\Pi\) has the component classes as its fibres on spaces.
Every prime of \(R\) is determined by a consistent choice among finite
clopen partitions. Quasi-compactness gives a point of \(G\) satisfying
all those choices, so \(p\) is surjective. The local rings of \(R\)
are the ground field: a locally constant function not vanishing at
the selected class is invertible on a clopen neighbourhood of it.
Thus \(p\) is flat and quasi-compact.

Its fibre relation is \(G^0\times G\). It suffices to test a pair of
sections over a local ring. The sections' closed points with the same
image are in the same component. Translate that component by a
rational point to \(G^0\). The canonical flat closed component ideal
vanishes in every local ring at its points, so both local sections
factor through it. Their ratio is in \(G^0\). Conversely invariant
functions agree on such pairs. This proves the equality relation
on all test schemes and identifies (Q.4) with the fpqc quotient.
All assertions descend from the chosen field extension, since the
kernel algebra commutes with flat extension and the torsor relation
and faithful flatness descend.

A.1 writes this affine group as a limit of finite-type affine groups
\(\Pi_i\) with faithfully flat projections. Over the checking field,
their rings embed in the locally constant algebra \(R\). A finite
set of generators involves finitely many constants and idempotents,
so each such ring is a finite product of the ground field. The
\(\Pi_i\) are therefore finite étale, a property descending to \(k\).
Their kernels have open and closed preimages \(C_i\) in \(G\), normal
by their group structure. Their scheme intersection is \(G^0\), the
identity fibre of \(p\), and their clopen affine transition maps
realize that intersection as the asserted inverse limit. \(\square\)

**Lemma A.10 (finite-type torsors over fields).** An fpqc torsor under
a finite-type field group is a finite-type scheme.

**Proof.** Choose an affine fpqc trivializing cover
\(\operatorname{Spec}S\to\operatorname{Spec}k\). A torsor datum is a
translation cocycle with values in the finite-presentation group on
\(S\otimes_kS\). Its map and its cocycle equality involve finitely
many affine-chart generators, relations, principal-cover identities
and overlap equations. They therefore descend to a finitely generated
nonzero \(k\)-subalgebra \(S_0\subset S\), after enlarging it once
for those equalities. Since \(k\) is a field, \(S_0\) is faithfully
flat over \(k\). The descended cocycle defines the same torsor sheaf
after refinement to \(S\). A closed point of \(\operatorname{Spec}S_0\)
has a finite residue extension \(E/k\), and its map to the torsor
trivializes the torsor over \(E\).

Over \(E\) it is the finite-type group, which has an affine
neighbourhood of every finite set of geometric points by Lemma 11.19.
The exact finite locally free descent theorem AG-GS-04 Theorem 5.5
therefore makes this finite-field descent datum effective as a
scheme. Finite type descends along \(E/k\). The descended equality
relation is the original torsor relation, so the scheme represents
the original sheaf. This argument neither presumes that every torsor
over an arbitrary scheme is representable nor that its original
trivializing algebra was of finite type. \(\square\)

**Theorem A.11 (full quasi-compact approximation).** Over an arbitrary
field, every quasi-compact group scheme \(G\) has a filtered family of
closed affine normal subgroups \(N_i\), each of finite presentation in
\(G\), such that

\[
\bigcap_iN_i=1,\qquad G_i=G/N_i\text{ is of finite type},
\qquad G=\varprojlim G_i.
\tag{Q.5}
\]

All projections and transitions in this chosen system are affine and
faithfully flat. If \(H\subset G\) is closed, then \(G/H\) is a scheme
when either \(H\to G\) is of finite presentation or \(H\) is normal.
In the finite-presentation case it is of finite type. In the normal
case it is a quasi-compact group scheme. The quotient maps are fpqc
and their equality relations are the subgroup action relations.

**Proof.** We first extend the finite stabilizers of \(G^0\) to normal
finite stabilizers of \(G\). Starting with a finite-equation affine
normal subgroup \(A\subset G^0\), take its normal core under \(G\):

\[
A'(T)=\{a\in G^0(T):gag^{-1}\in A
\text{ universally for }g\in G\}.
\]

This core has finitely many local equations. On an affine parameter
chart of \(G^0\), pull back the finite equation ideal of \(A\) to
\(G\) times that chart. A finite affine cover of the quasi-compact
\(G\) gives finitely many finite lists of equations. Expand each in
a basis of the corresponding \(G\)-chart algebra; vanishing for the
universal \(g\) is exactly vanishing of its finitely many coefficients
in the parameter algebra. These ideals glue, as their conditions are
universal. This is a closed subgroup of finite presentation in
\(G^0\), normal in \(G\), and closed in the affine \(A\). Applying
cores to all stabilizers retains intersection \(1\).

Use \(G^0=\varprojlim C_j\) of A.9. A fixed \(A'\subset G^0\)
descends to a closed finite-presentation subscheme of one \(C_j\),
by the exact finite-data descent theorem. Its multiplication,
inversion, identity and normality under the whole \(G\) descend at
a common later stage. For the normality assertion in particular,
pullback of its finitely generated ideal to \(G\) times the stage
subscheme vanishes at the limit; on a finite affine cover each of
these finitely many vanishings holds at a later stage. This proves
normality under \(G\), without assuming that \(G\) is already
approximated. Shrink farther until this stage subgroup lies in an
affine open containing \(A'\): the closed complement is
quasi-compact, and the decreasing stage supports have limit \(A'\).
It is then affine. We obtain a closed affine normal subgroup
\(N\subset G\) of finite presentation with \(N\cap G^0=A'\).
Doing this inside arbitrarily small \(C_j\), and taking finite
intersections, gives a filtered family with intersection \(1\).

For each such \(N\), put \(L=NG^0\) as a sheaf. Let \(J\) be the
closed schematic image of the affine group \(N\to\Pi=G/G^0\).
The affine Hopf result A.1 identifies its map to \(J\) as faithfully
flat. It follows on local quotient representatives that

\[
L=G\times_\Pi J.
\tag{Q.6}
\]

In particular \(L\) is a closed subgroup scheme. Also
\(L/N=G^0/(N\cap G^0)\) is a finite-type group. To see this last
assertion from connected approximation, the finite equation ideal
of \(N\cap G^0\) contains some normal approximation kernel; descent
of its closed ideal along the affine fpqc projection identifies the
quotient with a quotient of that finite-type stage.

The finite-stage membership proof in A.8, now with this \(L/N\),
shows that the closed immersion \(L\subset G\) has finitely
generated ideal. (Since closedness is already known from (Q.6),
one can directly apply the proof to the filtered quotients by its
finitely generated subideals.) Faithfully flat ideal descent along
\(G\to\Pi\) makes \(J\subset\Pi\) finitely presented. A
finite-equation closed subgroup of a pro-étale group is the inverse
image of a subgroup in one finite étale stage: descend its finite
ideal generators, then multiplication, inverse and identity
equations, using the affine limit and faithful-flat projections.
Its quotient \(\Pi/J\) is consequently finite étale.

The quotient sheaf \(G/N\to\Pi/J\) has fibre group \(L/N\),
and is a torsor under that group over each component, with the
conjugate action when a different component is used. After a
finite separable field extension the base is a finite set of field
points. A.10 represents each fibre torsor by a finite-type scheme.
Finite étale descent of their finite disjoint union, with its
affine finite-set neighbourhoods, is effective by the same finite
descent theorem. Hence \(G/N\) is a finite-type group scheme. Its
map from \(G\) is the fpqc torsor under the affine \(N\), and is
affine. If \(N_j\subset N_i\), the transition is the affine fpqc
torsor under \(N_i/N_j\); this kernel is affine by A.2 and of
finite type because it is a closed subgroup of the finite-type
\(G/N_j\). The limit in (Q.5) exists. The flatness, dominance,
surjectivity and identity-kernel argument already given proves
that its map from \(G\) is an isomorphism.

If \(H\) is normal, apply A.2 to this approximation. If
\(H\subset G\) has finite-presentation immersion, some \(N_i\)
is contained in \(H\): the ideal of \(H\) has finitely many
generators on a finite affine cover, all vanishing at the identity,
and the increasing union of the \(N_i\)-ideals is the identity
ideal. A common index includes all these generators. The affine
fpqc torsor \(G\to G_i\) descends the \(N_i\)-saturated ideal
of \(H\) to a closed subgroup \(H_i\subset G_i\). The sheaf
identity

\[
G/H=(G/N_i)/(H/N_i)=G_i/H_i
\]

follows by local lifting and equality of cosets. The finite-type
quotient theorem represents its right side, without assuming
normality of \(H_i\). The composite quotient map is fpqc and has
the asserted relation. Pulling back that relation and cover proves
all field-base-change assertions. This completes both parts of
SGA VI A 6.5 in their original scope. \(\square\)

### 5. Faithful-flat image factorization in the unrestricted scope

**Theorem A.12.** A quasi-compact, schematically dominant homomorphism
\(f:G\to H\) of arbitrary field group schemes is faithfully flat.
Neither group need be quasi-compact over the field, affine, reduced or
locally of finite type. Every quasi-compact homomorphism has the
factorization

\[
G\longrightarrow G/\ker f\ \lhook\joinrel\longrightarrow H,
\]

with its first map fpqc and its second a closed immersion, whose image
is the closed schematic image of \(f\). A quasi-compact group
monomorphism is consequently a closed immersion. If \(H\) is affine,
injectivity of \(\Gamma(H,\mathcal O_H)\to\Gamma(G,\mathcal O_G)\)
suffices for the first assertion.

**Proof.** First suppose \(G,H\) quasi-compact and choose the
approximation \(H=\varprojlim H_i\) of A.11. Set
\(N_i=\ker(G\to H_i)\). The identity immersion in the finite-type
\(H_i\) is of finite presentation, so \(N_i\subset G\) is too.
A.11 represents \(G/N_i\) as a finite-type group, with an fpqc
quotient map. The induced \(G/N_i\to H_i\) is a monomorphism: equal
local representatives differ precisely by \(N_i\). The finite-type
monomorphism theorem makes it closed. It is schematically dominant,
because the composite \(G\to H\to H_i\) is so. The second map is
faithfully flat, hence schematically dominant, and the first map is
schematically dominant by assumption. A closed immersion with zero
ideal is an isomorphism. Thus \(G\to H_i\) is faithfully flat
for every \(i\). The limit-flatness test makes \(f\) flat. Its
dominance and quasi-compactness give surjectivity by Proposition 5.6.

For arbitrary \(G,H\), use the canonical flat closed \(H^0\subset H\).
Flat base change preserves schematic dominance for a quasi-compact
quasi-separated morphism, by the exact direct-image theorem. Thus
\(G'=G\times_HH^0\to H^0\) is schematically dominant. Its source
is quasi-compact, since \(H^0\) and \(f\) are, and is a group scheme.
The already proved case makes it faithfully flat. At the identities
its local map is the original local map: the ideal of \(H^0\) is zero
in \(\mathcal O_{H,e}\), hence its pulled-back ideal is zero in
\(\mathcal O_{G,e}\). Therefore \(f\) is flat at \(e\).
To prove flatness at an arbitrary \(g\), extend the residue field to
make \(g\) rational. Field base change preserves flatness at the
identity, and translation by \(g\) on the source and by \(f(g)\)
on the target identifies the two local maps. Flatness at \(g\) then
descends along the faithfully flat local field extension. This is
the translation argument with no finiteness assumption. Proposition
5.6 still supplies global surjectivity.

For a general quasi-compact \(f\), let \(J\subset H\) be its closed
schematic image from Proposition 5.8. The factor \(G\to J\) is
quasi-compact and schematically dominant, and therefore fpqc by
the preceding argument. Its kernel is \(\ker f\), and the explicit
relation \(G\times\ker f=G\times_JG\) makes \(J\) represent
the fpqc quotient, also when \(G\) itself is not quasi-compact.
If \(f\) is a monomorphism this kernel is \(1\); an fpqc
monomorphism is an isomorphism, giving closedness of \(f\).
Finally, for affine \(H\), its schematic-image ideal is exactly
the kernel of the stated global-section map. Injectivity makes
that ideal zero. \(\square\)

**Theorem A.13 (abelian categories and the full subgroup
correspondence).** The categories of quasi-compact commutative field
groups and of affine commutative field groups are abelian. The latter
is a full subcategory closed under subobjects, quotients and
extensions. No finite-type restriction is imposed.

For an epimorphism \(G\to Q=G/F\) of fpqc group sheaves, the
assignments

\[
H\longmapsto H/F,\qquad K\longmapsto G\times_QK
\tag{Q.7}
\]

are inverse, inclusion-preserving bijections between **all subgroup
sheaves** \(H\subset G\) containing \(F\), and all subgroup sheaves
\(K\subset Q\). They preserve and detect normality. If \(G\) is a
quasi-compact field group and \(F\subset G\) a closed normal subgroup,
they restrict to inverse bijections on closed subgroup schemes and
preserve and detect closedness. The first and second isomorphism
theorems for those closed subgroups hold as scheme isomorphisms.

**Proof.** For the category assertions, pointwise multiplication gives
an abelian group of homomorphisms, since the targets are commutative.
The identity group is a zero object; a finite product is a biproduct,
with the inclusions, projections and sum identities verified on tests.
Kernels are closed subgroup schemes, and are quasi-compact (or
affine) in the respective category. A homomorphism between
quasi-compact groups is quasi-compact, because its target is separated.
A.12 factors it as an fpqc map onto its closed image \(J\), followed
by the inclusion of \(J\) in the target. Its cokernel is the represented
normal quotient of the target by \(J\), given by A.11 or, in the
affine case, A.2. This is a cokernel in the categorical sense:
any homomorphism killing the original source kills \(J\) after
its fpqc cover and hence factors uniquely through that quotient.
The coimage is \(G/\ker f\) and is canonically isomorphic to
\(J\), the image (kernel of the cokernel). This proves the abelian
axiom. A categorical monomorphism has zero kernel; the relation
calculation makes it a scheme monomorphism, hence closed by A.12.
Thus affine subobjects are affine. Affine quotients are A.2.
In an exact extension with affine kernel and affine quotient, the
middle group maps to the quotient as a torsor under the affine
kernel, so is affine by affine descent. The same torsor argument
shows quasi-compactness for an extension with quasi-compact
kernel and quotient.

For the sheaf correspondence, define \(H/F\) as the sheaf image of
\(H\to Q\). A section of its inverse image in \(G\) locally differs
from an \(H\)-section by an element of \(F\subset H\), so it is
itself in \(H\); membership descends since \(H\) is a subsheaf.
Conversely every section of \(K\subset Q\) locally lifts to \(G\)
and hence to \(G\times_QK\), giving the inverse assertion.
These calculations prove (Q.7) on arbitrary test schemes, not
only on geometric points. To test normality, locally lift a
conjugating section of \(Q\) and a section of \(K\) to \(G\);
conjugation preserves \(H\) exactly when it preserves \(K\).

Now assume the scheme hypotheses. The quotient \(q:G\to Q\) is
fpqc by A.11. A closed subgroup \(H\) containing \(F\) is
\(F\)-saturated. On the relation \(G\times_QG=G\times F\), its
two pulled-back ideals agree: right translation by \(F\) preserves
the closed subgroup on every test scheme. Effective descent of
quasi-coherent ideals gives a closed \(K\subset Q\) with
\(H=G\times_QK\). Multiplication and inversion descend, so
\(K\) is a subgroup scheme, and the base-change torsor
\(H\to K\) identifies it with \(H/F\). Pullback proves the
opposite direction; faithful flat ideal descent proves detection
of closedness. All subgroup schemes over a field are flat over
that field, so no extra subgroup-flatness hypothesis appears here.

If \(F\subset H\subset G\) are closed and \(F,H\) normal in
\(G\), local representatives give
\((G/F)/(H/F)=G/H\). Both sides are represented normal quotients,
and the sheaf identity is therefore a canonical scheme
isomorphism. For the second theorem let \(F\) be closed and
normal in \(G\), and \(H\subset G\) closed. Their semidirect
product has multiplication map \(F\rtimes H\to G\), with closed
normal kernel
\(F\cap H\to F\rtimes H\), \(h\mapsto(h^{-1},h)\).
All three groups are quasi-compact. A.12 identifies its quotient
with its closed schematic image \(I=FH\). The inverse image of
\(F\subset I\) under the fpqc product map is \(F\times(F\cap H)\),
so ideal descent makes \(F\) closed in \(I\). It is normal there.
Local representatives \(fh\) give the canonical sheaf, hence
scheme, isomorphism

\[
I/F\simeq H/(F\cap H).
\]

Every formula is compatible with field extension. This proves
the unrestricted sheaf prerequisite and its closed-scheme
realization, separately from the locally finite-type Artinian
scheme correspondence already proved in results 11.15–11.18.
\(\square\)

The coset form of the first isomorphism theorem has no group or
representability restriction on its ambient quotient. For subgroup
sheaves \(F\subset H\subset G\) with \(F\) normal in \(H\), the
group \(F\backslash H\) acts on the left-coset sheaf
\(F\backslash G\), and

\[
(F\backslash H)\backslash(F\backslash G)=H\backslash G.
\]

The action is well-defined because \(hfh^{-1}\in F\). Its local
coset representatives give surjectivity onto the right side; two
representatives there agree exactly when they differ by an
\(H\)-section, which locally gives an \(F\backslash H\)-section
relating their \(F\)-cosets. These equations give injectivity after
sheafification, prove the torsor equality relation, and show
equivariance for right multiplication by \(G\). If the three sheaves
are represented in one of the quotient scopes proved above, this is
a canonical isomorphism of schemes. The formal assertion is retained
even when the final coset sheaf is not represented.

### 6. Rational points over the given algebraically closed field

**Theorem A.14 (SGA VI A 6.10).** Let \(k\) be algebraically closed
and \(G\) a quasi-compact \(k\)-group.

1. Every faithfully flat group homomorphism \(f:G\to H\) induces
   a surjection \(G(k)\to H(k)\).
2. The \(k\)-rational points are dense in \(G\).

The field in both conclusions is this same \(k\).

**Proof.** Surjectivity of \(f\) makes \(H\) quasi-compact. Set
\(N=\ker f\), and choose an affine normal approximation kernel
\(A\subset G\) with finite-type quotient \(G_1=G/A\), as in
A.11. Let \(M\subset H\) be the closed schematic image of
\(A\to H\). A.12 makes \(A\to M\) faithfully flat. The
kernel is \(A\cap N\), so A.2 identifies
\(M=A/(A\cap N)\) and proves it affine. It is normal in \(H\):
lift a conjugating section fpqc locally through \(f\), use
normality of \(A\), and descend the conjugation equations.

Let \(N_1\subset G_1\) be the closed image of \(N\to G_1\).
Its sheaf image is the same closed image by A.12. Local lifts
give the sheaf identity

\[
H/M\simeq G_1/N_1.
\tag{Q.8}
\]

Both sides are represented normal quotients. The right side is
finite type, and \(G_1\to H/M\) is a faithfully flat finite-type
map of finite-type groups. For \(h\in H(k)\), its image in
\((H/M)(k)\) therefore has a lift \(g_1\in G_1(k)\): its
nonempty finite-type fibre has a rational point by the
Nullstellensatz. The fibre of \(G\to G_1\) over \(g_1\) is an
fpqc torsor under the affine \(A\). A.3 gives a point
\(g\in G(k)\) in that fibre. The element \(f(g)^{-1}h\) is in
\(M(k)\). Since the fibre of \(A\to M\) over this element is
a torsor under the affine \(A\cap N\), A.3 lifts it to
\(a\in A(k)\). Then \(f(ga)=h\). This proves (1).

For (2), a nonempty open in \(G=\varprojlim G_i\) contains the
inverse image of a nonempty quasi-compact open in some finite-type
stage, by the topology of affine-transition limits. That stage
open has a \(k\)-point by the Nullstellensatz. Its fibre in
\(G\) is a torsor under the affine approximation kernel \(N_i\),
and has a \(k\)-point by A.3. Thus every nonempty open in
\(G\) contains a \(k\)-point, proving density. No larger field
has been substituted for \(k\). \(\square\)

**Example A.15 (the scheme representability boundary).** The
formal sheaf correspondence of A.13 does not assert that every
arbitrary subgroup monomorphism, or its coset sheaf, is represented
by a scheme. The non-quasi-compact constant group \((\mathbf Q)_k\)
embeds in \(\mathbf G_a\) in characteristic zero by rational
translations. Its quotient sheaf is not a scheme, by the proved
fibre quasi-compactness contradiction in AG-GS-04 Example 11.18.
This preserves the full formal theorem and its scheme boundary.
The example also shows why the quasi-compact morphism hypothesis
in A.12 cannot be omitted. The nonreduced example
\(1\to\alpha_p\) in AG-GS-03 Example 5.7 retains the distinction
between topological dominance and schematic dominance.

The all-characteristic approximation and fixed-field rational-point arguments follow Daniel Perrin’s [1975 thesis](https://bibliotheque.imo.universite-paris-saclay.fr/media/filer_public/99/55/99556864-9947-4630-8154-76b1bc0b3edc/p_perrin-109.pdf), Part I, Chapters III–V, and [1976 article](https://www.numdam.org/articles/10.24033/bsmf.1830/), §§1–4, compared with SGA 3 VI A5.4.3 and6.5–6.10. Their statements and method are credited; this appendix supplies independently written proofs.

## What this lesson assumes and does not prove

The proofs above use the following general scheme-theoretic prerequisites with their stated scope.

- For schemes over a field, the structure map is universally open [Stacks, Tag 0383]. Flat maps satisfy going down, and a faithfully flat ring map is surjective on spectra. An algebraic field extension induces an integral projection.
- A connected scheme over a field with a rational point is geometrically connected [Stacks, Tag 04KV]. More generally, a connected scheme receiving a morphism from a geometrically connected scheme is geometrically connected [Stacks, Tag 056R].
- A closed subset stable under generalization has a canonical closed subscheme structure whose immersion is flat; this canonical structure receives every morphism whose set-theoretic image lies in the subset. An arbitrary closed subscheme on that subset need not be flat (a nontrivial nilpotent thickening already shows the distinction). This is the canonical flat closed structure used for a connected component [Stacks, Tags 04PW–04PX]. At a point of a flat closed subscheme, the surjective flat local-ring map is faithfully flat, hence injective and an isomorphism.
- Finite étale schemes over \(k\) are finite sets with continuous \(\operatorname{Gal}(k^s/k)\)-action, and morphisms and products respect that equivalence [Stacks, Tag 03QR]. Effective descent of schemes and morphisms is used for the finite separable extension in Section 3. The Galois action on connected components is recorded in [Stacks, Tags 038D–038E].
- Reduced schemes over perfect fields are geometrically reduced [Stacks, Tag 020I]. Smooth schemes over fields are regular [Stacks, Tag 056S]. Smoothness descends under field extension [Stacks, Tag 02VL], and a smooth morphism admits local étale coordinates [Stacks, Tag 054L]. For arbitrary subsets of two schemes over a field, the closure of their product is the product of their closures [Stacks, Tag 047B].
- The line-bundle prerequisites in Section 6 are Tags 0BCW, 0AG0, 0BEH and 0BDC. Localization of sections is Tag 01PW, the affine-basis characterization of ampleness is Tag 01Q3, and the finite-type immersion criterion is Tag 01VT.
- Chevalley's theorem says the image of a finite-type morphism between Noetherian schemes is constructible [Stacks, Tag 054K]. A dense constructible subset contains a dense open, and a nonempty constructible subset of a finite-type scheme over an algebraically closed field contains a rational point. Proper closed subsets of an irreducible variety have smaller dimension, and finite dominant morphisms preserve dimension.

The construction of \(\pi_0(G)\) and the smooth orbit argument of Theorem 7.1 do not use quotient existence. Theorem 7.13 subsequently uses *Quotients and torsors*, Theorem 11.1b, whose proof depends only on the earlier field-group and quasi-projectivity results. Its full scheme-level orbit argument therefore creates no circular dependency.

## References

- The Stacks Project, read in AI Integrated Stacks Project: Groupoid Schemes, Tags 047K, 0B7N, 047L–047M, 0B7P–0B7R, 047R–047U, 0BF7–0BF8; Varieties, Tags 038D–038E. The imported general prerequisites are identified above.
- J. S. Milne, *Algebraic Groups: The Theory of Group Schemes of Finite Type over a Field*, corrected edition dated 5 October 2021, published by Cambridge University Press, 2022: Chapters 1, 2, 5, 7 and 11. [Corrected author edition, freely available PDF](https://www.jmilne.org/math/Books/iAG2022.pdf).

- Pierre Gabriel, *Généralités sur les groupes algébriques*, SGA 3, Exposé VI A, corrected re-edition of 13 October 2024. [Open corrected text](https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp6A-13oct24.pdf).

- **[Stacks-normality]** The Stacks Project contributors, *The Stacks Project*, [geometrically normal algebras, Tag 037Y](https://stacks.math.columbia.edu/tag/037Y), [separable field normality, Tag 0C30](https://stacks.math.columbia.edu/tag/0C30), [normality descent, Tag 033G](https://stacks.math.columbia.edu/tag/033G), [filtered colimits of normal rings, Tag 037D](https://stacks.math.columbia.edu/tag/037D), [smooth models of finitely generated separable fields, Tag 037X](https://stacks.math.columbia.edu/tag/037X), and [constant-field irreducibility, Tag 037P](https://stacks.math.columbia.edu/tag/037P). Live version accessed 3 October 2026.

- **[Gille]** Philippe Gille, *Introduction to reductive group schemes over rings*, author notes dated 9 May 2025, [open author PDF](https://math.univ-lyon1.fr/~gille/prenotes/reductive.pdf), accessed 3 October 2026. Theorem 7.13 supplies the complete schematic orbit argument corresponding to Proposition 14.5.3, including the nonsmooth case omitted from its sketch.
