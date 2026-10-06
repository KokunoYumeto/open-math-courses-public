# Serre's comparison theorems and Chow's theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).* 

Locally, analytification preserves exact sequences but adds holomorphic functions. On a projective variety, the three comparison theorems say much more: coherent cohomology agrees, every analytic morphism of coherent sheaves is algebraic, and every coherent analytic sheaf is algebraic. We prove these assertions in that order. The proof of the last assertion needs a finite-dimensional analytic cohomology theorem; using the comparison theorem to assert finiteness for an arbitrary analytic sheaf at this stage would be circular.

Throughout, varieties are reduced separated schemes of finite type over \(\mathbf C\), as in Complex analytic spaces and analytification. Write \(P=\mathbf P^n_{\mathbf C}\), \(P^{\mathrm{an}}=\mathbf P^n(\mathbf C)\), and \(\mathcal O(d)^{\mathrm{an}}\) for the analytification of a twist. We use the generation, vanishing and projective cohomology proved in Serre's theorems and Cohomology of projective space.

## 1. The analytic cohomology foundation

Two openly reusable theorems will supply the analytic cohomology used below. Their proof provider is Jean-Pierre Demailly, *Complex Analytic and Differential Geometry*, version 21 June 2012, under the author's explicit [OpenContent permission](https://www-fourier.univ-grenoble-alpes.fr/~demailly/documents.html).

**Analytic vanishing theorem.** If a complex manifold admits a smooth strictly plurisubharmonic exhaustion, every coherent analytic sheaf on it has zero cohomology in positive degrees. An exhaustion has relatively compact sublevel sets; strict plurisubharmonicity means its complex Hessian is positive definite. The exact open proof is [Demailly, IX, Theorem 4.10 and Corollary 4.11, pp. 425–428](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=425), with the vector-bundle vanishing and local coherent resolutions proved in IX, Propositions 4.1 and 4.4, pp. 419–421. Corollary 4.11 is obtained by applying the theorem to the empty Runge open subset of a strongly complete space, so it gives vanishing rather than merely finite dimension.

**Analytic finiteness theorem (Cartan–Serre).** On a compact complex analytic space, the cohomology of every coherent analytic sheaf is finite-dimensional in every degree. The exact open proof is [Demailly, IX, Theorem 4.8, p. 424](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=424), including its preceding topology and local acyclicity constructions. It compares finite nested acyclic covers: restriction of coherent sections from a larger open set to a relatively compact smaller one is a compact operator, by the coherent version of Montel's theorem. The induced map between their Čech complexes is an isomorphism on cohomology. The [proved compact-operator criterion, IX, Theorems 1.8–1.9, pp. 406–407](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=406), then gives finite dimension and closed coboundaries. This proof applies before any algebraization of the sheaf is known.

For our standard projective cover \(U_i=\{T_i\ne0\}\), every nonempty intersection is biholomorphic to

\[
(\mathbf C^*)^r\times\mathbf C^{n-r}.
\]

The function

\[
\psi(z)=\sum_{j=1}^n|z_j|^2+\sum_{j=1}^r|z_j|^{-2}
\]

is a strictly plurisubharmonic exhaustion there. The first sum makes the Hessian positive, while the second prevents escape toward a deleted coordinate hyperplane. The vanishing theorem therefore makes this cover acyclic for every coherent analytic sheaf. By the Čech comparison proved earlier in the course, its ordered complex computes cohomology. There are \(n+1\) opens, so

\[
H^q(P^{\mathrm{an}},M)=0\qquad(q>n)
\tag{1}
\]

for every coherent analytic module \(M\). This bound concerns all coherent analytic modules, including those not yet known to be algebraic.

## 2. Starting the comparison: the structure sheaf and twists

**Lemma 2.1.** The analytic structure sheaf of projective space has cohomology \(\mathbf C\) in degree zero and zero in every positive degree. The natural comparison from algebraic cohomology is an isomorphism.

