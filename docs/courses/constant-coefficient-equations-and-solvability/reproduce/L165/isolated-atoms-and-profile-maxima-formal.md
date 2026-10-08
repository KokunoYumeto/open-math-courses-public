# Isolated atoms and separated singularities

Original exposition and proofs: GPT-6.1 Sol (OpenAI), Ultra. CC0 1.0. Self-checked by the writing AI; independent mathematical review is not claimed.

An isolated point of a distribution's support leaves a singularity that no convolution profile can hide. This gives a common geometric core for all its profile carriers. We use this observation to construct measures with any prescribed compact convex carrier, and then examine the maximum law for sums whose singularities are separate.

Basic references are Tao's *246B, Notes 2* and *245B, Notes 9*, and Hörmander's *The Analysis of Linear Partial Differential Operators I* and *II*. The prerequisites are Recovering singularities from convolution profiles, especially the one-point selector, its point-supported polynomial operators and its universal hull-addition criterion; Changing centers in Fourier windows, including the finite common-neighborhood corollary; Frequency-selective singularities and smooth convolutions, for the actual compact selector construction; Joint logarithmic-frequency limits, for finite coordinate projection; and Slow decrease and entire Fourier division, for invertibility. The local singular-support calculus needed below is proved here.

## 1. The geometric information in a profile

For a compact distribution \(u\) on \(\mathbb R^n\), \(n\geq1\), use
\[
 F_u(\zeta)=\langle u,e^{-ix\cdot\zeta}\rangle,\qquad
 L_u(z,c)=\frac{\log|F_u(c+z\log|c|)|}{\log|c|},
 \quad c\in\mathbb R^n,\quad |c|>2.
 \tag{1.1}
\]
Write \(\mathcal J(u)\) for the directional indicators of proper local \(L^1\) profiles and collapsed profiles. A proper indicator \(h\) is the support function of a nonempty compact convex carrier \(C_h\). The collapsed indicator is \(-\infty\), with \(C_{-\infty}=\varnothing\). Support functions and carriers are taken in this extended sense throughout.

The family \(\mathcal J(u_1,\ldots,u_k)\) consists of indicator tuples from one escaping real sequence with a joint proper-or-collapsed extraction in every coordinate. It is not the Cartesian product of the individual families. Every individual coordinate or finite subtuple can be extended to a tuple containing further compact distributions, by the finite joint-profile projection theorem.

Let
\[
 A(u)=\operatorname{sing\,supp}u,\qquad
 S_u=\operatorname{conv}A(u).
 \tag{1.2}
\]
The singular support is compact; its convex hull is compact when nonempty. The full hull recovery theorem proves
\[
 S_u=\overline{\operatorname{conv}
                   \bigcup_{h\in\mathcal J(u)}C_h}.
 \tag{1.3}
\]
In particular each proper carrier lies in \(S_u\), and \(S_u\) lies in the convex hull of the ordinary support. The family is nonempty by the PSH compactness alternative on any escaping sequence.

If a finite family of indicators has at least one proper member, the function \(\max_i h_i\) is the support function of the convex hull of their proper carriers. Indeed a continuous linear functional has the same supremum on a set and its convex hull. If every member is collapsed, the maximum is \(-\infty\) and this hull is empty.

## 2. Convolution cannot create a new pair of singular points

We first establish the local facts that prevent cancellation near an isolated singularity.

**Lemma 2.1 (compact singular-support calculus).** For compact distributions \(a,b\),
\[
 \operatorname{supp}(a*b)\subset
                       \operatorname{supp}a+\operatorname{supp}b,
 \qquad
 A(a*b)\subset A(a)+A(b).
 \tag{2.1}
\]
An empty summand makes the corresponding sum empty. In particular \(a*b\) is smooth if either factor is smooth. If \(A(b)=\{0\}\), then \(A(a*b)\subset A(a)\).

