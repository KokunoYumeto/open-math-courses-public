# Normal automorphism transport and Bernoulli fixed algebras

*Programme exposition: CC0-1.0 to the extent of rights held. Human-source terms remain separate.*

The [centrally trivial automorphism lesson](../src/centrally-trivial-automorphisms-and-decreasing-afd-factors.md) uses general factors with separable predual, an arbitrary finite-factor displacement argument, and two different Bernoulli index groups. The finite group supplies noncommuting outer classes. The infinite group supplies decreasing fixed algebras with scalar intersection. We prove the needed constructions at those full scopes.

The complete earlier inputs are CF, CP and BD, [NT1–2 and the dyadic model FG2](central-sequence-foundations.md), [PC/FCT comparison and the normal finite trace](central-finite-trace-inputs.md), [AF1–5](central-afd-uniqueness-inputs.md), [FH0's normality and uniqueness of finite-factor tracial states](fullness-hypercentrality-and-tail-inputs.md#fh0-normality-of-factor-tracial-states), and [SS0–3's exact coordinates, whole variable product and spatial splitting](strong-stability-matrix-and-product-inputs.md). Inner products are linear in the second variable.

<a id="ct0-normal-transport-and-automorphism-topology"></a>

## CT0. Normal transport, countable tests and the unitary action

Let \(\gamma\) be a normal automorphism of a von Neumann algebra \(M\). Precomposition preserves \(M_*\), its norm and positivity. For \(x,z\in M\),
\[
[\gamma(x),\psi](\gamma(z))=[x,\psi\gamma](z),
\qquad [x,\psi](z)=\psi(zx)-\psi(xz).
\tag{CT0.1}
\]
Since \(\gamma\) bijects the unit ball, the commutator norms agree. Thus \(\gamma\) and its inverse preserve bounded centralizing sequences, ordinarily or along any free ultrafilter. For each positive normal functional, its two square tests on \(\gamma(x)\) are the corresponding tests on \(x\) with functional precomposed by \(\gamma\). This proves preservation of bounded intrinsic strong* convergence. NT2 converts them to a faithful-state test whenever that state is used.

For \(M_*\) separable, choose a countable norm-dense sequence in its unit ball. Pointwise norm convergence on this family is equivalent to pointwise norm convergence on every normal functional, because every precomposition operator is an isometry. A metric formed by the sum of \(2^{-j}\) times each test distance truncated at one induces this topology. Its rational-radius balls give a countable neighborhood basis at each automorphism. The dense-state family may also be used: NT1's four positive normal functionals and normalization to states give the same dense linear span.

Group composition and inversion are continuous in this topology. Indeed the precomposition maps are surjective isometries of the Banach space \(M_*\). For isometries \(A_n\to A\), \(B_n\to B\) pointwise,
\[
\|A_nB_n\xi-AB\xi\|
\leq\|B_n\xi-B\xi\|+\|(A_n-A)B\xi\|\to0.
\]
Also
\(\|A_n^{-1}\xi-A^{-1}\xi\|=\|\xi-A_nA^{-1}\xi\|\to0\).
These estimates apply to nets as well. Normality of the subgroup of inner automorphisms follows from
\(\gamma\operatorname{Ad}(u)\gamma^{-1}=\operatorname{Ad}(\gamma(u))\); continuity then makes its closure a normal subgroup. Its abstract quotient by the inner subgroup is consequently defined even when the inner subgroup is not closed.

For a unitary \(u\), fixed multiplication by \(u^*\) bijects the operator unit ball and gives
\[
\|\psi\operatorname{Ad}(u)-\psi\|=\|[u,\psi]\|.
\tag{CT0.2}
\]
If \(u_n\to u\) strong*, then their inner automorphisms converge in this topology. CP expresses normal functionals as norm-summable vector-pair series. On each pair, conjugation replaces the vectors by \(u_n^*\xi,u_n^*\eta\), which converge in Hilbert norm. The pairing difference on the unit ball is bounded by the changed-vector norm times the other vector norm. Finite truncation and the uniform precomposition norm give convergence of every normal functional. This is the inner-implementation continuity used with the already complete strong* unitary metric.

