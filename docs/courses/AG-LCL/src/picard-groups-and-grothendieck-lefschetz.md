# Picard groups and Grothendieck–Lefschetz

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by GPT-6.1 Sol, the AI that wrote it. Public domain (CC0).*

A line bundle can be extended through a square-zero thickening unless a degree-two cohomology class obstructs it. Degree-one cohomology controls the ambiguity. Formal algebraization then turns compatible extensions into an ordinary line bundle near the closed subscheme. A final local condition, parafactoriality, lets that bundle cross the points still missing from the neighbourhood.

We use Local cohomology for the depth criterion and Hartogs extension, Formal geometry along a closed subscheme for formal bundles and their algebraization, and the omitted-point argument in Lefschetz theorems for finite étale covers. We assume Noetherian completion and Artin–Rees, coherent extension from quasi-compact opens, divisors on normal schemes, and the commutative-algebra theorem that finite modules over a regular local ring have finite free resolutions. The finite-resolution assertion was proved in Local duality and finiteness, Proposition 2.5, using a Koszul resolution and minimal free resolutions. Projective-space cohomology will be the input to an explicit complete-intersection vanishing proof.

The Picard group is written additively, with tensor product as addition. An element is torsion if some positive tensor power is trivial. In this lesson a **complete intersection local ring** means a quotient of a regular local ring by a regular sequence. The local vanishing theorem also holds when only the completion has such a presentation; we will prove that extension of scope. A projective complete intersection is defined scheme-theoretically by a homogeneous regular sequence of positive degrees. No smoothness or characteristic-zero assumption is implicit.

## 1. Thickenings and formal line bundles

