# Complexes, cones and localization

*Written and edited by GPT-6.1 Sol (OpenAI), in Codex at Ultra, October 2026. Mathematically self-checked by the writing AI. Original contributions are CC0; the combined course is distributed under GFDL-1.2-or-later. Full authorship and source attribution appear in the course notice.*

An exact sequence contains more information than its three objects: it specifies how a quotient attaches to a subobject. A complex contains still more attachment information, in each degree. Mapping cones retain that information when a map is replaced by a triangle. Localization then lets us compare complexes that have the same cohomology without requiring a chain homotopy equivalence between them.

This common reading precedes the resolution lessons. Its algebra prerequisite is Wen-Wei Li’s *Methods of Algebra, Volume 2*: [“Definition of an Abelian Category”](https://kokunoyumeto.github.io/methods-of-algebra-volume-2-en/#unit-chapter2-unit-021), and [“Some Diagram Lemmas”](https://kokunoyumeto.github.io/methods-of-algebra-volume-2-en/#unit-chapter2-unit-023), especially the exactness criterion by epimorphic lifting, the Snake Lemma and the Five Lemma. [“Complexes on an Abelian Category”](https://kokunoyumeto.github.io/methods-of-algebra-volume-2-en/#unit-chapter3-unit-037) proves the long exact cohomology sequence using that Snake Lemma. We recall its construction here and supply the cone and localization arguments in full.

The cone and triangulation arguments follow the Stacks project authors’ *Derived Categories*, in the [AI Integrated Stacks Project edition](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/derived.tex). We develop localization by roofs and common refinements, then prove that cone triangles descend to the derived category. Source attribution and the licence for adapted passages appear in the course notice.
## 1. Maps of complexes and homotopies

Let \(\mathcal A\) be an abelian category. A **cochain complex** \(K\) consists of objects \(K^n\) and differentials \(d_K^n:K^n\to K^{n+1}\) satisfying \(d_K^{n+1}d_K^n=0\). A chain map \(f:K\to L\) satisfies \(d_Lf=fd_K\). Its cohomology is

\[
H^n(K)=\ker(d_K^n)/\operatorname{im}(d_K^{n-1}).
\]

We set \(K[r]^n=K^{n+r}\), with differential \((-1)^r d_K\). A homotopy from \(g\) to \(f\) is a family \(s^n:K^n\to L^{n-1}\) with \(f-g=d_Ls+sd_K\). These homotopies form an equivalence relation: zero, negation and addition give reflexivity, symmetry and transitivity. Precomposing or postcomposing a homotopy with a chain map gives a homotopy of composites. Thus homotopy classes form an additive category \(K(\mathcal A)\), with the same objects as the category of complexes. Its finite sums and zero object are those of complexes. A **homotopy equivalence** is an isomorphism in this category. A complex is **contractible** when its identity is null-homotopic.

The group-valued Hom complex, as distinct from an internal sheaf Hom, is

\[
\operatorname{Hom}^{r}(K,L)=\prod_{n\in\mathbb Z}
\operatorname{Hom}_{\mathcal A}(K^n,L^{n+r}),\qquad
D(h)=d_Lh-(-1)^rhd_K.
\tag{1.1}
\]

**Lemma 1.1.** Formula (1.1) defines a complex of abelian groups, and

\[
H^r\operatorname{Hom}^{\bullet}(K,L)
=\operatorname{Hom}_{K(\mathcal A)}(K,L[r]).
\tag{1.2}
\]

**Proof.** Applying the differential twice cancels the two terms involving \(d_Lhd_K\); the other terms vanish because \(d_L^2=d_K^2=0\). A degree-\(r\) family is a cocycle precisely when \(d_Lh=(-1)^rhd_K\), which is the chain-map equation into \(L[r]\). If \(h=D(v)\) with \(v\) of degree \(r-1\), then

\[
h=d_Lv+(-1)^rvd_K
=d_{L[r]}\bigl((-1)^rv\bigr)+\bigl((-1)^rv\bigr)d_K.
\]

So boundaries are exactly the null-homotopic maps into \(L[r]\). Conversely a homotopy \(s\) gives the boundary of \((-1)^rs\). This proves (1.2). Composition of homogeneous families obeys

\[
D(gh)=D(g)h+(-1)^{\deg g}gD(h):
\]

expanding the right side cancels its two middle terms and leaves \(d_Mgh-(-1)^{\deg g+\deg h}ghd_K\). In particular composition descends to cohomology and hence to the homotopy category. \(\square\)

**Lemma 1.2 (cohomology of a short exact sequence).** A degreewise short exact sequence \(0\to A\xrightarrow{a}B\xrightarrow{b}C\to0\) has a natural long exact cohomology sequence. Homotopic maps induce the same cohomology map.

**Proof.** For the second assertion, on \(\ker d_K^n\) the summand \(sd_K\) vanishes and \(d_Ls\) has image in \(\operatorname{im}d_L^{n-1}\). It therefore induces zero on cohomology.

For the first assertion, apply the Snake Lemma to the exact rows

\[
\operatorname{coker}d_A^{n-2}\longrightarrow
\operatorname{coker}d_B^{n-2}\longrightarrow
\operatorname{coker}d_C^{n-2}\longrightarrow0,
\]

\[
0\longrightarrow\ker d_A^n\longrightarrow
\ker d_B^n\longrightarrow\ker d_C^n,
\]

whose vertical maps are induced by \(d^{n-1}\). The kernels of these vertical maps are \(H^{n-1}\); their cokernels are \(H^n\). The first row is right exact by the cokernel part of the Snake Lemma applied to the degreewise exact diagram with vertical maps \(d^{n-2}\); the second is left exact by its kernel part for \(d^n\). Thus the new Snake Lemma sequence joins \(H^{n-1}(C)\) to \(H^n(A)\) and gives exactly the six consecutive terms of the cohomology sequence. Varying \(n\) joins the sequences. Naturality follows from the naturality of the Snake Lemma construction by kernels, cokernels and pullbacks.

In modules, its boundary has the familiar precise description: lift a cocycle \(c\) to \(b\), write \(d_Bb=a(a')\), and send \([c]\) to \([a']\). A changed lift adds a boundary, and a changed cocycle by a boundary also changes \(a'\) by a boundary. In an arbitrary abelian category these lifts are performed after pullback along an epimorphism, as in the exactness criterion in the prerequisite; the kernel and cokernel description just given supplies the resulting canonical morphism. \(\square\)

A **quasi-isomorphism** is a map inducing an isomorphism on every cohomology object. A complex is **acyclic** when all its cohomology objects vanish. A homotopy equivalence is a quasi-isomorphism by Lemma 1.2, but an acyclic complex need not be contractible.

## 2. Cones and triangles from split sequences

For \(f:K\to L\), define

\[
C(f)^n=L^n\oplus K^{n+1},\qquad
d(l,k)=(d_Ll+fk,-d_Kk).
\tag{2.1}
\]

Squaring this differential gives zero because \(f\) is a chain map. Let \(i:L\to C(f)\) be inclusion and \(p:C(f)\to K[1]\) projection. Our **cone triangle** is

\[
K\xrightarrow fL\xrightarrow iC(f)\xrightarrow{-p}K[1].
\tag{2.2}
\]

The minus sign is intentional. With this convention, a triangle attached to a short exact sequence has the Snake Lemma's positive boundary.

**Lemma 2.1 (comparison of cones).** If \(bf-f'a=d h+h d\), the maps

\[
c^n=\begin{pmatrix}b^n&h^{n+1}\\0&a^{n+1}\end{pmatrix}:
C(f)^n\longrightarrow C(f')^n
\]

give a morphism of cone triangles in \(K(\mathcal A)\).

**Proof.** The diagonal entries of \(d c=c d\) are the chain-map equations for \(a,b\). Equality of the upper-right entries is \(d h+f'a=bf-hd\), exactly the assumed homotopy equation. The lower-left entries are zero. Also \(c i=i'b\) and \(p'c=a[1]p\) hold already as chain maps. This proves all triangle squares, including the one with negative projections. The choice of \(h\) need not be unique; the third triangle map is not canonically determined by a square in the homotopy category. \(\square\)

**Lemma 2.2 (split sequences).** Suppose \(0\to A\to B\to C\to0\) is split in each degree. Write

\[
B^n=A^n\oplus C^n,\qquad
d_B=\begin{pmatrix}d_A&\delta\\0&d_C\end{pmatrix}.
\tag{2.3}
\]

Then \(\delta:C\to A[1]\) is a chain map, and the triangle \(A\to B\to C\xrightarrow\delta A[1]\) is isomorphic to the cone triangle of \(A\to B\).

**Proof.** The upper-right entry of \(d_B^2=0\) is \(d_A\delta+\delta d_C=0\), the asserted chain-map equation. In degree \(n\), the cone of inclusion is \(A^n\oplus C^n\oplus A^{n+1}\). Define

\[
r(a,c,a')=c,\qquad t(c)=(0,c,-\delta c).
\]

Both are chain maps by (2.3), and \(rt=1\). The homotopy \(H(a,c,a')=(0,0,a)\), landing in degree \(n-1\), satisfies

\[
(dH+Hd)(a,c,a')=(a,0,a'+\delta c)=(1-tr)(a,c,a').
\]

Thus \(r,t\) are inverse in \(K\). Inclusion of \(B\) is carried to its quotient map into \(C\), and \((-p)t=\delta\). These give the claimed triangle isomorphism. Formula (2.3) also shows that \(H^n(\delta)\) is exactly the boundary constructed in Lemma 1.2. \(\square\)

**Lemma 2.3 (replacement by a split injection).** Every map \(f:K\to L\) factors as a degreewise split injection \(K\to\widetilde L\) followed by a homotopy equivalence \(\widetilde L\to L\). A finite string of maps can be replaced by degreewise split injections, with a commuting diagram of homotopy equivalences to the original string.

**Proof.** Put \(\widetilde L=L\oplus C(1_K)\), with degree-\(n\) coordinates \((l,k,k')\), differential \((d_Ll,d_Kk+k',-d_Kk')\), and injection \(k\mapsto(fk,k,0)\). Projection \(\pi\) to \(L\) has chain-map section \(s(l)=(l,0,0)\). The homotopy \(H(l,k,k')=(0,0,k)\) gives

\[
(dH+Hd)(l,k,k')=(0,k,-d_Kk)+(0,0,d_Kk+k')=(0,k,k')=1-s\pi.
\]

The injection is split by projection onto \(K^n\). For a string, start with its first object, perform this construction on the first map, then on the composite from the new second object to the original third object, and continue. Every resulting square commutes as a square of chain maps. Shifts and these replacements preserve boundedness above, below, or in both directions. \(\square\)

**Lemma 2.4 (representable exactness and cone uniqueness).** For a cone triangle, applying \(\operatorname{Hom}_K(T,-)\) or \(\operatorname{Hom}_K(-,T)\) gives a long exact sequence after shifts. A morphism of cone triangles which is an isomorphism on two objects is an isomorphism on the third.

**Proof.** There is a chain isomorphism

\[
\operatorname{Hom}^{\bullet}(T,C(f))
=C\bigl(\operatorname{Hom}^{\bullet}(T,f)\bigr).
\]

It follows by distributing products over the two summands in (2.1); its differential has exactly the matrix (2.1). For the contravariant version put \(U=\operatorname{Hom}^{\bullet}(L,T)\), \(V=\operatorname{Hom}^{\bullet}(K,T)\), and \(u=f^*:U\to V\). A degree-\(r\) map from the cone has coordinates \((a,b)\in U^r\oplus V^{r-1}\) and differential

\[
(a,b)\longmapsto\bigl(Da,Db+(-1)^{r+1}u(a)\bigr).
\]

The map \((a,b)\mapsto((-1)^{r-1}b,a)\) identifies this complex with \(C(u)[-1]\), whose differential is \((v,a)\mapsto(-Dv-u(a),Da)\). Lemma 1.2 for these group complexes and Lemma 1.1 give both exact sequences. Signs of individual arrows do not change exactness.

For a morphism of triangles, apply either representable functor and take five consecutive terms with the possibly unknown map in the middle. The four surrounding maps are isomorphisms when the other two object maps are isomorphisms. The Five Lemma makes the middle map an isomorphism for every \(T\). If \(c:Z\to Z'\) induces bijections \(\operatorname{Hom}(T,Z)\to\operatorname{Hom}(T,Z')\) for every \(T\), surjectivity for \(T=Z'\) gives a right inverse \(v\), and injectivity for \(T=Z\) gives \(vc=1\). Thus \(c\) is an isomorphism. Rotating the exact sequences proves the assertion for any two object maps. In particular cones of a fixed morphism are unique up to an isomorphism fixing its first two objects. Lemma 2.1 gives existence of that comparison, and this argument gives invertibility. \(\square\)

## 3. The triangulated structure of the homotopy category

A triangle means \(X\xrightarrow fY\xrightarrow gZ\xrightarrow hX[1]\). It is **distinguished** in \(K(\mathcal A)\) when it is isomorphic to (2.2). A triangulated category is an additive category with an additive shift equivalence and distinguished triangles satisfying four requirements: identity and completion triangles exist and are closed under isomorphism; rotation \((f,g,h)\mapsto(g,h,-f[1])\) preserves distinguished triangles in both directions; a commuting square between their first maps extends to a morphism of triangles; and composable maps have compatible cone triangles forming an octahedron. We give the exact octahedron maps in the proof, rather than using a picture as an axiom.

**Theorem 3.1.** These definitions make \(K(\mathcal A)\) a triangulated category. The full subcategories of bounded-below, bounded-above and bounded complexes are triangulated.

**Proof.** The isomorphism and completion requirements follow from the definition. The cone \(C(1_X)\) is contractible by Lemma 2.3, so its cone triangle is isomorphic to \(X\xrightarrow1X\to0\to X[1]\).

For rotation, \(0\to L\to C(f)\to K[1]\to0\) is split in each degree, with off-diagonal map \(f[1]\). By Lemma 2.2 its triangle \((i,p,f[1])\) is distinguished. Changing the sign on its third object identifies it with \((i,-p,-f[1])\), the rotation of (2.2). Conversely, suppose a rotated triangle is represented by a split sequence \(0\to A\to B\to C\to0\) with boundary \(\delta\). The inverse rotation is \(C[-1]\xrightarrow{-\delta[-1]}A\to B\to C\). Formula (2.3) identifies \(B\) with \(C(-\delta[-1])\) by the map \((a,c)\mapsto(a,-c)\); its projection into \(C\) becomes the negative cone projection. Hence this inverse rotation is distinguished. Every cone triangle has a split-sequence representative: use Lemma 2.3 on its first map, Lemma 2.1 and Lemma 2.4 to compare cones, and Lemma 2.2 on the new split injection. Thus the converse applies to all distinguished triangles.

The square-extension requirement is precisely Lemma 2.1 after replacing the rows by cone triangles.

For the octahedron take composable maps \(A\xrightarrow\alpha B\xrightarrow\beta C\). Lemma 2.3 replaces this string by degreewise split injections. Lemmas 2.1, 2.2 and 2.4 identify their three cone triangles with the triangles of the three quotient sequences. Choose degreewise decompositions \(B=A\oplus Q_1\) and \(C=A\oplus Q_1\oplus Q_3\). Their differentials have the forms

\[
d_B=\begin{pmatrix}d_A&u\\0&d_1\end{pmatrix},\qquad
d_C=\begin{pmatrix}d_A&u&v\\0&d_1&w\\0&0&d_3\end{pmatrix}.
\tag{3.1}
\]

Set \(Q_2=C/A=Q_1\oplus Q_3\), with differential \(\left(\begin{smallmatrix}d_1&w\\0&d_3\end{smallmatrix}\right)\). The three boundary maps are \(u\), \((u,v)\), and \((v,w)\). The split sequence \(0\to Q_1\to Q_2\to Q_3\to0\) has boundary \(w\), so its triangle is distinguished. Its first two maps are inclusion \(a:Q_1\to Q_2\) and projection \(b:Q_2\to Q_3\). The triples \((1_A,\beta,a)\) and \((\alpha,1_C,b)\) are morphisms of the three original triangles. All their squares commute strictly except possibly the second boundary square. The difference

\
(v,w)b-\alpha[1=\begin{pmatrix}-u&0\\0&w\end{pmatrix}
\]

is the homotopy boundary for \(H:Q_2^n\to B[1]^{n-1}=B^n\), \(H(q_1,q_3)=(0,q_1)\): substituting (3.1) into \(d_{B[1]}H+Hd_{Q_2}\) gives \((-u q_1,w q_3)\). Finally \(w=p_11\), where \(p_1:B\to Q_1\). Thus

\[
Q_1\xrightarrow aQ_2\xrightarrow bQ_3
\xrightarrow{p_1[1]\delta_3}Q_1[1]
\]

is the required fourth triangle, with exactly the required comparison maps. Transport this diagram through the homotopy equivalences of the string. For any initially chosen distinguished triangles of the three maps, Lemma 2.4 compares them by isomorphisms fixing their first two objects. Transport through those too. This proves the full octahedron requirement, not only a special choice of cones.

All complexes, shifts, cones and replacements used here preserve each stated boundedness condition. The same proof therefore works in the three bounded homotopy categories. \(\square\)

**Corollary 3.2.** An additive functor \(\Phi:\mathcal A\to\mathcal B\) induces a triangulated functor on homotopy categories. A quasi-isomorphism \(f\) is characterized by acyclicity of \(C(f)\).

**Proof.** Applying \(\Phi\) degreewise preserves differentials, homotopies, shifts, finite sums and every entry of (2.1), hence cone triangles. For the second assertion apply Lemma 1.2 to \(0\to L\to C(f)\to K[1]\to0\); its connecting map is \(H(f[1])\). Exactness proves that the middle complex is acyclic exactly when each \(H^n(f)\) is invertible. \(\square\)

## 4. Fractions at quasi-isomorphisms

We work in a larger universe if necessary: objects and arrows from the chosen small-module universe form sets in that larger universe. This makes the following constructions legitimate before proving that the derived Hom sets are small in the original universe. The resolution lessons will establish that stronger smallness conclusion for module sheaves.

Let \(S\) be the quasi-isomorphisms in \(K(\mathcal A)\). It contains identities, is closed under composition, and has the two-out-of-three property, because these assertions hold for isomorphisms after every \(H^n\).

**Lemma 4.1 (fraction squares and cancellation).** Given \(f:M\to Y\) and \(t:N\to Y\) with \(t\in S\), there are \(r:P\to M\) in \(S\) and \(a:P\to N\) with \(fr=ta\) in \(K\). If \(tf=tg\) for \(t:Y\to Z\) in \(S\), there is \(r:P\to X\) in \(S\) with \(fr=gr\). The dual assertions, with all arrows reversed, also hold.

**Proof.** For the square take \(P=C((f,-t):M\oplus N\to Y)[-1]\). Its coordinates in degree \(n\) are \((y,m,n')\), with differential \((-d_Yy-fm+tn',d_Mm,d_Nn')\). Let \(r,a\) be projections to \(m,n'\). Their required equality holds up to the homotopy \((y,m,n')\mapsto-y\). The kernel of \(r\) is \(C(-t)[-1]\), which is acyclic by Corollary 3.2. Since \(r\) is degreewise split onto, Lemma 1.2 makes \(r\) a quasi-isomorphism. This proves the square assertion.

For cancellation put \(v=f-g\). Choose a homotopy \(tv=d_Zh+hd_X\). The map \((-h,v):X\to C(t)[-1]\) is a chain map: its first component's chain-map equation is \(d_Zh-tv=-hd_X\), exactly the chosen homotopy equation. Its second component projects to \(v\). Write this map as \(e:X\to E\), where \(E=C(t)[-1]\) is acyclic. Projection \(r:C(e)[-1]\to X\) is a quasi-isomorphism, since its kernel \(E[-1]\) is acyclic. Moreover \(er\) is null-homotopic by projection onto the first cone coordinate with a minus sign, exactly as in the square computation. Therefore \(vr=0\).

For the dual square take the cone of \((t,-f):M\to N\oplus Y\); the inclusion of \(Y\) has acyclic quotient \(C(t)\), and the two composites agree up to the cone's homotopy. For the dual cancellation, representable exactness in Lemma 2.4 factors a map \(v\) satisfying \(vt=0\) through the acyclic cone \(C(t)\). If this factor is \(e:C(t)\to Z\), the inclusion \(Z\to C(e)\) is a quasi-isomorphism and kills \(e\) up to homotopy. It consequently kills \(v\). These are the asserted reversed constructions. \(\square\)

A **roof** from \(X\) to \(Y\) is \(X\xleftarrow{s}M\xrightarrow{f}Y\), with \(s\in S\). Declare two roofs equivalent if they have a common refinement: maps \(u:P\to M\), \(v:P\to M'\) such that \(su=s'v\in S\) and \(fu=f'v\). Two-out-of-three then implies \(u,v\in S\).

**Theorem 4.2 (localization).** Roof classes form a category \(D(\mathcal A)\). The map \(Q:K(\mathcal A)\to D(\mathcal A)\), \(f\mapsto(1,f)\), inverts quasi-isomorphisms and is their localization. Its morphism sets are abelian groups, and \(Q\) is additive. Moreover \(Qf=Qg\) if and only if \(fr=gr\) for some quasi-isomorphism \(r\) into their common source.

**Proof.** Equivalence is reflexive and symmetric. For transitivity, two refinements through a middle roof give two quasi-isomorphisms into its middle object. Lemma 4.1 gives a common square; two-out-of-three makes both new arrows quasi-isomorphisms. Composing the refinements gives the third required refinement. Thus the relation is transitive.

Compose roofs \((s,f):X\to Y\) and \((t,g):Y\to Z\) by using Lemma 4.1 to choose \(r:P\to M\) in \(S\) and \(a:P\to N\) with \(fr=ta\), and set the composite to \((sr,ga)\). Two choices \((r,a)\), \((r',a')\) have a common refinement of \(r,r'\). On it, \(ta=ta'\); cancellation in Lemma 4.1 refines once more to make \(a=a'\). Their resulting roofs are therefore equivalent. Replacing the first roof by a refinement is handled by a common square between its refinement arrow and \(r\); replacing the second by a refinement is handled by a square between \(a\) and that refinement arrow. Each produces precisely a refinement of the original composite. Since any two equivalent roofs admit such refinements, composition is well defined.

For associativity take three roofs \((s,f),(t,g),(u,h)\). First form a square \(g r=u b\), with \(r:P\to N\) in \(S\). Next form \(f r'=t r c\), with \(r':P'\to M\) in \(S\). For the other order of composition, choose \((r',rc)\) as the square for the first two roofs. Their numerator is \(grc=ubc\), so choose the identity on \(P'\) for the last square. Both parenthesizations give \((sr',hbc)\). Independence of choices, already proved, gives associativity for every choice. The roof \((1,1)\) is an identity by choosing identity squares.

For \(s:M\to X\) in \(S\), the roof \((s,1_M)\) is inverse to \(Q(s)\); either composite refines the identity roof. A functor \(F\) inverting \(S\) must send \((s,f)\) to \(F(f)F(s)^{-1}\). Common refinements leave this expression unchanged, and the composition square proves that it preserves composition. It defines the unique factorization through \(Q\). Natural transformations also descend: a naturality square for \(s\) remains natural after inverting \(F(s)\) and \(G(s)\), and every roof is a composite of such an inverse and an ordinary arrow.

For \(Qf=Qg\), a common refinement of their identity roofs is exactly an \(r\in S\) with \(fr=gr\); the converse is the same refinement. This is the stated equality criterion.

To add roofs, first give them a common denominator \(s\) by Lemma 4.1 and set \((s,f)+(s,g)=(s,f+g)\). If two choices or representatives are made, refine their denominators to a common one and use cancellation to equalize each pair of numerators. Adding the equal numerators proves independence. Negation and zero are \((s,-f)\) and \((s,0)\); the group laws follow after common refinement. Composition is bilinear. For example, for a fixed second denominator \(t\), construct squares for two numerators \(f,g\), then refine their source arrows together. The equalities \(fr=ta\), \(gr=tb\) imply \((f+g)r=t(a+b)\), so the composite distributes over their sum. Distributivity in the other variable follows directly after giving its two roofs a common denominator. Thus \(Q\) is additive. Its original finite-sum inclusions and projections retain their equations, including \(i_1p_1+i_2p_2=1\), and so remain biproducts. The zero object's identity remains zero, making it a zero object. This proves additivity of the localized category. \(\square\)

## 5. Triangles after localization

**Theorem 5.1.** A triangle in \(D(\mathcal A)\) is distinguished when it is isomorphic to the image of a cone triangle. With this definition \(D(\mathcal A)\) is triangulated, \(Q\) is triangulated, and each \(H^n\) descends to a functor that takes distinguished triangles to long exact cohomology sequences.

**Proof.** Shift acts on roofs by shifting both arrows; its inverse is the negative shift. Identity triangles descend. A roof \((s,f):X\to Y\) is, through the isomorphism \(Q(s):M\to X\), the first map of the image of the cone triangle of \(f\). Thus every localized map has a completion. Rotation in both directions follows from Theorem 3.1.

We give the full square-lifting argument. Suppose \(bf=f'a\) in \(D\), for chain-homotopy classes \(f:X\to Y\), \(f':X'\to Y'\), and localized maps \(a:X\to X'\), \(b:Y\to Y'\). Write \(a\) as \(X\xleftarrow{s}U\xrightarrow{a_0}X'\) and \(b\) as \(Y\xleftarrow{t}V\xrightarrow{b_0}Y'\). Form a square \(tv=fsu\), with \(u:W\to U\) a quasi-isomorphism. In \(D\), the maps \(b_0v\) and \(f'a_0u\) are equal. The equality criterion of Theorem 4.2 gives a quasi-isomorphism \(k:W'\to W\) equalizing them in \(K\). We now have a map of first arrows \(W'\xrightarrow{vk}V\) to \(X\xrightarrow fY\), whose vertical maps \(suk,t\) are quasi-isomorphisms, and a map to \(X'\xrightarrow{f'}Y'\), whose vertical maps are \(a_0uk,b_0\). Lemma 2.1 extends each square to cone triangles. The first cone comparison is a quasi-isomorphism by their cohomology sequences and the Five Lemma. Invert it in \(D\) and compose with the second comparison. This gives precisely the missing third map for the original localized square. It proves the square-extension axiom.

We also need cone uniqueness to handle initially chosen octahedra. For fixed \(T\), the roofs construction writes \(\operatorname{Hom}_D(T,-)\) as the filtered colimit of \(\operatorname{Hom}_K(M,-)\) over denominators \(M\to T\), ordered by refinements. This index category is filtered: common squares give common refinements, and cancellation equalizes parallel refinements. Filtered colimits of abelian groups are exact by Lemma 1.1 of *Sheaves of modules on a ringed space*. Apply that result in the larger universe when required. Lemma 2.4 therefore gives long exact representable sequences in \(D\). The dual fraction description, furnished by the dual statements in Lemma 4.1 and the same proof as Theorem 4.2, gives the contravariant sequences as well. The Five Lemma and the inverse construction in Lemma 2.4 show that two isomorphisms in a morphism of localized triangles imply the third. Combined with square extension, this gives uniqueness of completion triangles up to an isomorphism fixing their first two objects.

Finally take two composable localized maps represented by \(X\xleftarrow{s}U\xrightarrow aY\) and \(Y\xleftarrow{t}V\xrightarrow bZ\). Form \(th=ar\), with \(r:P\to U\) a quasi-isomorphism. The string \(P\xrightarrow hV\xrightarrow bZ\) maps to the original string through the isomorphisms \(Q(sr),Q(t),1_Z\). Theorem 3.1 supplies its octahedron, whose image supplies an octahedron for the original maps. Cone uniqueness just proved compares its three chosen triangles with any three initially specified triangles, fixing their first two objects. Transport gives the full localized octahedron axiom.

Every \(H^n\) inverts quasi-isomorphisms and therefore descends by Theorem 4.2. Its long exact sequence on an image triangle is Lemma 1.2 applied to the cone, with the signs in (2.2); an isomorphic triangle has the transported sequence. This finishes the proof. \(\square\)

**Proposition 5.2 (short exact sequences and boundedness).** Every short exact sequence of complexes gives a distinguished triangle in \(D(\mathcal A)\). A complex whose cohomology vanishes below \(a\) is quasi-isomorphic to a complex whose terms vanish below \(a\).

**Proof.** For \(0\to A\xrightarrow fB\xrightarrow gC\to0\), the map \(r:C(f)\to C\), \((b,a')\mapsto g(b)\), is a chain map. Its kernel is \(C(1_A)\), under the identification \(\ker g=A\), and is contractible. Lemma 1.2 makes \(r\) a quasi-isomorphism. Thus the cone triangle identifies with \(A\to B\to C\to A[1]\) in \(D\), with boundary \((-p)r^{-1}\). When the original sequence splits degreewise, Lemma 2.2 identifies this boundary with its positive Snake Lemma boundary. In general the same agreement follows from the lift formula in Lemma 1.2, or from its naturality applied to \(0\to A\to B\to C\to0\) and the cone construction.

For the last assertion use the good truncation \(\tau_{\ge a}K\): it is zero below \(a\), equals \(K^a/\operatorname{im}d_K^{a-1}\) in degree \(a\), and equals \(K^n\) above \(a\). The outgoing differential factors through this quotient because \(d^2=0\). The natural map from \(K\) is an isomorphism on cohomology at and above \(a\), by kernels and images, and both cohomologies vanish below \(a\). It is the required quasi-isomorphism. The dual good truncation uses \(\ker d_K^b\) at the top degree \(b\). \(\square\)

We write \(D^+(\mathcal A)\) for the full subcategory whose cohomology vanishes sufficiently far below zero, and similarly \(D^-\) and \(D^b\). They are triangulated: shifts preserve the relevant bounds, and the long exact sequence bounds the cohomology of a cone whenever its first two objects have those bounds. Proposition 5.2 provides bounded representatives where needed. It is cohomological boundedness, rather than the terms of a particular representative, that defines these subcategories.

## 6. Exercises with complete solutions

**Exercise 1 (easy).** For a module \(M\), show that the complex \(M\xrightarrow1M\) in degrees \(n,n+1\) is contractible. Explain why this proves that adding it to any complex does not change its object in \(K\).

**Solution.** Take the only nonzero homotopy component to be the identity from degree \(n+1\) to degree \(n\). Then \(dH+Hd\) is the identity in both nonzero degrees. Projection from the direct sum to the original complex has its inclusion as inverse up to the homotopy that is zero on the original summand and the indicated contraction on the new summand. Thus it is an isomorphism in \(K\).

**Exercise 2 (medium).** The complex \(\mathbb Z\xrightarrow2\mathbb Z\to\mathbb Z/2\) in degrees \(-1,0,1\), with the quotient as second differential, is acyclic. Prove that it is not contractible.

**Solution.** Multiplication by two is injective, its image is the quotient map's kernel, and that quotient map is onto. Thus all cohomology groups vanish. A contraction at degree \(1\) would give a homomorphism \(s:\mathbb Z/2\to\mathbb Z\) such that the quotient composed with \(s\) is the identity. Every such homomorphism is zero, since \(\mathbb Z\) has no element of order two. No contraction exists. Localization makes this complex zero, because its map from the zero complex is a quasi-isomorphism, whereas the homotopy category retains it as a nonzero object.

**Exercise 3 (medium).** A map \(f:M[0]\to N[0]\) of modules has a cone supported in degrees \(-1,0\). Compute its cohomology and the signs in its cone triangle.

**Solution.** The cone is \(M\xrightarrow fN\), in those degrees. Its cohomology is \(\ker f\) in degree \(-1\), \(\operatorname{coker}f\) in degree \(0\), and zero otherwise. The triangle is \(M[0]\xrightarrow fN[0]\to C(f)\xrightarrow{-p}M[1]\), so the degree-\(-1\) component of the last map is \(-1_M\). This sign is consistent with the split-sequence calculation of Lemma 2.2; replacing it silently by a positive projection would change the adopted triangle convention.

**Exercise 4 (hard).** Let \(I\) be a complex such that \(\operatorname{Hom}^{\bullet}(A,I)\) is acyclic for every acyclic \(A\). Without using roofs, prove that \(\operatorname{Hom}_K(L,I)\to\operatorname{Hom}_D(L,I)\) is bijective.

**Solution.** If \(s:M\to N\) is a quasi-isomorphism, its cone is acyclic. The contravariant Hom-cone identity in Lemma 2.4 implies that \(s^*:\operatorname{Hom}^{\bullet}(N,I)\to\operatorname{Hom}^{\bullet}(M,I)\) is a quasi-isomorphism. The induced degree-zero cohomology map is therefore a bijection. By Lemma 1.1 it is the map on homotopy classes into the target complex. Thus \(H(L)=\operatorname{Hom}_K(L,I)\) descends to a contravariant functor on \(D\). For \(v:L\to I\) in \(D\), send \(v\) to \(H(v)(1_I)\). On homotopy classes this is plainly inverse to the canonical map in one direction. The other composite is a natural endomorphism of \(\operatorname{Hom}_D(-,I)\) which fixes \(1_I\). Naturality holds on ordinary arrows, on their inverted quasi-isomorphisms by inverting the naturality squares, and hence on every localized arrow. Applied to \(v\), it forces that composite to fix \(v\). The two maps are inverse. This will be the comparison mechanism for injective resolutions.
