# The type and shift of a transverse kernel composition

A kernel need not be a constant sheaf on a submanifold. Its microsupport can be a smooth Lagrangian with a singular projection, and its coefficient type can be an arbitrary bounded complex. Transverse composition still has a precise answer: tensor the coefficient types and subtract a correction determined by the middle dimension and three ordered Lagrangian planes.

Use Microlocal composition at prescribed covectors, Composing hypersurface kernels with their shifts, Pure and simple sheaves from directional tests, and How simple sheaf shifts change along a Lagrangian. Coefficients are over a commutative ring \(k\) of finite global dimension. All sheaf and coefficient complexes are bounded; no finite-rank, perfect-coefficient or constructibility assumption is imposed on the two input kernels.

We first specify the ordered correction and the comparison maps used to compose germs. The linear identities, simultaneous complement choices and contact normalization are proved below. The sheaf arguments use the preceding kernel lessons: refined incoming cutoff, boundary-controlled isolated image, tensor/projection formula and proper-support Fubini. Each application retains those theorems' hypotheses.

*Original lesson text and solutions: CC0 1.0 Universal. Human mathematical sources are credited below.*

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

We prove both identities from the ordered cocycle and orthogonal-sum rules and the common-pair isotropic reduction rule. The latter allows reduction by an isotropic subspace contained in any two arguments, even when the third has a nonzero intersection with it. This will retain every excess in the endpoint propagations.

**The quotient and diagonal calculations.** For a Lagrangian \(L\) in a symplectic space of dimension \(2N\), and an isotropic \(I\) of dimension \(d\), put \(e=\dim(L\cap I)\). The pairing map \(L\to I^*\) has rank \(d-e\): its transpose has kernel \(I\cap L^\omega=I\cap L\). Hence \(\dim(L\cap I^\omega)=N-d+e\). Its image in \(I^\omega/I\) is isotropic and has dimension \(N-d\), after quotienting its kernel \(L\cap I\). Thus

\[
L_I=((L\cap I^\omega)+I)/I
\]

is Lagrangian. In particular, reducing \(\lambda_1\) by \(A_X\oplus0\), for any endpoint Lagrangian \(A_X\subset E_X\), gives its propagated plane in \(E_Y^a\). Reducing \(\lambda_2\) by \(0\oplus C_Z^a\) gives the other propagated plane in \(E_Y\). No kernel of either propagation is assumed zero. The calculation includes \(I=0\) and zero-dimensional endpoint spaces.

We will also use the diagonal identity in its proved order: for any three Lagrangians \(B,A,C\subset E\),

\[
\tau_{E^a\oplus E}(B^a\oplus B,A^a\oplus C,\Delta_E)
=\tau_E(B,C,A).
\]

Here is its short reduction proof to fix the signs. Insert \(H=A^a\oplus B\) into the cocycle for the displayed triple \((P,Q,\Delta_E)\). It gives \(\tau(P,Q,\Delta_E)=\tau(P,Q,H)+\tau(P,H,\Delta_E)-\tau(Q,H,\Delta_E)\). The first term is zero by direct sums and repeated arguments. In the second, reduce the common \(0\oplus B\); the quotient triple is \((B^a,A^a,B^a)\), so this term is zero as well. In the last, reduce the common \(A^a\oplus0\); its quotient triple in \(E\) is \((C,B,A)\). The result is \(-\tau_E(C,B,A)=\tau_E(B,C,A)\), as asserted. These reductions also apply when any pair intersects.

**One four-factor index represents the relation index.** In

\[
\mathcal F=E_X\oplus E_Y^a\oplus E_Y\oplus E_Z^a,
\qquad R=\lambda_1\oplus\lambda_2,
\]

choose any endpoint Lagrangians \(A_X,C_Z\) and a middle Lagrangian \(B_Y\). Set

\[
\begin{aligned}
P(A,B,C)&=A_X\oplus B_Y^a\oplus B_Y\oplus C_Z^a,\\
D(A,C)&=A_X\oplus\Delta_Y\oplus C_Z^a.
\end{aligned}
\]

