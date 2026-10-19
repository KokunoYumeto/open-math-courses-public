# Diagrams up to weak equivalence

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A derived category keeps the objects and morphisms of a homotopy theory but forgets how they sit in diagrams. The cone of a morphism of a derived category exists, but only up to an isomorphism that is not unique, and no choice of cones is a functor on arrows. The cone of an *arrow of complexes*, considered up to levelwise quasi-isomorphism, is a functor. In *Pursuing Stacks* (1983, §69) Grothendieck proposed to keep, for an abelian category \(\mathcal A\), all the derived categories \(D(\mathcal A^I)\) of diagram categories at once, together with the restriction functors between them, and to regard this system as the complete structure that \(\mathcal A\) defines. He called such a system a *derivator*.

This lesson makes the starting point precise. Section 1 builds the cone functor on arrows of complexes. Section 2 exhibits a nonzero morphism of arrows in a derived category whose two components are zero, and deduces that cones in \(D(\mathcal A)\) cannot be chosen functorially. Sections 3 and 4 construct localizations and assemble the categories \(D(I)\) into a *prederivator*, a strict 2-functor on small categories. Section 5 introduces the underlying diagram functors, which compare \(D(I)\) with the category of \(I\)-shaped diagrams in \(D(e)\).

**Prerequisites.** Categories, functors and natural transformations; abelian categories. The programme lesson [*Complexes, cones and localization*](course:derived-categories-and-sheaf-operations/complexes-cones-and-localization) supplies complexes, homotopies and cohomology (Lemmas 1.1–1.2), the cone \(C(f)\) of a chain map (formula (2.1) and Lemma 2.1), the derived category \(D(\mathcal A)\) as the category of roof classes with its localization functor \(Q\) (Theorem 4.2), and the triangulated structure of \(D(\mathcal A)\) (Theorem 5.1). The lessons [*Simplicial sets, nerves and Kan complexes*](course:AG-AS/simplicial-sets-nerves-and-kan-complexes) and [*Test categories and Grothendieck's homotopy programme*](course:AG-AS/test-categories-and-homotopy-programme) of the course *Algebraic spaces and stacks* describe the homotopy programme of *Pursuing Stacks* to which this course belongs.

## 1. The cone of an arrow of complexes

Throughout, \(\mathcal A\) is an abelian category, \(C(\mathcal A)\) its category of cochain complexes, \(K(\mathcal A)\) the homotopy category and \(Q:K(\mathcal A)\to D(\mathcal A)\) the localization at the quasi-isomorphisms. Differentials raise degree, \(K[r]^n=K^{n+r}\), and the cone of a chain map \(f:K\to L\) is

\[
C(f)^n=L^n\oplus K^{n+1},
\]
\[
d(l,k)=(d_Ll+fk,\,-d_Kk).
\]

For a small category \(I\), the category \(\mathcal A^I\) of functors \(I\to\mathcal A\) is abelian: kernels, cokernels and images are formed objectwise, and a sequence is exact when it is exact at every object of \(I\). A complex in \(\mathcal A^I\) is the same as a functor from \(I\) to \(C(\mathcal A)\). Cohomology is formed objectwise, so a chain map in \(\mathcal A^I\) is a quasi-isomorphism exactly when each of its components is. A homotopy between chain maps \(X\to Y\) in \(\mathcal A^I\) is a family of homotopies \(s_i:X_i\to Y_i[-1]\), natural in \(i\). We write \(D(\mathcal A^I)\) for the derived category of the abelian category \(\mathcal A^I\).

Let \([1]\) be the category with objects \(0,1\) and one non-identity arrow \(0\to1\). An object of \(C(\mathcal A^{[1]})\) is a chain map \(f:K\to L\). A morphism \((a,b):f\to f'\) is a pair of chain maps \(a:K\to K'\), \(b:L\to L'\) with \(bf=f'a\).

**Proposition 1.1 (cones of arrows).**

1. The assignments \(f\mapsto C(f)\) and \((a,b)\mapsto c\), where
\[
c^n=\begin{pmatrix}b^n&0\\0&a^{n+1}\end{pmatrix},
\]
define an additive functor \(C:C(\mathcal A^{[1]})\to C(\mathcal A)\).
2. \(C\) sends homotopic morphisms to homotopic chain maps, and levelwise quasi-isomorphisms to quasi-isomorphisms.
3. There is a unique functor \(\operatorname{Cone}:D(\mathcal A^{[1]})\to D(\mathcal A)\) with \(\operatorname{Cone}\circ Q=Q\circ C\). It sends zero objects to zero objects.

**Proof.** (1) Lemma 2.1 of *Complexes, cones and localization*, with the zero homotopy, shows that \(c\) is a chain map. Identities go to identity matrices, and the composite of two diagonal matrices is the diagonal matrix of the composites, so \(C\) is a functor. Its effect on morphisms is additive because the diagonal entries are.

(2) Let \((a,b)\) and \((a',b')\) be homotopic, through homotopies \(s_0\) from \(a'\) to \(a\) and \(s_1\) from \(b'\) to \(b\). Naturality of the family on the arrow \(0\to1\) says \(s_1f=f's_0\). Define \(H^n:C(f)^n\to C(f')^{n-1}\) by

