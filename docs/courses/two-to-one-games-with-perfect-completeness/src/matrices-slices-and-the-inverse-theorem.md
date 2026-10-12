# Matrices, slices and the inverse theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The analysis of the reduction of [OpenAI-G] looks at a table: a function on matrices over the field with two elements. If the table often keeps its value when a random matrix of rank one is added to the argument, then one of its values fills a positive fraction of a *slice*, a set of matrices given by a bounded number of prescribed row combinations and prescribed column values. This lesson proves this inverse theorem from a theorem on Grassmann graphs, which is stated as a hypothesis. The bounds do not depend on the number of columns or on the number of values of the table; the later steps need exactly this.

- Slices, the rank-one step, and the hypothesis (GE) on Grassmann graphs (Section 1).
- Sets of matrices that are often preserved by the step (Lemma 2.1).
- Removing dummy columns (Lemma 3.1).
- The inverse theorem for partial tables (Theorem 4.1) and its form with random row advice (Lemma 4.2).

The lesson follows [OpenAI-G, Sections 2.2 and 2.3]; according to [OpenAI-G], the passage from Grassmann graphs to matrices follows B. Barak, P. Kothari and D. Steurer. The lesson uses linear algebra over a finite field. It does not use the first lesson of the course.

## 1. Slices and the hypothesis

Let \(\mathbb F\) be the field with two elements. All vector spaces are finite-dimensional over \(\mathbb F\), and "uniform" means the uniform law on a finite set. Let \(K=\mathbb F^\ell\) and let \(H\) be a vector space. A *matrix* is a linear map \(M:H^*\to K\); the set of matrices is written \(K\otimes H\). For \(H=\mathbb F^m\) it is an \(\ell\times m\) matrix: it has \(\ell\) rows in \(H\), and for \(q\in H^*\) the vector \(Mq\in K\) is the combination of its columns with the coefficients \(q\). For a linear map \(A:K\to\mathbb F^k\), the matrix \(AM\) consists of \(k\) combinations of the rows of \(M\).

**Definition.** A *slice* is a nonempty set of the form
\[
\bigl\{M:\ AM=U,\ Mq_b=t_b\ (1\le b\le c)\bigr\},
\]
with a linear map \(A:K\to\mathbb F^k\), a matrix \(U\) with \(k\) rows, \(q_b\in H^*\) and \(t_b\in K\). It has *\(k\) row combinations and \(c\) column values*. A slice without column values is a *row fibre*. No independence of the equations is required.

For \(a\in K\) and \(h\in H\) let \(ah\) be the matrix \(q\mapsto q(h)\,a\); for \(H=\mathbb F^m\) it is \(ah^{\mathsf t}\). The *step* replaces \(M\) by \(M+ah\), where \(M\) is uniform, \(a\) is uniform in \(K\setminus\{0\}\), \(h\) is uniform in \(H\), and the three are independent. Then \(M+ah\) is uniform again.

The *Grassmann graph* has as vertices the subspaces of the dimension \(\ell\) of \(\mathbb F^N\); two different vertices are neighbours if their intersection has the dimension \(\ell-1\). The *retention* of a nonempty set \(S\) of vertices is the probability that a uniform neighbour of a uniform element of \(S\) lies in \(S\).

**Hypothesis (GE).** For every \(0<\zeta<1\) there are \(\alpha>0\) and integers \(r\ge1\), \(\ell_0\) such that for every \(\ell\ge\ell_0\) and every sufficiently large \(N\) the following holds. For every nonempty set \(S\) of vertices with retention at least \(\zeta\) there are subspaces \(A_0\subset B_0\) of \(\mathbb F^N\) with \(\dim A_0+\operatorname{codim}B_0\le r\) such that at least the fraction \(\alpha\) of the vertices \(L\) with \(A_0\subset L\subset B_0\) lies in \(S\).

