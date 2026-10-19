# Finite models of a von Neumann algebra

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text: public domain (CC0).*

Norm approximation of a C*-algebra controls its minimal and maximal tensor norms. A von Neumann algebra has a weaker, representation-sensitive approximation topology: bounded operators can converge through their values on vectors and normal functionals. Finite completely positive models in that topology lead to semidiscreteness and to injectivity.

We will prove the equivalence between those finite models, a norm bound for multiplication by the commutant, and norm approximation in the predual. We will also prove that these conditions give completely positive extension into the von Neumann algebra. The converse implication from injectivity is proved for finite and semifinite algebras in [Hypertraces and finite injective algebras](hypertraces-finite-injectivity.md), then for every von Neumann algebra in Averaging, crossed products, and injectivity.

Prerequisites are [Completely positive finite models](completely-positive-finite-models.md), [Tensor positivity and nuclearity](tensor-positivity-nuclearity.md), and [The positive cone of a standard representation](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-APPROX/prerequisites.html#standard-form-natural-cone). In particular, we use the exact-marginal correction and the GNS dominated-functional theorem. We also use the predual of a von Neumann algebra, normal maps, the Schwarz inequality for completely positive contractions, and ultraweak compactness. For the norm-one projection criterion, the concrete positivity, block preservation and bimodularity proofs are given in Q1–Q3 below. They use contractivity, vector tests, continuous calculus and strong closedness of the range. [Tomiyama's Theorem 1](https://www.jstage.jst.go.jp/article/pjab1945/33/10/33_10_608/_pdf/-char/en), printed pp.608–609, is the human source for the block-norm method. Corollary 4.3 then proves complete positivity by a matrix argument. The scalar and Hilbert inputs are the complete CF1–10 proofs; the vector-series predual is CP01–06. Matrix calculus uses [Scalar GNS and matrix norms](../scalar-gns-and-matrix-cstar-norms.html), and faithful spatial tensor norms use [the minimal tensor construction](../abstract-tensor-and-universal-bidual-foundations.html#mtn-theorem). The underlying approximation results are due to Effros and Lance; the extension and compactness methods used in Section 4 are proved in the freely readable Arveson article cited below.

We use one precise normal-representation comparison: if \(\pi_1\) and \(\pi_2\) are faithful normal representations of \(M\), then \(\pi_2\) is unitarily equivalent to the restriction of \(\pi_1\otimes1_K\) to \(p(H_1\otimes K)\), for some Hilbert space \(K\) and projection \(p\in(\pi_1(M)\otimes1_K)'\). The commutant on the restricted space is \(p(\pi_1(M)'\bar\otimes B(K))p\). The complete balanced-vector-series, dominated-form and cyclic-decomposition proof is given in Normal representations inside standard amplifications; it uses no injectivity or semidiscreteness theorem and imposes no separability assumption.

No factor, separability, or faithful normal state hypothesis is imposed. We assume the algebra is nonzero; the zero algebra satisfies the approximation statements trivially. Inner products are linear in the second variable.

## 1. Which topology should the models approximate?

A von Neumann algebra \(M\) is **semidiscrete** if there is a net of cpc maps
\[
M\xrightarrow{S_i}M_{n_i}\xrightarrow{T_i}M
\]
with \(S_i\) normal and \(T_iS_i(x)\to x\) ultraweakly for every \(x\in M\). Since the middle algebra is finite-dimensional, \(T_i\) is automatically normal.

The use of normal recording maps matters when we pass to preduals. An arbitrary completely positive map \(M\to M_n\) can have singular coordinate functionals, which cannot define a map from \(M_n^*\) into \(M_*\).

**Lemma 1.1.** Suppose cpc maps \(\Phi_i:M\to M\) converge pointwise ultraweakly to the identity. Then they converge pointwise in the \(\sigma\)-strong* topology.

**Proof.** A cpc map is adjoint preserving, because every self-adjoint element is a difference of positive elements. Apply its two-by-two amplification to the positive Gram matrix
\[
\begin{pmatrix}x^*x&x^*\\x&1\end{pmatrix}.
\]
Since \(0\le\Phi(1)\le1\), adding the positive bottom-right entry \(1-\Phi(1)\) gives
\[
\begin{pmatrix}\Phi(x^*x)&\Phi(x)^*\\\Phi(x)&1\end{pmatrix}\ge0.
\]
Its quadratic form at \((\eta,-\Phi(x)\eta)\) is
\(\langle\eta,(\Phi(x^*x)-\Phi(x)^*\Phi(x))\eta\rangle\).
Vector positivity therefore proves Schwarz, including a subunital map. Thus, for every normal positive functional \(f\), the Schwarz inequality gives
\[
\begin{aligned}
f((\Phi_i(x)-x)^*(\Phi_i(x)-x))
&\le f(\Phi_i(x^*x))
-2\operatorname{Re}f(x^*\Phi_i(x))+f(x^*x)\\
&\longrightarrow0.
\end{aligned}
\]
The functionals \(a\mapsto f(x^*a)\) are normal, so ultraweak convergence applies to the middle term. Apply the same argument to \(x^*\); positive maps preserve adjoints. The seminorms
\(a\mapsto\{f(a^*a)+f(aa^*)\}^{1/2}\), for normal positive \(f\), define the \(\sigma\)-strong* topology. \(\square\)

