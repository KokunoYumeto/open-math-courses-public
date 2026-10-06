# Spectral radius and characters of a Banach algebra

**Programme reading HA-LCA-PRE-BANACH.** This reading precedes HA-LCA-02 and HA-LCA-03. It proves the spectral-radius and character results used later in Bochner's theorem, including the case without an identity. Its final section supplies the product compactness needed for the topology of the character space.

We use set theory with choice, taking the maximal principle as the form of the choice axiom: a partially ordered set in which every chain has an upper bound has a maximal element. We also use the complete ordered real field and its complexification, and the definitions of vector space, norm, completeness, topology and continuity. The analytic and compactness results used below are proved here. A Banach space is a complete normed complex vector space. Algebra multiplication is associative and complex bilinear.

## 1. The integration facts needed for the resolvent

<a id="ha-lca-pre-banach-lemma-1-1"></a>
**Lemma 1.1 (elementary compactness).** A closed bounded subset of a finite-dimensional real coordinate space is compact. A continuous map from a compact metric space to a normed space is bounded and uniformly continuous. A real continuous function on a nonempty compact space attains its extrema. A real continuous function on an interval takes every value between its endpoint values.

**Proof.** Suppose an open cover of a closed box has no finite subcover. Bisect every coordinate interval and select one of the finitely many resulting closed boxes still having no finite subcover. Repeat. The nested coordinate intervals have lengths tending to zero, and completeness of the real field gives a common point: its coordinates are the suprema of the left endpoints. An open member of the cover containing this point contains all of a sufficiently small selected box. This contradicts the selection. A closed subset of the box is compact by adding its open complement to a cover. Every closed bounded set lies in a box.

For a continuous map \(f:K\to E\), continuity gives, at each \(x\in K\), a radius \(r_x>0\) such that
\(d(x,y)<2r_x\) implies \(\|f(y)-f(x)\|<\varepsilon/2\).
Choose a finite cover of \(K\) by the balls of radii \(r_x\). If \(\delta\) is the minimum of their radii, two points at distance less than \(\delta\) that meet the same selected ball of radius \(r_x\) both lie in its ball of radius \(2r_x\). The triangle inequality proves uniform continuity. The analogous finite cover with image oscillation less than one proves boundedness.

A continuous image of a compact space is compact, since inverse images turn an open cover into an open cover. A compact subset of a Hausdorff space is closed: for a point outside it, separate that point from each point of the compact set, and then take a finite subcover on the compact side and the intersection of the corresponding neighbourhoods on the other side. Thus a compact subset of \(\mathbb R\) contains its supremum and infimum. Finally, for a continuous function with opposite signs at the endpoints, successively bisect and retain a half interval whose endpoint signs are opposite, unless a zero has already been found. The common point of the retained intervals is a zero by continuity. Subtracting the desired value proves the last assertion. \(\square\)

<a id="ha-lca-pre-banach-lemma-1-2"></a>
**Lemma 1.2 (Banach-valued elementary calculus).** Let \(E\) be a Banach space.

1. A continuous \(f:[a,b]\to E\) has a Riemann integral. It is linear, additive over adjacent intervals, and satisfies
   \[
   \left\|\int_a^b f(t)\,dt\right\|\le (b-a)\sup_{[a,b]}\|f(t)\|.
   \]
   Uniform limits commute with this integral.
2. If \(F:[a,b]\to E\) is continuously differentiable, with one-sided derivatives at the endpoints, then
   \[
   F(b)-F(a)=\int_a^b F'(t)\,dt.
   \]
3. If \(q(r,t)\) and its partial derivative \(\partial_rq(r,t)\) are continuous on a compact rectangle, then in its interior
   \[
   \frac{d}{dr}\int_a^b q(r,t)\,dt
   =\int_a^b\partial_rq(r,t)\,dt.
   \]
4. Uniformly convergent series can be integrated term by term. A series of continuously differentiable functions whose derivatives converge uniformly, and whose values converge at one point, can be differentiated term by term on a compact interval.