According to [OpenAI-G], for sets of at most half of the vertices this is a theorem of S. Khot, D. Minzer and S. Safra (2018) on the expansion of Grassmann graphs; for a larger set one may take \(A_0=0\), \(B_0=\mathbb F^N\) and replace \(\alpha\) by \(\min\{\alpha,\tfrac12\}\). The theorem is not proved in this course. The numbers \(\alpha,r,\ell_0\) depend only on \(\zeta\); how large \(N\) must be may depend on \(\ell\).

## 2. Sets of matrices

**Lemma 2.1.** Assume (GE). For every \(0<\eta<1\) there are \(\alpha>0\) and integers \(r\ge1\), \(\ell_0\), depending only on \(\eta\), such that for every \(\ell\ge\ell_0\) and all sufficiently large \(m\) the following holds. Let \(S\) be a nonempty set of \(\ell\times m\) matrices such that, for \(M\) uniform in \(S\) and independent uniform \(a\in\mathbb F^\ell\setminus\{0\}\), \(h\in\mathbb F^m\),
\[
\mathbb P\bigl(M+ah^{\mathsf t}\in S\bigr)\ge\eta .
\]
Then there is a slice with at most \(r\) row combinations and at most \(r\) column values in which at least the fraction \(\alpha\) of the matrices lies in \(S\).

**Proof.** Let \(m\) be so large that \(2^{-m}\le\eta/2\). The event \(h=0\) has the probability \(2^{-m}\), so given \(h\ne0\) the probability in the assumption is at least \((\eta-2^{-m})/(1-2^{-m})\ge\eta/2\).

