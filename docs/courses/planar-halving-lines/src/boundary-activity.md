# Boundary activity

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the packing theorem, and with it Theorems A and B [OpenAI-HL, Section 7]. The finite observation is that, while the cutting lines of a short stretch of the sweep turn by a small angle \(\theta\), every participating vertex in a fixed region either lies in one of three strips of width about \(\theta\), or is accounted for by a token crossing the boundary of the region. Tokens move in a fixed cone of directions, so each crosses the boundary at most twice in all. In the limit, the spatial measure of [A spatial measure](a-spatial-measure.md) gives strips little mass, the angles add up to at most \(\pi\), and the boundary crossings add up to a bounded amount; Hölder's inequality then contradicts the positive edge mass of the good set.

## 1. Three strips

**Lemma 1.1** (three strips). Let \(P\) be a finite set in the plane, \(B\) a bounded open set and \(D\ge1\) with \(|x|\le D\) for \(x\in B\). Let \(M_0,\dots,M_m\subseteq P\) have the same number of points and be given by cuts
\[
\begin{gathered}
M_i=\{x\in P:\nu_i\cdot x<c_i\},\\
|\nu_i|=1,\qquad|\nu_i-\nu_0|\le\theta,
\end{gathered}
\]
with no point of \(P\) on any line \(\nu_i\cdot x=c_i\). For \(i\ge1\) fix a bijection from \(M_{i-1}\setminus M_i\) onto \(M_i\setminus M_{i-1}\), the *transfers* of step \(i\), and let \(C_B\) be the number of transfers with exactly one endpoint in \(B\). Let \(A=\bigcup_{i\ge1}(M_{i-1}\triangle M_i)\) be the set of *participating* points. Put \(\rho=D\theta\), \(c_-=\min c_i\), \(c_+=\max c_i\), and for \(q\in\{c_0,c_-,c_+\}\) let \(S_q=\{x:|\nu_0\cdot x-q|\le3\rho\}\). Then
\[
\#\bigl((A\cap B)\setminus(S_{c_0}\cup S_{c_-}\cup S_{c_+})\bigr)\le2C_B ,
\]
and hence \(\#(A\cap B)\le2C_B+\sum_q\#(P\cap B\cap S_q)\).

*Proof.* Write \(t(x)=\nu_0\cdot x\) and \(e_i(x)=(\nu_i-\nu_0)\cdot x\); for \(x\in B\), \(|e_i(x)|\le\rho\). Let \(S\) be the union of the three strips.

*Initially marked participants.* Let \(x\in(A\cap B)\setminus S\) with \(x\in M_0\). Then \(t(x)<c_0\), and outside \(S_{c_0}\), \(t(x)<c_0-3\rho\). Since \(x\) participates, it is unmarked at some \(i\): \(t(x)+e_i(x)>c_i\ge c_-\), so \(t(x)>c_--\rho\), and outside \(S_{c_-}\), \(t(x)>c_-+3\rho\). At an index \(i_-\) with \(c_{i_-}=c_-\), \(\nu_{i_-}\cdot x\ge t(x)-\rho>c_-\): \(x\notin M_{i_-}\). The existence of such an \(x\) gives \(c_0-c_->6\rho\). Then every \(y\in(P\cap B)\setminus M_0\) has \(\nu_{i_-}\cdot y\ge t(y)-\rho>c_0-\rho>c_-\), so \(y\notin M_{i_-}\): between the states \(0\) and \(i_-\), no point of \(B\) is gained, and \(M_{i_-}\cap B\subseteq M_0\cap B\).

Put a token on each point of \(M_0\) and move the tokens along the transfers, one step at a time. At each state the tokens occupy exactly the points of \(M_i\). So
\[
\#(M_0\cap B)-\#(M_{i_-}\cap B)
\]
equals the number of transfers leaving \(B\) minus the number entering \(B\) during the first \(i_-\) steps, which is at most \(C_B\). The left side counts the points of \(M_0\cap B\) lost by state \(i_-\), among them all the \(x\) considered.

*Initially unmarked participants.* For \(x\in(A\cap B)\setminus S\) with \(x\notin M_0\), symmetrically \(t(x)>c_0+3\rho\) and \(t(x)<c_+-3\rho\), so \(x\in M_{i_+}\) for an index with \(c_{i_+}=c_+\); every point of \(M_0\cap B\) is still marked at \(i_+\), and the gains in \(B\) up to state \(i_+\) number at most \(C_B\). The two classes together have at most \(2C_B\) points. \(\square\)

The lemma includes \(\theta=0\), when the strips have width zero, and points that change several times and return to their initial status.

## 2. Tokens and the boundary of a region

We keep the extremal sequence, the subsequence and the enhanced limiting measures of [A spatial measure](a-spatial-measure.md): the window \(K_0\) with closure in \((t_1,t_2)\), the set \(G\) with \(\lambda_{K_0}(G)>0\), the spatial measure \(\beta\), carried by the closed unit disk, with \(\beta(B(x,r))\le C_Gr^{d_*}\), \(d_*=32/17\), and the normalized plane of each configuration, the image of the original plane under an affine bijection \(\Psi_n\) whose linear part maps the lines of slopes \(\varsigma(t_1),\varsigma(t_2),\varsigma(t_3)\) to \(\mathbb Rv_1,\mathbb Rv_2,\mathbb Rv_3\).

*The cone of transfers.* In late configurations every batch of \(K_0\) lies strictly between the batches containing the times \(t_1\) and \(t_2\), so every exchange edge of \(K_0\), from a lost point to a gained point, points to the right with slope strictly between \(\varsigma(t_1)\) and \(\varsigma(t_2)\) (Lemma 3.1 of [Chains, crossings and Dey's bound](chains-crossings-and-deys-bound.md)). These vectors lie in the cone spanned by \((1,\varsigma(t_1))\) and \((1,\varsigma(t_2))\), which \(\Psi_n\) maps to a closed quadrant spanned by \(\pm v_1\) and \(\pm v_2\). Passing to a subsequence, it is one fixed closed quadrant \(\mathcal Q\). Choose linearly independent linear functionals \(\ell_1,\ell_2\) positive on \(\mathcal Q\setminus\{0\}\); for \(\mathcal Q=\{\epsilon_1x\ge0,\ \epsilon_2y\ge0\}\), \(\ell_1=2\epsilon_1x+\epsilon_2y\) and \(\ell_2=\epsilon_1x+2\epsilon_2y\) will do. Choose the open parallelogram
\[
\begin{aligned}
B=\{x:{}&a_1<\ell_1(x)<b_1,\\
&a_2<\ell_2(x)<b_2\}
\end{aligned}
\]
containing the closed unit disk, and \(D\ge\max(1,\sup_{x\in B}|x|)\).

*Tokens.* In each batch of \(K_0\) fix one perfect matching from the lost points to the gained points, and move tokens, starting on the marked points at the beginning of \(K_0\), along these matchings; there are at most \(N\) tokens. Each move of a token is a transfer vector in \(\mathcal Q\setminus\{0\}\) after normalization, so \(\ell_1\) and \(\ell_2\) increase strictly along every token's path. The set of times at which a token lies in \(B\) is therefore an interval of consecutive times: if the token is in \(B\) at two times, both functionals lie between their values at those times in between. So each token enters \(B\) at most once and leaves it at most once, and the number of transfers of \(K_0\) with exactly one endpoint in \(B\) is at most \(2N\).

*Budgets.* For a window \(J\subseteq K_0\) in configuration \(n\), let \(C_n(J)\) be the number of these transfers in the batches of \(J\), and \(\theta_n(J)\) the angle spanned, in the normalized plane, by the lines of the states bounding the batches of \(J\). The slopes of the states increase, so their lines turn monotonically in the original plane, and also after \(\Psi_n\), within half a turn; windows of a partition span angles with disjoint interiors. So for every partition of \(K_0\) into windows,
\[
\sum_J\frac{C_n(J)}N\le2,\qquad\sum_J\theta_n(J)\le\pi .
\]
Along a diagonal subsequence, \(C_n(J)/N\to b_J\) and \(\theta_n(J)\to\theta_J\) for all the countably many windows \(J\subseteq K_0\), and for every partition \(\sum_Jb_J\le2\) and \(\sum_J\theta_J\le\pi\).

## 3. Limiting boundary activity

**Lemma 3.1.** For every window \(J\subseteq K_0\), with \(\mu_J(G)\) the limiting participating-vertex measure of \(J\) of the labels in \(G\),
\[
\mu_J(G)\le2b_J+C_G'\theta_J^{\,d_*-1},
\]
where \(C_G'\) depends only on \(C_G\) and \(D\).

*Proof.* In configuration \(n\) apply Lemma 1.1 in the normalized plane to the marked sets at the states bounding the batches of \(J\), with the chosen matchings as transfers; the participating points are the endpoints of the exchange edges of \(J\). Each marked set is the set of points below a line of the state's slope, strictly, so after \(\Psi_n\) it is given by a cut \(\nu_i\cdot x<c_i\) with unit normals \(\nu_i\) chosen continuously; they turn within the angle \(\theta_n(J)\), so \(|\nu_i-\nu_0|\le\theta_n(J)\). Passing to a further subsequence, the normal \(\nu_0\) and the three thresholds \(c_0,c_-,c_+\) converge, possibly to \(\pm\infty\), simultaneously for all windows. A finite limit gives a closed limiting strip of half-width \(3D\theta_J\); a threshold tending to infinity gives strips that eventually miss every bounded set. Let \(\mathcal S_J\) be the union of the at most three limiting strips.

Let \(\alpha_n\) be the image on the position coordinate of the participating-vertex measure of \(J\), with mass \(1/N\) per vertex, and \(\alpha\) its limit. A continuous \(f\) with \(0\le f\le1\) and compact support in the open set \(B\setminus\mathcal S_J\) is, for late \(n\), zero on the three strips of configuration \(n\), since its support has positive distance from the limiting strips. By Lemma 1.1, \(\int f\,d\alpha_n\le2C_n(J)/N\), so \(\int f\,d\alpha\le2b_J\), and exhausting the open set, \(\alpha(B\setminus\mathcal S_J)\le2b_J\). The positions of the labels in \(G\) lie in the closed unit disk inside \(B\), and \(\mu_J\le\mu\), so
\[
\begin{aligned}
\mu_J(G)&\le\alpha(B\setminus\mathcal S_J)+\beta(\mathcal S_J)\\
&\le2b_J+\beta(\mathcal S_J).
\end{aligned}
\]
By Proposition 1.1(c) of [A spatial measure](a-spatial-measure.md), a strip of half-width \(r\) has \(\beta\)-mass at most \(C r^{d_*-1}\) for \(r<1\), and at most \(1\) in any case; so \(\beta(\mathcal S_J)\le C'_G\theta_J^{\,d_*-1}\), including \(\theta_J=0\), when the strips are lines. \(\square\)

## 4. The contradiction

Let \(\alpha_*=d_*-1=15/17\). Fix \(M\ge1\) and divide \(K_0\) into the windows \(J\) of length \(\delta=2^{-m}\), at most \(\delta^{-1}\) of them. By Lemma 1.1(d) of [Limiting measures](limiting-measures.md), at most \(C_1M^{-4/3}\delta^{-1}\) of them have \(s_J>M\delta^{3/4}\); each has \(\lambda_J\)-mass \(\delta\), so together they carry at most \(C_1M^{-4/3}\) of \(\lambda_{K_0}(G)\). For the other windows, Lemma 2.1 of [Limiting measures](limiting-measures.md), for the enhanced labels, gives \(\lambda_J(G)\le C^{1/3}M\delta^{3/4}\mu_J(G)^{1/3}\). By Hölder's inequality, Lemma 3.1, the budgets, and concavity of \(\theta\mapsto\theta^{\alpha_*}\),
\[
\begin{aligned}
&\sum_J\mu_J(G)^{1/3}\le\delta^{-2/3}\Bigl(\sum_J\mu_J(G)\Bigr)^{1/3}\\
&\quad\le\delta^{-2/3}\Bigl(4+C_G'\sum_J\theta_J^{\alpha_*}\Bigr)^{1/3},\\
&\sum_J\theta_J^{\alpha_*}\le\delta^{\alpha_*-1}\Bigl(\sum_J\theta_J\Bigr)^{\alpha_*}\le\pi\,\delta^{\alpha_*-1}.
\end{aligned}
\]
Since \(\delta^{\alpha_*-1}\ge1\), the bracket is at most \((4+\pi C_G')\delta^{\alpha_*-1}\), and
\[
\begin{aligned}
&\lambda_{K_0}(G)=\sum_J\lambda_J(G)\\
&\quad\le C_1M^{-4/3}+C''M\,\delta^{3/4-2/3+(\alpha_*-1)/3}\\
&\quad=C_1M^{-4/3}+C''M\,\delta^{3/68},
\end{aligned}
\]
because \(\frac34-\frac23-\frac2{51}=\frac{153-136-8}{204}=\frac{9}{204}=\frac3{68}\). Let \(\delta\to0\) with \(M\) fixed, and then \(M\to\infty\): \(\lambda_{K_0}(G)=0\). This contradicts \(\lambda_{K_0}(G)>0\).

**Conclusion.** No extremal sequence exists, so Theorem 4.1 of [From packing to a power saving](from-packing-to-a-power-saving.md) holds. By Lemma 4.2 there, the packing theorem (Theorem 1.1) holds, and by Proposition 3.1 there, Theorems A and B are proved. The exponent \(3/68\) only serves this contradiction; the saving \(\varepsilon\) of Theorem B comes from the induction and has no explicit value.

## 5. Exercises

**5.1** (easy). In Lemma 1.1 take \(\theta=0\): all cuts are parallel. Show directly that every participating point of \(B\) lies on a line \(\nu_0\cdot x=c\) with \(c\in\{c_0,c_-,c_+\}\) or is counted by \(C_B\), and that in fact a participating point lies strictly between \(c_-\) and \(c_+\).

**5.2** (medium). Show that the bound \(2N\) on transfers crossing the boundary of \(B\) fails for a disk \(B\) if the transfers may point in all directions.

**5.3** (easy). Verify \(\frac34-\frac23+\frac13\bigl(\frac{15}{17}-1\bigr)=\frac3{68}\), and find the exponent obtained if the spatial measure only had disk exponent \(d_*=7/4\).

## 6. Solutions

**5.1.** With parallel cuts, \(M_i=\{\nu_0\cdot x<c_i\}\cap P\), nested by threshold. A point \(x\) with \(t(x)<c_-\) is marked at every state, and one with \(t(x)>c_+\) is never marked; so participating points have \(c_-<t(x)<c_+\). The strips of width zero exclude only the three lines, and the lemma bounds the remaining participants in \(B\) by \(2C_B\).

**5.2.** If transfers may point in all directions, a token can enter and leave \(B\) many times; with \(N\) tokens moving back and forth across the boundary, the number of crossing transfers is unbounded in terms of \(N\). The cone condition makes \(\ell_1\) and \(\ell_2\) monotone along tokens, and the parallelogram is defined by these functionals.

**5.3.** \(\frac34-\frac23=\frac1{12}\) and \(\frac13\cdot(-\frac2{17})=-\frac2{51}\); \(\frac1{12}-\frac2{51}=\frac{17-8}{204}=\frac3{68}\). With \(d_*=7/4\), \(\alpha_*=3/4\), and the exponent is \(\frac1{12}-\frac1{12}=0\): the argument would just fail. This is why a disk exponent strictly greater than \(7/4\) is needed.

## References

- [OpenAI-HL] OpenAI, *A power saving for planar halving lines*, OpenAI Math Release preprint, 25 September 2026, Section 7. https://github.com/openai/math/tree/main/preprints/A-power-saving-for-planar-halving-lines-September-25-2026
