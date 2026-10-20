# From the moment to the pairing

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The pairing \(\langle f,\mathcal Ag\rangle\) of [*Physical states and good positions*](physical-states-and-good-positions.md) involves vectors of size \((UV)^{1/2}\) and an operator whose norm we cannot bound directly by anything better than a power of \(L\). A high moment of \(\mathcal A\mathcal A^*\) does better: its trace, averaged over positions, is shown in Lessons 11–16 to decay like \(L^{-E_0N}\) with \(N\asymp L^{0.5}\). This lesson converts such a moment bound into the bound \(\langle f,\mathcal Ag\rangle\ll UVL^{-E_0+4C}\). Two features make the conversion lossless. The edges only connect positions with nearly equal slopes, so the problem splits into pieces with \(O(H)\) positions each; and the price of passing from a trace to a quadratic form, a factor \(H\), is reduced to \(H^{1/(2R)}=O(1)\) by the high moment.

**Prerequisites.** [*Physical states and good positions*](physical-states-and-good-positions.md), Sections 1–4; [*Measure and Hilbert space tools for Haar integration*](course:harmonic-analysis-on-locally-compact-groups/reader/measure-and-hilbert-space-tools), Theorem 3.1 (Hölder's inequality).

We keep the notation of that lesson. For a position \(P\) let \(\mathbf u_P\in\mathcal H\) be the function equal to \(1\) at every state \((P,\mathbf p)\) and \(0\) at states with other positions. These vectors are not normalized. Put \(B_0=\mathcal A\mathcal A^*\), a positive semidefinite operator on the finite-dimensional space \(\mathcal H\), and

\[
\begin{gathered}
\mathfrak m=\sum_P\langle\mathbf u_P,B_0^R\mathbf u_P\rangle,\quad(0.1)
\end{gathered}
\]

the sum over all positions \(P\in\Omega\).

## 1. Two facts from linear algebra

**Lemma 1.1 (compression by arbitrary vectors).** Let \(B\) be a positive semidefinite operator on a finite-dimensional Hilbert space, \(\mathbf v_1,\dots,\mathbf v_n\) arbitrary vectors and \(c_1,\dots,c_n\) complex numbers. Then

\[
\begin{gathered}
\Bigl\langle\sum_Pc_P\mathbf v_P,B\sum_Qc_Q\mathbf v_Q\Bigr\rangle\\
\le\Bigl(\sum_P\langle\mathbf v_P,B\mathbf v_P\rangle\Bigr)\sum_P|c_P|^2 .
\end{gathered}
\]

**Proof.** The matrix \(C_{PQ}=\langle\mathbf v_P,B\mathbf v_Q\rangle\) is the Gram matrix of the vectors \(B^{1/2}\mathbf v_P\), hence positive semidefinite. Its largest eigenvalue is at most the sum of all its eigenvalues, which is its trace \(\sum_P\langle\mathbf v_P,B\mathbf v_P\rangle\). The left side equals \(\overline c^{\,T}Cc\le\lambda_{\max}(C)\sum|c_P|^2\). \(\square\)

No orthogonality or normalization of the \(\mathbf v_P\) is needed; this is why the unnormalized trace (0.1) suffices.

**Lemma 1.2 (spectral Hölder inequality).** For a positive semidefinite \(B\), a vector \(\mathbf v\) and an integer \(R\ge1\),

\[
\begin{gathered}
\langle\mathbf v,B\mathbf v\rangle\le\langle\mathbf v,B^R\mathbf v\rangle^{1/R}\|\mathbf v\|^{2-2/R}.
\end{gathered}
\]

**Proof.** Expand \(\mathbf v=\sum_jc_j\mathbf w_j\) in an orthonormal eigenbasis, \(B\mathbf w_j=\lambda_j\mathbf w_j\), \(\lambda_j\ge0\). With the probability weights \(\pi_j=|c_j|^2/\|\mathbf v\|^2\), Jensen's inequality for the convex function \(y\mapsto y^R\) gives \(\sum_j\pi_j\lambda_j\le(\sum_j\pi_j\lambda_j^R)^{1/R}\). Multiply by \(\|\mathbf v\|^2\). \(\square\)

## 2. Slope intervals

**Lemma 2.1.** If \((P,\mathbf p)\) and \((Q,\mathbf p')\) are joined by an edge with \(\mathcal K\ne0\), then \(|\det(P,Q)|\le10H\) and

\[
\begin{gathered}
\Bigl|\frac{P_2}{P_1}-\frac{Q_2}{Q_1}\Bigr|\le\frac{10H}{U^2}.\quad(2.1)
\end{gathered}
\]

**Proof.** On the support of \(\mathcal K\), \(D<2d_0\) and \(|t|\le5Y\), so \(|\det(P,Q)|=D|t|\le10d_0Y=10H\). The difference of slopes is \(\det(P,Q)/(P_1Q_1)\), and \(P_1,Q_1\ge U\). \(\square\)

Partition the positions according to their slope into the intervals \(I_j=[jH/U^2,(j+1)H/U^2)\), \(j\in\mathbb Z\). By (2.1), an edge joins positions whose interval indices differ by at most \(11\).

**Lemma 2.2.** Each \(I_j\) contains at most \(10^4H\) positions.

**Proof.** Fix a position \(P^0\) with slope in \(I_j\). Every other such position \(P\) satisfies \(|\det(P^0,P)|\)\(=P^0_1P_1|P_2/P_1-P^0_2/P^0_1|\)\(\le256U^2\cdot H/U^2\). For fixed \(d=\det(P^0,P)\), the integer solutions \(P\) form a coset of \(\mathbb ZP^0\), because \(P^0\) is primitive. Consecutive elements of a coset differ by at least \(P^0_1\ge U\) in the first coordinate, so at most \(16\) of them have first coordinate in \([U,16U]\). Hence there are at most \(16(512H+1)\le10^4H\) positions. \(\square\)

## 3. The pairing bound

**Proposition 3.1.** Suppose \(\mathfrak m\le UV\,L^{-E_0N}\) for some \(E_0>0\). Then

\[
\begin{gathered}
|\langle f,\mathcal Ag\rangle|\le C_{\rm abs}\,UV\,L^{4C-E_0},\quad(3.1)
\end{gathered}
\]

with an absolute constant \(C_{\rm abs}\), for \(x\) larger than a bound depending on \(K\).

**Proof.** Let \(f_j\) be \(f\) restricted to the states whose position has slope in \(I_j\), and \(g_j\) the restriction of \(g\) to the positions whose interval index differs from \(j\) by at most \(11\). The operators \(\mathcal G\) and \(\mathcal S\) do not move positions, and \(\mathcal T\) only joins positions in intervals at most \(11\) apart. Hence \(\langle f,\mathcal Ag\rangle=\sum_j\langle f_j,\mathcal Ag_j\rangle\), and

\[
\begin{gathered}
|\langle f_j,\mathcal Ag_j\rangle|=|\langle\mathcal A^*f_j,g_j\rangle|\\
\le\|g_j\|\,\langle f_j,B_0f_j\rangle^{1/2}.
\end{gathered}
\]

Since \(f\) depends only on the position, \(f_j=\sum_{P}f(P)\mathbf u_P\), the sum over positions in \(I_j\). Let \(d_j=\sum_P\langle\mathbf u_P,B_0^R\mathbf u_P\rangle\) over the same positions. Lemmas 1.1 and 1.2, together with Lemma 2.2 and \(\sup|f|\le L^{2C}\), give

\[
\begin{gathered}
\langle f_j,B_0f_j\rangle\\
\le\|f_j\|^{2-2/R}\bigl(10^4H\,L^{4C}d_j\bigr)^{1/R}.
\end{gathered}
\]

Therefore

\[
\begin{aligned}
|\langle f,\mathcal Ag\rangle|&\le\sum_j\|g_j\|\,\|f_j\|^{1-1/R}\\
&\quad\times\bigl(10^4HL^{4C}d_j\bigr)^{1/(2R)} .
\end{aligned}
\]

Apply Hölder's inequality in \(j\) (Theorem 3.1 of [*Measure and Hilbert space tools for Haar integration*](course:harmonic-analysis-on-locally-compact-groups/reader/measure-and-hilbert-space-tools), for the counting measure, used twice for three factors) with the exponents \(2\), \(2R/(R-1)\) and \(2R\), whose reciprocals add up to one. Every position lies in at most \(23\) of the sets defining the \(g_j\), so \(\sum_j\|g_j\|^2\le23\|g\|^2\); also \(\sum_j\|f_j\|^2=\|f\|^2\) and \(\sum_jd_j=\mathfrak m\). Thus

\[
\begin{aligned}
|\langle f,\mathcal Ag\rangle|&\le\sqrt{23}\,\|g\|\,\|f\|^{1-1/R}\\
&\quad\times\bigl(10^4HL^{4C}\bigr)^{1/(2R)}\mathfrak m^{1/(2R)} .
\end{aligned}
\]

By Lemma 4.2 of Lesson 8, \(\|f\|,\|g\|\le\sqrt{32}\,L^{2C}(UV)^{1/2}\), and by hypothesis \(\mathfrak m^{1/(2R)}\le(UV)^{1/(2R)}L^{-E_0}\), since \(N=2R\). The powers of \(UV\) add up to exactly one, and the powers of \(L^C\) to \(L^{4C}\). Finally \(\log H\le5KL^{0.21}\) and \(R\ge L^{0.5}/2\), so \(H^{1/(2R)}\le2\) for large \(x\). \(\square\)

Without the high moment, that is with \(R=1\), the same argument loses the factor \(H^{1/2}=x^{o(1)}\), which is larger than every power of \(L\). The exponent \(N\asymp L^{0.5}\) is chosen to exceed \(\log H\asymp L^{0.21}\) by a power of \(L\).

## 4. What remains

The rest of the minor-arc analysis proves the hypothesis of Proposition 3.1.

**Theorem 4.1 (the minor moment).** For every fixed \(E_0>0\), if \(A_0\) is large in terms of \(E_0\), and \(K\ge K_1(E_0)=200(E_0+7)\), then for large \(x\) and every pad dyad \(d_0\) and every \(Y\) in (2.1) of Lesson 7,

\[
\begin{gathered}
\mathfrak m\le UV\,L^{-E_0N}.\quad(4.1)
\end{gathered}
\]

This is proved in [*Birth distinctness and the minor moment*](birth-distinctness-and-the-minor-moment.md), Theorem 3.1, after the preparation of Lessons 10–15. Expanding (0.1), \(\mathfrak m\) is a sum over closed paths of \(N\) edges: sequences of states \(s_0,s_1,\dots,s_N\) in which \(s_0\) and \(s_N\) have the same position \(P\) (the lists at the two ends are unrelated), consecutive states are joined alternately by an edge of \(\mathcal A\) and by a reversed edge of \(\mathcal A^*\), and each path is weighted by the product of the edge weights, the measure of the initial lists, and the symmetrization and goodness factors. Lessons 10 and 11 replace the sum over the starting position \(P\) by an average over independent residue classes; Lessons 12–16 bound the resulting expression.

## 5. Exercises

**9.1.** Show that the largest eigenvalue of a positive semidefinite matrix is at most its trace, and give an example where Lemma 1.1 is an equality.

**9.2.** Show that Lemma 1.2 is an equality when \(\mathbf v\) is an eigenvector of \(B\).

**9.3.** Show that every integer \(j'\) is within distance \(11\) of at most \(23\) integers \(j\), and deduce \(\sum_j\|g_j\|^2\le23\|g\|^2\).

**9.4.** Let \(R=1\) in the proof of Proposition 3.1. Show that the method gives \(|\langle f,\mathcal Ag\rangle|\ll UVL^{4C}(H\mathfrak m/(UV))^{1/2}\), and explain why this is useless unless \(\mathfrak m\) is smaller than \(UV/H\) by a power of \(L\).

**9.5.** Show that \(H^{1/(2R)}\to1\) as \(x\to\infty\).

## 6. Solutions

**9.1.** The eigenvalues are nonnegative, so the largest is at most their sum, which is the trace. If \(n=1\), Lemma 1.1 reads \(|c|^2\langle\mathbf v,B\mathbf v\rangle\le\langle\mathbf v,B\mathbf v\rangle|c|^2\), an equality.

**9.2.** If \(B\mathbf v=\lambda\mathbf v\), both sides equal \(\lambda\|\mathbf v\|^2\).

**9.3.** The integers \(j\) with \(|j-j'|\le11\) are \(j'-11,\dots,j'+11\). A position with interval index \(j'\) appears in \(g_j\) only for these \(j\), so \(\sum_j\|g_j\|^2\le23\|g\|^2\).

**9.4.** With \(R=1\), \(|\langle f_j,\mathcal Ag_j\rangle|\le\|g_j\|(10^4HL^{4C}d_j)^{1/2}\), and Cauchy's inequality in \(j\) gives \(\sqrt{23}\|g\|(10^4HL^{4C}\mathfrak m)^{1/2}\)\(\ll UVL^{4C}(H\mathfrak m/(UV))^{1/2}\). Since \(H=x^{o(1)}\) exceeds every power of \(L\), one would need \(\mathfrak m\) smaller than \(UV/H\), a bound of a very different strength.

**9.5.** \(\log H^{1/(2R)}\le5KL^{0.21}/L^{0.5}\)\(=5KL^{-0.29}\to0\).

## References

- [PD] OpenAI, *The Poisson–Dirichlet law for prime predecessors*, OpenAI Math Release preprint, 24 September 2026, Section 3.3. https://github.com/openai/math/tree/main/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026
