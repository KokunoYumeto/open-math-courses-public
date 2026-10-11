# Compatible graphs and an actual continuum probability

Complete companion to [Unit 18](../established-approaches-and-open-problems.html). The [heat and action chapter](../two-dimensional-heat-and-action.html) supplies all HK and AC proofs, including every analytic input used below.

## GP.1. Physical rectangle, graphs and orientation

Fix physical lengths \(L_1,L_2>0\), a coupling \(g_2>0\) with units length\(^{-1}\), and \(D=[0,L_1]\times[0,L_2]\), oriented by \(dx^1\wedge dx^2\). Grid \(\Gamma_m\), \(m\in\mathbb N_0\), has vertices \((iL_1/2^m,jL_2/2^m)\), \(0\leq i,j\leq2^m\). Its positively designated edges run east and north. A face has physical area \(a_m=L_1L_2/4^m\) and dimensionless heat parameter

\[
 t_m=\frac{g_2^2a_m}{4}.                                    \tag{G1}
\]

The factor in this dictionary is proved from the original action in ACTION_COMPARISON_PROOF.md; it is not an implicit choice of units. Let \(E_m\) denote the designated edges, and \(X_m=G^{E_m}\), with product Haar probability. A configuration assigns \(U_e\in G\); on the reverse edge assign \(U_{e^{-1}}=U_e^{-1}\). For a traversed path \(\gamma=e_1\cdots e_r\), define

\[
 H_\gamma(U)=U_{e_r}\cdots U_{e_1},\quad H_{\rm id}=I,
 \quad H_{\gamma\delta}=H_\delta H_\gamma.                  \tag{G2}
\]

Composition \(\gamma\delta\) means first \(\gamma\), then \(\delta\). The products act on column vectors at their starting vertex and land at the final vertex. Cancellation of an immediately reversed pair and insertion of an identity preserve the product; reversal gives its inverse.

For a square face whose bottom, right, top and left designated links are \(h_b,v_r,h_t,v_l\), the positively oriented boundary starts at the lower left and has

\[
 P_f=v_l^{-1}h_t^{-1}v_rh_b.                                \tag{G3}
\]

Changing its starting vertex conjugates this matrix by the intervening path transport. Reversing the face orientation inverts it. Centrality and inverse invariance of \(p_t\) make its density independent of both choices.

## GP.2. Exact gauge maps

For arbitrary matrices \(h_v\in G\) at the finitely many vertices, define

\[
 (h\cdot U)_e=h_{t(e)}U_eh_{s(e)}^{-1},\quad
 H_\gamma(h\cdot U)=h_{t(\gamma)}H_\gamma(U)h_{s(\gamma)}^{-1}.       \tag{G4}
\]

The second identity follows by cancellation of adjacent endpoint factors in (G2), also for reversed edges. It proves composition of gauge maps and conjugation covariance of face holonomies. Left and right Haar invariance prove that the product Haar probability is preserved. This is the course's active gauge convention, not its inverse: for \(A^h=hAh^{-1}-dh\,h^{-1}\), differentiating \(h(\gamma(s))U(s)h(\gamma(0))^{-1}\) proves the transport equation \(U'=-A(\dot\gamma)U\) transforms by (G4).

## GP.3. The finite probability density

Define a Borel measure by

\[
 d\mu_m(U)=\prod_{f\subset\Gamma_m}p_{t_m}(P_f(U))\prod_{e\in E_m}d\mu(U_e).
                                                               \tag{G5}
\]

There is no omitted partition factor: its mass is exactly one, as proved in GP.4. Its density is smooth and strictly positive on the compact configuration space, so every nonempty open set has positive measure. GP.2 proves gauge invariance. Every path observable in (G2) is continuous. A Wilson character is \(W_n(\gamma)=\chi_n(H_\gamma)/(n+1)\); it is gauge invariant for closed paths and has absolute value at most one. The unscaled character \(\chi_n\) is also retained below when its dimension factor matters.

## GP.4. An explicit tree change of variables and independence

This calculation works for any rectangular grid with \(N_1,N_2\geq1\). Choose as tree all horizontal edges and all vertical edges in the leftmost column, and root it at \((0,0)\). It is a tree: each row is attached to the left column once, is internally a chain, and the left column itself is a chain; its edge count is \(N_1(N_2+1)+N_2=(N_1+1)(N_2+1)-1\). Let \(g_v\) be the product of the original links along the unique tree path from the root to \(v\), with \(g_{(0,0)}=I\). Apply the gauge field \(h_v=g_v^{-1}\). All tree links become identity. Write the remaining vertical links as \(V_{i,j}\), \(1\leq i\leq N_1\), \(0\leq j<N_2\), and set \(V_{0,j}=I\).

The change of variables is a bijection between original links and \((g_v:v\ne(0,0);V_{i,j}:i\geq1)\). Its inverse on an edge is \(U_e=g_{t(e)}V_eg_{s(e)}^{-1}\), where \(V_e=I\) on the tree. Order tree vertices so each parent precedes its child; changing each tree link to its child's \(g_v\) preserves conditional Haar measure by left or right translation. On every remaining edge the two endpoint matrices are already fixed, and changing \(U_e\) to \(V_e\) also preserves Haar. Successive finite integrations therefore prove exact preservation of product Haar measure, without a formal gauge-volume division.

In this gauge the face at \((i,j)\), \(0\leq i<N_1\), has

\[
 x_{i,j}=V_{i,j}^{-1}V_{i+1,j},\qquad
 V_{i,j}=x_{0,j}x_{1,j}\cdots x_{i-1,j}.                     \tag{G6}
\]

For each row this is a triangular change of variables preserving product Haar measure, by repeated translations. Its inverse is displayed. Thus (G5), with arbitrary positive face parameters \(t_{i,j}\), becomes exactly

\[
 \prod_{v\ne(0,0)}d\mu(g_v)\prod_{i,j}p_{t_{i,j}}(x_{i,j})d\mu(x_{i,j}).       \tag{G7}
\]

Every factor has mass one by HK.6. This proves GP.3, and proves independence of the displayed tree and face variables. The based lasso that follows the tree from the root to the lower-left face vertex, traverses that face positively and returns along the same tree has holonomy \(g_v^{-1}P_fg_v=x_{i,j}\). Therefore (G7) concerns actual explicitly specified non-Abelian path observables.

For example, two distinct such lassos have independent holonomies with strictly positive heat densities. Matrices \(i\sigma_1,i\sigma_2\) do not commute: their two products are \(-i\sigma_3\) and \(+i\sigma_3\). Continuity gives neighbourhoods of this pair on which the commutator is different from identity, and (G7) assigns their product positive probability. The construction has not replaced the group by its conjugacy-class interval or by an Abelian group.

## GP.5. The two elementary refinement integrations

First subdivide an edge as the path \(e_1e_2\), with old link \(U=U_2U_1\). The map \((U_1,U_2)\mapsto(U_1,U)\) preserves product Haar, since for each \(U_1\) right translation carries \(U_2\) to \(U\). Every old path product is preserved on substitution. This proves exact edge-subdivision consistency.

Next split a face by a new chord from \(v_0\) to \(v_1\), with link \(u\). Let the old positive boundary consist first of an arc \(a:v_0\to v_1\), with holonomy \(A\), then an arc \(b:v_1\to v_0\), with holonomy \(B\). Its holonomy is \(BA\). The two new face words, based at their suitable endpoints, may be chosen as \(u^{-1}A\) and \(Bu\). For positive times \(s,t\),

\[
 \int_G p_s(u^{-1}A)p_t(Bu)d\mu(u)=p_{s+t}(BA).               \tag{G8}
\]

To verify the noncommuting order, substitute \(x=u^{-1}A\), so \(u=Ax^{-1}\); Haar inversion and translation preserve measure. The integrand becomes \(p_s(x)p_t(BAx^{-1})\), whose integral is precisely (H9). No commuting relation between \(A\) and \(B\) is used. If \(A,B\) are retained, the exact probability density for the new chord is

\[
 b_{s,t}(u\mid A,B)=\frac{p_s(u^{-1}A)p_t(Bu)}{p_{s+t}(BA)}.   \tag{G9}
\]

Its denominator is strictly positive, and (G8) gives mass one. These formulas prove gluing with fixed retained boundary links as well as free-boundary gluing.

## GP.6. Dyadic projections and their complete consistency

The map \(\pi_m:X_{m+1}\to X_m\) multiplies the two fine links along each old edge in traversal order, and discards other fine links. It is continuous and surjective: prescribe the first half as identity and the second as the old link, and set unused links arbitrarily. Associativity gives the composed projections \(\pi_{m,k}\) for \(k>m\).

A full refinement can be executed using GP.5 only. Subdivide every old edge into halves. In each old face insert the vertical chord between its horizontal-side midpoints, dividing it into equal-area rectangles. Subdivide that chord at the face centre. Insert the horizontal chord in each half rectangle. These give its four dyadic children. The unchanged faces are unaffected; every new face parameter is proportional to its physical area, so the sums in (G8) are exactly the old face parameters. Applying the edge and chord integrations in reverse order proves

\[
 (\pi_m)_*\mu_{m+1}=\mu_m.                                  \tag{G10}
\]

The constructed geometric order also specifies a finite list of elementary conditional samplers for each refinement. Internal gauge factors cancel along every subdivided old edge, so the projections intertwine the fine gauge action with its restriction to old vertices.

## GP.7. Boundary holonomy and exact Wilson expectations

For a complete rectangular grid, (G6) shows that its positive outer boundary has holonomy

\[
 (x_{0,N_2-1}\cdots x_{N_1-1,N_2-1})\cdots
 (x_{0,0}\cdots x_{N_1-1,0}).                                \tag{G11}
\]

The rows appear from top to bottom in this matrix product because path transport multiplies later vertical edges on the left. This is its matrix value in the tree gauge, and conjugate to its value in any other vertex frame. The root gauge is identity, so when the base is the root the two values are equal. Products of independent variables with respective densities \(p_{t_1},p_{t_2}\) have density \(p_{t_1+t_2}\), by (H9) with the corresponding left or right product; centrality and inversion invariance make both orders give the same density. Iterating therefore gives outer-boundary law \(p_{\sum t_f}d\mu\).

