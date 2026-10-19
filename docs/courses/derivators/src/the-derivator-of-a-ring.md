# The derivator of a ring

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For a ring \(R\) and a small category \(I\), the functors from \(I\) to left \(R\)-modules form an abelian category \(\operatorname{Mod}_R^I\), and its derived category \(D(\operatorname{Mod}_R^I)\) is the category of \(I\)-shaped diagrams of complexes up to levelwise quasi-isomorphism. *Pursuing Stacks* (§69) proposes the assignment \(I\mapsto D(\operatorname{Mod}_R^I)\) as the full structure carried by the derived category of \(R\), and singles out one property to check: every restriction functor should have adjoints on both sides. This lesson proves that the assignment is a derivator, and that it is strong.

Two resolutions do the work. Left Kan extensions are computed on K-projective complexes, built from representable functors; right Kan extensions on K-injective complexes. Kan's formulas (Der4) then hold because restriction to a comma category sends K-projectives to K-projectives and K-injectives to K-injectives: the projections from comma categories are discrete fibrations, along which Kan extensions are exact.

**Prerequisites.** The lessons [*Diagrams up to weak equivalence*](diagrams-up-to-weak-equivalence.md) (Example 4.4: the prederivator \(\mathbb D_{\mathcal A}\)), [*Kan extensions and the derivator axioms*](kan-extensions-and-the-derivator-axioms.md) (Theorem 4.2 and Exercise 7.5) and [*Homotopy exact squares*](homotopy-exact-squares.md) (Proposition 2.3). From the course *Derived categories and sheaf operations*: [*Flat modules and K-flat resolutions*](course:derived-categories-and-sheaf-operations/flat-modules-and-k-flat-resolutions), Theorem 3.4 (semifree resolutions over a ring), and [*K-injective resolutions in Grothendieck abelian categories*](course:derived-categories-and-sheaf-operations/k-injective-resolutions-in-grothendieck-categories), Theorems 4.1 and 5.1, equation (5.1) and Proposition 5.2.

Throughout, \(R\) is an associative ring with unit, \(\operatorname{Mod}_R\) is the category of left \(R\)-modules, and \(\mathbb D_R(I)=D(\operatorname{Mod}_R^I)\) is the prederivator of Example 4.4 of the first lesson for \(\mathcal A=\operatorname{Mod}_R\). A complex of objects of \(\operatorname{Mod}_R^I\) is a functor from \(I\) to complexes of modules, and its cohomology and its quasi-isomorphisms are computed objectwise.

## 1. Representable functors and discrete fibrations