Both are Lagrangian. Reduce the isotropic \(A_X\oplus0\oplus0\oplus C_Z^a\), common to these two planes. Its symplectic quotient is \(E_Y^a\oplus E_Y\). The first plane reduces to \(B_Y^a\oplus B_Y\), the third to \(\Delta_Y\), and \(R\) to \(\gamma_1^a\oplus\gamma_2\), where \(\gamma_1=\lambda_1^t A_X\) and \(\gamma_2=\lambda_2 C_Z\) denote the two middle propagated planes. The quotient dimension calculation above includes their arbitrary endpoint excess. Common-pair reduction and the diagonal identity therefore give

\[
\tau_{\mathcal F}\bigl(P(A,B,C),R,D(A,C)\bigr)
=\tau_{E_Y}(B_Y,\gamma_2,\gamma_1).
\]

For \((A_X,B_Y,C_Z)=(V_X,V_Y,V_Z)\), this is exactly \(r(\lambda_1,\lambda_2)\) in (3).

For three successively composable Lagrangian relations, with the indicated transverse composites, the relation index satisfies

\[
r(\lambda_1,\lambda_2)+r(\lambda_1\circ\lambda_2,\lambda_3)
=r(\lambda_1,\lambda_2\circ\lambda_3)+r(\lambda_2,\lambda_3).
\qquad\text{(6)}
\]

**Proof of (6).** Let the three relations run from \(E_W\) through \(E_Z,E_Y\) to \(E_X\), as above. Work in the symplectic space

\[
\mathcal G=E_X\oplus E_Y^a\oplus E_Y
                 \oplus E_Z^a\oplus E_Z\oplus E_W^a.
\]

In its displayed factor order, define four Lagrangian planes and the product relation:

\[
\begin{aligned}
P&=V_X\oplus V_Y^a\oplus V_Y\oplus V_Z^a\oplus V_Z\oplus V_W^a,\\
R&=\lambda_1\oplus\lambda_2\oplus\lambda_3,\\
D_Y&=V_X\oplus\Delta_Y\oplus V_Z^a\oplus V_Z\oplus V_W^a,\\
D_Z&=V_X\oplus V_Y^a\oplus V_Y\oplus\Delta_Z\oplus V_W^a,\\
D&=V_X\oplus\Delta_Y\oplus\Delta_Z\oplus V_W^a.
\end{aligned}
\]

In each orthogonal summand, the triple \((P,D_Y,D)\) has a repeated plane: at \(Y\) its last two planes are \(\Delta_Y\), and at \(Z\) its first two are \(V_Z^a\oplus V_Z\). The endpoint triples also repeat. Thus \(\tau(P,D_Y,D)=0\). The same reasoning gives \(\tau(P,D_Z,D)=0\). Applying the cocycle with \(D_Y\), and using alternation, gives

\[
\tau_{\mathcal G}(P,R,D)
=\tau_{\mathcal G}(P,R,D_Y)+\tau_{\mathcal G}(D_Y,R,D).
\]

The first term is \(r(\lambda_1,\lambda_2)\): the first four factors give the preceding four-factor formula, and the last two give a zero index with repeated vertical planes. For the second term, reduce
\(K_Y=0\oplus\Delta_Y\oplus0\oplus0\oplus0\), the full middle diagonal, which lies in \(D_Y\cap D\). Its orthogonal imposes equality of the two \(E_Y\) vectors; quotienting by \(K_Y\) forgets their common value. The quotient is therefore canonically
\(E_X\oplus E_Z^a\oplus E_Z\oplus E_W^a\), and the reduced product relation is \((\lambda_1\circ\lambda_2)\oplus\lambda_3\). The other two reduced planes are respectively the product vertical plane and \(V_X\oplus\Delta_Z\oplus V_W^a\). The same four-factor formula identifies this term with \(r(\lambda_1\circ\lambda_2,\lambda_3)\).

