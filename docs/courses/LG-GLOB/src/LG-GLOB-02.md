# The Satake isomorphism for unramified groups and unramified L-factors

*Draft lesson. Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Public domain (CC0).*

The dual group becomes visible in a concrete algebra. At an unramified place, convolution operators form the spherical Hecke algebra. The Satake transform identifies that algebra with regular functions on a dual torus invariant under its Weyl group. An eigencharacter therefore determines a semisimple conjugacy class in the dual group. Applying a representation of the L-group to that class produces a local Euler factor.

The split proof includes Cartan and Iwasawa decomposition, the algebra property, Weyl invariance, the support bound and its leading coefficient. It applies to every split connected reductive group with the stated reductive integral model, in all residue characteristics. The nonsplit theorem retains its full unramified scope, with the torus case proved and the remaining steps identified in Section 6.

The conventions come from Reductive groups, root data and the L-group. The geometric proofs used here are in Root data, Weyl chambers and the Bruhat decomposition, Sections 5–8, and Automorphisms, forms and parabolic subgroups, Theorems 1.1–2.1. We identify each relevant statement as it is used. Gross's free author manuscript *On the Satake isomorphism* supplies the classical formulation; its Proposition 3.6 is a reference for the theorem, not a replacement for the arguments below.

## 1. Measures and decompositions

Let \(F\) be a nonarchimedean local field, \(\mathcal O\) its valuation ring, \(\varpi\) a uniformizer, and \(q\) the residue-field cardinality. Normalize \(|\varpi|=q^{-1}\). Let \(\mathcal G\) be a split connected reductive group scheme over \(\mathcal O\), \(G=\mathcal G_F\), and \(K=\mathcal G(\mathcal O)\). Choose an integral Borel pair \(B=TN\), with positive roots \(\Phi^+\), Weyl group \(W\), and cocharacter lattice \(Y=X_*(T)\). Put

\[
\rho=\frac12\sum_{\alpha\in\Phi^+}\alpha,\qquad
\delta(t)=\prod_{\alpha\in\Phi^+}|\alpha(t)|.
\]

Write \(t_\lambda=\lambda(\varpi)\). A cocharacter is dominant if \(\langle\alpha,\lambda\rangle\geq0\) for every simple positive root. Then

\[
\delta(t_\lambda)=q^{-2\langle\rho,\lambda\rangle}.
\]

Give \(G(F),T(F),N(F)\) Haar measures for which \(K,T(\mathcal O),N(\mathcal O)\) each have measure one. The two decomposition statements are

\[
G(F)=\coprod_{\lambda\in Y^+}Kt_\lambda K,\qquad
G(F)=B(F)K.
\tag{1.1}
\]

Proposition 1.2 proves Iwasawa decomposition in this generality, and Proposition 1.3 proves existence of a dominant Cartan representative. Lemma 4.1 will prove uniqueness of that representative, completing both assertions of (1.1). Compare [Gross, Proposition 2.6].

The Iwasawa integration formula, in the order \(tnk\), is

\[
\int_G h(g)\,dg
=\int_T\int_N\int_K h(tnk)\,dk\,dn\,dt.
\tag{1.2}
\]

In the order \(ntk\), a factor \(\delta(t)^{-1}\) occurs instead: conjugation \(n\mapsto tnt^{-1}\) multiplies \(dn\) by \(\delta(t)\). Here is a proof of (1.2). Average \(h\) on the right over \(K\). Iwasawa identifies \(G/K\) with \(B/(B\cap K)\). Left Haar measure on \(B\) is \(dt\,dn\) in \(tn\) order: left multiplication translates the \(T\)-coordinate and translates the \(N\)-coordinate by an element depending on \(t\), preserving this product measure. The compact open subgroup \(B\cap K=T(\mathcal O)N(\mathcal O)\) has measure one. Integration on either side is the sum of the same averaged values over the same right cosets.

For completeness, \(G\) is unimodular. A left-invariant top differential form gives Haar measure in smooth local \(F\)-coordinates; right translation multiplies it by \(|\det(\operatorname{Ad}g)|^{-1}\). This determinant character is one on \(T\), where positive and negative root weights cancel, and on every root group, since a character of \(\mathbf G_a\) is trivial. The torus and root groups generate \(G\), as proved by the big cell and Bruhat decomposition in *Root data, Weyl chambers and the Bruhat decomposition*, Sections 5–6. Thus the determinant character is identically one. Ordered root coordinates also make translations in \(N\) triangular with diagonal one, proving its unimodularity; \(T\) is abelian. Inverting the variables, using unimodularity of \(G,T,N\), also gives the order \(knt\) without a modulus factor. Thus the quotient measure on \(G/T\) satisfies

\[
\int_{G/T}H(x)\,dx=\int_K\int_N H(kn)\,dn\,dk
\tag{1.3}
\]

for right \(T\)-invariant integrable functions. These order conventions will control all powers of \(q\) below.

**Proposition 1.1 (the general linear decompositions).** For \(G=GL_n\), \(K=GL_n(\mathcal O)\), and the upper triangular Borel, both assertions of (1.1) hold.

*Proof.* Multiply a matrix \(g\in GL_n(F)\) by a scalar power of \(\varpi\) to make its entries integral. Choose a nonzero entry of smallest valuation. Integral row and column operations move it to the upper left corner and eliminate the other entries in its row and column: every entry is divisible by the chosen pivot. Continue with the remaining block. This produces diagonal elementary divisors, and arranging them in decreasing order gives

\[
g=k_1\operatorname{diag}(\varpi^{a_1},\ldots,\varpi^{a_n})k_2,
\qquad a_1\geq\cdots\geq a_n.
\]

Unit factors are absorbed in \(k_1,k_2\). Uniqueness follows from the ideals generated by the \(r\)-rowed minors: their valuations are \(a_{n-r+1}+\cdots+a_n\), and successive differences recover each \(a_i\).

For Iwasawa, scale the last row of \(g\) so it is a primitive vector in \(\mathcal O^n\). A primitive vector can be completed to an integral basis: one coordinate is a unit, and elementary column operations carry it to the last standard row. Hence some \(k\in K\) makes the last row of \(gk\) equal to \((0,\ldots,0,d)\). The upper-left block is invertible. Induction on its size, using column operations on the first \(n-1\) coordinates, makes it upper triangular. Thus \(gk\in B(F)\), proving \(G=BK\). The case \(n=1\) starts both inductions. \(\square\)


**Proposition 1.2 (Iwasawa for a split integral reductive group).** Under the hypotheses of Section 1, \(G(F)=B(F)K\).

*Proof.* The flag scheme \(X=\mathcal G/\mathcal B\) is smooth and projective over \(\mathcal O\), with an integral big cell \(\mathcal N^-\mathcal B/\mathcal B\simeq\mathcal N^-\). These statements are proved in Automorphisms, forms and parabolic subgroups, Theorem 2.1 and Root data, Weyl chambers and the Bruhat decomposition, Sections 5 and 8; compare [Conrad, Theorems 2.3.6 and 5.1.13].

Every \(F\)-point of \(X\) extends to an \(\mathcal O\)-point. Choose a closed projective embedding and scale its homogeneous \(F\)-coordinates so their minimum valuation is zero. The integral coordinates include a unit. The embedding's homogeneous equations still vanish, since \(\mathcal O\hookrightarrow F\) is injective.

Write \(\kappa\) for the residue field. Bruhat decomposition over \(\kappa\), proved in *Root data, Weyl chambers and the Bruhat decomposition*, Theorem 6.2, shows that every \(\kappa\)-point of \(X_\kappa\) is \(g_0\mathcal B_\kappa\) for \(g_0\in\mathcal G(\kappa)\): each cell has root coordinates defined over \(\kappa\) and an integral Weyl representative.

The point \(g_0\) lifts to \(k_0\in K\). Indeed, formal smoothness lifts it successively from \(\mathcal O/\varpi^a\) to \(\mathcal O/\varpi^{a+1}\), whose kernel is square-zero. The formal smoothness criterion is proved in Projective cohomology and smooth affine models, Section 3. Compatible lifts of the finitely many affine coordinates converge in complete \(\mathcal O\), and the equations vanish in the limit.

For \(x\in X(\mathcal O)\), choose this \(k_0\) matching its reduction. Then \(k_0^{-1}x\) reduces to the identity flag and therefore lies in the integral big cell: the inverse image of its closed complement is a closed subset of the local scheme \(\operatorname{Spec}\mathcal O\) avoiding the closed point, hence is empty. Thus \(k_0^{-1}x=n^-\mathcal B\) with \(n^-\in\mathcal N^-(\mathcal O)\subset K\). This proves \(K\)-transitivity on \(X(\mathcal O)\).

Extend \(g\mathcal B\) from \(F\) to \(\mathcal O\) and apply that transitivity. It gives \(g\in KB(F)\). Inversion proves \(G(F)=B(F)K\). \(\square\)

This proof does not assume Cartan existence.

**Proposition 1.3 (Cartan existence for every split integral reductive group).** Under the hypotheses of Section 1, every \(g\in G(F)\) belongs to \(Kt_\lambda K\) for some dominant \(\lambda\in Y\).

