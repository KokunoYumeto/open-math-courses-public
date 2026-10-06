# T-exact functors and adjoints between hearts

A triangulated functor can respect the upper degree bound, the lower degree bound, or both. These conditions determine what its degree-zero functor does to the abelian hearts. Respecting one bound gives one-sided exactness and a cohomology comparison on that half of the category. Respecting both bounds gives every truncation and cohomology comparison. An adjunction exchanges the upper-bound condition on its left adjoint with the lower-bound condition on its right adjoint.

*AI-generated exposition: GPT-6.1 Sol and GPT-6 Astra (OpenAI), Ultra. Edition: 5 October 2026. Independently written lesson text: CC0. Human mathematical sources are credited below.*

Truncation triangles and abelian hearts supplies the proved truncation adjunctions, orthogonal membership tests, abelian heart, and long exact heart-valued cohomology sequence. The bounded-below derived example additionally uses the precise injective-resolution prerequisite identified in its section below. The t-exactness and adjunction arguments themselves are proved here.

## Tensor and Hom test the two bounds

Use the bounded free resolution
\[
 P=[\,\mathbb Z\xrightarrow{2}\mathbb Z\,]
       \quad\text{in degrees }-1,0
 \tag{F1}
\]
of \(\mathbb Z/2\). The adjoint triangulated functors
\(L=P\otimes-\) and \(G=\operatorname{Hom}(P,-)\) preserve quasi-isomorphisms: their total complexes are cones of multiplication by two, with a shift for Hom, and cones of maps between acyclic complexes are acyclic. The chain tensor–Hom unit and counit descend to the derived categories and retain their triangular identities.

For an input with terms in degrees at most zero, \(L\) still has terms at most zero. For an input with terms at least zero, \(G\) still has terms at least zero. Their failures in the other directions are already explicit:
\[
 L(\mathbb Z/2)=(\mathbb Z/2)[1]\oplus(\mathbb Z/2),\qquad
 G(\mathbb Z)=(\mathbb Z/2)[-1].
 \tag{F2}
\]
Tensor kills the differential in (F1), while total Hom places multiplication by two in degrees zero and one. Thus one functor preserves the upper bound and the other the lower bound. On degree-zero modules their degree-zero values are respectively \(A/2A\) and \(A[2]=\{a:2a=0\}\). Here \(A[2]\) denotes the two-torsion subgroup, not a derived shift.

Apply them to \(0\to\mathbb Z\xrightarrow2\mathbb Z\to\mathbb Z/2\to0\). Tensor makes the first nonzero arrow \(0:\mathbb Z/2\to\mathbb Z/2\), losing injectivity; Hom gives \(0\to0\to\mathbb Z/2\), losing surjectivity. These same maps will test the general heart-exactness theorem and its adjunction below. The full exercises retain the resolution and boundedness checks, including an example where a right derived functor is not bounded above.

## Which half of the category is preserved

Let \(\mathcal D_i\) have t-structure \((\mathcal D_i^{\le0},\mathcal D_i^{\ge0})\), heart \(\mathcal A_i\), and cohomology \(H_i^n\), for \(i=1,2\). An **exact functor of triangulated categories** \(F:\mathcal D_1\to\mathcal D_2\) comes with its shift comparison and sends distinguished triangles to distinguished triangles. This use of “exact” concerns triangles; exactness on the abelian hearts will be a separate conclusion. Keep the convention

\[
 \mathcal D_i^{\le n}=\mathcal D_i^{\le0}[-n],
 \qquad
 \mathcal D_i^{\ge n}=\mathcal D_i^{\ge0}[-n].
 \tag{1}
\]

Thus \([1]\) lowers cohomological degree. We call \(F\)

\[
\begin{aligned}
 \text{left t-exact}&\quad\Longleftrightarrow\quad
        F(\mathcal D_1^{\ge0})\subset\mathcal D_2^{\ge0},\\
 \text{right t-exact}&\quad\Longleftrightarrow\quad
        F(\mathcal D_1^{\le0})\subset\mathcal D_2^{\le0},\\
 \text{t-exact}&\quad\Longleftrightarrow\quad
        F\text{ satisfies both conditions}.
\end{aligned}
\tag{2}
\]

