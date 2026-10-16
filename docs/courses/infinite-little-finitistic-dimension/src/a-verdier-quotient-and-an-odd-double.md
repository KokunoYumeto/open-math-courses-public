# A Verdier quotient and an odd double

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The algebra \(B\) of [Directed algebras and quadratic presentations](directed-algebras-and-quadratic-presentations.md) records a presentation of \(R\) with two families of arrows, but the arrows \(s\) and \(s'\) are not invertible in \(B\). This lesson inverts them in a quotient of the homotopy category of \(B\): in the Verdier quotient \(Q\), the generators of \(R\) act on the object \(L=\mathbf e_0B\) (Lemma 2.2), and tensoring with the module \(M(Y)\) recovers \(Y\) with its \(R\)-action (Proposition 3.2). The selection functor of [A selection process with unbounded extinction](a-selection-process-with-unbounded-extinction.md) needs the summand cut out by the idempotent \(e\), and this summand need not exist in \(Q\). The odd double lemma (Lemma 4.3) produces an object of \(Q\) that behaves like the summand plus a copy shifted by three. Section 5 assembles a diagram of shape \(B\) in \(Q\) whose evaluation at every \(Y\) is the selection \(eY\oplus(eY)[3]\). The construction follows [OpenAI-FD, Section 3].

Notation is as in the previous lesson: \(k\) is a field, \(R=k\langle x_1,\dots,x_d\rangle/(p_1,\dots,p_t)\) with relations of degree at most two, \(e\in R\) is a central idempotent, \(\alpha\) is an automorphism of \(R\), and \(B\) is the algebra with vertices \(0,1,2\), arrows \(s,a_h\colon0\to1\), \(s',a'_h\colon1\to2\), and the basis \(\mathcal R\) of its relations.

## 1. The homotopy category of B

Let \(K\) be the homotopy category of bounded complexes of finitely generated projective *right* \(B\)-modules. It is triangulated, with the mapping cone triangles as distinguished triangles (core course [Category Theory and Homological Methods](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D80); [Li, *Methods of Algebra*, Volume 2, Theorem 4.4.1 and Corollaries 4.4.2 and 4.4.4](https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en)). Shifts follow the convention \(T[s]^n=T^{n+s}\), \(d_{T[s]}=(-1)^sd_T\), so a module placed in degree \(0\) and shifted by \(s\) sits in degree \(-s\).

Put \(E_i=\mathbf e_iB\), a projective right module, regarded as a complex in degree \(0\). For an arrow \(a\colon i\to j\), the element \(a\) lies in \(\mathbf e_jB\mathbf e_i\), so left multiplication \(x\mapsto ax\) is a map of right modules \(E_i\to E_j\); we denote it by \(a\) again. For a path \(ba\), the map of \(ba\) is the composite of the maps of \(a\) and \(b\), and a linear combination of paths gives the corresponding combination of maps. In particular each relation \(\rho\in\mathcal R\) gives the zero map \(E_0\to E_2\), since \(\rho=0\) in \(B\).

## 2. Inverting two arrows

A *thick* subcategory of a triangulated category is a full triangulated subcategory closed under isomorphisms and direct summands. Intersections of thick subcategories are thick, so there is a smallest thick subcategory \(\mathcal S\) of \(K\) containing the cones of \(s\colon E_0\to E_1\) and \(s'\colon E_1\to E_2\). Let
\[
\Sigma=\{u\in\operatorname{Mor}K:\operatorname{Cone}(u)\in\mathcal S\}.
\]
**Theorem 2.1** (Verdier localization; core course [Category Theory and Homological Methods](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D80); [Li, Volume 2, Propositions 4.3.2–4.3.3, Theorem 4.3.4, Theorem 1.9.11 and Corollary 1.9.13](https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en)). The class \(\Sigma\) is a multiplicative system compatible with the triangulation. The localization \(Q=K[\Sigma^{-1}]\), written \(K/\mathcal S\), is a triangulated category, and the localization functor \(q\colon K\to Q\) is triangulated; up to isomorphism, the distinguished triangles of \(Q\) are the images of distinguished triangles of \(K\). Every morphism of \(Q\) has the form \(q(f)q(u)^{-1}\) with \(u\in\Sigma\), and \(q(f)=0\) for \(f\colon X\to Y\) if and only if \(fu=0\) for some \(u\colon X'\to X\) in \(\Sigma\). Every triangulated functor \(F\colon K\to\mathcal D\) that sends the objects of \(\mathcal S\) to zero factors uniquely as \(F=\bar F\circ q\) with \(\bar F\) triangulated.

We keep the names of objects and morphisms of \(K\) for their images under \(q\). Since the cones of \(s\) and \(s'\) lie in \(\mathcal S\), the maps \(s\) and \(s'\) belong to \(\Sigma\) and are isomorphisms in \(Q\). Let \(L=E_0\) and
\[
\overline x_h=s^{-1}a_h\in\operatorname{End}_Q(L)\quad(1\le h\le d).
\]
**Lemma 2.2.** There is a unique unital algebra homomorphism \(\theta\colon R\to\operatorname{End}_Q(L)\) with \(\theta(x_h)=\overline x_h\).

**Proof.** Uniqueness holds because the \(x_h\) generate \(R\). The relation \(a'_hs=s'a_h\) of \(B\) gives \(a'_h=s'a_hs^{-1}\) in \(Q\). Hence
\[
\begin{aligned}
(s's)^{-1}a'_ha_l&=s^{-1}a_hs^{-1}a_l=\overline x_h\overline x_l,\\
(s's)^{-1}s'a_h&=s^{-1}a_h=\overline x_h,\\
(s's)^{-1}s's&=\mathrm{id}_L .
\end{aligned}
\]
For each defining relation \(p_j\), the homogenization \(\widetilde p_j\) is obtained from \(p_j\) by the substitutions \(x_hx_l\mapsto a'_ha_l\), \(x_h\mapsto s'a_h\), \(1\mapsto s's\); so \(p_j(\overline x_1,\dots,\overline x_d)=(s's)^{-1}\widetilde p_j\), where \(\widetilde p_j\) denotes the corresponding map \(E_0\to E_2\). This map is zero, since \(\widetilde p_j=0\) in \(B\). The algebra homomorphism from the free algebra sending \(x_h\) to \(\overline x_h\) therefore kills the \(p_j\) and factors through \(R\). \(\square\)

## 3. Evaluation at an R-module

Let \(\mathrm D^b(k)\) be the bounded derived category of finite-dimensional vector spaces. For a finite-dimensional left \(R\)-module \(Y\), tensoring termwise with the module \(M(Y)\) of the previous lesson gives an additive functor from finitely generated projective right \(B\)-modules to finite-dimensional vector spaces, hence a triangulated functor on bounded homotopy categories ([Li, Volume 2, Proposition 4.4.3](https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en)); composing with the passage to the derived category gives the triangulated functor
\[
\operatorname{ev}_Y\colon K\to\mathrm D^b(k),\qquad T\mapsto T\otimes_BM(Y).
\]
The isomorphism \(E_i\otimes_BM(Y)\cong\mathbf e_iM(Y)=Y\), \(x\otimes v\mapsto xv\), identifies the map of an arrow \(a\colon E_i\to E_j\) with the action of \(a\) on \(M(Y)\): \(ax\otimes v\mapsto axv\). So \(\operatorname{ev}_Y(s)\) and \(\operatorname{ev}_Y(s')\) are identity maps of \(Y\), and \(\operatorname{ev}_Y(a_h)=\operatorname{ev}_Y(a'_h)=x_h\).

**Lemma 3.1.** The objects sent to zero by a triangulated functor \(F\) form a thick subcategory.

**Proof.** They are closed under isomorphisms and shifts. If two objects of a distinguished triangle are sent to zero, the image triangle has two zero objects, and its third object is zero: applying the cohomological functor \(\operatorname{Hom}(Z,-)\) ([Li, Volume 2, Proposition 4.1.12](https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en)) with \(Z\) the third object shows \(\operatorname{Hom}(Z,Z)=0\). If \(X\oplus X'\) is sent to zero, then \(F(X)\oplus F(X')\cong0\), so \(F(X)=0\). \(\square\)

**Proposition 3.2.** The functor \(\operatorname{ev}_Y\) factors uniquely through \(q\), as a triangulated functor \(\overline{\operatorname{ev}}_Y\colon Q\to\mathrm D^b(k)\). Under the identification \(\overline{\operatorname{ev}}_Y(L)=Y\), the endomorphism \(\overline{\operatorname{ev}}_Y(\theta(r))\) is the action of \(r\in R\) on \(Y\).

**Proof.** The cone of an identity map is zero, so \(\operatorname{ev}_Y\) sends the cones of \(s\) and \(s'\) to zero. By Lemma 3.1 it sends every object of \(\mathcal S\) to zero, and Theorem 2.1 gives the factorization. On generators, \(\overline{\operatorname{ev}}_Y(\overline x_h)=\operatorname{ev}_Y(s)^{-1}\operatorname{ev}_Y(a_h)=x_h\). Both \(r\mapsto\overline{\operatorname{ev}}_Y(\theta(r))\) and the action of \(R\) on \(Y\) are algebra homomorphisms \(R\to\operatorname{End}_k(Y)\) agreeing on generators, so they coincide. \(\square\)

## 4. Idempotent completion and the odd double

**Definition 4.1.** The *idempotent completion* \(\operatorname{Kar}(\mathcal T)\) of an additive category \(\mathcal T\) has as objects the pairs \((T,p)\) with \(T\in\mathcal T\) and \(p=p^2\in\operatorname{End}(T)\), and as morphisms \((T,p)\to(T',p')\) the morphisms \(u\colon T\to T'\) with \(u=p'up\); composition is that of \(\mathcal T\), and the identity of \((T,p)\) is \(p\). The functor \(T\mapsto(T,\mathrm{id}_T)\) is fully faithful. If \(\mathcal T\) has a shift functor, put \((T,p)[1]=(T[1],p[1])\).

In \(\operatorname{Kar}(\mathcal T)\), the morphisms \(p\colon(T,p)\to(T,\mathrm{id})\), \(p\colon(T,\mathrm{id})\to(T,p)\) and their analogues for \(1-p\) exhibit \(T\cong(T,p)\oplus(T,1-p)\). Every idempotent of \(\operatorname{Kar}(\mathcal T)\) has an image: for an idempotent \(v\) of \((T,p)\), the object \((T,v)\) is a summand of \((T,p)\).

**Lemma 4.2.** Let \(\mathcal T\) be triangulated, let \(A\to B'\to C\to A[1]\) be a distinguished triangle in \(\mathcal T\), and let \(Z\in\operatorname{Kar}(\mathcal T)\). Applying \(\operatorname{Hom}_{\operatorname{Kar}(\mathcal T)}(Z,-)\) to the triangle and its rotations gives a long exact sequence.

**Proof.** Write \(Z=(T,p)\). Precomposition with \(p\) is an idempotent endomorphism of each group \(\operatorname{Hom}_{\mathcal T}(T,X)\), natural in \(X\), with image \(\operatorname{Hom}_{\operatorname{Kar}(\mathcal T)}(Z,X)\). The sequence of groups \(\operatorname{Hom}_{\mathcal T}(T,-)\) is exact ([Li, Volume 2, Proposition 4.1.12 and Remark 4.1.11](https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en)), and the image of a natural idempotent on an exact sequence is exact: if \(y\) lies in the image of the idempotent and maps to zero, then \(y=f(x)\) for some \(x\), and \(y=py=f(px)\) with \(px\) in the image. \(\square\)

**Lemma 4.3** (odd double). Let \(\mathcal T\) be triangulated, \(L\in\mathcal T\), \(\epsilon\in\operatorname{End}(L)\) idempotent and \(U=(L,\epsilon)\in\operatorname{Kar}(\mathcal T)\). Then \(U\oplus U[1]\) and \(U\oplus U[3]\) are isomorphic in \(\operatorname{Kar}(\mathcal T)\) to objects of \(\mathcal T\).

**Proof.** *Step 1: a formal cone.* Let \(A\xrightarrow fB'\xrightarrow gC\xrightarrow hA[1]\) be distinguished in \(\mathcal T\), and suppose that in \(\operatorname{Kar}(\mathcal T)\) there are decompositions \(A=I\oplus A_0\), \(B'=I\oplus B_0\) in which \(f\) is the identity on \(I\) and zero on all other components. We show \(C\cong B_0\oplus A_0[1]\). Since \(gf=0\), \(g\) vanishes on \(I\): \(g=g_0\operatorname{pr}_{B_0}\) for some \(g_0\colon B_0\to C\). Since \(f[1]h=0\), the component of \(h\) in \(I[1]\) vanishes: \(h=\operatorname{in}_{A_0[1]}h_0\) for some \(h_0\colon C\to A_0[1]\). For every \(Z\in\operatorname{Kar}(\mathcal T)\), the sequence (4.1)
\[
\begin{aligned}
&0\to\operatorname{Hom}(Z,B_0)\xrightarrow{(g_0)_*}\operatorname{Hom}(Z,C)\\
&\qquad\xrightarrow{(h_0)_*}\operatorname{Hom}(Z,A_0[1])\to0
\end{aligned}
\]
is exact. Indeed, by Lemma 4.2: a map \(\varphi\colon Z\to B_0\) with \(g_0\varphi=0\) gives \(g\operatorname{in}_{B_0}\varphi=0\), so \(\operatorname{in}_{B_0}\varphi=f\psi\) for some \(\psi\), and \(\varphi=\operatorname{pr}_{B_0}f\psi=0\). A map \(\gamma\colon Z\to C\) with \(h_0\gamma=0\) has \(h\gamma=0\), so \(\gamma=g\beta=g_0(\operatorname{pr}_{B_0}\beta)\). Every map \(\delta\colon Z\to A_0[1]\) satisfies \(f[1]\operatorname{in}_{A_0[1]}\delta=0\), so \(\operatorname{in}_{A_0[1]}\delta=h\gamma\) for some \(\gamma\), and \(\delta=h_0\gamma\). Finally \(h_0g_0=0\), since \(hg=0\). Taking \(Z=A_0[1]\) gives \(\sigma\colon A_0[1]\to C\) with \(h_0\sigma=\mathrm{id}\). By (4.1), the map \((g_0,\sigma)\colon B_0\oplus A_0[1]\to C\) induces a bijection on \(\operatorname{Hom}(Z,-)\) for every \(Z\); taking \(Z=C\) and \(Z=B_0\oplus A_0[1]\) shows that it is an isomorphism.

*Step 2: \(U\oplus U[1]\).* Complete \(1-\epsilon\colon L\to L\) to a distinguished triangle \(L\to L\to S\to L[1]\) in \(\mathcal T\). With \(L=(L,1-\epsilon)\oplus(L,\epsilon)\) on both sides, \(1-\epsilon\) is the identity on \((L,1-\epsilon)\) and zero on the rest. Step 1 gives \(S\cong U\oplus U[1]\).

*Step 3: \(U\oplus U[3]\).* Let \(\phi\colon S[1]\to S\) be the morphism that, under \(S[1]\cong U[1]\oplus U[2]\) and \(S\cong U\oplus U[1]\), is the identity from \(U[1]\) to \(U[1]\) and zero on the other components. It is a morphism of \(\mathcal T\), because the embedding is full. Complete it to a distinguished triangle in \(\mathcal T\); Step 1, with \(I=U[1]\), \(A_0=U[2]\) and \(B_0=U\), shows that its third object is isomorphic to \(U\oplus U[3]\). \(\square\)

The two steps explain the shift by three: \(U\oplus U[1]\) appears as the cone of \(1-\epsilon\), and the second cone trades the summand \(U[1]\) for \(U[3]\). Balmer and Schlichting proved that \(\operatorname{Kar}(\mathcal T)\) is always triangulated [BS, Theorem 1.5]; Lemma 4.3 needs only the triangles of \(\mathcal T\).

## 5. A diagram in Q that evaluates to the selection

Apply Lemma 4.3 in \(Q\) to \(L=E_0\) and \(\epsilon=\theta(e)\). Let \(U=(L,\theta(e))\) and \(V=U\oplus U[3]\), and fix once and for all an object \(V_0\in Q\) and an isomorphism \(\iota\colon V_0\to V\) in \(\operatorname{Kar}(Q)\).

**Lemma 5.1.** The map \(r\mapsto\theta\bigl(e\,\alpha(r)\,e\bigr)\) is a unital algebra homomorphism \(R\to\operatorname{End}_{\operatorname{Kar}(Q)}(U)\).

**Proof.** The element \(\theta(e\alpha(r)e)=\theta(e)\theta(\alpha(r))\theta(e)\) is an endomorphism of \(U\). For \(r=1\) it is \(\theta(e)=\mathrm{id}_U\). Since \(e\) is central and idempotent, \(e\alpha(r)e\cdot e\alpha(r')e=e\alpha(rr')e\). \(\square\)

Let \(R\) act on \(U[3]\) by the shifted endomorphisms, on \(V\) diagonally, and on \(V_0\) by \(\varrho(r)=\iota^{-1}\circ(\text{action on }V)\circ\iota\). A *\(B\)-diagram* in a \(k\)-linear additive category consists of objects \(W_0,W_1,W_2\) and morphisms \(t_a\colon W_i\to W_j\) for the arrows \(a\colon i\to j\) such that \(\sum_{a,b}\rho_{ba}t_bt_a=0\) for every \(\rho\in\mathcal R\); a morphism of \(B\)-diagrams is a triple of morphisms commuting with all \(t_a\).

**Lemma 5.2.** Putting \(V_0\) at the three vertices, the identity for \(s\) and \(s'\), and \(\varrho(x_h)\) for \(a_h\) and \(a'_h\), defines a \(B\)-diagram \(\mathcal V\) in \(Q\).

**Proof.** The relation \(a'_hs-s'a_h\) gives \(\varrho(x_h)-\varrho(x_h)=0\). The homogenized relation \(\widetilde p_j\) evaluates to \(p_j\bigl(\varrho(x_1),\dots,\varrho(x_d)\bigr)=\varrho(p_j)=0\), since \(\varrho\) is an algebra homomorphism. The relations span the span of \(\mathcal R\), so every \(\rho\in\mathcal R\) evaluates to zero. \(\square\)

**Lemma 5.3.** Every object of \(\mathrm D^b(k)\) is isomorphic to a finite direct sum \(\bigoplus_nV^n[-n]\) of vector spaces placed in single degrees, and for two such objects \(V=\bigoplus_nV^n[-n]\) and \(W=\bigoplus_nW^n[-n]\),
\[
\operatorname{Hom}_{\mathrm D^b(k)}(V,W)=\bigoplus_n\operatorname{Hom}_k(V^n,W^n).
\]
In particular every idempotent of \(\mathrm D^b(k)\) has an image, and every additive functor \(F\colon Q\to\mathrm D^b(k)\) extends to an additive functor \(\operatorname{Kar}(Q)\to\mathrm D^b(k)\) commuting with shifts.

**Proof.** In a bounded complex \(V\) of vector spaces choose complements: \(V^n=Z^n\oplus C^n\) with \(Z^n=\ker d^n\), and \(Z^n=B^n\oplus H^n\) with \(B^n=d(V^{n-1})\). The differential maps \(C^n\) isomorphically onto \(B^{n+1}\), so \(V\) is the direct sum of the complex \(\bigoplus_nH^n[-n]\) with zero differential and the complexes \(C^n\to B^{n+1}\), which are contractible; hence \(V\cong\bigoplus_nH^n[-n]\). Morphisms \(V^n[-n]\to W^m[-m]\) in the derived category form \(\operatorname{Ext}^{n-m}_k(V^n,W^m)\) ([Li, Volume 2, Definition 4.5.8](https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en)), which is \(0\) for \(n<m\) and \(\operatorname{Hom}_k(V^n,W^n)\) for \(n=m\) ([Li, Volume 2, Proposition 4.5.9](https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en)), and \(0\) for \(n>m\) because every vector space is projective ([Li, Volume 2, Proposition 4.9.6](https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en)). An idempotent is thus a family of idempotents \(p^n\) of the \(V^n\), with image \(\bigoplus_np^n(V^n)[-n]\). For the extension, choose for every \((T,p)\) an image \(F_*(T,p)\) of \(F(p)\), with maps \(i\colon F_*(T,p)\to F(T)\) and \(r\colon F(T)\to F_*(T,p)\) satisfying \(ri=\mathrm{id}\) and \(ir=F(p)\), and send \(u\colon(T,p)\to(T',p')\) to \(r'F(u)i\). Since \(u=p'up\), this is compatible with composition. \(\square\)

**Proposition 5.4.** For every finite-dimensional \(R\)-module \(Y\), the image of the diagram \(\mathcal V\) under the extension of \(\overline{\operatorname{ev}}_Y\) is isomorphic to the \(B\)-diagram in \(\mathrm D^b(k)\) with \(eY\oplus(eY)[3]\) at every vertex, identities for \(s\) and \(s'\), and the action of \(\alpha(x_h)\) on both summands for \(a_h\) and \(a'_h\).

**Proof.** By Proposition 3.2, \(\overline{\operatorname{ev}}_Y(\theta(e))\) is the action of \(e\) on \(Y\), an idempotent with image \(eY\); so the extension sends \(U\) to \(eY\) and \(U[3]\) to \((eY)[3]\). It sends the endomorphism \(\theta(e\alpha(r)e)\) of \(U\) to the restriction of the action of \(e\alpha(r)e\) to \(eY\), which is the action of \(\alpha(r)\) on \(eY\). The isomorphism \(\iota\) is sent to an isomorphism from the image of \(V_0\) to \(eY\oplus(eY)[3]\) that intertwines the actions of \(R\), and applying it at the three vertices gives the isomorphism of diagrams. \(\square\)

In the notation of [A selection process with unbounded extinction](a-selection-process-with-unbounded-extinction.md), the target diagram is \(H(Y)\oplus H(Y)[3]\) placed at each vertex, with the arrows acting as in \(M(H(Y))\). The diagram \(\mathcal V\) was chosen before \(Y\); only its evaluation depends on \(Y\).

## 6. Exercises

**Exercise 6.1** (easy). Show that in \(\operatorname{Kar}(\mathcal T)\) every object \(T\) is isomorphic to \((T,p)\oplus(T,1-p)\) for every idempotent \(p\) of \(T\).

**Exercise 6.2** (easy). Let \(e=1\) and \(\alpha=\mathrm{id}\). Show that \(U\cong L\) and that one may take \(V_0=L\oplus L[3]\). What does Proposition 5.4 say in this case?

**Exercise 6.3** (medium). Show that the object \(S\) of Step 2 of Lemma 4.3 is zero when \(\epsilon=0\), and isomorphic to \(L\oplus L[1]\) when \(\epsilon=1\).

**Exercise 6.4** (medium). Let \(F\colon K\to\mathcal D\) be a triangulated functor that sends \(s\) and \(s'\) to isomorphisms. Show, without Theorem 2.1, that \(F\) sends \(\operatorname{Cone}(s)\) and \(\operatorname{Cone}(s')\) to zero.

## 7. Solutions

**6.1.** The morphisms \(p\colon(T,\mathrm{id})\to(T,p)\), \(1-p\colon(T,\mathrm{id})\to(T,1-p)\) and their counterparts \(p\colon(T,p)\to(T,\mathrm{id})\), \(1-p\colon(T,1-p)\to(T,\mathrm{id})\) satisfy \(p\cdot p=\mathrm{id}_{(T,p)}\), \((1-p)(1-p)=\mathrm{id}_{(T,1-p)}\), \(p(1-p)=0\) and \(p+(1-p)=\mathrm{id}_T\), which are the identities of a direct sum.

**6.2.** For \(e=1\), \(\theta(e)=\mathrm{id}_L\), so \(U=(L,\mathrm{id})\), which is \(L\) under the embedding, and \(V=L\oplus L[3]\) is an object of \(Q\). Proposition 5.4 says that \(V_0\) evaluates to \(Y\oplus Y[3]\) with the arrows acting as on \(M(Y)\) on both summands: the diagram records \(Y\) twice, three degrees apart.

**6.3.** If \(\epsilon=0\), the triangle is built on \(\mathrm{id}_L\), whose cone is zero. If \(\epsilon=1\), it is built on the zero map \(L\to L\), whose cone is \(L\oplus L[1]\); both agree with \(U\oplus U[1]\), since \(U=0\), respectively \(U\cong L\).

**6.4.** The image of the triangle \(E_0\xrightarrow sE_1\to\operatorname{Cone}(s)\to E_0[1]\) is distinguished in \(\mathcal D\) with first map an isomorphism. Applying \(\operatorname{Hom}(F\operatorname{Cone}(s),-)\) gives an exact sequence in which the maps induced by \(F(s)\) and \(F(s)[1]\) are bijective, so \(\operatorname{Hom}(F\operatorname{Cone}(s),F\operatorname{Cone}(s))=0\), and \(F\operatorname{Cone}(s)=0\). The same holds for \(s'\).

## References

- [OpenAI-FD] OpenAI, *An algebra of infinite little finitistic dimension*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026
- [BS] P. Balmer and M. Schlichting, *Idempotent completion of triangulated categories*, Journal of Algebra 236 (2001), 819–834; author's version. https://www.math.ucla.edu/~balmer/Pubfile/IdempCompl.pdf
- [Li] W.-W. Li, *Methods of Algebra*, Volume 2, English edition. https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en
