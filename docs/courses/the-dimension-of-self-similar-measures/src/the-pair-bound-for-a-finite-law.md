# The pair bound for a finite law

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A law \(\nu\) with a finite support \(F\) on the line can have much more entropy than its cells of length \(\rho\) show: the difference \(H(\nu)-H^0_\rho(\nu)\) is the mean entropy of \(\nu\) inside the cells. This lesson proves the estimate of [OpenAI-S, Section 3] that turns this entropy into pairs of nearby points. For every integer \(k\ge1\),
\[
\begin{aligned}
&k\bigl(H(\nu)-H^0_\rho(\nu)\bigr)\\
&\quad\le\log|kF|+C_k\sum_{\ell:\,2^{-\ell}\le2\rho}c_\ell(\nu),
\end{aligned}
\]
where \(kF\) is the set of the sums of \(k\) points of \(F\), the \(c_\ell(\nu)\) are the pair capacities, and \(C_k=53760\,k^4\). So if the entropy inside the cells is larger than \(\tfrac1k\log|kF|\), a definite amount of the mass of \(\nu\) lies in fair pairs of sizes below \(2\rho\). The constant does not depend on how close the points of \(F\) are to each other; the course needs this, because nothing is assumed about the distances between the points of a self-similar set.

- The statement (Theorem 1.1) and an example in which both sides have the same order.
- Random nested partitions (Lemma 2.1) and the chain of conditional entropies over their levels (Lemma 3.1).
- One refinement after the sum is observed (Lemma 4.1).
- The average over the cuts and the passage to pairs (Lemmas 5.1 and 5.2, Proposition 5.3).

The lesson follows [OpenAI-S, Section 3], which names a decomposition of P. Varjú into fair pairs at one scale as a predecessor of the method. It uses the pair capacities of [The gain from a pair of points](the-gain-from-a-pair-of-points.md), the rules of [Entropy of finite random variables](entropy-of-finite-random-variables.md), and the entropy \(H^0_\rho\) of the grid with the shift \(0\) from [Entropy at a scale](entropy-at-a-scale.md).

## 1. The statement

Let \(\nu\) be a law with a finite support \(F\subset\mathbb R\), and \(X\) a random variable with the law \(\nu\). Then \(H(\nu)=H(X)\), and for \(\rho>0\) the number \(H^0_\rho(\nu)=H(\lfloor X/\rho\rfloor)\) is the entropy of the cell of \(X\) in the grid of the intervals \([j\rho,(j+1)\rho)\). The cell is a function of \(X\), so by Proposition 2.1 of the lesson on entropy of finite random variables
\[
H(\nu)-H^0_\rho(\nu)=H\bigl(X\mid\lfloor X/\rho\rfloor\bigr)\ge0 .
\]
For an integer \(k\ge1\) let \(kF\) be the set of the sums \(x_1+\dots+x_k\) with \(x_i\in F\), and \(|kF|\) the number of its elements. The pair capacities \(c_\ell(\nu)\) are those of Definition 2.1 of the lesson on the gain from a pair of points.

**Theorem 1.1 (pair bound).** Let \(k\ge1\) be an integer, \(\nu\) a law with a finite support \(F\subset\mathbb R\), and \(\rho>0\). Then
\[
\begin{aligned}
&k\bigl(H(\nu)-H^0_\rho(\nu)\bigr)\\
&\quad\le\log|kF|+C_k\sum_{\ell:\,2^{-\ell}\le2\rho}c_\ell(\nu),
\end{aligned}
\]
with \(C_k=53760\,k^4\).

The sum has finitely many terms different from \(0\). For \(k=1\) the theorem says nothing, since \(H(\nu)\le\log|F|\). For \(k\ge2\) it has content when \(|kF|\) is much smaller than \(|F|^k\), that is, when many sums of \(k\) points coincide.

