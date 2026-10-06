# Derived pullback and pushforward

*Written and edited by GPT-6.1 Sol (OpenAI), in Codex at Ultra, October 2026. Mathematically self-checked by the writing AI. Original contributions are CC0; the combined course is distributed under GFDL-1.2-or-later. Full authorship and source attribution appear in the course notice.*

Pullback changes both the space and the coefficient ring. Pushforward collects sections over inverse images of opens. Their ordinary adjunction survives passage to derived categories, but proving this requires two different resolutions. A K-flat model controls the tensor in pullback, and a K-injective model controls pushforward. The proof must also work when pushforward of that K-injective model is not itself K-injective.

The prerequisites are The derived tensor product and Tor sheaves, Lemma 1.1, Theorem 1.2, Lemma 2.1 and Theorem 2.2, and K-injective resolutions in Grothendieck categories, Theorems 4.1 and 5.1 and Proposition 5.2. Their earlier prerequisites supply the chain-level adjunction (first lesson, Theorem 4.4), the open-extension adjunction (Lemma 5.1 there), maps into K-injectives (bounded-derived lesson, Theorem 3.3), and roof cancellation (common reading, Theorem 4.2). For the spectral-sequence exercise we use the lower-bound preservation in Theorem 4.1 of the bounded-derived lesson.

Unless explicitly stated otherwise, all structure sheaves are commutative and unital, and all derived categories are unbounded. Let
\(f:(X,\mathcal O_X)\to(Y,\mathcal O_Y)\) be a morphism of ringed spaces. Write

\[
f^*G=\mathcal O_X\otimes_{f^{-1}\mathcal O_Y}f^{-1}G.
\tag{0.1}
\]

We retain cohomological indexing, direct-sum tensor totalization and the common reading's negative cone-projection convention. These results require no separation, Noetherian, compactness or finite homological-dimension hypothesis.

The construction sources are the Stacks project authors’ *Cohomology of Sheaves*, “Derived pullback”, “Cohomology of unbounded complexes” and “Some properties of K-injective complexes”, in the [AI Integrated Stacks Project edition](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/cohomology.tex). The proofs use resolutions, roofs and adjunction to establish the comparison maps with their actual coefficient hypotheses. Source attribution and the licence for adapted passages appear in the course notice.
## 1. Derived pullback on K-flat models

**Theorem 1.1.** Choosing a K-flat resolution \(P\to G\) and setting

\[
Lf^*G=f^*P
\tag{1.1}
\]

defines a well-defined exact functor \(Lf^*:D(\mathcal O_Y)\to D(\mathcal O_X)\). It carries K-flat models to K-flat models. For composable \(f:X\to Y\), \(g:Y\to Z\), there are canonical natural isomorphisms

\[
Lf^*Lg^*G\cong L(gf)^*G.
\tag{1.2}
\]

**Proof.** Pullback preserves K-flatness by Lemma 2.2 of the K-flat lesson. It also preserves quasi-isomorphisms **between** K-flats. Indeed, at \(x\) their pullback map is

\[
\mathcal O_{X,x}\otimes_{\mathcal O_{Y,f(x)}}P_{f(x)}
\longrightarrow
\mathcal O_{X,x}\otimes_{\mathcal O_{Y,f(x)}}P'_{f(x)}.
\]

The stalk models are K-flat; Lemma 1.1 of the tensor lesson applies to their quasi-isomorphism and the possibly nonflat module \(\mathcal O_{X,x}\). Thus this map is a quasi-isomorphism on every stalk. Pullback is additive, so it preserves homotopies, shifts and cones. Lemma 2.1 of the tensor lesson identifies the localization of K-flat models with the full derived category. Localizing pullback on those models gives the claimed exact functor and canonical comparisons for all choices and roofs.

Choose \(P\) K-flat on \(Z\). Then \(g^*P\) is K-flat on \(Y\), so the iterated derived pullback is computed by \(f^*g^*P\). Ordinary pullback composition identifies this with \((gf)^*P\). On stalks its scalar-extension map has the formula

\[
\begin{gathered}
s\otimes(t\otimes p)\longmapsto s f^\sharp(t)\otimes p,\\
s\otimes p\longmapsto s\otimes(1\otimes p).
\end{gathered}
\]

Balancing proves that these are inverse maps; scalars have degree zero, so they commute with differentials. The same balanced sheaf maps, using inverse-image composition, define the identification before taking stalks. They are natural for chain maps, hence for inverse denominators and roofs. For three successive pullbacks every association multiplies the same successive scalar images; associativity proves coherence of (1.2). \(\square\)

**Proposition 1.2 (tensor compatibility).** There are canonical natural isomorphisms

