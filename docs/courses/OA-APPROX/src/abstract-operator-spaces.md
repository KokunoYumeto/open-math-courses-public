# From matrix norms to operators

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-checked relative to the stated prerequisites; not independently reviewed. New original text: public domain (CC0).*

A normed vector space remembers the size of a single vector. A subspace of bounded operators also remembers the size of every matrix of its vectors. These matrix norms interact with direct sums and scalar matrix multiplication. Ruan's theorem says that those two interactions are enough to recover an operator realization.

We will prove the theorem by constructing enough completely contractive maps to detect every matrix norm. The construction uses ordinary Hahn–Banach and finite-dimensional states. It does not assume that the vector space is complete or separable.

Prerequisites are elementary Hilbert-space operator theory, Hahn–Banach separation, and the definitions in [Completely bounded extension and factorization](completely-bounded-extension.md). The free norm-detecting method and the locally completed state-selection argument are identified below. Inner products are linear in the second variable.

## 1. The two axioms

Let \(V\) be a complex vector space. For each \(n\ge1\), suppose \(M_n(V)\) has a norm \(\|\cdot\|_n\). An **abstract operator space** satisfies:

1. For \(x\in M_m(V)\), \(y\in M_n(V)\),
   \[
   \|x\oplus y\|_{m+n}=\max\{\|x\|_m,\|y\|_n\}.
   \]
2. For \(x\in M_k(V)\), \(a\in M_{n,k}(\mathbb C)\), \(b\in M_{k,n}(\mathbb C)\),
   \[
   \|axb\|_n\le\|a\|\,\|x\|_k\,\|b\|.
   \]

The scalar matrix norms here are operator norms between Euclidean spaces. Products \(axb\) use linear combinations of the entries of \(x\), so require no multiplication on \(V\).

If \(V\subset B(H)\), its inherited matrix norms satisfy both axioms. The first follows from the norm of a block diagonal operator, and the second from composition with the operators \(a\otimes1_H\) and \(b\otimes1_H\).

Scalar unitary multiplication preserves the abstract norms: the second axiom gives one inequality, and multiplication by the inverse unitaries gives the reverse inequality. In particular, simultaneous rearrangement of matrix coordinates preserves norms.

## 2. A functional can be bounded by two states

Fix \(n\) and a linear functional \(f\) on \(M_n(V)\) with \(\|f\|\le1\). The following lemma is the main step.

**Lemma 2.1.** There are states \(p,q\) on \(M_n(\mathbb C)\) such that, for every \(k\), every \(x\in M_k(V)\), and all scalar \(a\in M_{n,k}\), \(b\in M_{k,n}\),
\[
|f(axb)|\le\|x\|_k\,p(aa^*)^{1/2}q(b^*b)^{1/2}.
\]

**Proof.** First require, for every triple with \(\|x\|_k\le1\),
\[
\operatorname{Re} f(axb)
\le\tfrac12\{p(aa^*)+q(b^*b)\}.                 \tag{1}
\]
The pairs of states form a compact convex set. Each requirement is a closed half-space in that set. We prove that every finite family of requirements has a common pair of states.

Take triples \((a_i,x_i,b_i)\), \(1\le i\le r\), with possibly different middle sizes and \(\|x_i\|\le1\). If their requirements had no common solution, separate the compact convex set of vectors
\[
\left(\tfrac12\{p(a_i a_i^*)+q(b_i^*b_i)\}
      -\operatorname{Re}f(a_i x_i b_i)\right)_{i=1}^r
\]
from the nonnegative orthant in \(\mathbb R^r\). A separating linear functional must have nonnegative coefficients \(\lambda_i\), since the orthant is unbounded in each positive coordinate. Its separation would give
\[
\sup_{p,q}\sum_i\lambda_i
\left(\tfrac12\{p(a_i a_i^*)+q(b_i^*b_i)\}
      -\operatorname{Re}f(a_i x_i b_i)\right)<0. \tag{2}
\]