*Proof.* For the ordinary support assertion, take a test function \(\phi\) supported outside the compact sum of the two supports. Choose compact smooth cutoffs equal to one near those supports and with sufficiently small support neighborhoods. The test function
\(\chi_a(x)\chi_b(y)\phi(x+y)\) then vanishes near the product of the two distribution supports. Its iterated distribution pairing, which defines \((a*b)(\phi)\), is zero. More explicitly the positive distance between the two compact sets lets us make \(\phi(x+y)\) identically zero on the product of the cutoff supports. Hence the outer and inner pairings both vanish. This proves the first assertion locally outside that sum.

If \(f\) is compact and smooth and \(b\) is a compact distribution, its convolution is the smooth function
\[
 (f*b)(x)=\langle b(y),f(x-y)\rangle.
 \tag{2.2}
\]
Insert a fixed cutoff in \(y\), equal to one near \(\operatorname{supp}b\), to make this pairing a test-function pairing. As \(x\) varies on any compact set, each derivative in \(x\) of the cutoff times \(f(x-y)\) exists and varies continuously in every test-function derivative seminorm. Continuity of \(b\) therefore permits every derivative through the pairing. The resulting function represents the convolution distribution: integration against a test function in \(x\) commutes with the pairing because its Riemann sums converge in that same test-function topology. Thus it is smooth. Commutativity gives the same conclusion when the second factor is smooth.

Assume both singular supports are nonempty. For any \(\varepsilon>0\), choose a compact smooth cutoff \(\theta_a\) equal to one on a neighborhood of \(A(a)\) and supported inside its open \(\varepsilon\)-neighborhood. Write
\[
 a=\theta_a a+(1-\theta_a)a=a_\varepsilon+a_{\mathrm{sm}}.
 \tag{2.3}
\]
The second summand is compact and smooth. It vanishes near \(A(a)\), and elsewhere it is a smooth multiple of a locally smooth distribution. The first is supported within the closed \(\varepsilon\)-neighborhood of \(A(a)\). Decompose \(b\) in the same way.

Every convolution term containing a smooth summand is smooth by (2.2). Consequently
\[
 A(a*b)\subset
       \operatorname{supp}a_\varepsilon+
       \operatorname{supp}b_\varepsilon
       \subset A(a)+A(b)+\overline B_{2\varepsilon}(0).
 \tag{2.4}
\]
To justify the first inclusion at a point outside the displayed support sum, the remaining convolution term vanishes on a neighborhood there and all other terms are smooth. The compact set \(A(a)+A(b)\) is closed. Any point outside it has positive distance from it, so (2.4) for sufficiently small \(\varepsilon\) excludes that point from \(A(a*b)\). This proves the second assertion. If one singular support is empty, its compact distribution is smooth and (2.2) proves the empty case directly. \(\square\)

**Lemma 2.2 (separate singularities cannot cancel).** If \(a_1,\ldots,a_k\) are compact distributions with pairwise disjoint singular supports, then
\[
 A\!\left(\sum_i a_i\right)=\bigcup_i A(a_i).
 \tag{2.5}
\]
The ordinary supports may overlap.

*Proof.* Outside the union every summand is smooth locally, so their sum is smooth. If \(x\in A(a_i)\), pairwise disjointness and the finite number of summands give a neighborhood of \(x\) on which all other summands are smooth. If their sum with \(a_i\) were smooth near \(x\), subtracting the other smooth summands would make \(a_i\) smooth there. This contradicts \(x\in A(a_i)\). Thus every point of the union remains singular. \(\square\)

## 3. Isolated support points belong to every carrier

Let \(I(u)\) be the set of isolated points of the ordinary support of \(u\), and put
\[
 K_I=\overline{\operatorname{conv} I(u)}.
 \tag{3.1}
\]
If there are no isolated support points, set \(K_I=\varnothing\) and \(H_{K_I}=-\infty\). Otherwise \(K_I\) is a nonempty compact convex set contained in the convex hull of \(\operatorname{supp}u\).

**Theorem 3.1 (a common carrier core).** Every \(h\in\mathcal J(u)\) satisfies
\[
 H_{K_I}(\eta)\leq h(\eta)
       \quad(\eta\in\mathbb R^n).
 \tag{3.2}
\]
Equivalently every carrier contains \(K_I\). If \(I(u)\neq\varnothing\), all profiles are proper; in particular \(u\) is invertible.

