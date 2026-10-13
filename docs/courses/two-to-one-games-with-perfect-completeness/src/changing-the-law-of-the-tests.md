# Changing the law of the tests

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The arrays on the path of a test are not uniform: their rows contain products of samples from the next node of the path. The inverse theorem of the course needs uniform matrices. This lesson proves that the arrays at one node of the path, and everything below it, can be replaced by uniform ones with a small change of the law of everything an observer sees, as long as the observer is not told which child continues the path. The reason is that the special child is one of \(n\) children, and all the others contribute uniform functions. The same computation shows that the base questions below a few random children can be replaced by their projections, and it bounds the chance that a child chosen after looking at the functions is one of these. A last statement bounds the bias of the samples; it does not use the number of children but the number of products.

- Distances between laws (Section 1).
- The calls that reach a node of the path (Lemma 2.1).
- One hidden child (Proposition 3.1).
- Sparse projection (Proposition 4.1), the posterior bound (Proposition 4.2), and the comparison at two levels (Proposition 4.3).
- Bias (Proposition 5.1).

The lesson follows [OpenAI-G, Section 4]; according to [OpenAI-G], comparisons of this kind go back to S. Khot and M. Safra. It continues [Folding and the law of the tests](folding-and-the-law-of-the-tests.md) and uses the sampler defined there, with the parameters \(t,d,n_p,\ell_p,R_p\), and the spaces of [The tree of function spaces and the questions](the-tree-of-function-spaces-and-the-questions.md).

## 1. Distances between laws

For laws \(P,Q\) on a finite set let
\[
\operatorname{TV}(P,Q)=\frac12\sum_x|P(x)-Q(x)| .
\]
The probabilities of every event under \(P\) and \(Q\) differ by at most \(\operatorname{TV}(P,Q)\). If \(Q(x)=q(x)P(x)\) with a function \(q\), the *density* of \(Q\), then by the inequality of Cauchy and Schwarz
\[
\begin{aligned}
\operatorname{TV}(P,Q)&=\tfrac12\,\mathbb E_P|q-1|\\
&\le\tfrac12\sqrt{\mathbb E_P(q-1)^2} .
\end{aligned}
\]
If both laws are mapped by the same map, the distance does not grow; the same holds if the same independent random data are added to both.

If \(P\) is uniform on a set of \(L\) elements, every law \(Q\) on this set has a density \(q\le L\), and \(\mathbb E_P(q-1)^2=\mathbb E_Pq^2-1\le L-1\).

## 2. The calls that reach a node of the path

Fix the family \(E\) of base questions and the path \(D_d,\dots,D_0\). A *call* at \(D_k\) is one sample of \(\operatorname{Sample}(D_k)\), with its own random choices. The array \(M_{D_k}\), \(k\ge1\), consists of \(b_k=2^{\ell_k}-1\) calls at \(D_k\), its buckets. By the definition of the sampler, a call at \(D_k\), \(k\ge1\), is
\[
\sum_{C\ne D_{k-1}}U_C+\sum_{h=1}^{R_k}G_hH_h ,
\]
with uniform functions \(U_C\in H_C(E)^2\) at the other children of \(D_k\) and \(c_k=2R_k\) calls \(G_h,H_h\) at \(D_{k-1}\).

**Lemma 2.1.** Let \(1\le p\le d\). Every bucket of an array \(M_{D_k}\) with \(k>p\) is a fixed expression, formed with sums and products, in

- uniform functions at children of \(D_k,\dots,D_{p+1}\) that are not on the path, and
- \(\prod_{h=p+1}^kc_h\) calls at \(D_p\).

Together with the buckets of \(M_{D_p}\), the arrays at \(D_d,\dots,D_p\) use at most
\[
T_p=\sum_{k=p}^db_k\prod_{h=p+1}^kc_h
\]
calls at \(D_p\). Given \(E\) and the path, these calls are independent of each other, of the uniform functions in the expressions, and of the arrays at all nodes other than \(D_d,\dots,D_p\).

