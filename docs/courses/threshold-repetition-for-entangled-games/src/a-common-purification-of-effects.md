# A common purification of effects

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Conditioning a repeated strategy on observed answers replaces the shared state by local positive operators applied to it. To compare such conditioned states without communication, the players need a representation of each positive operator \(T\) by a map \(F\) with \(F^*F=T\) whose values lie in one common space, in such a way that averaging \(T\) over a random question moves \(F\) by an amount controlled by an entropy gap. This lesson constructs such a representation, the resolvent purification, proves its entropy estimate, and shows how answer measurements are transported to the represented vectors with exactly the same answer probabilities.

- The resolvent purification and its entropy estimate (Section 1).
- Transporting answer measurements (Section 2).

Hilbert spaces are complex and finite-dimensional unless stated otherwise. An *effect* on \(\mathcal H\) is a self-adjoint operator with \(0\preceq T\preceq I\). Put \(f(t)=t\log t\) for \(t>0\) and \(f(0)=0\); for an effect, \(f(T)\) is defined by the spectral theorem, and \(f(T)\preceq0\).

## 1. The resolvent purification and its entropy estimate

For an effect \(T\) on \(\mathcal H\) define
\[
\begin{aligned}
&\mathcal F_T\colon\mathcal H\to L^2\bigl((0,\infty),ds;\mathcal H\bigr),\\
&(\mathcal F_Th)(s)=T(T+sI)^{-1}h .
\end{aligned}
\]
The inverse exists for every \(s>0\), also when \(T\) has a kernel. For effects \(S,T\), the operator \(\mathcal F_S^*\mathcal F_T\) on \(\mathcal H\) is defined by \(\langle h,\mathcal F_S^*\mathcal F_Th'\rangle=\langle\mathcal F_Sh,\mathcal F_Th'\rangle_{L^2}\).

**Lemma 1.1** (resolvent purification; [OpenAI-TR, Lemma 3.1]).

(1) \(\mathcal F_T^*\mathcal F_T=T\) for every effect \(T\).

(2) Let \(A_1,\dots,A_N\) be effects, \(q_1,\dots,q_N>0\) with \(\sum_jq_j=1\), \(B=\sum_jq_jA_j\), and let \(\Delta=\sum_jq_jf(A_j)-f(B)\) be their *entropy gap*. Then for every \(h\in\mathcal H\)
\[
\begin{aligned}
&\sum_jq_j\|(\mathcal F_{A_j}-\mathcal F_B)h\|^2\\
&\quad\le\langle h,\Delta h\rangle .
\end{aligned} \tag{1.1}
\]

(3) For a finite set \(\mathscr T\) of effects, the maps \(\mathcal F_T\), \(T\in\mathscr T\), take values in a common finite-dimensional subspace \(\mathcal K\) of \(L^2((0,\infty),ds;\mathcal H)\); regarded as maps into \(\mathcal K\), they have the same products \(\mathcal F_S^*\mathcal F_T\).

*Proof.* (1) Write \(T=\sum_k\lambda_kP_k\) with spectral projections \(P_k\). Then
\[
\begin{aligned}
&\|\mathcal F_Th\|^2\\
&\quad=\sum_k\|P_kh\|^2\int_0^\infty\frac{\lambda_k^2}{(\lambda_k+s)^2}\,ds\\
&\quad=\sum_k\lambda_k\|P_kh\|^2=\langle h,Th\rangle,
\end{aligned}
\]
since \(\int_0^\infty t^2(t+s)^{-2}\,ds=t\) for \(t\ge0\); polarization gives \(\mathcal F_T^*\mathcal F_T=T\).

(2) *Reduction.* If \(Bh=0\), then \(\sum_jq_j\langle h,A_jh\rangle=0\), so \(\langle h,A_jh\rangle=0\) and \(A_jh=0\) for every \(j\). So \(\ker B\) is contained in every \(\ker A_j\); all the operators in (1.1) vanish on \(\ker B\) and map its orthogonal complement into itself. Both sides of (1.1) split accordingly, and on \(\ker B\) they vanish. We may therefore assume \(B\) positive definite, with smallest eigenvalue \(b>0\).

*Two resolvent identities.* Write \(R_A=(A+sI)^{-1}\), \(D_j=A_j-B\) and, for effects \(A,B\), \(D=A-B\). Since \(R_A^{-1}-R_B^{-1}=D\),
\[
\begin{aligned}
&R_B-R_A=R_ADR_B,\\
&AR_A-BR_B\\
&\quad=s(R_B-R_A)\\
&\quad=sR_ADR_B .
\end{aligned} \tag{1.2}
\]
Substituting the first identity into itself, in the form \(R_A=R_B-R_ADR_B\),
\[
\begin{aligned}
R_A&=R_B-R_BDR_B\\
&\quad+R_BDR_ADR_B .
\end{aligned} \tag{1.3}
\]