*The chart.* To a matrix \(M\) associate the subspace
\[
L_M=\bigl\{(x,M^{\mathsf t}x):\ x\in\mathbb F^\ell\bigr\}\subset\mathbb F^\ell\oplus\mathbb F^m ,
\]
of the dimension \(\ell\). The map \(M\mapsto L_M\) is one-to-one, and its image, the *chart*, consists of the subspaces of dimension \(\ell\) that the first projection maps onto \(\mathbb F^\ell\). A vector \((x,M^{\mathsf t}x)\) lies in \(L_{M'}\) exactly if \((M-M')^{\mathsf t}x=0\), so
\[
\dim(L_M\cap L_{M'})=\ell-\operatorname{rank}(M-M').
\]
Hence two vertices of the chart are neighbours exactly if the matrices differ by a matrix of rank one. Over \(\mathbb F\) a matrix of rank one is \(ah^{\mathsf t}\) for exactly one pair of nonzero vectors. So for a uniform pair of nonzero \(a,h\), the vertex \(L_{M+ah^{\mathsf t}}\) is a uniform neighbour of \(L_M\) inside the chart, and \(L_M\) has \((2^\ell-1)(2^m-1)\) neighbours in the chart.

*All neighbours.* Let \(N=\ell+m\). A neighbour \(L'\) of a vertex \(L\) is given by the hyperplane \(L\cap L'\) of \(L\), for which there are \(2^\ell-1\) choices, and by a line in the quotient of \(\mathbb F^N\) by this hyperplane, different from the image of \(L\); this quotient has the dimension \(m+1\), so there are \(2^{m+1}-2\) choices. So \(L\) has \(2(2^\ell-1)(2^m-1)\) neighbours, and exactly half of the neighbours of a vertex of the chart lie in the chart. Therefore the set \(\widetilde S\) of the \(L_M\), \(M\in S\), has a retention of at least \(\eta/4\) in the Grassmann graph.

*The interval.* Apply (GE) with \(\zeta=\eta/4\); this fixes \(\alpha,r,\ell_0\), and for \(\ell\ge\ell_0\) the hypothesis applies when \(m\) is large. It gives \(A_0\subset B_0\) such that \(\widetilde S\) contains at least the fraction \(\alpha\) of the vertices between them. Since \(\widetilde S\) lies in the chart, it contains at least the fraction \(\alpha\) of the vertices of the chart between \(A_0\) and \(B_0\), and there are such vertices.

*The slice.* Let \((d_b,s_b)\) be a basis of \(A_0\). Then \(A_0\subset L_M\) exactly if \(M^{\mathsf t}d_b=s_b\) for all \(b\): the combination of the rows of \(M\) with the coefficients \(d_b\) is prescribed. Let \((t_b,q_b)\) be a basis of the space of the vectors that are orthogonal to \(B_0\) for the standard product. Then \(L_M\subset B_0\) exactly if \(\langle t_b,x\rangle+\langle q_b,M^{\mathsf t}x\rangle=0\) for all \(x\) and \(b\), that is, \(Mq_b=t_b\). So the matrices \(M\) with \(A_0\subset L_M\subset B_0\) form a slice with \(\dim A_0\) row combinations and \(\operatorname{codim}B_0\) column values. \(\blacksquare\)

## 3. Dummy columns

Lemma 2.1 needs many columns. A table on matrices with few columns can be extended to more columns on which it does not depend. The next lemma describes what a slice of the larger space looks like in the original columns.

**Lemma 3.1.** Let \(H,D,K\) be vector spaces, and write a matrix on \(H\oplus D\) as a pair \((X,Y)\) of matrices on \(H\) and on \(D\). Let \(\widetilde{\mathcal S}\) be the set of the pairs \((X,Y)\) with
\[
\begin{gathered}
AX=U_H,\qquad AY=U_D,\\
Xq_b+Yd_b=t_b\quad(1\le b\le c),
\end{gathered}
\]
and let it be a slice, with \(A:K\to\mathbb F^k\), \(q_b\in H^*\), \(d_b\in D^*\). Then its image \(\mathcal S\) under \((X,Y)\mapsto X\) is a slice with the \(k\) row combinations \(AX=U_H\) and at most \(c\) column values, and every \(X\in\mathcal S\) has the same number of preimages in \(\widetilde{\mathcal S}\). So a uniform element of \(\widetilde{\mathcal S}\) is mapped to a uniform element of \(\mathcal S\).

**Proof.** For \(\lambda\in\mathbb F^c\) let \(q(\lambda)=\sum_b\lambda_bq_b\), \(d(\lambda)=\sum_b\lambda_bd_b\), \(t(\lambda)=\sum_b\lambda_bt_b\), and let \(W\) be the kernel of \(A\). We claim that \(\mathcal S\) is the set of the \(X\) with
\[
\begin{gathered}
AX=U_H,\\
Xq(\lambda)=t(\lambda)\ \text{ for all }\lambda\text{ with }d(\lambda)=0 .
\end{gathered}
\]
A basis of the space of these \(\lambda\) gives at most \(c\) column values.

If \((X,Y)\in\widetilde{\mathcal S}\) and \(d(\lambda)=0\), the combination of the column equations with the coefficients \(\lambda\) is \(Xq(\lambda)=t(\lambda)\). So the conditions are necessary.

Conversely fix \((X_*,Y_*)\in\widetilde{\mathcal S}\), and let \(X\) satisfy the conditions. Then \(A(X_*-X)=0\). On the image of \(d\) define
\[
L_0(d(\lambda))=(X_*-X)\,q(\lambda).
\]
This is well defined: if \(d(\lambda)=0\), then \(X_*q(\lambda)=t(\lambda)=Xq(\lambda)\). The values of \(L_0\) lie in \(W\). Extend \(L_0\) to a linear map \(L:D^*\to W\) and put \(Y=Y_*+L\). Then \(AY=AY_*=U_D\), and for every \(\lambda\)
\[
\begin{aligned}
&Xq(\lambda)+Yd(\lambda)\\
&\quad=Xq(\lambda)+Y_*d(\lambda)+(X_*-X)q(\lambda)\\
&\quad=X_*q(\lambda)+Y_*d(\lambda)=t(\lambda).
\end{aligned}
\]
So \((X,Y)\in\widetilde{\mathcal S}\). Every preimage of \(X\) arises in this way: for \((X,Y)\in\widetilde{\mathcal S}\) the map \(Y-Y_*\) has its values in \(W\), and the column equations for \((X,Y)\) and \((X_*,Y_*)\) show that it is \(L_0\) on the image of \(d\). The number of the extensions of \(L_0\) is \(2^{\dim W\cdot(\dim D-\operatorname{rank}d)}\), which does not depend on \(X\). \(\blacksquare\)

## 4. The inverse theorem

A *partial table* with a finite set \(\mathcal Y\) of values is a function \(f\) on \(K\otimes H\) with values in \(\mathcal Y\cup\{\bot\}\), where \(\bot\notin\mathcal Y\) means "not defined".

**Theorem 4.1 (inverse theorem).** Assume (GE). For every \(0<\eta<1\) there are \(\alpha>0\) and integers \(r\ge1\), \(\ell_0\), depending only on \(\eta\), such that for every \(\ell\ge\ell_0\), every vector space \(H\), every finite set \(\mathcal Y\) and every partial table \(f\) on \(K\otimes H\), \(K=\mathbb F^\ell\): if
\[
\mathbb P\bigl(f(M)=f(M+ah)\ne\bot\bigr)\ge\eta
\]
for the step of Section 1, then there are a value \(y\in\mathcal Y\) and a slice with at most \(r\) row combinations and at most \(r\) column values on which \(f=y\) for at least the fraction \(\alpha\) of the matrices.

**Proof.** Take \(\alpha,r,\ell_0\) from Lemma 2.1 for \(\eta\). Choose a space \(D\) such that \(\dim(H\oplus D)\) is as large as Lemma 2.1 requires for \(\ell\), and let \(\widetilde f(X,Y)=f(X)\). A uniform matrix on \(H\oplus D\) has a uniform part \(X\), and a uniform vector of \(H\oplus D\) has a uniform part in \(H\). So \(\widetilde f\) satisfies the assumption with the same \(\eta\).

For \(y\in\mathcal Y\) let \(S_y\) be the set where \(\widetilde f=y\), let \(\mu_y\) be the probability that a uniform matrix lies in \(S_y\), and \(\theta_y\) the probability that the step leads from a uniform element of \(S_y\) into \(S_y\). Then the probability that \(\widetilde f(\widetilde M)=\widetilde f(\widetilde M+a\widetilde h)\ne\bot\) is
\[
\sum_{y\in\mathcal Y}\mu_y\,\theta_y ,
\]
and \(\sum_y\mu_y\le1\). So some \(y\) has \(\theta_y\ge\eta\). In coordinates, Lemma 2.1 gives a slice of matrices on \(H\oplus D\) in which \(S_y\) has at least the fraction \(\alpha\). By Lemma 3.1 its image is a slice on \(H\) with no more equations of either kind, the uniform law is mapped to the uniform law, and \(\widetilde f\) depends only on the image. So \(f=y\) on at least the fraction \(\alpha\) of the image. \(\blacksquare\)

The average over the values costs nothing: the number of values of the table does not enter. The dummy columns make the theorem valid for every \(H\), even for \(H=0\).

**Lemma 4.2 (many good row fibres).** Assume (GE). Let \(0<\eta<1\), and let \(\alpha,r,\ell_0\) be the numbers of Theorem 4.1 for \(\eta/2\). Let \(\ell\ge\ell_0\), and let \(f\) be a partial table on \(K\otimes H\) with \(\mathbb P(f(M)=f(M+ah)\ne\bot)\ge\eta\). For a linear map \(A:K\to\mathbb F^r\), call a row fibre \(\{M:AM=U\}\) *good* if it contains a slice, given by at most \(r\) additional column values, on which \(f\) takes one value of \(\mathcal Y\) for at least the fraction \(\alpha\) of the matrices. Then:

1. the probability that a uniform \(M\) lies in a good row fibre for some \(A\) is at least \(\eta/4\);
2. for independent uniform \(A\) and \(M\), the row fibre of \(M\) for \(A\) is good with a probability of at least \(\tfrac\eta4\,2^{-r\ell}\);
3. inside a row fibre, a nonempty slice given by at most \(r\) column values has at least the fraction \(2^{-r\ell}\) of the matrices.

**Proof.** (1) Let \(T\) be the union of all good row fibres, for all \(A\), and suppose that it has less than the fraction \(\eta/4\) of all matrices. Let \(f_0\) be \(f\) outside \(T\) and \(\bot\) on \(T\). Since \(M\) and \(M+ah\) are both uniform, each of them lies in \(T\) with a probability of less than \(\eta/4\), and
\[
\begin{aligned}
&\mathbb P\bigl(f_0(M)=f_0(M+ah)\ne\bot\bigr)\\
&\quad>\eta-\frac\eta4-\frac\eta4=\frac\eta2 .
\end{aligned}
\]
By Theorem 4.1 for \(\eta/2\), some value of \(f_0\) fills at least the fraction \(\alpha\) of a slice with at most \(r\) row combinations and \(r\) column values. Add zero rows to its row map to get a map to \(\mathbb F^r\). Since \(f_0=f\) where \(f_0\) is defined, the row fibre of this slice is good for \(f\), so it lies in \(T\), where \(f_0\) is not defined. This contradicts \(\alpha>0\).

(2) There are \(2^{r\ell}\) maps \(A\). For every \(M\in T\) at least one of them gives a good row fibre through \(M\).

(3) On a row fibre, \(c\le r\) column values are at most \(r\ell\) linear equations over \(\mathbb F\); if they have a solution, the solutions are at least the fraction \(2^{-r\ell}\). \(\blacksquare\)

The lemma does not say that the row fibres of one given \(A\) are good. It says that a random \(A\), which the decoders of [OpenAI-G] use as advice, finds a good fibre with a probability that depends only on \(\eta\) and \(\ell\).

## 5. Exercises

**5.1.** Let \(\ell=m=1\), so \(N=2\). List the vertices of the Grassmann graph and of the chart, and check the two counts of neighbours in the proof of Lemma 2.1.

**5.2.** Show that over \(\mathbb F\) a matrix of rank one has exactly one factorization \(ah^{\mathsf t}\), and that there are \((2^\ell-1)(2^m-1)\) matrices of rank one of the size \(\ell\times m\).

**5.3.** Let \(f\) be a table (defined everywhere) that depends only on \(AM\) for a surjective linear map \(A:K\to\mathbb F^k\). Show that \(f(M)=f(M+ah)\) with a probability of at least \((2^{\ell-k}-1)/(2^\ell-1)\), and that every row fibre of \(A\) is a slice on which \(f\) is constant.

**5.4.** In Lemma 3.1 let \(H=0\). What is \(\mathcal S\), and how many elements has \(\widetilde{\mathcal S}\)?

## 6. Solutions

**5.1.** The vertices are the three lines of \(\mathbb F^2\), spanned by \((1,0)\), \((0,1)\), \((1,1)\). Any two meet in \(0\), so every vertex has \(2\) neighbours; the formula gives \((2^1-1)(2^2-2)=2\). The chart consists of the lines \(L_M\) for the \(1\times1\) matrices \(M=0\) and \(M=1\): the lines spanned by \((1,0)\) and \((1,1)\). Each has one neighbour in the chart, \((2^1-1)(2^1-1)=1\), half of its neighbours.

**5.2.** If \(ah^{\mathsf t}=a'h'^{\mathsf t}\ne0\), the column spaces give that \(a\) and \(a'\) span the same line, so \(a=a'\), the only nonzero multiple; then \(h=h'\). The count is the number of the pairs of nonzero vectors.

**5.3.** \(A(M+ah)=AM+(Aa)h\), so \(f\) keeps its value if \(Aa=0\). The kernel of \(A\) has \(2^{\ell-k}\) elements, so \(Aa=0\) for \(2^{\ell-k}-1\) of the \(2^\ell-1\) nonzero \(a\). A row fibre \(\{AM=U\}\) is nonempty because \(A\) is surjective, and \(f\) is constant on it.

**5.4.** There are no matrices on \(H=0\) except the zero matrix, so \(\mathcal S\) is one point. By the proof, \(\widetilde{\mathcal S}\) has \(2^{\dim W\,(\dim D-\operatorname{rank}d)}\) elements.

## References

- [OpenAI-G] OpenAI, *Perfect completeness for 2-to-1 games*, OpenAI Math Release preprint, 23 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Perfect-completeness-for-2-to-1-games-September-23-2026