The same conclusion holds for a dyadic axis-aligned subrectangle \(R\subset D\), with its lower-left basepoint, even when it is strictly interior. To check this without assigning independent untransported face matrices, integrate the outside strips of faces, retaining all edges of \(R\). Remove the top rows and bottom rows first, then the remaining left and right columns. At each stage every face in the exposed outer row has an outward horizontal edge occurring only in that face density; integrating that edge gives one by Haar translation and \(\int p_t=1\). Remove its density and integrate any now-unused edges. The same operation with vertical edges removes the side strips. It leaves exactly the free-boundary rectangular-grid density on \(R\). Unused outside edges contribute factors one. Repeating (G11) there proves the assertion. Gauge invariance also ensures the resulting holonomy law is central, so a different base frame makes no change to its law.

Writing \(|R|\) for the actual physical area, HK.10 gives

\[
 \mathbb E_{\mu_m}\chi_n(H_{\partial R})=(n+1)
       \exp\!\left[-\frac{g_2^2|R|\,n(n+2)}8\right],\qquad
 \mathbb E_{\mu_m}W_n(\partial R)=
       \exp\!\left[-\frac{g_2^2|R|\,n(n+2)}8\right].         \tag{G12}
\]

The assumptions are \(R\) a rectangle with its sides in this grid, \(|R|>0\), \(n\in\mathbb N_0\). A zero-width retraced boundary has identity holonomy and the limiting value is one for the dimension-divided trace. This is an exact area law at every containing refinement. It neither assumes nor defines a four-dimensional confinement statement.

## GP.8. A countable supply of random choices from one probability space

We now prove existence of compatible configurations rather than appealing to an unproved extension theorem. Start from \(\Omega=[0,1]\) with Lebesgue probability. For non-dyadic \(\omega\), let \(b_k(\omega)\in\{0,1\}\) be its binary digits. Give dyadic points the expansion ending in zeros; this countable exceptional set has measure zero. Any specification of \(r\) distinct digits has probability \(2^{-r}\): partition into intervals of length \(2^{-M}\), where \(M\) is the largest specified place, and count the \(2^{M-r}\) allowed intervals.

Partition the positive integers into \(I_j=\{2^j(2k-1):k\geq1\}\), \(j\geq0\), and put \(Z_j=\sum_{k\geq1}2^{-k}b_{2^j(2k-1)}\). They are Borel maps. The digit calculation proves that every finite tuple of the \(Z_j\) has independent uniform distributions on dyadic intervals. Approximating interval endpoints from above and below by dyadic rationals proves the same for all interval boxes. It extends to Borel sets by the following elementary uniqueness argument, also used below: for a class of sets closed under intersections, equality of two finite measures on that class extends to its generated sigma algebra. To prove it, the equality class for complements and disjoint countable unions is a lambda system; first hold one intersected set fixed, then vary the other, to show the smallest such lambda system containing an intersection-closed generating class is closed under intersections, hence is a sigma algebra. Applying this argument coordinate by coordinate proves the asserted finite product laws. A fixed enumeration of \(\mathbb N_0\times\mathbb N_0\) partitions the indices of the \(Z_j\) into countably many disjoint infinite blocks. Each block can supply all proposals for one sampler, and different blocks are independent in every finite collection.

## GP.9. Exact Haar and heat samplers, with termination proofs

From three independent uniforms \(z_1,z_2,z_3\), put

\[
 F(\theta)=\frac{\theta-\sin\theta\cos\theta}{\pi},\quad
 \theta=F^{-1}(z_1),\quad v=2z_2-1,\quad\phi=2\pi z_3,
\]


\[
 \boldsymbol n=(\sqrt{1-v^2}\cos\phi,\sqrt{1-v^2}\sin\phi,v),\quad
 q=(\cos\theta,\sin\theta\boldsymbol n).
\]

Here \(F\) is continuous, strictly increasing from zero to one; \(F'=2\sin^2\theta/\pi\) is positive on the interior. Its inverse is continuous. The spherical area variable \((v,\phi)\) has density \(dv\,d\phi/(4\pi)\), and \(F'\) gives exactly (H3). Endpoint direction choices are immaterial. This is a Borel Haar sampler.

For \(p_t\), let \(M_t=\sum_{n\geq0}(n+1)^2e^{-t\lambda_n}\). Repeatedly sample a Haar point \(q\) and an additional uniform \(z\), accepting when \(z\leq p_t(q)/M_t\). HK.7 ensures \(0<p_t/M_t\leq1\), and each attempt has acceptance probability \(1/M_t>0\). The chance of failing forever is \(\lim_{k\to\infty}(1-1/M_t)^k=0\). The first accepted point has distribution \(p_t d\mu\): for any Borel set \(B\), sum the geometric series of first-success probabilities \((1-1/M_t)^{k-1}\int_Bp_t/M_t\). The first-success index and output are Borel functions of the input sequences.

For the bridge (G9), a bound uniform in the retained links is

\[
 M_{s,t}^{\rm bridge}=\frac{M_sM_t}{\min_Gp_{s+t}}<\infty.
\]

Accept Haar proposals when \(z\leq b_{s,t}(q\mid A,B)/M_{s,t}^{\rm bridge}\). All tests are Borel in the inputs and retained parameters. The same calculation proves its exact conditional law and almost-sure termination, with acceptance probability \(1/M_{s,t}^{\rm bridge}\). The bound is not presented as an efficient algorithm; it is a complete existence construction with fixed finite positive constants.

## GP.10. Recursive construction of every compatible level

At level zero sample \(h_b,h_t,v_l\) independently Haar and \(P\) independently with density \(p_{g_2^2L_1L_2/4}\). Set \(v_r=h_tv_lPh_b^{-1}\). The inverse change of variables is (G3), and Haar translations show that this has density (G5).

For every edge subdivision, sample its first half \(U_1\) Haar and set \(U_2=UU_1^{-1}\). For every chord insertion, use (G9) with the prescribed two child areas. Use unused independent uniform blocks for each successive sampling task in the finite refinement list GP.6, and then for each succeeding level. The lists together are countable. Conditional on all earlier choices, the elementary probability identities of GP.5 show that a subdivided configuration has exactly the new finite density: a chord replaces its old face factor \(p_{s+t}(BA)\) by its two child factors through multiplication by (G9); an edge subdivision uses its measure-preserving product map. This proves by induction that each level has law \(\mu_m\).

Each sampler terminates with probability one, even conditional on retained links, because its acceptance bound is uniform. The union of their countably many failure events has probability zero. On the complementary Borel event every resulting sequence satisfies \(\pi_m(U^{m+1})=U^m\) exactly. On the null failure event define the entire sequence to be the all-identity compatible sequence. This modification is Borel, preserves every marginal and supplies a map defined on every \(\omega\in\Omega\).

## GP.11. The continuum probability space and its uniqueness

Define

\[
 X_\infty=\{(U^0,U^1,\ldots)\in\prod_{m\geq0}X_m:
                  \pi_m(U^{m+1})=U^m\text{ for every }m\}.
\]

Choose bounded compatible metrics on the finite products and weight them by \(2^{-m-1}\). This gives a metric on the product; convergence is exactly coordinatewise convergence. Each \(X_m\) is compact. A diagonal subsequence chosen successively in its coordinates converges in this weighted metric, since its tail weights tend to zero. Thus the product is compact; the displayed equalities are closed, so \(X_\infty\) is compact as well. The recursive map GP.10 is Borel into it: each coordinate is Borel, and a countable product of second-countable metric spaces has a countable cylinder basis, so its Borel sigma algebra is generated by coordinate inverse images. Define \(\mu_\infty\) as the pushforward of Lebesgue probability by that actual map. This proves existence.

The marginal on \(X_m\) is \(\mu_m\). These marginals determine the probability uniquely: any finite collection of coordinates of a compatible sequence is a continuous function of the coordinate with largest index. Thus all finite-coordinate cylinder probabilities are determined. Cylinders are closed under intersections and generate the Borel sigma algebra; the elementary measure uniqueness argument in GP.8 proves uniqueness. This proof has not imported an unproved uncountable projective-limit theorem.

## GP.12. Precisely which continuum paths receive holonomy

Let \(V_\infty=\bigcup_m V_m\). Take all finite oriented edge words in all \(\Gamma_m\), with endpoints in this set, and identify a coarse edge with its two fine subedges; also identify insertion/removal of immediately reversed pairs and identity words. The resulting countable groupoid \(\mathcal P_{\rm dyad}(D)\) has objects \(V_\infty\). Composition is traversal followed by traversal when endpoints match; after passage to a common refinement all products are finite words, and associativity is literal word associativity. The relations are compatible with composition and reversal.

For a compatible configuration define \(H_\gamma\) using any containing grid and (G2). Projection compatibility and group cancellation prove independence of its representative. Every \(H_\gamma:X_\infty\to G\) is a continuous map depending on a finite level. The identities \(H_{\gamma\delta}=H_\delta H_\gamma\), \(H_{\gamma^{-1}}=H_\gamma^{-1}\), and \(H_{\rm id}=I\) hold for every configuration, including the null-set replacement in GP.10. Every finite joint distribution is the one from any common containing grid. This is the proved continuum object: holonomies on this specified countable family, with all dyadic refinements already present and no residual mesh parameter in the probability law.

It does not assert holonomy on every smooth curve, continuity in a metric on arbitrary paths, or a random differentiable connection. Nor are geometrically different paths identified by arbitrary homotopies: a contractible rectangle has the nontrivial law (G12), so that additional quotient would be false.

## GP.13. Gauge invariance at the constructed limit

For any fixed function \(h:V_\infty\to G\), act on each finite-level link by (G4). Internal endpoint factors cancel, so the resulting sequence is compatible. The map on \(X_\infty\) is continuous with inverse given by \(h^{-1}\). Its marginal pushforwards equal \(\mu_m\) by GP.2–GP.3; uniqueness in GP.11 proves it preserves \(\mu_\infty\). Thus the complete fixed gauge group of vertex functions acts by probability-preserving maps. Every closed Wilson character is invariant. The result is an exact map to gauge-invariant observables; no undefined quotient volume is used.

## GP.14. Boundary gluing as an actual probability operation

