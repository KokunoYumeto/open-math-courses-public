# A variance inequality for three rows

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

When the square of the operator \(H=\sum_ah_a\) of [The switch chain](the-switch-chain.md) is expanded, every product \(h_ah_b\) of two different pairs \(a,b\) that share a vertex involves only the three vertices of \(a\cup b\). This lesson proves that on every vertex triple \(T\) the operator
\[
H_T=\sum_{a\subseteq T,\ |a|=2}h_a
\]
satisfies \(H_T^2\succeq H_T\) (Theorem 4.1). The main tool is an inequality for random binary matrices with three rows and prescribed row and column sums (Theorem 3.1): the variance of a sum of three functions, the \(i\)-th depending only on row \(i\), is at most twice the sum of their variances. Fu, Qin and Wang proved an equivalent inequality in their analysis of the swap chain on binary matrices [FQW, Theorem 5.1]. The proof below is OpenAI's [OpenAI-SW, Section 3]. It treats separately the assignment of columns to rows when the sizes of the blocks are fixed (Section 1) and the random block sizes themselves (Section 2); for the latter it uses the coupling of Fu, Qin and Wang [FQW, Lemmas 5.2–5.4]. OpenAI credits its use of transpositions to the method of Carlen, Lieb and Loss for the symmetric group [CLL].

All functions are real. For a random variable \(X\) on a finite probability space, \(\|X\|^2=\mathbb EX^2\), and \(\langle X,Y\rangle=\mathbb E[XY]\).

## 1. Fixed block sizes

Let \(U\) and \(W\) be finite sets, and fix nonnegative integers \(\mu_1,\mu_2,\mu_3\) with sum \(|U|\) and \(\nu_1,\nu_2,\nu_3\) with sum \(|W|\). Let \(\Omega_0\) be the set of pairs consisting of an ordered partition \((U_1,U_2,U_3)\) of \(U\) with \(|U_i|=\mu_i\) and an ordered partition \((W_1,W_2,W_3)\) of \(W\) with \(|W_i|=\nu_i\), with the uniform measure. Thus the two partitions are independent and uniform.

**Lemma 1.1** (fixed blocks). For \(i=1,2,3\) let \(g_i\) be a real function on \(\Omega_0\) that depends only on \((U_i,W_i)\). Then
\[
\operatorname{Var}(g_1+g_2+g_3)\le2\bigl(\operatorname{Var}g_1+\operatorname{Var}g_2+\operatorname{Var}g_3\bigr).\tag{1.1}
\]

**Proof.** Replacing \(g_i\) by \(g_i-\mathbb Eg_i\), we may assume that each \(g_i\) has mean zero. A permutation \(\tau\) of \(U\), or of \(W\), acts on \(\Omega_0\) by applying it to every block, and on functions by \((T_\tau f)(\omega)=f(\tau\omega)\). Let
\[
J=\sum_\tau(I-T_\tau),
\]
summed over the transpositions \(\tau\) of two elements of \(U\) and of two elements of \(W\). Each \(T_\tau\) comes from a measure-preserving involution of \(\Omega_0\), so it is self-adjoint and orthogonal, and \(\mathbb E(f-T_\tau f)^2=2\langle f,(I-T_\tau)f\rangle\). Hence
\[
\langle f,Jf\rangle=\tfrac12\sum_\tau\mathbb E(f-T_\tau f)^2,\tag{1.2}
\]
and \(J\succeq0\). A function in the kernel of \(J\) is invariant under all transpositions, hence under all permutations of \(U\) and of \(W\). These permutations act transitively on \(\Omega_0\), so the kernel of \(J\) consists of the constants.

Let \(\mathcal F_i\) be the space of functions of \((U_i,W_i)\). If \(f\in\mathcal F_i\), then \(T_\tau f\) depends only on \((\tau U_i,W_i)\) when \(\tau\) permutes \(U\), and only on \((U_i,\tau W_i)\) when \(\tau\) permutes \(W\); in both cases \(T_\tau f\in\mathcal F_i\). So \(J\) maps \(\mathcal F_i\) into itself, and so does every spectral projection of \(J\), being a polynomial in \(J\). Write \(g_i=\sum_\lambda g_{i,\lambda}\), where \(g_{i,\lambda}\in\mathcal F_i\) is the component of \(g_i\) in the eigenspace of \(J\) for the eigenvalue \(\lambda\). The component for \(\lambda=0\) is the mean of \(g_i\), which is zero.

