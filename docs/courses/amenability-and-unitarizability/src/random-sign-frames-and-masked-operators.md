# Random sign frames and masked operators

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson converts the sparse assignment of [Contracting averages and sparse assignments](contracting-averages-and-sparse-assignments.md) into operators on \(\ell^2(G;\mathbb C^k)\) [OpenAI-U, Section 4]. Each edge \((x,i)\) from the row \(x\) to the column \(xs_i\) is weighted by the rank-one projection \(P_i\) onto a unit vector \(v_i\in\mathbb C^k\). The vectors are chosen so that every family of at most \(p\approx2r\) of them has a synthesis operator of norm at most \(10\) (Proposition 1.5), although there are \(n\) of them in a space of dimension \(k\approx2r\log(2n)\), much smaller than \(n\). An operator built from such weighted edges factors through a Hilbert space with one coordinate per edge, and the factorization bounds its norm by \(100\) as soon as every row and every column carries at most \(p\) of its edges (Lemma 2.1). Applied to the assignment, this bounds the block rows, the block columns and all conjugation differences of the operators used in the last lesson by \(100\) (Corollary 3.1 and Proposition 3.2), while the translation-invariant operator \(A\) has a kernel of Hilbert–Schmidt energy at least \(n\) (Lemma 3.3).

We use: from the core course [Measure and Integration (D10)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10), Lebesgue measure \(\lambda\) on \(\mathbb R^m\) is translation invariant (Fremlin, *Measure Theory*, Volume 1, 134A) and satisfies \(\lambda(T[E])=|\det T|\,\lambda(E)\) for every linear map \(T\) (Volume 2, 263A); and Proposition 3.2 of [Contracting averages and sparse assignments](contracting-averages-and-sparse-assignments.md). Probabilities below are uniform probabilities on finite sets, so expectations are finite averages.

## 1. Frames from random signs