The shift comparison transports either inclusion to every integer cut in (1). The induced additive functor of hearts is

\[
 F_{\heartsuit}:\mathcal A_1\longrightarrow\mathcal A_2,
 \qquad A\longmapsto H_2^0(F(A)).
 \tag{3}
\]

This definition makes sense even if \(F\) satisfies neither condition. In that case there is no claimed one-sided exactness.

## The cohomology comparison needs its degree bound

**Theorem.** If \(F\) is left t-exact, there is a natural isomorphism

\[
 F_{\heartsuit}(H_1^0X)\xrightarrow{\ \sim\ }H_2^0(FX)
                \qquad(X\in\mathcal D_1^{\ge0}).
 \tag{4}
\]

If \(F\) is right t-exact, there is a natural isomorphism

\[
 H_2^0(FX)\xrightarrow{\ \sim\ }F_{\heartsuit}(H_1^0X)
                \qquad(X\in\mathcal D_1^{\le0}).
 \tag{5}
\]

**Proof.** For \(X\ge0\), the truncation triangle is
\(H_1^0X\to X\to\tau_1^{\ge1}X\to(H_1^0X)[1]\).
Apply \(F\). Its third object lies in \(\mathcal D_2^{\ge1}\). Both its \(H_2^{-1}\) and \(H_2^0\) vanish, so the long exact sequence gives (4). The map is the actual map induced by \(H_1^0X\to X\). Functoriality of that triangle gives naturality.

For \(X\le0\), apply \(F\) to
\(\tau_1^{\le-1}X\to X\to H_1^0X\to(\tau_1^{\le-1}X)[1]\).
The first object after applying \(F\) lies in \(\mathcal D_2^{\le-1}\). Its \(H_2^0\) and \(H_2^1\) vanish. The middle-to-third map induces (5), again naturally. \(\square\)

Shifting the proof gives (4) in degree \(n\) for \(X\ge n\), and (5) in degree \(n\) for \(X\le n\). It does not give these comparisons on the opposite half. Exercises below exhibit both failures.

The same two-term resolution shows why these hypotheses are necessary. On \(X=\mathbb Z[1]\), outside the lower half, \(H^0G(X)=\mathbb Z/2\) but \(G_\heartsuit(H^0X)=0\). On \(X=(\mathbb Z/2)[-1]\), outside the upper half, \(H^0L(X)=\mathbb Z/2\) but \(L_\heartsuit(H^0X)=0\). These are the exact failures in the complete exercises, using the same \(P,L,G\) as (F1)–(F2).

## One-sided exactness on the heart

**Theorem.** A left t-exact \(F\) induces a left exact \(F_{\heartsuit}\). A right t-exact \(F\) induces a right exact \(F_{\heartsuit}\).

**Proof.** A short exact sequence in \(\mathcal A_1\),
\(0\to A\to B\to C\to0\), determines a distinguished triangle
\(A\to B\to C\to A[1]\). If \(F\) is left t-exact, \(FA,FB,FC\ge0\), and the long exact sequence contains

\[
 0=H_2^{-1}(FC)\longrightarrow F_{\heartsuit}A
       \longrightarrow F_{\heartsuit}B
       \longrightarrow F_{\heartsuit}C.
 \tag{6}
\]

It is exact at the first two heart objects. This is left exactness. If \(F\) is right t-exact, \(FA,FB,FC\le0\), and the sequence instead contains

\[
 F_{\heartsuit}A\longrightarrow F_{\heartsuit}B
       \longrightarrow F_{\heartsuit}C
       \longrightarrow H_2^1(FA)=0.
 \tag{7}
\]

This is right exactness. Additivity follows from that of \(F\) and \(H_2^0\). \(\square\)

The two missing end terms measure the possible failure of the other exactness condition. Their vanishing cannot be deduced from a single inclusion in (2).

For the sequence tested in the opening, (6) identifies the missing Hom surjection with the degree-one extension term, and (7) identifies the missing tensor injection with negative-degree Tor. Both failures persist even when the two functors are adjoints. Requiring both halves is the additional condition used in the next theorem.

## Full t-exactness transports the actual truncation triangles

