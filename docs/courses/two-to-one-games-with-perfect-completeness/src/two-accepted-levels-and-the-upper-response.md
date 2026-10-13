# Two accepted levels and the upper response

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let a labeling of the game of the reduction satisfy a random test with a probability of at least \(\varepsilon\). This lesson draws the first consequences. If the tree is deep enough, there are two levels \(i<j\) of the path at which the constraints are satisfied at the same time with a probability of about \(\varepsilon^2\). The answers of the labeling at the upper level \(j\) are collected in a table on matrices, and the constraint at the level \(j\) shows that this table often keeps its value under the step of rank one. The inverse theorem then gives a slice on which the table is mostly one value. This value determines a set \(z_0+Z\) of linear functionals such that, on the slice, the answer of the right player at the *lower* level \(i\) contains the vector \(Mz_0+\hat y\) more often than a fixed fraction of the time. Every functional of the set takes the value \(1\) at the constant \(1\), and on the products of the rows at a node of the level \(i\) it takes the values of a matrix of rank at most one.

- Two accepted levels (Lemma 1.1) and the modified law at the lower level (Lemma 2.1).
- The response table and the response at a matrix (Lemma 3.1).
- Equality along a step (Lemma 4.1, Proposition 4.2).
- Good advice, the functionals \(z_0+Z\) and the events \(I\subset J\) (Lemmas 5.1 to 5.3).
- The prediction of the upper response (Proposition 6.1).

The lesson follows [OpenAI-G, Sections 5.1 and 5.2]. It uses the questions and constraints of [The tree of function spaces and the questions](the-tree-of-function-spaces-and-the-questions.md), the lemmas of [Folding and the law of the tests](folding-and-the-law-of-the-tests.md), Lemma 4.2 of [Matrices, slices and the inverse theorem](matrices-slices-and-the-inverse-theorem.md) with its hypothesis (GE), and the comparisons of laws of [Changing the law of the tests](changing-the-law-of-the-tests.md), with the notation \(b_k=2^{\ell_k}-1\), \(c_k=2R_k\), \(T_p\), \(L_p\).

## 1. Two accepted levels

Fix the parameters \(t,d,n_p,\ell_p,R_p\) and a labeling: one label at every key. Draw \(E\), the path and the array family \(\mathbf M\) as in the test, and draw for every level \(p\in\{1,\dots,d\}\) an independent uniform nonzero vector \(a_p\in K_p\). Let \(\operatorname{Acc}_p\) be the event that the labeling satisfies the constraint of \((E,\mathbf M,D_p,a_p)\). The test of the game uses one level \(p\), uniform in \(\{1,\dots,d\}\). So the probability that the labeling satisfies the test is
\[
\frac1d\sum_{p=1}^d\mathbb P(\operatorname{Acc}_p).
\]

**Lemma 1.1.** Let this probability be at least \(\varepsilon\), with \(0<\varepsilon\le1\) and \(d\varepsilon\ge4\). Then there are levels \(i<j\) with
\[
\mathbb P(\operatorname{Acc}_i\cap\operatorname{Acc}_j)\ge\frac{3\varepsilon^2}4 .
\]

**Proof.** Let \(\nu\) be the number of the levels \(p\) at which \(\operatorname{Acc}_p\) holds. Then \(\mathbb E\nu\ge d\varepsilon\ge4\), and
\[
\begin{aligned}
\sum_{p\ne q}\mathbb P(\operatorname{Acc}_p\cap\operatorname{Acc}_q)&=\mathbb E\,\nu(\nu-1)\\
&\ge(\mathbb E\nu)^2-\mathbb E\nu\\
&\ge d^2\varepsilon^2-d\varepsilon ,
\end{aligned}
\]
because \(x^2-x\) increases for \(x\ge\tfrac12\). The sum has \(d(d-1)\) terms, so one of them is at least
\[
\frac{d\varepsilon^2-\varepsilon}{d-1}\ \ge\ \varepsilon^2-\frac\varepsilon d\ \ge\ \frac{3\varepsilon^2}4 ,
\]
where the last step uses \(1/d\le\varepsilon/4\). \(\blacksquare\)

