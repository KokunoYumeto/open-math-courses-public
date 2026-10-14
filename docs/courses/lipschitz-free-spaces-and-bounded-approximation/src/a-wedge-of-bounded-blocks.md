# A wedge of bounded blocks

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For every integer \(p\ge1\) there is a bounded metric space \(M_p\) with distances at least \(1\) whose free space is not approximated, at finitely many points, by operators of finite rank and norm at most \(p\). This is Theorem 5.1 of the first lesson; it is proved in the last three lessons. This lesson glues the spaces \(M_p\) at their base points. The free space of the resulting space \(M\) has the approximation property, because the free space of each block has the bounded one and because the blocks can be cut off one after the other by projections of norm \(1\). It does not have the bounded approximation property, because a bound for \(M\) would be a bound for every block. This proves Theorem 5.2 of the first lesson from Theorem 5.1.

The last section states a theorem of Kalton as a hypothesis and derives from it that \(\mathcal F(M)\) is not approximable by uniformly continuous maps with compact range.

- The wedge of pointed metric spaces and its retractions (Section 1).
- The operators between the free spaces (Lemma 2.1).
- The bounded approximation property passes to the blocks (Proposition 3.1).
- The approximation property of the wedge (Proposition 4.1).
- Proof of the main theorem from the theorem on blocks (Section 5).
- Approximable Banach spaces and the hypothesis (K) (Section 6).

The lesson follows [OpenAI-LF, Section 2]. It uses [Lipschitz-free spaces and approximation properties](lipschitz-free-spaces-and-approximation-properties.md): the linearization (Lemma 2.1 and Corollary 2.2), Lemma 3.1, Proposition 4.1 and Theorem 5.1 there. Section 6 uses the Hahn–Banach theorem (core course [Functional Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D20)).

## 1. The wedge

Let \((M_p,d_p,o_p)\), \(p=1,2,3,\dots\), be pointed metric spaces. Their *wedge* is the set \(M\) obtained from the disjoint union of the \(M_p\) by identifying all base points with one point \(o\):
\[
M=\{o\}\cup\bigsqcup_{p\ge1}\bigl(M_p\setminus\{o_p\}\bigr) .
\]
We regard each \(M_p\) as a subset of \(M\); two different blocks meet only in \(o\). The distance on \(M\) is defined in two cases. For two points of one block \(M_p\),
\[
d(x,y)=d_p(x,y) .
\]
For \(x\in M_p\) and \(y\in M_q\) with \(p\ne q\),
\[
d(x,y)=d_p(x,o)+d_q(y,o) .
\]
The two cases agree if one of the points is \(o\). In words: to go from one block to another one has to pass through \(o\).

**Lemma 1.1.** 1. \(d\) is a metric on \(M\), and on each block it is \(d_p\).

2. If every \(M_p\) has distances at least \(1\), then so has \(M\).

3. For every \(p\) the map \(r_p\) from \(M\) to \(M_p\) that fixes the points of \(M_p\) and sends all other points to \(o\) is pointed and \(1\)-Lipschitz.

4. For every \(N\ge1\) the map \(r_{\le N}\) from \(M\) to \(M\) that fixes the points of \(M_1,\dots,M_N\) and sends all other points to \(o\) is pointed and \(1\)-Lipschitz.

**Proof.** *Part 1.* Symmetry is clear, and \(d(x,y)=0\) only for \(x=y\). Write \(|x|\) for the distance of \(x\) to \(o\) inside its block. In all cases \(d(x,y)\le|x|+|y|\), by the triangle inequality in a block or by definition; and if \(x\) and \(y\) lie in different blocks, then \(d(x,y)=|x|+|y|\). Let \(x,y,z\in M\); we show \(d(x,y)\le d(x,z)+d(z,y)\). If all three lie in one block, this is the triangle inequality there. If \(x,y\) lie in one block and \(z\) in another, the right side is \(|x|+2|z|+|y|\ge d(x,y)\). If \(x\in M_p\), \(y\in M_q\) with \(p\ne q\), and \(z\in M_p\), then \(d(x,y)=|x|+|y|\le d_p(x,z)+|z|+|y|\), which is the right side; the case \(z\in M_q\) is symmetric. If \(z\) lies in a third block, the right side is \(|x|+2|z|+|y|\).

