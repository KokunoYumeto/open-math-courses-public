# Central disintegration and measurable matrix assembly

*AI-generated exposition by OpenAI GPT models. CC0-1.0 to the extent of rights held.*

Finite-dimensional approximation is the goal. We assemble bounded matrix models from countably many measurable candidate tuples, repair them inside central pieces, and retain finitely many pieces with a controlled trace tail. We then construct the countable candidates, establish the required factor models by stabilization, and build the central tracial field from its Gram data.

Throughout this lesson \(M\) is finite with separable predual and faithful normal tracial state \(\tau\). Write \(Z=Z(M)\), and let \(T:M\to Z\) be its normalized faithful normal center-valued trace. Thus \(\tau=\tau|_Z\circ T\). We use the selected trace and projection inputs of [Hypertraces and finite injectivity](hypertraces-finite-injectivity.md), the [properly infinite theorem](properly-infinite-injective-algebras-and-dyadic-approximation.md#theorem-4-2), the [finite injective-factor theorem](unitary-couplings-and-finite-injective-factors.md#theorem-5-1), and [Gram repair](repairing-small-matrix-corners.md#theorem-2-1).

The full field constructions used here are [Countably generated measurable fields and their algebras](../components/countable-measurable-fields.md), MF1–9. They construct a measurable field from countable Gram data, its Hilbert direct integral and localization, measurable operator fields and the diagonal commutant. Compact metric selections for the supported operator commutant give the countable generators needed for the algebra, center and fixed-base uniqueness formulas. MF9 proves the tensor-field identity. The base here is a probability space, and all Hilbert fibers are separable. Our inner products are linear in the second variable.

We use the complete Gelfand, GNS, bounded spectral calculus and bounded-density arguments in the operator foundations, and the [compact-metric measure representation](../components/compact-rmk-from-function-covers.md). The latter includes its scalar integration and regularity inputs.

The central field, the norm separable algebra \(A\), and the fiber traces used in the assembly proof are constructed in Theorem 1.1 below. Lemma 2.1 supplies full matrix models in almost every fiber. The countable contraction and projection candidates are constructed after Theorem 3.2. All three inputs are proved in full.

## Assembling finite matrix models

**Theorem 3.2.** Every finite injective von Neumann algebra with separable predual is locally AFD.

**Proof.** Use the central field of Theorem 1.1, the matrix models of Lemma 2.1, and the countable candidates proved below. Fix contractions \(a_1,\ldots,a_r\in M\) and \(0<\varepsilon<1\). Put \(\kappa=\varepsilon/4\). For each \(m\ge1\), choose a positive rational \(b(m)\) small enough for Gram repair with \(B=1\), and such that
\[
4m^2D_m(b(m))<\varepsilon/4.
\tag{10}
\]

**An explicit Gram budget.** Use the modulus supplied by the complete [simultaneous Gram-normalization proof](repairing-small-matrix-corners.md#simultaneous-gram-normalization). For the fixed \(0<\varepsilon<1\) and every integer \(m\ge1\), choose a positive rational number with
\[
0<b(m)<\frac{\varepsilon^2}{512m^6},
\qquad
D_m(b)^2=\frac{m^2b}{1-m^2b}.
\tag{DG1}
\]
Such a rational exists between zero and this positive real bound. The choice implies \(m^2b(m)<1/512\), and therefore \(b(m)<1/(4m^2)\), as required by simultaneous normalization. In particular \(1/(1-m^2b(m))<2\), so
\[
D_m(b(m))^2
<2m^2b(m)
<\frac{\varepsilon^2}{256m^4},
\qquad
4m^2D_m(b(m))<\varepsilon/4.
\tag{DG2}
\]
Thus (10) holds with a specific dimension-dependent budget. For each size \(m\), this one rational tolerance is fixed before the candidate tuples and their measurable qualification sets are formed.

Enumerate all tuples consisting of \(m\), one \(f_j\), \(m\) contractions \(x_i\) from the list \((b_j)\), and \(r\) contraction matrices \(C_l\in M_m\) with Gaussian-rational entries. These matrices form a norm dense subset of the matrix unit ball: approximate first a slight scalar contraction of the desired matrix by rational entries.

For a candidate tuple put
\[
v_l=\sum_{i,j}(C_l)_{ij}x_ifx_j^*.
\]
A tuple qualifies at \(y\) when
\[
\begin{aligned}
&\tau_y(f)\ge1/(2m),\\
&\|f x_i^*x_j f-\delta_{ij}f\|_{2,y}\\
&\qquad\le b(m)\sqrt{\tau_y(f)},\\
&\|a_l(y)-v_l(y)\|_{2,y}<\kappa .
\end{aligned}
\tag{11}
\]
All these tests are measurable: the fields and their products are measurable, and the trace is a pairing with the measurable unit vector \(\xi_y\). We use consistent representatives for this countable list of fields and the fixed finite list \((a_l)\).

Every good fiber has a qualifying tuple. Choose a full matrix model from Lemma 2.1 giving error \(<\kappa/2\). Its column operators \(v_i=e_{i1}\) and first projection \(p=e_{11}\) satisfy \(v_i^*v_j=\delta_{ij}p\), \(\tau_y(p)=1/m\). Its norm contractive approximants have contraction coefficient matrices. Approximate these matrices by rational contraction matrices, \(v_i\) by \(b_j(y)\), and \(p\) by \(f_j(y)\). The bounded product inequality \(\|uv-u'v'\|_2\le\|u-u'\|_2+\|v-v'\|_2\), for contractions, makes all errors in (11) as small as required. The trace lower bound persists, and the Gram bound has a strictly positive available tolerance.

Select the first qualifying tuple. Its level sets \(E_t\) form a countable measurable partition up to a null set; put \(z_t=1_{E_t}\in Z\). Discard null pieces. On \(z_tM\), use the normalized trace \(\tau_t=\tau/\tau(z_t)\). Integrating the squared Gram inequalities in (11) gives the global Gram hypothesis with \(f=z_tf_j\) and \(x_i=z_tb_{s_i}\). Gram repair gives \(e\le f\) and \(w_i^*w_j=\delta_{ij}e\), with
\[
\tau_t(f-e)\le D_m^2\tau_t(e),\qquad
\|x_i e-w_i\|_{2,t}\le D_m\sqrt{\tau_t(e)}.
\tag{12}
\]
In particular \(e\ne0\). Since \(\|x_i\|\le1\),
\[
\|x_i f-w_i\|_{2,t}\le2D_m\sqrt{\tau_t(e)},\qquad
\|x_i f x_j^*-w_iw_j^*\|_{2,t}\le4D_m\sqrt{\tau_t(e)}.
\tag{13}
\]
For the second inequality write \(x_i f x_j^*=(x_i f)(x_j f)^*\) and insert \(w_i,w_j\). Each matrix entry has absolute value at most one. Equations (10)–(13) therefore give
\[
\left\|z_ta_l-\sum_{i,j}(C_l)_{ij}w_iw_j^*\right\|_{2,t}
<\kappa+4m^2D_m<\varepsilon/2.
\tag{14}
\]
Here the first error in (11) integrates to at most \(\kappa\); the second is strictly below \(\varepsilon/4\).

Put \(s_t=\sum_iw_iw_i^*\). The finite algebra
\[
D_t=\operatorname{span}\{w_iw_j^*\}\oplus\mathbb C(z_t-s_t)
\tag{15}
\]
is unital in \(z_tM\); omit its second summand if it is zero. The approximant in (14) belongs to \(D_t\) and has norm at most one, since its matrix block is \(C_l\) and its residual scalar is zero.

Choose finitely many pieces with \(q=\sum_{t\le n}z_t\) and \(\tau(1-q)<\varepsilon^2/4\). Then
\[
D=\left(\bigoplus_{t\le n}D_t\right)\oplus\mathbb C(1-q)
\tag{16}
\]
is finite dimensional and unital. Take the above approximants on the retained pieces and zero on the tail. Central orthogonality and \(\|a_l\|\le1\) give
\[
\begin{aligned}
&\|a_l-d_l\|_2^2\\
&\le(\varepsilon/2)^2\tau(q)+\tau(1-q)\\
&<\varepsilon^2.
\end{aligned}
\tag{17}
\]
Here is the topology argument for the finite algebra at hand. Let \(c_\alpha\) be bounded in operator norm and satisfy \(\|c_\alpha\|_2\to0\). For \(b\in M\), in the tracial GNS space,
\[
\|c_\alpha[b]\|_2=\|c_\alpha b\|_2\le\|b\|\,\|c_\alpha\|_2.
\]
The vectors \([b]\) are dense, and the uniform operator bound extends convergence to every vector. Trace cyclicity gives \(\|c_\alpha^*\|_2=\|c_\alpha\|_2\), so the adjoints converge strongly as well. To see the intrinsic seminorms, express a positive normal functional in this faithful normal representation as a summable series of vector functionals. Its finite partial sums tend to zero on \(c_\alpha^*c_\alpha\), while the remaining sum is bounded by the common squared operator bound times the tail mass. Thus \(\phi(c_\alpha^*c_\alpha)\to0\), and similarly \(\phi(c_\alpha c_\alpha^*)\to0\). This proves sigma-strong* convergence without a factor hypothesis. The converse follows by taking \(\phi=\tau\).

The \(d_l\) are contractions. On bounded sets a faithful finite trace's \(2\)-norm gives the intrinsic sigma-strong* topology; the tracial equality of the two adjoint norms supplies both halves. Thus (17) proves local AFD. \(\square\)

The construction assembles finite matrix approximants. No choice of isomorphisms \(M_y\to R\), or trivialization of a field of copies of \(R\), is needed. The center-times-\(R\) structure follows afterward from the previously proved finite AFD structure theorem.

<a id="3-countably-many-candidates-suffice"></a>

### Countable candidates and spectral rounding

**Lemma 3.1.** If \(0\le a\le1\), \(p\) is a projection, and \(q=1_{[1/2,1]}(a)\), then
\[
\|q-p\|_2\le2\|a-p\|_2.
\tag{8}
\]
Consequently, for a contraction \(b\),
\[
\left\|1_{[1/2,1]}(b^*b)-p\right\|_2\le4\|b-p\|_2.
\tag{9}
\]

**Proof.** Spectral calculus on \(1-q\) and \(q\) gives
\[
\|(1-q)p\|_2\le2\|(a-p)p\|_2,\qquad
\|q(1-p)\|_2\le2\|(a-p)(1-p)\|_2.
\]
The square of \(\|q-p\|_2\) is the sum of the two left squares. The two right squares add to \(4\|a-p\|_2^2\), by tracial orthogonality. For (9), write \(b^*b-p=b^*(b-p)+(b^*-p)p\) and use contraction bounds. \(\square\)

Choose a countable norm dense set of contractions \(b_j\) in \(A\), and put \(f_j=1_{[1/2,1]}(b_j^*b_j)\in M\). For every good fiber, the \(b_j(y)\) are \(2\)-norm dense in the unit ball of \(M_y\). Indeed the quotient norm on \(\lambda_y(A)\) permits lifts with norm arbitrarily close to one; rescaling these lifts and using Kaplansky density proves the assertion. Formula (9) then gives a countable family \(f_j(y)\) that approximates all fiber projections.

Spectral rounding is compatible with these decomposable representatives. For \(h=b_j^*b_j\), take continuous functions
\[
g_n(t)=\min\{1,\max\{0,1+n(t-1/2)\}\},\qquad 0\le t\le1.
\]
They are bounded by one and converge pointwise to \(1_{[1/2,1]}\). Continuous functional calculus, using uniform polynomial approximation, makes \(g_n(h(y))\) a measurable operator field and gives \(g_n(h)=\int^\oplus g_n(h(y))\). The spectral theorem gives strong convergence in every fiber to \(q_j(y)=1_{[1/2,1]}(h(y))\). The measurable-operator testing criterion and closure of measurable sections under pointwise norm limits show that \(q_j\) is measurable. Dominated convergence on each square-integrable section identifies its integral with the strong limit \(1_{[1/2,1]}(h)=f_j\). Uniqueness of decomposable operator representatives therefore permits the choice \(f_j(y)=q_j(y)\); the countably many choices fit one conull set.

<a id="2-why-almost-every-fiber-has-full-matrix-models"></a>

## Full matrix models in the factor fibers

**Lemma 2.1.** If \(M\) is injective, almost every factor \(M_y\) in (1) is either \(M_n(\mathbb C)\) for a finite \(n\), or the tracial infinite product \(R\).

**Proof.** The algebra \(N=M\bar\otimes B(\ell^2)\) is injective, properly infinite and has separable predual. We give the permanence details. In a faithful normal representation of \(M\) on \(H\), let \(E:B(H)\to M\) be a ucp retraction, using the full retraction criterion. For \(x\in B(H\otimes\ell^2)\), apply \(E\) to every matrix entry of \(x\). Complete positivity and contractivity on each finite matrix corner bound the resulting form on finitely supported vectors by \(\|x\|\), so it defines a bounded operator \(E_\infty(x)\). Testing positive matrices on finitely supported vectors proves complete positivity at every matrix size. The diagonal entries of \(E_\infty(1)\) are one and the others zero.

An operator on \(H\otimes\ell^2\) belongs to \(M\bar\otimes B(\ell^2)\) exactly when all its entries belong to \(M\). One direction follows by commuting with \(M'\otimes1\) and testing entries; the other follows because the finite block compressions lie in \(M\otimes M_n\) and converge strongly to the operator. Hence \(E_\infty\) takes values in \(N\) and fixes \(N\). It is a ucp retraction, proving injectivity of \(N\); no normality of \(E\) was assumed. The two coordinate isometries onto the even and odd basis vectors exhibit proper infiniteness. Separable predual of \(M\) gives a separable faithful tracial GNS space, so \(N\) has a faithful normal representation on the separable space \(H\otimes\ell^2\). The normal-functional quotient of the completed Hilbert projective tensor product, proved in CP1–6, gives separable predual of \(N\): finite rational combinations of pairs from a countable Hilbert-dense set are dense in that tensor product, and their quotient images remain dense.

The proved properly infinite theorem gives increasing unital dyadic matrix algebras \(Q_k\), with \((\bigcup_k Q_k)''=N\). Tensoring the Hilbert field with \(\ell^2\) and adjoining the constant matrix units gives
\[
N=\int_Y^\oplus\bigl(M_y\bar\otimes B(\ell^2)\bigr)\,d\mu(y).
\tag{6}
\]
This identity also follows directly from the countable-generator theorem: both sides are generated by the fields from \(A\), the constant matrix units and the diagonal algebra.

Choose decomposable representatives for all matrix units of all \(Q_k\). Their countably many identities and inclusions hold off one null set. At each remaining point, \(Q_k(y)\) is a unital copy of its full matrix algebra. The integral of the field generated by their union is \(N\): apply the generator theorem, noting that adjoining its diagonal algebra still gives \(N\). Field uniqueness now gives
\[
\left(\bigcup_kQ_k(y)\right)''=M_y\bar\otimes B(\ell^2)
\quad\text{almost everywhere}.
\tag{7}
\]
The full [directed AFD-to-injectivity proof](central-traces-and-afd-finite-algebras.md#theorem-4-1) makes these stabilized fibers injective. It averages onto the finite-algebra commutants and then uses the standard-form commutant; it does not presume that a possibly nonnormal limit fixes a strongly dense subalgebra's closure. Corner permanence follows directly from the retraction criterion: for a projection \(p\) and a ucp retraction \(F:B(K)\to L\), the map \(b\mapsto pF(b)p\) on \(B(pK)\), with \(b\) extended by zero on \(p^\perp K\), is a ucp retraction onto \(pLp\). Its unit value is \(p\), and it fixes the corner. Compress by \(1\otimes e_{11}\), taking \(p=1\otimes e_{11}\) in this retraction, to obtain injectivity of \(M_y\).

Each \(H_y\) is separable and each \(\tau_y\) faithful, so \(M_y\) has separable predual by the same normal-functional quotient. A finite factor is either a finite matrix algebra or type \(\mathrm{II}_1\); in the latter case the finite injective-factor theorem identifies it with \(R\). Thus every finite list in \(M_y\) has tracial approximants in a unital full matrix subalgebra. \(\square\)

<a id="1-building-the-central-tracial-field"></a>

## Building the central tracial field

**Theorem 1.1.** There are a compact metrizable probability space \((Y,\mu)\), a measurable field of separable Hilbert spaces \(H_y\), and finite factors \(M_y\subset B(H_y)\) with faithful normal tracial states \(\tau_y\), such that
\[
L^2(M,\tau)\cong\int_Y^\oplus H_y\,d\mu(y),\qquad
M\cong\int_Y^\oplus M_y\,d\mu(y),\qquad
Z\cong L^\infty(Y,\mu).
\tag{1}
\]
For each fixed \(x\in M\), with a decomposable representative \(x(y)\),
\[
\tau(x)=\int_Y\tau_y(x(y))\,d\mu(y).
\tag{2}
\]

**Proof.** Choose countably many self-adjoint central contractions generating \(Z\), and put \(C=C^*(1,z_1,z_2,\ldots)\). Separability of the predual supplies such a sequence: choose a countable weak* dense subset of the central unit ball and take real and imaginary parts. Gelfand representation gives \(C=C(Y)\) for compact metrizable \(Y\). To see metrization explicitly, send a character to its values on the \(z_j\). These lie in \([-1,1]\) and determine the character on the dense polynomial algebra, hence on \(C\). This is a continuous injection from the compact character space into the Hausdorff countable cube, so is a homeomorphism onto its image. The metric \(\sum_j2^{-j}|s_j-t_j|\) induces the product topology on that cube.

The state \(\alpha=\tau|_Z\) gives a probability measure \(\mu\). In its faithful normal GNS representation, the strong closure of \(C(Y)\) is \(L^\infty(Y,\mu)\); this identifies \(Z\) with that algebra. Here is the scalar density step. Regularity approximates each measurable set by a compact subset and an open superset with arbitrarily small difference in measure. The compact metric separator between them is a continuous function between zero and one. These functions approximate the indicator in \(L^2(\mu)\). Their uniform bound gives strong convergence as multiplication operators, first on bounded functions and then on all of \(L^2(\mu)\). Indicators and uniform simple approximation consequently give all bounded measurable multipliers. Conversely those multipliers form a von Neumann algebra by MF4 on the constant one-dimensional field.

Choose a norm separable unital C* algebra \(A\subset M\), containing \(C\), with \(A''=M\). A countable weak* dense set in the unit ball of \(M\) gives the required generators. Let \(A_0\) be the countable algebra over \(\mathbb Q+i\mathbb Q\) generated by these generators and a countable dense subalgebra \(C_0\subset C\).

Choose measurable representatives for the countably many functions \(T(a^*b)\), \(a,b\in A_0\). Their linearity, positivity, trace identities and inequalities
\[
T(b^*a^*ab)\le\|a\|^2T(b^*b)
\tag{3}
\]
hold simultaneously off one null set: positivity is tested on countably many rational linear combinations. Include \(T(ca)=cT(a)\), \(c\in C_0\), in these simultaneous identities. Define
\[
\langle[a],[b]\rangle_y=T(a^*b)(y).
\tag{4}
\]
Quotient by its null space and complete to \(H_y\). Left multiplication \(\lambda_y(a)[b]=[ab]\) is bounded by \(\|a\|\), by (3). Right multiplication \(\rho_y(a)[b]=[ba]\) has the same bound by the trace identity. Both extend continuously from \(A_0\) to \(A\), with the usual adjoints, and commute. The sections \([a]\) have measurable Gram functions and are total, so the measurable-field generation theorem applies. Its operator testing criterion makes the \(\lambda_y(a)\) measurable.

Put \(\xi_y=[1]\), \(M_y=\lambda_y(A)''\). The vector \(\xi_y\) has norm one and is cyclic for both actions. It is therefore separating for \(M_y\): if \(x\xi_y=0\), then \(x\rho_y(a)\xi_y=0\) for every \(a\), hence \(x=0\). The vector state \(\tau_y\) is normal and faithful. It is tracial on \(\lambda_y(A)\) by construction, and on \(M_y\) by bounded strong* approximation and normality. More explicitly, approximate each of two bounded operators in \(M_y\) strongly* by bounded elements of \(\lambda_y(A)\); their products converge strongly, so the two trace pairings agree in the limit. Thus \(M_y\) is finite.

Equation (4) and \(\tau=\alpha T\) make
\[
U:[a]\longmapsto(y\longmapsto[a]_y)
\tag{5}
\]
an isometry from \(L^2(M,\tau)\) into the direct integral. It is onto. The range contains \(c(y)[a]_y\) for \(c\in C(Y)\), since multiplication by \(c\) agrees with central multiplication. The bounded fundamental sections satisfy \(\|[a]_y\|\le\|a\|\). Density of continuous functions in scalar \(L^2\) therefore gives \(1_E[a]_y\) in the closed range for every measurable \(E\). These sections span a dense subspace of the direct integral by the localization theorem.

The unitary \(U\) intertwines left multiplication by \(A\) with its decomposable fields. It intertwines \(Z\) with all diagonal multipliers. The countable-generator theorem gives \(UMU^*=\int^\oplus M_y\). Its center is \(UZU^*\), the diagonal algebra, so the direct-integral center theorem says that \(M_y\) is a factor almost everywhere. Formula (2) follows from the vector \(\xi=(\xi_y)\). All exceptional sets here concern countably many construction identities, followed by any fixed finite family of operators under consideration. We do not assert evaluation of every element of \(M\) on one universal conull set. \(\square\)

If the statement is read as assigning finite factors at every point of the compact base, replace the Hilbert space and algebra on the exceptional measurable null set by \(\mathbb C\) and \(\mathbb C1\), with their usual trace. Such a null-set replacement changes neither direct integral nor any of the displayed integral identities. All countable construction identities remain asserted on the common conull set.

## 4. Exercises with complete solutions

### Candidates, Gram repair and central tails

**Exercise 6.** Check (8) when \(a\) and \(p\) do not commute.

*Solution.* On \(1-q\), the operator \(1-a\) is bounded below by \(1/2\); hence \(\|(1-q)p\|_2\le2\|(1-q)(1-a)p\|_2\le2\|(a-p)p\|_2\). On \(q\), \(a\ge1/2\) gives the other estimate. Trace cyclicity identifies \(\|q-p\|_2^2=\|(1-q)p\|_2^2+\|q(1-p)\|_2^2\). Right multiplication by \(p\) and \(1-p\) decomposes \(\|a-p\|_2^2\) into orthogonal squares. No commutation with \(p\) is used.

**Exercise 7.** Why are rational contraction matrices dense in the closed matrix unit ball?

*Solution.* Given a contraction \(C\) and \(\delta>0\), put \(\eta=\min\{\delta,1\}\) and first replace it by \((1-\eta/2)C\). Approximate its finitely many entries by Gaussian rationals so the operator norm error is below \(\eta/2\). The resulting matrix has norm at most one and distance below \(\eta\le\delta\) from \(C\). The smaller positive budget ensures that the scalar contraction stays between zero and one for every original tolerance \(\delta>0\).

**Exercise 8.** Describe the first-qualifying selection sets explicitly.

*Solution.* If \(B_t\) is the measurable set where tuple \(t\) satisfies (11), put \(E_t=B_t\setminus\bigcup_{s<t}B_s\). These sets are measurable and disjoint. Their union is the union of the \(B_t\), which contains every good fiber. Thus its complement is null.

**Exercise 9.** Why does the integrated Gram estimate have the correct trace scale?

*Solution.* Squaring and integrating its pointwise bound gives \(\tau_t((fx_i^*x_jf-\delta_{ij}f)^*(fx_i^*x_jf-\delta_{ij}f))\le b(m)^2\tau_t(f)\). Taking square roots gives precisely the hypothesis of Gram repair in the normalized trace \(\tau_t\).

**Exercise 10.** Derive the first bound in (13).

*Solution.* Write \(x_if-w_i=x_i(f-e)+(x_ie-w_i)\). The first term has norm at most \(\sqrt{\tau_t(f-e)}\le D_m\sqrt{\tau_t(e)}\); the second has the same bound by (12). Their sum gives \(2D_m\sqrt{\tau_t(e)}\).

**Exercise 11.** Why may the matrix size depend on the selected central piece?

*Solution.* There are only countably many sizes and candidate tuples. Each retained piece has a finite matrix algebra, and only finitely many pieces are retained in (16). Their direct sum is finite dimensional even if the original countable selection has unbounded sizes.

**Exercise 12.** Check that the central tail causes at most the error stated in (17).

*Solution.* Its approximant is zero and \(\|a_l\|\le1\), so \(\tau((1-q)a_l^*a_l)\le\tau(1-q)\). Central orthogonality eliminates cross terms with all retained pieces. Summing (14) squared with weights \(\tau(z_t)\) proves (17).

### Central fields and stabilized fibers

**Exercise 1.** Why does a countable weak* dense set generate \(M\) as a von Neumann algebra?

*Solution.* The generated von Neumann algebra is weak* closed and contains that set and its scalar multiples. It therefore contains the unit ball of \(M\) and then all of \(M\). Taking the unital C* algebra generated by the set gives a norm separable algebra with this strong closure.

**Exercise 2.** Explain why the central multiplier \(c\in C_0\) acts as \(c(y)\) on \(H_y\).

*Solution.* For \(b\in A_0\), expand \(T(((c-c(y))b)^*(c-c(y))b)(y)\). Center bimodularity identifies its four terms with the same value \(|c(y)|^2T(b^*b)(y)\), with coefficients \(1,-1,-1,1\); their sum is zero. Thus \([cb]_y=c(y)[b]_y\). Norm density extends this identity to every \(c\in C\).

**Exercise 3.** Prove the separating assertion for \(\xi_y\).

*Solution.* If \(x\in M_y\) kills \(\xi_y\), commutation with the bounded right action gives \(x[b]_y=x\rho_y(b)\xi_y=\rho_y(b)x\xi_y=0\). These vectors are dense, so the bounded operator \(x\) vanishes. A vector state's support is therefore the identity, proving faithfulness.

**Exercise 4.** Why does a countable collection of identities admit a common conull set?

*Solution.* Each identity fails on a null set. The union of countably many such sets is measurable and null. The complement works for all identities. An uncountable union has no such guarantee, which is why universal evaluation of \(M\) was not asserted.

**Exercise 5.** What makes the field in (7) the whole stabilized field?

*Solution.* The integral of its countably generated matrix field, after adjoining the diagonal algebra, is generated by \(\bigcup_kQ_k\) and \(Z\otimes1\). The first set already generates \(N\). Both measurable fields therefore have integral \(N\), and the field uniqueness theorem identifies them almost everywhere.

## References and proof scope

The finite matrix assembly uses complete local proofs of the central tracial field, countable candidates, factor approximation and Gram repair. Its rational tolerance is fixed separately for each matrix size, with the explicit bound in (DG1)–(DG2). No choice of fiber isomorphisms to \(R\), or trivialization of a field of copies of \(R\), is required.

George A. Elliott, [*On approximately finite-dimensional von Neumann algebras*](https://journals.msp.org/mscand/article/download/2001/2000/2032), *Mathematica Scandinavica* 39 (1976), 91–101, Lemmas 3.3 and 3.5, pp.94–96, concerns direct summands of biduals. Lemma 3.3 invokes direct-integral representation and field uniqueness by reference and uses the continuum hypothesis in a cardinality argument. These lemmas do not supply the central tracial field or first-qualifying matrix assembly proved here.

Uffe Haagerup, [*A new proof of the equivalence of injectivity and hyperfiniteness for factors on a separable Hilbert space*](https://doi.org/10.1016/0022-1236(85)90002-3), *Journal of Functional Analysis* 62 (1985), 160–201, Section 6.3, describes the nonfactor extension context and refers to disintegration theory. The complete measurable construction and central-piece matrix repair used here are supplied by the linked local arguments.

The [countable measurable-field module](../components/countable-measurable-fields.md) proves the direct integral, diagonal commutant, compact continuous-equation choices, generated algebras, centers, fixed-base uniqueness and tensor identity. Edward G. Effros, [*The Borel space of von Neumann algebras on a separable Hilbert space*](https://msp.org/pjm/1965/15-4/pjm-v15-n4-p07-p.pdf), *Pacific Journal of Mathematics* 15 (1965), 1153–1164, Theorems 2–3, gives the broader Borel-choice and commutant context. The local compact selections prove the particular choices needed here; a general standard-Borel-space theorem is not assumed.

The construction has separable-predual scope, a probability base and separable Hilbert fibers. Null-set conclusions concern countable construction identities and specified operator lists. The broader finite local conclusion without separability is proved in [Injective algebras and separable tracial envelopes](injective-algebras-and-separable-tracial-envelopes.md).

