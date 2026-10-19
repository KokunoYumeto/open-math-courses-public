# Pointed and stable derivators

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

*Pursuing Stacks* (§69) observes that for the two shapes of a span and a cospan, the adjoints of restriction give amalgamated sums and fibre products, "and hence also" cofibres and fibres, and that the two Dold–Puppe sequences follow formally "with a suitable extra axiom" for exactness. This lesson supplies that axiom. A derivator is *pointed* when its underlying category has a zero object; then homotopy pushouts along zero objects give cofibres and suspensions, and homotopy pullbacks give fibres and loops. It is *stable* when a square is a homotopy pushout exactly when it is a homotopy pullback. The main theorem shows that the derivator of a ring is stable, by reducing both conditions to the acyclicity of one total complex.

**Prerequisites.** The lessons [*Homotopy exact squares*](homotopy-exact-squares.md) (Lemma 3.1, Proposition 3.3) and [*The derivator of a ring*](the-derivator-of-a-ring.md) (Sections 1–3). From *Complexes, cones and localization*: the cone of a chain map and Lemma 1.2; Proposition 5.2 (a short exact sequence of complexes gives a distinguished triangle; its proof shows that the map from the cone of an injection to the quotient is a quasi-isomorphism).

## 1. Pointed derivators

**Definition 1.1.** A derivator \(\mathbb D\) is *pointed* if \(\mathbb D(e)\) has a zero object, that is, an object that is both initial and terminal.

**Proposition 1.2.** Let \(\mathbb D\) be pointed and \(u:J\to K\) a functor. Then \(\mathbb D(K)\) has a zero object, and \(u^*\), \(u_!\), \(u_*\) send zero objects to zero objects.

**Proof.** By Proposition 5.1 of the lesson on Kan extensions, \(\mathbb D(K)\) has an initial object \(\emptyset\) and a terminal object \(*\). Each evaluation \(k^*\) has both adjoints, so it preserves initial and terminal objects; hence each component of the unique morphism \(\emptyset\to*\) is a morphism from a zero object to a zero object of \(\mathbb D(e)\), an isomorphism. By (Der2), \(\emptyset\to*\) is an isomorphism, and \(\mathbb D(K)\) has a zero object. Each of \(u^*,u_!,u_*\) is a left adjoint or a right adjoint, so it preserves initial or terminal objects, which are the zero objects. \(\square\)

**Proposition 1.3 (extension by zero).** Let \(\mathbb D\) be pointed. If \(u:J\to K\) is a cosieve, \(u_!\) is fully faithful with essential image the objects \(X\) with \(X_k\cong0\) for all \(k\) outside \(u(J)\). If \(u\) is a sieve, the same holds for \(u_*\).

**Proof.** Proposition 3.3 of the lesson on homotopy exact squares, with initial and terminal objects equal to zero. \(\square\)

The represented derivator of a category with a zero object (pointed sets, abelian groups) is pointed, and the derivator \(\mathbb D_R\) of a ring is pointed, since the zero complex is a zero object of \(D(R)\).

## 2. Cocartesian and cartesian squares

Let \(\square=[1]\times[1]\), with objects \((0,0)\), \((1,0)\), \((0,1)\), \((1,1)\), and let

\[
i_\ulcorner:{\ulcorner}\to\square,
\qquad
i_\lrcorner:{\lrcorner}\to\square
\]

be the full subcategories without \((1,1)\) and without \((0,0)\) respectively. The first is a sieve and the second a cosieve, and both are fully faithful.

**Definition 2.1.** An object \(X\) of \(\mathbb D(\square)\) is *cocartesian* if it lies in the essential image of \(i_{\ulcorner!}\), and *cartesian* if it lies in the essential image of \(i_{\lrcorner*}\).

**Lemma 2.2.** \(X\) is cocartesian if and only if the counit \(i_{\ulcorner!}i_\ulcorner^*X\to X\) is invertible at \((1,1)\), and the value of \(i_{\ulcorner!}Y\) at \((1,1)\) is the homotopy colimit of \(Y\) over \(\ulcorner\). Dually, \(X\) is cartesian if and only if the unit \(X\to i_{\lrcorner*}i_\lrcorner^*X\) is invertible at \((0,0)\), and the value of \(i_{\lrcorner*}Z\) at \((0,0)\) is the homotopy limit of \(Z\) over \(\lrcorner\).

**Proof.** The first statement is Lemma 3.1 of the lesson on homotopy exact squares, since \((1,1)\) is the only object outside \(\ulcorner\). Every object of \(\ulcorner\) has exactly one morphism to \((1,1)\) in \(\square\), so \(\ulcorner_{/(1,1)}\cong\ulcorner\), and (Der4) gives the second. The dual statements are proved dually. \(\square\)