*Proof.* The conclusion is immediate in the empty-\(I(u)\) case, so take \(x\in I(u)\). There is an open ball about \(x\) containing no other point of \(\operatorname{supp}u\). Choose a smooth cutoff equal to one near \(x\) and supported in that ball, and write \(u=a+b\) using that cutoff. Then \(a\) is nonzero and supported at the single point \(x\), while \(b\) vanishes on a neighborhood of \(x\). Nonzero follows from \(x\in\operatorname{supp}u\): if this cutoff piece were zero, \(u\) would vanish near \(x\).

The full point-support finite-jet theorem and polynomial-profile result in the preceding chapter apply to \(a\). For every compact distribution \(v\),
\[
 S_{a*v}=\{x\}+S_v.
 \tag{3.3}
\]
Fix any \(h\in\mathcal J(u)\). The profile-realization theorem gives a compact continuous \(v\notin C^1\), singular exactly at zero, with
\[
 S_v=\{0\},\qquad S_{u*v}=C_h.
 \tag{3.4}
\]
It includes the collapsed case, where the second hull is empty.

Formula (3.3) makes \(S_{a*v}=\{x\}\). Thus \(A(a*v)=\{x\}\): a nonempty singular hull consisting of one point has exactly that nonempty singular support. By Lemma 2.1, \(A(b*v)\subset A(b)\), and \(b*v\) is smooth near \(x\). The singularity of \(a*v\) therefore survives in
\(u*v=a*v+b*v\), by the local argument of Lemma 2.2. Hence
\[
 x\in A(u*v)\subset S_{u*v}=C_h.
 \tag{3.5}
\]
This rules out a collapsed \(h\), and places every isolated support point in every proper carrier. Each carrier is closed and convex, so contains \(K_I\). Taking support functions gives (3.2).

When \(I(u)\neq\varnothing\), the absence of a collapsed profile is the full slow-decrease criterion, and hence invertibility, from the preceding entire-division chapter. \(\square\)

The proof uses one selector for the whole distribution and the exact polynomial operator at the isolated point. It does not require a maximum formula for an arbitrary sum of Fourier transforms.

**Corollary 3.2 (finite support).** Suppose \(u\neq0\) has finite support, and let \(K=\operatorname{conv}(\operatorname{supp}u)\). Then
\[
 \mathcal J(u)=\{H_K\},\qquad
 S_{u*v}=K+S_v
       \quad\text{for every compact }v.
 \tag{3.6}
\]
Thus \(u\) is invertible even though its transform may have real zeros.

*Proof.* Every support point is isolated, so Theorem 3.1 gives \(H_K\leq h\) for every indicator. Every proper carrier is contained in \(S_u\subset K\), by (1.3), giving the reverse inequality. There is no collapsed indicator and the family is nonempty. Therefore it is exactly \(\{H_K\}\).
Every nonzero one-point distribution is singular at its support point. Indeed a smooth function supported at one point is zero, while that distribution is nonzero. Thus every support point of \(u\) is singular and \(S_u=K\). Apply the universal singleton-indicator addition criterion in the preceding chapter to obtain (3.6). \(\square\)

## 4. Positive atoms can prescribe any compact convex carrier

**Theorem 4.1 (a measure with one prescribed indicator).** For every compact convex \(K\subset\mathbb R^n\), there is a finite nonnegative measure \(u\), supported in \(K\), such that
\[
 \mathcal J(u)=\{H_K\}.
 \tag{4.1}
\]
If \(K\neq\varnothing\), \(u\) can have total mass one. It then has singular hull \(K\), is invertible, and satisfies universal singular-hull addition.

*Proof for the empty and singleton cases.* For \(K=\varnothing\), choose \(u=0\); every profile is collapsed and its sole indicator is \(H_\varnothing=-\infty\). If \(K=\{x\}\), choose \(u=\delta_x\) and use Corollary 3.2.

