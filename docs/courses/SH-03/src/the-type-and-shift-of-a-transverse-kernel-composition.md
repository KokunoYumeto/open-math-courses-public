# The type and shift of a transverse kernel composition

A kernel need not be a constant sheaf on a submanifold. Its microsupport can be a smooth Lagrangian with a singular projection, and its coefficient type can be an arbitrary bounded complex. Transverse composition still has a precise answer: tensor the coefficient types and subtract a correction determined by the middle dimension and three ordered Lagrangian planes.

Use Microlocal composition at prescribed covectors, Composing hypersurface kernels with their shifts, Pure and simple sheaves from directional tests, and How simple sheaf shifts change along a Lagrangian. Coefficients are over a commutative ring \(k\) of finite global dimension. All sheaf and coefficient complexes are bounded; no finite-rank, perfect-coefficient or constructibility assumption is imposed on the two input kernels.

The geometric inputs are the linear relation/index identities and the local contact normal forms stated below. The sheaf inputs are the refined incoming cutoff, boundary-controlled isolated image, ordinary tensor/projection formula and proper-support Fubini from the preceding kernel lessons. Their hypotheses remain in force throughout the proof.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-check recorded; not independently reviewed. New original text is public domain (CC0).*

## The ordered middle index

Let \(X,Y,Z\) be smooth real manifolds, and choose \(p_X,p_Y,p_Z\), allowing zero covectors. Suppose

\[
\Lambda_1\subset T^*(X\times Y),\qquad
\Lambda_2\subset T^*(Y\times Z)
\qquad\text{(1)}
\]

are smooth conic Lagrangian germs through \((p_X,p_Y^a)\) and \((p_Y,p_Z^a)\). The antipode \(a\) negates the covector. Require their twisted middle projections \(p_2^a\) and \(p_1\) to be transverse. The tangent proof in the hypersurface-composition lesson applies to these arbitrary Lagrangians: the matching tangent space has dimension \(\dim X+\dim Z\), its endpoint projection has zero kernel, and its middle symplectic terms cancel. It therefore embeds locally as a Lagrangian germ \(\Lambda=\Lambda_1\circ\Lambda_2\).

Write \(E_W=T_{p_W}T^*W\), with vertical plane \(V_W\), and identify the physical input tangent spaces with
\(\lambda_1\subset E_X\oplus E_Y^a\) and
\(\lambda_2\subset E_Y\oplus E_Z^a\).
Propagate the endpoint verticals into the middle space:

\[
\begin{split}
\alpha_1&=\{v:\text{there is }u\in V_X
                         \text{ with }(u,v)\in\lambda_1\},\\
\alpha_2&=\{v:\text{there is }w\in V_Z
                         \text{ with }(v,w)\in\lambda_2\}.
\end{split}
\qquad\text{(2)}
\]

Linear Lagrangian relations make these Lagrangian planes even when the propagation has excess. Use the middle form \(\omega_Y=d\theta_Y\) and set

\[
r(\lambda_1,\lambda_2)=\tau_{E_Y}(V_Y,\alpha_2,\alpha_1),
\qquad
c(\lambda_1,\lambda_2)=\frac{\dim Y+r(\lambda_1,\lambda_2)}2.
\qquad\text{(3)}
\]

The order is vertical, second propagated plane, first propagated plane. The superscript on \(E_Y^a\) changes its symplectic form; it does not authorize changing this order.

Suppose \(K_i\) has microsupport contained in \(\Lambda_i\) near its selected physical point and is of type \(L_i\) with shift \(d_i\), for \(i=1,2\). Then the two germs are microlocally composable and

\[
\begin{split}
\operatorname{SS}(K_1\circ_\mu K_2)&\subset\Lambda,\\
\text{type}(K_1\circ_\mu K_2)&=L_1\otimes_k^L L_2,\\
D&=d_1+d_2-c(\lambda_1,\lambda_2).
\end{split}
\qquad\text{(4)}
\]

All conclusions concern germs near \((p_X,p_Z^a)\). Transversality isolates the chosen middle point because endpoint projection is a local embedding. The represented formal composition and its confined microsupport estimate follow from the earlier isolated-composition theorem. This supplies the bounded output needed for the type argument. A distant middle branch or a global nonproper convolution is not included in (4).

