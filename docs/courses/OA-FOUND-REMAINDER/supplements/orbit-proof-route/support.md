<span id="precise-bridges-for-the-coefficient-route"></span>
# Precise bridges for the coefficient route

The lemmas below supply the coefficient-route arguments for the crossed-product constructions. Each proof states its mathematical prerequisites.

<span id="orbit-bridge-fourier--smooth-compact-support-fourier-inversion"></span>
<span id="ORBIT-BRIDGE-FOURIER"></span>
<span id="orbit-bridge-fourier"></span>
## ORBIT-BRIDGE-FOURIER — Smooth compact-support Fourier inversion

Let \(k\in C_c^\infty(\mathbb R)\) and define
\[
\widehat k(t)=\frac1{2\pi}\int_{\mathbb R}e^{-itp}k(p)\,dp.
\]
Then \(\widehat k\in L^1(\mathbb R)\) and
\[
k(p)=\int_{\mathbb R}\widehat k(t)e^{itp}\,dt.
\]
For a self-adjoint operator P on an arbitrary Hilbert space,
\[
k(P)\xi=\int_{\mathbb R}\widehat k(t)e^{itP}\xi\,dt
\quad(\xi\in H),\qquad \|k(P)\|\leq\|k\|_\infty.
\]

The exact inputs are scalar Lebesgue integration, Fubini for absolute integrals, dominated convergence, integration by parts, and the Gaussian transform proved in MA03; for the operator conclusion they are the arbitrary-Hilbert-space finite scalar spectral measures of SK04–07. No general Fourier inversion or measurable-operator-field theorem is assumed.

**Proof.** The integral defining the transform is continuous and bounded by \(\|k\|_1/(2\pi)\). Twice integrating by parts, with zero boundary terms because k and its derivatives have compact support, gives
\[
|\widehat k(t)|\leq\frac{\|k''\|_1}{2\pi |t|^2}\quad(t\ne0).
\]
Use the first bound on \([-1,1]\) and the second on its complement to prove integrability.

For \(\varepsilon>0\), absolute Fubini and the Gaussian transform give
\[
\begin{aligned}
I_\varepsilon(p)
&=\int\widehat k(t)e^{itp}e^{-\varepsilon t^2}\,dt\\
&=\int k(u)\frac{e^{-(p-u)^2/(4\varepsilon)}}{2\sqrt{\pi\varepsilon}}\,du.
\end{aligned}
\]
The positive Gaussian kernel in the last integral has integral one. For every fixed positive a its integral over \(|u-p|\geq a\) tends to zero by scaling and the integrable Gaussian tail. The function k is bounded and uniformly continuous. Splitting the last integral at \(|u-p|=a\), first choosing a by uniform continuity and then choosing epsilon by the tail estimate, proves \(I_\varepsilon(p)\to k(p)\), in fact uniformly in p. Dominated convergence on the first integral, with majorant \(|\widehat k|\), proves the scalar inversion formula.

For each fixed vector xi, \(t\mapsto e^{itP}\xi\) is norm continuous. Its image on bounded time intervals is norm compact and therefore separable, and the union of these images over integer intervals is separable. The integrable norm bound \(|\widehat k(t)|\|\xi\|\) thus supplies a Hilbert-space Bochner integral. Pair it with any eta. The complex spectral measure \(\langle E_P(\cdot)\xi,\eta\rangle\) has finite total variation, so absolute Fubini and the scalar inversion formula identify the pairing with \(\langle k(P)\xi,\eta\rangle\). Equality of all pairings proves the operator formula. The norm bound is the bounded spectral-calculus bound. This argument concerns each fixed vector and imposes no separability hypothesis on H. ∎

<span id="orbit-bridge-spectral-reduction--the-spectral-projections-follow-the-unitary-group"></span>
<span id="ORBIT-BRIDGE-SPECTRAL-REDUCTION"></span>
<span id="orbit-bridge-spectral-reduction"></span>
## ORBIT-BRIDGE-SPECTRAL-REDUCTION — The spectral projections follow the unitary group