*Construction in positive affine dimension.* Let \(A\) be the affine hull of a nonempty \(K\), of dimension \(d\geq1\). Work with the Euclidean metric restricted to \(A\). Choose \(d+1\) affinely independent points of \(K\). Their simplex lies in \(K\), and its barycenter has a relative open ball contained in that simplex. Hence there are \(o\in K\) and \(r>0\) with
\(\overline B_r^A(o)\subset K\), after decreasing the radius if necessary. In particular \(o\) is in the relative interior of \(K\).

The relative boundary \(B=\partial_A K\) is compact and nonempty. For any unit direction in \(A\), the ray from \(o\) meets \(K\) in a closed bounded interval of positive length. Its outer endpoint is in \(B\). Every boundary point on that ray is this endpoint: if a point on the ray lay strictly before a further point of \(K\), taking its convex combination with the relative ball about \(o\) would put a relative ball about that point inside \(K\), contradicting its being a boundary point.

For each integer \(m\geq1\), choose a finite \(1/m\)-net \(B_m\subset B\), with distinct points within that net, and set
\[
 t_m=1-2^{-m},\qquad
 X_m=\{(1-t_m)o+t_m b:b\in B_m\}.
 \tag{4.2}
\]
A finite net exists by compactness: select finitely many radius-\(1/m\) balls with centers in \(B\) covering \(B\). Every \(x\in X_m\) is in the relative interior of \(K\), since convexity puts the relative ball
\(B^A_{(1-t_m)r}(x)\) in \(K\).

All these points are distinct, including across different \(m\). Equality of two such points would put their two boundary points on the same ray from \(o\). The uniqueness of the boundary endpoint on that ray makes the boundary points equal, and then the distinct \(t_m\)'s make the indices equal.

Let \(R=\max_{b\in B}|b-o|\). Every point of \(X_m\) has distance at most \(2^{-m}R\) from \(B\). Therefore every accumulation point of the sequence obtained by listing the finite \(X_m\)'s in increasing \(m\) lies in \(B\). Conversely, for each \(b\in B\) choose \(b_m\in B_m\) with \(|b_m-b|<1/m\), allowing a non-strict bound if needed. Then
\[
 |(1-t_m)o+t_m b_m-b|
           \leq 2^{-m}R+1/m\longrightarrow0.
 \tag{4.3}
\]
These points are distinct, so \(b\) is an accumulation point. Thus the accumulation set is exactly \(B\).

Enumerate all the distinct interior points as \(x_1,x_2,\ldots\), and define
\[
 u=\sum_{j=1}^{\infty}2^{-j}\delta_{x_j}.
 \tag{4.4}
\]
This defines a nonnegative Borel measure of mass one: for any Borel set sum the nonnegative weights of its points; countable additivity follows by interchanging nonnegative sums. Its support is
\[
 \operatorname{supp}u=\overline{\{x_j:j\geq1\}}
                         =\{x_j:j\geq1\}\cup B\subset K.
 \tag{4.5}
\]
To verify the first equality, a neighborhood meeting an atom has positive measure, and any neighborhood of a limit point meets such an atom. Outside the closure there is an open neighborhood with no atom and zero measure.

Each \(x_j\) is isolated in this support. It has positive relative distance from \(B\). All sufficiently late blocks lie closer to \(B\) than half that distance, so cannot approach \(x_j\); the finitely many earlier atoms can be excluded by a smaller ball. The same ambient ball excludes them and \(B\), since distances on \(A\) are the ambient distances between these points.

The closed convex hull of the isolated atoms is \(K\). It contains \(B\) by (4.3). To see that \(\operatorname{conv}B=K\), any relative-interior point of \(K\) lies on a segment whose two endpoints are the outer boundary points in opposite directions on a line through it. The intersection of \(K\) with that line is a bounded closed interval containing the point in its interior. Both endpoints are relative boundary points: a relative open ball there would extend the line interval. The point is their convex combination. Boundary points already belong to \(B\). This proves the claimed convex-hull equality.

