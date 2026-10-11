# From safe samples to unrevealed rank

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

[Reverse exposure and safe samples](reverse-exposure-and-safe-samples.md) showed that many revealed labels of a group are safe. But revealed labels are sacrificed and can never be accepted. This lesson transfers the safe count to rank among *unrevealed* labels: the statistic \(z_h\) of [Layers and a rank bound for every order](layers-and-a-rank-bound-for-every-order.md). A safe label is either spanned by a few unrevealed witnesses, and then the density inequality charges it to their rank, or it belongs to a residual set lying entirely in the revealed masks. Such a residual is chosen with knowledge of the masks, so a bound for one fixed set does not suffice. The marked-pivot count of [Marked pivots and sign patterns](marked-pivots-and-sign-patterns.md) provides a small family containing every possible residual, fixed before the masks of the group are drawn, and a union bound finishes the argument.

Throughout \(H\) is fixed, so the candidates and the true groups \(U_i\) with sizes \(n_i\) and \(Y_i=Y\cap U_i\) are fixed; \(O=D\cup C\).

## 1. Witnesses and residuals

Fix a listed group \(h\). For each valid endpoint \(b\in\mathfrak B_h\) choose a *witness set* \(Z_b\subseteq S_{h,b}=P_{h,b}\setminus O\) by the greedy scan of Lemma 1.4 of the first lesson in label order, over the nominal base \(\Omega_b=X_h(b-2)\cup K_{h,b}\) of the fourth lesson. Then \(Z_b\) is independent over \(\Omega_b\) and
\[
\begin{gathered}
|Z_b|=\operatorname{rk}\bigl(S_{h,b}\bigm|\Omega_b\bigr),\\
S_{h,b}\subseteq\operatorname{cl}\bigl(\Omega_b\cup Z_b\bigr).
\end{gathered}\tag{1.1}
\]
The sets \(Z_b\) are disjoint, since the birth sets \(P_{h,b}\) are, and \(\sum_b|Z_b|=z_h\). The *residual* of group \(h\) is
\[
\begin{aligned}
\mathcal R_h&=\bigcup_{b\in\mathfrak B_h}\Bigl(P_{h,b}\\
&\qquad\setminus\operatorname{cl}\bigl(\Omega_b\cup Z_b\bigr)\Bigr).
\end{aligned}\tag{1.2}
\]
By (1.1) no label of \(S_{h,b}\) lies in it, so \(\mathcal R_h\subseteq O\): the residual consists of revealed labels.

**Lemma 1.1.** \(\sigma_h\leq\kappa z_h+|\mathcal R_h|\).

*Proof.* Fix \(b\in\mathfrak B_h\) and put \(Q'_b=Q_h(F_{h-1}(b-2)\cup K_{h,b})\). Since \(b-2\geq a_h\), the expansion is enabled at \(b-2\), and monotonicity gives \(X_h(b-2)=Q_h(F_{h-1}(b-2))\subseteq Q'_b\); also \(K_{h,b}\subseteq Q'_b\). A safe label \(d\) born at \(b\) lies in \(D_h\cap P_{h,b}\) and outside \(Q'_b\). If it is not in \(\mathcal R_h\), then \(d\in\operatorname{cl}(\Omega_b\cup Z_b)\subseteq\operatorname{cl}(Q'_b\cup Z_b)\). By the residual bound (1.1) of the third lesson, the number of such labels is at most \(\kappa\operatorname{rk}(Z_b\mid Q'_b)\leq\kappa|Z_b|\). Summing over \(b\) and adding the safe labels inside \(\mathcal R_h\) proves the lemma. \(\square\)

## 2. A uniform family of residuals

For integers \(0\leq q\leq n\) let \(S_q(n)=\sum_{\ell=0}^q\binom n\ell\), the number of subsets of an \(n\)-set with at most \(q\) elements.

**Lemma 2.1 (residual family).** Fix \(H\) and a true group \(U_i\) of size \(n=n_i\geq\kappa\). Condition on the parity and on all bits of \(D,C,T\) outside \(U_i\), but not on the bits inside \(U_i\) and not on whether \(U_i\) is listed. There is a family \(\mathfrak R_i\) of subsets of \(U_i\), determined by the conditioning, with
\[
|\mathfrak R_i|\leq\exp\Bigl(\tfrac{1000\log\kappa}\kappa\,n\Bigr),\tag{2.1}
\]
such that whenever \(U_i\) is listed, say as \(G_h\), and \(z_h\leq n/\kappa\), the residual \(\mathcal R_h\) belongs to \(\mathfrak R_i\).

