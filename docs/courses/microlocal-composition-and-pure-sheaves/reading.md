# Microlocal composition and pure sheaves

Two lessons explain how kernel germs compose at prescribed covectors and how closed half-space tests define pure and simple sheaves with their exact shifts. Fourteen exercises have complete solutions.

- [Microlocal composition at prescribed covectors](microlocal-composition-at-prescribed-covectors.html) · [editable source](src/microlocal-composition-at-prescribed-covectors.md)
- [Pure and simple sheaves from directional tests](pure-and-simple-sheaves-from-directional-tests.html) · [editable source](src/pure-and-simple-sheaves-from-directional-tests.md)

The proofs use the stated ordinary kernel calculus, localized-category cutoff and direct-image theorems, conormal coefficient models, contact normal forms and ordered Lagrangian index identities. Coefficients are arbitrary bounded modules over a commutative ring of finite global dimension. Simplicity and nonvanishing examples assume a nonzero ring.

The exact preceding proof providers are not included in this download; their revision bindings and transitive source checks remain open. The source comparison in each lesson identifies what its freely readable references prove. It does not replace the stated programme inputs or certify completion of the parent course.

Download the readings, editable sources and build code · [Reuse terms](LICENSE.txt) · Provenance


# Microlocal composition at prescribed covectors

Ordinary convolution integrates across an entire intermediate manifold. A kernel germ at one pair of covectors does not retain all that information. To compose two germs, we must isolate the intermediate covector that contributes to the chosen output. This lesson constructs that composition, explains why a formal system of convolutions is represented by a bounded sheaf germ, and proves its basic compatibilities.

Use the ordinary kernel and localized-category prerequisites from the preceding lessons. In particular, the refined incoming cutoff and the isolated-incidence direct-image theorem are inputs from the microlocal-category theory. We state exactly what is used. Coefficients are arbitrary modules over a commutative ring $k$ of finite global dimension; all sheaf complexes are bounded. Manifolds are finite dimensional, real, Hausdorff and second countable. No constructibility or global properness is assumed.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

## Which middle covector is being composed

Fix $p_X=(x_0;\xi_0)$, $p_Y=(y_0;\eta_0)$, and $p_Z=(z_0;\zeta_0)$. Zero covectors are allowed. Let $K_1$ be a germ on $X\times Y$ at $(p_X,p_Y^a)$, and $K_2$ a germ on $Y\times Z$ at $(p_Y,p_Z^a)$. A superscript $a$ reverses the covector and leaves its base point fixed.

For chosen representatives form the twisted matching set

$$
\begin{split}
\mathcal T(K_1,K_2)=\{(u,v,w):
 &(u,v^a)\in\operatorname{SS}(K_1),\\
 &(v,w^a)\in\operatorname{SS}(K_2)\},
\qquad \rho(u,v,w)=(u,w^a).
\end{split}
\tag{1}
$$

The opposite physical middle covectors are $-\eta$ in $K_1$ and $+\eta$ in $K_2$. Their sum is zero in the ordinary tensor kernel. We call the pair **microlocally composable** if

$$
\mathcal T(K_1,K_2)\cap
(\{p_X\}\times T^*Y\times\{p_Z\})
\subset\{(p_X,p_Y,p_Z)\}
\quad\text{near }(p_X,p_Y,p_Z).
\tag{2}
$$

The allowed singleton need not occur. Condition (2) is local around the specified middle covector. It does not exclude a different witness far away in that fibre. The germ of microsupport is invariant under an isomorphism in each point-localized category, so (2) depends only on the two kernel germs.

Ordinary convolution is
$K_1\circ K_2=Rq_{13!}(q_{12}^{-1}K_1\otimes^Lq_{23}^{-1}K_2)$.
For germs we first form the formal system

$$
P=\text{“}\!\lim_{K_1',K_2'}\!\text{”}\;K_1'\circ K_2',
\tag{3}
$$

where $K_i'\to K_i$ runs over incoming denominators at the appropriate physical pair. A denominator means its cone misses that pair. The notation in (3) means a pro-object: it specifies filtered colimits of morphisms out of the terms into each test object. It is not an inverse limit of sheaves, and it makes no assertion that one fixed ordinary convolution computes the answer.

## Replacing a kernel to control the whole middle fibre

At the fixed base points, two additional conditions are useful:

$$
\mathcal T\cap
(\{p_X\}\times T_{y_0}^*Y\times\{p_Z\})
\subset\{(p_X,p_Y,p_Z)\},
\tag{4}
$$

$$
\mathcal T\cap
(\{(x_0;0)\}\times \dot T_{y_0}^*Y\times\{(z_0;0)\})
=\varnothing.
\tag{5}
$$

The dot removes the zero covector. Condition (4) controls every covector in the middle fibre at $y_0$, not just those near $\eta_0$. Condition (5) rules out nonzero middle cancellation when both endpoint covectors vanish.

Here is the cutoff consequence we need. If $\xi_0\ne0$, a microlocally composable pair admits an incoming replacement $K_1'\to K_1$, invertible at $(p_X,p_Y^a)$, for which (4) holds and