*Part 2.* Inside a block this is the assumption. For \(x,y\ne o\) in different blocks, \(d(x,y)=|x|+|y|\ge2\).

*Parts 3 and 4.* Let \(r\) be one of the two maps. If \(x\) and \(y\) are both fixed by \(r\), their distance is unchanged. If both are sent to \(o\), the distance of the images is \(0\). If \(x\) is fixed and \(y\) is sent to \(o\) and \(y\ne o\), then \(y\) lies in a block that does not contain \(x\), unless \(x=o\); in both cases \(d(r(x),r(y))=|x|\le|x|+|y|=d(x,y)\). \(\blacksquare\)

## 2. The operators

Let \(i_p\) be the inclusion of \(M_p\) in \(M\). By the linearization lemma the maps \(i_p\), \(r_p\) and \(r_{\le N}\) induce operators of norm at most \(1\):
\[
\begin{gathered}
I_p=\widehat{i_p}\colon\ \mathcal F(M_p)\to\mathcal F(M),\\
P_p=\widehat{r_p}\colon\ \mathcal F(M)\to\mathcal F(M_p),\\
R_N=\widehat{r_{\le N}}\colon\ \mathcal F(M)\to\mathcal F(M).
\end{gathered}
\]

**Lemma 2.1.** 1. \(P_pI_p\) is the identity of \(\mathcal F(M_p)\), and \(\|I_pv\|=\|v\|\) for all \(v\in\mathcal F(M_p)\).

2. \(R_N=\sum_{p=1}^NI_pP_p\), and \(R_N^2=R_N\).

3. \(R_Nu\to u\) for every \(u\in\mathcal F(M)\), uniformly on every compact set.

**Proof.** *Part 1* is Corollary 2.2 of the first lesson.

*Part 2.* Both sides of the first equation are bounded operators, and so are \(R_N^2\) and \(R_N\); so it suffices to compare them on the evaluations \(\delta_x\). If \(x\ne o\) lies in the block \(M_q\), then \(I_pP_p\delta_x\) is \(\delta_x\) for \(p=q\) and \(\delta_o=0\) for \(p\ne q\). So \(\sum_{p\le N}I_pP_p\delta_x\) is \(\delta_x\) if \(q\le N\) and \(0\) otherwise, and this is \(R_N\delta_x\). Applying \(R_N\) twice gives the same.

*Part 3.* An evaluation combination \(v\) involves finitely many blocks, so \(R_Nv=v\) for all large \(N\). The evaluation combinations are dense and \(\|R_N\|\le1\). Lemma 3.1 of the first lesson gives the claim. \(\blacksquare\)

## 3. A bound for the wedge is a bound for every block

**Proposition 3.1.** Let \(\mathcal F(M)\) have \(\lambda\)-BAP. Then for every \(p\), every finite set \(F\subseteq\mathcal F(M_p)\) and every \(\varepsilon>0\) there is a bounded linear operator \(T\) of finite rank on \(\mathcal F(M_p)\) with \(\|T\|\le\lambda\) and \(\|Tv-v\|<\varepsilon\) for all \(v\in F\).

**Proof.** The set \(I_p(F)\) is finite. Choose an operator \(U\) of finite rank on \(\mathcal F(M)\) with \(\|U\|\le\lambda\) and \(\|UI_pv-I_pv\|<\varepsilon\) for \(v\in F\), and put \(T=P_pUI_p\). It has finite rank and \(\|T\|\le\lambda\), and by Lemma 2.1
\[
\begin{aligned}
\|Tv-v\|&=\|P_p(UI_pv-I_pv)\|\\
&\le\|UI_pv-I_pv\|<\varepsilon .
\end{aligned}
\]
\(\blacksquare\)

