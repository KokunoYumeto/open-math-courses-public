# The stopped walk and the cotype inequality

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves that \(\ell_1\) has metric Markov cotype two with the constant \(12\sqrt{21}\). Given points \(x_1,\dots,x_n\) of \(\ell_1\) on the states of a chain and a number \(t\), the new points are built in three moves. The points are replaced by vertices \(z_i\) of a cube (the cut representation). The vertex \(z_i\) is replaced by the mean \(h_i\) of the vertices at which a walk from \(i\) arrives if it stops after every step with the probability \(1/(t+1)\). Then the cubic map is applied and the result is mapped back into \(\ell_1\). The same points have a second description: \(y_i\) is the mean of the coordinatewise median of three independent copies of the place where the walk from \(i\) stops.

- The new points and the first-step identity (Section 1).
- The energy inequality with the constant \(108\) (Proposition 2.1).
- The theorem, for reversible and for stationary matrices (Theorem 3.1).
- The walk that stops; the mean of medians of three (Proposition 4.2).
- The example of two states that are exchanged (Section 5).

The lesson follows [OpenAI-MC, Section 5]. It uses the definitions, Lemma 1.1 and Proposition 4.3 of [Metric Markov cotype two](metric-markov-cotype-two.md), and Proposition 1.2, Lemma 2.1 and Corollary 4.1 of [Cuts, the cubic map and a quartic potential](cuts-the-cubic-map-and-a-quartic-potential.md).

## 1. The new points

Throughout Sections 1 and 2 the following are fixed: a stochastic matrix \(A=(a_{ij})\) on \([n]\) with a stationary vector \(\pi\); an integer \(t\ge1\); and points \(x_1,\dots,x_n\in\ell_1\) that are not all equal. Reversibility of \(A\) is not assumed.