*Proof.* If \(U_i\) is listed, its index is one more than the number of listed lighter groups, which the conditioning fixes; call this number \(h\) and put \(a=a_h\), \(q=\lfloor n/\kappa\rfloor\). The lighter paths, in particular \(F=F_{h-1}\), the competition sets \(K_{h,b}\), and the valid endpoints \(\mathfrak B_h\) are fixed by the conditioning: none of them involves a bit inside \(U_i\).

On a listed outcome, Lemma 3.1 of the third lesson provides at most \(q\) generators \(J_h\subseteq U_i\) with insertion times \(\tau(g)\in[a,0]\) such that, for all \(k\),
\[
X_h(k)=\operatorname{cl}\bigl(F(k)\cup J_h(k)\bigr),\tag{2.2}
\]
where \(J_h(k)=\{g\in J_h:\tau(g)\leq k\}\).
If moreover \(z_h\leq n/\kappa\), the witnesses \(Z=\bigcup_bZ_b\subseteq U_i\) number at most \(q\). We now describe \(\mathcal R_h\) through two marked sequences whose *old* occurrences are fixed by the conditioning and whose *movable* occurrences are the labels of \(J_h\) and \(Z\). A label in both \(J_h\) and \(Z\) contributes two occurrences.

*First sequence: valid births.* For \(k=a-2,a-1,\ldots,1\) in turn, list the labels of \(F(k)\) in label order, all with mark \(1\) if \(k\in\mathfrak B_h\) and mark \(0\) otherwise; then insert the generators with \(\tau(g)=k\), with the same mark. By (2.2), after the block of time \(k\) the labels so far span exactly \(X_h(k)\). A label \(f\in U_i\) is therefore first spanned within the block of its birth \(b_h(f)\), and its pivot mark is \(1\) exactly when \(b_h(f)\in\mathfrak B_h\). The set of labels of \(U_i\) with mark \(1\) is \(\bigcup_{b\in\mathfrak B_h}P_{h,b}\).

*Second sequence: layers.* Let \(b_0\in\{a-2,a-1\}\) and \(b_1\in\{0,1\}\) have the chosen parity. For the endpoints \(b=b_0+2,b_0+4,\ldots,b_1\) in turn, write:

1. the labels of \(K_{h,b}\) in label order, then the witnesses \(Z_b\) (empty if \(b\notin\mathfrak B_h\)), all with mark \(0\);
2. the labels of \(F(b)\) in label order, then the generators with \(b-2<\tau(g)\leq b\), all with mark \(1\).

We claim that the labels written up to the end of layer \(b\) span \(X_h(b)\), and up to the end of part 1 of layer \(b\) they span \(\operatorname{cl}(X_h(b-2)\cup K_{h,b}\cup Z_b)\). Initially nothing is written, and \(X_h(b_0)=L=\operatorname{cl}(\varnothing)\). If the claim holds at \(b-2\), part 1 gives the second span. Part 2 then adds \(F(b)\) and the generators inserted in \((b-2,b]\); since \(K_{h,b}\subseteq F(b)\) and \(Z_b\subseteq X_h(b)\), (2.2) shows that the span becomes \(X_h(b)\).

Now let \(f\in P_{h,b}\) with \(b\in\mathfrak B_h\). It lies outside \(X_h(b-1)\supseteq X_h(b-2)\) and inside \(X_h(b)\), so its pivot in the second sequence lies in layer \(b\), and its mark is \(1\) exactly when \(f\) is not spanned at the end of part 1, that is, when \(f\in\mathcal R_h\). Let \(M_1\) and \(M_2\) be the sets of labels of \(U_i\) with mark \(1\) in the first and in the second sequence. Hence
\[
\mathcal R_h=M_1\cap M_2.
\]
The first condition is needed: part 2 of a layer also spans labels born at \(b-1\), whose births are not valid.

*The family.* Let \(\mathfrak R_i\) consist of all intersections \(M_1\cap M_2\), where \(J,Z\subseteq U_i\) are sets of at most \(q\) labels, \(M_1\) is the set of labels of \(U_i\) with mark \(1\) after some insertion of the occurrences of \(J\) into the first old sequence, and \(M_2\) the same for some insertion of the occurrences of \(J\) and \(Z\) into the second old sequence. Positions, orders and marks of the inserted occurrences are arbitrary. The old sequences are fixed by the conditioning, and their labels span \(E\) because \(F(0)=E\). The family contains every actual residual, and possibly sets that arise from no actual outcome.