$$
\operatorname{SS}(K_1')\cap
(\{(x_0;0)\}\times\dot T_{y_0}^*Y)=\varnothing.
\tag{6}
$$

The same construction works with any specified closed conic set in place of $\operatorname{SS}(K_2)$. It also works simultaneously with a finite union of such sets. This last clause will allow common refinements of two denominators.

**Proof of the cutoff consequence.** Work in the cotangent fibre at $(x_0,y_0)$, and write $q=(\xi_0,-\eta_0)$. Local isolation gives a compact neighborhood $L$ of $\eta_0$ such that matching the two original microsupports at the fixed endpoints $p_X,p_Z$, for $\eta\in L$, occurs only at $\eta_0$. Choose two proper closed convex cones $C_-$ and $C_+$ around $q$, with $q\in\operatorname{Int}C_-$, $C_-\setminus0\subset\operatorname{Int}C_+$, and with the fixed-first-component slice of $C_+$ contained in $\{\xi_0\}\times(-L)$. They can also be chosen to contain no nonzero vector with first component zero. Indeed, because $\xi_0\ne0$, choose a linear functional $\ell$ of the first component with $\ell(\xi_0)=1$, take two sufficiently small nested closed convex balls around $q$ in the hyperplane $\ell(\xi)=1$, and take their positive cones. Their normalized sections and their fixed-first-component slices are compact.

Choose an open conic neighborhood $U$ of $q$ contained in $\operatorname{Int}C_-$. The refined incoming replacement will be an isomorphism throughout $U$. On a compact normalized section, $C_-\cap\operatorname{SS}(K_1)$ is disjoint from the set of second-kernel matching directions with fixed first component $\xi_0$ that lie in $C_+$ but outside $U$: an intersection would be an original matching covector in $L$, hence would equal $q$, which is in $U$. Both sets are closed on that compact section. Their separation therefore gives a conic neighborhood $W$ of $(C_-\cap\operatorname{SS}(K_1))\setminus0$, contained in $\operatorname{Int}C_+$, whose fixed-first-component slice contains no second-kernel matching covector outside $U$.

Apply the refined incoming replacement theorem with the closed cone $C_-$, the inner isomorphism cone $U$, and the directional neighborhood $W$. It gives $K_1'\to K_1$ invertible throughout $U$, with microsupport at the base point contained in $W\cup\{0\}$. A matching covector inside $U$ belongs to the original microsupport, because the replacement is an isomorphism there, and so it is the chosen covector. A matching covector outside $U$ is excluded by the choice of $W$. This proves (4). The containment in $C_+\cup\{0\}$ excludes every nonzero covector with first component zero and proves (6). For any prescribed closed conic matching set the same argument applies under the stated local isolation; for finitely many such sets choose $L$ for all of them and separate their finite closed union outside $U$. Inside $U$, agreement with the original microsupport preserves each isolation condition. The construction uses the refined replacement theorem at its stated arbitrary bounded coefficient scope. $\square$

If $\zeta_0\ne0$, apply the argument to $K_2$ after interchanging the endpoint roles. In either case (6), or its endpoint analogue, supplies (5).

There are two remaining cases. If both endpoint covectors are zero but $\eta_0\ne0$, positive scaling preserves their zeros. If both kernel microsupports contained the specified pairs, scaling $\eta_0$ by numbers tending to one would contradict (2). Thus one germ is zero and can be replaced by the zero kernel. If all three covectors are zero, (2) isolates the intersection of the two supports in the middle base variable. At the fixed bases, any nonzero matching middle covector could be scaled down towards zero, again contradicting (2). This proves (4) and (5) in the last case as well.

Consequently every composable pair admits incoming representatives satisfying (4) and (5), including the cases involving zero covectors.

## Why the formal composition is a bounded germ

**Theorem.** For a microlocally composable pair, the pro-object (3) is represented by an object of $D^b(k_{X\times Z};(p_X,p_Z^a))$. Denote it by $K_1\circ_\mu K_2$. For every neighborhood $W$ of the specified triple,

$$
\operatorname{SS}(K_1\circ_\mu K_2)
\subset\rho\bigl(W\cap\mathcal T(K_1,K_2)\bigr)
\quad\text{near }(p_X,p_Z^a).
\tag{7}
$$

If the representatives already satisfy (4) and (5), there is a canonical formal identification

$$
K_1\circ_\mu K_2
\simeq\text{“}\!\lim_{V\ni y_0}\!\text{”}\;(K_1)_{X\times V}\circ K_2.
\tag{8}
$$

If $\xi_0\ne0$, one may instead hold $K_2$ fixed and vary only $K_1'\to K_1$ in (3).

**Proof.** First (2), (4) and (5) imply isolated matching over the fixed endpoint covectors on a neighborhood of the middle *base point*, with no bound imposed on the middle covector. If this were false, choose offending $(y_j;\eta_j)$, with $y_j\to y_0$, matching those endpoints. If $\eta_j$ is bounded, closedness and (4) force a subsequence to converge to $p_Y$; then (2) excludes it. If $|\eta_j|\to\infty$, divide both physical kernel covectors by $|\eta_j|$. A subsequence of unit middle covectors converges to a nonzero vector at $y_0$, while the endpoint covectors tend to zero. Conicity and closedness give the forbidden pair in (5). This proves the asserted base-neighborhood isolation.

Put
$H=q_{12}^{-1}K_1\otimes^Lq_{23}^{-1}K_2$
on $X\times Y\times Z$. Condition (5) is exactly the noncharacteristic tensor condition at the fixed base point: possible cancellation has components $(0,-\eta,0)+(0,\eta,0)$. It persists on a smaller base neighborhood. Indeed a sequence of nonzero cancellations at convergent base points, normalized to unit length, would yield a prohibited limiting cancellation at the fixed bases. The ordinary tensor estimate therefore gives

$$
\operatorname{SS}(H)\subset
(\operatorname{SS}(K_1)\times T_Z^*Z)
+(T_X^*X\times\operatorname{SS}(K_2))
\tag{9}
$$

there. A covector on the right of (9) whose middle component vanishes comes from a matching triple (1). By the preceding isolation, the incidence for $q_{13}$ over $(p_X,p_Z^a)$ is confined to
$(x_0,y_0,z_0;\xi_0,0,-\zeta_0)$.

Apply the isolated-incidence direct-image prerequisite to $H$. In its exact form it represents the formal proper-support image by a bounded germ, identifies it with the formal ordinary image, and allows its microsupport witnesses to be confined to any prescribed neighborhood of that incidence point. Its direct-germ formula and boundary-control construction give (8). Restricting the open middle neighborhoods alone is legitimate *after this direct-image argument*; they have not been declared cofinal among all microlocal denominators beforehand. Combining the confined witnesses with (9) proves (7). A proper replacement has a closed image for the retained witnesses, so no uncontrolled witness at infinity has been added to the estimate.

It remains to identify this represented image with the system (3), rather than just one choice of representatives. Consider denominators $K_1'\to K_1$ and $K_2'\to K_2$. When $\xi_0\ne0$, make a further incoming replacement of $K_1'$ using the union of the matching sets of $K_2'$ and $K_2$. It satisfies (4) and (5) for both. Near the specified physical pair the cone of $K_2'\to K_2$ has no microsupport. The noncharacteristic tensor estimate now shows that the induced tensor comparison has cone invisible at the specified incidence point. The same isolated-incidence direct-image theorem makes its image comparison invertible at $(p_X,p_Z^a)$. Refining the first denominator is treated in the same way. Thus all comparisons become isomorphisms in the formal neighborhood systems after suitable refinements.

For precision, test these systems against an arbitrary output germ $A$. Morphisms from a formal system into $A$ are filtered colimits of the morphism groups from its terms. The preceding common refinements show both that every representative passes to the system (8), and that two representatives agree there exactly when they agree after a further refinement. The colimits are consequently identical. This proves (3) equals (8) as a pro-object, without asserting eventual equality of ordinary sheaves or a uniform stabilization of all denominators. It also proves that fixing $K_2$ gives the same pro-object when $\xi_0\ne0$.

For $\zeta_0\ne0$ reverse the construction. When both endpoints are zero and the middle is nonzero the zero representative described above makes all systems zero. When all are zero, localization is ordinary base-germ localization; support isolation gives the boundary-controlled image of the tensor germ directly. These exhaust the cases and complete the proof. $\square$

The construction respects morphisms of germs. Represent a morphism by a fraction, make the common incoming replacements just used, apply tensor and proper-support image to its ordinary numerator, and invert the resulting denominator. A further common refinement gives the same arrow. Composition of fractions and identity arrows are preserved because ordinary convolution preserves them before localization. This supplies the functoriality used below.

## Three compatibility calculations

First, composition can be expressed as a transformation with one enlarged output manifold. Let

$$
i:X\times Y\times Z\hookrightarrow
(X\times Z)\times(Y\times Z),
\qquad i(x,y,z)=(x,z;y,z),
$$

and put $\widetilde K_1=i_*(K_1\boxtimes k_Z)$. Then

$$
K_1\circ_\mu K_2\simeq\widetilde K_1\circ_\mu K_2,
\tag{10}
$$

where the right output point is $(p_X,p_Z^a)$, its middle point is $(p_Y,p_Z^a)$, and its last manifold is a point. The physical point of $\widetilde K_1$ is
$(p_X,p_Z^a,p_Y^a,p_Z)$.
To check composability, the closed-embedding microsupport formula forces the two physical $Z$-covectors to sum to zero; the constant $k_Z$ has no tangential $Z$-covector. Matching with $K_2$ therefore reduces exactly to (2), with no extra middle choice. For ordinary representatives, tensor with $K_2$ restricts to the closed diagonal in the two $Z$ copies. Integration over the second $Z$ removes that diagonal and leaves the original integration over $Y$. Projection formula gives (10). These maps commute with every denominator and neighborhood transition, so they identify the formal systems and then their representatives. Closed direct image introduces no exceptional orientation shift here.

Second, let $K_3$ be a germ from $W$ to $Z$, with fixed $p_W$. Suppose the triple matching set, after both antipodal matches, has

$$
\mathcal T(K_1,K_2,K_3)
=\{(p_X,p_Y,p_Z,p_W)\}
\tag{11}
$$

on a neighborhood of that point. This condition isolates the whole matching germ; unlike (2), it does not fix the endpoints before taking the intersection. Then the two adjacent pairs and the two pairs involving their composites are composable, and

$$
(K_1\circ_\mu K_2)\circ_\mu K_3
\simeq K_1\circ_\mu(K_2\circ_\mu K_3).
\tag{12}
$$

Here is the isolation check. The specified triple actually occurs by (11). Any other nearby middle witness for the first pair can be appended to the fixed $K_3$ witness, contradicting (11); the other adjacent pair is treated using the fixed $K_1$ witness. For a pair involving a composite, use (7) with arbitrarily small matching neighborhoods. Choose the confined, proper representatives from its proof. Any putative nearby witness outside the designated triple has a convergent witnessing subsequence within those representatives. Its limit gives a triple witness in (11), so it must be the designated one. Shrinking the matching neighborhoods proves isolation for the composite pairs too.

To prove (12) as an actual natural isomorphism, take the formal systems over all three denominators and over the two intermediate base neighborhoods. Common refined cutoffs and the just-proved isolation identify either iterated construction with that system. For every ordinary term, associativity of tensor and $!$-Fubini identify both parenthesizations with integration of
$q_{12}^{-1}K_1'\otimes q_{23}^{-1}K_2'\otimes q_{34}^{-1}K_3'$
over $Y\times Z$. The ordinary associativity maps commute with refinements and neighborhood maps. Testing against every output germ, iterated filtered colimits agree with the colimit over the joint indexing category: each finite set of choices has a common refinement. Thus the two formal systems are naturally isomorphic, and representability gives (12). The ordinary coherence equalities survive this construction, since they hold for each common ordinary term.

The literal hypothesis (11) is particularly strong. A nonzero matching tuple has nearby distinct tuples obtained by scaling all its covectors by the same positive number. Thus it cannot be an isolated singleton in the entire matching set. We retain (11) for this associativity statement; an associativity theorem with only endpoint-fibre isolation would require its own hypotheses and proof. Ordinary global convolution and the earlier admissible regional composition have their separately established associativity statements.

Third, take another composable pair $(K_1',K_2')$ on $X',Y',Z'$, with its own selected covectors. The external pair is composable, and

$$
(K_1\boxtimes^L K_1')\circ_\mu
(K_2\boxtimes^L K_2')
\simeq (K_1\circ_\mu K_2)\boxtimes^L
(K_1'\circ_\mu K_2').
\tag{13}
$$

Indeed external-product microsupport is contained in the product of the two microsupports, so every nearby matching witness has a witness for each original pair. Conditions (2) for those pairs force the prescribed two middle covectors. Product neighborhoods form a neighborhood basis at the product base point. Apply the representation proof with such neighborhoods; its proper replacements in the two factors have a proper product support. The ordinary external-product and $!$-Fubini maps give (13) for these representatives and commute with their transitions. The same filtered-colimit argument identifies the represented germs. This proves the compatibility without requiring the microsupport of an external product to equal the full product for arbitrary coefficients.

## Kernels that act on every incoming germ

Define $\mathcal N(X,Y;p_X,p_Y)$ as the full subcategory of kernel germs satisfying

$$
\operatorname{SS}(K)\cap
(\{p_X\}\times T^*Y)
\subset\{(p_X,p_Y^a)\}
\quad\text{near }(p_X,p_Y^a).
\tag{14}
$$

It is triangulated: shifts preserve microsupport, and the microsupport of a term of a triangle is contained in the union of the other two. For any input kernel germ $L$ from $Z$ to $Y$, (14) forces the sole possible middle witness to be $p_Y$. Thus the pair is composable and there is a bifunctor

$$
\mathcal N(X,Y;p_X,p_Y)\times
D^b(k_{Y\times Z};(p_Y,p_Z^a))
\longrightarrow D^b(k_{X\times Z};(p_X,p_Z^a)).
\tag{15}
$$

If $L$ satisfies the analogous condition at $p_Y,p_Z$, the composite satisfies (14) at $p_X,p_Z$. To check it, take the confined microsupport estimate (7) inside neighborhoods where both versions of (14) hold. A witness with first component $p_X$ first has middle component $p_Y$, then last component $p_Z$. The proper confined representatives exclude additional limiting witnesses. Hence composition also induces

$$
\mathcal N(X,Y;p_X,p_Y)\times
\mathcal N(Y,Z;p_Y,p_Z)
\longrightarrow\mathcal N(X,Z;p_X,p_Z).
\tag{16}
$$

In particular take $Z$ to be a point. A graph kernel satisfies (14), so it acts on every sheaf germ at its corresponding input point. When such a kernel also has the selected-region admissibility of the earlier kernel lessons, this germ action agrees with its regional localized operator. One checks the comparison by its proper-support kernel map: selected cotangent properness confines all middle covectors and base points over a compact output neighborhood, and the graph selects a unique input germ. The boundary-controlled direct-image comparison in the proof of (8) then removes the part outside a neighborhood of that input point. The actual comparison cones have no output incidence. Consequently a kernel isomorphism at the selected physical pair gives an isomorphism of these point-localized actions. This is the kernel-germ descent used for the diagonal coefficient model in Coefficients in a quantization of the identity.

## Exercises with complete solutions

### Check the middle sign

*Difficulty: Introductory.*

Let a witness of (1) have middle covector $\eta$. Write the covectors of both pulled-back kernels on $X\times Y\times Z$ and their sum. What goes wrong if the first physical middle covector is taken to be $+\eta$?

**Solution.** The two covectors are $(\xi,-\eta,0)$ and $(0,\eta,-\zeta)$. Their sum is $(\xi,0,-\zeta)$, which is the pullback of the output covector under $q_{13}$. With $+\eta$ in the first kernel the sum has middle component $2\eta$. It is not such a pullback unless $\eta=0$, so that convention fails to describe the pushforward incidence for nonzero middle covectors.

### Local isolation is weaker than whole-fibre isolation

*Difficulty: Intermediate.*

In one-dimensional cotangent fibres, let the two twisted relations be the unions of graphs $\xi=\eta$, $\xi=2\eta$ and $\eta=\zeta$, $\eta=\zeta/2$, respectively. Fix endpoint covectors $\xi=\zeta=1$ and chosen middle covector $\eta=1$. Compare (2) and (4) for these relations.

**Solution.** There are two matched middle values: $1$ uses the first branch of each relation, and $1/2$ uses the second branch of each. A neighborhood of $\eta=1$ excludes $1/2$, so the local isolation condition (2) holds. Condition (4) fails because it inspects the whole middle fibre at the fixed bases and sees both values. This is a calculation of closed conic relation models; it does not presume that every such relation is the microsupport of a particular kernel. The cutoff step is precisely what removes the unwanted remote middle branch from an appropriate representative.

### Cancellation with zero endpoints is an obstruction at infinity

*Difficulty: Intermediate.*

Take both $X$ and $Z$ to be points, $Y=\mathbb R$, and both kernels to be the skyscraper $k_{\{0\}}$, with $k\ne0$. At any chosen middle covector show why the pair fails (2), and exhibit the obstruction (5). Does ordinary convolution nevertheless exist?

**Solution.** Each skyscraper has the entire conormal fibre at zero as microsupport. Thus every $\eta\in T_0^*\mathbb R$ matches zero endpoint covectors. No middle covector is isolated, including $\eta=0$, so (2) fails. Every nonzero middle covector also violates (5). Ordinary convolution does exist and is $R\Gamma_c(\mathbb R;k_{\{0\}}\otimes^L k_{\{0\}})=k$. The obstruction concerns whether a result is determined by the specified two microlocal germs under the theorem's hypotheses; it is not a failure of ordinary $!$-convolution to be defined.

### Why the graph realization carries opposite Z covectors

*Difficulty: Advanced.*

For the embedding $i$ in (10), compute its conormal condition on the two $Z$ covectors. Explain the selected physical point of $\widetilde K_1$ and the absence of a codimension shift.

**Solution.** The tangent vector in the two $Z$ positions is $(v_Z,v_Z)$, so a conormal covector has $\zeta_1+\zeta_2=0$. The original external factor $k_Z$ has zero tangential covector, leaving the same sum-zero condition for the lifted microsupport. For output $(p_X,p_Z^a)$ and middle $(p_Y,p_Z^a)$, the physical kernel point is $(p_X,p_Z^a,p_Y^a,p_Z)$. Its $Z$ components are opposite as required. Formula (10) uses closed direct image and a diagonal support constraint; it does not apply exceptional restriction along $i$. No relative dualizing complex appears, and hence no extra shift arises.

### Isolating endpoints is different from isolating the whole graph

*Difficulty: Advanced.*

Take three diagonal kernels on copies of the same manifold and a nonzero covector $p$. At the triple with all selected covectors $p$, compare the pair condition (2), endpoint-fibre isolation for the triple, and the whole-matching condition (11). Does failure of the last condition negate ordinary associativity?

**Solution.** A diagonal kernel has twisted relation $u=v$. Thus either adjacent pair has matching triples $u=v=w$; after fixing its endpoints at $p$, its middle is forced to be $p$, proving (2). The three-kernel matching set is $u=v=w=t$, so fixing the outer endpoints also forces both middle points to be $p$. But the full set contains distinct nearby tuples with all covectors scaled from $p$ by a common positive factor. Therefore (11) fails. The ordinary diagonal kernels have proper identity projections, and their convolutions are again the diagonal kernel; ordinary associativity follows from the kernel calculus. Its proof uses those global support conditions, not (11). A sufficient condition in a particular theorem need not be necessary for the conclusion by another theorem.

### A formal pro-object is not a chosen term

*Difficulty: Advanced.*

In abelian groups consider the inverse system $\mathbb Z\xleftarrow{2}\mathbb Z\xleftarrow{2}\cdots$. Compute morphisms from its formal pro-object into the constant object $\mathbb Z$. Compare them with morphisms from one term and from the ordinary inverse limit.

**Solution.** By the pro-object convention the morphism group is the direct limit of $\operatorname{Hom}(\mathbb Z,\mathbb Z)=\mathbb Z$ under precomposition by multiplication by two. It is $\mathbb Z[1/2]$. One term instead gives $\mathbb Z$. The ordinary inverse limit is zero: its first component would have to be divisible by every power of two, and the same holds for every component. Its morphism group into $\mathbb Z$ is zero. Thus neither one term nor an ordinary inverse limit computes the formal pro-object. In the theorem, representability is proved using denominator refinements and isolated direct images; it is not obtained by erasing the quotation marks in (3).

## References

Masaki Kashiwara and Pierre Schapira's [Microlocal study of sheaves](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §6.3, pp. 108–114, supplies the microlocal kernel and contact-transformation setting. Its Proposition 6.3.1 imposes properness of a selected microsupport projection; Proposition 6.3.3 proves composition under the corresponding regional hypotheses. Those statements do not by themselves prove the isolated-covector formal representability theorem used here. In particular, this lesson has not acquired a constructibility or global properness assumption by comparison with that source.

The exact programme inputs remain `SH02-MC-CUTOFF` for the refined incoming directional bound and `SH02-MC-DIRECT-GERMS` and `SH02-MC-DIRECT-REP` for isolated direct images and representability. Their complete provider texts and revision bindings are not included in this two-lesson download. The written nested-cone separation, bounded/unbounded witness argument, denominator comparisons, compatibilities and solved exercises are proofs under those stated inputs; a reader must supply those inputs to obtain a closed proof chain. The free monograph provides the comparison just described, not a substitute proof of the missing providers.

The lesson and solutions are independently written teaching. No human source text or figures are reproduced; the original AI expression is CC0. The source comparison does not certify the transitive prerequisites or the whole parent course.

# Pure and simple sheaves from directional tests

A constant sheaf on a submanifold can have a nonzero microlocal shift even when its ordinary stalk lies in degree zero. The normalization compares a local half-space test with three tangent Lagrangian planes. Once the test's Morse index is removed, the remaining coefficient complex is independent of the test function. Purity means that this normalized complex has one cohomological degree; simplicity also specifies its coefficient module.

Use Composing hypersurface kernels with their shifts and When a kernel quantizes a contact transformation. Throughout, $X$ is a finite-dimensional smooth real manifold, $n=\dim X$, and $k$ is a commutative ring of finite global dimension. Inputs are in $D^b(k_X)$; coefficient modules need not be finitely generated. We use the exact conormal coefficient-object model, bounded support triangles, and the microlocal half-space test identification stated below. Normal forms and the shift of a submanifold transform binds the exact written parameter Morse proof, and Local existence of contact kernel equivalences proves simultaneous normalization of finitely many smooth conic Lagrangians and transverse auxiliary planes by one hypersurface contact chart. The zero-covector conormal geometry and the conormal index calculation are proved below. The ordered index proof proves alternation, the radical formula, parity, the four-plane cocycle and constant-intersection continuity. The common-pair reduction proof proves the isotropic reduction used below.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

For simplicity and assertions that its coefficient or sheaf is nonzero, assume $1_k\ne0$. The coefficient-complex, index and transport identities still apply to the zero ring, where all coefficient complexes vanish; we make no simplicity or nonvanishing assertion in that degenerate case. This convention adds no field, finite-generation or perfectness hypothesis.

## The test function includes a covector and a transversality condition

Let $\Lambda\subset T^*X$ be a smooth conic Lagrangian near a point $p=(x_0;\xi_0)$. A smooth real function $\varphi$ is a transverse test at $p$ when

$$
\varphi(x_0)=0,\qquad d\varphi(x_0)=\xi_0,
\qquad \Lambda\pitchfork\Lambda_\varphi\text{ at }p,
\quad \Lambda_\varphi=\{(x;d\varphi(x))\}.
\tag{1}
$$

The graph $\Lambda_\varphi$ is Lagrangian but usually is not conic. If $\Lambda=T_M^*X$, the last condition says that $x_0$ is a nondegenerate critical point of $\varphi|_M$. Indeed, in coordinates $x=(a,b)$ with $M=\{b=0\}$, a tangent vector common to the graph and the conormal has $\delta b=0$ and $\delta\xi_a=0$. The graph condition then reads
$\operatorname{Hess}(\varphi|_M)\delta a=0$. The common tangent vanishes exactly when this Hessian is invertible.

Assume $\operatorname{SS}(F)\subset\Lambda$ on a cotangent neighborhood of $p$. Put

$$
C_\varphi(F)=\bigl(R\Gamma_{\{\varphi\geq0\}}F\bigr)_{x_0},
\qquad V=T_p\pi_X^{-1}(x_0),
\quad A=T_p\Lambda,
\quad B_\varphi=T_p\Lambda_\varphi,
\quad \tau_\varphi=\tau(V,A,B_\varphi).
\tag{2}
$$

The support is the **closed** side $\varphi\geq0$. The ordered index uses $\omega=d\theta$, as in the preceding lesson. The opposite side would change the local calculation.

We need a precise support-test prerequisite: for any bounded $F$, when $\varphi(x_0)=0$ and $d\varphi(x_0)=p\ne0$,

$$
C_\varphi(F)\simeq
\mu hom(k_{\{\varphi=0\}},F)_p,
\tag{3}
$$

with the positive covector $d\varphi(x_0)$, no additional shift, and compatibility with representatives and morphisms. Here is the exact derivation from the hypersurface microlocalization and stalk theorems `SH02-MH-SUBMANIFOLD` and `SH02-MIC-STALKS`.

Write $H=\{\varphi=0\}$ and use $h=\varphi$ as a normal coordinate near $x_0$. The stalk theorem computes $(\mu_HF)_p$ by local closed supports $Z$ whose normal cone at $x_0$ lies in the positive normal half-line, together with zero. Every such support germ is contained in $\{h\geq0\}$. Indeed, otherwise points $(a_j,h_j)\in Z$ would approach $x_0$ with $h_j<0$; in the normal deformation take positive parameters $t_j=-h_j$. Their normal coordinates $h_j/t_j=-1$ exhibit a negative vector in $C_H(Z)_{x_0}$, contrary to the strict pairing condition. Conversely the normal cone of $\{h\geq0\}$ is the nonnegative normal half-line. Thus this closed half-space is terminal among the allowed support germs. The natural support maps identify the stalk colimit with $(R\Gamma_{\{h\geq0\}}F)_{x_0}$ in every cohomological degree, hence as a bounded derived object. The submanifold-Hom theorem identifies $\mu hom(k_H,F)_p$ with $(\mu_HF)_p$, without an antipodal map or residual codimension shift. This proves (3) naturally for arbitrary bounded $F$. Smooth-Lagrangian containment and graph transversality are additionally needed for test independence, rather than for this comparison alone.

There is also a direct check that replacing $F$ by an isomorphic point-localized representative does not change (2). The cone of such a replacement has microsupport avoiding $p$. The defining microsupport vanishing test for the function $\varphi$ makes its local support complex zero. Applying the support functor therefore makes the replacement invertible. Thus the conormal coefficient-object model can be used in the calculation below.

## Conormal sheaves give the normalization explicitly

Suppose $\Lambda=T_M^*X$, let $\ell=\dim M$ and $c=n-\ell$. The local conormal model gives $F\simeq Q_M$ at $p$, for some $Q\in D^b(k)$. Choose coordinates and use the Morse lemma on $M$ to write

$$
\varphi|_M=|u|^2-|v|^2,
\qquad \dim v=m,\quad \dim u=\ell-m.
\tag{4}
$$

Local cohomology depends on this restriction, so

$$
C_\varphi(F)\simeq Q[-m].
\tag{5}
$$

Here is the local calculation, including its degree. On a sufficiently small ball in $M$, the support triangle is the relative-cohomology triangle for that ball and its open part $\{|u|^2<|v|^2\}$. When $m=0$, the open part is empty and the relative complex is $Q$. When $m>0$, decrease $u$ to zero and then radially normalize $v$; the open part has the homotopy type of $S^{m-1}$. A finite good cover, with the usual constant-coefficient acyclicity on its contractible intersections, computes its cohomology by the sphere's augmented cochain complex. The relative complex is its reduced cochain complex shifted by $[-1]$, namely $Q[-m]$. This construction retains the map from constants on the ball to constants on the open part. It works for a complex of arbitrary coefficient modules because the finite sphere complex consists of finite free modules; tensoring it with $Q$ retains the calculation. For $m=1$, the open part has two components: the diagonal map $Q\to Q\oplus Q$ has a cokernel $Q$, and the relative complex puts it in degree one. Coordinate orientation identifies the resulting rank-one negative-direction line locally; no global trivialization is assumed.

Now compute the index directly, including mixed tangential and normal derivatives of the test. Write its Hessian at the point in blocks $H_{aa},H_{ab},H_{ba},H_{bb}$, with $H_{ba}=H_{ab}^T$. In the ordered three planes take vectors

$$
(0,0;u,v)\in V,\qquad
(x,0;0,y)\in A,\qquad
(s,t;H_{aa}s+H_{ab}t,H_{ba}s+H_{bb}t)\in B_\varphi.
$$

For $\omega=d\xi\wedge dx$, the defining cyclic quadratic form of this triple is

$$
u^T(x-s)+(y-v)^Tt-x^TH_{aa}s-x^TH_{ab}t.
$$

Set $z=x-s$, $\widetilde u=u-H_{aa}s$, and
$\delta=y-v-H_{ba}(s+z)$. This is an invertible change of variables when $(s,z,t,v)$ are retained. The form becomes

$$
\widetilde u^Tz+\delta^Tt-s^TH_{aa}s.
$$

The first two terms are hyperbolic pairings of equal positive and negative dimensions. The free $v$ variables are radical. The signature is therefore $-\operatorname{sgn}H_{aa}$, where $H_{aa}=\operatorname{Hess}(\varphi|_M)$. Its $m$ negative and $\ell-m$ positive eigenvalues give

$$
\tau_\varphi=m-(\ell-m)=2m-\ell.
\tag{6}
$$

Consequently, whenever the displayed shift is integral,

$$
C_\varphi(F)[j+\tau_\varphi/2]
\simeq Q[j-\ell/2].
\tag{7}
$$

The right side contains no test function. This is the cancellation that the general definition must preserve: the local Morse group changes with the negative Hessian directions, while the inertia correction changes by exactly the compensating degree.

## A hypersurface contact kernel transports the corrected test

Let $\chi:T^*X\to T^*X'$ be a local contact transformation at the nonzero covector $p$, with $\dim X'=n$. Suppose its graph, using the antipodal input convention, is the conormal of a smooth hypersurface $S\subset X'\times X$. Set $K=k_S$, let $p'=\chi(p)$, and let $T(F)=\Phi_K(F)$ denote the corresponding localized transform. In $E=T_pT^*X$, set

$$
V'=\chi_*^{-1}\bigl(T_{p'}\pi_{X'}^{-1}(\pi_{X'}p')\bigr).
\tag{8}
$$

Choose a function $\varphi$ with $\varphi(x_0)=0$, $d\varphi(x_0)=p$, whose conormal hypersurface germ is carried to $T^*_{\{\psi=0\}}X'$, with $\psi(\pi_{X'}p')=0$ and $d\psi(\pi_{X'}p')=p'$. The comparison in this section holds for every bounded $F$; no smooth-Lagrangian microsupport assumption is required for it. For the later independence application, a simultaneous choice for the conic Lagrangian and both test-level conormals is proved in the linked local-existence lesson.