The cut representation gives a finite nonempty set \(\mathcal B\) with weights \(w_B>0\), vertices \(z_1,\dots,z_n\) of the cube \(Q=[0,1]^{\mathcal B}\), and an affine map \(T\) from \(\mathbb R^{\mathcal B}\) to \(\ell_1\) with
\[
\begin{aligned}
T(z_i)&=x_i,\\
\|x_i-x_j\|_1&=\|z_i-z_j\|_H^2,\\
\|T(u)-T(u')\|_1&\le\|u-u'\|_{1,w} .
\end{aligned}
\]
Here \(\|\cdot\|_{1,w}\) and \(\|\cdot\|_H\) are the weighted norms of the cube, and \(\Phi\) is the map of \(Q\) that applies \(\phi(r)=3r^2-2r^3\) in every coordinate.

Put \(p=1/(t+1)\) and \(q=t/(t+1)\), and let
\[
G=p\sum_{s\ge0}q^sA^s
\]
be the geometric average of the powers of \(A\) with the ratio \(q\). It is a stochastic matrix with the stationary vector \(\pi\).

**Definition.** For \(i\in[n]\) put
\[
h_i=\sum_jG_{ij}\,z_j,\qquad y_i=T\bigl(\Phi(h_i)\bigr) .
\]

The vector \(h_i\) is an average of vertices with the weights \(G_{ij}\ge0\) of sum \(1\), so \(h_i\in Q\), and \(\Phi(h_i)\in Q\) is defined. The points \(y_i\) lie in \(\ell_1\).

In terms of a walk: start at \(i\), move with the matrix \(A\), and after every arrival (also at the start) stop with the probability \(p\). The walk stops at \(j\) with the probability \(G_{ij}\), and the number of steps before it stops has the mean \(t\). The coordinate \(h_i(B)=\sum_{j\in B}G_{ij}\) is the probability that the walk from \(i\) stops inside the cut \(B\).

**Lemma 1.1** (first-step identity). For every \(i\),
\[
h_i=p\,z_i+q\sum_ja_{ij}\,h_j .
\]

**Proof.** By Lemma 1.1 of the first lesson, \(G=pI+qAG\). Apply both sides to the family \((z_j)\). \(\blacksquare\)

The identity says: the walk at \(i\) stops there with the probability \(p\), and otherwise moves to \(j\) with the probability \(a_{ij}\) and goes on from there.

## 2. The energy inequality

Two numbers measure the new vertices \(\Phi(h_i)\): the cost of the replacement and the one-step energy,
\[
\begin{aligned}
\mathcal U&=\sum_i\pi_i\,\|z_i-\Phi(h_i)\|_{1,w}^2,\\
\mathcal V&=\sum_{i,j}\pi_ia_{ij}\,\|\Phi(h_i)-\Phi(h_j)\|_{1,w}^2 .
\end{aligned}
\]
Recall the energy \(\mathcal E_G(x)=\sum_{i,j}\pi_iG_{ij}\|x_i-x_j\|_1^2\).

**Proposition 2.1.** \(\mathcal U+t\,\mathcal V\le108\,\mathcal E_G(x)\).

**Proof.** *Step 1: the cost of one state.* For \(i\in[n]\) let
\[
\begin{aligned}
\kappa_i&=p\,\|z_i-\Phi(h_i)\|_{1,w}^2\\
&\quad+q\sum_ja_{ij}\,\|\Phi(h_j)-\Phi(h_i)\|_{1,w}^2 .
\end{aligned}
\]
Then \(\sum_i\pi_i\kappa_i=p\,\mathcal U+q\,\mathcal V\).

*Step 2: the inequality for one state.* Fix an index \(r\) and let \(e=z_r\); this is a vertex of \(Q\). With the potential \(F_e(u)=\|u-e\|_H^4\) put
\[
f_i=F_e(h_i),\qquad g_i=F_e(z_i) .
\]
So \(g_i=\|z_i-z_r\|_H^4=\|x_i-x_r\|_1^2\). Apply Corollary 4.1 of the lesson on the cubic map to the point \(u=h_i\) and the following points with weights: the point \(z_i\) with the weight \(p\), and the points \(h_j\) with the weights \(q\,a_{ij}\). The weights are \(\ge0\) with the sum \(1\), and by Lemma 1.1 the weighted mean of the points is \(h_i\). Since \(\Phi(z_i)=z_i\), the corollary gives
\[
\kappa_i\le108\,\Bigl(p\,g_i+q\sum_ja_{ij}f_j-f_i\Bigr) .
\]
Write this as an inequality between vectors indexed by \(i\): \(\kappa\le108\,(p\,g+q\,Af-f)\) in every entry.

*Step 3: summing along the walk.* Let \(m\ge0\). The matrix \(q^mA^m\) has entries \(\ge0\), so it keeps inequalities between vectors. Its row \(r\) gives
\[
\begin{aligned}
&q^m(A^m\kappa)_r\\
&\quad\le108\,\bigl(p\,q^m(A^mg)_r+q^{m+1}(A^{m+1}f)_r\\
&\qquad\qquad-q^m(A^mf)_r\bigr) .
\end{aligned}
\]
Sum over \(m=0,\dots,L-1\). The last two terms telescope:
\[
\begin{aligned}
&\sum_{m<L}q^m(A^m\kappa)_r\\
&\quad\le108\,\Bigl(p\sum_{m<L}q^m(A^mg)_r\\
&\qquad\qquad+q^L(A^Lf)_r-f_r\Bigr) .
\end{aligned}
\]
On the right, \(p\sum_{m<L}q^m(A^mg)_r\le(Gg)_r\) because \(g\ge0\); \(f_r\ge0\); and \(q^L(A^Lf)_r\le q^L\max_if_i\), which tends to \(0\) as \(L\to\infty\). The terms on the left are \(\ge0\). So
\[
\begin{aligned}
&\sum_{m\ge0}q^m(A^m\kappa)_r\le108\,(Gg)_r\\
&\qquad=108\sum_jG_{rj}\,\|x_j-x_r\|_1^2 .
\end{aligned}
\]

*Step 4: the average over the start.* The numbers \(\kappa_i\) do not depend on \(r\); only \(f\) and \(g\) do. Multiply the last inequality by \(\pi_r\) and sum over \(r\). Because \(\pi\) is stationary, \(\sum_r\pi_r(A^m\kappa)_r=\sum_i\pi_i\kappa_i\) for every \(m\). So the left side becomes
\[
\begin{aligned}
\sum_{m\ge0}q^m\sum_i\pi_i\kappa_i&=\frac1p\,\bigl(p\,\mathcal U+q\,\mathcal V\bigr)\\
&=\mathcal U+t\,\mathcal V ,
\end{aligned}
\]
because \(q/p=t\). The right side becomes \(108\,\mathcal E_G(x)\). \(\blacksquare\)

Three choices in this proof deserve a comment.

*The vertex \(e\) depends on the start.* For the walk that starts at \(r\) the potential is centred at the vertex \(z_r\) of the starting point. So the potential at the place \(j\) where the walk stops is \(\|z_j-z_r\|_H^4=\|x_j-x_r\|_1^2\): the squared distance in \(\ell_1\) between the start and the end. This is how the fourth power in \(H\) meets the square in \(\ell_1\).

*The stopping probability.* The sum \(\sum_mq^m=1/p\) counts the mean number of arrivals of the walk. Each arrival costs \(p\) times a term of \(\mathcal U\) and \(q\) times a term of \(\mathcal V\). The quotient \(q/p\) is the factor in front of \(\mathcal V\), and \(p=1/(t+1)\) makes it equal to \(t\).

*What was dropped.* Step 3 dropped the term \(-f_r=-\|h_r-z_r\|_H^4\). Keeping it gives the sharper inequality
\[
\begin{aligned}
&\mathcal U+t\,\mathcal V\\
&\quad\le108\,\Bigl(\mathcal E_G(x)-\sum_r\pi_r\|h_r-z_r\|_H^4\Bigr) .
\end{aligned}
\]

## 3. The theorem

**Theorem 3.1** ([OpenAI-MC, Section 1 and Section 5]). Let \(A\) be a stochastic matrix on \([n]\) with a stationary vector \(\pi\), let \(t\ge1\) and \(x_1,\dots,x_n\in\ell_1\). Then there are \(y_1,\dots,y_n\in\ell_1\) with
\[
\begin{aligned}
&\sum_i\pi_i\,\|x_i-y_i\|_1^2+t\,\mathcal E_A(y)\\
&\qquad\le3024\,\mathcal E_{M_t}(x) ,
\end{aligned}
\]
where \(\mathcal E_A(y)=\sum_{i,j}\pi_ia_{ij}\|y_i-y_j\|_1^2\) and \(M_t=\frac1t\sum_{s=1}^tA^s\). If the points \(x_i\) are not all equal, the points \(y_i=T(\Phi(h_i))\) of Section 1 have this property.

**Proof.** If all \(x_i\) are equal, take \(y_i=x_i\); the left side is \(0\). Otherwise use the points of Section 1. Since \(T(z_i)=x_i\) and \(T\) does not increase distances from \(\|\cdot\|_{1,w}\) to \(\|\cdot\|_1\),
\[
\begin{aligned}
\|x_i-y_i\|_1&=\|T(z_i)-T(\Phi(h_i))\|_1\\
&\le\|z_i-\Phi(h_i)\|_{1,w},\\
\|y_i-y_j\|_1&\le\|\Phi(h_i)-\Phi(h_j)\|_{1,w} .
\end{aligned}
\]
So the left side of the theorem is at most \(\mathcal U+t\,\mathcal V\). By Proposition 2.1 this is at most \(108\,\mathcal E_G(x)\), and by Proposition 4.3 of the first lesson \(\mathcal E_G(x)\le28\,\mathcal E_{M_t}(x)\). Finally \(108\cdot28=3024\). \(\blacksquare\)

**Corollary 3.2.** The real space \(\ell_1\) has metric Markov cotype two with the constant \(12\sqrt{21}\).

**Proof.** A matrix that is reversible for \(\pi\) has the stationary vector \(\pi\), and \(3024=144\cdot21\). \(\blacksquare\)

Theorem 3.1 is a little more than the definition asks: it holds for every stationary vector, without reversibility. The cyclic shift of three states is an example of a matrix that is covered by the theorem and not by the definition.

The constant \(3024\) is the product of the constant \(108\) of the flat inequality and the constant \(28\) of the comparison of the two averages. No attempt is made to find the best constant. In the examples computed for this course (random chains with up to five states, and walks on cycles) the quotient of the two sides did not exceed \(1.01\).

## 4. The walk that stops, and medians of three

The proof of Proposition 2.1 was written with sums. It has a reading in terms of chance, which explains where it comes from. Consider the walk with stopping of Section 1, started at an index \(r\). At every time it is either *alive* at an index \(i\) or it has *stopped* at an index \(i\). Attach to it the vector \(h_i\) while it is alive at \(i\), and the vertex \(z_i\) once it has stopped at \(i\). From the state *alive at \(i\)* the walk goes to *stopped at \(i\)* with the probability \(p\) and to *alive at \(j\)* with the probability \(q\,a_{ij}\). The first-step identity says that the mean of the attached vector after this step is the attached vector before it. The number \(\kappa_i\) is the mean squared change of the image under \(\Phi\) of the attached vector in this step. The walk is alive at time \(m\) and at \(i\) with the probability \(q^m(A^m)_{ri}\). So \(\sum_mq^m(A^m\kappa)_r\) is the mean of the sum of all squared changes along the walk, and Step 3 bounds it by \(108\) times the mean of the potential at the end, which is \(\|x_j-x_r\|_1^2\) if the walk stops at \(j\).

The second description of the points \(y_i\) uses medians. For three real numbers the *median* is the middle one. For three vectors \(x,x',x''\in\ell_1\) let \(\operatorname{med}(x,x',x'')\) be the vector whose coordinate \(k\) is the median of \(x(k),x'(k),x''(k)\). It lies in \(\ell_1\), because the absolute value of the median is at most \(|x(k)|+|x'(k)|+|x''(k)|\).

