# The Weyl integration formula

*Written and self-checked by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. No separate AI review of this revision is recorded. Public domain (CC0). Revised and self-checked on 3 October 2026 by GPT-6.1 Sol (OpenAI), Ultra effort.*

Integrating over a compact group can be reduced to integrating over its maximal torus. The correction factor measures how rapidly conjugacy classes change: it vanishes when a torus element acquires extra infinitesimal symmetries. For unitary matrices this factor becomes the squared Vandermonde determinant, expressing repulsion between coincident eigenvalues.

Throughout, \(G\) is a compact connected Lie group, \(T\) a maximal torus, and \(W=N_G(T)/T\). Haar measures \(dg,dt\) have mass one. We import the roots, multiplicity-one theorem, normalizer action and torus conjugacy from [Roots and the Weyl group](RT-CPT-07.md). Smooth homogeneous spaces and their local sections are [*Invariant connections on homogeneous bundles*, Theorem 1.1](course:DG-FND/invariant-connections-on-homogeneous-bundles#section-1); the inverse function theorem is [*Local tools for bundles and transport*, Theorem 1.1](course:DG-FND/local-tools-for-bundles-and-transport#section-1). We use the ordinary multivariable change-of-variables theorem for a smooth diffeomorphism, including nonnegative measurable functions, as a core calculus prerequisite. Covering and measure-zero assertions will be proved here.

Choose positive roots \(\Phi^+\) and define the honest function on \(T\)
\[
\Delta(t)=\prod_{\alpha\in\Phi^+}(1-\alpha(t)^{-1}),
\qquad j(t)=|\Delta(t)|^2. \tag{1.1}
\]
The modulus does not depend on the positive system: each opposite pair has the same modulus. This definition uses only characters of \(T\). A formal factor involving the half-sum \(\rho\) is unnecessary, and need not itself be a character for a group that is not simply connected.

## Measures and the differential of conjugation

An invariant positive inner product on \(\mathfrak g\) gives a bi-invariant metric on \(G\), its induced metric on \(T\), and the quotient metric on \(G/T\). Write \(\mathfrak m=\mathfrak t^\perp\); the quotient tangent space at \(eT\) is identified isometrically with \(\mathfrak m\). The resulting volume measures are invariant.

The probability measure \(d(gT)\) on \(G/T\) is also the pushforward of \(dg\). Here is a useful uniqueness check. If \(\nu\) is any invariant probability on this transitive space and \(F\) is continuous, then
\[
\int_{G/T}F\,d\nu
=\int_{G/T}\int_G F(gx)\,dg\,d\nu(x).
\]
The inner integral is independent of \(x\), by transitivity and right invariance of \(dg\), and equals \(\int_G F(gT)\,dg\). This proves uniqueness and identifies normalized quotient volume with the pushforward measure.

For the unnormalized metric volumes there is the exact identity
\[
\operatorname{vol}(G)
=\operatorname{vol}(G/T)\operatorname{vol}(T). \tag{1.2}
\]
Indeed \(G\to G/T\) has orthogonal horizontal and vertical tangent spaces, its differential is an isometry on the horizontal space, and every fiber is an isometric translate of \(T\). In a local bundle trivialization, the horizontal/vertical change of basis is triangular with diagonal identity. The volume density is therefore the base density times the fiber density. Local integration and a partition of unity prove (1.2). This establishes the normalization before the integration formula is used.

Consider the smooth map
\[
\psi:G/T\times T\longrightarrow G,\qquad
\psi(gT,t)=gtg^{-1}. \tag{1.3}
\]
It is well defined because \(T\) is abelian, and is onto by the maximal torus theorem.

**Lemma 1.4 (Jacobian).** For the product metric volume on the domain and the metric volume on the target, the absolute Jacobian of \(\psi\) at \((gT,t)\) is
\[
j(t)=\det_{\mathbb R}\bigl(\operatorname{Ad}(t^{-1})-1\mid\mathfrak m\bigr)
=\prod_{\alpha\in\Phi}(1-\alpha(t))
=\prod_{\alpha\in\Phi^+}|1-\alpha(t)|^2. \tag{1.5}
\]

*Proof.* Conjugating the target by \(g^{-1}\) and translating the domain quotient by \(g^{-1}\) are isometries, so compute at \((eT,t)\). For \(X\in\mathfrak m\) and \(H\in\mathfrak t\), use the curve
\[
(\exp(sX)T,t\exp(sH)).
\]
Left translating its image tangent by \(t^{-1}\) gives
\[
d\psi(X,H)=\bigl(\operatorname{Ad}(t^{-1})-1\bigr)X+H. \tag{1.6}
\]
The operator preserves \(\mathfrak m\), and the second summand is the identity on \(\mathfrak t\). Thus its determinant is the determinant displayed in (1.5).

Each opposite pair of roots is one real two-plane in \(\mathfrak m\), by multiplicity one. On its complexification \(\operatorname{Ad}(t^{-1})\) has eigenvalues \(\alpha(t)^{-1},\alpha(t)\). The determinant on that plane is
\[
(\alpha(t)^{-1}-1)(\alpha(t)-1)
=|1-\alpha(t)|^2\geq0.
\]
Multiplying these contributions proves the equality and shows that no absolute-value sign changes the resulting determinant. In particular the derivative is invertible precisely when no root takes the value one. \(\square\)

Identity (1.2) means the same Jacobian works for the three normalized measures: the source product volume and target volume are divided by the same total volume. If \(\Phi\) is empty, \(\mathfrak m=0\), the empty determinant and product are one, and \(G=T\).

## Regular elements and the number of sheets

Set
\[
T_{\mathrm{reg}}=\{t\in T:\alpha(t)\neq1\text{ for every }\alpha\in\Phi\},
\qquad G_{\mathrm{reg}}=\psi(G/T\times T_{\mathrm{reg}}).
\]
This definition of regularity concerns the group element's adjoint action. Its full centralizer is allowed to have more than one component.

**Lemma 2.1.** The set \(T_{\mathrm{reg}}\) is open, dense and has full Haar measure. The set \(G_{\mathrm{reg}}\) is open and has full Haar measure. The restriction
\[
\psi:G/T\times T_{\mathrm{reg}}\longrightarrow G_{\mathrm{reg}}
\]
is a covering with exactly \(|W|\) points over every target element.

*Proof.* A nontrivial root character has nonzero differential because \(T\) is connected. Hence \(\alpha:T\to S^1\) is a submersion: its differential is onto at the identity and at every point by translation. Its kernel is a compact smooth submanifold of codimension one, possibly with several components. It has measure zero and empty interior in torus charts. A finite union of these kernels is closed, null and has empty interior. This proves all three assertions about \(T_{\mathrm{reg}}\).

We give the corresponding image argument, since a null set cannot in general be pushed through an arbitrary smooth map without checking dimensions. Let \(d=\dim G\). Each compact manifold
\[
G/T\times\ker\alpha
\]
has dimension \(d-1\). A smooth image of such a manifold in a \(d\)-dimensional manifold has volume zero. To see this directly, cover the compact source by finitely many coordinate pieces with bounded first derivatives of the map, and work in finitely many target charts. A bounded \(k\)-dimensional coordinate piece can be covered by \(O(\varepsilon^{-k})\) cubes of side \(\varepsilon\). Lipschitz continuity puts each image in a ball of radius \(C\varepsilon\), whose target volume is \(O(\varepsilon^d)\). Thus the outer volume is \(O(\varepsilon^{d-k})\), tending to zero for \(k<d\). Smaller closed chart pieces give the asserted finite cover. Applying this with \(k=d-1\) proves that the finite union of their images is null.

A singular torus element cannot be conjugate to a regular torus element: the preceding lesson identifies torus conjugacy with a Weyl orbit, and \(W\) permutes roots. Surjectivity of \(\psi\) consequently gives
\[
G\setminus G_{\mathrm{reg}}
=\bigcup_{\alpha\in\Phi}\psi(G/T\times\ker\alpha). \tag{2.2}
\]
This is precisely the null set just considered. The inverse function theorem and Lemma 1.4 show that \(G_{\mathrm{reg}}\) is open and the restricted map is a local diffeomorphism.

Next count the fiber over \(s\in T_{\mathrm{reg}}\). Its Lie centralizer is \(\mathfrak t\), by the root decomposition. Hence
\[
C_G(s)^0=T. \tag{2.3}
\]
This equality does not assert \(C_G(s)=T\). If \(gtg^{-1}=s\) for \(t\in T_{\mathrm{reg}}\), the connected torus \(gTg^{-1}\) lies in \(C_G(s)^0=T\); equal dimensions give \(gTg^{-1}=T\). Thus \(g\in N_G(T)\). Every fiber point is therefore uniquely of the form
\[
(nT,n^{-1}sn),\qquad nT\in N_G(T)/T. \tag{2.4}
\]
There are exactly \(|W|\) of them. Distinct cosets give distinct first coordinates even if they happen to give the same second coordinate. Conjugating \(s\) proves the count over every point of \(G_{\mathrm{reg}}\).

The restricted map is proper. If \(K\subset G_{\mathrm{reg}}\) is compact, its preimage under the full map \(\psi\) is a compact subset of \(G/T\times T\); by (2.2) it contains no singular torus coordinate. It is therefore the preimage under the restricted map as well.

Finally a proper local diffeomorphism with these finite fibers is a covering. Around a target point choose disjoint inverse-function neighborhoods of all its preimages, and shrink their target neighborhoods to a common open set. No additional preimages can occur arbitrarily near that point outside these neighborhoods: otherwise a sequence of such preimages has a convergent subsequence by properness, with limit one of the already listed fiber points, a contradiction. Shrinking once more makes this an evenly covered neighborhood. This proves the covering assertion. The empty-root case is the identity map of a torus and satisfies the same statements. \(\square\)

For example a half-turn in \(SO(3)\) is regular: the root character on its rotation torus takes the value \(-1\). Its centralizer is the disconnected group \(O(2)\) described in the maximal-torus lesson. Both Weyl representatives fix that torus element, but (2.4) still gives two different quotient coordinates and two sheets.

## The general integration formula

**Theorem 3.1 (Weyl integration).** For every continuous complex-valued \(f\) on \(G\),
\[
\int_G f(x)\,dx
=\frac1{|W|}\int_T |\Delta(t)|^2
\left(\int_{G/T} f(gtg^{-1})\,d(gT)\right)dt. \tag{3.2}
\]
For a class function this reduces to
\[
\int_G f(x)\,dx
=\frac1{|W|}\int_T f(t)|\Delta(t)|^2\,dt. \tag{3.3}
\]

*Proof.* On an evenly covered open subset of \(G_{\mathrm{reg}}\), apply ordinary change of variables on each inverse sheet. The absolute Jacobian is \(j(t)\), and there are \(|W|\) sheets. A countable subordinate partition of unity, followed by integration, gives
\[
\int_{G/T\times T_{\mathrm{reg}}}
f(\psi(gT,t))j(t)\,d(gT)\,dt
=|W|\int_{G_{\mathrm{reg}}}f(x)\,dx. \tag{3.4}
\]
One can first use nonnegative functions and sum by monotone convergence, then apply the result to real and imaginary positive and negative parts. Countable partitions exist because these are finite-dimensional second-countable manifolds. Lemma 2.1 permits replacing \(G_{\mathrm{reg}}\) by \(G\). The omitted source set is null; also \(j\) is zero there. Replacing \(T_{\mathrm{reg}}\) by \(T\) is therefore valid. The normalized volume identity (1.2) and Fubini now give (3.2). Conjugation invariance makes its inner integral exactly \(f(t)\), proving (3.3). \(\square\)

In particular
\[
\int_T|\Delta(t)|^2\,dt=|W|. \tag{3.5}
\]
This normalization follows from the proved formula with \(f=1\); it was not assumed to fix an unknown constant in the proof.

The character orthogonality from [Fourier analysis and class functions](RT-CPT-03.md) consequently takes the torus form
\[
\frac1{|W|}\int_T
\chi_\pi(t)\overline{\chi_\sigma(t)}|\Delta(t)|^2\,dt
=\delta_{\pi\sigma}.
\]
Thus the torus's weighted measure computes the same character inner products as Haar measure on \(G\).

## Three classical densities

For \(SU(2)\), let \(t_\theta=\operatorname{diag}(e^{i\theta},e^{-i\theta})\). Its positive root is \(e^{2i\theta}\), so \(j(t_\theta)=4\sin^2\theta\) and \(|W|=2\). Formula (3.3) gives
\[
\int_{SU(2)}f(g)\,dg
=\frac1\pi\int_0^{2\pi}f(t_\theta)\sin^2\theta\,d\theta
=\frac2\pi\int_0^\pi f(t_\theta)\sin^2\theta\,d\theta. \tag{4.1}
\]
The last equality uses Weyl symmetry \(\theta\mapsto2\pi-\theta\). This agrees with the independent round-three-sphere calculation in the \(SU(2)\) lesson.

The trace is \(x=2\cos\theta\). Changing variables on \([0,\pi]\) gives its probability density
\[
\rho(x)=\frac{\sqrt{4-x^2}}{2\pi}\,\mathbf1_{[-2,2]}(x). \tag{4.2}
\]
This is the semicircle distribution on that interval. Its odd moments vanish by symmetry, and its even moments are
\[
\int x^{2k}\rho(x)\,dx
=\frac1{k+1}\binom{2k}{k}. \tag{4.3}
\]
For example substituting \(x=2u\) expresses the integral as
\[
\frac{2^{2k+1}}{\pi}
B\left(k+\tfrac12,\tfrac32\right).
\]
The beta integral \(B(a,b)=\int_0^1 v^{a-1}(1-v)^{b-1}\,dv\), its integration-by-parts recurrence, and \(B(\tfrac12,\tfrac32)=\pi/2\) give (4.3). In particular the second, fourth and sixth moments are \(1,2,5\). Also, using the characters \(\chi_m(t_\theta)=\sin((m+1)\theta)/\sin\theta\) established earlier, (4.1) reduces their orthogonality directly to
\[
\frac2\pi\int_0^\pi
\sin((m+1)\theta)\sin((n+1)\theta)\,d\theta=\delta_{mn}.
\]
Endpoint values are taken by continuity.

**Corollary 4.4 (unitary Vandermonde density).** For every continuous class function on \(U(n)\),
\[
\int_{U(n)}f(g)\,dg
=\frac1{n!}\int_{[0,2\pi)^n}
f(\operatorname{diag}(e^{i\theta_1},\ldots,e^{i\theta_n}))
\prod_{j<k}|e^{i\theta_j}-e^{i\theta_k}|^2
\frac{d\theta_1\cdots d\theta_n}{(2\pi)^n}. \tag{4.5}
\]

*Proof.* The positive roots are \(z_jz_k^{-1}\) for \(j<k\), and \(W=S_n\). Since \(|z_j|=|z_k|=1\), their factors satisfy \(|1-z_k/z_j|=|z_j-z_k|\). Substitute into (3.3). \(\square\)

This is the density for labeled eigenangles. On an ordered chamber one multiplies the density by \(n!\), since each generic unordered spectrum has that many labelings. For \(U(2)\), its density relative to \(d\theta_1d\theta_2/(2\pi)^2\) is
\[
\tfrac12|e^{i\theta_1}-e^{i\theta_2}|^2
=1-\cos(\theta_1-\theta_2).
\]
It integrates to one and vanishes when the eigenvalues coincide.

Write \(Sp(r)=USp(2r)\), to distinguish quaternionic dimension \(r\) from complex matrix size \(2r\). Its torus eigenvalues are \(e^{\pm i\theta_j}\), and \(|W|=2^r r!\). From the positive roots \(2\varepsilon_j,\varepsilon_j-\varepsilon_k,\varepsilon_j+\varepsilon_k\) we obtain
\[
j(\theta)=\prod_{j=1}^r4\sin^2\theta_j
\prod_{j<k}(2\cos\theta_j-2\cos\theta_k)^2.
\]
Indeed the pair of two-index factors is
\[
|1-e^{-i(\theta_j-\theta_k)}|^2
|1-e^{-i(\theta_j+\theta_k)}|^2
=(2\cos\theta_j-2\cos\theta_k)^2.
\]
Folding all sign changes to \([0,\pi]^r\) gives, for a class function \(F\),
\[
\int_{Sp(r)}F(g)\,dg
=\frac1{r!}\left(\frac2\pi\right)^r
\int_{[0,\pi]^r}F(t_\theta)
\prod_j\sin^2\theta_j
\prod_{j<k}(2\cos\theta_j-2\cos\theta_k)^2\,d\theta. \tag{4.6}
\]
Putting \(x_j=2\cos\theta_j\) gives the second form
\[
\int_{Sp(r)}F(g)\,dg
=\frac1{r!(2\pi)^r}\int_{[-2,2]^r}
F(t_{\arccos(x/2)})
\prod_{j<k}(x_j-x_k)^2
\prod_j\sqrt{4-x_j^2}\,dx. \tag{4.7}
\]
These are the two symplectic Sato–Tate measures in Lachaud's Theorem 3.1 and Proposition 3.2.

For \(USp(4)\), the density on the entire square is therefore
\[
\lambda_2(x,y)=\frac{(x-y)^2}{8\pi^2}
\sqrt{(4-x^2)(4-y^2)}
=\tfrac12(x-y)^2\rho(x)\rho(y). \tag{4.8}
\]
Its mass is \(\tfrac12(1+1)=1\), using the first two semicircle moments. Its trace is \(x+y\), with
\[
\mathbb E(\operatorname{tr}g)^2
=\tfrac12(2+2-2)=1,\qquad
\mathbb E(\operatorname{tr}g)^4
=\tfrac12(5+5-2-2)=3.
\]
For the second equality expand \((x+y)^4(x-y)^2\): its even part is \(x^6+y^6-x^4y^2-x^2y^4\), and odd terms integrate to zero. The ordered region \(x<y\) has twice the density in (4.8). Lachaud's Examples 3.3 prints \(1/(4\pi^2)\) for \(\lambda_2\); interpreted on the whole square as defined in Proposition 3.2, that coefficient gives mass two. Formula (4.8) retains the proposition's normalization.

## Exercises with complete solutions

**Exercise 1 (easy).** Check Theorem 3.1 for \(SU(2)\) against the round-sphere formula, and derive the trace distribution.

*Solution.* The torus character lattice has roots \(\pm2\), so the one positive-root factor gives \(4\sin^2\theta\). Haar measure on the torus is \(d\theta/(2\pi)\) and the Weyl order is two. Their product is \(\sin^2\theta\,d\theta/\pi\) on the full circle. The two Weyl-related halves agree for class functions, yielding \(2\sin^2\theta\,d\theta/\pi\) on \([0,\pi]\). Its mass is one since \(\int_0^\pi\sin^2\theta\,d\theta=\pi/2\). Under \(x=2\cos\theta\), \(|dx|=2\sin\theta\,d\theta\), so the pushed-forward density is \(\sin\theta/\pi=\sqrt{4-x^2}/(2\pi)\). This proves (4.2), including the normalization.

**Exercise 2 (medium).** Derive Corollary 4.4, and independently check its normalization by torus Fourier orthogonality.

*Solution.* On the diagonal torus of \(U(n)\), conjugating \(E_{jk}\) multiplies it by \(z_j/z_k\). The positive-root product thus has squared modulus \(\prod_{j<k}|z_j-z_k|^2\), and the normalizer quotient is the \(n!\) coordinate permutations. This gives (4.5).

For the independent check, put
\[
D(z)=\det[z_j^{\,n-i}]_{i,j=1}^n.
\]
Its modulus squared is the same Vandermonde product. Expand the determinant: its \(n!\) monomials have distinct exponent tuples and coefficients \(\pm1\). The monomials \(z_1^{a_1}\cdots z_n^{a_n}\) are orthonormal in normalized torus measure, because \(\int_{S^1}z^k\,dz=0\) unless \(k=0\), when it is one. Hence \(\int_{T^n}|D|^2=n!\). Dividing by \(n!\) gives mass one, including \(n=1\), where the determinant is the constant one.

**Exercise 3 (medium).** Compute
\[
\int_{U(n)}|\operatorname{tr}g|^2\,dg=1,
\qquad
\int_{U(n)}|\operatorname{tr}g|^4\,dg=2\quad(n\geq2).
\]

*Solution.* Write \(p(z)=\sum_jz_j\), and for a strictly decreasing integer tuple \(a\) write \(D_a(z)=\det[z_j^{a_i}]\). Torus orthogonality gives \(\|D_a\|^2=n!\); determinants with different unordered exponent sets are orthogonal. Expanding the determinant shows
\[
pD_a=\sum_{i=1}^n D_{a+e_i}. \tag{5.1}
\]
Here \(e_i\) raises the \(i\)-th row exponent by one, and a term with repeated row exponents is zero. Each monomial multiplied by \(z_j\) raises the exponent belonging to its unique row assigned to column \(j\), which proves (5.1).

For \(\delta=(n-1,n-2,\ldots,0)\), every term except the first has a collision. Thus
\[
pD_\delta=D_{\delta+e_1}.
\]
Weyl integration now gives \(\int|p|^2=\|pD_\delta\|^2/n!=1\).

If \(n\geq2\), raising an exponent in \(\delta+e_1\) is nonzero only for its first two rows. Hence
\[
p^2D_\delta=D_{\delta+2e_1}+D_{\delta+e_1+e_2}. \tag{5.2}
\]
Both exponent tuples are strictly decreasing and have different exponent sets. Their determinants are orthogonal and each has norm squared \(n!\). Therefore
\[
\int_{U(n)}|\operatorname{tr}g|^4\,dg
=\frac{\|p^2D_\delta\|^2}{n!}=2.
\]
For \(n=1\), \(|\operatorname{tr}g|=1\), so the fourth moment is one. The dimension restriction is necessary.

**Exercise 4 (hard).** Prove the regular-set and covering assertions, explaining why disconnected centralizers do not change the degree.

*Solution.* Each root character is a submersion onto the circle. Its kernel is a compact codimension-one submanifold, so the finite union of the kernels is null and nowhere dense. The conjugation map sends \(G/T\times\ker\alpha\), of dimension \(\dim G-1\), into \(G\). The coordinate cube estimate in Lemma 2.1 proves these images null; root invariance under Weyl conjugacy identifies their union exactly with the singular complement.

At every remaining domain point, (1.6) is invertible, so the map is a local diffeomorphism onto the open regular image. For \(s\in T_{\mathrm{reg}}\), its identity-component centralizer is \(T\). Every fiber point has \(gTg^{-1}\subset C_G(s)^0=T\), forcing \(g\) to normalize \(T\). Thus the fiber is exactly (2.4). Even a nontrivial stabilizer of \(s\) in \(W\) produces distinct first coordinates, so the count remains \(|W|\). Preimages of compact subsets of the regular image are compact under the full conjugation map and contain no singular coordinate, proving properness. The inverse-sheet neighborhoods and properness argument in Lemma 2.1 then give an evenly covered neighborhood of each target point. This proves all the assertions without assuming the full element centralizer connected.

## Sources and scope

Bourgade, *On random matrices and L-functions*, Chapter 1, Section 3, gives a probabilistic route to the unitary formula; its introductory statement is on PDF page 13. Lachaud, *On the distribution of the trace in the unitary symplectic group and the distribution of Frobenius*, Theorem 3.1 and Proposition 3.2, supplies the two symplectic forms. The numerical Haar density here is proved by (4.1), and was also proved geometrically in the earlier lesson.

The proof above establishes the general compact connected formula directly from the root decomposition and local change of variables. It does not import a probabilistic conditioning argument. A root-free torus is included, as are groups with a central torus and groups that are not simply connected. No character formula or highest-weight classification is needed.

## Accessible source notes

Pavel Etingof, [*Lie Groups and Lie Algebras*, arXiv:2201.09397v5](https://arxiv.org/abs/2201.09397v5), 23 May 2026 (accessed 3 October 2026), §27. The Weyl character and dimension formulas provide context for the alternating root products. The integration theorem, its degree and its probability normalization are proved above and do not depend on a source character formula.