Fix a transposition \(\tau\). If it exchanges two labels in the same block, it changes no block; otherwise it changes exactly two of the blocks of its set. So at every \(\omega\) at most two of the three numbers \(g_{i,\lambda}(\omega)-g_{i,\lambda}(\tau\omega)\) are nonzero, and pointwise
\[
\Bigl(\sum_i\bigl(g_{i,\lambda}-T_\tau g_{i,\lambda}\bigr)\Bigr)^2\le2\sum_i\bigl(g_{i,\lambda}-T_\tau g_{i,\lambda}\bigr)^2 .
\]
Take expectations and sum over \(\tau\). By (1.2), applied to the eigenfunctions \(\sum_ig_{i,\lambda}\) and \(g_{i,\lambda}\), this says
\[
\lambda\Bigl\|\sum_ig_{i,\lambda}\Bigr\|^2\le2\lambda\sum_i\|g_{i,\lambda}\|^2 .
\]
For \(\lambda>0\) divide by \(\lambda\). Eigenspaces for different eigenvalues are orthogonal, so summing over \(\lambda>0\) gives \(\|\sum_ig_i\|^2\le2\sum_i\|g_i\|^2\), which is (1.1). \(\square\)

The constant \(2\) cannot be lowered (Exercise 5.1).

## 2. Random block sizes

For an integer \(\alpha\ge0\) put
\[
w_\alpha(t)=\frac1{t!\,(t+\alpha)!}\qquad(t=0,1,2,\dots).
\]

**Lemma 2.1** (adjacent totals). Let \(\alpha,\beta\ge0\) be integers, and for \(s\ge0\) let \(Y_s\) be a random variable on \(\{0,\dots,s\}\) with \(\mathbb P(Y_s=y)\) proportional to \(w_\alpha(y)\,w_\beta(s-y)\). For \(s\ge1\), the variables \(Y_{s-1}\) and \(Y_s\) can be coupled so that
\[
Y_{s-1}\le Y_s\le Y_{s-1}+1 .
\]

