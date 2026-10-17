# Dyadic triangles and the main estimate

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The *triangular Hilbert form* couples three functions of two variables, each pair of them sharing one variable:
\[
\Lambda(F_0,F_1,F_2)=\mathrm{p.v.}\int_{\mathbf R^3}\frac{G(x)\,dx}{x_0+x_1+x_2},
\]
where \(G(x)=F_0(x_0,x_1)F_1(x_1,x_2)F_2(x_2,x_0)\).
Thiele asked whether it satisfies the symmetric bound \(|\Lambda|\le C\prod_v\|F_v\|_{L^3}\) [GOPSS, Section 9, Problem 13]; he also formulated the dyadic model studied here and asked for the analogous bound. Kovač, Thiele and Zorin-Kranich proved bounds for the dyadic model when one input has a special structure [KTZ]; Tao, Zorin-Kranich, and Durcik, Kovač and Thiele obtained bounds that grow slowly with the number of scales [T], [ZK], [DKT]. OpenAI proved the dyadic bound with no condition on the inputs and no dependence on the number of scales [OpenAI-D]. This course proves that theorem (Theorem A below). The continuous form is a different operator: OpenAI's manuscripts on the maximal and annular triangular Hilbert transform state the continuous bound at this exponent [OpenAI-M], and the present course treats only the dyadic model.

## The theorem

Write \(\mathbf R_+=[0,\infty)\). For \(k\in\mathbf Z\), the dyadic intervals of length \(2^k\) are
\[
\mathcal D_k=\{[2^kn,2^k(n+1)):n\in\mathbf Z_{\ge0}\},
\]
and \(n_I\) is the index \(n\) of \(I\in\mathcal D_k\). The *Haar function* of \(I\) is \(h_I=\mathbf 1_{I_{\rm left}}-\mathbf 1_{I_{\rm right}}\), the difference of the indicator functions of the two halves of \(I\). Write \(\oplus\) for the bitwise exclusive or of nonnegative integers. The *admissible triples* of scale \(k\) are
\[
\begin{aligned}
\mathcal A_k=\{&(I_0,I_1,I_2)\in\mathcal D_k^3:\\
&n_{I_0}\oplus n_{I_1}\oplus n_{I_2}=0\}.
\end{aligned}
\]
Indices of the three variables are taken modulo \(3\). For \(\mathbf I=(I_0,I_1,I_2)\in\mathcal A_k\) and real functions \(F_0,F_1,F_2\) on \(\mathbf R_+^2\), the *local form* is
\[
\begin{aligned}
&L_{\mathbf I}(F_0,F_1,F_2)\\
&\quad=2^{-k}\int_{I_0\times I_1\times I_2}G(x)\prod_{v=0}^2h_{I_v}(x_v)\,dx ,
\end{aligned}
\]
with \(G\) as above.
For a finite set \(S\subset\mathbf Z\) of scales and real coefficients \(|\epsilon_k|\le1\), the *dyadic triangular Hilbert form* is
\[
\Lambda^{\rm d}_{S,\epsilon}=\sum_{k\in S}\epsilon_k\sum_{\mathbf I\in\mathcal A_k}L_{\mathbf I}.
\]

**Theorem A** (OpenAI). For every finite \(S\subset\mathbf Z\) and all real functions \(F_0,F_1,F_2\in L^3(\mathbf R_+^2)\),
\[
\begin{aligned}
&\sum_{k\in S}\sum_{\mathbf I\in\mathcal A_k}\bigl|L_{\mathbf I}(F_0,F_1,F_2)\bigr|\\
&\quad\le40\prod_{v=0}^2\|F_v\|_{L^3(\mathbf R_+^2)} .
\end{aligned}
\]

In particular \(|\Lambda^{\rm d}_{S,\epsilon}(F_0,F_1,F_2)|\le40\prod_v\|F_v\|_3\), uniformly in \(S\) and \(\epsilon\), and the same holds with a separate coefficient of modulus at most \(1\) for every admissible triple. The local forms are absolutely convergent for \(L^3\) inputs (Lemma 1.3).

**The course.**

1. This lesson: the dyadic setting, step functions as matrices, the four children of an admissible triple, and the reduction of Theorem A to step functions.
2. [A matrix energy and a trace inequality](a-matrix-energy-and-a-trace-inequality.md): the energy \(\operatorname{tr}(P^{3/2})\), its Hessian, a comparison of Hessians under the order of matrices, and a bound for a cyclic product of three matrices by these Hessians.
3. [Energy increase and telescoping](energy-increase-and-telescoping.md): the energy of an admissible triple grows under dyadic splitting by at least a fixed multiple of its local form, and the increases telescope.

