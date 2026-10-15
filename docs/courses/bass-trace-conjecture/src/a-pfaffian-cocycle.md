# A Pfaffian cocycle

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Keep the data of [Path sums of an idempotent](path-sums-of-an-idempotent.md) and [Exterior chains and sparse cycles](exterior-chains-and-sparse-cycles.md): a finitely generated group \(G\), an idempotent \(e\), an element \(g\) of infinite order, \(J=C_G(g)\), \(H=J/\langle g\rangle\) acting freely on the graph \(Y=\langle g\rangle\backslash G\), the path sums \(v_k\) with total weight \(\lambda\), and the cycles \(z_{2m}\in(E_{2m})_H\). This lesson constructs, for every \(m\ge1\), an invariant cocycle \(\psi_m\) on \(E_{2m}\) with
\[
\psi_m(z_{2m})=2^{-m}\lambda .
\]
The construction records how many powers of \(g\) separate two group elements, takes Pfaffians of the resulting antisymmetric matrices, and sums over deletions. With the sparse-chain vanishing theorem it proves the trace theorem [OpenAI-BT, Sections 8 and 9]. The pairing of cyclic cocycles with projective modules, introduced by Connes [Connes, Part II, Section 2], is the conceptual background; the proofs below are direct and finite.

- Relative exponents (Section 1).
- Pfaffians (Section 2).
- A recurrence for weighted Pfaffians (Section 3).
- Descent to a cocycle (Section 4).
- Proof of the trace theorem (Section 5).

## 1. Relative exponents

