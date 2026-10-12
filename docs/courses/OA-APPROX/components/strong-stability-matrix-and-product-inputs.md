# Exact matrix averages and complete tracial product inputs

*Original programme exposition: CC0-1.0 to the extent of rights held.*

The [tensor-absorption lesson](../src/strong-stability-and-tensor-absorption.md) needs a finite matrix average, two kinds of normal limit map, and the entire tracial product for varying matrix sizes. These constructions retain arbitrary centers; a factor assumption will be used only where it is explicitly specified.

The complete earlier inputs are CF's calculus and Hilbert constructions, CP preduals, BD bounded density, STC for an already normal state, ST1–2 for its faithful normal image and inverse, [NT1–2](central-sequence-foundations.md#nt1-normal-functional-decomposition), [PC/FCT](central-finite-trace-inputs.md), [AF1–5](central-afd-uniqueness-inputs.md), and [CQ2's full trace representation](central-sequence-quotient-and-lifting-inputs.md#cq2-faithful-trace-hilbert-representation). Inner products are linear in the second variable.

<a id="ss0-exact-matrix-coordinates-and-finite-average"></a>

## SS0. Coordinates, a finite unitary average and the full numerical bound

Let \(M\subseteq B(H)\) be a von Neumann algebra containing unital matrix units \((e_{ij})_{1\leq i,j\leq p}\), \(p\geq1\). Put \(D=\operatorname{span}\{e_{ij}\}\) and \(B=D'\cap M\). The Hilbert-space map
\[
U:\mathbb C^p\otimes e_{11}H\longrightarrow H,\qquad
U(\delta_i\otimes\xi)=e_{i1}\xi
\tag{SS0.1}
\]
is unitary. The summands are isometric with mutually orthogonal ranges, and those ranges fill \(H\) because \(\sum_i e_{ii}=1\). It carries the scalar matrix units to the given \(e_{ij}\).

Writing \(Q=e_{11}Me_{11}\), compression gives
\[
U^*MU=M_p(Q).
\]
Indeed the \((i,j)\) entry of \(U^*xU\) is \(b_{ij}=e_{1i}xe_{j1}\in Q\), and every matrix of entries in \(Q\) is obtained from
\(\sum_{i,j}e_{i1}b_{ij}e_{1j}\in M\).
An element commutes with all matrix units exactly when this matrix is \(1_p\otimes b\), \(b\in Q\). Thus compression identifies \(B\) with \(Q\), with inverse
\[
b\longmapsto\sum_k e_{k1}b e_{1k}.
\]
These are normal maps on their entire domains by CP's fixed-multiplier and finite-vector-coordinate tests. Unitary conjugation is normal by the same vector-pair substitution. Consequently multiplication identifies \(M\) normally with the concrete spatial product \(D\bar\otimes B\).

In the original algebra the full coordinates are
\[
x=\sum_{i,j}e_{ij}a_{ij},\qquad
a_{ij}=\sum_k e_{ki}xe_{jk}\in B.
\tag{SS0.2}
\]
Under \(U\), \(a_{ij}\) is the diagonal amplification of \(b_{ij}\). Hence
\[
\|a_{ij}\|=\|b_{ij}\|\leq\|x\|.
\tag{SS0.3}
\]
This bound does not come from summing \(p\) separate norm estimates. The coefficient of \(e_{\ell m}a\), \(a\in B\), is
\(\delta_{i\ell}\delta_{jm}a\);
the matrix products and adjoints therefore give the claimed full algebra isomorphism.

Define the finite formula
\[
E_D(x)=\frac1p\sum_{i,j}e_{ij}xe_{ji}.
\tag{SS0.4}
\]
It is the normalized matrix trace on the first leg of SS0.2, times the identity on \(B\). To realize it as a finite unitary average, let \(\varepsilon=(\varepsilon_1,\ldots,\varepsilon_p)\in\{-1,1\}^p\), \(v_\varepsilon=\sum_i\varepsilon_i e_{ii}\), and let \(u_\sigma=\sum_i e_{\sigma(i),i}\) for a permutation \(\sigma\) of \(\{1,\ldots,p\}\). Both are unitary. Averaging over all signs kills each off-diagonal entry: flipping just its first sign pairs cancelling terms. Averaging the surviving diagonals over permutations distributes each to every diagonal position equally, with \((p-1)!\) occurrences at each position. Thus
\[
E_D(x)=\frac1{2^p p!}
\sum_{\varepsilon,\sigma}
(u_\sigma v_\varepsilon)x(u_\sigma v_\varepsilon)^*.
\tag{SS0.5}
\]
This includes \(p=1\), where the map is the identity. No existence or integration theorem for Haar measure is a premise.

The finite multiplier formula proves normality and complete positivity at every matrix level. It is unital, has range \(B\), fixes \(B\), and is a \(B\)-bimodule map. It is faithful: for \(x\geq0\), vanishing of the sum in SS0.4 makes every positive summand zero. In particular \(e_{ii}xe_{ii}=0\), so \(x^{1/2}e_{ii}=0\) for every \(i\); their sum gives \(x=0\). NT1's unital positive-map bound gives norm contraction. A faithful normal tracial state, when given, is preserved by the finite formula, and its Schwarz inequality gives trace \(2\)-norm contraction.

For a unitary \(u=\sum_{i,j}\lambda_{ij}e_{ij}\), the scalar matrix identity \(u^*u=1_p\) gives \(\sum_{i,j}|\lambda_{ij}|^2=p\). The finite scalar Schwarz inequality yields, for every normal functional \(\psi\),
\[
\|[u,\psi]\|
\leq\sqrt p\left(\sum_{i,j}\|[e_{ij},\psi]\|^2\right)^{1/2}
\leq p^{3/2}\max_{i,j}\|[e_{ij},\psi]\|.
\tag{SS0.6}
\]
The same estimate holds in trace \(2\)-norm for operator commutators. Also
\[
(\psi-\psi\circ\operatorname{Ad}u)(x)
=[u,\psi](xu^*),
\]
so its functional norm equals \(\|[u,\psi]\|\), since fixed multiplication by a unitary is an isometry onto the unit ball. Apply the triangle inequality to the exact finite average SS0.5. This proves the full bounds
\[
\|\psi-\psi E_D\|\leq p^{3/2}\max_{i,j}\|[e_{ij},\psi]\|,
\qquad
\|x-E_D(x)\|_2\leq p^{3/2}\max_{i,j}\|[e_{ij},x]\|_2.
\tag{SS0.7}
\]
For the second assertion right multiplication by \(u^*\) preserves the trace norm. All unitary coefficient, finite averaging and contraction steps are supplied here.

<a id="ss1-trace-domination-normality-and-complete-balls"></a>

## SS1. Trace-preserving positive maps are normal on the whole domain

Let \(A,B\) be nonzero finite von Neumann algebras with faithful normal normalized traces \(\tau_A,\tau_B\). If a bounded positive map \(\Phi:A\to B\) satisfies
\[
\tau_B\Phi=\tau_A,
\tag{SS1.1}
\]
then \(\Phi\) is ultraweakly continuous on its entire domain. Neither algebra has to be a factor or have separable predual.

First prove a domination fact. If a positive bounded functional \(\lambda\) on \(A\) satisfies \(\lambda\leq C\tau_A\), \(C\geq0\), on the positive cone, it is normal. At \(C=0\) it is zero. Otherwise its sesquilinear form on the trace Hilbert vectors is bounded:
\[
|\lambda(x^*y)|^2
\leq\lambda(x^*x)\lambda(y^*y)
\leq C^2\|x\|_{2,A}^2\|y\|_{2,A}^2.
\]
CF's full Hilbert Riesz construction gives \(0\leq K\leq C1\) with
\(\lambda(x^*y)=\langle x\Omega,K y\Omega\rangle\).
The identity
\(\lambda((ax)^*y)=\lambda(x^*a^*y)\)
makes \(L_a^*K=K L_a^*\) on dense vectors, hence everywhere. Thus \(K\) commutes with the represented algebra, as does its continuous positive square root. Therefore
\[
\lambda(x)=\langle K^{1/2}\Omega,L_xK^{1/2}\Omega\rangle.
\tag{SS1.2}
\]
STC and ST1–2 apply because the trace used for this representation was already normal and faithful. CP now makes SS1.2 a normal functional on the original \(A\).

For \(b\in B\), the normal positive functional
\(\rho_b(x)=\tau_B(b^*xb)\)
satisfies \(\rho_b\leq\|b\|^2\tau_B\). To check this for \(x\geq0\), use the trace law and
\(x^{1/2}bb^*x^{1/2}\leq\|b\|^2x\).
The span of these functionals is norm dense in \(B_*\). CP expresses each normal functional as a summable vector-pair series in the faithful normal trace representation. Truncate the series and approximate its finitely many vectors by \(a\Omega,b\Omega\); the operator-norm coefficient bound controls the predual error. These bounded-vector pairings are linear combinations of the positive \(\rho_b\), by the exact complex polarization identity
\[
\tau_B(a^*xb)=\frac14\sum_{k=0}^3(-i)^k
\rho_{a+i^k b}(x).
\tag{SS1.3}
\]
The identity follows by expanding all four terms and cancelling the two geometric scalar sums.

For each \(\rho_b\), positivity and SS1.1 give
\[
0\leq\rho_b\Phi\leq\|b\|^2\tau_A.
\]
The domination fact makes it normal. Norm approximation and
\(\|(\rho-\eta)\Phi\|\leq\|\rho-\eta\|\|\Phi\|\)
then make every \(\rho\Phi\), \(\rho\in B_*\), normal, because CP proves norm closedness of \(A_*\). This is exactly whole-domain ultraweak continuity. In particular a trace-preserving star isomorphism and its inverse are normal by applying this argument in both directions.

We also need completeness of bounded trace balls. The trace \(2\)-norm has the scalar formula
\[
\|x\|_2=\sup_{\substack{a\in A\\\|a\|_2\leq1}}|\tau_A(a^*x)|,
\]
proved by scalar Schwarz and \(a=x/\|x\|_2\) at nonzero \(x\). It is consequently ultraweakly lower semicontinuous. For a trace-Cauchy sequence of operator-norm contractions, CP/CF's compact unit ball gives an ultraweak ultrafilter limit \(x\) in that ball. For each fixed sequence index \(n\), apply the scalar formula to its difference from this limit:
\[
\|x_n-x\|_2\leq\lim_{m\to\omega}\|x_n-x_m\|_2.
\]
The Cauchy tails make the right side arbitrarily small for all sufficiently large \(n\). Thus the sequence converges in trace norm inside the same ball. Scaling handles every fixed operator-norm bound. Arbitrary Cauchy nets are covered by metric completeness: choose a sequence of increasingly late indices beyond the successive \(2^{-k}\) Cauchy thresholds, dominating the previously chosen indices, and then use the triangle inequality to compare every sufficiently late net element with that sequence's limit. No countable cofinal subset is assumed.

Finally NT2 makes bounded trace \(2\)-convergence intrinsic strong* convergence. Hence a uniformly bounded sequence of completely positive maps with pointwise trace-Cauchy values has a linear unital completely positive limit if the original maps were unital. Entrywise bounded strong convergence preserves positive matrices by testing all their vector quadratic forms. Trace preservation passes to the limit by scalar Schwarz. SS1.1 then proves whole-domain normality of that limit. This supplies the finite-trace summability proof without an unproved general order-normality criterion.

<a id="ss2-whole-variable-matrix-tracial-product"></a>

## SS2. The tracial product for every sequence of finite matrix sizes

Let \(p_\nu\geq1\) be integers. Embed
\[
A_n=\bigotimes_{\nu=1}^n M_{p_\nu}(\mathbb C)
\cong M_{d_n}(\mathbb C),\qquad d_n=\prod_{\nu=1}^n p_\nu,
\]
by unit padding, with the consistent product of normalized matrix traces. Finite tensor matrix units explicitly identify \(A_n\) with the displayed full matrix algebra; matrix entries show their multiplication, adjoints and unit sum. The normalized trace is the product trace on elementary tensors.

On the algebraic local union \(A_{\rm loc}\), complete the inner product
\(\langle x,y\rangle=\tau_{\rm loc}(x^*y)\)
to \(H_0\), with vector \(\Omega=1\). Positivity and faithfulness on any finite collection follow in a containing full matrix stage. Left and right multiplication by a local \(a\) are bounded by \(\|a\|\), using positive order and that stage's trace law, and have the expected adjoints. They commute. The finite trace version of CQ2's spectral argument proves that each local left representation is isometric. Let \(A\) be its norm closure and \(R(p_\nu)=A''\).

The vector \(\Omega\) is cyclic. It is separating for \(R(p_\nu)\) because the bounded right local multipliers commute with that whole bicommutant and their orbit of \(\Omega\) is dense. Its vector state is normal by CP. It is tracial on the local union, hence on \(A\) by norm continuity, and on the whole bicommutant by CQ2's two normal-functional extensions using BD. Separation makes it faithful. The isometry trace argument makes \(R(p_\nu)\) finite.

AF1's complete finite-dimensional trace projection gives a normal trace-preserving conditional expectation \(P_n:R(p_\nu)\to A_n\). In the trace Hilbert space it is exactly the orthogonal projection onto \(A_n\Omega\): its explicit matrix coefficients satisfy the trace pairings with every matrix unit. The union of these finite subspaces is dense by the construction of \(H_0\), so
\[
\|P_n(x)-x\|_2\longrightarrow0.
\tag{SS2.1}
\]
If \(x\) is central, bimodularity makes \(P_n(x)\) central in the full matrix algebra \(A_n\), so it is the scalar \(\tau(x)1\). Faithfulness and SS2.1 make \(x\) that scalar. Thus \(R(p_\nu)\) is a factor.

Its Hilbert space is separable: finite rational complex matrix combinations in countably many finite stages are a countable dense set. CP's summable vector-pair predual construction then gives a separable predual, by truncating the series and approximating each vector from a countable dense Hilbert set.

If infinitely many \(p_\nu\geq2\), then \(d_n\to\infty\). This factor has no minimal projection. If a nonzero minimal \(q\) had trace \(\alpha>0\), choose \(n\) with \(1/d_n<\alpha\). A diagonal cell of \(A_n\) has trace \(1/d_n\). FCT7 comparison would place a nonzero copy under \(q\), with trace strictly between zero and \(\alpha\), contradicting minimality. PC4 and [FH1's full-center type criterion](fullness-hypercentrality-and-tail-inputs.md#fh1-finite-type-and-whole-center-halving) therefore make it type \(\mathrm{II}_1\). The increasing full matrix stages are strongly dense by definition and BD; it is AFD. AF5's entire finite AFD uniqueness theorem identifies it normally with \(R\).

If only finitely many sizes are nontrivial, the unit-padded union is a single finite matrix algebra. Its whole closure remains that algebra. If every size is one, the product is \(\mathbb C\). These are the exact boundary cases; summability by itself does not change them.

For later use, \(M_p\bar\otimes R\cong R\) for every finite \(p\): the same construction with sizes \(p,2,2,\ldots\) gives its faithful product trace representation and increasing matrix stages, and AF5 applies. Also \(R\bar\otimes R\cong R\). Interleave its two dyadic strings. On the finite local trace vectors this reindexing preserves all inner products, so it extends to a unitary between their whole trace Hilbert completions. It intertwines the local algebras and their BD closures. STC/ST1–2 identifies the given faithful normal trace representations; CP makes conjugation normal in both directions. Thus the interleaving is a whole normal von Neumann algebra isomorphism.

<a id="ss3-complete-normal-gns-spatial-splitting"></a>

## SS3. A faithful normal product state supplies the spatial splitting

Let \(A,B\subseteq M\) be commuting unital von Neumann subalgebras, with \(M=A\vee B\). Suppose faithful normal states \(\alpha,\beta,\rho\) satisfy
\[
\rho(ab)=\alpha(a)\beta(b)\qquad(a\in A,\ b\in B).
\tag{SS3.1}
\]
Then multiplication gives a normal spatial isomorphism \(A\bar\otimes B\cong M\). No factor or tracial hypothesis is assumed.

STC and ST1–2 give faithful normal GNS representations, with whole-domain normal inverses onto their concrete images, because these states are already normal. On the dense product vectors define
\[
V(a\Omega_\alpha\otimes b\Omega_\beta)=ab\Omega_\rho.
\]
For two such vectors, commutation and SS3.1 give
\[
\rho((ab)^*a'b')
=\rho(a^*a'b^*b')
=\alpha(a^*a')\beta(b^*b').
\]
For the Hilbert tensor construction itself, expand the first-leg vectors of any finite tensor sum in an orthonormal basis of their finite-dimensional span. Its squared norm is the sum of the squared norms of the resulting second-leg coefficients. This proves positivity and nondegeneracy of the elementary product inner product. CF's Hilbert completion gives the whole tensor space. Applying this expansion in each leg separately proves the bounds for the two tensor leg actions and their adjoints. Expanding SS3.1 on finite sums now proves isometry and that \(V\) respects every null vector relation.

The map is onto. Products span a unital star algebra because the two legs commute, and its generated von Neumann algebra is \(M\). BD gives bounded strong approximation by its norm closure; norm approximation of each of those approximants by products then makes the product vectors dense in \(M\Omega_\rho\), hence in the cyclic GNS Hilbert space. Thus \(V\) extends to a unitary. On dense vectors it intertwines each leg action with that action in \(M\). Taking their complete von Neumann closures gives the spatial product, carried onto the whole represented \(M\). Unitary conjugation is normal by CP's entire vector-pair-series substitution, and the faithful normal GNS identifications have normal inverses. This proves the asserted whole spatial isomorphism.

The normal states needed in the nontracial summability proof can be supplied from its given dense normal-state family. If \((\psi_j)\) is such a family, \(\varphi=\sum_{j\geq1}2^{-j}\psi_j\) is a normalized normal state by predual norm completeness. It is faithful: a nonzero positive operator is detected by a positive normal vector state; norm density gives some \(\psi_j\) detecting it, and its strictly positive coefficient gives \(\varphi(x)>0\). Composing it with a faithful normal conditional expectation gives the required faithful normal state \(\rho\). The summability argument must prove that expectation's faithfulness and generation; SS3.1 does not assume them without that proof.

<a id="ss4-the-whole-stable-type-i-counterexample"></a>

## SS4. A stable factor that does not absorb \(R\)

Let \(H=\ell^2(\mathbb N)\). For each positive finite integer \(p\), finite matrix coordinates identify \(B(H)\bar\otimes M_p\) with \(B(H\otimes\mathbb C^p)\): every operator on the finite direct sum of \(p\) copies of \(H\) is exactly its finite matrix of bounded \(H\)-operators. The basis bijection \((n,j)\mapsto pn+j\), \(0\leq j<p\), gives a Hilbert unitary \(H\otimes\mathbb C^p\to H\). Conjugation therefore gives a normal isomorphism onto \(B(H)\), with normal inverse by CP. This is stability for every \(p\), including one.

The algebra is a factor: commuting with each rank-one diagonal and off-diagonal matrix unit forces every operator in its center to be one common scalar on the basis, and boundedness extends that scalar action to all vectors. Its predual is separable by CP's trace-class/vector-pair model on the separable \(H\). The normal state \(\sum_{n\geq0}2^{-n-1}\omega_{\delta_n}\) is faithful, since a positive operator annihilating all its basis square masses is zero.

[CQ6's complete rank-one/minimal-projection argument](central-sequence-quotient-and-lifting-inputs.md#cq6-minimal-projections-test-centrality) consequently gives \(B(H)_\omega=\mathbb C\) for every free ultrafilter. The absorption equivalence in the main lesson rules out strong stability. This supplies the specified example at its full finite amplification and scalar quotient scope.

## Combining the finite and infinite constructions

The main summability theorems construct the limit expectations, prove faithfulness from their converging tails, establish generation by the two commuting algebras, and prove the normal product-state identity needed by SS3. Finite-head quotient removal then lets each exact coordinate lift be taken inside the preceding head's relative commutant. These constructions combine SS0–4 into the full tensor-absorption argument.
