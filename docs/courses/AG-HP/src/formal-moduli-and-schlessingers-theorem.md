# Formal moduli and Schlessinger's theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A formal parameter ring should generate every infinitesimal deformation, and its first-order parameters should have no redundancy. Such a ring is a hull. Whether it classifies every deformation uniquely is a further question. The difference is measured by how deformations glue over fibre products of Artinian rings, and, for a groupoid of geometric objects, by whether their automorphisms lift.

We prove both directions of Schlessinger's theorem, constructing the hull by successive approximation. We retain the chosen identification with the special fibre throughout. This makes the distinction between infinitesimal automorphisms and ordinary symmetries of that fibre precise.

## 1 Rings, formal objects and small extensions

Fix a complete Noetherian local ring \(\Lambda\) with residue field \(k\). Let \(\mathcal C_\Lambda\) consist of Artinian local \(\Lambda\)-algebras whose residue field is identified with \(k\). Its morphisms are local \(\Lambda\)-algebra maps inducing the identity on \(k\). A deformation functor here is a covariant functor

\[
F:\mathcal C_\Lambda\longrightarrow\mathrm{Sets},\qquad F(k)=\{*\}.
\]

The covariance comes from passing from an algebra to its spectrum: a base change of schemes is covariant on these rings.

A **small extension** is a surjection \(B\to A\) with nonzero kernel \(I\) of dimension one over \(k\), annihilated by \(\mathfrak m_B\). In particular \(I^2=0\). Sometimes it is useful to allow a finite-dimensional kernel annihilated by \(\mathfrak m_B\); we call that a socle extension. Every surjection in \(\mathcal C_\Lambda\) factors into small extensions. Indeed, filter its kernel by powers of \(\mathfrak m_B\), and then refine each successive vector-space quotient by a flag. This terminates because the kernel has finite length.

If \(A''\to A\) is surjective, the fibre product \(A'\times_A A''\) again belongs to \(\mathcal C_\Lambda\). It is the ring of pairs with equal images in \(A\). Its residue field is \(k\), and its maximal ideal consists of pairs in the maximal ideals; the latter is nilpotent. It has finite length as a submodule of the finite-length \(\Lambda\)-module \(A'\oplus A''\).

For a complete Noetherian local \(\Lambda\)-algebra \(R\) with residue field \(k\), write

\[
h_R(A)=\operatorname{Hom}_{\Lambda,\mathrm{loc}}^{\mathrm{cont}}(R,A).
\]

Continuity means that the map factors through some \(R/\mathfrak m_R^n\); it is automatic for a local map to an Artinian ring. A compatible system \(\xi_n\in F(R/\mathfrak m_R^n)\) defines a natural transformation \(h_R\to F\), by pushing forward a sufficiently large \(\xi_n\). Conversely such a transformation gives that system. A **formal object** means such a compatible system, without asserting that it is the completion of an actual family over \(\operatorname{Spec}R\).

A morphism \(G\to F\) is **smooth** in this lesson if, for every surjection \(B\to A\),

\[
G(B)\longrightarrow G(A)\times_{F(A)}F(B)
\]

is surjective. It suffices to test small extensions, by their factorization. A **hull** is a formal object \(\xi\) over \(R\) whose transformation \(h_R\to F\) is smooth and whose map on tangent spaces is bijective. A prorepresenting object requires \(h_R\to F\) to be an isomorphism of functors. Thus a hull gives existence of parameters with optimal first-order size; prorepresentability also gives uniqueness at every order.

## 2 The four conditions and the tangent vector space