*Proof.* We give the affine-root argument, including its subgroup and multiplication steps. It uses neither Cartan decomposition nor a building. The classical comparison is [Iwahori–Matsumoto, Proposition 2.6, Proposition 2.8, Theorem 2.16 and Corollary 2.17](https://www.numdam.org/article/PMIHES_1965__25__5_0.pdf). The argument below works for the present integral model and every root datum.

**Integral coordinates and the subgroup \(I\).** Choose parameters \(x_\alpha:\mathbf G_a\to\mathcal U_\alpha\) over \(\mathcal O\). Root lines are free over this local ring. Choose the parameters for each opposite pair to be linked by its rank-one homomorphism \(\operatorname{SL}_2\to\mathcal G\). These constructions, with their matrix identities over arbitrary bases, are proved in Roots and reductive groups of rank one, Theorems 4.1, 6.1 and 7.1. Ordered root products in either unipotent radical and the integral big cell are proved in Root data, Weyl chambers and the Bruhat decomposition, equations (5.1)–(5.2). In particular, each ordering of the roots gives coordinates over \(\mathcal O\), including after reduction modulo \(\varpi\).

Let \(I\subset K\) be the inverse image of \(\mathcal B(\kappa)\), where \(\kappa=\mathcal O/\varpi\mathcal O\). The integral big cell gives
\[
I=\mathcal N^-(\varpi\mathcal O)\,T(\mathcal O)\,\mathcal N(\mathcal O).
\tag{1.4}
\]
Here \(\mathcal N^-(\varpi\mathcal O)\) denotes the kernel of reduction on the negative unipotent radical; in any ordered root coordinates all its parameters belong to \(\varpi\mathcal O\). To prove (1.4), an element of \(I\) reduces into \(B_\kappa\), which lies in the big cell. The inverse image of the big cell's closed complement in \(\operatorname{Spec}\mathcal O\) avoids the closed point and is therefore empty. The big-cell inverse then gives integral coordinates, with precisely these reduction conditions. Conversely every displayed product reduces into \(B_\kappa\). Consequently \(I\) is generated by \(T(\mathcal O)\), the groups \(x_\alpha(\mathcal O)\) for \(\alpha>0\), and the groups \(x_\alpha(\varpi\mathcal O)\) for \(\alpha<0\).

**Affine roots and the walls of one alcove.** Work in
\[
V=Y_{\mathbf R}/\{v:\alpha(v)=0\text{ for every root }\alpha\}.
\]
If the root system is empty, \(G=T\), and the valuations in split torus coordinates already give \(T(F)=T(\mathcal O)\{t_\lambda:\lambda\in Y\}\). We may therefore suppose \(V\ne0\). An affine root is the function \(a=\alpha+m\), \(m\in\mathbf Z\), with root subgroup
\[
U_a=x_\alpha(\varpi^m\mathcal O).
\]
The region
\[
C=\{x\in V:0<\gamma(x)<1\text{ for every }\gamma\in\Phi^+\}
\]
is nonempty: take a point of the positive Weyl chamber and scale it toward zero. It is convex and is one component of the complement of the hyperplanes \(\alpha(x)+m=0\). Indeed, throughout this region every affine root has a constant nonzero sign; a component containing one of its points cannot cross either boundary \(\gamma=0\) or \(\gamma=1\). Call these components *alcoves*. The affine roots positive on \(C\) are exactly
\[
\alpha+m\quad
\begin{cases}
m\geq0,&\alpha>0,\\
m\geq1,&\alpha<0.
\end{cases}
\tag{1.5}
\]
Thus their groups lie in \(I\), and together with \(T(\mathcal O)\) generate it.

The finitely many inequalities defining \(C\) show that each of its facets has defining positive affine root \(a=\gamma\) or \(a=-\gamma+1\), for some \(\gamma>0\). Only inequalities actually defining facets are selected; no classification of highest roots is needed. For such a wall, and indeed for any affine root \(a=\alpha+m\), put
\[
r_a(x)=x-a(x)\alpha^\vee,\qquad
n_a=x_\alpha(\varpi^m)x_{-\alpha}(-\varpi^{-m})x_\alpha(\varpi^m)
=\alpha^\vee(\varpi^m)n_\alpha .
\tag{1.6}
\]
The rank-one matrix for \(n_a\) is
\(\left(\begin{smallmatrix}0&\varpi^m\\-\varpi^{-m}&0\end{smallmatrix}\right)\).
It satisfies \(n_a^2=\alpha^\vee(-1)\in T(\mathcal O)\).
The reflection \(r_a\) permutes the affine-root hyperplanes: it sends the affine root \(\beta+l\) to
\[
s_\alpha\beta+l-m\langle\beta,\alpha^\vee\rangle.
\tag{1.7}
\]
The integer pairing makes this another affine root. Conjugation by \(n_a\) gives exactly this action on the groups \(U_b\). To see that parameter choices do not affect the assertion, any integral Weyl representative sends one root line isomorphically to another, multiplying its parameter by a unit of \(\mathcal O\); torus conjugation then gives the indicated valuation shift. The normalizer and its integral representatives are proved in Root data, Weyl chambers and the Bruhat decomposition, Theorem 4.2.

When \(a\) defines a facet of \(C\), the reflected alcove \(r_aC\) is its neighbor across that facet. Choose a point in the relative interior of the facet avoiding all other affine-root hyperplanes. This is possible because the arrangement is locally finite and, for a reduced root system, only \(a\) and \(-a\) have that hyperplane. A sufficiently short crossing changes only their signs. Reflection preserves the arrangement, so it carries \(C\) to that neighboring component. Therefore
\[
r_a(b)>0\quad\text{for every positive affine root }b\ne a.
\tag{1.8}
\]
This elementary sign assertion is the wall property we need.

**The one root coordinate missing from an intersection.** Define \(J_a=I\cap n_a^{-1}In_a\). Every generator \(U_b\) of \(I\), except \(U_a\), lies in \(J_a\) by (1.8), and \(T(\mathcal O)\subset J_a\). Moreover
\[
U_{a+1}\subset J_a:
\quad r_a(a+1)=-a+1>0
\]
for either possible wall root \(\gamma\) or \(1-\gamma\).
If \(a=\gamma\), order the positive root coordinates in (1.4) with \(\gamma\) last. All preceding factors lie in \(J_a\), proving \(I=J_aU_a\). If \(a=-\gamma+1\), order the negative root coordinates with \(-\gamma\) first. This gives \(I=U_aJ_a\), and taking inverses gives \(I=J_aU_a\) again. No commutation of opposite root groups has been assumed.

Choose representatives \(R\subset\mathcal O\) of \(\kappa\), with zero represented by zero and every other representative a unit. Since the root parameter is additive and \(U_{a+1}\subset J_a\), we have
\[
I=\bigcup_{u\in R}J_a\,x_\alpha(\varpi^m u),
\qquad a=\alpha+m.
\tag{1.9}
\]
Equality is sufficient here; disjointness is unnecessary.

**The rank-one multiplication rule.** Let \(N_G(T)(F)\) be the torus normalizer, and let \(n\) be any of its elements. Its conjugation action permutes the groups \(U_b\); write \(w\) for this action on affine roots. We claim
\[
I n_a I n I\ \subset\ I n_a n I\ \cup\ I n I
\tag{1.10}
\]
for each facet root \(a\). Formula (1.9), and \(n_aJ_an_a^{-1}\subset I\), reduce the left side to terms \(I n_a x_\alpha(\varpi^m u)nI\).

If \(w^{-1}a>0\), then \(n^{-1}U_an\subset I\), and every term lies in \(I n_a n I\). If \(w^{-1}a<0\), the term \(u=0\) still lies there. For each nonzero residue representative, \(u\in\mathcal O^\times\). Direct multiplication of the rank-one matrices gives
\[
n_a x_\alpha(\varpi^m u)
=x_\alpha(-\varpi^m u^{-1})\,
\alpha^\vee(-u^{-1})\,
x_{-\alpha}(\varpi^{-m}u^{-1}).
\tag{1.11}
\]
The first two factors lie in \(I\). The last belongs to \(U_{-a}\), and \(w^{-1}(-a)>0\), so it is absorbed into the right \(I\) after multiplication by \(n\). These terms lie in \(InI\), proving (1.10). Identity (1.11) is an identity in \(\operatorname{SL}_2(F)\) before applying its homomorphism to \(G(F)\); it uses no characteristic restriction.

**All normalizer classes are generated by these reflections and alcove stabilizers.** Split torus coordinates give \(T(F)/T(\mathcal O)=Y\). Integral Weyl representatives give
\[
\widetilde W=N_G(T)(F)/T(\mathcal O)\simeq Y\rtimes W.
\tag{1.12}
\]
Indeed any normalizer element is \(tn_w\), and products of integral representatives differ from the chosen representative by \(T(\mathcal O)\). This proves the claimed quotient, including its multiplication. A class represented by \(t_\lambda n_w\) acts on \(V\) as \(x\mapsto wx-\lambda\); its action on affine roots is pullback by the inverse. It preserves the arrangement because all root–cocharacter pairings are integers. Formula (1.6) induces the reflection \(r_a\).

Let \(W_C\) be the subgroup generated by the reflections in the facets of \(C\). It acts transitively on alcoves. Here is the gallery proof. Join an interior point of \(C\) to one in any target alcove by a generic segment. In a bounded neighborhood of that segment only finitely many hyperplanes occur. The endpoints can be chosen so the segment avoids their distinct intersections of codimension at least two: each forbidden incidence is a proper condition on the endpoints, and finitely many such conditions cannot contain their open sets of choices. The segment then crosses finitely many walls, one at a time. If its current alcove is \(vC\), reflection across its next wall is \(v r_a v^{-1}\) for some facet of \(C\), and the next alcove is \(v r_aC\). Induction supplies a word in the facet reflections reaching the target.

For \(w\in\widetilde W\), choose \(v\in W_C\) with \(vC=wC\). Then \(\omega=v^{-1}w\) fixes \(C\). Its lift normalizes \(I\): it permutes the positive affine-root groups (1.5) and preserves \(T(\mathcal O)\), which generate \(I\). Thus the normalizer is generated by \(T(\mathcal O)\), the elements \(n_a\) for facets of \(C\), and lifts of the group of classes fixing \(C\). Central cocharacters may act trivially on \(V\); they belong to this last group. Consequently the argument does not require the cocharacter lattice to be the coroot lattice or the derived group to be simply connected.

**Covering \(G(F)\).** Put
\[
D=\bigcup_{n\in N_G(T)(F)}InI.
\]
It contains the identity and is stable under left multiplication by \(I\). Equation (1.10) makes it stable under each facet lift \(n_a\); their inverses give the same assertion because \(n_a^{-1}\) differs from \(n_a\) by \(T(\mathcal O)\). A lift fixing \(C\) normalizes \(I\), so also preserves \(D\) under left multiplication. The preceding normalizer generation therefore makes \(D\) stable under the whole normalizer.

Finally \(I\) and the normalizer generate \(G(F)\). Bruhat decomposition over \(F\), proved in Root data, Weyl chambers and the Bruhat decomposition, Theorem 6.2, expresses every element using \(B(F)\) and finite Weyl representatives. The positive root groups generate \(N(F)\). For a parameter \(z\in F\) in one of them, choose an integer \(h\geq0\) with \(\varpi^{2h}z\in\mathcal O\). Then
\[
t_{h\alpha^\vee}x_\alpha(z)t_{h\alpha^\vee}^{-1}
=x_\alpha(\varpi^{2h}z)\in I.
\]
Thus these root elements belong to the subgroup generated by \(I\) and the normalizer; \(T(F)\) already belongs to the normalizer. This proves the generation assertion. Stability and \(1\in D\) now give \(G(F)=D\).

Writing each normalizer element as \(t_\lambda n_w\), with \(n_w\in K\), yields
\[
G(F)=\bigcup_{\lambda\in Y}Kt_\lambda K.
\tag{1.13}
\]
Every finite Weyl orbit on \(Y_{\mathbf R}\) meets the closed dominant chamber. For clarity, choose a \(W\)-invariant positive inner product by averaging one over the finite group, and an interior positive-chamber vector \(h\) in the root directions. Maximize \((w\lambda,h)\) over this finite orbit. If some simple root is negative on the maximizer \(\mu\), then
\[
(s_\alpha\mu-\mu,h)
=-\alpha(\mu)(\alpha^\vee,h)>0,
\]
contradicting maximality. The final strict inequality follows because, for the invariant inner product, \(\alpha^\vee\) is a positive multiple of the vector representing \(\alpha\): the reflection formula identifies its perpendicular direction and \(\alpha(\alpha^\vee)=2\) fixes its sign. Hence the maximizing cocharacter is dominant. Integral Weyl representatives conjugate \(t_\lambda\) to \(t_{w\lambda}\) inside \(K\), proving the proposition. Lemma 4.1 below will prove uniqueness of this dominant index. \(\square\)

## 2. The normalized transform is an algebra map

Let

\[
\mathcal H(G,K)=C_c(K\backslash G(F)/K,\mathbf C),\qquad
(f*h)(g)=\int_G f(x)h(x^{-1}g)\,dx.
\]

Its identity is \(1_K\). Proposition 1.3 and the uniqueness proved in Lemma 4.1 give the vector-space basis \(c_\lambda=1_{Kt_\lambda K}\), indexed by dominant cocharacters. The algebra-map argument below does not require that basis. Since \(T(F)/T(\mathcal O)=Y\), the torus Hecke algebra is the group algebra \(\mathbf C[Y]\). Denote its basis element at \(\lambda\) by \(e^\lambda\).

Define

\[
Sf(t)=\delta(t)^{1/2}\int_N f(tn)\,dn,\qquad
Sf=\sum_{\lambda\in Y}Sf(t_\lambda)e^\lambda.
\tag{2.1}
\]

The result is constant on \(T(\mathcal O)\)-cosets. It has finite support: the projection \(B(F)\to T(F)\) maps the compact set \(B(F)\cap\operatorname{supp}(f)\) to a compact subset of \(T(F)\). Each integral is finite because, for fixed \(t\), the map \(n\mapsto tn\) is a closed embedding.

For an unramified character \(\chi:T(F)\to\mathbf C^\times\), let \(I(\chi)\) be normalized induction, realized as smooth functions with

\[
v(tng)=\delta(t)^{1/2}\chi(t)v(g).
\tag{2.2}
\]

The group acts by right translation. Iwasawa gives a unique \(K\)-fixed vector \(\phi_\chi\) with \(\phi_\chi(1)=1\). In fact any \(K\)-fixed function is determined by its value at one; (2.2) is consistent on \(B\cap K\), where both characters are trivial.

For \(f\in\mathcal H(G,K)\), integration (1.2) yields

\[
I(\chi)(f)\phi_\chi
=\left(\sum_{\lambda\in Y}Sf(t_\lambda)\chi(t_\lambda)\right)\phi_\chi.
\tag{2.3}
\]

The product of these operators is \(I(\chi)(f*h)\). Therefore evaluation at every point \(\chi\in\operatorname{Hom}(Y,\mathbf C^\times)\) gives

\[
S(f*h)(\chi)=Sf(\chi)\,Sh(\chi).
\]

A Laurent polynomial vanishing at all points of \((\mathbf C^\times)^r\) is zero: multiply by a monomial and successively regard it as a polynomial in one variable. Consequently \(S(f*h)=Sf\,Sh\). Also \(S1_K=e^0\). This proves the algebra property directly.

The injectivity proved in Section 4 will imply commutativity: the transform then embeds this algebra into the commutative Laurent-polynomial algebra.

There is also an anti-involution proof of commutativity. Choose linked simple-root parameters. The lattice automorphism \(-1\) carries the based root datum for \(B\) to that for \(B^-\). The integral pinned classification in Pinnings and the classification of split reductive groups, Theorem 5.1 gives an integral automorphism \(\theta\) acting on \(T\) by inversion and satisfying
\[
\theta(x_\alpha(u))=x_{-\alpha}(-u),\qquad
\theta(x_{-\alpha}(u))=x_\alpha(-u)
\]
for each simple root. The second identity follows from the linked rank-one \(\operatorname{SL}_2\) map, on which the operation is inverse transpose. Applying it twice fixes the torus and the pinned simple-root groups. Uniqueness in the same classification theorem gives \(\theta^2=1\). Thus \(\iota(g)=\theta(g^{-1})\) is an anti-involution preserving \(K\) and fixing \(T\) pointwise; for \(GL_n\) it is transpose. Cartan makes it fix every double coset. It preserves normalized Haar measure, and changing convolution variables gives \((f*h)^\iota=h^\iota*f^\iota\). Every spherical function is fixed by \(\iota\), so \(f*h=h*f\). This is Gelfand's argument as formulated in [Gross, Proposition 2.10]; see also [Conrad, Theorem 6.1.17]. The later injectivity proof gives the same conclusion independently.

## 3. Weyl invariance from an orbital integral

The orbital-integral argument also appears in [Casselman, Proposition 9.6]; its support conclusion is compared with [Casselman, Proposition 10.2 and Lemma 10.3] in Section 4.

**Proposition 3.1.** For every \(f\in\mathcal H(G,K)\), \(Sf\in\mathbf C[Y]^W\).

*Proof.* First take \(t\in T(F)\) with \(\alpha(t)\ne1\) for every root. Define the integral on the torus quotient

\[
O_t(f)=\int_{G/T}f(xtx^{-1})\,dx.
\]

This is well-defined because \(T\) centralizes \(t\). We use \(G/T\) even when the full centralizer has additional components; no connected-centralizer assertion is needed.

Formula (1.3) and \(K\)-bi-invariance give

\[
O_t(f)=\int_N f(ntn^{-1})\,dn.
\tag{3.1}
\]

Ordered root coordinates and the height-raising commutator formula are proved in Root data, Weyl chambers and the Bruhat decomposition, Section 5, (5.1)–(5.3); compare [Conrad, Theorem 5.1.13 and Proposition 5.1.14]. Order those coordinates by increasing height. The map

\[
N\longrightarrow N,\qquad n\longmapsto u=t^{-1}ntn^{-1}
\]

is triangular in these coordinates: its coordinate for \(\alpha\) is
\((\alpha(t)^{-1}-1)x_\alpha\) plus a polynomial in coordinates of smaller height. All these diagonal factors are nonzero, so successive substitution gives a polynomial inverse. Its absolute Jacobian is the constant

\[
j(t)=\prod_{\alpha>0}|\alpha(t)^{-1}-1|
=\delta(t)^{-1}\prod_{\alpha>0}|1-\alpha(t)|.
\tag{3.2}
\]

Since \(ntn^{-1}=tu\), equations (2.1), (3.1), and (3.2) show

\[
Sf(t)=|D(t)|^{1/2}O_t(f),\qquad
D(t)=\prod_{\alpha\in\Phi}(1-\alpha(t)).
\tag{3.3}
\]

Indeed the product of the negative-root factors contributes \(\delta(t)^{-1}\) to the absolute value, so
\(|D(t)|^{1/2}=\delta(t)^{-1/2}\prod_{\alpha>0}|1-\alpha(t)|\).
The integrals converge: the change of variables reduces (3.1) to the integral of a compactly supported function on \(N\).

A representative of \(w\in W\) lies in \(K\): products of the integral rank-one elements \(x_\alpha(1)x_{-\alpha}(-1)x_\alpha(1)\) give such representatives, as proved in Pinnings and the classification of split reductive groups, Proposition 1.1. Conjugating \(t\) by it preserves \(O_t(f)\) and permutes the factors in \(D(t)\). Haar measure on \(T\) is preserved, since the representative preserves \(T(\mathcal O)\); hence its induced quotient measure is preserved as well. Thus \(Sf(wt)=Sf(t)\) for regular \(t\).

Every coset \(t_\lambda T(\mathcal O)\) contains a regular element. Identify \(T(\mathcal O)=(\mathcal O^\times)^r\). The product of the finitely many excluded Laurent polynomials \(\alpha(t_\lambda t_0)-1\) is nonzero. Such a polynomial cannot vanish on all of \((\mathcal O^\times)^r\): multiply by a monomial and induct on \(r\), using the fact that a nonzero one-variable polynomial has only finitely many roots whereas \(\mathcal O^\times\) is infinite. Thus some \(t_0\) avoids every excluded equation. Since \(Sf\) is constant on torus cosets, equality at these representatives proves \(Sf(t_{w\lambda})=Sf(t_\lambda)\) for every \(\lambda\). \(\square\)

This also explains the normalization: the square root of the modulus produces the symmetric discriminant in (3.3). Without it, the residual factor \(\delta(t)^{1/2}\) depends on the choice of positive chamber.

## 4. The support bound and its leading coefficient

We give the group-theoretic step behind triangularity. Define the rational dominance order on \(Y\) by

\[
\mu\preceq\lambda
\quad\Longleftrightarrow\quad
\lambda-\mu\in\sum_{\alpha\in\Delta}\mathbf R_{\geq0}\alpha^\vee.
\tag{4.1}
\]

This is a partial order; the coefficients are rational for lattice points. It is an enlargement of the integral dominance order, and is sufficient for the finite triangular induction. No assertion about equality of the two orders is needed.

We construct the integral representations needed for the support bound. Flag projectivity and the ample equivariant anticanonical bundle are proved in Roots and reductive groups of rank one, Lemma 5.1 and Automorphisms, forms and parabolic subgroups, Theorems 1.1–2.1; compare [Conrad, Theorem 2.3.6 and Remark 2.3.7]. The integral big-cell and Bruhat proofs are in *Root data, Weyl chambers and the Bruhat decomposition*, Sections 5–8.

Let \(\mathcal P^-\) be an opposite standard parabolic, with Levi positive roots \(\Phi_L^+\), and put
\[
\eta=\sum_{\alpha\in\Phi^+\setminus\Phi_L^+}\alpha,\qquad
X=\mathcal G/\mathcal P^-,\qquad \mathcal L=\omega_{X/\mathcal O}^{-1}.
\]
The tangent weights at the identity flag are the positive roots outside the Levi, so its fibre in \(\mathcal L\) has weight \(\eta\). Choose \(m\) so large that \(\mathcal L^m\) is very ample, globally generated, and has no positive cohomology. The requisite embedding and finiteness assertions are proved in Algebra and sheaf cohomology before reductive groups, Lemma 8.3 and Theorem 8.5.

We also need sections to commute with reduction. The finite projective complex in Projective cohomology and smooth affine models, Lemma 5.1 computes these sections after every base change. Since its positive cohomology vanishes, its exact tail splits successively starting at its last finite projective term. Its remaining degree-zero term is finite projective and computes \(H^0\) after every tensor product. Thus \(E=H^0(X,\mathcal L^m)\) is finite free over \(\mathcal O\), and its geometric fibres are the complete section modules. Equivariance gives its \(\mathcal G\)-action: the flat base-change proof in *Algebra and sheaf cohomology before reductive groups*, Section 6, identifies the translated sections over the affine flat group with \(E\otimes\mathcal O[\mathcal G]\); the line bundle's equivariance identity gives the coaction identity.

Set \(V_\eta=E^\vee\). The complete section system contains a very ample system and therefore gives a closed equivariant embedding
\[
X\longrightarrow\mathbf P(V_\eta),\qquad
1\mathcal P^-\longmapsto[v_-].
\tag{4.2}
\]
Here projective space parametrizes lines, equivalently one-dimensional quotients of \(E\). The vector \(v_-\) is the dual of evaluation at the identity flag. Global generation makes that evaluation surjective; hence \(v_-\) is primitive and has weight \(-m\eta\).

We prove the weight bound directly. On the generic fibre, translation trivializes \(\mathcal L^m\) on the opposite-parabolic big cell, whose coordinates are the positive roots outside the Levi. A section restricts to a polynomial \(f\) there; restriction is injective because the cell is dense and the flag variety is integral. In this trivialization,
\[
(t\cdot f)(n)=(m\eta)(t)\,f(t^{-1}nt).
\]
The function coordinate for a positive root \(\alpha\) has weight \(-\alpha\). Therefore every section weight is \(m\eta-\sum_{\alpha>0}a_\alpha\alpha\), with \(a_\alpha\geq0\). Only constants have weight \(m\eta\), so its multiplicity is at most one; evaluation shows it is one. Dualizing gives
\[
\beta+m\eta\in\sum_{\alpha>0}\mathbf Z_{\geq0}\alpha
\]
for every weight \(\beta\) of \(V_\eta\), with a one-dimensional lowest space of weight \(-m\eta\). The same polynomial proof works on each geometric fibre, by the section base change just proved. The integral split torus grading makes its weight summands direct summands, so these bounds and the rank-one lowest summand hold over \(\mathcal O\) too.

Normalize the lowest coordinate to take value one on \(v_-\). Root groups can only raise weights: expand \(x_\alpha(u)v\) as a polynomial in \(u\), and compare \(t x_\alpha(u)t^{-1}=x_\alpha(\alpha(t)u)\). Its coefficient of \(u^j\) has weight \(\operatorname{wt}(v)+j\alpha\). This is an integral character identity, valid also in positive residue characteristic. Consequently the lowest coordinate of \(nv_-\) remains one.

For a maximal parabolic omitting a simple root \(\alpha_i\), its \(\eta_i\) is a positive integral multiple of the corresponding fundamental weight \(\omega_i\). Indeed Levi reflections permute the positive roots outside the Levi, so \(\eta_i\) pairs to zero with every other simple coroot. Its pairing with \(\alpha_i^\vee\) is
\(2-\langle2\rho_L,\alpha_i^\vee\rangle>0\), since the Cartan entries from the other simple roots to \(\alpha_i^\vee\) are nonpositive.

For the full flag scheme, \(\eta=2\rho\) is strictly dominant. In this case the nonvanishing locus of the lowest coordinate in (4.2) is exactly the big cell \(\mathcal N\mathcal B^-/\mathcal B^-\). Here is a check over every geometric fibre. Bruhat writes a flag as \(nw\mathcal B^-\). The vector \(wv_-\) has weight \(-mw\eta\); applying \(n\) only raises weights. If \(w\ne1\), strict dominance makes \(\eta-w\eta\) a nonzero sum of positive roots, so its lowest coordinate is zero. If \(w=1\), that coordinate is one. Thus the coordinate open set and the big cell have identical points on all geometric fibres, and are the same open subscheme. The integral big-cell isomorphism is proved in *Root data, Weyl chambers and the Bruhat decomposition*, Section 5 and Theorem 8.1; compare [Conrad, Theorem 5.1.13].

**Lemma 4.1.** Let \(\lambda,\mu\) be dominant.

1. If \(nt_\mu\in Kt_\lambda K\) for some \(n\in N(F)\), then \(\mu\preceq\lambda\).
2. \(nt_\lambda\in Kt_\lambda K\) if and only if \(n\in N(\mathcal O)\).

*Proof.* For each maximal parabolic representation just constructed, write \(L_\eta=V_\eta(\mathcal O)\). Since \(\lambda\) is dominant, the weight inequalities give

\[
t_\lambda L_\eta\subset
\varpi^{-\langle m\eta,\lambda\rangle}L_\eta.
\tag{4.3}
\]

Elements of \(K\) preserve \(L_\eta\). Thus every \(g\in Kt_\lambda K\) satisfies the same inclusion. If \(g=nt_\mu\), its value on \(v_-\) has lowest-weight coordinate
\(\varpi^{-\langle m\eta,\mu\rangle}\), because a positive unipotent element leaves that coordinate unchanged. It follows that

\[
\langle\eta,\mu\rangle\leq\langle\eta,\lambda\rangle.
\tag{4.4}
\]

The \(\eta_i\) give every fundamental-weight inequality. An algebraic character \(\zeta\) of \(G\) is trivial on \(N\), and \(\zeta(K)\subset\mathcal O^\times\), so \(nt_\mu\in Kt_\lambda K\) also implies \(\langle\zeta,\mu\rangle=\langle\zeta,\lambda\rangle\). Such characters span the central directions over \(\mathbf R\). Indeed the construction of the derived subgroup and the integral torus quotient in Pinnings and the classification of split reductive groups, Section 10, “The derived group” proves that \(G/G^{\mathrm{der}}\) is a torus, with character lattice the annihilator of the coroot lattice in \(X^*(T)\). Its pullback characters extend to the integral model. This annihilator spans the entire central dual subspace by elementary linear algebra, so their equalities fix the central component of \(\lambda-\mu\). In the remaining simple-coroot space, the fundamental weights are the dual basis. Their inequalities say precisely that every simple-coroot coefficient of \(\lambda-\mu\) is nonnegative. This proves (4.1).

For the second assertion use the full flag representation and put \(\mu=\lambda\). Equation (4.3) applied to \(v_-\), and \(t_\lambda v_-=\varpi^{-\langle m\eta,\lambda\rangle}v_-\), give \(nv_-\in L_\eta\). Its lowest-weight coordinate is one, so it is primitive and defines an \(\mathcal O\)-point of projective space. Its generic point lies in the closed flag embedding (4.2), so the whole \(\mathcal O\)-point does: the homogeneous equations vanish over \(F\) and hence over \(\mathcal O\). Its lowest coordinate is a unit; therefore it lies in the big cell over \(\mathcal O\). The big-cell isomorphism identifies it with an element of \(N(\mathcal O)\). Over \(F\) that element is \(n\), giving the required integrality. Conversely \(n\in N(\mathcal O)\subset K\) plainly implies \(nt_\lambda\in Kt_\lambda K\). For a torus, \(N=1\) and only the character equalities are needed. \(\square\)

Cartan uniqueness now follows without its existence theorem. If \(Kt_\lambda K=Kt_\mu K\) for dominant \(\lambda,\mu\), apply Lemma 4.1 with \(n=1\) in both directions. It gives \(\mu\preceq\lambda\) and \(\lambda\preceq\mu\), hence \(\lambda=\mu\). Together with the existence proof in Proposition 1.3, this completes Cartan decomposition (1.1).

For any fixed dominant \(\lambda\), the set of dominant \(\mu\preceq\lambda\) is finite. To verify this, write
\(\lambda-\mu=\sum c_\alpha\alpha^\vee\), \(c_\alpha\geq0\), and pair with \(2\rho\). A dominant \(\mu\) has \(\langle2\rho,\mu\rangle\geq0\), while
\(\langle2\rho,\alpha^\vee\rangle=2\) for simple roots: the simple reflection permutes all positive roots except \(\alpha\), so it sends \(2\rho\) to \(2\rho-2\alpha\), which gives that pairing by the reflection formula. Thus
\(\sum c_\alpha\leq\langle\rho,\lambda\rangle\).
The central component of \(\mu\) is fixed. These conditions put \(\mu\) in a bounded subset of the finite-dimensional cocharacter space, which meets its lattice in finitely many points.

For a dominant \(\lambda\), let
\(m_\lambda=\sum_{\nu\in W\lambda}e^\nu\), with each distinct orbit element counted once.
Each Weyl orbit has a unique dominant representative, including points on chamber walls. The combinatorial proof is The centre of the enveloping algebra and Harish-Chandra's theorem, Lemma 9.1, applied to the dual root system; it uses the finite reflection group and the positive-root cone, and leaves central directions fixed. Invariance is precisely constancy of coefficients on each finite orbit. These orbit sums therefore form a basis of \(\mathbf C[Y]^W\).

**Proposition 4.2 (triangularity).** One has

\[
Sc_\lambda
=q^{\langle\rho,\lambda\rangle}m_\lambda
+\sum_{\substack{\mu\in Y^+\\\mu\prec\lambda}}
b_{\lambda\mu}m_\mu,
\tag{4.5}
\]

where only finitely many terms occur.

*Proof.* Weyl invariance permits us to test support only at dominant \(\mu\). If \(c_\lambda(t_\mu n)\ne0\), then
\(t_\mu n=(t_\mu nt_\mu^{-1})t_\mu\), and Lemma 4.1 gives \(\mu\preceq\lambda\).
For \(\mu=\lambda\), the same lemma says the integration domain is exactly
\(t_\lambda^{-1}N(\mathcal O)t_\lambda\).
Its measure is \(\delta(t_\lambda)^{-1}\). Multiplying by the normalization \(\delta(t_\lambda)^{1/2}\) gives

\[
Sc_\lambda(t_\lambda)=\delta(t_\lambda)^{-1/2}
=q^{\langle\rho,\lambda\rangle}.
\]

The remaining support is strictly lower, and the previously proved finiteness gives (4.5). \(\square\)

**Theorem 4.3 (Satake, 1963; split case; [Gross, Proposition 3.6]).** The normalized transform is an algebra isomorphism

\[
S:\mathcal H(G,K)\overset{\sim}{\longrightarrow}\mathbf C[Y]^W.
\]

*Proof.* Proposition 1.3 and Lemma 4.1 supply Cartan decomposition for every split connected reductive group with the stated integral model. The algebra property and Weyl invariance were proved in Sections 2–3. Suppose a finite linear combination \(\sum a_\lambda c_\lambda\) is nonzero. Choose a maximal \(\lambda\) among its nonzero indices in the partial order. Formula (4.5) shows the coefficient of \(m_\lambda\) in its transform is
\(a_\lambda q^{\langle\rho,\lambda\rangle}\ne0\).
An incomparable index contributes nothing to \(m_\lambda\); an index capable of contributing would be above \(\lambda\), contradicting maximality. Hence \(S\) is injective.

For surjectivity, induct on the finite lower set of a dominant \(\lambda\). If the orbit sums for all \(\mu\prec\lambda\) are in the image, subtract their contributions from \(Sc_\lambda\) and divide by its nonzero leading coefficient to obtain \(m_\lambda\). Minimal indices start the induction. More formally, repeatedly lowering an index remains inside its finite lower set and therefore terminates. All orbit sums, and hence all invariants, are obtained. \(\square\)

The usual integral dominance refinement restricts the possible lower coefficients further, but the proof above establishes the full complex-algebra isomorphism without that refinement. Explicit lower-coefficient formulas are not needed for this isomorphism.

## 5. From Hecke characters to representations

**Lemma 5.0 (finite torus quotients).** Let a finite group \(\Gamma\) act on \(R=\mathbf C[z_1^{\pm1},\ldots,z_r^{\pm1}]\). Then \(R^\Gamma\) is finitely generated, its simple modules are one-dimensional, and its complex characters are exactly the \(\Gamma\)-orbits of torus points.

*Proof.* For each Laurent generator \(a_i=z_j,z_j^{-1}\), take the monic polynomial \(\prod_{\gamma\in\Gamma}(X-\gamma a_i)\). Let \(A_0\subset R^\Gamma\) be generated by their finitely many coefficients. Each \(a_i\) is integral over \(A_0\), so products with bounded exponents in the \(a_i\) span \(R\) as an \(A_0\)-module.

We include the finiteness argument. A polynomial ring over a Noetherian ring is Noetherian: the leading coefficients of polynomials in an ideal generate an ideal of the coefficient ring. Choose finitely many polynomials realizing its generators and let \(d\) be their maximum degree. Their multiples remove the leading term of any element of degree at least \(d\). The ideal's elements of degree less than \(d\) form a submodule of the finite free coefficient module of polynomials of degree less than \(d\), hence have finitely many module generators. Those generators and the first polynomials generate the ideal by induction on degree. Submodules of finite modules over a Noetherian ring are finite: for a free module, project to its last coordinate and induct on the rank; the image is an ideal, and the kernel has smaller rank. A quotient of a finite free module gives the general case. Starting with \(\mathbf C\) proves the polynomial-ring assertion by induction, and quotients preserve it. Thus \(A_0\) is Noetherian. Its submodule \(R^\Gamma\subset R\) is finite, so the invariant algebra is finitely generated over \(\mathbf C\).

Here is the needed residue-field argument. A field \(L\) finitely generated as a \(\mathbf C\)-algebra equals \(\mathbf C\). Choose a maximal algebraically independent subset \(u_1,\ldots,u_d\) of its generators. The others are algebraic over \(\mathbf C(u_1,\ldots,u_d)\); after inverting one nonzero polynomial \(a\), they are integral over \(A=\mathbf C[u_1,\ldots,u_d,a^{-1}]\). They generate a finite \(A\)-module equal to \(L\). Integrality of the field \(L\) over \(A\) forces \(A\) to be a field: a monic equation for \(b^{-1}\in L\), multiplied by \(b^{n-1}\), expresses \(b^{-1}\) in \(A\) for every nonzero \(b\in A\). If \(d>0\), choose \(c\in\mathbf C\) for which \(u_1-c\) does not divide \(a\); only finitely many \(c\) are excluded. This is a nonunit of \(A\), a contradiction. Therefore \(d=0\), and algebraic closedness gives \(L=\mathbf C\). A simple module over a finitely generated commutative complex algebra is its residue field at a maximal ideal, so is one-dimensional.

For a character \(\xi:R^\Gamma\to\mathbf C\), let \(\mathfrak m=\ker\xi\). The ideal \(\mathfrak mR\) is proper: averaging a hypothetical equation \(1=\sum a_i r_i\), \(a_i\in\mathfrak m\), would give \(1=\sum a_i\operatorname{Av}(r_i)\in\mathfrak m\). Take a maximal ideal in the nonzero finitely generated complex algebra \(R/\mathfrak mR\). Its residue field is \(\mathbf C\) by the previous paragraph; it gives a torus point extending \(\xi\).

Finally two disjoint finite orbits can be separated by a Laurent polynomial which is zero on one and one on the other, followed by averaging. To construct that polynomial, the ideals of distinct points are comaximal: some coordinate differs, so the corresponding two linear coordinate polynomials generate one. The two-ideal gluing formula, iterated, prescribes values on every finite set. Thus invariant characters identify exactly the orbits. \(\square\)

**Proposition 5.1 (spherical classification; [Gross, Proposition 6.4]).** Irreducible smooth complex representations of \(G(F)\) having a nonzero \(K\)-fixed vector are classified by characters of \(\mathcal H(G,K)\). Their \(K\)-fixed spaces have dimension one, and these representations are admissible. Theorem 4.3 supplies the required split Satake isomorphism.

*Proof.* Let \(A=C_c^\infty(G(F),\mathbf C)\) be the full convolution algebra and \(e=1_K\); thus \(eAe=\mathcal H(G,K)=H\). Averaging over \(K\) is the operator \(e\) in every smooth representation. It is an exact projection: if an invariant vector in a quotient has a lift, averaging that lift gives an invariant lift.

If \(V\) is irreducible and \(eV\ne0\), then \(eV\) is a simple \(H\)-module. Indeed, for an \(H\)-submodule \(U\subset eV\), the \(G\)-span of \(U\) is either zero or \(V\), and its \(K\)-fixed part is \(U\): each averaged translate is an element of \(eAe\) applied to \(U\). Thus a nonzero \(U\) equals \(eV\).

Lemma 5.0 makes \(H\simeq\mathbf C[Y]^W\) finitely generated and makes every simple \(H\)-module a one-dimensional evaluation module. Hence \(eV=\mathbf C_\xi\) for a character \(\xi\).

Conversely form

\[
X_\xi=Ae\otimes_H\mathbf C_\xi.
\]

The averaging projection on \(Ae\) has image \(eAe=H\) and splits as a right \(H\)-module. It follows that \(eX_\xi=\mathbf C_\xi\). The corresponding vector generates \(X_\xi\). Every proper \(G\)-submodule has zero \(K\)-fixed part, since otherwise it contains that generator. The sum of all proper submodules still has zero fixed part, by averaging each finite sum, and hence is proper. It is the unique maximal submodule. Its quotient \(V_\xi\) is irreducible, with the indicated Hecke character. Any irreducible representation with that character is a quotient of \(X_\xi\), so is this unique quotient.

Finally choose an unramified \(\chi\) extending \(\xi\) under Satake, as justified in the next paragraph. Equation (2.3) maps \(X_\xi\) onto the subrepresentation of \(I(\chi)\) generated by \(\phi_\chi\). Its unique irreducible quotient is \(V_\xi\). The principal series is admissible: restriction to \(K\) is induction from \(B\cap K\); invariants under a sufficiently small compact open subgroup are functions on a finite quotient of \(K\). Exact averaging then shows subquotients are admissible too. \(\square\)

Put \(\widehat T(\mathbf C)=\operatorname{Hom}(Y,\mathbf C^\times)\). Lemma 5.0 gives
\[
\operatorname{Hom}_{\mathbf C\text{-alg}}(\mathbf C[Y]^W,\mathbf C)
=\widehat T(\mathbf C)/W.
\tag{5.1}
\]

We give the remaining conjugacy argument. Every element of a connected complex reductive group lies in a Borel; this is proved in Regular elements and centralizers, Section 1, the normalizer theorem, using the proper Borel quotient. For a semisimple element \(s\), the Zariski closure \(D\) of its cyclic subgroup is diagonalizable: diagonalize \(s\) in a faithful representation, and \(D\) is a closed subgroup of the diagonal torus. In its Borel \(B=T_B\ltimes U_B\), its intersection with \(U_B\) is trivial. Projection to \(T_B\) embeds \(D\) as a diagonalizable subgroup, and its lift is a regular unipotent crossed homomorphism. Tori, maximal tori and their conjugacy, Lemmas 2.A–2.C prove the trivial intersection and the conjugation of this crossed homomorphism into \(T_B\). Those lemmas apply to disconnected diagonalizable groups, so finite-order semisimple elements are included. Maximal-torus conjugacy, proved in Theorem 2.2 of that lesson, puts \(s\) in \(\widehat T\).

If \(s,s'\in\widehat T\) and \(gsg^{-1}=s'\), then \(\widehat T\) and \(g\widehat T g^{-1}\) are maximal tori in \(C_{\widehat G}(s')^0\). They lie in its identity component because they are connected, and remain maximal because a larger torus there would be larger in \(\widehat G\). This is a smooth connected affine complex group: the smoothness assertion for characteristic-zero group schemes, including schematic centralizers, is proved in Supporting group-scheme proofs, Theorem G.3.4. Apply the same maximal-torus conjugacy theorem within this group. Some \(c\) centralizing \(s'\) makes \(cg\) normalize \(\widehat T\). Thus \(s,s'\) are Weyl conjugate; the converse follows from normalizer representatives. This proves that (5.1) is the set of semisimple \(\widehat G\)-conjugacy classes, and establishes the split parametrization after Satake. Compare [Conrad, Sections 1.1–1.2].

**Corollary 5.2 (general linear principal series).** If
\(I(\chi_1,\ldots,\chi_n)\) is normalized unramified induction for \(GL_n(F)\), its unique spherical irreducible subquotient has Satake class

\[
t_\pi=\operatorname{diag}(\chi_1(\varpi),\ldots,\chi_n(\varpi)).
\tag{5.2}
\]

*Proof.* Its spherical vector has Hecke character \(Sf\mapsto Sf(t_\pi)\) by (2.3). Proposition 5.1 identifies the unique irreducible representation with this character. Permuting the inducing characters permutes the diagonal entries, exactly the Weyl equivalence. This includes reducible principal series: the spherical constituent is determined without assuming the whole induction is irreducible. \(\square\)

## 6. Examples and Euler factors

For \(GL_2\), put \(x_i=\chi_i(\varpi)\). The double coset of \(\operatorname{diag}(\varpi,1)\) has right-coset representatives

\[
\begin{pmatrix}\varpi&a\\0&1\end{pmatrix}\quad
(a\in\mathcal O/\varpi\mathcal O),\qquad
\begin{pmatrix}1&0\\0&\varpi\end{pmatrix}.
\]

Evaluation on the spherical vector gives \(q\cdot q^{-1/2}x_1+q^{1/2}x_2\). Therefore

\[
S1_{K\operatorname{diag}(\varpi,1)K}
=q^{1/2}(x_1+x_2),\qquad
S1_{K\varpi I K}=x_1x_2.
\tag{6.1}
\]

For \(SL_2\), Cartan existence follows already from the \(GL_2\) elementary-divisor proof. The exponents sum to zero; if the two integral basis changes have determinants \(u,u^{-1}\), insert the commuting diagonal unit matrix \(\operatorname{diag}(u^{-1},1)\) on one side and its inverse on the other. Both changes then have determinant one. The cocharacter \(z\mapsto\operatorname{diag}(z,z^{-1})\) generates \(Y\), and \(W\) inverts its coordinate \(x\). The parameter belongs to \(PGL_2(\mathbf C)\); its coordinate is the ratio of diagonal entries. The primitive dominant double coset has transform

\[
q(x+x^{-1})+(q-1).
\tag{6.2}
\]

To check the constant, take \(n(u)t_1=
\begin{pmatrix}\varpi&u\varpi^{-1}\\0&\varpi^{-1}\end{pmatrix}\).
At cocharacter zero, \(n(u)\) has Cartan exponent one exactly when \(v(u)=-1\), a set of measure \(q-1\). At cocharacter one, Lemma 4.1 gives leading coefficient \(q\). No other dominant exponent can occur, giving (6.2).

For \(PGL_2\), a rational point is an invertible projective matrix and has a \(GL_2(F)\)-representative. An integral point has a \(GL_2(\mathcal O)\)-representative because a projective line over the local ring \(\mathcal O\) is free, and its determinant is a unit. Hence the \(GL_2\) decompositions descend. The generator is the class of \(\operatorname{diag}(\varpi,1)\). Its dual is \(SL_2(\mathbf C)\), and the parameter is \(\operatorname{diag}(z,z^{-1})\). Equation (6.1) descends to
\(q^{1/2}(z+z^{-1})\).
These two rank-one groups have different cocharacter lattices; the distinction changes both the parameter group and the primitive double coset.

Let \(r:{}^LG\to GL(V)\) be finite dimensional, algebraic on \(\widehat G\), with the chosen unramified local data. For split \(G\) and \(r\) trivial on the Weil factor, define

\[
L(s,\pi,r)=
\det(1-r(t_\pi)q^{-s}\mid V)^{-1}.
\tag{6.3}
\]

More generally use \(r(t_\pi\rtimes\operatorname{Frob})\). We choose the local reciprocity convention sending a uniformizer to the Frobenius used here; all comparisons with Galois representations must keep this convention fixed. Conjugating the parameter changes the matrix by similarity and leaves (6.3) unchanged.

For \(GL_n\) and its standard representation, (5.2) gives
\(L(s,\pi)=\prod_i(1-x_iq^{-s})^{-1}\).
For \(GL_2\), the symmetric-square eigenvalues are \(x_1^2,x_1x_2,x_2^2\); those of the adjoint representation are \(x_1/x_2,1,x_2/x_1\). The trivial representation of \(GL_2(F)\) has normalized parameter
\(\operatorname{diag}(q^{1/2},q^{-1/2})\), so its Hecke eigenvalue in (6.1) is \(q+1\), the number of right cosets. This is a useful check that unramified does not mean tempered. For split \(G\), tempered spherical parameters have a representative in a maximal compact subgroup of \(\widehat G\), equivalently a bounded unramified dual image; that criterion is stated in [Gross, Section 6, immediately after Proposition 6.4]. Its proof is still missing here; it is not used in the algebraic Satake argument. The full complex conjugacy class need not be compact. For example, \(t=\operatorname{diag}(i,-i)\) has finite powers and belongs to \(U(2)\), but conjugating by \(u(x)=\left(\begin{smallmatrix}1&x\\0&1\end{smallmatrix}\right)\) gives \(u(x)tu(x)^{-1}=\left(\begin{smallmatrix}i&-2ix\\0&-i\end{smallmatrix}\right)\), an unbounded family as real \(x\) tends to infinity.

**Theorem 6.1 (Satake, 1963; Langlands's unramified extension).** Let \(G/F\) be connected reductive, quasi-split, and split over a finite unramified extension. Let \(K\) be hyperspecial, and let \(\sigma\) be the pinned action of the chosen Frobenius on the dual group. Characters of \(\mathcal H(G,K)\), and hence irreducible \(K\)-spherical representations, are parametrized by the closed \(\widehat G\)-conjugacy orbits in \(\widehat G\rtimes\operatorname{Frob}\). The action on the first factor is
\[
h\longmapsto gh\sigma(g)^{-1}.
\]

Choose the torus \(T\) in an \(F\)-Borel. Let \(N_F\subset N_{\widehat G}(\widehat T)\) be the inverse image of the rational Weyl group under the dual-root-datum identification. The Satake algebra is
\[
\mathcal H(G,K)\simeq
\mathcal O(\widehat T\rtimes\operatorname{Frob})^{N_F}.
\tag{6.4}
\]

The torus part of \(N_F\) acts by twisted conjugation and cannot be omitted from these invariants. The precise source statement is [Getz–Hahn, free draft of 22 April 2022, Theorem 7.5.1 and Corollary 7.5.2]; its equation (7.23) is the twisted restriction theorem identifying torus and group quotients. For split \(G\), \(\sigma=1\), its algebra assertion is Theorem 4.3 and its semisimple parametrization agrees with (5.1). Formula (6.3) uses \(r(h\rtimes\operatorname{Frob})\) in this generality.

**Proposition 6.2 (the nonsplit torus case).** Theorem 6.1, including (6.4), holds for every unramified torus.

*Proof.* Let \(E/F\) be a finite unramified Galois extension splitting \(T\), with generator \(\sigma\), and let \(Y=X_*(T_E)\). For \(t\in T(F)\), the integers \(v_E(\chi(t))\), for all \(\chi\in X^*(T_E)\), define \(\nu(t)\in Y^\sigma\). Its kernel is \(T(\mathcal O)\): after splitting, all coordinates and their inverses must be integral units, and its split coordinate homomorphism takes values in \(\mathcal O_E\). Galois equivariance then sends invariant coordinate functions to \(\mathcal O_E^{\mathrm{Gal}(E/F)}=\mathcal O\), giving the integral point of the descended torus. Every \(\lambda\in Y^\sigma\) is defined over \(F\), extends over the unramified integral model, and satisfies \(\nu(\lambda(\varpi))=\lambda\). Indeed \(\varpi\) has valuation one in \(E\), and a Galois-invariant lattice homomorphism gives an equivariant map of the split Hopf algebras, hence descends. These torus lattice and descent constructions are proved in Tori, maximal tori and their conjugacy, Section 1.

Thus \(T(F)/T(\mathcal O)=Y^\sigma\), and normalized convolution gives \(\mathcal H(T,T(\mathcal O))=\mathbf C[Y^\sigma]\). There is no unipotent radical or modulus factor. Twisted conjugation on the dual torus is translation by the image of
\[
1-\sigma:\widehat T\longrightarrow\widehat T,\qquad
g\longmapsto g\sigma(g)^{-1}.
\]
That image is a closed subtorus. To check this, diagonalize the integer lattice homomorphism by invertible integral row and column operations. The Euclidean algorithm finds a nonzero entry of smallest positive size; if it fails to divide another entry, taking a remainder produces a smaller pivot. Once it divides all remaining entries, clear its row and column and continue on the smaller block. This terminates and gives Smith normal form. Thus on complex points the nonzero coordinates are \(z\mapsto z^d\), which are surjective, and all remaining image coordinates equal one. The quotient torus has character lattice
\[
\ker(1-\sigma:X^*(\widehat T)\to X^*(\widehat T))=Y^\sigma.
\]
Every orbit is a closed coset of that subtorus, and its quotient ring is \(\mathbf C[Y^\sigma]\). Hence its points are precisely the Hecke characters, by Lemma 5.0 for the trivial group. They give the one-dimensional smooth characters of \(T(F)\) trivial on \(T(\mathcal O)\), and exhaust spherical irreducibles by the compact-induction proof in Proposition 5.1, which only uses the computed commutative Hecke algebra in this case. This proves the theorem for every unramified torus. \(\square\)

For the norm-one torus of an unramified quadratic extension, \(Y=\mathbf Z\) and \(\sigma\) acts by \(-1\), so \(Y^\sigma=0\). Its Hecke algebra is \(\mathbf C\), and its only spherical irreducible is the trivial representation: a norm-one element has valuation zero, so the group is a closed subgroup of the compact unit group of \(E\). On the dual torus, twisted conjugation multiplies \(h\) by \(g^2\). Squaring is surjective on \(\mathbf C^\times\), so the Frobenius coset has one twisted orbit, in agreement with the Hecke calculation.

For \(T=\operatorname{Res}_{E/F}\mathbf G_m\), with \(E/F\) unramified quadratic, \(Y=\mathbf Z^2\) and \(\sigma\) interchanges its basis. The fixed generator is \((1,1)\), and a character with value \(a\) on that generator corresponds to the twisted dual invariant \(h_1h_2=a\). Let the two-dimensional L-group representation have diagonal torus action and let Frobenius interchange the basis vectors. Then
\[
r((h_1,h_2)\rtimes\operatorname{Frob})
=\begin{pmatrix}0&h_1\\h_2&0\end{pmatrix},\qquad
\det(1-Xr)=1-aX^2.
\]
Its Euler factor is \((1-aq^{-2s})^{-1}\). This is the unramified character factor over \(E\), whose residue cardinality is \(q^2\). The Frobenius permutation in the full coset element is essential to this computation.

For a general nonsplit unramified reductive group, two proofs are still required here. First, one must establish Cartan existence and the relative triangularity and Weyl-invariance assertions for the integral quasi-split model; split absolute root coordinates alone do not establish them, especially when the relative root system is nonreduced. Second, one must prove that every closed orbit in the Frobenius coset meets \(\widehat T\rtimes\operatorname{Frob}\), with intersections exactly the \(N_F\)-orbits. This is equation (7.23) of the free Getz–Hahn draft. Proposition 6.2 proves it for a dual torus. The full Theorem 6.1 remains a known theorem whose proof is unfinished here; a free citation does not close either step.

## 7. Exercises and complete solutions

**Exercise 7.1 (easy).** Compute the transform of the double coset of
\(\operatorname{diag}(\varpi,1,\ldots,1)\) in \(GL_n(F)\).

**Exercise 7.2 (intermediate).** Prove Weyl invariance of \(S\), keeping track of the modulus in both orders \(tn\) and \(nt\).

**Exercise 7.3 (intermediate).** Compute \(L(s,\pi,\operatorname{Sym}^2)\) for a spherical representation of \(GL_2(F)\), including the case of equal eigenvalues.

**Exercise 7.4 (advanced).** Prove injectivity of \(S\) from triangularity when a finite set of cocharacters has several incomparable maximal elements.

**Solution 7.1.** Right cosets correspond to sublattices of \(\mathcal O^n\) of index \(q\), equivalently hyperplanes in its residue space. Choose the leftmost nonzero coordinate of a defining linear functional to be position \(j\), and normalize it to one. Its earlier coordinates vanish, and its \(n-j\) later coordinates are arbitrary, giving \(q^{n-j}\) choices. A basis of its kernel has columns \(e_i\) for \(i<j\), \(\varpi e_j\), and \(e_i-a_i e_j\) for \(i>j\). It therefore gives an upper triangular coset representative with diagonal entry \(\varpi\) at \(j\) and all other diagonal entries one. Its spherical-vector value is
\(q^{-(n+1-2j)/2}x_j\), since
\(\langle\rho,e_j\rangle=(n+1-2j)/2\).
Summing all right cosets gives

\[
\sum_{j=1}^n q^{n-j}q^{-(n+1-2j)/2}x_j.
\]

The exponent simplifies independently of \(j\), so the answer is

\[
S1_{K\operatorname{diag}(\varpi,1,\ldots,1)K}
=q^{(n-1)/2}(x_1+\cdots+x_n).
\tag{7.1}
\]

Indeed \(n-j-(n+1-2j)/2=(n-1)/2\). One can also obtain (7.1) without pivot conventions from Proposition 4.2: the dominant cocharacter \((1,0,\ldots,0)\) has no strictly lower dominant integer cocharacter with the same central coordinate, so only its orbit sum occurs, with coefficient \(q^{(n-1)/2}\).

**Solution 7.2.** In \(tn\) order the normalized transform is
\(\delta(t)^{1/2}\int f(tn)\,dn\). Changing to \(nt\) gives
\(\delta(t)^{-1/2}\int f(nt)\,dn\).
For regular \(t\), the map \(n\mapsto t^{-1}ntn^{-1}\) has Jacobian
\(\delta(t)^{-1}\prod_{\alpha>0}|1-\alpha(t)|\), so either expression becomes \(|D(t)|^{1/2}O_t(f)\). Both the discriminant and the orbital integral are unchanged by Weyl conjugation. Finally vary the unit part of \(t\) to obtain a regular representative of every torus coset. This proves invariance at every lattice point, as in Proposition 3.1.

**Solution 7.3.** If the standard eigenvalues are \(\alpha,\beta\), use the basis \(e_1^2,e_1e_2,e_2^2\). The symmetric square acts diagonally with eigenvalues \(\alpha^2,\alpha\beta,\beta^2\). Therefore

\[
L(s,\pi,\operatorname{Sym}^2)
=\frac1{(1-\alpha^2q^{-s})(1-\alpha\beta q^{-s})(1-\beta^2q^{-s})}.
\]

If \(\alpha=\beta\), all three eigenvalues equal \(\alpha^2\), and the factor is \((1-\alpha^2q^{-s})^{-3}\). Multiplicities are retained; one does not replace the determinant by a product over distinct eigenvalues.

**Solution 7.4.** Take any maximal nonzero index \(\lambda\). An index \(\nu\) contributes to \(m_\lambda\) only if \(\lambda\preceq\nu\). Among the nonzero indices this forces \(\nu=\lambda\), since maximality excludes a strictly larger one; incomparable maximal elements contribute zero to this coefficient. The coefficient is therefore the nonzero number \(a_\lambda q^{\langle\rho,\lambda\rangle}\). Choosing any one of the maximal indices is enough to disprove vanishing of the transform.

## Proof dependencies and unfinished arguments

The geometric dependencies have available preceding proofs. Root data, Weyl chambers and the Bruhat decomposition, Sections 5–8, proves ordered integral root coordinates, commutators, the big cell and Bruhat decomposition. Pinnings and the classification of split reductive groups, Proposition 1.1 and Theorem 5.1, supplies integral Weyl representatives and pinned classification. Roots and reductive groups of rank one, Lemma 5.1, and Automorphisms, forms and parabolic subgroups, Theorem 2.1, prove flag projectivity and the ample canonical determinant bundle. These proofs apply to the split integral model over \(\mathcal O\), including positive residue characteristic. Algebra and sheaf cohomology before reductive groups, Sections 6 and 8, and Projective cohomology and smooth affine models, Lemma 5.1, prove the cohomology, ample-embedding and section base-change assertions. Section 4 proves its weight bound from polynomial functions on the big cell; it does not transfer a characteristic-zero Lie-algebra theorem into positive characteristic.

The conjugacy proofs are Tori, maximal tori and their conjugacy, Lemmas 2.A–2.C and Theorem 2.2; the Borel-containment argument in Regular elements and centralizers, Section 1; and characteristic-zero smoothness in Supporting group-scheme proofs, Theorem G.3.4. The finite-invariant-algebra, residue-field and orbit-separation arguments are proved in Lemma 5.0 here.

Proposition 1.3 proves general split Cartan existence from integral root coordinates and rank-one identities: it supplies the affine-wall sign argument, the intersection factorization, the double-coset multiplication rule, normalizer generation and the covering of \(G(F)\). Its root-group and rank-one inputs are the actual proofs in *Roots and reductive groups of rank one*, Theorems 4.1, 6.1 and 7.1; its ordered coordinates, normalizer and field Bruhat inputs are the actual proofs in *Root data, Weyl chambers and the Bruhat decomposition*, Theorem 4.2, equations (5.1)–(5.2), and Theorem 6.2. Proposition 1.2 proves general split Iwasawa, and Lemma 4.1 proves Cartan uniqueness. Together these complete Theorem 4.3 and the split representation parametrization for all split connected reductive groups with the stated reductive integral models.

The nonsplit theorem retains every hypothesis in Theorem 6.1. Its unfinished steps, specified after Proposition 6.2, are the relative group-theoretic Satake proof and twisted conjugacy restriction. The unramified torus case is proved. The temperedness criterion, stated in [Gross, Section 6, immediately after Proposition 6.4], also lacks a proof here. None of the Euler-factor calculations uses it. Explicit lower-coefficient formulas are not asserted or used.

## References

- [Satake] I. Satake, [*Theory of spherical functions on reductive algebraic groups over p-adic fields*](https://www.numdam.org/item/PMIHES_1963__18__5_0/), 1963, freely readable original paper at Numdam.
- [Gross] B. H. Gross, [*On the Satake isomorphism*](https://people.math.harvard.edu/~gross/preprints/sat.pdf), free author manuscript, Sections 2–3 and 6: Proposition 2.6 (Cartan), Proposition 2.10 (commutativity), Proposition 3.6 (split isomorphism), equations (3.7)–(3.9) (triangularity), Proposition 6.4 (spherical classes), and the following paragraph (temperedness).
- [Iwahori–Matsumoto] N. Iwahori and H. Matsumoto, [*On some Bruhat decomposition and the structure of the Hecke rings of p-adic Chevalley groups*](https://www.numdam.org/article/PMIHES_1965__25__5_0.pdf), Publications Mathématiques de l’IHÉS 25 (1965), 5–48, freely readable original paper: Proposition 2.6, Proposition 2.8, Theorem 2.16 and Corollary 2.17. Proposition 1.3 supplies its own proof for the integral model and arbitrary reduced root datum used here.
- [Casselman] W. Casselman, [*A companion to Macdonald's book on p-adic spherical functions*](https://personal.math.ubc.ca/~cass/courses/seminar-06b/macdonald.pdf), free notes, Sections 9–10, especially Propositions 9.6 and 10.2 and Lemma 10.3.
- [Getz–Hahn] J. R. Getz and H. Hahn, [*An Introduction to Automorphic Representations, with a View toward Trace Formulae*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), free author draft of 22 April 2022, Section 7.5: equation (7.23), Theorem 7.5.1 and Corollary 7.5.2. The result numbers cited here belong to that draft.
- [Conrad] B. Conrad, [*Reductive Group Schemes*](https://math.stanford.edu/~conrad/papers/luminysga3smf.pdf), free author text, 2014: Sections 1.1–1.2; Theorems 1.4.12 and 2.3.6; Remark 2.3.7; Corollary 5.1.11; Theorem 5.1.13 and Proposition 5.1.14; Theorem 6.1.17.