Conversely, \(u\)-convergence \(\beta_i\to\beta\) of automorphisms gives pointwise strong* convergence. For fixed \(x\), expand the square of \(\beta_i(x)-\beta(x)\) under a positive normal \(\varphi\). Its first square term tests \(\beta_i(x^*x)\); the two cross terms test \(\beta_i(x)\) by fixed normal multiplier functionals. Every term converges by the predual topology to its \(\beta\)-value, so the whole square tends to zero. Apply the same argument to \(x^*\) for the other square. This argument does not assert a continuity property of the map from automorphisms to an ultrafilter quotient.

Finally \(\gamma\) induces an automorphism on \(M_\omega\) whenever the complete quotient construction applies: CT0.1 preserves \(C_\omega\), the two square tests preserve \(J_\omega\), and the inverse gives bijectivity of the induced star map. Scalar ultraweak limits are preserved by normality and its predual tests. Hence the quotient trace is preserved. SS1 proves whole-domain normality of this induced map and its inverse.

<a id="ct1-matrix-implementation-and-approximate-innerness"></a>

## CT1. Finite matrix implementation and every automorphism of \(R\)

In a finite factor, FH0 proves that any normalized tracial state is the canonical faithful normal trace \(\tau\). Thus every normal automorphism \(\alpha\) preserves it: \(\tau\alpha\) is another normalized tracial state. This uses neither separability nor an additional normality assumption on a trace originally specified only as tracial.

For a unital \(D\cong M_d\) with units \(e_{ij}\), let \(f_{ij}=\alpha(e_{ij})\). Each family has diagonal trace \(1/d\), since the diagonals are equivalent and sum to one. FCT7 therefore gives \(v\) with \(v^*v=e_{11}\), \(vv^*=f_{11}\). The exact finite sum
\[
w=\sum_i f_{i1}ve_{1i}
\tag{CT1.1}
\]
has \(w^*w=\sum_i e_{ii}=1\) and \(ww^*=\sum_i f_{ii}=1\). Multiplying its indices gives \(we_{ij}w^*=f_{ij}\). This is a complete implementation on the whole \(D\).

Now use the complete dyadic \(R\), its increasing \(D_n\), and the normal trace projections \(P_n:R\to D_n\) from AF1. Their trace-vector orthogonal projections give \(\|P_n(x)-x\|_2\to0\), with \(\|P_n(x)\|\leq\|x\|\). Choose \(w_n\) by CT1.1 for \(\alpha|_{D_n}\), and let \(\gamma_n=\operatorname{Ad}(w_n)\). For \(n\geq k\),
\[
\|\gamma_n(x)-\alpha(x)\|_2
\leq2\|x-P_k(x)\|_2,
\]
because they agree on \(D_k\) and both preserve the trace norm. Thus \(\gamma_n(x)\to\alpha(x)\) in trace norm for every \(x\). Their inverses also converge at every \(x\):
\[
\|\gamma_n^{-1}(x)-\alpha^{-1}(x)\|_2
=\|x-\gamma_n(\alpha^{-1}(x))\|_2\to0.
\tag{CT1.2}
\]

To prove the full \(u\)-convergence, not only bounded-operator convergence, take the normal functionals
\(\rho_{a,b}(x)=\tau(a^*xb)\), \(a,b\in R\). CP's faithful normal trace representation makes their span predual norm dense: truncate any vector-pair series and approximate its vectors by bounded trace vectors. Trace preservation gives
\[
\rho_{a,b}\gamma_n(x)
=\tau(\gamma_n^{-1}(a)^*x\gamma_n^{-1}(b)).
\]
On \(\|x\|\leq1\), the difference from \(\rho_{a,b}\alpha\) is at most
\[
\|\gamma_n^{-1}(a)-\alpha^{-1}(a)\|_2\,\|b\|_2
+\|a\|_2\,\|\gamma_n^{-1}(b)-\alpha^{-1}(b)\|_2.
\]
Scalar trace Schwarz proves this bound. CT1.2 makes it vanish; predual density and isometry extend it to every normal functional. Therefore every automorphism of \(R\) is approximately inner.

