# Trace-preserving finite models

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Self-checked by the writing AI. New original text: public domain (CC0).*

A useful finite record has two jobs: reproduce the ambient trace exactly and represent the chosen unitary observations accurately. We start with the second job and the error allowed when a matrix contraction is replaced by a unitary. We then design a rational record by mixing reconstruction with state preparation, construct the two trace-preserving maps, and check that their composite recovers the observations.

Throughout, \(M\) has a faithful normal tracial state \(\tau\), and \(\tau_m=\operatorname{Tr}/m\). No factor or separability assumption is needed. Such an algebra is finite: if \(v^*v=1\), traciality gives \(\tau(1-vv^*)=0\), and faithfulness forces \(vv^*=1\). The incoming matrix models are therefore supplied by the [direct faithful-trace construction](hypertraces-finite-injectivity.md#theorem-5-1), using its trace realization, trace-retaining finite densities, scalar spatial bound and explicit matrix maps. Its stronger center-valued statements and the continuous-core construction are unnecessary here.

The [complete tracial-adjoint lesson](tracial-adjoints-and-rational-matrix-models.md) supplies finite diagonalization and matrix densities (P03), all CP and Schwarz rules (P04), the trace Hilbert completion (P05), ordinary normal trace adjoints (Lemma 1.1), the weighted Hilbert bound (Theorem 2.1), and the rational-density channel (Theorem 3.1). Their scalar and coefficient-predual inputs are the retained Sections 1–10 and CP01–06. General bounded polar decomposition is proved by [the positive-inverse argument T04a](regular-group-operator-foundations.md#t04a); Exercise 9 below proves the finite complement extension. Its closed-range projections and positive inverses are the Hilbert projection and continuous-calculus arguments of retained scalar Sections 8 and 6. For its bounded strong limits, the coefficient-series proof is direct: choose a finite prefix with small summable tail; strong convergence handles the prefix, while the uniform operator bound controls the tail. Thus a bounded strong limit is ultraweak and stays in the given ultraweakly closed algebra. These same precise elementary inputs apply to the direct faithful-trace construction. No trace-preserving conditional expectation or general Radon–Nikodym theorem is required. Unitary budgets for Theorems 2.1 and 3.1 may always be chosen below one. The normal unital model construction below supplies the topology conversion and exact unit correction used when we assemble the trace-preserving maps.

The [unitary test](#lemma-4-1) uses the state actually induced by reconstruction. The [state-preparation construction](#lemma-1-1) makes the record faithful and rational. The [trace reconstruction](#theorem-2-1) and its [ordinary adjoint](#theorem-3-1) then give both exact trace identities. The worked diagnostics include a density with a zero eigenvalue and a reconstruction that does not preserve matrix trace.

<a id="4-replacing-matrix-contractions-by-unitaries"></a>

## Test unitary observations before designing the record

A reconstruction map determines its own matrix state. The unitary replacement estimate works for that state even when reconstruction does not preserve the normalized matrix trace. This lets us decide the necessary error budget before constructing the finite record.

**Lemma 4.1.** Let \(T:M_m\to M\) be any ucp map, let \(u\in M\) be unitary and let \(y\in M_m\) be a contraction. If \(\|T(y)-u\|_2<\eta\), there is a unitary \(v\in M_m\) with
\[
\|T(v)-u\|_2<\eta+\sqrt{2\eta}.
\tag{16}
\]
Trace preservation of \(T\) is unnecessary.

**Proof.** Extend the polar partial isometry of the square matrix \(y\) to a unitary \(v\), so \(y=v|y|\). Put \(\varphi=\tau T\). Schwarz gives
\[
\begin{aligned}
\|T(v-y)\|_2^2
&\le\varphi((v-y)^*(v-y))\\
&=\varphi((1-|y|)^2)
\le1-\varphi(y^*y)
\le1-\|T(y)\|_2^2<2\eta.
\end{aligned}
\tag{17}
\]
The scalar inequality \((1-t)^2\le1-t^2\) holds for \(0\le t\le1\). For the final bound, put \(d=\|T(y)-u\|_2<\eta\). Contractivity and the reverse triangle inequality give \(0\le1-\|T(y)\|_2\le d\); hence \(1-\|T(y)\|_2^2\le2d<2\eta\). This works for every positive \(\eta\). The triangle inequality proves (16). \(\square\)

<a id="1-rationalizing-a-density-without-losing-positivity"></a>

## Design the record by mixing state preparations

**Lemma 1.1.** If \(T:M_m\to M\) is ucp, then for every \(\varepsilon>0\) there is a ucp map \(T'\) with \(\|T'-T\|<\varepsilon\) such that the density of \(\tau T'\) has strictly positive rational eigenvalues. In particular \(T'\) is faithful on positive elements.

<a id="a-state-preparation-construction"></a>

**Proof by state preparation.** Write
\[
\tau T(x)=\tau_m(hx),\qquad
h=\sum_{i=1}^m\lambda_i e_i,\qquad
\lambda_i\ge0,\quad\sum_i\lambda_i=m,
\tag{1}
\]
where the \(e_i\) are rank-one orthogonal projections summing to \(1\). Choose \(0<\alpha<\min(1,\varepsilon/2)\) and positive rational numbers \(r_i\) such that
\[
\sum_i r_i=m,\qquad r_i>(1-\alpha)\lambda_i.
\]
Such a choice is possible because the vector \(((1-\alpha)\lambda_i+\alpha)_i\) lies in this open simplex and has sum \(m\). Rational points in the sum-\(m\) hyperplane are dense: approximate the first \(m-1\) coordinates rationally and define the last by subtraction; sufficiently small errors retain all strict inequalities. For \(m=1\), take \(r_1=1\).

Put \(g=\sum_i r_i e_i\) and \(k=(g-(1-\alpha)h)/\alpha\). Then \(k>0\) and \(\tau_m(k)=1\), so \(\psi(x)=\tau_m(kx)\) is a state. The map
\[
\widetilde T(x)=(1-\alpha)T(x)+\alpha\psi(x)1
\]
is ucp, has density \(g\) under \(\tau\), and satisfies \(\|\widetilde T-T\|\le2\alpha<\varepsilon\). Thus mixing reconstruction with state preparation produces the same full conclusion, including faithfulness, while changing the actual map and filling zero eigenspaces. The congruence construction below supplies a second realization for the worked diagnostics.

### Congruence formulas for the worked diagnostics

Using the diagonalization (1), the same conclusion also has the following direct construction. Choose \(0<\delta<1\). For each positive \(\lambda_i\), choose a rational number
\[
(1-\delta)\lambda_i<q_i<\lambda_i;
\]
put \(q_i=0\) when \(\lambda_i=0\). Define
\[
b=\sum_i b_i e_i,\qquad
b_i=q_i/\lambda_i\quad(\lambda_i>0),\qquad b_i=1\quad(\lambda_i=0).
\tag{2}
\]
Thus \((1-\delta)1\le b\le1\). Set
\[
T'(x)=T(b^{1/2}xb^{1/2})+\tau_m(x)T(1-b).
\tag{3}
\]
Both summands are cp, and their values at \(1\) add to \(1\). For \(\|x\|\le1\), contractivity of \(T\) gives
\[
\|T'(x)-T(x)\|
\le2\|1-b^{1/2}\|+\|1-b\|\le3\delta.
\tag{4}
\]
Here \(\|1-b^{1/2}\|\le\delta\) follows from \(1-\sqrt t\le1-t\) on \([0,1]\).

Since \(b\) commutes with \(h\), the new density is
\[
h'=hb+\tau_m(h(1-b))1
=\sum_i(q_i+c)e_i,\qquad
c=1-\frac1m\sum_iq_i>0.
\tag{5}
\]
The number \(c\) is rational, and so are all \(q_i+c\). Strict positivity also fills every original zero eigenspace. The density remains normalized, because \(\tau_m(h')=1\). Choose \(3\delta<\varepsilon\). If \(x\ge0\) and \(T'(x)=0\), then \(\tau_m(h'x)=0\); invertibility of \(h'\) gives \(x=0\). \(\square\)

The correction in (3) changes the actual cp map as well as its density. Simply replacing \(h\) by a rational matrix would not specify a compatible positive reconstruction map.

<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="410" viewBox="0 0 1000 410" role="img" aria-label="Rational channels convert a matrix state to ordinary trace and the ordinary adjoint preserves both traces">
<title>From a weighted reconstruction to two trace-preserving maps</title>
<desc>R takes the density state phi to ordinary matrix trace, L takes that trace back, and T equals T2 composed with L. Its ordinary adjoint S equals T sharp, and both traces are preserved exactly. The displayed error budgets refer to the two distinct approximation stages.</desc>
<defs><marker id="finite-model-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8Z" fill="#345c7b"/></marker></defs>
<rect width="1000" height="410" fill="#f5f8fc"/>
<g font-family="Arial,sans-serif" fill="#19384f" text-anchor="middle">
<text x="500" y="30" font-size="23">Rational recording supplies an ordinary matrix trace</text>
<rect x="35" y="70" width="230" height="95" rx="10" fill="#e5edf8"/><text x="150" y="102" font-size="22">Mₘ, φ = τT₂</text><text x="150" y="135" font-size="18">positive rational density h</text>
<rect x="385" y="70" width="230" height="95" rx="10" fill="#edf5ee"/><text x="500" y="102" font-size="22">M_q, τ_q</text><text x="500" y="135" font-size="18">ordinary normalized trace</text>
<rect x="735" y="70" width="230" height="95" rx="10" fill="#e5edf8"/><text x="850" y="102" font-size="22">M, τ</text><text x="850" y="135" font-size="18">original faithful trace</text>
<path d="M275 90H375" stroke="#345c7b" stroke-width="2" marker-end="url(#finite-model-arrow)"/><text x="325" y="77" font-size="18">R</text>
<path d="M375 150H275" stroke="#345c7b" stroke-width="2" marker-end="url(#finite-model-arrow)"/><text x="325" y="140" font-size="18">L</text>
<path d="M625 110H725" stroke="#345c7b" stroke-width="2" marker-end="url(#finite-model-arrow)"/><text x="675" y="95" font-size="18">T = T₂L</text>
<text x="500" y="197" font-size="18">τ_qR = φ; φL = τ_q; τT = τ_q</text>
<text x="500" y="233" font-size="18">First budget: ‖T(R(x_k)) − u_k‖₂ &lt; η + 2√η (Theorem 2.1)</text>
<path d="M850 259H510" stroke="#345c7b" stroke-width="2" marker-end="url(#finite-model-arrow)"/><text x="680" y="283" font-size="19">S = T♯ : M → M_q; τ_qS = τ</text>
<text x="500" y="329" font-size="18">If ‖T(y_k) − u_k‖₂ &lt; δ, then ‖TS(u_k) − u_k‖₂ &lt; √(2δ) + δ</text>
<text x="500" y="370" font-size="17">Second budget: Theorem 3.1, the complex pairing estimate (14), and Schwarz</text>
</g>
</svg>

*Figure.* The upper loop changes the state on the finite record, while the right arrow composes its return with the perturbed reconstruction. The lower arrow is the actual ordinary trace adjoint. The two error labels use different parameters: choose the first small enough to obtain the second stage's desired \(\delta\). The formulas assert approximation of the selected unitaries and exact trace identities; they do not assert that the finite maps are algebra embeddings.

<a id="finite-unital-model-input"></a>

### Normal unital models with an explicit trace-norm budget

The direct faithful-trace theorem gives normal cpc maps \(A_i:M\to M_{m_i}\) and cpc maps \(B_i:M_{m_i}\to M\) for which \(\Phi_i=B_iA_i\) converges pointwise ultraweakly to the identity. Here cpc means completely positive and contractive. For a cp map the norm is its unit-value norm, so \(0\le A_i(1)\le1\), \(0\le B_i(1)\le1\), and \(0\le\Phi_i(1)\le1\).

Schwarz also holds for these subunital maps. Apply complete positivity to the Gram block \(\left[\begin{smallmatrix}x^*x&x^*\\x&1\end{smallmatrix}\right]\), then add the positive lower-right block \(1-\Phi_i(1)\). Sandwiching by \(\left[\begin{smallmatrix}1\\-\Phi_i(x)\end{smallmatrix}\right]\) gives \(\Phi_i(x)^*\Phi_i(x)\le\Phi_i(x^*x)\). Consequently
\[
 \|\Phi_i(x)-x\|_2^2
 \le \tau(\Phi_i(x^*x))-2\operatorname{Re}\tau(x^*\Phi_i(x))+\tau(x^*x)
 \longrightarrow0.
\tag{N1}
\]
Both tests on the right are normal: fixed multiplication preserves the coefficient predual by P02 of the tracial-adjoint lesson. Thus ultraweak convergence of these contractions gives the required \(2\)-norm convergence directly.

Put \(a_i=A_i(1)\), \(b_i=B_i(1)\), and define
\[
 A_i^u(x)=A_i(x)+\tau(x)(1-a_i),\qquad
 B_i^u(y)=B_i(y)+\tau_{m_i}(y)(1-b_i).
\tag{N2}
\]
A positive scalar functional is completely positive: a scalar compression of a positive block has nonnegative functional value. Multiplying the resulting positive scalar matrix by a fixed positive operator is again positive, by its square-root sandwich. Both corrections are therefore cp, their unit values fill the exact defects, and both maps are ucp. The first correction is normal because \(\tau\) is normal and has fixed finite-dimensional range. The second has finite-dimensional domain.

Write \(c_i=1-\Phi_i(1)\). Since \(0\le a_i\le1\),
\[
 0\le B_i(1-a_i)=b_i-\Phi_i(1)\le c_i,
 \qquad0\le1-b_i\le c_i.
\]
Every positive contraction \(d\le c_i\) has \(\|d\|_2^2=\tau(d^2)\le\tau(d)\le\tau(c_i)\). Expanding the composite of (N2), using \(|\tau(x)|\le\|x\|\) and \(|\tau_{m_i}(A_i^u(x))|\le\|x\|\), therefore gives
\[
 \|B_i^uA_i^u(x)-\Phi_i(x)\|_2
 \le 2\|x\|\sqrt{\tau(c_i)}\longrightarrow0.
\tag{N3}
\]
The last limit uses the normal trace test at \(1\). Combining (N1)–(N3), one sufficiently late index meets any finite list and any prescribed positive error. These are exactly the normal ucp recording maps and ucp reconstruction maps used in Theorem 2.1, with the original injectivity hypothesis intact. The index set is a net; no countable approximation assumption entered.

<a id="2-reconstruction-maps-preserving-the-matrix-trace"></a>

## Reconstruct the observations with the exact trace

**Theorem 2.1.** Suppose \(M\) is injective. Given unitaries \(u_1,\ldots,u_n\in M\) and \(\varepsilon>0\), there are a ucp map \(T:M_q\to M\) and contractions \(y_k\in M_q\) such that
\[
\tau T=\tau_q,\qquad \|T(y_k)-u_k\|_2<\varepsilon.
\tag{6}
\]

**Proof.** Fix a small \(\eta>0\). Semidiscreteness gives ucp maps \(S_1:M\to M_m\), \(T_1:M_m\to M\) with
\(\|T_1S_1(u_k)-u_k\|_2<\eta/2\). Put \(x_k=S_1(u_k)\), so \(\|x_k\|\le1\). Lemma 1.1 gives a faithful ucp \(T_2\) with rational strictly positive density \(h\) and \(\|T_2-T_1\|<\eta/2\). Therefore
\[
\|T_2(x_k)-u_k\|_2<\eta.
\tag{7}
\]
Write \(\varphi=\tau T_2=\tau_m(h\,\cdot)\). The improved weighted Hilbert bound in the preceding lesson implies, for every contraction \(x\),
\[
\begin{aligned}
\|[h^{1/2},x]\|_{2,\tau_m}^2
&=\varphi(x^*x)+\varphi(xx^*)
-2\tau_m(h^{1/2}x^*h^{1/2}x)\\
&\le2-2\|T_2(x)\|_2^2.
\end{aligned}
\tag{8}
\]
The two cross traces agree by cyclicity; they are real and nonnegative. From (7), \(\|T_2(x_k)\|_2>1-\eta\) and \(\|T_2(x_k)\|_2\le1\). In particular
\[
\|[h^{1/2},x_k]\|_{2,\tau_m}^2<4\eta.
\tag{9}
\]
Apply the rational density theorem to obtain ucp maps \(R:M_m\to M_q\) and \(L:M_q\to M_m\) satisfying
\[
\tau_qR=\varphi,\qquad\varphi L=\tau_q,\qquad
\|LR(x_k)-x_k\|_\varphi^\#<2\sqrt\eta.
\tag{10}
\]
For arbitrary \(a\), Schwarz and traciality of the target give
\[
\|T_2(a)\|_2^2
\le\tfrac12\varphi(a^*a+aa^*)=(\|a\|_\varphi^\#)^2.
\tag{11}
\]
Set \(y_k=R(x_k)\) and \(T=T_2L\). These are contractions and a ucp map. Equations (7), (10) and (11) give
\[
\|T(y_k)-u_k\|_2<\eta+2\sqrt\eta,
\qquad \tau T=\varphi L=\tau_q.
\tag{12}
\]
Choosing \(\eta+2\sqrt\eta<\varepsilon\) proves the result. \(\square\)

One common error budget \(\eta\) controls the perturbed reconstruction throughout (7)–(12). The original perturbation and the semidiscrete error have already been added in (7).

<a id="3-an-ordinary-adjoint-preserves-both-traces"></a>

## Use the adjoint to preserve both traces

**Theorem 3.1.** For every finite list \(a_1,\ldots,a_N\in M\) in an injective faithfully tracial algebra and every \(\varepsilon>0\), there are ucp maps
\[
M\xrightarrow{S}M_q\xrightarrow{T}M
\]
such that \(S\) is normal and
\[
\tau_qS=\tau,\qquad \tau T=\tau_q,\qquad
\|TS(a_j)-a_j\|_2<\varepsilon.
\tag{13}
\]

**Proof.** First treat a finite list of unitaries. Choose \(T,y_k\) from Theorem 2.1 with error less than \(\eta\). Its ordinary trace adjoint \(S=T^\sharp\) is normal and cp by the preceding lesson. Since \(\tau T=\tau_q\), its density is \(1\), so \(S(1)=1\). Pairing with \(1\) gives \(\tau_qS=\tau\). Both maps are \(L^2\) contractions by Schwarz and their trace identities.

The adjoint identity gives the complex estimate
\[
\left|\tau_q(S(u_k)y_k^*)-1\right|
=\left|\tau(u_k(T(y_k)-u_k)^*)\right|<\eta.
\tag{14}
\]
Consequently its real part exceeds \(1-\eta\). As both \(\|S(u_k)\|_2\) and \(\|y_k\|_2\) are at most \(1\),
\[
\|S(u_k)-y_k\|_2^2<2\eta,
\qquad
\|TS(u_k)-u_k\|_2<\sqrt{2\eta}+\eta.
\tag{15}
\]
Choose the small budget before applying Theorem 2.1.

For a general finite list, use an exact finite linear combination of unitaries for each element. Indeed a self-adjoint contraction \(b\) is \((v+v^*)/2\), where \(v=b+i(1-b^2)^{1/2}\) is unitary. Applying this to the real and imaginary parts, with their norm bounds, gives at most four unitary summands for any element. Collect their finite list and take a unitary error smaller than \(\varepsilon\) divided by the maximum sum of absolute coefficients. Zero elements need no tests. Linearity proves (13). \(\square\)

In (14) the difference of the complex pairing from \(1\) is controlled directly. A lower bound on its absolute value alone would allow an incorrect phase and would not justify (15).

**Corollary 4.2.** Given finitely many unitaries in an injective faithfully tracial \(M\), they can be approximated in \(2\)-norm by \(T(v_k)\), where \(T:M_m\to M\) is ucp, \(\tau T=\tau_m\), and every \(v_k\) is unitary. This follows from Theorem 2.1 and Lemma 4.1 with a sufficiently small initial budget. Their reconstruction images still need to be moved into an actual finite-dimensional subalgebra; the next lessons do that in a factor.

<a id="5-problems-with-complete-solutions"></a>

## Worked diagnostics and complete solutions

**Exercise 1.** In Lemma 1.1 take \(h=\operatorname{diag}(2,0)\), \(q_1=19/10\), \(q_2=0\). Compute \(b,c,h'\).

*Solution.* Equations (2) and (5) give \(b=\operatorname{diag}(19/20,1)\), \(c=1/20\), and \(h'=\operatorname{diag}(39/20,1/20)\). Its normalized trace is \(1\), its eigenvalues are positive rationals, and its previously zero eigenvalue is now positive. For any \(\delta>1/20\) the required strict rational inequalities hold.

**Exercise 2.** Explain why the scalar correction in (3) is completely positive.

*Solution.* A positive scalar functional is cp. At any matrix level, \([\tau_m(x_{ij})]\ge0\) when \([x_{ij}]\ge0\). Tensoring this scalar positive matrix with the positive operator \(T(1-b)\) gives the positive block matrix \([\tau_m(x_{ij})T(1-b)]\). This is exactly the amplification of the correction.

**Exercise 3.** Check that \(\tau_m(h')=1\) even when \(h\) has a kernel.

*Solution.* Equation (5) gives \(\tau_m(h')=m^{-1}\sum_iq_i+c=1\). The coordinates with zero eigenvalues contribute \(q_i=0\), and the positive constant \(c\) occurs in every coordinate. No division by a zero eigenvalue occurs in (2).

**Exercise 4.** Derive the cross term in (8) from the square of the commutator.

*Solution.* Expand \((h^{1/2}x-xh^{1/2})^*(h^{1/2}x-xh^{1/2})\) and take \(\tau_m\). The first two terms become \(\tau_m(hxx^*)\) and \(\tau_m(hx^*x)\). Cyclicity makes both negative cross terms \(\tau_m(h^{1/2}x^*h^{1/2}x)\). This equals \(\|h^{1/4}xh^{1/4}\|_{2,\tau_m}^2\), so it is real and nonnegative.

**Exercise 5.** Give an explicit positive \(\eta\) making the bound in (12) smaller than a prescribed \(\varepsilon>0\).

*Solution.* Take \(\eta=\min(\varepsilon/4,\varepsilon^2/64,1/4)\). Then \(\eta\le\varepsilon/4\), and \(2\sqrt\eta\le\varepsilon/4\). Their sum is at most \(\varepsilon/2<\varepsilon\). The extra bound \(\eta\le1/4\) keeps the near-unitary lower bound positive.

**Exercise 6.** Why do the two trace identities in (13) imply \(L^2\) contractivity?

*Solution.* Schwarz gives \(T(x)^*T(x)\le T(x^*x)\). Applying \(\tau\) gives \(\|T(x)\|_2^2\le\tau_m(x^*x)\). The same argument for \(S\), applying \(\tau_m\) and using \(\tau_mS=\tau\), proves its contraction inequality. Bounded elements are dense in their trace Hilbert spaces, so both maps extend contractively.

**Exercise 7.** Why is \(|z|>1-\eta\) insufficient for (15), whereas \(|z-1|<\eta\) suffices?

*Solution.* The number \(z=-1\) has absolute value \(1\), but real part \(-1\); a squared-distance formula involving \(2\operatorname{Re}z\) would then have the wrong bound. If \(|z-1|<\eta\), then \(\operatorname{Re}z>1-\eta\), which is the estimate actually used in (15).

**Exercise 8.** Show that the state in (17) need not be \(\tau_m\).

*Solution.* Take \(M=\mathbb C\), \(m=2\), and \(T(x)=x_{11}\). This is ucp, but \(\tau T(e_{11})=1\) while \(\tau_2(e_{11})=1/2\). The proof therefore uses \(\varphi=\tau T\) rather than the normalized matrix trace. Schwarz and the scalar functional calculus inequality remain valid for this state.

**Exercise 9.** Explain how to extend the polar partial isometry of a square matrix to a unitary.

*Solution.* Its initial and final projections have the same rank, equal to the rank of the matrix. Their complements therefore have the same dimension. Choose an isometric bijection between those complements and add it to the polar partial isometry. The orthogonal initial and final partitions make the sum unitary, and the extra term annihilates \(|y|\), so \(y=v|y|\) remains true.

**Exercise 10.** Suppose the error in Theorem 3.1 is at most \(\gamma\) on all unitary summands of \(a=\sum_j\alpha_j u_j\). Bound its error on \(a\).

*Solution.* Linearity and the triangle inequality give \(\|TS(a)-a\|_2\le\gamma\sum_j|\alpha_j|\). A finite list has a finite maximum of these coefficient sums. Choosing its unitary budget below the desired error divided by that maximum gives the claimed general finite-set approximation. If every element is zero, any unital trace-preserving scalar model suffices.

## References and proof scope

The rational perturbation and trace-preserving factorization were developed by Uffe Haagerup in *A new proof of the equivalence of injectivity and hyperfiniteness for factors on a separable Hilbert space*, *Journal of Functional Analysis* 62 (1985), 160–201. A freely accessible method comparison is Xiaoyan Zhou and Junsheng Fang, [*A note on relative amenability of finite von Neumann algebras*](https://jot.theta.ro/jot/archive/2019-081-001/2019-081-001-005.pdf), *Journal of Operator Theory* 81:1 (2019), 107–132: Lemmas 3.5–3.6 and the scalar specialization of Claim 1 in the proof of Theorem 3.2, printed pp.120–127. The source's later relative-algebra hypotheses are not imported. The finite injectivity input is the direct local faithful-trace proof, and the exact complex estimate (14) supplies the needed real part without inferring its sign from an absolute-value lower bound.

The state-preparation proof gives the primary rational perturbation with bound \(2\alpha\). Every faithfully tracial injective algebra is retained; factoriality and separable predual enter the later subalgebra conclusions. These finite maps prove no AFD conclusion by themselves. The new normalization argument (N1)–(N3) proves the incoming topology and unit correction with its own explicit trace budget.

For optional reading on trace-preserving expectations, Matthew Daws's *Conditional Expectations*, Section 4, Theorem 4.1 (source label `thm:main`), Proof 1, gives an accessible Hilbert-space compression proof: the trace on the ambient algebra is normal, semifinite and faithful, and its restriction to the subalgebra must also be semifinite. [Editable author source at commit a2d5477](https://github.com/MatthewDaws/Mathematics/blob/a2d54776c75fc99f12d8e317e3e3c3fd34c813f9/Conditional-Expectations/ce.tex). The [repository notice](https://github.com/MatthewDaws/Mathematics/blob/a2d54776c75fc99f12d8e317e3e3c3fd34c813f9/README.md) licenses those notes under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). This is supplementary reading; no expectation theorem is an input of this lesson's finite-model proofs.