But concatenate the matrices as
\[
A=(\sqrt{\lambda_1}a_1\ \cdots\ \sqrt{\lambda_r}a_r),\qquad
B=\begin{pmatrix}\sqrt{\lambda_1}b_1\\\vdots\\\sqrt{\lambda_r}b_r\end{pmatrix},
\qquad X=x_1\oplus\cdots\oplus x_r.
\]
The axioms give \(\|X\|\le1\) and
\[
\begin{aligned}
\left|\sum_i\lambda_i f(a_i x_i b_i)\right|
&=|f(AXB)|\\
&\le\|A\|\|B\|\\
&=\left\|\sum_i\lambda_i a_i a_i^*\right\|^{1/2}
  \left\|\sum_i\lambda_i b_i^*b_i\right\|^{1/2}\\
&\le\tfrac12\left(
  \left\|\sum_i\lambda_i a_i a_i^*\right\|
 +\left\|\sum_i\lambda_i b_i^*b_i\right\|\right).
\end{aligned}
\]
The last expression is exactly the supremum of the state part in (2): a positive scalar matrix has a state attaining its norm, and \(p\) and \(q\) can be chosen independently. This contradicts (2).

Compactness now gives one pair \(p,q\) satisfying all requirements (1). Replacing \(x\) by a scalar phase times \(x\) replaces its real part by its absolute value. Replacing \(a,b\) by \(ta,t^{-1}b\), for \(t>0\), gives
\[
|f(axb)|\le\tfrac12\{t^2p(aa^*)+t^{-2}q(b^*b)\}
\quad(\|x\|\le1).
\]
The infimum over \(t\) is the geometric mean in the statement. If one of the two state values is zero, taking \(t\) to zero or infinity gives zero. Finally rescale a nonzero \(x\) by its norm. The zero case is immediate. \(\square\)

The same two states work at every middle matrix size. This uniformity is what will make the operator map completely contractive.

## 3. Turn the bound into a coefficient operator

For the states in Lemma 2.1, make Hilbert spaces from the scalar matrices. Let \(H_p\) be \(M_n\) modulo the null space of
\[
\|a\|_p^2=p(aa^*),
\]
and let \(H_q\) be the analogous quotient for
\(\|b\|_q^2=q(b^*b)\).
The inner products are
\(\langle a,c\rangle_p=p(ca^*)\) and
\(\langle b,d\rangle_q=q(b^*d)\).
They are positive semidefinite before quotienting and positive definite afterward. These spaces are finite-dimensional. Write \(\overline{H_p}\) for the conjugate Hilbert space; the correspondence \(a\mapsto\bar a\) is conjugate linear.

For \(v\in V\), let \(D_n(v)\) be the diagonal matrix with \(v\) repeated \(n\) times. The direct-sum axiom gives \(\|D_n(v)\|_n=\|v\|_1\). Define an operator
\[
\theta_f(v):H_q\to\overline{H_p}
\]
by the coefficient identity
\[
\langle\bar a,\theta_f(v)b\rangle=f(aD_n(v)b).                 \tag{3}
\]
The right side is linear in \(a\), \(v\), and \(b\), as required because the first Hilbert-space entry is \(\bar a\). Lemma 2.1 bounds it by
\(\|v\|\|a\|_p\|b\|_q\).
It therefore vanishes on the null spaces and defines a unique bounded operator. The dependence on \(v\) is linear.

**Lemma 3.1.** The map \(\theta_f\) is completely contractive.

**Proof.** Let \(Y=[v_{ij}]\in M_m(V)\), and take matrices \(a_1,\ldots,a_m\), \(b_1,\ldots,b_m\in M_n\). The relevant coefficient of \(\theta_f^{(m)}(Y)\) is
\[
\sum_{i,j}f(a_iD_n(v_{ij})b_j)=f(AXB),
\]
where \(A=(a_1\ \cdots\ a_m)\), \(B=(b_1\ \cdots\ b_m)^{\mathsf T}\), and \(X=[D_n(v_{ij})]\in M_{mn}(V)\).
After a scalar permutation of coordinates, \(X\) is a direct sum of \(n\) copies of \(Y\). Thus \(\|X\|=\|Y\|_m\). Lemma 2.1 gives
\[
|f(AXB)|\le\|Y\|_m
\left(\sum_i p(a_i a_i^*)\right)^{1/2}
\left(\sum_j q(b_j^*b_j)\right)^{1/2}.
\]
These two sums are the squared norms of the left and right Hilbert-space tuples. Taking their unit-ball supremum proves
\(\|\theta_f^{(m)}(Y)\|\le\|Y\|_m\). \(\square\)