So a square is cocartesian when its corner \(X_{1,1}\) is the homotopy pushout of the rest; this is the derivator form of a pushout square.

## 3. Suspension, loops, cone and fibre

Let \(\mathbb D\) be pointed. The object \((0,0)\) is a sieve in \(\ulcorner\), and \((1,1)\) is a cosieve in \(\lrcorner\). Write \(\mathcal M\subset\mathbb D(\square)\), \(\mathcal M^\ulcorner\subset\mathbb D(\ulcorner)\) and \(\mathcal M^\lrcorner\subset\mathbb D(\lrcorner)\) for the full subcategories of objects vanishing at \((1,0)\) and \((0,1)\).

**Definition 3.1.** The *suspension* and the *loop functor* are

\[
\Sigma=(1,1)^*\,i_{\ulcorner!}\,(0,0)_*,
\]
\[
\Omega=(0,0)^*\,i_{\lrcorner*}\,(1,1)_!,
\]

functors \(\mathbb D(e)\to\mathbb D(e)\).

For \(x\) in \(\mathbb D(e)\), the object \((0,0)_*x\) of \(\mathbb D(\ulcorner)\) is the span \(0\leftarrow x\to0\) (Proposition 1.3), and \(\Sigma x\) is its homotopy pushout. For topological spaces this is the classical suspension: two cones glued along their common base.

**Proposition 3.2.** \(\Sigma\) is left adjoint to \(\Omega\).

**Proof.** By Proposition 1.3, \((0,0)_*\) is an equivalence from \(\mathbb D(e)\) onto \(\mathcal M^\ulcorner\) with inverse \((0,0)^*\), and \((1,1)_!\) is an equivalence onto \(\mathcal M^\lrcorner\) with inverse \((1,1)^*\). The functors \(i_{\ulcorner!}\) and \(i_\ulcorner^*\) restrict to \(\mathcal M^\ulcorner\) and \(\mathcal M\), since restriction and extension along \(i_\ulcorner\) keep the values at \((1,0)\) and \((0,1)\) (the unit of \(i_{\ulcorner!}\dashv i_\ulcorner^*\) is invertible, Proposition 6.1 of the lesson on Kan extensions); likewise for \(i_\lrcorner^*\dashv i_{\lrcorner*}\). Hence

\[
\Sigma\cong(1,1)^*\,i_\lrcorner^*\,i_{\ulcorner!}\,(0,0)_*,
\]
\[
\Omega\cong(0,0)^*\,i_\ulcorner^*\,i_{\lrcorner*}\,(1,1)_!,
\]

and these are composites of the four adjunctions \((0,0)_*\dashv(0,0)^*\), \(i_{\ulcorner!}\dashv i_\ulcorner^*\), \(i_\lrcorner^*\dashv i_{\lrcorner*}\) and \((1,1)^*\dashv(1,1)_!\), the outer two being equivalences restricted to \(\mathcal M^\ulcorner\) and \(\mathcal M^\lrcorner\). \(\square\)

In the same way, extension by zero along the arrow \([1]\to\ulcorner\) onto \((0,0)\to(1,0)\) and a homotopy pushout produce, for an object \(f\) of \(\mathbb D([1])\), a square

\[
\begin{array}{ccc}
X_0&\xrightarrow{f}&X_1\\
\downarrow&&\downarrow\\
0&\longrightarrow&\operatorname{cof}(f)
\end{array}
\]

whose corner is the *cofibre* of \(f\); the *fibre* is defined dually. A pointed derivator thus has functorial cofibres on \(\mathbb D([1])\), which the first lesson showed to be impossible on \(\mathbb D(e)^{[1]}\) in general.

## 4. Stable derivators

**Definition 4.1.** A pointed derivator is *stable* if an object of \(\mathbb D(\square)\) is cocartesian if and only if it is cartesian.

**Proposition 4.2.** In a stable derivator, \(\Sigma\) and \(\Omega\) are inverse equivalences.

**Proof.** In the factorization of Proposition 3.2, \(i_{\ulcorner!}\) is an equivalence from \(\mathcal M^\ulcorner\) onto the cocartesian objects of \(\mathcal M\), and \(i_{\lrcorner*}\) an equivalence from \(\mathcal M^\lrcorner\) onto the cartesian ones, with inverses the restrictions (Proposition 6.1 of the lesson on Kan extensions). In a stable derivator these two subcategories of \(\mathcal M\) coincide. So \(\Sigma\) is a composite of four equivalences, and its right adjoint \(\Omega\) is a quasi-inverse. \(\square\)

