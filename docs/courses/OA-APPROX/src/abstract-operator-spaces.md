# From matrix norms to operators

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text: public domain (CC0).*

A normed vector space remembers the size of a single vector. A subspace of bounded operators also remembers the size of every matrix of its vectors. These matrix norms interact with direct sums and scalar matrix multiplication. Ruan's theorem says that those two interactions are enough to recover an operator realization.

We will prove the theorem by constructing enough completely contractive maps to detect every matrix norm. The construction uses ordinary Hahn–Banach and finite-dimensional states. It does not assume that the vector space is complete or separable.

The retained scalar foundations prove scalar compactness, Hahn–Banach, Hilbert representation, operator adjoints, the C*-identity and Hilbert completion. [MG01](../scalar-gns-and-matrix-cstar-norms.html#mg01) proves scalar Cauchy–Schwarz and norming states, including for a positive scalar matrix. We use the exact retained scalar inputs for that proof. A linear map is completely contractive when its entrywise map on matrices is contractive at every size; a complete isometry preserves every such norm. No extension or factorization theorem for completely bounded maps is required here. Inner products are linear in the second variable.

The construction has one concrete goal: given a matrix \(Y\), find a coefficient operator whose norm at that size detects \(\|Y\|\), while its norms at every other size stay below the prescribed norms. The finite-state lemma provides those simultaneous bounds. Rectangular coefficient operators then combine into one Hilbert-space direct sum.

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
The state set of \(M_n(\mathbb C)\) is nonempty: a unit vector gives the state \(c\mapsto\langle\xi,c\xi\rangle\). Identify a functional with its \(n^2\) values on the matrix units. Positivity and value one at the unit are closed conditions. Scalar Cauchy–Schwarz gives norm one for a positive functional of value one at the unit, hence bounds each of these coordinates by one. Conversely those closed conditions characterize the states. The state set is therefore closed in a finite product of compact discs, hence compact. Convexity follows by taking convex combinations of positive functionals. This proves that pairs of states form a compact convex set. Each requirement is a closed half-space in that set. We prove that every finite family of requirements has a common pair of states.

Take triples \((a_i,x_i,b_i)\), \(1\le i\le r\), with possibly different middle sizes and \(\|x_i\|\le1\). Their simultaneous requirements say that the compact convex set
\[
 C=\left\{
\left(\tfrac12\{p(a_i a_i^*)+q(b_i^*b_i)\}
      -\operatorname{Re}f(a_i x_i b_i)\right)_{i=1}^r:p,q\text{ states}
 \right\}
\]
meets the nonnegative orthant \(Q=\mathbb R_+^r\). Suppose it does not. The squared distance to \(Q\) is the continuous function \(c\mapsto\sum_i\min(c_i,0)^2\), so it has a minimizer \(c\in C\), with strictly positive minimum. Put
\[
 u_i=\max(c_i,0),\qquad \lambda_i=u_i-c_i\ge0.
\]
Then \(\lambda\ne0\), \(\lambda\cdot u=0\), and \(\lambda\cdot c=-\|\lambda\|^2\). For any \(d\in C\), the segment \(c+t(d-c)\), \(0\le t\le1\), lies in \(C\). Its distance to the fixed \(u\in Q\) is at least the minimal distance from \(C\) to \(Q\). Expanding its squared distance and dividing by \(t>0\), then letting \(t\downarrow0\), gives
\[
 (c-u)\cdot(d-c)\ge0,
 \qquad \lambda\cdot d\le\lambda\cdot c=-\|\lambda\|^2<0.
\]
This proves the needed strict separation and the nonnegative coefficients directly. It gives
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

<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="os-title os-desc" width="1050" height="400" viewBox="0 0 1050 400">
<title id="os-title">Finite-state selection by the distance to the positive orthant</title>
<desc id="os-desc">For a finite family of r matrix triples, pairs of states yield a compact convex set C of r real constraint values. If it missed the positive orthant, the closest point c would give u equal to its coordinatewise positive part and nonzero lambda equal to u minus c. Nonnegative lambda gives strict separation. The row and column matrix norm bound forces the supremum of these same lambda-weighted values to be nonnegative, a contradiction.</desc>
<defs><marker id="os-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#285a77"/></marker></defs>
<rect x="1" y="1" width="1048" height="398" rx="12" fill="#f7fafc" stroke="#9ab0bd"/>
<text x="24" y="34" font-family="Arial,sans-serif" font-size="21" font-weight="bold" fill="#163d56">One pair of states must meet every finite list of constraints</text>
<rect x="24" y="57" width="445" height="121" rx="9" fill="white" stroke="#608497"/>
<text x="43" y="85" font-family="Arial,sans-serif" font-size="17" fill="#163d56">Compact convex C in R^r, from all pairs (p,q)</text>
<text x="43" y="115" font-family="Arial,sans-serif" font-size="16" fill="#163d56">C_i(p,q) = (p(a_i a_i*) + q(b_i* b_i))/2</text>
<text x="43" y="141" font-family="Arial,sans-serif" font-size="16" fill="#163d56">                 - Re f(a_i x_i b_i),  ||x_i|| &lt;= 1</text>
<text x="43" y="165" font-family="Arial,sans-serif" font-size="15" fill="#163d56">A common pair means C meets Q = R_+^r.</text>
<path d="M480 111H559" stroke="#285a77" stroke-width="2" marker-end="url(#os-arrow)"/>
<text x="520" y="89" text-anchor="middle" font-family="Arial,sans-serif" font-size="14" fill="#163d56">suppose not</text>
<rect x="573" y="57" width="451" height="121" rx="9" fill="#fff7ec" stroke="#b79055"/>
<text x="591" y="85" font-family="Arial,sans-serif" font-size="17" fill="#163d56">Choose c minimizing distance(C,Q).</text>
<text x="591" y="115" font-family="Arial,sans-serif" font-size="17" fill="#163d56">u_i = max(c_i,0); lambda = u - c &gt;= 0</text>
<text x="591" y="142" font-family="Arial,sans-serif" font-size="17" fill="#163d56">lambda is nonzero; lambda dot u = 0.</text>
<text x="591" y="165" font-family="Arial,sans-serif" font-size="15" fill="#163d56">Expand along every segment c + t(d-c).</text>
<path d="M799 188V217" stroke="#285a77" stroke-width="2" marker-end="url(#os-arrow)"/>
<path d="M246 188V217" stroke="#285a77" stroke-width="2" marker-end="url(#os-arrow)"/>
<rect x="24" y="228" width="445" height="85" rx="9" fill="#edf7ec" stroke="#6e9864"/>
<text x="43" y="256" font-family="Arial,sans-serif" font-size="17" fill="#163d56">The block row/column norm estimate gives</text>
<text x="43" y="284" font-family="Arial,sans-serif" font-size="18" fill="#163d56">sup_(p,q) sum_i lambda_i C_i(p,q) &gt;= 0.</text>
<rect x="573" y="228" width="451" height="85" rx="9" fill="#fff7ec" stroke="#b79055"/>
<text x="591" y="256" font-family="Arial,sans-serif" font-size="17" fill="#163d56">For every d in C, the distance proof gives</text>
<text x="591" y="284" font-family="Arial,sans-serif" font-size="18" fill="#163d56">lambda dot d &lt;= -||lambda||^2 &lt; 0.</text>
<text x="525" y="275" text-anchor="middle" font-family="Arial,sans-serif" font-size="16" font-weight="bold" fill="#8c3e35">conflict</text>
<text x="24" y="354" font-family="Arial,sans-serif" font-size="17" fill="#163d56">Therefore each finite family has a common pair. Compactness gives one pair for every triple.</text>
<text x="24" y="380" font-family="Arial,sans-serif" font-size="15" fill="#163d56">Proof locator: Lemma 2.1. Objects are the actual finite constraint image and coordinatewise orthant projection.</text>
</svg>

*Figure.* For a fixed finite list of matrix triples, \(C\subset\mathbb R^r\) is their actual constraint-value image as the pair of states varies, and \(Q\) is the nonnegative orthant. The closest-point construction is used only under the contradictory assumption \(C\cap Q=\varnothing\). The block row and column estimate then contradicts its strictly negative weighted supremum. Compactness passes from all finite lists to the one pair required by Lemma 2.1.

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
Positivity of the states makes these forms positive semidefinite. Scalar Cauchy–Schwarz shows that a null vector pairs to zero with every vector, so the null sets are linear subspaces, and the forms descend to positive definite forms on the quotients. A finite-dimensional inner-product space is complete: choose an orthonormal basis by the finite Gram–Schmidt procedure and take the coordinate limits of any Cauchy sequence. These spaces are therefore finite-dimensional Hilbert spaces. Write \(\overline{H_p}\) for the conjugate Hilbert space; the correspondence \(a\mapsto\bar a\) is conjugate linear.

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
\(B(\overline{H_p}\oplus H_q)\), with all other corners zero. For every size \(m\) and \(X\in M_m(V)\), this corner sends a tuple \(u\oplus w\) to \(\theta_f^{(m)}(X)w\oplus0\). The upper bound is its operator norm, and testing tuples \(0\oplus w\) gives the reverse bound. Thus corner insertion preserves the norm at every size. For each nonzero matrix \(Y\) at each size, choose such a map that detects its norm. Form the Hilbert direct sum of their spaces and the block diagonal map
\[
\Theta(v)=\bigoplus_Y\theta_Y(v).
\]
The direct sum is the space of families \((\zeta_Y)\) for which the supremum of the finite sums \(\sum_{Y\in F}\|\zeta_Y\|^2\) is finite. Finite-support vectors are dense by that supremum; coordinatewise limits of a Cauchy sequence, and passage of its Cauchy bound to each finite sum, prove completeness. Each coordinate is a complete contraction. Summing the squared coordinate bounds first on finite-support vectors defines \(\Theta(v)\) with norm at most \(\|v\|\), and then extends it by continuity. At a fixed matrix size, interchanging the finite tuple with the Hilbert direct sum is an isometry, since its squared norm is the same sum in either order. The corresponding entrywise operator acts coordinatewise, so the identical bound proves contractivity at every matrix size. For any \(Y\), its own coordinate gives the reverse inequality at that size. Thus \(\Theta\) is a complete isometry.

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

Edward G. Effros and Zhong-Jin Ruan, [*On matricially normed spaces*](https://msp.org/pjm/1988/132-2/pjm-v132-n2-p05-s.pdf), *Pacific Journal of Mathematics* 132(2) (1988), Theorem 2.2(1), printed p.248 (PDF p.7), states the representation theorem by reference; it is not its proof. Sections 1–4 here contain the complete realization argument, without completeness or separability assumptions. Section 5 proves the minimal matrix-norm example directly; the lecture notes' Section 1.3.3 states that realization without proving it. The complete scalar compactness, Hahn–Banach and Hilbert-space proofs consumed here are the exact retained foundations linked above; MG01 supplies the scalar positive-functional norm and norming-state argument. The finite orthant distance proof replaces the separation implication rather than importing it from the referred-to thesis. The human notes and paper retain their own rights; their source text and PDFs are not reproduced or relicensed. These mathematical proof inputs do not certify the inherited wording, selection and organization of the whole course.