The special role of the identity limit is visible in this proof: the positive term \(\Phi_i(x^*x)\) converges to exactly the product needed for the limiting vector estimate. An arbitrary ultraweak limit of cpc maps need not give strong convergence.

## 2. Multiplication by the commutant

Represent \(M\) in standard form on \(H\), and put \(N=M'\). The commuting actions give an algebraic *-homomorphism
\[
\mu:M\odot N\to B(H),\qquad
\mu\left(\sum_jx_j\otimes y_j\right)=\sum_jx_jy_j.
\]
It always extends to the maximal tensor product. The relevant extra assertion is
\[
\left\|\sum_jx_jy_j\right\|
\le\left\|\sum_jx_j\otimes y_j\right\|_{\min}.                \tag{1}
\]

**Theorem 2.1.** A von Neumann algebra is semidiscrete if and only if (1) holds in one faithful normal representation. In that case (1) holds in every faithful normal concrete representation. The finite models may be chosen with unital recording maps.

**Proof.** Suppose first that \(\Phi_i=T_iS_i\) is a semidiscrete approximation. In any faithful normal representation \(M\subset B(K)\), let \(y_j\in M'\). For each \(i\), the map
\[
M_{n_i}\odot M'\to B(K),\qquad z\otimes y\mapsto T_i(z)y
\]
is a completely positive contraction on the maximal tensor product. This follows from the commuting Stinespring construction in **Completely positive finite models**: the commutant action lifts to the dilation of \(T_i\), and compression gives the displayed product map. Matrix algebras have a unique C*-tensor norm, so the map is contractive for the minimal norm as well. Compose it with the minimal tensor map \(S_i\otimes\operatorname{id}_{M'}\). We obtain
\[
\left\|\sum_j\Phi_i(x_j)y_j\right\|
\le\left\|\sum_jx_j\otimes y_j\right\|_{\min}.
\]
The left-hand operators converge ultraweakly to \(\sum_jx_jy_j\). An operator-norm ball is ultraweakly closed, proving (1).

Conversely suppose (1) holds in a faithful normal representation. Lemma 2.2 below transfers the inequality to a standard representation; use that representation for the rest of the proof. Fix finitely many normal positive functionals \(f_1,\ldots,f_r\) on \(M\), and put \(w=\sum_jf_j\). Let \(\xi_w\) be its standard-cone vector. The functional
\[
\Omega(x\otimes y)=\langle\xi_w,xy\xi_w\rangle
\]
is positive on the maximal tensor product. By (1) it is bounded on the minimal tensor product. Its associated map is
\[
\theta:M\to N_*,\qquad
\theta(x)(y)=\langle\xi_w,xy\xi_w\rangle.
\]

Approximate \(\Omega\) weak* by convex combinations of vector functionals whose vectors are finite sums of elementary tensors in the faithful spatial representation on \(H\otimes H\). The factorization of such a vector functional from **Tensor positivity and nuclearity** has recording map
\[
S(x)_{kl}=\langle u_k,xu_l\rangle.
\]
It is normal on \(M\), because every coordinate is a normal vector functional. Its reconstruction map has values in \(N_*\). The associated maps converge pointwise weakly in \(N_*\). Convexity and Hahn–Banach on each finite product of preduals give pointwise norm approximation there.

Apply exact-marginal correction to these factorizations, with marginal
\(\psi=\theta(1)=\omega_{\xi_w}|_N\). Its recording maps remain normal. To check this last point, finite block sums and multiplication by fixed scalar matrices preserve normality, and the added scalar block can use a normal state of \(M\). Such a state exists on every nonzero von Neumann algebra: normalize any nonzero normal positive functional. The normalization at the finite-dimensional support also preserves normality. We obtain a normal ucp \(S:M\to M_n\) and a completely positive \(T:M_n\to N_*\), with \(T(1)=\psi\), whose composite meets any specified finite set of norm tests against \(\theta\).

Let \(e\in M\) be the projection onto \(\overline{N\xi_w}\). The dominated-functional inverse converts \(T\) into a ucp map
\(T':M_n\to eMe\), whose unit is \(e\). As a map into \(M\), it is cpc. Each \(f_j\le w\) has a GNS Radon–Nikodym contraction \(b_j\in N\) with
\(f_j(x)=\langle b_j\xi_w,xb_j\xi_w\rangle\).
Consequently,
\[
|f_j(x-T'S(x))|
=|(\theta(x)-TS(x))(b_j^*b_j)|
\le\|\theta(x)-TS(x)\|.
\]
If all the selected functionals are zero, use the normal-state recording map and zero reconstruction map instead. Every normal functional is a linear combination of four positive normal functionals. Thus, by directing finite sets of operators, finite sets of normal functional tests and positive tolerances, these cpc factorizations approximate the identity pointwise ultraweakly. Their recording maps are normal and unital. This proves semidiscreteness. The first half of the proof gives (1) in every faithful normal representation. \(\square\)

The construction of the arbitrary-algebra standard cone is [NC00–NC08](../components/natural-cone-construction.md#nc00), with its complex-power multiplication and original graph domains proved in NC00c. The support-corner and vector-distance arguments are [CG01–CG10](../components/standard-cone-geometry.md#cg01); cyclic positive-functional realization is [CR00–CR07](../components/cyclic-cone-realization.md#cr00). Their dependency order is NC, then CG01–CG09a, then CR, then CG10. The norm-additive normal decomposition is the independent [NJ01–NJ06 proof](../components/normal-jordan-from-scalar-norm-attainment.md#nj01). The finite-vector factorization and exact-marginal correction are the full proofs in tensor positivity, Lemmas 1.1–1.3, Proposition 1.6 and Lemma 2.1. Thus every support corner in this converse comes from the selected functional, without a faithful-state assumption on the original algebra.

This proof uses one normal positive functional at a time to organize finitely many tests. It does not replace an arbitrary von Neumann algebra by a countably decomposable one.

**Lemma 2.2 (Transfer between normal representations).** Inequality (1) passes to Hilbert-space amplifications and to faithful commutant restrictions. Consequently it passes between any two faithful normal representations.

**Proof.** Suppose \(M\subset B(H)\) satisfies (1), so its multiplication map extends to a *-homomorphism on \(M\otimes_{\min}M'\). Amplify the representation to \(H\otimes K\). The commutant is \(M'\bar\otimes B(K)\).

For a finite-dimensional subspace \(F\subset K\), compression
\[
M'\bar\otimes B(K)\to M'\otimes B(F),\qquad
y\mapsto(1\otimes p_F)y(1\otimes p_F)
\]
is cpc. If \(z=\sum_jx_j\otimes y_j\), this compression followed by multiplication is precisely the restriction to \(H\otimes F\) of the compressed operator \(\sum_j(x_j\otimes1)y_j\). On that finite corner, multiplication is the matrix amplification of the original minimal-tensor *-homomorphism, after permuting the tensor factors. It is contractive. CP tensor functoriality for the compression therefore gives
\[
\left\|(1\otimes p_F)\sum_j(x_j\otimes1)y_j(1\otimes p_F)\right\|
\le\|z\|_{\min}.
\]
As \(F\) increases, these compressions converge strongly to the original operator. Their uniform norm bound proves (1) for the amplification, with no restriction on the dimension of \(K\).

Next take \(p\in M'\bar\otimes B(K)\) such that the restriction of \(M\otimes1\) to \(p(H\otimes K)\) is faithful. The commutant of that restriction is \(p(M'\bar\otimes B(K))p\). Inclusion of this corner into the larger commutant preserves the minimal tensor norm. The product operator on the restricted space is the compression by \(p\) of the corresponding product in the amplification. Hence (1) passes to the restriction. Apply the complete normal-representation construction linked in the prerequisites to obtain the final assertion. \(\square\)

## 3. The predual formulation uses dual matrix norms

The Banach predual \(M_*\) inherits the dual matrix order from \(M^*\). The middle space in a contractive predual factorization is \(M_n^*\), with trace norm, rather than \(M_n\) with operator norm.


<a id="dual-matrix-order"></a>

### D1. Why the adjoints retain complete positivity

For \(f_{ij}\in M_*\), the dual matrix order declares \([f_{ij}]\) positive when
\(x\mapsto[f_{ij}(x)]\) is completely positive. The following equivalent functional test fixes the indices:
\[
F([x_{ij}])=\sum_{i,j}f_{ij}(x_{ij})
\quad\hbox{is positive on }M_r(M).                         \tag{D1}
\]
Indeed, if the coefficient map is completely positive, apply its \(r\)-th amplification to a positive \([x_{ij}]\), then evaluate at \(\sum_i e_i\otimes e_i\). The resulting scalar is exactly (D1).

Conversely, assume \(F\) is positive. Let \(X=[x_{kl}]\ge0\) in \(M_s(M)\), and choose arbitrary vectors \(\zeta_k\in\mathbb C^r\). The scalar matrix \(C\), with \(C_{ki}=\zeta_k(i)\), gives the positive matrix \(C^*XC\in M_r(M)\). Thus
\[
0\le F(C^*XC)
=\sum_{k,l,i,j}\overline{\zeta_k(i)}f_{ij}(x_{kl})\zeta_l(j).
\]
These are all vector tests on the coefficient-map amplification of \(X\). Hence that amplification is positive for every \(s\), proving the equivalence.

Let \(\Phi:M\to N\) be normal and completely positive. Its preadjoint sends \(f\) to \(f\circ\Phi\). If \([f_{ij}]\) is positive in the dual order of \(N_*\), compose its completely positive coefficient map with \(\Phi\). This proves complete positivity of \(\Phi_*\).

In the other direction, let \(\delta:M_*\to N_*\) be completely positive in the dual orders, and set \(\Phi=\delta^*:N\to M\). A normal positive functional \(F\) on \(M_s(M)\) has coefficient functionals \(f_{ij}\in M_*\), defined by restricting \(F\) to the matrix with its sole entry \(a\) in position \((i,j)\). It has the form (D1). The equivalence just proved makes \([f_{ij}]\) positive. Therefore \([\delta(f_{ij})]\) is positive, and for \(X=[x_{ij}]\ge0\) in \(M_s(N)\),
\[
F(\Phi^{(s)}(X))
=\sum_{i,j}\delta(f_{ij})(x_{ij})\ge0.
\]
In particular this holds for every normal vector functional on the concrete matrix algebra \(M_s(M)\). Those vector tests detect positivity, so \(\Phi\) is completely positive. Its scalar normal tests satisfy \(f\circ\Phi=\delta(f)\in N_*\), which also proves normality. This argument uses the actual preduals; no identification of an arbitrary functional with a normal one occurs.

The adjoint and preadjoint norms agree by the norming Hahn–Banach identity: for a bounded map \(L:E\to F\),
\[
\|L\|=\sup_{\|e\|\le1,\,\|g\|\le1}|g(Le)|=\|L^*\|.
\]
Thus both directions preserve contractivity.

**The singular-state example used in Exercise 3.** On \(H=\ell^2(\mathbb N)\), let \(\mathcal K\) be the norm closure of finite-rank operators and let \(e_n\) be the standard unit vectors. Every \(k\in\mathcal K\) satisfies \(\|ke_n\|\to0\): it holds for finite rank by the square-summable scalar coordinates, and a uniform operator-norm approximation proves it for \(k\). In particular \(1\notin\mathcal K\). On the operator system \(\mathcal K+\mathbb C1\), define \(f(k+\lambda1)=\lambda\). This is well defined. If \(k+\lambda1\ge0\), its vector values at \(e_n\) tend to \(\lambda\), so \(\lambda\ge0\). Thus \(f\) is positive and \(f(1)=1\). The positive-functional extension proved in **Completely positive finite models, Lemma 2.2** extends it to a state \(s\) on \(B(H)\). For the increasing finite-coordinate projections \(p_n\), we have \(s(p_n)=0\), although \(s(1)=1\). A normal vector-series functional has \(s(p_n)\to s(1)\), by its finite-coordinate convergence and uniformly small square-summable tails. Hence this state is singular, providing the required concrete counterexample.

### D2. The norm of the finite middle space

Every functional on \(M_n\) has a unique density matrix \(D\), with \(f(x)=\operatorname{Tr}(Dx)\) and \(D_{ji}=f(e_{ij})\). Diagonalize the positive matrix \(D^*D\) by the complete finite unit-sphere and induction proof in [P03 of Tracial adjoints and rational matrix models](tracial-adjoints-and-rational-matrix-models.md#p03). If its eigenvalues are \(\lambda_k\), set \(v e_k=D e_k/\sqrt{\lambda_k}\) for \(\lambda_k>0\), and \(v e_k=0\) otherwise. The nonzero images are orthonormal, so \(\|v\|\le1\), \(D=v|D|\), and \(v^*v\) is the support of \(|D|\).
For finite matrices, \(\operatorname{Tr}(AB)=\sum_{i,j}A_{ij}B_{ji}=\operatorname{Tr}(BA)\); in particular trace is unchanged by unitary changes of basis. For \(\|x\|\le1\), this cyclic identity and the finite trace sum give
\[
|\operatorname{Tr}(Dx)|
=\left|\sum_k\sqrt{\lambda_k}\langle e_k,xv e_k\rangle\right|
\le\sum_k\sqrt{\lambda_k}=\operatorname{Tr}|D|.
\]
Equality holds at \(x=v^*\); when \(D=0\), both sides are zero. Consequently \(\|f\|=\operatorname{Tr}|D|\). This is the trace norm on \(M_n^*\), which is the norm used below.

**Theorem 3.1.** The following are equivalent:

1. \(M\) is semidiscrete.
2. The identity of \(M_*\) is approximated pointwise in norm by cpc factorizations
   \[
   M_*\xrightarrow{\gamma_i}M_{n_i}^*
        \xrightarrow{\delta_i}M_*.
   \]

Complete positivity in 2 uses the dual matrix orders, and contractivity uses the Banach norms.

**Proof.** Adjoint a normal cpc factorization \(\Phi_i=T_iS_i\) on \(M\). Its preadjoint is
\[
(\Phi_i)_*=(S_i)_*(T_i)_*,
\quad M_*\xrightarrow{(T_i)_*}M_{n_i}^*
       \xrightarrow{(S_i)_*}M_*.
\]
D1 proves that preadjoints preserve norms and complete positivity in the dual orders. Ultraweak convergence of \(\Phi_i(x)\) to \(x\) says that \((\Phi_i)_*(f)\to f\) weakly in \(M_*\), for every \(f\in M_*\).

The set of such composites is convex. For nonnegative \(t_j\) summing to one, record with \(S(x)=\bigoplus_jS_j(x)\), and reconstruct with
\[
T(z)=\sum_j t_j T_j(p_j z p_j).
\]
Here \(p_j\) are the scalar matrix block projections. Compression and the individual maps are completely positive; the block-diagonal norm is a maximum and \(\|T(z)\|\le\sum_jt_j\|z\|=\|z\|\). Thus these maps are cpc, and \(S\) is normal coordinatewise. Their preadjoint composite is the desired convex combination.

Fix \(f_1,\ldots,f_r\in M_*\). The tuple \((f_1,\ldots,f_r)\) is in the weak closure of the convex set of approximate tuples. If it were outside the norm closure, real Hahn–Banach separation would give a continuous real functional strictly separating it from that convex closure. Every such functional on the finite product is \(\operatorname{Re}\sum_j g_j(x_j)\), for fixed \(x_j\in M=(M_*)^*\). This contradicts weak closure. The complete separation argument is [SEP in Hypertraces](hypertraces-finite-injectivity.md#separation). Hence one factorization meets any given finite list of norm tolerances; directing those lists and tolerances proves 2.

Conversely, adjoint a factorization in 2. The adjoint of \(\delta_i\) is a normal cpc recording map \(M\to M_{n_i}\), and the adjoint of \(\gamma_i\) is a cpc reconstruction map \(M_{n_i}\to M\). Normality of the first map follows precisely because \(\delta_i\) has range in the predual. For \(x\in M\), \(f\in M_*\),
\[
|f(\gamma_i^*\delta_i^*(x)-x)|
\le\|\delta_i\gamma_i(f)-f\|\,\|x\|\longrightarrow0.
\]
Thus these maps prove semidiscreteness. \(\square\)

Under separability of \(M_*\), norm approximation in 2 can be arranged as a sequence by the usual dense-list argument with a uniform contractive bound. Without separability, the finite-set formulation gives a net. Lemma 1.1 also shows that the primal approximations converge in the \(\sigma\)-strong* topology.

## 4. The finite models give an extension property

Call a von Neumann algebra \(M\) **injective** if every completely positive map from an operator system \(S\subset C\), where \(C\) is a unital C*-algebra, to \(M\) extends completely positively to \(C\). The extension retains the value at the unit, hence retains the norm; unital maps have unital extensions. No normality of the extension is requested.

**Proposition 4.1.** In a faithful normal representation \(M\subset B(H)\), injectivity is equivalent to the existence of a ucp retraction \(E:B(H)\to M\). This criterion is independent of the faithful normal representation.

**Proof.** Extend the identity map on the operator system \(M\) to \(B(H)\) by injectivity. The extension takes the unit to the unit, has range in \(M\), and fixes \(M\), giving the retraction.

Conversely, given \(E\), first extend a completely positive \(\phi:S\to M\subset B(H)\) by Arveson's theorem to a map \(\Phi:C\to B(H)\). Then \(E\Phi\) has range in \(M\) and agrees with \(\phi\) on \(S\). Its unit value is unchanged because \(E\) fixes \(M\). Hence it has the same norm and is unital when \(\phi\) is unital. This is an abstract property of \(M\), proving the representation assertion. \(\square\)

**Theorem 4.2.** Every semidiscrete von Neumann algebra is injective.

**Proof.** Represent \(M\subset B(H)\) faithfully and normally, and take its normal cpc finite models \(T_iS_i\). Arveson's theorem extends each \(S_i\) to a cpc map \(\widehat S_i:B(H)\to M_{n_i}\); its value at the unit is preserved. The composite
\(E_i=T_i\widehat S_i:B(H)\to M\) is cpc.

For each \(a\in B(H)\), the values \(E_i(a)\) lie in the ultraweakly compact ball of radius \(\|a\|\) in \(M\). A subnet converges ultraweakly at every \(a\), by compactness of the product of these balls. The linearity equations are closed in this product, so the limit \(E\) is linear. For \(X=[x_{kl}]\ge0\) in \(M_n(B(H))\) and \(\eta=(\eta_1,\ldots,\eta_n)\in H^n\),
\[
\sum_{k,l}\langle\eta_k,E_i(x_{kl})\eta_l\rangle\ge0.
\]
Each of the finitely many coefficient tests is normal on \(M\); its limit is the same expression with \(E\). All vector tests therefore give \(E^{(n)}(X)\ge0\). This holds for every \(n\), proving complete positivity. Likewise the bounds \(|\langle\eta,E_i(a)\zeta\rangle|\le\|a\|\|\eta\|\|\zeta\|\) pass to the limit and prove contractivity. For \(x\in M\),
\(E_i(x)=T_iS_i(x)\to x\), so \(E(x)=x\). In particular \(E(1)=1\). It is a ucp retraction, and Proposition 4.1 gives injectivity. \(\square\)

The extension \(\widehat S_i\) and the limiting retraction need not be normal. Ultraweak compactness gives their existence but does not assert ultraweak continuity. This is consistent with the definition of injectivity.


<a id="projection-positivity-and-blocks"></a>

### Q1. Contractivity and the fixed unit give positivity

Let \(E:B(H)\to M\) be a norm-one linear projection, where \(M\) is a nonzero concrete von Neumann algebra with the shared unit. It fixes every element of \(M\). For a unit vector \(\eta\in H\), put
\(g(x)=\langle\eta,E(x)\eta\rangle\).
Then \(\|g\|\le1\) and \(g(1)=1\). For \(h=h^*\), the norm-convergent exponential series gives
\[
g(e^{ith})=1+it g(h)+O(t^2),\qquad |g(e^{ith})|\le1.
\]
Squaring the modulus gives \(1-2t\operatorname{Im}g(h)+O(t^2)\le1\). Taking both signs of \(t\) and letting \(t\to0\) forces \(\operatorname{Im}g(h)=0\). If \(0\le a\le1\), then \(\|1-a\|\le1\), so
\[
g(a)=1-g(1-a)\ge0.
\]
Scale to all positive \(a\). Since every vector test on \(E(a)\) is nonnegative, \(E(a)\ge0\). Differences of positive elements show that \(E\) is adjoint preserving. This proves positivity directly from the norm bound.

### Q2. A wrong off-diagonal block contradicts contractivity

Let \(p\in M\) be a projection and \(q=1-p\). For \(0\le a\le1\),
\(0\le E(pap)\le E(p)=p\).
A positive operator \(b\le p\) vanishes on \(qH\): its square-root quadratic form there is zero. Its adjoint also vanishes across that corner. Thus \(b=pbp\). Every operator in \(pB(H)p\) is a linear combination of four positive operators in that corner, giving
\[
E(pxp)=pE(pxp)p.
\tag{Q1}
\]

Take \(x=pxq\) with \(\|x\|\le1\), and write \(y=E(x)\). The row and column operator norms give, for every positive integer \(n\),
\[
\|x+np\|\le\sqrt{1+n^2},\qquad
\|x+nq\|\le\sqrt{1+n^2}.
\]
For a unit vector \(\eta\in pH\), contractivity and \(E(p)=p\) give
\[
|n+e^{it}\langle\eta,y\eta\rangle|
\le\|np+e^{it}y\|\le\sqrt{1+n^2}.
\]
If the scalar coefficient were nonzero, choose its phase to make it positive. Then \(n+|\langle\eta,y\eta\rangle|\le\sqrt{1+n^2}\) for every \(n\), which is impossible as \(n\to\infty\). All such coefficients vanish. Polarization gives \(pyp=0\). Using unit vectors in \(qH\) and adding \(nq\) gives \(qyq=0\) in the same way.

Put \(v=qyp\in M\). If \(v\ne0\), the two remaining blocks have orthogonal domains and ranges. Since \(E(v)=v\), contractivity requires
\[
\begin{aligned}
\max\{\|pyq\|,(n+1)\|v\|\}
&=\|y+nv\|\\
&=\|E(x+nv)\|\le\|x+nv\|
=\max\{\|x\|,n\|v\|\}.
\end{aligned}                                                    \tag{Q2}
\]
For sufficiently large \(n\), this reads \((n+1)\|v\|\le n\|v\|\), a contradiction. Hence \(v=0\), and
\(E(pxq)=pE(pxq)q\).
Scale to every \(x\); apply adjoints for the reverse block. Equation (Q1) and the four-block decomposition now give
\[
E(px)=pE(x),\qquad E(xp)=E(x)p.
\tag{Q3}
\]

<a id="projection-block-diagram"></a>

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 370" role="img" aria-labelledby="projection-block-title projection-block-desc">
<title id="projection-block-title">The two off-diagonal blocks in the norm contradiction</title>
<desc id="projection-block-desc">Rows are pH and qH and columns are pH and qH. The input x occupies the upper-right block. A wrong lower-left output v is fixed by E because v is in M. Adding n v gives output norm (n+1) times norm v and input norm n times norm v for large n, contradicting contractivity.</desc>
<rect width="900" height="370" rx="16" fill="#f6f8fc"/>
<g font-family="system-ui,sans-serif" fill="#18304d">
<text x="26" y="35" font-size="22" font-weight="600">A block in the wrong direction cannot survive E</text>
<text x="92" y="76" font-size="18">input x + n v</text><text x="514" y="76" font-size="18">output E(x + n v) = y + n v</text>
<text x="130" y="103" font-size="16">pH</text><text x="244" y="103" font-size="16">qH</text>
<text x="34" y="153" font-size="16">pH</text><text x="34" y="212" font-size="16">qH</text>
<rect x="80" y="112" width="225" height="120" fill="white" stroke="#74839a"/>
<rect x="193" y="113" width="111" height="59" fill="#cce8ef"/><rect x="81" y="173" width="112" height="58" fill="#ffdfc2"/>
<path d="M193 112V232M80 172H305" stroke="#74839a"/>
<text x="135" y="151" font-size="21">0</text><text x="242" y="151" font-size="21">x</text><text x="124" y="212" font-size="21">n v</text><text x="247" y="212" font-size="21">0</text>
<path d="M340 171H455" stroke="#18304d" stroke-width="3"/><path d="M445 162L455 171L445 180" fill="none" stroke="#18304d" stroke-width="3"/>
<text x="372" y="150" font-size="22">E</text>
<text x="560" y="103" font-size="16">pH</text><text x="709" y="103" font-size="16">qH</text>
<text x="460" y="153" font-size="16">pH</text><text x="460" y="212" font-size="16">qH</text>
<rect x="505" y="112" width="295" height="120" fill="white" stroke="#74839a"/>
<rect x="653" y="113" width="146" height="59" fill="#cce8ef"/><rect x="506" y="173" width="147" height="58" fill="#ffdfc2"/>
<path d="M653 112V232M505 172H800" stroke="#74839a"/>
<text x="570" y="151" font-size="21">0</text><text x="696" y="151" font-size="21">p y q</text><text x="531" y="212" font-size="21">(n + 1) v</text><text x="717" y="212" font-size="21">0</text>
<text x="26" y="280" font-size="19">For large n, ||x + n v|| = n ||v||, but ||y + n v|| = (n + 1) ||v||.</text>
<text x="26" y="315" font-size="18">Contractivity forces v = q y p = 0. The remaining output stays in p B(H) q.</text>
<text x="26" y="345" font-size="16">Exact mechanism: orthogonal block norms in (Q2); no normality of E is used.</text>
</g>
</svg>

The rows and columns show the actual \(pH\oplus qH\) decomposition. The zero diagonal blocks have already been proved. The lower-left block is a hypothetical nonzero \(v\in M\), and (Q2) excludes it. This is a schematic for every Hilbert-space dimension, not a numerical example.

<a id="projection-bimodularity"></a>

### Q3. Projection identities extend to all range multipliers

We give the norm approximation by finite sums of projections needed to extend (Q3). For \(b\ge0\) in \(M\), the positive contractions
\[
b(b+\varepsilon1)^{-1}\in M
\]
converge strongly as \(\varepsilon\downarrow0\) to the projection onto \(\overline{bH}\). They vanish on \(\ker b\). On \(b\eta\), their error has norm at most \(\varepsilon\|\eta\|\), since
\((1-b(b+\varepsilon1)^{-1})b=\varepsilon b(b+\varepsilon1)^{-1}\).
The orthogonal decomposition \(H=\ker b\oplus\overline{bH}\) and the uniform contraction bound extend convergence from this dense set to every vector. Strong closedness puts the limit projection in \(M\).

For \(a=a^*\in M\), let \(p_t\) be this support projection for \((a-t1)_+\), defined by continuous calculus. Each \(p_t\) commutes with \(a\). If \(s<t\), then \((a-t)_+\le(a-s)_+\); vector quadratic forms show that the former vanishes on the latter's kernel. Hence \(p_t\le p_s\). The positive and negative parts of \(a-t\) have product zero. Taking the above strong limit therefore gives
\[
(a-t)p_t\ge0,\qquad (a-t)(1-p_t)\le0.
\]
Choose a partition \(t_0<\cdots<t_m\) containing the spectrum strictly between its endpoints, with every mesh width at most \(\delta\). Then \(p_{t_0}=1\), \(p_{t_m}=0\), and
\(q_j=p_{t_j}-p_{t_{j+1}}\) are mutually orthogonal projections summing to one. On their ranges,
\[
t_jq_j\le aq_j\le t_{j+1}q_j.
\]
Thus \(a_\delta=\sum_{j=0}^{m-1}t_jq_j\in M\) and \(0\le a-a_\delta\le\delta1\), so \(\|a-a_\delta\|\le\delta\). Empty projection ranges cause no difficulty.

Linearity extends (Q3) to every \(a_\delta\). Letting \(\delta\to0\), boundedness of \(E\) and multiplication gives
\(E(ax)=aE(x)\) and \(E(xa)=E(x)a\) for every self-adjoint \(a\in M\). Split a general \(a\) into its real and imaginary self-adjoint parts, and apply the two identities successively. We obtain
\[
E(axb)=aE(x)b\qquad(a,b\in M,\ x\in B(H)).
\]
This supplies the whole passage from range projections to bimodularity with no appeal to a general Borel spectral theorem.

**Corollary 4.3 (Norm-one projection criterion).** A nonzero von Neumann algebra \(M\subset B(H)\) is injective if and only if it is the range of a bounded linear projection of norm one on \(B(H)\).

**Proof.** Injectivity gives the ucp retraction of Proposition 4.1. It is a projection of norm one because it is contractive and fixes the unit.

Conversely, let \(E:B(H)\to M\) be a norm-one projection. It fixes \(M\), and Q1–Q3 prove positivity and \(M\)-bimodularity. We derive complete positivity explicitly. For \(X=[x_{ij}]\ge0\) in \(M_n(B(H))\), put \(Y=[E(x_{ij})]\). Positivity of \(E\) makes \(Y\) self-adjoint. For every column \(b=(b_1,\ldots,b_n)^{\mathsf T}\) with entries in \(M\),
\[
b^*Yb=\sum_{i,j}b_i^*E(x_{ij})b_j
=E\left(\sum_{i,j}b_i^*x_{ij}b_j\right)\ge0.                 \tag{2}
\]
Here the last input is positive because it equals \(b^*Xb\).

To see that these tests imply \(Y\ge0\), let \(R=Y_-\) be its negative part and let \(c_k\) be the \(k\)-th column of \(R^{1/2}\in M_n(M)\). Functional calculus gives
\[
c_k^*Yc_k=(R^{1/2}YR^{1/2})_{kk}=-(R^2)_{kk}.
\]
Equation (2) makes this nonnegative, whereas \((R^2)_{kk}\ge0\). Thus
\(0=(R^2)_{kk}=\sum_iR_{ik}^*R_{ik}\) for every \(k\), so every entry of \(R\) vanishes. Hence \(Y\ge0\). This holds for every \(n\), proving that \(E\) is completely positive. It fixes the shared unit, so is ucp. Proposition 4.1 gives injectivity. No normality of the projection follows or is needed. \(\square\)

## 5. Exercises with solutions

**Exercise 1 (A normal finite model for all bounded operators; intermediate).** On an arbitrary Hilbert space \(H\), let \(p_K\) range over the finite-dimensional subspace projections. Show that compression \(B(H)\to B(K)\), followed by inclusion \(B(K)\to B(H)\), proves semidiscreteness of \(B(H)\).

*Solution.* Both maps are cpc and normal, and the composite is \(x\mapsto p_Kxp_K\). The net \(p_K\) converges strongly to one. On bounded operators this gives strong convergence of the composites to \(x\), and applying it to \(x^*\) gives strong* convergence. The same conclusion holds in the \(\sigma\)-strong* topology: normal positive functionals are sums of vector functionals, and the uniform norm bound controls the tails of such sums. Thus the algebra is semidiscrete. When \(H\) is nonseparable, the finite subspaces are directed by inclusion rather than a sequence.

**Exercise 2 (Why the limit map matters; intermediate).** Give cpc maps converging pointwise ultraweakly to a map other than the identity, but failing pointwise strong convergence.

*Solution.* Let \(H=\mathbb Ce_0\oplus\mathbb Cf\oplus\ell^2(\mathbb N)\), with all the indicated vectors orthonormal. Let \(u_n\) be the self-adjoint unitary exchanging \(e_0\) and the \(n\)-th basis vector \(e_n\) of the last summand and fixing the orthogonal complement. The automorphisms \(\Phi_n(x)=u_nxu_n\) are ucp. Compactness of the product of the ultraweak operator-norm balls gives a subnet converging pointwise ultraweakly to a ucp map \(\Phi\).

For \(x=|e_0\rangle\langle f|\), the images are \(|e_n\rangle\langle f|\). They converge weakly as operators to zero and are uniformly bounded, hence converge ultraweakly to zero. Thus \(\Phi(x)=0\). But \(\|\Phi_n(x)f\|=\|e_n\|=1\), so the subnet cannot converge strongly on this \(x\). The limit is not the identity: the images of the rank-one projection \(p_0\) are \(p_n\), which converge ultraweakly to zero, giving \(\Phi(p_0)=0\).

**Exercise 3 (Normality belongs to the predual; intermediate).** Why does an arbitrary bounded map \(S:M\to M_n\) not always give a preadjoint \(M_n^*\to M_*\)?

*Solution.* Its Banach adjoint always maps \(M_n^*\) into \(M^*\). It has range in \(M_*\) exactly when each scalar coordinate functional of \(S\) is normal, which is equivalent to normality of \(S\). For example, a singular state on an infinite-dimensional von Neumann algebra, viewed as a map to \(\mathbb C\), has an adjoint sending the scalar unit to that singular state, outside \(M_*\).

**Exercise 4 (The unit of a corner; introductory).** In Theorem 2.1, why is \(T'\) cpc as a map into \(M\) even though it is unital only as a map into \(eMe\)?

*Solution.* Its value at \(1_n\) is \(e\), a projection of norm at most one. For a completely positive map from a unital algebra, its norm is the norm of its value at the unit. Inclusion of the corner preserves positivity at every matrix size. Hence it is cpc in \(M\).

**Exercise 5 (Amplifying weak convergence; intermediate).** In Lemma 1.1, show that \(a\mapsto f(x^*a)\) is a normal functional whenever \(f\in M_*\) and \(x\in M\).

*Solution.* Left multiplication by a fixed element is ultraweakly continuous in a von Neumann algebra. Composing it with the normal functional \(f\) gives a normal functional. Equivalently, realize \(f\) as an absolutely summable series of vector coefficients; replace the first vector in each coefficient by its image under \(x\). The bounded multiplier preserves absolute summability.

**Exercise 6 (Keep the extension's unit value; intermediate).** In Theorem 4.2, do the cpc maps \(E_i\) have to be unital? Why is their limit unital?

*Solution.* The reconstruction map can have unit value a proper projection or another positive contraction, so the composite need not be unital. On the particular input \(1\in M\), however, \(E_i(1)=T_iS_i(1)\to1\) ultraweakly. The limit therefore satisfies \(E(1)=1\). It is the approximation to the identity on the subalgebra that gives unitality at the limit.

## References

Jun Tomiyama, [On the projection of norm one in W*-algebras](https://www.jstage.jst.go.jp/article/pjab1945/33/10/33_10_608/_pdf/-char/en), *Proceedings of the Japan Academy* 33, no.10 (1957), 608–612. Theorem 1, printed pp.608–609 (one-based native PDF pages 1–2), supplies the range-block norm method used in Q2. The article reduces its general C*-algebra statement to biduals, refers briefly to an earlier lemma for positivity, and passes from projections to arbitrary multipliers using the von Neumann algebra range. Q1 supplies the full positivity argument here; Q3 supplies the complete finite-projection approximation needed for that passage. The concrete proof needs no bidual theorem, separability, or normality of the projection. Corollary 4.3 supplies the full matrix proof of complete positivity. This attribution concerns the mathematical method; the human paper's prose, scans and PDF are not redistributed or relicensed.

William B. Arveson, [Subalgebras of C*-algebras](https://projecteuclid.org/euclid.acta/1485889628), *Acta Mathematica* 123 (1969), 141–224. Theorem 1.1.1 gives the dilation underlying Lemma 1.1’s Schwarz estimate. Theorem 1.2.3 and its proof give the completely positive extension and bounded compactness methods expanded in [Completely positive finite models](completely-positive-finite-models.md). Section 4 applies those methods to construct the retraction explicitly, for arbitrary Hilbert spaces and von Neumann algebras. It proves semidiscreteness implies injectivity without a separability or faithful normal state assumption.

The commutant characterization in Section 2 also uses the tensor-positivity lesson's exact-marginal correction and its explicit proof of both matrix-order directions for dominated functionals. Arveson's Lemma 1.4.1 and Theorem 1.4.2, printed pp.159–160, supply the corresponding dilation-commutant order method. The finite models in Section 2 retain normal recording maps through every block sum, scalar addition and support normalization; Section 3 then uses their actual preadjoints with dual matrix norms.

Huzihiro Araki, [Some properties of modular conjugation operator of von Neumann algebras and a non-commutative Radon–Nikodym theorem with a chain rule](https://msp.org/pjm/1974/50-2/pjm-v50-n2-p02-p.pdf), *Pacific Journal of Mathematics* 50 (1974), 309–354, Theorem 4(8), printed p.332, gives the cone-vector estimate used in marginal correction. Uffe Haagerup, [The standard form of von Neumann algebras](https://doi.org/10.7146/math.scand.a-11606), *Mathematica Scandinavica* 37 (1975), 271–283, Lemma 2.10, carries that estimate to arbitrary von Neumann algebras by support corners. These inputs do not require a faithful normal state on the whole algebra. The normal representation comparison and Tomiyama's norm-one projection theorem retain their exact stated prerequisites.