## 5. The derivator of a ring is stable

For a commutative square \(S\) of complexes

\[
\begin{array}{ccc}
S_{00}&\xrightarrow{f}&S_{10}\\
{\scriptstyle g}\downarrow&&\downarrow{\scriptstyle h}\\
S_{01}&\xrightarrow{k}&S_{11}
\end{array}
\]

consider the chain maps

\[
\varphi=(f,-g):S_{00}\to S_{10}\oplus S_{01},
\]
\[
\kappa:C(\varphi)\to S_{11},\quad\kappa(a,b,x)=ha+kb,
\]

where \(C(\varphi)^n=S_{10}^n\oplus S_{01}^n\oplus S_{00}^{n+1}\). The map \(\kappa\) is a chain map because \(hf=kg\). Define the *total complex* \(\operatorname{Tot}(S)=C(\kappa)\): its terms are

\[
S_{11}^n\oplus S_{10}^{n+1}\oplus S_{01}^{n+1}\oplus S_{00}^{n+2},
\]

with differential

\[
\begin{aligned}
d(s,a,b,x)=\bigl(&ds+ha+kb,\;-da-fx,\\
&-db+gx,\;dx\bigr).
\end{aligned}
\]

**Lemma 5.1.** \(\operatorname{Tot}\) sends levelwise quasi-isomorphisms of squares to quasi-isomorphisms. Moreover, with

\[
\psi=(h,-k):S_{10}\oplus S_{01}\to S_{11},
\]
\[
\begin{gathered}
\lambda:S_{00}\to C(\psi)[-1],\\
\lambda(x)=(0,fx,gx),
\end{gathered}
\]

the map \((s,a,b,x)\mapsto(s,a,-b,x)\) is an isomorphism of complexes \(\operatorname{Tot}(S)\to C(\lambda)[1]\).

**Proof.** A morphism of squares induces morphisms of the cones \(C(\varphi)\) and \(C(\kappa)\), compatible with the degreewise split sequences \(0\to S_{10}\oplus S_{01}\to C(\varphi)\to S_{00}[1]\to0\) and \(0\to S_{11}\to C(\kappa)\to C(\varphi)[1]\to0\). If it is a levelwise quasi-isomorphism, the long exact sequences (Lemma 1.2 of *Complexes, cones and localization*) and the Five Lemma show first that \(C(\varphi)\) and then that \(C(\kappa)\) changes by a quasi-isomorphism.

For the second statement, \(C(\psi)[-1]\) has terms \(S_{11}^{n-1}\oplus S_{10}^n\oplus S_{01}^n\) and differential \((s,a,b)\mapsto(-ds-ha+kb,\,da,\,db)\); \(\lambda\) is a chain map because \(-hf+kg=0\). Then \(C(\lambda)[1]\) has the terms of \(\operatorname{Tot}(S)\) and differential

\[
\begin{aligned}
(s,a,b,x)\mapsto\bigl(&ds+ha-kb,\;-da-fx,\\
&-db-gx,\;dx\bigr).
\end{aligned}
\]

Applying it to \((s,a,-b,x)\) gives \((ds+ha+kb,\,-da-fx,\,db-gx,\,dx)\), which is the image under the sign change of the differential of \(\operatorname{Tot}(S)\) at \((s,a,b,x)\). \(\square\)

**Lemma 5.2.** Let \(J\) be an injective object of \(\operatorname{Mod}_R^\lrcorner\), with maps \(h:J_{10}\to J_{11}\) and \(k:J_{01}\to J_{11}\). Then \((h,-k):J_{10}\oplus J_{01}\to J_{11}\) is surjective.

**Proof.** In \(\lrcorner\) the representable functors at \((1,0)\) and \((0,1)\) are \(R_{10}=(R\to R\leftarrow0)\) and \(R_{01}=(0\to R\leftarrow R)\), with identity maps, and the representable at \((1,1)\) is \(R_{11}=(0\to R\leftarrow0)\). The map \(\iota:R_{11}\to R_{10}\oplus R_{01}\) sending \(1\) to \((1,-1)\) at \((1,1)\) is a natural monomorphism. An element \(z\in J_{11}\) is a map \(R_{11}\to J\) (Lemma 1.1 of the preceding lesson); since \(J\) is injective it extends along \(\iota\) to a map \(R_{10}\oplus R_{01}\to J\), given by elements \(x\in J_{10}\) and \(y\in J_{01}\). The extension condition at \((1,1)\) reads \(z=h(x)-k(y)\). \(\square\)