The number \(D\) is a geometric normalized shift. Every exponent applied to a complex in its test definition is integral. The proof below also verifies its allowed parity.

## Reassociation when a contact graph is present

We need actual comparison maps when contact kernels are inserted into (4). Work at nonzero selected covectors for now. A **contact graph kernel** here means a selected germ with microsupport in the graph of a local homogeneous symplectic isomorphism, represented on paired cotangent regions by a kernel satisfying the contact-operator admissibility conditions. The local simple graph kernels and their normalized inverses constructed earlier have these properties.

Consider a finite word of kernels with such graph kernels inserted before, after or between a transverse pair of arbitrary kernels. Assume the remaining pair is transverse after the graph coordinates have been transported. Eliminating each graph determines its matched covector uniquely. Endpoint projection of the remaining matching relation is locally injective. Thus fixing the outer endpoints isolates **all** intermediate covectors in this word. The ordinary tensor/Fubini map induces the natural regroupings of its microlocal germ composition, and neighboring inverse graph kernels cancel by their actual diagonal identities.

Here is the formal comparison proof. It explains the cutoff conditions needed to descend those ordinary maps.

Choose representatives of the graph kernels on their paired regions. Over a compact, sufficiently small output cotangent neighborhood, their selected graph projections are proper. Moreover, on a closed angular subregion, homogeneity and nonvanishing of both projections bound the ratio of the two covector norms above and below. A graph sector consequently cannot contribute an unbounded intermediate covector with its other covector bounded. Contributions outside that sector are removed by the graph operator's selected-region comparison; the comparison cone has no retained output incidence.

For the arbitrary transverse pair, use the refined incoming replacement from the prescribed-covector lesson. It isolates the entire middle fibre at the fixed bases and excludes nonzero middle cancellation with both endpoint covectors zero. Apply it against the finite union of the conic sets occurring in the two proposed parenthesizations and in their denominator cones. If a contact graph is between the pair, transport these sets through its graph first. Transport preserves closed selected sectors, homogeneity and their finite unions; its proper graph comparison represents precisely this transport. The same refined cutoff therefore applies in the transported coordinates.

A joint matching sequence with fixed outer endpoints now has bounded intermediate covectors. Here are the three placements of one graph in a triple. If the first kernel is the graph, its norm bound controls the first intermediate covector from the fixed output. The second pair's whole-fibre cutoff and exclusion of cancellation with both endpoint covectors zero then bound its remaining middle covector: an unbounded sequence, divided by its norm, would give that forbidden cancellation. If the graph is in the middle, take the stronger first-kernel replacement available at a nonzero output covector: its microsupport has no covector of the form \((0,v)\) with \(v\ne0\) over the fixed bases. Apply it against the graph-transported second conic set. An unbounded first intermediate covector would contradict this exclusion after normalization; the graph's norm bound controls the second intermediate covector. If the graph is last, use that same stronger first replacement, while the graph's inverse norm bound controls the second intermediate covector from the fixed input. All selected covectors in this argument are nonzero, as ensured by the later stabilization.

Closedness confines every bounded limiting witness to the unique selected tuple. These exclusions persist on a smaller base neighborhood: otherwise a sequence approaching the fixed bases, normalized in its unbounded intermediate covector, supplies the same forbidden limiting direction. For longer words, graph bounds control each consecutive graph segment and the retained transverse-pair cutoff controls the remaining intermediate direction. The same argument applies to comparison cones; at the unique retained tuple a denominator cone has no microsupport, so its image comparison has no retained output incidence.

These are exactly the whole-fibre, infinity and comparison conditions of the boundary-controlled isolated-image construction. Apply it to the joint tensor on the product of the base manifolds, with all intermediate base variables retained. Product neighborhoods give a basis, and proper confined representatives exclude boundary witnesses. Each iterated parenthesization identifies with this joint formal system. This identification occurs after the tensor and image comparisons; base restrictions have not been assumed cofinal among all incoming microlocal denominators.