**Proof.** Write \(\omega(\delta)=\sup\{\|f(s)-f(t)\|:|s-t|\le\delta\}\). Lemma 1.1 gives \(\omega(\delta)\to0\). A tagged Riemann sum and any refinement differ by at most \((b-a)\omega(\delta)\), where \(\delta\) is the original mesh. Comparing two sums through a common refinement proves that all sums of small mesh have the same limit in \(E\). The norm estimate, linearity and additivity pass from sums to their limits. The estimate applied to a difference proves continuity under uniform limits.

Here is a norm-valued substitute for the real mean-value argument. If a differentiable \(H\) satisfies \(\|H'(t)\|\le M\), then
\[
\|H(v)-H(u)\|\le M(v-u)\quad(u<v).
\]
Otherwise choose \(c>M\) with \(\|H(v)-H(u)\|>c(v-u)\). At least one half interval has the same strict inequality with \(c\), by the triangle inequality. Nested bisection produces intervals \([u_j,v_j]\) containing a common point \(t_0\). Differentiability at \(t_0\) gives
\[
H(v_j)-H(u_j)=H'(t_0)(v_j-u_j)+o(v_j-u_j),
\]
since \(|v_j-t_0|+|u_j-t_0|=v_j-u_j\). This contradicts \(c>M\). One-sided differentiability handles an endpoint. In particular, a function with zero derivative is constant.

For continuous \(f\), the function \(J(t)=\int_a^t f(s)\,ds\) has derivative \(f(t)\): the difference quotient is the average over a small interval, whose difference from \(f(t)\) is bounded by its local oscillation. Apply this to \(f=F'\). The difference \(F-J\) has zero derivative, proving assertion 2.

For assertion 3, assertion 2 in the \(r\) variable gives
\[
\frac{q(r+h,t)-q(r,t)}h-\partial_rq(r,t)
=\frac1h\int_r^{r+h}\bigl(\partial_rq(s,t)-\partial_rq(r,t)\bigr)\,ds.
\]
Its norm tends uniformly to zero in \(t\), by Lemma 1.1. Assertion 1 now proves differentiation under the integral. For assertion 4, apply assertion 1 to partial sums. For derivatives, integrate the uniformly convergent derivative series and use the identity in assertion 2 for each partial sum and the convergent values at the fixed point. This gives both uniform convergence of the original series and the claimed derivative. The product and chain rules used with these assertions follow by subtracting and adding the intermediate product, or by substituting the defining first-order remainder; bounded bilinear multiplication controls the product remainder. \(\square\)

<a id="ha-lca-pre-banach-lemma-1-3"></a>
**Lemma 1.3 (a periodic parametrization).** There is a number \(\tau>0\) and a continuously differentiable scalar function \(e(t)\), \(t\in\mathbb R\), such that
\[
e(0)=e(\tau)=1,\qquad e(t+s)=e(t)e(s),\qquad
e'(t)=ie(t),\qquad |e(t)|=1.
\]
For every integer \(k\ne0\),
\[
\int_0^\tau e(t)^k\,dt=0,
\qquad \int_0^\tau 1\,dt=\tau.
\]
One may write \(\tau=2\pi\) and \(e(t)=\exp(it)\).

**Proof.** Define \(\exp z=\sum_{n\ge0}z^n/n!\). On \(|z|\le R\), the terms of this series and of its formal derivative are bounded by a summable sequence: after any integer larger than \(2R+2\), the ratios of successive majorants are at most \(1/2\). The scalar majorant bounds every difference of partial sums; completeness therefore gives a uniform limit for each series. Lemma 1.2 applied on real parameter intervals gives
\(d\exp(it)/dt=i\exp(it)\).

Absolutely convergent series can be multiplied and regrouped: discard tails so that the sum of norms of all omitted products is small, and perform the remaining finite multiplication. The binomial formula, obtained by expanding a finite product, then gives \(\exp(z+w)=\exp z\exp w\). Conjugating the series and putting \(w=-z\) shows \(|\exp(it)|^2=1\).

Let \(c(t)=\operatorname{Re}\exp(it)\) and \(s(t)=\operatorname{Im}\exp(it)\). Then \(c'=-s\), \(s'=c\), \(c(0)=1\), \(s(0)=0\). Also \(c(2)<0\): its series begins \(1-2+2/3\), and the remaining alternating terms have negative sum, since their absolute values strictly decrease; this last assertion follows by grouping successive negative-positive pairs and taking the tail limit. Lemma 1.1 supplies a zero in \((0,2)\). The closed set of zeros in \([0,2]\) has a least member \(\alpha>0\); continuity and the intermediate-value assertion give \(c(t)>0\) on \([0,\alpha)\). Hence
\(s(\alpha)=\int_0^\alpha c(t)\,dt>0\).
The strict inequality follows by integrating over a small interval where \(c>1/2\); elsewhere \(c\ge0\). Since \(c^2+s^2=1\), we obtain \(s(\alpha)=1\) and \(\exp(i\alpha)=i\). Put \(\tau=4\alpha\). The multiplication law gives \(\exp(i\tau)=1\) and periodicity. For every integer \(k\), including negative integers, differentiation of \(e^k\) gives \(ik e^k\); inverses exist because \(|e|=1\). The integral identities follow from Lemma 1.2 and equal endpoint values. \(\square\)

<a id="ha-lca-pre-banach-lemma-1-4"></a>
**Lemma 1.4 (radial coefficient identity).** Suppose \(H\) is a Banach-valued complex differentiable function with continuous complex derivative on the annulus \(r_0<|z|<r_1\). For each integer \(n\ge0\), set
\[
J_n(r)=\frac1\tau\int_0^\tau
 r^{n+1}e(t)^{n+1}H(re(t))\,dt
\quad(r_0<r<r_1).
\]
Then \(J_n(r)\) is independent of \(r\).

**Proof.** On a compact subinterval of the permitted radii, the integrand \(Q(r,t)\) and both partial derivatives are continuous. The chain rule gives
\[
\partial_tQ=ir\,\partial_rQ.
\]
Consequently Lemma 1.2 yields
\[
J_n'(r)=\frac1{ir\tau}\int_0^\tau\partial_tQ(r,t)\,dt
=\frac{Q(r,\tau)-Q(r,0)}{ir\tau}=0.
\]
The final equality is Lemma 1.3. The zero-derivative assertion in Lemma 1.2 proves constancy between any two permitted radii. \(\square\)

## 2. Resolvents and the spectral radius

A **Banach algebra** \(A\) has a complete norm satisfying \(\|ab\|\le\|a\|\|b\|\). A unital Banach algebra in this section is nonzero and has identity \(1\) of norm one. An inverse always means a two-sided inverse. Write
\[
\sigma_A(a)=\{z\in\mathbb C:z1-a\text{ is not invertible in }A\}.
\]

<a id="ha-lca-pre-banach-lemma-2-1"></a>
**Lemma 2.1 (geometric inversion).** If \(\|b\|<1\), then
\[
(1-b)^{-1}=\sum_{k=0}^\infty b^k.
\]
The invertible elements form an open set and inversion is continuous there. For fixed \(a\in A\), its resolvent \(R(z)=(z1-a)^{-1}\) has continuous complex derivative \(R'(z)=-R(z)^2\) wherever it is defined. Moreover,
\[
|z|>\|a\|\quad\Longrightarrow\quad
R(z)=\sum_{k=0}^\infty a^k z^{-k-1},\qquad
\|R(z)\|\le\frac1{|z|-\|a\|}.
\]

**Proof.** Every series with summable norms converges in a Banach space: the norm of a difference of partial sums is bounded by the corresponding scalar tail. Multiplication of the partial geometric sum by \(1-b\), on either side, gives \(1-b^{N+1}\to1\). This proves the first assertion.

If \(u\) is invertible and \(\|u^{-1}v\|<1\), then
\(u+v=u(1+u^{-1}v)\) is invertible, and its inverse converges to \(u^{-1}\) as \(v\to0\), by the geometric tail bound. This proves openness and continuity. Factoring \(z1-a=z(1-a/z)\) proves the last display. Near a resolvent point \(z\),
\[
R(z+h)=(1+hR(z))^{-1}R(z)
=R(z)-hR(z)^2+O(|h|^2).
\]
The geometric tail bounds the remainder in norm; continuity of inversion gives continuity of the displayed derivative. \(\square\)

<a id="ha-lca-pre-banach-theorem-2-2"></a>
**Theorem 2.2 (nonempty spectrum and spectral radius).** The spectrum of \(a\) is nonempty and compact. Its radius satisfies the full limit formula
\[
r_A(a):=\max_{z\in\sigma_A(a)}|z|
=\lim_{n\to\infty}\|a^n\|^{1/n}
=\inf_{n\ge1}\|a^n\|^{1/n}.                 \tag{1}
\]
The algebra need not be commutative.

**Proof.** Lemma 2.1 says the complement of the spectrum is open and contains \(\{|z|>\|a\|\}\). Thus the spectrum is closed and bounded, and Lemma 1.1 makes it compact.

For \(r>\|a\|\), insert the uniformly convergent geometric resolvent series into Lemma 1.4. Its \(k\)-th integrated term is
\[
a^k r^{n-k}\frac1\tau\int_0^\tau e(t)^{n-k}\,dt.
\]
Only \(k=n\) survives, by Lemma 1.3. Therefore
\[
J_n(r)=a^n.                                  \tag{2}
\]
If the spectrum were empty, \(R\) would be defined on all of \(\mathbb C\). Lemma 1.4 would make \(J_0(r)=1\) for every \(r>0\). But continuity of \(R\) near zero would give
\(\|J_0(r)\|\le r\sup_{0\le t\le\tau}\|R(re(t))\|\to0\),
a contradiction. This proves nonemptiness and justifies the maximum defining \(r_A(a)\).

For any fixed \(r>r_A(a)\), the whole annulus \(r_A(a)<|z|<\infty\) lies in the resolvent set. Lemma 1.4 extends (2) to this \(r\). Hence, with finite \(M_r=\sup_t\|R(re(t))\|\),
\[
\|a^n\|\le r^{n+1}M_r.
\]
Taking \(n\)-th roots gives \(\limsup_n\|a^n\|^{1/n}\le r\), and then at most \(r_A(a)\) by letting \(r\downarrow r_A(a)\). The elementary limit \(C^{1/n}\to1\) for \(C>0\) follows, for example, because \((1+\varepsilon)^n\ge1+n\varepsilon\to\infty\); apply this also to \(1/C\) when \(C<1\). Thus the argument includes \(r_A(a)=0\).

For the reverse bound, let \(z\in\sigma_A(a)\). The factorization
\[
z^n1-a^n=(z1-a)\sum_{j=0}^{n-1}z^{n-1-j}a^j
\]
has commuting factors. If commuting elements \(u,v\) have invertible product \(uv\), then \(u\) is invertible: both \(u\) and \(v\) commute with \((uv)^{-1}\), and \(v(uv)^{-1}\) is a two-sided inverse for \(u\). The commutation with the inverse follows by multiplying \(u(uv)=(uv)u\) on both sides by that inverse. It follows that \(z^n\in\sigma_A(a^n)\). Lemma 2.1 applied to \(a^n\) now gives \(|z|^n\le\|a^n\|\). Maximize over \(z\). Every root in (1) is at least \(r_A(a)\), while their upper limit is at most that number. They therefore converge to it, and their infimum is also that number. \(\square\)

<a id="ha-lca-pre-banach-corollary-2-3"></a>
**Corollary 2.3 (division algebras).** A nonzero unital complex Banach algebra in which every nonzero element is invertible consists exactly of scalar multiples of its identity.

**Proof.** For \(a\), choose \(z\in\sigma_A(a)\) by Theorem 2.2. The noninvertible element \(z1-a\) must be zero. Thus every \(a\) is a scalar multiple of \(1\), uniquely since \(1\ne0\). The identification with \(\mathbb C\) preserves sums, products and norm. \(\square\)

## 3. Ideals, characters and adjoining an identity

<a id="ha-lca-pre-banach-lemma-3-1"></a>
**Lemma 3.1 (closed quotients).** If \(I\) is a closed two-sided ideal in a Banach algebra \(A\), then \(A/I\), with
\[
\|a+I\|=\inf_{y\in I}\|a+y\|,
\]
is a Banach algebra. If \(A\) is unital and \(I\) proper, the quotient identity has norm one.

**Proof.** The infimum is independent of representative. Homogeneity and the triangle inequality follow by choosing representatives within an arbitrary positive error of their infima. Norm zero means the representative lies in the closure of \(I\), hence in \(I\). Multiplication is well-defined because \(I\) is two-sided. Choosing separate nearly minimal representatives for two cosets proves submultiplicativity, on letting their errors tend to zero.

For completeness, take a Cauchy sequence of cosets and a subsequence \(q_j\) with \(\|q_{j+1}-q_j\|<2^{-j-1}\). Choose a representative \(b_j\) of \(q_{j+1}-q_j\) with \(\|b_j\|<2^{-j}\). For a representative \(b_0\) of \(q_1\), the convergent series \(b_0+\sum_{j\ge1}b_j\) represents the limit of the subsequence. The quotient norm is at most the norm of each representative, so the coset convergence follows from the series tail estimate. The original Cauchy sequence has the same limit by its Cauchy property.

The quotient identity has norm at most one. If it had norm less than one, there would be \(y\in I\) with \(\|1-y\|<1\). Lemma 2.1 would make \(y\) invertible, forcing \(1\in I\), a contradiction. \(\square\)

<a id="ha-lca-pre-banach-lemma-3-2"></a>
**Lemma 3.2 (maximal ideals).** In a commutative unital Banach algebra, each proper ideal is contained in a maximal proper ideal. Every maximal proper ideal \(M\) is closed, and \(A/M\) is canonically \(\mathbb C\).

**Proof.** Order the proper ideals containing a fixed proper ideal by inclusion. The union of a chain is an ideal: any finite list of its elements lies in one member of the chain. The union is proper because none of its members contains \(1\). The maximal principle therefore supplies a maximal proper ideal.

The closure of an ideal is an ideal, by continuity of addition and multiplication. The closure of a proper ideal is proper: otherwise some element of the ideal would be at distance less than one from \(1\), contrary to Lemma 2.1. Maximality now makes \(M\) closed. For \(a\notin M\), the ideal \(M+Aa\) is all of \(A\), so \(1=m+ba\) for some \(m\in M,b\in A\). Thus the nonzero coset of \(a\) is invertible in \(A/M\). Lemma 3.1 and Corollary 2.3 identify this quotient with the scalars. The identification is canonical because it sends the quotient identity to \(1\in\mathbb C\). \(\square\)

<a id="ha-lca-pre-banach-theorem-3-3"></a>
**Theorem 3.3 (spectrum through characters).** A character is a nonzero complex-linear multiplicative map \(\chi:A\to\mathbb C\). On a commutative unital Banach algebra every character is continuous, has norm one, and sends \(1\) to \(1\). Moreover,
\[
\sigma_A(a)=\{\chi(a):\chi\text{ a character}\},\qquad
r_A(a)=\sup_\chi|\chi(a)|.                    \tag{3}
\]
The kernels of characters are exactly the maximal proper ideals, and each such ideal is the kernel of exactly one character.

**Proof.** Choose \(b\) with \(\chi(b)\ne0\). From \(\chi(b)=\chi(1)\chi(b)\) we get \(\chi(1)=1\). An invertible element has nonzero character value, by applying \(\chi\) to its inverse identity. Therefore \(\chi(a)1-a\) is noninvertible and \(\chi(a)\in\sigma_A(a)\). Lemma 2.1 gives \(|\chi(a)|\le\|a\|\), proving continuity and norm at most one; evaluation at \(1\) gives equality.

The kernel is maximal: if an ideal \(J\) strictly contains it, choose \(b\in J\) with \(\chi(b)\ne0\). Then \(b-\chi(b)1\) lies in the kernel and hence in \(J\), so subtraction and division by \(\chi(b)\) put \(1\) in \(J\). Thus \(J=A\). Conversely Lemma 3.2 constructs a character with kernel any given maximal ideal. If a character has kernel \(M\), the equality \(a+M=z1+M\) forces \(\chi(a)=z\); hence it is unique.

If \(z\in\sigma_A(a)\), the ideal \(A(z1-a)\) is proper: containing \(1\) would give an inverse, using commutativity. Put it inside a maximal ideal, and apply its character. This gives \(z=\chi(a)\), proving the reverse inclusion in (3). Taking absolute values proves the radius statement. \(\square\)

<a id="ha-lca-pre-banach-theorem-3-4"></a>
**Theorem 3.4 (the case without an identity).** For any complex Banach algebra \(A\), including the zero algebra, its unitization is
\[
A^+=\mathbb C\oplus A,\qquad
(\lambda,a)(\mu,b)=(\lambda\mu,\lambda b+\mu a+ab),
\qquad \|(\lambda,a)\|=|\lambda|+\|a\|.
\]
It is a unital Banach algebra, and \(a\mapsto(0,a)\) is an isometric algebra embedding. If \(A\) is commutative and \(\Delta(A)\) is its set of characters, then
\[
\sigma_{A^+}((0,a))=\{0\}\cup\{\chi(a):\chi\in\Delta(A)\},
\qquad
\lim_{n\to\infty}\|a^n\|^{1/n}
=\sup\bigl(\{0\}\cup\{|\chi(a)|:\chi\in\Delta(A)\}\bigr).
                                                        \tag{4}
\]
All characters of \(A\) are contractive. For a unital \(A\), using this unitization merely adds zero to its ordinary spectrum and leaves its radius unchanged.

**Proof.** Bilinearity is immediate. Expanding a triple product on either association gives scalar part \(\lambda\mu\nu\) and vector part
\[
\lambda\mu c+\lambda\nu b+\mu\nu a+\lambda bc+\mu ac+\nu ab+(ab)c,
\]
with \((ab)c=a(bc)\). This proves associativity, even when \(A\) is noncommutative. The identity is \((1,0)\), of norm one. The triangle inequality and submultiplicativity in \(A\) bound the norm of a product by \((|\lambda|+\|a\|)(|\mu|+\|b\|)\). A Cauchy sequence has Cauchy scalar and vector coordinates, so the norm is complete. The embedding and its norm assertion follow directly from the definition.

Every \(\chi\in\Delta(A)\) extends to a character
\(\chi^+(\lambda,a)=\lambda+\chi(a)\); direct expansion verifies multiplication. By Theorem 3.3 it is contractive, so \(|\chi(a)|\le\|a\|\). Every character of \(A^+\) restricts either to a character of \(A\), in which case it is this extension, or to zero, in which case it is \(\epsilon(\lambda,a)=\lambda\). Apply Theorems 3.3 and 2.2 in \(A^+\), and note \((0,a)^n=(0,a^n)\), to obtain (4). If \(A\) already has an identity, Theorem 3.3 identifies the nonzero-character values with its ordinary spectrum, proving the last assertion. \(\square\)

## 4. Compactness and the Gelfand transform

<a id="ha-lca-pre-banach-lemma-4-1"></a>
**Lemma 4.1 (arbitrary product compactness).** A product of compact Hausdorff spaces, with the product topology, is compact Hausdorff. No countability hypothesis is needed.

**Proof.** A proper filter on a set is a family of subsets closed under supersets and finite intersections, containing the whole set and not the empty set. A maximal such filter is an ultrafilter. Every proper filter extends to one by the maximal principle: a chain union is again a proper filter. An ultrafilter contains, for every subset \(S\), either \(S\) or its complement. Indeed, if adjoining \(S\) cannot generate a proper filter, some member of the original filter is disjoint from \(S\), which puts the complement in the filter. Otherwise maximality puts \(S\) in it. It cannot contain both.

A space is compact if and only if every ultrafilter on its underlying set converges to some point, where convergence means that every neighbourhood of the point belongs to the filter. To prove the forward implication, the closures of filter members have the finite-intersection property. Compactness implies their common intersection is nonempty, since otherwise their open complements would have a finite subcover. Choose a point \(x\) in that intersection. If an open neighbourhood \(U\) of \(x\) were absent from the filter, its closed complement would belong to the filter, contradicting the choice of \(x\). Thus the filter converges. Conversely, a cover with no finite subcover has complements generating a proper filter. An ultrafilter extending it could not converge: a covering open set containing a putative limit and its complement would both belong to the filter. This proves the characterization.

If a product has an empty factor, it is empty and hence compact. Otherwise choice supplies an element of each factor. Given an ultrafilter on the product, its image filter in coordinate \(j\), defined by \(S\mapsto p_j^{-1}(S)\), is an ultrafilter on that factor. Choose a limit \(x_j\) in each compact factor. Every basic neighbourhood of \(x=(x_j)_j\) imposes conditions on only finitely many coordinates. Its inverse-image conditions belong to the original filter, and so does their finite intersection. The original filter therefore converges to \(x\). The characterization proves compactness. Two distinct product points differ in a coordinate; disjoint neighbourhoods in that Hausdorff factor separate the points in the product. \(\square\)

<a id="ha-lca-pre-banach-theorem-4-2"></a>
**Theorem 4.2 (topology of the character space).** Give \(\Delta(A)\) the topology of pointwise convergence on \(A\).

For a commutative unital Banach algebra it is a nonempty compact Hausdorff space. For a general commutative Banach algebra it is locally compact Hausdorff, and each function
\[
\widehat a:\Delta(A)\to\mathbb C,\qquad \widehat a(\chi)=\chi(a),
\]
belongs to \(C_0(\Delta(A))\). The Gelfand transform \(a\mapsto\widehat a\) is a contractive algebra homomorphism and
\[
\|\widehat a\|_\infty=r_{A^+}((0,a))
=\lim_n\|a^n\|^{1/n}.                       \tag{5}
\]
For the empty character space its uniform norm is zero. Injectivity or density of its range is not asserted for an arbitrary Banach algebra.

**Proof.** In the unital case place the character space inside
\(\prod_{a\in A}\{z\in\mathbb C:|z|\le\|a\|\}\).
Each factor is compact by Lemma 1.1, so the product is compact Hausdorff by Lemma 4.1. The equations expressing additivity, complex homogeneity, multiplication and value one at \(1\) are closed conditions on the coordinates; subtraction and multiplication of finitely many complex coordinates are continuous. They specify exactly the characters. A closed subset of a compact space is compact, as proved in Lemma 1.1, and a subspace of a Hausdorff space is Hausdorff. Existence follows from Lemma 3.2 and Theorem 3.3.

For general \(A\), Theorem 3.4 identifies \(\Delta(A)\) with \(\Delta(A^+)\setminus\{\epsilon\}\), where \(\epsilon(\lambda,a)=\lambda\). This is a homeomorphism: restriction is continuous coordinate by coordinate, and the inverse extension has coordinate values \(\lambda+\chi(a)\), also continuous. The point \(\epsilon\) is closed in the compact Hausdorff space, so its complement is open. An open subspace of a compact Hausdorff space is locally compact: for a point in the open subspace, separate it from each point of the closed compact complement, take a finite subcover of that complement, and intersect the corresponding neighbourhoods of the first point. The closure of this intersection avoids the complement and is compact. If the complement is empty, the whole compact space itself is a compact neighbourhood. This supplies the required local compactness in every case.

The continuous coordinate function \(\widehat{(0,a)}\) on \(\Delta(A^+)\) vanishes at \(\epsilon\). Therefore for every \(\delta>0\), its closed level set \(\{|\widehat{(0,a)}|\ge\delta\}\) is compact and avoids \(\epsilon\). Restricted to \(\Delta(A)\), this is exactly the assertion that \(\widehat a\) vanishes at infinity. Linearity and multiplication are coordinatewise identities. Contractivity and (5) are Theorem 3.4. In the already unital case the added zero leaves the radius unchanged. \(\square\)

## Source reading

The freely accessible author versions used for comparison are Michael Taylor's [*Lectures on Banach Algebras*](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/banalg.pdf), §1, §2 through Proposition 2.6 and Appendix B through Proposition B.1, and Jacob Lurie's [*Math 261y: von Neumann Algebras, Lecture 2*](https://people.math.harvard.edu/~lurie/261ynotes/lecture2.pdf), 2 September 2011, Proposition 5 through Remark 15. Both were accessed on 4 October 2026. This reading supplies its own complete derivations, including the radial integral argument and the supporting calculus, quotient and compactness proofs; none of the source citations is used in place of a proof.
