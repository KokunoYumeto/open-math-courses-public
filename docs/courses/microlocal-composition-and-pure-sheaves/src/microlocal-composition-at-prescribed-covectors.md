# Microlocal composition at prescribed covectors

Ordinary convolution integrates across an entire intermediate manifold. A kernel germ at one pair of covectors does not retain all that information. To compose two germs, we must isolate the intermediate covector that contributes to the chosen output. This lesson constructs that composition, explains why a formal system of convolutions is represented by a bounded sheaf germ, and proves its basic compatibilities.

Use the ordinary kernel and localized-category prerequisites from the preceding lessons. In particular, the refined incoming cutoff and the isolated-incidence direct-image theorem are inputs from the microlocal-category theory. We state exactly what is used. Coefficients are arbitrary modules over a commutative ring \(k\) of finite global dimension; all sheaf complexes are bounded. Manifolds are finite dimensional, real, Hausdorff and second countable. No constructibility or global properness is assumed.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

## Which middle covector is being composed

Fix \(p_X=(x_0;\xi_0)\), \(p_Y=(y_0;\eta_0)\), and \(p_Z=(z_0;\zeta_0)\). Zero covectors are allowed. Let \(K_1\) be a germ on \(X\times Y\) at \((p_X,p_Y^a)\), and \(K_2\) a germ on \(Y\times Z\) at \((p_Y,p_Z^a)\). A superscript \(a\) reverses the covector and leaves its base point fixed.

For chosen representatives form the twisted matching set

\[
\begin{split}
\mathcal T(K_1,K_2)=\{(u,v,w):
 &(u,v^a)\in\operatorname{SS}(K_1),\\
 &(v,w^a)\in\operatorname{SS}(K_2)\},
\qquad \rho(u,v,w)=(u,w^a).
\end{split}
\tag{1}
\]

The opposite physical middle covectors are \(-\eta\) in \(K_1\) and \(+\eta\) in \(K_2\). Their sum is zero in the ordinary tensor kernel. We call the pair **microlocally composable** if

\[
\mathcal T(K_1,K_2)\cap
(\{p_X\}\times T^*Y\times\{p_Z\})
\subset\{(p_X,p_Y,p_Z)\}
\quad\text{near }(p_X,p_Y,p_Z).
\tag{2}
\]

The allowed singleton need not occur. Condition (2) is local around the specified middle covector. It does not exclude a different witness far away in that fibre. The germ of microsupport is invariant under an isomorphism in each point-localized category, so (2) depends only on the two kernel germs.

Ordinary convolution is
\(K_1\circ K_2=Rq_{13!}(q_{12}^{-1}K_1\otimes^Lq_{23}^{-1}K_2)\).
For germs we first form the formal system

\[
P=\text{“}\!\lim_{K_1',K_2'}\!\text{”}\;K_1'\circ K_2',
\tag{3}
\]

