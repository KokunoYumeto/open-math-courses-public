# An intersection inequality for subspaces

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(U_1,\ldots,U_m\) and \(V_1,\ldots,V_m\) be subspaces of an \(N\)-dimensional real vector space such that each \(U_i\) meets its partner \(V_i\) only in \(0\). How large can the intersections \(U_i\cap V_j\) of the other pairs be in total? Splitting the space into two halves and the indices into two groups shows that the total can reach \(\lfloor m^2/4\rfloor N\). This lesson proves that it cannot be larger [OpenAI-B, Lemma 2.1], by interpolating vectors with polynomials and counting the zeros of a determinant. Applied to graphs of linear maps, the inequality becomes a lower bound for the ranks of differences \(X_i-Y_j\) of matrices [OpenAI-B, Corollary 2.3], which is the algebraic heart of [The Zarankiewicz formula](the-zarankiewicz-formula.md). Nothing in this lesson refers to drawings.

- Polynomial vectors and matrices (Section 1).
- The inequality (Section 2).
- Ranks of differences (Section 3).

## 1. Polynomial vectors and matrices

Let \(W\) be a real vector space of dimension \(N\) with a fixed basis, and \(Z\subseteq W\) a subspace. Write \(Z[\xi]\) for the polynomials in one variable \(\xi\) with coefficients in \(Z\), that is, expressions \(P=\sum_kz_k\xi^k\) with \(z_k\in Z\); for a real number \(t\), \(P(t)=\sum_kz_kt^k\in Z\). In coordinates, \(P\) is a column of \(N\) polynomials, and finitely many such columns form a *polynomial matrix* \(M(\xi)\), whose value \(M(t)\) at \(t\) is a real matrix. Its minors are polynomials in \(\xi\).

**Lemma 1.1** (rank at special points). Let \(M(\xi)\) be a polynomial matrix and \(r\ge0\). If \(\operatorname{rank}M(t)\le r\) for infinitely many real \(t\), then \(\operatorname{rank}M(t)\le r\) for every real \(t\).

*Proof.* A real matrix has rank at most \(r\) exactly when all its minors of size \(r+1\) vanish. Indeed, if the rank is at least \(r+1\), choose \(r+1\) linearly independent columns; the submatrix they form has column rank \(r+1\), hence row rank \(r+1\) [Hefferon, Theorem Two.III.3.11], so it has \(r+1\) independent rows, and the square submatrix on these rows and columns is nonsingular, with nonzero determinant [Hefferon, Lemma Four.I.2.4]. Conversely, a nonzero minor of size \(r+1\) gives \(r+1\) independent columns. Each minor of size \(r+1\) of \(M(\xi)\) is a polynomial in \(\xi\); vanishing at infinitely many \(t\), it is zero. \(\square\)

**Lemma 1.2** (rank loss and multiple roots). Let \(M(\xi)\) be a square polynomial matrix of size \(k\), \(t_0\) a real number and \(q\ge0\). If \(\operatorname{rank}M(t_0)\le k-q\), then \((\xi-t_0)^q\) divides \(\det M(\xi)\).

*Proof.* The kernel of \(M(t_0)\) has dimension at least \(q\), by rank plus nullity [Hefferon, Theorem Three.II.2.14]; choose a basis of \(\mathbb R^k\) whose last \(q\) vectors lie in it, and let \(C\) be the invertible real matrix with these columns. The last \(q\) columns of \(M(\xi)C\) vanish at \(\xi=t_0\), so each of their entries is divisible by \(\xi-t_0\). Taking the factor \(\xi-t_0\) out of each of these columns, by multilinearity in the columns [Hefferon, Corollary Four.I.3.16], shows that \((\xi-t_0)^q\) divides \(\det\bigl(M(\xi)C\bigr)=\det M(\xi)\det C\) [Hefferon, Theorem Four.II.1.5], and \(\det C\ne0\). Here the determinant of a polynomial matrix is given by the permutation expansion [Hefferon, Definition Four.I.3.12], a polynomial in \(\xi\), and the two determinant rules hold for it because they are polynomial identities in the entries. \(\square\)

If \((\xi-t_1)^{q_1},\ldots,(\xi-t_m)^{q_m}\) all divide a nonzero polynomial, with \(t_1,\ldots,t_m\) distinct, then so does their product, and the degree of the polynomial is at least \(q_1+\cdots+q_m\): each \(t_j\) is a root of multiplicity at least \(q_j\), and the multiplicities of the distinct roots of a nonzero polynomial add up to at most its degree.

## 2. The inequality