## 4. The approximation property of the wedge

**Proposition 4.1.** If every \(\mathcal F(M_p)\) has the bounded approximation property, with a constant \(\lambda_p\) that may depend on \(p\), then \(\mathcal F(M)\) has the approximation property.

**Proof.** Let \(C\subseteq\mathcal F(M)\) be compact and \(\varepsilon>0\). By Lemma 2.1 there is \(N\) with
\[
\sup_{u\in C}\|R_Nu-u\|<\frac\varepsilon2 .
\]
For \(p\le N\) the set \(P_p(C)\) is compact in \(\mathcal F(M_p)\). Choose an operator \(T_p\) of finite rank on \(\mathcal F(M_p)\) with \(\|T_p\|\le\lambda_p\) and
\[
\sup_{u\in C}\|T_pP_pu-P_pu\|<\frac\varepsilon{2N} .
\]
The operator
\[
T=\sum_{p=1}^NI_pT_pP_p
\]
on \(\mathcal F(M)\) has finite rank and is bounded, with \(\|T\|\le\lambda_1+\dots+\lambda_N\). Since \(R_N=\sum_{p\le N}I_pP_p\), for \(u\in C\)
\[
\begin{aligned}
\|Tu-u\|&\le\|R_Nu-u\|\\
&\quad+\sum_{p=1}^N\|I_p(T_pP_pu-P_pu)\|\\
&<\frac\varepsilon2+N\cdot\frac\varepsilon{2N} .
\end{aligned}
\]
\(\blacksquare\)

The order of the choices matters. The number \(N\) of blocks that are kept depends on \(C\) and \(\varepsilon\), and the bound \(\lambda_1+\dots+\lambda_N\) for the norm of \(T\) grows with \(N\). The approximation property allows this.

## 5. Proof of the main theorem

Let \(M_p\) and \(A_p\), \(p\ge1\), be the spaces and the finite sets of Theorem 5.1 of the first lesson, and let \(M\) be the wedge of the spaces \(M_p\). We prove the statements of Theorem 5.2 there.

*The space.* \(M\) is countable, as a countable union of countable sets, and its distances are at least \(1\) by Lemma 1.1.

*The approximation property.* Each \(M_p\) is countable with distances at least \(1\) and diameter at most \(B_p\). By Proposition 4.1 of the first lesson, \(\mathcal F(M_p)\) has \(2B_p\)-BAP. By Proposition 4.1 above, \(\mathcal F(M)\) has the approximation property.

*No bounded approximation property.* Suppose \(\mathcal F(M)\) has \(\lambda\)-BAP. Choose an integer \(p\ge\lambda\). By Proposition 3.1, applied to the finite set \(\{\delta_a:a\in A_p\}\) and \(\varepsilon=\tfrac12\), there is an operator \(T\) of finite rank on \(\mathcal F(M_p)\) with \(\|T\|\le\lambda\le p\) and \(\|T\delta_a-\delta_a\|<\tfrac12\) for all \(a\in A_p\). This contradicts Theorem 5.1.

*The space is unbounded.* Suppose \(M\) has a finite diameter \(C_0\). Then \(C_0\ge1\), and every \(M_p\) has a diameter of at most \(C_0\). By Proposition 4.1 of the first lesson every \(\mathcal F(M_p)\) has \(2C_0\)-BAP. For an integer \(p\ge2C_0\) this gives an operator of finite rank and norm at most \(p\) on \(\mathcal F(M_p)\) with errors less than \(\tfrac12\) at all \(\delta_a\), \(a\in A_p\), against Theorem 5.1.