**Proof.** Replace every call at \(D_k\) by its definition, then the calls at \(D_{k-1}\) in it, and so on down to \(D_{p+1}\). Each step replaces a call at \(D_h\) by an expression with \(c_h\) calls at \(D_{h-1}\). The independence is the rule that every call draws its random choices anew. \(\blacksquare\)

The number \(T_p\) depends on the numbers \(\ell_k\) and \(R_k\) with \(k\ge p\), and not on the numbers \(n_k\) of children. The *exterior data* \(\Xi_p\) consist of the uniform functions in the expressions and of the arrays at the nodes that are neither on the path nor in the subtree of \(D_p\). All of them are functions of arguments outside the subtree of \(D_p\), and they are drawn without the part of the path below \(D_p\). The arrays at the path nodes above \(D_p\) do not belong to \(\Xi_p\): they are computed from \(\Xi_p\) and the calls at \(D_p\).

## 3. One hidden child

Fix \(E\), the path from the root to \(D_p\), and the exterior data \(\Xi_p\); the child \(J=D_{p-1}\) of \(D_p\) on the path is uniform among the \(n=n_p\) children and is not fixed. Fix an integer \(T\ge T_p\), and consider \(T\) independent calls at \(D_p\), which include all calls of Lemma 2.1.

**The blocks.** For a child \(C\) of \(D_p\) let \(V_C=H_C(E)^2\). Each call at \(D_p\) is a sum of one *contribution* in \(V_C\) from every child \(C\): the uniform function \(U_C\) if \(C\ne J\), and the sum of the \(R_p\) products if \(C=J\). The *block* \(X_C\) of the child \(C\) consists of its contributions to the \(T\) calls and of the arrays at all nodes of the subtree of \(C\) that are not leaves. It is an element of the finite set
\[
\mathcal X_C=V_C^{\,T}\times\prod_{D'}\bigl(K_{\operatorname{level}(D')}\otimes H_{D'}(E)\bigr),
\]
the product over these nodes \(D'\). Let \(L_p\) be the largest number of elements of a set \(\mathcal X_C\). It is bounded in terms of \(t\), \(T\), the numbers \(\ell_k\), and the numbers \(n_k\) with \(k<p\); it does not depend on \(n_p\), on the \(n_k\) with \(k>p\), or on the formula.

Two laws of the family of all blocks are compared.

- \(\mathsf A_p\), the *original* law: the law in the test.
- \(\mathsf U_p\), the *unrestricted* law: the blocks are independent, and each \(X_C\) is uniform in \(\mathcal X_C\).

Under \(\mathsf U_p\) the \(T\) calls are independent and uniform in \(H_{D_p}(E)\), and independent of the arrays below \(D_p\), which are uniform: the sum map from \(\prod_CV_C\) to \(H_{D_p}(E)\) is linear and onto, so it carries the uniform law to the uniform law. In particular, by Lemma 3.1 of the lesson on folding, \(M_{D_p}\) is then a uniform matrix.

**Proposition 3.1 (one hidden child).** Given \(E\), the path to \(D_p\) and \(\Xi_p\),
\[
\operatorname{TV}(\mathsf A_p,\mathsf U_p)\le\frac12\sqrt{\frac{L_p}{n_p}} .
\]
The same bound holds for the laws of every function of the blocks, of \(\Xi_p\) and of independent random data; for example for all the arrays at \(D_d,\dots,D_p\) and below \(D_p\) together.

**Proof.** Let \(P_C\) be the uniform law on \(\mathcal X_C\) and \(P\) their product. Given \(J=C\), the blocks are independent; a block \(X_{C'}\) with \(C'\ne C\) has the law \(P_{C'}\), because its contributions are the independent uniform functions \(U_{C'}\) and its arrays are off the path, hence uniform; and \(X_C\) has some law \(Q_C\), which we average over the path below \(C\). Let \(q_C\le L_p\) be the density of \(Q_C\). Since \(J\) is uniform, \(\mathsf A_p\) has the density
\[
Z=\frac1n\sum_Cq_C(X_C)
\]
with respect to \(P\). Under \(P\) the terms \(q_C(X_C)-1\) are independent with the mean \(0\), so by Section 1
\[
\begin{aligned}
\mathbb E_P(Z-1)^2&=\frac1{n^2}\sum_C\mathbb E_{P_C}(q_C-1)^2\\
&\le\frac{L_p}n .
\end{aligned}
\]
The second statement holds because the distance does not grow under maps. By Lemma 2.1 the arrays at the path nodes above \(D_p\) are functions of \(\Xi_p\) and of the calls, and the calls are the sums of the contributions. \(\blacksquare\)

The bound is at most \(L_p/(2\sqrt{n_p})\), the form in which [OpenAI-G] states it. An observer who knew \(J\) would see the law with the density \(q_J\), and the factor \(n^{-1/2}\) would be lost: the comparison holds only for observations that do not use the continuation of the path.

*Rows in place of buckets.* The row \(r\) of \(M_{D_p}\) is the sum of the buckets \(h_v\) with \(v_r=1\), so the contribution of a child \(C\) to this row is the sum of its contributions to these buckets. Under \(\mathsf U_p\) the contributions of \(C\) to the buckets are independent and uniform in \(V_C\); by Lemma 3.1 of the lesson on folding, applied to \(V_C\), its contributions to the \(\ell_p\) rows are then independent and uniform in \(V_C\) as well. So under \(\mathsf U_p\) the array at \(D_p\) can be described by its rows: each row is a sum of independent uniform contributions of the children.

## 4. Sparse projection

Let \(1\le i\le d\) and \(0<\beta<1\). Fix \(E\), the path to \(D_i\), and \(\Xi_i\). The *modified* law \(\mathsf M_i\) is defined as follows.

- Mark each child of \(D_i\) independently with the probability \(\beta\).
- At every leaf below a marked child draw a base edge at its left question, and replace the left question by the right question. This gives a mixed family \(O\).
- For every child \(C\) draw its block as follows: \(T\) independent uniform contributions in \(H_C(O)^2\), and for every node \(D'\) of its subtree that is not a leaf an independent uniform array in \(K_{\operatorname{level}(D')}\otimes H_{D'}(O)\). By Lemma 2.1 of the lesson on the tree of function spaces these are elements of \(\mathcal X_C\).

The exterior data \(\Xi_i\) are drawn as in the test, on the family \(E\); the part of the path below \(D_i\) is not used. So under \(\mathsf M_i\) the calls at \(D_i\) are independent and uniform in \(H_{D_i}(O)\), and the arrays at \(D_i\) and below are uniform in the spaces of \(O\); the arrays above \(D_i\) are computed from the calls and \(\Xi_i\) by the expressions of Lemma 2.1. An unmarked child has \(H_C(O)=H_C(E)\), and its block is uniform in \(\mathcal X_C\). As under \(\mathsf U_i\), the array at \(D_i\) can be described by its rows, each a sum of independent uniform contributions in the spaces \(H_C(O)^2\).

**Proposition 4.1 (sparse projection).** Given \(E\), the path to \(D_i\) and \(\Xi_i\), the law of the family of blocks under \(\mathsf M_i\), without the marks and the family \(O\), satisfies
\[
\operatorname{TV}(\mathsf M_i,\mathsf U_i)\le\frac12\sqrt{(1+\beta^2L_i)^{n_i}-1} .
\]

**Proof.** For a marked child let \(Q_C\) be the law of its block, averaged over the edges drawn at its leaves, with the density \(q_C\le L_i\). The blocks are independent, and the block of \(C\) has the law \((1-\beta)P_C+\beta Q_C\), with the density \(1+\beta(q_C-1)\). So \(\mathsf M_i\) has the density \(Z=\prod_C(1+\beta(q_C(X_C)-1))\) with respect to \(P\), and by independence
\[
\begin{aligned}
\mathbb E_PZ^2&=\prod_C\bigl(1+\beta^2\,\mathbb E_{P_C}(q_C-1)^2\bigr)\\
&\le(1+\beta^2L_i)^{n_i} .
\end{aligned}
\]
Then \(\mathbb E_P(Z-1)^2=\mathbb E_PZ^2-1\), and Section 1 applies. \(\blacksquare\)

With \(\beta=\beta_i=n_i^{-2/3}\) the bound tends to \(0\) as \(n_i\to\infty\), because \((1+n^{-4/3}L)^n\le\exp(Ln^{-1/3})\). The mean number of marked children is \(n_i^{1/3}\), which tends to infinity. Together with Proposition 3.1,
\[
\begin{aligned}
\operatorname{TV}(\mathsf A_i,\mathsf M_i)&\le\frac12\sqrt{\frac{L_i}{n_i}}\\
&\quad+\frac12\sqrt{(1+\beta_i^2L_i)^{n_i}-1} .
\end{aligned}
\]

The next statement is about an observer who sees the blocks under \(\mathsf M_i\) and then points at a child.

**Proposition 4.2 (posterior bound).** Under \(\mathsf M_i\), given \(E\), the path to \(D_i\) and \(\Xi_i\):

1. for every child \(C\), the conditional probability that \(C\) is marked, given all the blocks and any random data independent of the marks and blocks, is at most \(\beta L_i/(1-\beta)\);
2. if a set of at most \(m\) children is chosen as a function of the blocks and of such data, the probability that it contains a marked child is at most \(m\,\beta L_i/(1-\beta)\);
3. if \(F_0,F_1\) are bilinear forms on \(H_{D_i}(E)\) that are functions of the blocks, of \(\Xi_i\) and of such data, then the event that \(F_0\ne F_1\) while \(F_0\) and \(F_1\) agree on \(H_{D_i}(O)\times H_{D_i}(O)\) has a probability of at most \(2\beta L_i/(1-\beta)\).

**Proof.** (1) The children are independent. By the formula of Bayes, the conditional probability that \(C\) is marked, given its block \(X_C\), is
\[
\frac{\beta\,q_C(X_C)}{1-\beta+\beta\,q_C(X_C)}\le\frac{\beta L_i}{1-\beta},
\]
and the other blocks and independent data do not change it. (2) Given the blocks and the data, the chosen set is fixed, and by (1) the conditional mean of the number of its marked elements is at most \(m\beta L_i/(1-\beta)\). (3) Let \(F_0\ne F_1\). Since \(H_{D_i}(E)\) is the sum of the spaces \(V_C=H_C(E)^2\), there are children \(C_1,C_2\) and \(x\in V_{C_1}\), \(y\in V_{C_2}\) with \(F_0(x,y)\ne F_1(x,y)\). Choose the first such children in a fixed order; this is a function of the data. If neither is marked, then \(V_{C_1}\) and \(V_{C_2}\) lie in \(H_{D_i}(O)\), and the forms do not agree there. So the event is contained in the event that one of two chosen children is marked. \(\blacksquare\)

The bounds of this proposition are probabilities of events before any conditioning on a success. They can be subtracted from the probability of a success; they are not claims about the law inside a success event.

The last comparison joins a modification at a level \(i\) with uniform draws at a higher level \(j\). Let \(1\le i<j\le d\), and fix \(E\) and the path from the root to \(D_j\). Fix a number \(T'\ge T_j\) of calls at \(D_j\). Let \(\mathcal W\) be the family that consists of \(\Xi_j\), of these calls, and of the arrays at all nodes below \(D_j\) that are not leaves, each with its place in the tree. By Lemma 2.1, applied between the levels \(j\) and \(i\), for every path \(\varpi\) from \(D_j\) to a node \(D_i\) of the level \(i\) the family \(\mathcal W\) is a fixed function \(\Phi_\varpi\) of \(\Xi_i\) and of the blocks at \(D_i\), with
\[
T=T'\prod_{h=i+1}^jc_h+\sum_{k=i}^{j-1}b_k\prod_{h=i+1}^kc_h
\]
calls at \(D_i\): every call at \(D_j\) uses \(c_j\cdots c_{i+1}\) calls at \(D_i\), and the arrays at \(D_{j-1},\dots,D_i\) use the others. Three laws of \(\mathcal W\) are compared: the law \(\mathsf A\) in the test; the law \(\mathsf U_j\), in which the calls at \(D_j\) are independent and uniform in \(H_{D_j}(E)\), the arrays below \(D_j\) are independent and uniform, and \(\Xi_j\) is as in the test; and the law \(\mathsf M_{i,j}\), in which \(\varpi\) and \(\Xi_i\) are drawn as in the test, the blocks at \(D_i\) with the law \(\mathsf M_i\), and \(\mathcal W=\Phi_\varpi(\Xi_i,\text{blocks})\).

**Proposition 4.3 (two levels).** Given \(E\) and the path to \(D_j\),
\[
\begin{aligned}
\operatorname{TV}(\mathsf M_{i,j},\mathsf U_j)&\le\frac12\sqrt{\frac{L_j}{n_j}}+\frac12\sqrt{\frac{L_i}{n_i}}\\
&\quad+\frac12\sqrt{(1+\beta^2L_i)^{n_i}-1},
\end{aligned}
\]
where \(L_j\) belongs to \(T'\) calls at \(D_j\) and \(L_i\) to \(T\) calls at \(D_i\). The same bound holds for every function of \(\mathcal W\) and of independent random data.

**Proof.** For a fixed \(\varpi\), the laws of \(\Phi_\varpi(\Xi_i,\text{blocks})\) in the test and under \(\mathsf M_i\) differ by at most \(\operatorname{TV}(\mathsf A_i,\mathsf M_i)\), because \(\Xi_i\) has the same law in both and the map is the same. The distance of two mixtures with the same weights is at most the mean of the distances; so after averaging over \(\varpi\), the laws \(\mathsf A\) and \(\mathsf M_{i,j}\) of \(\mathcal W\) differ by at most the sum of the last two terms. The family \(\mathcal W\) is also a function of \(\Xi_j\) and of the blocks at \(D_j\), so by Proposition 3.1 at the level \(j\) the laws \(\mathsf A\) and \(\mathsf U_j\) of \(\mathcal W\) differ by at most the first term. \(\blacksquare\)

The family \(\mathcal W\) contains the arrays below \(D_j\) with their places in the tree, but it does not say which of them lie on the path. A function of \(\mathcal W\) can therefore use the array at every node of the level \(i\) below \(D_j\), and it cannot use the node \(D_i\) itself.

## 5. Bias

A law on a vector space \(V\) over \(\mathbb F\) is *quarter-balanced* if every nonzero linear functional takes each of its two values with a probability of at least \(\tfrac14\). The *bias* of a functional \(f\) under the law of \(x\) is \(|\mathbb E(-1)^{f(x)}|\).

**Proposition 5.1.** Let \(R_k\ge6\) for all \(k\). Fix \(E\) and the path. For \(p\ge1\) and every nonzero linear functional \(f\) on \(H_{D_p}(E)\), a call \(h\) at \(D_p\) satisfies
\[
\bigl|\mathbb E(-1)^{f(h)}\bigr|\le\Bigl(\frac78\Bigr)^{R_p},
\]
and the law of every call is quarter-balanced. The same holds under \(\mathsf M_i\), given the marks, the family \(O\) and the path to \(D_i\), for the calls at the path nodes \(D_p\) with \(p>i\) and the nonzero functionals on \(H_{D_p}(O)\). If \(X=\sum_vv\otimes h_v\) is formed with independent calls \(h_v\) at \(D_j\), for the nonzero \(v\) in a subspace \(W\subset K_j\), then every nonzero linear functional on \(W\otimes H_{D_j}\) has a bias of at most \((\tfrac78)^{R_j}\) under the law of \(X\); this holds also given any data that are independent of these calls, for example the other buckets of the array at \(D_j\) and the arrays at the other nodes.

**Proof.** *Products.* Let \(g,h\) be independent with quarter-balanced laws on \(V\), and \(B\) a nonzero bilinear form on \(V\). The \(g\) with \(B(g,\cdot)=0\) form a proper subspace, which lies in the kernel of a nonzero functional; so \(B(g,\cdot)\ne0\) with a probability of at least \(\tfrac14\). For such \(g\), the functional \(B(g,\cdot)\) takes each value at \(h\) with a probability of at least \(\tfrac14\). So \(B(g,h)\) takes each value with a probability of at least \(\tfrac1{16}\), and its bias is at most \(\tfrac78\).

*Induction on \(p\).* A uniform law is quarter-balanced, with the bias \(0\) for every nonzero functional; this covers the calls at a leaf. Let \(p\ge1\), let the calls at \(D_{p-1}\) be quarter-balanced, and \(f\ne0\) on \(H_{D_p}(E)\). If \(f\) is not zero on \(H_C(E)^2\) for a child \(C\ne D_{p-1}\), the uniform summand \(U_C\) makes \(f(h)\) a uniform bit. Otherwise \(f\) is not zero on \(H_{D_{p-1}}(E)^2\), because the square spaces of the children span \(H_{D_p}(E)\). Then \(B(g,g')=f(gg')\) is a nonzero bilinear form on \(H_{D_{p-1}}(E)\), since the products span the square space. Each of the \(R_p\) independent products has a bias of at most \(\tfrac78\) for \(f\), and the biases of independent summands multiply. Since \((\tfrac78)^6<\tfrac12\), the law of the call is quarter-balanced again.

Under \(\mathsf M_i\) the calls at \(D_i\) are uniform, and the same induction runs upward from \(D_i\) in the spaces of \(O\).

*The sum \(X\).* A nonzero functional \(\Phi\) on \(W\otimes H\) has \(\Phi(v\otimes\cdot)\ne0\) for some nonzero \(v\in W\), because the elements \(v\otimes h\) span. The \(h_v\) are independent, so the bias of \(\Phi\) is the product of the biases of the functionals \(\Phi(v\otimes\cdot)\) under the laws of the \(h_v\); one factor is at most \((\tfrac78)^{R_j}\) and the others at most \(1\). \(\blacksquare\)

The bound uses no dimension. A small bias at the level \(j\) is obtained by a large \(R_j\) alone; the lower levels need only \(R_k\ge6\).

## 6. Exercises

**6.1.** Let \(P\) be uniform on \(\{1,\dots,L\}\) and \(Q\) the unit mass at \(1\). Compute \(\operatorname{TV}(P,Q)\) and \(\mathbb E_P(q-1)^2\).

**6.2.** Compute \(T_p\) for \(d=2\), \(\ell_1=\ell_2=2\), \(R_1=R_2=6\), and \(p=1,2\).

**6.3.** In Proposition 3.1, why is the proof not valid for an observer who is given \(J\)? What is the density of the law of the blocks given \(J=C\)?

**6.4.** Show that the product of two independent uniform bits has the bias \(\tfrac12\), and that the sum of \(R\) independent such products has the bias \(2^{-R}\). Compare with Proposition 5.1.

## 7. Solutions

**6.1.** The density is \(q(1)=L\) and \(q(x)=0\) otherwise. The distance is \(\tfrac12\bigl((1-\tfrac1L)+(L-1)\tfrac1L\bigr)\), which is \(1-\tfrac1L\). The mean of \((q-1)^2\) under \(P\) is \(\tfrac1L(L-1)^2+\tfrac{L-1}L\), which is \(L-1\). So the bound \(L-1\) of Section 1 is attained.

**6.2.** \(b_1=b_2=3\) and \(c_2=12\). For \(p=2\): \(T_2=b_2=3\). For \(p=1\): \(T_1=b_1+b_2c_2=3+36=39\).

**6.3.** Given \(J=C\) the density with respect to \(P\) is \(q_C(X_C)\), which need not be near \(1\): the block of the special child contains products. Only the average over the \(n\) possible children gives a density \(Z\) whose variance is of the order \(1/n\).

**6.4.** The product is \(1\) with the probability \(\tfrac14\), so \(\mathbb E(-1)^{gg'}=\tfrac34-\tfrac14=\tfrac12\). For independent summands the expectations of the signs multiply. Proposition 5.1 gives the weaker bound \((\tfrac78)^R\), which holds for all functionals and all levels.

## References

- [OpenAI-G] OpenAI, *Perfect completeness for 2-to-1 games*, OpenAI Math Release preprint, 23 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/Perfect-completeness-for-2-to-1-games-September-23-2026