For a diagram \(A'\to A\leftarrow A''\), consider

\[
\theta:F(A'\times_A A'')\longrightarrow
F(A')\times_{F(A)}F(A'').
\]

Schlessinger's conditions are:

- **(H1)** \(\theta\) is surjective whenever \(A''\to A\) is a small extension.
- **(H2)** \(\theta\) is bijective when \(A=k\) and \(A''=k[\epsilon]/(\epsilon^2)\).
- **(H3)** \(t_F=F(k[\epsilon]/(\epsilon^2))\) is finite-dimensional over \(k\), with the vector-space structure described below.
- **(H4)** \(\theta\) is bijective when \(A'=A''=B\) and \(B\to A\) is a small extension.

Under (H1), the same surjectivity holds for every surjection \(A''\to A\). Induct on a small-extension factorization: first glue over an intermediate ring \(C\), then glue the result to \(A''\) over \(C\). The resulting ring is \((A'\times_A C)\times_C A''=A'\times_A A''\).

**Lemma 2.1.** Condition (H2) gives \(t_F\) a canonical \(k\)-vector-space structure. For every finite-dimensional vector space \(V\), putting \(k[V]=k\oplus V\) with square-zero ideal \(V\), there is a natural identification

\[
F(k[V])=t_F\otimes_k V.
\]

**Proof.** A decomposition of \(V\) into one-dimensional summands gives \(k[V]\) as an iterated fibre product of dual-number rings over \(k\). Repeated (H2) identifies its image under \(F\) with a product of copies of \(t_F\). Addition on \(t_F\) is the map induced by \(k[k\oplus k]\to k[k]\), \((a,u,v)\mapsto(a,u+v)\); multiplication by \(c\in k\) is induced by \(u\mapsto cu\). The zero comes from \(k\to k[k]\). The vector-space axioms follow from the corresponding equalities between these linear maps: use the product of three copies for associativity, the exchange map for commutativity, and \(u\mapsto-u\) for inverses. For example the two maps adding three coordinates are equal ring maps, so induce the same addition on triples of tangent elements.

This argument also shows that every linear map \(V\to W\) induces its expected matrix of linear operations on the products. The identifications are therefore independent of the decompositions chosen and give the natural tensor formula. \(\square\)

For a prorepresentable functor the tangent space is

\[
t_{h_R}=\operatorname{Der}_\Lambda(R,k)
=\operatorname{Hom}_k\left(
\frac{\mathfrak m_R}{\mathfrak m_R^2+\mathfrak m_\Lambda R},k\right).
\]

A map to dual numbers is its residue map plus a derivation, which proves the formula. The classical assumption that \(k\) is the residue field of \(\Lambda\) matters in the second expression; no additional derivations of the residue-field extension occur here.

## 3 The action on lifts

**Lemma 3.1.** Assume (H1) and (H2). If \(B\to A\) is a small extension with kernel \(I\), the vector space \(t_F\otimes I\) acts transitively on every nonempty fibre of \(F(B)\to F(A)\). If (H4) holds, this action is free.

**Proof.** There is an isomorphism of rings

\[
B\times_A B\simeq B\times_k k[I],\qquad
(b_1,b_2)\longmapsto(b_1,(\overline b_1,b_2-b_1)).
\]

The first projection is \((b,i)\mapsto b\), and the second is the addition map \((b,i)\mapsto b+i\). By (H2),

\[
F(B\times_k k[I])\simeq F(B)\times(t_F\otimes I).
\]

The second projection thus defines the claimed action. The group law follows from the three-factor square-zero construction used in Lemma 2.1. If two elements of \(F(B)\) have the same reduction, (H1) lifts the pair to \(F(B\times_A B)\); under the displayed identification, its second factor carries the first element to the second. This proves transitivity.

Under (H4) two elements of \(F(B\times_A B)\) with the same pair of restrictions are equal. If a tangent vector fixes an element, its pair of restrictions equals the pair for the zero tangent vector, hence the tangent vectors are equal. The action is free. \(\square\)

For maps \(f,g:R\to B\) with the same reduction to \(A\), their difference is a \(\Lambda\)-derivation \(R\to I\). Conversely adding such a derivation to \(f\) gives another ring map. Since \(\mathfrak m_B I=0\), these derivations form \(t_{h_R}\otimes I\). Natural transformations commute with these actions. Thus a bijective tangent map lets us correct a lift of ring maps to produce any prescribed lift of deformation classes. The lift action need not be free for a general hull.

## 4 Successive approximation constructs a hull

We first isolate the finite-dimensional obstruction quotient used at each stage.

**Lemma 4.1.** Assume (H1). Let \(C\to A\) be a socle extension with kernel \(I\), and let \(\xi\in F(A)\). Among the subspaces \(J\subset I\) for which \(\xi\) lifts to \(F(C/J)\), there is a unique smallest one.

**Proof.** The set is nonempty because it contains \(I\), and is closed under enlarging \(J\). It is also closed under intersection. For liftable \(J,K\), enlarge \(J\) to \(J'\) by a complement of \(J+K\) in \(I\). Then \(J'+K=I\) and \(J'\cap K=J\cap K\). The two chosen lifts glue by the surjective version of (H1) over

\[
C/(J\cap K)=C/J'\times_{C/I}C/K.
\]

So the intersection is liftable. The vector space \(I\) is finite-dimensional. Choose a liftable subspace of smallest dimension; intersection with any other liftable subspace has the same dimension, proving that it is contained in all the others. \(\square\)

We also need a completion fact, for which it is useful to give the proof.

**Lemma 4.2.** Let \(S\) be a complete Noetherian local ring and \(J_n\) a decreasing sequence of ideals. If \(J=\bigcap_nJ_n\), then for every \(q\), some image of \(J_n\) in \(S/J\) is contained in the \(q\)-th power of its maximal ideal. If each \(S/J_n\) is Artinian, the two filtrations are cofinal.

**Proof.** Work in \(S/J\), so the intersection is zero. For each \(q\), the images of \(J_n\) in the finite-length module \(S/\mathfrak m^q\) eventually stabilize; call the stable image \(K_q\). The maps \(K_{q+1}\to K_q\) are surjective: choose one index after the images at both levels have stabilized, and use the surjection between the images of that same ideal at the two levels. A nonzero element of \(K_q\) could therefore be extended to a compatible sequence of elements in all higher \(K_l\). Completeness would give \(x\in S\) whose image lies in every \(J_n+\mathfrak m^l\). Ideals of a complete Noetherian local ring are closed, so \(x\in J_n\) for all \(n\), a contradiction. Thus \(K_q=0\); for some \(n\), \(J_n\subset\mathfrak m^q\). The reverse cofinality follows when each \(J_n\) contains a power of \(\mathfrak m\), as will be the case below. \(\square\)

The closedness of ideals used here is the Krull-intersection consequence \(\bigcap_l(J_n+\mathfrak m^l)=J_n\), one of the ordinary completion prerequisites.

**Theorem 4.3 (existence of a hull).** If \(F\) satisfies (H1)–(H3), it has a hull.

**Proof.** Put \(r=\dim_k t_F\), choose a basis \(v_1,\ldots,v_r\), and set

\[
S=\Lambda[[x_1,\ldots,x_r]],\qquad
J_1=\mathfrak m_S,\qquad
J_2=\mathfrak m_S^2+\mathfrak m_\Lambda S.
\]

The ring \(S/J_2\) is \(k[V]\), with basis \(x_1,\ldots,x_r\) for \(V\). By Lemma 2.1 there is an element \(\xi_2\) corresponding to \(\sum_i v_i\otimes x_i\). Its tangent map is an isomorphism. Its reduction is the unique \(\xi_1\in F(k)\).

Inductively suppose \(J_n\) and \(\xi_n\in F(S/J_n)\) have been chosen. The surjection

\[
S/\mathfrak m_SJ_n\longrightarrow S/J_n
\]

has kernel \(J_n/\mathfrak m_SJ_n\), annihilated by the maximal ideal. Lemma 4.1 supplies a smallest ideal \(J_{n+1}\) with

\[
\mathfrak m_SJ_n\subset J_{n+1}\subset J_n
\]

such that \(\xi_n\) lifts to an element \(\xi_{n+1}\) over \(S/J_{n+1}\). Choose one such lift. All these quotient rings are Artinian: \(J_2\) contains \(\mathfrak m_S^2\), and induction gives \(\mathfrak m_S^{n+1}\subset J_{n+1}\).

Set \(J=\bigcap_nJ_n\) and \(R=S/J\). Lemma 4.2 identifies the \(J_n/J\)-adic and \(\mathfrak m_R\)-adic topologies. Hence the compatible \(\xi_n\) give a formal object \(\xi\) over the complete Noetherian ring \(R\). Its tangent map remains the isomorphism chosen at stage two: since \(J\subset J_2\), the relative cotangent space of \(R\) is still freely generated by the images of the \(x_i\).

We prove smoothness. Suppose \(B\to A\) is a small extension, \(a:R\to A\) is given, and \(y\in F(B)\) reduces to \(a_*\xi\). Choose \(n\) such that \(a\) factors through \(A_n=S/J_n\), and form

\[
C=A_n\times_A B\longrightarrow A_n.
\]

Its kernel is the kernel of \(B\to A\), a one-dimensional socle. If this projection has a section, the section followed by \(C\to B\) already gives a ring lift \(R\to B\).

Otherwise lift the variables of the map \(S\to A_n\) to \(C\), obtaining a \(\Lambda\)-algebra map \(S\to C\). Its image surjects onto \(A_n\). If it did not meet the nonzero kernel of \(C\to A_n\), its image would supply a section, contrary to the case under consideration. It therefore contains that one-dimensional kernel and equals \(C\). Write \(C=S/K\). Then \(\mathfrak m_SJ_n\subset K\subset J_n\).

By (H1), the compatible pair \((\xi_n,y)\) lifts to \(F(C)\). Thus \(K\) is one of the ideals allowed in the choice of \(J_{n+1}\), so \(J_{n+1}\subset K\). The resulting map \(R\to S/J_{n+1}\to C\to B\) lifts \(a\).

In either case its image in \(F(B)\) may differ from \(y\). Lemma 3.1 expresses that difference by a vector of \(t_F\otimes\ker(B\to A)\). The tangent isomorphism lifts that vector to a derivation \(R\to\ker(B\to A)\). Add this derivation to the ring lift. Naturality of the action makes its image exactly \(y\). This proves smoothness for small extensions, hence for all surjections. Together with the tangent isomorphism it proves that \(\xi\) is a hull. \(\square\)

The smallest ideal at a stage records precisely which parts of the next socle extension cannot support the current deformation. There is no assumption of an obstruction vector space or a finite list of equations made in advance; Noetherianity of \(S\) supplies the eventual finite presentation of its closed ideal \(J\).

## 5 Necessity and prorepresentability

**Theorem 5.1 (Schlessinger).** A functor \(F:\mathcal C_\Lambda\to\mathrm{Sets}\) with \(F(k)=\{*\}\) has a hull if and only if it satisfies (H1)–(H3). It is prorepresentable by a complete Noetherian local \(\Lambda\)-algebra if and only if it satisfies (H1)–(H4).

**Proof.** Sufficiency for a hull is Theorem 4.3. For necessity let \(h_R\to F\) be a hull. Its smoothness makes \(h_R(A)\to F(A)\) surjective for every Artinian \(A\), by induction along small extensions from \(k\).

For (H1), take compatible \(\xi'\in F(A')\), \(\xi''\in F(A'')\), with \(A''\to A\) small. Choose \(f':R\to A'\) realizing \(\xi'\). Smoothness over \(A''\to A\) lifts its composite \(R\to A\) to \(f'':R\to A''\) realizing \(\xi''\). The pair gives a map to \(A'\times_A A''\), whose image realizes the pair. Notice that no surjectivity of \(A'\to A\) was needed.

For injectivity in (H2), let \(\eta,\eta'\in F(A'\times_k k[\epsilon])\) have the same restrictions. Choose \(f:R\to A'\times_k k[\epsilon]\) realizing \(\eta\). Apply smoothness along the projection to \(A'\), with its map \(f_{A'}\) and target \(\eta'\). This gives \(g\) realizing \(\eta'\) with \(g_{A'}=f_{A'}\). The maps \(f\) and \(g\) to dual numbers have the same tangent image, and the hull tangent map is injective, so they are equal. Both components of \(f,g\) are now equal, proving \(\eta=\eta'\). Surjectivity is already (H1). Finally (H3) follows from the finite-dimensional relative cotangent space of the Noetherian ring \(R\).

A prorepresentable functor commutes with all the fibre products in question, by the universal property of a fibre product of rings. Its tangent space is finite-dimensional by the formula in Section 2. It therefore satisfies (H1)–(H4).

Conversely assume all four conditions, and construct the hull \(h_R\to F\). Smoothness already gives surjectivity on every Artinian ring. We prove injectivity by induction on length. Suppose \(B\to A\) is small and the claim holds for \(A\). If \(f,g:R\to B\) have the same image in \(F(B)\), their reductions are equal by induction. Their difference is a derivation, hence a vector in \(t_{h_R}\otimes I\), with \(I=\ker(B\to A)\). Its tangent image fixes \(f_*\xi\). By Lemma 3.1 and (H4) the lift action is free, so that image is zero. The tangent isomorphism makes the derivation zero, and \(f=g\). Induction proves bijectivity on every object, and naturality gives \(F\simeq h_R\). \(\square\)

Hulls are unique up to a noncanonical isomorphism of their rings and formal objects. To check this, let \((R,\xi)\) and \((R',\xi')\) be hulls. Smoothness constructs compatible maps \(R\to R'/\mathfrak m_{R'}^n\) realizing \(\xi'\), and hence a map \(R\to R'\); likewise one obtains \(R'\to R\). Both maps induce isomorphisms on relative cotangent spaces. Complete Nakayama makes them surjective: lift generators degree by degree and take their convergent sums. Their composites are surjective endomorphisms of Noetherian rings and therefore isomorphisms. For the latter assertion, the kernels of powers stabilize; if \(f(x)=0\), lift \(x=f^n(y)\) by surjectivity at an index with \(\ker f^n=\ker f^{n+1}\), obtaining \(x=0\). Thus both original maps are isomorphisms. Nothing in this argument makes the chosen isomorphism canonical.

## 6 Groupoids and the automorphism-lifting criterion

A category cofibred in groupoids over \(\mathcal C_\Lambda\) records objects, their isomorphisms and their pushforwards along base changes. Its fibre \(\mathcal D(A)\) is a groupoid. A **predeformation category** here has terminal fibre over \(k\). For geometric deformations one achieves this by fixing an identification with the special fibre and requiring all isomorphisms to respect it.

The **Rim–Schlessinger condition (RS)** says that, whenever \(A''\to A\) is surjective, the natural functor

\[
\mathcal D(A'\times_A A'')\longrightarrow
\mathcal D(A')\times_{\mathcal D(A)}\mathcal D(A'')
\]

is an equivalence. The groupoid fibre product includes a specified isomorphism between the two reductions. This is stronger information than just saying that their isomorphism classes agree. Let \(\overline{\mathcal D}(A)\) be its set of isomorphism classes.

**Theorem 6.1.** A predeformation category satisfying (RS), with finite-dimensional tangent space, has a formal object \(\xi\) over a complete Noetherian local ring \(R\) that is smooth as a morphism \(h_R\to\mathcal D\) and induces an isomorphism of tangent spaces. Its isomorphism-class transformation is a hull. Here smoothness of the groupoid morphism allows a specified isomorphism on the smaller base in every lifting problem.

**Proof.** (RS) makes \(\overline{\mathcal D}\) satisfy (H1): choose an isomorphism between compatible reductions and glue in the groupoid fibre product. It makes (H2) bijective because \(\mathcal D(k)\) is terminal: over \(k\) the gluing isomorphism is unique, so the isomorphism classes of that fibre product are exactly the product of the two sets of isomorphism classes. The tangent-space construction of Lemma 2.1 therefore applies.

Repeat the construction of Theorem 4.3 using actual objects \(\xi_n\), with a chosen isomorphism between each reduction and \(\xi_{n-1}\). In Lemma 4.1 the lifts over \(C/J'\) and \(C/K\) have a specified common reduction \(\xi_n\). The equivalence (RS) glues them over \(C/(J\cap K)\), respecting those identifications. Thus the smallest ideal exists with this stronger meaning as well. The compatible objects and isomorphisms give a formal groupoid object over \(R\).

It remains to verify smoothness with a prescribed reduction isomorphism. Suppose \(y\in\mathcal D(B)\) and an isomorphism \(a_*\xi\simeq y_A\) are given for a small extension \(B\to A\). Form \(C=A_n\times_A B\) as in Theorem 4.3. By (RS) there is an object \(z\) over \(C\) with prescribed restrictions \(\xi_n,y\) and precisely that gluing isomorphism. The same minimal-ideal argument supplies a map \(R\to C\) lifting \(R\to A_n\).

For completeness, the correction argument now concerns lifts with a chosen identification of their reduction. Their isomorphism classes are a torsor under \(t_{\mathcal D}\otimes I\). To see this, glue two such lifts by their specified reduction identification over \(B\times_A B\). Using its isomorphism with \(B\times_k k[I]\), (RS) identifies the glued object with the first lift and an object over \(k[I]\). Pullback by the addition map recovers the second lift with its given reduction identification. If the tangent object is zero, the same equivalence gives an isomorphism of the two lifts respecting that identification. Conversely such an isomorphism makes the tangent object zero. This proves transitivity and freeness for these *identified* lifts.

Apply this argument to \(C\to A_n\): the chosen pushforward of \(\xi\) and \(z\) differ by a tangent vector. Adjust the map \(R\to C\) by its corresponding derivation, using the tangent isomorphism. Its pushforward is then isomorphic to \(z\), with the prescribed reduction identification. Composition with \(C\to B\) solves the original groupoid lifting problem. Factorization into small extensions proves smoothness for all surjections. The construction has exactly \(\dim_k t_{\mathcal D}\) relative tangent parameters, so is miniversal in the stated sense, and its isomorphism-class map is a hull. \(\square\)

The chosen reduction identification in this proof is essential. After forgetting it, the lift action on isomorphism classes can have stabilizers, as in Lemma 3.1.

**Proposition 6.2 (automorphism lifting).** For a predeformation category satisfying (RS), its isomorphism-class functor satisfies (H4) if and only if for every object \(y\in\mathcal D(B)\) and every small extension \(B\to A\), the map

\[
\operatorname{Aut}_B(y)\longrightarrow\operatorname{Aut}_A(y_A)
\]

is surjective.

**Proof.** Assume (H4), fix an automorphism \(\alpha\) of \(y_A\), and compare the two groupoid gluing objects \((y,y,\alpha)\) and \((y,y,1)\) over \(B\times_A B\). Their two restrictions have identical isomorphism classes. By (H4) their glued objects are isomorphic, and full faithfulness in (RS) gives automorphisms \(\beta_1,\beta_2\) of \(y\) whose reductions differ by \(\alpha\). Their appropriate quotient lifts \(\alpha\).

Conversely, consider two groupoid gluings with the same classes of their two component objects. Choose component isomorphisms. The failure of these isomorphisms to respect the gluing isomorphisms is an automorphism over the common smaller base. Lift that automorphism to the component over the surjective side, and modify its isomorphism. The component isomorphisms now form an isomorphism in the groupoid fibre product, hence of the glued objects by (RS). This proves injectivity on isomorphism classes. Surjectivity follows directly from (RS). Small-extension factorization supplies the same argument for any surjective side, and in particular proves (H4). \(\square\)

Nonzero infinitesimal automorphisms alone do not obstruct prorepresentability. What matters is the existence of automorphisms on a smaller deformation that fail to lift to an existing deformation on the larger base.

## 7 Smooth proper schemes: gluing is the obstruction

Let \(X\) be smooth and proper over \(k\). A marked deformation over \(A\in\mathcal C_\Lambda\) is a flat proper finitely presented \(A\)-scheme \(X_A\), with an isomorphism of its closed fibre with \(X\). Isomorphisms must respect the marking. Write

\[
T_X=\mathcal Hom_{\mathcal O_X}(\Omega_{X/k},\mathcal O_X).
\]

Every such deformation is smooth over \(A\): it is flat and finitely presented and its geometric fibres are smooth [Stacks, Tag 01V8]. Its affine opens over an affine open of \(X\) are affine, since nilpotent thickenings preserve affineness [Stacks, Tag 06AD].

Here is the local lifting input in a form that also works when \(\Lambda\) has mixed characteristic. Refine an affine cover of \(X\) to standard smooth presentations, with an invertible Jacobian minor [Stacks, Tag 01V7]. Lift their polynomial coefficients to \(\Lambda\) and invert the lifted minor. The standard-smooth criterion [Stacks, Tag 00T7] gives smooth, hence flat, affine \(\Lambda\)-models of those opens. Given a marked deformation of one such open over \(A\), formal smoothness of the model lifts its special-fibre coordinate map to the deformation algebra. Tensoring to \(A\) gives an isomorphism. Indeed it is surjective by nilpotent Nakayama, and its kernel is zero by flatness and the same argument applied to the kernel after reduction. Formal smoothness of a smooth finitely presented algebra is [Stacks, Tag 00TN].

It follows that local smooth deformations lift over every small extension and that any two lifts are locally isomorphic with a prescribed isomorphism on the smaller base. To verify the latter directly, a smooth algebra on the larger base lifts a map into the smaller-base reduction of the other algebra; the lifted map is an isomorphism by the preceding flat nilpotent argument.

**Lemma 7.1.** The category of marked smooth proper deformations of \(X\) satisfies (RS).

**Proof.** Suppose deformations over \(A',A''\) have a specified common reduction over \(A\), with \(A''\to A\) surjective. Work on the standard smooth affine opens just chosen. Their deformation algebras are isomorphic to the base changes of a common smooth \(\Lambda\)-model. The specified comparison over \(A\) lifts to an automorphism on the \(A''\)-side by formal smoothness; adjust that trivialization to make the comparisons equal. The fibre product of the two algebras over the common reduction is then the base change of the same model to \(A'\times_A A''\): tensor the exact sequence

\[
0\longrightarrow A'\times_A A''\longrightarrow A'\oplus A''
\xrightarrow{(a',a'')\mapsto a'-a''} A\longrightarrow0
\]

with the flat \(\Lambda\)-model. The resulting algebra is flat and finitely presented over the fibre-product base.

On intersections, the two transition isomorphisms give a unique transition isomorphism of these fibre-product algebras, by the universal property of the ring fibre product. Their cocycle identities hold because they hold on both projections. One may refine intersections by principal affine opens; localization of these flat fibre-product models gives exactly those refinements. They therefore glue to a deformation over \(A'\times_A A''\). It is proper because its closed fibre is proper and properness extends across a nilpotent thickening in this finitely presented setting [Stacks, Tag 0BPG].

The construction is unique up to the specified component isomorphisms. A morphism of two glued objects is determined on each affine open by its two component algebra maps, and such maps glue exactly when their reductions agree. This proves full faithfulness as well as essential surjectivity, which is (RS). \(\square\)

**Proposition 7.2.** For a small extension \(B\to A\) with kernel \(I\), a marked deformation \(X_A\) has a canonical obstruction class

\[
o(X_A,B)\in H^2(X,T_X)\otimes_k I.
\]

It lifts if and only if this class is zero. When it lifts, the isomorphism classes of lifts with a specified identification of their reduction form a torsor under \(H^1(X,T_X)\otimes I\). The automorphisms of a lift that reduce to the identity form \(H^0(X,T_X)\otimes I\). In particular the tangent space is \(H^1(X,T_X)\).

**Proof.** Take a finite affine cover \(U_i\) of \(X\), refining further where necessary for the local smooth lifting argument. All finite intersections are affine because \(X\) is separated. Choose smooth lifts of the corresponding opens of \(X_A\) to \(B\). On their overlaps choose isomorphisms \(g_{ij}\) lifting the original transition isomorphisms, with \(g_{ji}=g_{ij}^{-1}\).

An automorphism of a flat \(B\)-algebra that reduces to the identity over \(A\) has the form \(1+D\), where

\[
D\in\operatorname{Der}_k(\mathcal O_X,\mathcal O_X)\otimes I.
\]

To prove this, subtract the identity. Its image lies in \(I\mathcal O_{X_B}=I\otimes_k\mathcal O_X\) by flatness, and multiplication gives the derivation law since \(I^2=0\). It depends only on the special-fibre argument since \(\mathfrak m_BI=0\). Conversely every such derivation gives a ring automorphism \(1+D\), with inverse \(1-D\). The composition of these automorphisms adds their derivations.

The triple-overlap error

\[
g_{ij}g_{jk}g_{ki}=1+c_{ijk}
\]

is thus a section of \(T_X\otimes I\). On a quadruple overlap associativity of composition, followed by reduction to the special fibre, gives

\[
c_{jkl}-c_{ikl}+c_{ijl}-c_{ijk}=0.
\]

Conjugation of an infinitesimal derivation by a transition map uses its special-fibre restriction, so this identity is precisely the Čech cocycle identity for the sheaf \(T_X\). Changing \(g_{ij}\) by \(1+b_{ij}\) changes \(c\) by the Čech coboundary of the one-cochain \(b\), with the sign determined by which side is used for multiplication. Changing the local lifts first identifies them by local isomorphisms and has the same effect. Refining the cover preserves the cohomology class. This proves that \([c]\) is well-defined.

The class vanishes exactly when one can modify the overlap isomorphisms to satisfy the cocycle identity, after which they glue the local lifts to \(X_B\). Conversely a global lift supplies overlaps with zero triple error. Affine Čech cohomology computes the cohomology of the quasi-coherent sheaf \(T_X\), so this is the stated obstruction in \(H^2\).

For two global lifts, choose local isomorphisms respecting their reduction identification. Their overlap discrepancies form a one-cocycle in \(T_X\otimes I\). Changing the local isomorphisms changes it by a zero-cochain coboundary. Zero discrepancy class is exactly the existence of a global isomorphism with the given reduction identification. All one-cocycles occur by modifying the gluing maps of one lift. This gives the torsor under \(H^1\). An automorphism reducing to the identity consists of compatible local derivations, hence of a global section of \(T_X\otimes I\). Finally, over the dual numbers the constant deformation supplies the zero point, so the torsor is canonically the vector space \(H^1(X,T_X)\). \(\square\)

**Theorem 7.3.** The marked deformation functor of a smooth proper \(X/k\), on \(\mathcal C_\Lambda\), has a hull with tangent space \(H^1(X,T_X)\). If \(H^0(X,T_X)=0\), it is prorepresentable. If \(H^2(X,T_X)=0\), it is smooth and a hull ring is

\[
\Lambda[[t_1,\ldots,t_r]],\qquad r=\dim_kH^1(X,T_X).
\]

**Proof.** Lemma 7.1 gives (RS), and Proposition 7.2 identifies the tangent space. Proper coherent cohomology makes it finite-dimensional, so Theorem 6.1 gives a hull. If \(H^0(T_X)=0\), every marked automorphism is the identity: induct along a small-extension filtration of the base, using the zero automorphism kernel in Proposition 7.2 at each step. All automorphism maps are therefore surjective, and Proposition 6.2 and Schlessinger's theorem give prorepresentability.

If \(H^2(T_X)=0\), every deformation lifts along a small extension, hence the functor is smooth. A hull \(h_R\to F\) then makes \(h_R\) smooth as well: first lift its image in \(F\), then use the smooth hull map to lift the given ring map. A complete Noetherian local \(\Lambda\)-algebra with this lifting property and relative tangent dimension \(r\) is a power-series ring. One direct verification is to choose a surjection \(S=\Lambda[[t_1,\ldots,t_r]]\to R\) inducing the tangent isomorphism. On \(S/(\mathfrak m_S^2+\mathfrak m_\Lambda S)=k\oplus k^r\), choose the map from \(R\) corresponding to the inverse relative cotangent map. Such maps are exactly residue maps plus \(\Lambda\)-derivations, as in Section 2. Smoothness lifts this chosen map first to \(S/\mathfrak m_S^2\) and then compatibly to all \(S/\mathfrak m_S^n\), giving a map \(R\to S\) with the desired tangent map. Complete Nakayama makes it surjective. Its composite endomorphism of \(R\) is surjective and hence an isomorphism; it follows that \(S\to R\) has zero kernel and is an isomorphism. Thus the displayed ring is a hull, and it is a prorepresenting ring when the preceding automorphism criterion also holds. \(\square\)

## 8 Curves, plane embeddings and a cubic's automorphisms

Let \(C\) be a smooth proper geometrically connected curve of genus \(g\). Its canonical bundle has degree \(2g-2\), and \(T_C=\omega_C^{-1}\). Riemann–Roch [Stacks, Tag 0BS6] gives

\[
\chi(T_C)=3-3g.
\]

For \(g\geq2\), the degree of \(T_C\) is negative, so it has no nonzero section: a nonzero section of a line bundle produces an effective divisor of its degree. Therefore

\[
h^0(T_C)=0,\qquad h^1(T_C)=3g-3,
\qquad H^2(C,T_C)=0.
\]

Theorem 7.3 proves that its marked deformation functor is prorepresented by \(\Lambda[[t_1,\ldots,t_{3g-3}]]\). This holds in every characteristic. Ordinary automorphisms of the special curve do not change the conclusion: the marking only permits automorphisms that reduce to its identity.

For a smooth plane curve \(C=V(f)\) of degree \(d\), the embedded first-order deformation is an equation \(f+\epsilon g\). Replacing it by a unit multiple changes \(g\) by a scalar multiple of \(f\). Thus its tangent space is

\[
H^0(C,\mathcal O_C(d)),\qquad
\dim=\binom{d+2}{2}-1.
\]

The ideal sequence \(0\to\mathcal O_{\mathbb P^2}\xrightarrow{f}\mathcal O_{\mathbb P^2}(d)\to\mathcal O_C(d)\to0\) proves this dimension, using \(H^1(\mathbb P^2,\mathcal O)=0\). The forgetful map to abstract deformations is the connecting homomorphism in

\[
0\longrightarrow T_C\longrightarrow
T_{\mathbb P^2}|_C\longrightarrow\mathcal O_C(d)\longrightarrow0. \tag{8.1}
\]

To check the interpretation, lift an embedded deformation locally by a change of ambient coordinates. On an overlap, their difference is a tangent vector preserving \(C\); these are precisely the one-cocycle defining its abstract deformation. This is the connecting map of (8.1). The exact sequence exists because a smooth hypersurface is a regular immersion and the conormal sequence is locally split by the smooth Jacobian criterion.

The Euler sequence is \(0\to\mathcal O\to\mathcal O(1)^3\to T_{\mathbb P^2}\to0\): on a coordinate chart its first map is the three homogeneous coordinates, and differentiating the two coordinate ratios identifies its quotient with the tangent bundle. Its dual has determinant \(\mathcal O(-3)\). Taking determinants in the conormal sequence of \(C\) therefore gives \(\omega_C=\mathcal O_C(d-3)\). Its degree is \(d(d-3)=2g-2\), so \(g=(d-1)(d-2)/2\). Embedded and abstract parameter spaces consequently have different tangent dimensions. For a plane quartic, the embedded dimension is \(14\), the abstract dimension is \(6\), and the kernel has dimension \(8\), the projective-coordinate directions. The restriction of the Euler sequence, followed by Serre duality, shows \(H^1(T_{\mathbb P^2}|_C)=0\): the relevant dual map \(k^3\to H^0(\mathcal O_C(1))\) is an isomorphism. Thus every first-order abstract quartic deformation is induced by a plane deformation.

For a plane quintic the embedded dimension is \(20\), while its genus is \(6\) and its abstract dimension is \(15\). The same Euler calculation gives \(h^0(T_{\mathbb P^2}|_C)=8\) and \(h^1(T_{\mathbb P^2}|_C)=3\): dually the multiplication map \(H^0(\mathcal O_C(1))^3\to H^0(\mathcal O_C(2))\) is onto, with kernel dimension \(9-6=3\). Also \(H^1(\mathcal O_C(5))=0\), since its Serre-dual bundle is \(\mathcal O_C(-3)\). Exactness of (8.1) therefore gives a three-dimensional space of abstract directions absent from the plane family. Keeping the ambient embedding is a real constraint.

Now let \(C\) be a smooth plane cubic over an algebraically closed field. Then \(T_C=\mathcal O_C\), so \(h^0(T_C)=h^1(T_C)=1\) and \(H^2(T_C)=0\). Its hull has one parameter. We prove that its abstract marked functor is nevertheless prorepresentable.

We need a group-law fact, which can be proved in this particular setting. Let \(E\to\operatorname{Spec}A\) be a smooth proper genus-one curve with a section \(e\). For two sections \(P,Q\) after any base change \(T\), put \(M=\mathcal O(P+Q-e)\). On each field fibre this line bundle has degree one, so \(h^0=1\) and \(h^1=0\). Proper flat cohomology [Stacks, Tag 0A1H] makes \(p_*M\) a line bundle, compatibly with base change. Its evaluation defines an effective relative divisor of degree one: the section is nonzero on every fibre, and the Cartier criterion [Stacks, Tag 062Y] makes its zero divisor flat. The divisor is proper with finite fibres, hence finite [Stacks, Tag 02LS], and finite locally free of rank one, hence a section \(R\).

This section is the unique one with \(\mathcal O(R)\) equal to \(M\) up to a line bundle from the base, because evaluation of its one-dimensional section space has a unique zero divisor. Define \(P+Q=R\). Uniqueness of this degree-one representative proves associativity, since both associations represent \(\mathcal O(P+Q+R-2e)\); it also proves commutativity and identity \(e\). The degree-one bundle \(\mathcal O(2e-P)\) gives the inverse. These constructions commute with all base changes and hence define morphisms by Yoneda. They give the elliptic group law over \(A\), with no characteristic restriction.

In a deformation of \(C\), choose a section lifting a fixed point of \(C(k)\); smoothness supplies it through each Artinian extension. Any marked automorphism \(\alpha\) factors as translation by \(\alpha(e)\), followed by an automorphism \(\beta\) fixing \(e\) and reducing to the identity. Such a \(\beta\) is the identity. Indeed its kernel at a small extension consists of vector fields vanishing at \(e\), and

\[
H^0(C,T_C(-e))=H^0(C,\mathcal O_C(-e))=0.
\]

Induction along a filtration of the base proves the assertion. Consequently every marked automorphism is a translation by a section reducing to \(e\). Given an existing larger-base deformation, that section lifts by its smoothness, and its translation lifts the automorphism. Proposition 6.2 gives (H4). Together with the already proved hull and unobstructedness, this proves prorepresentation by \(\Lambda[[t]]\). It is an explicit example where \(H^0(T_C)\ne0\) and automorphism lifting succeeds.

## 9 Line bundles on a fixed scheme

Fix a smooth proper \(X/k\) and a line bundle \(L\). In this section the base ring is \(\Lambda=k\), and the underlying family is the fixed product \(X_A=X\times_k\operatorname{Spec}A\). Consider line bundles on \(X_A\) with a specified identification of their reduction with \(L\), up to isomorphisms respecting this identification.

For a small extension \(B\to A\) with kernel \(I\), the sheaves of units on this fixed family have an exact sequence

\[
1\longrightarrow 1+I\mathcal O_X
\longrightarrow\mathcal O_{X_B}^{\times}
\longrightarrow\mathcal O_{X_A}^{\times}\longrightarrow1,
\qquad 1+I\mathcal O_X\simeq\mathcal O_X\otimes I.
\]

Surjectivity holds locally by lifting a unit across a nilpotent ideal; multiplication of \(1+u\) and \(1+v\) adds \(u,v\) because \(I^2=0\). The cohomology sequence, or equivalently lifting transition functions on an affine cover, places the obstruction to lifting the line bundle in \(H^2(X,\mathcal O_X)\otimes I\). When it vanishes, identified lifts form a torsor under \(H^1(X,\mathcal O_X)\otimes I\). In particular the tangent space is \(H^1(X,\mathcal O_X)\).

These line bundles form an (RS) category: locally their modules are free of rank one, and one may lift the common-base comparison unit along the surjective side to align their bases. The aligned modules glue over the fibre-product ring; their transition units and all isomorphisms are recovered from their two components. Theorem 6.1 therefore gives a hull.

The automorphisms of a line bundle are global units of \(\mathcal O_{X_A}\), independently of \(L\). For the fixed product,

\[
H^0(X_A,\mathcal O_{X_A})=H^0(X,\mathcal O_X)\otimes_k A.
\]

One can check this directly with an affine Čech complex and the flatness of \(A\) over \(k\). Thus global units lift across every small extension, since the corresponding algebra surjection has nilpotent kernel. Units reducing to one have lifts reducing to one as well. Proposition 6.2 proves prorepresentability. For a smooth proper geometrically connected curve of genus \(g\), \(H^2(\mathcal O)=0\) and \(h^1(\mathcal O)=g\). Its formal Picard functor is therefore smooth and prorepresented by \(k[[t_1,\ldots,t_g]]\). This is a formal statement; global existence of its Picard scheme will be proved later.

## 10 The node: a smooth hull with nonunique parameters

Let \(\Lambda=k\), and let \(F\) classify marked flat algebra deformations of the affine node \(k[x,y]/(xy)\). The completed-node version uses continuous maps and \(k[[x,y]]/(xy)\); the calculation below gives the same hull for it. The family

\[
k[[t]]\longrightarrow F,\qquad
t\longmapsto A[x,y]/(xy-t_A),\quad t_A\in\mathfrak m_A,
\]

means the natural transformation from \(h_{k[[t]]}\), not a map of a ring into a set. These algebras are flat over \(A\). Polynomial reduction by \(xy=t_A\) gives an \(A\)-basis \(1,x,x^2,\ldots,y,y^2,\ldots\). Completion preserves flatness, by the flatness of Noetherian completion [Stacks, Tag 00MB].

Every deformation has a presentation \(A[x,y]/(f)\) with \(f\equiv xy\pmod{\mathfrak m_A}\). Lift the two generators to its algebra \(D\). The map \(A[x,y]\to D\) is onto by nilpotent Nakayama applied to its cokernel. Flatness of \(D\) identifies the reduction of its kernel with the ideal \((xy)\). Lift its generator to \(f\); Nakayama, with the nilpotent base ideal, makes the entire kernel generated by \(f\). The same argument with topological generators and the finite ideal of a Noetherian power-series ring gives the completed presentation.

To prove the lifting property for the proposed hull, take a small extension \(B\to A\) with kernel \(I\), an equation \(xy-t_A\), and a deformation over \(B\) identified with it on reduction. Lift the chosen generators and the relation so that its equation is

\[
f=xy-\widetilde t+h,\qquad h\in I[x,y],
\]

where \(\widetilde t\) lifts \(t_A\). Write uniquely its constant term \(s\in I\), and express the rest as \(xu+yv\), with \(u,v\in I[x,y]\). Set \(x'=x+v\), \(y'=y+u\). These changes are invertible: their correction operator has square zero since \(I^2=0\). They preserve the prescribed smaller-base coordinates, and

\[
f=x'y'-(\widetilde t-s).
\]

Thus the prescribed parameter lifts to \(t_B=\widetilde t-s\). The identical manipulation works for formal series. On dual numbers the constant correction is invariant under all coordinate changes reducing to the identity: such a change adds a multiple of \(x\) or \(y\), and multiplying the equation by a unit adds a multiple of \(xy\). Therefore \(t_F=k\). We have proved smoothness and a tangent isomorphism, so \(k[[t]]\), with equation \(xy=t\), is a hull.

This hull is not a prorepresenting object. To check the automorphism criterion explicitly, put

\[
A=k[e]/(e^2),\qquad B=k[e]/(e^3),\qquad
D_B=B[x,y]/(xy-e).
\]

On \(D_A\), the map \(x\mapsto(1+e)x\), \(y\mapsto y\) is an automorphism reducing to the identity on the special fibre, because \((1+e)e=e\) in \(A\). A lift to \(D_B\) would have the form

\[
x\longmapsto(1+e)x+e^2u,\qquad
y\longmapsto y+e^2v.
\]

Preserving \(xy=e\) would imply

\[
e^2(1+uy+xv)=0.
\]

Flatness identifies the coefficient of \(e^2\) with the special-fibre algebra, so this requires \(1+uy+xv=0\) in \(k[x,y]/(xy)\), impossible after quotienting by \((x,y)\). The automorphism does not lift.

For applying Proposition 6.2, the algebra deformation category has (RS). Here is the module mechanism. Flat modules over an Artinian local ring are free: lift a basis modulo the maximal ideal, use nilpotent Nakayama for surjectivity, and use flatness followed by nilpotent Nakayama to kill the kernel. Given two flat deformation algebras with a common identified reduction, align their module bases along the surjective side by lifting that basis. Their fibre-product module is free over the base fibre-product ring, with exactly this basis, and its multiplication is the componentwise multiplication. It recovers the original algebras on base change, and morphisms are recovered by the ring fibre-product property. The resulting algebra is finitely presented: lift the two special-fibre generators, obtain a surjection from the polynomial ring by nilpotent Nakayama, and use its Noetherianity. This proves (RS) for the affine node.

In the completed case choose compatible lifts of \(x,y\) in the two component algebras. A power series in these lifts can be evaluated componentwise, since both algebras are complete; the evaluations agree in the common reduction. This defines a map from the power-series ring over the base fibre product to the fibre-product algebra. Its reduction is the usual surjection onto \(k[[x,y]]/(xy)\), so nilpotent Nakayama makes the map surjective. The fibre-product algebra is therefore a quotient of a complete Noetherian power-series ring, and is complete because its kernel is closed. This proves (RS) also in the completed setting. Proposition 6.2 now shows failure of (H4), hence failure of prorepresentability.

The one smoothing parameter and the smooth hull therefore coexist with nonunique higher-order classification. The displayed nonlifting automorphism identifies the exact reason.

## 11 Exercises with complete solutions

**Exercise 1.** Prove that \(h_R\), for a complete Noetherian local \(\Lambda\)-algebra \(R\) with residue field \(k\), satisfies (H1)–(H4).

**Solution.** A map \(R\to A'\times_A A''\) is exactly a pair of local \(\Lambda\)-algebra maps to \(A',A''\) with the same composite to \(A\). Localness and continuity follow from those of the two component maps. Thus the comparison map in Section 2 is bijective for every admissible diagram, giving (H1), (H2) and (H4). Its tangent space is the dual of \(\mathfrak m_R/(\mathfrak m_R^2+\mathfrak m_\Lambda R)\). This quotient is finite-dimensional because \(R\) is Noetherian, giving (H3).

**Exercise 2.** Verify (H1)–(H3) for the marked deformation functor of a smooth proper \(X/k\).

**Solution.** Lemma 7.1 gives the groupoid equivalence over every fibre product with a surjective side. For (H1), choose an isomorphism between the two identified common reductions and glue its groupoid object. For (H2), the common reduction is over \(k\), whose marked groupoid has only the identity object and identity automorphism. Hence the gluing isomorphism is unique, and the equivalence gives a bijection of isomorphism classes. Proposition 7.2 identifies the tangent space as \(H^1(X,T_X)\). The tangent sheaf is coherent and \(X\) is proper, so this cohomology is finite-dimensional. This is (H3). No vanishing of \(H^0(T_X)\) was used in these three conditions.

**Exercise 3.** For a smooth proper geometrically connected curve of genus \(g\geq2\), prove prorepresentability and smoothness with \(3g-3\) parameters.

**Solution.** The tangent bundle is \(\omega_C^{-1}\), of degree \(2-2g<0\), so \(H^0(T_C)=0\). Thus every automorphism reducing to the identity on the marked fibre is the identity, inducting through small extensions with the derivation kernel of Proposition 7.2. Automorphism lifting holds, which gives (H4), and Exercise 2 gives the other conditions. Schlessinger's theorem proves prorepresentability. A coherent sheaf on a curve has no second cohomology, so every small-extension obstruction vanishes and the functor is smooth. Riemann–Roch gives \(\chi(T_C)=3-3g\); with \(H^0=0\), the tangent dimension is \(3g-3\). The final power-series argument in Theorem 7.3 identifies the prorepresenting ring with \(\Lambda[[t_1,\ldots,t_{3g-3}]]\).

**Exercise 4.** Compute a hull for the node \(xy=0\). Decide whether it prorepresents the unframed-coordinate deformation functor.

**Solution.** The relation presentation and the small-extension normalization in Section 10 show that all lifts of \(xy-t_A\) have the form \(xy-t_B\), with coordinates chosen to respect the specified reduction. A perturbation \(h\) has a constant part \(s\); the remaining part is \(xu+yv\) and is removed by \(x'=x+v\), \(y'=y+u\). The parameter changes to \(\widetilde t-s\). Thus the family over \(k[[t]]\) is formally smooth as a morphism to the deformation functor. On dual numbers the only invariant relation perturbation is its constant term, so its tangent map is an isomorphism and it is a hull. This remains true for the completed node.

The automorphism \(x\mapsto(1+e)x,y\mapsto y\) on \(k[e]/(e^2)[x,y]/(xy-e)\) cannot lift to the identical equation over \(k[e]/(e^3)\): any lift would force \(1+uy+xv=0\) on the closed-fibre node. Its value at the singular point would be \(1=0\). This violates the automorphism-lifting criterion, so the hull does not prorepresent the functor that forgets coordinate choices. Marking the special fibre has been retained; it does not mean fixing the coordinates at every order.

**Exercise 5.** Prove the existence of a hull under (H1)–(H3) by successive approximation. Explain why the resulting formal object is smooth, rather than only surjective on objects.

**Solution.** Choose a tangent basis and \(S=\Lambda[[x_1,\ldots,x_r]]\). Set \(J_2=\mathfrak m_S^2+\mathfrak m_\Lambda S\), with its universal first-order element. At stage \(n\), look at lifts across \(S/\mathfrak m_SJ_n\to S/J_n\). The ideals killing the obstruction are closed under intersection by (H1), after enlarging one of a pair to make their sum the full socle. Finite-dimensionality of \(J_n/\mathfrak m_SJ_n\) therefore gives a smallest such ideal \(J_{n+1}\), and choose a lift over it. Let \(J=\bigcap J_n\), \(R=S/J\). Lemma 4.2 makes these quotients a cofinal system of Artinian neighbourhoods of \(R\), so the compatible lifts form a formal object. The tangent map remains an isomorphism because all \(J_n\), and hence \(J\), lie in \(J_2\).

For a prescribed small-extension lifting problem \(R\to A\), \(y\in F(B)\), factor the ring map through \(A_n=S/J_n\) and form \(C=A_n\times_A B\). If \(C\to A_n\) splits, it immediately yields a ring lift. Otherwise a lift of the variables makes \(S\to C\) surjective: an image missing the one-dimensional kernel would give a section. Its kernel lies between \(\mathfrak m_SJ_n\) and \(J_n\), and (H1) gives a lift of the current element over \(C\). Minimality forces that kernel to contain \(J_{n+1}\), so a ring lift \(R\to B\) exists. It may yield the wrong lift in \(F(B)\); transitivity of the tangent action and the tangent isomorphism correct it by a derivation \(R\to\ker(B\to A)\). The corrected map yields exactly \(y\), preserving its prescribed reduction. This proves the smooth lifting property, the missing step in a mere object-surjectivity argument.

## 12 What this lesson does not prove

Schlessinger's theorem, the groupoid miniversal construction, the automorphism-lifting criterion and the smooth proper tangent–obstruction calculation were proved here. The foundational inputs are:

- The usual properties of complete Noetherian local rings, including closedness of ideals by Krull intersection and complete Nakayama; flatness of Noetherian completion is [Stacks, Tag 00MB]. Lemma 4.2 gives the additional descending-ideal cofinality argument needed in the construction.
- A smooth finitely presented algebra is formally smooth [Stacks, Tag 00TN], and a flat finitely presented morphism with smooth geometric fibres is smooth [Stacks, Tag 01V8]. Smooth morphisms locally have standard-smooth presentations [Stacks, Tag 01V7]; an invertible Jacobian minor makes those presentations smooth [Stacks, Tag 00T7]. These supply the coefficient lifts used in Section 7.
- Affineness is invariant under nilpotent thickenings [Stacks, Tag 06AD], and properness extends across a base thickening for the locally finite-type morphisms with the stated cartesian closed fibre [Stacks, Tag 0BPG].
- Affine Čech cohomology computes quasi-coherent sheaf cohomology on a separated scheme [Stacks, Tag 01XD]. Proper coherent cohomology over a field is finite-dimensional [Stacks, Tag 02O6]. The derivation, cocycle and obstruction constructions using these prerequisites were proved in Proposition 7.2.
- Riemann–Roch for smooth proper curves is [Stacks, Tag 0BS6]. Curve duality identifies \(H^1(M)^\vee\) with \(H^0(M^\vee\otimes\omega_C)\), and for a smooth proper curve \(\omega_C=\Omega_{C/k}\) [Stacks, Tag 0BS2]. The Euler and plane-curve adjunction sequences were derived in Section 8 before using these prerequisites.
- Proper flat cohomology with arbitrary base change [Stacks, Tag 0A1H], the relative Cartier criterion [Stacks, Tag 062Y], and properness with finite fibres implying finiteness [Stacks, Tag 02LS] are used in the degree-one construction of the elliptic group law. The uniqueness and group identities, and the subsequent automorphism lifting, were proved here.

A formal hull is not asserted to be algebraizable, or to represent a functor on all schemes. Those are separate existence questions. The smoothness conclusions above are formal lifting statements on the Artinian category.

## References

- Schlessinger, *Functors of Artin rings*, Transactions of the American Mathematical Society **130** (1968), 208–222, Theorem 2.11. [Original paper](https://doi.org/10.1090/S0002-9947-1968-0217093-3).
- The Stacks project, *Formal deformation theory*: [tangent spaces](https://stacks.math.columbia.edu/tag/06IH), [versal construction](https://stacks.math.columbia.edu/tag/06IW), [miniversal objects](https://stacks.math.columbia.edu/tag/06IX), and [automorphism lifting](https://stacks.math.columbia.edu/tag/06J8). The tagged texts are read in the AI Integrated Stacks Project edition.
- The Stacks project, *Deformation problems*: [scheme tangent spaces](https://stacks.math.columbia.edu/tag/0DY6) and [proper finiteness](https://stacks.math.columbia.edu/tag/0DYA).
- Grothendieck, *Technique de descente et théorèmes d'existence en géométrie algébrique II: le théorème d'existence en théorie formelle des modules*, Séminaire Bourbaki, Exposé 195, Parts A–C. [Original text](https://www.numdam.org/item/SB_1958-1960__5__369_0/). Also *Géométrie formelle et géométrie algébrique*, Exposé 182, §7.
- Oort, *Finite group schemes, local moduli for abelian varieties, and lifting problems*, Compositio Mathematica **23** (1971), 265–296, Propositions 2.2.5–2.2.6. [Original paper](https://www.numdam.org/item/CM_1971__23_3_265_0/).
