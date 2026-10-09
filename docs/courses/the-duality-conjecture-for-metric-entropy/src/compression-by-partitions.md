# Compression by partitions

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The matrix of [Covering numbers and polar bodies](covering-numbers-and-polar-bodies.md) needs columns all of whose signed combinations of \(\ell^1\)-norm at most \(1\) can be approximated, in the maximum norm over the rows, by a short list of functions. This lesson constructs such columns from finitely many partitions of the row set [OpenAI-E, Section 3]. Each column is a function of a graph distance to a centre, decreasing logarithmically with the distance. The point is that the length of the approximation list depends on the number of classes of the partitions, not on the number of rows: in an approximant, every centre is replaced by a *label*, the class of a pivot point in one of the partitions. Replacing a point by its label moves it by at most one step in the graph, which enlarges distances from \(j\) to at most \(3j+2\), and the logarithmic profile makes the cost of this enlargement small.

The lesson is self-contained apart from elementary counting.

## 1. Partitions, graphs and profiles

Let \(X\) be a finite nonempty set, \(u,q\) positive integers and \([u]=\{1,\dots,u\}\). For each \(i\in[u]\) let \(L_i:X\to\Sigma_i\) be a map taking at most \(q\) values (the *labels*); its fibres form a partition of \(X\) into at most \(q\) classes. Fix \(0<\theta<1\) and a nonempty family \(\mathcal T\) of subsets of \([u]\) with
\[
|[u]\setminus T|\le\theta u\qquad(T\in\mathcal T).\tag{1.1}
\]
For \(T\in\mathcal T\), join distinct \(x,z\in X\) by an edge if \(L_i(x)=L_i(z)\) for some \(i\in T\), and let \(d_T(x,z)\in\{0,1,2,\dots\}\cup\{\infty\}\) be the graph distance (\(\infty\) between different components). It satisfies the triangle inequality.

Fix a positive integer \(h\) with
\[
\frac{\log3}{\log(h+1)}\le\theta,\qquad\text{and put}\quad s=\lceil1/\theta\rceil.\tag{1.2}
\]
The *logarithmic profile* is \(\phi_h(d)=\max\{0,1-\frac{\log(d+1)}{\log(h+1)}\}\) for \(d=0,1,2,\dots\) and \(\phi_h(\infty)=0\). Let \(Y=X\times\mathcal T\), and for \(y=(v,T)\in Y\) define the column
\[
g_y(x)=\phi_h\bigl(d_T(x,v)\bigr)\in[0,1]\qquad(x\in X).
\]

**Lemma 1.1** (the profile as a sum of balls). The numbers \(\gamma_j=\frac{\log(j+2)-\log(j+1)}{\log(h+1)}\), \(0\le j<h\), are positive and sum to \(1\), and for every \(d\in\{0,1,2,\dots\}\cup\{\infty\}\)
\[
\phi_h(d)=\sum_{j=0}^{h-1}\gamma_j\mathbf1_{\{d\le j\}},\qquad\sum_{j=0}^{h-1}\gamma_j\mathbf1_{\{d\le3j+2\}}\le\phi_h(d)+\frac{\log3}{\log(h+1)}.\tag{1.3}
\]

**Proof.** The sum of the \(\gamma_j\) telescopes to \(\frac{\log(h+1)}{\log(h+1)}=1\). For \(0\le d<h\), the first sum runs over \(j=d,\dots,h-1\) and telescopes to \(\frac{\log(h+1)-\log(d+1)}{\log(h+1)}=\phi_h(d)\); for \(d\ge h\) both sides vanish. In the second sum, the indices not counted by \(\phi_h(d)\) are those with \(j<d\le3j+2\). For finite \(d\) they form the integers from \(a=\lceil\frac{d+1}3\rceil-1\ge0\) to \(b=\min\{h-1,d-1\}\), with total weight \(\frac1{\log(h+1)}\log\frac{b+2}{a+1}\), and \(b+2\le d+1\le3(a+1)\). For \(d=\infty\) all indicators vanish. \(\square\)

## 2. Uniform compression

For nonnegative \(\mu\in\mathbb R^Y\) with \(\sum_y\mu_y\le1\) put \(f_\mu=\sum_y\mu_yg_y\), and let \(\mathcal F_+\) be the set of these functions. For \(S\subseteq Y\) write \(\mu(S)=\sum_{y\in S}\mu_y\).