*Counting.* There are at most \(S_q(n)^2\) choices of \(J,Z\). Each sequence receives at most \(2q\) movable occurrences, so by Lemma 2.1 of the seventh lesson
\[
|\mathfrak R_i|\leq S_q(n)^2\bigl(4^{2q}S_{2q}(n)\bigr)^2.
\]
For \(0<\alpha\leq1\), using \(\alpha^\ell\geq\alpha^{\alpha n}\) for \(\ell\leq\alpha n\),
\[
\begin{aligned}
\alpha^{\alpha n}S_{\lfloor\alpha n\rfloor}(n)&\leq\sum_{\ell\leq\alpha n}\binom n\ell\alpha^\ell\\
&\leq(1+\alpha)^n\leq e^{\alpha n},
\end{aligned}
\]
so that \(S_{\lfloor\alpha n\rfloor}(n)\leq(e/\alpha)^{\alpha n}\).
Apply this with \(\alpha=1/\kappa\) to \(S_q(n)\), and with \(\alpha=2/\kappa\) to \(S_{2q}(n)\leq S_{\lfloor2n/\kappa\rfloor}(n)\). Together with \(q\leq n/\kappa\),
\[
\begin{aligned}
\log|\mathfrak R_i|&\leq\frac n\kappa\Bigl(2(1+\log\kappa)\\
&\qquad+8\log2+4\bigl(1+\log\tfrac\kappa2\bigr)\Bigr)\\
&=\frac n\kappa\bigl(6\log\kappa+6+4\log2\bigr)\\
&\leq\frac{1000\log\kappa}\kappa\,n.\qquad\square
\end{aligned}
\]

The bound does not depend on how many auxiliary times the path passes through: the marked-pivot count already includes every placement of generators and witnesses.

## 3. The sample-to-rank transfer

For a true group \(U_i\), put \(z_i=z_h\) and \(\sigma_i=\sigma_h\) if it is listed as \(G_h\), and \(z_i=\sigma_i=0\) otherwise.

**Lemma 3.1 (sample-to-rank transfer).** If \(n_i\geq\kappa\), then, with \(\gamma=\eta/16=2^{-16}\),
\[
\mathbb E[z_i\mid H]\geq\frac{\gamma|Y_i|-2^{-23}n_i}\kappa.
\]

*Proof.* Write \(n=n_i\). *The safe count.* On outcomes where \(U_i\) is listed as \(G_h\), \(D_h\cap Y=D\cap Y_i\) and \(D_h=D\cap U_i\). On the other outcomes \(D\cap U_i=\varnothing\) and \(\sigma_i=0\). So Lemma 1.1 of the sixth lesson gives, for every \(D\),
\[
\mathbb E[\sigma_i\mid H,D]\geq\frac\eta4|D\cap Y_i|-\frac{|D\cap U_i|}\kappa.
\]
The mask \(D\) is independent of \(H\) with rate \(\frac14\), so averaging over \(D\) gives, as \(\eta/16=\gamma\),
\[
\mathbb E[\sigma_i\mid H]\geq\gamma|Y_i|-\frac n{4\kappa}.\tag{3.1}
\]

*Large residuals are unlikely.* Use the conditioning of Lemma 2.1. Within \(U_i\), whose labels lie outside \(H\), the events \(\{e\in O\}\) are independent, each of probability \(1-\frac34(1-t)=\frac14+\frac34t\leq\frac12\). So every fixed \(R_0\in\mathfrak R_i\) satisfies \(\Pr(R_0\subseteq O)\leq2^{-|R_0|}\). Let \(\delta=2^{-26}\) and let \(\mathcal E_i\) be the event that some \(R_0\in\mathfrak R_i\) with \(|R_0|>\delta n\) lies in \(O\). By (2.1) and the union bound, with \(\log\kappa=100\log2\),
\[
\begin{aligned}
&\Pr(\mathcal E_i\mid\cdot)\\
&\quad\leq\exp\Bigl(\frac{1000\log\kappa}\kappa\,n-\delta n\log2\Bigr)\\
&\quad=2^{-(2^{-26}-10^5\cdot2^{-100})\,n}\\
&\quad\leq2^{-2^{-27}n}\leq2^{-2^{73}}<2^{-26},
\end{aligned}
\]
using \(10^5\cdot2^{-100}<2^{-27}\) and \(n\geq\kappa=2^{100}\). The bound does not depend on the conditioning, so it also holds given \(H\) alone.

