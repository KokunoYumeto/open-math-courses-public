# From tested rank to full rank

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The two decoders of the upper level output bilinear forms \(F_L\) and \(F_R\) that agree on the projected space with a probability of at least \(\gamma\). The left form has the shape \(F_L(x,y)=z(xy)\), and its matrix on the rows of the array \(S\) at the node \(D_i\) has a rank of at most one. This is a statement about the \(\ell_i\) rows that the decoder was given; the decoder may choose a different form for every array. This lesson proves that a fixed part of the agreement comes from left forms whose rank on the whole space is bounded: with a probability of at least \(\gamma/2\) the forms agree and \(F_L\) has a rank of at most \(s\), where \(s\) depends only on \(\gamma\).

The proof assumes the contrary and removes the forms of rank at most \(s\) from the outputs. Two arrays that differ by a step of rank one in the direction that the right side does not see lead to the same right output, so the two left outputs agree on the projected space with a probability of at least the square of the agreement. Two different forms that are computed without knowledge of the projection rarely agree on the projected space. So the left output is often the same form along the step, and the inverse theorem gives one fixed form of large rank that is the output on a fraction of a slice. A fixed form of large rank has a matrix of rank at most one on few arrays of a slice. This is a contradiction.

- Admissible forms and the statement (Proposition 1.1).
- Decoders without random choices (Lemma 2.1).
- Two draws of the lower array (Lemmas 3.1 and 3.2, Proposition 3.3).
- A fixed form on a slice (Lemma 4.1).
- Proof of the statement (Section 5).