\[
\begin{gathered}
Lf^*(A\otimes_{\mathcal O_Y}^{\mathbf L}B)
\\ \cong Lf^*A\otimes_{\mathcal O_X}^{\mathbf L}Lf^*B,\\
F\otimes_{\mathcal O_X}^{\mathbf L}Lf^*G
\\ \cong F\otimes_{f^{-1}\mathcal O_Y}^{\mathbf L}f^{-1}G.
\end{gathered}
\tag{1.3}
\]

In the second line \(F\) is an \(\mathcal O_X\)-complex; the right side retains its \(\mathcal O_X\)-action from \(F\). The isomorphisms respect the tensor associativity, symmetry, unit and pullback-composition comparisons.

**Proof.** For K-flat \(P,R\) on \(Y\), their tensor is K-flat. Thus the first line is computed by the ordinary isomorphism \(f^*(P\otimes R)\cong f^*P\otimes f^*R\). On a stalk, with coefficient map \(R_0\to S\), the inverse-direction map and its inverse are

\[
\begin{gathered}
(s\otimes p)\otimes(t\otimes r)\longmapsto st\otimes(p\otimes r),\\
s\otimes(p\otimes r)\longmapsto(s\otimes p)\otimes(1\otimes r).
\end{gathered}
\]

Commutativity of the rings and balancing make the formulas well defined. Their differential signs are \(1,(-1)^{|p|}\) on both sides. Inverse image and scalar extension commute with direct sums, so the same maps identify the totalizations. They commute with elementary reassociation, the Koszul flip and units; on four scalar factors every route is scalar multiplication in the same order. Their naturality extends to localized models.

For the second line choose only a K-flat \(P\to G\). Then \(f^{-1}P\) is K-flat over \(f^{-1}\mathcal O_Y\), by the K-flat pullback criterion applied with unchanged coefficients, and \(f^*P\) is K-flat over \(\mathcal O_X\). The one-resolution construction computes both sides by

\[
F\otimes_{\mathcal O_X}
(\mathcal O_X\otimes_{f^{-1}\mathcal O_Y}f^{-1}P)
\cong F\otimes_{f^{-1}\mathcal O_Y}f^{-1}P.
\]

The map sends \(a\otimes(s\otimes p)\) to \(sa\otimes p\), with inverse \(a\otimes p\mapsto a\otimes(1\otimes p)\). This proves the asserted module action and naturality without assuming \(F\) flat. \(\square\)

There is also a natural comparison \(Lf^*G\to f^*G\) for a specified complex \(G\), induced by \(f^*P\to f^*G\). It need not be an isomorphism. All comparisons to ordinary tensor commute with (1.3): on resolving tensors both routes send \((s\otimes p)\otimes(t\otimes r)\) to \(st\otimes(\epsilon_Pp\otimes\epsilon_Rr)\). For the map \(a:P\otimes R\to A\otimes B\), Corollary 4.4 of the K-flat lesson supplies a factorization \(a=cb\) through a K-flat resolution \(c:N\to A\otimes B\). Applying pullback gives \(f^*c\,f^*b=f^*a\); the left side represents the route through \(Lf^*(A\otimes B)\) and its ordinary comparison, and the right side is the same elementary tensor formula. This proves the complete comparison square, including the augmentation maps.

## 2. Derived pushforward and the adjunction

Choose \(F\to I\) K-injective with injective terms, using Theorem 4.1 of the K-injective lesson. Theorem 5.1 there, applied to the additive functor \(f_*\), gives an exact functor

\[
\begin{gathered}
Rf_*:D(\mathcal O_X)\longrightarrow D(\mathcal O_Y),\\
Rf_*F=f_*I.
\end{gathered}
\tag{2.1}
\]

Two K-injective models are homotopy equivalent, and additive pushforward preserves these equivalences and their homotopies. Maps between the models, unique up to homotopy, define the functor on all derived morphisms. No claim about K-injectivity of \(f_*I\) is needed for this construction.

**Lemma 2.1 (a relative Hom comparison).** For \(P\) K-flat on \(Y\) and \(I\) K-injective on \(X\), localization induces a bijection

\[
\begin{gathered}
\operatorname{Hom}_{K(\mathcal O_Y)}(P,f_*I)\\
\cong
\operatorname{Hom}_{D(\mathcal O_Y)}(P,f_*I).
\end{gathered}
\tag{2.2}
\]

**Proof.** Represent a derived map by a roof \(P\leftarrow Z\to f_*I\). Resolve \(Z\) by a K-flat \(T\to Z\). Its composite \(s:T\to P\) is a quasi-isomorphism between K-flats. Theorem 1.1 makes \(f^*s\) a quasi-isomorphism. Maps into \(I\) consequently give a bijection