*The entropy gap.* For \(t\ge0\),
\[
f(t)=\int_0^\infty\Bigl(\frac t{1+s}-\frac t{t+s}\Bigr)ds,
\]
because \(\int_0^S(\frac t{1+s}-\frac t{t+s})\,ds=t\log t+t\log\frac{1+S}{t+S}\) for \(t>0\). By the spectral theorem \(f(A)=\int_0^\infty(\frac A{1+s}-AR_A)\,ds\) for every effect \(A\), the integral converging in norm. Since \(\sum_jq_jA_j=B\), the terms \(A_j/(1+s)\) cancel in the average, and \(AR_A=I-sR_A\) gives
\[
\begin{aligned}
\Delta&=\int_0^\infty s\sum_jq_j(R_{A_j}-R_B)\,ds\\
&=\int_0^\infty s\sum_jq_jR_BD_jR_{A_j}D_jR_B\,ds,
\end{aligned}
\]
where the second equality averages (1.3) and uses \(\sum_jq_jD_j=0\). The last integrand is bounded near \(s=0\), because \(\|R_B\|\le1/b\) and \(sR_{A_j}\preceq I\), and it is \(O(s^{-2})\) as \(s\to\infty\).

*The estimate.* By (1.2), \(((\mathcal F_{A_j}-\mathcal F_B)h)(s)=sR_{A_j}D_jR_Bh\). Since \(sR_A^2\preceq R_A\) (the function \(s/(a+s)^2\) is at most \(1/(a+s)\) for \(a\ge0\)),
\[
\begin{aligned}
&\|sR_{A_j}D_jR_Bh\|^2\\
&\quad=s^2\langle D_jR_Bh,R_{A_j}^2D_jR_Bh\rangle\\
&\quad\le s\langle D_jR_Bh,R_{A_j}D_jR_Bh\rangle .
\end{aligned}
\]
Averaging over \(j\) with weights \(q_j\) and integrating over \(s\) gives (1.1), by the formula for the entropy gap.

(3) The span \(\mathcal K\) of all vectors \(\mathcal F_Th\), \(T\in\mathscr T\), \(h\in\mathcal H\), has dimension at most \(|\mathscr T|\dim\mathcal H\). Regarding each \(\mathcal F_T\) as a map into \(\mathcal K\) preserves all inner products of their values. \(\square\)

The common codomain matters: compressing different maps into different spaces would not preserve the distances \(\|(\mathcal F_{A_j}-\mathcal F_B)h\|\) in (1.1). In what follows each \(\mathcal F_T\) is regarded as a map into a fixed finite-dimensional space \(\mathcal K\), chosen for the finitely many effects at hand. The construction and its entropy estimate are those of Chapter 6 of [OpenAI-TA] (Definition 4.2 and Lemma 4.3 there). In particular the entropy gap \(\Delta\) is positive semidefinite.

## 2. Transporting answer measurements

**Lemma 2.1** (transporting measurements; [OpenAI-TR, Lemma 3.2]). Let \(T\) be an effect on \(\mathcal H\), let \(F\colon\mathcal H\to\mathcal K\) satisfy \(F^*F=T\), and let \((G_a)_{a\in\mathcal A}\) be positive operators on \(\mathcal H\), indexed by a nonempty finite set, with \(\sum_aG_a=T\). There is a POVM \((\widetilde G_a)_{a\in\mathcal A}\) on \(\mathcal K\), depending only on \(F\) and the \(G_a\), with
\[
F^*\widetilde G_aF=G_a\quad(a\in\mathcal A). \tag{2.1}
\]

*Proof.* Inverses and square roots below act on the support of \(T\), the orthogonal complement of its kernel, and vanish on the kernel; \(\Pi_T\) is the orthogonal projection onto the support. Since \(0\preceq G_a\preceq T\), each \(G_a\) vanishes on \(\ker T\) and \(G_a=\Pi_TG_a\Pi_T\). Since \(\|Fh\|^2=\langle h,Th\rangle\), \(F\) vanishes on \(\ker T\). Put \(V=FT^{-1/2}\). Then \(V^*V=T^{-1/2}TT^{-1/2}=\Pi_T\), so \(V\) is a partial isometry, \(VV^*\) is an orthogonal projection on \(\mathcal K\), and \(VT^{1/2}=F\Pi_T=F\). Fix \(a_*\in\mathcal A\) and put
\[
\begin{aligned}
\widetilde G_a&=VT^{-1/2}G_aT^{-1/2}V^*\\
&\quad+\mathbf 1_{\{a=a_*\}}(I_{\mathcal K}-VV^*).
\end{aligned}
\]
These are positive, and \(\sum_a\widetilde G_a=V\Pi_TV^*+I_{\mathcal K}-VV^*=I_{\mathcal K}\). Finally, because \(V^*(I-VV^*)V=0\),
\[
\begin{aligned}
F^*\widetilde G_aF&=T^{1/2}V^*V\,T^{-1/2}G_aT^{-1/2}\\
&\qquad\cdot V^*VT^{1/2}+0\\
&=\Pi_TG_a\Pi_T=G_a .
\end{aligned}
\]
If \(T=0\), every \(G_a\) and \(V\) vanish and the POVM always gives \(a_*\). \(\square\)