Repeat the cocycle with \(D_Z\) instead. The first term is now \(r(\lambda_2,\lambda_3)\), since the first two factors have a repeated vertical plane. In the second, reduce the full \(Z\)-diagonal \(K_Z\subset D_Z\cap D\). Matching and forgetting its common vector reduces \(R\) to \(\lambda_1\oplus(\lambda_2\circ\lambda_3)\). Its index is \(r(\lambda_1,\lambda_2\circ\lambda_3)\). Both sums therefore equal the same number \(\tau_{\mathcal G}(P,R,D)\), proving (6).

Every constraint just used lies in two displayed arguments, so the common-pair reduction rule applies without imposing transversality on the propagated endpoint planes or on the index triples. In the linear quotients, the reduced relation is its endpoint image even if a matching vector has nonunique middle representatives; the quotient removes precisely those representatives. The stated transverse hypotheses ensure the smooth geometric compositions used in the lesson, but no unmentioned zero-excess hypothesis enters this signature calculation. \(\square\)

The two middle dimensions on each side are the same, so the cost \(c\) in (3) satisfies the same equality. This is the exact linear relation identity, independent of sheaf associativity. When the graph regrouping just proved applies, validity of the type formula for any three of the four pairs in (6) proves it for the fourth: expand both total degrees, use (6), and use associativity of the derived coefficient tensor.

We first prove that the simultaneous product complements needed below exist. Fix finitely many labelled real symplectic spaces \(E_j\), with vertical Lagrangians \(V_j\). Each prescribed product uses a subset of these labelled spaces, with each label occurring at most once. Occurrences of the same geometric space in different independent roles receive independent labels and plane choices. Choose symplectic coordinates \((q_j,p_j)\) with \(V_j=\{q_j=0\}\). Every plane

\[
\mu_j(S_j)=\{p_j=S_jq_j\},\qquad S_j=S_j^t,
\]

is Lagrangian and transverse to \(V_j\). We can choose the matrices so that their products are simultaneously transverse to any finite collection of Lagrangian planes in products of the \(E_j\), allowing a separate sign on each factor of each product.

Here is a determinant proof of this assertion. For one prescribed Lagrangian \(L\) in a signed product of total dimension \(2N\), change each negative factor's momentum coordinate to \(-p_j\). The product form is then \(\sum dp\wedge dq\). Write a basis of \(L\) as the columns of \(\binom QP\), where \(Q,P\) are \(N\)-by-\(N\) real matrices. Isotropy gives \(Q^tP=P^tQ\), and the stacked matrix has full column rank. Product transversality is precisely the nonvanishing of

\[
\det\!\left(P-\operatorname{diag}(\epsilon_jS_j)Q\right),
\]

where \(\epsilon_j=1\) or \(-1\) records the factor's sign. This is a real polynomial in the independent entries of the symmetric matrices. It is not identically zero: substitute \(S_j=\epsilon_j tI\), obtaining \(\det(P-tQ)\). The latter polynomial is nonzero because

\[
(P+iQ)^t(P-iQ)=P^tP+Q^tQ
\]

is positive definite and hence \(P-iQ\) is invertible. The same proof covers a condition on a single factor. The product of the finitely many nonzero determinant polynomials is a nonzero real polynomial, so it has a nonzero value at some real tuple of symmetric matrices. Indeed a real polynomial vanishing everywhere is zero, by induction on its number of variables and the one-variable root theorem. In dimension zero the relevant determinant is one. This proves the assertion in every dimension.

Apply it to \(\lambda_1\), \(\lambda_2\) and \(\lambda_1\circ\lambda_2\) in their respective signed products. It gives \(\mu_X,\mu_Y,\mu_Z\) transverse to the verticals and all three required product planes. For continuous relations near the selected tuple, use local symplectic frames adapted to the verticals and keep these three matrices fixed in the frames. The three determinant conditions remain nonzero on a smaller neighborhood by continuity. No constancy of a projection rank or of an intersection with the original verticals is needed. Put

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