No independence of the events \(\operatorname{Acc}_p\) was used.

## 2. The modified law at the lower level

Fix levels \(i<j\). The comparisons of laws need numbers of calls. At \(D_j\) we use \(T'=T_j+1\) calls: the calls of the arrays at \(D_d,\dots,D_j\) and one more. By Proposition 4.3 of the lesson on changing the law, these calls and the arrays at \(D_{j-1},\dots,D_i\) are computed from
\[
T=T'\prod_{h=i+1}^jc_h+\sum_{k=i}^{j-1}b_k\prod_{h=i+1}^kc_h
\]
calls at \(D_i\). Let \(L_j\) and \(L_i\) be the bounds of that lesson for these numbers of calls, let \(\beta=n_i^{-2/3}\), and
\[
\begin{aligned}
\delta_i&=\frac12\sqrt{\frac{L_i}{n_i}}+\frac12\sqrt{(1+\beta^2L_i)^{n_i}-1},\\
\delta_{ij}&=\frac12\sqrt{\frac{L_j}{n_j}}+\delta_i .
\end{aligned}
\]

**The law \(\mathbb P_i\).** Draw \(E\), the path from the root to \(D_i\) and the exterior data \(\Xi_i\) as in the test, and the blocks of the children of \(D_i\) with the modified law \(\mathsf M_i\): each child is marked with the probability \(\beta\), the left questions below the marked children are replaced by right questions, which gives the mixed family \(O\), and the contributions and the arrays of the blocks are uniform in the spaces of \(O\). The arrays at the path nodes above \(D_i\) are computed from the calls. The vectors \(a_1,\dots,a_d\) are independent of all this.

Under \(\mathbb P_i\) every array has its rows in the spaces \(H_D(O)\subset H_D(E)\). So \(\mathbf M\) is an array family for \(O\), and, read on \(\Omega(E)\), an array family for \(E\). By Lemma 4.3 of the lesson on the tree of function spaces, the joint functions of the two readings have the same keys and the same restored values, also after a map \(\Theta_{D,a}\). So the events \(\operatorname{Acc}_p\) are defined under \(\mathbb P_i\), and the constraint of \((E,\mathbf M,D_p,a_p)\) joins the same two keys as the constraint formed with \(O\).

*Calls under \(\mathbb P_i\).* Given \(E\), the marks, \(O\) and the path to \(D_i\), the calls at \(D_i\) are independent and uniform in \(H_{D_i}(O)\), and a call at a path node \(D_k\) with \(k>i\) is formed by the rule of the sampler: uniform functions at the children of \(D_k\) off the path, and \(c_k\) calls at \(D_{k-1}\). Every call has its own draws. So, given these data, different calls are independent of each other, and a call is independent of every array that is not computed from it.

**Lemma 2.1.** The probabilities of \(\operatorname{Acc}_i\cap\operatorname{Acc}_j\) under the law of the test and under \(\mathbb P_i\) differ by at most \(\delta_i\). So under the assumptions of Lemma 1.1, for the levels \(i<j\) found there, and if \(\delta_i\le\varepsilon^2/4\),
\[
\mathbb P_i(\operatorname{Acc}_i\cap\operatorname{Acc}_j)\ge c,\qquad c=\frac{\varepsilon^2}2 .
\]

**Proof.** Given \(E\) and the path to \(D_i\), the array family is a function of \(\Xi_i\) and of the blocks at \(D_i\), in the test and under \(\mathbb P_i\), and the event is a function of the array family, of the nodes \(D_i,D_j\) and of \(a_i,a_j\). By Propositions 3.1 and 4.1 of the lesson on changing the law, the two laws of the blocks differ by at most \(\delta_i\) in total variation. \(\blacksquare\)

## 3. The response table

Write \(H=H_{D_j}(E)\), \(K=K_j\), \(\ell=\ell_j\) and \(M=M_{D_j}\). The *background* \(\Gamma\) consists of \(E\), of the path from the root to \(D_j\), and of the arrays at all nodes other than \(D_j\). Let \(\mathcal N\) be the set of all nodes of the level \(i\) below \(D_j\). The background does not say which node of \(\mathcal N\) is \(D_i\).

Let \(B=B(\Gamma)\subset H\) be the span of the constant \(1\) and of the products \((M_C)_u(M_C)_v\), where \(C\in\mathcal N\) and \(u,v\) are rows of \(M_C\). These products lie in \(H\) by Lemma 2.1 of the lesson on the tree of function spaces. Let \(\pi:H\to H/B\) be the quotient map. Fix a rule that chooses, for every \(\Gamma\), a linear map \(s:H/B\to H\) with \(\pi\circ s=\mathrm{id}\); then \(H=B\oplus s(H/B)\). The maps \(\pi\) and \(s\) are applied to matrices row by row, and for a matrix \(M\in K\otimes H\) we write \(\bar M=\pi M\in K\otimes(H/B)\).

**Definition.** For \(\bar M\in K\otimes(H/B)\) take the array family with the arrays of \(\Gamma\) and the array \(s(\bar M)\) at \(D_j\), and the label that the labeling gives at the left key of its joint function. The value of the *response table* is
\[
f_\Gamma(\bar M)=\bigl(\hat y,(y_C)_{C\in\mathcal N}\bigr),
\]
where \(\hat y\in K\) is the restored value of this label at \(D_j\) and \(y_C\in K_i\) its restored value at \(C\).

The table contains the restored values at all nodes of \(\mathcal N\), without a mark at \(D_i\). The number of its possible values is large; no bound of this lesson depends on it.

For a value \((\hat y,(y_C))\) of the table, let \(b_y:B\to\mathbb F\) be the functional of Lemma 2.1 of the lesson on folding, for the node \(D_j\) and the set \(\mathcal N\): it is linear, \(b_y(1)=1\), and \(b_y((M_C)_u(M_C)_v)=(y_C)_u(y_C)_v\). For a matrix \(\Delta\in K\otimes B\) let \(\Delta b_y\in K\) be the vector with the coordinates \(b_y(\Delta_h)\), where \(\Delta_h\) is the row \(h\).

**Lemma 3.1.** Let \(M\in K\otimes H\), \((\hat y,(y_C))=f_\Gamma(\bar M)\) and \(\Delta=M-s(\bar M)\). Then \(\Delta\in K\otimes B\), and the label that the labeling gives at the left key of the family with the arrays of \(\Gamma\) and \(M\) at \(D_j\) has the restored values
\[
y_C\ \text{ at }C\in\mathcal N,\qquad \hat y+\Delta b_y\ \text{ at }D_j .
\]

**Proof.** \(\pi\Delta=\bar M-\bar M=0\), so the rows of \(\Delta\) lie in \(B\): each is a constant plus a sum of products of rows at nodes of \(\mathcal N\). These nodes lie below \(D_j\). By Lemma 1.1 of the lesson on folding, the families with \(s(\bar M)\) and with \(M\) at \(D_j\) have the same left key, so the labeling gives the same label; its restored values at the nodes other than \(D_j\) are the same for both families, and at the row \(h\) of \(D_j\) they differ by the constant and the products of the \(y_C\) that correspond to the row \(\Delta_h\). By the definition of \(b_y\) this is \(b_y(\Delta_h)\), for every way to write \(\Delta_h\) with the generators. \(\blacksquare\)

**Definition.** Let \(\kappa=c/2\). A pair \((\Gamma,\bar M)\) is *useful* if it is a value of \((\Gamma,\pi M)\) with positive probability under \(\mathbb P_i\) and
\[
\mathbb P_i\bigl(\operatorname{Acc}_i\ \big|\ \Gamma,\ \pi M=\bar M\bigr)\ge\kappa .
\]
The *partial table* \(\widetilde f_\Gamma\) is \(f_\Gamma\) at the useful pairs and \(\bot\) elsewhere.

In this conditional probability the node \(D_i\), the marks, the vector \(a_i\) and the part of \(M\) in \(B\) are random. The partial tables are defined with the law \(\mathbb P_i\) once and for all; below, the same tables are examined under another law.

## 4. Equality along a step

Under \(\mathbb P_i\) let \(a=a_j\), let \(h_v\) be the buckets of \(M\), and let \(h'\) be one more call at \(D_j\), independent of the others. Replacing the bucket \(h_a\) by \(h'\) gives, by Lemma 3.1 of the lesson on folding,
\[
M'=M+a\otimes(h_a+h').
\]

