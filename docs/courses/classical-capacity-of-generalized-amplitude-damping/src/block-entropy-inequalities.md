# Block entropy inequalities

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

When a qubit and a second system are in a joint pure state, one use of the damping channel on the qubit produces a block matrix whose blocks are built from the outputs of the second system's two conditional states. This lesson proves the two entropy inequalities for such block matrices on which the whole course rests. The first concerns a Gram matrix \(MM^*\) of a two-by-two block matrix \(M\) with one zero block: its entropy is at least the weighted entropies of the three blocks plus the entropy of the scalar matrix of their norms (Theorem 1.1). The second extends this to the block matrices that appear for thermal damping, which have no zero block, by writing them as mixtures of two zero-block matrices with the same scalar term (Theorem 2.1).

- The zero-block inequality (Theorem 1.1).
- The thermal block inequality (Theorem 2.1) and its sharpness (Remark 2.2).

The lesson follows [OpenAI-GAD, Sections 2 and 3]. It uses the integral formula, the joint convexity and the scalar deficit of [Entropy differences and log-determinants](entropy-differences-and-log-determinants.md), and the facts on entropy of [Quantum channels and Holevo information](quantum-channels-and-holevo-information.md), Section 2, in particular concavity (Proposition 2.1 there).

## 1. The zero-block inequality

**Theorem 1.1** ([OpenAI-GAD, Theorem 2.1]). Let \(A,B,C\in\mathbb C^{d\times e}\) and
\[
\begin{gathered}
M=\begin{pmatrix}A&B\\ C&0\end{pmatrix},\qquad x=\operatorname{Tr}AA^*,\\
y=\operatorname{Tr}BB^*,\qquad z=\operatorname{Tr}CC^*.
\end{gathered}
\]
If \(x+y+z=1\), then
\[
\begin{aligned}
S(MM^*)&\ge xS\Bigl(\frac{AA^*}x\Bigr)+yS\Bigl(\frac{BB^*}y\Bigr)\\
&\quad+zS\Bigl(\frac{CC^*}z\Bigr)+g(yz),
\end{aligned}
\]
where a term with zero weight is omitted.

The term \(g(yz)\) is the entropy of the Gram matrix of the scalar matrix \(\bigl(\begin{smallmatrix}\sqrt x&\sqrt y\\ \sqrt z&0\end{smallmatrix}\bigr)\) of the block norms: its trace is \(1\) and its determinant is \(yz\). For blocks of size \(1\times1\) the inequality is therefore an equality. The next section applies the theorem to block matrices without a zero block, by writing them as mixtures of matrices with one.

*Proof.* *The deficit.* Put
\[
\begin{aligned}
\Delta&=S(AA^*)+S(BB^*)\\
&\quad+S(CC^*)-S(MM^*).
\end{aligned}
\]
For \(x>0\), fact 3 of Section 2 of the first lesson gives \(S(AA^*)=xS(AA^*/x)-x\ln x\), and similarly for the other blocks; a block of mass zero is zero and contributes nothing. Since \(F(x,y,z)=H(x,y,z)-g(yz)\) on the simplex (Section 4 of the second lesson), the theorem is equivalent to
\[
\Delta\le F(x,y,z).
\]
We prove this inequality for all masses \(x,y,z\ge0\), first for square blocks.

*Square blocks.* Let \(d=e=N\). The matrices \(U=AA^*\oplus BB^*\oplus CC^*\) and \(V=MM^*\) have the same trace \(x+y+z\), so by Lemma 1.1 of the second lesson
\[
\Delta=\int_0^\infty\frac{f(r)}{r^2}\,dr,
\]
where \(f(r)\) is the difference of \(\ln\det(I+rU)\) and \(\ln\det(I+rV)\). Fix \(r>0\) and put \(D=I+rBB^*\) and \(E=I+rC^*C\). In block form, \(I+rMM^*\) has the diagonal blocks \(I+rAA^*+rBB^*\) and \(I+rCC^*\) and the off-diagonal blocks \(rAC^*\) and \(rCA^*\). Its lower right block is positive definite, and elimination gives
\[
\begin{aligned}
&\det(I+rMM^*)\\
&\quad=\det(I+rCC^*)\\
&\qquad\times\det(D+rA\,\Xi A^*),
\end{aligned}
\]
with \(\Xi=I-rC^*(I+rCC^*)^{-1}C\). Since \(C^*(I+rCC^*)^{-1}=(I+rC^*C)^{-1}C^*\), we have \(\Xi=(I+rC^*C)^{-1}=E^{-1}\). Therefore
\[
\begin{aligned}
&\det(I+rMM^*)\\
&\quad=\det(I+rCC^*)\\
&\qquad\times\det(D+rAE^{-1}A^*),
\end{aligned}
\]
and
\[
f(r)=\ln\det(I+rAA^*)-G_{\sqrt rA}(D,E),
\]
with the function \(G\) of Lemma 2.1 of the second lesson, because \(\ln\det(I+rBB^*)=\ln\det D\).