**Proof of (8).** Return to \(\mathcal F\) and \(R=\lambda_1\oplus\lambda_2\). Use the four Lagrangian planes

\[
\begin{aligned}
P&=V_X\oplus V_Y^a\oplus V_Y\oplus V_Z^a,\\
Q&=\mu_X\oplus\mu_Y^a\oplus\mu_Y\oplus\mu_Z^a,\\
D_P&=V_X\oplus\Delta_Y\oplus V_Z^a,\\
D_Q&=\mu_X\oplus\Delta_Y\oplus\mu_Z^a.
\end{aligned}
\]

Orthogonal-sum additivity identifies \(\tau(P,R,Q)=t_1+t_2\). Put
\(r_\mu=\tau_{E_Y}(\mu_Y,\beta_2,\beta_1)\), with the same second-before-first propagation order as \(r\). The preceding four-factor formula gives

\[
\tau(P,R,D_P)=r,\qquad \tau(Q,R,D_Q)=r_\mu.
\]

The full \(Y\)-diagonal \(K_Y=0\oplus\Delta_Y\oplus0\) lies in \(D_P\cap D_Q\). Its orthogonal is the matching subspace and its quotient is \(E_X\oplus E_Z^a\). The three reductions of \((D_P,R,D_Q)\) are the endpoint vertical plane, \(\lambda_1\circ\lambda_2\), and the auxiliary endpoint product, respectively. Thus the common-pair reduction rule gives \(\tau(D_P,R,D_Q)=t\), with exactly the order in (7).

Two remaining terms vanish. For \(\tau(P,D_P,D_Q)\), the endpoint factors have their first two arguments equal, and the middle factor has its last two arguments equal, so every direct-sum contribution is zero. For \(\tau(P,Q,D_Q)\), the endpoint factors have their last two arguments equal. Its middle contribution is

\[
\tau_{E_Y^a\oplus E_Y}
 (V_Y^a\oplus V_Y,\mu_Y^a\oplus\mu_Y,\Delta_Y)
=\tau_{E_Y}(V_Y,\mu_Y,\mu_Y)=0
\]

by the ordered diagonal identity. Consequently the cocycle for \((P,R,D_P,D_Q)\) gives \(\tau(P,R,D_Q)=r+t\), since \(\tau(R,D_P,D_Q)=-t\). The cocycle for \((P,R,Q,D_Q)\) then gives

\[
t_1+t_2
=\tau(P,R,D_Q)+\tau(R,Q,D_Q)
=r+t-r_\mu.
\]

Subtract \(t+r\) and use alternation in the middle space:
\(-r_\mu=-\tau(\mu_Y,\beta_2,\beta_1)
=\tau(\mu_Y,\beta_1,\beta_2)\). This is (8).

The calculation proves the identity for all the displayed Lagrangian planes, including degenerate triples and nonzero propagation kernels. The auxiliary transversality assumptions in (7) are needed for the following continuous-family argument, rather than for this algebraic identity. Formula (8) therefore retains the auxiliary order \(\beta_1,\beta_2\), while (3) retains the vertical order \(\alpha_2,\alpha_1\). \(\square\)

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

Here is the comparison behind (11). The external-composition proof applies to the original pair and the pair of diagonal kernels. A matching witness for the external kernels projects to a witness for each pair, because external microsupport is contained in the product. The first pair isolates \(p_Y\); the diagonal pair forces the added covector to be \(q\). Use product neighborhoods and the confined proper representatives of the two pairs. Their product is proper over the product output. Ordinary external tensor and \(!\)-Fubini then identify the convolution with the external product of the two convolutions. These maps commute with every denominator and neighborhood refinement. Testing against an output germ identifies the same filtered colimit of morphisms, so the formal comparison descends to the represented objects. Finally the actual diagonal unit map identifies \(k_\Delta\circ_\mu k_\Delta\) with \(k_\Delta\). Only the microsupport inclusion was used; equality for arbitrary coefficient complexes is unnecessary.

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