**Theorem 5.3.** The derivator \(\mathbb D_R\) of a ring is stable. More precisely, for \(X\) in \(\mathbb D_R(\square)\) represented by a commutative square of complexes \(S\), the following are equivalent:

1. \(X\) is cocartesian;
2. \(\operatorname{Tot}(S)\) is acyclic;
3. \(X\) is cartesian.

**Proof.** By Lemma 5.1, condition 2 does not depend on the representative, so we may choose it.

(1)⇔(2). Take \(S=P\) semifree on \(\square\). The inclusion \(\ulcorner\to\square\) is a sieve; the representables of \(\square\) at the objects of \(\ulcorner\) restrict to representables of \(\ulcorner\), and the one at \((1,1)\) restricts to zero, so \(i_\ulcorner^*P\) is semifree. By the argument at the end of Section 2 of the preceding lesson, the derived counit of \(\mathbb Li_{\ulcorner!}\dashv i_\ulcorner^*\) at \(P\) is \(Q\) of the chain-level counit, whose component at \((1,1)\) is, by Kan's formula, the canonical map from the pushout

\[
P_{10}\sqcup_{P_{00}}P_{01}\longrightarrow P_{11}.
\]

On semifree objects of \(\ulcorner\) the maps \(P_{00}\to P_{10}\) and \(P_{00}\to P_{01}\) are inclusions of direct summands in each degree, because the representable at \((0,0)\) is \((R\leftarrow R\to R)\) and the other two are \((R\leftarrow0\to0)\) and \((0\leftarrow0\to R)\). So \(\varphi\) is injective in each degree, the pushout is its cokernel, and the map \(C(\varphi)\to P_{10}\sqcup_{P_{00}}P_{01}\), \((a,b,x)\mapsto[a,b]\), is a quasi-isomorphism (proof of Proposition 5.2 of *Complexes, cones and localization*). Its composite with the canonical map is \(\kappa\). Hence the counit at \((1,1)\) is invertible exactly when \(\kappa\) is a quasi-isomorphism, that is, when \(C(\kappa)=\operatorname{Tot}(P)\) is acyclic. Lemma 2.2 gives (1)⇔(2).

(3)⇔(2). Take \(S=I\) K-injective with injective terms (Theorem 4.1 of the K-injective lesson). The inclusion \(\lrcorner\to\square\) is a cosieve, and its left Kan extension is extension by zero, which is exact; so \(i_\lrcorner^*\) preserves K-injective complexes (Proposition 5.2 of the K-injective lesson) and injective objects. Dually to the previous step, the derived unit at \(I\) is \(Q\) of the chain-level unit, whose component at \((0,0)\) is the canonical map \(I_{00}\to I_{10}\times_{I_{11}}I_{01}\). By Lemma 5.2 the map \(\psi\) is surjective in each degree, the pullback is its kernel, and \(I_{10}\times_{I_{11}}I_{01}\to C(\psi)[-1]\), \((a,b)\mapsto(0,a,b)\), is a quasi-isomorphism by the dual argument. The composite with the canonical map is \(\lambda\). So \(X\) is cartesian exactly when \(\lambda\) is a quasi-isomorphism, that is, when \(C(\lambda)\) is acyclic, which by Lemma 5.1 is acyclicity of \(\operatorname{Tot}(I)\).

Finally, condition 2 is the same for \(P\) and \(I\), because \(P\) and \(I\) represent the same object. \(\square\)

**Corollary 5.4.** In \(\mathbb D_R\), \(\Sigma x\cong x[1]\) and \(\Omega x\cong x[-1]\) for every \(x\) in \(D(R)\).

**Proof.** For the square \((0,0)_*x\) extended by \(i_{\ulcorner!}\), take a semifree representative with \(P_{10}\) and \(P_{01}\) acyclic; the corner is \(C(\varphi)\), which is quasi-isomorphic to \(P_{00}[1]\) because \(P_{10}\oplus P_{01}\) is acyclic (the sequence \(0\to P_{10}\oplus P_{01}\to C(\varphi)\to P_{00}[1]\to0\) and Lemma 1.2). The loop functor is its inverse by Proposition 4.2. \(\square\)

## 6. Exercises

**6.1** (easy). Show that the represented derivator of abelian groups is pointed but not stable, by exhibiting a pushout square that is not a pullback square.

**6.2** (easy). In a pointed derivator, show that \(\Sigma0\cong0\) and that \(\Sigma\) preserves finite coproducts.

