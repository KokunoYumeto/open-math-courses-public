# Constructible costalks and Verdier duality

A constructible complex has perfect stalks. Its costalks are perfect too, but this needs a local cohomology argument: the costalk is the fibre of restriction from a small ball to its punctured ball. Verdier duality exchanges these two measurements, with their degrees intact. The resulting biduality comes from the actual evaluation map.

Use the [three small-ball comparisons](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/small-balls-central-fibres-and-supported-cohomology.md#the-three-comparisons) with their [proper-support transport](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/small-balls-central-fibres-and-supported-cohomology.md#transport-along-the-map-proper-on-coefficient-support) and [compact chart cutoff](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/small-balls-central-fibres-and-supported-cohomology.md#applying-the-theorem-in-an-open-coordinate-chart) for the local restriction and support maps. The [compact-set perfection lemma](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/perfect-coefficients-on-compact-fibres.md#finite-descent-on-a-compact-triangulation) applies to the small sphere. Weak duality uses [internal-Hom stability](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH03/weak-constructibility-under-sheaf-operations.md#tensor-and-internal-hom-retain-the-full-limiting-sum) together with the uniform bounded-Hom estimate.

The exceptional-operation proofs supply [trace-normalized dual sections](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-dual-sections--duality-of-ordinary-and-supported-sections) and the [exceptional internal-Hom comparison](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/exceptional-operations.md#sh02-ex-hom--exceptional-inverse-image-of-internal-hom). The cohomological-biduality lesson specifies [formal neighborhood systems](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/cohomological-biduality.md#sh02-cb-systems--what-stabilization-means), their [canonical stalk and costalk comparisons](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/cohomological-biduality.md#sh02-cb-costalk-continuity--stalk-and-costalk-compatibility) and the [evaluation-compatible dual pairings](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/sheaf-proof-readings/src/SH02/cohomological-biduality.md#sh02-cb-biduality--duality-exchanges-the-two-local-measurements). We apply these contracts to the small-ball systems below.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text is public domain (CC0).*

## The two local measurements

Let \(k\) be commutative of finite global dimension. Let \(X\) be a finite-dimensional real analytic manifold, Hausdorff and countable at infinity, with a uniform dimension bound. All complexes are globally bounded. Write

\[
A_x(F)=F_x,\qquad C_x(F)=i_x^!F=R\Gamma_{\{x\}}(X;F),
\qquad D_XF=R\mathcal Hom(F,\omega_X).
\tag{1}
\]

Here \(i_x\) is the point inclusion and \(\omega_X\) the manifold dualizing complex. A perfect coefficient complex has a bounded finite-projective representative. For coefficients put \(P^\vee=R\operatorname{Hom}_k(P,k)\). This notation does not assert perfection or biduality of \(P\).

Suppose first that \(F\) is only weakly \(\mathbb R\)-constructible. In a coordinate chart centered at \(x\), the small-ball theorem gives, for sufficiently small radii, the actual compatible isomorphisms

\[
R\Gamma(B_\epsilon;F)\longrightarrow A_x(F),\qquad
C_x(F)\longrightarrow R\Gamma_c(B_\epsilon;F).
\tag{2}
\]

All shrinking ordinary restrictions and compact-support extension maps commute with these identifications. The theorem also gives ordinary sections on closed balls and on the punctured ball, with the latter identified by restriction with sections on any sufficiently small interior sphere. A compact chart cutoff justifies the local application when the chart is not globally proper.

The balls are cofinal among neighborhoods of \(x\). Therefore the formal ind-system of ordinary sections is represented by \(A_x(F)\), and the formal pro-system of compact sections by \(C_x(F)\). Their representing maps are the canonical ones in (2). This statement retains the transition maps. It is stronger than stabilization of the dimensions of cohomology groups. Neither representative is yet claimed perfect.

The existing definition calls \(F\) **cohomologically constructible** when these two formal neighborhood systems are represented, their canonical representatives are the stalk and costalk, and both representatives are perfect. Within the weakly constructible class, (2) has already supplied everything except the two perfection conditions.

## Perfect stalks give perfect costalks

**Proposition.** If \(F\in D^b_{\mathbb R\text{-}c}(k_X)\), then \(C_x(F)\) is perfect for every \(x\).

**Proof.** In positive dimension choose a small coordinate ball and an interior sphere \(S_\delta\), with \(0<\delta<\epsilon\), within the stabilized range. Support localization and the actual small-ball restrictions give

\[
C_x(F)\longrightarrow A_x(F)
\xrightarrow{u_x}R\Gamma(S_\delta;F|_{S_\delta})\xrightarrow{+1}.
\tag{3}
\]

The map \(u_x\) is restriction through the punctured ball. The stalk term is perfect by definition. The sphere is compact and subanalytic, so its section complex is perfect by the compact-set lemma. That lemma applies to the whole ordinary restriction of \(F\); it does not require a globally constant coefficient on the sphere. Finite cone closure makes the fibre in (3) perfect. In dimension zero the point is open locally and its costalk equals its stalk. \(\square\)

Consequently, for bounded weakly constructible \(F\),

\[
F\text{ is }\mathbb R\text{-constructible}
\quad\Longleftrightarrow\quad
F\text{ is cohomologically constructible}.
\tag{4}
\]

The forward implication uses (2) and (3). The reverse implication uses the perfect stalk clause of the definition together with the given weak constructibility. The same definition directly makes every costalk perfect. No Noetherian hypothesis enters (3) or (4).

## Duality exchanges the measurements before biduality

The dual-sections prerequisite identifies, naturally and with the evaluation pairings,

\[
R\Gamma(U;D_XF)\simeq
R\operatorname{Hom}_k(R\Gamma_c(U;F),k).
\tag{5}
\]

For bounded weakly constructible \(F\), its compact-section system in (2) is already constant as a formal system with representative \(C_x(F)\). Applying the contravariant derived coefficient dual gives a represented ordinary-section system for \(D_XF\). Exact filtered stalk colimits then give

\[
(D_XF)_x\simeq C_x(F)^\vee.
\tag{6}
\]

This application uses a functor on a represented formal system. It requires no assertion that derived Hom commutes with an arbitrary inverse limit.

The other measurement follows directly from exceptional duality, without any perfection assumption. The normalized formula
\(i_x^!D_XF\simeq D_{\{x\}}(i_x^{-1}F)\), obtained from internal exceptional adjunction and \(i_x^!\omega_X=\omega_{\{x\}}=k\), gives

\[
C_x(D_XF)\simeq A_x(F)^\vee.
\tag{7}
\]

Both are canonical local dual pairings. Boundedness of \(D_XF\) follows from the manifold bounded-Hom theorem and the bounded orientation complex. Weak constructibility follows from the weak internal-Hom theorem, since \(\omega_X\) is a locally constant shifted orientation line. Thus the small-ball stabilization also applies to \(D_XF\).

If all \(C_x(F)\) are perfect, then their coefficient duals are perfect, so (6) makes \(D_XF\) \(\mathbb R\)-constructible. We have proved the general-ring implications

\[
\begin{gathered}
F\text{ is }\mathbb R\text{-constructible}
\ \Longleftrightarrow\ F\text{ is cohomologically constructible},\\
F\text{ is cohomologically constructible}
\ \Longrightarrow\ (\forall x,\ C_x(F)\text{ perfect})
\ \Longrightarrow\ D_XF\text{ is }\mathbb R\text{-constructible}.
\end{gathered}
\tag{8}
\]

These are assertions about a given bounded weakly constructible input. That standing assumption supplies the geometric part of the output and the local stabilization used in (6).

## The evaluation map is biduality

If \(P\) is perfect, then \(P^\vee\) is perfect and the canonical evaluation
\(\eta_P:P\to P^{\vee\vee}\) is an isomorphism. Indeed, for a finite projective module evaluation is the usual coordinate isomorphism for a finite free module, restricted to a direct summand. A bounded finite-projective complex gives the same chain isomorphism, with the standard cohomological dual signs.

For constructible \(F\), (8) makes \(D_XF\) constructible. Apply (6) to its dual and use (7):

\[
(D_XD_XF)_x\simeq C_x(D_XF)^\vee
\simeq A_x(F)^{\vee\vee}.
\tag{9}
\]

Under these identifications the stalk of the sheaf evaluation map
\(F\to D_XD_XF\) is \(\eta_{A_x(F)}\). This is where the natural maps matter: (5)–(7) come from the adjunction evaluation and trace, and restriction and support extension preserve those pairings. They identify the actual evaluation, rather than just two abstractly isomorphic objects. Perfectness makes it an isomorphism at every stalk; stalkwise detection gives

\[
F\xrightarrow{\sim}D_XD_XF.
\tag{10}
\]

Thus Verdier duality is a contravariant equivalence on the bounded \(\mathbb R\)-constructible category over the full coefficient ring in use. On a map \(F\to G\) its direction is \(D_XG\to D_XF\). Orientations have remained inside \(\omega_X\); no global orientation was chosen.

## Detecting perfection over a field or the integers

To reverse the last implication in (8), we need an additional algebraic detection result. We prove it for the two coefficient rings treated here.

**Detection lemma.** Let \(k\) be a field or \(\mathbb Z\), and \(M\in D^b(k)\). If \(M^\vee\) is perfect, then \(M\) is perfect.

We first prove that the coefficient dual detects zero on bounded complexes. Over a field, dualization is exact and a nonzero vector space has a nonzero linear functional. Its derived dual therefore detects each nonzero cohomology group.

For \(\mathbb Z\), start with an abelian group \(T\) such that

\[
\operatorname{Hom}(T,\mathbb Z)=0,
\qquad\operatorname{Ext}^1(T,\mathbb Z)=0.
\tag{11}
\]

The integral coefficient dual has no Ext degrees above one. One concrete reason is the injective resolution
\(0\to\mathbb Z\to\mathbb Q\to\mathbb Q/\mathbb Z\to0\).
Divisible groups are injective: to extend a homomorphism from a subgroup across one new element, divide its prescribed multiple if that element has finite order modulo the subgroup, and choose an arbitrary value if it has infinite order there. The least positive multiple in the subgroup makes the first extension well-defined. Zorn's lemma then extends across the whole group. This proves injectivity of both displayed divisible groups.

If \(T\) contained a subgroup \(\mathbb Z/n\), with \(n>1\), its inclusion and the long Ext sequence would give a surjection
\(\operatorname{Ext}^1(T,\mathbb Z)\to\operatorname{Ext}^1(\mathbb Z/n,\mathbb Z)=\mathbb Z/n\), because the next Ext degree of the quotient vanishes. Hence (11) makes \(T\) torsion free.

For each prime \(p\), apply \(\operatorname{Hom}(T,-)\) to
\(0\to\mathbb Z\xrightarrow{p}\mathbb Z\to\mathbb Z/p\to0\).
Equation (11) gives \(\operatorname{Hom}(T,\mathbb Z/p)=0\). If \(T/pT\) were nonzero, its vector-space structure over \(\mathbb F_p\) would give a nonzero such functional. Thus \(pT=T\). Factoring integers into primes makes \(T\) divisible. A torsion-free divisible group is a \(\mathbb Q\)-vector space, with division by each nonzero integer uniquely determined.

We also need \(\operatorname{Ext}^1(\mathbb Q,\mathbb Z)\ne0\). Here is a proof. Put \(B=\mathbb Z[1/2]\). Every compatible family \(a_n\in\mathbb Z/2^n\), with \(a_{n+1}\equiv a_n\pmod{2^n}\), defines

\[
h_a:B\to\mathbb Q/\mathbb Z,\qquad
h_a(2^{-n})=a_n/2^n\pmod{\mathbb Z}.
\tag{12}
\]

These homomorphisms vanish on \(\mathbb Z\), and arbitrary infinite binary sequences give uncountably many distinct compatible families. Injectivity of \(\mathbb Q/\mathbb Z\) extends each to \(\mathbb Q\); distinct restrictions give distinct extensions. In contrast, every map \(\mathbb Q\to\mathbb Q\) is multiplication by one rational number, so there are only countably many maps which can lift to \(\mathbb Q\). The injective resolution identifies

\[
\operatorname{Ext}^1(\mathbb Q,\mathbb Z)
\simeq\operatorname{Hom}(\mathbb Q,\mathbb Q/\mathbb Z)
\big/\operatorname{im}\operatorname{Hom}(\mathbb Q,\mathbb Q).
\tag{13}
\]

This quotient is nonzero, and in fact uncountable. If \(T\ne0\), a vector-space complement gives \(T\simeq\mathbb Q\oplus L\). Its Ext group then has the nonzero group in (13) as a summand, contradicting (11). Thus \(T=0\).

For bounded \(M\), the integral hyper-Ext spectral sequence has only columns zero and one. Its short exact sequences are

\[
0\longrightarrow\operatorname{Ext}^1(H^{q+1}(M),\mathbb Z)
\longrightarrow H^{-q}(M^\vee)
\longrightarrow\operatorname{Hom}(H^q(M),\mathbb Z)
\longrightarrow0.
\tag{14}
\]

Finite cohomological bounds justify convergence, and no splitting of these sequences is assumed. If \(M^\vee=0\), (14) and the group argument make every \(H^q(M)\) zero. This proves zero detection over \(\mathbb Z\).

Now put \(N=M^\vee\), assumed perfect. Its evaluation \(\eta_N:N\to N^{\vee\vee}\) is an isomorphism. The evaluation identity

\[
(\eta_M)^\vee\circ\eta_{M^\vee}
=\operatorname{id}_{M^\vee}
\tag{15}
\]

makes \((\eta_M)^\vee\) its inverse, hence an isomorphism. Dualize the cone of \(\eta_M\). It is zero; zero detection makes that cone zero. Therefore \(M\simeq M^{\vee\vee}=N^\vee\), which is perfect. This proves the lemma. It does not presuppose biduality of \(M\).

Finally suppose \(D_XF\) is constructible. Its costalks are perfect by (3); (7) says that these are \(F_x^\vee\). The detection lemma makes every \(F_x\) perfect. The given weak constructibility then makes \(F\) constructible. Thus all four conditions in (8) are equivalent over a field or \(\mathbb Z\). For the general coefficient ring we retain precisely the implications already proved in (8).

## Examples and exercises with solutions

### A line costalk carries the integration degree

*Difficulty: Introductory.*

Let \(P\) be a perfect coefficient complex, constant on the oriented real line. Calculate its stalk, costalk and Verdier-dual stalk at zero, including the map used for the costalk.

**Solution.** The stalk is \(P\). A punctured small interval has two contractible components, so its coefficient complex is \(P\oplus P\). The restriction map is the diagonal
\(P\to P\oplus P\). Its fibre is \(P[-1]\), using the increasing orientation to identify the difference quotient by \((a,b)\mapsto b-a\). Equation (6) gives the dual stalk \((P[-1])^\vee=P^\vee[1]\). This agrees with \(\omega_{\mathbb R}=k_{\mathbb R}[1]\) and
\(D_{\mathbb R}P_{\mathbb R}=(P^\vee)_{\mathbb R}[1]\).
For \(P=k\), the costalk is in degree one and the dual stalk in degree minus one. These opposite degrees come from fibre and dual operations.

### Integral torsion at a point survives duality

*Difficulty: Intermediate.*

In \(X=\mathbb R^2\), let \(i:\{0\}\hookrightarrow X\) and
\(F=i_*(\mathbb Z/n)\), \(n>1\). Compute both local measurements, \(D_XF\), and its second dual.

**Solution.** Sections on a small ball are the point coefficient, and all their support is at that point. Thus \(A_0(F)=C_0(F)=\mathbb Z/n\), while both measurements vanish elsewhere. Resolve the coefficient by \([\mathbb Z\xrightarrow{n}\mathbb Z]\) in degrees minus one and zero. Its derived integral dual has zero degree-zero cohomology and \(\mathbb Z/n\) in degree one, hence is \((\mathbb Z/n)[-1]\). Exceptional duality for the closed point gives
\(D_XF=i_*((\mathbb Z/n)[-1])\): the dualizing complex of the point is \(\mathbb Z\), so no ambient two-dimensional shift is inserted in this point calculation. Dualizing again yields
\((\mathbb Z/n[-1])^\vee=(\mathbb Z/n)^\vee[1]=\mathbb Z/n\).
The actual finite-projective evaluation gives \(F\to D_XD_XF\) as an isomorphism. Perfection includes this torsion, and ordinary \(\operatorname{Hom}(\mathbb Z/n,\mathbb Z)=0\) alone would miss its dual.

### A closed half-line has zero boundary costalk

*Difficulty: Intermediate.*

On the increasing oriented real line take \(F=k_{[0,\infty)}\). Compute \(C_0(F)\), the stalks of \(D_{\mathbb R}F\), and the resulting dual sheaf complex.

**Solution.** At zero the ordinary stalk is \(k\). The left punctured interval contributes zero and the right contributes \(k\); the restriction map is \(k\xrightarrow{\mathrm{id}}k\). Its fibre is zero, so \(C_0(F)=0\). At a positive point the costalk is \(k[-1]\), and at a negative point it is zero. Thus (6) gives dual stalks \(k[1]\) on the positive open half-line and zero at and to the left of zero. On that open half-line the dual is its constant shifted coefficient by the local orientation calculation. Localization, with zero ordinary restriction to the closed complement, identifies the whole object with its open extension:
\(D_{\mathbb R}F=k_{(0,\infty)}[1]\).
All these local measurements are perfect, including the zero boundary costalk. The theorem then returns \(F\) on a second dualization. A nonzero stalk need not give a nonzero costalk at the same point.

### Rank of the attachment map determines two dual degrees

*Difficulty: Intermediate.*

Work over a field. Near a cut on the line, let the point stalk be \(A=k^a\), the sum of its two neighboring interval coefficients be \(B=k^b\), and the actual restriction \(u:A\to B\) have rank \(r\). Compute the costalk and dual stalk cohomology at the cut.

**Solution.** The costalk is the two-term complex \([A\xrightarrow{u}B]\) in degrees zero and one. Its cohomology is \(\ker(u)\) in degree zero and \(\operatorname{coker}(u)\) in degree one, of dimensions \(a-r\) and \(b-r\). Exact field dualization reverses the degrees. Thus the dual stalk has \(\operatorname{coker}(u)^*\) in degree minus one and \(\ker(u)^*\) in degree zero, and no other cohomology. Its costalk is \(A^*\) in degree zero by (7). In particular the list of coefficient dimensions \(a,b\) does not determine the dual stalk: the attachment rank changes both groups. Every displayed complex is perfect.

### Stabilized infinite coefficients still fail biduality

*Difficulty: Advanced.*

Over a field let \(V=\bigoplus_{m\geq1}k\) and \(F=i_*V\) at one point of a manifold. Its neighborhood systems stabilize. Decide whether it is cohomologically constructible, whether its dual is \(\mathbb R\)-constructible, and whether evaluation into the second dual is an isomorphism.

**Solution.** Both local measurements at the point are \(V\), with identity transitions; elsewhere they are zero. Thus representability and the canonical comparisons hold. The point coefficient is infinite dimensional, so it is not perfect and the full cohomological-constructibility condition fails. Its dual is \(i_*V^*\), with \(V^*\simeq k^{\mathbb N}\). The coordinate vectors already give infinitely many independent elements of this product, so the dual is also not constructible.

The evaluation \(V\to V^{**}\) is injective but is not onto. The quotient \(k^{\mathbb N}/k^{(\mathbb N)}\) is nonzero, as seen from the all-ones sequence. Choose a linear functional on the quotient nonzero on that class, and compose it with the quotient map. The resulting functional on \(V^*=k^{\mathbb N}\) vanishes on all finitely supported sequences but is nonzero. Evaluation by a vector \(v\in V\) is a finite linear combination of coordinate evaluations. If it vanished on every finitely supported sequence, all coefficients of \(v\) would be zero. Therefore the chosen functional is outside the evaluation image. This establishes the failure directly. The weak small-ball stabilization never asserted finite coefficients or weak biduality.

### The rational point coefficient is detected in Ext

*Difficulty: Advanced.*

Over \(\mathbb Z\), let \(F=i_*\mathbb Q\). Show that its coefficient dual is nonzero although its ordinary integral Hom is zero. Give a specific homomorphism which represents a nonzero Ext class, and decide whether the dual is perfect.

**Solution.** A homomorphism \(\mathbb Q\to\mathbb Z\) sends \(1\) to an integer divisible by every positive integer, hence to zero; unique rational division then makes the entire map zero. To obtain an Ext class, set
\(a_n=\sum_{m!<n,\ m\geq2}2^{m!}\pmod{2^n}\).
These residues are compatible. Equation (12) defines a homomorphism on \(\mathbb Z[1/2]\), zero on \(\mathbb Z\). Extend it to \(\mathbb Q\) by injectivity of \(\mathbb Q/\mathbb Z\).

It cannot lift to a map \(\mathbb Q\to\mathbb Q\). Such a lift would be multiplication by a rational \(q\); its value at \(1\), reduced modulo \(\mathbb Z\), is zero, so \(q\) would be an integer. Its residues modulo \(2^n\) would then have to be every \(a_n\). A nonnegative integer has binary digits eventually zero, and a negative integer has its compatible binary digits eventually one. The chosen digits have infinitely many isolated ones at factorial positions and arbitrarily long zero gaps, so neither is possible. Equation (13) makes this a nonzero element of
\(E=\operatorname{Ext}^1(\mathbb Q,\mathbb Z)\).

The coefficient dual is \(E[-1]\). The proof of (13) also gives uncountably many distinct classes, since an uncountable set is being divided by a countable subgroup. Thus \(E\) is not finitely generated over \(\mathbb Z\), and \(E[-1]\) is not perfect. Accordingly \(D_XF=i_*E[-1]\) is weakly constructible but not \(\mathbb R\)-constructible. This example explains why derived dual detection over the integers must include its Ext degree.

## References

Masaki Kashiwara and Pierre Schapira, *Microlocal study of sheaves*, Astérisque 128 (1985), [Definition 5.6.1 and Proposition 5.6.2, printed p. 98](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf#page=101), give the formal perfect-system definition and a biduality statement using the constant sheaf as dualizing coefficient. [Remark 8.2.9, printed p. 148](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf#page=151), states that real constructible complexes satisfy that cohomological constructibility condition.

Pierre Schapira, [*An Introduction to Sheaves on Grothendieck Topologies*, 1 August 2026, §4.8, pp. 98–99](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/SHV.pdf#page=98), gives the neighborhood-system definition and its canonical comparisons in Definition 4.8.2. Remark 4.8.1 replaces the Noetherian finiteness condition by perfection. Proposition 4.8.3 states Verdier biduality and the stalk–costalk exchanges, leaving its proof as an exercise. The adjunction and evaluation arguments used here are supplied by the linked programme proofs.

- The neighborhood-system and evaluation contracts specify cohomological constructibility and natural biduality; they come from the existing prerequisite lane. The application here retains their canonical maps.
- The integral detection argument above includes nonvanishing of the rational Ext group and detection of perfection through the evaluation cone.

## Accessible duality comparison

Andreas Hohl and Pierre Schapira, [*Unusual functorialities for weakly constructible sheaves*, version 2, 7 January 2025, §3](https://arxiv.org/abs/2303.11189v2), state the stalk–costalk duality proposition for weakly cohomologically constructible sheaves. The author source labels it `pro:dual` and explains that perfection is unused in the earlier proof, which it does not repeat. The natural small-ball systems and evaluation proofs in this lesson retain that weak-coefficient assertion; perfection is required when evaluation is inverted. The modern inverse/direct comparison extensions follow the [constructible evaluation criterion](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#applying-the-criterion-to-constructible-coefficients-constructible-case) and [infinite-twist comparison proofs](https://github.com/KokunoYumeto/open-math-courses-public-public/blob/main/docs/courses/constructible-duality-and-infinite-twists/src/duality-maps-for-constructible-inverse-and-direct-images.md#infinite-twists-applying-hom-instead-of-biduality-infinite-twists), without inverting evaluation of an infinite locally constant twist.

## Readable source and dependency account

The small-ball comparison maps identify the formal neighbourhood systems before dualizing them. Perfection of a costalk is proved from a compact supported-cohomology fibre; the actual evaluation map then becomes the perfect-complex evaluation under those identifications. The field and integer detection arguments, including the rational Ext calculation, are independent arguments written here. They do not assert the converse for every ring. The free notes leave a biduality proof as an exercise, so that exercise is not cited as a completed proof of the larger coefficient scope.

For the distinction between the two duality functors and the perfect-complex condition at a point, see Pierre Schapira, [*A short review on microlocal sheaf theory*, 19 January 2016, p. 7](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf#page=7). This is notation and coefficient context for the arguments above. Original programme exposition remains CC0; the human works retain their own rights.
