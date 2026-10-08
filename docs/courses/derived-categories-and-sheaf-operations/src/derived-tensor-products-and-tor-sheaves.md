# The derived tensor product and Tor sheaves

*Written and edited by GPT-6.1 Sol (OpenAI), in Codex at Ultra, October 2026. Mathematically self-checked by the writing AI. Original text: public domain (CC0). Authorship and sources are listed in the [course notice](../LICENCE.md).*

Ordinary tensor products preserve quotients, but can lose an injection. For example, tensoring \(\mathbb Z\xrightarrow{2}\mathbb Z\) with \(\mathbb Z/2\) turns an injection into the zero map. A resolution keeps the lost information in negative cohomological degrees. The derived tensor product packages this information without depending on a chosen resolution, and Tor sheaves name its cohomology for two module sheaves.

The prerequisite is [Flat modules and K-flat resolutions](flat-modules-and-k-flat-resolutions.md), Lemmas 1.1–1.3 and 2.1–2.4, Theorem 3.1, Lemmas 3.2 and 4.1, and Lemma 4.5. We also use its earlier prerequisite, [Complexes, cones and localization](complexes-cones-and-localization.md), Theorems 4.2 and 5.1 and Proposition 5.2. In particular, roofs and their common refinements have already been proved, rather than assumed.

Throughout, \(X\) is an arbitrary topological space and \(\mathcal O\) is a sheaf of **commutative unital rings**. Complexes are cohomologically indexed and can be unbounded in both directions. Their tensor product means the direct-sum totalization

\[
\begin{aligned}
(A\otimes B)^n&=\bigoplus_{p+q=n}A^p\otimes_{\mathcal O}B^q,\\
d(a\otimes b)&=d_Aa\otimes b\\
&\quad+(-1)^p a\otimes d_Bb .
\end{aligned}
\tag{0.1}
\]

We write \(K(\mathcal O)\) for the homotopy category, \(D(\mathcal O)\) for its localization at quasi-isomorphisms, and \(Q\) for localization. Cone triangles have the convention \((f,i,-p)\) of the common reading. No compactness, separation, finite dimension or Noetherian assumption enters the construction.

The construction follows the Stacks project authors’ *Cohomology of Sheaves*, “Flat resolutions”, especially Tags 06YG, 06YH, 08BP and 08BQ, in the [AI Integrated Stacks Project edition](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/cohomology.tex). We prove the comparison and coherence maps before defining Tor sheaves. Source attribution appears in the [course notice](../LICENCE.md).
## 1. The two tensor comparisons

A K-flat complex \(P\) has \(A\otimes P\) acyclic whenever \(A\) is acyclic. The two variables in a tensor comparison play different roles.

