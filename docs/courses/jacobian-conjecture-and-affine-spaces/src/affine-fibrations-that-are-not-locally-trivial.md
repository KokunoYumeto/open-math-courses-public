# Affine-space fibrations that are not locally trivial

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(R\) be a ring. An **\(\mathbb A^n\)-fibration** over \(R\) is a finitely generated flat \(R\)-algebra \(B\) such that \(B\otimes_R\kappa(\mathfrak p)\) is a polynomial ring in \(n\) variables over the residue field \(\kappa(\mathfrak p)\) for every prime \(\mathfrak p\) of \(R\). Geometrically, \(\operatorname{Spec}B\to\operatorname{Spec}R\) is flat and each of its fibres is affine \(n\)-space over the residue field of its point. Locally trivial bundles with fibre \(\mathbb A^n\) have these properties. A question going back to Dolgachev and Weisfeiler asks for a converse, in the form recorded in [Gupta-survey, Question 3]: if \(R\) is a regular noetherian domain, is every \(\mathbb A^n\)-fibration over \(R\) the symmetric algebra of a projective \(R\)-module, and in particular a polynomial ring when \(R\) is a regular local ring? For \(n=1\) the answer is yes, and for \(n=2\) and a discrete valuation ring containing \(\mathbb Q\) it is yes by a theorem of Sathaye [Gupta-survey, Section 4].

This lesson shows that the answer is no for \(n=3\). The polynomial \(H\) of [A fourfold whose cylinder is affine space](a-fourfold-whose-cylinder-is-affine-space.md) makes the polynomial ring in five variables a smooth \(\mathbb A^3\)-fibration over the plane, through the map \((p,H)\), and makes the hypersurface \(H=0\) a smooth \(\mathbb A^3\)-fibration over the line \(\operatorname{Spec}k[p]\). Neither fibration is locally trivial, and the second remains nontrivial over the discrete valuation ring \(k[p]_{(p)}\). The examples are from [OpenAI-cancellation, Section 7].