For an object \(i\) of \(I\), let \(R_i\) be the functor \(j\mapsto R[I(i,j)]\), the free module on the set of morphisms \(i\to j\), with \(I(j,j')\) acting by composition.

**Lemma 1.1 (Yoneda).** For \(M\) in \(\operatorname{Mod}_R^I\), the map \(\operatorname{Hom}(R_i,M)\to M(i)\), \(\varphi\mapsto\varphi_i(1_i)\), is bijective. Hence \(R_i\) is projective, and every \(M\) is a quotient of a direct sum of representables.

**Proof.** A natural transformation \(\varphi\) is determined by \(x=\varphi_i(1_i)\), since naturality forces \(\varphi_j(g)=M(g)(x)\) for \(g:i\to j\); conversely this formula defines a natural transformation for every \(x\). Evaluation at \(i\) is exact, so \(\operatorname{Hom}(R_i,-)\) is exact. The map \(\bigoplus_{(i,x)}R_i\to M\), over all objects \(i\) and all \(x\in M(i)\), is surjective. \(\square\)

**Lemma 1.2.** For a functor \(u:J\to K\), the left Kan extension of Theorem 2.1 of the second lesson satisfies \(u_!R_j\cong R_{u(j)}\), and \(u_!\) preserves direct sums.

**Proof.** By Lemma 1.1, naturally in \(N\),
\[
\begin{aligned}
\operatorname{Hom}(u_!R_j,N)&\cong\operatorname{Hom}(R_j,u^*N)\\
&\cong N(u(j))\\
&\cong\operatorname{Hom}(R_{u(j)},N);
\end{aligned}
\]
the Yoneda lemma for \(\operatorname{Mod}_R^K\) gives the isomorphism. A left adjoint preserves direct sums. \(\square\)

A functor \(q:E\to B\) is a *discrete fibration* if for every object \(e\) of \(E\) and every morphism \(f:b'\to q(e)\) there is exactly one morphism \(\tilde f:e'\to e\) with \(q(\tilde f)=f\). It is a *discrete opfibration* if \(q^{\mathrm{op}}\) is a discrete fibration. For \(u:J\to K\) and \(k\) in \(K\):

- \(\mathrm{pr}:J_{/k}\to J\) is a discrete fibration: the lift of \(g:j'\to j\) at \((j,f)\) is \(g:(j',f\,u(g))\to(j,f)\).
- \(\mathrm{pr}:J_{k/}\to J\) is a discrete opfibration, dually.

The *fibre* \(q^{-1}(b)\) is the set of objects over \(b\); for a discrete (op)fibration the only morphisms of \(E\) over \(1_b\) are identities.

**Lemma 1.3.** Let \(q:E\to B\) be a functor between small categories.

1. If \(q\) is a discrete fibration, the right Kan extension of \(N\) in \(\operatorname{Mod}_R^E\) is
\[
(q_*N)(b)=\prod_{e\in q^{-1}(b)}N(e),
\]
and \(q_*\) is exact.
2. If \(q\) is a discrete opfibration, the left Kan extension is
\[
(q_!N)(b)=\bigoplus_{e\in q^{-1}(b)}N(e),
\]
and \(q_!\) is exact.

**Proof.** (1) By Theorem 2.2 of the second lesson, \((q_*N)(b)\) is the limit of \(N\,\mathrm{pr}\) over \(E_{b/}\), whose objects are pairs \((e,f:b\to q(e))\). Let \(c:q^{-1}(b)\to E_{b/}\) send \(e'\) to \((e',1_b)\), regarding the fibre as a discrete category, and let \(r(e,f)\) be the object \(e'\) over \(b\) with the lift \(\tilde f:e'\to e\) of \(f\). A morphism \((e',1_b)\to(e,f)\) is a morphism \(e'\to e\) over \(f\), and there is one exactly when \(e'=r(e,f)\). So \(c\) is left adjoint to \(r\). By Proposition 2.3 of the lesson on homotopy exact squares, applied to the represented derivator of \(\operatorname{Mod}_R\), the limit over \(E_{b/}\) is the limit over the discrete fibre, a product. Products of modules are exact. (2) is dual, with direct sums, which are exact. \(\square\)

A complex \(P\) is *K-projective* if \(\operatorname{Hom}_K(P,A)\), the group of homotopy classes of chain maps, vanishes for every acyclic complex \(A\); it is *K-injective* if \(\operatorname{Hom}_K(A,P)=0\) for every acyclic \(A\).

**Corollary 1.4.** For \(u:J\to K\) and \(k\) in \(K\), restriction along \(\mathrm{pr}:J_{/k}\to J\) preserves K-projective complexes, and restriction along \(\mathrm{pr}:J_{k/}\to J\) preserves K-injective complexes.

**Proof.** For the first, \(\mathrm{pr}^*\) is left adjoint to the exact functor \(\mathrm{pr}_*\) of Lemma 1.3. The adjunction is compatible with homotopies, so \(\operatorname{Hom}_K(\mathrm{pr}^*P,A)=\operatorname{Hom}_K(P,\mathrm{pr}_*A)\), which is zero when \(A\) is acyclic. The second is Proposition 5.2 of *K-injective resolutions in Grothendieck abelian categories*, applied to the exact left adjoint \(\mathrm{pr}_!\). \(\square\)

## 2. Resolutions

A complex \(P\) in \(\operatorname{Mod}_R^I\) is *semifree* if there is a set \(S\) of generators, each \(s\in S\) with a degree \(n_s\) and an object \(i_s\), and a division \(S=S_0\cup S_1\cup\cdots\) into stages, such that

\[
P^n=\bigoplus_{n_s=n}R_{i_s},
\]

and the differential of each generator, that is the image of \(1_{i_s}\in R_{i_s}(i_s)\), is a finite combination of generators of earlier stages (zero for \(s\in S_0\)).

**Theorem 2.1.** Every complex \(G\) in \(\operatorname{Mod}_R^I\) has a quasi-isomorphism \(P\to G\), surjective in each degree, with \(P\) semifree. Every semifree complex is K-projective, and for semifree \(P\) and every complex \(N\)

\[
\operatorname{Hom}_{K}(P,N)\to\operatorname{Hom}_{D}(P,N)
\]

is bijective. A quasi-isomorphism between semifree complexes is a homotopy equivalence.

**Proof.** This is the proof of Theorem 3.4 of *Flat modules and K-flat resolutions*, with free modules replaced by representables and Lemma 1.1 used to define maps out of them.

*Construction.* For every object \(i\), degree \(n\) and \(x\in G^n(i)\), take a *disk*: generators \(a\) in degree \(n\) and \(b\) in degree \(n+1\), both at the object \(i\), with \(da=b\), mapped (by Lemma 1.1) to \(x\) and to \(dx\). Put all generators \(b\) in stage \(0\) and all generators \(a\) in stage \(1\). This gives a complex \(P_1\) with a map \(P_1\to G\) that is surjective in every degree. Inductively, for every object \(i\), degree \(n\) and cycle \(z\in P_s^n(i)\) whose image in \(G^n(i)\) is zero, add a generator \(c\) in degree \(n-1\) at \(i\), in stage \(s+1\), with \(dc=z\) and image \(0\) in \(G\). The differential of \(c\) involves finitely many earlier generators, because \(P_s^n(i)\) is a direct sum. Let \(P\) be the union of the \(P_s\), and \(L\) the kernel of \(P\to G\). A cycle of \(L\) at an object \(i\) involves finitely many generators, so it lies in some \(P_s\); it is a cycle of \(P_s\) with image zero, so the generator attached to it in stage \(s+1\) lies in \(L\) and bounds it. Hence \(L\) is acyclic. The long exact cohomology sequence of \(0\to L\to P\to G\to0\), computed objectwise, shows that \(P\to G\) is a quasi-isomorphism.

*K-projectivity.* Let \(f:P\to A\) be a chain map with \(A\) acyclic. Define \(h:P^n\to A^{n-1}\) on generators, stage by stage. For a generator \(s\) of degree \(n\) at \(i\), with \(h\) defined on earlier stages, the element \(w=f(s)-h(ds)\in A^n(i)\) is a cycle, since \(dw=f(ds)-dh(ds)=h(d\,ds)=0\) by the identity \(f=dh+hd\) on earlier stages. Choose \(h(s)\in A^{n-1}(i)\) with \(dh(s)=w\), and extend by Lemma 1.1. Then \(f=dh+hd\) on \(s\). The same argument with \(A[m]\) in place of \(A\) shows that every shift of \(P\) has only null-homotopic maps to acyclic complexes.

*Hom.* If \(t:Z\to N\) is a quasi-isomorphism, its cone is acyclic, so \(\operatorname{Hom}_K(P,-)\) applied to the triangle of \(t\) gives a bijection \(\operatorname{Hom}_K(P,Z)\to\operatorname{Hom}_K(P,N)\). As in Theorem 3.4 of *Flat modules and K-flat resolutions*, this bijectivity shows that every roof \(P\xleftarrow{s}Z\to N\) comes from a unique homotopy class \(P\to N\). If \(f:P\to P'\) is a quasi-isomorphism of semifree complexes, bijectivity of \(\operatorname{Hom}_K(P',P)\to\operatorname{Hom}_K(P',P')\) and of \(\operatorname{Hom}_K(P,P)\to\operatorname{Hom}_K(P,P')\) give a homotopy inverse. \(\square\)

Write \(K_{\mathrm{sf}}(I)\) for the full subcategory of \(K(\operatorname{Mod}_R^I)\) on semifree complexes and \(K_{\mathrm{inj}}(I)\) for the one on K-injective complexes. By Theorem 2.1, \(Q:K_{\mathrm{sf}}(I)\to D(\operatorname{Mod}_R^I)\) is fully faithful and essentially surjective. The category \(\operatorname{Mod}_R^I\) is a locally small Grothendieck abelian category: filtered colimits are exact objectwise, and \(\bigoplus_iR_i\) is a generator. So Theorem 4.1 of *K-injective resolutions in Grothendieck abelian categories* gives K-injective resolutions, and equation (5.1) there makes \(Q:K_{\mathrm{inj}}(I)\to D(\operatorname{Mod}_R^I)\) fully faithful and essentially surjective as well. We choose quasi-inverses

\[
P:D(\operatorname{Mod}_R^I)\to K_{\mathrm{sf}}(I),
\]
\[
I:D(\operatorname{Mod}_R^I)\to K_{\mathrm{inj}}(I),
\]

with \(P(QP_0)=P_0\) for semifree \(P_0\) and \(I(QI_0)=I_0\) for K-injective \(I_0\).

**Proposition 2.2 (derived Kan extensions).** For \(u:J\to K\), the functors

\[
\mathbb Lu_!=Q\,u_!\,P,
\]
\[
\mathbb Ru_*=Q\,u_*\,I
\]

are left and right adjoint to \(u^*:D(\operatorname{Mod}_R^K)\to D(\operatorname{Mod}_R^J)\).

**Proof.** By Lemma 1.2, \(u_!\) sends a semifree complex to a semifree complex, with the same generators moved along \(u\) and the same stages. The adjunction \(u_!\dashv u^*\) on complexes is compatible with homotopies, and \(u^*\) preserves quasi-isomorphisms. For \(X\) in \(D(\operatorname{Mod}_R^J)\) and \(Y=QN\),

\[
\begin{aligned}
&\operatorname{Hom}_D(Qu_!PX,QN)\\
&\quad\cong\operatorname{Hom}_K(u_!PX,N)\\
&\quad\cong\operatorname{Hom}_K(PX,u^*N)\\
&\quad\cong\operatorname{Hom}_D(QPX,Qu^*N)\\
&\quad\cong\operatorname{Hom}_D(X,u^*Y),
\end{aligned}
\]

naturally, using Theorem 2.1 twice. On the right, \(u^*\) is exact and left adjoint to \(u_*\), so \(u_*\) preserves K-injectives (Proposition 5.2 of the K-injective lesson), and the same computation with equation (5.1) there gives \(\operatorname{Hom}_D(u^*X,QI_0)\cong\operatorname{Hom}_D(X,Qu_*I_0)\). \(\square\)

On semifree complexes the derived unit is \(Q\) of the unit of \(u_!\dashv u^*\): under the bijections of the proof, the identity of \(Qu_!P_0\) corresponds to \(Q\) of the chain-level unit \(P_0\to u^*u_!P_0\). Dually, on K-injectives the derived counit is \(Q\) of the chain-level counit.

## 3. The axioms

**Theorem 3.1.** \(\mathbb D_R\) is a derivator.

**Proof.** (Der1) and (Der2) hold for the prederivator of any abelian category (Exercise 7.5 of the lesson on Kan extensions). (Der3) is Proposition 2.2.

(Der4) for left Kan extensions. Let \(u:J\to K\) and \(k\) in \(K\). Base change morphisms are natural, so it suffices to show that \((\alpha^{/k})_!\) is invertible at \(X=QP_0\) with \(P_0\) semifree. By its definition (Section 3 of the second lesson), \((\alpha^{/k})_!\) at \(X\) is the morphism that corresponds, under the adjunction bijection of \(\mathbb L\operatorname{colim}_{J_{/k}}\dashv p^*\) at \(\mathrm{pr}^*X\), to

\[
\begin{gathered}
\varphi=(\alpha^{/k})^*\,\mathbb Lu_!X\cdot\mathrm{pr}^*\eta_X:\\
\mathrm{pr}^*X\to p^*k^*\mathbb Lu_!X .
\end{gathered}
\]

Every K-projective complex \(Y\) has \(\operatorname{Hom}_K(Y,-)\to\operatorname{Hom}_D(Y,-)\) bijective (the proof in Theorem 2.1 uses only K-projectivity). The colimit functor on complexes has the exact right adjoint \(p^*\), so it preserves K-projective complexes, by the argument of Corollary 1.4. Hence the computation in the proof of Proposition 2.2 shows that \(Q\operatorname{colim}P'\), where \(P'\) is a quasi-inverse of \(Q\) on K-projective complexes with \(P'(Y)=Y\) for K-projective \(Y\), is a left adjoint of \(p^*\) on \(D(\operatorname{Mod}_R^{J_{/k}})\), with unit \(Q\) of the chain-level unit at K-projective objects. By Lemma 3.1 of the second lesson we may use this left adjoint. By Corollary 1.4, \(\mathrm{pr}^*P_0\) is K-projective. So the adjunction bijection at \(\mathrm{pr}^*X\) sends the class of a chain map \(g:\operatorname{colim}_{J_{/k}}\mathrm{pr}^*P_0\to N\) to \(Q(p^*g\cdot\text{unit})\).

Let \(\beta:\operatorname{colim}_{J_{/k}}\mathrm{pr}^*P_0\to(u_!P_0)(k)\) be the chain-level base change morphism. In each degree it is the identity of \(\operatorname{colim}_{J_{/k}}P_0^n\,\mathrm{pr}=(u_!P_0^n)(k)\), by the computation in the proof of Theorem 4.2 of the second lesson, and by definition \(p^*\beta\cdot\text{unit}=(\alpha^{/k})^*u_!P_0\cdot\mathrm{pr}^*\eta^{\mathrm{ch}}\), with \(\eta^{\mathrm{ch}}\) the chain-level unit of \(u_!\dashv u^*\). The derived unit \(\eta_X\) is \(Q(\eta^{\mathrm{ch}})\) (end of Section 2), so \(Q\) of the right side is \(\varphi\). Hence \((\alpha^{/k})_!=Q(\beta)\), an isomorphism.

(Der4) for right Kan extensions is dual: represent \(X\) by a K-injective \(I_0\), use Corollary 1.4 for \(J_{k/}\), and the limit formula for \(u_*\). \(\square\)

For \(I=e\), \(\operatorname{Mod}_R^e=\operatorname{Mod}_R\) and \(\mathbb D_R(e)=D(R)\). Homotopy colimits in \(\mathbb D_R\) are the classical *derived colimits*, computed by applying the colimit degreewise to a semifree resolution; for the shape \(\ulcorner\) this is the mapping-cone description of a homotopy pushout, worked out in the lesson on pointed and stable derivators.

## 4. Strongness

**Theorem 4.1.** For every small category \(J\), the partial underlying diagram functor

\[
\operatorname{dia}_{[1],J}:\mathbb D_R([1]\times J)\to\mathbb D_R(J)^{[1]}
\]

is full and essentially surjective. Thus \(\mathbb D_R\) is a strong derivator.

**Proof.** An object of \(\operatorname{Mod}_R^{[1]\times J}\) is an arrow \(M_0\to M_1\) in \(\operatorname{Mod}_R^J\), and \(\operatorname{dia}_{[1],J}\) sends the class of an arrow of complexes \(f:P_0\to P_1\) to the morphism \(Qf\) of \(\mathbb D_R(J)\).

*Essentially surjective.* A morphism \(\varphi:X\to Y\) of \(\mathbb D_R(J)\) with \(X=QP_0\), \(P_0\) semifree, and \(Y=QN\) is \(Qf\) for a chain map \(f:P_0\to N\), by Theorem 2.1. The arrow \(f\) is an object of \(\mathbb D_R([1]\times J)\) with underlying morphism \(\varphi\).

*Full.* The representables of \([1]\times J\) are \(R_{(0,j)}=(R_j\xrightarrow{1}R_j)\) and \(R_{(1,j)}=(0\to R_j)\). So a semifree complex on \([1]\times J\) is an arrow \(f:P_0\to P_1\) such that, as graded objects, \(P_1=P_0\oplus P''\) with \(f\) the inclusion; \(P_0\) is semifree on \(J\) with the generators at objects \((0,j)\), and \(P_1\) is semifree on \(J\) with all generators. Every object \(A\) of \(\mathbb D_R([1]\times J)\) is represented by such an arrow (Theorem 2.1 on \([1]\times J\)). Let \(B\) be represented by any arrow \(g:N_0\to N_1\), and let \((a,b):\operatorname{dia}A\to\operatorname{dia}B\) be a commutative square in \(\mathbb D_R(J)\). By Theorem 2.1, \(a=Qa'\) and \(b=Qb'\) for chain maps \(a':P_0\to N_0\) and \(b':P_1\to N_1\), and \(Q(b'f)=Q(ga')\) gives a homotopy \(h\) with

\[
b'f-ga'=dh+hd.
\]

Extend \(h\) to \(\tilde h:P_1\to N_1[-1]\) by zero on \(P''\), and put \(b''=b'-(d\tilde h+\tilde hd)\). Then \(Qb''=Qb'=b\), and since \(\tilde hf=h\) and \(\tilde hdf=\tilde hfd=hd\),

\[
b''f=b'f-dh-hd=ga'.
\]

So \((a',b'')\) is a morphism of arrows of complexes, and its image under \(\operatorname{dia}_{[1],J}\) is \((a,b)\). \(\square\)

The functor \(\operatorname{dia}_{[1],J}\) is not faithful: for \(R=\mathbb Z\) and \(J=e\), the first lesson (Proposition 2.1) gives a nonzero morphism whose underlying square is zero.

## 5. Exercises

**5.1** (easy). Compute \(\operatorname{Hom}(R_i,R_j)\) in \(\operatorname{Mod}_R^I\), and describe composition of such maps in terms of composition in \(I\).

**5.2** (easy). For \(I=[1]\), list the representables and show that \(\operatorname{Mod}_R^{[1]}\) has the projective object \((R\xrightarrow{1}R)\) and the injective object \((E\to0)\) for an injective module \(E\).

**5.3** (medium). Let \(u:\{0\}\to[1]\) be the inclusion of \(0\). Compute \(\mathbb Lu_!\) and \(\mathbb Ru_*\) on \(D(R)\), and show that they send \(X\) to \((X\xrightarrow{1}X)\) and \((X\to0)\).

**5.4** (medium). Show that the projection \(\mathrm{pr}:J_{/k}\to J\) need not be a discrete opfibration, by an example with \(J=K=[1]\) and \(u=1_{[1]}\).

**5.5** (hard). Let \(u:J\to K\) be a functor, \(k\) an object of \(K\) and \(X\) in \(D(\operatorname{Mod}_R^J)\). Show that if \(J_{/k}\) has a terminal object \(t=(j,f)\), then \((\mathbb Lu_!X)_k\cong X_j\). For \(R=\mathbb Z\), \(J=\ulcorner=(b\leftarrow a\rightarrow c)\), \(K=e\), and the diagram of modules \(X=(0\leftarrow\mathbb Z\xrightarrow{0}\mathbb Z)\) placed in degree \(0\), show that the homotopy pushout has nonzero cohomology in degree \(-1\), although the ordinary pushout of modules is \(\mathbb Z\) in degree \(0\).

## 6. Solutions

**5.1.** By Lemma 1.1, \(\operatorname{Hom}(R_i,R_j)\cong R_j(i)=R[I(j,i)]\). Composition corresponds to composition in \(I\), reversed.

**5.2.** \(R_0=(R\xrightarrow{1}R)\) and \(R_1=(0\to R)\), projective by Lemma 1.1. For \(N=(N_0\to N_1)\), \(\operatorname{Hom}(N,(E\to0))\cong\operatorname{Hom}_R(N_0,E)\), which is exact in \(N\) because evaluation at \(0\) is exact and \(E\) is injective.

**5.3.** \(\{0\}_{/0}\) and \(\{0\}_{/1}\) each have one object, so \(u_!M=(M\xrightarrow{1}M)\) for a module \(M\), and the same degreewise for complexes; this functor preserves quasi-isomorphisms, so it is its own derived functor on semifree complexes. \(\{0\}_{1/}\) is empty and \(\{0\}_{0/}\) has one object, so \(u_*M=(M\to0)\), exact as well.

**5.4.** Take \(k=0\). The category \(J_{/0}\) has the single object \((0,1_0)\), since there is no morphism \(1\to0\). A discrete opfibration would need a lift of the arrow \(0\to1\) of \(J\) starting at \((0,1_0)\), that is, an object of \(J_{/0}\) over \(1\); there is none. So \(\mathrm{pr}:J_{/0}\to J\) is not a discrete opfibration. (It is a discrete fibration, as every \(\mathrm{pr}:J_{/k}\to J\) is.)

**5.5.** If \(t\) is terminal in \(J_{/k}\), (Der4) and Corollary 2.4 of the lesson on homotopy exact squares give isomorphisms \((\mathbb Lu_!X)_k\cong\operatorname{hocolim}_{J_{/k}}\mathrm{pr}^*X\) and \(\operatorname{hocolim}_{J_{/k}}\mathrm{pr}^*X\cong(\mathrm{pr}^*X)_t=X_j\).

For the example, \(X_a=\mathbb Z\), \(X_b=0\), \(X_c=\mathbb Z\), and both maps are zero. By Proposition 2.2 for \(p:{\ulcorner}\to e\), the homotopy pushout is \(Q\operatorname{colim}_\ulcorner P\) for a semifree resolution \(P\to X\). The representables are \(R_a=(\mathbb Z\leftarrow\mathbb Z\to\mathbb Z)\) with identity maps, \(R_b=(\mathbb Z\leftarrow0\to0)\) and \(R_c=(0\leftarrow0\to\mathbb Z)\). Take:

- in degree \(0\), generators \(s\) at \(a\) and \(t\) at \(c\), mapped to \(1\in X_a\) and \(1\in X_c\);
- in degree \(-1\), generators \(v\) at \(b\) and \(w\) at \(c\), with \(dv=s\in P^0(b)\) and \(dw=s\in P^0(c)\).

Objectwise, \(P\) is \(0\to\mathbb Zs\) at \(a\); \(\mathbb Zv\to\mathbb Zs\), an isomorphism, at \(b\); and \(\mathbb Zw\to\mathbb Zs\oplus\mathbb Zt\), \(w\mapsto s\), at \(c\). So \(P\to X\) is a quasi-isomorphism at every object, and \(P\) is semifree with stages \(\{s,t\}\) and \(\{v,w\}\). The colimit over \(\ulcorner\) is the pushout of the values: \(\mathbb Zs\oplus\mathbb Zt\) in degree \(0\), where the two copies of \(s\) are identified, and \(\mathbb Zv\oplus\mathbb Zw\) in degree \(-1\), with \(v\mapsto s\) and \(w\mapsto s\). Its cohomology is \(\mathbb Zt\) in degree \(0\) and \(\mathbb Z(v-w)\) in degree \(-1\). The ordinary pushout of modules is the cokernel of the zero map \(\mathbb Z\to0\oplus\mathbb Z\), that is \(\mathbb Z\), with nothing in degree \(-1\).

## Sources

- [PS] A. Grothendieck, *Pursuing Stacks*, §69, arXiv:2111.01000. https://arxiv.org/abs/2111.01000 — the assignment \(I\mapsto D(\operatorname{Hom}(I,\mathcal A))\) and the demand that restriction have adjoints on both sides.
- [Gr] M. Groth, *Derivators, pointed derivators and stable derivators*, Algebraic & Geometric Topology 13 (2013), 313–374; arXiv:1112.3840. https://arxiv.org/abs/1112.3840 — Section 1.3 proves the derivator property for combinatorial model categories through projective and injective model structures and a discrete-fibration lemma; the argument here follows the same pattern with resolutions instead of model structures.
- Programme lessons [*Flat modules and K-flat resolutions*](course:derived-categories-and-sheaf-operations/flat-modules-and-k-flat-resolutions) and [*K-injective resolutions in Grothendieck abelian categories*](course:derived-categories-and-sheaf-operations/k-injective-resolutions-in-grothendieck-categories).