**Lemma 1.1 (tensor invariance).** If \(P\) is K-flat and \(u:A\to B\) is a quasi-isomorphism, then \(u\otimes1_P\) is a quasi-isomorphism. If \(v:P\to P'\) is a quasi-isomorphism **between K-flat complexes**, then \(1_G\otimes v\) is a quasi-isomorphism for every complex \(G\).

**Proof.** Lemma 2.1 of the K-flat lesson identifies the tensor of a cone with the cone of the tensored map. When the cone is in the second variable, the shifted summand acquires the factor \((-1)^{|a|}\); the graded flip gives the other variable. The cone of \(u\) is acyclic, so its tensor with \(P\) is acyclic. This proves the first assertion.

For the second, choose a K-flat resolution \(R\to G\), using Theorem 3.1 of that lesson. Consider the commuting square

\[
\begin{array}{ccc}
R\otimes P&\longrightarrow&R\otimes P'\\
\downarrow&&\downarrow\\
G\otimes P&\longrightarrow&G\otimes P'.
\end{array}
\tag{1.1}
\]

Both vertical maps are quasi-isomorphisms by the first assertion, using respectively \(P\) and \(P'\). The top map is one because \(R\) is K-flat, after interchanging the tensor factors. On every cohomology sheaf, three arrows are isomorphisms and the square commutes; the fourth is therefore an isomorphism. This proves the second assertion for arbitrary, possibly unbounded and nonflat, \(G\). In particular an acyclic K-flat complex tensors acyclicly with every complex, by applying this assertion to its map to zero. \(\square\)

The second assertion would be false for an arbitrary quasi-isomorphism in place of \(v\). For example \((\mathbb Z\xrightarrow{2}\mathbb Z)\to\mathbb Z/2[0]\), in degrees \(-1,0\), becomes a map from a zero-differential two-term complex to a one-term complex after tensoring with \(\mathbb Z/2\). It loses an isomorphism in degree \(-1\). Its target is not K-flat.

**Theorem 1.2 (one-variable definition and independence).** For a K-flat resolution \(\epsilon:P\to F\), the rule \(G\mapsto G\otimes P\) defines an exact functor

\[
-\otimes_{\mathcal O}^{\mathbf L}F:D(\mathcal O)\longrightarrow D(\mathcal O).
\tag{1.2}
\]

The functors from different resolutions have canonical natural comparison isomorphisms satisfying the identity and cocycle laws. If \(R\to G\) is K-flat, both arrows in

\[
G\otimes P\ \longleftarrow\ R\otimes P\ \longrightarrow\ R\otimes F
\tag{1.3}
\]

are quasi-isomorphisms. Thus either variable, or both variables, may be resolved.

**Proof.** Tensor respects homotopies, shifts and cone triangles by Lemma 2.1 of the K-flat lesson. Lemma 1.1 shows that \(Q(-\otimes P)\) inverts quasi-isomorphisms, so the localization universal property, Theorem 4.2 of the common reading, gives (1.2). Theorem 5.1 there identifies distinguished triangles with images of cone triangles; their tensor images are distinguished, so the functor is exact.

For the comparison, first let \(\epsilon_i:P_i\to F\), \(i=1,2\), be termwise-surjective K-flat resolutions. Form the ordinary fibre product of complexes

\[
W=P_1\times_F P_2.
\tag{1.4}
\]

Its projection onto \(P_1\) is termwise surjective with kernel \(\ker\epsilon_2\); similarly for the other projection. Each kernel is acyclic, by the short exact cohomology sequence. Hence both projections are quasi-isomorphisms. Choose a termwise-surjective K-flat resolution \(T\to W\). Its maps \(r_i:T\to P_i\) are quasi-isomorphisms between K-flats. Lemma 1.1 gives a natural comparison \(c_{12}(G)\) from \(Q(G\otimes P_1)\) to \(Q(G\otimes P_2)\), given by

\[
c_{12}(G)=Q(1\otimes r_2)Q(1\otimes r_1)^{-1}.
\tag{1.5}
\]

Two choices \(T,T'\to W\) have a common refinement: resolve \(T\times_W T'\) by a termwise-surjective K-flat complex. The projections are again surjective quasi-isomorphisms. All maps to the \(P_i\) commute strictly, so after tensoring and inverting the refinement arrows the two formulas (1.5) agree.

For three resolutions, resolve \(P_1\times_F P_2\times_F P_3\). Its projections to the pairwise products are surjective quasi-isomorphisms, with acyclic kernels. The previous refinement argument allows every pairwise comparison to be computed through this one model. Cancelling the middle invertible arrow proves the cocycle law.

For the identity law put \(W=P\times_F P\). Its diagonal \(\delta:P\to W\) is a quasi-isomorphism, because either projection is one and its composite with \(\delta\) is the identity. Lemma 3.2 of the K-flat lesson enlarges \(\delta\) to a termwise-surjective K-flat resolution \(P\oplus D\to W\), with \(D\) contractible. The two maps from this resolution to \(P\) agree after precomposition with \(P\to P\oplus D\). Tensoring that inclusion with \(G\) gives an invertible derived map by Lemma 1.1. The two tensor maps therefore agree in the derived category, proving the identity law. The maps are natural in \(G\), first for chain maps and homotopies and then for roofs by localization.

If a chosen resolution is not termwise surjective, Lemma 3.2 of the K-flat lesson enlarges it by a contractible disk complex. Its inclusion into the enlargement is a quasi-isomorphism between K-flats over \(F\). Lemma 1.1 supplies the comparison to the enlargement. Here is compatibility for two enlargements \(E_1,E_2\) of \(P\). The inclusions give \(b:P\to W=E_1\times_F E_2\); it is a quasi-isomorphism because \(W\to E_1\) and \(P\to E_1\) are. Resolve \(W\) by a surjective \(T\to W\). The projection \(T\times_W P\to P\) is a surjective quasi-isomorphism, with kernel \(\ker(T\to W)\). Its other projection to \(T\) is a quasi-isomorphism by two out of three after composing into \(W\). Resolve this fibre product by a K-flat complex. Its commuting maps to \(P,T,E_1,E_2\), all quasi-isomorphisms between K-flats, show after tensoring that the comparison of the enlargements intertwines their inclusions from \(P\). This proves independence of the enlargement.

Finally the left arrow of (1.3) is a quasi-isomorphism because \(P\) is K-flat; the right one is a quasi-isomorphism because \(R\) is K-flat. This proves balancing. \(\square\)

## 2. Morphisms, associativity and symmetry

Choosing resolutions of objects does not by itself define the action on morphisms. We now justify that action and its compatibility with every comparison above.

**Lemma 2.1 (localizing the K-flat models).** Let \(K_{\rm fl}(\mathcal O)\) be the full subcategory of \(K(\mathcal O)\) on K-flat complexes, and let \(S_{\rm fl}\) consist of its quasi-isomorphisms. The inclusion induces an equivalence

\[
K_{\rm fl}(\mathcal O)[S_{\rm fl}^{-1}]
\ \simeq\ D(\mathcal O).
\tag{2.1}
\]

**Proof.** Lemma 2.4 of the K-flat lesson shows that this full subcategory contains zero and is closed under shifts, finite sums and cones. All fraction squares and cancellation constructions in Lemma 4.1 of the common reading use these operations. When their starting objects are K-flat, their new cone or shifted cone is therefore K-flat. Consequently the roof construction and equivalence by common refinements in Theorem 4.2 there apply within \(K_{\rm fl}\).

Every object of \(D(\mathcal O)\) is isomorphic to a K-flat resolution, proving essential surjectivity. A roof \(P\leftarrow Z\to R\) in the ambient homotopy category, with \(P,R\) K-flat, can be refined by a K-flat resolution \(T\to Z\). The composite \(T\to P\) is a quasi-isomorphism. Thus it has a roof entirely in \(K_{\rm fl}\), proving fullness. If two such roofs are equal in \(D(\mathcal O)\), Theorem 4.2 supplies a common refinement, possibly with a nonflat middle complex \(Z\). Resolve that \(Z\) by a K-flat \(T\). The composites are a common refinement within \(K_{\rm fl}\), proving faithfulness. These operations use homotopy classes of maps; strict equality of arbitrary resolution lifts is not assumed. \(\square\)

**Theorem 2.2 (the tensor bifunctor).** There is a bifunctor

\[
\otimes_{\mathcal O}^{\mathbf L}:
D(\mathcal O)\times D(\mathcal O)\longrightarrow D(\mathcal O)
\tag{2.2}
\]

exact in each variable, whose value is represented by \(P\otimes R\) for K-flat models of its two arguments. It has canonical associativity, symmetry and unit isomorphisms, and commutes with restriction to any open subset.

**Proof.** On \(K_{\rm fl}\times K_{\rm fl}\) use ordinary total tensor. It respects homotopies and sends a quasi-isomorphism in either variable to one by Lemma 1.1. Localize successively in each variable. To check that the two resulting morphism actions commute, first note that \(f\otimes1\) and \(1\otimes g\) commute for chain maps of degree zero. They therefore commute with inverse denominators too: invert either side of the commuting square. A general roof is a numerator followed by an inverse denominator. This proves the commuting rule for all pairs of roofs and defines a bifunctor on the two localizations. Lemma 2.1 transfers it to \(D(\mathcal O)\times D(\mathcal O)\).

Cones of maps between K-flats are K-flat. Cone squares and tensor shift comparisons thus prove exactness on their localization. More explicitly, any roof between K-flats can be written \(Qf\,(Qs)^{-1}\) with the middle object K-flat; its cone triangle is isomorphic to the image of the cone triangle of \(f\). Tensor preserves the latter, so it preserves the former. Theorem 1.2 identifies this bifunctor with the one-variable construction, including its resolution comparisons.

For three K-flat models \(P,R,T\), the ordinary association map is

\[
\begin{gathered}
(P\otimes R)\otimes T\longrightarrow P\otimes(R\otimes T),\\
(p\otimes r)\otimes t\longmapsto p\otimes(r\otimes t).
\end{gathered}
\tag{2.3}
\]

Its inverse removes the parentheses. Both totalizations have the same direct sum indexed by \(i+j+k=n\). Their differentials on an elementary tensor have the three terms with signs \(1,(-1)^i,(-1)^{i+j}\), so (2.3) is a chain isomorphism. The tensor product of two K-flats is K-flat by Lemma 2.4 of the previous lesson. Thus the left and right sides compute the two iterated derived products. Naturality for chain maps extends to roofs and inverse denominators as above, proving a natural derived associativity isomorphism.

For \(|p|=i\) and \(|r|=j\), symmetry is represented by

\[
c_{P,R}(p\otimes r)=(-1)^{ij}r\otimes p.
\tag{2.4}
\]

For the \(d_Pp\) term the two routes have sign exponents \((i+1)j\) and \(ij+j\); for the \(d_Rr\) term they have exponents \(i+i(j+1)\) and \(ij\), equal modulo two. This checks the chain-map equation. Its square has sign \((-1)^{2ij}=1\), giving its inverse. The unit is \(\mathcal O[0]\), which is K-flat; the usual multiplication \(P\otimes\mathcal O\to P\) is a chain isomorphism.

These identifications are coherent. For four factors every path around the associativity pentagon sends a tensor to the same tensor with the final parentheses. The unit triangle does the same after multiplying by the degree-zero scalar. In the symmetry hexagon, moving a degree-\(i\) tensor past degrees \(j,k\) gives either \(i(j+k)\) or \(ij+ik\); the signs agree. These are equalities of chain maps, hence of derived maps. Naturality and (2.1) imply that replacing any model preserves these equalities.

Finally, restriction \(j^*\) to an open \(U\) is exact and commutes with tensor and direct sums, by the stalk and sheafification formulas of the first lesson. It preserves K-flatness by Lemma 2.2 of the K-flat lesson. Restricting resolutions \(P\to F\), \(R\to G\) therefore gives resolutions on \(U\), and the ordinary tensor identification gives

\[
(F\otimes_{\mathcal O}^{\mathbf L}G)|_U
\cong F|_U\otimes_{\mathcal O_U}^{\mathbf L}G|_U.
\tag{2.5}
\]

On local elementary tensors this is the identity, so it commutes with the association, symmetry and unit maps and with all roof comparisons. \(\square\)

The tensor sign in (2.4) concerns the degrees of the tensors. A morphism in the homotopy or derived category has degree zero, so no additional sign is inserted when composing the two morphism actions. Shifts carry the signed identifications already checked in Lemma 2.1 of the K-flat lesson.

## 3. Tor sheaves and the flatness criterion

For module sheaves \(F,G\), viewed in degree zero, and integers \(p\ge0\), define

\[
\operatorname{Tor}^{\mathcal O}_p(F,G)
=H^{-p}(F\otimes_{\mathcal O}^{\mathbf L}G).
\tag{3.1}
\]

They are sheaves of \(\mathcal O\)-modules and are functorial in both arguments. The cohomological minus sign is essential: ordinary projective or flat resolutions have their resolving terms in nonpositive degrees.

**Proposition 3.1 (degree zero and stalks).** There is a natural identification \(\operatorname{Tor}_0(F,G)=F\otimes G\). The derived tensor of two sheaves has no positive cohomology. Moreover

\[
\operatorname{Tor}^{\mathcal O}_p(F,G)_x
\cong\operatorname{Tor}^{\mathcal O_x}_p(F_x,G_x).
\tag{3.2}
\]

**Proof.** Lemma 4.1 of the K-flat lesson supplies a resolution \(P\to F[0]\) by flat terms, with \(P^n=0\) for \(n>0\). It is K-flat by Lemma 2.3 there. Its degree-zero cohomology is \(F\), so \(\operatorname{coker}(d_P^{-1})=F\). Tensoring this presentation with \(G\) is right exact and gives

\[
H^0(P\otimes G)
=\operatorname{coker}(d_P^{-1}\otimes1_G)=F\otimes G.
\]

The tensor has no positive terms, hence no positive cohomology. The augmentation induces the displayed degree-zero identification; naturality follows either by the roof construction or by the uniqueness of the degree-zero quotient map.

Stalks are exact and commute with tensor and direct sums, by Theorems 2.1 and 3.1 of the first lesson and Lemma 1.2 of the K-flat lesson. Hence \((P\otimes G)_x=P_x\otimes_{\mathcal O_x}G_x\) and taking stalks commutes with cohomology. Lemma 2.2 of that lesson says \(P_x\) is K-flat, and its map to \(F_x\) is a quasi-isomorphism. It therefore computes the tensor over the stalk ring, proving (3.2). \(\square\)

**Proposition 3.2 (long exact Tor sequence).** A short exact sequence \(0\to F_1\to F_2\to F_3\to0\) gives a natural long exact sequence

\[
\begin{gathered}
\cdots\longrightarrow\operatorname{Tor}_p(F_1,G)\\
\to\operatorname{Tor}_p(F_2,G)
\to\operatorname{Tor}_p(F_3,G)\\
\longrightarrow\operatorname{Tor}_{p-1}(F_1,G)
\longrightarrow\cdots\\
\longrightarrow\operatorname{Tor}_1(F_3,G)
\longrightarrow F_1\otimes G\\
\longrightarrow F_2\otimes G
\longrightarrow F_3\otimes G\longrightarrow0.
\end{gathered}
\tag{3.3}
\]

There is the analogous sequence in the second variable.

**Proof.** Proposition 5.2 of the common reading turns the short exact sequence into a distinguished triangle. The exact tensor functor of Theorem 2.2 gives a distinguished triangle after tensoring with \(G\). Its long exact cohomology sequence exists by Theorem 5.1 of that reading. Replace \(H^{-p}\) by (3.1) and \(H^0\) by Proposition 3.1; the subsequent positive cohomology is zero. The connecting map is the usual connecting cohomology map with the cone sign convention fixed above. The construction is natural for maps of short exact sequences. Symmetry gives the second-variable assertion. \(\square\)

**Theorem 3.3 (Tor detects flatness).** For a module sheaf \(F\), the following are equivalent:

1. \(F\) is flat.
2. \(\operatorname{Tor}_1(F,G)=0\) for every module sheaf \(G\).
3. \(\operatorname{Tor}_p(F,G)=0\) for every \(p>0\) and every module sheaf \(G\).

**Proof.** If \(F\) is flat, \(F[0]\) is K-flat by Lemma 2.3 of the preceding lesson. The one-variable construction therefore computes \(F\otimes^{\mathbf L}G\) as the ordinary sheaf \(F\otimes G\) in degree zero. This proves \(1\Rightarrow3\Rightarrow2\).

For \(2\Rightarrow1\), take any injection \(G\to H\), with cokernel \(C\). The second-variable version of (3.3) contains

\[
\operatorname{Tor}_1(F,C)\longrightarrow F\otimes G
\longrightarrow F\otimes H.
\]

The left sheaf is zero, so the right arrow is injective. Tensor is already right exact, so it is exact and \(F\) is flat. This proves all implications without a finiteness assumption. \(\square\)

The quantifier “every \(G\)” cannot be replaced by the single test \(G=F\). The continuous-function example below makes this failure explicit.

### Quotients by ideals

**Lemma 3.4.** For ideals \(I,J\) in a commutative ring \(R\),

\[
\begin{gathered}
\operatorname{Tor}_0^R(R/I,R/J)\\
{}=R/(I+J),\\
\operatorname{Tor}_1^R(R/I,R/J)\\
{}=(I\cap J)/(IJ).
\end{gathered}
\tag{3.4}
\]

For \(p\ge2\), \(\operatorname{Tor}_p^R(R/I,R/J)\cong
\operatorname{Tor}_{p-1}^R(I,R/J)\). The same assertions hold for ideal sheaves, with intersections, sums and products taken as sheaf ideals.

**Proof.** Apply (3.3) to \(0\to I\to R\to R/I\to0\), with second factor \(R/J\). Flatness of \(R\) annihilates all its positive Tor. The resulting first segment is

\[
\begin{gathered}
0\longrightarrow\operatorname{Tor}_1(R/I,R/J)
\longrightarrow I\otimes_R R/J
\\
\longrightarrow R/J
\longrightarrow (R/I)\otimes_R R/J\longrightarrow0.
\end{gathered}
\]

The presentation of tensor by balancing relations identifies \(I\otimes_R R/J\) with \(I/IJ\): the map sends \(i\otimes(r+J)\) to \(ri+IJ\), and its inverse sends \(i+IJ\) to \(i\otimes1\). The kernel of \(I/IJ\to R/J\) is \((I\cap J)/IJ\), and the cokernel is \(R/(I+J)\). The remaining exact segments give the dimension-shifting assertion. For sheaf ideals perform these calculations on every stalk; stalks preserve the relevant kernels and images, including ideal products, so they give the stated sheaf identities. \(\square\)

Formula (3.4) computes only the first two groups without extra information on \(I\). The higher groups require a resolution or the displayed dimension shift. Exercise 1 supplies a complete all-degree computation for two integer ideals.

## 4. Two geometric calculations

### Holomorphic coordinate germs

For the holomorphic examples here and in the later Hom and perfect-complex lessons, use the definition in the earlier programme reading [*Holomorphic functions of several variables*, Definition 1.1 and Theorem 1.2](prerequisites/holomorphic-power-series.md#polydiscs-and-holomorphy). Its [Theorem 2.1 and Proposition 2.2](prerequisites/holomorphic-power-series.md#power-series-and-regularity) prove the precise analytic input: every holomorphic germ has a unique Taylor expansion, absolutely convergent on a sufficiently small polydisc, with Cauchy coefficient estimates; and a convergent power series defines a holomorphic function. The following proves the coordinate algebra needed in those examples.

**Lemma (holomorphic coordinate germs).** Put \(R_1=\mathcal O_{\mathbf C,a}\), with coordinate \(w=z-a\), and \(R_2=\mathcal O_{\mathbf C^2,0}\), with coordinates \(x,y\). Multiplication by \(w\) on \(R_1\) and by \(x\) on \(R_2\) is injective. Evaluation gives \(R_1/(w)=\mathbf C\), restriction to \(x=0\) gives
\[
R_2/(x)\cong\mathcal O_{\mathbf C,0},
\]
with the coordinate on the right equal to \(y\), and multiplication by \(y\) on this quotient is injective. Consequently \(R_2/(x,y)=\mathbf C\), by evaluation at the origin. At a point where one of these coordinate functions is nonzero, it is a unit in the holomorphic stalk.

**Proof.** Represent a germ in \(R_1\) by \(f=\sum_{n\geq0}c_nw^n\). Choose a closed disc inside its domain of holomorphy. The earlier Taylor theorem gives radii and a bound \(|c_n|\leq Mr^{-n}\). The coefficients of \(wf\) are zero in degree zero and \(c_n\) in degree \(n+1\). Uniqueness of Taylor coefficients therefore makes multiplication by \(w\) injective. Evaluation is \(c_0\) and is onto by constant functions. If \(c_0=0\), put \(g=\sum_{n\geq0}c_{n+1}w^n\). For \(0<\rho<r\),
\[
\sum_{n\geq0}|c_{n+1}|\rho^n
\leq\frac{M}{r}\sum_{n\geq0}(\rho/r)^n
=\frac{M}{r(1-\rho/r)}.
\]
Thus \(g\) converges on a smaller disc, is holomorphic by the earlier Proposition 2.2, and \(f=wg\). Conversely a multiple of \(w\) evaluates to zero. This proves the one-variable assertions.

Now write \(f\in R_2\) as \(\sum_{m,n\geq0}c_{mn}x^my^n\), with \(|c_{mn}|\leq Mr_x^{-m}r_y^{-n}\) on chosen radii. Multiplication by \(x\) shifts the first coefficient index, so uniqueness again proves injectivity. Restriction to \(x=0\) is the germ \(\sum_n c_{0n}y^n\); it is holomorphic by Definition 1.1. It is onto: any holomorphic germ \(h(y)\) extends as the function \(h(y)\) independent of \(x\), which is continuous and holomorphic in each coordinate. Its kernel consists exactly of germs with every \(c_{0n}=0\), by the one-variable coefficient uniqueness. For such a germ the shifted series
\[
g=\sum_{m,n\geq0}c_{m+1,n}x^my^n
\]
converges absolutely and uniformly on smaller closed polydiscs, since
\[
\sum_{m,n\geq0}|c_{m+1,n}|\rho_x^m\rho_y^n
\leq\frac{M}{r_x}
\frac1{(1-\rho_x/r_x)(1-\rho_y/r_y)}
\qquad(0<\rho_j<r_j).
\]
The tails of the product geometric majorant also bound the series tails uniformly on each such closed polydisc. Proposition 2.2 makes \(g\) holomorphic, and \(f=xg\). This identifies the restriction kernel with \((x)\) and proves the displayed quotient isomorphism as an isomorphism of rings. Multiplication by \(y\) there is the one-variable injective map already proved. Quotienting once more by \(y\) gives \(\mathbf C\). Explicitly, if \(f(0,0)=c_{00}=0\), its terms with positive \(x\)-exponent give \(xg\) as above, and the remaining terms are \(yh(y)\), with \(h=\sum_{n\geq0}c_{0,n+1}y^n\); the same one-variable estimate makes \(h\) holomorphic. Hence the evaluation kernel is exactly \((x,y)\).

Finally, near a point where a coordinate \(u\) is nonzero, \(1/u\) is continuous. Its difference quotient in that coordinate is \(-1/(u(u+h))\), tending to \(-u^{-2}\), and it is constant in any other coordinate. Definition 1.1 therefore makes \(1/u\) holomorphic. This proves the unit assertion. \(\square\)

### Skyscrapers on a smooth one-dimensional local model

Take \(X=\mathbb R\) with \(\mathcal O\) the sheaf of real analytic functions, and let \(k_a=a_*\mathbb R\), with the action given by evaluation at \(a\). Multiplication by \(t-a\) gives an exact sequence

\[
0\longrightarrow\mathcal O
\xrightarrow{\ t-a\ }\mathcal O
\longrightarrow k_a\longrightarrow0.
\tag{4.1}
\]

Here is a stalk proof. At \(b\ne a\), the germ \(t-a\) is invertible. At \(a\), a germ of an analytic function has a convergent power series in \(t-a\). Vanishing at \(a\) means its constant coefficient is zero, so dividing by \(t-a\) shifts that series and gives another convergent series on a smaller interval. Conversely every such multiple vanishes at \(a\). Multiplication is injective because a continuous function with \((t-a)f(t)=0\) vanishes away from \(a\) and hence also at \(a\). Evaluation is surjective on germs, by constants. The first lesson's stalk criterion proves (4.1).

The two \(\mathcal O\) terms give a bounded flat, hence K-flat, resolution in degrees \(-1,0\). For the same point \(a\), tensoring it with \(k_a\) makes its differential zero. Therefore

\[
\begin{gathered}
\operatorname{Tor}_0(k_a,k_a)=k_a,\\
\operatorname{Tor}_1(k_a,k_a)=k_a,\\
\operatorname{Tor}_p(k_a,k_a)=0\quad(p\ge2).
\end{gathered}
\tag{4.2}
\]

For \(a\ne b\), tensoring (4.1) with \(k_b\) makes the differential multiplication by the nonzero real number \(b-a\), an isomorphism. All Tor sheaves are then zero. The nonzero degree-one sheaf at a coincident point records the kernel lost by ordinary tensor; its location is visible directly from the stalk computation.

### Continuous functions and two axes in the plane

Now let \(X=\mathbb R^2\) and \(\mathcal O\) be the sheaf of real-valued continuous functions. Set \(Z=\{y=0\}\), \(Z'=\{x=0\}\), and write \(I_Z,I_{Z'}\) for the sheaf ideals of functions vanishing on these subsets. Define

\[
\mathcal O_Z=\mathcal O/I_Z,\qquad
\mathcal O_{Z'}=\mathcal O/I_{Z'}.
\]

These are the continuous-function sheaves along the axes, extended to \(X\): a continuous function on an axis extends locally by projection onto that axis, proving surjectivity of the restriction map on germs. Its kernel is precisely the indicated vanishing ideal.

For these ideals

\[
I_Z\cap I_{Z'}=I_ZI_{Z'}.
\tag{4.3}
\]

The square-root facts needed here follow from the earlier programme [intermediate value theorem, Theorem 6](prerequisites/real-analysis-on-closed-intervals.md#compact-intervals-and-continuous-functions). The function \(t\mapsto t^2\) is continuous: for \(|t-s|<1\),
\[
|t^2-s^2|\leq(2|s|+1)|t-s|.
\]
For \(a\geq0\), the number \(a\) lies between its values \(0\) and \((a+1)^2\) on \([0,a+1]\), so the intermediate value theorem supplies a nonnegative \(u\) with \(u^2=a\). This \(u\) is unique, since \(v^2-u^2=(v-u)(v+u)>0\) for \(0\leq u<v\); write it as \(\sqrt a\). If \(a\geq b\geq0\), then \(u=\sqrt a\geq v=\sqrt b\), and
\[
(u-v)^2\leq(u-v)(u+v)=a-b.
\]
Interchanging \(a,b\) gives \((\sqrt a-\sqrt b)^2\leq|a-b|\) in all cases. Thus \(|a-b|<\varepsilon^2\) implies \(|\sqrt a-\sqrt b|<\varepsilon\), proving continuity of the nonnegative square root.

Now, for a real continuous function \(f\) vanishing on both axes, put \(h=\sqrt{|f|}\) and define \(g=f/\sqrt{|f|}\) where \(f\ne0\), with \(g=0\) on its zero set. The inequality \(\bigl||s|-|t|\bigr|\leq|s-t|\) makes absolute value continuous, so \(h\) is continuous by composition. Near a nonzero value of \(f\), its sign is fixed by continuity and \(g\) equals either \(h\) or \(-h\), so \(g\) is continuous there. At a zero, continuity of \(f\) gives \(|f|<\varepsilon^2\) nearby, hence \(|h|=|g|=\sqrt{|f|}<\varepsilon\). Thus both functions are continuous everywhere. Both vanish on each axis and \(f=gh\). This proves inclusion into the product on every germ; the reverse inclusion follows from vanishing. Lemma 3.4 gives

\[
\operatorname{Tor}_1(\mathcal O_Z,\mathcal O_{Z'})=0.
\tag{4.4}
\]

The ordinary tensor is the real skyscraper at the origin. Outside the origin at least one quotient has zero stalk. At the origin the sum of the two ideals is the maximal ideal of germs vanishing there. To prove this last assertion, decompose such a germ \(f\) as

\[
f=\frac{x^2f}{x^2+y^2}+\frac{y^2f}{x^2+y^2},
\tag{4.5}
\]

with both terms defined to be zero at the origin. Their absolute values are bounded by \(|f|\), so they are continuous there. The first vanishes on \(Z'\), and the second on \(Z\). Thus \(\mathcal O/(I_Z+I_{Z'})=0_*\mathbb R\), including its evaluation action. Equations (4.4) and (4.5) compute degree one and degree zero for the required closed-subset example.

This behaviour of first Tor does not imply flatness. Let \(R=\mathcal O_0\), \(\mathfrak m\) its evaluation kernel, and \(k=R/\mathfrak m=\mathbb R\). The same square-root factorization gives \(\mathfrak m=\mathfrak m^2\), so \(\operatorname{Tor}_1^R(k,k)=0\). But multiplication by the coordinate \(x\) is injective on \(R\): a continuous germ annihilated by \(x\) vanishes on the dense complement of the vertical axis and therefore everywhere on a neighbourhood. The two-term free resolution of \(R/(x)\) tensors with \(k\) to a zero-differential complex, giving

\[
\operatorname{Tor}_1^R(k,R/(x))=k\ne0.
\tag{4.6}
\]

Thus \(k\) is nonflat by Theorem 3.3. Notice that \(I_{Z',0}\ne(x)\): the continuous germ \(\sqrt{|x|}\) vanishes on the vertical axis, but cannot be divided by \(x\) continuously at the origin. In the analytic curve calculation division by its parameter was possible. The ideals in these examples must therefore be calculated in their actual function rings.

### Bounded inputs with an unbounded answer

On a one-point space put \(R=k[\varepsilon]/(\varepsilon^2)\) and view \(k=R/(\varepsilon)\) in degree zero. The resolution

\[
\cdots\xrightarrow{\varepsilon}R
\xrightarrow{\varepsilon}R
\xrightarrow{\varepsilon}R\longrightarrow k
\tag{4.7}
\]

has its last \(R\) in degree zero. In each negative degree the kernel and image of multiplication by \(\varepsilon\) are the same ideal \((\varepsilon)\), and the degree-zero cokernel is \(k\). It is a bounded-above free resolution, hence K-flat. Tensoring with \(k\) kills every differential, so \(\operatorname{Tor}_p^R(k,k)=k\) for every \(p\ge0\). Even two sheaves in degree zero can therefore have derived tensor with infinitely many negative cohomology sheaves. The perfect-complex lesson later proves the finite bounds furnished by a finite locally free model.

For the Hom computations over a one-point ringed space, define
\[
\operatorname{Ext}_R^i(M,L)=
\operatorname{Hom}_{D(R)}(M[0],L[i])\qquad(i\geq0).
\]
If \(P\to M[0]\) is a semifree resolution, Theorem 3.4 of *Flat modules and K-flat resolutions* and the Hom-complex formula of the common reading give
\[
\operatorname{Ext}_R^i(M,L)=
H^i\operatorname{Hom}_R^\bullet(P,L[0]).
\]
In particular, every bounded-above free resolution has this property. Choose a basis in each degree, put the basis of the top degree in stage zero, and then add the bases in successively lower degrees. Each differential raises degree and is a finite linear combination in the basis of the next degree, so this is a semifree filtration. This proves the needed Hom computation by the theorem already established, for associative unital \(R\) as well as commutative \(R\).

### Koszul models for several equations

The one-equation calculations extend to a finite regular sequence. The elementary Koszul argument is treated in Pierre Schapira's [*Algebra and Topology*, §4.7](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/AlTo.pdf). The following uses the cohomological degrees and tensor signs fixed in this course.

**Proposition 4.1 (regular-sequence calculation).** Let \(R\) be a commutative unital ring, \(a_1,\ldots,a_r\in R\), and \(M\) an \(R\)-module. Put
\[
K_R(a_1,\ldots,a_r)=\bigotimes_{i=1}^r
\bigl[R\xrightarrow{a_i}R\bigr],
\]
with each two-term factor in degrees \(-1,0\). This is a bounded complex of finite free modules, hence K-flat. If multiplication by \(a_i\) is injective on \(M/(a_1,\ldots,a_{i-1})M\) for every \(i\), then
\[
H^q(K_R(a_1,\ldots,a_r)\otimes_R M)=
\begin{cases}
M/(a_1,\ldots,a_r)M,&q=0,\\
0,&q\ne0.
\end{cases}
\]
If the sequence is regular on \(R\), \(K_R(a_1,\ldots,a_r)\) resolves \(R/(a_1,\ldots,a_r)\). For every module \(N\), with no regularity assumption on \(N\), it consequently computes all \(\operatorname{Tor}_i^R(R/(a_1,\ldots,a_r),N)\).

**Proof.** Write the basis vector attached to \(a_i\) as \(e_i\) in degree \(-1\). The degree-\(-s\) term of the tensor product has one basis vector for each \(s\)-element subset: use \(e_i\) in the chosen factors and the degree-zero unit in all other factors. We write that basis vector as \(e_{i_1}\wedge\cdots\wedge e_{i_s}\), with \(i_1<\cdots<i_s\). Define \(\bigwedge^s R^r\) to be the quotient of \((R^r)^{\otimes s}\) by the submodule generated by tensors with two equal entries. By the tensor universal property, maps from this quotient are precisely alternating multilinear maps. Expanding the relation with those two entries equal to \(u+v\) gives the adjacent-interchange rule \(u\wedge v=-v\wedge u\), with the other entries fixed. Expand any wedge in the basis of \(R^r\) and apply this rule to order the entries. Repeated entries make the wedge zero, so the ordered wedges span. This identifies the term with \(\bigwedge^s R^r\) once independence is checked. For each ordered subset, the alternating multilinear function given by the corresponding coordinate determinant descends to an \(R\)-linear functional on the exterior power and has value one on its matching ordered wedge and zero on the others. (In the determinant expansion, interchanging two entries pairs terms with opposite signs, and equal entries cancel those terms.) These functionals prove linear independence, over any commutative ring and also in characteristic two. On this ordered basis,
\[
d(e_{i_1}\wedge\cdots\wedge e_{i_s})=
\sum_{j=1}^s(-1)^{j-1}a_{i_j}
e_{i_1}\wedge\cdots\widehat e_{i_j}\cdots\wedge e_{i_s}.
\]
Removing a pair \(i_j,i_l\) in either order gives opposite signs and the same product of coefficients. Thus \(d^2=0\), including in characteristic two. This is exactly the tensor differential for the displayed two-term factors.

For \(r=1\), its tensor with \(M\) has kernel of multiplication in degree \(-1\) and cokernel in degree zero. The asserted injectivity gives the result. Suppose the result holds for \(r-1\). That tensor complex is quasi-isomorphic to \(M/(a_1,\ldots,a_{r-1})M\) in degree zero. Tensor with the last two-term free complex preserves this quasi-isomorphism by K-flatness. Its cohomology is again the kernel and cokernel of multiplication by \(a_r\), and regularity gives the assertion. Induction proves the formula. Every term of \(K_R\) is finite free and there are only \(r+1\) nonzero terms; bounded-above flatness proves K-flatness. Its augmentation onto the quotient is the asserted quasi-isomorphism when \(M=R\), so the derived tensor construction proves the final claim. \(\square\)

For \(R=k[x_1,\ldots,x_r]\) and \(a_i=x_i\), setting the first \(i-1\) variables to zero identifies the quotient at step \(i\) with the polynomial ring \(k[x_i,\ldots,x_r]\): the kernel consists exactly of the monomials divisible by one of those first variables. Multiplication by \(x_i\) increases its exponent in each monomial and sends distinct monomials to distinct monomials. Uniqueness of polynomial coefficients therefore proves injectivity, over any field. Thus the required regularity holds. Tensoring the resolution with \(k=R/(x_1,\ldots,x_r)\) makes every differential zero. Therefore
\[
\operatorname{Tor}_i^R(k,k)=\bigwedge\nolimits^i k^r
\quad(0\leq i\leq r),\qquad
\operatorname{Tor}_i^R(k,k)=0\quad(i>r).
\]
The same finite free resolution is semifree by the degree filtration just proved, so it computes the Ext groups defined above. Applying \(\operatorname{Hom}_R(-,k)\) makes every differential zero: each differential entry is a signed \(x_j\), and \(x_j\) acts as zero on \(k\). In degree \(i\) its Hom complex is
\[
\operatorname{Hom}_R(\bigwedge^i R^r,k)
\cong\operatorname{Hom}_k(\bigwedge^i k^r,k),
\]
where both sides assign one independent value in \(k\) to each ordered \(i\)-element subset. Consequently
\(\operatorname{Ext}_R^i(k,k)=\operatorname{Hom}_k(\bigwedge^i k^r,k)\) as vector spaces for \(0\leq i\leq r\), and it is zero for \(i>r\). The ordered subset basis has \(\binom ri\) elements, proving the stated dimensions. This calculation asserts groups and vector spaces; an assertion about the Yoneda multiplication would require its additional comparison.

### A bar model without commutativity

The bar construction gives a uniform computational example at a one-point space. Roman Bezrukavnikov's [MIT 18.706 lecture notes, §12.2, p. 37](https://ocw.mit.edu/courses/18-706-noncommutative-algebra-spring-2023/mit18_706_s23_full_lec.pdf), prepared by Serina Hu and Vasily Krylov, present the construction. We write out the module version and its contraction independently.

**Proposition 4.2 (bar resolution).** Let \(A\) be an associative unital algebra over a field \(k\), and \(M\) a left \(A\)-module. There is a free resolution in nonpositive cohomological degrees with
\[
B^{-n}(M)=A\otimes_k A^{\otimes_k n}\otimes_k M\quad(n\geq0)
\]
and augmentation \(a\otimes m\mapsto am\). For \(n\geq1\), its differential is
\[
\begin{aligned}
d(a_0|\cdots|a_n|m)
&=\sum_{i=0}^{n-1}(-1)^i
(a_0|\cdots|a_i a_{i+1}|\cdots|a_n|m)\\
&\quad+(-1)^n(a_0|\cdots|a_{n-1}|a_n m).
\end{aligned}
\]
It computes \(\operatorname{Tor}^A_i(N,M)\) for every right \(A\)-module \(N\) after applying \(N\otimes_A-\), and computes \(\operatorname{Ext}_A^i(M,L)\) after applying \(\operatorname{Hom}_A(-,L)\).

**Proof.** Let \(\partial_i\) be the operation of multiplying the \(i\)-th adjacent pair, with the last operation acting on \(m\). Associativity of \(A\) and its module action gives
\(\partial_i\partial_j=\partial_{j-1}\partial_i\) for \(i<j\), with compositions read from right to left. Each term in the square of the alternating differential is therefore paired with an identical operation of opposite sign. This proves \(d^2=0\); the same action identity verifies the augmentation.

On the augmented complex, define \(h(m)=1|m\) and
\[
h(a_0|\cdots|a_n|m)=1|a_0|\cdots|a_n|m.
\]
The first face of \(dh\) returns the original tensor. Every subsequent face of \(dh\) is the negative of the corresponding term of \(hd\); in degree zero this includes the augmentation followed by \(h(m)\). Hence \(dh+hd=1\). The contraction is \(k\)-linear; it need not be \(A\)-linear. It proves exactness of the underlying complex, and therefore exactness as \(A\)-modules.

Each term is a free left \(A\)-module: choose a \(k\)-basis of \(A^{\otimes n}\otimes M\) and use it as the free basis of the first-factor module. The complex is bounded above and free. Filtering it by degrees starting at zero and then adding degrees \(-1,-2,\ldots\) gives a semifree filtration, since the differential raises cohomological degree. Theorem 3.4 in the K-flat lesson makes it both K-projective and K-flat. The derived tensor and Hom comparisons then prove the two computational assertions for all \(N,L\). \(\square\)

The field hypothesis ensures the stated freeness of every term. Over a general base ring this same formula is a relative resolution, and additional flatness or projectivity conditions are needed before using it to compute absolute derived functors. No commutativity of \(A\) is assumed here.

## 5. Exercises with checked solutions

**Exercise 1 (easy: ideals on a one-point space).** Let \(R\) be a commutative ring and \(I,J\) ideals. Derive formulas for Tor in degrees zero and one. Then compute every \(\operatorname{Tor}_p^{\mathbb Z}(\mathbb Z/m,\mathbb Z/n)\), for positive integers \(m,n\ge2\). Explain why the first formulas alone do not determine all higher groups for arbitrary ideals.

**Solution.** Tensor \(0\to I\to R\to R/I\to0\) with \(R/J\) in the derived sense. The vanishing of positive Tor against \(R\) embeds first Tor as the kernel of \(I/IJ\to R/J\). This kernel is \((I\cap J)/IJ\), and the cokernel is \(R/(I+J)\). The next segments identify higher Tor with \(\operatorname{Tor}_{p-1}(I,R/J)\), which need not vanish.

For \(\mathbb Z/m\), use the injective multiplication map in the free resolution \(\mathbb Z\xrightarrow{m}\mathbb Z\), in degrees \(-1,0\). Tensor with \(\mathbb Z/n\). Put \(d=\gcd(m,n)\). Its cokernel is \(\mathbb Z/d\), and its kernel consists of the multiples of \(n/d\) modulo \(n\), also a cyclic group of order \(d\). Thus

\[
\operatorname{Tor}^{\mathbb Z}_p(\mathbb Z/m,\mathbb Z/n)
=
\begin{cases}
\mathbb Z/d,&p=0,1,\\
0,&p\ge2.
\end{cases}
\]

The first-degree ideal formula agrees: \(I\cap J=\operatorname{lcm}(m,n)\mathbb Z\) and \(IJ=mn\mathbb Z\). In contrast, for the dual-number ring in (4.7), the ideals \(I=J=(\varepsilon)\) have all positive Tor equal to \(k\), by that explicit free resolution. Thus the higher-degree answer needs information about the actual ideal or resolution.

**Exercise 2 (medium: associativity with changed models).** Let \(P,R,T\) resolve \(F,G,H\). Prove the derived associativity isomorphism, including independence when a different K-flat model \(V\to P\otimes R\) is used for the intermediate object. Check the symmetry hexagon on tensors of degrees \(1,1,-1\).

**Solution.** The product \(P\otimes R\) is K-flat, so \((P\otimes R)\otimes T\) computes the left-associated product without another resolution. The right-associated product is computed by \(P\otimes(R\otimes T)\). Their summands are indexed by the same triples, and their differential terms have signs \(1,(-1)^i,(-1)^{i+j}\). Reassociation is therefore a chain isomorphism with no extra sign.

The map \(V\to P\otimes R\) is a quasi-isomorphism between K-flats. Lemma 1.1 makes \(V\otimes T\to(P\otimes R)\otimes T\) a quasi-isomorphism. Its composite with reassociation gives the comparison from this alternative intermediate model. For two such choices, resolve their termwise-surjective enlargements' fibre product; the resulting comparisons agree by Theorem 1.2. Changing the individual \(P,R,T\) is handled by the same comparison and the naturality of the ordinary association map. Consequently the isomorphism belongs to the derived objects, rather than to the displayed choice alone.

For the stated degrees, moving the degree-one factor across the combined block has sign \((-1)^{1(1-1)}=1\). Moving it successively past the two odd-degree factors gives \((-1)^{1\cdot1}(-1)^{1\cdot(-1)}=(-1)(-1)=1\). This checks that instance of the hexagon; the calculation \(i(j+k)=ij+ik\) proves every instance.

**Exercise 3 (medium: which Tor tests suffice?).** Prove Theorem 3.3 from the derived construction. Show also that it is enough to test \(\operatorname{Tor}_1(F,x_*N)=0\) for every point \(x\) and every \(\mathcal O_x\)-module \(N\). Explain the role of “every” using the continuous germ ring at the origin.

**Solution.** A flat \(F\) in degree zero is K-flat, so its ordinary tensor with \(G[0]\) already computes the derived tensor and has no negative cohomology. Thus flatness implies all positive Tor vanish, which implies first Tor vanishes. Conversely, the exact sequence for an injection \(G\to H\) has \(\operatorname{Tor}_1(F,\operatorname{coker}(G\to H))\) immediately before \(F\otimes G\to F\otimes H\). Vanishing of this first Tor makes that map injective. Right exactness then proves flatness.

For the point tests, take the stalk at \(x\). Proposition 3.1 and \((x_*N)_x=N\), from Lemma 5.2 of the first lesson, give \(\operatorname{Tor}_1^{\mathcal O_x}(F_x,N)=0\). For any injection of stalk-ring modules apply the same Tor exact sequence, proving that \(F_x\) is flat. The stalk criterion, Lemma 1.2 of the K-flat lesson, proves \(F\) flat.

In the continuous germ ring \(R\), the residue \(k\) has \(\operatorname{Tor}_1(k,k)=\mathfrak m/\mathfrak m^2=0\), but \(\operatorname{Tor}_1(k,R/(x))=k\). This particular additional test detects the failure. Testing against the residue itself therefore does not replace testing against all modules.

**Exercise 4 (hard: only one resolution for an unbounded input).** Over \(\mathbb Z\), let \(F=\mathbb Z/2[0]\), and let \(G\) have \(\mathbb Z/2\) in every integer degree with zero differentials. Compute \(G\otimes^{\mathbf L}F\) by resolving only \(F\). Prove in general that the resulting one-resolution answer agrees with resolving both variables. Compare it with the ordinary tensor.

**Solution.** Use \(P=(\mathbb Z\xrightarrow{2}\mathbb Z)\) in degrees \(-1,0\), with its augmentation to \(F\). This is a bounded free, hence K-flat, resolution. In total degree \(n\), \(G\otimes P\) has two summands, \(G^n\otimes P^0\) and \(G^{n+1}\otimes P^{-1}\). Both are \(\mathbb Z/2\). The \(G\) differential is zero, and the contribution of \(2\) on \(P\) is zero after tensoring; the total differential is therefore zero. Hence

\[
\begin{gathered}
H^n(G\otimes^{\mathbf L}F)
=(\mathbb Z/2)\oplus(\mathbb Z/2),\\
\text{for every }n\in\mathbb Z.
\end{gathered}
\]

No resolution of \(G\) was needed for this computation. To verify agreement in general, choose any K-flat \(R\to G\). The map \(R\otimes P\to G\otimes P\) is a quasi-isomorphism by K-flatness of \(P\), and \(R\otimes P\to R\otimes F\) is a quasi-isomorphism by K-flatness of \(R\). This gives (1.3) with no boundedness assumption. If \(P\) is replaced by another K-flat resolution, the common-refinement comparison in Theorem 1.2 makes the resulting isomorphisms agree naturally.

The ordinary tensor \(G\otimes F\) has only one \(\mathbb Z/2\) in each degree. The augmentation map \(G\otimes P\to G\otimes F\) is the projection to the \(P^0\) summand, so it is not a quasi-isomorphism. The target \(F\) is not K-flat; it cannot serve as the target K-flat model in the second assertion of Lemma 1.1.

**Exercise 5 (medium: where can tensor cohomology occur?).** For complexes \(A,B\), put \(\Sigma(A)=\{x:H^n(A)_x\ne0\text{ for some }n\}\). Prove

\[
\Sigma(A\otimes^{\mathbf L}B)\subset\Sigma(A)\cap\Sigma(B).
\]

Use this to compute the derived tensor of sheaves supported at two distinct points of a Hausdorff space.

**Solution.** Choose K-flat resolutions \(P\to A\), \(R\to B\). At a point outside \(\Sigma(A)\), the stalk \(A_x\) is acyclic, so \(P_x\) is an acyclic K-flat complex. Lemma 1.1 says that its tensor with every complex, in particular \(R_x\), is acyclic. Since stalks commute with total tensor and cohomology, all stalk cohomology of \(P\otimes R\) vanishes there. The same argument applies outside \(\Sigma(B)\), proving the inclusion.

For a sheaf supported at one point the only possibly nonzero cohomology stalk is at that point. If the two points are distinct the two sets are disjoint, so every cohomology stalk of the derived tensor is zero. Exactness detection by stalks makes the product zero in the derived category. On a Hausdorff space ordinary skyscrapers have precisely this stalk support: a different point has a neighbourhood avoiding the chosen point. This recovers the distinct-point part of the curve example without its parameter resolution.

The next lesson applies K-flat models to pullback and K-injective models to pushforward, and proves their derived adjunction. The tensor bifunctor and its comparisons established here will make the pullback's compatibility with tensor natural.

Sources: the tensor-invariance and construction arguments of Lemma 1.1 and Theorem 1.2 follow the Stacks project, tags 06YA, 06YG and 06YH, in its AI Integrated Stacks Project edition, checked and edited by GPT-6.1 Sol (OpenAI), at Ultra, with the full fibre-product comparison included. The Tor definition and flatness proof follow the Stacks project, tags 08BP and 08BQ, in that edition, checked and edited by the same writing AI; the explicit K-flat computation is given above. The pinned [complete source passage](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/cohomology.tex#L6562) and its preceding comparison lemmas were read. The localization, coherence, geometric calculations and exercises are expanded here with their actual conditions. See the [course notice](../LICENCE.md).