**What the course assumes.** Linear algebra over \(\mathbf R\) (symmetric matrices, the spectral theorem, the trace); the inverse function theorem for maps between finite-dimensional spaces; the Lebesgue integral and \(L^p\) spaces with Hölder's inequality, as in Fremlin's *Measure Theory* in the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10).

## 1. Step functions and matrices

Fix \(m\in\mathbf Z\) and call the intervals of \(\mathcal D_m\) *atoms*. In this section and in the third lesson, \(F_0,F_1,F_2\) are bounded, have bounded support, and are constant on every product \(J\times J'\) of atoms; write \(F_v(i,j)\) for the value of \(F_v\) on the product of the atoms \(i\) and \(j\).

Let \(\mathbf I=(I_0,I_1,I_2)\in\mathcal A_k\) with \(k\ge m\). Let \(H_v\) be the real inner product space with orthonormal basis indexed by the atoms contained in \(I_v\); there are \(2^{k-m}\) of them. Each atom has weight \(w=2^{m-k}\) in the probability measure \(|I_v|^{-1}dx_v\). Define linear maps \(W_v:H_{v+1}\to H_v\) by their matrices
\[
W_v(i,j)=w\,F_v(i,j)
\]
for atoms \(i\subseteq I_v\) and \(j\subseteq I_{v+1}\), that is, \(\sqrt{w\cdot w}\) times the value of \(F_v\). If \(k\ge m+1\), the Haar function \(h_{I_v}\) is constant on each atom of \(I_v\); let \(D_v\) be the diagonal matrix on \(H_v\) of these values \(\pm1\). Put
\[
\tau(\mathbf I)=\operatorname{tr}(D_0W_0D_1W_1D_2W_2).
\]

**Lemma 1.1.** For \(\mathbf I\in\mathcal A_k\) with \(k\ge m+1\), \(L_{\mathbf I}(F_0,F_1,F_2)=2^{2k}\tau(\mathbf I)\).

*Proof.* Expanding the trace over atoms \(i_v\subseteq I_v\),
\[
\tau(\mathbf I)=w^3\sum_{i_0,i_1,i_2}G(i_0,i_1,i_2)\prod_{v=0}^2h_{I_v}(i_v),
\]
where \(G(i_0,i_1,i_2)\) is \(F_0(i_0,i_1)F_1(i_1,i_2)F_2(i_2,i_0)\) and \(h_{I_v}(i_v)\) is the value of \(h_{I_v}\) on \(i_v\). The integral in \(L_{\mathbf I}\) is the same sum with \(w^3\) replaced by \((2^m)^3\), the volume of a product of three atoms. So the integral is \(2^{3k}\tau(\mathbf I)\), and \(L_{\mathbf I}=2^{-k}2^{3k}\tau(\mathbf I)\). \(\square\)

## 2. The four children

Let \(\mathbf I\in\mathcal A_k\). Choosing a half of each \(I_v\), with \(b_v=0\) for the left and \(b_v=1\) for the right half, gives three intervals of \(\mathcal D_{k-1}\) with indices \(2n_{I_v}+b_v\). The binary digits of \(2n_{I_v}+b_v\) are those of \(n_{I_v}\) followed by \(b_v\), so the exclusive or of the three new indices has the digits of \(n_{I_0}\oplus n_{I_1}\oplus n_{I_2}=0\) followed by \(b_0\oplus b_1\oplus b_2\). The new triple is therefore admissible exactly when \(b_0\oplus b_1\oplus b_2=0\). With the signs \(s_v=(-1)^{b_v}\), this condition reads \(s_0s_1s_2=1\). So \(\mathbf I\) has four admissible *children*, with the sign triples \((+,+,+)\), \((+,-,-)\), \((-,+,-)\) and \((-,-,+)\); write \(\operatorname{ch}(\mathbf I)\) for this set of four triples and \(\mathbf I(s)\) for the child with signs \(s=(s_0,s_1,s_2)\).

**Lemma 1.2.** (1) Choose one of the four children uniformly at random. Then each sign \(s_v\) takes the values \(\pm1\) with probability \(\frac12\), and conditionally on \(s_v\), each of the other two signs still takes the values \(\pm1\) with probability \(\frac12\).

(2) Every admissible triple of scale \(k-1\) is a child of exactly one admissible triple of scale \(k\).

*Proof.* (1) For \(s_0=+1\) the children are \((+,+,+)\) and \((+,-,-)\), and for \(s_0=-1\) they are \((-,+,-)\) and \((-,-,+)\); in each case \(s_1\) and \(s_2\) take both values once. The list is symmetric under permutations of the three positions. (2) Deleting the last binary digit of the three indices of an admissible triple gives the indices of the intervals containing them; their exclusive or is the exclusive or of the original indices with its last digit deleted, which is \(0\). So the parent is admissible, and it is the only triple of scale \(k\) of which the given triple is a child. \(\square\)

## 3. One scale, and the reduction to step functions

**Lemma 1.3** (one scale). For every \(k\in\mathbf Z\) and all real \(F_v\in L^3(\mathbf R_+^2)\), the integrals defining \(L_{\mathbf I}\) converge absolutely, and
\[
\sum_{\mathbf I\in\mathcal A_k}\bigl|L_{\mathbf I}(F_0,F_1,F_2)\bigr|\le\prod_{v=0}^2\|F_v\|_3 .
\]

*Proof.* Put \(a_v(\mathbf I)=(|I_v||I_{v+1}|)^{-1}\int_{I_v\times I_{v+1}}|F_v|^3\). On the probability space \(I_0\times I_1\times I_2\) with normalized Lebesgue measure, each \(|F_v(x_v,x_{v+1})|^3\) has integral \(a_v(\mathbf I)\), so Hölder's inequality with three exponents \(3\), and \(|h_{I_v}|\le1\), give
\[
\begin{aligned}
|L_{\mathbf I}|&\le2^{-k}\,2^{3k}\prod_va_v(\mathbf I)^{1/3}\\
&=2^{2k}\prod_va_v(\mathbf I)^{1/3},
\end{aligned}
\]
with absolute convergence of the integral. For each \(v\) and each pair \((I_v,I_{v+1})\in\mathcal D_k^2\) there is exactly one \(I_{v+2}\in\mathcal D_k\) completing it to an admissible triple, namely the interval with index \(n_{I_v}\oplus n_{I_{v+1}}\). Hence \(\sum_{\mathbf I\in\mathcal A_k}2^{2k}a_v(\mathbf I)=\|F_v\|_3^3\), and Hölder's inequality for the sum over \(\mathcal A_k\) with weights \(2^{2k}\) proves the bound. \(\square\)

**Lemma 1.4** (reduction). If the inequality of Theorem A holds whenever \(F_0,F_1,F_2\) are bounded step functions with bounded support, constant on products of atoms of some level \(m\le\min S-1\), then it holds for all real \(F_v\in L^3(\mathbf R_+^2)\).

*Proof.* Such step functions are dense in \(L^3(\mathbf R_+^2)\): a function in \(L^3\) is approximated by a continuous function with compact support, and that function by its averages over the products of atoms of a small level, by uniform continuity; refining the level does not change a step function, so the level can be taken at most \(\min S-1\). Let \(F_v^{(n)}\to F_v\) in \(L^3\). By trilinearity, for two input triples \(F\) and \(F'\), \(L_{\mathbf I}(F)-L_{\mathbf I}(F')\) is the sum of the three local forms with inputs \((F_0-F'_0,F_1,F_2)\), \((F'_0,F_1-F'_1,F_2)\) and \((F'_0,F'_1,F_2-F'_2)\). By Lemma 1.3, for each \(k\in S\), the sequences \((L_{\mathbf I}(F^{(n)}))_{\mathbf I\in\mathcal A_k}\) converge in \(\ell^1(\mathcal A_k)\) to \((L_{\mathbf I}(F))_{\mathbf I}\). As \(||a|-|b||\le|a-b|\), the left side of Theorem A converges, and so does the right side. \(\square\)