**Theorem.** If \(F\) is t-exact, \(F(\mathcal A_1)\subset\mathcal A_2\), its restriction to the heart is exact, and there are natural comparisons

\[
\begin{aligned}
 F(\tau_1^{\le n}X)&\simeq\tau_2^{\le n}(FX),\\
 F(\tau_1^{\ge n}X)&\simeq\tau_2^{\ge n}(FX),\\
 F(H_1^nX)&\simeq H_2^n(FX)
                \qquad(n\in\mathbb Z,\ X\in\mathcal D_1).
\end{aligned}
\tag{8}
\]

They respect the truncation maps, connecting arrows, and the long exact cohomology sequences.

**Proof.** An object in both halves has image in both halves, so \(F(A)\) is a heart object and canonically equals \(F_{\heartsuit}(A)\). Combining (6) and (7) proves that this heart restriction is exact.

Apply \(F\) to the actual triangle at cut \(n\):
\(\tau_1^{\le n}X\to X\to\tau_1^{\ge n+1}X\to(\tau_1^{\le n}X)[1]\).
Its first object lies in \(\mathcal D_2^{\le n}\), and its third lies in \(\mathcal D_2^{\ge n+1}\). It is therefore a truncation triangle for \(FX\). The proved uniqueness of truncation triangles gives its unique isomorphism with the chosen one for \(FX\), with the identity on the middle object. Uniqueness makes these isomorphisms natural in \(X\) and retains all three arrows. This proves the first two lines of (8).

Use the interval description \(H_1^nX=(\tau_1^{[n,n]}X)[n]\). Applying the two truncation comparisons and the shift comparison gives the last line of (8). The heart cohomology sequence was constructed from successive truncation triangles and their maps. The comparisons just obtained identify these constructions before taking heart kernels or cokernels. The exact heart restriction preserves those kernels and cokernels, so it identifies the connecting maps as well as the objects. \(\square\)

For the standard t-structure of an abelian category \(\mathcal B\), these abstract truncations are the usual smart truncations:

\[
 (\tau^{\le n}K)^j=
 \begin{cases}K^j&j<n,\\ \ker(d^n)&j=n,\\0&j>n,\end{cases}
 \quad
 (\tau^{\ge n}K)^j=
 \begin{cases}0&j<n,\\ \operatorname{coker}(d^{n-1})&j=n,\\K^j&j>n.\end{cases}
 \tag{9}
\]

Indeed these complexes and their maps give the truncation triangle already proved in the preceding lesson. Uniqueness identifies their images in \(D(\mathcal B)\) with the abstract adjoint truncations. The degree convention in (8) consequently agrees with ordinary complex cohomology.

## Why a bounded-below right derived functor is left t-exact

Let \(\mathcal B_1,\mathcal B_2\) be abelian categories, assume \(\mathcal B_1\) has enough injectives, and let \(\Phi:\mathcal B_1\to\mathcal B_2\) be additive and left exact. Use the standard t-structures. The required derived-category prerequisite is:

*A complex with zero terms below \(a\) admits a quasi-isomorphism to a complex \(I\) of injectives with \(I^j=0\) below \(a\). A bounded-below injective complex is K-injective, and applying an additive functor to it computes the right derived functor on \(D^+\).*

The exact internal provider is Injective modules, flasque sheaves and bounded-below derived functors, Theorem 4.1(1)–(3), together with Lemma 3.2 and Theorem 3.3. Theorem 4.1 is stated for arbitrary abelian categories with enough injectives and any additive functor: its pushout construction preserves the specified lower term bound, its K-injective comparison computes all derived maps, and its cone argument constructs the triangulated functor on \(D^+\). Left exactness identifies \(R^0\Phi=\Phi\). Theorem 2.3 separately proves enough injectives for sheaves of associative unital rings, including modules on a point. Thus the provider supplies every clause of the italicized interface, with no commutativity restriction on its underlying ring and no uniform upper-bound claim. The component retains the Stacks project authors' GFDL-1.2-or-later text, the earlier GPT-6 Astra proof contributions and the GPT-6.1 Sol edits; its licence and source notices remain separate from this CC0 lesson.

**Theorem.** The exact triangulated functor

\[
 R\Phi:D^+(\mathcal B_1)\longrightarrow D^+(\mathcal B_2)
 \tag{10}
\]