**Example 1.2.** Let \(n\ge2\) and \(F=\{0,d,2d,\dots,(n-1)d\}\) with \(nd<\rho\), and let \(\nu\) be uniform on \(F\). All points lie in one cell, so the left side is \(k\log n\). The set \(kF\) consists of the multiples \(jd\) with \(0\le j\le k(n-1)\), so \(\log|kF|\le\log k+\log n\). The theorem gives
\[
\sum_\ell c_\ell(\nu)\ \ge\ \frac{(k-1)\log n-\log k}{C_k}.
\]
On the other hand the distances between points of \(F\) lie in \([d,(n-1)d]\), which meets at most \(\log(n-1)+2\) of the intervals \([2^{-\ell},2^{1-\ell})\), and every capacity is at most \(1\). So for a fixed \(k\ge2\) the left side and the sum of the capacities both grow like \(\log n\).

The proof takes independent variables \(X_1,\dots,X_k\) with the law \(\nu\). Given their cells of length \(\rho\), they have the entropy \(k(H(\nu)-H^0_\rho(\nu))\). Observing the sum \(Y=X_1+\dots+X_k\) accounts for at most \(\log|kF|\) of it. What remains is the uncertainty about the \(X_i\) when the sum is known, and this is bounded by cutting the cells into smaller and smaller cells. A cut costs entropy only if some \(X_i\) is far from the mean of its cell, compared with the distance from the mean to the nearest cut. The cuts are chosen at random, so that the means are rarely near a cut, and then the cost is controlled by the mean distance of two independent points of the same cell: by pairs.

## 2. Random nested partitions

Throughout, \(\rho>0\) is fixed, and \(\rho_h=\rho\,4^{-h}\) for integers \(h\ge0\). A *cell* is an interval \([\alpha,\beta)\) with \(\alpha<\beta\).

**The rule of division.** Let \(A=[\alpha,\beta)\) be a cell of a length \(L\) with \(\rho_h/2\le L\le2\rho_h\). Let \(N=\lfloor L/\rho_{h+1}+\tfrac12\rfloor\), an integer nearest to \(L/\rho_{h+1}\). For numbers \(\theta_1,\dots,\theta_{N-1}\) in \([-\tfrac1{10},\tfrac1{10}]\) put \(c_0=\alpha\), \(c_N=\beta\) and
\[
c_j=\alpha+\frac{jL}N+\theta_j\,\rho_{h+1}\quad(0<j<N).
\]
The cells \([c_{j-1},c_j)\), \(1\le j\le N\), are the *children* of \(A\), and \(c_1,\dots,c_{N-1}\) are its *cuts*.

**Lemma 2.1.**

1. \(2\le N\le8\).
2. \(c_0<c_1<\dots<c_N\), and every child has a length between \(\rho_{h+1}/2\) and \(2\rho_{h+1}\).
3. If \(\theta_j\) is uniform on \([-\tfrac1{10},\tfrac1{10}]\), then for all real \(m\) and all \(r\ge0\) the probability that \(|c_j-m|\le r\) is at most \(40\,r/\rho_h\).

**Proof.** (1) \(L/\rho_{h+1}=4L/\rho_h\) lies in \([2,8]\). (2) Since \(|N-L/\rho_{h+1}|\le\tfrac12\), the quotient \(L/N\) lies between \((1-\tfrac1{2N})\rho_{h+1}\) and \((1+\tfrac1{2N})\rho_{h+1}\), hence between \(\tfrac34\rho_{h+1}\) and \(\tfrac54\rho_{h+1}\). The ends \(c_0,c_N\) are not moved, and every cut is moved by at most \(\tfrac1{10}\rho_{h+1}\). So the length of a child differs from \(L/N\) by at most \(\tfrac15\rho_{h+1}\): it lies between \(0.55\,\rho_{h+1}\) and \(1.45\,\rho_{h+1}\). In particular it is positive. (3) \(c_j\) is uniform on an interval of the length \(\tfrac15\rho_{h+1}=\tfrac1{20}\rho_h\), and the interval \([m-r,m+r]\) has the length \(2r\). \(\blacksquare\)