**Lemma 4.1.** In the setting of Section 1, for all \(j_1,j_2,j_3\in[n]\),
\[
\operatorname{med}(x_{j_1},x_{j_2},x_{j_3})=T(\mu),
\]
where \(\mu\in\{0,1\}^{\mathcal B}\) is the vertex with \(\mu_B=1\) exactly if at least two of the three indices \(j_1,j_2,j_3\) (counted with repetition) lie in \(B\).

**Proof.** Fix a coordinate \(k\), let \(\alpha_1<\dots<\alpha_m\) be the different values of \(x_1(k),\dots,x_n(k)\) and \(B_r=\{i:x_i(k)\ge\alpha_{r+1}\}\). By Lemma 1.1 of the lesson on cuts, \(T(\mu)(k)\) is \(\alpha_1\) plus the sum of the gaps \(\alpha_{r+1}-\alpha_r\) over those \(r\) for which at least two of the three indices lie in \(B_r\). At least two of the indices lie in \(B_r\) exactly if at least two of the three values \(x_{j_a}(k)\) are \(\ge\alpha_{r+1}\), that is, exactly if their median is \(\ge\alpha_{r+1}\). The sum of the gaps below the median is the median minus \(\alpha_1\). \(\blacksquare\)

**Proposition 4.2** (mean of medians). In the setting of Section 1, for every \(i\),
\[
\begin{aligned}
y_i=\sum_{j_1,j_2,j_3}&G_{ij_1}G_{ij_2}G_{ij_3}\\
&\times\operatorname{med}(x_{j_1},x_{j_2},x_{j_3}) .
\end{aligned}
\]

