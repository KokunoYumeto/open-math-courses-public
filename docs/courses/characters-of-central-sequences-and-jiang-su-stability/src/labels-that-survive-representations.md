# Labels that survive representations

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

An irreducible representation of a maximal tensor product need not be a tensor product of representations of the factors. This lesson shows that, nevertheless, a finite tensor power of an algebra without characters contains *labels*: finitely many self-adjoint elements whose images stay linearly independent in every irreducible representation of every larger tensor power (Corollary 5.1). The next lesson uses labels to combine finitely many witnesses into a single element without losing any of them.

- Independence in commuting factors (Lemma 1.1).
- Represented blocks of a tensor product are factors (Lemma 2.1).
- A finite-dimensional space that detects noncommutativity (Lemma 3.1).
- Real labels from Sard's theorem (Lemma 4.1).
- Labels in tensor powers (Corollary 5.1).

The lesson follows [OpenAI-KRC, Sections 4.1 and 4.2]. All tensor products of C\*-algebras are maximal, and \(D^{\otimes k}\) denotes the maximal tensor power \(D^{\otimes_{\max}k}\) of [Central sequences and the character criterion](central-sequences-and-the-character-criterion.md), Section 3. A *factor* on a Hilbert space \(H\) is a von Neumann algebra \(N\subseteq B(H)\), containing \(1_H\), with \(N\cap N'=\mathbb C1\).

## 1. Independence in commuting factors

**Lemma 1.1.**

1. Let \(N\) be a factor on \(H\), let \(a_1,\dots,a_p\in N\), and let \(B_1,\dots,B_p\in N'\) be linearly independent. If \(\sum_ta_tB_t=0\), then every \(a_t\) is \(0\).
2. Let \(N_1,\dots,N_n\) be pairwise commuting factors on \(H\). For each \(j\) let \(b^{(j)}_1,\dots,b^{(j)}_{d_j}\in N_j\) be linearly independent. Then the products
\[
\begin{gathered}
b^{(1)}_{s_1}b^{(2)}_{s_2}\cdots b^{(n)}_{s_n},\\
s\in[d_1]\times\cdots\times[d_n],
\end{gathered}
\]
are linearly independent; here \([d]=\{1,\dots,d\}\).

*Proof.* (1) By the theorem of Murray and von Neumann ([Tensor products of C\*-algebras and the minimal norm](course:tensor-products-of-operator-algebras/tensor-products-of-c-star-algebras-and-the-minimal-norm), Theorem 5.1), \(\sum_ta_t\otimes B_t=0\) in the algebraic tensor product \(N\odot N'\). Since the \(B_t\) are linearly independent, every \(a_t\) is \(0\) ([Tensor products of Banach and Hilbert spaces, Jordan homomorphisms and isometries of C\*-algebras](course:tensor-products-of-operator-algebras/tensor-products-of-banach-and-hilbert-spaces-jordan-homomorphisms-and-isometries-of-c-star), Lemma 1.1).

(2) Induction on \(n\); the case \(n=1\) is the hypothesis. Let \(n\ge2\). By induction, the products \(B_t=b^{(2)}_{t_2}\cdots b^{(n)}_{t_n}\) are linearly independent, and they lie in \(N_1'\). Suppose \(\sum_sc_s\,b^{(1)}_{s_1}B_{(s_2,\dots,s_n)}=0\), and put \(a_t=\sum_{s_1}c_{(s_1,t)}b^{(1)}_{s_1}\in N_1\). Then \(\sum_ta_tB_t=0\), so every \(a_t\) is \(0\) by (1). As the \(b^{(1)}_{s_1}\) are linearly independent, all \(c_s\) vanish. \(\blacksquare\)

Without the factor hypothesis the lemma fails (Exercise 6.1).

## 2. Represented blocks of a tensor product

Let \(A_1,\dots,A_k\) be unital C\*-algebras and \(P=A_1\otimes\cdots\otimes A_k\). The *legs* of \(P\) are the embeddings \(a\mapsto1\otimes\cdots\otimes a\otimes\cdots\otimes1\) of the \(A_j\); they are injective, unital, and have commuting ranges ([Central sequences and the character criterion](central-sequences-and-the-character-criterion.md), Lemma 3.1(2)).

**Lemma 2.1.** Let \(\pi\) be an irreducible representation of \(P\) on \(H\), and let \(\{1,\dots,k\}=I_1\cup\cdots\cup I_q\) be a partition into nonempty sets. Let \(L_b\) be the union of the ranges of the legs with index in \(I_b\), and \(N_b=\pi(L_b)''\). Then \(N_1,\dots,N_q\) are pairwise commuting factors on \(H\).

*Proof.* \(\pi\) is unital (Lemma 3.1(6) of the same lesson), so \(1_H\in\pi(L_b)\), and \(N_b\) is a von Neumann algebra ([The double commutant theorem](course:foundations-of-von-neumann-algebras/the-double-commutant-theorem), Proposition 2.1). For \(b\ne b'\), \(\pi(L_{b'})\subseteq\pi(L_b)'\), because the legs commute; taking commutants, \(N_b\subseteq\pi(L_{b'})'\), that is, \(\pi(L_{b'})\subseteq N_b'\), and then \(N_{b'}\subseteq N_b'''=N_b'\). So the \(N_b\) commute pairwise. Let \(z\in N_b\cap N_b'\). Then \(z\) commutes with \(\pi(L_b)\subseteq N_b\) and with \(\pi(L_{b'})\subseteq N_{b'}\subseteq N_b'\) for \(b'\ne b\). Elementary tensors are products of leg elements and span a dense subalgebra of \(P\), so \(z\) commutes with \(\pi(P)\), and \(z\in\mathbb C1\) by Schur's lemma ([Building representations from positive functionals](course:foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark), Corollary 2.3). \(\blacksquare\)

The lemma needs no faithfulness of the restrictions to the legs and no decomposition of \(H\) as a tensor product.

## 3. A detecting space

Write \(D_{\mathrm{sa}}\) for the real vector space of self-adjoint elements of \(D\).

**Lemma 3.1** ([OpenAI-KRC, Lemma 4.3]). Let \(D\) be a nonzero unital C\*-algebra without characters. There is a finite-dimensional real subspace \(V\subseteq D_{\mathrm{sa}}\) such that, for every unital representation \(\rho\) of \(D\) on a nonzero Hilbert space, \(\rho(V)\) contains two operators that do not commute. Moreover \(\dim_{\mathbb R}V\ge2\).

*Proof.* As in the proof of Lemma 4.2 of [Central sequences and the character criterion](central-sequences-and-the-character-criterion.md), there are self-adjoint \(b_i,c_i\) and elements \(h_i,k_i\) of \(D\), \(1\le i\le r\), with
\[
\|1-y\|<1,\qquad y=\sum_{i=1}^rh_i[b_i,c_i]k_i .
\]
So \(y\) is invertible. Let \(V\) be the real span of the \(b_i\) and \(c_i\). If \(\rho(V)\) were commutative, then \(\rho([b_i,c_i])=0\) for all \(i\) and \(\rho(y)=0\), while \(\rho(y)\rho(y^{-1})=\rho(1)=1\ne0\). A unital representation of \(D\) on a nonzero space exists: take a faithful representation \(\rho_0\) ([Building representations from positive functionals](course:foundations-of-von-neumann-algebras/representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark), Theorem 7.2) on the range of the nonzero projection \(\rho_0(1)\). If \(\dim V\le1\), then \(V\) would be commutative, which is excluded. So \(\dim V\ge2\). \(\blacksquare\)

## 4. Real labels

For integers \(m,n\ge1\), \(\mathbb R^{[m]^n}\) is the space of real arrays \(x=(x_k)\) indexed by \(k=(k_1,\dots,k_n)\in[m]^n\); its dimension is \(m^n\). For real matrices \(A_j\) of size \(d_j\times m\), let \(A_1\otimes\cdots\otimes A_n\) be the linear map \(\mathbb R^{[m]^n}\to\mathbb R^{[d_1]\times\cdots\times[d_n]}\),
\[
\begin{aligned}
&\bigl((A_1\otimes\cdots\otimes A_n)x\bigr)_s\\
&\quad=\sum_{k}A_1[s_1,k_1]\cdots A_n[s_n,k_n]\,x_k .
\end{aligned}
\]
The same formula is used for complex arrays. Expanding the sums gives
\[
\begin{aligned}
&(R_1\otimes\cdots\otimes R_n)(A_1\otimes\cdots\otimes A_n)\\
&\quad=R_1A_1\otimes\cdots\otimes R_nA_n
\end{aligned}
\]
for matrices \(R_j\) with \(d_j\) columns. If every \(A_j\) has rank \(d_j\), then \(A_1\otimes\cdots\otimes A_n\) is surjective: choose \(u_j\in\mathbb R^m\) with \(A_ju_j\) equal to the \(s_j\)-th standard basis vector; the array \((u_1)_{k_1}\cdots(u_n)_{k_n}\) is mapped to the standard basis array at \(s\).

**Lemma 4.1** (real labels; [OpenAI-KRC, Lemma 4.4]). Let \(m\ge2\) and \(r\ge1\). There are \(n\ge1\) and arrays \(x^{(1)},\dots,x^{(r)}\in\mathbb R^{[m]^n}\) such that, for all real \(2\times m\) matrices \(P_1,\dots,P_n\) of rank \(2\), the arrays
\[
(P_1\otimes\cdots\otimes P_n)x^{(i)},\qquad1\le i\le r,
\]
are linearly independent.

*Proof.* Choose \(n\) with \(2^n>2mn+r-1\). Let \(\mathcal P\) be the set of \(n\)-tuples of real \(2\times m\) matrices of rank \(2\); a matrix has rank \(2\) when one of its \(2\times2\) minors is nonzero, so \(\mathcal P\) is open in \(\mathbb R^{2mn}\). The unit sphere \(S^{r-1}\subset\mathbb R^r\) is a smooth manifold of dimension \(r-1\), the regular level set of \(u\mapsto|u|^2\) at \(1\) ([Regular values and degree modulo two](course:borsuks-conjecture-in-dimension-nine/regular-values-and-degree-modulo-two), Proposition 3.1). Put \(W=\mathbb R^{[m]^n}\) and consider the smooth manifold \(\mathcal X=\mathcal P\times S^{r-1}\times W^r\), of dimension \(2mn+r-1+rm^n\), and the polynomial map
\[
\begin{aligned}
&\Phi\colon\mathcal X\to\mathbb R^{[2]^n},\\
&\Phi(P,u,x)\\
&\quad=(P_1\otimes\cdots\otimes P_n)\Bigl(\sum_{i=1}^ru_ix^{(i)}\Bigr).
\end{aligned}
\]
At every point some \(u_i\) is nonzero, and the derivative of \(\Phi\) in the direction of \(x^{(i)}\) alone is \(\dot x\mapsto u_i(P_1\otimes\cdots\otimes P_n)\dot x\), which is surjective. So \(0\) is a regular value of \(\Phi\), and \(Z=\Phi^{-1}(0)\) is a smooth manifold of dimension
\[
\begin{aligned}
2mn+r-1&+rm^n-2^n\\
&<rm^n=\dim W^r
\end{aligned}
\]
(Proposition 3.1 there), on which the projection \(\operatorname{pr}\colon Z\to W^r\) is smooth. Since \(\dim Z<\dim W^r\), every point of \(Z\) is a critical point of \(\operatorname{pr}\), so \(\operatorname{pr}(Z)\) is a null set (Sard's theorem, Corollary 2.2 there). A null set is not all of \(W^r\); choose \(x=(x^{(1)},\dots,x^{(r)})\notin\operatorname{pr}(Z)\). If \(\sum_ic_i(P_1\otimes\cdots\otimes P_n)x^{(i)}=0\) for some \(P\in\mathcal P\) and a real vector \(c\ne0\), then \(u=c/|c|\) gives \(\Phi(P,u,x)=0\), so \(x\in\operatorname{pr}(Z)\), which is false. \(\blacksquare\)

The labels are found by a measure argument, not written down; the lemma asserts only their existence, with an exponent \(n\) depending on \(m\) and \(r\).

## 5. Labels in tensor powers

**Corollary 5.1** (labels; [OpenAI-KRC, Corollary 4.5]). Let \(D\) be a nonzero unital C\*-algebra without characters and \(r\ge1\). There are \(n\ge1\) and self-adjoint \(x_1,\dots,x_r\in D^{\otimes n}\) with the following property. For all integers \(k\ge n\) and \(0\le j\le k-n\), and every irreducible representation \(\pi\) of \(D^{\otimes k}\), the operators
\[
\pi\bigl(1^{\otimes j}\otimes x_i\otimes1^{\otimes(k-j-n)}\bigr),\qquad1\le i\le r,
\]
are linearly independent.

Here \(D^{\otimes k}\) is identified with \(D^{\otimes j}\otimes D^{\otimes n}\otimes D^{\otimes(k-j-n)}\) by regrouping (Lemma 3.1(3) of [Central sequences and the character criterion](central-sequences-and-the-character-criterion.md)), with an empty factor omitted.

*Proof.* Let \(V\) be the space of Lemma 3.1, with a real basis \(v_1,\dots,v_m\), \(m\ge2\). Take \(n\) and the arrays \(x^{(i)}\) of Lemma 4.1, and put
\[
x_i=\sum_{k\in[m]^n}x^{(i)}_k\,v_{k_1}\otimes\cdots\otimes v_{k_n}\in D^{\otimes n}.
\]
It is self-adjoint: a real combination of tensors with self-adjoint entries.

Fix \(k\), \(j\) and \(\pi\), and let \(\pi_1,\dots,\pi_k\) be the restrictions of \(\pi\) to the legs: unital representations with commuting ranges. By Lemma 2.1, applied to the partition into single legs, the algebras \(N_l=\pi_l(D)''\) are pairwise commuting factors. For \(l=1,\dots,n\), the real space \(E_l=\pi_{j+l}(V)\) consists of self-adjoint operators, and its dimension \(d_l\) is at least \(2\), because it contains two operators that do not commute (Lemma 3.1). Choose a real basis \(f^{(l)}_1,\dots,f^{(l)}_{d_l}\) of \(E_l\), and write
\[
\pi_{j+l}(v_q)=\sum_{s=1}^{d_l}A_l[s,q]\,f^{(l)}_s
\]
with a real \(d_l\times m\) matrix \(A_l\) of rank \(d_l\). A real basis of a space of self-adjoint operators is complex linearly independent: if \(\sum_s(\alpha_s+i\beta_s)f_s=0\) with real \(\alpha_s,\beta_s\), taking adjoints gives \(\sum_s(\alpha_s-i\beta_s)f_s=0\), so \(\sum_s\alpha_sf_s=\sum_s\beta_sf_s=0\). Now, writing \(\hat x_i=1^{\otimes j}\otimes x_i\otimes1^{\otimes(k-j-n)}\),
\[
\begin{aligned}
&\pi(\hat x_i)\\
&\quad=\sum_kx^{(i)}_k\,\pi_{j+1}(v_{k_1})\cdots\pi_{j+n}(v_{k_n})\\
&\quad=\sum_sy^{(i)}_s\,f^{(1)}_{s_1}\cdots f^{(n)}_{s_n},
\end{aligned}
\]
where \(y^{(i)}=(A_1\otimes\cdots\otimes A_n)x^{(i)}\). By Lemma 1.1(2), applied to the factors \(N_{j+1},\dots,N_{j+n}\), the products \(f^{(1)}_{s_1}\cdots f^{(n)}_{s_n}\) are linearly independent. So a complex relation \(\sum_ic_i\pi(\hat x_i)=0\) gives \(\sum_ic_iy^{(i)}=0\). The rows of \(A_l\) are linearly independent; let \(R_l\) be the \(2\times d_l\) matrix selecting two of them, so that \(P_l=R_lA_l\) has rank \(2\). Applying \(R_1\otimes\cdots\otimes R_n\) gives \(\sum_ic_i(P_1\otimes\cdots\otimes P_n)x^{(i)}=0\). The real arrays \((P_1\otimes\cdots\otimes P_n)x^{(i)}\) are linearly independent over \(\mathbb R\) by Lemma 4.1, hence over \(\mathbb C\) (take real and imaginary parts). So all \(c_i\) vanish. \(\blacksquare\)

## 6. Exercises

**6.1.** Let \(N_1=N_2\) be the diagonal \(2\times2\) matrices acting on \(\mathbb C^2\). Show that they commute, that they are not factors, and that the products of the independent families \((e_{11},e_{22})\) and \((e_{11},e_{22})\) are linearly dependent.

**6.2.** For \(D=M_2\), show that the real span \(V\) of \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\) and \(\begin{pmatrix}1&0\\0&-1\end{pmatrix}\) has the property of Lemma 3.1.

**6.3.** Show that the conclusion of Lemma 4.1 cannot hold when \(r>2^n\).

**6.4.** Find two operators that are linearly independent over \(\mathbb R\) but not over \(\mathbb C\), and explain why the proof of Corollary 5.1 works with self-adjoint operators.

**6.5.** In Lemma 2.1, why must \(\pi\) be irreducible? Give a representation of \(\mathbb C^2\otimes\mathbb C^2\) in which the first leg generates a von Neumann algebra that is not a factor.

## 7. Solutions

**6.1.** Diagonal matrices commute. The algebra contains the nonscalar projection \(e_{11}\), and it is commutative, so its centre is itself, not \(\mathbb C1\). The products \(e_{11}e_{22}=e_{22}e_{11}=0\) form a dependent family.

**6.2.** A unital representation \(\rho\) of \(M_2\) on a nonzero space is injective, since \(\ker\rho\) is a proper ideal of the simple algebra \(M_2\). The two matrices do not commute (their products in the two orders differ by a sign and are nonzero), so their images do not commute.

**6.3.** The arrays \((P_1\otimes\cdots\otimes P_n)x^{(i)}\) lie in a space of dimension \(2^n\), which contains no more than \(2^n\) linearly independent vectors.

**6.4.** \(1\) and \(i1\) are independent over \(\mathbb R\) and dependent over \(\mathbb C\). For self-adjoint operators, taking adjoints separates the real and imaginary parts of a complex relation, as in the proof.

**6.5.** Irreducibility gives \(\pi(P)'=\mathbb C1\), which makes a central element of \(N_b\) scalar. The identity representation of \(\mathbb C^2\otimes\mathbb C^2\cong\mathbb C^4\) on \(\mathbb C^4\) (diagonal matrices) is not irreducible, and its first leg generates the diagonal matrices \(\operatorname{diag}(a,a,b,b)\), a commutative algebra containing a nonscalar projection.

## References

- [OpenAI-KRC] OpenAI, *The Kirchberg–Rørdam character criterion*, OpenAI Math Release preprint, 25 September 2026, Sections 4.1 and 4.2. https://github.com/openai/math/tree/main/preprints/The-Kirchberg-Rordam-character-criterion-September-25-2026