**Lemma 4.1.** If \(\mathbb P_i(\operatorname{Acc}_i\cap\operatorname{Acc}_j)\ge c\), then
\[
\mathbb P_i\bigl(\widetilde f_\Gamma(\bar M)=\widetilde f_\Gamma(\bar M')\ne\bot\bigr)\ge\frac{c^2}8 .
\]

**Proof.** *Useful and accepted.* The event that \(\operatorname{Acc}_i\) holds and \((\Gamma,\bar M)\) is not useful has a probability of less than \(\kappa\): given \((\Gamma,\bar M)\) not useful, the conditional probability of \(\operatorname{Acc}_i\) is less than \(\kappa\). So the event \(G\) that \(\operatorname{Acc}_j\) holds and \((\Gamma,\bar M)\) is useful has \(\mathbb P_i(G)\ge c-\kappa=c/2\).

*At most two values.* Let \(\mathcal G\) consist of \(E\), the marks, \(O\), the path to \(D_i\), the arrays at all nodes other than \(D_j\), the vector \(a\), and the buckets \(h_v\) with \(v\ne a\). Given \(\mathcal G\), the functions \(h_a\) and \(h'\) are independent with the same law, by Section 2. The background \(\Gamma\) is a part of \(\mathcal G\). The function \(\Theta_{D_j,a}\circ\Psi_{E,\mathbf M}\) does not depend on \(h_a\), because \(h_a\) enters the value of \(M\) at a point only through a multiple of \(a\). So the right key of the constraint at \(D_j\), the label at it, and its restored value \(y'\) are functions of \(\mathcal G\). If \(\operatorname{Acc}_j\) holds, the restored value \(y\) of the left label satisfies \(\Theta_{D_j,a}(y)=y'\), by Lemma 5.1 of the lesson on the tree of function spaces. So on \(\operatorname{Acc}_j\) the components \(y_C\) with \(C\ne D_j\) are functions of \(\mathcal G\), and the component at \(D_j\) is one of two vectors that differ by \(a\). By Lemma 3.1, on \(\operatorname{Acc}_j\) the components \(y_C\), \(C\in\mathcal N\), of \(f_\Gamma(\bar M)\) are these functions of \(\mathcal G\), hence also \(b_y\), and
\[
\hat y=y_{D_j}+\Delta b_y,\qquad \Delta=M-s(\bar M).
\]
If the bucket \(h_a\) changes by a function \(h\), then \(\Delta\) changes by \(a\otimes(h-s(\pi h))\), and \(\Delta b_y\) by a multiple of \(a\). Therefore, given \(\mathcal G\), the table value \(f_\Gamma(\bar M)\) takes at most two values on \(\operatorname{Acc}_j\).

*Two draws.* Given \(\mathcal G\), let \(p_1,p_2\) be the conditional probabilities that \(G\) holds and \(f_\Gamma(\bar M)\) is the first or the second of these values. The same probabilities belong to \(M'\). The two draws are independent given \(\mathcal G\), so the conditional probability that \(\widetilde f_\Gamma(\bar M)\) and \(\widetilde f_\Gamma(\bar M')\) are equal and defined is at least
\[
p_1^2+p_2^2\ \ge\ \frac{(p_1+p_2)^2}2 .
\]
Here \(p_1+p_2=\mathbb P_i(G\mid\mathcal G)\), and the mean of its square is at least \(\mathbb P_i(G)^2\ge c^2/4\). \(\blacksquare\)

**The unrestricted law \(\mathbb P_j^0\).** Draw \(E\), the path to \(D_j\) and \(\Xi_j\) as in the test, draw the \(T'\) calls at \(D_j\) independently and uniformly in \(H\), and the arrays at the nodes below \(D_j\) independently and uniformly. The arrays at \(D_d,\dots,D_j\) are computed from the calls as in the test; in particular \(M\) from its buckets, and \(M'\) with the additional call \(h'\). The vectors \(a_p\), and further random data that are named below, are independent of all this. This is the law \(\mathsf U_j\) of the lesson on changing the law.

**Proposition 4.2.** Under \(\mathbb P_j^0\) the matrix \(M\) is uniform in \(K\otimes H\), the function \(h=h_a+h'\) is uniform in \(H\), and \(\Gamma\), \(M\), \(a\), \(h\) are independent. So, given \(\Gamma\), the pair \((\bar M,\bar M')\) is a uniform matrix of \(K\otimes(H/B)\) and its image under the step \(\bar M'=\bar M+a\otimes\pi h\) of the lesson on matrices and slices. If \(\mathbb P_i(\operatorname{Acc}_i\cap\operatorname{Acc}_j)\ge c\), then
\[
\mathbb P_j^0\bigl(\widetilde f_\Gamma(\bar M)=\widetilde f_\Gamma(\bar M')\ne\bot\bigr)\ge\frac{c^2}8-\delta_{ij} .
\]

**Proof.** Under \(\mathbb P_j^0\) the buckets of \(M\) and \(h'\) are independent uniform functions, and they are independent of \(\Gamma\): the arrays above \(D_j\) use other calls, and the other parts of \(\Gamma\) belong to \(\Xi_j\) or are the arrays below \(D_j\). Lemma 3.1 of the lesson on folding gives the first statement. The linear map \(\pi\) is onto, so \(\pi M\) and \(\pi h\) are uniform.

The event of the inequality is a function of \(\Gamma\), \(M\), \(M'\), with the fixed partial tables. Given \(E\) and the path to \(D_j\), these are functions of \(a\) and of the family \(\mathcal W\) of Proposition 4.3 of the lesson on changing the law: \(\Xi_j\), the \(T'\) calls at \(D_j\), and the arrays below \(D_j\). The law of \(\mathcal W\) under \(\mathbb P_i\) is the law \(\mathsf M_{i,j}\) of that proposition, so the probabilities of the event under \(\mathbb P_i\) and \(\mathbb P_j^0\) differ by at most \(\delta_{ij}\). Lemma 4.1 gives the bound. \(\blacksquare\)

The comparison is possible because the event does not use the node \(D_i\): the table was built with all nodes of \(\mathcal N\).

## 5. Good advice and the functionals

Assume the hypothesis (GE), let \(\mathbb P_i(\operatorname{Acc}_i\cap\operatorname{Acc}_j)\ge c\) and \(\delta_{ij}\le c^2/16\), and put
\[
\theta=\frac{c^2}{16},\qquad\eta=\frac\theta2 .
\]
Let \(\alpha,r,\ell_0\) be the numbers of Lemma 4.2 of the lesson on matrices and slices for this \(\eta\), and let \(\ell\ge\ell_0\). They depend only on \(\varepsilon\). The number \(\alpha\) is a lower bound for a fraction, and we take \(\alpha\le1\).

By Proposition 4.2 the probability of equality along the step is at least \(\theta=2\eta\) under \(\mathbb P_j^0\). Call \(\Gamma\) *rich* if the conditional probability of this equality, given \(\Gamma\), is at least \(\eta\). A random variable \(X\) with values in \([0,1]\) and \(\mathbb EX\ge2\eta\) satisfies \(\mathbb P(X\ge\eta)\ge\eta\), since \(\mathbb EX\le\eta+\mathbb P(X\ge\eta)\). So \(\Gamma\) is rich with a probability of at least \(\eta\).

Let \(A:K\to\mathbb F^r\) be a uniform linear map, independent of the rest. An *advice* is a triple \((\Gamma,A,N)\) with \(N\in\mathbb F^r\otimes(H/B)\). It is *good* if the row fibre \(\{\bar M:A\bar M=N\}\) is good for the partial table \(\widetilde f_\Gamma\) in the sense of that Lemma 4.2: it contains a slice, given by at most \(r\) column values, on which \(\widetilde f_\Gamma\) takes one value different from \(\bot\) for at least the fraction \(\alpha\) of the matrices.

**The witness.** For every good advice fix, by a rule that uses only the advice, such a slice and such a value: functionals \(q_1,\dots,q_m\in(H/B)^*\), vectors \(t_1,\dots,t_m\in K\) with \(m\le r\), and a value
\[
t_*=\bigl(\hat y^*,(y^*_C)_{C\in\mathcal N}\bigr),
\]
such that the slice consists of the matrices \(\bar M\) with \(A\bar M=N\) and \(\bar Mq_b=t_b\) for \(1\le b\le m\).

**Lemma 5.1.** Let \(h_0=2^{-r\ell}\) and \(g=\tfrac{\eta^2}4h_0\). Under \(\mathbb P_j^0\) the advice \((\Gamma,A,A\bar M)\) is good with a probability of at least \(g\).

**Proof.** Let \(\Gamma\) be rich. Given \(\Gamma\), the matrix \(\bar M\) is uniform, and the partial table \(\widetilde f_\Gamma\) on \(K\otimes(H/B)\) satisfies the assumption of Lemma 4.2 of the lesson on matrices and slices with \(\eta\). By its part (2), for the independent uniform \(A\) the row fibre of \(\bar M\) is good with a probability of at least \(\tfrac\eta4h_0\). Multiply by the probability \(\eta\) of a rich \(\Gamma\). \(\blacksquare\)

**The functionals.** Let the advice be good. Composed with \(\pi\), the \(q_b\) are functionals on \(H\) that vanish on \(B\); let \(Z\subset H^*\) be their span. The value \(t_*\) is a value of the response table, so the functional \(b_*=b_{y^*}\) on \(B\) exists. Define \(z_0\in H^*\) by
\[
z_0\bigl(b+s(x)\bigr)=b_*(b)
\]
for \(b\in B\) and \(x\in H/B\).

**Lemma 5.2.** Let the advice \((\Gamma,A,A\bar M)\) be good.

1. If \(f_\Gamma(\bar M)=t_*\), the label that the labeling gives at the left key of the family with the arrays of \(\Gamma\) and \(M\) has the restored value \(Mz_0+\hat y^*\) at \(D_j\).
2. Every \(z\in z_0+Z\) satisfies \(z(1)=1\), and for every \(C\in\mathcal N\) and all rows \(u,v\) of \(M_C\)
\[
z\bigl((M_C)_u(M_C)_v\bigr)=(y^*_C)_u\,(y^*_C)_v .
\]

**Proof.** (1) By Lemma 3.1 the restored value is \(\hat y^*+\Delta b_*\) with \(\Delta=M-s(\bar M)\). The rows of \(\Delta\) lie in \(B\), where \(z_0=b_*\), and \(z_0\) vanishes on the rows of \(s(\bar M)\). So \(Mz_0=\Delta b_*\). (2) The elements of \(Z\) vanish on \(B\), so \(z\) is \(b_*\) on \(B\). \(\blacksquare\)

Part (2) says that the matrix \(\bigl(z((M_C)_u(M_C)_v)\bigr)_{u,v}\) is \(y^*_C(y^*_C)^{\mathsf t}\), of rank at most one, at every node \(C\) of the level \(i\) below \(D_j\); in particular at \(D_i\).

**The events.** For the data \((\Gamma,A,M)\) define two events:

- \(J\): the advice \((\Gamma,A,A\bar M)\) is good, and \(Mq_b=t_b\) for all \(b\);
- \(I\): \(J\) holds, and \(\widetilde f_\Gamma(\bar M)=t_*\).

**Lemma 5.3.** The events \(I\) and \(J\) are functions of \((\Gamma,A,\bar M)\), and with \(g_0=g\,h_0\)
\[
\mathbb P_j^0(J)\ge g_0,\qquad\mathbb P_j^0(I)\ge\alpha\,\mathbb P_j^0(J).
\]

**Proof.** The \(q_b\) vanish on \(B\), so \(Mq_b=\bar Mq_b\), and the witness depends only on the advice. Under \(\mathbb P_j^0\), given \(\Gamma\), \(A\) and \(A\bar M\) with a good advice, \(\bar M\) is uniform in its row fibre. The slice of the witness is not empty, so by part (3) of Lemma 4.2 of the lesson on matrices and slices it has at least the fraction \(h_0\) of the fibre; this gives \(\mathbb P_j^0(J)\ge g\,h_0\). On the slice, \(\widetilde f_\Gamma=t_*\) for at least the fraction \(\alpha\). \(\blacksquare\)

## 6. The prediction of the upper response

Under \(\mathbb P_i\) let \(\mathsf R\in K\) be the component at \(D_j\) of the restored value of the label that the labeling gives at the right key of the constraint of \((E,\mathbf M,D_i,a_i)\). This is an answer of the right player at the lower level; the constraint at \(D_i\) removes one bit at \(D_i\) and shows the value at \(D_j\) in full.

**Proposition 6.1.** Assume (GE). Let the labeling satisfy the test with a probability of at least \(\varepsilon\), let \(d\varepsilon\ge4\), let \(i<j\) be the levels of Lemma 1.1, \(\ell_j\ge\ell_0\), and
\[
\delta_{ij}\le\frac{\alpha g_0}{16}.
\]
Then, with \(\rho=\kappa\alpha/4\) and \(b_0=\kappa\alpha g_0/4\),
\[
\mathbb P_i\bigl(J,\ \mathsf R=Mz_0+\hat y^*\bigr)-\rho\,\mathbb P_i(J)\ \ge\ b_0 .
\]

**Proof.** The assumption on \(\delta_{ij}\) contains \(\delta_i\le\varepsilon^2/4\) and \(\delta_{ij}\le c^2/16\), because \(\alpha g_0/16\le c^2/16\le\varepsilon^2/4\). So Lemma 2.1 and the statements of Sections 4 and 5 apply.

*From \(I\) to the prediction.* On \(I\) the pair \((\Gamma,\bar M)\) is useful. The map \(A\) is independent of the other data, so the conditional probability of \(\operatorname{Acc}_i\) given \((\Gamma,\bar M,A)\) is the one given \((\Gamma,\bar M)\), and since \(I\) is a function of \((\Gamma,A,\bar M)\),
\[
\mathbb P_i(I\cap\operatorname{Acc}_i)\ge\kappa\,\mathbb P_i(I).
\]
On \(I\cap\operatorname{Acc}_i\): by Lemma 5.2 the left label has the restored value \(Mz_0+\hat y^*\) at \(D_j\); and the satisfied constraint at \(D_i\) gives \(\Theta_{D_i,a_i}(y)=y'\) for the restored values, in which the components at \(D_j\ne D_i\) are equal. So \(\mathsf R=Mz_0+\hat y^*\) there, and
\[
\mathbb P_i\bigl(J,\ \mathsf R=Mz_0+\hat y^*\bigr)\ge\kappa\,\mathbb P_i(I).
\]

*Comparison.* The events \(I\) and \(J\) are functions of \(\Gamma\), \(M\) and \(A\), hence of \(A\) and of the family \(\mathcal W\). As in Proposition 4.2 their probabilities under \(\mathbb P_i\) and \(\mathbb P_j^0\) differ by at most \(\delta=\delta_{ij}\). Let \(x=\mathbb P_j^0(J)\ge g_0\). By Lemma 5.3,
\[
\mathbb P_i(I)\ge\alpha x-\delta,\qquad\mathbb P_i(J)\le x+\delta .
\]
So the left side of the claim is at least
\[
\begin{aligned}
&\kappa(\alpha x-\delta)-\rho(x+\delta)\\
&\quad=\tfrac34\kappa\alpha\,x-(\kappa+\rho)\,\delta\\
&\quad\ge\tfrac34\kappa\alpha g_0-\tfrac54\kappa\cdot\tfrac{\alpha g_0}{16}\\
&\quad=\tfrac{43}{64}\,\kappa\alpha g_0 ,
\end{aligned}
\]
which is more than \(b_0\). \(\blacksquare\)

The numbers \(c,\kappa,\theta,\eta,\alpha,r,\ell_0\) depend only on \(\varepsilon\), and \(h_0,g,g_0,\rho,b_0\) only on \(\varepsilon\) and \(\ell_j\). They do not depend on \(\ell_i\), on the numbers of children, on the numbers \(R_p\) or on the formula. The assumption on \(\delta_{ij}\) can be met by the choice of the numbers of children: \(L_i\) does not depend on \(n_i\), so \(\delta_i\) is small when \(n_i\) is large; and \(L_j\) depends on \(n_i\) and not on \(n_j\), so the first term of \(\delta_{ij}\) is small when \(n_j\) is chosen large after \(n_i\).

The proposition is an inequality between two probabilities under \(\mathbb P_i\), without a conditioning. It says that, on the event \(J\), the vector \(Mz_0+\hat y^*\) is the upper value of the right answer more often than the fraction \(\rho\) of the time, with a surplus \(b_0\). The matrix \(M\) is not determined by what the right player sees, and the functional \(z_0\) is computed from data on the left side. [OpenAI-G] turns this inequality into two procedures, one for each side, that output the same bilinear form with a fixed probability. That step is not part of this lesson.

## 7. Exercises

**7.1.** Check the two inequalities at the end of the proof of Lemma 1.1 for \(d=8\), \(\varepsilon=\tfrac12\).

**7.2.** Compute \(c,\kappa,\theta,\eta\) for \(\varepsilon=\tfrac12\).

**7.3.** Let \(\ell=1\), let \(\mathcal N\) have one node \(C\) with one row \(m\), and let \(H\) have the basis \(1,m,k\). Then \(B\) has the basis \(1,m\), since \(m\cdot m=m\) for a function with values in \(\mathbb F\). Take \(s(\pi k)=k\). Let \(M=1+m+k\), and let \(f_\Gamma(\pi k)=(\hat y,y_C)\). Compute the restored value at \(D_j\) of the label at the left key of the family with \(M\), for \(y_C=1\) and for \(y_C=0\).

**7.4.** In the proof of Lemma 4.1, suppose that the table could take \(w\) values on \(\operatorname{Acc}_j\) given \(\mathcal G\), with the probabilities \(p_1,\dots,p_w\). What bound does the argument give? Why does the bound of the lemma not depend on the number of the values of the table?

**7.5.** Show that the functionals \(z\in H^*\) with \(z=b_*\) on \(B\) are the elements of \(z_0+\operatorname{Ann}(B)\), where \(\operatorname{Ann}(B)\) is the space of the functionals that vanish on \(B\), and that all of them have the properties of Lemma 5.2 (2).

## 8. Solutions

**7.1.** \((d\varepsilon^2-\varepsilon)/(d-1)=(2-\tfrac12)/7=\tfrac3{14}\); \(\varepsilon^2-\varepsilon/d=\tfrac14-\tfrac1{16}=\tfrac3{16}\); \(\tfrac34\varepsilon^2=\tfrac3{16}\). Indeed \(\tfrac3{14}\ge\tfrac3{16}\ge\tfrac3{16}\); here \(d\varepsilon=4\), and the second inequality is an equality.

**7.2.** \(c=\tfrac18\), \(\kappa=\tfrac1{16}\), \(\theta=\tfrac1{1024}\), \(\eta=\tfrac1{2048}\).

**7.3.** \(\bar M=\pi k\), \(s(\bar M)=k\), \(\Delta=1+m\). The functional has \(b_y(1)=1\) and \(b_y(m)=b_y(m\cdot m)=y_C\,y_C=y_C\). So the restored value is \(\hat y+1+y_C\): it is \(\hat y\) for \(y_C=1\) and \(\hat y+1\) for \(y_C=0\).

**7.4.** The two draws agree and are defined with a probability of at least \(\sum p_k^2\ge(\sum p_k)^2/w\). The lemma has \(w=2\) because a constraint of the game has at most two preimages of every label: given the answer on the right side, an accepted answer on the left side is one of two. The total number of values of the table plays no role.

**7.5.** Two functionals that agree on \(B\) differ by an element of \(\operatorname{Ann}(B)\), and \(z_0=b_*\) on \(B\). The properties of Lemma 5.2 (2) are statements about the values on \(B\): \(1\in B\) and the products lie in \(B\).

## References

- [OpenAI-G] OpenAI, *Perfect completeness for 2-to-1 games*, OpenAI Math Release preprint, 23 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/Perfect-completeness-for-2-to-1-games-September-23-2026
