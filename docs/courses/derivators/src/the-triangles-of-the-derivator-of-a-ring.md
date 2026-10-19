# The triangles of the derivator of a ring

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The derived category \(D(R)\) of a ring carries its classical triangulated structure, defined by the cones of chain maps, with a sign convention fixed by hand. The derivator of the ring gives \(D(R)\) a second triangulated structure, without choices. This lesson compares the two and finds that they agree once the suspension is identified with the shift through the correct one of two possible isomorphisms; the other one reverses the sign of every connecting map. Before that, the lesson shows that restriction and homotopy Kan extensions are exact functors for the canonical structures, and it derives the long exact sequences that *Pursuing Stacks* calls the Dold–Puppe sequences.

**Prerequisites.** The lessons [*Kan extensions and the derivator axioms*](kan-extensions-and-the-derivator-axioms.md) (Section 1), [*Homotopy exact squares*](homotopy-exact-squares.md) (Lemma 1.1, Proposition 2.3, Proposition 3.3), [*The derivator of a ring*](the-derivator-of-a-ring.md) (Theorems 2.1 and 4.1), [*Pointed and stable derivators*](pointed-and-stable-derivators.md) (Lemma 5.1, Theorem 5.3, Corollary 5.4), [*Recognizing cocartesian squares*](recognizing-cocartesian-squares.md) (Proposition 3.1, Corollaries 3.2 and 3.3), [*Stable derivators are additive*](stable-derivators-are-additive.md) (Corollary 4.2) and [*The canonical triangulated structure*](the-canonical-triangulated-structure.md) (Lemma 1.2, Definition 1.3, naturality of \(\iota\), Theorem 3.1, Lemma 3.3). From [*Complexes, cones and localization*](course:derived-categories-and-sheaf-operations/complexes-cones-and-localization): the cone (2.1), the cone triangle (2.2), Lemma 2.2, and the triangulated structure of the derived category (Theorem 5.1).

Throughout, \(\mathbb D\) is a strong stable derivator, and each \(\mathbb D(J)\) carries the canonical triangulated structure of the preceding lesson.

## 1. Exact functors

A functor \(F\) between triangulated categories is *exact* if it is additive and comes with a natural isomorphism \(\theta:F\Sigma\to\Sigma F\) such that for every distinguished triangle \((u,v,w)\) the triangle \((Fu,Fv,\theta\circ Fw)\) is distinguished.

**Lemma 1.1 (Kan extensions in one variable).** Let \(u:J\to K\) and \(w:A\to B\) be functors. The commutative square with top \(1_J\times w\), left \(u\times1_A\), right \(u\times1_B\) and bottom \(1_K\times w\) is homotopy exact. So is its dual for right Kan extensions.