\[
\operatorname{Hom}_{K(\mathcal O_X)}(f^*P,I)
\longrightarrow
\operatorname{Hom}_{K(\mathcal O_X)}(f^*T,I),
\]

by Theorem 3.3 of the bounded-derived lesson. The chain-level adjunction identifies this with precomposition by \(s\) on maps into \(f_*I\). Thus the roof's numerator comes from a unique homotopy class \(P\to f_*I\), proving surjectivity of (2.2).

For injectivity, if such a homotopy class becomes zero after localization, roof cancellation (common reading, Theorem 4.2) gives a quasi-isomorphism \(Z\to P\) making its composite zero in the homotopy category. Resolve \(Z\) by a K-flat \(T\). Precomposition along the resulting \(T\to P\) is the bijection just proved by the chain adjunction, so the original class was zero. Applying this to a difference also proves injectivity for equality of two classes. \(\square\)

**Theorem 2.2 (unbounded adjunction).** There is a bifunctorial bijection

\[
\begin{gathered}
\operatorname{Hom}_{D(\mathcal O_X)}(Lf^*G,F)
\\ \cong\operatorname{Hom}_{D(\mathcal O_Y)}(G,Rf_*F).
\end{gathered}
\tag{2.3}
\]

It gives \(Lf^*\dashv Rf_*\), with natural unit \(\eta:G\to Rf_*Lf^*G\) and counit \(\epsilon:Lf^*Rf_*F\to F\).

**Proof.** Choose \(P\to G\) K-flat and \(F\to I\) K-injective. The left group is \(\operatorname{Hom}_K(f^*P,I)\), because the target is K-injective. The ordinary adjunction on complexes, including homotopies, identifies this with \(\operatorname{Hom}_K(P,f_*I)\). Lemma 2.1 identifies the latter with \(\operatorname{Hom}_D(P,f_*I)\); use \(P\simeq G\) to obtain the right group.

For naturality in \(G\), every derived map between its K-flat models is a roof with K-flat middle, by Lemma 2.1 of the tensor lesson. The chain adjunction and all Hom comparisons commute with its numerator and denominator, hence with the inverse denominator. For naturality in \(F\), derived maps between K-injective models are homotopy classes of chain maps; the adjunction commutes with them. Replacing either model uses these same comparisons. Thus (2.3) is independent of choices and bifunctorial.

Define the unit as the transpose of \(1_{Lf^*G}\), and the counit as the inverse transpose of \(1_{Rf_*F}\). Write \(L=Lf^*\), \(R=Rf_*\), and \(\alpha\) for the bijection. Naturality implies \(\alpha(u)=R(u)\eta\) and \(\alpha^{-1}(v)=\epsilon L(v)\). Applying these to \(\eta=\alpha(1)\) and \(\epsilon=\alpha^{-1}(1)\) gives

\[
\begin{gathered}
\epsilon_{LG}L(\eta_G)=1_{LG},\\
R(\epsilon_F)\eta_{RF}=1_{RF}.
\end{gathered}
\tag{2.4}
\]

These are the triangle identities, so the asserted maps give the adjunction. \(\square\)

**Corollary 2.3 (unchanged coefficients, also noncommutative).** If \(\mathcal O_X=f^{-1}\mathcal O_Y\), for any unital sheaf of rings, \(f^{-1}\dashv Rf_*\) on unbounded derived categories.

**Proof.** Inverse image is exact, and \(f_*\) is its right adjoint. Proposition 5.2 of the K-injective lesson makes \(f_*I\) K-injective. Therefore

\[
\begin{gathered}
\operatorname{Hom}_D(f^{-1}G,F)
=\operatorname{Hom}_K(f^{-1}G,I)\\
=\operatorname{Hom}_K(G,f_*I)
=\operatorname{Hom}_D(G,Rf_*F).
\end{gathered}
\]

Each equality is natural for maps and homotopies and extends to roofs. This proves the exact-coefficient adjunction without using commutative K-flat theory in the noncommutative case. \(\square\)

## 3. Composition, Leray and the local descriptions

**Proposition 3.1.** For composable morphisms \(f:X\to Y\) and \(g:Y\to Z\),

\[
Rg_*Rf_*F\cong R(gf)_*F
\tag{3.1}
\]

canonically and naturally. In particular,

\[
R\Gamma(Y,Rf_*F)\cong R\Gamma(X,F).
\tag{3.2}
\]

The second identification is in \(D(\Gamma(Y,\mathcal O_Y))\), with the right side's scalars restricted along \(\Gamma(Y,\mathcal O_Y)\to\Gamma(X,\mathcal O_X)\).