**6.3** (medium). For a chain map \(f:K\to L\) of complexes of \(R\)-modules, regarded as an object of \(\mathbb D_R([1])\), show that its cofibre in \(\mathbb D_R\) is the cone \(C(f)\).

**6.4** (medium). Show that a square of complexes whose two vertical maps are quasi-isomorphisms has acyclic total complex, and deduce from Theorem 5.3 that such a square is cocartesian and cartesian in \(\mathbb D_R\).

**6.5** (hard). Let \(0\to K\xrightarrow{f}L\xrightarrow{p}M\to0\) be a short exact sequence of complexes of \(R\)-modules. Show that the square with \(f:K\to L\) on top, \(0\to M\) below, and vertical maps \(K\to0\) and \(p\), is cocartesian and cartesian in \(\mathbb D_R\). Deduce that \(M\) is the cofibre of \(f\) and \(K\) the fibre of \(p\).

## 7. Solutions

**6.1.** The square with corners \(\mathbb Z\), \(0\), \(0\), \(0\) (the zero object at \((1,0)\), \((0,1)\), \((1,1)\)) is a pushout of abelian groups, since \(0\sqcup_{\mathbb Z}0=0\), but not a pullback, since \(0\times_00=0\neq\mathbb Z\).

**6.2.** \((0,0)_*0\) is the zero object of \(\mathbb D(\ulcorner)\) and \(i_{\ulcorner!}\) preserves it (Proposition 1.2), so \(\Sigma0\cong0\). \(\Sigma\) is a left adjoint (Proposition 3.2), so it preserves coproducts.

**6.3.** Represent \(f\) by a semifree arrow \(P_0\to P_1\), an inclusion of a direct summand in each degree (proof of Theorem 4.1 of the preceding lesson). Extension by zero gives the span \(P_1\leftarrow P_0\to0\); replacing \(0\) by the contractible cone \(C(1_{P_0})\), with the inclusion \(\iota:P_0\to C(1_{P_0})\), gives a semifree representative. By the proof of Theorem 5.3, the cofibre is \(C(\varphi)\) with \(\varphi=(f,-\iota)\). The map \(C(\varphi)\to C(f)\), \((a,b,x)\mapsto(a,x)\), is a surjective chain map with kernel \(C(1_{P_0})\), which is acyclic, so it is a quasi-isomorphism: the cofibre is \(C(f)\).

**6.4.** The pair \((g,h)\) is a morphism of arrows from the top row \(f:S_{00}\to S_{10}\) to the bottom row \(k:S_{01}\to S_{11}\), and it induces \(c:C(f)\to C(k)\) (Proposition 1.1 of the first lesson). The cone \(C(c)\) has terms \(S_{11}^n\oplus S_{01}^{n+1}\oplus S_{10}^{n+1}\oplus S_{00}^{n+2}\) and differential
\[
\begin{aligned}
(s,b,a,x)\mapsto\bigl(&ds+kb+ha,\;-db+gx,\\
&-da-fx,\;dx\bigr),
\end{aligned}
\]
which is the differential of \(\operatorname{Tot}(S)\) with the two middle components exchanged. If \(g\) and \(h\) are quasi-isomorphisms, so is \(c\) (Proposition 1.1 of the first lesson), and its cone is acyclic. Theorem 5.3 then gives both properties.

**6.5.** By the description in Exercise 6.4, \(\operatorname{Tot}(S)\) is the cone of the map \(C(f)\to C(0\to M)=M\) induced by \((K\to0,\,p)\), which is \((l,k)\mapsto p(l)\). This is the cone-to-quotient map of Proposition 5.2 of *Complexes, cones and localization*, a quasi-isomorphism, so \(\operatorname{Tot}(S)\) is acyclic and Theorem 5.3 applies. The square is the cofibre square of \(f\), since its lower left corner is \(0\), so \(M\) is the cofibre of \(f\). Being cartesian, it exhibits \(K\) as the homotopy pullback of \(L\to M\leftarrow0\), which is the fibre of \(p\).

## Sources

- [PS] A. Grothendieck, *Pursuing Stacks*, §69, arXiv:2111.01000. https://arxiv.org/abs/2111.01000
- [Gr] M. Groth, *Derivators, pointed derivators and stable derivators*, Algebraic & Geometric Topology 13 (2013), 313–374; arXiv:1112.3840. https://arxiv.org/abs/1112.3840 — Sections 3 and 4.1: pointed derivators defined by a zero object in the underlying category, cocartesian and cartesian squares, suspension, loops, cones and fibres, stability.