**Proof.** For \(n=0\), the space is a point. For general \(n\), use the acyclic cover of Section 1. A function on \(U_S=\bigcap_{i\in S}U_i\) pulls back to a homogeneous holomorphic function of weight zero on the cone where all \(T_i\), \(i\in S\), are nonzero. Choose one such coordinate as the denominator. The iterated Laurent expansion in the other nonzero ratios and Taylor expansion in the remaining ratios is unique and normally convergent on compact subsets. Its homogeneous monomials have exponents

\[
\alpha\in\mathbf Z^{n+1},\qquad
\sum_i\alpha_i=0,\qquad
\alpha_j\geq0\quad(j\notin S).
\]

Group the series by its negative-exponent set \(N=\{j:\alpha_j<0\}\). There are only finitely many such sets. Cauchy integrals in each ratio give these projections; normal convergence is preserved. When an inverted coordinate has only nonnegative powers, the corresponding projected series extends across its zero hyperplane. This follows directly from the positive part of the Laurent series: it is a Taylor series converging on every smaller compact polydisc, and the radii can be taken arbitrarily large in that ratio. Thus the extensions used below are holomorphic on the whole required intersection.

For a fixed \(N\), the allowed faces of the Čech complex are exactly the nonempty \(S\) containing \(N\). If \(N\) is proper and nonempty, choose an index \(j\notin N\). Inserting \(j\) into a face, with the sign of its ordered position, gives the usual simplex contraction: to define a component on \(U_S\) from one on \(U_{S\cup\{j\}}\), extend the nonnegative-power part across \(T_j=0\). The alternating differential satisfies \(dh+hd=1\). The identity is verified term by term, where all terms other than the face omitting \(j\) cancel in pairs. Normal convergence and the finite grouping by \(N\) make it an identity on the analytic series themselves.

If \(N\) is empty, all exponents are nonnegative and sum to zero, so the only monomial is 1. This is the ordinary simplex complex of constants, with cohomology \(\mathbf C\) in degree zero. If \(N\) were all indices, their sum would be negative, so this part is absent. These contractions prove the analytic assertion. Algebraically the same cohomology was computed in our projective-space lesson, and comparison sends a constant to the identical constant. \(\square\)

For any algebraic module \(F\), the map on global sections to those of \(F^{\mathrm{an}}\) extends canonically to maps

\[
c_F^q:H^q(X,F)\longrightarrow H^q(X^{\mathrm{an}},F^{\mathrm{an}}).
\tag{2}
\]

Indeed analytification is an exact functor on all modules, by local flatness. The target groups therefore form a cohomological delta functor, and the universal derived functors of algebraic global sections extend the degree-zero map uniquely. Consequently (2) is natural and commutes with connecting maps in long exact sequences. For coherent modules, it also commutes with closed-immersion pushforward, whose stalkwise quotient description was proved in the preceding lesson.

**Lemma 2.2.** Comparison is an isomorphism for \(\mathcal O(d)\) on \(\mathbf P^n\), for every integer \(d\) and every degree.

**Proof.** Induct on \(n\). On \(\mathbf P^0\) every twist is a one-dimensional module, including negative twists. For \(n>0\), let \(i:E\hookrightarrow P\) be a hyperplane. Its equation gives

\[
0\to\mathcal O(d-1)\to\mathcal O(d)
\to i_*\mathcal O_E(d)\to0.
\tag{3}
\]

Analytification preserves this sequence. The induction hypothesis supplies comparison on \(E\). The two long exact sequences show that comparison for \(\mathcal O(d)\) in all degrees is equivalent to comparison for \(\mathcal O(d-1)\): for either unknown term, take five successive terms with that term in the middle; all four other comparison maps are isomorphisms. Begin with \(d=0\), proved in Lemma 2.1, and move upward and downward. \(\square\)

## 3. The first comparison theorem