**Proof.** Successive adjunctions show that \(Rg_*Rf_*\) is right adjoint to \(Lf^*Lg^*\). Theorem 1.1 identifies the latter with \(L(gf)^*\), whose right adjoint is \(R(gf)_*\).

For completeness, a right adjoint is unique in the required canonical sense. If \(L\dashv R_1\) and \(L\dashv R_2\), send the counit \(LR_1B\to B\) through the second adjunction to a map \(\beta_B:R_1B\to R_2B\). Reverse the roles to obtain \(\gamma_B\). Naturality of the adjunctions and their triangle identities show that the transpose of \(\gamma_B\beta_B\) under the first adjunction is its counit, so \(\gamma_B\beta_B=1\); likewise \(\beta_B\gamma_B=1\). Transposing maps after a morphism \(B\to B'\) proves naturality. This is the unique isomorphism compatible with the given adjunctions, and its uniqueness also gives compatibility for three successive functors. It proves (3.1) without assuming \(f_*I\) is K-injective.

Put \(A=\Gamma(Y,\mathcal O_Y)\). The canonical morphism \(Y\to(\mathrm{pt},A)\) has pushforward \(\Gamma(Y,-)\). Its composite with \(f\) has pushforward \(\Gamma(X,-)\) with the indicated \(A\)-action. Apply (3.1) to obtain (3.2). \(\square\)

**Proposition 3.2 (opens and cohomology sheaves).** Let \(U\subset X\) and \(V\subset Y\) be open, and for the restriction formula set \(U=f^{-1}V\), \(f_V:U\to V\). Then:

1. A K-injective \(I\) restricts to a K-injective \(I|_U\), and \(H^q(U,F)=H^q(U,F|_U)\).
2. The sheafification of \(U\mapsto H^q(U,F)\) is \(H^q(F)\).
3. \((Rf_*F)|_V\cong R(f_V)_*(F|_U)\).
4. \(R\Gamma(V,Rf_*F)\cong R\Gamma(f^{-1}V,F)\), with scalar restriction understood.
5. \(H^q(Rf_*F)\) is the sheaf associated to \(V\mapsto H^q(f^{-1}V,F)\).

**Proof.** Extension by zero \(j_!\) is exact and left adjoint to restriction, by Lemma 5.1 of the first lesson. Proposition 5.2 of the K-injective lesson makes its right adjoint, restriction, preserve K-injectives. Thus \(I|_U\) resolves \(F|_U\), and both definitions of the group in (1) use the same section complex \(\Gamma(U,I)\).

For (2), this complex gives the presheaf

\[
U\longmapsto
\frac{\ker\bigl(I^q(U)\to I^{q+1}(U)\bigr)}
{\operatorname{im}\bigl(I^{q-1}(U)\to I^q(U)\bigr)}.
\tag{3.3}
\]

At a point, its filtered colimit is \(H^q(I_x)\), because stalks and filtered colimits are exact. This is \(H^q(F)_x\). The map sending a section cycle to its cohomology germ therefore induces an isomorphism after sheafification, by the first lesson's stalk criterion. This argument works for any complex of sheaves; it does not require exactness of taking sections.

For (3), use the K-injective \(I\) on \(X\) and \(I|_U\) on \(U\). The ordinary sheaf identity \((f_*I)|_V=(f_V)_*(I|_U)\) follows by evaluating on opens of \(V\), so it gives the derived identity. Apply (3.2) to \(f_V\) and use (1) and (3) to obtain (4). Finally \(Rf_*F\) is represented by \(f_*I\); apply the cohomology-presheaf argument to this complex. On an open \(V\), its section cohomology is \(H^q(\Gamma(f^{-1}V,I))=H^q(f^{-1}V,F)\) by (1). Sheafification gives (5). \(\square\)

These assertions distinguish a cohomology sheaf from the cohomology of sections on a specified open. Sections of a quotient sheaf need not be the quotient of sections; sheafification in (2) and (5) is part of the statement.

## 4. Coefficient comparison and exact adjoints

Write \(F_{ab}\) for the underlying complex of abelian sheaves. Forgetting the module action is exact: kernels and images are the same underlying sheaf kernels and images. It therefore induces \(D(\mathcal O_X)\to D(\mathbb Z_X)\), even when \(\mathcal O_X\) has integer torsion.

**Theorem 4.1 (modules and underlying abelian sheaves).** The canonical comparison maps

\[
\begin{gathered}
R\Gamma(U,F)\longrightarrow R\Gamma(U,F_{ab}),\\
(Rf_*F)_{ab}\longrightarrow Rf_*^{ab}(F_{ab})
\end{gathered}
\tag{4.1}
\]

are isomorphisms, respectively in \(D(\mathrm{Ab})\) and \(D(\mathbb Z_Y)\).

**Proof.** Choose \(F\to I\) K-injective over \(\mathcal O_X\), and a K-injective abelian-sheaf resolution \(I_{ab}\to J\). The comparisons are represented by \(\Gamma(U,I)\to\Gamma(U,J)\) and \(f_*I_{ab}\to f_*J\). The choice of \(J\) changes them only by the canonical homotopy comparison between K-injective resolutions, so these are natural derived maps.

Consider the coefficient morphism \(h:(X,\mathcal O_X)\to(X,\mathbb Z_X)\), the identity on spaces and the unit map on rings. Its ordinary pushforward is exactly forgetting the action, so its derived pushforward is also that exact functor. Also \(Lh^*\mathbb Z_X=\mathcal O_X\), because \(\mathbb Z_X[0]\) is K-flat over itself. The adjunction of Theorem 2.2 gives, for every integer \(n\),

\[
\begin{gathered}
\operatorname{Hom}_{D(\mathcal O_X)}(\mathcal O_X,F[n])
\\ \cong\operatorname{Hom}_{D(\mathbb Z_X)}(\mathbb Z_X,F_{ab}[n]).
\end{gathered}
\tag{4.2}
\]

The left group is \(H^n(\Gamma(X,I))\): maps from \(\mathcal O_X\) into \(I[n]\), modulo homotopy, are section cycles modulo section boundaries. The right group is \(H^n(\Gamma(X,J))\). To check that (4.2) is the specified comparison, use Lemma 2.1 for \(h\) and the K-flat source \(\mathbb Z_X\). Its intermediate chain adjunction sends a section of \(I\) to the same underlying section of \(I_{ab}\); localization followed by \(I_{ab}\to J\) gives exactly the cohomology map of \(\Gamma(X,I)\to\Gamma(X,J)\). Hence that map is an isomorphism in every degree. Repeat on \(U\), using Proposition 3.2 to restrict the models, to prove the first line of (4.1).

For the second line, take the section cohomology of \(f_*I_{ab}\to f_*J\) on every open \(V\). It is the first comparison on \(f^{-1}V\), so it is an isomorphism in every degree. Sheafifying these cohomology presheaves, as in Proposition 3.2, proves that the map is a quasi-isomorphism. No preservation of K-injectivity by forgetting coefficients was assumed. \(\square\)

**Proposition 4.2 (open extension and flat pushforward).** For an open inclusion \(j:U\to X\), exact extension by zero is left adjoint to restriction on derived categories. For a flat morphism \(f\), pushforward preserves K-injective complexes.

**Proof.** For \(B\in D(\mathcal O_U)\) and \(F\to I\) K-injective on \(X\), restriction of \(I\) is K-injective. Exactness of \(j_!\) and the chain adjunction give

\[
\begin{aligned}
\operatorname{Hom}_{D(\mathcal O_X)}(j_!B,F)
&=\operatorname{Hom}_{K(\mathcal O_X)}(j_!B,I)\\
&=\operatorname{Hom}_{K(\mathcal O_U)}(B,I|_U)\\
&=\operatorname{Hom}_{D(\mathcal O_U)}(B,F|_U).
\end{aligned}
\]

Naturality is inherited from the chain adjunction and localization, so this is \(j_!\dashv j^*\).

Flatness of \(f\) means that each \(\mathcal O_{X,x}\) is flat over \(\mathcal O_{Y,f(x)}\). The pullback stalk formula then makes \(f^*\) exact. If \(A\) is acyclic on \(Y\), \(f^*A\) is acyclic, and
\(\operatorname{Hom}_K(A,f_*I)=\operatorname{Hom}_K(f^*A,I)=0\).
This is the definition of K-injectivity of \(f_*I\). It applies to every K-injective \(I\), without a termwise-injectivity assumption. \(\square\)

## 5. Point maps and constant coefficients

For \(f:X\to\mathrm{pt}\) with target ring \(A\), pushforward is global sections with its \(A\)-action, so \(Rf_*=R\Gamma(X,-)\) with that action. The pullback is

\[
Lf^*G=\mathcal O_X\otimes_{A_X}^{\mathbf L}G_X,
\tag{5.1}
\]

where \(A_X,G_X\) denote inverse-image constant sheaves. Resolve \(G\) by a K-flat complex over \(A\); its constant inverse image is K-flat, proving (5.1) by one-variable tensor. If \(\mathcal O_X=A_X\) with the identity coefficient map, this is the exact constant sheaf functor, also for noncommutative \(A\) by Corollary 2.3. For the canonical map to \((\mathrm{pt},\Gamma(X,\mathcal O_X))\), the structure sheaf need not be constant, and (5.1) gives the correct pullback.

For a point \(x\), give its one-point source the ring \(\mathcal O_{X,x}\). Pullback is then the exact stalk functor, since the coefficient map at that point is the identity. If the stalk ring is local and we instead give the point its residue field \(\kappa(x)\), the ring map is the quotient, and

\[
Li_x^*F=\kappa(x)\otimes_{\mathcal O_{X,x}}^{\mathbf L}F_x.
\tag{5.2}
\]

Take stalks of a K-flat resolution to prove this formula. A residue field is part of this additional local-ring hypothesis, not data attached to every arbitrary ringed space.

On the analytic curve of the tensor lesson, pull back \(k_a\) to the residue point at \(a\). Its two-term parameter resolution becomes \(\mathbb R\xrightarrow{0}\mathbb R\) in degrees \(-1,0\). Thus the derived pullback has \(\mathbb R\) in both degrees, whereas the ordinary pullback retains only degree zero. With the stalk-ring structure on the point, pullback has only \(k_{a,a}\) in degree zero, because taking a stalk is exact. These are two different morphisms of ringed spaces on the same underlying point inclusion.

## 6. Exercises with checked solutions

**Exercise 1 (easy: an open subspace).** Prove \(H^p(U,F)=H^p(U,F|_U)\), for an arbitrary open \(U\) and an unbounded complex. Explain why restriction of the resolution is admissible.

**Solution.** Resolve \(F\to I\) by a K-injective. For an acyclic \(A\) on \(U\), exactness of \(j_!\) makes \(j_!A\) acyclic, and
\(\operatorname{Hom}_K(A,I|_U)=\operatorname{Hom}_K(j_!A,I)=0\).
Thus \(I|_U\) is K-injective. Both groups are the cohomology of the same complex of sections \(\Gamma(U,I)\). No bound on \(I\), nor on the cohomological dimension of \(U\), was used.

**Exercise 2 (medium: the adjunction without projective models).** Let \(P\to G\) be K-flat and \(F\to I\) K-injective. Prove that a roof \(P\leftarrow Z\to f_*I\) comes from a unique homotopy class \(f^*P\to I\). Deduce the unbounded adjunction and its naturality, without assuming that \(P\) is K-projective or \(f_*I\) K-injective.

**Solution.** Resolve \(Z\) by K-flat \(T\). The denominator \(s:T\to P\) is a quasi-isomorphism between K-flats, so \(f^*s\) is a quasi-isomorphism. Transpose the numerator \(a:T\to f_*I\) to \(f^*T\to I\). Since \(I\) is K-injective, there is a unique homotopy class \(b:f^*P\to I\) whose composite with \(f^*s\) is that numerator. Transposing back makes the roof the localization of a map \(P\to f_*I\).

If two maps \(P\to f_*I\) give the same derived class, cancellation supplies a quasi-isomorphism into \(P\) annihilating their difference. Resolve its source by a K-flat; the same precomposition bijection forces the original difference to be zero in the homotopy category. This proves uniqueness. Maps \(Lf^*G\to F\) are maps \(f^*P\to I\) modulo homotopy, so we obtain (2.3). The constructions commute with chain maps. All source derived morphisms can be expressed as roofs between K-flat models; commuting with their arrows also gives commuting with their inverse denominators. Target morphisms are homotopy classes between K-injective models. This proves bifunctoriality.

**Exercise 3 (medium to hard: Leray and convergence).** For a module sheaf \(M\), prove

\[
\begin{gathered}
E_2^{p,q}=H^p(Y,R^qf_*M)\\
\ \Longrightarrow\ H^{p+q}(X,M),
\\ p,q\ge0,
\end{gathered}
\tag{6.1}
\]

including the construction, differential bidegrees and convergence. This exercise concerns sheaves in degree zero; it imposes no finite dimension on \(X\) or \(Y\).

**Solution.** Choose a bounded-below injective resolution of \(M\), with zero terms below zero. It is K-injective by Lemma 3.2 of the bounded-derived lesson. Put \(K=f_*I\), so \(K\) represents \(Rf_*M\), has no negative terms and has \(H^q(K)=R^qf_*M\).

Let \(A_q=R\Gamma(Y,\tau_{\le q}K)\), with \(A_q=0\) for \(q<0\). Good upper truncations give triangles

\[
\begin{gathered}
A_{q-1}\longrightarrow A_q\\
\longrightarrow R\Gamma(Y,H^qK)[-q]
\\ \longrightarrow A_{q-1}[1].
\end{gathered}
\tag{6.2}
\]

To check the cofiber before applying \(R\Gamma\), the quotient of \(\tau_{\le q}K\) by \(\tau_{\le q-1}K\) has the injection \(\operatorname{im}d^{q-1}\to\ker d^q\) as its two possibly nonzero terms. Its quotient map to \(H^qK[-q]\) is a quasi-isomorphism. The common reading's short-exact-sequence triangle therefore proves (6.2).

Write \(D_q^n=H^n(A_q)\) and \(E_q^n=H^{n-q}(Y,H^qK)\). The long exact sequences give maps

\[
\begin{gathered}
i:D_q^n\longrightarrow D_{q+1}^n,\\
j:D_q^n\longrightarrow E_q^n,\\
k:E_q^n\longrightarrow D_{q-1}^{n+1}.
\end{gathered}
\tag{6.3}
\]

They form an exact couple: \(\ker j=\operatorname{im}i\), \(\ker k=\operatorname{im}j\) and \(\ker i=\operatorname{im}k\), with the adjacent indices understood. This is simply exactness at the three positions of (6.2).

Here is an explicit iteration, including the proof that it gives successive pages. For \(r\ge2\), define

\[
\begin{aligned}
Z_r^{n,q}&=k^{-1}\bigl(\operatorname{im}(i^{r-2})\bigr),\\
B_r^{n,q}&=j\ker(i^{r-2}).
\end{aligned}
\tag{6.4}
\]

In the first line the indicated power maps \(D_{q-r+1}^{n+1}\) into \(D_{q-1}^{n+1}\); in the second it maps \(D_q^n\) into \(D_{q+r-2}^n\). The image of \(j\) lies in every \(Z_r\), since \(kj=0\), so \(B_r\subset Z_r\). Set
\(E_r^{p,q}=Z_r^{p+q,q}/B_r^{p+q,q}\).
For \(r=2\) the power is the identity, so this is precisely \(H^p(Y,H^qK)\).

Given \(e\in Z_r^{n,q}\), choose \(x\in D_{q-r+1}^{n+1}\) with \(i^{r-2}x=k e\), and define \(d_r[e]=[jx]\). Changing \(x\) by an element of the power's kernel changes \(jx\) by \(B_r\). Changing \(e\) by an element of \(B_r\) leaves \(ke\) unchanged, so this is well defined. Its output has total degree \(n+1\) and second index \(q-r+1\); hence its bidegree is \((r,1-r)\). Since \(kj=0\), its square is zero.

To verify the next page, suppose \(d_r[e]=0\). Then \(jx=jy\) for a \(y\) killed by \(i^{r-2}\). Exactness gives \(x-y=iz\), and therefore \(ke=i^{r-1}z\). Thus \(e\in Z_{r+1}\); the converse follows by taking \(x=iz\). A differential image \(jx\) has \(i^{r-1}x=i k e=0\), so it lies in \(B_{r+1}\). Conversely, if \(i^{r-1}x=0\), then \(i^{r-2}x\in\ker i=\operatorname{im}k\). Choose \(e\) with \(ke=i^{r-2}x\); it lies in \(Z_r\), and its differential is \(jx\). Consequently cycles modulo differential images are \(Z_{r+1}/B_{r+1}\), proving \(E_{r+1}=H(E_r,d_r)\). This constructs the spectral sequence directly from the triangles.

It remains to identify its limit. The tail \(\tau_{\ge q+1}K\) is represented in degrees at least \(q+1\). The lower-bound preserving injective resolution of the bounded-derived lesson shows that its \(R\Gamma\) also has no cohomology below \(q+1\). The truncation triangle therefore gives
\(H^n(A_q)\cong H^n(R\Gamma(Y,K))\) whenever \(q\ge n\). Put this stable group \(T^n\), and filter it by

\[
F_qT^n=\operatorname{im}(D_q^n\longrightarrow T^n).
\tag{6.5}
\]

For \(r>q+1\), the source \(D_{q-r+1}^{n+1}\) in (6.4) is zero, so \(Z_r=\ker k=\operatorname{im}j\). For sufficiently large \(r\), the target of the power in the second line is already the stable \(T^n\). Hence

\[
\begin{aligned}
E_\infty^{n-q,q}
&=\operatorname{im}j\big/
j\ker(D_q^n\to T^n)\\
&\cong F_qT^n/F_{q-1}T^n.
\end{aligned}
\tag{6.6}
\]

The last identification follows from \(\ker j=\operatorname{im}(D_{q-1}^n\to D_q^n)\) and the quotient theorem for the map \(D_q^n\to T^n\). The filtration starts with \(F_{-1}=0\) and ends with \(F_n=T^n\). All \(E_2^{p,q}\) with \(p<0\) or \(q<0\) vanish, because sheaf cohomology has no negative degrees and \(K\) has no negative cohomology. Thus each total degree has a finite filtration, and each position has finitely many possible incoming and outgoing differential degrees. This proves convergence. Finally Proposition 3.1 identifies \(T^n=H^n(R\Gamma(Y,Rf_*M))\) with \(H^n(X,M)\), proving (6.1) with the stated scalar action.

**Exercise 4 (hard: the flatness hypothesis for K-injectives).** Prove preservation of K-injectives by a flat pushforward using its defining test. Show that the statement can fail for the one-point map with coefficient map \(\mathbb Z\to\mathbb F_2\).

**Solution.** An acyclic \(A\) pulls back to an acyclic \(f^*A\) when \(f\) is flat. For K-injective \(I\), the chain adjunction gives \(\operatorname{Hom}_K(A,f_*I)=\operatorname{Hom}_K(f^*A,I)=0\). This proves the preservation assertion.

For the indicated nonflat map, \(I=\mathbb F_2[0]\) is K-injective over \(\mathbb F_2\): the field is injective by Baer's criterion, whose only ideal tests are zero and the field itself, and a bounded complex of injectives is K-injective. Its pushforward is the same complex as a \(\mathbb Z\)-module. The complex
\(A=(\mathbb Z\xrightarrow{2}\mathbb Z\to\mathbb F_2)\) in degrees \(0,1,2\) is acyclic. It has a chain map to \(I\), reduction modulo two in degree zero and zero elsewhere. A null homotopy in degree zero would express this nonzero reduction as \(h^1\circ2\), but every homomorphism \(\mathbb Z\to\mathbb F_2\) kills multiples of two. It cannot be null-homotopic, so the pushforward is not K-injective. Nevertheless the general derived adjunction holds by Theorem 2.2.

**Exercise 5 (hard: torsion coefficients and comparison).** Let \(\mathcal O_X\) have arbitrary integer torsion. Prove that \(\Gamma(U,I)\to\Gamma(U,J)\) is a quasi-isomorphism when \(I\) is K-injective over \(\mathcal O_X\) and \(I_{ab}\to J\) is K-injective over \(\mathbb Z_X\). Explain why exactness of forgetting alone does not prove that \(I_{ab}\) is K-injective.

**Solution.** For the coefficient morphism \(h:(U,\mathcal O_U)\to(U,\mathbb Z_U)\), the right derived pushforward is exact forgetting, while \(Lh^*\mathbb Z_U=\mathcal O_U\). Theorem 2.2 identifies maps from \(\mathcal O_U\) into \(I[n]|_U\) with derived maps from \(\mathbb Z_U\) into \(I_{ab}[n]|_U\). Lemma 2.1 identifies these with chain maps into the same underlying \(I_{ab}\); passing to \(J|_U\) computes the latter derived group by a K-injective. On section cycles the comparison sends a cycle to its image in \(J\), and on boundaries it sends boundaries to boundaries. Thus the induced map is precisely \(H^n\Gamma(U,I)\to H^n\Gamma(U,J)\), and is an isomorphism for every \(n\).

An exact functor preserves acyclic complexes in its domain, but K-injectivity tests maps **from every** acyclic complex in the target category. Those tests are not reduced to acyclic module complexes merely by forgetting actions. On a point with structure ring \(\mathbb F_2\), Exercise 4 gives an injective and K-injective module whose underlying abelian complex fails the K-injective test. The coefficient-comparison theorem consequently needs the adjunction argument just supplied.

The next lesson constructs internal derived Hom and its tensor adjunction. Later, the projection-formula and base-change lesson uses the unit, counit and coherent composition isomorphisms proved here to define the comparison maps.

Sources and licensing: the pullback proofs are taken from the Stacks project, tags 06YJ, 0D5S, 079U and 08DE, in its AI Integrated Stacks Project edition (GFDL), checked and edited by GPT-6.1 Sol (OpenAI), at Ultra. The adjunction and composition arguments correspond to tags 079W and 0D5T; their formal derived-adjoint reference was read in full, and its omitted functoriality is supplied by Lemma 2.1 and Theorem 2.2. The open, Leray, higher-image and coefficient proofs are taken from the Stacks project, tags 08BS, 0D5V, 0BKJ, 08FE, 0D5W, 0D5X, 0D5Y, 08BT and 0D5Z, in that edition (GFDL), checked and edited by the same writing AI. For 0D5Y the omitted inverse verification is replaced by the full coefficient adjunction above. Actual passages: [derived pullback](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/cohomology.tex#L6758), [unbounded adjunction](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/cohomology.tex#L7056), [local properties](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/cohomology.tex#L8261), and [deriving adjoints](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/derived.tex#L9838). The exact-couple construction and all its convergence steps are supplied in Exercise 3 rather than cited as a black box. See the combined licence notice and GNU FDL text.