The enlarged-output comparison identifies \(\widetilde K_1\circ_\mu K_2\) with the original composition. In detail, the conormal of the closed embedding \(i\) forces the two physical \(Z\)-covectors to sum to zero; the constant factor \(k_Z\) has zero tangential covector. Matching with \(K_2\) therefore gives precisely the original middle incidence, with no new choice. For ordinary representatives the tensor is supported on the diagonal in the two \(Z\) copies. Projection formula and integration over the second copy remove that diagonal and leave integration over \(Y\). Applying these maps to the common confined denominator systems gives a comparison compatible with all transitions. Finite collections of representatives and their comparisons admit common refinements, so the induced morphism colimits agree. The represented comparison is the claimed isomorphism. Up to permuting factors, \(\widetilde K_1=K_1\boxtimes k_{\Delta_Z}\); hence its type is \(L_1\) with shift \(d_1+\dim Z/2\). The new middle dimension is \(\dim Y+\dim Z\). The physical point of the enlarged kernel is \((p_X,p_Z^a;p_Y^a,p_Z)\), so the new middle symplectic space is \(E_Y\oplus E_Z^a\).

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

We also need (15) when the last manifold is a point, as in (13). The stated hypersurface composition theorem assumes three nonzero selected covectors, so this case requires its own check. Keep \(p_X\ne0\) and \(p_Y\ne0\), and let \(S_1\subset X\times Y\), \(S_2\subset Y\) be hypersurfaces with the same transverse conormal matching and smooth conormal image. Choose defining functions \(h_1(x,y)\), \(h_2(y)\). The selected covectors imply \(d_Xh_1\ne0\), \(d_Yh_1\ne0\) and \(dh_2\ne0\). In a relation \(a\,dh_1+b\,dh_2=0\), the \(X\) component first gives \(a=0\), and then \(b=0\). Thus the lifted hypersurfaces meet transversely, and

\[
W=S_1,\qquad N=S_1\cap(X\times S_2),\qquad
f=\pi_X|_W
\]

have exactly the dimensions used in the reduction to a single hypersurface. The condition \(d_Yh_1\ne0\) makes \(f\) a submersion. Its pulled-back target cotangent bundle consists of ambient covectors with zero \(Y\) component. Such a covector can be a multiple of \(dh_1\) only if that multiple is zero. Consequently the nonzero output lift \((p_X,0)\) remains nonzero after restriction to \(T^*W\).

The same middle-difference map used in that proof is onto by the assumed conormal transversality; its base and fibre parts give the two regular cotangent restrictions. The quotient by the normal line \(I_W=\mathbb R\,dh_1\) has no kernel on the pulled-back target bundle, just proved, and identifies its intersection with the conormal of \(N\) with the ambient transverse intersection. Its dimension is \(\dim X\), exactly the transverse dimension for the submersion \(f\) of relative dimension \(\dim Y-1\). The preceding normal-form theorem therefore applies to this same hypersurface \(N\subset W\), with no null directions and with a nonzero selected covector.

The tensor of the two closed-support coefficient factors is still \((L_1\otimes^L L_2)_N\), and the closed-extension and proper-image comparisons are the same actual maps as in that proof. Transverse endpoint projection isolates the selected middle witness. Its confined formal-image comparison consequently identifies the resulting image with the kernel-germ composition. The index reductions in Keeping the index order through reduction allow \(E_Z=V_Z=0\); they give the same ordered index (3). The normal-form degree, using \(\dim W=\dim X+\dim Y-1\), is therefore exactly (15) with \(Z\) a point. This proves the extra case used below, without applying a nonzero-covector hypothesis to the zero cotangent bundle of a point.

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