In words: let \(J_1,J_2,J_3\) be three independent copies of the place where the walk from \(i\) stops. Then \(y_i\) is the mean of the coordinatewise median of \(x_{J_1},x_{J_2},x_{J_3}\).

**Proof.** The map \(T\) is affine and the weights \(G_{ij_1}G_{ij_2}G_{ij_3}\) are \(\ge0\) with the sum \(1\). So by Lemma 4.1 the right side is \(T(\bar\mu)\), where \(\bar\mu\) is the mean of the vertices \(\mu\) with these weights. The coordinate \(\bar\mu_B\) is the total weight of the triples with at least two indices in \(B\). The three indices are independent, and each lies in \(B\) with the probability \(\sum_{j\in B}G_{ij}=h_i(B)\). By Lemma 2.1 of the lesson on the cubic map, the probability that at least two of three independent events of probability \(h_i(B)\) occur is \(\phi(h_i(B))\). So \(\bar\mu=\Phi(h_i)\) and the right side is \(T(\Phi(h_i))=y_i\). \(\blacksquare\)

So the points \(y_i\) do not depend on the cuts: they are determined by the points \(x_j\) and the matrix \(G\). The description also shows the two roles of the construction. The average over the place where the walk stops smooths the points along the chain. The median of three, in place of a plain average of the vectors, is the nonlinear operation that keeps the smoothed points close to the old ones in the norm of \(\ell_1\).

## 5. An example: two states that are exchanged

Let \(n=2\), \(\pi=(\tfrac12,\tfrac12)\), let \(A\) exchange the two states, and let \(x_1=0\) and \(x_2=1\) in the first coordinate of \(\ell_1\) (all other coordinates are \(0\)). In Example 2.3 of the first lesson, \(\mathcal E_{M_t}(x)=\lceil t/2\rceil/t\ge\tfrac12\), and the choice \(y=x\) costs \(t\).