## 4. Detect every matrix norm

**Theorem 4.1 (Ruan representation).** Every abstract operator space \(V\) has a linear complete isometry into \(B(H)\) for some Hilbert space \(H\). If \(V\) is complete, its image is a closed subspace.

**Proof.** Fix nonzero \(Y=[v_{ij}]\in M_n(V)\). Hahn–Banach gives a functional \(f\) on \(M_n(V)\) with
\(\|f\|=1\) and \(f(Y)=\|Y\|_n\).
Use Lemmas 2.1 and 3.1 to construct \(\theta_f\).

Take \(a_i=E_{i1}\) and \(b_j=E_{1j}\). Their tuple norms are both one, since
\[
\sum_i p(a_i a_i^*)=p(1_n)=1,
\qquad
\sum_j q(b_j^*b_j)=q(1_n)=1.
\]
Moreover,
\[
\sum_{i,j}a_iD_n(v_{ij})b_j=Y.
\]
Equation (3) shows that a coefficient of \(\theta_f^{(n)}(Y)\), between these unit tuples, equals \(f(Y)=\|Y\|_n\). Complete contractivity gives the other inequality. Hence
\(\|\theta_f^{(n)}(Y)\|=\|Y\|_n\).

Embed the rectangular operator \(\theta_f(v):H_q\to\overline{H_p}\) as the upper-right corner in
\(B(\overline{H_p}\oplus H_q)\), with all other corners zero. This preserves its norm at every size. For each nonzero matrix \(Y\) at each size, choose such a map that detects its norm. Form the Hilbert direct sum of their spaces and the block diagonal map
\[
\Theta(v)=\bigoplus_Y\theta_Y(v).
\]
Each coordinate is a complete contraction, so this defines a bounded operator of norm at most \(\|v\|\); the same is true at every matrix size. For any \(Y\), its own coordinate gives the reverse inequality at that size. Thus \(\Theta\) is a complete isometry.

The zero vector space has the trivial realization. In the nonzero case the index family is a set: it is contained in the union of the sets \(M_n(V)\), \(n\ge1\). There is no separability assertion about the resulting Hilbert space. Finally an isometry from a complete normed space has closed image. \(\square\)

The operator realization need not be an algebra, self-adjoint, or unital. The theorem realizes the specified linear space and all of its matrix norms. It introduces none of those additional structures.

## 5. An elementary construction of matrix norms

Let \(E\) be any normed space. Set
\[
\|[x_{ij}]\|_n^{\min}
=\sup_{\substack{g\in E^*\\\|g\|\le1}}
   \|[g(x_{ij})]\|_{M_n}.
\]
This is a norm. If an entry is nonzero, Hahn–Banach gives a functional detecting it. The direct-sum and scalar-multiplication axioms follow from their scalar matrix versions and taking suprema. At scalar size the norm is the original norm of \(E\).

There is a direct operator realization here: map \(x\) to the bounded scalar function
\(g\mapsto g(x)\) on the dual unit ball, and let that function act by multiplication on the Hilbert space \(\ell^2\) of that set. At every size the operator norm is exactly the displayed supremum. This example illustrates that the same scalar norm can be extended to matrix norms in a way that reflects a chosen operator structure. The representation theorem applies to every structure satisfying the axioms, not only to this one.

## 6. Exercises with solutions

**Exercise 1 (Unitary rearrangement; introductory).** Prove that \(\|uxv\|_n=\|x\|_n\) whenever \(u,v\in M_n\) are unitaries.

*Solution.* The second axiom gives \(\|uxv\|\le\|x\|\). Apply it to \(u^*(uxv)v^*=x\) to obtain the reverse inequality. This justifies the coordinate permutation in Lemma 3.1.