**Theorem 2.1** (subspace intersection inequality; [OpenAI-B, Lemma 2.1]). Let \(W\) be a real vector space of dimension \(N\), let \(m\ge1\), and let \(U_1,\ldots,U_m,V_1,\ldots,V_m\) be subspaces of \(W\) with \(U_i\cap V_i=0\) for every \(i\). Then
\[
\sum_{i,j=1}^m\dim(U_i\cap V_j)\le\Bigl\lfloor\frac{m^2}4\Bigr\rfloor N .
\]

*Proof.* *Interpolation spaces.* Choose distinct real numbers \(t_1,\ldots,t_m\), the *nodes*. For a subspace \(Z\subseteq W\) and an integer \(h\ge0\) let
\[
\begin{gathered}
\mathcal P_h(Z)=\bigl\{P\in Z[\xi]:\deg P\le h,\\
P(t_i)\in U_i\text{ for }i=1,\ldots,m\bigr\},
\end{gathered}
\]
and \(\mathcal P_{-1}(Z)=0\). These are nested subspaces, \(\mathcal P_{h-1}(Z)\subseteq\mathcal P_h(Z)\). Put
\[
\begin{gathered}
k_h(Z)=\dim\mathcal P_h(Z)-\dim\mathcal P_{h-1}(Z),\\
E_h(Z;t)=\{P(t):P\in\mathcal P_h(Z)\}\subseteq Z .
\end{gathered}
\]

*(a) Evaluation away from the nodes.* Let \(t\) be a real number other than the nodes. If \(P\in\mathcal P_h(Z)\) and \(P(t)=0\), then \(P=(\xi-t)Q\) with \(Q\in Z[\xi]\) of degree at most \(h-1\), dividing coordinate by coordinate, and \(Q(t_i)=P(t_i)/(t_i-t)\in U_i\); so \(Q\in\mathcal P_{h-1}(Z)\). Conversely \((\xi-t)\mathcal P_{h-1}(Z)\subseteq\mathcal P_h(Z)\). Hence the kernel of \(P\mapsto P(t)\) on \(\mathcal P_h(Z)\) is \((\xi-t)\mathcal P_{h-1}(Z)\), which has the dimension of \(\mathcal P_{h-1}(Z)\), and for every \(t\) that is not a node
\[
\dim E_h(Z;t)=k_h(Z).\tag{2.1}
\]

*(b) Evaluation at all nodes.* The map \(P\mapsto(P(t_1),\ldots,P(t_m))\) is a bijection from \(\mathcal P_{m-1}(Z)\) onto \(\bigoplus_i(U_i\cap Z)\): it lands there, since the coefficients lie in \(Z\); it is injective, since a polynomial of degree at most \(m-1\) vanishing at \(m\) nodes is zero, coordinate by coordinate; and it is surjective, since for \(z_i\in U_i\cap Z\) the polynomial \(\sum_iL_i(\xi)z_i\) with the Lagrange polynomials \(L_i\) of Lemma 1.1 of [Interpolation](interpolation.md) has coefficients in \(Z\) and value \(z_i\) at \(t_i\). Summing the definition of \(k_h\),
\[
\begin{gathered}
\sum_{h=0}^{m-1}k_h(Z)\\
=\dim\mathcal P_{m-1}(Z)\\
=\sum_{i=1}^m\dim(U_i\cap Z).
\end{gathered}\tag{2.2}
\]

*(c) A filtration of \(W\).* Fix a real number \(t_*\) other than the nodes. As \(\mathcal P_{h-1}(W)\subseteq\mathcal P_h(W)\), the spaces \(E_h(W;t_*)\) increase with \(h\), and by (2.1) the numbers \(\ell_h=k_h(W)-k_{h-1}(W)\), with \(k_{-1}=0\), are nonnegative. Choose polynomials stage by stage: at stage \(h=0,1,\ldots,m-1\), choose \(\ell_h\) elements of \(\mathcal P_h(W)\) whose values at \(t_*\) extend the values chosen before to a basis of \(E_h(W;t_*)\). Let \(M_h(\xi)\) be the polynomial matrix whose columns are all elements chosen up to stage \(h\); it has \(r_h=k_h(W)\) columns, linearly independent at \(t_*\), each in \(\mathcal P_h(W)\), and a column chosen at stage \(e\) has degree at most \(e\).