**Theorem 3.1 (cohomological GAGA).** If \(X\) is projective over \(\mathbf C\) and \(F\) is coherent, (2) is an isomorphism for every \(q\geq0\).

**Proof.** Embed \(X\) as a closed subvariety of \(P\). Closed-immersion pushforward is exact, preserves coherence and cohomology, and commutes with analytification. Thus it suffices to prove the result on \(P\).

Descend on \(q\), simultaneously for all coherent sheaves. For \(q>n\), both groups vanish: algebraically by the standard affine cover, analytically by (1). Choose a presentation

\[
0\to R\to L\to F\to0,
\tag{4}
\]

where \(L\) is a finite sum of twists and \(R\) is coherent. Suppose comparison in degree \(q+1\) is already known for every coherent sheaf. Lemma 2.2 gives comparison for \(L\) in every degree.

To prove surjectivity for \(F\) in degree \(q\), start with an analytic class. Its boundary in \(H^{q+1}(R^{\mathrm{an}})\) lifts uniquely to an algebraic class. That lift maps to zero in \(H^{q+1}(L)\), since its analytic image does and comparison for \(L\) is injective. Exactness lifts it to \(H^q(F)\). The difference between this class's analytic image and the original class has zero boundary, so comes from \(H^q(L^{\mathrm{an}})\). Comparison for \(L\) lifts the difference, establishing surjectivity.

This proves surjectivity in degree \(q\) for every coherent sheaf, in particular for \(R\). If an algebraic class in \(H^q(F)\) has zero analytic image, its boundary is zero by injectivity in degree \(q+1\) for \(R\), so it comes from \(H^q(L)\). That lift maps analytically into the image of \(H^q(R^{\mathrm{an}})\). Surjectivity for \(R\) lifts this correcting class. Subtract it in \(H^q(L)\); comparison for \(L\) forces the corrected lift to be zero. Thus the original class was zero. The induction proves injectivity and surjectivity in all degrees. \(\square\)

The simultaneous induction is essential: we first establish surjectivity for all coherent sheaves before using it for the kernel \(R\). No finite global locally free resolution of \(F\) has been assumed.

## 4. The second comparison theorem

**Theorem 4.1 (full faithfulness).** For coherent \(F,G\) on a projective complex variety,

\[
\operatorname{Hom}_X(F,G)
\xrightarrow{\sim}
\operatorname{Hom}_{X^{\mathrm{an}}}(F^{\mathrm{an}},G^{\mathrm{an}}).
\]

**Proof.** The internal Hom \(A=\mathcal Hom(F,G)\) is coherent. Finite presentations and local flatness give

\[
A^{\mathrm{an}}\cong\mathcal Hom(F^{\mathrm{an}},G^{\mathrm{an}}),
\]

as proved in Proposition 5.1 of the preceding lesson. Apply Theorem 3.1 in degree zero to \(A\). These global sections are exactly the two morphism groups, and the comparison takes a morphism to its analytification. \(\square\)

In particular, an analytic isomorphism between algebraic coherent sheaves lifts uniquely to an algebraic isomorphism: lift it and its inverse, then use faithfulness to identify their compositions with the identities.

## 5. The third comparison theorem

**Lemma 5.1 (analytic generation).** Every coherent analytic module \(M\) on \(P^{\mathrm{an}}\) has \(M(d)\) generated by finitely many global sections for all sufficiently large \(d\).

**Proof.** We prove this together with essential surjectivity, inducting on \(n\). At \(n=0\) a coherent module is a finite-dimensional vector space. Assume essential surjectivity on every hyperplane \(E\cong\mathbf P^{n-1}\). On \(E\), Theorem 3.1 and algebraic Serre vanishing now imply vanishing of all positive cohomology of sufficiently large twists of every coherent analytic module.

Fix \(x\in P^{\mathrm{an}}\) and choose a hyperplane through \(x\), with equation \(t\). Multiplication has coherent kernel and cokernel:

\[
0\to C\to M(-1)\xrightarrow{t}M\to B\to0.
\]