**Proposition 2.1** (uniform compression). There is a list \(\mathcal A\) of \(Q\) real functions on \(X\) such that every \(f\in\mathcal F_+\) has some \(A\in\mathcal A\) with
\[
f(x)-3\theta\le A(x)\le f(x)+\theta\qquad(x\in X),\tag{2.1}
\]
and
\[
\log Q\le hs\log q+C_{h,\theta,u},\qquad C_{h,\theta,u}=\log u+hs2^u\log\Bigl(1+\frac{s2^u}\theta\Bigr).\tag{2.2}
\]

**Proof.** Fix once and for all, for each \(i\), a map \(\rho_i\) from the labels of \(L_i\) to \(X\) with \(L_i(\rho_i(\sigma))=\sigma\): a representative of each class.

*One partition for most of the mass.* Let \(f=f_\mu\). By (1.1),
\[
\frac1u\sum_{i=1}^u\mu\{(v,T):i\notin T\}=\sum_{(v,T)\in Y}\mu_{(v,T)}\frac{|[u]\setminus T|}u\le\theta,
\]
so some \(i_0\in[u]\) has \(\mu\{(v,T):i_0\notin T\}\le\theta\). Put \(Y_0=\{(v,T)\in Y:i_0\in T\}\).

*Few pivots at each level.* Fix \(j\in\{0,\dots,h-1\}\) and let \(I_x=\{(v,T)\in Y_0:d_T(x,v)\le j\}\) for \(x\in X\). Starting from \(U=\varnothing\), as long as some \(I_z\) has \(\mu(I_z\setminus U)>\theta\), choose such a \(z\) and replace \(U\) by \(U\cup I_z\). Each step adds mass more than \(\theta\), and the total mass is at most \(1\), so there are \(k_j<1/\theta\) steps, hence \(k_j\le s\). The result is a set of pivots \(z_{j,1},\dots,z_{j,k_j}\) and \(U_j=\bigcup_kI_{z_{j,k}}\) with
\[
\mu(I_x\setminus U_j)\le\theta\qquad(x\in X).\tag{2.3}
\]
Assign each \(y\in U_j\) to the first pivot \(z_{j,k}\) with \(y\in I_{z_{j,k}}\), and write \(k=\kappa_j(y)\).