is left t-exact. Its heart functor is naturally \(\Phi\).

**Proof.** If \(X\ge0\), choose a bounded-below representative \(K\) and replace it by its smart truncation \(\tau^{\ge0}K\). Since the negative cohomology of \(K\) vanishes, this replacement is quasi-isomorphic to \(K\), and its terms are zero below zero. The prerequisite supplies \(K'\to I\) with \(I^j=0\) for \(j<0\). Thus \(R\Phi(X)\) is represented by \(\Phi(I)\), whose terms below zero are also zero: an additive functor sends the zero object to a zero object. This proves left t-exactness.

For \(A\in\mathcal B_1\), use \(0\to A\to I^0\to I^1\to\cdots\). Left exactness of \(\Phi\) identifies \(\Phi(A)\) with the kernel of \(\Phi(I^0)\to\Phi(I^1)\), which is \(H^0(\Phi(I))\). This identification respects maps of resolutions and hence gives the natural heart isomorphism. \(\square\)

The lower-bound argument works for every additive \(\Phi\) for which (10) is constructed by that prerequisite. Left exactness is what identifies its degree-zero functor with the original \(\Phi\). In the stated left exact case, (4) becomes

\[
 H^0(R\Phi X)\simeq\Phi(H^0X)\qquad(X\ge0).
 \tag{11}
\]

The domain and codomain in (10) are \(D^+\). Enough injectives does not give a uniform upper bound on \(R\Phi(A)\), even when \(A\) is concentrated in degree zero. Exercise 6 computes an explicit failure to remain in \(D^b\).

## Adjoint functors exchange the two one-sided conditions

Let \(f:\mathcal D_1\to\mathcal D_2\) and \(g:\mathcal D_2\to\mathcal D_1\) be exact triangulated functors with \(f\dashv g\).

**Theorem.**

\[
 f\text{ is right t-exact}
       \quad\Longleftrightarrow\quad
 g\text{ is left t-exact}.
 \tag{12}
\]

**Proof.** Suppose \(f\) is right t-exact. For \(Y\in\mathcal D_2^{\ge0}\) and \(U\in\mathcal D_1^{\le-1}\), the shift comparison gives \(fU\le-1\), so
\(\operatorname{Hom}_{\mathcal D_1}(U,gY)
\simeq\operatorname{Hom}_{\mathcal D_2}(fU,Y)=0\).
The right orthogonal description of \(\mathcal D_1^{\ge0}\) proves \(gY\ge0\).

Conversely, if \(g\) is left t-exact, then for \(X\in\mathcal D_1^{\le0}\) and \(V\in\mathcal D_2^{\ge1}\), one has \(gV\ge1\). Adjunction gives
\(\operatorname{Hom}_{\mathcal D_2}(fX,V)
\simeq\operatorname{Hom}_{\mathcal D_1}(X,gV)=0\).
The left orthogonal description of \(\mathcal D_2^{\le0}\) proves \(fX\le0\). \(\square\)

Neither direction asserts the other half of t-exactness for either functor. For example, the adjoint shifts \([1]\dashv[-1]\) satisfy exactly the two conditions in (12) for a nonzero standard heart.

## Restricting an ambient adjunction requires membership

Suppose instead that the adjunction lives in larger triangulated categories:
\(f:\widetilde{\mathcal D}_1\rightleftarrows\widetilde{\mathcal D}_2:g\).
Let \(\mathcal D_i\) be full triangulated subcategories equipped with their own t-structures.

**Theorem.** There are two precise restricted assertions:

\[
\begin{aligned}
 &f(\mathcal D_1)\subset\mathcal D_2,\quad
     f|_{\mathcal D_1}\text{ right t-exact},\\
 &Y\in\mathcal D_2^{\ge0},\quad gY\in\mathcal D_1
                 \quad\Longrightarrow\quad gY\in\mathcal D_1^{\ge0};
 \tag{13}\\[2pt]
 &g(\mathcal D_2)\subset\mathcal D_1,\quad
     g|_{\mathcal D_2}\text{ left t-exact},\\
 &X\in\mathcal D_1^{\le0},\quad fX\in\mathcal D_2
                 \quad\Longrightarrow\quad fX\in\mathcal D_2^{\le0}.
\end{aligned}
\]

**Proof.** In the first case, test \(gY\) against every \(U\in\mathcal D_1^{\le-1}\). Fullness identifies these Hom groups with their ambient Hom groups. Adjunction identifies them with \(\operatorname{Hom}(fU,Y)\), which vanishes by the t-structure on \(\mathcal D_2\). The hypothesis \(gY\in\mathcal D_1\) permits the orthogonal membership test inside \(\mathcal D_1\), proving the first conclusion.

In the second case, test \(fX\) against every \(V\in\mathcal D_2^{\ge1}\). Fullness and adjunction identify the test with \(\operatorname{Hom}(X,gV)=0\). Now \(fX\in\mathcal D_2\) permits the left orthogonal membership test there. \(\square\)

Orthogonality against objects of a full subcategory does not force an ambient object into that subcategory. The explicit membership clauses in (13) have that separate job.

## The induced adjunction on hearts

**Theorem.** Under the conditions of (12), the two heart functors satisfy \(f_{\heartsuit}\dashv g_{\heartsuit}\). The first is right exact and the second left exact.

**Proof.** For \(A\in\mathcal A_1\), \(B\in\mathcal A_2\), right t-exactness gives \(fA\le0\) and left t-exactness gives \(gB\ge0\). Truncation adjunctions at zero then give

\[
\begin{aligned}
 \operatorname{Hom}_{\mathcal A_2}(f_{\heartsuit}A,B)
 &\simeq\operatorname{Hom}_{\mathcal D_2}(fA,B)\\
 &\simeq\operatorname{Hom}_{\mathcal D_1}(A,gB)\\
 &\simeq\operatorname{Hom}_{\mathcal A_1}(A,g_{\heartsuit}B).
\end{aligned}
\tag{14}
\]

For clarity, the first isomorphism follows by applying \(\operatorname{Hom}(-,B)\) to \(\tau^{\le-1}fA\to fA\to H^0fA\); both the Hom terms from \(\tau^{\le-1}fA\) and its shift \([1]\) vanish. The last follows by applying \(\operatorname{Hom}(A,-)\) to \(H^0gB\to gB\to\tau^{\ge1}gB\); both Hom terms to \(\tau^{\ge1}gB\) and its shift \([-1]\) vanish. The isomorphisms are natural, so they define an adjunction. Equations (6)–(7) give its stated exactness properties. \(\square\)

## Detecting equivalences without bounding every object

**Theorem.** Suppose \(F:\mathcal D_1\to\mathcal D_2\) is t-exact, the t-structure on \(\mathcal D_1\) is nondegenerate, and \(F_{\heartsuit}\) reflects isomorphisms. Then \(F\) reflects isomorphisms on all of \(\mathcal D_1\). The target t-structure need not be nondegenerate.

**Proof.** Let \(u:X\to Y\) have invertible \(Fu\). The natural comparisons (8) identify \(F_{\heartsuit}(H_1^n u)\) with \(H_2^n(Fu)\), which is an isomorphism for every integer \(n\). Reflection on the heart makes every \(H_1^n u\) an isomorphism. The nondegenerate detection theorem in the preceding lesson then makes \(u\) an isomorphism. The reverse implication holds for every functor. \(\square\)

Only the source needs nondegeneracy: it is where the cohomology test is used to recover the original morphism. For instance, an exact conservative functor between abelian categories, applied term by term to unbounded complexes, descends to a t-exact conservative functor of their derived categories. It descends because exactness preserves kernels, images and cokernels and hence cohomology and quasi-isomorphisms; its heart restriction is the original functor. The standard source t-structure is nondegenerate by the preceding lesson. Bounded-interval detection without a global nondegeneracy hypothesis is proved separately in Exercise 8.

## Eight exercises with complete solutions

### Shifts distinguish left and right

*Difficulty: Introductory.*

For the standard t-structure on \(D^b(k)\), with \(k\) a field, determine the one-sided t-exactness of \([1]\) and \([-1]\). Compute their heart functors and verify (12) and (14).

**Solution.** \(H^j(X[1])=H^{j+1}(X)\), so \([1]\) preserves the upper bound zero. It fails to preserve the lower bound: \(k[1]\) has nonzero cohomology in degree \(-1\). Thus \([1]\) is right t-exact but not left t-exact. The shift \([-1]\) preserves the lower bound and fails the upper bound, since \(k[-1]\) has degree \(1\). On a degree-zero vector space, both shifted objects have zero \(H^0\), so both heart functors are zero. The shifts are inverse equivalences and \([1]\dashv[-1]\). Their heart adjunction is the zero-to-zero adjunction: both Hom spaces in (14) are the zero vector space. A heart adjunction can consequently lose information retained by its ambient adjunction.

### A left t-exact functor can see a negative input

*Difficulty: Intermediate.*

Set \(G=R\operatorname{Hom}_{\mathbb Z}(\mathbb Z/2,-)\) on \(D^b(\mathbb Z)\). Prove that \(G\) is left t-exact, compute \(G(\mathbb Z)\), and test (11) on \(X=\mathbb Z[1]\). Show that \(G_{\heartsuit}\) fails right exactness.

**Solution.** The free resolution \(P=(\mathbb Z\xrightarrow{2}\mathbb Z)\), in degrees \(-1,0\), gives
\(\operatorname{Hom}(P,Y)\) as the derived Hom complex. It computes the derived functor because \(P\) is bounded free: Hom from each term preserves exact complexes, and its two-term total Hom is a shifted cone, which also preserves acyclicity. For a smart representative \(Y\) with zero terms below zero, this total Hom has zero terms below zero. Hence \(G\) is left t-exact.

For \(Y=\mathbb Z\), the resulting complex is isomorphic to \(\mathbb Z\xrightarrow{2}\mathbb Z\) in degrees \(0,1\) (change the sign of one term if the total Hom differential is \(-2\)). Its only cohomology is \(\mathbb Z/2\) in degree \(1\); thus \(G(\mathbb Z)\simeq(\mathbb Z/2)[-1]\). Shifting gives \(H^0G(\mathbb Z[1])=\mathbb Z/2\), whereas \(\operatorname{Hom}(\mathbb Z/2,H^0(\mathbb Z[1]))=0\). The input is outside \(D^{\ge0}\), exactly the bound needed in (11). On the heart, \(G_{\heartsuit}=\operatorname{Hom}(\mathbb Z/2,-)\). The epimorphism \(\mathbb Z\to\mathbb Z/2\) maps to \(0\to\mathbb Z/2\), which is not an epimorphism. Left t-exactness has not supplied right exactness.

### A right t-exact functor can see a positive input

*Difficulty: Intermediate.*

Set \(L=(\mathbb Z/2)\otimes_{\mathbb Z}^L-\) on \(D^b(\mathbb Z)\). Verify right t-exactness and compute \(L(\mathbb Z/2)\). Test (5) on \(X=(\mathbb Z/2)[-1]\), and show that \(L_{\heartsuit}\) fails left exactness.

**Solution.** The same free resolution \(P\) computes \(L(Y)=P\otimes Y\). Tensoring its two terms gives the cone of multiplication by \(2\) on \(Y\), so it preserves acyclic complexes and computes the derived tensor. If a smart representative \(Y\) has zero terms above zero, the total tensor also has zero terms above zero. Thus \(L\) is right t-exact.

Tensor \(P\) with \(\mathbb Z/2\). Its differential becomes zero, so \(L(\mathbb Z/2)\) has one \(\mathbb Z/2\) in degree \(-1\) and one in degree \(0\). After shifting by \([-1]\), these degrees are \(0,1\). Hence \(H^0(LX)=\mathbb Z/2\), whereas \(L_{\heartsuit}(H^0X)=(\mathbb Z/2)\otimes0=0\). The positive input is outside the upper-bound hypothesis in (5). Finally, the heart monomorphism \(2:\mathbb Z\to\mathbb Z\) becomes the zero map \(\mathbb Z/2\to\mathbb Z/2\), which is not monic.

### Scalar extension commutes with every truncation

*Difficulty: Intermediate.*

Let \(k\subset K\) be fields. Show that extension of scalars \(E=K\otimes_k-\) and restriction of scalars \(U\) on their bounded derived categories are t-exact adjoints. Identify the comparisons (8).

**Solution.** Every short exact sequence of vector spaces splits. Tensoring a splitting with \(K\) preserves the sequence, so \(E\) is exact on vector spaces; \(U\) preserves the underlying kernels and cokernels and is also exact. Both therefore commute with complex cohomology. They descend to the derived categories and preserve both cohomological bounds, proving t-exactness. The usual tensor–restriction adjunction on complexes, with its natural unit and counit, respects homotopies and descends through quasi-isomorphisms, retaining the two triangular identities. Thus \(E\dashv U\) on the derived categories.

Since the two functors preserve kernels and cokernels, applying either to the explicit complexes in (9) gives the corresponding smart truncations. Their comparisons in (8) are these actual degreewise maps. In particular \(H^n(EX)\simeq K\otimes_kH^nX\), naturally, including the connecting arrows of every triangle sequence. No finite extension-degree hypothesis is needed.

### Derived tensor–Hom induces an adjunction with unequal exactness

*Difficulty: Advanced.*

For \(L,G\) in Exercises 2–3, establish the derived adjunction \(L\dashv G\) and compute its heart adjunction. Does either heart functor become exact because the two are adjoints?

**Solution.** Use the bounded free complex \(P\). The total-complex tensor–Hom adjunction
\(\operatorname{Hom}(P\otimes X,Y)\simeq\operatorname{Hom}(X,\operatorname{Hom}(P,Y))\)
has the usual degree signs. It gives unit and counit maps on complexes satisfying the triangular identities. Both functors preserve quasi-isomorphisms by the cone computations in Exercises 2–3. Consequently the unit and counit descend to \(D^b(\mathbb Z)\), still satisfy those identities, and give \(L\dashv G\). Boundedness is preserved because \(P\) has only two nonzero terms.

On a heart object \(A\), the degree-zero tensor cohomology is \(A/2A\), and the degree-zero Hom cohomology is \(A[2]=\{a:2a=0\}\). Formula (14) is thus

\[
 \operatorname{Hom}_{\mathbb Z}(A/2A,B)
       \simeq\operatorname{Hom}_{\mathbb Z}(A,B[2]).
 \tag{15}
\]

Indeed a map from \(A/2A\) into \(B\) has image killed by \(2\), and a map from \(A\) into \(B[2]\) vanishes on \(2A\). These inverse factorizations are natural. The failures on \(2:\mathbb Z\to\mathbb Z\) and \(\mathbb Z\to\mathbb Z/2\) in the earlier exercises still apply. Adjunction gives right exactness for the left heart functor and left exactness for the right one, without making either exact.

### A right derived functor need not preserve boundedness

*Difficulty: Advanced.*

Let \(R=\mathbb Z/4\), \(M=R/(2)\), and \(\Phi=\operatorname{Hom}_R(M,-)\). Compute every \(\operatorname{Ext}_R^j(M,M)\) and show that \(R\Phi(M)\) lies in \(D^+\) but not \(D^b\). The category of \(R\)-modules has enough injectives; this is also the point-space case of the programme's sheaf-module enough-injective theorem.

**Solution.** There is a projective resolution

\[
 \cdots\xrightarrow{2}R\xrightarrow{2}R
       \xrightarrow{2}R\longrightarrow M\longrightarrow0.
 \tag{16}
\]

Successive differentials compose to multiplication by \(4\), which is zero in \(R\). At every \(R\) the kernel and image of multiplication by \(2\) are both \((2)\); the augmentation has that same kernel. Thus (16) is exact. Applying \(\operatorname{Hom}_R(-,M)\) gives \(M\) in each degree \(j\ge0\), with every differential zero because \(2M=0\). Therefore \(\operatorname{Ext}_R^j(M,M)=M\) for every \(j\ge0\).

For completeness this projective-resolution calculation agrees with the injective definition: for an injective resolution \(M\to I\), use the first-quadrant double complex \(\operatorname{Hom}_R(P^{-p},I^q)\), \(p,q\ge0\). Each diagonal has finitely many terms. Taking vertical cohomology leaves \(\operatorname{Hom}_R(P^{-p},M)\), since \(P^{-p}\) is free; taking horizontal cohomology leaves \(\operatorname{Hom}_R(M,I^q)\), since \(I^q\) is injective and the augmented resolution is exact. The two filtrations of each finite diagonal consequently compute the same total cohomology, giving the claimed Ext groups. They are nonzero in arbitrarily high degrees. Left t-exactness is respected, but no bounded-above target is possible.

### Orthogonal tests cannot create subcategory membership

*Difficulty: Advanced.*

Set \(\widetilde{\mathcal D}_1=\widetilde{\mathcal D}_2=D^b(k)\times D^b(k)\), and take \(f=g=\mathrm{id}\). Let \(\mathcal D_1=D^b(k)\times\{0\}\) have its standard t-structure. Let \(\mathcal D_2\) be the whole product, with the standard t-structure on the first factor and the second factor shifted so that its heart is \(k\)-vector spaces in degree \(-1\). Check the first hypotheses of (13). What happens to \(Y=(0,k[1])\)?

**Solution.** On the second factor the new cuts at zero are \(D^{\le-1}_{\mathrm{std}}\) and \(D^{\ge-1}_{\mathrm{std}}\); they are a shifted t-structure and their intersection has degree \(-1\). On the first factor the cuts remain standard. The inclusion \(f(\mathcal D_1)\subset\mathcal D_2\) holds, and \((X,0)\) with \(X\le0\) satisfies the product upper cut. Hence \(f|_{\mathcal D_1}\) is right t-exact.

The object \(Y=(0,k[1])\) is in the heart of \(\mathcal D_2\), and thus in its positive half. Every Hom from \((U,0)\) to \(gY\) vanishes, even without a degree condition on \(U\). Nevertheless \(gY=Y\) is outside \(\mathcal D_1\). It therefore cannot be asserted to belong to \(\mathcal D_1^{\ge0}\). The missing membership hypothesis is exactly what fails; an orthogonal test inside the first factor is unable to detect any second-factor object.

### Conservativity on a bounded t-structure and its limitation

*Difficulty: Advanced.*

Suppose \(F\) is t-exact and its heart restriction reflects isomorphisms. Prove that \(F\) reflects isomorphisms between objects lying in finite t-structure intervals. Explain why the boundedness assumption matters.

**Solution.** If \(Z\) lies in an interval \([a,b]\) and \(FZ=0\), then (8) gives \(F_{\heartsuit}(H_1^nZ)=0\) for every \(n\). Apply reflection of isomorphisms to \(0\to H_1^nZ\): its image is the isomorphism \(0\to0\), so \(H_1^nZ=0\). Finite successive truncation triangles then give \(Z=0\).

For a map \(u:X\to Y\) between finite-interval objects, its cone \(C\) also lies in a finite interval: choose common bounds \([a,b]\); the triangle \(Y\to C\to X[1]\to Y[1]\) and extension closure place \(C\) in \([a-1,b]\). If \(Fu\) is invertible, its cone \(FC\) vanishes. The preceding argument gives \(C=0\), so \(u\) is invertible.

Without boundedness or a suitable nondegeneracy assumption, cohomology can miss an object. In a nonzero triangulated category take the degenerate t-structure \((\mathcal D,\{0\})\), whose heart and all cohomology functors are zero. The zero endofunctor is t-exact and its restriction to the zero heart reflects isomorphisms. It does not reflect isomorphisms in \(\mathcal D\). The finite interval subcategory here contains only zero, so this example does not contradict the proved assertion.

## Sources and further prerequisites

A. A. Beilinson, J. Bernstein and P. Deligne, [*Faisceaux pervers*](https://publications.ias.edu/sites/default/files/Faisceaux%20pervers.pdf), Astérisque 100 (1982), supplies the freely accessible treatment of t-exact functors, one-sided heart exactness and adjunctions. The preceding lesson proves the abstract truncation and heart results used here; the arguments above prove the functor comparisons, the explicit ambient-membership variant and the nondegenerate conservativity statement in full.

The bounded-below injective construction/computation is supplied by the exact internal provider linked in its section, with the inherited Stacks GFDL terms and visible AI contribution notices. These references retain their own licences. The perverse support/costalk construction supplies the geometric existence argument for perverse truncations; the formal statements proved here apply after that construction.