\[
H(l,k)=(s_1l,\,-s_0k).
\]

Then

\[
dH(l,k)=(d s_1l-f's_0k,\;d s_0k),
\]
\[
Hd(l,k)=(s_1dl+s_1fk,\;s_0dk).
\]

The sum has first coordinate \((ds_1+s_1d)l+(s_1f-f's_0)k=(b-b')l\) and second coordinate \((ds_0+s_0d)k=(a-a')k\). Thus \(dH+Hd=c-c'\).

For quasi-isomorphisms, the inclusion \(L\to C(f)\) and the projection \(C(f)\to K[1]\) form a sequence

\[
0\to L\to C(f)\to K[1]\to0
\]

that is split exact in each degree, and a morphism \((a,b)\) maps it to the corresponding sequence of \(f'\) through \(b\), \(c\) and \(a[1]\). Lemma 1.2 of *Complexes, cones and localization* gives long exact cohomology sequences and a map between them. If \(a\) and \(b\) are quasi-isomorphisms, the Five Lemma shows that every \(H^n(c)\) is an isomorphism.

(3) By (2), \(C\) induces a functor \(K(\mathcal A^{[1]})\to K(\mathcal A)\), and \(Q\circ C\) inverts quasi-isomorphisms. Theorem 4.2 of *Complexes, cones and localization* gives the unique factorization through \(Q:K(\mathcal A^{[1]})\to D(\mathcal A^{[1]})\). The cone of \(0\to0\) is the zero complex, and \(Q\) preserves zero objects because it is additive. Every zero object of \(D(\mathcal A^{[1]})\) is isomorphic to \(Q\) of the zero arrow, so \(\operatorname{Cone}\) sends it to a zero object. \(\square\)

An object of \(D(\mathcal A^{[1]})\) has two *components* in \(D(\mathcal A)\) and an arrow between them. Evaluation at \(0\) and at \(1\) are exact functors \(\mathcal A^{[1]}\to\mathcal A\), so they preserve homotopies and quasi-isomorphisms and induce functors \(0^*,1^*:D(\mathcal A^{[1]})\to D(\mathcal A)\). For \(X\) represented by \(f:K\to L\) we write \(X_0=Q(K)\), \(X_1=Q(L)\), and \(X_{01}=Q(f):X_0\to X_1\). For a morphism \(\varphi:X\to Y\) we write \(\varphi_0=0^*\varphi\) and \(\varphi_1=1^*\varphi\). Section 5 shows that \(X\mapsto X_{01}\) is a functor \(D(\mathcal A^{[1]})\to D(\mathcal A)^{[1]}\), the *underlying diagram functor*.

## 2. A morphism that its components do not see

Take \(\mathcal A=\mathrm{Ab}\), the category of abelian groups. Let \(\mathbb Z\) also denote the complex with \(\mathbb Z\) in degree \(0\), and let \(\mathbb Z[1]\) be \(\mathbb Z\) in degree \(-1\). The cone of the identity,

\[
P=C(1_{\mathbb Z}),
\]

is \(\mathbb Z\) in degrees \(-1\) and \(0\) with \(d^{-1}=1\). It is acyclic. Let \(\iota:\mathbb Z\to P\) be the inclusion in degree \(0\). Consider the three arrows of complexes

\[
X=(\mathbb Z\to0),
\]
\[
\widetilde X=(\iota:\mathbb Z\to P),
\]
\[
Y=(0\to\mathbb Z[1]),
\]

and the two morphisms of arrows

\[
q=(1_{\mathbb Z},\,P\to0):\widetilde X\to X,
\]
\[
\psi=(0,\,g):\widetilde X\to Y,
\]

where \(g:P\to\mathbb Z[1]\) is the identity of \(\mathbb Z\) in degree \(-1\) and zero in degree \(0\). The map \(g\) is a chain map: its only condition is \(g^0d_P^{-1}=d_{\mathbb Z[1]}^{-1}g^{-1}\), and both sides are zero. The square for \(\psi\) commutes because \(g\iota\) has source in degree \(0\), where \(\mathbb Z[1]\) vanishes. The square for \(q\) commutes because both composites end in \(0\). The morphism \(q\) is a levelwise quasi-isomorphism, since \(P\) is acyclic. Define

\[
\varphi=Q(\psi)\,Q(q)^{-1}:X\to Y
\]

in \(D(\mathrm{Ab}^{[1]})\).

**Proposition 2.1.**

1. The components \(\varphi_0\) and \(\varphi_1\) are zero in \(D(\mathrm{Ab})\).
2. The cones of \(X\) and \(Y\) have cohomology \(\mathbb Z\) in degree \(-1\) and zero in all other degrees, and \(\operatorname{Cone}(\varphi)\) induces \(-1\) on \(H^{-1}\) for the generators chosen in the proof. In particular \(\operatorname{Cone}(\varphi)\) is an isomorphism.
3. \(\varphi\neq0\).

**Proof.** (1) The morphism \(\varphi_0\) ends at \(Y_0=0\), and \(\varphi_1\) starts at \(X_1=0\). In the additive category \(D(\mathrm{Ab})\) a morphism into or out of a zero object is zero.

(2) The cone of \(\mathbb Z\to0\) is \(0\oplus\mathbb Z[1]=\mathbb Z[1]\), and the cone of \(0\to\mathbb Z[1]\) is \(\mathbb Z[1]\). The cone of \(\iota\) has \(C(\iota)^{-1}=P^{-1}\oplus\mathbb Z^0=\mathbb Z^2\) and \(C(\iota)^0=P^0=\mathbb Z\), with

\[
d^{-1}(p,z)=p+z.
\]

Its cohomology is \(\mathbb Z\) in degree \(-1\), generated by \(u=(1,-1)\), and zero elsewhere. On cones, \(q\) induces \((p,z)\mapsto z\) in degree \(-1\), so \(C(q)\) sends \(u\) to \(-1\), a generator of \(H^{-1}\) of \(\mathbb Z[1]\). The map \(\psi\) induces \((p,z)\mapsto g(p)=p\), so \(C(\psi)\) sends \(u\) to \(1\). Both \(C(q)\) and \(C(\psi)\) are quasi-isomorphisms, and by Proposition 1.1

\[
\operatorname{Cone}(\varphi)=Q(C(\psi))\,Q(C(q))^{-1},
\]

which induces \(1\cdot(-1)^{-1}=-1\) on \(H^{-1}\).

(3) If \(\varphi=0\), then \(\varphi\) factors through a zero object of \(D(\mathrm{Ab}^{[1]})\). By Proposition 1.1, \(\operatorname{Cone}(\varphi)\) then factors through a zero object and is zero. But a zero morphism induces zero on \(H^{-1}\), while \(\operatorname{Cone}(\varphi)\) induces \(-1\) on \(H^{-1}\cong\mathbb Z\). \(\square\)

**Corollary 2.2.**

1. The functor \(D(\mathrm{Ab}^{[1]})\to D(\mathrm{Ab})^{[1]}\), \(X\mapsto X_{01}\), \(\varphi\mapsto(\varphi_0,\varphi_1)\), is not faithful.
2. There is no functor \(F:D(\mathrm{Ab})^{[1]}\to D(\mathrm{Ab})\) with a natural isomorphism from \(F(X_{01})\) to \(\operatorname{Cone}(X)\).

**Proof.** (1) \(\varphi\) and \(0\) have the same image \((0,0)\).

(2) Suppose \(\theta:F(X_{01})\to\operatorname{Cone}(X)\) is a natural isomorphism. Naturality at \(\varphi\) gives

\[
\operatorname{Cone}(\varphi)=\theta_Y\,F(0,0)\,\theta_X^{-1}.
\]

The morphism \((0,0):X_{01}\to Y_{01}\) of \(D(\mathrm{Ab})^{[1]}\) factors through the arrow \(0\to0\). This arrow is \(N_{01}\) for the zero object \(N\) of \(D(\mathrm{Ab}^{[1]})\), so \(F(0\to0)\) is isomorphic, through \(\theta_N\), to \(\operatorname{Cone}(N)\), a zero object. Hence \(F(0,0)\) and \(\operatorname{Cone}(\varphi)\) are zero, contradicting Proposition 2.1. \(\square\)

Every morphism \(u:x\to y\) of \(D(\mathcal A)\) does have a cone: Theorem 5.1 of *Complexes, cones and localization* completes it to a distinguished triangle \(x\to y\to z\to x[1]\), and \(z\) is unique up to an isomorphism. Corollary 2.2 shows that no choice of these cones is compatible with the cones of arrows of complexes. Grothendieck's remedy is to keep \(D(\mathcal A^{[1]})\), and every other \(D(\mathcal A^{I})\), as part of the structure.

## 3. Localization

**Definition 3.1.** Let \(\mathcal M\) be a category and \(\mathcal W\) a class of morphisms of \(\mathcal M\). A *localization of \(\mathcal M\) at \(\mathcal W\)* is a functor \(\gamma:\mathcal M\to\mathcal M[\mathcal W^{-1}]\) that sends the morphisms of \(\mathcal W\) to isomorphisms and has two properties.

1. For every functor \(F:\mathcal M\to\mathcal C\) sending \(\mathcal W\) to isomorphisms there is exactly one functor \(\bar F\) with \(\bar F\gamma=F\).
2. For functors \(G,H:\mathcal M[\mathcal W^{-1}]\to\mathcal C\), every natural transformation \(\alpha:G\gamma\to H\gamma\) is \(\beta\gamma\) for exactly one natural transformation \(\beta:G\to H\).

Here \(\beta\gamma\) denotes the natural transformation with components \(\beta_{\gamma(X)}\). Property 2 says that \(\gamma\) induces a fully faithful functor between functor categories.

**Theorem 3.2 (existence).** For every category \(\mathcal M\) and class \(\mathcal W\) there is a localization \(\gamma\) that is the identity on objects. Every morphism of \(\mathcal M[\mathcal W^{-1}]\) is a composite of morphisms \(\gamma(f)\) and \(\gamma(w)^{-1}\) with \(f\) in \(\mathcal M\) and \(w\in\mathcal W\).

**Proof.** Form the directed graph whose vertices are the objects of \(\mathcal M\) and whose edges are the morphisms \(f:X\to Y\) of \(\mathcal M\), together with one reversed edge \(\bar w:Y\to X\) for each \(w:X\to Y\) in \(\mathcal W\). Its path category has finite composable strings of edges as morphisms, with the empty strings as identities. Let \(\sim\) be the smallest equivalence relation on strings that is compatible with concatenation and identifies

- the string \((f,g)\) with the one-letter string \(gf\), for composable \(f,g\) in \(\mathcal M\);
- the one-letter string \(1_X\) with the empty string at \(X\);
- for \(w:X\to Y\) in \(\mathcal W\), the strings \((w,\bar w)\) and \((\bar w,w)\) with the empty strings at \(X\) and at \(Y\).

The quotient \(\mathcal M[\mathcal W^{-1}]\) of the path category by \(\sim\) is a category, because \(\sim\) is compatible with concatenation. Sending \(f\) to the class of its one-letter string defines a functor \(\gamma\), by the first two relations. The third relation makes \(\gamma(w)\) invertible with inverse the class of \(\bar w\). Every class is a composite of classes of one-letter strings, which proves the last assertion.

For property 1, a functor \(\bar F\) with \(\bar F\gamma=F\) must send \(f\) to \(F(f)\) and \(\bar w\) to \(F(w)^{-1}\). Conversely, these values define a functor on the path category, and it takes equal values on strings related by each of the three generating relations. The relation on which two strings have equal values is an equivalence relation compatible with concatenation, so it contains \(\sim\). Hence \(\bar F\) exists and is unique.

For property 2, put \(\beta_X=\alpha_X\); this is possible because \(\gamma\) is the identity on objects. Naturality of \(\beta\) with respect to \(\gamma(f)\) is naturality of \(\alpha\). For \(w:X\to Y\) in \(\mathcal W\), naturality of \(\alpha\) at \(w\) reads \(H\gamma(w)\,\alpha_X=\alpha_Y\,G\gamma(w)\). Multiplying on the left by \(H\gamma(w)^{-1}\) and on the right by \(G\gamma(w)^{-1}\) gives

\[
\alpha_X\,G(\gamma(w)^{-1})=H(\gamma(w)^{-1})\,\alpha_Y,
\]

which is naturality at \(\gamma(w)^{-1}\). Naturality with respect to a composite follows from naturality with respect to its factors, so \(\beta\) is natural. It is unique because its components are prescribed. \(\square\)

When \(\mathcal M\) is small, \(\mathcal M[\mathcal W^{-1}]\) is small. In general its morphisms between two objects form a set in a larger universe, and we work in such a universe when necessary, as *Complexes, cones and localization* does for derived categories. Whether these sets are small in the original universe is a separate question; for module categories the resolution lessons of the course *Derived categories and sheaf operations* answer it.

A localization is unique up to a unique isomorphism: if \(\gamma'\) is another, property 1 for each of them gives functors \(\bar\gamma'\) and \(\bar\gamma\) between the targets, and both composites restrict along \(\gamma\) or \(\gamma'\) to the localization functor itself, so they are identities by uniqueness. Theorem 4.2 of *Complexes, cones and localization* states both properties of Definition 3.1 for \(Q:K(\mathcal A)\to D(\mathcal A)\) and the quasi-isomorphisms.

**Lemma 3.3 (induced functors and transformations).** Let \(\gamma:\mathcal M\to\mathcal M[\mathcal W^{-1}]\) and \(\gamma':\mathcal M'\to\mathcal M'[\mathcal W'^{-1}]\) be localizations.

1. A functor \(F:\mathcal M\to\mathcal M'\) with \(F(\mathcal W)\subset\mathcal W'\) induces a unique functor \(\bar F\) with \(\bar F\gamma=\gamma'F\).
2. A natural transformation \(\alpha:F\to G\) between two such functors induces a unique natural transformation \(\bar\alpha:\bar F\to\bar G\) with \(\bar\alpha\gamma=\gamma'\alpha\).
3. \(\overline{GF}=\bar G\bar F\) and \(\overline{1}=1\) whenever \(G\) is defined on \(\mathcal M'\) and induced through a third localization; \(\overline{\beta\alpha}=\bar\beta\bar\alpha\), \(\overline{1_F}=1_{\bar F}\), and \(\overline{K\alpha}=\bar K\bar\alpha\), \(\overline{\alpha L}=\bar\alpha\bar L\) for functors \(K\), \(L\) of the same kind.

**Proof.** (1) The functor \(\gamma'F\) inverts \(\mathcal W\); apply property 1 of \(\gamma\). (2) Apply property 2 of \(\gamma\) to \(\gamma'\alpha:\bar F\gamma\to\bar G\gamma\). (3) In each identity both sides satisfy the defining equation of the induced functor or transformation; for instance \(\bar G\bar F\gamma=\bar G\gamma'F=\gamma''GF\). Uniqueness in (1) and (2) gives the equalities. \(\square\)

## 4. Prederivators

Let \(\mathrm{Cat}\) be the 2-category of small categories, functors and natural transformations, and \(e\) the category with one object and one morphism.

**Definition 4.1.** A *prederivator* \(\mathbb D\) assigns

- to every small category \(J\) a category \(\mathbb D(J)\);
- to every functor \(u:J\to K\) a functor \(u^*:\mathbb D(K)\to\mathbb D(J)\);
- to every natural transformation \(\alpha:u\to v\) between functors \(J\to K\) a natural transformation \(\alpha^*:u^*\to v^*\),

such that the following equalities hold:

- \((vu)^*=u^*v^*\) and \((1_J)^*=1\);
- \((\beta\alpha)^*=\beta^*\alpha^*\) and \((1_u)^*=1_{u^*}\);
- \((w\alpha)^*=\alpha^*w^*\) and \((\alpha t)^*=t^*\alpha^*\), for functors \(w:K\to L\) and \(t:I\to J\).

In the third line, \(w\alpha:wu\to wv\) and \(\alpha t:ut\to vt\) are whiskerings, and \(\alpha^*w^*\) has components \(\alpha^*_{w^*X}\). These are the conditions for a strict 2-functor from \(\mathrm{Cat}\) to categories that reverses functors and keeps the direction of natural transformations. *Strict* means that the equalities hold on the nose, not up to isomorphism.

**Theorem 4.2 (the prederivator of a category with weak equivalences).** Let \(\mathcal M\) be a category and \(\mathcal W\) a class of morphisms containing the identities. For a small category \(J\), let \(\mathcal W_J\) be the morphisms of \(\mathcal M^J\) whose components lie in \(\mathcal W\), and choose a localization \(\gamma_J:\mathcal M^J\to\mathbb D(J)\) at \(\mathcal W_J\). Then there is exactly one prederivator \(\mathbb D=\mathbb D_{(\mathcal M,\mathcal W)}\) with values \(\mathbb D(J)\) such that

\[
u^*\gamma_K=\gamma_J\,u^*,
\]
\[
\alpha^*\gamma_K=\gamma_J\,\alpha^*,
\]

where on the right \(u^*X=X\circ u\) and \((\alpha^*)_X=X\alpha:Xu\to Xv\).

**Proof.** Precomposition \(u^*:\mathcal M^K\to\mathcal M^J\) sends \(\mathcal W_K\) into \(\mathcal W_J\), because the components of \(Xu\to Yu\) are components of \(X\to Y\). Lemma 3.3 gives unique induced functors and transformations with the two displayed equations. On the level of diagrams the equalities of Definition 4.1 hold: \(X(vu)=(Xv)u\); the components of \((\beta\alpha)^*\) are \(X\beta\circ X\alpha\); and \((X(w\alpha))=(Xw)\alpha\), \((X\alpha)t=X(\alpha t)\). Lemma 3.3(3) transports each of these equalities to the induced functors and transformations. \(\square\)

**Example 4.3 (represented prederivators).** For a category \(\mathcal C\), take \(\mathcal W\) to be the identities. Then \(\gamma_J\) can be the identity of \(\mathcal C^J\), and \(\mathbb D(J)=\mathcal C^J\). This is the prederivator *represented* by \(\mathcal C\), written \(y(\mathcal C)\).

**Example 4.4 (the prederivator of an abelian category).** Let \(\mathcal A\) be abelian and put \(\mathbb D_{\mathcal A}(J)=D(\mathcal A^J)\), with \(Q_J:K(\mathcal A^J)\to D(\mathcal A^J)\). For \(u:J\to K\), precomposition \(K(\mathcal A^K)\to K(\mathcal A^J)\) is well defined, since it carries homotopies to homotopies, and it preserves quasi-isomorphisms, since they are objectwise. For \(\alpha:u\to v\), the chain maps \(X\alpha:Xu\to Xv\) are natural in \(X\) up to homotopy. Lemma 3.3, applied to the localizations \(Q_J\), gives \(u^*\) and \(\alpha^*\), and the proof of Theorem 4.2 applies word for word. This is Grothendieck's assignment

\[
I\longmapsto D(\mathcal A^I)
\]

of *Pursuing Stacks*, §69. Exercise 6.5 shows that \(D(\mathcal A^J)\) is also a localization of \(C(\mathcal A^J)\) at the quasi-isomorphisms, so \(\mathbb D_{\mathcal A}\) is the prederivator of Theorem 4.2 for \(\mathcal M=C(\mathcal A)\) and the quasi-isomorphisms, up to the unique isomorphisms of localizations.

**Example 4.5 (shifted prederivators).** For a prederivator \(\mathbb D\) and a small category \(M\), put \(\mathbb D^M(J)=\mathbb D(M\times J)\), \(u^*=(1_M\times u)^*\) and \(\alpha^*=(1_M\times\alpha)^*\). The equalities of Definition 4.1 for \(\mathbb D^M\) are those of \(\mathbb D\) for the functors \(1_M\times u\). An object of \(\mathbb D^M(J)\) is a family of objects of \(\mathbb D(J)\) indexed by \(M\), retained with its coherence. This is the "inner stability" that *Pursuing Stacks* asks of the structure: systems of objects of \(\mathbb D(J)\) are themselves objects of a value of \(\mathbb D\).

## 5. Underlying diagrams

Let \(\mathbb D\) be a prederivator and \(J\) a small category. An object \(j\) of \(J\) is a functor \(j:e\to J\), and a morphism \(\alpha:j\to j'\) is a natural transformation between such functors. They give the *evaluation functors* and transformations

\[
j^*:\mathbb D(J)\to\mathbb D(e),
\]
\[
\alpha^*:j^*\to j'^*.
\]

We write \(X_j=j^*X\) and \(f_j=j^*f\) for objects and morphisms of \(\mathbb D(J)\).

**Proposition 5.1.** The assignment

\[
X\longmapsto\bigl(j\mapsto X_j,\ \alpha\mapsto(\alpha^*)_X\bigr)
\]

defines a functor \(\operatorname{dia}_J:\mathbb D(J)\to\mathbb D(e)^J\), the *underlying diagram functor*.

**Proof.** For fixed \(X\), the second line of Definition 4.1 says that \(\alpha\mapsto(\alpha^*)_X\) preserves composition and identities, so it is a diagram \(J\to\mathbb D(e)\). For \(f:X\to Y\), naturality of each \(\alpha^*\) says that the family \((f_j)_j\) is a morphism of diagrams. Composition of morphisms is preserved because each \(j^*\) is a functor. \(\square\)

More generally, for small categories \(M\) and \(J\), the functors \(m\times1_J:J\to M\times J\) and the transformations induced by the morphisms of \(M\) give a *partial underlying diagram functor*

\[
\operatorname{dia}_{M,J}:\mathbb D(M\times J)\to\mathbb D(J)^M,
\]

by the same proof. For \(J=e\) it is \(\operatorname{dia}_M\).

For the represented prederivator \(y(\mathcal C)\), \(X_j\) is the value \(X(j)\) and \((\alpha^*)_X=X(\alpha)\), so \(\operatorname{dia}_J\) is the identity of \(\mathcal C^J\). For \(\mathbb D_{\mathcal A}\) and \(J=[1]\), the functor \(\operatorname{dia}_{[1]}\) is the functor \(X\mapsto X_{01}\) of Section 1: the transformation \((0\to1)^*:0^*\to1^*\) is induced by the chain maps \(f:K\to L\) themselves. Corollary 2.2 shows that \(\operatorname{dia}_{[1]}\) is not faithful for \(\mathcal A=\mathrm{Ab}\). An object of \(\mathbb D(J)\) is therefore more than a diagram in \(\mathbb D(e)\): Grothendieck describes it as a "refinement and substitute" for a family of objects of \(\mathbb D(e)\) indexed by \(J\).

The underlying category \(\mathbb D(e)\) has few limits and colimits in general. *Pursuing Stacks* identifies the variance property that replaces them: each restriction functor \(u^*\) should have a left adjoint \(u_!\) and a right adjoint \(u_*\). For \(u:J\to e\) these adjoints play the role of colimits and limits of \(J\)-shaped diagrams; for the two categories

\[
b\leftarrow a\rightarrow c,
\]
\[
b\rightarrow a\leftarrow c,
\]

they give pushouts and pullbacks, hence cofibres and fibres. The lesson [*Kan extensions and the derivator axioms*](kan-extensions-and-the-derivator-axioms.md) states this demand as axioms and proves them for represented prederivators of complete and cocomplete categories.

## 6. Exercises

**6.1** (easy). Let \(\mathcal M=[1]\) and let \(\mathcal W\) consist of the arrow \(0\to1\). Show that \(\mathcal M[\mathcal W^{-1}]\) has two objects and exactly one morphism between any two objects.

**6.2** (easy). For a category \(\mathcal C\), show that \(\operatorname{dia}_{M,J}:\mathcal C^{M\times J}\to(\mathcal C^J)^M\) is an isomorphism of categories for the represented prederivator.

**6.3** (medium). Show that a chain map \(f\) is a quasi-isomorphism if and only if \(C(f)\) is acyclic. Deduce that for \(X\) in \(D(\mathcal A^{[1]})\), \(\operatorname{Cone}(X)\) is a zero object if and only if \(X_{01}\) is an isomorphism of \(D(\mathcal A)\).

**6.4** (medium). For an integer \(n\), put \(\varphi_n=Q(n\psi)\,Q(q)^{-1}\) in the notation of Section 2. Show that the \(\varphi_n\) are pairwise distinct morphisms \(X\to Y\), and that all of them have \(\operatorname{dia}_{[1]}(\varphi_n)=(0,0)\).

**6.5** (hard). Show that the composite \(C(\mathcal A)\to K(\mathcal A)\xrightarrow{Q}D(\mathcal A)\) is a localization of \(C(\mathcal A)\) at the quasi-isomorphisms in the sense of Definition 3.1.

## 7. Solutions

**6.1.** In the construction of Theorem 3.2 the edges are \(1_0\), \(1_1\), \(w:0\to1\) and \(\bar w:1\to0\). The relations reduce every string to the empty string, to \(w\) or to \(\bar w\), and \(w\bar w\), \(\bar ww\) reduce to empty strings. So the only morphisms are \(1_0\), \(1_1\), \(\gamma(w)\) and its inverse.

**6.2.** For a functor \(X:M\times J\to\mathcal C\), \(\operatorname{dia}_{M,J}(X)\) sends \(m\) to \(X(m,-)\) and a morphism \(\mu:m\to m'\) to the natural transformation \(X(\mu,-)\). Conversely a functor \(Y:M\to\mathcal C^J\) defines \(X(m,j)=Y(m)(j)\) and \(X(\mu,\nu)=Y(m')(\nu)\circ Y(\mu)_j\), a functor because \(Y(\mu)\) is natural. The two constructions are inverse, also on morphisms.

**6.3.** The sequence \(0\to L\to C(f)\to K[1]\to0\) gives the exact sequence

\[
H^nL\to H^nC(f)\to H^{n+1}K\xrightarrow{\delta}H^{n+1}L.
\]

Its connecting map is \(\delta=H^{n+1}(f)\): a cycle \(k\) of \(K^{n+1}\), viewed in \(K[1]^n\), lifts to \((0,k)\), whose differential is \((fk,0)\), the image of \(fk\in L^{n+1}\). So \(H^nC(f)\) sits between the cokernel of \(H^n(f)\) and the kernel of \(H^{n+1}(f)\). Hence \(H^nC(f)=0\) for all \(n\) if and only if every \(H^n(f)\) is injective and surjective. For the second statement, represent \(X\) by \(f:K\to L\). Then \(\operatorname{Cone}(X)=Q(C(f))\) and \(X_{01}=Q(f)\). The functors \(H^n\) descend to \(D(\mathcal A)\) (Theorem 5.1 of *Complexes, cones and localization*), so \(Q(C(f))\) is a zero object exactly when \(C(f)\) is acyclic, and \(Q(f)\) is an isomorphism exactly when \(f\) is a quasi-isomorphism.

**6.4.** The proof of Proposition 2.1 with \(n\psi\) in place of \(\psi\) shows that \(C(n\psi)\) sends \(u\) to \(n\), so \(\operatorname{Cone}(\varphi_n)\) induces \(-n\) on \(H^{-1}\cong\mathbb Z\). Different \(n\) give different maps on \(H^{-1}\), hence different \(\varphi_n\). The components vanish for the reason in Proposition 2.1(1).

**6.5.** Write \(\pi:C(\mathcal A)\to D(\mathcal A)\) for the composite. Let \(F:C(\mathcal A)\to\mathcal C\) invert quasi-isomorphisms. For a complex \(K\), the *cylinder* \(\mathrm{Cyl}(K)\) has terms \(K^n\oplus K^{n+1}\oplus K^n\) and differential

\[
d(x,y,z)=(dx+y,\,-dy,\,dz-y).
\]

A direct computation gives \(d^2=0\). The maps \(i_0(x)=(x,0,0)\), \(i_1(z)=(0,0,z)\) and \(p(x,y,z)=x+z\) are chain maps with \(pi_0=pi_1=1\). With \(h(x,y,z)=(0,-z,0)\) one finds \(dh+hd=1-i_0p\), so \(p\) is a homotopy equivalence and in particular a quasi-isomorphism. If \(s\) is a homotopy from \(g\) to \(f\), that is \(f-g=ds+sd\), then

\[
H(x,y,z)=fx+sy+gz
\]

is a chain map \(\mathrm{Cyl}(K)\to L\) with \(Hi_0=f\) and \(Hi_1=g\). Since \(F(p)\) is invertible and \(F(p)F(i_0)=F(p)F(i_1)\), we get \(F(i_0)=F(i_1)\) and \(F(f)=F(g)\). So \(F\) factors uniquely through \(K(\mathcal A)\), and the factor inverts quasi-isomorphisms; Theorem 4.2 of *Complexes, cones and localization* factors it uniquely through \(Q\). This proves property 1. For property 2, \(\pi\) is the identity on objects, and every morphism of \(D(\mathcal A)\) is \(\pi(f)\pi(s)^{-1}\) with \(s\) a quasi-isomorphism; the argument in the proof of Theorem 3.2 applies.

## Sources

- [PS] A. Grothendieck, *Pursuing Stacks (À la poursuite des champs). First episode: the modelizing story* (typescript, 1983), §69; public-domain edition by the scrivener (2015), extended by M. Carmona with U. Buchholtz. arXiv:2111.01000. https://arxiv.org/abs/2111.01000
- [Gr] M. Groth, *Derivators, pointed derivators and stable derivators*, Algebraic & Geometric Topology 13 (2013), 313–374; arXiv:1112.3840. https://arxiv.org/abs/1112.3840
- Programme lesson [*Complexes, cones and localization*](course:derived-categories-and-sheaf-operations/complexes-cones-and-localization): complexes, cones, the derived category and its triangulated structure.

The cone example of Section 2 is a concrete instance of the failure of faithfulness of underlying diagram functors discussed in the introduction of [Gr].