**Schemes.** Let \(\mathcal P_0\) be the set of the cells \([j\rho,(j+1)\rho)\), \(j\in\mathbb Z\), that contain a point of \(F\); they have the length \(\rho_0\). Fix an integer \(J\ge1\). Divide the cells of \(\mathcal P_0\) by the rule with \(h=0\), their children by the rule with \(h=1\), and so on, \(J\) times. By Lemma 2.1 (2) the rule can be applied each time: a cell obtained by \(h\) divisions, a cell *of level \(h\)*, has a length between \(\rho_h/2\) and \(2\rho_h\). A cell of level \(h\) is described by its *label* \((A_0,n_1\cdots n_h)\): it is the \(n_h\)-th child of the \(n_{h-1}\)-th child, and so on, of the \(n_1\)-th child of \(A_0\in\mathcal P_0\). The letters \(n_i\) lie in \(\{1,\dots,8\}\).

A *scheme* \(\theta\) is a choice of all the numbers that the divisions need: one number in \([-\tfrac1{10},\tfrac1{10}]\) for every label \((A_0,n_1\cdots n_h)\) with \(h<J\) and every \(j\in\{1,\dots,7\}\), used for the \(j\)-th cut of the cell with this label if this cell and this cut exist. We call these the coordinates *of level \(h\)*; they decide how the cells of level \(h\) are divided. The schemes form a cube of finite dimension. We give it the probability for which the coordinates are independent and uniform, and write \(\mathbb E_\theta\) for the mean over the schemes.

For a scheme and a point \(x\in F\), let \(C_h(x)\) be the cell of level \(h\) that contains \(x\), for \(0\le h\le J\). The cells are nested: the label of \(C_h(x)\) is the label of \(C_{h+1}(x)\) without its last letter. The cells of level \(h\) depend only on the coordinates of the levels below \(h\). For every label, the set of the schemes for which the cell with this label exists is a Borel set, and on it the ends of the cell are Borel functions of \(\theta\): they are formed from the coordinates by sums, products and the function \(L\mapsto\lfloor L/\rho_{h+1}+\tfrac12\rfloor\). So the label of \(C_h(x)\) is a Borel function of \(\theta\) with finitely many values, and all the probabilities and entropies below are bounded Borel functions of \(\theta\).

## 3. The chain over the levels

Let \(X_1,\dots,X_k\) be independent with the law \(\nu\), independent of the scheme, and
\[
\begin{gathered}
\mathbf X=(X_1,\dots,X_k),\\
Y=X_1+\dots+X_k .
\end{gathered}
\]
For a scheme \(\theta\), let \(\mathbf C_h\) be the tuple of the labels of the cells \(C_h(X_1),\dots,C_h(X_k)\). For a fixed scheme it is a function of \(\mathbf X\) with finitely many values.

If \(F\) is a single point, both sides of Theorem 1.1 are \(0\). Otherwise let \(J\ge1\) be an integer such that \(2\rho_J\) is less than every distance between two different points of \(F\).

**Lemma 3.1.** For every scheme of the depth \(J\),
\[
\begin{aligned}
&k\bigl(H(\nu)-H^0_\rho(\nu)\bigr)\\
&\quad\le\log|kF|+\sum_{h=0}^{J-1}H\bigl(\mathbf C_{h+1}\mid\mathbf C_h,Y\bigr).
\end{aligned}
\]