Here is the simultaneous geometric normal form needed for the general case. First perform (11), then (13). Every original selected covector has become nonzero after (11). After (13), the selected output and middle covectors are \((p_X,p_Z^a)\) and \((p_Y,p_Z^a)\), respectively, and are nonzero. The last manifold is now a point. The enlarged first relation has middle projection equal to the old first middle projection times the full \(Z\)-cotangent factor. Its sum with the second relation's middle projection is therefore the whole new middle tangent space exactly when the original two middle projections span \(E_Y\). Thus transversality survives this reduction.

Rename the enlarged output and middle manifolds \(X,Y\). At their selected nonzero covectors let \(R_X,R_Y\) be the radial vectors, let \(\lambda_1\subset E_X\oplus E_Y^a\) be the first tangent relation, and let \(\ell_Y\subset E_Y\) be the second tangent Lagrangian, now a sheaf relation from a point. Its composite is a Lagrangian \(\ell_X\subset E_X\). Conicity gives

\[
(R_X,R_Y)\in\lambda_1,\qquad
R_Y\in\ell_Y,\qquad R_X\in\ell_X.
\]

Put \(I=\mathbb R(R_X,0)+\mathbb R(0,R_Y)\), an isotropic two-plane in the signed product. The transverse-composition kernel calculation says that \((0,v)\in\lambda_1\), \(v\in\ell_Y\), forces \(v=0\). Consequently

\[
\lambda_1\cap I=\mathbb R(R_X,R_Y).
\]

Indeed, subtract \(a(R_X,R_Y)\) from a vector \((aR_X,bR_Y)\in\lambda_1\); the remaining vector \((0,(b-a)R_Y)\) has its middle component in \(\ell_Y\), so \(b=a\). This is the place where transversality prevents a second forced radial intersection.

Define the two radial symplectic quotients

\[
\overline E_X=R_X^\omega/\mathbb R R_X,\qquad
\overline E_Y=R_Y^\omega/\mathbb R R_Y.
\]

Their dimensions are \(2\dim X-2\) and \(2\dim Y-2\). The reduction

\[
\overline\lambda_1
=\bigl((\lambda_1\cap I^\omega)+I\bigr)/I
\subset\overline E_X\oplus\overline E_Y^a
\]

is Lagrangian. To check the dimension directly, the pairing map \(\lambda_1\to I^*\) has rank \(\dim I-\dim(I\cap\lambda_1)=1\): its transpose has kernel \(I\cap\lambda_1^\omega=I\cap\lambda_1\). Thus \(\lambda_1\cap I^\omega\) has dimension \(\dim X+\dim Y-1\), and its image after quotienting its one-dimensional intersection with \(I\) has dimension \(\dim X+\dim Y-2\). Isotropy descends, so this is half the reduced dimension. The images \(\overline\ell_X,\overline\ell_Y\) and \(\overline V_X,\overline V_Y\) are Lagrangian in their respective radial quotients: each original plane contains its radial line and lies in its orthogonal.

Use the finite product-complement construction proved before (7), now in these two radial quotients. Choose \(\overline U_X,\overline U_Y\) transverse to \(\overline V_X,\overline V_Y\), respectively, such that they are also transverse to \(\overline\ell_X,\overline\ell_Y\), and

\[
\overline\lambda_1\cap
 (\overline U_X\oplus\overline U_Y^a)=0.
\]

The single-factor and product conditions form one finite list of nonzero determinant conditions. Their simultaneous satisfaction was proved there; an independent one-Lagrangian normalization would not suffice. Lift \(\overline U_X,\overline U_Y\) to their full inverse images \(U_X\subset R_X^\omega\), \(U_Y\subset R_Y^\omega\). They are Lagrangian and satisfy

\[
\begin{gathered}
U_X\cap V_X=U_X\cap\ell_X=\mathbb R R_X,\\
U_Y\cap V_Y=U_Y\cap\ell_Y=\mathbb R R_Y,\\
\lambda_1\cap(U_X\oplus U_Y^a)=\mathbb R(R_X,R_Y).
\end{gathered}
\]