Since the columns of \(M_h(t_*)\) are independent, \(M_h(t_*)\) has \(r_h\) linearly independent rows [Hefferon, Theorem Two.III.3.11]; let \(\Delta_h(\xi)\) be the determinant of the square submatrix of \(M_h(\xi)\) formed by these rows (with \(\Delta_h=1\) if \(r_h=0\)). Then \(\Delta_h(t_*)\ne0\), so \(\Delta_h\) is a nonzero polynomial, and in the permutation expansion each term is a product of one entry from each column, so
\[
\deg\Delta_h\le\sum_{e=0}^he\,\ell_e .\tag{2.3}
\]

*(d) Rank loss at the nodes.* Fix \(j\) and let \(\pi_j:W\to W/V_j\) be the quotient map. We claim
\[
\begin{gathered}
\dim E_h(W;t_j)\\
\le k_h(W)-k_h(V_j).
\end{gathered}\tag{2.4}
\]
Let \(t\) be a real number other than the nodes. The space \(E_h(W;t)\) has dimension \(k_h(W)\) by (2.1) and contains \(E_h(V_j;t)\), of dimension \(k_h(V_j)\), which lies in \(V_j=\ker\pi_j\); so \(\dim\pi_j(E_h(W;t))\le k_h(W)-k_h(V_j)\). Take a basis of \(\mathcal P_h(W)\) and the polynomial matrix whose columns are the images of its elements under \(\pi_j\), in coordinates of \(W/V_j\); its value at \(t\) spans \(\pi_j(E_h(W;t))\). By Lemma 1.1 its rank at \(t_j\) is also at most \(k_h(W)-k_h(V_j)\). But \(E_h(W;t_j)\subseteq U_j\), by the definition of \(\mathcal P_h\), and \(\pi_j\) is injective on \(U_j\) because \(U_j\cap V_j=0\); so \(\dim E_h(W;t_j)=\dim\pi_j(E_h(W;t_j))\), which proves (2.4).

The columns of \(M_h(t_j)\) lie in \(E_h(W;t_j)\), so \(M_h(t_j)\) and its square submatrix defining \(\Delta_h\) have rank at most \(r_h-k_h(V_j)\). By Lemma 1.2, \((\xi-t_j)^{k_h(V_j)}\) divides \(\Delta_h\). This holds for every \(j\), and the nodes are distinct, so by the remark after Lemma 1.2 and (2.3),
\[
\begin{gathered}
\sum_{j=1}^mk_h(V_j)\le\deg\Delta_h\\
\le\sum_{e=0}^he\,\ell_e .
\end{gathered}\tag{2.5}
\]

*(e) Summation.* Add (2.5) over \(h=0,\ldots,m-1\). By (2.2) with \(Z=V_j\) the left side becomes \(\sum_j\sum_i\dim(U_i\cap V_j)\). On the right, \(\ell_e\) occurs for the \(m-e\) values \(h=e,\ldots,m-1\). Hence
\[
\begin{aligned}
\sum_{i,j=1}^m\dim(U_i\cap V_j)&\le\sum_{e=0}^{m-1}e(m-e)\,\ell_e\\
&\le\Bigl\lfloor\frac{m^2}4\Bigr\rfloor\sum_{e=0}^{m-1}\ell_e\\
&\le\Bigl\lfloor\frac{m^2}4\Bigr\rfloor N,
\end{aligned}
\]
because \(e(m-e)\le m^2/4\) for every integer \(e\), so \(e(m-e)\le\lfloor m^2/4\rfloor\), and \(\sum_{e=0}^{m-1}\ell_e=k_{m-1}(W)\), which equals \(\dim E_{m-1}(W;t_*)\le N\). \(\square\)

**Remark 2.2** (sharpness; [OpenAI-B, Remark 2.2]). Write \(W=P\oplus Q\) with \(\dim P+\dim Q=N\), split the indices into a group of \(\lfloor m/2\rfloor\) and a group of \(\lceil m/2\rceil\), and put \((U_i,V_i)=(P,Q)\) in the first group and \((U_i,V_i)=(Q,P)\) in the second. Then \(U_i\cap V_i=0\), pairs within a group contribute \(0\), and each pair from different groups contributes \(\dim P\) or \(\dim Q\); the total is \(\lfloor m/2\rfloor\lceil m/2\rceil N=\lfloor m^2/4\rfloor N\).

## 3. Ranks of differences

**Corollary 3.1** (ranks of differences; [OpenAI-B, Corollary 2.3]). Let \(X_1,\ldots,X_m,Y_1,\ldots,Y_m\) be real \(d\times d\) matrices such that \(X_i-Y_i\) is invertible for every \(i\). Then
\[
\begin{gathered}
\sum_{i\ne j}\operatorname{rank}(X_i-Y_j)\ge2\,d_m\,d,\\
d_m=\Bigl\lfloor\frac m2\Bigr\rfloor\Bigl\lfloor\frac{m-1}2\Bigr\rfloor,
\end{gathered}
\]
the sum over the ordered pairs of distinct indices.