Theorem 3.1 now gives \(H_K\leq h\) for every profile indicator. Conversely every proper carrier is contained in \(S_u\subset K\), giving \(h\leq H_K\). There are isolated atoms, so a collapsed profile is impossible. The nonempty profile family therefore has exactly the sole indicator \(H_K\).

For completeness its singular hull is indeed \(K\). Near each isolated atom the measure is a nonzero multiple of \(\delta_{x_j}\), so it is singular there. A smooth function cannot represent this point mass: it would be zero on the punctured neighborhood and hence at the center by continuity. The singular support is closed and contains the closure in (4.5). Since it is always contained in the ordinary support, the two supports are equal for this measure. Their convex hull is \(K\). Invertibility and universal addition follow from the preceding full profile criteria. \(\square\)

This construction uses relative interior and relative boundary. It therefore applies to a segment or a planar convex body in a higher-dimensional ambient space. The singleton case was treated separately because its relative boundary is empty.

## 5. One selector can serve a finite tuple

To understand sums with separated singularities, we need the selector to preserve several prescribed profile carriers simultaneously.

**Lemma 5.1 (simultaneous realization).** Suppose a finite tuple of compact distributions \(a_1,\ldots,a_\ell\) has prescribed proper-or-collapsed profiles on one escaping real sequence, with indicators \(h_1,\ldots,h_\ell\). For every \(\varepsilon>0\), there is a compact continuous \(v\notin C^1\), supported in \(\overline B_\varepsilon(0)\), such that
\[
 A(v)=\{0\},\qquad S_{a_i*v}=C_{h_i}
                  \quad(1\leq i\leq\ell).
 \tag{5.1}
\]

*Proof.* The finite common-neighborhood corollary in the changing-frequency chapter supplies radii \(r_j\to\infty\) and one union
\[
 E=\bigcup_j B_{\mathbb R^n}(c_j,r_j\log|c_j|).
 \tag{5.2}
\]
For every proper coordinate the normalized logarithms satisfy, on each compact parameter set and with every positive tolerance, the eventual ceiling
\[
 L_{a_i}(z,d)\leq N_i+h_i(\operatorname{Im}z)
                         +\text{tolerance}
       \quad(d\in E,\ |d|\to\infty).
 \tag{5.3}
\]
Each collapsed coordinate collapses uniformly locally along the entire union. The corollary is a finite diagonal: take the maximum of all coordinate thresholds at each parameter radius and tolerance, then choose one expanding radius sequence. It retains each coordinate's own order and indicator.

Apply the full frequency-selective construction to this \(E\) and to the support radius \(\varepsilon\). The resulting \(v\) has singular support \(\{0\}\), collapses uniformly locally outside \(E\), and has the zero proper profile on a subsequence of the original centers \(c_j\). Every prescribed coordinate profile is retained on that same subsequence.

For a proper \(h_i\), the selected product profile is the prescribed \(a_i\) profile plus zero. Its carrier \(C_{h_i}\) thus occurs in the output family, so is contained in \(S_{a_i*v}\). Conversely a proper output profile cannot have infinitely many centers outside \(E\): the selector's exterior collapse and a common local upper bound for \(L_{a_i}\) would collapse that subsequence. On a tail inside \(E\), extract its two input profiles jointly. Both are proper, since a collapsed input would collapse the product. Passing (5.3) to the canonical PSH representative gives
\[
 U_i(z)\leq N_i+h_i(\operatorname{Im}z).
 \tag{5.4}
\]
Indeed a proper \(L^1\) extraction first gives this bound almost everywhere. Submean on small balls and continuity of the right side give it pointwise. Its directional indicator is at most \(h_i\), by dividing along positive dilations and letting the dilation radius tend to infinity. Its carrier is therefore contained in \(C_{h_i}\).

Every proper selector profile has a nonempty carrier contained in \(S_v=\{0\}\), hence has carrier \(\{0\}\). The exact common-frequency convolution law makes every proper output carrier a subset of \(C_{h_i}+\{0\}=C_{h_i}\). The closed-convex-hull recovery formula (1.3) proves the reverse containment and hence (5.1).