*A bounded closed ball that is not compact.* The closed ball of \(M\) with the centre \(o\) and the radius \(B_1\) contains \(M_1\), which is infinite. A sequence of different points of \(M_1\) has no convergent subsequence, because its points have distances at least \(1\). So the ball is not compact. \(\blacksquare\)

All blocks and all sets \(A_p\) are fixed before the number \(\lambda\) and the operator are considered. Each block defeats the operators of norm at most \(p\), and the wedge contains all blocks.

## 6. Approximable spaces

This section derives a consequence about approximation by nonlinear maps. It depends on a theorem of Kalton that is stated as a hypothesis.

A map \(\psi\) between metric spaces is *uniformly continuous* if for every \(\varepsilon>0\) there is \(\eta>0\) such that points at a distance of at most \(\eta\) have images at a distance of at most \(\varepsilon\). A family of maps is *equi-uniformly continuous* if for every \(\varepsilon\) one \(\eta\) serves for all maps of the family.

**Definition** (Kalton [K12, Section 4]). A separable Banach space \(X\) is *approximable* if there is an equi-uniformly continuous sequence of maps \(\psi_n\) from \(X\) to \(X\), each with a relatively compact range, such that \(\psi_n(x)\to x\) for every \(x\in X\).

Kalton remarks that every Banach space with the bounded approximation property is approximable [K12, Section 4]; this remark is not used here. He asked whether every separable Banach space is approximable [K12, Problem 1].

A subset \(N\) of a Banach space \(X\) is a *net* if there are numbers \(0<a<b\) with \(\|x-y\|\ge a\) for different \(x,y\in N\) and with the distance from every point of \(X\) to \(N\) at most \(b\).

**Hypothesis (K)** (Kalton [K12, Theorem 4.4, the implication from (i) to (v)]). Let \(X\) be a separable Banach space that is approximable, and let \(N\subseteq X\) be a net that contains \(0\). Then there is a number \(\Lambda\) such that for every finite set \(E\subseteq N\) and every \(\varepsilon>0\) there is a \(\Lambda\)-Lipschitz map \(g\) from \(N\) to \(N\) with a relatively compact range and \(\|g(x)-x\|<\varepsilon\) for all \(x\in E\).

This statement is not proved in this course or elsewhere in the programme. Kalton applies it in this form to the free space of a uniformly discrete space in [K12, the paragraph after Problem 1], with the argument given below.

**Lemma 6.1** (linearization of maps into a Banach space). Let \((M,d,o)\) be a pointed metric space, \(X\) a Banach space, and \(\gamma\) a \(\Lambda\)-Lipschitz map from \(M\) to \(X\) with \(\gamma(o)=0\). There is exactly one bounded linear operator \(T\) from \(\mathcal F(M)\) to \(X\) with \(T\delta_x=\gamma(x)\) for all \(x\in M\), and \(\|T\|\le\Lambda\).

**Proof.** Let \(v=\sum_xc_x\delta_x\) be an evaluation combination and \(w=\sum_xc_x\gamma(x)\). For a functional \(\phi\in X^*\) with \(\|\phi\|\le1\) the function \(\phi\circ\gamma\) lies in \(\operatorname{Lip}_0(M)\) and has a Lipschitz constant of at most \(\Lambda\). So
\[
\begin{aligned}
|\phi(w)|&=\Bigl|\sum_xc_x\,(\phi\circ\gamma)(x)\Bigr|\\
&=|v(\phi\circ\gamma)|\le\Lambda\,\|v\| .
\end{aligned}
\]
By the Hahn–Banach theorem \(\|w\|\) is the supremum of \(|\phi(w)|\) over these \(\phi\). So \(\|w\|\le\Lambda\|v\|\). In particular \(w=0\) if \(v=0\), so \(w\) depends only on \(v\), and \(v\mapsto w\) is a linear map of norm at most \(\Lambda\) on the span of the evaluations. It extends to the closure \(\mathcal F(M)\) because \(X\) is complete. Uniqueness holds because the span is dense. \(\blacksquare\)