## 4. The plan

For a step function input and \(\mathbf I\in\mathcal A_k\), the *row star* at the vertex \(v\) collects the two maps meeting at \(H_v\), \(R_v=[\,W_v\ \ W_{v-1}^{\mathsf T}\,]:H_{v+1}\oplus H_{v-1}\to H_v\), and the *energy* of \(\mathbf I\) is
\[
e(\mathbf I)=\sum_{v=0}^2\operatorname{tr}\bigl((R_vR_v^{\mathsf T})^{3/2}\bigr).
\]
The second lesson bounds \(|\tau(\mathbf I)|\) by the curvature of \(P\mapsto\operatorname{tr}(P^{3/2})\) in three directions. The third lesson shows that this curvature is at most a multiple of the growth \(\frac14\sum_{\mathbf I'\in\operatorname{ch}(\mathbf I)}e(\mathbf I')-e(\mathbf I)\) of the energy under splitting. By Lemma 1.2(2), the weighted energies \(\sum_{\mathbf I\in\mathcal A_k}2^{2k}e(\mathbf I)\) then telescope over the scales, and they are bounded by a constant multiple of \(\sum_v\|F_v\|_3^3\) at every scale.

## 5. Exercises

**1.1** (easy). List the admissible triples in \(\mathcal A_0\) with indices at most \(3\), and check that every pair of indices in \(\{0,1,2,3\}\) occurs exactly once as \((n_{I_0},n_{I_1})\).