Let \(\Omega=\{-1,1\}^N\) with the uniform probability \(\Pr(E)=|E|/2^N\) and the expectation \(\mathbb E X=2^{-N}\sum_{\omega\in\Omega}X(\omega)\). For functions \(f_1,\dots,f_N\) of one sign, \(\mathbb E\prod_if_i(\varepsilon_i)=\prod_i\frac12\bigl(f_i(1)+f_i(-1)\bigr)\), by expanding the sum over \(\Omega\). For \(X\ge0\) and \(c>0\), \(\Pr(X\ge c)\le\mathbb EX/c\) (Markov's inequality), and \(\Pr(E_1\cup\dots\cup E_q)\le\sum_j\Pr(E_j)\).

**Lemma 1.1.** \(\cosh t\le e^{t^2/2}\) for real \(t\).

**Proof.** \(\cosh t=\sum_jt^{2j}/(2j)!\) and \(e^{t^2/2}=\sum_jt^{2j}/(2^jj!)\), and \((2j)!\ge2^jj!\), since \((2j)!/j!=(j+1)(j+2)\cdots(2j)\ge2^j\). \(\square\)

**Lemma 1.2** (sums of signs). Let \(c\in\mathbb R^N\) with \(\sum_ic_i^2=\sigma^2>0\) and \(X(\varepsilon)=\sum_ic_i\varepsilon_i\) on \(\Omega\). For \(u>0\), \(\Pr(|X|>u)\le2e^{-u^2/(2\sigma^2)}\).

**Proof.** For \(t>0\), \(\mathbb Ee^{tX}=\prod_i\cosh(tc_i)\le e^{t^2\sigma^2/2}\) by Lemma 1.1, so Markov's inequality gives \(\Pr(X>u)\le e^{-tu}\mathbb Ee^{tX}\le e^{-tu+t^2\sigma^2/2}\). With \(t=u/\sigma^2\) this is \(e^{-u^2/(2\sigma^2)}\). The same bound for \(-X\) gives the claim. \(\square\)

**Lemma 1.3** (nets). For every \(m\ge1\) the unit sphere of \(\mathbb R^m\) contains a set \(\mathcal N\) of at most \(9^m\) points such that every unit vector lies within distance \(\frac14\) of a point of \(\mathcal N\).

**Proof.** Call a set \(\mathcal N\) of unit vectors *separated* if distinct points of it have distance at least \(\frac14\). For such a set, the open balls \(B(u,\frac18)\), \(u\in\mathcal N\), are pairwise disjoint and contained in \(B(0,\frac98)\). By translation invariance and the formula for linear images, \(\lambda(B(u,\rho))=\rho^m\lambda(B(0,1))\), and \(0<\lambda(B(0,1))<\infty\), because the unit ball contains a box of positive volume and lies in the box \([-1,1]^m\). Comparing measures, every finite subset of \(\mathcal N\) has at most \((9/8)^m/(1/8)^m=9^m\) points. So separated sets are finite with at most \(9^m\) points, and there is a separated set \(\mathcal N\) of largest cardinality. If a unit vector \(z\) had distance at least \(\frac14\) from every point of \(\mathcal N\), then \(\mathcal N\cup\{z\}\) would be a larger separated set. \(\square\)

**Lemma 1.4.** Let \(M\) be a real \(k\times p\) matrix and \(\mathcal N_k\subseteq\mathbb R^k\), \(\mathcal N_p\subseteq\mathbb R^p\) sets as in Lemma 1.3. If \(|w_0^{\mathsf T}Mz_0|\le5\) for all \(w_0\in\mathcal N_k\) and \(z_0\in\mathcal N_p\), then the operator norm of \(M\) on real Euclidean spaces is at most \(10\). The operator norm of a real matrix on complex Euclidean spaces equals its real operator norm.

**Proof.** Let \(L\) be the real operator norm, so \(L=\sup|w^{\mathsf T}Mz|\) over real unit vectors \(w,z\). Given such \(w,z\), choose net points with \(\|w-w_0\|\le\frac14\) and \(\|z-z_0\|\le\frac14\). Then
\[
|w^{\mathsf T}Mz|\le|w_0^{\mathsf T}Mz_0|+|(w-w_0)^{\mathsf T}Mz|+|w_0^{\mathsf T}M(z-z_0)|\le5+\tfrac L4+\tfrac L4,
\]
so \(L\le5+\frac L2\) and \(L\le10\). For the second statement, write a complex vector as \(u+iv\) with real \(u,v\); then \(\|M(u+iv)\|^2=\|Mu\|^2+\|Mv\|^2\le L^2(\|u\|^2+\|v\|^2)=L^2\|u+iv\|^2\), and real vectors show that the complex norm is not smaller. \(\square\)

For unit vectors \(v_1,\dots,v_n\in\mathbb C^k\) and \(J\subseteq[n]=\{1,\dots,n\}\), the *synthesis operator* is \(V_J:\ell^2(J)\to\mathbb C^k\), \(V_Jz=\sum_{i\in J}z_iv_i\).

**Proposition 1.5** (frames). Let \(n\ge2\) and \(r\ge1\) be integers and put
\[
p=\min(2r,n),\qquad k=\lceil2r\log(2n)\rceil,\tag{1.1}
\]
with the natural logarithm. There are unit vectors \(v_1,\dots,v_n\in\mathbb C^k\) with \(\|V_J\|\le10\) for every \(J\subseteq[n]\) with \(|J|\le p\).

**Proof.** On \(\Omega=\{-1,1\}^{k\times n}\) put \(v_i=k^{-1/2}(\varepsilon_{1i},\dots,\varepsilon_{ki})\), a real unit vector. Fix \(J=\{i_1<\dots<i_p\}\) and unit vectors \(w_0\in\mathcal N_k\), \(z_0\in\mathcal N_p\) from Lemma 1.3. Then
\[
X=w_0^{\mathsf T}V_Jz_0=\sum_{a=1}^k\sum_{j=1}^p\frac{w_{0,a}z_{0,j}}{\sqrt k}\,\varepsilon_{a\,i_j}
\]
is a sum of distinct signs whose coefficients have squared sum \(\frac1k\|w_0\|^2\|z_0\|^2=\frac1k\), so \(\Pr(|X|>5)\le2e^{-25k/2}\) by Lemma 1.2. There are at most \(n^p\) sets \(J\) with \(|J|=p\) and at most \(9^k9^p\) pairs \((w_0,z_0)\). So the probability that \(|w_0^{\mathsf T}V_Jz_0|>5\) for some such \(J,w_0,z_0\) is at most \(2n^p9^{k+p}e^{-25k/2}\). Since \(n\ge2\), \(\log(2n)\ge\log4>1\); hence \(k\ge2r\log(2n)\ge p\log n\) and \(k\ge2r\ge p\). The logarithm of the bound is therefore at most
\[
\log2+k+2k\log9-\tfrac{25}2k=\log2-\bigl(\tfrac{23}2-2\log9\bigr)k<\log2-7<0,
\]
because \(2\log9<4.4\) and \(k\ge1\). So some \(\omega\in\Omega\) avoids all these events. For it, every \(V_J\) with \(|J|=p\) satisfies the hypothesis of Lemma 1.4 and has norm at most \(10\). If \(|J|<p\), then \(J\) lies in some \(J'\) with \(|J'|=p\), as \(p\le n\), and \(V_J\) is the restriction of \(V_{J'}\) to the coordinate subspace \(\ell^2(J)\); so \(\|V_J\|\le10\) as well. \(\square\)

The dimension \(k\) cannot be much smaller than \(p\) (Exercise 4.2).

## 2. Masked operators

Let \(G\) be a countable group, \(s_1,\dots,s_n\in G\) a list in which repetitions are allowed, \(v_1,\dots,v_n\in\mathbb C^k\) unit vectors, \(P_i=v_iv_i^*\) the projection onto \(\mathbb Cv_i\), and \(\mathcal H=\ell^2(G;\mathbb C^k)\). For a function \(c:G\times[n]\to\mathbb C\) with \(|c|\le1\), the *masked operator* is
\[
(T_c\xi)(x)=\sum_{i=1}^nc(x,i)\,P_i\,\xi(xs_i)\qquad(\xi\in\mathcal H,\ x\in G).\tag{2.1}
\]
The \(i\)-th term is the composite of the unitary \(\xi\mapsto\xi(\cdot\,s_i)\), the pointwise projection \(P_i\) and multiplication by \(c(\cdot,i)\), so it has norm at most \(1\), and \(\|T_c\|\le n\). Put
\[
\mathcal R_x=\{i:c(x,i)\neq0\},\qquad\mathcal C_y=\{i:c(ys_i^{-1},i)\neq0\},
\]
the labels of the edges of \(c\) at the row \(x\) and at the column \(y\).

**Lemma 2.1** (masked operator estimate). Let \(1\le p\le n\), \(b_0>0\), and suppose \(\|V_J\|\le b_0\) whenever \(|J|\le p\). If \(|\mathcal R_x|\le p\) and \(|\mathcal C_y|\le p\) for all \(x,y\in G\), then \(\|T_c\|\le b_0^2\).

**Proof.** Let \(E_c=\{(x,i):c(x,i)\neq0\}\), a countable set, and define \(F:\mathcal H\to\ell^2(E_c)\), \(M_c:\ell^2(E_c)\to\ell^2(E_c)\) and \(S:\ell^2(E_c)\to\mathcal H\) by
\[
(F\xi)(x,i)=v_i^*\xi(xs_i),\qquad(M_c\alpha)(x,i)=c(x,i)\alpha(x,i),\qquad(S\alpha)(x)=\sum_{i\in\mathcal R_x}\alpha(x,i)\,v_i.
\]
The map \((x,i)\mapsto(xs_i,i)\) is a bijection of \(G\times[n]\), and \((x,i)\in E_c\) exactly when \(i\in\mathcal C_{xs_i}\). Regrouping by \(y=xs_i\),
\[
\|F\xi\|^2=\sum_{y\in G}\sum_{i\in\mathcal C_y}|v_i^*\xi(y)|^2=\sum_y\|V_{\mathcal C_y}^*\xi(y)\|^2\le b_0^2\|\xi\|^2,
\]
since \(V_J^*u=(v_i^*u)_{i\in J}\) and \(\|V_J^*\|=\|V_J\|\). Since \(E_c\) is the disjoint union of the sets \(\{x\}\times\mathcal R_x\),
\[
\|S\alpha\|^2=\sum_x\bigl\|V_{\mathcal R_x}\bigl(\alpha(x,i)\bigr)_{i\in\mathcal R_x}\bigr\|^2\le b_0^2\sum_x\sum_{i\in\mathcal R_x}|\alpha(x,i)|^2=b_0^2\|\alpha\|^2.
\]
So \(\|F\|,\|S\|\le b_0\) and \(\|M_c\|\le1\). Finally \((SM_cF\xi)(x)=\sum_{i\in\mathcal R_x}c(x,i)v_iv_i^*\xi(xs_i)=(T_c\xi)(x)\), so \(\|T_c\|\le b_0^2\). \(\square\)

Two labels \(i\neq j\) with \(s_i=s_j\) give two edges from \(x\) to the same column; they are different coordinates of \(\ell^2(E_c)\), and the counts \(|\mathcal R_x|\), \(|\mathcal C_y|\) count them separately. The proof uses only that a fixed label \(i\) and a column \(y\) determine the row \(ys_i^{-1}\).

## 3. The operators of an assignment

Fix integers \(n\ge2\) and \(r\ge1\), let \(p\), \(k\) and \(v_1,\dots,v_n\) be as in Proposition 1.5, and let \(G\), \(s_i\), \(P_i\), \(\mathcal H\) be as in Section 2. Suppose \(a:G\times[n]\to\{0,1\}\) satisfies
\[
\#\{i:a(x,i)=1\}\le r\quad(x\in G),\qquad\#\{i:a(ys_i^{-1},i)=0\}\le r\quad(y\in G),\tag{3.1}
\]
as the assignment of Proposition 3.2 of the previous lesson does. Put
\[
A=T_{\mathbf1},\qquad T=T_a,\qquad(U(g)\xi)(x)=\xi(g^{-1}x),
\]
where \(\mathbf1(x,i)=1\). For \(y\in G\) let \(\iota_y:\mathbb C^k\to\mathcal H\) be the inclusion at the coordinate \(y\) and \(q_y=\iota_y^*\) the evaluation at \(y\).

**Corollary 3.1** (block rows and columns). \(\|q_xT\|\le100\) and \(\|(A-T)\iota_y\|\le100\) for all \(x,y\in G\).

**Proof.** Fix \(x_0,y_0\in G\) and let \(c_{\rm r}(x,i)=\mathbf1_{x=x_0}a(x,i)\) and \(c_{\rm c}(x,i)=\mathbf1_{xs_i=y_0}(1-a(x,i))\). The mask \(c_{\rm r}\) has edges only at the row \(x_0\), at most \(r\) of them by (3.1); so every \(\mathcal R_x\) and every \(\mathcal C_y\) has at most \(\min(r,n)\le p\) elements. The mask \(c_{\rm c}\) has edges only at the column \(y_0\), namely the edges \((y_0s_i^{-1},i)\) with \(a(y_0s_i^{-1},i)=0\), at most \(r\) of them; again all \(\mathcal R_x,\mathcal C_y\) have at most \(p\) elements. Lemma 2.1 bounds \(\|T_{c_{\rm r}}\|\) and \(\|T_{c_{\rm c}}\|\) by \(100\). From (2.1),
\[
T_{c_{\rm r}}=\iota_{x_0}q_{x_0}T,\qquad T_{c_{\rm c}}=(A-T)\iota_{y_0}q_{y_0}.
\]
Since \(\iota_{x_0}\) is isometric, \(\|q_{x_0}T\|=\|T_{c_{\rm r}}\|\); since \(q_{y_0}\iota_{y_0}=1\) and \(\|q_{y_0}\|=1\), \(\|(A-T)\iota_{y_0}\|=\|T_{c_{\rm c}}\iota_{y_0}\|\le\|T_{c_{\rm c}}\|\). \(\square\)

**Proposition 3.2** (conjugation differences). \(U\) is a unitary representation of \(G\) on \(\mathcal H\), \(A\) commutes with every \(U(g)\), and
\[
\|T-U(g)TU(g)^{-1}\|\le100\qquad(g\in G).
\]

**Proof.** \(U(g)\) is unitary since left multiplication by \(g\) permutes \(G\), and \(U(g)U(h)=U(gh)\). For a mask \(c\), substituting in (2.1),
\[
(U(g)T_cU(g)^{-1}\xi)(x)=(T_cU(g)^{-1}\xi)(g^{-1}x)=\sum_ic(g^{-1}x,i)P_i\,\xi(xs_i),
\]
so \(U(g)T_cU(g)^{-1}=T_{c(g^{-1}\cdot,\cdot)}\). With \(c=\mathbf1\) this shows \(U(g)AU(g)^{-1}=A\). With \(c=a\) it shows \(T-U(g)TU(g)^{-1}=T_{c_g}\) for
\[
c_g(x,i)=a(x,i)-a(g^{-1}x,i)\in\{-1,0,1\}.
\]
At a row \(x\), the labels with \(c_g(x,i)\neq0\) lie in \(\{i:a(x,i)=1\}\cup\{i:a(g^{-1}x,i)=1\}\), which has at most \(2r\) elements by (3.1), and at most \(n\). At a column \(y\), put \(Z_y=\{i:a(ys_i^{-1},i)=0\}\), so \(|Z_y|\le r\). The labels with \(c_g(ys_i^{-1},i)\neq0\) are those with \(a(ys_i^{-1},i)\neq a(g^{-1}ys_i^{-1},i)\); as \(a\) takes only the values \(0\) and \(1\), they form \(Z_y\mathbin\triangle Z_{g^{-1}y}\), with at most \(2r\) elements, and at most \(n\). So all these sets have at most \(p=\min(2r,n)\) elements, and Lemma 2.1 gives \(\|T_{c_g}\|\le100\). \(\square\)

For an operator \(F\) on \(\mathcal H\) write \(F[x,y]=q_xF\iota_y\) for its \(k\times k\) blocks, and \(\|W\|_{\rm HS}^2=\operatorname{Tr}(W^*W)\) for the Hilbert–Schmidt norm of a \(k\times k\) matrix \(W\), the sum of the squared moduli of its entries.

**Lemma 3.3** (the kernel of \(A\)). \(A[x,y]=W(x^{-1}y)\) with \(W(s)=\sum_{i:s_i=s}P_i\), and
\[
\sum_{s\in G}\|W(s)\|_{\rm HS}^2=\sum_{i,j:\,s_i=s_j}|\langle v_i,v_j\rangle|^2\ge n.
\]

**Proof.** For \(u\in\mathbb C^k\), \((A\iota_yu)(x)=\sum_iP_i(\iota_yu)(xs_i)=\sum_{i:xs_i=y}P_iu\), which is \(W(x^{-1}y)u\). Next \(\|W(s)\|_{\rm HS}^2=\sum_{i,j:s_i=s_j=s}\operatorname{Tr}(P_iP_j)\) and \(\operatorname{Tr}(P_iP_j)=\operatorname{Tr}(v_iv_i^*v_jv_j^*)=|\langle v_i,v_j\rangle|^2\ge0\). Summing over \(s\) gives the formula. The terms with \(i=j\) equal \(1\), and the others are nonnegative. \(\square\)

Coincidences \(s_i=s_j\) among the products can only increase this energy, because the weights are positive.

## 4. Exercises

**Exercise 4.1** (easy). Show that the constant \(\frac12\) in Lemma 1.1 cannot be replaced by a smaller one: if \(\cosh t\le e^{\gamma t^2}\) for all \(t\), then \(\gamma\ge\frac12\).

**Exercise 4.2** (medium). Let \(v_1,\dots,v_n\in\mathbb C^k\) be unit vectors with \(\|V_J\|\le b_0\) for all \(|J|\le p\). Show that \(k\ge p/b_0^2\). So in Proposition 1.5 the dimension \(k=\lceil2r\log(2n)\rceil\) is within a factor of order \(\log n\) of the smallest possible.

**Exercise 4.3** (easy). Show directly from (2.1) that \(A\) commutes with every \(U(g)\), and that \(T\) need not: find \(G\), \(s_1\) and \(a\) with \(n=1\) for which \(TU(g)\neq U(g)T\).

**Exercise 4.4** (medium). The row condition in Lemma 2.1 cannot be dropped. Let \(G=\mathbb Z\) (written additively), \(n\ge1\), \(s_i=i\), \(k=1\), \(v_i=1\), and \(c(x,i)=1\) if \(x=0\) and \(0\) otherwise. Compute \(\|T_c\|\), \(|\mathcal R_0|\) and the sets \(\mathcal C_y\).

## 5. Solutions

**4.1.** As \(t\to0\), \(\cosh t=1+\frac{t^2}2+O(t^4)\) and \(e^{\gamma t^2}=1+\gamma t^2+O(t^4)\); the inequality forces \(\frac12\le\gamma\).

**4.2.** For \(|J|=p\) we have \(\operatorname{Tr}(V_JV_J^*)=\operatorname{Tr}(V_J^*V_J)=\sum_{i\in J}\|v_i\|^2=p\), while \(V_JV_J^*\) is a positive \(k\times k\) matrix of norm \(\|V_J\|^2\le b_0^2\), so its trace is at most \(kb_0^2\). Hence \(p\le kb_0^2\).

**4.3.** \(U(g)AU(g)^{-1}=T_{\mathbf1(g^{-1}\cdot,\cdot)}=T_{\mathbf1}=A\) by the computation in the proof of Proposition 3.2. For \(G=\mathbb Z\), \(n=1\), \(s_1=0\), \(k=1\), \(v_1=1\) and \(a(x,1)=1\) exactly for \(x=0\): \(T\) is the projection onto the coordinate \(0\), and \(U(1)TU(1)^{-1}\) is the projection onto the coordinate \(1\).

**4.4.** \((T_c\xi)(0)=\sum_{i=1}^n\xi(i)\) and \((T_c\xi)(x)=0\) for \(x\neq0\), so \(\|T_c\|=\sqrt n\), attained at \(\xi=\mathbf1_{\{1,\dots,n\}}\). Here \(|\mathcal R_0|=n\), while \(\mathcal C_y=\{y\}\) for \(1\le y\le n\) and \(\mathcal C_y=\varnothing\) otherwise. The column condition holds with \(p=1\), the row condition fails for \(p<n\), and the norm grows like \(\sqrt{|\mathcal R_0|}\).

## References

- [OpenAI-U] OpenAI, *Unitarizability implies amenability for discrete groups*, OpenAI Math Release preprint, 23 September 2026, Section 4. https://github.com/openai/math/blob/main/preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026