*Proof.* In \(W=\mathbb R^d\oplus\mathbb R^d\), of dimension \(N=2d\), let \(U_i=\{(x,X_ix)\}\) and \(V_j=\{(x,Y_jx)\}\) be the graphs of the two matrices. The map \(x\mapsto(x,X_ix)\) is injective and carries \(\ker(X_i-Y_j)\) onto \(U_i\cap V_j\), so
\[
\dim(U_i\cap V_j)=d-\operatorname{rank}(X_i-Y_j),
\]
and in particular \(U_i\cap V_i=0\). Theorem 2.1 gives \(\sum_{i,j}\bigl(d-\operatorname{rank}(X_i-Y_j)\bigr)\le2d\lfloor m^2/4\rfloor\). The \(m\) diagonal terms have rank \(d\), so
\[
\begin{gathered}
\sum_{i\ne j}\operatorname{rank}(X_i-Y_j)\\
\ge\Bigl(m^2-m-2\Bigl\lfloor\frac{m^2}4\Bigr\rfloor\Bigr)d ,
\end{gathered}
\]
and \(m^2-m-2\lfloor m^2/4\rfloor\) equals \(4r^2-2r-2r^2=2r(r-1)\) for \(m=2r\) and \(4r^2+2r-2(r^2+r)=2r^2\) for \(m=2r+1\), which is \(2d_m\) in both cases. \(\square\)

For \(m\le2\) the bound is \(0\); for \(m=3\) it says that the six off-diagonal differences have total rank at least \(2d\).

## 4. Exercises

**4.1.** Prove Theorem 2.1 for \(m=2\) directly: if \(U_1\cap V_1=0\) and \(U_2\cap V_2=0\), then \(\dim(U_1\cap V_2)+\dim(U_2\cap V_1)\le N\). (Show that the two intersections meet only in \(0\).)

**4.2.** Let \(m=3\) and \(d=1\): \(X_i,Y_i\) are numbers with \(X_i\ne Y_i\). Show directly that at least two of the six differences \(X_i-Y_j\), \(i\ne j\), are nonzero.

**4.3.** Give an example of real numbers \(X_1,X_2,X_3,Y_1,Y_2,Y_3\) with \(X_i\ne Y_i\) for which exactly two of the six off-diagonal differences are nonzero, so Corollary 3.1 is sharp for \(m=3\), \(d=1\).

## 5. Solutions

**4.1.** A vector in \((U_1\cap V_2)\cap(U_2\cap V_1)\) lies in \(U_1\cap V_1=0\). Two subspaces meeting only in \(0\) have dimensions adding up to at most \(N\). Here \(\lfloor4/4\rfloor=1\).

**4.2.** Suppose at most one off-diagonal difference is nonzero. Renumbering the indices (the same permutation for the \(X\) and the \(Y\)), we may assume that all except possibly \(X_1-Y_2\) vanish. Then \(X_1=Y_3=X_2=Y_1\), using \(X_1-Y_3=0\), \(X_2-Y_3=0\) and \(X_2-Y_1=0\); this contradicts \(X_1\ne Y_1\).

**4.3.** Take \(X_1=X_2=0\), \(Y_1=Y_2=1\), and \(X_3=1\), \(Y_3=0\). Then \(X_1-Y_3=X_2-Y_3=0\), \(X_3-Y_1=X_3-Y_2=0\), and the nonzero ones are \(X_1-Y_2=-1\) and \(X_2-Y_1=-1\).

## References

- [Hefferon] J. Hefferon, *Linear Algebra*, fourth edition, 2020, Theorem Two.III.3.11, Theorem Three.II.2.14, Lemma Four.I.2.4, Definition Four.I.3.12, Corollary Four.I.3.16 and Theorem Four.II.1.5; the text of the core course [Linear Algebra](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-B40), on the author's page. https://jheffero.w3.uvm.edu/linearalgebra/
- [OpenAI-B] OpenAI, *The crossing number of complete bipartite graphs*, OpenAI Math Release preprint, 23 September 2026, Section 2, Lemma 2.1, Remark 2.2 and Corollary 2.3. https://github.com/openai/math/tree/main/preprints/The-crossing-number-of-complete-bipartite-graphs-September-23-2026