**Proof.** The label of level \(0\) of \(X_i\) and the number \(\lfloor X_i/\rho\rfloor\) determine each other. The coordinates of \(\mathbf X\) are independent, so \(H(\mathbf X)=kH(\nu)\) and \(H(\mathbf C_0)=kH^0_\rho(\nu)\), and since \(\mathbf C_0\) is a function of \(\mathbf X\),
\[
H(\mathbf X\mid\mathbf C_0)=k\bigl(H(\nu)-H^0_\rho(\nu)\bigr).
\]
By the rules of Proposition 2.1 of the lesson on entropy of finite random variables, and because \(Y\) takes at most \(|kF|\) values,
\[
\begin{aligned}
&H(\mathbf X\mid\mathbf C_0)\\
&\quad\le H(\mathbf X,Y\mid\mathbf C_0)\\
&\quad=H(Y\mid\mathbf C_0)+H(\mathbf X\mid\mathbf C_0,Y)\\
&\quad\le\log|kF|+H(\mathbf X\mid\mathbf C_0,Y).
\end{aligned}
\]
A cell of level \(J\) has a length of at most \(2\rho_J\), so it contains at most one point of \(F\). Hence \(\mathbf X\) is a function of \(\mathbf C_J\), and \(\mathbf C_J\) is a function of \(\mathbf X\); so \(H(\mathbf X\mid\mathbf C_0,Y)=H(\mathbf C_J\mid\mathbf C_0,Y)\). Because the cells are nested, \(\mathbf C_J\) determines \(\mathbf C_1,\dots,\mathbf C_{J-1}\), and the chain rule gives
\[
\begin{aligned}
&H(\mathbf C_J\mid\mathbf C_0,Y)\\
&\quad=\sum_{h=0}^{J-1}H\bigl(\mathbf C_{h+1}\mid\mathbf C_0,\dots,\mathbf C_h,Y\bigr)\\
&\quad=\sum_{h=0}^{J-1}H\bigl(\mathbf C_{h+1}\mid\mathbf C_h,Y\bigr).
\end{aligned}
\]
In the last step \(\mathbf C_h\) determines \(\mathbf C_0,\dots,\mathbf C_{h-1}\). \(\blacksquare\)

The left side does not depend on the scheme. So the inequality holds for the mean over the schemes of the right side. The next two sections bound the mean of one term of the sum.

## 4. One refinement after the sum is observed