**Corollary 2.2.** Let \(T,S\) be effects on \(\mathcal H_A,\mathcal H_B\), with maps \(F_T\colon\mathcal H_A\to\mathcal K_A\) and \(F_S\colon\mathcal H_B\to\mathcal K_B\) satisfying \(F_T^*F_T=T\) and \(F_S^*F_S=S\). Let \(\sum_aG_a=T\) and \(\sum_bH_b=S\) with positive \(G_a,H_b\), and let \(\widetilde G_a,\widetilde H_b\) be the POVMs of Lemma 2.1. For a unit vector \(\psi\in\mathcal H_A\otimes\mathcal H_B\) and \(\Psi=(F_T\otimes F_S)\psi\),
\[
\begin{aligned}
&\|\Psi\|^2=\langle\psi,(T\otimes S)\psi\rangle,\\
&\langle\Psi,(\widetilde G_a\otimes\widetilde H_b)\Psi\rangle=\langle\psi,(G_a\otimes H_b)\psi\rangle .
\end{aligned}
\]

*Proof.* For operators \(X\) on \(\mathcal K_A\) and \(Y\) on \(\mathcal K_B\),
\[
\begin{aligned}
&(F_T\otimes F_S)^*(X\otimes Y)(F_T\otimes F_S)\\
&\quad=F_T^*XF_T\otimes F_S^*YF_S ;
\end{aligned}
\]
take \(X,Y\) equal to identities, or to \(\widetilde G_a,\widetilde H_b\), and use (2.1). \(\square\)

So the purified vector carries the exact answer probabilities, not only the norm of the conditioned vector. The transport of answer effects follows the construction of the ideal conditioned state in Chapter 6 of [OpenAI-TA] (Lemma 3.2 there).

## 3. Exercises

**3.1.** Prove \(\int_0^\infty t^2(t+s)^{-2}\,ds=t\) for \(t\ge0\).

**3.2.** Let \(A_1=1\), \(A_2=0\) on \(\mathcal H=\mathbb C\) and \(q_1=q_2=\frac12\), so \(B=\frac12\). Compute both sides of (1.1) for \(h=1\).

**3.3.** Show that the right side of (1.1) is nonnegative directly from the concavity of \(-t\log t\) when all \(A_j\) commute.

**3.4.** In Lemma 2.1, show that the pullbacks \(F^*\widetilde G_aF\) do not depend on the choice of \(a_*\), although the POVM does.

**3.5.** Show that \(T^{1/2}\colon\mathcal H\to\mathcal H\) also satisfies \((T^{1/2})^*T^{1/2}=T\), and compute \(\|T^{1/2}h-S^{1/2}h\|^2\) and \(\|(\mathcal F_T-\mathcal F_S)h\|^2\) for \(\mathcal H=\mathbb C\), \(T=1\), \(S=0\), \(h=1\).

## 4. Solutions

**3.1.** For \(t>0\), \(\int_0^\infty(t+s)^{-2}\,ds=1/t\); for \(t=0\) both sides vanish.

**3.2.** \(\mathcal F_1(s)=1/(1+s)\), \(\mathcal F_0=0\), \(\mathcal F_{1/2}(s)=1/(1+2s)\). The left side is \(\frac12\int_0^\infty\bigl(\frac1{1+s}-\frac1{1+2s}\bigr)^2ds+\frac12\int_0^\infty\frac{ds}{(1+2s)^2}\). The second integral is \(\frac12\); the first equals \(\int_0^\infty\frac{s^2}{(1+s)^2(1+2s)^2}\,ds=\frac32-2\log2\) (partial fractions). So the left side is \(\frac12(\frac32-2\log2)+\frac14=1-\log2\approx0.307\). The right side is \(\frac12(0+0)-\frac12\log\frac12=\frac12\log2\approx0.347\).

**3.3.** In a common eigenbasis the inequality reads \(\sum_jq_jf(a_j)\ge f(\sum_jq_ja_j)\) for each eigenvalue, which is convexity of \(f\).

**3.4.** \(F^*(I-VV^*)F\) equals \(T^{1/2}V^*(I-VV^*)VT^{1/2}=0\), so the extra term never contributes to the pullback.

**3.5.** \((T^{1/2})^*T^{1/2}=T\). With \(T=1\), \(S=0\), \(h=1\): \(\|T^{1/2}h-S^{1/2}h\|^2=1\), and \(\|(\mathcal F_1-\mathcal F_0)h\|^2=\int_0^\infty(1+s)^{-2}ds=1\). Both equal \(\langle h,(T-S)h\rangle\) here.

## References

- [OpenAI-TR] OpenAI, *Threshold parallel repetition for finite-dimensional entangled games*, OpenAI Math Release preprint, 25 September 2026, Lemmas 3.1 and 3.2. https://github.com/openai/math/tree/main/preprints/Threshold-parallel-repetition-for-finite-dimensional-entangled-games-September-25-2026
- [OpenAI-TA] OpenAI, *Ten Advances in Mathematics and Theoretical Computer Science*, report, updated 6 August 2026, Chapter 6, Lemma 3.2, Definition 4.2, Lemma 4.3. https://cdn.openai.com/pdf/ten-proofs-oai.pdf