**1.2** (easy). Show that \(L_{\mathbf I}(F_0,F_1,F_2)=0\) if \(F_0(x_0,x_1)=g(x_1)\) and \(F_2(x_2,x_0)=\tilde g(x_2)\) do not depend on \(x_0\).

**1.3** (medium). Let \(m=0\), \(k=1\) and \(\mathbf I=([0,2),[0,2),[0,2))\). Write \(W_0,W_1,W_2\) and \(D_0,D_1,D_2\) as \(2\times2\) matrices and check Lemma 1.1 for \(F_0=F_1=F_2=\mathbf 1_{[0,1)\times[0,1)}\).

**1.4** (medium). Show that for \(L^3\) inputs the series \(\sum_{\mathbf I\in\mathcal A_k}L_{\mathbf I}\) defining \(\Lambda^{\rm d}_{S,\epsilon}\) converges absolutely for each \(k\), and that \(|\Lambda^{\rm d}_{S,\epsilon}|\le|S|\prod_v\|F_v\|_3\). (Theorem A removes the factor \(|S|\).)

## 6. Solutions

**1.1.** The triples are \((n_0,n_1,n_0\oplus n_1)\) with \(n_0,n_1\in\{0,1,2,3\}\); for example \((1,2,3)\), \((2,3,1)\), \((3,3,0)\). Each ordered pair \((n_0,n_1)\) determines \(n_2\), and \(n_0\oplus n_1\le3\).

**1.2.** The variable \(x_0\) appears in the integrand only in the factor \(h_{I_0}(x_0)\). By Fubini's theorem, integrating first in \(x_0\) gives \(\int_{I_0}h_{I_0}=0\), so \(L_{\mathbf I}=0\).

**1.3.** The atoms are \([0,1)\) and \([1,2)\), and \(w=\frac12\). Each \(W_v\) has the single nonzero entry \(\frac12\) in the position of the pair of left atoms, and \(D_v=\operatorname{diag}(1,-1)\), so \(D_vW_v=\operatorname{diag}(\frac12,0)\) and \(\tau(\mathbf I)=\frac18\); Lemma 1.1 predicts \(L_{\mathbf I}=2^2\cdot\frac18=\frac12\). Directly, the integrand is \(1\) on \([0,1)^3\), where all three Haar functions equal \(1\), and \(0\) elsewhere, so \(L_{\mathbf I}=2^{-1}\cdot1=\frac12\).

**1.4.** Lemma 1.3 gives absolute convergence and \(\sum_{\mathbf I\in\mathcal A_k}|L_{\mathbf I}|\le\prod_v\|F_v\|_3\) for each \(k\); sum over the \(|S|\) scales.

## References

- [OpenAI-D] OpenAI, *An \(L^3\) bound for the dyadic triangular Hilbert form*, OpenAI Math Release preprint, 5 October 2026. https://github.com/openai/math/tree/main/preprints/An-L3-bound-for-the-dyadic-triangular-Hilbert-form-October-5-2026
- [OpenAI-M] OpenAI, *The maximal triangular Hilbert transform at the symmetric point*, OpenAI Math Release preprint, 24 September 2026, https://github.com/openai/math/tree/main/preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026 ; and *Annular variation of the triangular Hilbert transform at the symmetric point*, 5 October 2026, https://github.com/openai/math/tree/main/preprints/Annular-variation-of-the-triangular-Hilbert-transform-at-the-symmetric-point-October-5-2026
- [GOPSS] L. Grafakos, D. Oliveira e Silva, M. Pramanik, A. Seeger and B. Stovall, *Some problems in harmonic analysis*, arXiv:1701.06637, Section 9 (contributed by C. Thiele). https://arxiv.org/abs/1701.06637
- [KTZ] V. Kovač, C. Thiele and P. Zorin-Kranich, *Dyadic triangular Hilbert transform of two general functions and one not too general function*, Forum of Mathematics, Sigma 3 (2015), e25; arXiv:1506.00861. https://arxiv.org/abs/1506.00861
- [T] T. Tao, *Cancellation for the multilinear Hilbert transform*, Collectanea Mathematica 67 (2016), 191–206; arXiv:1505.06479. https://arxiv.org/abs/1505.06479
- [ZK] P. Zorin-Kranich, *Cancellation for the simplex Hilbert transform*, Mathematical Research Letters 24 (2017), 581–592; arXiv:1507.02436. https://arxiv.org/abs/1507.02436
- [DKT] P. Durcik, V. Kovač and C. Thiele, *Power-type cancellation for the simplex Hilbert transform*, Journal d'Analyse Mathématique 139 (2019), 67–82; arXiv:1608.00156. https://arxiv.org/abs/1608.00156