Equation (G9) is also the precise conditional probability for a face decomposition with retained boundary data. Its bounded continuous density depends measurably on that data and integrates to one for every data point, not only almost everywhere. Multiplying and integrating these kernels in a specified finite subdivision order gives a Borel conditional probability for all inserted edges. Equation (G8) proves that integrating it recovers the original face density. Different insertion orders give the same resulting finite measure whenever their final grid is the same, because their final density is literally the common product in (G5), and both constructions preserve Haar changes of variables. No unspecified gluing functional is needed.

## GP.15. Exact comparison with the receiving literature

Lévy, [math/0101239v1](https://arxiv.org/abs/math/0101239v1), chap1.tex lines 224–352, defines forward holonomy in the same reverse matrix order as (G2), but his gauge variable \(j_v\) acts as \(j_{t(e)}^{-1}U_ej_{s(e)}\). The exact conversion to (G4) is \(j_v=h_v^{-1}\). His face-area heat parameter uses \(\partial_s=\tfrac12\Delta_{\mathrm L}\) for the volume-one metric. The complete HK.11 comparison gives \(s_{\mathrm L}=g_2^2|f|/(2V_\kappa^{2/3})\), with \(V_\kappa=4\sqrt2\pi^2\). The separate same-\(\kappa\) half-Laplacian has parameter \(s=2t=g_2^2|f|/2\). Both comparisons preserve the actual course trace, physical area, coupling and time \(t=g_2^2|f|/4\).

The source's full subdivision proof at chap1.tex lines 575–798 treats a broader graph/boundary setting. GP.5–GP.6 prove the particular maps and boundary kernels needed here; the source's displayed \(p_{s+t}(AB)\) versus our \(p_{s+t}(BA)\) is legitimate because \(AB=A(BA)A^{-1}\), while the raw path holonomy remains \(BA\). Its preliminary convolution typo is recorded in HK.11. The source's projective-limit discussion in chap2.tex lines 1–68 cites an external existence theorem rather than proving it there; GP.8–GP.11 supply a complete construction for this bounded countable scope. We do not attribute our restricted sampling proof to that source, and do not import its unexamined later all-path results.

## GP.16. What finite-area consistency establishes

For every fixed dyadic rectangle and every finite collection of the specified paths, their probability distribution is exactly unchanged by every further dyadic refinement. The physical lengths and \(g_2\) are held fixed; face times shrink because physical face areas shrink. Equations (G8), (G10), the sampler, and the limit uniqueness prove that statement together, rather than treating it as a formal lattice limit. The construction is two-dimensional and uses a heat semigroup. It is not a proof that the four-dimensional Wilson regulator possesses any continuum limit.


## DP.1. Fixed objects and the complete analytic input

Fix \(L_1,L_2,g_2,\hbar,c>0\), with \(L_1,L_2\) lengths, \(g_2\) of units length\(^{-1}\), \(\hbar\) of action units and \(c\) of speed units. Set \(D=[0,L_1]\times[0,L_2]\), oriented by \(dx^1\wedge dx^2\). The group is \(G=SU(2)\), represented as


\[
 Q(q)=q_0I+i\sum_{a=1}^3q_a\sigma_a,\qquad |q|^2=1,\qquad
 \kappa(X,Y)=-\operatorname{tr}_{\mathbb C^2}(XY).
 \tag{DP.1}
\]


The Pauli matrices and their multiplication are exactly those in HK.1. In particular the vector part of quaternion multiplication in this \(+i\sigma_a\) convention has cross term \(-\boldsymbol q\times\boldsymbol q'\). The metric is twice the unit-round metric on \(S^3\), its volume is \(V_\kappa=4\sqrt2\pi^2\), and \(\Delta_\kappa=\frac12\Delta_{S^3}\). Haar probability is


\[
 d\mu=\frac{\sin^2\theta}{2\pi^2}d\theta\,d\Omega,\qquad
 \int_G F(\theta)d\mu=\frac2\pi\int_0^\pi F(\theta)\sin^2\theta\,d\theta.
 \tag{DP.2}
\]


Here \(q=(\cos\theta,\sin\theta\boldsymbol n)\), \(0\leq\theta\leq\pi\), and the two polar directions have no effect on this probability. Left/right multiplication and inversion preserve it because they are orthogonal transformations of \(\mathbb R^4\). Define, with continuous endpoint values,


\[
 \chi_n(\theta)=\frac{\sin((n+1)\theta)}{\sin\theta},\quad
 \lambda_n=\frac{n(n+2)}2,\quad
 p_t(g)=\sum_{n=0}^{\infty}(n+1)e^{-t\lambda_n}\chi_n(g),\quad t>0.
 \tag{DP.3}
\]


HK.3–HK.7 provide the complete proof that this series is smooth, central, inverse invariant and strictly positive, has Haar integral one, and satisfies


\[
 \int_Gp_s(xy^{-1})p_t(y)d\mu(y)=p_{s+t}(x),\qquad
 0<p_t(g)\leq M_t:=\sum_{n=0}^{\infty}(n+1)^2e^{-t\lambda_n}<\infty.
 \tag{DP.4}
\]


The exact analytic provider is its polynomial approximation, harmonic decomposition, projection identity \(K_n(q,q')=(n+1)\chi_n(Q(q)Q(q')^{-1})\), and maximum argument followed by the convolution/analytic-zero proof of strict positivity. None of the present probability arguments assumes an unproved positivity or projective-limit theorem. The provider proves all these statements for this trace metric, Haar probability and \(\partial_t=\Delta_\kappa\), including both conjugacy endpoints. HK.8 supplies its independently derived Gaussian image formula; DP.12 below checks the error bound directly.

The physical parameter of each positive-area face is always


\[
 t_f=\frac{g_2^2|f|}{4}.
 \tag{DP.5}
\]


This is the parameter received from the original action \(S_2[A]=\hbar g_2^{-2}\int_D\kappa(F_{12},F_{12})d^2x\), whose ordered-index form is \(\hbar(2g_2^2)^{-1}\int\sum_{\mu,\nu=1}^2\kappa(F_{\mu\nu},F_{\mu\nu})d^2x\). For \(x^2=c\tau\), area is \(c\,dx^1d\tau\); a width \(R\), duration \(T\) rectangle has \(t=g_2^2RcT/4\). These factors are retained even though the probability construction itself uses the two length coordinates.

## DP.2. Finite configurations, path words and gauge maps

At level \(m\geq0\), vertices are \((iL_1/2^m,jL_2/2^m)\), \(0\leq i,j\leq2^m\), and designated edges point east or north. Let \(E_m\) be that finite edge set, \(X_m=G^{E_m}\), and \(a_m=L_1L_2/4^m\). A reversed edge has matrix \(U_{e^{-1}}=U_e^{-1}\); a word \(\gamma=e_1\cdots e_r\), traversed in written order, has


\[
 H_\gamma(U)=U_{e_r}\cdots U_{e_1},\quad H_{\mathrm{id}_v}=I,\quad
 H_{\gamma\delta}=H_\delta H_\gamma,\quad H_{\gamma^{-1}}=H_\gamma^{-1}.
 \tag{DP.6}
\]


Every adjacent inverse pair cancels exactly, including pairs of reverse-designated edges. For a positive face based at its lower-left corner, the links bottom/right/top/left give


\[
 P_f=v_l^{-1}h_t^{-1}v_rh_b,\qquad
 d\mu_m(U)=\prod_{f\subset\Gamma_m}p_{g_2^2a_m/4}(P_f(U))\prod_{e\in E_m}d\mu(U_e).
 \tag{DP.7}
\]


The gauge map for a vertex function \(h\) is \(U_e\mapsto h_{t(e)}U_eh_{s(e)}^{-1}\). Multiplying successive factors proves \(H_\gamma\mapsto h_{t(\gamma)}H_\gamma h_{s(\gamma)}^{-1}\); reverse links obey the same formula. Haar invariance and centrality prove invariance of the entire density. Changing a face basepoint conjugates its matrix, while reversing its orientation inverts it; hence its factor in (DP.7) is unchanged. All these maps are continuous on finite products.

## DP.3. Exact mass one and face coordinates

For any rectangular \(N_1\times N_2\) grid, choose the tree consisting of every horizontal edge and every left-column vertical edge, rooted at \((0,0)\). It has \((N_1+1)(N_2+1)-1\) edges, is connected, and has no cycles: each horizontal row attaches to the single left-column chain. Let \(g_v\) be the original tree transport root-to-\(v\), with \(g_{(0,0)}=I\). Gauge-transform by \(g_v^{-1}\). Every tree edge becomes \(I\); call the remaining vertical links \(V_{i,j}\), with \(V_{0,j}=I\).

The inverse map is \(U_e=g_{t(e)}V_eg_{s(e)}^{-1}\), with \(V_e=I\) on the tree. Order each tree vertex after its parent. Then replacing the parent link by \(g_v\) preserves conditional Haar measure, since the remaining parent product is fixed. Replacing a non-tree link by \(V_e\) is a left/right translation with both endpoints fixed. Iterating finitely many such integrals proves preservation of product Haar. No gauge quotient or division is involved.

In this gauge the actual face matrix is \(x_{i,j}=V_{i,j}^{-1}V_{i+1,j}\). Conversely \(V_{i,j}=x_{0,j}\cdots x_{i-1,j}\). This row-by-row triangular change also preserves Haar. A face originally based at \(v\) has \(x_{i,j}=g_v^{-1}P_fg_v\), so centrality yields precisely


\[
 \prod_{v\ne(0,0)}d\mu(g_v)
 \prod_{0\leq i<N_1,\ 0\leq j<N_2}p_{t_{i,j}}(x_{i,j})d\mu(x_{i,j}).
 \tag{DP.8}
\]


Every factor has integral one. This proves the actual mass of (DP.7) is one, independent of the number or sizes of faces. It also proves independence of these particular transported face matrices, without asserting independence of untransported plaquettes in arbitrary frames. The strictly positive continuous density gives positive mass to every nonempty open set of \(X_m\).

## DP.4. Both elementary refinement identities and conditional laws

Splitting an edge into the traversal \(e_1e_2\) gives \(U=U_2U_1\). The map \((U_1,U_2)\mapsto(U_1,U)\) preserves product Haar by right translation in the second factor; its inverse is \(U_2=UU_1^{-1}\). Substitution preserves every old path, including its reverse, because \((U_2U_1)^{-1}=U_1^{-1}U_2^{-1}\). Thus, conditional on \(U\), choose \(U_1\) Haar and set \(U_2=UU_1^{-1}\).

To cut a face, let its positive boundary be the traversal \(a b\), with \(a:v_0\to v_1\), \(b:v_1\to v_0\), matrices \(A,B\), and old holonomy \(BA\). Give the new chord \(v_0\to v_1\) matrix \(u\). The new positive face matrices can be taken as \(u^{-1}A\) and \(Bu\), at their respective starting points. Haar inversion/translation and (DP.4), with \(x=u^{-1}A\), prove


\[
 \int_G p_s(u^{-1}A)p_t(Bu)d\mu(u)=p_{s+t}(BA),\qquad
 b_{s,t}(u\mid A,B)=\frac{p_s(u^{-1}A)p_t(Bu)}{p_{s+t}(BA)}.
 \tag{DP.9}
\]


The density is positive, continuous in all variables, and integrates to one for every \((A,B)\in G^2\). It is the conditional insertion kernel with those links retained: multiplying the old joint density by this kernel cancels its single old face factor and gives exactly the two new factors and the added Haar differential. Every other link and factor remains present. This argument proves the kernel identity for bounded Borel observables by direct integration, not just for continuous test functions.

## DP.5. The actual dyadic refinement and all joint laws

Define \(\pi_m:X_{m+1}\to X_m\) by replacing each old designated edge by the product of its two fine designated links, second on the left, and forgetting the unused fine links. It is continuous and onto: set the first half \(I\), the second equal to the desired old edge, and the unused links \(I\). Compositions \(\pi_{m,k}\) satisfy \(\pi_{m,k}\pi_{k,l}=\pi_{m,l}\) by associativity.

To produce exactly \(\Gamma_{m+1}\), split all old edges, insert in each old face the vertical midpoint chord, split that chord at its centre, then insert one horizontal midpoint chord in each half. All created faces have positive area; the vertical split uses \((s,t)=(t_m/2,t_m/2)\) and each horizontal split uses \((t_m/4,t_m/4)\). Since \(t_m=g_2^2a_m/4\), those are the times of the actual half- and quarter-areas. Reversing the integrations of DP.4 gives


\[
 (\pi_m)_*\mu_{m+1}=\mu_m,\qquad
 (\pi_{m,k})_*\mu_k=\mu_m.
 \tag{DP.10}
\]


Equivalently, using the displayed conditional samplers forward constructs the finer density from the coarser density. Different valid finite insertion orders give the same final measure because that final product density is identical. Internal gauge factors cancel on split edges, so \(\pi_m\) intertwines a fine vertex gauge map with its restriction to old vertices.

For any finite list of old path words, substitution on split edges proves equality of their matrix-valued observable maps after \(\pi_m\). Consequently their full joint distributions, including all overlaps and self-intersections, agree under every further refinement. Independence is asserted only where DP.3 proves it.

## DP.6. Independent random streams on one existing Lebesgue space

Use the source's \(\Omega=[0,1]\) with Lebesgue probability and digits


\[
 b_k(\omega)=\lfloor2^k\omega\rfloor-2\lfloor2^{k-1}\omega\rfloor\in\{0,1\}
 \quad(0\leq\omega<1),\qquad b_k(1)=0.
 \tag{DP.11}
\]


These maps are Borel and choose the terminating expansion at a dyadic point; the assigned fractional digits at the endpoint \(1\) affect only a singleton of measure zero. If \(r\) distinct positions at most \(K\) are prescribed, exactly \(2^{K-r}\) of the \(2^K\) half-open dyadic intervals satisfy them, so the probability is \(2^{-r}\). Partition positive positions as \(2^j(2k-1)\), \(j\geq0,k\geq1\), and define \(Z_j=\sum_{k\geq1}2^{-k}b_{2^j(2k-1)}\). They are Borel limits. A tail of these digits all equal to one or all zero from a fixed place has probability at most \(2^{-r}\) for every finite further length \(r\), hence probability zero. Countably many such events are null. Thus the possible alternate binary expansions do not change the dyadic-box laws: every finite tuple of the \(Z_j\) consists of independent uniform variables.

For precision, the extension from dyadic interval boxes to all Borel sets uses the following elementary finite-measure uniqueness argument. A family containing the whole space and closed under complements and disjoint countable unions is a lambda system. For an intersection-closed generating family \(\mathcal C\), first fix one member of \(\mathcal C\) and apply those closures to intersections with it; then vary the fixed member. This shows that the smallest lambda system containing \(\mathcal C\) is closed under intersections, hence also arbitrary countable unions by disjointification; it is the generated sigma algebra. The equality set of two finite measures of equal mass is a lambda system. Therefore agreement on \(\mathcal C\) implies agreement on that sigma algebra. Applying this to dyadic boxes proves the assertion, without assuming an infinite product-space existence theorem.

Choose a fixed bijection \(\mathbb N_0^3\to\mathbb N_0\) (successive diagonal enumerations suffice). Use its coordinates as task number, proposal number and uniform-coordinate number. Each task receives an infinite sequence of independent proposal blocks, each with enough coordinates to sample Haar and a test uniform. For every finite collection of tasks, independence of their entire sequence-valued streams follows from the finite-digit calculation and the same uniqueness argument on the countable cylinder sigma algebra. The product sigma algebra is Borel because these countable products of second-countable spaces have countable cylinder bases. This proves independence also of the sigma fields generated by earlier task streams, including tasks whose outputs depend on arbitrarily many proposals.

## DP.7. Borel samplers, finite tails and termination

For three independent uniforms \(z_1,z_2,z_3\), let


\[
 F(\theta)=\frac{\theta-\sin\theta\cos\theta}{\pi},\quad
 \theta=F^{-1}(z_1),\quad v=2z_2-1,\quad\phi=2\pi z_3,\quad
 \boldsymbol n=(\sqrt{1-v^2}\cos\phi,\sqrt{1-v^2}\sin\phi,v).
 \tag{DP.12}
\]


The derivative \(F'=2\sin^2\theta/\pi\) is positive in the interior, so \(F\) is a continuous strictly increasing bijection \([0,\pi]\to[0,1]\). The inverse is continuous. The map \(q=(\cos\theta,\sin\theta\boldsymbol n)\) is Borel at all endpoints as well; its law is (DP.2), since \(v,\phi\) have joint density \(1/(4\pi)\) on \([-1,1]\times[0,2\pi)\). Values on probability-zero coordinate endpoints can be assigned by the same formula.

For a positive density \(d_z(q)\) with integral one and bound \(d_z(q)\leq B<\infty\), where \(z\) is retained data and \(B\) is independent of it, use independent Haar proposals \(Q_k\) and uniforms \(V_k\), accepting the first \(V_k\leq d_z(Q_k)/B\). Its acceptance probability is exactly \(1/B\), so necessarily \(B\geq1\), and for every integer \(K\geq0\)


\[
 \mathbb P(N>K\mid z)=(1-B^{-1})^K\leq e^{-K/B},\qquad
 \mathbb E(N\mid z)=B.
 \tag{DP.13}
\]


When \(B=1\), \(N=1\) almost surely; the \(K=0\) expression is understood as probability one. For a Borel set \(C\subset G\), summing the first-success probabilities gives


\[
 \sum_{k=1}^{\infty}(1-B^{-1})^{k-1}\frac1B\int_Cd_z(q)d\mu(q)
 =\int_Cd_z(q)d\mu(q).
\]


The tests, first-success index and successful output are Borel in \((z,(Q_k,V_k)_{k\geq1})\). Set the output to \(I\) if there is no success; that event is Borel and has conditional probability zero. This proves the exact sampling kernel and its null failure set for every retained-data value.

For \(p_t\), take \(B=M_t\). For the bridge in (DP.9), take


\[
 B_{s,t}=\frac{M_sM_t}{\min_{g\in G}p_{s+t}(g)}<\infty.
 \tag{DP.14}
\]


Compactness and strict positivity prove the denominator is positive. The upper bound is uniform in \(A,B\); in this formula the subscripted \(B_{s,t}\) is a bound, while \(B\) in (DP.9) is a boundary matrix. Formula (DP.13) proves quantitative tails for these actual samplers. No efficiency claim is made as face times shrink.

For a fixed list of \(J\) sampling tasks, possibly with adaptively retained boundary matrices, proposal caps \(K_j\geq B_j\log(J/\varepsilon)\), \(0<\varepsilon<1\), make the probability that at least one cap is exceeded at most \(\varepsilon\), by conditional (DP.13) and a union bound. Finite-level construction therefore has an explicit finite probabilistic proposal bound, while its exact, uncapped version has the required law.

## DP.8. Recursive configurations, including all exceptional inputs

At level zero sample \(h_b,h_t,v_l\) independently Haar and \(P\) with density \(p_{g_2^2L_1L_2/4}\), using distinct streams. Set \(v_r=h_tv_lPh_b^{-1}\). Then \(v_l^{-1}h_t^{-1}v_rh_b=P\); translations in \(v_r\) prove exactly density (DP.7).

Apply each finite refinement list of DP.5 in a fixed lexicographic face/edge order. Edge splits use a fresh Haar stream; face splits use a fresh bridge stream. Enumerate all these tasks by the natural numbers. At each finite stage retained matrices are Borel functions of earlier streams; current-stream independence and the kernel identity in DP.7 give the asserted conditional law. This last assertion follows first for indicators of retained-data and proposal-cylinder sets by independence, then for bounded Borel integrands by simple approximation and monotone convergence. Thus the adaptive dependence creates no extra hypothesis.

Define every task output on its own failure set by \(I\), so recursion remains a Borel formula for every input. Since all retained matrices remain in \(G\), the next sampler's uniform bound still applies even on such inputs. Each task fails with probability zero; the union \(F\) of all failures is a Borel null set. On \(\Omega\setminus F\), all dyadic products are exactly compatible, and induction using DP.4 proves each level has law \(\mu_m\). Finally replace the entire output sequence on \(F\) by the all-identity sequence. The replacement is Borel, is compatible at every level, and changes no finite law. This is an actual map on the whole of one probability space, not a claim about prospective consistent marginals.

## DP.9. The compact receiving space and uniqueness of its probability

Choose metrics \(d_m\leq1\) compatible with each finite product topology, and equip \(\prod_{m\geq0}X_m\) with \(d(U,V)=\sum_{m\geq0}2^{-m-1}d_m(U^m,V^m)\). Coordinate convergence is equivalent to convergence for \(d\): a finite initial sum converges termwise and the remaining tail is uniformly small. A diagonal subsequence argument using compactness of each \(X_m\) gives a convergent subsequence of every sequence in the product. In a metric space sequential compactness implies compactness: otherwise a cover with no finite subcover yields either failure of total boundedness and a separated sequence, or, using a finite-radius covering sequence, a Cauchy subsequence whose limit contradicts the original open cover. Thus the product is compact. The equalities below are closed:


\[
 X_\infty=\{U:\pi_m(U^{m+1})=U^m\text{ for every }m\geq0\},\qquad
 \mu_\infty=\Phi_*\operatorname{Leb}_{[0,1]},
 \tag{DP.15}
\]


where \(\Phi\) is DP.8's globally defined compatible map. The coordinate formulas are Borel, and the product has a countable cylinder basis, so \(\Phi:\Omega\to X_\infty\) is Borel. This proves existence of a Borel probability on the compact space.

Let \(\rho_m:X_\infty\to X_m\) be projection. Then \((\rho_m)_*\mu_\infty=\mu_m\). Any finite set of coordinates on \(X_\infty\) is a continuous function of the largest coordinate, so these marginals determine all finite-cylinder probabilities. Finite cylinders are intersection closed and generate the Borel sigma algebra. The uniqueness argument of DP.6 proves that no second Borel probability has these marginals. Its support is all \(X_\infty\): a nonempty basic open cylinder is the inverse image of a nonempty open set at its largest level, which has positive finite probability by DP.3.

## DP.10. Exact groupoid correspondence, gauges and finite laws

Let \(V_\infty=\bigcup_mV_m\). Take finite composable oriented edge words in all grids, with identity words at all these vertices, and quotient only by coarse-edge subdivision into its two fine edges and by insertion/removal of adjacent reverse pairs. This defines a countable groupoid \(\mathcal P_{\rm dyad}(D)\): the union of finite-word sets over countably many finite alphabets is countable; every finite groupoid relation can be placed in one common refinement, where composition and reversal are the finite-word operations. Relations preserve endpoints and are stable under composition and reversal.

Let \(\mathscr H\) be all maps \(H:\mathcal P_{\rm dyad}(D)\to G\) satisfying (DP.6). Evaluation gives a bijection


\[
 X_\infty\longleftrightarrow\mathscr H,\qquad U\longmapsto(H_\gamma(U))_\gamma.
 \tag{DP.16}
\]


Indeed compatibility and cancellation prove well-definedness; conversely evaluating \(H\) on every designated edge gives configurations whose projections agree by the subdivision relation. These constructions are inverse on every edge and hence on every word. With the subspace topology from the countable product \(G^{\mathcal P_{\rm dyad}}\), both directions are continuous: each path evaluation is a finite product at one level, while each inverse coordinate is an edge evaluation. The defining equations of \(\mathscr H\) are closed, so this is also an exact compact-space identification, rather than merely an informal description of random paths.

For paths \(\gamma_1,\ldots,\gamma_r\) contained in level \(m\) and bounded Borel \(f:G^r\to\mathbb C\), their complete joint law is


\[
 \mathbb E_{\mu_\infty}f(H_{\gamma_1},\ldots,H_{\gamma_r})
 =\int_{G^{E_m}}f(H_{\gamma_1}(U),\ldots,H_{\gamma_r}(U))
       \prod_fp_{g_2^2a_m/4}(P_f(U))\prod_ed\mu(U_e).
 \tag{DP.17}
\]


Equation (DP.10) ensures this expression is unchanged at any containing refinement. Every fixed \(h:V_\infty\to G\) acts by \(H_\gamma\mapsto h_{t(\gamma)}H_\gamma h_{s(\gamma)}^{-1}\). This is a homeomorphism with inverse \(h^{-1}\); its finite marginals preserve \(\mu_m\), so uniqueness proves it preserves \(\mu_\infty\). The group action is also jointly continuous in the product topology on \(G^{V_\infty}\), since every output coordinate uses finitely many input coordinates. No gauge quotient measure is required.

The quotient does not identify arbitrary homotopies. In particular a positive-area rectangle boundary has the nontrivial heat law proved next, although it is contractible as a geometric curve. Zero-length identity paths and retraced pairs do have matrix \(I\) at every configuration.

## DP.11. Rectangle laws with the original area and energy factors

In the tree gauge of DP.3 the positive outer boundary, based at its root, is


\[
 (x_{0,N_2-1}\cdots x_{N_1-1,N_2-1})\cdots
 (x_{0,0}\cdots x_{N_1-1,0}).
 \tag{DP.18}
\]


Each row product is its rightmost vertical link; traversing that right edge upward places later rows on the left, while the other boundary tree links are \(I\). The factors \(x_{i,j}\) are independent with respective heat laws. Convolution proves that the displayed product has density \(p_{\sum_f t_f}\), regardless of the successive left/right order: for a product \(YX\), integrate \(p_s(x)p_t(gx^{-1})\); for \(XY\), use the reversed roles. Both integrals are \(p_{s+t}(g)\) by (DP.4) and centrality.

For a subrectangle with dyadic coordinates, integrate outside top/bottom rows first, then the remaining left/right strips. A face in an exposed top or bottom row has one outward horizontal edge present only in that face factor; fixing the others, its integral is one by Haar translations. After removing that factor the next exposed row can be treated in the same way; unused edges integrate to one. Vertical edges give the identical argument for side strips. What remains is the full free-boundary density on the subrectangle. Repeating (DP.18) proves that its based boundary has heat density \(p_{g_2^2|R|/4}\). No untransported-face independence was used.

Sine orthogonality in (DP.2), termwise justified by the uniformly convergent series, gives


\[
 \mathbb E\chi_n(H_{\partial R})=(n+1)e^{-g_2^2|R|n(n+2)/8},\quad
 \mathbb E\frac{\chi_n(H_{\partial R})}{n+1}=e^{-g_2^2|R|n(n+2)/8}.
 \tag{DP.19}
\]


For \(|R|=RcT\), the exponent is \(-T\hbar^{-1}[\hbar c g_2^2R\,n(n+2)/8]\). The fundamental value is \(e^{-3g_2^2|R|/8}\), with the energy factor \(3\hbar c g_2^2R/8\). A zero-width or zero-height boundary reduces by retracing and has \(H=I\), so (DP.19) holds at area zero as its deterministic limit. No density \(p_0\) with respect to Haar is asserted.

## DP.12. Direct quantitative check of the image-series remainder

The exact HK.8 formula, obtained by Fourier integration of a periodized Gaussian and differentiation, is


\[
 p_t(\theta)=\frac{\sqrt{2\pi}}{2t^{3/2}}
       \frac{e^{t/2}}{\sin\theta}
       \sum_{k\in\mathbb Z}(\theta-2\pi k)e^{-(\theta-2\pi k)^2/(2t)}.
 \tag{DP.20}
\]


At \(0,\pi\) its value is the continuous limit supplied also by (DP.3). No pole or logarithm coordinate is used to define the kernel there. On \(|\theta|\leq\pi/2\), set \(f_t(z)=ze^{-z^2/(2t)}\), \(a=2\pi k\), \(k\geq1\). The paired nonzero terms \(f_t(\theta-a)+f_t(\theta+a)\) vanish at \(\theta=0\). Since
\(f'_t(z)=(1-z^2/t)e^{-z^2/(2t)}\), their absolute value divided by \(|\theta|\), with its derivative value at zero, is at most

\[
 2\left(1+\frac{(a+\pi/2)^2}{t}\right)
       e^{-(a-\pi/2)^2/(2t)}.
\]

This follows by integrating the two derivatives from zero to \(\theta\); throughout the interval their arguments have absolute value between \(a-\pi/2\) and \(a+\pi/2\). Dividing by the central term's factor \(e^{-\theta^2/(2t)}\), and using \(0<t\leq1\), gives the exact receiving bound


\[
 p_t(\theta)=
 \frac{\sqrt{2\pi}}{2t^{3/2}}e^{t/2}
 \frac{\theta}{\sin\theta}e^{-\theta^2/(2t)}
 [1+r_t(\theta)],\qquad
 |r_t(\theta)|\leq\delta(t):=\frac{C_*}{t}e^{-\pi^2/t},
\]


\[
 C_*=2\sum_{k=1}^{\infty}
   [1+(2\pi k+\pi/2)^2]e^{-\pi^2(2k^2-k-1)}.
 \tag{DP.21}
\]


Indeed \(((a-\pi/2)^2-(\pi/2)^2)/(2t)=\pi^2(2k^2-k)/t\). Extract \(e^{-\pi^2/t}\); the remaining exponent can be bounded with \(t\leq1\), since \(2k^2-k-1\geq0\). This checks every exponent and the zero-angle derivative in HK.9.

One can make its stated small-time range completely explicit: \(C_*<129\), and \(\delta(t)<129/512<1/2\) for every \(0<t\leq1\). To prove the first bound, use \(9<\pi^2<10\) and

\[
 2[1+(2\pi k+\pi/2)^2]\leq128k^2,\quad
 2k^2-k-1\geq5(k-1),\quad k^2\leq4^{k-1}\quad(k\geq1).
\]

The middle inequality is \(2(k-1)(k-2)\geq0\); the last follows by induction. Since \(e>2\), \(e^{-45}<1/1024\), whence

\[
 C_*<128\sum_{k=1}^{\infty}(4/1024)^{k-1}
       =\frac{32768}{255}<129.
\]

For the second bound, \(t^{-1}e^{-\pi^2/t}\) is increasing on \((0,1]\), because its derivative has the sign of \(\pi^2-t>0\). Thus \(\delta(t)\leq C_*e^{-\pi^2}<129e^{-9}<129/512\). The strict geometric bound is intentionally elementary; the exact \(C_*\) and \(\delta(t)\) remain in (DP.21).

## DP.13. Quantitative radial limit and Gaussian tails

Put \(W(g)=2-\operatorname{tr}g=2(1-\cos\theta)\). Under \(p_t\,d\mu\), let \(h_t(r)\) denote the density of \(r=\theta/\sqrt t\), extended by zero beyond \(\pi/\sqrt t\). Multiplying (DP.21) by the exact radial Haar density and \(d\theta=\sqrt t\,dr\), on \(0\leq r\leq b_t:=\pi/(2\sqrt t)\), gives


\[
 h_t(r)=f(r)e^{t/2}\frac{\sin(\sqrt t\,r)}{\sqrt t\,r}
       [1+r_t(\sqrt t\,r)],\qquad
 f(r)=\sqrt{\frac2\pi}\,r^2e^{-r^2/2}.
 \tag{DP.22}
\]


All endpoint quotients take their continuous value. The Gaussian integral and integration by parts give \(\int_0^\infty f=1\), \(\int r^2f=3\), and \(\int r^4f=15\). The exact expectation from (DP.19) is \(\mathbb E_tW=2-2e^{-3t/2}\). Since \(W\geq2\) for \(\theta\geq\pi/2\),

\[
 \mathbb P_t(\theta\geq\pi/2)\leq1-e^{-3t/2}\leq\frac32t.
\]

On the central interval \(0\leq\sin z/z\leq1\) and \(1-\sin z/z\leq z^2/6\). The latter follows from \(z-\sin z=\int_0^z(1-\cos u)du\leq z^3/6\). Consequently


\[
 \int_0^\infty|h_t(r)-f(r)|dr\leq
 \mathcal B(t):=(e^{t/2}-1)+e^{t/2}\left(\frac t2+\delta(t)\right)
       +(1-e^{-3t/2})+\mathcal G(b_t),\quad 0<t\leq1,
\]


\[
 \mathcal G(R)=\sqrt{\frac2\pi}
 \left(Re^{-R^2/2}+\int_R^\infty e^{-u^2/2}du\right)
 \leq\sqrt{\frac2\pi}(R+R^{-1})e^{-R^2/2},\quad R>0.
 \tag{DP.23}
\]


The central-interval bound follows by writing
\(e^{t/2}\operatorname{sinc}(\sqrt t r)(1+r_t)-1\) as the sum of \(e^{t/2}-1\), the sinc difference and the remainder; integrate their bounds against \(f\). Outside it the integral of \(h_t\) is the omitted-region probability and that of \(f\) is \(\mathcal G(b_t)\). Integration by parts yields \(\mathcal G\); its last estimate follows from \(u/R\geq1\) on the remaining integral. Thus \(\mathcal B(t)\to0\), with every term explicit. Total variation distance is at most \(\mathcal B(t)/2\), by the definition using half the density \(L^1\) norm.

The same density bound gives, for all \(R>0\) and \(0<t\leq1\),


\[
 \mathbb P_t(\theta/\sqrt t\geq R)
 \leq\frac32e^{1/2}\mathcal G(R)+\frac32t,\qquad
 \mathbb P_t(W/t\geq R^2)
 \leq\frac32e^{1/2}\mathcal G(R)+\frac32t.
 \tag{DP.24}
\]


If \(R\leq b_t\), integrate the central majorant and add the omitted mass. If \(R>b_t\), the entire event lies in that omitted region, so the same bound still holds. The second inequality uses \(W=4\sin^2(\theta/2)\leq\theta^2\).

The distribution of \(W/t\) tends to the law with density

\[
 f_Y(y)=\frac1{\sqrt{2\pi}}y^{1/2}e^{-y/2}\mathbf1_{\{y>0\}}.
 \tag{DP.25}
\]

There is a quantitative verification: for every bounded function \(\psi\) with \(\|\psi\|_\infty\leq1\) and Lipschitz constant at most one, set
\(T_t(r)=2(1-\cos(\sqrt t r))/t\). Taylor's integral remainder gives
\(0\leq r^2-T_t(r)\leq tr^4/12\) for all \(r\geq0\); the upper bound also follows by integrating \(0\leq x^2/2-(1-\cos x)\leq x^4/24\). Replacing \(h_t\) by \(f\) first therefore yields

\[
 \left|\mathbb E_t\psi(W/t)-\int_0^\infty\psi(r^2)f(r)dr\right|
 \leq\mathcal B(t)+\frac54t.
\]

To pass to every bounded continuous \(\psi\), truncate to a compact interval using (DP.24) and the Gaussian tail, uniformly approximate \(\psi\) there by a polygonal function, and extend that function constantly beyond the interval. The error of the approximation and both tails can be made arbitrarily small. The change \(y=r^2\), with \(dr=dy/(2\sqrt y)\), gives (DP.25). Its integral is one, and it has no atom at zero. This independently proves CN.2 and verifies its tail justification quantitatively.

## DP.14. A small-ball bound that proves the null-set claim directly

The null-set proof also admits a route independent of the scaled-limit calculation. For \(0<t\leq1\), substitute \(k=n+1\) in \(M_t\). On \(x\in[k-1,k]\), \(k^2\leq(x+1)^2\) and \(e^{-tk^2/2}\leq e^{-tx^2/2}\). Hence


\[
 M_t=e^{t/2}\sum_{k=1}^\infty k^2e^{-tk^2/2}
 \leq e^{t/2}\left[
 \sqrt{\frac\pi2}t^{-3/2}+2t^{-1}
       +\sqrt{\frac\pi2}t^{-1/2}\right]
 \leq K_0t^{-3/2},\quad
 K_0=e^{1/2}\left(2\sqrt{\frac\pi2}+2\right).
 \tag{DP.26}
\]


For \(0\leq\theta\leq\pi\), concavity of sine on \([0,\pi/2]\) gives
\(W=4\sin^2(\theta/2)\geq4\theta^2/\pi^2\). Thus \(W\leq w\) implies \(\theta\leq(\pi/2)\sqrt w\). Integrating \(\sin^2\theta\leq\theta^2\) in (DP.2) and using (DP.26) proves


\[
 \mathbb P_t(W\leq w)\leq
 \min\left\{1,Q_0(w/t)^{3/2}\right\},\qquad
 Q_0=\frac{\pi^2K_0}{12},\quad w\geq0,\quad 0<t\leq1.
 \tag{DP.27}
\]


If the implied angle bound exceeds \(\pi\), extending the elementary cubic upper integral to that bound still gives a valid inequality; taking the minimum with one handles all \(w\). At \(w=0\), Haar has no atom at \(I\), so both sides give zero. This bound retains the actual dimension-three small-ball power and the original time.

For the nested corner rectangles \(R_m=[0,L_1/2^m]\times[0,L_2/2^m]\), let

\[
 a_m=L_1L_2\,4^{-m},\quad t_m=g_2^2a_m/4,\quad
 W_m=2-\operatorname{tr}H_{\partial R_m}.
\]

Their individual laws are exactly those used in (DP.27), by (DP.19). In particular, whenever \(t_m\leq1\),


\[
 \mu_\infty(W_m/a_m\leq\varepsilon)
 \leq \min\left\{1,Q_0(4\varepsilon/g_2^2)^{3/2}\right\},
 \qquad \varepsilon\geq0.
 \tag{DP.28}
\]


The dimensions are consistent: \(W_m\) is dimensionless, \(W_m/a_m\) and \(\varepsilon\) have units length\(^{-2}\), so \(4\varepsilon/g_2^2\) is dimensionless.

## DP.15. The explicit Borel null set and stronger almost-sure bounds

Define


\[
 \mathcal E=
 \bigcap_{k=1}^\infty\ \bigcup_{N=0}^\infty\
       \bigcap_{m\geq N}\{W_m/a_m<g_2^2/k\}
 =\{U:W_m(U)/a_m\longrightarrow0\}.
 \tag{DP.29}
\]


Each \(W_m\) is continuous on \(X_\infty\), so this is Borel. For every fixed \(\varepsilon>0\), its indicators \(\mathbf1_{\mathcal E}\mathbf1_{\{W_m/a_m<\varepsilon\}}\) converge pointwise to \(\mathbf1_{\mathcal E}\). Bounded convergence and (DP.28) give
\(\mu_\infty(\mathcal E)\leq Q_0(4\varepsilon/g_2^2)^{3/2}\). Letting \(\varepsilon\downarrow0\) proves \(\mu_\infty(\mathcal E)=0\). The CN.2 distribution limit proves the same statement because its limiting law has no zero atom; (DP.28) additionally supplies an explicit bound at each sufficiently fine level. Neither proof assumes independence of the nested loops.

For a quantitative statement about exceptional resolutions, take \(\delta,K>0\) and \(M\) with \(t_M\leq1\). The union bound and (DP.27) yield


\[
 \mu_\infty\{\text{some }m\geq M:W_m\leq Kt_m^{1+\delta}\}
 \leq \frac{Q_0K^{3/2}t_M^{3\delta/2}}{1-4^{-3\delta/2}}.
 \tag{DP.30}
\]


The right side tends to zero as \(M\to\infty\). Thus only finitely many of these events occur almost surely; this is the first Borel–Cantelli implication proved here directly by the tail union estimate. Taking all positive integer \(K\) gives \(W_m/t_m^{1+\delta}\to\infty\) almost surely for each fixed \(\delta>0\). Taking a countable intersection over positive rational \(\delta\) makes this true simultaneously for all real \(\delta>0\): choose a smaller positive rational exponent and use \(t_m\to0\). This strengthening excludes every fixed faster-than-area power of \(W_m\) almost surely.

For an upper bound, choose \(q>1\), \(R_m=\sqrt{2q\log(m+2)}\), and use (DP.24). The series of Gaussian terms is bounded by a constant times


\[
\sum_m[(\log(m+2))^{1/2}+(\log(m+2))^{-1/2}](m+2)^{-q}
\]

, which converges: eventually \((\log x)^{1/2}\leq x^{(q-1)/2}\), proved by comparing the exponential series with a power after setting \(x=e^y\). Also \(\sum_m t_m<\infty\). The same tail-union argument gives

\[
 W_m/t_m<2q\log(m+2)\quad\text{eventually, almost surely}.
\]

This statement concerns \(m\) as the resolution index, not physical time. It supplies no independence claim or missing all-path regularity.

## DP.16. The actual continuous-connection holonomy map

Let
\(\mathcal A^0=C(D,\mathfrak{su}(2))^2\), with the maximum of the two operator-norm suprema. This definition also covers restrictions of connections on a neighbourhood of \(D\). On each oriented coordinate segment, parametrized by arclength \(s\), solve

\[
 U'(s)=-B_A(s)U(s),\qquad U(0)=I,\qquad
 B_A(s)=A_\mu(\gamma(s))\dot\gamma^\mu(s).
 \tag{DP.31}
\]

The iterated integral series converges uniformly since its degree-\(r\) term has norm at most \((\ell M)^r/r!\), where \(M=\|A\|_\infty\) and \(\ell\) is length. Its sum solves the integral equation. Applying the same iteration to a difference with zero initial data bounds it by a fixed supremum times \((\ell M)^r/r!\) for every \(r\), proving uniqueness. Differentiating \(U^*U\) gives zero since \(B_A^*=-B_A\). The determinant derivative then gives \((\det U)'=-\operatorname{tr}(B_A)\det U=0\), so \(U\in SU(2)\). Reversal gives the inverse by the reversed differential equation. Gluing segment solutions and using uniqueness proves the exact subdivision and word laws.

Consequently there is a defined map

\[
 \operatorname{Hol}:\mathcal A^0\longrightarrow X_\infty,\qquad
 [\operatorname{Hol}(A)]^m_e=U_A(e).
 \tag{DP.32}
\]

It is continuous. Indeed differentiation of \(U_A(s)^*U_B(s)\), or integration of its derivative, gives
\(\|U_A(e)-U_B(e)\|\leq\ell_e\|A-B\|_\infty\), since both propagators are unitary. Products give the corresponding bound by total coordinate-path length. Thus each coordinate is continuous, and the weighted product metric proves continuity of (DP.32).

The map is injective. For each point \(x\in D\) and coordinate \(\mu\), choose a designated \(\mu\)-edge \(e_m\) whose endpoints approach \(x\); at the top/right boundary choose the nearest edge on the inside. Its length is \(\ell_m=L_\mu/2^m\). The integral equation, uniform continuity of \(A_\mu\), and \(\|U_A(s)-I\|\leq sM\) give

\[
 \left\|\frac{I-U_A(e_m)}{\ell_m}-A_\mu(x)\right\|
 \leq\sup_{y\in e_m}\|A_\mu(y)-A_\mu(x)\|+\frac12\ell_mM^2
 \longrightarrow0.
\]

Equal dyadic holonomies therefore determine equal values of both components at every \(x\), including the boundary.

For \(C^1\) gauge transformations \(h:D\to SU(2)\), differentiating \(h(\gamma(s))U_A(s)h(\gamma(0))^{-1}\) gives the transport equation for \(A^h=hAh^{-1}-dh\,h^{-1}\). Hence (DP.32) intertwines this actual classical gauge map with the vertex gauge map in DP.10, with the same forward minus sign.

## DP.17. The original \(C^1\) curvature bound, with its constants

Let \(A\in C^1(D,\mathfrak{su}(2))^2\), and \(F_{12}=\partial_1A_2-\partial_2A_1+[A_1,A_2]\); write \(M_F=\sup_D\|F_{12}\|\). For any cell \([0,b_1]\times[0,b_2]\) in local coordinates \((s,r)\), solve

\[
 u_r(0,r)=u(0,r)A_2(0,r),\quad u(0,0)=I,\qquad
 u_s(s,r)=u(s,r)A_1(s,r).
\]

The same convergent integral argument gives a unitary \(u\), with \(u_r\) obtained by differentiating the horizontal integral equation, since \(A\) has continuous first derivatives. Put
\(\widetilde A_\mu=uA_\mu u^{-1}-(\partial_\mu u)u^{-1}\).
Then \(\widetilde A_1=0\) and \(\widetilde A_2(0,r)=0\). Directly differentiating \(\widetilde A_2\) in \(s\), using
\(\partial_su=uA_1\) and
\(\partial_s\partial_ru=(\partial_ru)A_1+u\partial_rA_1\), gives

\[
 \partial_s\widetilde A_2(s,r)=u(s,r)F_{12}(s,r)u(s,r)^{-1},\qquad
 \widetilde A_2(b_1,r)=\int_0^{b_1}uF_{12}u^{-1}(s,r)\,ds.
\]

Only these existing mixed derivatives are used; no second derivative of \(A\) is required.

Bottom, top and left transports in this gauge equal \(I\); the positive boundary is the right-edge transport upward. Its integral equation and unitarity yield

\[
 \|H_{\partial R}-I\|\leq b_1b_2M_F,\qquad
 W(H_{\partial R})=\tfrac12\|I-H_{\partial R}\|_{\rm HS}^2
       \leq(b_1b_2)^2M_F^2.
 \tag{DP.33}
\]

The original basepoint gauge is \(u(0,0)=I\), so this is its actual original matrix; at other starting frames the norm and trace are unchanged by conjugation. The Hilbert–Schmidt bound is \(\|X\|_{\rm HS}\leq\sqrt2\|X\|\), hence exactly the coefficient one in (DP.33).

Applying (DP.33) to \(R_m\) gives \(W_m/a_m\leq a_mM_F^2\to0\). Therefore every such \(C^1\) holonomy belongs to the Borel null set \(\mathcal E\), proving CN.3 with the actual curvature factor and without supposing the holonomy image is Borel.

## DP.18. Strengthening to every continuous connection

Derivatives and curvature are unnecessary for membership in \(\mathcal E\). For \(A\in\mathcal A^0\), set \(M=\|A\|_\infty\) and

\[
 \omega_\mu(\rho)=
 \sup\{\|A_\mu(x)-A_\mu(y)\|:x,y\in D,\ |x-y|\leq\rho\}.
\]

Uniform continuity on the compact rectangle proves \(\omega_\mu(\rho)\to0\). For a positive rectangle with sides \(b_1,b_2\), concatenate its four arclength transports into (DP.31); the piecewise continuous coefficient has norm at most \(M\), and total length \(P=2(b_1+b_2)\). The integral equation and unitarity give \(\|U(s)-I\|\leq Ms\) and therefore the exact first-order remainder

\[
 \left\|H_{\partial R}-I+\oint_{\partial R}A\right\|
 \leq\int_0^P M\,\|U(s)-I\|ds\leq\frac12M^2P^2.
\]

The four signed line integrals cancel in pairs up to

\[
 \left\|\oint_{\partial R}A\right\|
 \leq b_1\omega_1(b_2)+b_2\omega_2(b_1).
\]

This follows by writing the bottom-minus-top horizontal integral and right-minus-left vertical integral separately; signs agree with the positive orientation and the forward minus transport. Consequently


\[
 \|H_{\partial R}-I\|
 \leq b_1\omega_1(b_2)+b_2\omega_2(b_1)
       +2M^2(b_1+b_2)^2.
 \tag{DP.34}
\]


For the actual \(R_m\), divide by \(\sqrt{a_m}\) to retain the aspect ratio:

\[
 \frac{\|H_{\partial R_m}-I\|}{\sqrt{a_m}}
 \leq
 \sqrt{\frac{L_1}{L_2}}\omega_1(L_2\,2^{-m})
 +\sqrt{\frac{L_2}{L_1}}\omega_2(L_1\,2^{-m})
 +\frac{2M^2(L_1+L_2)^2}{\sqrt{L_1L_2}}\,2^{-m}
 \longrightarrow0.
\]

Since \(W\leq\|I-H\|^2\) for these \(2\times2\) unitaries, it follows that

\[
 \operatorname{Hol}(\mathcal A^0)\subset\mathcal E,\qquad
 \mu_\infty(\mathcal E)=0.
 \tag{DP.35}
\]

This is a strict weakening of the source's sufficient regularity hypothesis, with a complete comparison to the same original holonomy map. In fact each vertex-gauge orbit of this entire image is contained in \(\mathcal E\), because the loop trace is invariant under every vertex gauge function, including those with no smooth extension.

It also follows that there is no Borel probability \(\nu\) on \(\mathcal A^0\) with \(\operatorname{Hol}_*\nu=\mu_\infty\): the measurable set \(\operatorname{Hol}^{-1}(\mathcal E)\) is all of \(\mathcal A^0\), while \(\mu_\infty(\mathcal E)=0\). This argument uses continuity of the actual map and never requires its image to be Borel.

## DP.19. The null image is dense; all finite smooth realizations

The null-set statement is compatible with full support, and there is an exact construction proving more: every \(U\in X_m\) is realized by a \(C^\infty\) connection defined on a neighbourhood of \(D\). For each designated edge \(e\), select \(X_e\in\mathfrak{su}(2)\) with \(e^{X_e}=U_e\). Such an \(X_e\) exists explicitly: if \(U_e=\cos\theta I+i\sin\theta\,\boldsymbol n\cdot\boldsymbol\sigma\), choose \(X_e=i\theta\boldsymbol n\cdot\boldsymbol\sigma\); at \(I\) choose zero, at \(-I\) choose any unit direction with \(\theta=\pi\). No continuous choice across \(U_e=-I\) is required for this finite existence assertion.

Take a compact subinterval of the interior of each edge. The finitely many such subintervals are disjoint and separated from every other edge not containing them; choose disjoint thin open tubes meeting no other grid edge. In the oriented coordinates \(s,r\) of the tube choose smooth compactly supported functions \(\rho_e(s)\), \(\eta_e(r)\), with \(\int\rho_e(s)ds=1\) and \(\eta_e(0)=1\). Define globally, extending each tube contribution by zero,

\[
 A=-\sum_{e\in E_m}X_e\rho_e(s)\eta_e(r)\,ds.
 \tag{DP.36}
\]

The supports stay away from vertices. Each coefficient is smooth on the ambient plane, and on edge \(e\) its transport equation is \(U'=X_e\rho_e(s)U\), so the transport is \(e^{X_e\int\rho_e ds}=U_e\). Other contributions vanish along that edge. This proves the finite realization including boundary edges. The coefficient \(\rho_e\) has units length\(^{-1}\), so the connection retains the original physical component units.

Any nonempty finite-cylinder neighbourhood in \(X_\infty\) is determined by an open condition at one largest level and contains some chosen \(U\) at that level. The preceding construction places \(\operatorname{Hol}(A)\) inside it. Hence \(\operatorname{Hol}(C^\infty)\) and \(\operatorname{Hol}(\mathcal A^0)\) are dense in \(X_\infty\), although both are contained in \(\mathcal E\) of measure zero. The full receiving space and its exact maps therefore describe both the deterministic classical objects and the probability law; nullness is a probability statement, not a loss of finite smooth realizability.

## DP.20. Source convention correction and comparison verdict

The retained author TeX chap1.tex lines 224–352 uses the same reversed matrix order for path traversal. Its vertex gauge variable \(j_v\) acts by \(j_{t(e)}^{-1}U_ej_{s(e)}\); our exact variable map is \(j_v=h_v^{-1}\). Lines 575–798 prove subdivision by the same edge and chord integrations. At line 585 the printed convolution uses \(p_s,p_t\) and result \(p_t\); with those two factors it must be \(p_{s+t}\). Lines 713–722 actually add the two face areas. The independent formula (DP.9) preserves the raw order \(BA\); the source's \(AB\) inside a central density is equivalent because \(AB=A(BA)A^{-1}\). Chap2.tex lines 1–68 invokes an external projective-limit theorem. DP.6–DP.10 supply the complete construction in this countable scope and do not import that cited theorem or unread all-path results.

The following source-convention comparison is incorporated in the current HK.11 and GP.15. Chap1.tex lines 324–325 explicitly describes its bi-invariant Riemannian metric as having total volume one. An earlier draft of HK.11 and GP.15 described its metric as otherwise arbitrary and chose it equal to \(\kappa\). Those are different metric conventions: \(\kappa\) has volume \(V_\kappa=4\sqrt2\pi^2\).

For SU(2), an invariant inner product on the Lie algebra is a positive scalar multiple of \(\kappa\). To verify this directly, conjugations by \(e^{i\theta\sigma_a}\) rotate the other two Pauli coordinates through angle \(2\theta\). Invariance under those three coordinate-plane rotations forces the quadratic-form matrix to be diagonal with equal diagonal entries. If a three-dimensional metric is multiplied by \(b>0\), its volume form multiplies by \(b^{3/2}\) and its Laplacian by \(b^{-1}\): these follow respectively from the determinant and from \(|g|^{-1/2}\partial_i(|g|^{1/2}g^{ij}\partial_j)\), with \(b\) constant. Thus the author's literal volume-one SU(2) metric and half-Laplacian parameter satisfy


\[
 \kappa_{\mathrm L}=V_\kappa^{-2/3}\kappa,\quad
 \Delta_{\mathrm L}=V_\kappa^{2/3}\Delta_\kappa,\quad
 p_s^{\mathrm L}=p_{V_\kappa^{2/3}s/2},\quad
 s_{\mathrm L}=\frac{2t}{V_\kappa^{2/3}}
       =\frac{g_2^2|f|}{2V_\kappa^{2/3}}.
 \tag{DP.37}
\]


Both kernels are densities with respect to the same Haar probability: the volume-one metric's Riemannian measure is \(V_\kappa^{-1}d\mathrm{vol}_\kappa=d\mu\). The identity in (DP.37) follows either from their harmonic coefficients or from the explicitly rescaled differential equation and initial kernel. Every factor is therefore fixed, rather than absorbed into the measure or coupling.

The separate statement “use the half-Laplacian with the same metric \(\kappa\)” has kernel \(p^{(\kappa,1/2)}_s=p_{s/2}\) and time \(s=2t=g_2^2|f|/2\). That is a valid comparison convention, but it must be identified as a change from the author's literal volume-one metric. If “volume one” were intended solely as a probability normalization of volume rather than of metric, this latter dictionary describes that alternate reading; the literal metric reading and the same-metric comparison must not be conflated. In either presentation the course's actual \(p_t\), \(t=g_2^2|f|/4\), finite laws, physical factors, and all results above remain unchanged.

The original GP.1–GP.16 construction and CN.1–CN.5 regularity conclusion are mathematically valid in their stated \(L_1,L_2,g_2>0\), countable-path domain, with the source-metric comparison correction just proved and incorporated in this edition. An earlier draft of equation G7 had a mechanical space in its product command, corrected in this edition; (DP.8) records the complete intended product. The present proof adds explicit sampler and heat-tail bounds, the Borel small-ball proof, all continuous-connection holonomies in the same null set, and dense smooth realizability. These are proved strengthenings, not claims of novelty.

At \(g_2=0\) or a degenerate whole rectangle, the positive-time hypotheses of the given density and rejection construction do not hold. No such case is silently included: the theorem assumes the stated positive parameters. Individual zero-area retraced loops within the positive rectangle were handled explicitly in DP.11. The two-dimensional construction does not identify a four-dimensional quantum measure or infer a mass gap.


## CN.1. The scale of a shrinking holonomy

Under \(p_t(g)d\mu(g)\), let \(\theta\in[0,\pi]\) be its conjugacy angle and \(W(g)=2-\operatorname{tr}g=2(1-\cos\theta)\). HK.10 proves

\[
 \mathbb E W=2-2e^{-3t/2}=3t+O(t^2),\qquad
 \mathbb E W^2=5-8e^{-3t/2}+3e^{-4t}=15t^2+O(t^3).
\]

The scale is \(W\) of order \(t\), and hence order physical area by (A5). An expectation alone would not justify an almost-sure regularity conclusion, so CN.2 proves the actual limiting distribution.

## CN.2. A proved scaled distribution, with its probability density

On \(0\leq\theta\leq\pi/2\) use (H11)–(H13), the radial Haar formula (H3), and the variable \(r=\theta/\sqrt t\). The radial density with respect to \(dr\) becomes exactly

\[
 \sqrt{\frac2\pi}\,r^2e^{-r^2/2}e^{t/2}
 \frac{\sin(\sqrt t\,r)}{\sqrt t\,r}\,[1+r_t(\sqrt t\,r)]
 \mathbf1_{\{0\leq r\leq\pi/(2\sqrt t)\}}.
\]

At zero use the continuous limit. For all sufficiently small \(t\), the absolute value is bounded by a fixed constant times \(r^2e^{-r^2/2}\), using \(|\sin z/z|\leq1\), \(|r_t|\leq\delta(t)\to0\). It tends pointwise to
\(f(r)=\sqrt{2/\pi}\,r^2e^{-r^2/2}\), whose integral on \([0,\infty)\) is one by the Gaussian integral and integration by parts. The probability of the omitted region tends to zero: \(W\geq2\) when \(\theta\geq\pi/2\), so its probability is at most \(\mathbb EW/2\to0\). Dominated convergence proves convergence of expectations of every bounded continuous function of \(\theta/\sqrt t\) to its integral against \(f\).

Moreover \(2(1-\cos(\sqrt t\,r))/t\to r^2\) uniformly for bounded \(r\); the tail is uniformly small by the same integrable majorant and the omitted-region estimate. Thus \(W/t\) converges in distribution to \(Y=r^2\), with density

\[
 f_Y(y)=\frac1{\sqrt{2\pi}}\,y^{1/2}e^{-y/2}\mathbf1_{\{y>0\}}.
\]

This is the sum-of-three-squared-unit-Gaussians distribution, but the displayed derivation is the needed provider. It has no atom at zero and has a continuous distribution function at every nonnegative argument. In particular its mean is three and its second moment is fifteen, agreeing with CN.1.

## CN.3. A Borel null set containing all \(C^1\) connection holonomies

Inside the continuum probability space of GP.11, let \(R_m=[0,L_1/2^m]\times[0,L_2/2^m]\), with area \(a_m=L_1L_2/4^m\), and put \(W_m=2-\operatorname{tr}H_{\partial R_m}\). GP.7 and compatibility give its exact marginal heat time \(t_m=g_2^2a_m/4\). By CN.2, \(W_m/a_m\) converges in distribution to \((g_2^2/4)Y\), a positive random variable with no atom at zero.

Define the Borel subset \(E=\{U:\lim_m W_m(U)/a_m=0\}\) of \(X_\infty\); it is Borel by the countable epsilon definition of a sequence limit. For any \(\epsilon>0\), the indicators of \(\{W_m/a_m<\epsilon\}\) tend to one on \(E\). Dominated convergence on \(E\) gives

\[
 \mu_\infty(E)\leq\liminf_m\mu_\infty(W_m/a_m<\epsilon)
 =\mathbb P((g_2^2/4)Y<\epsilon).
\]

Let \(\epsilon\downarrow0\); the right side tends to zero. Hence \(\mu_\infty(E)=0\). No independence between these nested loops was assumed or needed.

Every fixed \(C^1\) connection on a neighbourhood of \(D\) maps into \(E\). Its curvature is continuous and bounded. The local axial-transport part of AC.2 uses only that regularity to give \(\|P-I\|\leq a_mM_F\), hence \(W_m\leq a_m^2M_F^2\). Therefore \(W_m/a_m\to0\). The construction of its compatible holonomy sequence is GP.1–GP.2 plus uniqueness of the transport ODE; splitting a segment gives the same solution by that uniqueness. Thus the entire image of these \(C^1\) connections is contained in an explicitly exhibited Borel null set. This is stronger and more precise than asserting an unsupported density on a space of smooth fields. It does not require that the image itself be Borel.

## CN.4. Why the classical action comparison remains valid

Equation (A7) proves convergence of field-dependent heat actions for each fixed smooth connection, including its full retained multiplier. CN.3 proves that the resulting probability measure gives a Borel null set to all these smooth holonomy configurations. The two statements are compatible: the former evaluates a finite-density function along a specified deterministic family of configurations, while the latter calculates the law of the compatible random configurations. Their exact common map is the smooth-connection-to-path-holonomy map proved in AC.2 and GP.12. No formal continuum measure \(\mathcal D A\) on smooth connections is needed or inferred.

The obstruction defines a concrete receiving space: \(X_\infty\), the compatible multiplicative group-valued path maps, with the probability law constructed in GP.8–GP.11. It retains all smooth holonomy images as a subset, and supports the random holonomies actually constructed. This gives both the inclusion map and the proved failure of probability concentration on its smooth image.

## CN.5. Joint consequence and literature scope

Exact heat convolution, not a generic positive plaquette density, is what supplies consistency under face subdivision. The Wilson density has the same proved classical limit but fails that exact convolution by AC.5. Together these results show that equality of the leading classical action alone does not determine an exact refinement law. The invariant finite laws, compatible continuum law and smooth-image obstruction have all been proved for the specific SU(2) dyadic rectangle model. Lévy's original-author source supplies the established broader heat-kernel gauge-measure context and the subdivision mechanism; this note claims neither novelty nor the broader results whose source proofs were not read. It supplies no four-dimensional continuum theory, mass gap, or transfer of a two-dimensional area law to four dimensions.