For example, three kernels give the common ordinary terms

\[
Rq_{14!}\bigl(q_{12}^{-1}A'\otimes^L
                  q_{23}^{-1}B'\otimes^L
                  q_{34}^{-1}C'\bigr),
\qquad\text{(5)}
\]

indexed jointly by incoming denominators and intermediate neighborhoods. Their tensor and \(!\)-Fubini maps commute with every refinement. To verify equality of the formal systems, test against any output germ \(T\). An arrow into \(T\) uses finitely many representatives, which admit the common cutoff just constructed. Equality of two such arrows is likewise checked after a further common refinement. Thus the iterated filtered colimits of morphisms are the same colimit over the joint choices. Representability turns the resulting pro-object comparison into a natural isomorphism of bounded germs. For longer finite words repeat this argument with their finite collection of comparison cones.

For inverse graph neighbors, the map in this joint system restricts to their actual kernel identity \(G\circ_\mu F\simeq k_\Delta\). The graph bounds and isolated comparison make convolution with that map invertible on the remaining selected germs. The diagonal projection formula then removes \(k_\Delta\). Ordinary coherence and unit equalities hold in every common term and hence survive passage to represented germs.

This proof uses the extra graph properness and transported-cutoff conditions. The earlier source associativity statement with an isolated entire matching germ retains its own stronger hypothesis. In particular, a nonzero tuple can be scaled and is not an isolated point of the entire conic matching set. We have established the graph regroupings used here by their separate comparison argument.

## Reassociation for a transverse three-kernel chain

There is also a sufficient transverse-chain case without a graph factor. Continue at nonzero selected covectors, as will be ensured by the stabilization in this proof. Let the successive tangent relations be \(\lambda_1,\lambda_2,\lambda_3\), from \(W\) through \(Z,Y\) to \(X\). Require \((\lambda_1,\lambda_2)\) transverse over \(E_Y\), \((\lambda_2,\lambda_3)\) transverse over \(E_Z\), and \((\lambda_1\circ\lambda_2,\lambda_3)\) transverse over \(E_Z\).

The other composite pair is then transverse too. Indeed form the linear map from \(\lambda_1\oplus\lambda_2\oplus\lambda_3\) to \(E_Y\oplus E_Z\) recording the two differences of matched middle vectors. Eliminating the first equality identifies its kernel with the matching tangent of \(\lambda_1\circ\lambda_2\) together with \(\lambda_3\); the first and third transversality assumptions make the joint map surjective. Eliminate the second equality instead. The second assumption makes that first elimination surjective, and joint surjectivity implies the required remaining surjectivity for \((\lambda_1,\lambda_2\circ\lambda_3)\). Both parenthesized relations consequently identify with the same joint matching tangent and its endpoint image. Its endpoint kernel is zero by either successive transverse-composition calculation. At the nonlinear germs, the implicit-function and local-embedding arguments give the same unique joint matching tuple over fixed outer endpoints.

To descend ordinary reassociation, first make an incoming replacement of the second kernel against the third. Because its selected output covector \(p_Y\) is nonzero, the stronger refined cutoff excludes every covector \((0,v_Z)\), \(v_Z\ne0\), at the fixed second-kernel bases. It also supplies whole-middle-fibre isolation for that pair. Choose its boundary-controlled representative of the composite, with witnesses confined to the selected middle neighborhood. Now refine the first kernel against the finite union of the second kernel, the just-chosen composite and the comparison cones in question. Its nonzero selected output \(p_X\) supplies the analogous exclusion of \((0,v_Y)\), \(v_Y\ne0\). The two composite-pair transversality statements justify the local isolations used by these cutoffs. The latter first cutoff confines the first matched covector, and the former second cutoff then confines the second one. This is a sequential choice; it does not require alternating an infinite sequence of cutoffs.

For completeness, any unbounded sequence of first middle covectors, with the outer output fixed, normalizes to the first forbidden pure middle covector. Once those covectors are bounded, an unbounded sequence of second middle covectors normalizes to the second forbidden pure middle covector. The exclusions at the fixed bases persist after shrinking by the same closedness and unit-direction compactness argument. Thus the joint matching fibre is bounded. The whole-fibre cutoffs, including the first cutoff against the confined second composite, and the adjacent-pair isolation now reduce its bounded witnesses to the unique selected tuple. A joint tensor cancellation with zero outer covectors first forces the \(Y\)-covector to vanish by the first exclusion, and then the \(Z\)-covector to vanish by the second; hence the ordinary joint tensor is noncharacteristic on a smaller base neighborhood.

Apply the isolated-image construction to that joint tensor. If any term is changed by an incoming denominator, its cone has no microsupport at its selected physical pair, so the confined joint comparison has no output incidence. For any finite collection of terms, repeat the sequential choices against the finite union of their conic comparison sets; this provides a common refinement. The two parenthesizations therefore identify with the same formal system (5). Its ordinary tensor/Fubini map is compatible with all transitions. The morphism-colimit argument following (5) makes it a natural isomorphism of represented germs, with its ordinary coherence maps. No whole-matching singleton has been assumed; the argument uses the stated transverse-chain geometry and two explicit no-infinity cutoffs.

This supplies the three-kernel supporting argument used after the nonzero stabilization, including the case of a graph among the factors. The earlier statement under the literal isolated-entire-matching condition is preserved separately.

## The two index identities needed by the proof

We use two precise linear identities. For three successively composable Lagrangian relations, with the indicated transverse composites, the relation index satisfies

\[
r(\lambda_1,\lambda_2)+r(\lambda_1\circ\lambda_2,\lambda_3)
=r(\lambda_1,\lambda_2\circ\lambda_3)+r(\lambda_2,\lambda_3).
\qquad\text{(6)}
\]

The two middle dimensions on each side are the same, so the cost \(c\) in (3) satisfies the same equality. This is the exact linear relation identity, independent of sheaf associativity. When the graph regrouping just proved applies, validity of the type formula for any three of the four pairs in (6) proves it for the fourth: expand both total degrees, use (6), and use associativity of the derived coefficient tensor.

For continuous relations choose Lagrangian planes \(\mu_X,\mu_Y,\mu_Z\) transverse to the verticals, such that their product planes are transverse to \(\lambda_1,\lambda_2,\lambda_1\circ\lambda_2\), respectively. These simultaneous generic complement choices are a local geometric input. Put

\[
\begin{split}
t_1&=\tau(V_X\oplus V_Y^a,\lambda_1,\mu_X\oplus\mu_Y^a),\\
t_2&=\tau(V_Y\oplus V_Z^a,\lambda_2,\mu_Y\oplus\mu_Z^a),\\
t&=\tau(V_X\oplus V_Z^a,\lambda_1\circ\lambda_2,
                                      \mu_X\oplus\mu_Z^a).
\end{split}
\qquad\text{(7)}
\]

Let \(\beta_1\) be the propagation of \(\mu_X\) through the inverse of \(\lambda_1\), and \(\beta_2\) the propagation of \(\mu_Z\) through \(\lambda_2\), both in \(E_Y\). The second index identity, with all these orders, is

\[
t_1+t_2-t-r(\lambda_1,\lambda_2)
       =\tau_{E_Y}(\mu_Y,\beta_1,\beta_2).
\qquad\text{(8)}
\]

These are the linear identities of the relation and inertia calculus. They follow by the diagonal reduction and the four-plane cocycle; their exact geometric proofs are prerequisites. Formula (8) retains the auxiliary order \(\beta_1,\beta_2\), whereas (3) retains the vertical order \(\alpha_2,\alpha_1\).

The right side of (8) is locally constant for the chosen family. To see the relevant rank conditions, an intersection \(\mu_Y\cap\beta_1\) corresponds to a vector in \(\lambda_1\cap(\mu_X\oplus\mu_Y^a)\), so is zero. The analogous intersection with \(\beta_2\) is zero. An intersection \(\beta_1\cap\beta_2\) gives a vector in the composed relation lying in \(\mu_X\oplus\mu_Z^a\); its endpoint vector is zero by the last product transversality, and then middle-projection injectivity makes it zero too. The same argument shows that propagation has no kernel in these complement coordinates, so the middle planes vary continuously. All three pairwise intersection dimensions are consequently zero. Index continuity proves the asserted local constancy.

## A formula at regular projection points extends to the chosen point

Take a small connected neighborhood \(P\) of the selected tuple in the smooth matching fibre product. Choose the auxiliary complements of (7) continuously there. The continuous-type theorem provides the input shift functions

\[
d_i(q)-t_i(q)/2=\kappa_i,
\qquad i=1,2,
\qquad\text{(9)}
\]

with \(d_i\) equal to the specified input shift at the chosen tuple, and with the input coefficient types still \(L_i\). Define the candidate output shift by (4) pointwise. Then (8) gives

\[
D(q)-t(q)/2
=\kappa_1+\kappa_2-\frac{\dim Y}2
            +\frac12\tau(\mu_Y,\beta_1,\beta_2).
\qquad\text{(10)}
\]

This is constant after shrinking \(P\). If (4) is known at one point of this neighborhood, start the output's continuous-type rule there. Its allowed shift function has the same corrected degree as (10). Therefore the coefficient type and the displayed output shift extend throughout \(P\), including the selected tuple. This argument also proves the allowed parity of \(D\) throughout the neighborhood, starting from the known calculation. It never assumes the conclusion's parity to prove the conclusion.

It suffices that the known points accumulate at the selected tuple: take one in the chosen connected neighborhood. In particular regular projection points are sufficient. They are dense because every open set contains a neighborhood where the derivative of the base projection has its maximal local rank. On that constant-rank neighborhood the conic Lagrangian is the conormal of its smooth projected submanifold, by the regular-projection normal form. The relevant microsupport estimate was established before this propagation argument, so the output is a bounded sheaf with the required smooth Lagrangian support.

## Two reductions preserve the degree formula

First we may ensure that all three selected covectors are nonzero. Take \(q\in\dot T^*\mathbb R\), and tensor both kernels externally with the diagonal coefficient \(k_{\Delta_{\mathbb R}}\) at \((q,q^a)\). Replace every manifold \(W\) by \(W\times\mathbb R\) and every selected point by \((p_W,q)\). The external-composition comparison gives

\[
(K_1\boxtimes k_\Delta)\circ_\mu(K_2\boxtimes k_\Delta)
\simeq(K_1\circ_\mu K_2)\boxtimes k_\Delta.
\qquad\text{(11)}
\]

Each diagonal factor is simple with normalized shift \(1/2\). Thus the input shifts increase by \(1/2\), the middle dimension increases by one, and the diagonal's relation index is zero: its two propagated verticals coincide. The new predicted output degree is

\[
(d_1+1/2)+(d_2+1/2)-\frac{\dim Y+1+r}{2}=D+1/2.
\qquad\text{(12)}
\]

This is exactly the output degree obtained by the external-product rule. Conversely, take any transverse test defining the original output's coefficient type at an allowed shift. Tensoring with this diagonal keeps that coefficient complex and adds \(1/2\) to its normalization. Therefore the stabilized calculation detects the original type and degree. No tensor conservativity for a general coefficient complex is being used: the extra coefficient is \(k\) itself.

Second we may enlarge the output and make the last manifold a point. Define

\[
i(x,y,z)=(x,z;y,z),\qquad
\widetilde K_1=i_*(K_1\boxtimes k_Z)
\quad\text{on }(X\times Z)\times(Y\times Z).
\qquad\text{(13)}
\]

The graph-realization comparison identifies \(\widetilde K_1\circ_\mu K_2\) with the original composition. Up to permuting factors, \(\widetilde K_1=K_1\boxtimes k_{\Delta_Z}\); hence its type is \(L_1\) with shift \(d_1+\dim Z/2\). The new middle dimension is \(\dim Y+\dim Z\). The physical point of the enlarged kernel is \((p_X,p_Z^a;p_Y^a,p_Z)\), so the new middle symplectic space is \(E_Y\oplus E_Z^a\).

In that space, its first propagated plane is \(\alpha_1\oplus V_Z^a\), its second is \(\lambda_2\), and its vertical is \(V_Y\oplus V_Z^a\). Reduce the common \(V_Z^a\) in the first and third planes of the ordered index. The resulting index is exactly (3). Consequently

\[
d_1+\frac{\dim Z}{2}+d_2
 -\frac{\dim Y+\dim Z+r}{2}=D.
\qquad\text{(14)}
\]

The extra diagonal degree cancels the extra middle dimension. Closed direct image in (13) introduces no exceptional shift. This reduction and the nonzero stabilization commute through the ordinary external-product comparisons.

## Hypersurfaces and contact graph kernels

If the two input Lagrangians are hypersurface conormals and their composition is a conormal \(T_S^*(X\times Z)\), use their local coefficient models. Writing \(K_i=(L_i)_{S_i}[s_i]\) gives \(d_i=s_i+1/2\). The hypersurface theorem gives the coefficient \(L_1\otimes^L L_2\) on \(S\), with ordinary shift

\[
s_1+s_2+1-\frac{\dim Y+\operatorname{codim}S+r}{2}.
\qquad\text{(15)}
\]

Adding \(\operatorname{codim}S/2\) to normalize this output gives (4). The arbitrary derived coefficients have been retained. The constant-rank conormal model and its localized replacement arrows justify using these representatives near the selected point.

Now assume \(\Lambda_1\) is a contact graph. Apply the enlarged-output reduction if needed. Factor its contact transformation as two hypersurface contact graphs, with simple unshifted kernels \(H_1,H_2\). The type formula for \(H_1\circ_\mu H_2\) follows first where its base projection has constant rank, by (15), and then everywhere by (10).

Its coefficient type is \(k\). Apply one common conormal chart to this simple composite and to \(K_1\). Their coefficient-object models identify the composite with an integral shift of \(k_M\), and \(K_1\) with the corresponding integral shift of \((L_1)_M\). The inverse chart commutes with constant coefficient tensor by the projection formula. Thus the local object decomposition gives
\(K_1\simeq (L_1)_{X\times Y}\otimes^L(H_1\circ_\mu H_2)[b]\)
for the integer \(b\) adjusting its normalized shift to \(d_1\). This uses an object model, not a full equivalence of all coefficient morphisms. For each hypersurface factor the earlier contact-type theorem applies to the arbitrary input sheaf. The graph regrouping identifies their successive action with action by their composite. The cost identity (6) makes their total degree precisely (4). Finally the ordinary constant-coefficient projection formula pulls \(L_1\) through the bounded convolution and retains the derived tensor with \(L_2\); the integer \(b\) shifts its degree as specified. Thus (4) holds whenever the first kernel is a contact graph.

The corresponding statement with a graph second follows by transposing the ordinary kernel convolution. At the transposed physical points the new selected endpoint covectors are \(p_Z^a,p_Y^a,p_X^a\). Factor permutation preserves each kernel's type and shift. In the middle symplectic space both the form and the propagated order are reversed, giving

\[
\tau_{E_Y^a}(V_Y^a,\alpha_1^a,\alpha_2^a)
       =\tau_{E_Y}(V_Y,\alpha_2,\alpha_1).
\qquad\text{(16)}
\]

Hence the cost is the same and the symmetric derived tensor gives (4). This transposition uses the existing physical microsupport branch; it does not assume that an arbitrary sheaf's microsupport is invariant under a full antipode.

## Contact normalization proves the general case

We now use the following simultaneous geometric normal form. After (11) and (13), choose endpoint and middle contact transformations such that the transformed two Lagrangians and their composed Lagrangian are conormals of hypersurfaces. The transformations preserve the selected germs and middle transversality. This is the precise simultaneous input used here; it includes the finite generic choices, rather than asserting that a one-Lagrangian normal form automatically provides them all. We retain its local geometric proof as a prerequisite.

Choose simple graph kernels \(F_1,F_2\) for the two transformations and normalized inverse graph kernels \(G_1,G_2\), with their actual diagonal identities. In the enlarged-output situation the last manifold is a point. Set

\[
H=F_1\circ_\mu K_1,
\qquad A=H\circ_\mu G_2,
\qquad B=F_2\circ_\mu K_2.
\qquad\text{(17)}
\]

All pairs defining (17) have a graph factor, so their types and shifts are already known. Their Lagrangians are the transformed relations. In particular \(A,B\), and their composition have the hypersurface conormal forms just specified; (15) applies to \((A,B)\).

The graph regrouping and cancellation give

\[
A\circ_\mu B
\simeq(H\circ_\mu G_2)\circ_\mu(F_2\circ_\mu K_2)
\simeq H\circ_\mu K_2.
\qquad\text{(18)}
\]

To obtain the degree of the last pair, apply (6) to \((H,G_2,B)\). The pairs \((H,G_2)\) and \((G_2,B)\) have graph factors, and \((H\circ_\mu G_2,B)=(A,B)\) is the known hypersurface pair. These three degree formulas determine the formula for \((H,G_2\circ_\mu B)=(H,K_2)\). The coefficient factors of \(G_2,F_2\) are \(k\); their normalized shifts cancel according to their diagonal identity. Explicitly the diagonal has shift \(\dim Y/2\) and costs \(\dim Y/2\) when composed with a sheaf germ, since its repeated propagated vertical makes the index zero. It therefore acts with zero net degree.

Finally apply the same cost argument to \((G_1,H,K_2)\). Both pairs with \(G_1\) are graph cases, and \((H,K_2)\) has just been established. Graph regrouping identifies \(G_1\circ_\mu H\) with \(K_1\), so the remaining pair is exactly \((K_1,K_2)\). Its coefficient type and normalized degree are (4). This is a cancellation of already proved cases, not an application of the hypersurface contact action to an arbitrary kernel with a nontrivial last manifold.

Undo (13) and (11) using (12) and (14). This proves (4) for all selected covectors, including zero, relative to the stated geometric and sheaf prerequisites. No transitive prerequisite closure or global support theorem is inferred.

## Complex composition has a complex dimension correction

If the manifolds and the Lagrangians are complex, use the underlying real cotangent symplectic form \(2\operatorname{Re}\omega\). The propagated verticals in (2) are complex Lagrangian planes. Multiplication by \(i\) negates their real index quadratic form and pairs its positive and negative parts. Thus \(r=0\). Since \(\dim_{\mathbb R}Y=2\dim_{\mathbb C}Y\), inputs of normalized shift zero have output

\[
\text{type }L_1\otimes_k^L L_2,
\qquad D=-\dim_{\mathbb C}Y.
\qquad\text{(19)}
\]

The coefficients remain arbitrary bounded \(k\)-complexes. Complex geometry eliminates this inertia term; it does not eliminate the middle dimension or higher Tor in the coefficient tensor.

## What the comparison with Fourier integral operators expresses

The geometric mechanism is a canonical relation, its transverse composition and its ordered inertia correction. In this sheaf theory the objects acted on are sheaf germs; the operators are derived kernel functors; and the local coefficient type is a bounded complex over \(k\). Contact graphs give inverse category equivalences under their exact sheaf admissibility hypotheses. These are the precise features behind the comparison with classical contact transformations of distributions or Fourier integral operators.

The comparison by itself supplies no analytic symbol class, oscillatory-integral representation or equality of a sheaf functor with an arbitrary operator on distributions. Nor does a simple sheaf with complex Lagrangian support alone prove an equivalence with a holonomic differential-system category. Such applications require their own coefficient, constructibility and analytic hypotheses, developed later. The common geometry explains the analogy while each theory retains its own objects and comparison maps.

## Exercises with complete solutions

### Recover the ordinary hypersurface shift

*Difficulty: Introductory.*

Suppose \(\dim Y=3\), the ordered relation index is one, both inputs are unshifted constant hypersurface kernels, and the composed conormal has codimension two. Compute the normalized degree and the ordinary coefficient-sheaf shift.

**Solution.** Each input has normalized shift \(1/2\). Formula (4) gives \(D=1-(3+1)/2=-1\). A constant coefficient on the output codimension-two submanifold has normalized shift equal to its ordinary shift plus one. Its ordinary shift is therefore \(-2\), agreeing with (15). Confusing these two degrees loses the codimension correction.

### A diagonal factor changes two different dimensions

*Difficulty: Intermediate.*

Let the original input shifts be \(d_1=0,d_2=3/2\), with \(\dim Y=2\) and \(r=1\), in a model satisfying the theorem. Compute the predicted degree before and after one-dimensional nonzero diagonal stabilization.

**Solution.** Initially \(D=3/2-(2+1)/2=0\). Stabilization gives input shifts \(1/2,2\), middle dimension three, and unchanged index one. Thus the new degree is \(5/2-(3+1)/2=1/2\). This agrees with tensoring the original output with a diagonal of normalized shift \(1/2\). The ordinary diagonal coefficient still has no ordinary cohomological shift.

### Why the auxiliary index can be constant at a singular projection

*Difficulty: Advanced.*

In (7), suppose along a connected small family \(t_1,t_2,t\) change by \(2,0,1\), while \(r\) changes by one. Assuming the geometric complement hypotheses, find the changes of the two input shifts and of the predicted output shift. Check its corrected degree.

**Solution.** Equation (9) gives input changes \(1,0\). Formula (4) gives output change \(1-1/2=1/2\). Subtracting half the change of \(t\) gives zero. Also the change of the left side of (8) is \(2+0-1-1=0\), consistent with the pairwise-transverse auxiliary triple. The physical type stays fixed while the normalized numerical degree may change by a half-integer across a projection-rank change.

### The graph comparison is still needed for a unit kernel

*Difficulty: Advanced.*

At a nonzero \(p\), consider three diagonal kernels with all selected covectors \(p\). Why does the isolated-entire-matching hypothesis fail, and which comparisons establish their regrouping in this lesson?

**Solution.** Their matching tuples are \((u,u,u,u)\). Scaling \(p\) by any nearby positive scalar gives a distinct tuple, so the entire matching germ is not a singleton. Fixing the outer endpoint covectors nevertheless forces every intermediate covector. The diagonal is a proper identity graph with bounded covector ratios, and its actual convolution unit maps identify every joint ordinary term with the same diagonal. The graph isolated-image comparisons descend these maps through the common denominator refinements. This proves the stated regrouping under the graph hypotheses without changing the earlier entire-matching condition.

### Complex geometry does not remove coefficient Tor

*Difficulty: Intermediate.*

In the complex case let \(\dim_{\mathbb C}Y=2\), \(k=\mathbb Z\), and both input coefficient types be \(\mathbb Z/2\) with normalized shift zero. Find the output normalized shift and the cohomology degrees of its coefficient type. Is it pure at any shift?

**Solution.** The complex index is zero and (19) gives shift \(-2\). A length-one free resolution computes \(\mathbb Z/2\otimes^L_{\mathbb Z}\mathbb Z/2\) with \(\mathbb Z/2\) in degrees \(-1\) and zero. These are the coefficient type's degrees at the specified normalization. Changing the normalized shift translates both degrees together; it cannot concentrate them in one degree. The output is not pure at any allowed shift. The complex middle dimension controls the geometric normalization, whereas the coefficient ring controls this Tor.

### Enlarging the output leaves the degree unchanged

*Difficulty: Intermediate.*

Suppose \(\dim Z=4\). Explain all three changes in passing to (13), and why their combination leaves (4) unchanged.

**Solution.** The first kernel gains the diagonal factor \(k_{\Delta_Z}\), so its normalized shift increases by two. The middle manifold gains four real dimensions, increasing the subtracted half-dimension by two. The ordered index stays the same after reducing the common \(V_Z^a\). Thus the two numerical changes cancel and the type coefficient is still \(L_1\otimes^L L_2\). The exact physical opposite \(Z\)-covectors in (13) enforce the diagonal match.

## References

The type and shift of a transverse composition of kernels belong to Kashiwara and Schapira's theory of pure sheaves and contact transformations; see M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §§7.1–7.4. The contact factorization, the normal forms and the linear identities are proved in Appendix A; the graph-specific formal comparisons, the coefficient and degree bookkeeping and the propagation argument are proved here.