<a id="ct2-tensor-relative-commutant-and-normal-tests"></a>

## CT2. The tensor relative commutant and topology transport

Let \(N\) be any nonzero factor, normally represented on \(H\), and let \(R\) be faithfully normally represented on \(K\). In the concrete spatial product,
\[
(N\otimes1)'\cap(N\bar\otimes R)=1\otimes R.
\tag{CT2.1}
\]
Here is a direct whole-operator proof. For \(X\in N\bar\otimes R\), compression between fixed second-leg vectors \(\xi,\eta\) gives an operator \(X_{\xi,\eta}\) on \(H\). It commutes with \(N'\), since \(X\) commutes with \(N'\otimes1\); hence \(X_{\xi,\eta}\in N''=N\). If \(X\) also commutes with \(N\otimes1\), every such coefficient lies in \(Z(N)=\mathbb C\).

Choose a unit first-leg vector \(h_0\). Compression between \(h_0,h_0\) defines a bounded \(T\in B(K)\), with \(\|T\|\leq\|X\|\). The scalar coefficient identities give every elementary matrix coefficient of \(X\) equal to that of \(1\otimes T\); density of finite tensor vectors proves equality of the whole operators. Since \(X\) commutes with \(1\otimes R'\), \(T\in R''=R\). The converse inclusion is direct. SS3 supplies the complete Hilbert tensor construction used for these vector compressions.

For topology transport assume \(N\) has a faithful normal state, as it does in the general-factor application with separable predual. If \(\gamma_n\to\gamma\) in the \(u\)-topology on \(R\), then
\(\operatorname{id}_N\otimes\gamma_n\to\operatorname{id}_N\otimes\gamma\) in that topology on \(N\bar\otimes R\). The normal tensor maps exist on the whole product: represent \(N\) by a faithful normal state and \(R\) by its preserved faithful normal trace, apply the trace-GNS unitary implementing \(\gamma\) on the second leg and conjugate. Its normal inverse follows from CP and the faithful normal GNS identifications. The general-factor application has separable predual and such a faithful normal state, as NT2 proves.

For the convergence assertion, finite sums of elementary normal tensor functionals are predual norm dense by CP: truncate a vector-pair series and approximate each vector by finite tensors. Their elementary norm bound is \(\|\eta\otimes\zeta\|\leq\|\eta\|\|\zeta\|\), proved by taking almost norm-minimizing trace-class extensions to each represented \(B(H)\) and tensoring their summable vector-pair series, then letting the norm errors tend to zero. Thus
\[
\|(\eta\otimes\zeta)(\operatorname{id}\otimes\gamma_n)
-(\eta\otimes\zeta)(\operatorname{id}\otimes\gamma)\|
\leq\|\eta\|\,\|\zeta\gamma_n-\zeta\gamma\|\to0.
\]
The uniform precomposition norm makes the same conclusion hold on the entire predual. If \(\gamma_n=\operatorname{Ad}(w_n)\), their tensor maps are implemented by \(1\otimes w_n\).

<a id="ct3-entire-bernoulli-product-and-outerness"></a>

## CT3. Bernoulli products for finite and countably infinite groups

Let \(K_0\) be a nonempty finite or countably infinite discrete group. For each \(h\in K_0\) take a dyadic \(R_h\), with the same identified finite heads \(D_r\). Construct the complete product \(B\) by placing one \(M_2\) at every index in \(K_0\times\mathbb N\). This index set is countably infinite even when \(K_0\) is finite. SS2 constructs its faithful normal product trace representation and identifies its whole closure with \(R\).

Grouping the legs at a fixed \(h\) gives \(R_h\subseteq B\). On local trace vectors every regrouping or countable permutation preserves all finite product inner products. It consequently extends to a Hilbert unitary, intertwining the local actions and their BD closures normally in both directions. This identifies \(B\) with the complete product of the \(R_h\)'s. A finite set \(F\subseteq K_0\) supports its corresponding whole finite product. Trace factorization for operators on disjoint supports follows first on finite matrix legs and then by normality in each factor on the whole supported algebras.

The left Bernoulli convention is
\[
\alpha_g\left(\bigotimes_h x_h\right)
=\bigotimes_h x_{g^{-1}h}.
\tag{CT3.1}
\]
It sends an operator formerly in coordinate \(h\) to coordinate \(gh\). On finite products its compositions satisfy \(\alpha_g\alpha_k=\alpha_{gk}\), preserve multiplication, adjoints and the product trace, and have inverse \(\alpha_{g^{-1}}\). The trace-vector unitary extends them to the whole \(B\); CP's unitary-conjugation tests and the faithful normal GNS inverse prove normality. The group identities extend by BD.

In coordinate \(e\), choose \(a_r=e_{11}-e_{22}\) at its \(r\)-th dyadic leg, with identities at the other legs. These are trace-zero self-adjoint unitaries. Write \(\widetilde a_r\) for their images in \(B\). Each fixed finite matrix stage commutes with them eventually. For \(x\in B\), bounded finite-stage trace approximation therefore gives
\(\|[\widetilde a_r,x]\|_2\leq2\|x-x_0\|_2\) at all sufficiently large \(r\). Adjoint estimates are the same; their trace functional commutator is zero. The complete tracial centrality criterion makes this an ordinary centralizing sequence.

For \(g\ne e\), \(\alpha_g(\widetilde a_r)\) has distinct coordinate support \(g\). Both unitaries have trace zero and trace square norm one. Product trace factorization yields
\[
\|\alpha_g(\widetilde a_r)-\widetilde a_r\|_2^2=2.
\tag{CT3.2}
\]
Every inner automorphism moves a bounded centralizing sequence by a strong*-zero difference, hence a trace-norm-zero difference here. CT3.2 rules this out. Thus each nonidentity \(\alpha_g\) is outer, for finite groups as well as infinite ones. In particular \(K_0=S_3\) supplies a faithful everywhere-outer action on an algebra normally isomorphic to \(R\).

<a id="ct4-irreducible-diffuse-afd-finite-fixed-algebras"></a>

## CT4. Direct irreducibility and type of the finite fixed algebras

Now let \(K_0\) be countably infinite and \(H_0\subseteq K_0\) a finite subgroup, \(m=|H_0|\). Set \(N=B^{H_0}\). It is a von Neumann subalgebra, since each fixed equation is ultraweakly closed. The finite map
\[
E_{H_0}(x)=m^{-1}\sum_{h\in H_0}\alpha_h(x)
\]
is normal, unital, completely positive, trace-preserving, \(N\)-bimodular and has exactly range \(N\). It is a trace \(2\)-contraction by the finite triangle inequality.

We prove \(N'\cap B=\mathbb C\) without a crossed-product assertion. Fix \(x\in N'\cap B\) and a finite-support operator \(a\). Choose a finite matrix-stage \(x_L\), supported on finite \(L\), with \(\|x-x_L\|_2<\delta\). Let \(F\) support \(a\). Infinitude permits a \(k\notin H_0(L\cup F)\); thus all distinct coordinates \(hk\), \(h\in H_0\), lie outside \(L\cup H_0F\).

Take a trace-zero unitary \(b\) in coordinate \(k\), and put \(b_h=\alpha_h(b)\). The operator
\[
t=\sum_{h\in H_0}\alpha_h(a)b_h
\]
is fixed by \(H_0\), since each group element permutes the summands. Its norm is at most \(m\|a\|\), and \([x,t]=0\). The \(b_h\)'s commute with \(x_L\) and with every coefficient \([x_L,\alpha_j(a)]\). Their mutually disjoint trace-zero supports give \(\tau(b_h^*b_j)=\delta_{hj}\). Full product trace factorization therefore proves
\[
\|[x_L,t]\|_2^2
=\sum_{h\in H_0}\|[x_L,\alpha_h(a)]\|_2^2.
\tag{CT4.1}
\]
Meanwhile \(\|[x_L,t]\|_2\leq2m\|a\|\delta\). The identity-index term in CT4.1 gives
\[
\|[x,a]\|_2\leq2(m+1)\|a\|\delta.
\]
Let \(\delta\) decrease to zero. Hence \(x\) commutes with all finite-support operators, including the generating finite matrix stages. Fixed multiplication and BD then make it commute with \(B\). The complete product is a factor, so \(x\) is scalar.

Thus \(N\) is a factor, since \(Z(N)\subseteq N'\cap B\). Its restricted trace is faithful normal, making it finite. It has no minimal projection. In one orbit \(H_0k\), take the diagonal tensor cells of \(\bigotimes_{h\in H_0}D_r\), \(d=2^r\). Their \(d^m\) equal trace masses are \(d^{-m}\). The sum of the cells in each \(H_0\)-orbit is a nonzero fixed projection, of trace at most \(m/d^m\), and these sums partition the unit. If \(q\in N\) were minimal, choose \(r\) with \(m/d^m<\tau(q)\). FCT7 within the finite factor \(N\) places a nonzero copy of one orbit-sum projection under \(q\), with strictly smaller trace, a contradiction. PC4/FH1 consequently makes \(N\) type \(\mathrm{II}_1\).

For AFD, enumerate \(K_0\) by \(k_1,k_2,\ldots\), put \(F_r=H_0\{k_1,\ldots,k_r\}\), and let
\[
B_r=\bigotimes_{h\in F_r}D_r.
\]
These are increasing finite full matrix algebras, invariant under \(H_0\), and their union contains every finite matrix leg eventually. AF1's trace projections onto \(B_r\) give bounded \(x_r\in B_r\) with \(x_r\to x\) in trace norm. At \(x\in N\), their finite averages belong to the finite-dimensional \(B_r^{H_0}\), remain bounded and converge in trace norm to \(x\). NT2 gives bounded strong* convergence; therefore these fixed stages generate \(N\), proving AFD.

Its predual is separable. For \(\eta\in N_*\), the map \(\eta\mapsto\eta E_{H_0}\) embeds it isometrically in \(B_*\), because the finite expectation fixes its unit ball. The image is closed, and the complete countable product has separable predual. AF5 now identifies \(N\) normally with \(R\). The argument includes the trivial subgroup, and uses infinitude only where a remote coordinate is required.

<a id="ct5-compact-twisted-orbit-minimization"></a>

## CT5. Compact minimization of a twisted unitary orbit

Let \(M\) be any \(\mathrm{II}_1\) factor, without separability, with its canonical normal trace from FH0. For a normal automorphism \(\alpha\) and a unital matrix factor \(D\), put \(C=D'\cap M\) and
\(d=\sup_{u\in\mathcal U(C)}\|\alpha(u)-u\|_2<1\).
The orbit \(u\alpha(u^*)\) lies in the operator unit ball and the trace ball of radius \(d\) about \(1\). Let \(K\) be its ultraweakly closed convex hull.

CP/CF makes the bounded operator ball ultraweakly compact. The scalar formula
\[
\|z\|_2=\sup_{\substack{a\in M\\\|a\|_2\leq1}}|\tau(a^*z)|
\]
follows from Schwarz and \(a=z/\|z\|_2\) for nonzero \(z\). Each pairing is normal; hence centered trace balls are ultraweakly closed. Consequently \(K\) is compact and still lies in the radius-\(d\) ball about \(1\); it excludes zero.

If \(s=\inf_{z\in K}\|z\|_2\), the compact nonempty nested sublevel sets with bounds \(s+1/n\) have nonempty intersection. They supply a least-norm \(y\in K\). If two points had that norm, their midpoint's squared norm would be \(s^2\) minus one quarter of their squared distance. Trace faithfulness and convexity therefore prove uniqueness. No Hilbert convex-set projection theorem is needed.

For \(v\in\mathcal U(C)\), the normal linear map \(z\mapsto vz\alpha(v^*)\) bijects \(K\) and is a trace-norm isometry. It sends the orbit element at \(u\) to the one at \(vu\), with inverse the map at \(v^*\). Uniqueness fixes \(y\). Since \(0\notin K\), \(y\ne0\), and the resulting identity is
\[
y\alpha(v)=vy\qquad(v\in\mathcal U(C)).
\]
NT1's complete four-unitary span extends it to all \(v\in C\). CT1's matrix implementer and SS0's coefficients finish the innerness argument in the main lesson.