We use from this course Sections 2–4 of [A fourfold whose cylinder is affine space](a-fourfold-whose-cylinder-is-affine-space.md), Theorem 9.1 of [Cancellation fails in dimension four](cancellation-fails-in-dimension-four.md#9-conclusion) and Theorem 3.1 of [A stable coordinate in five variables](a-stable-coordinate-in-five-variables.md#3-the-theorem). From the course on projective modules we use Lemmas 1.2, 1.3 and Corollary 2.2 of [Locally polynomial algebras](course:projective-modules-and-locally-polynomial-algebras/locally-polynomial-algebras#2-the-theorem), which rests on the Quillen–Suslin theorem, and Lemma 1.1 of [Horrocks' theorem and the Quillen–Suslin theorem](course:projective-modules-and-locally-polynomial-algebras/horrocks-and-quillen-suslin#1-projective-modules). From commutative algebra we use the definitions of formally smooth and smooth ring maps in Sections 1 and 4 of [Formally smooth, unramified and étale ring maps](course:AG-CA/formally-smooth-unramified-and-etale-ring-maps#4-standard-smooth-presentations); Propositions 3.1, 3.2 and Theorem 3.3 of [Tor and flat modules](course:AG-CA/tor-and-flat-modules#3-stability-and-localization); Grothendieck's slicing lemma, Theorem 5.2 of [Faithful flatness and the local criterion for flatness](course:AG-CA/faithful-flatness-and-the-local-criterion-for-flatness#5-lifting-a-regular-equation-from-the-fibre); and Theorem 5.1 (local detection) of [Localization, local properties and support](course:AG-CA/localization-local-properties-and-support#5-recovering-global-information). The field \(k\) has characteristic zero.

Basic references are [OpenAI-cancellation] and [Gupta-survey].

## 1. Fibrations and locally trivial bundles

An \(R\)-algebra \(B\) is a **Zariski-locally trivial \(\mathbb A^n\)-bundle** if there are \(g_1,\ldots,g_m\in R\) generating the unit ideal and isomorphisms of \(R_{g_i}\)-algebras \(B_{g_i}\cong R_{g_i}[X_1,\ldots,X_n]\). The principal open sets form a basis of the topology of the quasi-compact space \(\operatorname{Spec}R\), so this says that \(\operatorname{Spec}B\) is a product with \(\mathbb A^n\) over each member of an open covering of \(\operatorname{Spec}R\). A finitely generated Zariski-locally trivial \(\mathbb A^n\)-bundle is an \(\mathbb A^n\)-fibration, and it is **locally polynomial**: \(B_{\mathfrak m}\cong R_{\mathfrak m}[X_1,\ldots,X_n]\) for every maximal ideal \(\mathfrak m\) of \(R\) (Exercise 6.1).

Over a polynomial ring over a field, locally polynomial algebras are polynomial rings: by Corollary 2.2 of [Locally polynomial algebras](course:projective-modules-and-locally-polynomial-algebras/locally-polynomial-algebras#2-the-theorem), a finitely presented algebra over \(F[y_1,\ldots,y_r]\), \(F\) a field, which is locally polynomial in \(n\) variables is a polynomial ring in \(n\) variables. Finitely generated algebras over a noetherian ring are finitely presented. So over such a base, an \(\mathbb A^n\)-fibration that is not a polynomial ring fails to be a polynomial ring after localizing at some maximal ideal, and it is not locally trivial.

## 2. Smoothness and flatness of a hypersurface

**Lemma 2.1.** Let \(R\) be a ring, \(f\in R[X_1,\ldots,X_n]\) and \(S=R[X_1,\ldots,X_n]/(f)\). If the images of \(\partial f/\partial X_1,\ldots,\partial f/\partial X_n\) generate the unit ideal of \(S\), then \(S\) is a smooth \(R\)-algebra.

**Proof.** The algebra \(S\) is finitely presented. Choose \(c_1,\ldots,c_n,h\in R[X]\) with \(\sum_jc_j\,\partial f/\partial X_j=1+fh\). Let \(A\) be an \(R\)-algebra, \(J\subseteq A\) an ideal with \(J^2=0\), and \(\bar u\colon S\to A/J\) a homomorphism of \(R\)-algebras. Choose \(a_1,\ldots,a_n\in A\) lifting the images \(\bar u(X_j)\). Then \(f(a)\in J\), and \(e=\sum_jc_j(a)\,(\partial f/\partial X_j)(a)=1+f(a)h(a)\) is a unit, since \(f(a)h(a)\in J\) has square zero. Put \(\varepsilon_j=-c_j(a)\,e^{-1}f(a)\in J\). In \(R[X,Y]\), \(f(X+Y)-f(X)-\sum_j(\partial f/\partial X_j)(X)\,Y_j\) lies in the ideal generated by the products \(Y_iY_j\); as \(J^2=0\),
\[
f(a+\varepsilon)=f(a)+\sum_j(\partial f/\partial X_j)(a)\,\varepsilon_j=f(a)-e^{-1}f(a)\,e=0 .
\]
So \(X_j\mapsto a_j+\varepsilon_j\) defines a homomorphism of \(R\)-algebras \(S\to A\) lifting \(\bar u\). Hence \(S\) is formally smooth over \(R\), and smooth. \(\square\)

**Lemma 2.2.** Let \(R\) be a noetherian ring and \(f\in R[X_1,\ldots,X_n]\) such that for every prime \(\mathfrak p\) of \(R\) the image of \(f\) in \(\kappa(\mathfrak p)[X_1,\ldots,X_n]\) is nonzero. Then \(S=R[X_1,\ldots,X_n]/(f)\) is flat over \(R\).

**Proof.** Let \(\mathfrak Q\) be a prime of \(S\), \(\mathfrak q\) its preimage in \(R[X]\) and \(\mathfrak p=\mathfrak q\cap R\). The free \(R\)-module \(R[X]\) is flat, so by Propositions 3.1, 3.2 and Theorem 3.3 of [Tor and flat modules](course:AG-CA/tor-and-flat-modules#3-stability-and-localization) the local homomorphism \(R_{\mathfrak p}\to R[X]_{\mathfrak q}\) of noetherian local rings is flat. Its closed fibre \(R[X]_{\mathfrak q}/\mathfrak pR[X]_{\mathfrak q}\) is a localization of the domain \((R/\mathfrak p)[X]\subseteq\kappa(\mathfrak p)[X]\) at a prime ideal. The image of \(f\) in it is nonzero, hence a nonzerodivisor, and \(f\) lies in the maximal ideal \(\mathfrak qR[X]_{\mathfrak q}\). By the slicing lemma, \(S_{\mathfrak Q}=R[X]_{\mathfrak q}/(f)\) is flat over \(R_{\mathfrak p}\).

Let \(N'\to N\) be an injective map of \(R\)-modules and \(K\) the kernel of \(N'\otimes_RS\to N\otimes_RS\), an \(S\)-module. For a prime \(\mathfrak Q\) of \(S\), with \(\mathfrak p\) as above, localization is exact and \((N'\otimes_RS)_{\mathfrak Q}=N'_{\mathfrak p}\otimes_{R_{\mathfrak p}}S_{\mathfrak Q}\), so \(K_{\mathfrak Q}\) is the kernel of \(N'_{\mathfrak p}\otimes_{R_{\mathfrak p}}S_{\mathfrak Q}\to N_{\mathfrak p}\otimes_{R_{\mathfrak p}}S_{\mathfrak Q}\), which is zero. By local detection \(K=0\). So \(S\) is flat over \(R\). \(\square\)

## 3. A residual coordinate

Recall from [A fourfold whose cylinder is affine space](a-fourfold-whose-cylinder-is-affine-space.md) that \(P=k[p,s,u,F,J]\),
\[
x=s^2+u^3+p^2F,\qquad y=s+x(x-u^3),\qquad z=sx+p^2J,\qquad H=x^2F-(1+2sx)J-p^2J^2-pu,
\]
and \(A=P/(H)\). We regard \(P\) as the polynomial ring in \(s,u,F,J\) over \(k[p]\). For a prime \(\mathfrak p\) of \(k[p]\) let \(H_{\mathfrak p}\) be the image of \(H\) in \(P\otimes_{k[p]}\kappa(\mathfrak p)=\kappa(\mathfrak p)[s,u,F,J]\).

**Proposition 3.1.** For every prime \(\mathfrak p\) of \(k[p]\) there are \(G_1,G_2,G_3\in\kappa(\mathfrak p)[s,u,F,J]\) such that \(H_{\mathfrak p},G_1,G_2,G_3\) are algebraically independent over \(\kappa(\mathfrak p)\) and
\[
\kappa(\mathfrak p)[s,u,F,J]=\kappa(\mathfrak p)[H_{\mathfrak p},G_1,G_2,G_3].
\]

**Proof.** If \(p\notin\mathfrak p\), then \(\kappa(\mathfrak p)\) is a \(k[p,p^{-1}]\)-algebra. By the proof of Proposition 2.2 of the cylinder lesson, \(P[p^{-1}]=k[p,p^{-1}][x,y,z,H]\) with \(x,y,z,H\) algebraically independent over \(k[p,p^{-1}]\). Tensoring with \(\kappa(\mathfrak p)\) over \(k[p,p^{-1}]\) gives the claim, with \(G_1,G_2,G_3\) the images of \(x,y,z\).

If \(p\in\mathfrak p\), then \(\mathfrak p=(p)\) and \(\kappa(\mathfrak p)=k\). By (4.3) of the cylinder lesson \(H\equiv L\) modulo \(p\), and by (4.1) and (4.2) there, \(P/pP=k[s,u,M,L]\) with \(s,u,M,L\) algebraically independent (Exercise 6.3 there). Take \(G_1,G_2,G_3\) to be the images of \(s,u,M\). \(\square\)

So \(H\) is a **residual coordinate** of \(P\) over \(k[p]\): it becomes a coordinate over every residue field of \(k[p]\).

**Lemma 3.2.** The partial derivatives \(\partial H/\partial s\), \(\partial H/\partial u\), \(\partial H/\partial F\), \(\partial H/\partial J\) generate the unit ideal of \(P\).

**Proof.** Let \(\mathfrak j\) be the ideal they generate. The derivation \(\Delta\) of Lemma 3.1 of the cylinder lesson is a \(k[p]\)-derivation of \(P\) with \(\Delta(H)=p^3\). By the chain rule,
\[
p^3=\Delta(H)=\Delta(s)\frac{\partial H}{\partial s}+\Delta(u)\frac{\partial H}{\partial u}+\Delta(F)\frac{\partial H}{\partial F}+\Delta(J)\frac{\partial H}{\partial J}\in\mathfrak j .
\]
Differentiation in \(s,u,F,J\) commutes with reduction modulo \(p\). Modulo \(p\), \(H\equiv x_0^2F-(1+2sx_0)J\) with \(x_0=s^2+u^3\), so \(\partial H/\partial F\equiv x_0^2\), \(\partial H/\partial J\equiv-(1+2sx_0)\), and
\[
4s^2\frac{\partial H}{\partial F}-(1-2sx_0)\frac{\partial H}{\partial J}\equiv4s^2x_0^2+(1-2sx_0)(1+2sx_0)=1 ,
\]
the determinant of the change of variables (4.1) of the cylinder lesson. So \(1+pc\in\mathfrak j\) for some \(c\in P\), and \(1=(1+pc)(1-pc+p^2c^2)-c^3p^3\in\mathfrak j\). \(\square\)

## 4. Two smooth A3-fibrations

**Theorem 4.1.** Make \(P\) an algebra over \(k[p,q]\) through \(q\mapsto H\).

1. \(P\) is a smooth \(\mathbb A^3\)-fibration over \(k[p,q]\): it is a flat and smooth \(k[p,q]\)-algebra, and for every prime \(\mathfrak y\) of \(k[p,q]\) the ring \(P\otimes_{k[p,q]}\kappa(\mathfrak y)\) is a polynomial ring in three variables over \(\kappa(\mathfrak y)\).
2. \(A\) is a smooth \(\mathbb A^3\)-fibration over \(k[p]\).

**Proof.** (1) As a \(k[p,q]\)-algebra, \(P=k[p,q][s,u,F,J]/(q-H)\). Let \(\mathfrak y\) be a prime of \(k[p,q]\), \(\kappa=\kappa(\mathfrak y)\), \(b\) the image of \(q\) in \(\kappa\), and \(\mathfrak p=\mathfrak y\cap k[p]\). The map \(k[p]/\mathfrak p\to\kappa\) is injective, so \(k[p]\to\kappa\) factors through the field \(\kappa(\mathfrak p)\). The isomorphism \(\kappa(\mathfrak p)[T_0,\ldots,T_3]\to\kappa(\mathfrak p)[s,u,F,J]\), \(T_0\mapsto H_{\mathfrak p}\), \(T_i\mapsto G_i\), of Proposition 3.1 stays an isomorphism after tensoring with \(\kappa\). So \(\kappa[s,u,F,J]=\kappa[\bar H,\bar G_1,\bar G_2,\bar G_3]\) with algebraically independent generators, where \(\bar H\) is the image of \(H\). Hence
\[
P\otimes_{k[p,q]}\kappa=\kappa[s,u,F,J]/(\bar H-b)\cong\kappa[\bar G_1,\bar G_2,\bar G_3],
\]
a polynomial ring in three variables. In particular the image \(b-\bar H\) of \(q-H\) in \(\kappa[s,u,F,J]\) is nonzero, so \(P\) is flat over \(k[p,q]\) by Lemma 2.2. It is finitely generated, and it is smooth by Lemmas 2.1 and 3.2, because \(\partial(q-H)/\partial v=-\partial H/\partial v\) for \(v=s,u,F,J\).

(2) As a \(k[p]\)-algebra, \(A=k[p][s,u,F,J]/(H)\). For a prime \(\mathfrak p\) of \(k[p]\), Proposition 3.1 gives \(A\otimes_{k[p]}\kappa(\mathfrak p)=\kappa(\mathfrak p)[s,u,F,J]/(H_{\mathfrak p})\cong\kappa(\mathfrak p)[G_1,G_2,G_3]\), and \(H_{\mathfrak p}\ne0\). So \(A\) is flat by Lemma 2.2, and smooth by Lemmas 2.1 and 3.2, the partial derivatives of \(H\) generating the unit ideal of \(A\) because they do in \(P\). \(\square\)

## 5. Neither fibration is locally trivial

**Theorem 5.1.**

1. For every maximal ideal \(\mathfrak m\ne(p)\) of \(k[p]\), \(A_{\mathfrak m}\) is a polynomial ring in three variables over \(k[p]_{\mathfrak m}\). But \(A_{(p)}=A\otimes_{k[p]}k[p]_{(p)}\) is not a polynomial ring in three variables over the discrete valuation ring \(k[p]_{(p)}\).
2. \(P\otimes_{k[p,q]}k[p,q]_{(p,q)}\) is not a polynomial ring in three variables over \(k[p,q]_{(p,q)}\).

**Proof.** (1) If \(p\notin\mathfrak m\), then \(p\) is a unit of \(k[p]_{\mathfrak m}\), and Proposition 2.2 of the cylinder lesson gives \(A_{\mathfrak m}=A[p^{-1}]\otimes_{k[p,p^{-1}]}k[p]_{\mathfrak m}=k[p]_{\mathfrak m}[x,y,z]\). Suppose that \(A_{(p)}\) were a polynomial ring in three variables over \(k[p]_{(p)}\). Then the finitely presented \(k[p]\)-algebra \(A\) would be locally polynomial in three variables, and Corollary 2.2 of [Locally polynomial algebras](course:projective-modules-and-locally-polynomial-algebras/locally-polynomial-algebras#2-the-theorem) would give \(A\cong k[p][X_1,X_2,X_3]\), a polynomial ring in four variables over \(k\). This contradicts Theorem 9.1 of [Cancellation fails in dimension four](cancellation-fails-in-dimension-four.md#9-conclusion).

(2) Let \(R=k[p,q]_{(p,q)}\). Reduction modulo \(q\) turns \(R\) into \(k[p]_{(p)}\), and, since \(q\) maps to \(H\) and \(P/HP=A\), it turns \(P\otimes_{k[p,q]}R\) into \(A\otimes_{k[p]}k[p]_{(p)}=A_{(p)}\). An isomorphism of \(R\)-algebras \(P\otimes_{k[p,q]}R\cong R[X_1,X_2,X_3]\) would reduce to an isomorphism of \(k[p]_{(p)}\)-algebras \(A_{(p)}\cong k[p]_{(p)}[X_1,X_2,X_3]\), contrary to (1). \(\square\)

**Corollary 5.2.** Neither \((p,H)\colon\mathbb A^5\to\mathbb A^2\) nor \(p\colon\operatorname{Spec}A\to\mathbb A^1\) is a Zariski-locally trivial \(\mathbb A^3\)-bundle. None of the \(\mathbb A^3\)-fibrations \(P\) over \(k[p,q]\), \(A\) over \(k[p]\) and \(A_{(p)}\) over \(k[p]_{(p)}\) is isomorphic to the symmetric algebra of a projective module. So the question recalled at the beginning has a negative answer for \(n=3\), over the regular local ring \(k[p]_{(p)}\) and over the polynomial rings \(k[p]\) and \(k[p,q]\).

**Proof.** \(A_{(p)}\) is an \(\mathbb A^3\)-fibration over \(k[p]_{(p)}\): it is flat by Proposition 3.2 of [Tor and flat modules](course:AG-CA/tor-and-flat-modules#3-stability-and-localization), and its fibre rings over the two primes of \(k[p]_{(p)}\) are fibre rings of \(A\). A Zariski-locally trivial \(\mathbb A^3\)-bundle is locally polynomial (Exercise 6.1), which Theorem 5.1 excludes at the maximal ideals \((p,q)\) and \((p)\).

Let \(B\) be one of the three algebras over its base \(R_0\), and suppose \(B\cong S(Q)\) with \(Q\) a projective \(R_0\)-module. By Lemma 1.3 of [Locally polynomial algebras](course:projective-modules-and-locally-polynomial-algebras/locally-polynomial-algebras#1-modules-over-two-localizations), \(Q\) is finitely presented, so for a maximal ideal \(\mathfrak m\) of \(R_0\) the module \(Q_{\mathfrak m}\) is free, by Lemma 1.1 of [Horrocks' theorem and the Quillen–Suslin theorem](course:projective-modules-and-locally-polynomial-algebras/horrocks-and-quillen-suslin#1-projective-modules). Its rank is three: \(S(Q\otimes\kappa(\mathfrak m))\cong B\otimes\kappa(\mathfrak m)\) is a polynomial ring in three variables, so \(Q\otimes\kappa(\mathfrak m)\cong\kappa(\mathfrak m)^3\) by Lemma 1.2 of [Locally polynomial algebras](course:projective-modules-and-locally-polynomial-algebras/locally-polynomial-algebras#1-modules-over-two-localizations). Hence \(B_{\mathfrak m}\cong S(R_{0,\mathfrak m}^3)\) is a polynomial ring in three variables over \(R_{0,\mathfrak m}\) at every maximal ideal \(\mathfrak m\), contrary to Theorem 5.1 at \(\mathfrak m=(p,q)\), respectively \((p)\). \(\square\)

## 6. Exercises

**Exercise 6.1.** Let \(B\) be a finitely generated \(R\)-algebra which is a Zariski-locally trivial \(\mathbb A^n\)-bundle. Show that \(B\) is an \(\mathbb A^n\)-fibration and that \(B_{\mathfrak m}\cong R_{\mathfrak m}[X_1,\ldots,X_n]\) for every maximal ideal \(\mathfrak m\) of \(R\).

**Exercise 6.2.** Show that \(P[p^{-1}]\cong k[p,p^{-1},q][X_1,X_2,X_3]\) as \(k[p,p^{-1},q]\)-algebras, so that \((p,H)\) is a trivial bundle over the open set \(p\ne0\) of \(\mathbb A^2\).

**Exercise 6.3.** Show that \(A[w]\cong k[p][X_1,X_2,X_3,X_4]\) as \(k[p]\)-algebras. Deduce that over the discrete valuation ring \(V=k[p]_{(p)}\), the algebra \(A_V=A\otimes_{k[p]}V\) satisfies \(A_V[w]\cong V[X_1,\ldots,X_4]\), although \(A_V\) is not a polynomial ring over \(V\).

**Exercise 6.4.** For \(c\in k\), show that \(P/(H-c)\) is an \(\mathbb A^3\)-fibration over \(k[p]\) and that \((P/(H-c))[w]\) is a polynomial ring in five variables over \(k\).

## 7. Solutions

**6.1.** For a maximal ideal \(\mathfrak m\), choose \(i\) with \(g_i\notin\mathfrak m\). Then \(B_{\mathfrak m}=(B_{g_i})_{\mathfrak m}\cong R_{\mathfrak m}[X_1,\ldots,X_n]\), a free \(R_{\mathfrak m}\)-module, so \(B\) is flat by Theorem 3.3 of [Tor and flat modules](course:AG-CA/tor-and-flat-modules#3-stability-and-localization). For a prime \(\mathfrak p\), choose \(i\) with \(g_i\notin\mathfrak p\). Then \(\kappa(\mathfrak p)\) is an \(R_{g_i}\)-algebra, and \(B\otimes_R\kappa(\mathfrak p)=B_{g_i}\otimes_{R_{g_i}}\kappa(\mathfrak p)\cong\kappa(\mathfrak p)[X_1,\ldots,X_n]\).

**6.2.** By the proof of Proposition 2.2 of the cylinder lesson, \(P[p^{-1}]=k[p,p^{-1}][x,y,z,H]\) with \(x,y,z,H\) algebraically independent over \(k[p,p^{-1}]\). Since \(q\) maps to \(H\), this is \(k[p,p^{-1},q][x,y,z]\).

**6.3.** The automorphism \(\Phi=\exp(w\Delta)\) of the cylinder lesson fixes \(p\) and \(w\) and induces an isomorphism of \(k[p]\)-algebras \(A[w]\cong T\), by (3.2) there, and \(T=k[p][s,u,M,e]\) with \(s,u,M,e\) algebraically independent over \(k[p]\), by Theorem 4.1 there. Tensoring with \(V\) gives \(A_V[w]\cong V[s,u,M,e]\). If \(A_V\) were a polynomial ring over \(V\), it would have three variables, since \(A_V\otimes_Vk=A/pA\) is a polynomial ring in three variables over \(k\); this is excluded by Theorem 5.1.

**6.4.** \(P/(H-c)=P\otimes_{k[p,q]}k[p,q]/(q-c)\), and \(k[p,q]/(q-c)=k[p]\). Finite generation and flatness are preserved by base change (Proposition 3.2 of [Tor and flat modules](course:AG-CA/tor-and-flat-modules#3-stability-and-localization)). For a prime \(\mathfrak p\) of \(k[p]\) with preimage \(\mathfrak y\) in \(k[p,q]\), \(\kappa(\mathfrak y)=\kappa(\mathfrak p)\) and the fibre ring \((P/(H-c))\otimes_{k[p]}\kappa(\mathfrak p)=P\otimes_{k[p,q]}\kappa(\mathfrak y)\) is a polynomial ring in three variables by Theorem 4.1. By Theorem 3.1 of [A stable coordinate in five variables](a-stable-coordinate-in-five-variables.md#3-the-theorem), \(P[w]=k[H,f_2,\ldots,f_6]\) with \(H,f_2,\ldots,f_6\) algebraically independent, so \(P[w]/(H-c)\cong k[\bar f_2,\ldots,\bar f_6]\) by Exercise 4.3 there; and \(P[w]/(H-c)=(P/(H-c))[w]\).

## References

- [OpenAI-cancellation] OpenAI, An explicit failure of complex affine-space cancellation, preprint, 23 September 2026. https://github.com/openai/math/blob/main/preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/paper.pdf
- [Gupta-survey] N. Gupta, The Zariski cancellation problem and related problems in affine algebraic geometry, Proceedings of the International Congress of Mathematicians 2022, vol. 3, EMS Press, 2023, 1578–1598. https://doi.org/10.4171/ICM2022/151