*Diagonal \(A\).* Choose a singular value decomposition \(A=U_A\Sigma V_A^*\) with unitaries \(U_A,V_A\). Replacing \((A,B,C)\) by \((\Sigma,U_A^*B,CV_A)\) replaces \(M\) by \(\operatorname{diag}(U_A^*,I)\,M\operatorname{diag}(V_A,I)\), which conjugates \(MM^*\), \(AA^*\) and \(BB^*\) by unitaries and leaves \(CC^*\) unchanged. All entropies and masses are preserved, so we may assume
\[
\begin{gathered}
A=\operatorname{diag}(\sqrt{x_1},\dots,\sqrt{x_N}),\\
y_i=(BB^*)_{ii},\qquad z_i=(C^*C)_{ii},
\end{gathered}
\]
with \(x_i,y_i,z_i\ge0\) and \(\sum_i(x_i,y_i,z_i)=(x,y,z)\).

*Averaging over signs.* For \(\varepsilon\in\{-1,1\}^N\) let \(S_\varepsilon=\operatorname{diag}(\varepsilon_1,\dots,\varepsilon_N)\). Since \(A\) and \(S_\varepsilon\) are diagonal, \(S_\varepsilon AS_\varepsilon=A\) and \(AS_\varepsilon=S_\varepsilon A\), so
\[
\begin{aligned}
&S_\varepsilon DS_\varepsilon+rA(S_\varepsilon ES_\varepsilon)^{-1}A\\
&\qquad=S_\varepsilon(D+rAE^{-1}A)S_\varepsilon ,
\end{aligned}
\]
and \(G_{\sqrt rA}(S_\varepsilon DS_\varepsilon,S_\varepsilon ES_\varepsilon)=G_{\sqrt rA}(D,E)\). The average of \(S_\varepsilon DS_\varepsilon\) over all \(2^N\) sign vectors is the diagonal part of \(D\), because the entry \((i,j)\) is multiplied by \(\varepsilon_i\varepsilon_j\), whose average is \(0\) for \(i\ne j\); likewise for \(E\). The diagonal parts are \(D'=\operatorname{diag}(1+ry_i)\) and \(E'=\operatorname{diag}(1+rz_i)\), and joint convexity (Lemma 2.1 of the second lesson) therefore gives
\[
G_{\sqrt rA}(D,E)\ge G_{\sqrt rA}(D',E').
\]
The right side is a sum of scalar terms, so \(f(r)\) is at most
\[
\begin{aligned}
\sum_i\Bigl[&\ln(1+rx_i)\\
&-\ln\Bigl(1+\frac{rx_i}{(1+ry_i)(1+rz_i)}\Bigr)\Bigr].
\end{aligned}
\]
By the integral formula in the proof of Proposition 4.1 of the second lesson, the \(i\)-th summand integrates against \(dr/r^2\) to \(F(x_i,y_i,z_i)\). Integrating, and using the superadditivity of \(F\),
\[
\Delta\le\sum_iF(x_i,y_i,z_i)\le F(x,y,z).
\]
Only inverses of positive definite matrices occur, also when \(A\), \(B\) or \(C\) is singular, so this covers all square blocks.