where \(K_i'\to K_i\) runs over incoming denominators at the appropriate physical pair. A denominator means its cone misses that pair. The notation in (3) means a pro-object: it specifies filtered colimits of morphisms out of the terms into each test object. It is not an inverse limit of sheaves, and it makes no assertion that one fixed ordinary convolution computes the answer.

## Replacing a kernel to control the whole middle fibre

At the fixed base points, two additional conditions are useful:

\[
\mathcal T\cap
(\{p_X\}\times T_{y_0}^*Y\times\{p_Z\})
\subset\{(p_X,p_Y,p_Z)\},
\tag{4}
\]

\[
\mathcal T\cap
(\{(x_0;0)\}\times \dot T_{y_0}^*Y\times\{(z_0;0)\})
=\varnothing.
\tag{5}
\]

The dot removes the zero covector. Condition (4) controls every covector in the middle fibre at \(y_0\), not just those near \(\eta_0\). Condition (5) rules out nonzero middle cancellation when both endpoint covectors vanish.

Here is the cutoff consequence we need. If \(\xi_0\ne0\), a microlocally composable pair admits an incoming replacement \(K_1'\to K_1\), invertible at \((p_X,p_Y^a)\), for which (4) holds and

\[
\operatorname{SS}(K_1')\cap
(\{(x_0;0)\}\times\dot T_{y_0}^*Y)=\varnothing.
\tag{6}
\]

The same construction works with any specified closed conic set in place of \(\operatorname{SS}(K_2)\). It also works simultaneously with a finite union of such sets. This last clause will allow common refinements of two denominators.

**Proof of the cutoff consequence.** Work in the cotangent fibre at \((x_0,y_0)\), and write \(q=(\xi_0,-\eta_0)\). Local isolation gives a compact neighborhood \(L\) of \(\eta_0\) such that matching the two original microsupports at the fixed endpoints \(p_X,p_Z\), for \(\eta\in L\), occurs only at \(\eta_0\). Choose two proper closed convex cones \(C_-\) and \(C_+\) around \(q\), with \(q\in\operatorname{Int}C_-\), \(C_-\setminus0\subset\operatorname{Int}C_+\), and with the fixed-first-component slice of \(C_+\) contained in \(\{\xi_0\}\times(-L)\). They can also be chosen to contain no nonzero vector with first component zero. Indeed, because \(\xi_0\ne0\), choose a linear functional \(\ell\) of the first component with \(\ell(\xi_0)=1\), take two sufficiently small nested closed convex balls around \(q\) in the hyperplane \(\ell(\xi)=1\), and take their positive cones. Their normalized sections and their fixed-first-component slices are compact.

Choose an open conic neighborhood \(U\) of \(q\) contained in \(\operatorname{Int}C_-\). The refined incoming replacement will be an isomorphism throughout \(U\). On a compact normalized section, \(C_-\cap\operatorname{SS}(K_1)\) is disjoint from the set of second-kernel matching directions with fixed first component \(\xi_0\) that lie in \(C_+\) but outside \(U\): an intersection would be an original matching covector in \(L\), hence would equal \(q\), which is in \(U\). Both sets are closed on that compact section. Their separation therefore gives a conic neighborhood \(W\) of \((C_-\cap\operatorname{SS}(K_1))\setminus0\), contained in \(\operatorname{Int}C_+\), whose fixed-first-component slice contains no second-kernel matching covector outside \(U\).

Apply the refined incoming replacement theorem with the closed cone \(C_-\), the inner isomorphism cone \(U\), and the directional neighborhood \(W\). It gives \(K_1'\to K_1\) invertible throughout \(U\), with microsupport at the base point contained in \(W\cup\{0\}\). A matching covector inside \(U\) belongs to the original microsupport, because the replacement is an isomorphism there, and so it is the chosen covector. A matching covector outside \(U\) is excluded by the choice of \(W\). This proves (4). The containment in \(C_+\cup\{0\}\) excludes every nonzero covector with first component zero and proves (6). For any prescribed closed conic matching set the same argument applies under the stated local isolation; for finitely many such sets choose \(L\) for all of them and separate their finite closed union outside \(U\). Inside \(U\), agreement with the original microsupport preserves each isolation condition. The construction uses the refined replacement theorem at its stated arbitrary bounded coefficient scope. \(\square\)

If \(\zeta_0\ne0\), apply the argument to \(K_2\) after interchanging the endpoint roles. In either case (6), or its endpoint analogue, supplies (5).

There are two remaining cases. If both endpoint covectors are zero but \(\eta_0\ne0\), positive scaling preserves their zeros. If both kernel microsupports contained the specified pairs, scaling \(\eta_0\) by numbers tending to one would contradict (2). Thus one germ is zero and can be replaced by the zero kernel. If all three covectors are zero, (2) isolates the intersection of the two supports in the middle base variable. At the fixed bases, any nonzero matching middle covector could be scaled down towards zero, again contradicting (2). This proves (4) and (5) in the last case as well.

Consequently every composable pair admits incoming representatives satisfying (4) and (5), including the cases involving zero covectors.

## Why the formal composition is a bounded germ

**Theorem.** For a microlocally composable pair, the pro-object (3) is represented by an object of \(D^b(k_{X\times Z};(p_X,p_Z^a))\). Denote it by \(K_1\circ_\mu K_2\). For every neighborhood \(W\) of the specified triple,

\[
\operatorname{SS}(K_1\circ_\mu K_2)
\subset\rho\bigl(W\cap\mathcal T(K_1,K_2)\bigr)
\quad\text{near }(p_X,p_Z^a).
\tag{7}
\]

If the representatives already satisfy (4) and (5), there is a canonical formal identification

\[
K_1\circ_\mu K_2
\simeq\text{“}\!\lim_{V\ni y_0}\!\text{”}\;(K_1)_{X\times V}\circ K_2.
\tag{8}
\]

If \(\xi_0\ne0\), one may instead hold \(K_2\) fixed and vary only \(K_1'\to K_1\) in (3).

**Proof.** First (2), (4) and (5) imply isolated matching over the fixed endpoint covectors on a neighborhood of the middle *base point*, with no bound imposed on the middle covector. If this were false, choose offending \((y_j;\eta_j)\), with \(y_j\to y_0\), matching those endpoints. If \(\eta_j\) is bounded, closedness and (4) force a subsequence to converge to \(p_Y\); then (2) excludes it. If \(|\eta_j|\to\infty\), divide both physical kernel covectors by \(|\eta_j|\). A subsequence of unit middle covectors converges to a nonzero vector at \(y_0\), while the endpoint covectors tend to zero. Conicity and closedness give the forbidden pair in (5). This proves the asserted base-neighborhood isolation.

Put
\(H=q_{12}^{-1}K_1\otimes^Lq_{23}^{-1}K_2\)
on \(X\times Y\times Z\). Condition (5) is exactly the noncharacteristic tensor condition at the fixed base point: possible cancellation has components \((0,-\eta,0)+(0,\eta,0)\). It persists on a smaller base neighborhood. Indeed a sequence of nonzero cancellations at convergent base points, normalized to unit length, would yield a prohibited limiting cancellation at the fixed bases. The ordinary tensor estimate therefore gives

\[
\operatorname{SS}(H)\subset
(\operatorname{SS}(K_1)\times T_Z^*Z)
+(T_X^*X\times\operatorname{SS}(K_2))
\tag{9}
\]

there. A covector on the right of (9) whose middle component vanishes comes from a matching triple (1). By the preceding isolation, the incidence for \(q_{13}\) over \((p_X,p_Z^a)\) is confined to
\((x_0,y_0,z_0;\xi_0,0,-\zeta_0)\).

Apply the isolated-incidence direct-image prerequisite to \(H\). In its exact form it represents the formal proper-support image by a bounded germ, identifies it with the formal ordinary image, and allows its microsupport witnesses to be confined to any prescribed neighborhood of that incidence point. Its direct-germ formula and boundary-control construction give (8). Restricting the open middle neighborhoods alone is legitimate *after this direct-image argument*; they have not been declared cofinal among all microlocal denominators beforehand. Combining the confined witnesses with (9) proves (7). A proper replacement has a closed image for the retained witnesses, so no uncontrolled witness at infinity has been added to the estimate.

It remains to identify this represented image with the system (3), rather than just one choice of representatives. Consider denominators \(K_1'\to K_1\) and \(K_2'\to K_2\). When \(\xi_0\ne0\), make a further incoming replacement of \(K_1'\) using the union of the matching sets of \(K_2'\) and \(K_2\). It satisfies (4) and (5) for both. Near the specified physical pair the cone of \(K_2'\to K_2\) has no microsupport. The noncharacteristic tensor estimate now shows that the induced tensor comparison has cone invisible at the specified incidence point. The same isolated-incidence direct-image theorem makes its image comparison invertible at \((p_X,p_Z^a)\). Refining the first denominator is treated in the same way. Thus all comparisons become isomorphisms in the formal neighborhood systems after suitable refinements.

For precision, test these systems against an arbitrary output germ \(A\). Morphisms from a formal system into \(A\) are filtered colimits of the morphism groups from its terms. The preceding common refinements show both that every representative passes to the system (8), and that two representatives agree there exactly when they agree after a further refinement. The colimits are consequently identical. This proves (3) equals (8) as a pro-object, without asserting eventual equality of ordinary sheaves or a uniform stabilization of all denominators. It also proves that fixing \(K_2\) gives the same pro-object when \(\xi_0\ne0\).

For \(\zeta_0\ne0\) reverse the construction. When both endpoints are zero and the middle is nonzero the zero representative described above makes all systems zero. When all are zero, localization is ordinary base-germ localization; support isolation gives the boundary-controlled image of the tensor germ directly. These exhaust the cases and complete the proof. \(\square\)

The construction respects morphisms of germs. Represent a morphism by a fraction, make the common incoming replacements just used, apply tensor and proper-support image to its ordinary numerator, and invert the resulting denominator. A further common refinement gives the same arrow. Composition of fractions and identity arrows are preserved because ordinary convolution preserves them before localization. This supplies the functoriality used below.

## Three compatibility calculations

First, composition can be expressed as a transformation with one enlarged output manifold. Let

\[
i:X\times Y\times Z\hookrightarrow
(X\times Z)\times(Y\times Z),
\qquad i(x,y,z)=(x,z;y,z),
\]

and put \(\widetilde K_1=i_*(K_1\boxtimes k_Z)\). Then

\[
K_1\circ_\mu K_2\simeq\widetilde K_1\circ_\mu K_2,
\tag{10}
\]

where the right output point is \((p_X,p_Z^a)\), its middle point is \((p_Y,p_Z^a)\), and its last manifold is a point. The physical point of \(\widetilde K_1\) is
\((p_X,p_Z^a,p_Y^a,p_Z)\).
To check composability, the closed-embedding microsupport formula forces the two physical \(Z\)-covectors to sum to zero; the constant \(k_Z\) has no tangential \(Z\)-covector. Matching with \(K_2\) therefore reduces exactly to (2), with no extra middle choice. For ordinary representatives, tensor with \(K_2\) restricts to the closed diagonal in the two \(Z\) copies. Integration over the second \(Z\) removes that diagonal and leaves the original integration over \(Y\). Projection formula gives (10). These maps commute with every denominator and neighborhood transition, so they identify the formal systems and then their representatives. Closed direct image introduces no exceptional orientation shift here.

Second, let \(K_3\) be a germ from \(W\) to \(Z\), with fixed \(p_W\). Suppose the triple matching set, after both antipodal matches, has

\[
\mathcal T(K_1,K_2,K_3)
=\{(p_X,p_Y,p_Z,p_W)\}
\tag{11}
\]

on a neighborhood of that point. This condition isolates the whole matching germ; unlike (2), it does not fix the endpoints before taking the intersection. Then the two adjacent pairs and the two pairs involving their composites are composable, and

\[
(K_1\circ_\mu K_2)\circ_\mu K_3
\simeq K_1\circ_\mu(K_2\circ_\mu K_3).
\tag{12}
\]

Here is the isolation check. The specified triple actually occurs by (11). Any other nearby middle witness for the first pair can be appended to the fixed \(K_3\) witness, contradicting (11); the other adjacent pair is treated using the fixed \(K_1\) witness. For a pair involving a composite, use (7) with arbitrarily small matching neighborhoods. Choose the confined, proper representatives from its proof. Any putative nearby witness outside the designated triple has a convergent witnessing subsequence within those representatives. Its limit gives a triple witness in (11), so it must be the designated one. Shrinking the matching neighborhoods proves isolation for the composite pairs too.

To prove (12) as an actual natural isomorphism, take the formal systems over all three denominators and over the two intermediate base neighborhoods. Common refined cutoffs and the just-proved isolation identify either iterated construction with that system. For every ordinary term, associativity of tensor and \(!\)-Fubini identify both parenthesizations with integration of
\(q_{12}^{-1}K_1'\otimes q_{23}^{-1}K_2'\otimes q_{34}^{-1}K_3'\)
over \(Y\times Z\). The ordinary associativity maps commute with refinements and neighborhood maps. Testing against every output germ, iterated filtered colimits agree with the colimit over the joint indexing category: each finite set of choices has a common refinement. Thus the two formal systems are naturally isomorphic, and representability gives (12). The ordinary coherence equalities survive this construction, since they hold for each common ordinary term.

The literal hypothesis (11) is particularly strong. A nonzero matching tuple has nearby distinct tuples obtained by scaling all its covectors by the same positive number. Thus it cannot be an isolated singleton in the entire matching set. We retain (11) for this associativity statement; an associativity theorem with only endpoint-fibre isolation would require its own hypotheses and proof. Ordinary global convolution and the earlier admissible regional composition have their separately established associativity statements.

Third, take another composable pair \((K_1',K_2')\) on \(X',Y',Z'\), with its own selected covectors. The external pair is composable, and

\[
(K_1\boxtimes^L K_1')\circ_\mu
(K_2\boxtimes^L K_2')
\simeq (K_1\circ_\mu K_2)\boxtimes^L
(K_1'\circ_\mu K_2').
\tag{13}
\]

Indeed external-product microsupport is contained in the product of the two microsupports, so every nearby matching witness has a witness for each original pair. Conditions (2) for those pairs force the prescribed two middle covectors. Product neighborhoods form a neighborhood basis at the product base point. Apply the representation proof with such neighborhoods; its proper replacements in the two factors have a proper product support. The ordinary external-product and \(!\)-Fubini maps give (13) for these representatives and commute with their transitions. The same filtered-colimit argument identifies the represented germs. This proves the compatibility without requiring the microsupport of an external product to equal the full product for arbitrary coefficients.

## Kernels that act on every incoming germ

Define \(\mathcal N(X,Y;p_X,p_Y)\) as the full subcategory of kernel germs satisfying

\[
\operatorname{SS}(K)\cap
(\{p_X\}\times T^*Y)
\subset\{(p_X,p_Y^a)\}
\quad\text{near }(p_X,p_Y^a).
\tag{14}
\]

It is triangulated: shifts preserve microsupport, and the microsupport of a term of a triangle is contained in the union of the other two. For any input kernel germ \(L\) from \(Z\) to \(Y\), (14) forces the sole possible middle witness to be \(p_Y\). Thus the pair is composable and there is a bifunctor

\[
\mathcal N(X,Y;p_X,p_Y)\times
D^b(k_{Y\times Z};(p_Y,p_Z^a))
\longrightarrow D^b(k_{X\times Z};(p_X,p_Z^a)).
\tag{15}
\]

If \(L\) satisfies the analogous condition at \(p_Y,p_Z\), the composite satisfies (14) at \(p_X,p_Z\). To check it, take the confined microsupport estimate (7) inside neighborhoods where both versions of (14) hold. A witness with first component \(p_X\) first has middle component \(p_Y\), then last component \(p_Z\). The proper confined representatives exclude additional limiting witnesses. Hence composition also induces

\[
\mathcal N(X,Y;p_X,p_Y)\times
\mathcal N(Y,Z;p_Y,p_Z)
\longrightarrow\mathcal N(X,Z;p_X,p_Z).
\tag{16}
\]

In particular take \(Z\) to be a point. A graph kernel satisfies (14), so it acts on every sheaf germ at its corresponding input point. When such a kernel also has the selected-region admissibility of the earlier kernel lessons, this germ action agrees with its regional localized operator. One checks the comparison by its proper-support kernel map: selected cotangent properness confines all middle covectors and base points over a compact output neighborhood, and the graph selects a unique input germ. The boundary-controlled direct-image comparison in the proof of (8) then removes the part outside a neighborhood of that input point. The actual comparison cones have no output incidence. Consequently a kernel isomorphism at the selected physical pair gives an isomorphism of these point-localized actions. This is the kernel-germ descent used for the diagonal coefficient model in Coefficients in a quantization of the identity.

## Exercises with complete solutions

### Check the middle sign

*Difficulty: Introductory.*

Let a witness of (1) have middle covector \(\eta\). Write the covectors of both pulled-back kernels on \(X\times Y\times Z\) and their sum. What goes wrong if the first physical middle covector is taken to be \(+\eta\)?

**Solution.** The two covectors are \((\xi,-\eta,0)\) and \((0,\eta,-\zeta)\). Their sum is \((\xi,0,-\zeta)\), which is the pullback of the output covector under \(q_{13}\). With \(+\eta\) in the first kernel the sum has middle component \(2\eta\). It is not such a pullback unless \(\eta=0\), so that convention fails to describe the pushforward incidence for nonzero middle covectors.

### Local isolation is weaker than whole-fibre isolation

*Difficulty: Intermediate.*

In one-dimensional cotangent fibres, let the two twisted relations be the unions of graphs \(\xi=\eta\), \(\xi=2\eta\) and \(\eta=\zeta\), \(\eta=\zeta/2\), respectively. Fix endpoint covectors \(\xi=\zeta=1\) and chosen middle covector \(\eta=1\). Compare (2) and (4) for these relations.

**Solution.** There are two matched middle values: \(1\) uses the first branch of each relation, and \(1/2\) uses the second branch of each. A neighborhood of \(\eta=1\) excludes \(1/2\), so the local isolation condition (2) holds. Condition (4) fails because it inspects the whole middle fibre at the fixed bases and sees both values. This is a calculation of closed conic relation models; it does not presume that every such relation is the microsupport of a particular kernel. The cutoff step is precisely what removes the unwanted remote middle branch from an appropriate representative.

### Cancellation with zero endpoints is an obstruction at infinity

*Difficulty: Intermediate.*

Take both \(X\) and \(Z\) to be points, \(Y=\mathbb R\), and both kernels to be the skyscraper \(k_{\{0\}}\), with \(k\ne0\). At any chosen middle covector show why the pair fails (2), and exhibit the obstruction (5). Does ordinary convolution nevertheless exist?

**Solution.** Each skyscraper has the entire conormal fibre at zero as microsupport. Thus every \(\eta\in T_0^*\mathbb R\) matches zero endpoint covectors. No middle covector is isolated, including \(\eta=0\), so (2) fails. Every nonzero middle covector also violates (5). Ordinary convolution does exist and is \(R\Gamma_c(\mathbb R;k_{\{0\}}\otimes^L k_{\{0\}})=k\). The obstruction concerns whether a result is determined by the specified two microlocal germs under the theorem's hypotheses; it is not a failure of ordinary \(!\)-convolution to be defined.

### Why the graph realization carries opposite Z covectors

*Difficulty: Advanced.*

For the embedding \(i\) in (10), compute its conormal condition on the two \(Z\) covectors. Explain the selected physical point of \(\widetilde K_1\) and the absence of a codimension shift.

**Solution.** The tangent vector in the two \(Z\) positions is \((v_Z,v_Z)\), so a conormal covector has \(\zeta_1+\zeta_2=0\). The original external factor \(k_Z\) has zero tangential covector, leaving the same sum-zero condition for the lifted microsupport. For output \((p_X,p_Z^a)\) and middle \((p_Y,p_Z^a)\), the physical kernel point is \((p_X,p_Z^a,p_Y^a,p_Z)\). Its \(Z\) components are opposite as required. Formula (10) uses closed direct image and a diagonal support constraint; it does not apply exceptional restriction along \(i\). No relative dualizing complex appears, and hence no extra shift arises.

### Isolating endpoints is different from isolating the whole graph

*Difficulty: Advanced.*

Take three diagonal kernels on copies of the same manifold and a nonzero covector \(p\). At the triple with all selected covectors \(p\), compare the pair condition (2), endpoint-fibre isolation for the triple, and the whole-matching condition (11). Does failure of the last condition negate ordinary associativity?

**Solution.** A diagonal kernel has twisted relation \(u=v\). Thus either adjacent pair has matching triples \(u=v=w\); after fixing its endpoints at \(p\), its middle is forced to be \(p\), proving (2). The three-kernel matching set is \(u=v=w=t\), so fixing the outer endpoints also forces both middle points to be \(p\). But the full set contains distinct nearby tuples with all covectors scaled from \(p\) by a common positive factor. Therefore (11) fails. The ordinary diagonal kernels have proper identity projections, and their convolutions are again the diagonal kernel; ordinary associativity follows from the kernel calculus. Its proof uses those global support conditions, not (11). A sufficient condition in a particular theorem need not be necessary for the conclusion by another theorem.

### A formal pro-object is not a chosen term

*Difficulty: Advanced.*

In abelian groups consider the inverse system \(\mathbb Z\xleftarrow{2}\mathbb Z\xleftarrow{2}\cdots\). Compute morphisms from its formal pro-object into the constant object \(\mathbb Z\). Compare them with morphisms from one term and from the ordinary inverse limit.

**Solution.** By the pro-object convention the morphism group is the direct limit of \(\operatorname{Hom}(\mathbb Z,\mathbb Z)=\mathbb Z\) under precomposition by multiplication by two. It is \(\mathbb Z[1/2]\). One term instead gives \(\mathbb Z\). The ordinary inverse limit is zero: its first component would have to be divisible by every power of two, and the same holds for every component. Its morphism group into \(\mathbb Z\) is zero. Thus neither one term nor an ordinary inverse limit computes the formal pro-object. In the theorem, representability is proved using denominator refinements and isolated direct images; it is not obtained by erasing the quotation marks in (3).

## References

Masaki Kashiwara and Pierre Schapira's [Microlocal study of sheaves](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §6.3, pp. 108–114, supplies the microlocal kernel and contact-transformation setting. Its Proposition 6.3.1 imposes properness of a selected microsupport projection; Proposition 6.3.3 proves composition under the corresponding regional hypotheses. Those statements do not by themselves prove the isolated-covector formal representability theorem used here. In particular, this lesson has not acquired a constructibility or global properness assumption by comparison with that source.

The exact programme inputs remain `SH02-MC-CUTOFF` for the refined incoming directional bound and `SH02-MC-DIRECT-GERMS` and `SH02-MC-DIRECT-REP` for isolated direct images and representability. Their complete provider texts and revision bindings are not included in this two-lesson download. The written nested-cone separation, bounded/unbounded witness argument, denominator comparisons, compatibilities and solved exercises are proofs under those stated inputs; a reader must supply those inputs to obtain a closed proof chain. The free monograph provides the comparison just described, not a substitute proof of the missing providers.

The lesson and solutions are independently written teaching. No human source text or figures are reproduced; the original AI expression is CC0. The source comparison does not certify the transitive prerequisites or the whole parent course.