**Proof.** All the weights are positive. Write \(\pi_s(y)=\mathbb P(Y_s=y)\). For \(0\le y\le s-1\),
\[
\frac{\pi_s(y)}{\pi_{s-1}(y)}=c\,\frac{w_\beta(s-y)}{w_\beta(s-1-y)}=\frac{c}{(s-y)(s-y+\beta)}
\]
with a constant \(c>0\), and this is nondecreasing in \(y\). So the law of \(Y_s\) conditioned on \(\{Y_s\le s-1\}\) is the law of \(Y=Y_{s-1}\) reweighted by a positive nondecreasing function \(\psi\). For a nondecreasing function \(\varphi\) and an independent copy \(Y'\) of \(Y\),
\[
\mathbb E[\psi(Y)\varphi(Y)]-\mathbb E[\psi(Y)]\,\mathbb E[\varphi(Y)]=\tfrac12\mathbb E\bigl[(\psi(Y)-\psi(Y'))(\varphi(Y)-\varphi(Y'))\bigr]\ge0,
\]
so the reweighting does not decrease the expectation of \(\varphi\). With \(\varphi=\mathbf 1_{[y,\infty)}\) this gives \(\mathbb P(Y_s\ge y\mid Y_s\le s-1)\ge\mathbb P(Y_{s-1}\ge y)\). For \(y\le s\),
\[
\mathbb P(Y_s\ge y)=(1-\pi_s(s))\,\mathbb P(Y_s\ge y\mid Y_s\le s-1)+\pi_s(s)\ge\mathbb P(Y_{s-1}\ge y),
\]
and for \(y>s\) both sides vanish. So \(Y_s\) stochastically dominates \(Y_{s-1}\).

The variable \(s-Y_s\) has the same kind of law with \(\alpha\) and \(\beta\) exchanged. Hence \(s-Y_s\) dominates \(s-1-Y_{s-1}\), that is, \(Y_{s-1}+1\) dominates \(Y_s\). Let \(Q_s(u)=\min\{y:\mathbb P(Y_s\le y)\ge u\}\) for \(0<u<1\). If \(X'\) dominates \(X\), the quantile function of \(X'\) is at least that of \(X\), and the quantile function of \(Y_{s-1}+1\) is \(Q_{s-1}+1\). Taking one uniform random variable \(u\) and setting \(Y_{s-1}=Q_{s-1}(u)\) and \(Y_s=Q_s(u)\) gives the coupling. \(\square\)

**Proposition 2.2** (random block sizes). Let \(m,\alpha_1,\alpha_2,\alpha_3\ge0\) be integers, and let \(x=(x_1,x_2,x_3)\) be a random triple of nonnegative integers with \(x_1+x_2+x_3=m\) and
\[
\mathbb P(x)\ \text{proportional to}\ w_{\alpha_1}(x_1)\,w_{\alpha_2}(x_2)\,w_{\alpha_3}(x_3).
\]
For real functions \(b_1,b_2,b_3\) on \(\{0,\dots,m\}\),
\[
\operatorname{Var}\Bigl(\sum_{i=1}^3b_i(x_i)\Bigr)\le2\sum_{i=1}^3\operatorname{Var}\bigl(b_i(x_i)\bigr).\tag{2.1}
\]

**Proof.** If \(m=0\), then \(x\) is constant. Let \(m\ge1\); then each \(x_i\) takes every value in \(\{0,\dots,m\}\) with positive probability. Let \(\mathcal H\) be the space of triples \(b=(b_1,b_2,b_3)\) of functions on \(\{0,\dots,m\}\) with \(\mathbb Eb_i(x_i)=0\), normed by \(\|b\|^2=\sum_i\mathbb Eb_i(x_i)^2\), and let \(Ab=\sum_ib_i(x_i)\). It suffices to show that every eigenvalue \(\lambda\) of the self-adjoint operator \(A^*A\) on \(\mathcal H\) is at most \(2\), because \(\|Ab\|^2\le\lambda_{\max}\|b\|^2\). Since \(\mathbb E[b_i(x_i)F]=\mathbb E\bigl[b_i(x_i)\,\mathbb E[F\mid x_i]\bigr]\), an eigenvector \(b\neq0\) satisfies
\[
\lambda\,b_i(t)=\mathbb E\Bigl[\sum_{j=1}^3b_j(x_j)\Bigm|x_i=t\Bigr]\qquad(i=1,2,3,\ 0\le t\le m).\tag{2.2}
\]
Let \(M\) be the largest of the numbers \(|b_i(t+1)-b_i(t)|\) with \(1\le i\le3\) and \(0\le t<m\). If \(M=0\), each \(b_i\) is constant, hence zero; so \(M>0\).

Fix \(i\) and let \(j,k\) be the other two indices. Given \(x_i=t\), the pair \((x_j,x_k)\) has the law of \((Y_s,s-Y_s)\) from Lemma 2.1 with \(s=m-t\), \(\alpha=\alpha_j\) and \(\beta=\alpha_k\). For \(0\le t<m\), couple the conditional laws given \(x_i=t\) and given \(x_i=t+1\) as in Lemma 2.1: from the first to the second, exactly one of \(x_j,x_k\) decreases by one and the other is unchanged. Therefore the conditional expectations of \(b_j(x_j)+b_k(x_k)\) given \(x_i=t+1\) and given \(x_i=t\) differ by at most \(M\). Subtracting (2.2) at \(t\) from (2.2) at \(t+1\) gives
\[
\bigl|(\lambda-1)\bigl(b_i(t+1)-b_i(t)\bigr)\bigr|\le M .
\]
Choosing \(i\) and \(t\) with \(|b_i(t+1)-b_i(t)|=M\) gives \(|\lambda-1|\le1\), so \(\lambda\le2\). \(\square\)

## 3. Binary matrices with three rows

**Theorem 3.1** (three-row variance inequality; Fu, Qin and Wang, OpenAI). Fix a finite set \(C\) of columns, row sums \(\rho_1,\rho_2,\rho_3\) and column sums \((\kappa_c)_{c\in C}\), and let \(S\) be a uniformly random binary matrix with rows \(1,2,3\), columns \(C\) and these margins, the set of such matrices being nonempty. Let \(S_i\) be the \(i\)-th row of \(S\). For real functions \(f_1,f_2,f_3\),
\[
\operatorname{Var}\Bigl(\sum_{i=1}^3f_i(S_i)\Bigr)\le2\sum_{i=1}^3\operatorname{Var}\bigl(f_i(S_i)\bigr).
\]

**Proof.** A column with sum \(0\) or \(3\) is the same in every such matrix; let \(c_3\) be the number of columns with sum \(3\). Let \(U\) be the set of columns with sum \(1\) and \(W\) the set of columns with sum \(2\). Assign each column of \(U\) to the row of its one and each column of \(W\) to the row of its zero, and let \(U_i\) and \(W_i\) be the columns assigned to row \(i\). Row \(i\) is determined by \((U_i,W_i)\): its ones are the columns in \(U_i\), in \(W\setminus W_i\) and of sum \(3\). Conversely, ordered partitions \((U_1,U_2,U_3)\) of \(U\) and \((W_1,W_2,W_3)\) of \(W\) define a matrix with the given column sums, and its row sums \(|U_i|+|W|-|W_i|+c_3\) are right exactly when
\[
|U_i|=|W_i|+\delta_i,\qquad \delta_i=\rho_i-|W|-c_3 .\tag{3.1}
\]
So \(S\) corresponds to a uniformly random pair of ordered partitions satisfying (3.1).

Let \(k_i=|W_i|\) and \(k=(k_1,k_2,k_3)\). Given \(k\), the pair of partitions is uniform among those with block sizes \((k_i+\delta_i)_i\) and \((k_i)_i\), so the two partitions are independent and uniform, and Lemma 1.1, applied to \(g_i=f_i(S_i)\), gives
\[
\operatorname{Var}\Bigl(\sum_if_i(S_i)\Bigm|k\Bigr)\le2\sum_i\operatorname{Var}\bigl(f_i(S_i)\bigm|k\bigr).\tag{3.2}
\]
Counting the pairs of partitions, \(\mathbb P(k)\) is proportional to \(\prod_i\bigl[k_i!\,(k_i+\delta_i)!\bigr]^{-1}\) on the set of \(k\) with \(k_i\ge0\), \(k_i+\delta_i\ge0\) and \(\sum_ik_i=|W|\). (Then \(\sum_i(k_i+\delta_i)=|U|\) holds automatically, because \(\sum_i\rho_i=|U|+2|W|+3c_3\).) Put \(l_i=\max(0,-\delta_i)\), \(x_i=k_i-l_i\), \(\alpha_i=|\delta_i|\) and \(m=|W|-\sum_il_i\). The constraints become \(x_i\ge0\) and \(\sum_ix_i=m\), and \(k_i!\,(k_i+\delta_i)!=x_i!\,(x_i+\alpha_i)!\) in both cases \(\delta_i\ge0\) and \(\delta_i<0\). So \(x\) has the law of Proposition 2.2. Given \(k\), the sets \(U_i\) and \(W_i\) are uniform subsets of \(U\) and \(W\) of sizes \(k_i+\delta_i\) and \(k_i\), so \(\mathbb E[f_i(S_i)\mid k]\) is a function \(b_i(x_i)\) of \(x_i\) alone. By Proposition 2.2,
\[
\operatorname{Var}\Bigl(\sum_i\mathbb E[f_i(S_i)\mid k]\Bigr)\le2\sum_i\operatorname{Var}\bigl(\mathbb E[f_i(S_i)\mid k]\bigr).\tag{3.3}
\]
Since \(\operatorname{Var}X=\mathbb E\operatorname{Var}(X\mid k)+\operatorname{Var}\mathbb E[X\mid k]\) for every random variable \(X\), adding the average of (3.2) over \(k\) to (3.3) gives the theorem. \(\square\)

## 4. Vertex triples

We return to the graphs of [The switch chain](the-switch-chain.md): \(V=\{1,\dots,n\}\) with \(n\ge4\), a graphical vector \(d\), the set \(\Omega_d\) with its uniform measure, the pair fibers, and the operators \(E_a\) and \(h_a=I-E_a\).

**Theorem 4.1** (OpenAI). For every vertex triple \(T\), \(H_T^2\succeq H_T\).

**Proof.** *Cells.* Call two graphs of \(\Omega_d\) equivalent if they have the same edges inside \(V\setminus T\) and every \(w\notin T\) has the same number of neighbours in \(T\) in both; the equivalence classes are the *cells*. Two graphs in the same \(a\)-fiber, for a pair \(a\subseteq T\), lie in the same cell: they share all edges with no endpoint in \(a\), among them the edges inside \(V\setminus T\) and the edges from the third vertex of \(T\) to \(V\setminus T\), and every \(w\notin T\) has the same number of neighbours in \(a\). So \(E_a\), \(h_a\) and \(H_T\) map functions supported on a cell to functions supported on it, and it suffices to prove the inequality on every cell, with its uniform measure. On a cell, the number \(e\) of edges inside \(T\) is fixed, because \(\sum_{t\in T}d_t=2e+\sum_{w\notin T}|N(w)\cap T|\).

*Encoding.* For a graph in the cell, let \(s_t\) be the number of neighbours of \(t\in T\) inside \(T\). Form the binary matrix with rows \(t\in T\) and columns \(w\notin T\) whose entry is \(1\) when \(tw\) is an edge, and add one more column, depending on \(e\):

| \(e\) | edges inside \(T\) | extra column | row sum of row \(t\) |
| --- | --- | --- | --- |
| 0 | none | none | \(d_t\) |
| 1 | one edge | entry \(s_t\) in row \(t\) (column sum 2) | \(d_t\) |
| 2 | a path | entry \(s_t-1\) in row \(t\) (column sum 1) | \(d_t-1\) |
| 3 | a triangle | none | \(d_t-2\) |

For \(e=1\) the extra column marks the two ends of the edge, and for \(e=2\) it marks the middle vertex of the path. The row sums in the table follow from \(d_t=s_t+(\text{number of neighbours of }t\text{ outside }T)\), and the column sum of a column \(w\notin T\) is the fixed number \(|N(w)\cap T|\). Conversely, every binary matrix with these margins comes from exactly one graph of the cell: the extra column gives the edges inside \(T\), the other columns give the edges between \(T\) and \(V\setminus T\), the edges inside \(V\setminus T\) are those of the cell, and the row and column sums give every vertex its prescribed degree. Hence the cell with its uniform measure is the space of a uniformly random binary matrix with prescribed margins, as in Theorem 3.1. Let \(S_t\) denote row \(t\), including its extra entry.

*The three resamplings.* Let \(t\in T\) and \(a=T\setminus\{t\}\). We show that on the cell \(E_a\) is the conditional expectation given \(S_t\). Inside the cell, the \(a\)-fiber of a graph is determined by the neighbours of \(t\) outside \(T\): these give \(s_t=d_t-|N(t)\setminus T|\); the edge inside \(a\) is present exactly when \(e-s_t=1\); a vertex \(w\notin T\) has \(|N(w)\cap T|-[tw\text{ is an edge}]\) neighbours in \(a\); the vertex \(t\) has \(s_t\) of them; and the edges with no endpoint in \(a\) are those inside \(V\setminus T\) together with the edges from \(t\) to \(V\setminus T\). Conversely, the \(a\)-fiber determines the edges from \(t\) to \(V\setminus T\), and with them \(s_t\) and the extra entry of \(S_t\). So the \(a\)-fibers inside the cell are exactly the sets on which \(S_t\) is constant, and \(E_a=\mathbb E[\,\cdot\mid S_t]\) there.

*The inequality.* Let \(f\) be a function on the cell with mean zero, and put \(P_tf=\mathbb E[f\mid S_t]\) and \(\beta=\sum_t\|P_tf\|^2\). The functions \(P_tf\) have mean zero and depend on single rows, so Theorem 3.1 gives \(\|\sum_tP_tf\|^2\le2\beta\). Since each \(P_t\) is an orthogonal projection,
\[
\beta=\Bigl\langle f,\sum_tP_tf\Bigr\rangle\le\|f\|\,\Bigl\|\sum_tP_tf\Bigr\|\le\|f\|\sqrt{2\beta},
\]
so \(\beta\le2\|f\|^2\) and
\[
\langle f,H_Tf\rangle=\sum_t\langle f,(I-P_t)f\rangle=3\|f\|^2-\beta\ge\|f\|^2 .
\]
So on the cell \(H_T\) kills the constants and is at least the identity on the functions with mean zero. Both subspaces are invariant under the self-adjoint operator \(H_T\), and on each of them \(H_T^2-H_T=H_T(H_T-I)\succeq0\). \(\square\)

The case \(s_t=1\) shows why the extra column is needed: fixing \(S_t\) fixes how many neighbours \(t\) has inside \(T\), but not which (Exercise 5.4).

## 5. Exercises

**Exercise 5.1** (easy). Let \(U=\{1,2\}\), \(W=\varnothing\) and \((\mu_1,\mu_2,\mu_3)=(1,1,0)\) in Lemma 1.1. Find \(g_1,g_2,g_3\) for which (1.1) is an equality with both sides positive.

**Exercise 5.2** (easy). Show that \(\operatorname{Var}(X_1+X_2+X_3)\le3\sum_i\operatorname{Var}X_i\) for all random variables, with equality when \(X_1=X_2=X_3\). Deduce from Theorem 3.1 that a random variable that is a function of \(S_1\), a function of \(S_2\) and a function of \(S_3\) is constant.

**Exercise 5.3** (medium). Take \(\alpha=\beta=0\) in Lemma 2.1. Compute the laws of \(Y_1\) and \(Y_2\), and write down the quantile coupling of the proof explicitly.

**Exercise 5.4** (medium). Let \(T=\{t,u,v\}\) with \(e=1\), let \(tu\) be the edge inside \(T\), and let \(w\notin T\) be adjacent to \(v\) but not to \(u\). Show that replacing the edges \(tu,wv\) by \(tv,wu\) gives a graph in the same \(\{u,v\}\)-fiber, and that the row \(S_t\), with its extra entry, is unchanged.

## 6. Solutions

**5.1.** The space \(\Omega_0\) has two points, \(U_1=\{1\}\) or \(U_1=\{2\}\), with \(U_2\) the other set. Take \(g_1=\mathbf 1_{\{1\in U_1\}}\), \(g_2=\mathbf 1_{\{2\in U_2\}}\) and \(g_3=0\). Then \(g_1=g_2\), so \(\operatorname{Var}(g_1+g_2)=4\cdot\frac14=1=2\bigl(\frac14+\frac14\bigr)\).

**5.2.** By the Cauchy–Schwarz inequality \((y_1+y_2+y_3)^2\le3(y_1^2+y_2^2+y_3^2)\); apply it to the centered variables and take expectations. If \(X=f_1(S_1)=f_2(S_2)=f_3(S_3)\), Theorem 3.1 gives \(9\operatorname{Var}X\le6\operatorname{Var}X\), so \(\operatorname{Var}X=0\).

**5.3.** \(\mathbb P(Y_1=y)\) is proportional to \(w_0(y)w_0(1-y)=1\) for \(y=0,1\), so \(Y_1\) is uniform on \(\{0,1\}\). The weights of \(Y_2\) are \(\frac14,1,\frac14\), so its law is \(\frac16,\frac23,\frac16\). With \(u\) uniform on \((0,1)\): \(Y_1=0\) for \(u\le\frac12\) and \(1\) otherwise; \(Y_2=0\) for \(u\le\frac16\), \(1\) for \(\frac16<u\le\frac56\), and \(2\) otherwise. The pairs \((Y_1,Y_2)\) are \((0,0),(0,1),(1,1),(1,2)\) on the four intervals, and each satisfies \(Y_1\le Y_2\le Y_1+1\).

**5.4.** Before the change, \(t\) is adjacent to \(u\) and not to \(v\), and \(w\) is adjacent to \(v\) and not to \(u\); so \(t\) and \(w\) are singletons of the pair \(\{u,v\}\) assigned to different endpoints, and the change exchanges them. It keeps all edges with no endpoint in \(\{u,v\}\), the absence of the edge \(uv\), and the number of neighbours in \(\{u,v\}\) of every other vertex. The neighbours of \(t\) outside \(T\) are unchanged, and \(s_t=1\) before and after, so \(S_t\) (whose extra entry is \(s_t\)) is unchanged; the extra entries of \(u\) and \(v\) change from \(1,0\) to \(0,1\).

## References

- [OpenAI-SW] OpenAI, *Polynomial mixing of the switch chain for every graphical degree sequence*, OpenAI Math Release preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/Polynomial-Mixing-of-the-Switch-Chain-for-Every-Graphical-Degree-Sequence-September-25-2026
- [FQW] W. Fu, Q. Qin and G. Wang, *Spectral gap for the binary fixed-margin swap chain*, 2026. https://arxiv.org/abs/2606.22636
- [CLL] E. Carlen, E. H. Lieb and M. Loss, *An inequality of Hadamard type for permanents*, Methods and Applications of Analysis 13 (2006), 1–18. https://arxiv.org/abs/math/0508096