**Proposition 6.2.** Assume (K). Let \(M\) be a countable pointed metric space with distances at least \(1\) such that \(\mathcal F(M)\) does not have the bounded approximation property; for instance the space of Theorem 5.2 of the first lesson. Then \(\mathcal F(M)\) is not approximable.

**Proof.** Let \(X=\mathcal F(M)\). It is separable: the evaluation combinations with rational coefficients are countable and dense.

*A net.* The set \(N_0=\{\delta_x:x\in M\}\) contains \(\delta_o=0\), and \(\|\delta_x-\delta_y\|=d(x,y)\ge1\) for \(x\ne y\). Let \(w_1,w_2,\dots\) be dense in \(X\). Go through this sequence and add \(w_i\) to the set whenever its distance to all points of the set so far is at least \(1\). The resulting set \(N\) contains \(N_0\), and its points have distances at least \(1\). Every \(u\in X\) has \(\|u-w_i\|<\tfrac12\) for some \(i\), and \(w_i\) lies in \(N\) or has a distance less than \(1\) to a point of \(N\). So the distance from \(u\) to \(N\) is less than \(\tfrac32\), and \(N\) is a net.

*Operators.* Suppose \(X\) is approximable, and let \(\Lambda\) be the number of (K) for the net \(N\). Let \(F\subseteq M\) be finite with \(o\in F\). By (K) with \(E=\{\delta_x:x\in F\}\) and \(\varepsilon=1\) there is a \(\Lambda\)-Lipschitz map \(g\) from \(N\) to \(N\) with a relatively compact range and \(\|g(\delta_x)-\delta_x\|<1\) for \(x\in F\). Both \(g(\delta_x)\) and \(\delta_x\) lie in \(N\), where different points have distances at least \(1\); so \(g(\delta_x)=\delta_x\) for \(x\in F\). The range of \(g\) is a relatively compact set of points with distances at least \(1\), so it is finite (Exercise 7.3). The map \(\gamma(x)=g(\delta_x)\) from \(M\) to \(X\) satisfies \(\gamma(o)=0\) and
\[
\begin{aligned}
\|\gamma(x)-\gamma(y)\|&\le\Lambda\,\|\delta_x-\delta_y\|\\
&=\Lambda\,d(x,y) .
\end{aligned}
\]
By Lemma 6.1 there is an operator \(T_F\) on \(X\) with \(\|T_F\|\le\Lambda\) and \(T_F\delta_x=\gamma(x)\). Its range lies in the span of the finite set \(\gamma(M)\), so it has finite rank, and \(T_F\delta_x=\delta_x\) for \(x\in F\).

*The bounded approximation property.* Let \(C\subseteq X\) be compact and \(\varepsilon>0\). Cover \(C\) by finitely many balls of radius \(\varepsilon\) with centres \(u_1,\dots,u_r\in C\), and choose evaluation combinations \(v_i\) with \(\|u_i-v_i\|<\varepsilon\). Let \(F\) contain \(o\) and all points that occur in the \(v_i\). Then \(T_Fv_i=v_i\), and for \(u\in C\) with \(\|u-u_i\|<\varepsilon\):
\[
\begin{aligned}
\|T_Fu-u\|&\le\|T_F(u-v_i)\|+\|v_i-u\|\\
&<2\varepsilon\,(\Lambda+1) .
\end{aligned}
\]
So \(X\) has \(\lambda\)-BAP with \(\lambda=\max\{\Lambda,1\}\), against the assumption. \(\blacksquare\)

So, under (K), the space \(\mathcal F(M)\) of the main theorem answers Kalton's question [K12, Problem 1] in the negative: it is a separable Banach space with the approximation property that is not approximable.

## 7. Exercises

