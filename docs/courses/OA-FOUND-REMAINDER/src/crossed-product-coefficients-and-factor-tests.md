# Crossed-product coefficients and factor tests

*Self-checked by the writing AI. Original text: CC0 1.0.*

A crossed-product operator determines one coefficient for each group element. The coefficients recover every matrix entry, so they determine the operator uniquely. They also compute products, adjoints, expectations and the centre. Recovering the matrix is a different assertion from convergence of the operator's unordered Fourier partial sums. Those partial sums can have unbounded norms.

We prove the coefficient calculus directly from rows and columns. It gives the maximal-abelian and factor tests for free actions, the canonical group trace, and the infinite-conjugacy-class criterion. We also construct concrete finite and infinite factors from these tests.

The regular construction and its independence of a faithful normal coefficient representation are existing prerequisites: [Changing the Hilbert space of a regular crossed product](../reader/supplements/discrete-regular-model-independence.html#OA-FLOW.REG.CONSTRUCTION), equations R1–R3 and the [normal comparison and relabeling results](../reader/supplements/discrete-regular-model-independence.html#OA-FLOW.REG.INDEPENDENCE), R13–R17. We use their discrete specialization. The algebraic freeness criterion is the multiplier criterion (3a) in [Kernels, local fixed parts, and freeness](../reader/supplements/kernels-and-freeness.html#OA-FLOW.KERNEL.PROJECTION). Its full support-projection proof gives, for an automorphism \(\beta\) of an abelian von Neumann algebra \(A\),
\[
\beta\text{ is free}
\quad\Longleftrightarrow\quad
\bigl[(a-\beta(a))b=0\text{ for every }a\in A\bigr]
\Longrightarrow b=0.
\tag{0.1}
\]
Here free means that no nonzero projection supports a summand on which \(\beta\) acts identically. The linked prerequisites supply their complete arguments. For the tensor extension used in the regular-model comparison, Proposition 8.1(5), Theorem 8.2 and Corollary 8.4 of [Spatial tensor products](../reader/supplements/spatial-tensor-products.html#8-maps-between-tensor-products-and-normal-homomorphisms) also give a complete route: implement a normal homomorphism by amplification and compression, tensor that implementation, and tensor the inverse to obtain the inverse extension. No spatial equivalence of the original coefficient Hilbert spaces is required.

For operator topology and normal functionals we use [Operator spaces, trace class and preduals](../../foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies.html) and [The double commutation theorem](../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html). Type-I factor classification and matrix-unit splitting are Theorem 10.3, Corollary 10.4 and Proposition 8.4 of [Projections and types](../../foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html). The tensor centre formula is Corollary 11.5 of [Spatial tensor products](../reader/supplements/spatial-tensor-products.html). The multiplication-algebra identification is Theorem 3.1 of [Abelian operator algebras](../../foundations-of-von-neumann-algebras/abelian-operator-algebras.html). Elementary Hilbert-space tools include orthogonal sums, Cauchy–Schwarz and uniform boundedness. The circle example uses the usual trigonometric orthonormal basis of \(L^2(\mathbb T)\).

Anantharaman and Popa’s freely readable *An introduction to II₁ factors* treats group traces, the infinite-conjugacy-class criterion and crossed products of probability spaces. The row-and-column arguments here apply to arbitrary abelian coefficient algebras in faithful normal models: Sections 1–3 assume neither an invariant probability measure nor separability of the coefficient Hilbert space. Fourier coefficient reconstruction and convergence of Fourier partial sums remain distinct assertions.

Let \(G\) be a countable discrete group, with identity \(e\). Let \(A\subseteq B(H)\) be a nonzero abelian von Neumann algebra in a faithful normal unital representation, and let
\[
\alpha:G\longrightarrow\operatorname{Aut}(A),\qquad
\alpha_{gh}=\alpha_g\alpha_h
\]
be an action. Both infinite and finite groups are included; finite groups provide useful examples. On
\(\mathcal K=H\otimes\ell^2(G)=\ell^2(G;H)\), use the regular operators
\[
(\pi(a)\xi)(s)=\alpha_{s^{-1}}(a)\xi(s),\qquad
(u_g\xi)(s)=\xi(g^{-1}s).
\tag{0.2}
\]
The cited construction gives normal faithful \(\pi\) and covariance
\[
u_g\pi(a)u_g^*=\pi(\alpha_g(a)).
\tag{0.3}
\]
Write
\[
R=A\rtimes_\alpha G=\{\pi(A),u_g:g\in G\}'',
\qquad
R_0=\left\{\sum_{g\in F}\pi(a_g)u_g:
F\subset G\text{ finite},\ a_g\in A\right\}.
\tag{0.4}
\]
Covariance makes \(R_0\) a unital star algebra; by the regular construction it is ultraweakly dense in \(R\). Changing the faithful normal model of \(A\) gives the named normal isomorphism from the prerequisite comparison theorem.

## 1. Compression and coefficients

Let \(J_s:H\to\mathcal K\) put a vector in coordinate \(s\), and write
\[
x_{s,t}=J_s^*xJ_t,\qquad x\in B(\mathcal K).
\]
For a polynomial in (0.4), direct evaluation gives
\[
x_{s,t}=\alpha_{s^{-1}}(a_{s t^{-1}}),
\tag{1.1}
\]
with the missing coefficients interpreted as zero.

**Proposition 1.1.** Compression at the identity defines a faithful normal unital completely positive map
\[
E:R\longrightarrow A,\qquad E(x)=J_e^*xJ_e.
\tag{1.2}
\]
It satisfies
\[
\begin{aligned}
E(\pi(a))&=a,\\
E(\pi(a)x\pi(b))&=aE(x)b,\\
E(u_gxu_g^*)&=\alpha_g(E(x)).
\end{aligned}
\tag{1.3}
\]
For the coefficients
\[
x_g=E(xu_g^*)\in A
\tag{1.4}
\]
one has, for every \(x\in R\),
\[
x_{s,t}=\alpha_{s^{-1}}(x_{s t^{-1}}).
\tag{1.5}
\]
In particular, all coefficients zero implies \(x=0\).

**Proof.** Compression is normal and completely positive. For \(x\in R_0\), (1.1) gives \(J_e^*xJ_e=a_e\in A\). Approximate an arbitrary \(x\in R\) ultraweakly by elements of \(R_0\); compression is ultraweakly continuous and \(A\) is ultraweakly closed, so the compressed operator still belongs to \(A\). As an \(A\)-valued map it is normal: the given identification of \(A\) with its faithful normal concrete image is a normal isomorphism. It is unital, and therefore has norm one.

The first two identities in (1.3) follow from
\(\pi(a)J_e=J_ea\) and \(J_e^*\pi(a)=aJ_e^*\). The last identity follows for polynomials from covariance: conjugation takes
\(\pi(a_h)u_h\) to \(\pi(\alpha_g(a_h))u_{ghg^{-1}}\). Its identity coefficient is \(\alpha_g(a_e)\). Both sides are normal maps of \(x\), so ultraweak density proves the identity on \(R\).

For a polynomial, (1.4) selects exactly \(a_g\), and (1.5) is (1.1). For fixed \(s,t\), both sides of (1.5) are normal linear functions of \(x\); density proves it in general. If all coefficients vanish, all matrix entries vanish, and hence \(x=0\), since finite-coordinate vectors are dense in \(\mathcal K\).

Finally, suppose \(x\geq0\) and \(E(x)=0\). Formula (1.5) makes every diagonal entry \(x_{s,s}=\alpha_{s^{-1}}(x_e)\) zero. Thus
\[
\|x^{1/2}J_s\eta\|^2
=\langle x_{s,s}\eta,\eta\rangle=0
\quad(s\in G,\ \eta\in H).
\]
Their ranges span a dense subspace, so \(x^{1/2}=0\) and \(x=0\). This proves faithfulness. \(\square\)

It is often convenient to view the expectation as the projection
\(\pi E:R\to\pi(A)\). Equations (1.3) say that this is a normal conditional expectation.

The coefficient rules for multiplication by the coefficient algebra and conjugation by group operators are
\[
\begin{aligned}
(\pi(a)x)_g&=a x_g,&
(x\pi(a))_g&=x_g\alpha_g(a),\\
(u_hxu_h^*)_g
&=\alpha_h(x_{h^{-1}gh}).
\end{aligned}
\tag{1.6}
\]
They hold first on polynomials by covariance, and then on \(R\) because each coordinate map is normal.

The expectation also respects the prerequisite's normal change of regular model. If \(\theta:A\to B\) intertwines two actions and \(C_\theta\) is the named crossed-product isomorphism, then
\[
E_B C_\theta=\theta E_A.
\tag{1.7}
\]
Indeed the maps are normal and agree on every \(\pi(a)u_g\): their values are \(\theta(a)\) for \(g=e\) and zero otherwise. Density proves (1.7). Consequently \(C_\theta\) transports each coefficient by \((C_\theta x)_g=\theta(x_g)\).

## 2. Reconstruction and multiplication

For finite \(F\subseteq G\), put
\[
Q_F=\sum_{s\in F}J_sJ_s^*.
\]
The net of these projections increases strongly to \(1_{\mathcal K}\).

**Theorem 2.1.** The coefficients recover \(x\in R\) by its matrix:
\[
x=\operatorname*{s^*\!-\!lim}_{F\Subset G}
\sum_{s,t\in F}
J_s\alpha_{s^{-1}}(x_{s t^{-1}})J_t^*.
\tag{2.1}
\]
For \(x,y\in R\), products and adjoints have coefficients
\[
\begin{aligned}
(xy)_g&=\operatorname*{s^*\!-\!\sum}_{h\in G}
x_h\alpha_h(y_{h^{-1}g}),\\
(x^*)_g&=\alpha_g(x_{g^{-1}}^*).
\end{aligned}
\tag{2.2}
\]
The first sum means the net of finite subsets of \(G\), and its finite partial sums have norm at most \(\|x\|\|y\|\). Its convergence also holds in the intrinsic sigma-strong-star topology of \(A\).

**Proof.** The finite sum in (2.1) is exactly \(Q_FxQ_F\). For every \(\xi\in\mathcal K\),
\[
\|(Q_FxQ_F-x)\xi\|
\leq \|x\|\|(Q_F-1)\xi\|
+\|(Q_F-1)x\xi\|\longrightarrow0.
\tag{2.3}
\]
Apply the same estimate to \(x^*\). This proves the strong-star limit and the reconstruction assertion. The uniform bound \(\|Q_FxQ_F\|\leq\|x\|\) also gives sigma-strong-star convergence in \(B(\mathcal K)\), by the normal vector-expansion argument below. These coordinate compressions are operators on \(\mathcal K\); they need not belong to \(R\).

The product coefficient is the matrix entry \((xy)_{e,g^{-1}}\). Insert \(Q_F\) between \(x\) and \(y\):
\[
\begin{aligned}
J_e^*xQ_FyJ_{g^{-1}}
&=\sum_{t\in F}x_{e,t}\,y_{t,g^{-1}}\\
&=\sum_{t\in F}x_{t^{-1}}\,
\alpha_{t^{-1}}(y_{tg}).
\end{aligned}
\tag{2.4}
\]
Putting \(h=t^{-1}\) gives the first formula in (2.2). The operators in (2.4) have norm at most \(\|x\|\|y\|\). They converge strongly to \(J_e^*xyJ_{g^{-1}}\), since \(Q_F\to1\) strongly. Their adjoints
\[
J_{g^{-1}}^*y^*Q_Fx^*J_e
\]
also converge strongly. Thus the coefficient sum converges strongly-star.

There is an accompanying absolute estimate for its scalar matrix coefficients. For \(\xi,\eta\in H\), Cauchy–Schwarz for the row of \(x\) and the column of \(y\) gives
\[
\begin{aligned}
\sum_{t\in G}
\left|\langle x_{e,t}y_{t,g^{-1}}\xi,\eta\rangle\right|
&\leq
\left(\sum_t\|y_{t,g^{-1}}\xi\|^2\right)^{1/2}
\left(\sum_t\|x_{e,t}^*\eta\|^2\right)^{1/2}\\
&\leq\|y\|\|\xi\|\,\|x\|\|\eta\|.
\end{aligned}
\tag{2.5}
\]
This explains the summation through actual rows and columns, rather than through a formal convolution.

The adjoint coefficient follows directly from (1.5):
\[
(x^*)_g=x^*_{e,g^{-1}}
=(x_{g^{-1},e})^*
=\alpha_g(x_{g^{-1}}^*).
\]

For intrinsic sigma-strong-star convergence, let \(z_F\) be the difference between a partial coefficient sum and its limit. It is uniformly bounded and tends strongly-star to zero in the faithful normal representation of \(A\). Every positive normal functional on \(A\) has an ambient positive normal extension, hence a square-summable positive vector expansion
\(\varphi(a)=\sum_j\langle a\eta_j,\eta_j\rangle\).
Consequently
\[
\varphi(z_F^*z_F)=\sum_j\|z_F\eta_j\|^2\longrightarrow0.
\]
Finite initial portions tend to zero and the square-summable tail is uniformly bounded by the common norm bound. The same argument applies to \(z_Fz_F^*\). These are exactly the sigma-strong-star seminorms. \(\square\)

The convergence statement in (2.2) concerns sums in the *coefficient algebra* obtained from one matrix product. It does not assert that
\[
\sum_{g\in F}\pi(x_g)u_g
\tag{2.6}
\]
converges strongly-star to \(x\) as \(F\) ranges over all finite subsets.

**Example 2.2 — unordered Fourier partial sums can be unbounded.** Take \(A=\mathbb C\) and \(G=\mathbb Z\). Identify \(\ell^2(\mathbb Z)\) with \(L^2(\mathbb T,d\theta/(2\pi))\) by
\(\delta_n\mapsto e^{in\theta}\). The group shift becomes multiplication by \(e^{i\theta}\), and \(L(\mathbb Z)\) becomes the multiplication algebra \(L^\infty(\mathbb T)\).

Let \(f=1_{(0,\pi)}\). Its coefficients are
\[
\widehat f(0)=\frac12,\qquad
\widehat f(n)=
\begin{cases}
\dfrac{1}{\pi i n},&n\ne0\text{ odd},\\
0,&n\ne0\text{ even}.
\end{cases}
\tag{2.7}
\]
For \(F_N=\{1,3,\ldots,2N+1\}\), the Fourier polynomial has multiplication-operator norm at least its absolute value at \(\theta=0\):
\[
\left\|\sum_{n\in F_N}\widehat f(n)e^{in\theta}\right\|_\infty
\geq\frac1\pi\sum_{k=0}^N\frac1{2k+1}
\longrightarrow\infty.
\tag{2.8}
\]
The polynomial is continuous, so its essential supremum is its supremum; evaluating at that point is valid for the norm estimate.

If the net of all finite partial sums were strongly convergent, it would be pointwise bounded on every Hilbert vector. To include the early parts of the net, fix a finite \(F_0\) beyond which the vector norms are bounded. For any finite \(F\),
\[
S_F\xi=S_{F\cup F_0}\xi-S_{F_0\setminus F}\xi.
\]
The first term lies in the bounded tail, and the second has only finitely many possibilities. Uniform boundedness would then bound all operator norms, contradicting (2.8). Thus unconditional strong, and hence unconditional strong-star, convergence fails. This does not assert failure of symmetric partial sums for this particular function.

The valid reconstruction (2.1) retains both coordinate indices. Regrouping those compressions into (2.6) would lose the uniform compression bound.

## 3. Positive coefficient sums, maximal abelianness and regularity

**Proposition 3.1.** For \(x\in R\),
\[
\begin{aligned}
E(xx^*)&=\operatorname*{s\!-\!\sum}_{g\in G}x_gx_g^*,\\
E(x^*x)&=\operatorname*{s\!-\!\sum}_{g\in G}
\alpha_{g^{-1}}(x_g^*x_g).
\end{aligned}
\tag{3.1}
\]
Both sums are increasing nets of finite positive sums, bounded by \(\|x\|^2 1\); their limits are also sigma-strong limits.

**Proof.** The first is the increasing compression sum
\[
J_e^*xQ_Fx^*J_e
=\sum_{t\in F}x_{e,t}x_{e,t}^*
=\sum_{t\in F}x_{t^{-1}}x_{t^{-1}}^*.
\]
It increases and converges strongly to \(J_e^*xx^*J_e\). The second is
\[
J_e^*x^*Q_FxJ_e
=\sum_{t\in F}x_{t,e}^*x_{t,e}
=\sum_{t\in F}\alpha_{t^{-1}}(x_t^*x_t),
\]
with strong limit \(J_e^*x^*xJ_e\). The norm bound follows from compression. The positive normal vector-expansion argument at the end of Theorem 2.1 proves intrinsic sigma-strong convergence as well. \(\square\)

Call the action free if each \(\alpha_g\), \(g\ne e\), is free in (0.1), and ergodic if \(A^\alpha=\mathbb C1\). The latter agrees with the absence of nontrivial invariant projections: the spectral projections of a fixed self-adjoint element are invariant, and a fixed projection is a fixed element.

**Theorem 3.2.** The coefficient algebra \(\pi(A)\) is maximal abelian in \(R\) if and only if the action is free. In that case
\[
Z(R)=\pi(A^\alpha).
\tag{3.2}
\]
Thus a free action gives a factor exactly when it is ergodic.

**Proof.** If \(x\) commutes with \(\pi(A)\), (1.6) gives
\[
a x_g=x_g\alpha_g(a)\qquad(a\in A,\ g\in G).
\tag{3.3}
\]
For a free action, the multiplier criterion forces \(x_g=0\) for \(g\ne e\). Coefficient uniqueness makes \(x=\pi(x_e)\). This proves maximal abelianness.

If \(\alpha_g\) is not free for some \(g\ne e\), let \(p\ne0\) be a projection supporting its identity part. Then
\((a-\alpha_g(a))p=0\) for every \(a\in A\). Covariance shows that \(\pi(p)u_g\) commutes with \(\pi(A)\). Its \(g\)-coefficient is \(p\), while every element of \(\pi(A)\) has zero \(g\)-coefficient. It is therefore outside \(\pi(A)\), disproving maximal abelianness.

For a free action, every central element lies in the maximal abelian \(\pi(A)\). Such a \(\pi(a)\) commutes with every \(u_g\) exactly when \(\alpha_g(a)=a\) for all \(g\). These are all the generators of \(R\), so (3.2) follows. \(\square\)

A maximal abelian subalgebra \(B\subseteq R\) is called **regular** if its unitary normalizer
\[
\mathcal N_R(B)=\{v\in\mathcal U(R):vBv^*=B\}
\]
generates \(R\) as a von Neumann algebra.

**Corollary 3.3.** For a free action, \(\pi(A)\) is a regular maximal abelian subalgebra of \(R\). Ergodicity is not needed for regularity.

**Proof.** Every \(u_g\) normalizes \(\pi(A)\) by covariance. Every unitary in \(\pi(A)\) normalizes it too. These unitaries generate \(\pi(A)\): for a self-adjoint \(a\), the norm limit
\[
\frac{e^{ita}-1}{it}\longrightarrow a\qquad(t\to0)
\]
places \(a\) in the algebra generated by its unitary exponentials, and every element is a linear combination of self-adjoint elements. Thus the normalizer generates both families in (0.4), and hence \(R\). Maximal abelianness is Theorem 3.2. \(\square\)

## 4. Finite invariant measures and the group trace

**Proposition 4.1.** Let \(\nu\) be an invariant normal state on \(A\). Then
\[
\widetilde\nu=\nu E
\tag{4.1}
\]
is a normal tracial state on \(R\). It is faithful if \(\nu\) is faithful. Conversely, \(\nu E\) can be tracial only if \(\nu\) is invariant.

**Proof.** Normality and positivity follow from composition; the value at \(1\) is one. Normality allows \(\nu\) to be applied to the increasing positive sums in (3.1). Invariance and abelianness of \(A\) give
\[
\begin{aligned}
\widetilde\nu(x^*x)
&=\sum_g\nu(\alpha_{g^{-1}}(x_g^*x_g))
=\sum_g\nu(x_g^*x_g)\\
&=\sum_g\nu(x_gx_g^*)
=\widetilde\nu(xx^*).
\end{aligned}
\tag{4.2}
\]
Polarization of this equality gives the trace identity
\(\widetilde\nu(ab)=\widetilde\nu(ba)\). Faithfulness follows from the faithfulness of \(E\) and \(\nu\).

For necessity, a tracial state is invariant under unitary conjugation. Applying it to \(u_g\pi(a)u_g^*=\pi(\alpha_g(a))\) yields
\(\nu(\alpha_g(a))=\nu(a)\). \(\square\)

Specialize to \(A=\mathbb C\), with the trivial action. Write
\[
L(G)=\{u_g:g\in G\}'',\qquad
\tau(x)=\langle x\delta_e,\delta_e\rangle.
\tag{4.3}
\]
The identity-state extension in Proposition 4.1 proves that \(\tau\) is a faithful normal tracial state. Thus \(L(G)\) is finite. Its coefficients are scalars and
\[
\tau(x^*x)=\sum_{g\in G}|x_g|^2.
\tag{4.4}
\]

**Theorem 4.2.** \(L(G)\) is a factor if and only if every conjugacy class of a nonidentity element of \(G\) is infinite. When \(G\) is infinite and satisfies this condition, \(L(G)\) is a type-II\(_1\) factor.

**Proof.** Formula (1.6), with scalar coefficients, shows that a central \(x\) has coefficients constant on each conjugacy class. Equation (4.4) makes the coefficient family square summable. A nonzero constant cannot occupy an infinite class, so if all nonidentity classes are infinite, \(x_g=0\) for \(g\ne e\). Uniqueness gives \(x=x_e1\).

Conversely, if a nonidentity element has a finite conjugacy class \(C\), the finite sum
\[
z_C=\sum_{h\in C}u_h
\tag{4.5}
\]
is central, since conjugation by any \(u_g\) permutes its terms. It is nonscalar: its image of \(\delta_e\) is \(\sum_{h\in C}\delta_h\), orthogonal to \(\delta_e\) and nonzero. So \(L(G)\) is not a factor.

For infinite \(G\), the operators \(u_g\) are linearly independent by their values on \(\delta_e\); \(L(G)\) is therefore infinite dimensional. It is finite by (4.3). The existing classification says that a finite type-I factor is a matrix algebra, so this infinite-dimensional finite factor must be type II\(_1\). \(\square\)

An infinite group with the stated conjugacy property is called **ICC**, for infinite conjugacy classes.

## 5. ICC examples and infinite semifinite factors

**Proposition 5.1.** The following are countable ICC groups: the group of finitely supported permutations of a countably infinite set; a free group with finitely or countably many generators, at least two; a nonempty finite product of countable ICC groups; and a restricted direct product over a nonempty countable family of countable ICC groups.

**Proof.** A nonidentity finitely supported permutation has nonempty finite support \(S\). Choose infinitely many pairwise disjoint sets of the same cardinality as \(S\), and extend bijections from \(S\) to those sets to finitely supported permutations. Conjugation transports the support to each chosen set, giving infinitely many distinct conjugates. The group is countable, since it is a countable union of finite permutation groups on finite subsets.

For a free group, fix a free generator \(a\). If a reduced word \(w\) is outside \(\langle a\rangle\), write it uniquely as
\[
w=a^r v a^s,
\]
where \(v\) is nonempty and neither its first nor its last letter is \(a\) or \(a^{-1}\). This just strips the maximal initial and final strings of those letters. For \(n\ne0\),
\[
a^nwa^{-n}=a^{r+n}v a^{s-n}\ne a^r v a^s,
\tag{5.1}
\]
since these stripped leading exponents differ and there is no cancellation with \(v\). Thus the centralizer of a nontrivial power of \(a\) is \(\langle a\rangle\). A nonidentity \(w\) is outside the cyclic group of some generator: use \(a\) if possible, and a different generator if \(w\in\langle a\rangle\). Its conjugates by all powers of the chosen generator are distinct by (5.1). There are only countably many finite reduced words in a finite or countable alphabet.

In either product construction, a nonidentity tuple has a nonidentity coordinate. Vary conjugation in that coordinate alone, leaving the others unchanged; the chosen coordinate gives infinitely many distinct conjugates. Finite products of countable groups are countable. A restricted product over a countable index set is countable too, as the union of the countably many finite-coordinate products. \(\square\)

In particular \(L(\mathbb F_2)\), on \(\ell^2(\mathbb F_2)\), is an explicitly constructed separably represented type-II\(_1\) factor.

**Corollary 5.2.** The spatial tensor product
\[
N=L(\mathbb F_2)\bar\otimes B(\ell^2(\mathbb N))
\tag{5.2}
\]
is a separably represented type-II\(_\infty\) factor.

**Proof.** The tensor centre theorem gives \(Z(N)=\mathbb C1\). The projection \(p=1\otimes E_{11}\) has corner normally isomorphic to \(L(\mathbb F_2)\), so it is nonzero and finite. In the factor \(N\) it has central carrier one, giving semifiniteness by the good-projection characterization. The identity of \(N\) is properly infinite, since the even- and odd-range isometries in the second tensor factor give two orthogonal copies of it.

It cannot be type I: a corner of a type-I algebra is type I, whereas \(pNp\) is type II\(_1\). A nonfinite semifinite factor outside type I is type II\(_\infty\). The tensor Hilbert space is separable. \(\square\)

## 6. Graded exercises with solutions

**Exercise 6.1 — introductory: a two-point crossed product.** Let \(A=\mathbb C^2\), let \(G=\{e,s\}\) with \(s^2=e\), and let \(\alpha_s\) interchange the two coordinates. Prove that the action is free and ergodic. Construct matrix units in \(R\), identify \(R\), and compute \(E\) and the trace extending the uniform state on \(A\).

**Solution.** The only nonzero invariant projection other than individual atoms is \(1\), and \(\alpha_s\) is not the identity on its summand. It has no nonzero identity part, so the action is free. Its fixed elements are \((c,c)\), so it is ergodic.

Let \(p_1=(1,0)\), \(p_2=(0,1)\), and put
\[
e_{11}=\pi(p_1),\quad e_{22}=\pi(p_2),\quad
e_{12}=\pi(p_1)u_s,\quad e_{21}=\pi(p_2)u_s.
\]
Covariance and \(u_s^2=1\) give
\[
e_{12}^*=e_{21},\qquad e_{12}e_{21}=e_{11},\qquad
e_{21}e_{12}=e_{22}.
\]
The remaining matrix-unit equations follow from \(p_1p_2=0\). The sum of the diagonal units is \(1\), and every polynomial in (0.4) lies in their four-dimensional span. That span is a von Neumann algebra, so \(R\cong M_2(\mathbb C)\); the four-dimensional regular Hilbert-space representation has multiplicity two.

For a matrix \(b=(b_{ij})\), its coefficients are
\[
b_e=(b_{11},b_{22}),\qquad b_s=(b_{12},b_{21}),
\]
and \(E(b)=b_e\). The uniform state \(\nu(a_1,a_2)=(a_1+a_2)/2\) is invariant; its extension is the normalized matrix trace
\((b_{11}+b_{22})/2\). The diagonal algebra is a regular maximal abelian subalgebra, as can also be seen from the diagonal unitaries and the swapping unitary.

**Exercise 6.2 — intermediate: an infinite group with finite conjugacy classes.** Let
\[
D_\infty=\langle r,s:r\text{ has infinite order},\ s^2=e,\ srs=r^{-1}\rangle.
\]
Show that a nontrivial rotation \(r^n\) has conjugacy class \(\{r^n,r^{-n}\}\), while each reflection has an infinite class. Exhibit a nonscalar central element of \(L(D_\infty)\) and compute its canonical trace and squared \(L^2\) norm.

**Solution.** Every word has the form \(r^k\) or \(r^ks\). The action on the integers by \(r(m)=m+1\) and \(s(m)=-m\) shows that these forms are distinct and that \(r\) has infinite order. Rotations commute with each other, while conjugation by a reflection inverts them. Hence the conjugacy class of \(r^n\), \(n\ne0\), is exactly the displayed two-element set.

For a reflection,
\[
r^k(r^ns)r^{-k}=r^{n+2k}s,
\]
giving infinitely many distinct conjugates. Thus the failure of ICC occurs in the rotation classes.

The self-adjoint operator
\[
z=u_r+u_{r^{-1}}
\]
is central by the finite-class construction. Its two nonidentity coefficients are both one; it is nonscalar and \(\tau(z)=0\). Expanding
\[
z^*z=z^2=u_{r^2}+2\,1+u_{r^{-2}}
\]
gives \(\tau(z^*z)=2\), also equal to the sum of squared coefficients. The algebra is finite by its canonical trace, but it is not a factor.

**Exercise 6.3 — advanced: an atomic infinite factor and a missing probability measure.** Let \(A=\ell^\infty(\mathbb Z)\), let \(G=\mathbb Z\), and let \(\alpha_k(f)(m)=f(m-k)\). Prove that the crossed product is normally isomorphic to \(B(\ell^2(\mathbb Z))\). Explain why no invariant normal state on \(A\) exists, and exhibit a nonzero finite projection in the crossed product despite the absence of a finite faithful normal trace on the whole algebra.

**Solution.** Let \(p_i=1_{\{i\}}\). A nonidentity translation fixes no atom and has no nonzero identity part. The only invariant subsets of the transitive set \(\mathbb Z\) are empty and full, so the action is free and ergodic. Theorem 3.2 makes \(R\) a factor.

Set
\[
e_{ij}=\pi(p_i)u_{i-j}\qquad(i,j\in\mathbb Z).
\tag{6.1}
\]
Since \(\alpha_{i-j}(p_k)=p_{k+i-j}\), covariance gives
\[
e_{ij}e_{kl}=\delta_{jk}e_{il},\qquad
e_{ij}^*=e_{ji},\qquad
\sum_i e_{ii}=1
\]
with a strong diagonal sum. The corner \(\pi(p_0)R\pi(p_0)\) is scalar: compression of the dense polynomial algebra has only its identity-group term, because
\[
\pi(p_0)\pi(a)u_k\pi(p_0)
=\pi(p_0a\,\alpha_k(p_0))u_k
\]
vanishes for \(k\ne0\), and equals \(a(0)\pi(p_0)\) for \(k=0\). Normal compression and ultraweak density retain exactly the scalar corner.

The proved matrix-unit splitting theorem therefore identifies \(R\) normally with \(B(\ell^2(\mathbb Z))\), possibly with an identity multiplicity in its particular regular representation. Explicitly its matrix units are (6.1). They also generate all the original generators: the diagonal sums give \(\pi(f)\), and
\[
u_k=\operatorname*{s\!-\!\sum}_{i\in\mathbb Z}e_{i+k,i}.
\]
For a vector this is the sum of its orthogonal coordinate images, so the last strong sum is valid.

If \(\nu\) were an invariant normal state on \(A\), all \(\nu(p_i)\) would have one common nonnegative value \(c\). Normality and \(\sum_i p_i=1\) would give \(1=\sum_i c\), impossible whether \(c=0\) or \(c>0\). Thus the invariant-state construction in Proposition 4.1 supplies no finite trace here.

There cannot be any finite faithful normal trace on \(R\): under the matrix-unit identification all \(e_{ii}\) are equivalent, so their trace values would be a common positive number, and normality would force an infinite trace of \(1\). Nevertheless \(e_{00}\) is a nonzero finite projection, since its corner is \(\mathbb Ce_{00}\). Its central carrier is one in this factor, giving semifiniteness. This is an explicit separably represented type-I\(_\infty\) example.

## References

- [Anantharaman–Popa] Claire Anantharaman and Sorin Popa, *An introduction to II₁ factors*, [author-hosted draft IIunV15](https://www.math.ucla.edu/~popa/Books/IIunV15.pdf).
- [Takesaki] M. Takesaki, *Theory of Operator Algebras I*, Springer, New York, 1979.
- The programme lessons *Kernels, local fixed parts, and freeness* and *Changing the Hilbert space of a regular crossed product*, with the exact prerequisite locators specified above.