For the last equality, a vector in the intersection maps to zero in the reduced product by the preceding transversality. It therefore lies in \(I\), whose intersection with \(\lambda_1\) was calculated explicitly. This argument includes dimensions one, where a radial quotient is zero and its unique plane is used.

Realize these two vertical choices by independent homogeneous contact charts \(\chi_X,\chi_Y\). More precisely, map each \(U_W\) isomorphically to the vertical plane at \((0,e_1)\in T^*\mathbb R^{\dim W}\), sending \(R_W\) to its radial vector. The alternating-subspace extension lemma extends this to a symplectic isomorphism of the whole tangent spaces. Apply homogeneous prescribed coordinates, Theorem 3.1, with no prescribed functions and with this radial-compatible marked differential. Its construction retains the differential even in the final position correction, and yields \(d\chi_W(U_W)=V_W'\). Both dimensions are positive because both marked covectors are nonzero. The charts can be restricted around the chosen rays and extended homogeneously to conic neighborhoods, as in that theorem.

In untwisted relation notation the first image is obtained by applying \(\chi_X\) and \(\chi_Y\) to its two entries; on the physical input factor the latter map is \(a\chi_Ya\). The second image is \(\chi_Y\Lambda_2\), and the composite image is \(\chi_X(\Lambda_1\circ\Lambda_2)\). The matching middle transformation cancels exactly, so these really are the two transformed inputs and their composed relation. Its differential is invertible on the middle space, preserving transversality.

The three equalities for \(U_X,U_Y\) show that the base-projection kernels of these three transformed Lagrangians are exactly their nonzero radial lines at the marked points. Each projection therefore has rank one less than its Lagrangian dimension. A nonzero minor keeps this rank at least that large nearby; the persistent nonzero radial kernel keeps it at most that large. It has constant rank there. Constant-rank conormal recognition, Theorem 5.1 consequently identifies all three germs with open conormal pieces of smooth hypersurfaces. The equalities \(U_W\cap V_W=\mathbb R R_W\) give the same rank argument for the physical graphs of the two charts, so those graphs themselves may be taken to be hypersurface conormals, as in the two-factor contact-chart construction.

There are only finitely many conditions, so one common restriction preserves every rank and transversality just verified. Restricting the base charts further makes the resulting embedded hypersurfaces closed in those charts. All conormal statements concern the selected nonzero pieces; no claim about every sign or every conormal direction is made. In particular the transformed first relation still has nonzero output and middle covectors, while the second relation ends at a point. The point-endpoint extension of (15) proved above is exactly the hypersurface theorem required for this pair. Zero original covectors entered only before (11); no homogeneous contact chart has been applied at a zero covector.

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

Undo (13) and (11) using (12) and (14). This proves (4) at all selected covectors, including zero. The conclusion concerns the represented composition of the selected germs; identifying it with an original global convolution still requires the full incidence and support hypotheses of the image comparison.

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

Masaki Kashiwara and Pierre Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §7.3, develops direct and inverse images of pure sheaves. Corollaries 7.3.4–7.3.5, printed pp. 135–138 (PDF pp. 138–141), give the Hom and tensor kernel actions. Their conclusions name ordinary module types under vanishing higher Ext or Tor. They also impose proper support, isolated full-fibre incidence and the stated noncharacteristic condition. Corollary 7.3.5 uses an antipodal kernel Lagrangian and writes the kernel shift as \(-d\); its displayed index must therefore be read with that convention.

Here (1)–(3) fix the physical kernel points and the ordered middle-space index before any degree calculation. The proof treats selected germs with arbitrary bounded derived coefficient types. Its two relation identities, simultaneous product complements and contact normalization are proved above; the linked kernel lessons supply the confined representatives, conormal coefficient models and contact graph identities. The reassociation arguments specify the comparisons needed to cancel those graph factors. Thus the full derived tensor in (4), including possible higher Tor, has its own argument. The complex specialization and solved calculations test the dimension, antipodal and stabilization conventions.