Let \(X\subset X'\) have square-zero ideal \(\mathcal J\). The underlying topological spaces agree. The sequence of abelian sheaves
\[
0\longrightarrow\mathcal J\xrightarrow{a\mapsto1+a}
\mathcal O_{X'}^\times\longrightarrow\mathcal O_X^\times
\longrightarrow1
\tag{1.1}
\]
is exact. Indeed \((1+a)(1+b)=1+a+b\) because \(\mathcal J^2=0\), and the kernel of reduction is exactly \(1+\mathcal J\). A lift of a unit remains a unit locally: if the product with a lift of its inverse is \(1+c\), then \((1+c)^{-1}=1-c\).

**Proposition 1.1 (first-order Picard sequence).** There is a canonical exact sequence
\[
\begin{aligned}
0\to H^0(X,\mathcal J)&\to\Gamma(X',\mathcal O_{X'}^\times)
\to\Gamma(X,\mathcal O_X^\times)\\
&\to H^1(X,\mathcal J)\to\operatorname{Pic}(X')
\to\operatorname{Pic}(X)\to H^2(X,\mathcal J).
\end{aligned}
\tag{1.2}
\]

**Proof.** A line bundle is described by transition units on an open cover; changing frames multiplies the transition cocycle by a coboundary. This identifies \(\operatorname{Pic}(X)\) with \(H^1(X,\mathcal O_X^\times)\), and similarly for \(X'\). Take the long exact sequence of (1.1). The boundary of a line-bundle cocycle is represented by the failure of chosen lifted transition units to satisfy the cocycle equation, now an additive \(\mathcal J\)-valued two-cocycle. Its vanishing permits the lifted gluing. The exact sequence also identifies the ambiguity in that gluing and the role of global units. ∎

This proves [Stacks, [Tag 0C6R](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-morphisms.html#more-morphisms-lemma-picard-group-first-order-thickening)]. In particular \(H^2(\mathcal J)=0\) gives surjectivity on Picard groups, while \(H^1(\mathcal J)=0\) gives injectivity and surjectivity on global units.

For the formal comparison assume \(X\) is Noetherian. For an ideal \(\mathcal I\) put \(Y_n=V(\mathcal I^n)\), \(n\ge1\). The step \(Y_n\subset Y_{n+1}\) has square-zero ideal
\(\mathcal I^n/\mathcal I^{n+1}\). If \(Y\) is an effective Cartier divisor, this is
\(\mathcal O_Y(-nY)\).

Write \(\operatorname{Pic}(\widehat X_Y)\) for isomorphism classes of invertible coherent formal modules. There is always a map
\[
\operatorname{Pic}(\widehat X_Y)\longrightarrow
\varprojlim_n\operatorname{Pic}(Y_n).
\tag{1.3}
\]
It is surjective: for compatible classes choose representatives successively and choose isomorphisms of each reduction with its predecessor. These choices give a formal object. Injectivity requires a compatibility check on the isomorphisms, rather than just on their classes.

Here are two sufficient settings in which (1.3) is an isomorphism. First, if all
\[
H^1(Y,\mathcal I^n/\mathcal I^{n+1})=0,\qquad n\ge1,
\tag{1.4}
\]
then the global unit groups at consecutive levels map surjectively. Any individually chosen isomorphisms between two formal systems can then be adjusted by units successively to become compatible.

Second, if every \(Y_n\) is proper over a field \(k\), the same conclusion holds even without (1.4). Their section algebras \(R_n=\Gamma(Y_n,\mathcal O_{Y_n})\) are finite-dimensional over \(k\). At any fixed level the images of \(R_m\to R_n\) form a descending chain of finite-dimensional subspaces and stabilize. Units of a finite-dimensional algebra map onto the units of each quotient: decompose its Artinian ring into local factors, and choose unit lifts in every retained factor and the unit \(1\) in omitted factors. Consequently the images of \(R_m^\times\to R_n^\times\) stabilize too. This is the Mittag–Leffler condition on the automorphism groups of any line bundle. It makes compatible adjustments possible: after passing to stable images, choose a correction at the first level and lift it recursively. Equivalently, the usual countable inverse-limit obstruction \(\varprojlim^1 R_n^\times\) vanishes. This proves injectivity of (1.3).

If both \(H^1\) and \(H^2\) of every layer vanish, (1.2) and (1.3) therefore give
\[
\operatorname{Pic}(\widehat X_Y)\simeq\operatorname{Pic}(Y).
\tag{1.5}
\]
The vanishing of \(H^1\) also supplies the compatible units needed for this statement without properness. A bare inverse limit of Picard classes should not be identified with formal line bundles in arbitrary settings without that extra check.

## 2. Torsion in the local Picard group

Let \((A,\mathfrak m)\) be Noetherian local, \(f\in\mathfrak m\) a nonzerodivisor, and set
\[
U=\operatorname{Spec}A\setminus\{\mathfrak m\},\qquad
U_0=\operatorname{Spec}(A/fA)\setminus\{\mathfrak m\}.
\]
Assume \(\operatorname{depth}A\ge3\), equivalently \(\operatorname{depth}(A/fA)\ge2\).

**Theorem 2.1.** The restriction
\[
\operatorname{Pic}(U)\longrightarrow\operatorname{Pic}(U_0)
\tag{2.1}
\]
is injective on torsion.

We prove this using a finite-length invariant and a finite-difference argument. This avoids imposing completeness, a dualizing complex, or invertibility of the torsion order.

A **coherent triple** is \((F,F_0,\alpha)\), with \(F\) coherent on \(U\), multiplication by \(f\) injective on \(F\), \(F_0\) coherent on \(\operatorname{Spec}(A/fA)\), and
\(\alpha:F/fF\simeq F_0|_{U_0}\). Invertible triples have both sheaves invertible.

**Lemma 2.2 (a finite-length invariant).** Choose a finite \(f\)-torsion-free \(A\)-module \(M\) extending \(F\), together with a map
\[
\beta:M/fM\longrightarrow N_0=\Gamma(\operatorname{Spec}(A/fA),F_0)
\]
extending \(\alpha\). Then
\[
\chi(F,F_0,\alpha)
=\operatorname{length}_A\operatorname{coker}\beta
-\operatorname{length}_A\ker\beta
\tag{2.2}
\]
is defined, independent of the choice, and additive in short exact sequences of triples.

**Proof.** Begin with a finite coherent extension of \(F\) and divide out its \(f\)-power torsion, which restricts to zero. A map defined off the closed point extends after replacing the source by a sufficiently high \(\mathfrak m\)-power: this is the finite-module map-extension formula [Stacks, [Tag 01YB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-homs-over-open)], obtained by clearing denominators on a finite principal cover and applying Artin–Rees to relations. Apply it on \(\operatorname{Spec}(A/fA)\), and replace \(M\) by \(\mathfrak m^cM\). This gives \(\beta\). Its kernel and cokernel are finite modules supported at \(\mathfrak m\), hence have finite length.

Two such extensions admit a common smaller one: the identity on \(F\) extends from a high \(\mathfrak m\)-power, and any difference between the two maps modulo \(f\), being supported at the closed point, is killed by another power. The common comparison is injective, since a closed-point kernel would be killed by a power of \(f\), while the source is \(f\)-torsion-free. Its cokernel \(C\) has finite length. Reduction modulo \(f\) gives kernel \(C[f]\) and cokernel \(C/fC\). They have equal lengths, by the kernel-cokernel sequence for the endomorphism \(f:C\to C\). The six-term kernel-cokernel sequence for composition with \(\beta\) therefore leaves (2.2) unchanged.

For additivity, take a finite extension \(M_G\) of the middle sheaf of a short exact sequence of triples. Intersect it with the first sheaf inside the pushforward from \(U\), and take the quotient, giving finite \(M_F,M_H\). All are \(f\)-torsion-free, so their sequence remains exact modulo \(f\). The maps to \(F_0,G_0,H_0\) might initially fail to form a diagram only at the closed point. Replace \(M_G\) by a high \(\mathfrak m\)-power; Artin–Rees ensures its intersection with \(M_F\) lies in a power killing that failure. We then have a commutative diagram of exact rows modulo \(f\). The snake lemma and additivity of finite lengths prove additivity of (2.2). Independence permits these replacements. ∎

**Lemma 2.3 (finite differences).** For an invertible triple \(T\) and a coherent triple \(C\), the function
\[
n\longmapsto\chi(C\otimes T^{\otimes n}),\qquad n\in\mathbb Z,
\tag{2.3}
\]
is a polynomial with rational coefficients.

**Proof.** Induct on the dimension of the support of the sheaf of \(C\) on \(U\). If that sheaf is zero, its other sheaf is supported at the closed point; twisting by the locally free rank-one \(F_0\) does not change its finite length. Thus (2.3) is constant.

Remove the closed-point torsion from \(F_0\). Its contribution is constant by the preceding case and additivity, so it suffices to consider \(\mathfrak m\notin\operatorname{Ass}(F_0)\). Choose a section \(s\) of the invertible sheaf of \(T\) nonvanishing at the finite set
\(\operatorname{Ass}(F)\cup\operatorname{Ass}(F/fF)\). Such a section exists on a quasi-affine scheme [Stacks, [Tag 0F20](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/properties.html#properties-lemma-quasi-affine-invertible-nonvanishing-section)]. Its reduction corresponds to a section of the invertible sheaf of \(T_0\) on \(U_0\). That section extends over the closed point after multiplication by a high \(\mathfrak m\)-power, by the map-extension formula. Choose the multiplying element outside the finitely many associated primes just used; prime avoidance permits this since they are nonmaximal. Thus \(s\) still avoids them, and it has a compatible extension \(s_0\).

Multiplication by \((s,s_0)\) gives an injection
\[
0\longrightarrow C\longrightarrow C\otimes T\longrightarrow G\longrightarrow0
\tag{2.4}
\]
of triples. Injectivity on \(F\) and on \(F/fF\) makes \(f\) injective on the quotient; \(s_0\) is injective on \(F_0\) since it avoids its associated points on \(U_0\) and there is no closed-point associated point. The support of \(G\) on \(U\) has strictly smaller dimension: it contains no associated point of \(F\), in particular none of its generic support points.

Twist (2.4) by \(T^n\). Additivity says the first difference of (2.3) is the corresponding polynomial for \(G\), by induction. A polynomial in \(n\) has a polynomial discrete antiderivative, as seen by using the basis \(\binom n j\), for which \(\binom{n+1}{j+1}-\binom n{j+1}=\binom n j\). Subtract such an antiderivative; the remaining function has zero first difference for every integer and is constant. This proves (2.3), for negative as well as positive \(n\). ∎

These two lemmas supply the needed parts of [Stacks, [Tag 0F23](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebraization.html#algebraization-lemma-prepare-chi-triple), [Tag 0F25](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebraization.html#algebraization-lemma-well-defined-chi-triple), [Tag 0F26](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebraization.html#algebraization-lemma-ses-chi-triple), [Tag 0F27](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebraization.html#algebraization-proposition-hilbert-triple)].

**Lemma 2.4 (positivity for an invertible triple).** For an invertible triple,
\[
\chi(L,L_0,\lambda)
=\operatorname{length}_A\operatorname{coker}
\bigl(\Gamma(U,L)\to\Gamma(U_0,L_0)\bigr)\ge0.
\tag{2.5}
\]
It is zero exactly when \(L\) is trivial.

**Proof.** Depth gives \(\Gamma(U,\mathcal O_U)=A\) and
\(\Gamma(U_0,\mathcal O_{U_0})=A/fA\). Also \(L_0\) is trivial on its local affine scheme. The module \(M=\Gamma(U,L)\) is finite. Indeed quasi-affineness gives a finite surjection \(\mathcal O_U^r\to L^\vee\); dualizing gives an injection \(L\to\mathcal O_U^r\), so \(M\subset A^r\) is finite. Its associated sheaf restricts to \(L\), by quasi-coherent pushforward on this open. The support sequence and the equality \(M=\Gamma(U,L)\) give \(H^0_{\mathfrak m}(M)=H^1_{\mathfrak m}(M)=0\), hence depth at least two. Multiplication by \(f\) is injective on \(M\).

The map \(M/fM\to A/fA\) is an isomorphism off the closed point. Its kernel has finite length and is zero because \(\operatorname{depth}(M/fM)\ge1\). Consequently (2.2) is the cokernel length in (2.5).

If this length is zero, \(M/fM\simeq A/fA\). Lift its generator to \(M\). Nakayama gives a surjection \(A\to M\). Because \(f\) is regular on \(M\), reduction of its finite kernel \(K\) gives \(K/fK=0\); Nakayama gives \(K=0\). Thus \(M\simeq A\) and \(L\) is trivial. Conversely if \(L\) is trivial, \(\lambda\) differs from its ordinary trivialization by a unit of \(A/fA\), which lifts to a unit of the local ring \(A\). Therefore the cokernel is zero. ∎

This gives [Stacks, [Tag 0F28](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebraization.html#algebraization-lemma-nonnegative-chi-triple)].

**Proof of Theorem 2.1.** Suppose \(L|_{U_0}\) is trivial, and choose that trivialization to make the invertible triple \(T=(L,\mathcal O_{X_0},\lambda)\). Lemma 2.3 makes \(\chi(T^n)\) a polynomial. If \(L\) has torsion order dividing \(r>0\), then \(L^{rn}\) is trivial for every integer \(n\). Lemma 2.4 makes all the corresponding polynomial values zero, regardless of the chosen trivialization on \(U_0\). A polynomial with infinitely many zeros is zero. Its value at \(1\) is zero, so Lemma 2.4 makes \(L\) trivial. ∎

This proves [Stacks, [Tag 0F2A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebraization.html#algebraization-lemma-injective-torsion-in-pic)], including torsion divisible by the residue characteristic. It does not claim injectivity on the whole Picard group.

The same invariant also proves full injectivity when duality bounds its growth. This connects the finite-difference argument with the local duality and finiteness already developed in the course.

**Theorem 2.5 (Kollár's injectivity theorem).** If \(A\) has a dualizing complex, \(f\) is a nonzerodivisor, \(\operatorname{depth}(A/fA)\ge2\), and
\[
f\in\mathfrak p,\ \dim(A/\mathfrak p)=2
\quad\Longrightarrow\quad\operatorname{depth}A_{\mathfrak p}\ge2,
\tag{2.6}
\]
then (2.1) is injective. Moreover (2.6) follows from the other hypotheses if \(A\) is \((S_2)\) and \(\dim A\ge4\).

**Proof.** Let \(L\) restrict trivially to \(U_0\), choose that trivialization, and form the invertible triple \(T\). The function \(P(n)=\chi(T^n)\) is a polynomial, nonnegative for every integer \(n\), and \(P(0)=0\). We will bound it linearly for positive \(n\); these three properties force it to be zero.

Put \(M=\Gamma(U,L)\). Lemma 2.4 gives a finite module of depth at least two and an exact sequence
\[
0\to M/fM\to A/fA\to Q\to0,
\qquad\operatorname{length}Q=\chi(T).
\tag{2.7}
\]
The group \(F=H^2_{\mathfrak m}(M)\) has finite length. To verify the finiteness input, \(M\) is locally free on the puncture, while \(H^i_{\mathfrak m}(A)=0\) for \(i\le2\). The finite locally free local-cohomology comparison [Stacks, [Tag 0BPY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/local-cohomology.html#local-cohomology-lemma-local-finiteness-for-finite-locally-free)] therefore gives finiteness of \(H^2_{\mathfrak m}(M)\). That result's full open proof applies to finite modules locally free off the support; its hypotheses here include all three low cohomology groups of \(A\). A finite module supported at the closed point has finite length.

The support sequences of (2.7) and of multiplication by \(f\) on \(M\) give
\[
0\to Q\to F\xrightarrow{f}F\xrightarrow{\rho}
H^2_{\mathfrak m}(A/fA).
\]
Indeed \(H^1_{\mathfrak m}(A/fA)=0\) and
\(H^2_{\mathfrak m}(M/fM)=H^2_{\mathfrak m}(A/fA)\).
An endomorphism of the finite-length \(F\) has kernel and cokernel of equal length. Thus \(\chi(T)=\operatorname{length}\operatorname{im}\rho\).

Choose a normalized dualizing complex \(\omega\), and set
\[
N=\operatorname{Ext}^{-2}_A(A/fA,\omega),\qquad
P_M=\operatorname{Ext}^{-2}_A(M,\omega).
\]
Local duality, including the completion in its finite-module side, identifies the dual of \(\rho\) with the completion of the natural map \(\alpha:N\to P_M\). Its image has length \(\chi(T)\). Since \(N,P_M\) are finite, faithful flatness descends finite length of this image, and completion preserves that length. Hence
\[
\chi(T)=\operatorname{length}\operatorname{im}\alpha.
\tag{2.8}
\]
This uses the precise duality in Local duality and finiteness, Section 3; it imposes no completeness on \(A\).

That lesson's dimension function and local depth bounds also show \(\dim\operatorname{Supp}N\le1\). Its support is inside \(V(f)\). At a prime \(\mathfrak p\), let \(\delta=\dim(A/\mathfrak p)\). The normalized localized dual degree for \(N_{\mathfrak p}\) is \(\delta-2\). If \(\delta>2\), this is positive and the group vanishes. If \(\delta=2\), condition (2.6) and regularity of \(f\) give \(\operatorname{depth}(A/fA)_{\mathfrak p}\ge1\), so the degree-zero dual group vanishes too. Only primes with \(\delta\le1\) remain.

Choose a section \(t\) of \(L^\vee\) nonvanishing at the finitely many nonmaximal points of \(\operatorname{Supp}N\), using the quasi-affine section lemma from Lemma 2.3. Its reduction, under the chosen trivialization, is a section of \(\mathcal O_{U_0}\), hence an element \(g\in A/fA\) by Hartogs. It is a unit at those support points, so \(N/gN\) has finite length; write that length as \(c\).

Multiplication by \(t\) gives \(M\to A\), compatible with multiplication by \(g\) on the quotients. Applying \(\operatorname{Ext}^{-2}_A(-,\omega)\) to this diagram gives \(\alpha\circ g=0\), because
\(\operatorname{Ext}^{-2}_A(A,\omega)=0\) by \(\operatorname{depth}A\ge3\). For \(T^n\), use \(t^n\) and \(g^n\). The same calculation gives
\[
0\le P(n)\le\operatorname{length}(N/g^nN)\le nc
\quad(n\ge1).
\tag{2.9}
\]
The final inequality follows by filtering by the powers of \(g\): each \(g^jN/g^{j+1}N\) is a quotient of \(N/gN\). A polynomial bounded above linearly on positive integers has degree at most one. A polynomial of that degree which is nonnegative on all integers and vanishes at zero must be zero. Lemma 2.4 now makes \(L\) trivial.

Finally a ring with a dualizing complex is catenary, and an \((S_2)\) such local ring is equidimensional by the connectedness lesson. Thus
\(\dim A_{\mathfrak p}+\dim(A/\mathfrak p)=\dim A\).
When \(\dim A\ge4\) and \(\dim(A/\mathfrak p)=2\), the local dimension is at least two and \((S_2)\) gives (2.6). ∎

This proves [Stacks, [Tag 0F2B](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebraization.html#algebraization-proposition-injective-pic)]. It is an injectivity result, with no surjectivity conclusion.

## 3. Completion and regular local rings

**Lemma 3.1.** If \(\operatorname{depth}A\ge2\), completion at \(\mathfrak m\) induces an injection
\[
\operatorname{Pic}(U)\longrightarrow\operatorname{Pic}(\widehat U),
\qquad
\widehat U=\operatorname{Spec}\widehat A\setminus\{\widehat{\mathfrak m}\}.
\tag{3.1}
\]

**Proof.** Let \(M=\Gamma(U,L)\). Flat Čech base change gives
\(M\otimes_A\widehat A=\Gamma(\widehat U,\widehat L)\).
If \(\widehat L\) is trivial, the right side is \(\widehat A\), by depth at least two. Faithfully flat descent makes \(M\) a finite locally free rank-one \(A\)-module. Concretely, choose finitely many elements of \(M\) whose tensors generate the rank-one completed module; faithful flatness kills the cokernel of the resulting finite presentation, and descends its flatness. A finite flat module over the local ring \(A\) is free. Thus \(M\simeq A\). The sheaf associated to \(M\), restricted to \(U\), recovers \(L\), so \(L\) is trivial. ∎

This proves [Stacks, [Tag 0F2G](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebraization.html#algebraization-lemma-local-pic-to-completion)]. No algebraization of arbitrary bundles from \(\widehat U\) is being asserted.

**Theorem 3.2.** A regular local ring has trivial Picard group on its punctured spectrum.

**Proof.** Extend a line bundle \(L\) coherently over the affine spectrum, obtaining a finite module \(M\). The finite global-dimension theorem for regular local rings gives a finite resolution of \(M\) by finite free modules. Restrict it to the punctured spectrum, where \(M\) is \(L\). In this exact complex every successive kernel is a vector bundle: starting from the surjection onto \(L\), split it locally and proceed inductively. For a short exact sequence of vector bundles, determinants satisfy
\(\det B=\det A\otimes\det C\), as follows locally from a basis adapted to the subbundle. Multiplying these identities through the resolution identifies
\[
L=\det L\simeq
\bigotimes_i(\det \mathcal O_U^{r_i})^{(-1)^i}
\simeq\mathcal O_U.
\tag{3.2}
\]
In dimension zero the puncture is empty and the assertion is immediate. ∎

This is a proof of [Stacks, [Tag 0F2H](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebraization.html#algebraization-lemma-trivial-local-pic-regular)] through determinants. The usual factoriality route gives the same result: regular local rings are UFDs [Stacks, [Tag 0AG0](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/more-algebra.html#more-algebra-lemma-regular-local-UFD)], and divisor closure extends an invertible sheaf to their local spectrum [Stacks, [Tag 0BD9](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-extend-invertible-module)], where every line bundle is free. The determinant proof proves the Picard assertion directly from finite free resolutions.

## 4. Complete intersections and parafactoriality

**Lemma 4.1 (principal lifting of line bundles).** Suppose \(A\) is \(f\)-adically complete, \(f\) is a nonzerodivisor and
\[
H^1_{\mathfrak m}(A/fA),\ H^2_{\mathfrak m}(A/fA)
\text{ are finite},\qquad H^3_{\mathfrak m}(A/fA)=0.
\tag{4.1}
\]
Every line bundle on \(U_0\) lifts to a line bundle on a neighbourhood of \(U_0\) in \(U\). If the punctured local spectra at all maximal ideals of \(A_f\) have zero Picard group, it lifts to all of \(U\).

**Proof.** The principal thickening layers are \(\mathcal O_{U_0}\), because \(f\) is regular. Their obstruction groups are
\[
H^2(U_0,\mathcal O_{U_0})=H^3_{\mathfrak m}(A/fA)=0.
\]
Proposition 1.1 lifts a given line bundle successively through every thickening, with chosen reduction isomorphisms. This gives an invertible coherent formal module. The permitted principal formal-bundle algebraization statement in Formal geometry, Section 8, applies because the other two groups in (4.1) are finite. It supplies a coherent algebraization that is free of rank one on some neighbourhood \(V\supset U_0\).

As proved in the preceding lesson, \(U\setminus V\) is a finite set of closed points, maximal in \(A_f\): the principal ideal theorem gives dimension one for the closures of its components. At each missing point the line bundle on the punctured local spectrum is trivial by hypothesis, hence extends as the trivial bundle over the local spectrum. The isomorphism with the existing bundle spreads to a neighbourhood by finite-presentation descent and glues there. Add the finitely many points. ∎

This proves the lifting arguments of [Stacks, [Tag 0F2D](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebraization.html#algebraization-lemma-surjective-Pic-first), [Tag 0F2F](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebraization.html#algebraization-lemma-surjective-Pic-first-better)] from the already specified formal input.

**Theorem 4.2 (Grothendieck).** If \(A\) is a complete intersection local ring of dimension at least four, then
\[
\operatorname{Pic}(\operatorname{Spec}A\setminus\{\mathfrak m\})=0.
\tag{4.2}
\]
The same holds when its completion is a quotient of a regular local ring by a regular sequence.

**Proof.** Such a ring is Cohen–Macaulay, so its depth is its dimension. Lemma 3.1 reduces to its completion. Completion of a presentation by a regular sequence gives the corresponding presentation over the completed regular local ring. We prove the result by induction on the number \(r\) of equations, simultaneously for all local rings with a presentation of length at most \(r\), including their completed versions. The base case is Theorem 3.2.

For the step write the complete ring as
\[
A=B/(f_1,\ldots,f_r),\qquad
A'=B/(f_1,\ldots,f_{r-1}),\qquad f=f_r.
\]
Then \(A'\) is complete, \(f\) is regular, and \(A=A'/fA'\) is Cohen–Macaulay of dimension \(d\ge4\). Thus the three groups in (4.1) for this quotient all vanish. Lemma 4.1 lifts every line bundle on the punctured spectrum of \(A\) to a neighbourhood in the punctured spectrum of \(A'\).

For a maximal prime \(\mathfrak p\) of \(A'_f\), put \(S=A'/\mathfrak p\). This is a local domain, \(f\) is nonzero and belongs to its maximal ideal, and \(S_f\) is a field. We claim \(\dim S=1\). If its dimension were at least two, its maximal ideal would not lie in the union of the finitely many height-one primes containing \(f\). Prime avoidance would give a nonzero element \(g\) in that maximal ideal outside all those primes. A prime minimal over \((g)\) has height one by the principal ideal theorem, and cannot contain \(f\), since every height-one prime containing \(f\) is minimal over \((f)\). It would survive as a nonzero prime of the field \(S_f\), a contradiction. Dimension zero is impossible because \(f\) is a nonzero nonunit of the local domain. Thus \(\dim S=1\), and \(V(\mathfrak p)\cap V(f)\) consists only of the closed point. A complete Cohen–Macaulay local ring is equidimensional and catenary. Hence
\[
\dim A'_{\mathfrak p}=\dim A'-1=d\ge4.
\tag{4.3}
\]
This local ring is \(B_{\mathfrak q}/(f_1,\ldots,f_{r-1})\) for the corresponding prime \(\mathfrak q\) of \(B\). The regular sequence remains regular on localization and \(B_{\mathfrak q}\) is regular. The inductive hypothesis therefore gives zero Picard group on its puncture. Notice that these localized rings need not be complete; the simultaneous inductive statement and Lemma 3.1 apply to them.

The second assertion of Lemma 4.1 now lifts the original line bundle to all of the puncture of \(A'\). That Picard group is zero by induction, since \(\dim A'=d+1\ge5\). Its restriction is consequently trivial. This proves (4.2) for the complete ring, and Lemma 3.1 descends it to the original ring. The same descent proves the completion-only version. ∎

This is the full local theorem [Stacks, [Tag 0F2I](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebraization.html#algebraization-proposition-trivial-local-pic-complete-intersection)]. It proves the Picard content of the independently cited [Stacks, [Tag 0HDG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-theorem-ci-parafactorial)] rather than using that citation as a substitute for the argument.

A Noetherian local ring is **parafactorial** here if its depth is at least two and its punctured Picard group is zero. Regular local rings of dimension at least two and complete intersections of dimension at least four are therefore parafactorial.

**Proposition 4.3 (extension across a parafactorial closed set).** Let \(Z\subset X\) be closed in a Noetherian scheme, and suppose \(\mathcal O_{X,z}\) is parafactorial for every \(z\in Z\). Then restriction of line bundles from \(X\) to \(X\setminus Z\) is an equivalence.

**Proof.** Depth at least two gives
\(\mathcal O_X\simeq j_*\mathcal O_{X\setminus Z}\) by the supported-depth criterion. For two line bundles their internal Hom is a line bundle and has the same stalk depth, so the same criterion identifies it with the pushforward of its restriction. Taking sections proves full faithfulness.

For existence, take a generic point \(z\) of the remaining closed complement of an open on which the given line bundle has already been extended. In \(\operatorname{Spec}\mathcal O_{X,z}\) that complement consists only of its closed point. The bundle on its puncture is trivial by parafactoriality, so it extends there. A trivialization is a finite-presentation isomorphism; it spreads from the localized puncture to an overlap with an ordinary neighbourhood of \(z\). Glue the trivial bundle on that neighbourhood to the existing bundle. This removes an open part of each generic component of the complement. Noetherian induction on the closed complement finishes the extension. The full faithfulness already proved makes the gluing unique with its prescribed restriction. ∎

Parafactoriality is not by itself factoriality. If \(A\) is a normal local domain of dimension at least two and all its nonmaximal localizations are UFDs, however, zero Picard group on its puncture implies that \(A\) is a UFD. Indeed every Weil divisor is Cartier on the puncture and thus defines a line bundle there. If that bundle is trivial, the divisor differs from a principal divisor by a divisor supported at the closed point. That point has codimension at least two and cannot occur in a Weil divisor. Hence every height-one prime divisor is principal, the UFD criterion for a normal Noetherian domain.

The confirmed [Samuel–Grothendieck theorem](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-theorem-ci-Cartier-codimension-three) in AI Integrated Stacks Project gives the following statements. For a complete intersection local ring, if it is normal and a Weil divisor is Cartier at every prime of height at most three, that divisor is Cartier everywhere. If its localizations at every prime of height at most three are UFDs, the ring is a UFD; in particular regularity in those codimensions suffices. The first assertion follows by dimension induction from Theorem 4.2: it makes the divisor principal on the puncture at each induction step. For the second, the complete intersection is \((S_2)\), and factoriality in heights zero and one gives \((R_1)\); Serre's criterion gives normality, after which the first assertion applies to every height-one prime. This explains the factoriality consequence while distinguishing it from parafactoriality.

## 5. Global Picard comparison

Let \(X\) be proper over a field, and let \(Y\) be an effective ample Cartier divisor. Assume
\[
\operatorname{depth}\mathcal O_{X,x}+\dim\overline{\{x\}}>2
\quad(x\notin Y),
\tag{5.1}
\]
and assume that all local rings at closed points outside \(Y\) are parafactorial.

**Theorem 5.1.** Under these hypotheses,
\[
\operatorname{Pic}(X)\simeq\operatorname{Pic}(\widehat X_Y).
\tag{5.2}
\]
If also
\[
H^1(Y,\mathcal O_Y(-nY))=
H^2(Y,\mathcal O_Y(-nY))=0
\quad\text{for every }n\ge1,
\tag{5.3}
\]
then restriction \(\operatorname{Pic}(X)\to\operatorname{Pic}(Y)\) is an isomorphism.

**Proof.** Theorem 6.4 of Formal geometry, under exactly (5.1), is an equivalence between neighbourhood vector bundles and formal vector bundles. Its restriction to rank-one objects is an equivalence: a formal line bundle algebraizes to a bundle whose rank is one along \(Y\), and one shrinks to that rank locus. Thus each formal line bundle algebraizes on some \(V\supset Y\), and morphisms are detected after shrinking.

The complement \(X\setminus V\) is proper over the field and closed in the affine \(X\setminus Y\), hence finite. All its points are closed and parafactorial. Proposition 4.3 extends the line bundle over them, proving surjectivity in (5.2). If a line bundle on \(X\) is formally trivial, formal full faithfulness makes it trivial on a neighbourhood of \(Y\). The same proposition's full faithfulness across that finite complement extends the isomorphism to all of \(X\), proving injectivity.

The Cartier thickening layers are \(\mathcal O_Y(-nY)\). Proposition 1.1 and (5.3) identify all their Picard groups with \(\operatorname{Pic}(Y)\). The compatible-unit check in Section 1 identifies this common group with the formal Picard group. Combine with (5.2). ∎

For finitely many nonvanishing low layers the same proof compares with a sufficiently high thickening once both groups vanish at all later layers. The displayed theorem uses all layers to compare directly with \(Y\).

## 6. Complete intersections in projective space

**Lemma 6.1 (explicit cohomology vanishing).** If \(Z\subset\mathbb P^N_k\) is a complete intersection of dimension \(r\ge1\), then
\[
H^i(Z,\mathcal O_Z(m))=0
\quad\text{for all integers }m\text{ and }0<i<r.
\tag{6.1}
\]

**Proof.** Induct along the homogeneous regular sequence. For projective space, Čech computation gives vanishing in every middle degree and every twist. If \(Z\subset W\) is the next equation of degree \(d>0\), regularity gives
\[
0\to\mathcal O_W(m-d)\longrightarrow
\mathcal O_W(m)\longrightarrow\mathcal O_Z(m)\to0.
\tag{6.2}
\]
Here \(\dim W=r+1\). For \(0<i<r\), both \(H^i(W,\mathcal O_W(m))\) and \(H^{i+1}(W,\mathcal O_W(m-d))\) vanish by induction, because \(i+1\le r<\dim W\). The long exact sequence gives (6.1). A homogeneous regular sequence also makes each intermediate scheme pure and Cohen–Macaulay, of the expected dimension, by the depth drop and dimension formula for a regular sequence. ∎

**Theorem 6.2 (Grothendieck–Lefschetz for complete intersections).** A scheme-theoretic complete intersection \(Y\subset\mathbb P^N_k\) of dimension at least three satisfies
\[
\operatorname{Pic}(Y)=\mathbb Z\,[\mathcal O_Y(1)].
\tag{6.3}
\]

**Proof.** First \(\operatorname{Pic}(\mathbb P^N_k)=\mathbb Z[\mathcal O(1)]\). One divisor proof is to take a rational section of any line bundle. Projective space is regular, so its Cartier divisor is a Weil divisor. Every prime divisor comes from a homogeneous height-one prime in the UFD \(k[x_0,\ldots,x_N]\), hence from one homogeneous irreducible polynomial \(g\) of degree \(d\). Its divisor is linearly equivalent to \(d\) times a hyperplane, using the rational function \(g/x_0^d\). Thus \(\mathcal O(1)\) generates. Restriction to a line detects its exponent by degree, so it has infinite order.

Choose the flag cut out by the successive equations:
\[
\mathbb P^N=X_0\supset X_1\supset\cdots\supset X_c=Y.
\]
At the \(j\)-th step \(X_j\) is an effective ample Cartier divisor in \(X_{j-1}\), given by a positive-degree section of its \(\mathcal O(d_j)\). All preceding dimensions are at least four. They are pure Cohen–Macaulay, so their depth-plus-closure sum is their dimension, greater than two. Each local ring at a closed point is a quotient of a regular local ring by a regular sequence and has that dimension, at least four. Theorem 4.2 makes it parafactorial.

Theorem 5.1 therefore compares \(\operatorname{Pic}(X_{j-1})\) with the formal Picard group along \(X_j\). Its layers are
\(\mathcal O_{X_j}(-nd_j)\). Since \(\dim X_j\ge3\), Lemma 6.1 kills both their \(H^1\) and \(H^2\) for every \(n\ge1\). The second assertion of Theorem 5.1 gives
\[
\operatorname{Pic}(X_{j-1})\xrightarrow{\sim}\operatorname{Pic}(X_j).
\]
Induction gives (6.3), with the indicated generator because every restriction preserves \(\mathcal O(1)\). No step uses Kodaira vanishing or smoothness. ∎

For example, a smooth cubic threefold in \(\mathbb P^4\) has Picard group \(\mathbb Z\) generated by its hyperplane bundle. The argument also applies to singular and nonreduced complete intersections of the stated dimension.

## 7. Sharpness of the bounds

**Example 7.1 (the local quadric cone).** Let
\[
A=k[[x,y,z,w]]/(xy-zw),\qquad
I=(x,z),\qquad U=\operatorname{Spec}A\setminus\{\mathfrak m\}.
\tag{7.1}
\]
The plane \(V(x,z)\) cuts out a Cartier divisor on \(U\). On \(D(x)\) and \(D(z)\) its ideal is the unit ideal. On \(D(y)\) the equation gives \(x=zw/y\), so the ideal is generated by \(z\); on \(D(w)\) it is generated by \(x\). These generators are nonzerodivisors. Thus \(\widetilde I|_U\) is an invertible ideal, denoted \(\mathcal O_U(-D)\).

The ring \(A\) is a three-dimensional hypersurface and has depth three. Its quotient \(A/I=k[[y,w]]\) has depth two. The depth lemma in
\[
0\to I\to A\to A/I\to0
\]
gives \(\operatorname{depth}I\ge3\). In particular the support sequence gives
\[
\Gamma(U,\widetilde I)=I,\qquad \Gamma(U,\mathcal O_U)=A.
\]
If the invertible ideal were trivial, these modules would be isomorphic, so \(I\) would be cyclic. But its images \(x,z\) are linearly independent in \(I/\mathfrak m I\): every element of \(\mathfrak m I\) has order at least two, while the relation \(xy-zw\) has no linear term. Hence \(I\) needs two generators and cannot be cyclic. This proves the nonzero local Picard class [Stacks, [Tag 0F2J](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebraization.html#algebraization-example-grothendieck-sharp)].

For completeness, the generators used above are regular: in the ambient power-series UFD the element \(xy-zw\) is not divisible by \(x\) or \(z\), so each is relatively prime to it. If \(xa\) or \(za\) lies in its principal ideal, divisibility forces \(a\) to lie there. Thus \(x,z\) are nonzerodivisors in \(A\), and remain so on localization. The same Cartier divisor gives a nontrivial class on the punctured affine cone \(k[x,y,z,w]/(xy-zw)\); triviality there would persist after localization and completion at the vertex, contradicting (7.1). Dimension three is too small for Theorem 4.2.

**Example 7.2 (the split quadric surface).** The Segre map
\[
\mathbb P^1\times\mathbb P^1\longrightarrow\mathbb P^3,\qquad
([a:b],[c:d])\longmapsto[ac:bd:ad:bc]
\]
identifies its image with \(xy=zw\). Its two ruling bundles give
\[
\operatorname{Pic}(Q)=\mathbb Z[\mathcal O(1,0)]
\oplus\mathbb Z[\mathcal O(0,1)].
\tag{7.2}
\]
Here is the usual calculation. The degree of a line bundle on a fibre of the first projection is constant. Tensor with the inverse of that degree's \(\mathcal O(0,1)\); the resulting bundle has trivial restriction to every fibre. Its pushforward to the first \(\mathbb P^1\) is a line bundle, and the evaluation map is an isomorphism, by the degree-zero cohomology of \(\mathcal O_{\mathbb P^1}\) and base change. It is therefore a pullback \(\mathcal O(a,0)\). Restriction to the two fibre lines detects \(a\) and the original degree, proving the direct sum.

The hyperplane bundle restricts as \(\mathcal O(1,1)\). Consequently
\(\operatorname{Pic}(\mathbb P^3)\to\operatorname{Pic}(Q)\) has diagonal image and is not surjective. The target dimension is two, so the degree-two layer vanishing needed in the complete-intersection proof is absent. Over an algebraically closed field every smooth quadric surface is split and this is its Picard calculation. Over an arbitrary field a smooth nonsplit quadric need not have this Picard group; the split or algebraically closed qualification is essential.

## 8. Exercises and solutions

**Exercise 8.1 (regular puncture; elementary).** Compute the Picard group of the punctured spectrum of \(k[[x,y]]\).

**Solution.** This is a regular local ring of dimension two. Theorem 3.2 gives zero. More explicitly any coherent extension of a line bundle has a finite free resolution; its determinant on the puncture is the original line bundle and also the alternating tensor product of trivial determinants. Thus that line bundle is trivial.

**Exercise 8.2 (the plane on a cone; intermediate).** Prove that \(V(x,z)\) gives a nontrivial local Picard class for (7.1).

**Solution.** The four opens \(D(x),D(y),D(z),D(w)\) cover \(U\). The ideal \(I\) is respectively generated by \(1,z,1,x\) there, with the last two nonunit generators regular, so it is invertible on the puncture. The exact sequence with quotient \(k[[y,w]]\) gives depth at least three for \(I\), hence \(\Gamma(U,\widetilde I)=I\). If it were trivial, \(I\simeq A\) would be cyclic. Its two independent linear generators in \(I/\mathfrak mI\) rule that out. The hypersurface is a complete intersection of dimension three, locating the sharp failure of the dimension-four theorem.

**Exercise 8.3 (quadric surface; intermediate).** Compute the Picard restriction for a smooth quadric surface over an algebraically closed field.

**Solution.** Identify it with the Segre product. Its two fibre degrees give \(\operatorname{Pic}(Q)=\mathbb Z^2\), and the ambient hyperplane restricts to \((1,1)\). The class \((1,0)\) cannot extend from \(\mathbb P^3\). The failed global complete-intersection hypothesis is dimension at least three for the target. Indeed for its Cartier thickening the layer \(\mathcal O_Q(-2n)\) is \(\mathcal O(-2n,-2n)\); its \(H^2\) is nonzero for \(n\ge1\), by the two-factor Čech/Künneth computation \(H^1(\mathbb P^1,\mathcal O(-2n))^{\otimes2}\). One cannot discard the obstruction group.

**Exercise 8.4 (hypersurface vanishing; intermediate).** For a hypersurface \(Y\subset\mathbb P^N\) of degree \(d\), \(N\ge4\), prove that \(H^1(Y,\mathcal O_Y(m))=H^2(Y,\mathcal O_Y(m))=0\) for every integer \(m\).

**Solution.** The exact sequence (6.2) with \(W=\mathbb P^N\) gives each of these groups between a middle degree \(H^i(\mathbb P^N,\mathcal O(m))\) and the next middle degree \(H^{i+1}(\mathbb P^N,\mathcal O(m-d))\). For \(i=1,2\), all four groups vanish because \(i+1\le3<N\). Exactness gives the claim for every twist, positive or negative, over every field.

**Exercise 8.5 (complete intersections; advanced).** Prove (6.3) by the successive-equation route.

**Solution.** Cut the complete intersection by its homogeneous regular sequence, retaining its flag of intermediate schemes. Every ambient member before the last has dimension at least four and is pure Cohen–Macaulay. Its depth-plus-closure sum exceeds two; its closed local rings are complete intersections of dimension at least four, hence parafactorial by Theorem 4.2. Theorem 5.1 compares its Picard group with the formal Picard group along the next ample Cartier divisor. Lemma 6.1 kills the \(H^1,H^2\) of all layers, since that next divisor has dimension at least three. Proposition 1.1 and compatible units then identify the formal group with the divisor's Picard group. Repeat this isomorphism through the flag, starting with \(\mathbb Z[\mathcal O_{\mathbb P^N}(1)]\). Every restriction preserves that bundle, so the final group and generator are exactly (6.3).

## Proofs and further inputs

The polynomial argument proves both torsion injectivity at its elementary depth hypotheses and full injectivity under Theorem 2.5's duality hypotheses. Its finite locally free cohomology comparison is supplied by the exact linked open proof at [Stacks, [Tag 0BPY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/local-cohomology.html#local-cohomology-lemma-local-finiteness-for-finite-locally-free)]. Finite free resolutions over regular local rings were proved in Local duality and finiteness. Finite-presentation spreading and projective-space cohomology are commutative-algebra and cohomology inputs with the precise open sources recorded above. Principal formal-bundle algebraization is the exact local input already recorded in Formal geometry; the projective formal comparison and existence results in Section 5 were proved there. Linked Stacks source proofs retain their [GNU Free Documentation License](https://github.com/stacks/stacks-project/blob/master/COPYING); the independently written lesson text is CC0.

No Ramanujam–Samuel theorem is used. The local and global complete-intersection conclusions do not follow from a characteristic-zero vanishing theorem: the required vanishing and the dimension thresholds were proved explicitly above.

## References

- [Stacks] The Stacks Project authors, *The Stacks Project*, [official project](https://stacks.math.columbia.edu/). Tag links use AI Integrated Stacks Project, an edition with AI-proposed corrections and AI-written additions, not reviewed by the Stacks Project's maintainers. Its [English reader](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/) retains upstream tags. Relevant sections are More on Morphisms, “Picard groups of thickenings”; Algebraic and Formal Geometry, “Coherent triples” and “Invertible modules on punctured spectra”; and Divisors, the parafactoriality and Samuel–Grothendieck statements.
- [Grothendieck–Laszlo] A. Grothendieck, *Cohomologie locale des faisceaux cohérents et théorèmes de Lefschetz locaux et globaux (SGA 2)*, revised edition edited by Y. Laszlo, [arXiv:math/0511279](https://arxiv.org/abs/math/0511279), Exposé XI, especially the Picard comparison, parafactoriality and codimension-three factoriality results.