**Lemma 1.1** ([OpenAI-BT, Lemma 8.1]). There is a function \(\beta:G\times G\to\mathbb R\) such that for all \(h,h'\in G\), \(c\in J\) and \(r,s\in\mathbb Z\),
\[
\begin{aligned}
\beta(h',h)&=-\beta(h,h'),\\
\beta(ch,ch')&=\beta(h,h'),\\
\beta(g^rh,\,g^sh')&=\beta(h,h')\\
&\quad+s-r .
\end{aligned}
\tag{1.1}
\]

*Proof.* The group \(H\) acts on \(Y\times Y\) diagonally, and the action is free because it is free on the first coordinate; this includes the pairs \((y,y)\). For each orbit choose a representative pair \((y_o,y'_o)\) and elements \(l_o,l'_o\in G\) with \(\bar l_o=y_o\), \(\bar l'_o=y'_o\). Given \((h,h')\in G^2\), let \(o\) be the orbit of \((\bar h,\bar h')\) and \(\bar c\in H\) the unique element carrying \((y_o,y'_o)\) to \((\bar h,\bar h')\). For a lift \(c\in J\) of \(\bar c\), the elements \(h\) and \(cl_o\) have the same coset, and so do \(h'\) and \(cl'_o\):
\[
h=g^rcl_o,\qquad h'=g^scl'_o
\]
for integers \(r\), \(s\), which are unique because \(g\) has infinite order. Replacing \(c\) by another lift \(g^tc\) replaces \((r,s)\) by \((r-t,s-t)\). So
\[
B(h,h')=s-r
\]
depends only on \((h,h')\). For \(c'\in J\), the pair \((c'h,c'h')\) has the same orbit, carried by \(\bar c'\bar c\), and \(c'h=g^r(c'c)l_o\) since \(c'\) commutes with \(g\); so \(B(c'h,c'h')=B(h,h')\). Changing \(h\), \(h'\) to \(g^ah\), \(g^bh'\) changes \(r\), \(s\) to \(r+a\), \(s+b\), so \(B(g^ah,g^bh')=B(h,h')+b-a\). The function
\[
\beta(h,h')=\tfrac12\bigl(B(h,h')-B(h',h)\bigr)
\]
is antisymmetric, \(J\)-invariant, and satisfies \(\beta(g^ah,g^bh')=\beta(h,h')+b-a\): the difference \(B(g^ah,g^bh')-B(g^bh',g^ah)\) exceeds \(B(h,h')-B(h',h)\) by \((b-a)-(a-b)\). \(\square\)

The function \(\beta\) does not descend to \(Y\times Y\): by (1.1), \(\beta(h,g^kh)=k\), although \(h\) and \(g^kh\) have the same coset. Its values need not be integers. For \(G=\langle t\rangle\) infinite cyclic and \(g=t^2\), the three conditions force \(\beta(t^a,t^b)=(b-a)/2\) (Exercise 6.3); here \(\bar t\in H\) exchanges the two vertices of \(Y\).

## 2. Pfaffians

Let \(N=2m\) and let \(M\) be an antisymmetric \(N\times N\) matrix over \(\mathbb C\), with rows and columns indexed by \(\{0,\ldots,N-1\}\). In the exterior algebra \(\Lambda(\{0,\ldots,N-1\})\) of [Exterior chains and sparse cycles](exterior-chains-and-sparse-cycles.md), Section 1, put
\[
b_M=\sum_{i<j}M_{ij}\,\varepsilon_i\wedge\varepsilon_j .
\]
The *Pfaffian* \(\operatorname{Pf}(M)\) is the coefficient of \(\varepsilon_{\{0,\ldots,N-1\}}\) in \(b_M^m/m!\). For \(m=0\) put \(\operatorname{Pf}=1\). For \(N=2\), \(\operatorname{Pf}(M)=M_{01}\).

**Lemma 2.1.** (a) \(\operatorname{Pf}(M)=\sum_\mu\operatorname{sgn}(\mu)\prod_{k=1}^mM_{i_kj_k}\), the sum over the partitions \(\mu=\{\{i_1,j_1\},\ldots,\{i_m,j_m\}\}\) of \(\{0,\ldots,N-1\}\) into pairs with \(i_k<j_k\), where \(\operatorname{sgn}(\mu)\) is the sign of the permutation \(i_1,j_1,\ldots,i_m,j_m\). More generally, for \(S\subseteq\{0,\ldots,N-1\}\) with \(|S|=2l\), the coefficient of \(\varepsilon_S\) in \(b_M^l/l!\) is the Pfaffian of the submatrix \(M_S\) with rows and columns in \(S\), in increasing order.
(b) For a permutation \(\sigma\) of \(\{0,\ldots,N-1\}\), the matrix \(M^\sigma_{ij}=M_{\sigma(i)\sigma(j)}\) satisfies \(\operatorname{Pf}(M^\sigma)=\operatorname{sgn}(\sigma)\operatorname{Pf}(M)\).
(c) For \(m\ge1\),
\[
\begin{aligned}
\operatorname{Pf}(M)=\sum_{i=0}^{N-2}&(-1)^iM_{i,N-1}\\
&\cdot\operatorname{Pf}\bigl(M_{\{0,\ldots,N-2\}\setminus\{i\}}\bigr).
\end{aligned}
\]

*Proof.* (a) The two-forms \(\varepsilon_i\wedge\varepsilon_j\) commute, and a product of two-forms vanishes when two of them share an index. So \(b_M^l\) is the sum over ordered \(l\)-tuples of disjoint pairs, and each set of \(l\) disjoint pairs occurs \(l!\) times. The product \(\varepsilon_{i_1}\wedge\varepsilon_{j_1}\wedge\cdots\) of a partition of \(S\) equals \(\operatorname{sgn}\cdot\varepsilon_S\) by Lemma 1.2(c) of that lesson, applied to the order of \(S\).
(b) Let \(L\) be the linear map \(\varepsilon_i\mapsto\varepsilon_{\sigma^{-1}(i)}\) and \(\Lambda(L)\) the multiplicative map of Lemma 1.2(b) there. Using antisymmetry to reorder the pairs, \(\Lambda(L)b_M=b_{M^\sigma}\), hence \(\Lambda(L)(b_M^m/m!)=b_{M^\sigma}^m/m!\). On the top vector, \(\Lambda(L)\) multiplies by \(\operatorname{sgn}(\sigma^{-1})=\operatorname{sgn}(\sigma)\) by Lemma 1.2(c) there. Comparing top coefficients gives \(\operatorname{sgn}(\sigma)\operatorname{Pf}(M)=\operatorname{Pf}(M^\sigma)\).
(c) Write \(b_M=b'+w\wedge\varepsilon_{N-1}\) with \(b'\) the part not involving \(\varepsilon_{N-1}\) and \(w=\sum_{i<N-1}M_{i,N-1}\varepsilon_i\). Since \((w\wedge\varepsilon_{N-1})^2=0\) and two-forms commute,
\[
\frac{b_M^m}{m!}=\frac{b'^m}{m!}+\frac{b'^{m-1}}{(m-1)!}\wedge w\wedge\varepsilon_{N-1}.
\]
The first term has no top component. By (a), \(b'^{m-1}/(m-1)!=\sum_T\operatorname{Pf}(M_T)\varepsilon_T\) over \((N-2)\)-subsets \(T\subseteq\{0,\ldots,N-2\}\), and \(\varepsilon_T\wedge\varepsilon_i\wedge\varepsilon_{N-1}\) is nonzero only for \(T=\{0,\ldots,N-2\}\setminus\{i\}\). Then \(\varepsilon_T\wedge\varepsilon_i\) has sign \((-1)^{\#\{t\in T:t>i\}}=(-1)^{N-2-i}=(-1)^i\), and appending \(\varepsilon_{N-1}\) adds no sign. \(\square\)

For example, when \(N=4\), \(\operatorname{Pf}(M)\) is \(M_{01}M_{23}-M_{02}M_{13}+M_{03}M_{12}\).

## 3. A recurrence for weighted Pfaffians

For a list \(\mathbf h=(h_0,\ldots,h_{2m-1})\) of elements of \(G\) put
\[
\begin{gathered}
p_m(\mathbf h)=\operatorname{Pf}\bigl(\beta(h_i,h_j)\bigr)_{0\le i,j<2m},\\
p_0=1 .
\end{gathered}
\]
By (1.1) the matrix is antisymmetric, and \(p_m\) is constant on \(J\)-orbits of lists. By Lemma 2.1(b), permuting the list multiplies \(p_m\) by the sign of the permutation. Define the finite sums
\[
q_m=v_{2m}(p_m)\quad(m\ge1),\qquad q_0=\lambda .
\]

**Lemma 3.1** ([OpenAI-BT, Lemma 8.2]). For every \(m\ge1\), \(q_m=\tfrac12q_{m-1}\). Hence \(q_m=2^{-m}\lambda\).

*Proof.* Let \(\mathbf h'=(h_1,\ldots,h_{2m-1},h_0)\) be the cyclic rotation of \(\mathbf h\). A cyclic permutation of \(2m\) entries has sign \((-1)^{2m-1}=-1\), so \(p_m(\mathbf h')=-p_m(\mathbf h)\). The twisted shift \(T\mathbf h=(h_1,\ldots,h_{2m-1},gh_0)\) differs from \(\mathbf h'\) only in the last entry. By (1.1), \(\beta(h_i,gh_0)=\beta(h_i,h_0)+1\), so the matrix of \(T\mathbf h\) is that of \(\mathbf h'\) with \(1\) added to every entry of the last column above the diagonal, and \(1\) subtracted below. By Lemma 2.1(c), the Pfaffian is linear in these entries, and the minor omitting the position \(i\) and the last position is the matrix of the list \(h_1,\ldots,\widehat{h_{i+1}},\ldots,h_{2m-1}\). Writing \(j=i+1\) and \(\mathbf h^{(j)}\) for the list \(h_1,\ldots,\widehat{h_j},\ldots,h_{2m-1}\),
\[
\begin{aligned}
&p_m(T\mathbf h)\\
&\ =-p_m(\mathbf h)\\
&\ \ \ +\sum_{j=1}^{2m-1}(-1)^{j+1}\\
&\qquad\cdot p_{m-1}\bigl(\mathbf h^{(j)}\bigr).
\end{aligned}
\tag{3.1}
\]
Take weighted sums. Since \(T\) is a bijection of \(Q_{2m}\) preserving the weights (Lemma 4.1 of [Path sums of an idempotent](path-sums-of-an-idempotent.md)), \(v_{2m}(p_m\circ T)=v_{2m}(p_m)=q_m\). The \(j\)-th function on the right of (3.1) depends only on the list with the entries \(0\) and \(j\) deleted; deleting position \(0\) and then position \(j-1\) of the shortened list, the deletion identities give the weighted sum \(v_{2m-2}(p_{m-1})=q_{m-1}\) for \(m\ge2\). For \(m=1\) the function is the constant \(p_0=1\), whose weighted sum is the total weight \(v_2(1)=\lambda=q_0\). As \(\sum_{j=1}^{2m-1}(-1)^{j+1}=1\), (3.1) gives \(q_m=-q_m+q_{m-1}\). \(\square\)

## 4. Descent to a cocycle

**Proposition 4.1** ([OpenAI-BT, Proposition 8.3]). Let \(m\ge1\). For vertices \(y_0,\ldots,y_{2m}\) of \(Y\), choose \(h_i\in G\) with \(\bar h_i=y_i\), write \(\hat{\mathbf h}_i\) for the list \(h_0,\ldots,\widehat{h_i},\ldots,h_{2m}\), and put
\[
\begin{aligned}
&\psi_m(y_0,\ldots,y_{2m})\\
&\quad=\sum_{i=0}^{2m}(-1)^i\,p_m\bigl(\hat{\mathbf h}_i\bigr).
\end{aligned}
\tag{4.1}
\]
This does not depend on the choice of the \(h_i\), and it defines an invariant linear functional \(\psi_m:E_{2m}\to\mathbb C\) with \(\psi_m([y_0,\ldots,y_{2m}])=\psi_m(y_0,\ldots,y_{2m})\), such that
\[
\psi_m\circ\partial=0,\qquad \psi_m(z_{2m})=2^{-m}\lambda .
\]

*Proof.* Work in the exterior algebra of the positions \(\{0,\ldots,2m\}\) and put
\[
\begin{gathered}
u=\sum_{i=0}^{2m}\varepsilon_i,\\
b=\sum_{0\le i<j\le2m}\beta(h_i,h_j)\,\varepsilon_i\wedge\varepsilon_j .
\end{gathered}
\]
By Lemma 2.1(a), \(b^m/m!=\sum_S p_m(\mathbf h_S)\varepsilon_S\) over the \(2m\)-subsets \(S\), where \(\mathbf h_S\) is the sublist on \(S\). For \(S=\{0,\ldots,2m\}\setminus\{i\}\), \(\varepsilon_i\wedge\varepsilon_S=(-1)^i\varepsilon_{\{0,\ldots,2m\}}\), since \(i\) elements of \(S\) are smaller than \(i\). So the right side of (4.1) is the top coefficient of \(u\wedge b^m/m!\).

*Independence of the lifts.* Replacing \(h_i\) by \(g^{r_i}h_i\) replaces \(\beta(h_i,h_j)\) by \(\beta(h_i,h_j)+r_j-r_i\), so it replaces \(b\) by \(b+u\wedge v\) with \(v=\sum_ir_i\varepsilon_i\); indeed \(u\wedge v=\sum_{i,j}r_j\varepsilon_i\wedge\varepsilon_j\), which is \(\sum_{i<j}(r_j-r_i)\varepsilon_i\wedge\varepsilon_j\). Since two-forms commute, \((b+u\wedge v)^m\) is \(b^m\) plus terms divisible by \(u\wedge v\), and \(u\wedge u=0\). So \(u\wedge(b+u\wedge v)^m=u\wedge b^m\).

*Alternation.* A permutation of the positions fixes \(u\) and transforms \(b\) into the form of the permuted list; as in Lemma 2.1(b), the top coefficient of \(u\wedge b^m/m!\) changes by the sign of the permutation. So the value is alternating in the list of lifts, and by independence of the lifts it is alternating in \(y_0,\ldots,y_{2m}\). If \(y_a=y_b\) with \(a\ne b\), choose \(h_a=h_b\): exchanging the positions \(a\) and \(b\) leaves the list unchanged and changes the sign, so the value is \(0\). Extending multilinearly from vertices to \(\Lambda^1(Y)\), Lemma 1.2(a) of [Exterior chains and sparse cycles](exterior-chains-and-sparse-cycles.md) gives the linear functional \(\psi_m\) on \(E_{2m}=\Lambda^{2m+1}(Y)\).

*Invariance.* For \(\bar c\in H\) with lift \(c\in J\), the elements \(ch_i\) are lifts of \(\bar cy_i\), and \(\beta(ch_i,ch_j)=\beta(h_i,h_j)\).

*Cocycle identity.* Given \(2m+2\) vertices, choose lifts of all of them once. Then \(\psi_m(\partial[y_0,\ldots,y_{2m+1}])\) is the alternating sum, over two successive deletions, of the values of \(p_m\) on the remaining lists. Each list with the positions \(a<b\) removed occurs twice, with the signs \((-1)^a(-1)^{b-1}\) and \((-1)^b(-1)^a\), which cancel.

*The value on \(z_{2m}\).* The cycle \(z_{2m}\) is the class of \(\sum_qw_{2m+1}(q)[\bar h_0,\ldots,\bar h_{2m}]\), one term for each orbit \(q\) with a representative \((h_0,\ldots,h_{2m})\); terms with repeated vertices are \(0\) on both sides. Computing \(\psi_m\) with the lifts \(h_i\) themselves,
\[
\begin{aligned}
\psi_m(z_{2m})&=\sum_{i=0}^{2m}(-1)^i\,v_{2m+1}(p_m\circ d_i)\\
&=\sum_{i=0}^{2m}(-1)^i\,v_{2m}(p_m)=q_m ,
\end{aligned}
\]
by the deletion identities and \(\sum_{i=0}^{2m}(-1)^i=1\). Lemma 3.1 gives \(q_m=2^{-m}\lambda\). \(\square\)

**Example 4.2.** Let \(G\) be the Heisenberg group of triples \((a,b,c)\in\mathbb Z^3\) with
\[
\begin{aligned}
&(a,b,c)(a',b',c')\\
&\quad=(a+a',\,b+b',\,c+c'+ab'),
\end{aligned}
\]
and let \(g=(0,0,1)\), which is central. Then \(J=G\), \(H=G/\langle g\rangle\cong\mathbb Z^2\), and \(Y\) is identified with \(\mathbb Z^2\) by \(\overline{(a,b,c)}=(a,b)\), with \(H\) acting by translations. Choosing the representative pairs \(((0,0),(p,q))\) and the lifts \((0,0,0)\), \((p,q,0)\) in the proof of Lemma 1.1 gives \(B(h,h')=c'-c-a(b'-b)\), hence
\[
\beta(h,h')=(c'-c)-\tfrac12(a+a')(b'-b)
\]
for \(h=(a,b,c)\), \(h'=(a',b',c')\). In the sum \(\beta(h_1,h_2)-\beta(h_0,h_2)+\beta(h_0,h_1)\) that defines \(\psi_1(y_0,y_1,y_2)\), the third coordinates cancel, and the remaining terms add up to \(-\tfrac12\det(y_1-y_0,y_2-y_0)\): \(\psi_1\) is minus the signed area of Example 5.2 of [Exterior chains and sparse cycles](exterior-chains-and-sparse-cycles.md). Its value on the cycle of that example is \(-1\). So the Pfaffian cocycles can take nonzero values on sparse cycles of low dimension; what Theorem 5.1 of that lesson excludes is a nonzero value in high dimension.

## 5. Proof of the trace theorem

*Proof of Theorem 4.1 of [Traces of projective modules](traces-of-projective-modules.md).* First let \(G\) be finitely generated, \(e\in\operatorname{Mat}_q(\mathbb CG)\) idempotent and \(g\in G\) of infinite order, and let \(\lambda=\operatorname{HS}_G([e(\mathbb CG)^q])([g])\). Construct \(Y\), \(H\) and \(D\) as in Lemma 2.1 of [Path sums of an idempotent](path-sums-of-an-idempotent.md); they are fixed before any dimension is chosen. Choose \(m\ge1\) with \(2m\ge n_0(D)\), where \(n_0(D)\) is the bound of the sparse-chain vanishing theorem (Theorem 5.1 of [Exterior chains and sparse cycles](exterior-chains-and-sparse-cycles.md)). By Proposition 4.1 above, \(\psi_m\) is an invariant cocycle with \(\psi_m(z_{2m})=2^{-m}\lambda\). By Proposition 4.1 of that lesson, either \(z_{2m}=0\), and then \(\lambda=0\); or \(z_{2m}\) is the image of a cycle of \(C_{2m}(K)_H\) for a complex \(K\) satisfying the hypotheses of Theorem 5.1, which then gives \(\psi_m(z_{2m})=0\), so again \(\lambda=0\).

Every finitely generated projective module over \(\mathbb CG\) is isomorphic to some \(e(\mathbb CG)^q\), and every element of \(K_0(\mathbb CG)\) is a difference of two such classes; the trace is additive. So \(\operatorname{HS}_G(x)([g])=0\) for all \(x\in K_0(\mathbb CG)\) when \(G\) is finitely generated. Corollary 5.2 of [Traces of projective modules](traces-of-projective-modules.md) extends this to all groups. \(\square\)

The sparse-chain vanishing theorem used here is proved in the next four lessons, beginning with [A transport metric with small balls](a-transport-metric-with-small-balls.md).

## 6. Exercises

**6.1** (easy). Compute \(\operatorname{Pf}(M)\) for \(N=4\) from Lemma 2.1(c), and check it against the sum over the three partitions into pairs.

**6.2** (easy). Let \(M\) be block diagonal with blocks \(\begin{pmatrix}0&t_k\\-t_k&0\end{pmatrix}\), \(k=1,\ldots,m\). Show \(\operatorname{Pf}(M)=t_1\cdots t_m\).

**6.3** (medium). Let \(G=\langle t\rangle\) be infinite cyclic and \(g=t^2\). Show that the conditions (1.1) determine \(\beta\), and that \(\beta(t^a,t^b)=(b-a)/2\).

**6.4** (medium). Show directly from (4.1) and (1.1) that \(\psi_1\) does not depend on the lifts.

**6.5** (medium). In Example 4.2, verify that \(\beta\) satisfies (1.1), and that \(\psi_1(y_0,y_1,y_2)\) equals \(-\tfrac12\det(y_1-y_0,y_2-y_0)\).

## 7. Solutions

**6.1.** By Lemma 2.1(c) with \(N=4\),
\[
\begin{aligned}
\operatorname{Pf}(M)={}&M_{03}\operatorname{Pf}(M_{\{1,2\}})\\
&-M_{13}\operatorname{Pf}(M_{\{0,2\}})\\
&+M_{23}\operatorname{Pf}(M_{\{0,1\}})\\
={}&M_{03}M_{12}-M_{13}M_{02}\\
&+M_{23}M_{01}.
\end{aligned}
\] The partitions \(\{01,23\}\), \(\{02,13\}\), \(\{03,12\}\) give the permutations \(0123\), \(0213\), \(0312\), of signs \(+1\), \(-1\), \(+1\).

**6.2.** In Lemma 2.1(a) only pairs with \(M_{ij}\ne0\) contribute, and the only partition into such pairs is \(\{0,1\},\{2,3\},\ldots\), whose permutation is the identity.

**6.3.** \(J\)-invariance with \(J=G\) gives \(\beta(t^a,t^b)=\varphi(b-a)\) for a function \(\varphi\) on \(\mathbb Z\). The rule \(\beta(g^rh,g^sh')=\beta(h,h')+s-r\) gives \(\varphi(d+2)=\varphi(d)+1\), and antisymmetry gives \(\varphi(-d)=-\varphi(d)\). So \(\varphi(0)=0\) and \(\varphi(1)=-\varphi(-1)=-(\varphi(1)-1)\), hence \(\varphi(1)=\tfrac12\), and by the first rule \(\varphi(d)=d/2\) for all \(d\). This function satisfies the three conditions.

**6.4.** Replacing \(h_i\) by \(g^{r_i}h_i\) adds \((r_2-r_1)-(r_2-r_0)+(r_1-r_0)=0\) to \(\beta(h_1,h_2)-\beta(h_0,h_2)+\beta(h_0,h_1)\).

**6.5.** Antisymmetry is clear. Left multiplication by \((x,y,w)\) changes \(c\) to \(c+w+xb\) and \(a\) to \(a+x\), so \(\beta\) changes by \(x(b'-b)-\tfrac12\cdot2x(b'-b)=0\). Multiplying \(h\) by \(g^r\) adds \(r\) to \(c\), which gives the third rule. For \(\psi_1\), the third coordinates cancel, and with \(y_i=(a_i,b_i)\),
\[
-2\psi_1=\sum(a_i+a_j)(b_j-b_i),
\]
the sum over \((i,j)\in\{(1,2),(2,0),(0,1)\}\). Expanding, the terms \(a_jb_j-a_ib_i\) cancel around the cycle, and the remaining \(\sum(a_ib_j-a_jb_i)\) is \(\det(y_1-y_0,y_2-y_0)\), as in Exercise 6.3 of [Exterior chains and sparse cycles](exterior-chains-and-sparse-cycles.md).

## References

- [OpenAI-BT] OpenAI, *The Bass trace conjecture for complex group rings*, OpenAI Math Release preprint, 24 September 2026, Lemma 8.1, Lemma 8.2, Proposition 8.3 and Section 9. https://github.com/openai/math/tree/main/preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026
- [Connes] A. Connes, *Non-commutative differential geometry*, Publications Mathématiques de l'IHÉS 62 (1985), 41–144, Part II, Section 2; free at Numdam. https://www.numdam.org/item/PMIHES_1985__62__41_0/