There is one cut, \(\{2\}\), with the weight \(1\); \(z_1=0\), \(z_2=1\), and \(T(u)=u\) in the first coordinate. The powers of \(A\) are \(A\) for odd and \(I\) for even exponents, so
\[
G_{12}=p\sum_{s\ \mathrm{odd}}q^s=\frac{pq}{1-q^2}=\frac q{1+q} .
\]
With \(q=t/(t+1)\) this gives
\[
h_1=\frac t{2t+1},\qquad h_2=\frac{t+1}{2t+1} .
\]
Put \(\eta=\frac1{2(2t+1)}\), so that \(h_1=\tfrac12-\eta\) and \(h_2=\tfrac12+\eta\). Since \(\phi(\tfrac12\pm\eta)=\tfrac12\pm(\tfrac32\eta-2\eta^3)\),
\[
y_1=\tfrac12-\bigl(\tfrac32\eta-2\eta^3\bigr),\qquad y_2=1-y_1 .
\]
For \(t=1\): \(h_1=\tfrac13\), \(y_1=\tfrac7{27}\), \(y_2=\tfrac{20}{27}\). For large \(t\) both points are close to \(\tfrac12\). The left side of the cotype inequality is
\[
\begin{aligned}
&\tfrac12\,y_1^2+\tfrac12\,(1-y_2)^2+t\,(y_2-y_1)^2\\
&\qquad=y_1^2+t\,(3\eta-4\eta^3)^2 .
\end{aligned}
\]
Here \(y_1\le\tfrac12\), and \(t\,(3\eta)^2=\frac{9t}{4(2t+1)^2}\le\frac9{32}\) because \((2t+1)^2\ge8t\). So the left side is at most \(\tfrac14+\tfrac9{32}=\tfrac{17}{32}\) for every \(t\), while \(\mathcal E_{M_t}(x)\ge\tfrac12\). In this example the quotient of the two sides is at most \(\tfrac{17}{16}\).

## 6. Exercises

**6.1.** Show that \(\sum_i\pi_ih_i=\sum_i\pi_iz_i\).

**6.2.** Show that every coordinate of \(y_i\) lies between the smallest and the largest of the numbers \(x_1(k),\dots,x_n(k)\).

**6.3.** Compute the points \(y_i\) (a) for \(A=I\); (b) if every row of \(A\) is equal to \(\pi\), in terms of \(z_i\) and \(\bar z=\sum_j\pi_jz_j\).

**6.4.** In the example of Section 5 with \(t=1\), compute the left side of the cotype inequality exactly.

**6.5.** Let all points \(x_i\) have only the values \(0\) and \(1\) in every coordinate. Show that \(y_i(k)=\phi(g_i(k))\), where \(g_i(k)=\sum_jG_{ij}x_j(k)\).

## 7. Solutions

**6.1.** \(\sum_i\pi_iG_{ij}=\pi_j\) because \(\pi\) is stationary for \(G\). So \(\sum_i\pi_ih_i=\sum_j\pi_jz_j\).

**6.2.** \(y_i=T(u)\) with \(u=\Phi(h_i)\in Q\). By Exercise 5.2 of the lesson on cuts, every coordinate of \(T(u)\) with \(u\in Q\) lies between the smallest and the largest value of the points in this coordinate. Another proof: a median of three of the values lies between these bounds, and so does a mean of such medians (Proposition 4.2).

**6.3.** (a) \(G=I\), so \(h_i=z_i\), \(\Phi(z_i)=z_i\) and \(y_i=T(z_i)=x_i\). (b) \(A^s=A\) for \(s\ge1\), so \(G=pI+qA\) and \(h_i=p\,z_i+q\,\bar z\); then \(y_i=T(\Phi(p\,z_i+q\,\bar z))\). For large \(t\) the number \(p\) is small and all \(y_i\) are close to \(T(\Phi(\bar z))\).

**6.4.** \(y_1=\tfrac7{27}\), \(y_2=\tfrac{20}{27}\), \(y_2-y_1=\tfrac{13}{27}\). The left side is \(\tfrac{49}{729}+\tfrac{169}{729}=\tfrac{218}{729}\), and \(\mathcal E_{M_1}(x)=1\).

**6.5.** Fix \(k\). If all \(x_j(k)\) are equal, both sides are this common value, because \(\phi(0)=0\) and \(\phi(1)=1\). Otherwise the values are \(0<1\), and by Lemma 1.1 of the lesson on cuts the only cut with \(b_B(k)>0\) is \(B=\{j:x_j(k)=1\}\), with \(b_B(k)=1\); also \(v(k)=0\). So \(y_i(k)=\phi(h_i(B))\), and \(h_i(B)=\sum_{j\in B}G_{ij}=\sum_jG_{ij}x_j(k)\).

## References

- [OpenAI-MC] OpenAI, *Metric Markov Cotype Two of \(\ell_1\)*, OpenAI Math Release preprint, 5 October 2026, Sections 1 and 5. https://github.com/openai/math/tree/main/preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026