*Rectangular blocks.* For \(d\times e\) blocks let \(N=\max(d,e)\) and let \(J\colon\mathbb C^d\to\mathbb C^N\) and \(K\colon\mathbb C^e\to\mathbb C^N\) be the coordinate isometries. Replace each block \(X\) by \(JXK^*\). The new block matrix is \((J\oplus J)M(K\oplus K)^*\), whose Gram matrix \((J\oplus J)MM^*(J\oplus J)^*\) has the nonzero eigenvalues of \(MM^*\); the same holds for each block, and the masses do not change. So \(\Delta\) and \(F(x,y,z)\) do not change, and the square case applies. \(\blacksquare\)

Theorem 1.1 is the case of blocks of one common shape of the triangular block entropy inequality of Tang, Zhu, Bai and Wang [TZBW, Theorem 4.2], after exchanging the two block rows: their lower triangular matrix \(\bigl(\begin{smallmatrix}A'&0\\ B'&D'\end{smallmatrix}\bigr)\) becomes ours with \(A'=C\), \(B'=A\) and \(D'=B\), and their scalar term, written with the concurrence \(2\sqrt{\operatorname{Tr}A'A'^*\cdot\operatorname{Tr}D'D'^*}\), is \(g(yz)\). They allow blocks of different shapes; the case of a common shape is the one needed below.

## 2. The thermal block inequality

For thermal damping both excitation and decay occur, and the output of a branch decomposition has the following form.

**Theorem 2.1** ([OpenAI-GAD, Theorem 3.1]). Let \(X\) and \(Y\) be complex matrices of the same shape with \(\operatorname{Tr}XX^*=\operatorname{Tr}YY^*=1\). Let \(\alpha,\beta,\eta,\delta\ge0\) with \(\alpha+\beta+\eta+\delta=1\) and
\[
\alpha\delta-\beta\eta=K^2,\qquad K\ge0 .
\]
Put \(U_0=\alpha+\beta\), \(U_1=\eta+\delta\), \(u=U_0U_1-K^2\), and
\[
\begin{gathered}
T=\begin{pmatrix}T_{00}&KXY^*\\ KYX^*&T_{11}\end{pmatrix},\\
T_{00}=\alpha XX^*+\beta YY^*,\\
T_{11}=\eta XX^*+\delta YY^*.
\end{gathered}
\]
Then \(T\) is a state, \(0\le u\le\frac14\), and
\[
\begin{aligned}
S(T)&\ge(\alpha+\eta)S(XX^*)\\
&\quad+(\beta+\delta)S(YY^*)+g(u).
\end{aligned}
\]

No orthogonality of \(X\) and \(Y\), and no commutation of \(XX^*\) and \(YY^*\), is assumed.

*Proof.* *The parameter \(u\).* Expanding \(U_0U_1\) and subtracting \(K^2=\alpha\delta-\beta\eta\) gives
\[
u=\alpha\eta+2\beta\eta+\beta\delta=\beta U_1+\eta U_0 .
\]
Hence \(0\le u\le U_0U_1\le\frac14\), since \(U_0+U_1=1\).

*The case \(u>0\).* Then \(U_0,U_1>0\): if \(U_0=0\), then \(\alpha=\beta=0\), so \(K=0\) and \(u=0\); similarly for \(U_1\). Keep \(X\), \(Y\), \(K\), \(U_0\) and \(U_1\) fixed. Writing \(\alpha=U_0-\beta\) and \(\delta=U_1-\eta\), the condition \(\alpha\delta-\beta\eta=K^2\) becomes the linear equation \(U_1\beta+U_0\eta=u\), whose nonnegative solutions form the segment from \((\beta,\eta)=(u/U_1,0)\) to \((0,u/U_0)\). At each end one coefficient vanishes. The two ends give the coefficient sets
\[
\begin{gathered}
\alpha_1=\frac{K^2}{U_1},\quad\beta_1=\frac u{U_1},\\
\eta_1=0,\quad\delta_1=U_1;\\
\alpha_2=U_0,\quad\beta_2=0,\\
\eta_2=\frac u{U_0},\quad\delta_2=\frac{K^2}{U_0},
\end{gathered}
\]
and the weights that express the given coefficients as their mixture are
\[
w_1=\frac{\beta U_1}u,\qquad w_2=\frac{\eta U_0}u .
\]
Both sets are nonnegative with \(\alpha_i+\beta_i=U_0\) and \(\eta_i+\delta_i=U_1\), because \(K^2+u=U_0U_1\); so each set sums to \(1\), and \(\alpha_i\delta_i-\beta_i\eta_i=K^2\). The weights satisfy \(w_1+w_2=1\) by the formula for \(u\), and
\[
\begin{gathered}
w_1\beta_1+w_2\beta_2=\beta,\\
w_1\eta_1+w_2\eta_2=\eta ;
\end{gathered}
\]
with the fixed sums \(U_0\) and \(U_1\), the mixture also recovers \(\alpha\) and \(\delta\).

Let \(T_i\) be the matrix \(T\) built with the coefficient set \(i\). Both have the off-diagonal blocks \(KXY^*\) and \(KYX^*\), so \(T=w_1T_1+w_2T_2\). Each is a Gram matrix with a zero block:
\[
\begin{gathered}
M_1=\begin{pmatrix}\sqrt{\alpha_1}X&\sqrt{\beta_1}Y\\ \sqrt{\delta_1}Y&0\end{pmatrix},\\
M_2=\begin{pmatrix}\sqrt{\alpha_2}X&0\\ \sqrt{\delta_2}Y&\sqrt{\eta_2}X\end{pmatrix},\\
T_i=M_iM_i^* ,
\end{gathered}
\]
using \(\eta_1=\beta_2=0\) and \(\sqrt{\alpha_i\delta_i}=K\). In particular \(T_1\), \(T_2\) and \(T\) are positive semidefinite with trace \(1\). Apply Theorem 1.1 to \(M_1\), and to \(M_2\) after exchanging its two block rows, which conjugates \(M_2M_2^*\) by a unitary. The products of the masses of the two blocks next to the zero block are
\[
\beta_1\delta_1=u,\qquad\eta_2\alpha_2=u ,
\]
so the same scalar term \(g(u)\) appears in both inequalities:
\[
\begin{aligned}
S(T_i)&\ge(\alpha_i+\eta_i)S(XX^*)\\
&\quad+(\beta_i+\delta_i)S(YY^*)+g(u).
\end{aligned}
\]
Concavity of entropy, \(S(T)\ge w_1S(T_1)+w_2S(T_2)\), and the mixture identities for the coefficients give the claim. A zero weight does not affect the argument.

*The case \(u=0\).* If \(U_0=0\), then \(\alpha=\beta=0\) and \(K=0\), so \(T=0\oplus(\eta XX^*+\delta YY^*)\) with \(\eta+\delta=1\); it is a state, and concavity and \(g(0)=0\) give the claim. The case \(U_1=0\) is the same. If \(U_0,U_1>0\), then \(u=\beta U_1+\eta U_0=0\) forces \(\beta=\eta=0\) and \(K=\sqrt{\alpha\delta}\). Then \(T=MM^*\) for
\[
M=\begin{pmatrix}\sqrt\alpha X&0\\ \sqrt\delta Y&0\end{pmatrix},
\]
which is the matrix \(M_1\) built with the coefficients \((\alpha,0,0,\delta)\). So \(T\) is a state, and Theorem 1.1, with a zero block mass, gives \(S(T)\ge\alpha S(XX^*)+\delta S(YY^*)\), which is the claim because \(\beta=\eta=0\) and \(g(0)=0\). \(\blacksquare\)

**Remark 2.2** (sharpness). For \(X=Y\),
\[
T=\begin{pmatrix}U_0&K\\K&U_1\end{pmatrix}\otimes XX^* ,
\]
the first factor is a state on \(\mathbb C^2\) with determinant \(u\), and \(S(T)=g(u)+S(XX^*)\), which is the right side of Theorem 2.1. So the inequality is sharp for every admissible choice of coefficients.

## 3. Exercises

**3.1.** Let \(R\) be a matrix with \(\operatorname{Tr}RR^*=1\), and \(A=\sqrt xR\), \(B=\sqrt yR\), \(C=\sqrt zR\) with \(x+y+z=1\). Show that Theorem 1.1 holds with equality.

**3.2.** Show that Theorem 1.1 with \(z=0\), and with \(y=0\), is the concavity of entropy for two states.

**3.3.** Show that \(g(yz)\) in Theorem 1.1 cannot be replaced by a larger function of \(yz\).

**3.4.** For \(\alpha=\delta=0.4\) and \(\beta=\eta=0.1\), compute \(K\), \(u\), the two coefficient sets and the weights in the proof of Theorem 2.1, and check the mixture identities.

**3.5.** In Theorem 2.1 let \(K=0\), that is \(\alpha\delta=\beta\eta\), with \(U_0,U_1>0\). Show that the inequality follows directly from the concavity of entropy.

## 4. Solutions

**3.1.** Here \(M=\bigl(\begin{smallmatrix}\sqrt x&\sqrt y\\ \sqrt z&0\end{smallmatrix}\bigr)\otimes R\) in block form, so \(MM^*\) is the tensor product of the scalar Gram matrix, with entropy \(g(yz)\), and \(RR^*\). Hence \(S(MM^*)=g(yz)+S(RR^*)\), and the right side is \((x+y+z)S(RR^*)+g(yz)\).

**3.2.** For \(z=0\), \(C=0\) and \(MM^*=(AA^*+BB^*)\oplus0\); the inequality says that \(S(AA^*+BB^*)\) is at least \(xS(AA^*/x)+yS(BB^*/y)\), with \(x+y=1\). For \(y=0\), \(B=0\), and \(MM^*\) is the Gram matrix of the column \(\bigl(\begin{smallmatrix}A\\ C\end{smallmatrix}\bigr)\), whose nonzero eigenvalues are those of \(A^*A+C^*C\); the inequality says that \(S(A^*A+C^*C)\) is at least \(xS(A^*A/x)+zS(C^*C/z)\), using \(S(AA^*)=S(A^*A)\).

**3.3.** For \(1\times1\) blocks \(S(MM^*)=g(yz)\) and the block entropies vanish (Exercise 3.1 with \(R=(1)\)). If a function \(\phi\) with \(\phi(yz)>g(yz)\) for some admissible \(y,z\) replaced \(g\), the inequality would fail for those scalar blocks.

**3.4.** \(K^2=0.16-0.01=0.15\), \(U_0=U_1=0.5\), \(u=0.25-0.15=0.1\). The first set is \((0.3,0.2,0,0.5)\) with \(w_1=0.05/0.1=0.5\), the second \((0.5,0,0.2,0.3)\) with \(w_2=0.5\). Then \(0.5\cdot0.2=0.1=\beta=\eta\), \(0.5(0.3+0.5)=0.4=\alpha\) and \(0.5(0.5+0.3)=0.4=\delta\); each set has \(\alpha_i\delta_i=0.15\).

**3.5.** The off-diagonal blocks vanish, so \(T=T_0\oplus T_1\) with \(T_0=\alpha XX^*+\beta YY^*\) of trace \(U_0\) and \(T_1=\eta XX^*+\delta YY^*\) of trace \(U_1\). By facts 2 and 3 of Section 2 of the first lesson,
\[
\begin{aligned}
S(T)&=U_0S\Bigl(\frac{T_0}{U_0}\Bigr)+U_1S\Bigl(\frac{T_1}{U_1}\Bigr)\\
&\quad+h(U_0).
\end{aligned}
\]
Concavity gives \(U_0S(T_0/U_0)\ge\alpha S(XX^*)+\beta S(YY^*)\) and \(U_1S(T_1/U_1)\ge\eta S(XX^*)+\delta S(YY^*)\). Finally \(u=U_0U_1=U_0(1-U_0)\), so \(g(u)=h(U_0)\).

## References

- [OpenAI-GAD] OpenAI, *Classical capacity and entropy inequalities for generalized amplitude damping*, OpenAI Math Release preprint, 24 September 2026, Sections 2 and 3. https://github.com/openai/math/tree/main/preprints/Classical-capacity-and-entropy-inequalities-for-generalized-amplitude-damping-September-24-2026
- [TZBW] Z. Tang, C. Zhu, G. Bai and X. Wang, *Classical capacity and entanglement cost of the amplitude damping channel*, arXiv:2609.28592 (2026), Theorem 4.2. https://arxiv.org/abs/2609.28592