Let \(U_t=e^{itP}\) be a strongly continuous unitary group on an arbitrary Hilbert space. If a closed subspace K reduces every U_t, then K reduces every spectral projection of P.

The exact inputs are Stone's theorem SG04, its two vector Laplace resolvents SG13–14, and the bounded Borel calculus/real change of variable of SK04/SK06/SK08. No group Fourier transform is assumed.

**Proof.** Let q be the projection onto K. Reduction means \(qU_t=U_tq\) for all real t. The vector-integral formulas
\[
(P-i)^{-1}\xi=i\int_0^\infty e^{-t}U_{-t}\xi\,dt,
\qquad
(P+i)^{-1}\xi=-i\int_0^\infty e^{-t}U_t\xi\,dt
\]
therefore show that q commutes with both resolvents, because bounded q passes through their norm-convergent vector integrals. It commutes with the Cayley unitary
\[
C=(P-i)(P+i)^{-1}=1-2i(P+i)^{-1}
\]
and with its adjoint. SK08's bounded-normal commutation argument gives commutation with every Borel spectral projection of C. The inverse real Cayley change of variable in SK06 transports those projections to every \(E_P(B)\), for Borel \(B\subset\mathbb R\). The Cayley point 1 has zero spectral projection for this self-adjoint P and creates no extra summand. Thus q commutes with every \(E_P(B)\), which is precisely reduction. ∎

Applied to \(P\oplus P\), this proves the exact reduction step used in FLOW07 G1. FLOW07's graph-localization proof then gives the graph core for every spectral Borel function, including the half-power used by FLOW12 M25. The original density, imaginary-power invariance and half-power domain inclusion still have to be supplied by FLOW09/12.

<span id="orbit-bridge-covariant-topology--the-given-implementation-supplies-action-continuity"></span>
<span id="ORBIT-BRIDGE-COVARIANT-TOPOLOGY"></span>
<span id="orbit-bridge-covariant-topology"></span>
## ORBIT-BRIDGE-COVARIANT-TOPOLOGY — The given implementation supplies action continuity

Let \(\rho:M\to B(K)\) be faithful normal unital and let the strongly continuous unitary representation V implement a normal automorphism action \(\alpha_s\). Then every predual orbit \(s\mapsto\omega\circ\alpha_s\) is norm continuous. Together with FLOW11 TOP.JOINT's elementary positive-seminorm argument, this gives joint sigma-strong-star continuity on norm-bounded varying coefficients. It uses no Banach weak-compact-convex-hull theorem.

**Proof.** WA Proposition 12.1 identifies M normally with its concrete image. The concrete-predual vector-pair series gives
\[
\omega(x)=\sum_n\langle\rho(x)\xi_n,\eta_n\rangle,
\qquad \sum_n\|\xi_n\|\|\eta_n\|<\infty.
\]
Covariance gives the same series for \(\omega\circ\alpha_s\), with vectors \(V_s^*\xi_n,V_s^*\eta_n\). For a single pair, the functional norm difference at s and r is at most
\[
\|(V_s^*-V_r^*)\xi_n\|\|\eta_n\|
+\|\xi_n\|\|(V_s^*-V_r^*)\eta_n\|.
\]
Finite sums tend to zero by strong continuity. The remaining tail of the difference has norm at most \(2\sum_{n>N}\|\xi_n\|\|\eta_n\|\), uniformly in s and r. First discard this tail and then pass to the limit in the finite head. This proves norm continuity. The normal-image identification transports the estimate to \(M_*\). ∎

This hypothesis is already part of BF77; in BF75 its canonical implementer U is strongly continuous. For a nonfaithful normal unital covariant representation, pass to its invariant central-kernel quotient, which is faithfully represented with the same V. Thus this choice preserves the stated general commutant theorem. It does not purport to replace FLOW11's theorem for actions initially given without a strongly continuous implementation.