The lesson follows [OpenAI-G, Section 6]. It continues [The heavy list and the two decoders](the-heavy-list-and-the-two-decoders.md) and uses its decoders, the left and right data, the law \(\mathbb P_i\) and the spaces \(H_i=H_{D_i}(E)\), \(H_i'=H_{D_i}(O)\). It uses the posterior bound and sparse projection from [Changing the law of the tests](changing-the-law-of-the-tests.md), the inverse theorem of [Matrices, slices and the inverse theorem](matrices-slices-and-the-inverse-theorem.md), and Lemma 3.1 of [Folding and the law of the tests](folding-and-the-law-of-the-tests.md).

## 1. Admissible forms and the statement

Let \(K_i=\mathbb F^{\ell_i}\) and \(S=M_{D_i}\), an array with the rows \(S_1,\dots,S_{\ell_i}\in H_i\). For a bilinear form \(F\) on \(H_i\) let
\[
\operatorname{Gram}_F(S)=\bigl(F(S_u,S_v)\bigr)_{u,v}
\]
be its matrix on the rows of \(S\), and let \(\operatorname{rank}F\) be the rank of \(F\) as a form on \(H_i\), that is, the rank of the linear map \(x\mapsto F(x,\cdot)\) from \(H_i\) to \(H_i^*\).

**Definition.** A bilinear form \(F\) on \(H_i\) is *admissible at \(S\)* if there is a linear functional \(z\) on \(H_i^2\) with
\[
F(x,y)=z(xy),\qquad z(1)=1,
\]
and \(\operatorname{rank}\operatorname{Gram}_F(S)\le1\).

Every value of the left decoder is admissible at the array \(S\) of its data, by Proposition 3.1 of the lesson on the heavy list. The left decoder is defined for all left data, also for data that have the probability \(0\) under \(\mathbb P_i\): the advice is good or not, and in both cases the output is formed by the same rule, with the same two properties.

**Proposition 1.1.** Let the assumptions of Proposition 3.1 of the lesson on the heavy list hold for the levels \(i<j\), and let \(\gamma=\gamma_j\). Let \(\alpha'\le1\), \(r'\), \(\ell_0'\) be the numbers of the inverse theorem (Theorem 4.1 of the lesson on matrices and slices) for \(\eta'=\gamma^2/8\). Let \(m\ge1\) and \(s\ge1\) be integers with
\[
\begin{gathered}
\bigl[1+(2^m-1)^2\bigr]\,2^{-m^2}<\frac{\alpha'}2,\\
2^{\,m-(s-2r')}<\frac{\alpha'}2,
\end{gathered}
\]
and let \(\ell_i\ge\max\{\ell_0',\,2m+r'\}\). Let \(L\) be the bound \(L_i\) of the lesson on changing the law for the calls at \(D_i\) used so far and one more, \(\beta=n_i^{-2/3}\), and let
\[
\begin{gathered}
\frac{2\beta L}{1-\beta}\le\frac{\gamma^2}{64},\\
\upsilon=\frac12\sqrt{(1+\beta^2L)^{n_i}-1}\le\frac{\gamma^2}{64}.
\end{gathered}
\]
Then the probability under \(\mathbb P_i\) that \(F_L=F_R\) on \(H_i'\times H_i'\) and \(\operatorname{rank}F_L\le s\) is at least \(\gamma/2\).

The numbers \(\alpha',r',\ell_0'\) depend only on \(\gamma\). Since the first expression tends to \(0\) as \(m\) grows, one can choose \(m\), then \(s\), then \(\ell_i\), all in terms of \(\gamma\) alone. The number \(L\) does not depend on \(n_i\), so the last two conditions hold when \(n_i\) is large.

## 2. Decoders without random choices

Each decoder uses its data and independent random choices. Its random choices can be drawn before the data are known: one draws a function that assigns to all possible data an output. So a decoder is a random choice among finitely many functions from data to outputs, independent of the data and of the other decoder.

**Lemma 2.1.** Let \(\mathcal E\) be an event that is determined by the data of the two sides and the two outputs. Then there are a function \(f_L\) from left data to bilinear forms on \(H_i\) and a function \(f_R\) from right data to bilinear forms on \(H_i'\), each a possible choice of the corresponding decoder, such that the probability of \(\mathcal E\) with the outputs \(f_L\), \(f_R\) is at least \(\mathbb P_i(\mathcal E)\). Every value of \(f_L\) is admissible at the array \(S\) of its data.

**Proof.** \(\mathbb P_i(\mathcal E)\) is the mean, over the choices of the two functions, of the probability of \(\mathcal E\) for these functions. One pair of functions is at least as good as the mean. \(\blacksquare\)

Fixing the functions is not a conditioning on an outcome of the test.

## 3. Two draws of the lower array

Let \(f_L,f_R\) be functions as in Lemma 2.1, and \(s\ge1\). The *table* \(f\) assigns to left data the form \(f_L\) of these data if its rank is more than \(s\), and \(\bot\) otherwise.

Under \(\mathbb P_i\) let \(k_v\) be the buckets of \(S\), let \(k'\) be one more call at \(D_i\), independent of the others, and \(a=a_i\). Replacing the bucket \(k_a\) by \(k'\) gives
\[
S'=S+a\otimes l,\qquad l=k_a+k' .
\]
The *rest* \(\mathcal C\) consists of \(E\), the marks, \(O\) with the edges chosen at the marked leaves, the path to \(D_i\), the map \(A\), the exterior data \(\Xi_i\), the calls at \(D_i\) other than the \(k_v\) and \(k'\), and the arrays below \(D_i\). Under \(\mathbb P_i\), given the marks and \(O\), the calls at \(D_i\) are independent and uniform in \(H_i'\). So by Lemma 3.1 of the lesson on folding, given \(\mathcal C\): \(S\) is uniform in \(K_i\otimes H_i'\), \(l\) is uniform in \(H_i'\), \(a\) is uniform in \(K_i\setminus\{0\}\), and the three are independent.

The left data are a function of \(\mathcal C\) and \(S\): the arrays at the nodes other than \(D_i\), and the buckets of the upper matrix, are computed from \(\mathcal C\). We write \(f(S)\) for the value of the table at the left data with the array \(S\), and \(f(S')\) for its value at the left data with \(S'\) in place of \(S\). The right data are a function of \(\mathcal C\), of \(a\) and of the class of \(S\) modulo \(a\); they are the same for \(S\) and \(S'\). Let \(F_R\) be the value of \(f_R\) at them.

**Lemma 3.1.** Let \(h\) be the probability under \(\mathbb P_i\) that \(f(S)\ne\bot\) and \(f(S)=F_R\) on \(H_i'\times H_i'\). Then the probability that \(f(S)\) and \(f(S')\) are both defined and agree on \(H_i'\times H_i'\) is at least \(h^2\).

**Proof.** Fix \(\mathcal C\), \(a\) and the class \(q\) of \(S\) modulo \(a\). The arrays with this class are the arrays \(S+a\otimes x\), \(x\in H_i'\), and \(x\mapsto S+a\otimes x\) is one-to-one. So, given \((\mathcal C,a,q)\), the arrays \(S\) and \(S'\) are independent, and each is uniform among the arrays of the class \(q\). The form \(F_R\) is a function of \((\mathcal C,a,q)\). Let \(p\) be the conditional probability that \(f(S)\ne\bot\) and \(f(S)=F_R\) on \(H_i'\times H_i'\). The same holds for \(S'\) with the same \(p\), and the two events are independent given \((\mathcal C,a,q)\). So both hold with the probability
\[
\mathbb E\,p^2\ge(\mathbb E\,p)^2=h^2 ,
\]
and if both hold, \(f(S)\) and \(f(S')\) agree on \(H_i'\times H_i'\) with \(F_R\). \(\blacksquare\)

**Lemma 3.2.** The probability under \(\mathbb P_i\) that \(f(S)\) and \(f(S')\) are both defined, different, and equal on \(H_i'\times H_i'\) is at most \(2\beta L/(1-\beta)\).

**Proof.** Let \(F_0\) be \(f(S)\) where it is defined and the form \(0\) elsewhere, and \(F_1\) the same for \(S'\). Given \(E\) and the path to \(D_i\), the two left data are functions of \(\Xi_i\), of the blocks of the children of \(D_i\), which contain the contributions to all the calls, and of the independent data \(A\) and \(a\). So \(F_0\) and \(F_1\) are bilinear forms on \(H_i\) that are functions of these data. They do not use the marks or \(O\). By part (3) of Proposition 4.2 of the lesson on changing the law, the event that \(F_0\ne F_1\) and the two forms agree on \(H_i'\times H_i'\) has a probability of at most \(2\beta L/(1-\beta)\). The event of the lemma is contained in it. \(\blacksquare\)

The bound of Lemma 3.2 is a probability under \(\mathbb P_i\) without a conditioning; it is subtracted from the probability of Lemma 3.1.

**The unrestricted law \(\mathbb P_i^0\).** Draw \(E\), the path to \(D_i\) and \(\Xi_i\) as in the test, the calls at \(D_i\) independently and uniformly in \(H_i\), and the arrays below \(D_i\) independently and uniformly; \(A\) and \(a\) are independent of these. This is the law \(\mathsf U_i\) of the lesson on changing the law. The arrays, the left data, \(S\), \(l\) and \(S'\) are computed by the same rules as under \(\mathbb P_i\). Let \(\mathcal C^0\) be the rest: \(E\), the path, \(A\), \(\Xi_i\), the other calls and the arrays below \(D_i\).

**Proposition 3.3.** Under \(\mathbb P_i^0\), given \(\mathcal C^0\), the array \(S\) is uniform in \(K_i\otimes H_i\), the function \(l\) is uniform in \(H_i\), the vector \(a\) is uniform in \(K_i\setminus\{0\}\), and the three are independent. With \(h\) as in Lemma 3.1,
\[
\begin{aligned}
&\mathbb P_i^0\bigl(f(S)=f(S+a\otimes l)\ne\bot\bigr)\\
&\quad\ge h^2-\frac{2\beta L}{1-\beta}-\upsilon .
\end{aligned}
\]
For every value of \(\mathcal C^0\), the map \(S\mapsto f(S)\) is a partial table on \(K_i\otimes H_i\) in the sense of the lesson on matrices and slices. Each of its values other than \(\bot\) is a bilinear form \(F\) on \(H_i\) with \(\operatorname{rank}F>s\) that is admissible at \(S\).

**Proof.** The first statement is Lemma 3.1 of the lesson on folding. By Lemmas 3.1 and 3.2, under \(\mathbb P_i\) the forms \(f(S)\) and \(f(S')\) are defined and equal with a probability of at least \(h^2-2\beta L/(1-\beta)\). This event is a function of \(\Xi_i\), of the blocks, and of \(A\) and \(a\), given \(E\) and the path. By Proposition 4.1 of the lesson on changing the law its probabilities under \(\mathbb P_i\) and \(\mathbb P_i^0\) differ by at most \(\upsilon\). The last statement holds because the left data depend on \(S\) only through the array at \(D_i\), once \(\mathcal C^0\) is fixed, and by the definition of the table and Lemma 2.1. \(\blacksquare\)

In the table of the proposition, the array \(S\) is the only argument. The background, the space \(B\), the advice and the witness of the left decoder are computed again for every \(S\); they are not held fixed.

## 4. A fixed form on a slice

This section is linear algebra over \(\mathbb F\). Let \(H\) be a vector space, \(F\) a bilinear form on \(H\), and \(K=\mathbb F^\ell\). An element \(S\in K\otimes H\) is a list of rows \(S_1,\dots,S_\ell\in H\), and \(\operatorname{Gram}_F(S)=(F(S_u,S_v))_{u,v}\).

**Lemma 4.1.** Let \(m\ge1\), \(r'\ge0\) and \(\ell\ge2m+r'\). Let \(\mathcal S\subset K\otimes H\) be a slice with at most \(r'\) row combinations and at most \(r'\) column values. Then for \(S\) uniform in \(\mathcal S\),
\[
\begin{aligned}
&\mathbb P\bigl(\operatorname{rank}\operatorname{Gram}_F(S)\le1\bigr)\\
&\quad\le(2^m-1)\,2^{-(\operatorname{rank}F-2r')}\\
&\qquad+\bigl[1+(2^m-1)^2\bigr]\,2^{-m^2}.
\end{aligned}
\]
If \(\operatorname{rank}F>s\), the first term is less than \(2^{\,m-(s-2r')}\).

**Proof.** *New rows.* The slice is given by \(A_0S=U\) with a map \(A_0:K\to\mathbb F^k\), \(k\le r'\), and by \(Sq_b=t_b\) for functionals \(q_1,\dots,q_c\in H^*\), \(c\le r'\). Let \(e\le r'\) be the rank of \(A_0\). Choose an invertible \(\ell\times\ell\) matrix \(T\) whose first \(e\) rows span the rows of \(A_0\), and let \(Y=TS\): the rows of \(Y\) are the combinations of the rows of \(S\) with the coefficients in the rows of \(T\). By bilinearity
\[
\operatorname{Gram}_F(Y)=T\,\operatorname{Gram}_F(S)\,T^{\mathsf t},
\]
so the two matrices have the same rank. The map \(S\mapsto Y\) is one-to-one and linear. In terms of \(Y\) the slice says: the first \(e\) rows of \(Y\) are prescribed, and \(q_b(Y_u)\) is prescribed for every row \(u\) and every \(b\). Let \(N\subset H\) be the space where all \(q_b\) vanish; its codimension is at most \(c\le r'\). Since the slice is not empty, the conditions on each row \(u>e\) are satisfied by the elements of a coset of \(N\), and there is no condition that joins two rows. So for \(S\) uniform in the slice, the rows \(Y_u\) with \(u>e\) are independent, and each is uniform in its coset of \(N\). There are \(\ell-e\ge2m\) such rows.

*The rank on \(N\).* Let \(F_N\) be the restriction of \(F\) to \(N\times N\), and \(t\) its rank. Restricting the first argument to \(N\) lowers the rank of the map \(x\mapsto F(x,\cdot)\) by at most the codimension of \(N\), and restricting the functionals \(F(x,\cdot)\) to \(N\) lowers it by at most the same number. So
\[
t\ge\operatorname{rank}F-2r' .
\]
Let \(V\subset N^*\) be the image of \(N\) under \(n\mapsto F(n,\cdot)|_N\); it has the dimension \(t\).

*The first group of rows.* Take \(2m\) of the rows \(Y_u\), \(u>e\), and call them \(x_1,\dots,x_m\) and \(y_1,\dots,y_m\). Write \(x_u=\xi_u+n_u\) with a fixed \(\xi_u\) and \(n_u\) uniform in \(N\). The functional
\[
\begin{aligned}
\lambda_u&=F(x_u,\cdot)|_N\\
&=F(\xi_u,\cdot)|_N+F(n_u,\cdot)|_N
\end{aligned}
\]
is uniform in a coset of \(V\), and \(\lambda_1,\dots,\lambda_m\) are independent. For a nonzero vector \(\epsilon\in\mathbb F^m\) the sum \(\sum_u\epsilon_u\lambda_u\) is uniform in a coset of \(V\) as well: fix all summands except one with \(\epsilon_u=1\). So it is \(0\) with a probability of at most \(2^{-t}\). There are \(2^m-1\) vectors \(\epsilon\), so the probability that \(\lambda_1,\dots,\lambda_m\) are linearly dependent is at most \((2^m-1)\,2^{-t}\).

*The second group.* Let the \(\lambda_u\) be linearly independent. Then the map \(n\mapsto(\lambda_1(n),\dots,\lambda_m(n))\) from \(N\) to \(\mathbb F^m\) is onto. Write \(y_v=\zeta_v+n'_v\) with \(n'_v\) uniform in \(N\), independent of the first group and of each other. The column
\[
\begin{aligned}
\bigl(F(x_u,y_v)\bigr)_u&=\bigl(F(x_u,\zeta_v)\bigr)_u\\
&\quad+\bigl(\lambda_u(n'_v)\bigr)_u
\end{aligned}
\]
is uniform in \(\mathbb F^m\). So, given the first group, the \(m\times m\) matrix \(C=(F(x_u,y_v))_{u,v}\) is uniform among all \(m\times m\) matrices.

*Counting.* The zero matrix has the rank \(0\), and a matrix of rank one is \(pq^{\mathsf t}\) for exactly one pair of nonzero vectors \(p,q\in\mathbb F^m\). So \(1+(2^m-1)^2\) of the \(2^{m^2}\) matrices have a rank of at most one. The matrix \(C\) is a part of \(\operatorname{Gram}_F(Y)\); if the latter has a rank of at most one, so has \(C\). Together:
\[
\begin{aligned}
&\mathbb P\bigl(\operatorname{rank}\operatorname{Gram}_F(S)\le1\bigr)\\
&\quad\le(2^m-1)\,2^{-t}\\
&\qquad+\bigl[1+(2^m-1)^2\bigr]\,2^{-m^2}.
\end{aligned}
\]
If \(\operatorname{rank}F>s\), then \(t>s-2r'\), and \((2^m-1)2^{-t}<2^{\,m-(s-2r')}\). \(\blacksquare\)

The form \(F\) is fixed in this lemma. No symmetry of \(F\) is used, and no property of a procedure that may have chosen it.

## 5. Proof of Proposition 1.1

By Proposition 3.1 of the lesson on the heavy list, the forms agree on \(H_i'\times H_i'\) with a probability of at least \(\gamma\). Suppose that the event \(\mathcal E\) that they agree and \(\operatorname{rank}F_L>s\) has \(\mathbb P_i(\mathcal E)\ge\gamma/2\). Take functions \(f_L,f_R\) as in Lemma 2.1 for \(\mathcal E\), and the table \(f\) of Section 3 for them. Then \(h\ge\gamma/2\), and by Proposition 3.3
\[
\begin{aligned}
&\mathbb P_i^0\bigl(f(S)=f(S+a\otimes l)\ne\bot\bigr)\\
&\quad\ge\frac{\gamma^2}4-\frac{\gamma^2}{64}-\frac{\gamma^2}{64}=\frac{7\gamma^2}{32}>\eta' .
\end{aligned}
\]
So there is a value of \(\mathcal C^0\) for which the conditional probability of this event is at least \(\eta'\). Fix it. Given this value, \(S\), \(a\), \(l\) are uniform and independent by Proposition 3.3, so \((S,S+a\otimes l)\) is the step of the lesson on matrices and slices on \(K_i\otimes H_i\), and \(S\mapsto f(S)\) is a partial table whose values are bilinear forms on \(H_i\).

By the inverse theorem for \(\eta'\), with \(\ell_i\ge\ell_0'\), there are one form \(F\) and a slice with at most \(r'\) row combinations and at most \(r'\) column values such that \(f(S)=F\) for at least the fraction \(\alpha'\) of the arrays \(S\) of the slice. By Proposition 3.3, \(\operatorname{rank}F>s\), and at every \(S\) with \(f(S)=F\) the form \(F\) is admissible at \(S\); in particular \(\operatorname{rank}\operatorname{Gram}_F(S)\le1\). So this rank condition holds on at least the fraction \(\alpha'\) of the slice.

By Lemma 4.1 for this fixed \(F\), with \(\ell_i\ge2m+r'\), and by the choice of \(m\) and \(s\), the rank condition holds on less than \(\alpha'/2+\alpha'/2=\alpha'\) of the slice. This is a contradiction. So \(\mathbb P_i(\mathcal E)<\gamma/2\), and the agreement with \(\operatorname{rank}F_L\le s\) has a probability of more than \(\gamma-\gamma/2\). \(\blacksquare\)

The functions \(f_L,f_R\) were used only to refute the assumption. The proposition is about the decoders of the lesson on the heavy list, with their random choices.

The proposition gives, with a probability of at least \(\gamma/2\), a left form \(F_L(x,y)=z(xy)\) with \(z(1)=1\) and a rank of at most \(s\) on \(H_i\) that agrees with the right form on the projected space. [OpenAI-G] derives from such forms short lists of answers at the leaves, and from these a strategy for many independent base questions. That step is not part of this lesson.

## 6. Exercises

**6.1.** List the \(2\times2\) matrices over \(\mathbb F\) of rank at most one, and compare with the count \(1+(2^m-1)^2\). Compute \([1+(2^m-1)^2]\,2^{-m^2}\) for \(m=1,2,3,4\).

**6.2.** Let \(H=\mathbb F^2\) with the form \(F(x,y)=x_1y_1+x_2y_2\), and \(\ell=2\). For which arrays \(S=(S_1,S_2)\) does \(\operatorname{Gram}_F(S)\) have a rank of at most one? Count them among the 16 arrays.

**6.3.** Prove the identity \(\operatorname{Gram}_F(TS)=T\operatorname{Gram}_F(S)T^{\mathsf t}\).

**6.4.** In Lemma 3.1, why are \(S\) and \(S'\) independent given \((\mathcal C,a,q)\), although \(S'\) is computed from \(S\)?

**6.5.** Let \(\alpha'=\tfrac1{10}\) and \(r'=2\). Find the smallest \(m\) and then the smallest \(s\) that satisfy the two conditions of Proposition 1.1.

## 7. Solutions

**6.1.** The zero matrix, and the nine matrices \(pq^{\mathsf t}\) with \(p,q\in\{(1,0),(0,1),(1,1)\}\): ten of the sixteen. The values are \(2\cdot\tfrac12=1\) for \(m=1\), \(\tfrac{10}{16}\) for \(m=2\), \(\tfrac{50}{512}\) for \(m=3\), and \(\tfrac{226}{65536}\) for \(m=4\).

**6.2.** The matrix has the entries \(F(S_u,S_v)\). Its determinant is the sum of \(F(S_1,S_1)F(S_2,S_2)\) and \(F(S_1,S_2)F(S_2,S_1)\). For \(x\in\mathbb F^2\), \(F(x,x)=x_1+x_2\). The rank is two exactly if the determinant is \(1\). If \(S_1=S_2\) or one row is \(0\), the determinant is \(0\). For two different nonzero rows: \(\{(1,0),(0,1)\}\) gives \(1\cdot1+0=1\); \(\{(1,0),(1,1)\}\) gives \(1\cdot0+1\cdot1=1\); \(\{(0,1),(1,1)\}\) gives \(1\). So the rank is two for the \(6\) ordered pairs of different nonzero rows, and at most one for the other \(10\) arrays.

**6.3.** The row \(u\) of \(TS\) is \(\sum_aT_{ua}S_a\). So \(F((TS)_u,(TS)_v)\) is the sum \(\sum_{a,b}T_{ua}F(S_a,S_b)T_{vb}\), which is the entry \((u,v)\) of the product.

**6.4.** Given \((\mathcal C,a,q)\), the array \(S\) is uniform among the arrays of the class \(q\), and \(S'=S+a\otimes l\) with \(l\) uniform and independent of \(S\). For every fixed \(S\), the array \(S'\) is then uniform among the arrays of the class; so its conditional law does not depend on \(S\).

**6.5.** The first condition asks for a value below \(\tfrac1{20}\): \(m=3\) gives \(\tfrac{50}{512}>\tfrac1{20}\), and \(m=4\) gives \(\tfrac{226}{65536}<\tfrac1{20}\). So \(m=4\). The second condition is \(2^{4-(s-4)}<\tfrac1{20}\), that is \(2^{s-8}>20\), so \(s=13\).

## References

- [OpenAI-G] OpenAI, *Perfect completeness for 2-to-1 games*, OpenAI Math Release preprint, 23 September 2026, Section 6. https://github.com/openai/math/tree/main/preprints/Perfect-completeness-for-2-to-1-games-September-23-2026