**Proof.** By (Der2) it suffices to check the base change morphism at each object \((k,a)\) of \(K\times A\). The comma category of \(u\times1_A\) over \((k,a)\) is \(J_{/k}\times A_{/a}\), and that of \(u\times1_B\) over \((k,w(a))\) is \(J_{/k}\times B_{/w(a)}\); the functor \(w\) induces \(1\times w_\sharp\) from the first to the second, with \(w_\sharp(a',g)=(w(a'),w(g))\). The comma square of \(u\times1_A\) at \((k,a)\), pasted on the left of our square, gives the same square as the square of \(1\times w_\sharp\), with sides \(p\) and identity transformation, pasted on the left of the comma square of \(u\times1_B\) at \((k,w(a))\): both have the same edges, and both transformations have components \((f,w(g))\) at \(((j,f),(a',g))\). By horizontal pasting and (Der4), the base change morphism at \((k,a)\) is invertible exactly when the comparison map of homotopy colimits along \(1\times w_\sharp\) is. The functors \(s:J_{/k}\to J_{/k}\times A_{/a}\), \(\xi\mapsto(\xi,(a,1_a))\), and \(s'=(1\times w_\sharp)\,s\) are right adjoints, because \((a,1_a)\) and \((w(a),1_{w(a)})\) are terminal. By Proposition 2.3 of the lesson on homotopy exact squares their comparison maps are invertible, and horizontal pasting gives \(\kappa_{s'}=\kappa_{1\times w_\sharp}\cdot\kappa_s\,(1\times w_\sharp)^*\), so \(\kappa_{1\times w_\sharp}\) is invertible. Right Kan extensions are dual. \(\square\)

Exchanging the two factors, Lemma 1.1 also says that restriction along \(u\times1\) commutes with homotopy Kan extensions along \(1\times w\).

**Proposition 1.2.** For a functor \(u:J\to K\), the functors \(u^*:\mathbb D(K)\to\mathbb D(J)\) and \(u_!,u_*:\mathbb D(J)\to\mathbb D(K)\) are exact.

**Proof.** Let \(F\) be one of them, and for a small category \(A\) let \(F_A\) be the corresponding functor along \(u\times1_A\) between \(\mathbb D(J\times A)\) and \(\mathbb D(K\times A)\). This is the functor \(u^*\), \(u_!\) or \(u_*\) of the shifted derivator \(\mathbb D^A\), and the objects of \(\mathbb D(J\times A)\) are diagrams of shape \(A\) in \(\mathbb D^J\). We use three properties.

1. \(F_A\) commutes with restriction along \(1\times w\) for every \(w:A'\to A\), up to natural isomorphism: by Lemma 1.1 for \(u_!\) and \(u_*\), and on the nose for \(u^*\). In particular \(F_A\) acts objectwise in \(A\), and it sends objects vanishing at an object \(a\) to objects vanishing at \(a\), since \(F\) preserves zero objects.
2. \(F_\square\) sends cocartesian squares to cocartesian squares. For \(u_!\), left Kan extensions along \(u\times1\) and along \(1\times i_\ulcorner\) commute, being left adjoints of commuting restrictions. For \(u^*\), use Lemma 1.1 with the factors exchanged. For \(u_*\), the dual argument shows that it sends cartesian squares to cartesian squares, and in the stable derivators \(\mathbb D^J\) and \(\mathbb D^K\) cartesian and cocartesian squares coincide (Corollary 3.3 of the lesson on recognizing cocartesian squares).
3. \(F\) is additive (Corollary 4.2 of the lesson *Stable derivators are additive*).

By 1 and 2, \(F_{[2]\times[1]}\) sends cofibre diagrams to cofibre diagrams, and \(F_\square\) sends a suspension square \(W_x=i_{\ulcorner!}(0,0)_*x\) to a cocartesian square with zero legs and value \(Fx\) at \((0,0)\). Define \(\theta_x:F\Sigma x\to\Sigma Fx\) as the inverse of \(\iota_{F_\square W_x}\), composed with the identification of \((F_\square W_x)_{11}\) with \(F\Sigma x\); it is natural by naturality of \(\iota\). For \(f\) in \(\mathbb D(J\times[1])\), the triangle of the cofibre diagram \(F_{[2]\times[1]}Y_f\) has the maps \(Fu\), \(Fv\) and \(\iota^{-1}_{FY}\circ F(Y_{11}\to Y_{21})\). Applying \(F_\square\) to the isomorphism \(W_{f_0}\cong s_{02}^*Y_f\) and using naturality of \(\iota\) gives \(\iota_{FY}^{-1}\circ F(\iota_Y)=\theta\). So this triangle is \((Fu,Fv,\theta\circ Fw)\) with \(w\) the third map of \(T_f\), and it is distinguished by Lemma 1.2 and Definition 1.3 of the preceding lesson. Every distinguished triangle is isomorphic to some \(T_f\), and \(F\) preserves isomorphisms of triangles. \(\square\)

## 2. The Dold–Puppe sequences

**Proposition 2.1.** Let \(x\xrightarrow uy\xrightarrow vz\xrightarrow w\Sigma x\) be distinguished. Then the sequence

\[
\begin{aligned}
&\cdots\to\Sigma^{-1}z\xrightarrow{-\Sigma^{-1}w}x\xrightarrow uy\xrightarrow vz\\
&\quad\xrightarrow w\Sigma x\xrightarrow{-\Sigma u}\Sigma y\xrightarrow{-\Sigma v}\Sigma z\to\cdots,
\end{aligned}
\]

in which each map is \(-\Sigma\) of the map three places earlier, has every three consecutive maps forming a distinguished triangle. For every object \(T\) the functors \(\operatorname{Hom}(T,-)\) and \(\operatorname{Hom}(-,T)\) turn it into long exact sequences of abelian groups.

**Proof.** The triangles are the iterated rotations in both directions (Theorem 3.1 of the preceding lesson). Exactness of \(\operatorname{Hom}(T,-)\) is Lemma 3.3 there, applied to each rotation. For \(\operatorname{Hom}(-,T)\): composites of consecutive maps vanish. If \(b:y\to T\) satisfies \(bu=0\), the triangle \(0\to T\xrightarrow1T\to0\), a rotation of the identity triangle of \(T\), and the square formed by \(u\), \(0\to T\) and the verticals \(0\) and \(b\), give by extension of squares a map \(c:z\to T\) with \(cv=b\). So \(\operatorname{Hom}(z,T)\to\operatorname{Hom}(y,T)\to\operatorname{Hom}(x,T)\) is exact, and rotation gives exactness everywhere. \(\square\)

For the derivator of a ring and \(T\) the ring placed in degree \(0\), these are the long exact cohomology sequences, since \(\operatorname{Hom}_{D(R)}(R,x[n])\cong H^n(x)\).

## 3. Comparison for the derivator of a ring

Let \(R\) be a ring and \(\mathbb D_R\) its derivator, strong by Theorem 4.1 and stable by Theorem 5.3 of the lessons on the derivator of a ring and on pointed and stable derivators. On \(D(R)=\mathbb D_R(e)\) there are two triangulated structures: the canonical one, with suspension \(\Sigma\), and the classical one, with shift \([1]\) and the triangles isomorphic to cone triangles

\[
P_0\xrightarrow{u}P_1\xrightarrow{i}C(u)\xrightarrow{-p}P_0[1]
\]

as in (2.2) and Theorem 5.1 of *Complexes, cones and localization*. Here \(C(u)^n=P_1^n\oplus P_0^{n+1}\) with \(d(l,k)=(dl+uk,-dk)\), \(i(l)=(l,0)\), \(p(l,k)=k\), and \(P[1]\) has differential \(-d\).

**The identification \(\xi\).** Let \(x\) be represented by a semifree complex \(P\), and let \(\jmath:P\to C(1_P)\) be the inclusion into the cone of the identity, which is contractible. The span \(C(1_P)\xleftarrow{\jmath}P\xrightarrow{\jmath}C(1_P)\), with the first copy at \((1,0)\) and the second at \((0,1)\), represents \((0,0)_*x\), and it is semifree, so the suspension square of \(x\) is its pushout square. Write elements of the pushout \(C(1_P)\sqcup_PC(1_P)\) as \([a,b]\), with \(a=(l_A,k_A)\) and \(b=(l_B,k_B)\) in \(C(1_P)=P\oplus P[1]\). Corollary 5.4 of the lesson on pointed and stable derivators identifies \(\Sigma x\) with \(x[1]\) through the roof formed by two quasi-isomorphisms out of the cone of \(\varphi=(\jmath,-\jmath):P\to C(1_P)\oplus C(1_P)\):

\[
\begin{gathered}
C(\varphi)\to C(1_P)\sqcup_PC(1_P),\\
(a,b,y)\mapsto[a,b],
\end{gathered}
\]
\[
C(\varphi)\to P[1],\quad(a,b,y)\mapsto y .
\]

Call this isomorphism \(\xi_x:\Sigma x\to x[1]\).

**Lemma 3.1.** \(\xi_x\) is represented by the chain map \(\rho:[a,b]\mapsto k_B\) from the pushout to \(P[1]\), and \(-\xi_x\) by \([a,b]\mapsto k_A\).

**Proof.** \(\rho\) is well defined, since the two copies of \(l\in P\) both have zero second coordinate, and it is a chain map. Its composite with \(C(\varphi)\to C(1_P)\sqcup_PC(1_P)\) is \((a,b,y)\mapsto k_B\). In \(C(\varphi)\) the differential is

\[
d(a,b,y)=\bigl(d a+\jmath y,\;d b-\jmath y,\;-dy\bigr),
\]

whose \(P\)-coordinate in the second summand is \(dl_B+k_B-y\). The map \(h(a,b,y)=l_B\), of degree \(-1\) into \(P[1]\), satisfies

\[
\begin{aligned}
dh+hd&=-dl_B+(dl_B+k_B-y)\\
&=k_B-y,
\end{aligned}
\]

so \((a,b,y)\mapsto k_B\) and \((a,b,y)\mapsto y\) are homotopic. For the second statement, \(h'([a,b])=l_A+l_B\) gives \(dh'+h'd=k_A+k_B\) on the pushout, so \(k_A\) and \(-k_B\) are homotopic. \(\square\)

**Theorem 3.2.** Let \(f\) in \(\mathbb D_R([1])\) be represented by a chain map \(u:P_0\to P_1\) of semifree complexes that is injective and split in each degree. Then \((1,1,1,\xi)\) is an isomorphism from \(T_f\) to

\[
P_0\xrightarrow uP_1\xrightarrow iC(u)\xrightarrow pP_0[1].
\]

Consequently a triangle \((u,v,w)\) of \(D(R)\) is distinguished for the canonical structure if and only if \((u,v,-\xi w)\) is distinguished for the classical structure. The identity functor of \(D(R)\), with the natural isomorphism \(-\xi:\Sigma\to[1]\), is an isomorphism of triangulated categories.

**Proof.** *A model of the cofibre diagram.* Consider the diagram of complexes on \([2]\times[1]\)

\[
\begin{array}{ccccc}
P_0&\xrightarrow{u}&P_1&\longrightarrow&C(1_{P_1})\\
\downarrow&&\downarrow&&\downarrow\\
C(1_{P_0})&\longrightarrow&C(u)&\longrightarrow&Z
\end{array}
\]

where the vertical maps out of \(P_0\) and \(P_1\) are the inclusions \(\jmath\) and \(i\), the map \(C(1_{P_0})\to C(u)\) is \((l,k)\mapsto(ul,k)\), and \(Z=C(u)\sqcup_{P_1}C(1_{P_1})\). The left square is a pushout: \(C(u)\) is the quotient of \(P_1\oplus C(1_{P_0})\) by the image of \(P_0\), and the differential of \(C(1_{P_0})\) becomes that of \(C(u)\). Both squares are pushouts along maps that are injective and split in each degree. For such a square the map from the cone \(C(\varphi)\) of Lemma 5.1 of the lesson on pointed and stable derivators to the pushout is a quasi-isomorphism (proof of Proposition 5.2 of *Complexes, cones and localization*), so the total complex is acyclic and the square is cocartesian and cartesian (Theorem 5.3 of the lesson on pointed and stable derivators). The values \(C(1_{P_1})\) and \(C(1_{P_0})\) are contractible. So the diagram is a cofibre diagram whose restriction to \((0,0)\to(1,0)\) represents \(f\), and by Lemma 1.2 of the preceding lesson its triangle is isomorphic to \(T_f\) through an isomorphism that is the identity on the first two objects.

*The identification \(\iota\).* Write elements of \(Z\) as \((l,k,m)\) with \(l\in P_1\), \(k\in P_0[1]\) and \(m\in P_1[1]\); its differential is \(d(l,k,m)=(dl+uk+m,-dk,-dm)\). The suspension square of \(P_0\), with legs \(C(1_{P_0})\), maps to the composite square of the diagram by the identity at \((0,0)\), by \((l,k)\mapsto(ul,uk)\) into \(C(1_{P_1})\) at \((1,0)\), and by the identity at \((0,1)\); the induced map of pushouts is

\[
\psi:[a,b]\longmapsto\bigl(u(l_A+l_B),\,k_B,\,uk_A\bigr).
\]

By naturality of \(\iota\), \(\psi\) represents \(\iota_Y\) composed with the inverse of the identification of the pushout with \(\Sigma P_0\). The chain map \(\rho':Z\to P_0[1]\), \((l,k,m)\mapsto k\), satisfies \(\rho'\psi=\rho\), so by Lemma 3.1, \(\rho'\) represents \(\xi\circ\iota_Y^{-1}\). It is a quasi-isomorphism, with contractible kernel \(C(1_{P_1})\).

*The third map.* The third map of the triangle is \(w=\iota_Y^{-1}\circ(C(u)\to Z)\), and \(C(u)\to Z\) is \((l,k)\mapsto(l,k,0)\). Hence \(\xi w\) is represented by \(\rho'(l,k,0)=k\), that is, by \(p\). This proves the isomorphism \((1,1,1,\xi)\).

*Comparison of the two classes.* By Theorem 4.1 of the lesson on the derivator of a ring and its proof, every object of \(\mathbb D_R([1])\) is represented by such a \(u\), and every morphism of \(D(R)\) is isomorphic to the underlying arrow of one. So the canonical distinguished triangles are, up to isomorphism, the triangles \((u,i,\xi^{-1}p)\), and the classical ones are, up to isomorphism, the triangles \((u,i,-p)\) (Theorem 5.1 of *Complexes, cones and localization*). Both classes are closed under isomorphism, and \((u,i,\xi^{-1}p)\) is sent to \((u,i,-p)\) by composing its third map with \(-\xi\). \(\square\)

Two conventions meet here. *Complexes, cones and localization* puts a sign on the cone projection so that a short exact sequence produces the boundary map of the snake lemma. The derivator puts no sign anywhere, and its suspension square has two legs. Identifying \(\Sigma x\) with \(x[1]\) through the vertical leg gives \(\xi\), and through the horizontal leg gives \(-\xi\) (Lemma 3.1); the two differ by the flip of the suspension. The classical convention corresponds to the horizontal leg. With \(\xi\) instead, every connecting map changes sign, and the canonical triangles become the triangles \((u,v,-w)\) of the classical structure.

## 4. Exercises

**4.1** (medium). Let \(f\) in \(\mathbb D_{\mathbb Z}([1])\) be represented by multiplication by \(2\) on \(\mathbb Z\), a complex concentrated in degree \(0\). Show that the third object of \(T_f\) is isomorphic to \(\mathbb Z/2\) in degree \(0\), and that the third map is the nonzero element of \(\operatorname{Hom}_{D(\mathbb Z)}(\mathbb Z/2,\Sigma\mathbb Z)\cong\mathbb Z/2\).

**4.2** (easy). Let \(0\to K\to L\to M\to0\) be a sequence of complexes of \(R\)-modules that is split exact in each degree, with boundary \(\delta:M\to K[1]\) as in Lemma 2.2 of *Complexes, cones and localization*. Show that \(K\to L\to M\xrightarrow{(-\xi)^{-1}\delta}\Sigma K\) is a canonical distinguished triangle of \(\mathbb D_R\).

**4.3** (medium). Show that the functor \(\operatorname{hocolim}_{[1]}:\mathbb D([1])\to\mathbb D(e)\) is exact, and identify it with evaluation at \(1\).

**4.4** (medium). Show that the cofibre functor \(\operatorname{cof}:\mathbb D([1])\to\mathbb D(e)\) is exact, and that for every \(f\) the sequence \(f_0\to f_1\to\operatorname{cof}(f)\to\Sigma f_0\) of Definition 1.3 of the preceding lesson is natural in \(f\).

**4.5** (hard). Let \(J\) be a small category. Prove the analogue of Theorem 3.2 for \(\mathbb D_R(J)=D(\operatorname{Mod}_R^J)\), with its classical triangulated structure.

## 5. Solutions

**4.1.** A semifree model of \(f\) on \([1]\): generators \(a\) at \(0\) and \(b\) at \(1\) in degree \(0\), mapped to \(1\) and \(1\), and a generator \(c\) at \(1\) in degree \(-1\) with \(dc=a-2b\). Its value at \(0\) is \(P_0=\mathbb Za\); its value at \(1\) is \(P_1\), with \(\mathbb Zc\) in degree \(-1\) and \(\mathbb Za\oplus\mathbb Zb\) in degree \(0\). The map \(P_1\to\mathbb Z\), \(a\mapsto2\), \(b\mapsto1\), is a quasi-isomorphism, and the inclusion \(u':P_0\to P_1\) is split injective and corresponds to multiplication by \(2\). By Theorem 3.2 the third object is \(C(u')\): \(\mathbb Zc\oplus\mathbb Za'\) in degree \(-1\) and \(\mathbb Za\oplus\mathbb Zb\) in degree \(0\), with \(c\mapsto a-2b\) and \(a'\mapsto a\). Its cohomology is \(\mathbb Z/2\), generated by \(b\), in degree \(0\), and zero elsewhere.

The group \(\operatorname{Hom}_{D(\mathbb Z)}(\mathbb Z/2,\Sigma\mathbb Z)\), isomorphic to \(\operatorname{Hom}_{D(\mathbb Z)}(\mathbb Z/2,\mathbb Z[1])\), is computed on the semifree resolution \(\mathbb Z\xrightarrow2\mathbb Z\) of \(\mathbb Z/2\) in degrees \(-1,0\): chain maps to \(\mathbb Z[1]\) are given by any integer in degree \(-1\), and homotopies change it by even integers, so the group is \(\mathbb Z/2\). Similarly \(\operatorname{Hom}_{D(\mathbb Z)}(\mathbb Z/2,\mathbb Z)=0\). If the third map \(w\) were zero, exactness of \(\operatorname{Hom}(z,y)\to\operatorname{Hom}(z,z)\to\operatorname{Hom}(z,\Sigma x)\) (Lemma 3.3 of the preceding lesson), with \(z\cong\mathbb Z/2\) and \(y\cong\mathbb Z\), would make \(1_z\) factor through \(\operatorname{Hom}(\mathbb Z/2,\mathbb Z)=0\), so \(z\cong0\), which is false. So \(w\) is the nonzero element; in a group of order two the sign conventions of Section 3 do not matter.

**4.2.** By Lemma 2.2 of *Complexes, cones and localization*, the triangle \(K\to L\to M\xrightarrow{\delta}K[1]\) is isomorphic in the homotopy category to the cone triangle (2.2) of \(K\to L\), hence classically distinguished. By Theorem 3.2, \((K\to L,\;L\to M,\;(-\xi)^{-1}\delta)\) is canonically distinguished.

**4.3.** It is \(p_!\) for \(p:[1]\to e\), exact by Proposition 1.2. Since \(1\) is terminal in \([1]\), \(1:e\to[1]\) is right adjoint to \(p\), so \(p_!\cong1^*\) (Proposition 2.3 and Corollary 2.4 of the lesson on homotopy exact squares).

**4.4.** \(\operatorname{cof}=(1,1)^*i_{\ulcorner!}k_*\), with \(k:[1]\to\ulcorner\) the sieve onto \((0,0)\to(1,0)\). Each factor is exact by Proposition 1.2, and a composite of exact functors is exact, with the composite of the isomorphisms \(\theta\). Naturality of the sequence follows from the naturality of \(Y_f\) in \(f\) and of \(\iota\).

**4.5.** Objects of \(\mathbb D_R^J([1])=D(\operatorname{Mod}_R^{J\times[1]})\) are represented by semifree complexes on \(J\times[1]\) (Theorem 2.1 of the lesson on the derivator of a ring), which are arrows \(u:P_0\to P_1\) of complexes in \(\operatorname{Mod}_R^J\), split injective in each degree, with \(P_0\) and \(P_1\) built from representable functors (proof of Theorem 4.1 there). Form the diagram of the proof of Theorem 3.2 in \(\operatorname{Mod}_R^J\). At each object of \(J\) its squares are pushouts along split injections, hence cocartesian by Theorem 5.3 of the lesson on pointed and stable derivators, so they are cocartesian in \(\mathbb D_R^J\) by Corollary 3.2 of the lesson on recognizing cocartesian squares; the values at \((2,0)\) and \((0,1)\) are contractible. Lemma 3.1 holds with the same formulas, which are natural in \(J\), and so does the computation of \(\rho'\). Hence \(T_f\) is isomorphic to \((u,i,\xi^{-1}p)\), and the cone triangles (2.2) of the abelian category \(\operatorname{Mod}_R^J\) define its classical structure.

## Sources

- [Gr] M. Groth, *Derivators, pointed derivators and stable derivators*, Algebraic & Geometric Topology 13 (2013), 313–374; arXiv:1112.3840. https://arxiv.org/abs/1112.3840 — Section 4.2: exact morphisms of stable derivators, and the exactness of restriction and homotopy Kan extensions. The comparison with the classical triangles of \(D(R)\), including the sign, is worked out in this lesson.
- [PS] A. Grothendieck, *Pursuing Stacks*, §69, arXiv:2111.01000. https://arxiv.org/abs/2111.01000 — the expectation that the two Dold–Puppe sequences and the triangulated structure follow formally from the derivator.