For a collapsed \(h_i\), \(L_{a_i}\) collapses inside \(E\) and \(L_v\) collapses outside \(E\). On each parameter compact set the other input has a common upper bound. Taking a finite maximum of the two required frequency thresholds makes their sum smaller than any prescribed negative bound at all sufficiently large centers. Thus all output profiles collapse. Their carriers are empty, so (1.3) makes the singular hull empty and the output smooth. This proves (5.1) for every coordinate, with the same \(v\). \(\square\)

The finiteness of the tuple permits the common diagonal. No assertion about an arbitrary infinite tuple is needed.

## 6. Separated singularities give a maximum law

**Theorem 6.1 (the joint maximum formula).** Let \(u_1,\ldots,u_k\) be compact distributions with pairwise disjoint singular supports, and put \(u=\sum_i u_i\). If
\((h,h_1,\ldots,h_k)\in\mathcal J(u,u_1,\ldots,u_k)\), then
\[
 h=\max_{1\leq i\leq k} h_i.
 \tag{6.1}
\]
Consequently
\[
 \mathcal J(u)=
 \left\{\max_i h_i:
           (h_1,\ldots,h_k)\in\mathcal J(u_1,\ldots,u_k)\right\}.
 \tag{6.2}
\]
Both formulas include collapsed coordinates and an entirely collapsed tuple.

*Proof of the joint identity.* Apply Lemma 5.1 to the tuple containing \(u\) and all \(u_i\). It gives one compact \(v\), singular exactly at zero, with
\[
 S_{u*v}=C_h,\qquad S_{u_i*v}=C_{h_i}.
 \tag{6.3}
\]
By Lemma 2.1, \(A(u_i*v)\subset A(u_i)\). These output singular supports are therefore pairwise disjoint. Bilinearity gives \(u*v=\sum_i(u_i*v)\). Lemma 2.2 then yields
\[
 A(u*v)=\bigcup_i A(u_i*v),\qquad
 C_h=\operatorname{conv}\bigcup_i C_{h_i}.
 \tag{6.4}
\]
The second equality follows by taking convex hulls in the first and using (6.3). Taking a convex hull of the union of the individual convex hulls gives the same set as taking the convex hull of the original union. There are only finitely many compact sets, so this convex hull is compact and needs no extra closure. Empty sets can be omitted; if all are empty, both sides are empty.
Taking support functions in (6.4) proves (6.1), including the all-collapsed case.

*Proof of the family identity.* For each \(h\in\mathcal J(u)\), extend its profile to a joint tuple containing every \(u_i\), using the finite projection theorem. Formula (6.1) puts \(h\) in the right side of (6.2).
Conversely a tuple in \(\mathcal J(u_1,\ldots,u_k)\) can be extended to include \(u\). The prescribed component profiles are retained on a further subsequence. Its added indicator \(h\) satisfies (6.1), so the maximum is an actual member of \(\mathcal J(u)\). This proves the opposite inclusion. \(\square\)

The theorem concerns the indicators of profiles on the same frequencies. It does not assert addition of normalized logarithms for a sum, or pointwise dominance of one Fourier summand at every complex frequency. Without separate singularities the conclusion can fail: \(u_1=\delta_0\) and \(u_2=-\delta_0\) each have indicator zero, while their zero sum has only the collapsed indicator.

## References

- Terence Tao, [246B, Notes 2: Some connections with the Fourier transform](https://terrytao.wordpress.com/2021/01/23/246b-notes-2-some-connections-with-the-fourier-transform/), 2021. Background on compact support, entire Fourier transforms and convolution; its normalization differs from (1.1).
- Terence Tao, [245B, Notes 9: The Baire category theorem and its Banach space consequences](https://terrytao.wordpress.com/2009/02/01/245b-notes-9-the-baire-category-theorem-and-its-banach-space-consequences/), 2009. Background on the complete frequency-selective construction used in the preceding lesson.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, Springer, 1983. Compact distributions, singular support and polynomial Fourier transforms.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, Springer, 1983, Chapter XVI. Isolated support points and convolution profile geometry. The local calculus,common-core argument,atomic construction and finite joint maximum formula are proved above.