*The error term.* Let \(e_i=|\mathcal R_h|\) on outcomes where \(U_i\) is listed as \(G_h\) and \(z_h\leq n/\kappa\), and \(e_i=0\) otherwise. On the first kind of outcome \(\mathcal R_h\in\mathfrak R_i\) and \(\mathcal R_h\subseteq O\), so \(|\mathcal R_h|>\delta n\) forces \(\mathcal E_i\). Hence \(e_i\leq\delta n+n\mathbf 1_{\mathcal E_i}\) and
\[
\mathbb E[e_i\mid H]\leq\delta n+2^{-26}n=2^{-25}n.
\]
No independence of the selected residual itself is used: the union bound runs over the fixed family.

*Conclusion.* In every outcome \(\sigma_i\leq\kappa z_i+e_i\). When \(U_i\) is listed and \(z_i\leq n/\kappa\), this is Lemma 1.1. When it is listed and \(z_i>n/\kappa\), then \(\sigma_i\leq|U_i|=n<\kappa z_i\). When it is unlisted, both sides vanish. Taking expectations and using (3.1),
\[
\begin{aligned}
\kappa\,\mathbb E[z_i\mid H]&\geq\gamma|Y_i|-\Bigl(\frac1{4\kappa}+2^{-25}\Bigr)n\\
&\geq\gamma|Y_i|-2^{-23}n.\qquad\square
\end{aligned}
\]

## 4. Exercises

**4.1.** Show that \(\sum_b|Z_b|=z_h\) and that the witness sets of different endpoints are disjoint.

**4.2.** Show that \(S_{\lfloor\alpha n\rfloor}(n)\leq(e/\alpha)^{\alpha n}\) is weaker than the trivial \(S_q(n)\leq2^n\) when \(\alpha\) is close to one, and compute both for \(n=100\), \(\alpha=0.01\).

**4.3.** Verify that \(6\log\kappa+6+4\log2\leq1000\log\kappa\) for \(\kappa=2^{100}\), and that \(10^5\cdot2^{-100}<2^{-27}\).

**4.4.** Why would it be wrong to argue that \(\mathcal R_h\subseteq O\) has probability at most \(2^{-|\mathcal R_h|}\)?

**4.5.** Where is \(n_i\geq\kappa\) used, and how are the smaller groups handled?

## 5. Solutions

**4.1.** By (1.1), \(|Z_b|\) is the \(b\)-th summand of \(z_h\) in (2.1) of the fourth lesson. A label of \(Z_b\) lies in \(P_{h,b}\), the labels of \(G_h\) born at \(b\); a label has one birth.

**4.2.** For \(\alpha=1\) the bound is \(e^n>2^n\). For \(n=100\) and \(\alpha=0.01\): \(S_1(100)=101\) and \((100e)^1\approx271.8\); both are far below \(2^{100}\).

**4.3.** \(\log\kappa=100\log2\approx69.3\), so the left side is about \(424.7\), while the right side is about \(69{,}300\). And \(10^5<2^{17}\), so \(10^5\cdot2^{-100}<2^{-83}<2^{-27}\).

**4.4.** The residual is selected after the masks are drawn; for instance \(O\cap U_i\) itself always lies in \(O\). The bound \(2^{-|R_0|}\) is valid for a set \(R_0\) fixed in advance. The family \(\mathfrak R_i\) is fixed before the bits inside \(U_i\) are drawn, and it contains every residual that can occur, so the union bound over it is legitimate.

**4.5.** It is used to make \(2^{-2^{-27}n}\) smaller than \(2^{-26}\). Groups with \(n_i<\kappa\) are discarded in the ninth lesson: each has \(|Y_i|<\kappa\), and their total weight is less than \(2\kappa m_*\), which is covered by the maximum rule when \(m_*\) is large.

## References

- [OpenAI-P] OpenAI, *One Sample Suffices for Matroid Prophet Inequalities against an Almighty Adversary*, OpenAI Math Release preprint, 23 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/One-Sample-Suffices-for-Matroid-Prophet-Inequalities-against-an-Almighty-Adversary-September-23-2026