**7.1.** Let \(M\) be the wedge of the spaces \(M_p\). Show that for \(f\in\operatorname{Lip}_0(M)\) the norm \(\|f\|_{\mathrm{Lip}}\) is the supremum of the Lipschitz constants of the restrictions of \(f\) to the blocks, and conclude that \(\|\sum_{p\le N}I_pv_p\|=\sum_{p\le N}\|v_p\|\) for \(v_p\in\mathcal F(M_p)\).

**7.2.** Show that the wedge of two copies of the interval \([0,1]\) with the base point \(0\) is isometric to the interval \([-1,1]\).

**7.3.** Show that a relatively compact subset of a metric space whose points have distances at least \(1\) is finite.

**7.4.** Let \(M\) be the space of Theorem 5.2 of the first lesson. Show that \(\mathcal F(M)\) is not isomorphic to \(\ell_1\), although \(\mathcal F(M_p)\) is isomorphic to \(\ell_1\) for every \(p\).

**7.5.** In the situation of Section 5, let \(\lambda_p\) be the smallest number such that \(\mathcal F(M_p)\) has \(\lambda\)-BAP for all \(\lambda>\lambda_p\). Show that \(p\le\lambda_p\le2B_p\).

## 8. Solutions

**7.1.** Let \(\Lambda\) be the supremum of the constants on the blocks; clearly \(\Lambda\le\|f\|_{\mathrm{Lip}}\). For \(x\in M_p\) and \(y\in M_q\) with \(p\ne q\),
\[
\begin{aligned}
|f(x)-f(y)|&\le|f(x)-f(o)|\\
&\quad+|f(o)-f(y)|\\
&\le\Lambda\,\bigl(d_p(x,o)+d_q(y,o)\bigr)\\
&=\Lambda\,d(x,y) .
\end{aligned}
\]
So \(\|f\|_{\mathrm{Lip}}=\Lambda\). Hence the functions \(f\) with \(\|f\|_{\mathrm{Lip}}\le1\) are exactly the functions whose restrictions \(f_p\) to the blocks are arbitrary elements of \(\operatorname{Lip}_0(M_p)\) with norm at most \(1\). Since \((I_pv_p)(f)=v_p(f_p)\), the supremum of \(\sum_pv_p(f_p)\) over these \(f\) is the sum of the suprema, \(\sum_p\|v_p\|\).

**7.2.** Map the points \(t\) of the first copy to \(t\) and the points \(s\) of the second copy to \(-s\). Distances inside a copy are kept, and for \(t\) in the first and \(s\) in the second copy, \(d=t+s=|t-(-s)|\).

**7.3.** A relatively compact set is covered by finitely many balls of radius \(\tfrac13\). Each of these balls contains at most one point of the set, because two points in one ball have a distance of at most \(\tfrac23\).

**7.4.** The space \(\ell_1\) has MAP (Example 3.3 of the first lesson). If \(\mathcal F(M)\) were isomorphic to \(\ell_1\), it would have BAP by Lemma 3.2 of the first lesson. \(\mathcal F(M_p)\) is isomorphic to \(\ell_1\) by Proposition 4.1 of the first lesson.

**7.5.** \(\lambda_p\le2B_p\) by Proposition 4.1 of the first lesson. If \(\lambda_p<p\), the space would have \(p\)-BAP, which gives an operator of finite rank and norm at most \(p\) with errors less than \(\tfrac12\) at the anchors, against Theorem 5.1.

## References

- [OpenAI-LF] OpenAI, *A uniformly discrete counterexample to bounded approximation in Lipschitz-free spaces*, OpenAI Math Release preprint, 26 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Failure-of-Bounded-Approximation-in-a-Lipschitz-Free-Space-over-a-Uniformly-Discrete-Metric-Space-September-26-2026
- [K12] N. J. Kalton, *The uniform structure of Banach spaces*, Mathematische Annalen 354 (2012), 1247–1288, Section 4: the definitions, Theorem 4.4 and Problem 1; free on the archive of the author's university. https://kaltonmemorial.missouri.edu/assets/docs/ma2012.pdf