Both \(C\) and \(B\) are annihilated by \(t\), so are coherent modules on \(E^{\mathrm{an}}\). This remains true when multiplication by \(t\) is not injective. Let \(L_d\) be the image of \(M(d-1)\to M(d)\). The two short exact sequences give, for large \(d\), surjections

\[
H^1(M(d-1))\twoheadrightarrow H^1(L_d)
\twoheadrightarrow H^1(M(d)),
\tag{5}
\]

because \(H^2(C(d))=H^1(B(d))=0\). By the Cartan–Serre finiteness theorem in Section 1, these dimensions are finite. Thus the nonnegative integers \(h^1(M(d))\) eventually stop decreasing. In the stable range both arrows in (5) are isomorphisms. The second short exact sequence then shows that

\[
H^0(M(d))\twoheadrightarrow H^0(B(d)).
\tag{6}
\]

By induction \(B\) is algebraic on \(E\); its large twists are generated by global sections. Lift generators using (6). At \(x\), these generate \(M(d)_x/tM(d)_x\); Nakayama makes them generate \(M(d)_x\), since \(t\) belongs to the local maximal ideal.

Generation by finitely many fixed sections holds on a neighbourhood, because their coherent cokernel vanishes there. Once generation holds at a point in degree \(d\), multiplying these sections by a homogeneous coordinate nonzero at that point proves generation in every degree \(d'\geq d\). Compactness supplies finitely many neighbourhoods and a common bound on \(d\). At each such degree take the union of their finite generating families. This proves the lemma. \(\square\)

**Theorem 5.2 (essential surjectivity).** Every coherent analytic module on \(X^{\mathrm{an}}\), for projective \(X\), is isomorphic to \(F^{\mathrm{an}}\) for some coherent algebraic \(F\). Together with Theorem 4.1, analytification is an equivalence of coherent categories.

**Proof.** First take \(X=P\), continuing the induction of Lemma 5.1. Global generation gives a surjection \(L_0^{\mathrm{an}}\to M\), where \(L_0\) is a finite sum of equal negative twists. Its kernel \(R\) is coherent. Generate a twist of \(R\) as well, to obtain

\[
L_1^{\mathrm{an}}\xrightarrow{v}L_0^{\mathrm{an}}\to M\to0.
\]

Full faithfulness lifts \(v\) uniquely to an algebraic map \(u:L_1\to L_0\). Put \(F=\operatorname{coker}u\). Exactness of analytification gives \(F^{\mathrm{an}}\cong M\), completing the induction on \(n\).

For \(i:X\hookrightarrow P\), algebraize \(i_*M\) to \(G\) on \(P\). If \(I\) is the ideal of \(X\), then \((IG)^{\mathrm{an}}=I^{\mathrm{an}}G^{\mathrm{an}}=0\). Exactness and faithfulness give \(IG=0\). Hence \(G=i_*F\) for a unique coherent module \(F\) on \(X\). Compatibility with closed-immersion pushforward identifies \(F^{\mathrm{an}}\) with \(M\). \(\square\)

The correct uniqueness assertion fixes the identification. If \((F,\phi)\) and \((G,\psi)\) are algebraizations equipped with isomorphisms to \(M\), there is a unique isomorphism \(u:F\to G\) satisfying \(\psi\circ u^{\mathrm{an}}=\phi\). Without specified identifications, an algebraic sheaf can have many automorphisms: every nonzero scalar acts on \(\mathcal O_X\). Thus its bare isomorphism class is unique, but its possible isomorphisms are not.

## 6. Chow's theorem and geometric consequences

**Theorem 6.1 (Chow).** Every closed analytic subset of a complex projective variety is the analytification of a unique reduced closed algebraic subvariety.

**Proof.** Its analytic vanishing ideal \(J\subset\mathcal O_{X^{\mathrm{an}}}\) is coherent by Cartan coherence. Algebraize \(J\) as a coherent module by Theorem 5.2, and lift its inclusion into the structure sheaf by Theorem 4.1. Exactness and faithfulness make the lift injective, with image an algebraic coherent ideal \(I\) whose analytification is \(J\).

The ideal \(I\) is radical. At every closed stalk, if \(a^m\in I_x\), the image of \(a\) belongs to the radical ideal \(J_x=I_x\mathcal O_{X^{\mathrm{an}},x}\); faithful flatness contracts this to \(a\in I_x\). Radicality at closed stalks suffices: a nonzero nilpotent ideal in the coherent quotient would have support containing a closed point. The reduced closed scheme defined by \(I\) therefore analytifies to the given analytic subset. If two algebraic ideals have the same analytic extension, faithful flatness gives equal closed stalks, and coherent support detects equality globally. This proves uniqueness. \(\square\)

**Theorem 6.2.** Every holomorphic map between the analytifications of projective complex varieties is the analytification of a unique algebraic morphism.

**Proof.** Its graph is a closed reduced analytic subspace of the projective product. Apply Chow's theorem to algebraize the graph to \(Z\subset X\times Y\). The first projection \(p:Z\to X\) is proper and its analytification is an isomorphism. Each closed fiber has one complex point and is zero-dimensional. Upper semicontinuity of fiber dimension for proper maps shows that all fibers are zero-dimensional: any nonempty closed locus of positive-dimensional fibers would contain a closed point. Thus \(p\) has finite fibers and is finite by Formal functions, Theorem 5.2.

At a closed point \(x\), the finite algebra \((p_*\mathcal O_Z)_x=B\) over \(A=\mathcal O_{X,x}\) has only one maximal ideal, since the closed fiber has one point. Its maximal-ideal topology is cofinal with its \(\mathfrak m_A\)-adic topology. Thus \(B\otimes_A\widehat A=\widehat B\). Local analytic comparison and the analytic graph isomorphism identify the map \(\widehat A\to\widehat B\) with an isomorphism. Faithful flatness of completion makes \(A\to B\) an isomorphism. The kernel and cokernel of \(\mathcal O_X\to p_*\mathcal O_Z\) are coherent and vanish at every closed point, so they vanish everywhere. A finite map is the relative spectrum of this algebra, hence \(p\) is an isomorphism. The second projection composed with \(p^{-1}\) is the required morphism. Uniqueness follows from uniqueness of the reduced graph. \(\square\)

**Proposition 6.3.** For \(n\geq1\), every analytic line bundle on \(\mathbf P^n(\mathbf C)\) is \(\mathcal O(d)^{\mathrm{an}}\) for a unique \(d\in\mathbf Z\).

**Proof.** GAGA gives a coherent algebraic module \(L\). It is a line bundle: at a closed point choose one element lifting an analytic fiber basis. Nakayama and faithful flatness make the resulting map \(A\to L_x\) onto; after analytic tensor it is a map between rank-one free modules with nonzero residue, hence an isomorphism. Faithfulness makes its algebraic kernel zero. The locally free locus is open, and its closed complement contains no closed point, so is empty.

A rational nonzero section of \(L\) gives a Cartier divisor. Projective space is locally factorial, since its affine local rings are localizations of polynomial rings. Every prime divisor is the zero set of an irreducible homogeneous polynomial \(f\): its homogeneous prime cone ideal has height one in the factorial ring \(\mathbf C[T_0,\ldots,T_n]\), so is principal. If \(\deg f=e\) and \(H=V(T_0)\), then the rational function \(f/T_0^e\) has divisor \(V(f)-eH\). Summing shows every divisor is linearly equivalent to \(dH\), and hence \(L\cong\mathcal O(d)\). If \(\mathcal O(d)\) were trivial, its global-section dimension would be one. The calculation in our projective-space lesson gives zero for \(d<0\), and \(\binom{d+n}{n}\) for \(d\geq0\), which is one only for \(d=0\). This proves uniqueness. On \(\mathbf P^0\), there is just the trivial line bundle and every twist represents it. \(\square\)

A compact Riemann surface holomorphically embedded in projective space consequently has algebraic image. It is an algebraic smooth projective curve: dimensions and regularity agree at complex points by local comparison. The hypothesis includes an embedding; this conclusion does not assert that an arbitrary compact analytic space is projectively embeddable.

## 7. Exercises with solutions

**Exercise 7.1 (easy).** Show why the cohomological comparison theorem fails for \(\mathbf A^1\).

**Solution.** In degree zero it is the inclusion \(\mathbf C[z]\to\mathcal O(\mathbf C)\). The entire function \(e^z\) is absent from the image, as its derivatives never become zero. Thus even degree-zero surjectivity fails. The projective hypothesis supplies the compactness and twist arguments used above.

**Exercise 7.2 (medium).** Classify analytic line bundles on projective space, explaining the dimension-zero exception.

**Solution.** Essential surjectivity algebraizes the bundle; local faithful flatness descends its rank-one freeness as in Proposition 6.3. A rational section and homogeneous prime-divisor equations make its divisor a multiple of a hyperplane, so it is \(\mathcal O(d)^{\mathrm{an}}\). For \(n\geq1\), the global-section dimension distinguishes the trivial twist and hence makes \(d\) unique. For \(n=0\), every \(\mathcal O(d)\) is the same one-dimensional bundle, so there is no unique integer.

**Exercise 7.3 (medium).** Deduce Chow's theorem for a nonempty analytic hypersurface of \(\mathbf P^n\) directly from its ideal, using GAGA.

**Solution.** An analytic hypersurface in projective space has an invertible coherent ideal: the convergent local rings are factorial, by the exact open proof [Demailly, II, Theorem 2.10, pp. 82–83](https://www-fourier.univ-grenoble-alpes.fr/~demailly/manuscripts/agbook.pdf#page=82), so a reduced pure codimension-one vanishing ideal is locally the product of its prime equations. Algebraize this ideal and its inclusion into the structure sheaf. The ideal descends to an algebraic line bundle by the same local argument as in Proposition 6.3, so is \(\mathcal O(-d)\). Its inclusion is a nonzero section of \(\mathcal O(d)\), hence a homogeneous polynomial of degree \(d\). A nonempty zero set requires \(d>0\). The ideal's analytic extension is the original vanishing ideal; radicality descends by faithful flatness. Thus this polynomial defines exactly the given reduced hypersurface; the ideal formulation handles reducible hypersurfaces as well.

**Exercise 7.4 (medium).** Describe holomorphic maps \(\mathbf P^1(\mathbf C)\to\mathbf P^1(\mathbf C)\).

**Solution.** Theorem 6.2 makes the map algebraic. Its pullback of \(\mathcal O(1)\) is \(\mathcal O(d)\), and the pulled-back coordinate sections generate it, so \(d\geq0\). They are homogeneous degree-\(d\) polynomials \(F_0,F_1\) without a common projective zero. The map is \([T_0:T_1]\mapsto[F_0(T):F_1(T)]\), and in an affine target chart it is their rational quotient. For \(d=0\) it is constant; for \(d>0\) its degree is \(d\).

**Exercise 7.5 (medium).** Compute analytic cohomology of \(\mathcal O(d)\) on \(\mathbf P^1\), and verify comparison explicitly.

**Solution.** Use \(z=T_1/T_0\), with trivializations \(e_0=T_0^d\), \(e_1=T_1^d=z^de_0\). The acyclic two-chart cover gives the degree-one quotient of holomorphic functions on \(\mathbf C^*\) by entire functions in \(z\) and \(z^d\) times entire functions in \(z^{-1}\). In the Laurent expansion the first family removes exponents \(a\geq0\); the second removes exponents \(a\leq d\). The remaining basis is \(z^{d+1},\ldots,z^{-1}\) when \(d\leq-2\), and is empty otherwise. Thus \(h^1=\max(-d-1,0)\). Global sections must have exponents both \(a\geq0\) and \(a\leq d\), giving \(1,z,\ldots,z^d\) for \(d\geq0\) and zero otherwise. Therefore \(h^0=\max(d+1,0)\); higher cohomology vanishes. The algebraic Laurent Čech calculation has the identical bases, and comparison takes each basis monomial to itself.

**Exercise 7.6 (harder).** State and prove the uniqueness of algebraization with a fixed analytic identification. Give a counterexample to uniqueness of the bare isomorphism.

**Solution.** For \(\phi:F^{\mathrm{an}}\to M\) and \(\psi:G^{\mathrm{an}}\to M\), full faithfulness lifts \(\psi^{-1}\phi\) uniquely to \(u:F\to G\). Lifting the inverse and using faithfulness proves \(u\) is an isomorphism. It is the unique one compatible with the identifications. On a nonempty projective variety, multiplication by any \(\lambda\in\mathbf C^*\) is an automorphism of \(\mathcal O_X\); there are many isomorphisms of that bare sheaf to itself. The compatibility condition singles out the correct one.

## 8. Sources and the comparison chain

J.-P. Serre's [*Géométrie algébrique et géométrie analytique*](https://www.numdam.org/item/AIF_1956__6__1_0/), Annales de l'Institut Fourier 6 (1956), 1–42, is the historical source for these three theorems and their applications. The linked edition is free to read; no permission to copy or translate it is asserted. Chow's theorem is credited to W.-L. Chow. Demailly's open analytic proofs are linked in Section 1 and retain his custom OpenContent permission.

Kiran S. Kedlaya's [*GAGA*, updated 30 April 2009](https://ocw.mit.edu/courses/18-726-algebraic-geometry-spring-2009/resources/mit18_726s09_lec22_gaga/), MIT OpenCourseWare 18.726, treats comparison, full faithfulness, algebraization and Chow in Sections 3–5 and 8. Its notes are reusable under [CC BY-NC-SA 4.0](https://ocw.mit.edu/pages/privacy-and-terms-of-use/). They offer useful parallel reading, while this course retains its explicit Laurent contraction, two-stage descending comparison induction and treatment of noninjective hyperplane multiplication.

For a broader framework, Jack Hall's [*GAGA theorems*, arXiv:1804.01976v3, 17 May 2022](https://arxiv.org/abs/1804.01976v3), Theorem A and Examples 9.2–9.3, compares analytic and formal GAGA for proper schemes. Theorem A requires coherence, finite total coherent cohomology, detection at closed points and specified local flatness and residue-field conditions. Its non-Noetherian extensions have further hypotheses. This public author draft is further reading, not a source licensed for adaptation or a replacement for the proofs above.

The corresponding open AI Integrated Stacks Project treatments are [cohomological comparison](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/gaga.html#gaga-section-proof-gaga-cohomology), [full faithfulness](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/gaga.html#gaga-section-proof-gaga-fully-faithful), [analytic global generation](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/gaga.html#gaga-lemma-projective-analytic-global-generation), [essential surjectivity](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/gaga.html#gaga-section-completion-gaga-essential-surjectivity), and [Chow's theorem](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/gaga.html#gaga-theorem-chow-closed-analytic-projective). Their reference texts retain GFDL 1.2 and contain AI-written additions not reviewed by the official Stacks maintainers. Section 1 supplies the analytic finiteness used in their generation argument; Sections 1–2 supply analytic acyclicity, the coherent dimension bound and the structure-sheaf computation directly.

The comparison and algebraicity results are proved above. The chain is local analytic algebra and faithful flatness; analytic Čech cohomology and finiteness; comparison for twists; comparison for all coherent sheaves; internal Hom and full faithfulness; analytic generation and two presentations; coherent-category equivalence; algebraicity of ideals and graphs. This completes the course's passage from sheaf cohomology to GAGA.