*Replacing pivots by labels.* For a pivot \(z\), let \(z'=\rho_{i_0}(L_{i_0}(z))\). Then \(L_{i_0}(z')=L_{i_0}(z)\), so \(d_T(z,z')\le1\) for every \(T\) containing \(i_0\). If \(y=(v,T)\) is assigned to \(z\), then \(i_0\in T\) and \(d_T(v,z)\le j\), so \(d_T(v,z')\le j+1\), and for every \(x\in X\):
\[
d_T(x,v)\le j\ \Longrightarrow\ d_T(x,z')\le2j+1,\qquad d_T(x,z')\le2j+1\ \Longrightarrow\ d_T(x,v)\le3j+2.\tag{2.4}
\]
Writing \(z'_{j,k}\) for the replacement of \(z_{j,k}\), define
\[
A_j(x)=\sum_{y=(v,T)\in U_j}\mu_y\mathbf1_{\{d_T(x,z'_{j,\kappa_j(y)})\le2j+1\}},\qquad f_{\mu,j}(x)=\sum_{y=(v,T)\in Y}\mu_y\mathbf1_{\{d_T(x,v)\le j\}}.
\]
A column counted in \(f_{\mu,j}(x)\) is either in \(U_j\), and then counted in \(A_j(x)\) by (2.4), or outside \(Y_0\) (mass at most \(\theta\)), or in \(I_x\setminus U_j\) (mass at most \(\theta\) by (2.3)). A column counted in \(A_j(x)\) has \(d_T(x,v)\le3j+2\) by (2.4). Hence
\[
f_{\mu,j}(x)-2\theta\le A_j(x)\le\sum_{y=(v,T)}\mu_y\mathbf1_{\{d_T(x,v)\le3j+2\}}.\tag{2.5}
\]

*Combining the levels.* Let \(F=\sum_j\gamma_jA_j\). By (1.3), \(f_\mu=\sum_j\gamma_jf_{\mu,j}\), so (2.5) gives \(F\ge f_\mu-2\theta\); and summing the second part of (1.3) over the columns with weights \(\mu_y\), with \(\frac{\log3}{\log(h+1)}\le\theta\) and \(\sum_y\mu_y\le1\), gives \(F\le f_\mu+\theta\).

*Encoding.* The centre \(v\) of a column does not appear in \(A_j\). Grouping the columns by their slot \(k\) and their set \(T\),
\[
A_j(x)=\sum_{k=1}^s\sum_{T\in\mathcal T}w_{j,k,T}\mathbf1_{\{d_T(x,z'_{j,k})\le2j+1\}},\qquad w_{j,k,T}=\sum_{v:\ (v,T)\in U_j,\ \kappa_j(v,T)=k}\mu_{(v,T)}\in[0,1],
\]
where unused slots get weight \(0\) and an arbitrary fixed label. There are at most \(M_0=s2^u\) weights per level. Round each weight down to a multiple of \(\delta=\theta/M_0\), call the resulting functions \(\widetilde A_j\), and put \(A=\sum_j\gamma_j\widetilde A_j\). Since the indicators are at most \(1\), \(0\le A_j-\widetilde A_j\le M_0\delta=\theta\), so \(0\le F-A\le\theta\), and (2.1) follows.

*Counting.* \(A\) is determined by \(i_0\), the \(hs\) labels \(L_{i_0}(z_{j,k})\) (the points \(z'_{j,k}\) are recovered through \(\rho_{i_0}\)), and the at most \(hM_0\) rounded weights, each taking at most \(1+M_0/\theta\) values. Listing all such data, whether or not they arise from some \(\mu\), gives a list of length at most \(u\,q^{hs}(1+\frac{s2^u}\theta)^{hs2^u}\), which is (2.2). \(\square\)

The partitions, the graphs, the family \(\mathcal T\) and the representatives \(\rho_i\) are fixed before the list is formed; only \(i_0\), the labels and the weights depend on \(\mu\). Nothing is assumed about the separation of the rows.

**Corollary 2.2** (signed compression). There is a list of at most \(Q^2\) functions on \(X\) such that every \(f_\lambda=\sum_y\lambda_yg_y\) with \(\sum_y|\lambda_y|\le1\) lies within \(6\theta\) of one of them in the maximum norm.

**Proof.** Write \(\lambda=\lambda^+-\lambda^-\) with \(\lambda^\pm_y=\max\{\pm\lambda_y,0\}\). Both parts are nonnegative with mass at most \(1\), so Proposition 2.1 gives \(A^\pm\in\mathcal A\) with \(\max_X|f_{\lambda^\pm}-A^\pm|\le3\theta\). Then \(A^+-A^-\) is within \(6\theta\) of \(f_\lambda\), and there are at most \(Q^2\) differences. \(\square\)

## 3. Exercises

**Exercise 3.1** (easy). Show that \(\phi_h\) is nonincreasing, \(\phi_h(0)=1\) and \(\phi_h(d)=0\) for \(d\ge h\).

**Exercise 3.2** (medium). Replace the logarithmic profile by the linear profile \(\psi_h(d)=\max\{0,1-d/h\}\). Show that the analogue of the second inequality in (1.3) then holds only with an error close to \(\frac23\) for some \(d\), and explain why the argument needs the logarithm.

**Exercise 3.3** (easy). Check that the number of steps in the greedy choice of pivots satisfies \(k_j\le s\), even when \(1/\theta\) is an integer.

## 4. Solutions

**3.1.** \(\log(d+1)\) is increasing, \(\log1=0\), and \(\log(d+1)\ge\log(h+1)\) for \(d\ge h\).

**3.2.** For \(\psi_h=\sum_{j<h}\frac1h\mathbf1_{\{d\le j\}}\) the extra indices \(j<d\le3j+2\) have weight about \(\frac1h\cdot\frac{2d}3\) for \(d\le h\), which is close to \(\frac23\) when \(d\) is close to \(h\). The dilation \(j\mapsto3j+2\) multiplies scales by about \(3\), and only a weight that is uniform in \(\log j\) charges each dyadic-type range \([j,3j+2]\) by the same small amount \(\frac{\log3}{\log(h+1)}\).

**3.3.** After \(k\) steps the union has mass greater than \(k\theta\) and at most \(1\), so \(k<1/\theta\le s\).

## References

- [OpenAI-E] OpenAI, *Counterexamples to the duality conjecture for metric entropy*, OpenAI Math Release preprint, 24 September 2026, Section 3. https://github.com/openai/math/blob/main/preprints/Counterexamples-to-the-duality-conjecture-for-metric-entropy-September-24-2026