Let $A$ be any tangent Lagrangian plane under consideration, including $T_p\Lambda$. Use $\tau_\varphi=\tau(V,A,B_\varphi)$ and $\tau_\psi=\tau(V',A,B_\varphi)$, identifying tangent spaces by $\chi_*$. Here the latter index uses the transported graph-test plane. When $A=T_p\Lambda$ for a conic $\Lambda$, it equals the index of the actual target test $\psi$, as verified below. Choose $j$ with $j+\tau_\varphi/2\in\mathbb Z$. Then

$$
C_\varphi(F)[j+\tau_\varphi/2]
\simeq C_\psi(TF)[j+\tau_\psi/2+e],
\qquad e=\frac12(n-1)+\frac12\tau(V,A,V').
\tag{9}
$$

**Proof.** Write $H=\{\varphi=0\}$. Its conormal tangent $B_H$ contains the radial line $\rho$ through $p$. Homogeneity of $\chi$ gives $\rho\subset V\cap V'$, independently of $A$. The proved common-pair reduction, applied to this radial line contained in both vertical planes, shows
$\tau(V,B_\varphi,V')=\tau(V,B_H,V')$.
Indeed the reduction of $B_\varphi$ is the image of $B_\varphi\cap\rho^\perp$, exactly the reduction of the hypersurface conormal tangent. A tangent vector to the graph has base component tangent to $H$ precisely when it belongs to $\rho^\perp$. Conormalizing this base tangent and adjoining the radial direction gives the other plane. Both three-plane reductions meet the required pairwise-intersection condition through $V\cap V'$.

Hypersurface-kernel composition gives

$$
T(k_H)\simeq k_{\{\psi=0\}}[a],
\qquad a=1-\frac12\bigl[n+1+\tau(V,B_H,V')\bigr].
\tag{10}
$$

To obtain this particular composition, we need an endpoint that is a point. Here is a direct application of the submanifold transform with its hypotheses checked; the three-nonzero-endpoint hypersurface theorem alone would not supply it.

Put $W=S\subset X'\times X$, $N=S\cap(X'\times H)$, and $f=q_{X'}|_S:W\to X'$. Choose a defining function $h$ for $S$ with selected physical normal $(p',-p)$. Both $d_{X'}h$ and $d_Xh$ are nonzero. The first makes $dh$ and $d\varphi$, lifted from $X$, independent: a linear relation first has zero $X'$-component and therefore zero coefficient of $dh$, then zero coefficient of $d\varphi$. Hence $N$ is a smooth closed hypersurface in $W$. The second makes $f$ a submersion, since its nonzero $X$-derivative can solve the tangent equation for any prescribed $X'$-tangent vector.

The covector $\nu=f^*p'$ on $W$ is nonzero because $f$ is a submersion. Modulo the normal line of $W$, $(p',0)$ equals $(0,p)$, so $\nu$ is the selected conormal of $N$. Its conormal image is $T^*_{\{\psi=0\}}X'$ by the assumed contact image of $T_H^*X$.

For transversality, compose the contact graph with $T_H^*X$. The graph projection to $T^*X$ is a local diffeomorphism, so its derivative and the derivative of that conormal inclusion are transverse. The general tangent-composition proof applies with the last endpoint symplectic space equal to zero; it does not require a nonzero covector there. Its matching kernel is zero: a vector with zero output must have zero input by the graph isomorphism. The diagonal restriction and subsequent zero-middle-covector restriction therefore have no remaining middle tangent direction. Quotienting the normal line of $W$ gives precisely the transverse intersection of $T_N^*W$ with the target cotangent pullback required by the submanifold transform. Thus there are no null or excess directions.

We spell out the ordered index, too. Before quotienting the normal of $W$, lift the triple from $T^*W$ to the ambient cotangent tangent space. That normal line lies in the vertical plane and the lifted conormal plane, so the common-pair reduction preserves its index. Lift next through the middle diagonal to
$E_{X'}\oplus E_X^a\oplus E_X$, where the planes in order are
$$
V_{X'}\oplus V^a\oplus V,\qquad
 \lambda_S\oplus B_H,\qquad
 V_{X'}\oplus\Delta_X.
 \tag{E1}
$$
These are two comparisons of the same lifted triple (E1). Reducing its middle diagonal normal, which is common to the first and third planes, recovers the triple before that lift; the preceding reduction of the normal of $W$ identifies this index with $\tau_W$. To compute the same index in another way, return to (E1) and instead reduce only the endpoint vertical $V_{X'}$, again common to its first and third planes. The graph carries this endpoint vertical to $V'$. This alternative reduction leaves the triple
$$
(\,V^a\oplus V,\ (V')^a\oplus B_H,\ \Delta_X\,).
 \tag{E2}
$$
The same diagonal identity as in the ordered hypersurface-composition proof gives
$\tau_W=\tau(V,V,B_H,V')=\tau(V,B_H,V')$; the triangle index with repeated $V$ is zero. The point endpoint contributes the zero symplectic space and no index term. Thus the order is exactly the one in (10).

Here $\dim W=2n-1$ and the target hypersurface has dimension $n-1$. The transverse submanifold-transform formula consequently gives
$$
a=\frac{1+(n-1)-(2n-1)-\tau_W}{2}
   =\frac{1-n-\tau(V,B_H,V')}{2}.
 \tag{E3}
$$
This is the exponent in (10). Local coordinate orientations give the same normalized constant coefficient; no global orientation trivialization is asserted.

Finally identify the functor, not just this exponent. On a small ambient product neighborhood, stalkwise flatness of the constant closed-support sheaf gives
$k_S\otimes^L q_X^{-1}k_H=k_N$.
The closed-embedding projection formula therefore identifies its proper-support image with $Rf_!k_N$, with the neighborhood restriction retained. Product neighborhoods and their intersections with $W$ give bases for these local images. The contact graph isolates the chosen middle covector. The refined cutoff and formal-comparison theorem for [composition at prescribed covectors](microlocal-composition-at-prescribed-covectors.html) identifies the represented formal system of these images with the localized transform $T(k_H)$, after tensor and direct image. This uses the selected local graph's admissibility; it neither assumes global properness of $f$ nor substitutes ordinary base restrictions for all microlocal denominators. The submanifold-transform comparison now proves (10) as an isomorphism in the stated output germ category.


Contact transport of microlocal Hom, with both its arguments transported, and (3) therefore give
$C_\varphi(F)\simeq C_\psi(TF)[-a]$.
The negative sign is forced by shifting the **first** Hom argument by $[a]$. To compare with (9), the remaining degree is

$$
2e=\tau(V,A,B_\varphi)-2a-\tau(V',A,B_\varphi).
\tag{11}
$$

Substitute (10) and apply the four-plane cocycle identity in the order $(V,A,B_\varphi,V')$. Its index terms give
$\tau(V,A,V')+\tau(V,B_H,V')-\tau(V,B_\varphi,V')$.
The last two terms cancel by the common-line reduction just proved. The dimension term is $n-1$, proving (9) for an arbitrary $A$.

For the application $A=T_p\Lambda$, conicity supplies the additional containment $\rho\subset A$. Thus reduction through $V\cap A$ also gives $\tau(V,A,B_\varphi)=\tau(V,A,B_H)$. After transport, reduction through the target radial line gives equality of the indices for the transported $B_\varphi$, the target level-hypersurface conormal tangent, and the actual graph-test tangent $B_\psi$. This verifies the promised interpretation of $\tau_\psi$ for the type calculation. We did not require the arbitrary plane in the lemma to contain the radial line. Every index order and the Hom-argument shift have now been fixed. $\square$

For reference, graph-test transversality can also be read on the level hypersurface. At a nonzero covector the intersection of its conormal tangent with $A$ is just $\rho$ exactly when $B_\varphi\cap A=0$. This follows by reducing both statements by the same radial line. It is what permits the hypersurface calculation in (10) for transverse tests.

## A smooth conic Lagrangian at the zero covector is conormal

Suppose a smooth conic Lagrangian germ $\Lambda\subset T^*X$ contains $(x_0,0)$. Then $\Lambda$ is the conormal of an embedded base submanifold germ near that point, including its zero covectors.

**Proof.** Identify the tangent space at a zero covector with $T_{x_0}X\oplus T_{x_0}^*X$. Its Lagrangian plane $A$ is invariant under every positive fibre dilation $(v,\eta)\mapsto(v,t\eta)$. If $(v,\eta)\in A$, subtract its image under any fixed $t\ne1$: both $(0,\eta)$ and $(v,0)$ belong to $A$. Thus $A=P\oplus Q$, with $P\subset T_{x_0}X$ and $Q\subset T_{x_0}^*X$. Isotropy gives $Q\subset P^\perp$; dimension $n$ gives equality. Choose base coordinates $x=(a,b)$ with $P=\{b=0\}$, and dual coordinates $(\alpha,\beta)$. The tangent plane is $\{\delta b=\delta\alpha=0\}$.

Projection to $(a,\beta)$ has invertible derivative on $\Lambda$. After shrinking, the inverse function theorem therefore writes the actual germ as

$$
b=g(a,\beta),\qquad \alpha=h(a,\beta).
$$

Fibre dilation and uniqueness of this graph imply, for $0<t\leq1$ in a common small chart,

$$
g(a,t\beta)=g(a,\beta),\qquad
h(a,t\beta)=t\,h(a,\beta).
$$

Letting $t\to0$ gives $g(a,\beta)=g(a,0)=g_0(a)$ and $h(a,0)=0$. Dividing the second equality by $t$ and differentiating at zero gives $h(a,\beta)=d_\beta h(a,0)\beta$; smoothness at the zero fibre is essential here. Let $M=\{b=g_0(a)\}$.

The radial vector is tangent to $\Lambda$. Since $\Lambda$ is isotropic, its canonical form $\theta=\iota_R\omega$ vanishes on every tangent vector, including at the zero fibre. Evaluating on the graph's $a$-directions gives

$$
h(a,\beta)+dg_0(a)^T\beta=0.
$$

Consequently $\Lambda$ has exactly the equations
$b=g_0(a)$, $\alpha=-dg_0(a)^T\beta$, with free small $(a,\beta)$. These are the conormal equations for $M$. The equality includes the local zero covectors. The cases $P=0$ and $P=T_{x_0}X$ give a cotangent-fibre germ and the zero-section germ, respectively. No global projection image or global conormal equality is asserted. $\square$

## Independence of the transverse test

Let $r=\dim(V\cap T_p\Lambda)$. If

$$
j-\frac12(n+r)\in\mathbb Z,
\tag{12}
$$

then the isomorphism class of $C_\varphi(F)[j+\tau_\varphi/2]$ is independent of the transverse test $\varphi$.

**Proof.** The conormal case is (7). At a nonzero $p$, apply the proved simultaneous normalization to the three conic Lagrangian germs: $\Lambda$ and the positive conormals of the two prescribed test level hypersurfaces. It gives a single hypersurface contact kernel carrying all three to hypersurface conormal germs. The reduced radial-intersection criterion in that proof makes both transformed tests transverse. Apply (9) to the two tests. Its extra term $e$ depends on $V,A,V'$, not on the test. The transformed corrected complexes agree by the conormal calculation (7), hence so do the original ones.

At a zero covector, the preceding smooth-conic proof makes $\Lambda$ a conormal germ. Use (7) directly. The base submanifold can have any codimension; its conormal need not be the zero section.

Finally, the parity rule for three Lagrangian planes says
$\tau_\varphi\equiv n+r\pmod{2}$, because $B_\varphi$ is transverse to both $V$ and $A$. Equation (12) makes $j+\tau_\varphi/2$ an integer. We have compared actual complexes with integral cohomological shifts. The conclusion is an isomorphism class, rather than a preferred orientation-free identification between all tests. $\square$

## Type, purity and simplicity

Choose a number $d$ satisfying

$$
d\equiv \frac12\dim(V\cap T_p\Lambda)\pmod{\mathbb Z}.
\tag{13}
$$

We say that $F$ has **type $L$ with shift $d$** at $p$ along $\Lambda$ when

$$
C_\varphi(F)\bigl[-d+n/2+\tau_\varphi/2\bigr]\simeq L
\quad\text{in }D^b(k).
\tag{14}
$$

The exponent in (14) is an integer by (13) and the parity rule. Test independence makes the definition unambiguous. Although $d$ may be a half-integer, (14) does not introduce a half-integer shift functor on complexes.

The sheaf is **pure** at $p$ if this type can be chosen concentrated in degree zero. It is **simple** there if, additionally, its type is a free $k$-module of rank one. The condition is about $k$, rather than a field chosen later. Pure coefficients can have torsion and arbitrary rank. A zero coefficient complex is permitted by the definition of type and purity; simplicity excludes it.

There are two useful shift rules. If $F$ has type $L$ with shift $d$, then

$$
F\text{ has type }L[-b]\text{ with shift }d+b,
\qquad F[b]\text{ has type }L\text{ with shift }d+b
\quad(b\in\mathbb Z).
\tag{15}
$$

Both follow by substituting into (14). In particular one must specify the shift when naming a type complex; transferring an integer between $d$ and $L$ changes its displayed degree.

For the conormal model $F=Q_M[s]$, equations (5)–(6) give

$$
\text{type at shift }d=Q[s+c/2-d].
\tag{16}
$$

Thus $k_M$ is simple with shift $c/2$. More generally $Q_M[s]$ has type $Q$ with shift $s+c/2$. This remains true for a zero conormal covector when the stated local conormal assumptions hold.

For a smooth boundary $h=0$ at its positive covector $dh$, the closed upper-side sheaf $k_{\{h\geq0\}}$ is isomorphic in the point-localized category to $k_{\{h=0\}}$. The boundary triangle gives
$k_{\{h\geq0\}}\simeq k_{\{h<0\}}[1]$ there: the whole constant sheaf in that triangle is null at a nonzero covector. Therefore the closed upper side is simple with shift $1/2$, while the open lower side is simple with shift $-1/2$. They refer to the same positive boundary covector, despite lying on opposite sides in the base.

## Contact transport changes the shift by a specified index

Under the hypersurface contact kernel of (8), if $F$ has type $L$ with shift $d$, then $TF$ has the same type with shift

$$
d'=d-\frac12(n-1)-\frac12\tau(V,T_p\Lambda,V').
\tag{17}
$$

**Proof.** Select a transverse test allowed in (9). Substitute $j=-d+n/2$. Its left side is $L$ by (14), while its right side has exponent
$-d+n/2+\tau_\psi/2+e=-d'+n/2+\tau_\psi/2$.
That is precisely (14) for $TF$ with shift $d'$. Independence of the test proves the conclusion for every allowed transverse test. The transported test exponent is integral, so (17) has the required shift parity for the transformed tangent conormal rank. $\square$

This statement concerns the unshifted hypersurface kernel $k_S$. Shifting the kernel by $[b]$ adds $b$ to the transform's shift by (15). Nor can the three-plane index be dropped solely because the contact transformation is a local diffeomorphism: the two vertical planes generally differ.

## The coefficient type is locally constant up to integer shift

Suppose $\operatorname{SS}(F)\cap U\subset\Lambda$ on an open cotangent region $U$. Fix $L\in D^b(k)$, and allow the shift in its type to vary. Then

$$
\{p\in\Lambda\cap U:F\text{ is of type }L
\text{ with some allowed shift at }p\}
\tag{18}
$$

is open and closed in $\Lambda\cap U$.

**Proof.** Work near any chosen point. A local hypersurface contact normal form takes $\Lambda$ to a conormal. The transformed sheaf has the coefficient model $Q_M$ at the selected point. An isomorphism in a point-localized category is represented by a finite collection of denominator arrows. Each cone avoids that point; after shrinking a cotangent neighborhood, each cone avoids the entire neighborhood. Thus the same model holds on that neighborhood. Near a zero covector use the ordinary local conormal model directly.

In the conormal chart, (16) says that the possible type complexes are exactly the integer shifts of the fixed $Q$. Membership in the set (18) is therefore constant throughout the chart. Formula (17) preserves the coefficient type while adjusting the allowed shift; its inverse gives the converse implication. Every point consequently has a neighborhood wholly in (18) or wholly in its complement. Both sets are open, proving the assertion. This does not say that a numerical shift is constant across a varying projection rank. $\square$

Locally there is also a useful object decomposition. If $F$ has type $L$, choose a simple object $G$ at the point so that

$$
F\simeq L_X\otimes^L G
\quad\text{in }D^b(k_X;p).
\tag{19}
$$

To construct it, take the conormal chart just used. Its coefficient model for $F$ is $Q_M$; if its normalized type is $L$, (16) identifies $Q$ with an integral shift of $L$. Take the correspondingly shifted $k_M$ and carry it back by the inverse contact kernel. It is simple by (17). The constant-coefficient projection formula makes the inverse transform commute with tensoring by the arbitrary bounded $L$, yielding (19). No choice of a global simple generator, preferred orientation line or full categorical equivalence of coefficient morphisms is asserted by this local object construction.

## Exercises with complete solutions

### Two transverse tests of the same plane

*Difficulty: Introductory.*

Let $M$ be two-dimensional in a three-dimensional $X$, and let $F=k_M$. A test restricts to $a_1^2+a_2^2$ on $M$; another restricts to $a_1^2-a_2^2$. Compute their raw complexes, indices and normalized types at shift $d=1/2$.

**Solution.** The negative dimensions are zero and one. The raw complexes are $k$ and $k[-1]$. Formula (6) gives indices $-2$ and zero. The exponent in (14) is respectively $-1/2+3/2-1=0$ and $-1/2+3/2=1$. Both normalized types are $k$. Omitting the inertia term would give two different degrees for the same conormal sheaf.

### A half-integer is not a shift functor

*Difficulty: Introductory.*

At a point with $n=4$ and $\dim(V\cap T_p\Lambda)=1$, an allowed shift is $d=3/2$. Which parity must $\tau_\varphi$ have, and why is the exponent of (14) integral?

**Solution.** Its parity is $n+1=5$, hence it is odd. The exponent is $-3/2+2+\tau_\varphi/2=(1+\tau_\varphi)/2$, an integer. Only this exponent acts on the complex. The number $d$ is part of the geometric normalization.

### Purity over an integral coefficient ring

*Difficulty: Intermediate.*

Take $k=\mathbb Z$, a codimension-two submanifold $M$, and $F=(\mathbb Z/2)_M$. Is $F$ pure or simple? What about $\mathbb Z_M\oplus\mathbb Z_M[1]$?

**Solution.** Formula (16) gives type $\mathbb Z/2$ with shift one, so the first sheaf is pure. Its type is not a free rank-one $\mathbb Z$-module, so it is not simple; moving to a residue field would change the coefficient problem. The second sheaf has two nonzero normalized cohomology degrees for every allowed integral change of shift. It is not pure.

### Keep the kernel's own degree

*Difficulty: Intermediate.*

Suppose $n=3$, the ordered index in (17) is zero, and $F$ is simple with shift $d=2$. Find the shift of its transform by $k_S$, and then by $k_S[2]$.

**Solution.** The unshifted kernel gives $d'=2-(3-1)/2=1$. Shifting the kernel by two shifts the entire transform by two, so its shift becomes three. The coefficient type remains $k$ in both cases.

### The two sides at one positive covector

*Difficulty: Intermediate.*

At $(0;dx)$ on $\mathbb R$, compare the simple shifts of $k_{[0,\infty)}$, $k_{\{0\}}$ and $k_{(-\infty,0)}$. Explain the degree in their localized relation.

**Solution.** The point sheaf and the closed positive half-line have shift $1/2$. The open negative half-line has shift $-1/2$. The triangle $k_{(-\infty,0)}\to k_\mathbb R\to k_{[0,\infty)}\xrightarrow{+1}$ has null middle term at the positive covector, hence $k_{[0,\infty)}\simeq k_{(-\infty,0)}[1]$. The difference of their simple shifts is exactly one. The open positive half-line instead is null at that covector and is not the object used here.

### An object model does not compute every morphism

*Difficulty: Advanced.*

Does (19) alone prove that $A\mapsto A_X\otimes^L G$ is fully faithful from $D^b(k)$ to $D^b(k_X;p)$? Specify the additional comparison needed.

**Solution.** No. An object decomposition supplies no computation of arbitrary derived morphisms between its coefficient factors. Full faithfulness requires the natural isomorphisms $\operatorname{Hom}_{D^b(k)}(A,B[j])\simeq\operatorname{Hom}_{D^b(k_X;p)}(A_X\otimes^L G,B_X\otimes^L G[j])$ for all bounded $A,B$ and all integers $j$, compatible with identity and composition. Neither the existence of $G$ nor (19) states these comparisons. The coefficient-equivalence lesson treats that morphism normalization as an explicit separate prerequisite.

### A test must meet the chosen covector

*Difficulty: Advanced.*

For the conormal of $M=\{b=0\}\subset\mathbb R_a\times\mathbb R_b$, fix $p=(0;db)$. Compare $\varphi=b+a^2$, $\psi=b-a^2$, and $h=b$. Which are transverse tests, and what fails for $h$?

**Solution.** All three vanish at zero and have differential $db$. The restrictions of the first two to $M$ have nonzero Hessians, so both are transverse. Their raw complexes are $k$ and $k[-1]$, and their indices are $-1$ and one. At simple shift $1/2$ their corrected types are both $k$. The restriction of $h$ is identically zero; its Hessian is zero, the graph and conormal tangents have a common nonzero $a$-direction, and the transversality in (1) fails. Matching only the value and differential is insufficient.

### Zero covectors retain a curved base submanifold

*Difficulty: Intermediate.*

On $T^*\mathbb R^2$, with coordinates $(a,b;\alpha,\beta)$, inspect
$\Lambda=\{b=a^2,\ \alpha=-2a\beta\}$.
Verify smoothness, conicity and the Lagrangian property, identify its zero-fibre base germ, and compare with the positive half of a cotangent fibre at its zero endpoint.

**Solution.** The free coordinates $(a,\beta)$ parameterize $\Lambda$; projection to them is its smooth inverse, so the image is an embedded two-dimensional manifold. Positive covector dilation multiplies both $\alpha$ and $\beta$ and preserves its equations. Its canonical form pulls back to
$(-2a\beta)\,da+\beta\,d(a^2)=0$.
Its symplectic form therefore vanishes, and its dimension is half the ambient dimension, so it is Lagrangian. Its zero covectors are exactly those with $\beta=\alpha=0$, over the parabola $M=\{b=a^2\}$; the full equations are $T_M^*\mathbb R^2$. The zero-covector theorem keeps this curved base rather than replacing it by a point or the entire zero section. By contrast $\{x=0,\xi\geq0\}\subset T^*\mathbb R$ has a boundary at its zero endpoint. It is not a smooth submanifold without boundary there, so it does not satisfy the theorem's hypothesis and cannot be used to infer a full two-sided conormal germ.

## References

Masaki Kashiwara and Pierre Schapira's [Microlocal study of sheaves](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §7.2, Lemmas 7.2.2–7.2.4, Definition 7.2.5 and Examples 7.2.6, pp. 123–128, supplies the closed-support Morse calculation, ordered degree correction and pure/simple module conventions. The full comparison includes the positive closed half-line shift and the negative open half-line shift. Lemma 7.2.4 is a statement about the corrected cohomology modules. The bounded coefficient-object isomorphisms and contact-transport argument written in this lesson use the stronger programme inputs stated above; the comparison with that lemma does not independently prove those inputs.

Pierre Schapira's [A short review on microlocal sheaf theory](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf), dated 19 January 2016, §5.2, pp. 26–27, provides a qualitative comparison of purity and simplicity. Its proof references and discussion of the Maslov shift refer elsewhere. It is not used here as a complete proof of numerical normalization, the conormal coefficient-object model or contact equivalence.

This download contains the comparisons and solved examples written above, including the zero-covector conormal geometry, but not the complete preceding programme providers. Those dependencies include the conormal coefficient-object model, `SH02-MH-SUBMANIFOLD`, `SH02-MIC-STALKS`, the parameter Morse and submanifold-transform proofs, simultaneous contact normalization, and the ordered-index and common-pair reduction proofs. Their exact revision bindings remain to be supplied before claiming a closed proof chain. Arbitrary bounded coefficients, zero covectors and the stated nonzero-ring qualification on simplicity are retained.

The lesson and solutions are independently written teaching. No human source text or figures are reproduced; the original AI expression is CC0. The source comparison does not certify the transitive prerequisites or the whole parent course.