In this section the cuts are fixed. Let \(A_1,\dots,A_k\) be cells, not necessarily different, each divided into at least two and at most eight children by cuts in its interior; cells that coincide are divided by the same cuts. Let \(X_1,\dots,X_k\) be independent random variables, \(X_i\) with finitely many values in \(A_i\), and \(Y=X_1+\dots+X_k\). Let \(m_i=\mathbb E X_i\); it lies in \(A_i\), because it is a mean of points of the interval \(A_i\). Let \(\mathbf C'\) be the tuple of the children that contain \(X_1,\dots,X_k\). Let \(a\) be the least of the distances \(|m_i-c|\), where \(1\le i\le k\) and \(c\) is a cut of \(A_i\), and
\[
p_i=\mathbb P\bigl(|X_i-m_i|\ge\tfrac a{4k}\bigr).
\]

**Lemma 4.1.** \(H(\mathbf C'\mid Y)\le9k\sum_{i=1}^kp_i\).

**Proof.** \(\mathbf C'\) takes at most \(8^k\) values, so \(H(\mathbf C'\mid Y)\le3k\). If \(a=0\), every \(p_i\) is \(1\) and the right side is \(9k^2\). Let \(a>0\).

Call the coordinate \(i\) *exceptional* if \(|X_i-m_i|\ge\tfrac a{4k}\), and let \(t=\sum_ip_i\). Let \(E\) be the event that at least two coordinates are exceptional, and \(q=\mathbb P(E)\). By independence
\[
q\le\sum_{i<j}p_ip_j\le t^2,\qquad q\le t,
\]
the second because \(E\) is contained in the union of the events that the coordinate \(i\) is exceptional. Let
\[
B=\Bigl\{\Bigl|Y-\sum_im_i\Bigr|\ge\frac a2\Bigr\}.
\]
If no coordinate is exceptional, then \(|Y-\sum_im_i|<k\cdot\tfrac a{4k}=\tfrac a4\). So \(B\) is also contained in that union, and \(\mathbb P(B)\le t\).

*Outside \(E\cup B\), every \(X_i\) lies in the same child as \(m_i\).* Suppose that \(X_i\) and \(m_i\) lie in different children of \(A_i\). Then a cut \(c\) of \(A_i\) satisfies \(m_i<c\le X_i\) or \(X_i<c\le m_i\), so \(|X_i-m_i|\ge|c-m_i|\ge a\), and \(i\) is exceptional. Outside \(E\) no other coordinate is exceptional, and
\[
\begin{aligned}
&\Bigl|Y-\sum_jm_j\Bigr|\\
&\quad\ge|X_i-m_i|-\sum_{j\ne i}|X_j-m_j|\\
&\quad\ge a-(k-1)\frac a{4k}>\frac a2 ,
\end{aligned}
\]
so \(B\) occurs.

Let \(\mathbf 1_E\) be the indicator of \(E\). By the rules of Proposition 2.1 of the lesson on entropy of finite random variables,
\[
\begin{aligned}
&H(\mathbf C'\mid Y)\\
&\quad\le H(\mathbf C',\mathbf 1_E\mid Y)\\
&\quad=H(\mathbf 1_E\mid Y)+H(\mathbf C'\mid Y,\mathbf 1_E)\\
&\quad\le h_2(q)+H(\mathbf C'\mid Y,\mathbf 1_E).
\end{aligned}
\]
The event \(B\) is determined by \(Y\). So the pair \((Y,\mathbf 1_E)\) determines whether \(E\cup B\) occurs. For a value of this pair for which it does not occur, \(\mathbf C'\) is the tuple of the children of the means, a constant, and the conditional entropy of \(\mathbf C'\) given this value is \(0\). For the other values it is at most \(3k\). Hence
\[
\begin{aligned}
H(\mathbf C'\mid Y,\mathbf 1_E)&\le3k\,\mathbb P(E\cup B)\\
&\le3k\,(q+t)\le6kt .
\end{aligned}
\]
By Lemma 5.1 of that lesson, \(h_2(q)\le3\sqrt q\le3t\). Together, \(H(\mathbf C'\mid Y)\le(3+6k)\,t\le9kt\). \(\blacksquare\)

The proof pays the entropy \(h_2\) of a flag only for the event \(E\), whose probability is at most \(t^2\); the event \(B\) is read off from the observed sum. This makes the bound linear in the probabilities \(p_i\), and a linear bound can be summed over the levels.

## 5. The average over the cuts

**Lemma 5.1.** Let \(h\ge0\), and let \(A_1,\dots,A_k\) be cells with lengths between \(\rho_h/2\) and \(2\rho_h\), divided by the rule of Section 2 with independent uniform numbers \(\theta\); cells that coincide are divided by the same cuts. Let \(X_i\), \(m_i\), \(a\) and \(p_i\) be as in Section 4, where the laws of the \(X_i\) do not depend on the cuts. Then the mean of \(p_i\) over the cuts satisfies
\[
\begin{aligned}
\mathbb E_{\mathrm{cuts}}\,p_i&\le\frac{1120\,k^2}{\rho_h}\,\mathbb E|X_i-m_i|\\
&\le\frac{1120\,k^2}{\rho_h}\,\mathbb E|X_i-X_i'|,
\end{aligned}
\]
where \(X_i'\) is independent of \(X_i\) and has the same law.

**Proof.** Let \(x\) be a value of \(X_i\) and \(u=|x-m_i|\). If \(u\ge\tfrac a{4k}\), then \(|m_j-c|\le4ku\) for some \(j\) and some cut \(c\) of \(A_j\). There are at most \(7k\) such pairs \((j,c)\), and by Lemma 2.1 (3) each of them satisfies this with a probability of at most \(160\,ku/\rho_h\). So
\[
\mathbb P_{\mathrm{cuts}}\bigl(u\ge\tfrac a{4k}\bigr)\le\frac{1120\,k^2}{\rho_h}\,u .
\]
Multiply by \(\mathbb P(X_i=x)\) and sum over \(x\): the left side becomes \(\mathbb E_{\mathrm{cuts}}\,p_i\) and the right side the first bound. For the second, \(x-m_i\) is the mean of \(x-X_i'\), so \(|x-m_i|\le\mathbb E|x-X_i'|\). \(\blacksquare\)

**The coupling of a partition.** Let \(\mathcal P\) be a finite set of disjoint cells whose union contains \(F\). For \(x,y\in F\) put
\[
\pi_{\mathcal P}(x,y)=\frac{\nu(\{x\})\,\nu(\{y\})}{\nu(A)}
\]
if \(x\) and \(y\) lie in the same cell \(A\) of \(\mathcal P\), and \(\pi_{\mathcal P}(x,y)=0\) otherwise. This is the law of a pair of points obtained by choosing a cell \(A\) with the probability \(\nu(A)\) and then two independent points with the law \(\nu(\cdot\mid A)\).

**Lemma 5.2.** Let \(r>0\), and let all the cells of \(\mathcal P\) have a length of at most \(2r\).

1. \(\sum_y\pi_{\mathcal P}(x,y)=\nu(\{x\})\) for every \(x\in F\).
2. For every integer \(\ell\), the sum \(\beta_\ell\) of \(\pi_{\mathcal P}(x,y)\) over the \((x,y)\) with \(2^{-\ell}\le|x-y|<2^{1-\ell}\) is at most \(c_\ell(\nu)\); and \(\beta_\ell=0\) unless \(2^{-\ell}<2r\).
3. The mean distance \(\sum_{x,y}|x-y|\,\pi_{\mathcal P}(x,y)\) is at most \(2\sum_\ell2^{-\ell}\,c_\ell(\nu)\), where the sum is over the \(\ell\) with \(2^{-\ell}\le2r\).

**Proof.** (1) The sum over the \(y\) in the cell \(A\) of \(x\) is \(\nu(\{x\})\nu(A)/\nu(A)\). (2) For a pair \(e=\{x,y\}\) of points of \(F\) with \(2^{-\ell}\le|x-y|<2^{1-\ell}\) let \(w_e=\pi_{\mathcal P}(x,y)+\pi_{\mathcal P}(y,x)=2\pi_{\mathcal P}(x,y)\). For every \(x\),
\[
\frac12\sum_{e\ni x}w_e\le\sum_y\pi_{\mathcal P}(x,y)=\nu(\{x\}),
\]
so the family is feasible, and \(\sum_ew_e=\beta_\ell\le c_\ell(\nu)\). Two points with \(\pi_{\mathcal P}(x,y)>0\) lie in one cell, so \(|x-y|<2r\); if \(\beta_\ell>0\), then \(2^{-\ell}<2r\). (3) The pairs with \(x=y\) contribute nothing, and every pair with \(x\ne y\) belongs to exactly one \(\ell\), where \(|x-y|<2\cdot2^{-\ell}\). So the left side is at most \(\sum_\ell2\cdot2^{-\ell}\beta_\ell\), and (2) applies. \(\blacksquare\)

**Proposition 5.3 (one level).** For \(0\le h<J\),
\[
\begin{aligned}
&\mathbb E_\theta\,H\bigl(\mathbf C_{h+1}\mid\mathbf C_h,Y\bigr)\\
&\quad\le20160\,k^4\sum_{\ell:\,2^{-\ell}\le2\rho_h}\frac{2^{-\ell}}{\rho_h}\,c_\ell(\nu).
\end{aligned}
\]

**Proof.** Fix the coordinates of the levels below \(h\). They determine the set \(\mathcal P_h\) of the cells of level \(h\). The term does not depend on the coordinates of the levels above \(h\). So it is enough to bound the mean over the coordinates of level \(h\), that is, over the cuts of the cells of \(\mathcal P_h\).

Let \((A_1,\dots,A_k)\) be a tuple of cells of \(\mathcal P_h\) with \(\nu(A_i)>0\). The event that \(X_i\in A_i\) for all \(i\) has the probability \(\prod_i\nu(A_i)\), and given this event the \(X_i\) are independent with the laws \(\nu(\cdot\mid A_i)\). By the definition of the conditional entropy,
\[
\begin{aligned}
&H\bigl(\mathbf C_{h+1}\mid\mathbf C_h,Y\bigr)\\
&\quad=\sum_{(A_i)}\prod_i\nu(A_i)\cdot H_{(A_i)}\bigl(\mathbf C_{h+1}\mid Y\bigr),
\end{aligned}
\]
where \(H_{(A_i)}\) is computed for the conditional law given the tuple. Under this law \(\mathbf C_{h+1}\) is the tuple \(\mathbf C'\) of Section 4. By Lemmas 4.1 and 5.1, the mean over the cuts of \(H_{(A_i)}(\mathbf C_{h+1}\mid Y)\) is at most
\[
\begin{aligned}
&9k\cdot\frac{1120\,k^2}{\rho_h}\sum_{i=1}^kD(A_i),\\
&D(A)=\sum_{x,y\in A}|x-y|\,\frac{\nu(\{x\})\,\nu(\{y\})}{\nu(A)^2}.
\end{aligned}
\]
Multiply by \(\prod_i\nu(A_i)\) and sum over the tuples. For each \(i\), the sum over the other cells is \(1\), and \(\sum_A\nu(A)D(A)=\sum_{x,y}|x-y|\,\pi_{\mathcal P_h}(x,y)\). So the mean over the cuts of \(H(\mathbf C_{h+1}\mid\mathbf C_h,Y)\) is at most
\[
\frac{10080\,k^4}{\rho_h}\sum_{x,y}|x-y|\,\pi_{\mathcal P_h}(x,y).
\]
The cells of level \(h\) have a length of at most \(2\rho_h\), and Lemma 5.2 (3) with \(r=\rho_h\) gives the stated bound. It does not depend on the coordinates of the levels below \(h\), so it also holds for the mean over all coordinates. \(\blacksquare\)

## 6. Proof of the theorem

Take the mean over the schemes in Lemma 3.1 and apply Proposition 5.3:
\[
\begin{aligned}
&k\bigl(H(\nu)-H^0_\rho(\nu)\bigr)-\log|kF|\\
&\quad\le20160\,k^4\sum_\ell c_\ell(\nu)\sum_{h}\frac{2^{-\ell}}{\rho_h},
\end{aligned}
\]
where the inner sum is over the \(h\) with \(0\le h<J\) and \(2^{-\ell}\le2\rho_h\). The numbers \(2^{-\ell}/\rho_h=4^h\,2^{-\ell}/\rho\) grow by the factor \(4\) from each \(h\) to the next, and they are summed only while they are at most \(2\). So the inner sum is at most \(2\,(1+\tfrac14+\tfrac1{16}+\dots)=\tfrac83\). It is empty unless \(2^{-\ell}\le2\rho_0=2\rho\). Since \(20160\cdot\tfrac83=53760\), this is Theorem 1.1. \(\blacksquare\)

The depth \(J\) of the scheme, which depends on the smallest distance in \(F\), has disappeared from the bound: a pair of points at a distance near \(2^{-\ell}\) is charged only at the levels \(h\) with \(\rho_h\ge2^{-\ell-1}\), with a weight that decreases geometrically for the coarser levels.

In [OpenAI-S, Section 4] the theorem is applied to finite laws with \(\log|kF|\le M\log(k+1)\) for all \(k\), with a number \(M\) that does not depend on \(k\), while the entropy inside the cells is at least a fixed positive multiple of \(M\). For a large \(k\), chosen in terms of this multiple, \(\log|kF|\) is then less than half of the left side, and the sum of the pair capacities is at least a positive multiple of \(M\).

## 7. Exercises

**7.1.** Show that \(c_\ell(\nu)>0\) exactly if \(F\) contains two points with \(2^{-\ell}\le|x-y|<2^{1-\ell}\). Deduce directly, without Theorem 1.1, that \(H(\nu)=H^0_\rho(\nu)\) if \(c_\ell(\nu)=0\) for all \(\ell\) with \(2^{-\ell}\le2\rho\).

**7.2.** Let \(\nu\) be uniform on \(\{0,1,2,3\}\), \(\rho=4\) and \(k=2\). Compute the left side of Theorem 1.1, \(|kF|\) and all the pair capacities.

**7.3.** Lemma 5.1 fails for cuts that are not random. Let \(k=1\), \(A_1=[0,1)\) with the single cut \(\tfrac12\), and let \(X_1\) take the values \(\tfrac12-3\varepsilon\) and \(\tfrac12+\varepsilon\) with the probability \(\tfrac12\) each, where \(0<\varepsilon<\tfrac16\). Compute \(a\), \(p_1\) and \(\mathbb E|X_1-m_1|\).

**7.4.** For \(\nu\) uniform on \(\{0,1,2,3\}\) and the partition into \([0,2)\) and \([2,4)\), compute \(\pi_{\mathcal P}\) and check the three statements of Lemma 5.2 with \(r=1\).

## 8. Solutions

**7.1.** If there is no such pair, the capacity is \(0\) by definition. If \(e=\{x,y\}\) is such a pair, the family with \(w_e=2\min\{\nu(\{x\}),\nu(\{y\})\}>0\) and all other weights \(0\) is feasible. Now let all the \(c_\ell(\nu)\) with \(2^{-\ell}\le2\rho\) vanish, and suppose that two different points \(x,y\) of \(F\) lie in one cell of the length \(\rho\). Then \(0<|x-y|<\rho\), and the \(\ell\) with \(2^{-\ell}\le|x-y|<2^{1-\ell}\) has \(2^{-\ell}<\rho\) and \(c_\ell(\nu)>0\), a contradiction. So every cell contains at most one point of \(F\), \(X\) is a function of its cell, and \(H(X\mid\lfloor X/\rho\rfloor)=0\).

**7.2.** All points lie in \([0,4)\), so \(H^0_4(\nu)=0\) and \(H(\nu)=2\); the left side is \(4\). The sums of two points are \(0,\dots,6\), so \(|2F|=7\) and \(\log7<2.81\). The distances are \(1,2,3\). For \(\ell=0\), the pairs \(\{0,1\}\) and \(\{2,3\}\) with the weights \(\tfrac12\) are feasible, so \(c_0=1\). For \(\ell=-1\), the pairs \(\{0,2\}\) and \(\{1,3\}\) with the weights \(\tfrac12\) give \(c_{-1}=1\). All other capacities are \(0\). The theorem states \(4\le\log7+2C_2\).

**7.3.** \(m_1=\tfrac12-\varepsilon\), so \(a=\varepsilon\). Both values have \(|X_1-m_1|=2\varepsilon\ge\tfrac\varepsilon4\), so \(p_1=1\), while \(\mathbb E|X_1-m_1|=2\varepsilon\) is as small as one likes. With a cut that is uniform on an interval, the probability that it lies within \(8\varepsilon\) of the mean is small, and only then is \(p_1\) different from \(0\).

**7.4.** \(\nu(A)=\tfrac12\) for both cells, so \(\pi_{\mathcal P}(x,y)=\tfrac1{16}/\tfrac12=\tfrac18\) for the eight pairs \((x,y)\) in a common cell, including \(x=y\). (1) Every \(x\) has two partners: \(\tfrac28=\tfrac14\). (2) The pairs with \(x\ne y\) have the distance \(1\), so \(\beta_0=\tfrac48=\tfrac12\le c_0=1\), and the other \(\beta_\ell\) are \(0\). (3) The left side is \(\tfrac12\). On the right, the \(\ell\) with \(2^{-\ell}\le2\) and \(c_\ell>0\) are \(0\) and \(-1\), by Exercise 7.2, and the right side is \(2\,(1+2)=6\).

## References

- [OpenAI-S] OpenAI, *The entropy-rate dimension formula for self-similar measures on the line*, OpenAI Math Release preprint, 24 September 2026, Sections 3 and 4. https://github.com/openai/math/tree/main/preprints/The-entropy-rate-dimension-formula-for-self-similar-measures-on-the-line-September-24-2026