<span id="orbit-bridge-haar-masa--the-local-haar-multiplication-algebra-and-its-standard-form"></span>
<span id="ORBIT-BRIDGE-HAAR-MASA"></span>
<span id="orbit-bridge-haar-masa"></span>
## ORBIT-BRIDGE-HAAR-MASA — The local Haar multiplication algebra and its standard form

Use the completed locally determined Haar measure \(\mu_\ell\) of current HR-09, not an identification with the global outer-regular \(L^\infty\) space. Write G as the disjoint open sigma compact cosets D of HR-08. Then
\[
L^2(G)=\bigoplus_D L^2(D),\qquad
\mathcal D=L^\infty(G,\mu_\ell)=\prod_D L^\infty(D).
\]
Multiplication represents \(\mathcal D\) faithfully and normally on \(L^2(G)\), and \(\mathcal D'=\mathcal D\). The multiplication operators from \(C_c(G)\) generate \(\mathcal D\). The integration weight \(\mu_\ell\) is normal faithful semifinite; its GNS space is \(L^2(G)\), its closed Tomita involution is complex conjugation C on all of that space, and its modular operator is 1.

**Proof.** On each sigma-finite coset choose measurable finite-measure sets increasing to D and a function \(a_D\in L^2(D)\) strictly positive almost everywhere, for example a sum of positive multiples of their indicators with summable L2 norms. The span of \(fa_D\), \(f\in L^\infty(D)\), is dense: truncate a target vector to where its ratio to \(a_D\) is bounded and apply scalar dominated convergence. If T commutes with every multiplication on D, let \(b=Ta_D\). Commutation with indicators gives
\(\|1_Eb\|_2\leq\|T\|\|1_Ea_D\|_2\) for every measurable E. Testing where \(|b|>(\|T\|+\epsilon)a_D\), and then using the countable finite-measure exhaustion, shows \(|b|\leq\|T\|a_D\) almost everywhere. Thus \(h=b/a_D\in L^\infty(D)\); on the dense vectors \(fa_D\), T equals multiplication by h. Globally a commuting T also commutes with the projections \(1_D\), so it is the direct sum of these multipliers. Its uniform bound puts the family in \(\mathcal D\). This proves the MASA assertion.

To check generation by \(C_c(G)\), let T commute with all its multiplication operators. For each compact \(K\subset D\), choose a cutoff \(0\leq h_K\leq1\) within D that equals one on K, and direct the compact sets by inclusion. For each fixed \(\xi\in L^2(D)\), finite-density regularity in HR-03 gives a compact K with \(\int_{D\setminus K}|\xi|^2<\epsilon^2\). Every subsequent cutoff has \(\|(1-h_L)\xi\|_2<\epsilon\), because it is one on K. These explicit tail estimates prove strong convergence to \(1_D\); no dominated-convergence theorem for an arbitrary pointwise net is used. Thus T commutes with \(1_D\). On D, HR-03 gives, for each measurable E, compact cutoffs \(0\leq h_n\leq1\) approximating \(1_E\) in L2 on each finite-measure member of an exhaustion. A diagonal choice and a subsequence give convergence almost everywhere on D; sequential bounded convergence against each fixed L2 vector gives strong convergence to \(1_E\). Consequently T commutes with all projections of \(L^\infty(D)\), hence all bounded simple functions and their bounded limits. The preceding paragraph identifies T as a multiplier. Bicommutants now prove the asserted generation. The cutoff choice on finite pieces uses only completed finite-set regularity; it does not assume D metrizable.

Faithfulness of multiplication follows by testing finite-measure subsets of a nonzero multiplier's support. For normality, on a sigma-finite coset the integral of a nonnegative function is the supremum of its bounded normal integrals over a finite-measure exhaustion; these finite integrals are normal vector functionals on the multiplication algebra. On G take additionally the supremum over finite sets of cosets. Suprema of these positive functionals preserve bounded increasing positive suprema, so the integration weight is normal. Faithfulness is the zero-integral criterion. Finite-coset finite-measure truncations of a positive function, followed by value truncation, increase to it and have finite integrals; thus the weight is semifinite. Its finite left ideal is \(L^\infty\cap L^2\), with GNS map the usual function class. This is dense by HR-03 and has involution f to its complex conjugate. The restriction of C to this dense star ideal closes to C on all of L2, because C is bounded. Its polar positive factor is 1. ∎

The section/tensor identification at arbitrary Hilbert dimension is already the full proof of current group-completions Proposition 4.2, and vector Fubini is Proposition 4.3. HR-05 supplies the full Radon-product proof with its qualified Borel carrier statement; continuous compact-support and nonnegative lower-semicontinuous integrands are handled by HR-05a–c and its approximation argument. These exports exactly fit FLOW08/09/12; no unrestricted product-Borel equality is imported.

<span id="orbit-bridge-tensor-commutant--the-particular-tensor-commutant-used-by-flow10"></span>
<span id="ORBIT-BRIDGE-TENSOR-COMMUTANT"></span>
<span id="orbit-bridge-tensor-commutant"></span>
## ORBIT-BRIDGE-TENSOR-COMMUTANT — The particular tensor commutant used by FLOW10

In the common weight-constructed standard form of M, let J be its conjugation, and let \(\mathcal D\) be the preceding Haar multiplication algebra with conjugation C. Then
\[
(M\bar\otimes\mathcal D)'=M'\bar\otimes\mathcal D,
\qquad (M'\bar\otimes\mathcal D)'=M\bar\otimes\mathcal D.
\]

**Proof.** TG-04 constructs the tensor left Hilbert algebra of an arbitrary nsf weight of M and the nsf Haar integration weight. Its left algebra is \(M\bar\otimes\mathcal D\), and its exact closed polar conjugation is \(J\otimes C\). Apply the general left-Hilbert-algebra theorem MF-05. Conjugating elementary generators and taking their strong closures gives
\((J\otimes C)(M\bar\otimes\mathcal D)(J\otimes C)=M'\bar\otimes\mathcal D\), since \(JMJ=M'\) and \(C\mathcal DC=\mathcal D\). MF-05 identifies this with the commutant. Take the commutant once more and use the bicommutant theorem to obtain the second equality. ∎

This uses TG-04's full graph tensor construction, not merely TG-03's representation comparison or a finite-dimensional example. It depends on the same MF-05 exact revision already selected for BF75.

<span id="orbit-bridge-amplification-slice--the-tensor-facts-in-bf77-e8e9"></span>
<span id="ORBIT-BRIDGE-AMPLIFICATION-SLICE"></span>
<span id="orbit-bridge-amplification-slice"></span>
## ORBIT-BRIDGE-AMPLIFICATION-SLICE — The tensor facts in BF77 E8–E9

For arbitrary Hilbert L and a concrete von Neumann algebra A on K,
\((1_L\otimes A)'=B(L)\bar\otimes A'\). For a unit e in L, the vector slice of \(B(L)\bar\otimes A\) belongs to A and is normal.

**Proof.** Choose an arbitrary orthonormal basis of L. Matrix entries of an operator commuting with \(1\otimes A\) lie in A'. Compress to finite basis subsets: each compression is a finite matrix over A' and hence belongs to \(B(L)\bar\otimes A'\). These compressions converge strongly to the operator, over the directed set of finite subsets. The algebra is strongly closed; this proves the nontrivial inclusion. Elementary tensors commute with \(1\otimes A\), and taking their strong closure gives the reverse inclusion. No basis enumeration is used.

For the slice let \(W:K\to L\otimes K\) be \(W\xi=e\otimes\xi\). The slice is \(W^*XW\). It belongs to A: for \(y\in A'\), \(Wy=(1\otimes y)W\), and every X in the tensor algebra commutes with \(1\otimes y\). Hence \(W^*XW\) commutes with A', so is in A. Its pairings are vector pairings \(\langle X(e\otimes\xi),e\otimes\eta\rangle\), and the same formula for square-summable vector pairs proves ultraweak continuity and normality on arbitrary L and K. Finally the slice of \(1\otimes x\) is x, which is precisely the removal of amplification in E9. ∎