**Exercise 2 (The row and column bounds; intermediate).** In Lemma 2.1, verify \(\|A\|^2=\|\sum_i\lambda_i a_i a_i^*\|\) and \(\|B\|^2=\|\sum_i\lambda_i b_i^*b_i\|\).

*Solution.* Matrix multiplication gives \(AA^*=\sum_i\lambda_i a_i a_i^*\) and \(B^*B=\sum_i\lambda_i b_i^*b_i\). The operator norm satisfies \(\|A\|^2=\|AA^*\|\) and \(\|B\|^2=\|B^*B\|\), including for rectangular operators.

**Exercise 3 (A zero state value; intermediate).** If \(p(aa^*)=0\), explain why the optimized bound in Lemma 2.1 implies \(f(axb)=0\), even when \(q(b^*b)>0\).

*Solution.* For \(\|x\|\le1\), the bound after replacing \(a,b\) by \(ta,t^{-1}b\) is \(\tfrac12t^{-2}q(b^*b)\). Let \(t\to\infty\). General \(x\) follows by rescaling. This is why (3) is well-defined on the Hilbert-space quotient.

**Exercise 4 (The detecting vectors; intermediate).** For \(a_i=E_{i1}\), \(b_j=E_{1j}\), compute \(a_iD_n(v)b_j\) and verify the unit-tuple calculation in Theorem 4.1.

*Solution.* The product has only one possibly nonzero entry, at position \((i,j)\), and that entry is \(v\). Also \(a_i a_i^*=E_{ii}\) and \(b_j^*b_j=E_{jj}\); summing and applying the states gives one on each side.

**Exercise 5 (Matrix norms from a Banach space; intermediate).** Prove both operator-space axioms for the norms in Section 5 and explain where Hahn–Banach is used.

*Solution.* For each \(g\), the scalar matrix of \(x\oplus y\) has norm the maximum of the two scalar block norms. The supremum of these maxima is the maximum of the separate suprema. For scalar \(a,b\), \([g((axb)_{ij})]=a[g(x_{ij})]b\), giving the second axiom. Hahn–Banach supplies a norm-one functional detecting a nonzero entry, so the formula is a norm rather than merely a seminorm, and gives \(\|x\|_1^{\min}=\|x\|\).

**Exercise 6 (Closure changes no old matrix norms; intermediate).** Suppose \(V\) is not complete. Realize it by Theorem 4.1 and take the norm closure of its image in \(B(H)\). Explain why the completed space extends every original matrix norm without changing it.

*Solution.* At each fixed size, convergence of all entries in operator norm is equivalent to convergence of the matrix in operator norm, by the estimates \(\max_{ij}\|x_{ij}\|\le\|[x_{ij}]\|\le\sum_{ij}\|x_{ij}\|\). Thus a matrix over the closure is a limit of matrices over the image. Its norm extends the given norm continuously, and the complete isometry on the original matrices remains exact. The inherited norms on the closure still satisfy both axioms.

## References

Ved Prakash Gupta, Prabha Mandayam and V. S. Sunder, [*The Functional Analysis of Quantum Information Theory*, arXiv:1410.7188v3](https://arxiv.org/pdf/1410.7188v3), Section 1.3.1, Theorem 1.3.1, printed pp.23–25 (PDF pp.28–30), gives the norm-detecting coefficient and direct-sum route. Its two-state selection inequality (1.3) is left by reference. Section 2 here supplies the full compact separation argument for fixed states on finite matrices at every middle size. Section 3 specifies the conjugate Hilbert space needed for the stated inner-product convention.

Edward G. Effros and Zhong-Jin Ruan, [*On matricially normed spaces*](https://msp.org/pjm/1988/132-2/pjm-v132-n2-p05-s.pdf), *Pacific Journal of Mathematics* 132(2) (1988), Theorem 2.2(1), printed p.248 (PDF p.7), states the representation theorem by reference; it is not its proof. Sections 1–4 here contain the complete realization argument, without completeness or separability assumptions. Section 5 proves the minimal matrix-norm example directly; the lecture notes' Section 1.3.3 states that realization without proving it. Exact transitive free Hahn–Banach and Hilbert-space foundations remain pending; no source expression was imported.
