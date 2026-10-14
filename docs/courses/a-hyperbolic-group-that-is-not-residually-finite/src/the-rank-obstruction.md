# The rank obstruction

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The previous lesson, [Punctured lines and the complex](punctured-lines-and-the-complex.md), built a finite triangle complex \(K\) whose fundamental group \(G\) is torsion-free and word-hyperbolic, together with a finite set \(\mathcal R\) of nontrivial elements, the rectangular words. This lesson proves that no finite quotient of \(G\) keeps all of them nontrivial (Theorem 3.4). Consequently one fixed rectangular word dies in every finite quotient, and \(G\) is not residually finite: this is the theorem of the course. With Malcev's theorem the same word is killed by every finite-dimensional linear representation over a field (Corollary 4.3).

The argument compares ranks. In the regular representation of a finite quotient that keeps all rectangular words, an \(r\times r\) array of permutation matrices has large real rank (Section 2). A rank lower bound survives reduction modulo the fixed prime \(q\) of the construction (Lemma 1.2). Over \(\mathbb F_q\), the triangle relations factor the sums of these arrays over the blocks at each point through a small space, and an interpolation identity over the punctured lines expresses the direct sum of all arrays through these sums (Section 3). The two rank estimates contradict the numerical budget of the construction.

- Rank under reduction modulo a prime (Lemma 1.2).
- Arrays of permutation matrices (Proposition 2.2).
- Local factorizations and the line certificate (Lemmas 3.1–3.3, Theorem 3.4).
- Residual finiteness and linear representations (Theorems 4.1 and 4.2, Corollary 4.3).

The lesson follows [OpenAI-RF, Sections 1, 2.4 and 2.5]. Notation is that of the previous lesson: the prime \(q\), \(P=\mathbb F_q^h\), \(m=q^h\), the labels \(I\) with \(|I|=N\), marks \(a_i\in S^h\), the sets \(I(z)\) and \(E\), the blocks \(b\) with their bijections \(\alpha_b,\beta_b\), the elements \(g_e\in G\), and the budget
\[
q>r,\qquad\frac{Nr}4>2m+r|E| .
\]

## 1. Rank under reduction

**Lemma 1.1** (Hadamard's inequality). For a real \(d\times d\) matrix \(B\) with rows \(b_1,\dots,b_d\), \(|\det B|\le\prod_k\|b_k\|\).

*Proof.* If the rows are dependent, \(\det B=0\). Otherwise the Gram–Schmidt process writes \(B=TQ\) with \(T\) lower triangular and \(Q\) orthogonal; the \(k\)-th diagonal entry of \(T\) is the distance from \(b_k\) to the span of \(b_1,\dots,b_{k-1}\), at most \(\|b_k\|\). So \(|\det B|=|\det T|\le\prod_k\|b_k\|\). \(\blacksquare\)

**Lemma 1.2** (rank under reduction; [OpenAI-RF, Lemma 2.4]). Let \(M\) be an integer matrix whose rows have Euclidean norm at most \(\sqrt r\), where \(r\ge1\). For every prime \(q>r\),
\[
\operatorname{rank}_{\mathbb F_q}M\ge\tfrac12\operatorname{rank}_{\mathbb R}M .
\]

*Proof.* Let \(d=\operatorname{rank}_{\mathbb R}M\); there is nothing to prove for \(d=0\). Choose a \(d\times d\) submatrix \(B\) with \(\det B\ne0\). Then \(1\le|\det B|\le r^{d/2}\), by Lemma 1.1 and because \(\det B\) is a nonzero integer. Let \(d'\) be the rank of \(B\) modulo \(q\), and choose \(d'\) rows of \(B\) whose reductions span the row space of \(B\) modulo \(q\). Subtract from each other row an integer combination of the chosen rows that agrees modulo \(q\) with its expression through them. These operations do not change \(\det B\), and afterwards \(d-d'\) rows are divisible by \(q\). Hence \(q^{d-d'}\) divides \(\det B\), and
\[
q^{d-d'}\le r^{d/2}<q^{d/2}.
\]
So \(d'>d/2\), and \(\operatorname{rank}_{\mathbb F_q}M\ge d'\). \(\blacksquare\)

The prime \(q\) was fixed before any finite quotient is considered; Lemma 1.2 applies to integer matrices of every size, with a bound that does not depend on their size.

## 2. Arrays of permutation matrices

Let \(Q\) be a finite group and \(\pi\colon G\to Q\) a surjective homomorphism, with \(D=|Q|\). For \(g\in G\), let \(U(g)\) be the \(D\times D\) permutation matrix of left multiplication by \(\pi(g)\) on \(Q\), acting on column vectors indexed by \(Q\). Then \(U\) is a homomorphism, \(U(g)^{\mathsf T}=U(g^{-1})\), and
\[
\operatorname{tr}U(g)=\begin{cases}D,&\pi(g)=1,\\0,&\pi(g)\ne1,\end{cases}
\]
because left multiplication by a nonidentity element has no fixed point. For \(i\in I\) let \(Y_i\) be the \(rD\times rD\) block matrix
\[
Y_i=\bigl(U(g_{iuv})\bigr)_{u,v\in[r]} .
\]

**Lemma 2.1.** For a nonzero positive semidefinite real matrix \(A\),
\[
\operatorname{rank}A\ge\frac{(\operatorname{tr}A)^2}{\operatorname{tr}A^2}.
\]

*Proof.* If \(\lambda_1,\dots,\lambda_\rho>0\) are the nonzero eigenvalues, the Cauchy–Schwarz inequality gives \((\sum_k\lambda_k)^2\le\rho\sum_k\lambda_k^2\). \(\blacksquare\)

**Proposition 2.2** ([OpenAI-RF, Section 2.4]). Suppose that \(\pi\) keeps every rectangular word nontrivial. Then, for every \(i\in I\),
\[
\operatorname{rank}_{\mathbb F_q}Y_i\ge\frac{rD}4 .
\]

*Proof.* The block \((u,u')\) of \(Y_iY_i^{\mathsf T}\) is \(\sum_vU(g_{iuv}g_{iu'v}^{-1})\). Hence
\[
\operatorname{tr}(Y_iY_i^{\mathsf T})=\sum_{u,v}\operatorname{tr}U(1)=r^2D,
\]
and
\[
\begin{aligned}
&\operatorname{tr}\bigl((Y_iY_i^{\mathsf T})^2\bigr)\\
&\quad=\sum_{u,u',v,v'}\operatorname{tr}U\bigl(w_{uu'vv'}\bigr),
\end{aligned}
\]
with \(w_{uu'vv'}=g_{iuv}g_{iu'v}^{-1}g_{iu'v'}g_{iuv'}^{-1}\). This element is \(1\) when \(u=u'\) or \(v=v'\), and a rectangular word otherwise, which \(\pi\) keeps nontrivial. There are \(2r^3-r^2\) choices with \(u=u'\) or \(v=v'\), so
\[
\operatorname{tr}\bigl((Y_iY_i^{\mathsf T})^2\bigr)=(2r^3-r^2)D .
\]
By Lemma 2.1,
\[
\begin{aligned}
\operatorname{rank}_{\mathbb R}Y_i&\ge\frac{r^4D^2}{(2r^3-r^2)D}\\
&=\frac{r^2D}{2r-1}\ge\frac{rD}2 .
\end{aligned}
\]
Each row of \(Y_i\) has exactly \(r\) entries \(1\) and the others \(0\), so its norm is \(\sqrt r\), and Lemma 1.2 with \(q>r\) gives the claim. \(\blacksquare\)

No condition relates \(D\) and \(q\); in particular \(q\) may divide \(D\).

## 3. Local factorizations and the line certificate

From now on all matrices are reduced modulo \(q\), over \(\mathbb F_q\). For \(z\in P\) put
\[
Z(z)=\sum_{i\in I(z)}Y_i ,
\]
an \(rD\times rD\) matrix.

**Lemma 3.1** (local factorization). If \(z\notin E\), then \(\operatorname{rank}Z(z)\le2D\). For every \(z\), \(\operatorname{rank}Z(z)\le rD\).

*Proof.* The second bound is the size of the matrix. For \(z\notin E\), \(I(z)\) is the union of its two blocks, so it suffices to show that \(\sum_{i\in I_b}Y_i\) has rank at most \(D\) for a block \(b\). Put
\[
\begin{aligned}
A_u&=\sum_{j\in\mathbb Z/s_b}U\bigl(g_{L_{b,u,j}}^{-1}\bigr),\\
B_v&=\sum_{k\in\mathbb Z/t_b}U\bigl(g_{R_{b,v,k}}\bigr).
\end{aligned}
\]
By the triangle relations (Lemma 4.1 of the previous lesson), the block \((u,v)\) of \(\sum_{i\in I_b}Y_i\) is
\[
\sum_{i\in I_b}U\bigl(g_{L_{b,u,\alpha_b(i)+v}}^{-1}\bigr)\,U\bigl(g_{R_{b,v,\beta_b(i)+u}}\bigr).
\]
As \(i\) runs through \(I_b\), the pair \((\alpha_b(i)+v,\beta_b(i)+u)\) runs through \(\mathbb Z/s_b\times\mathbb Z/t_b\) exactly once, so this block equals \(A_uB_v\). Hence \(\sum_{i\in I_b}Y_i\) is the product of the block column \((A_u)_u\) and the block row \((B_v)_v\), whose inner dimension is \(D\). The order of the factors is kept; no commutativity is used. \(\blacksquare\)

**Lemma 3.2** (sums over lines). Let \(F\in\mathbb F_q[X_1,\dots,X_h]\) have total degree less than \(q-1\). Then \(\sum_{z\in\ell}F(z)=0\) for every affine line \(\ell\subset P\).

*Proof.* Parametrizing \(\ell=\{a+sd\}\), \(F(a+sd)\) is a polynomial in \(s\) of degree less than \(q-1\), so it suffices that \(\sum_{s\in\mathbb F_q}s^n=0\) for \(0\le n<q-1\). For \(n=0\) the sum is \(q\cdot1=0\). For \(1\le n<q-1\), the polynomial \(T^n-1\) has at most \(n<q-1\) roots, so some \(a\in\mathbb F_q^\times\) has \(a^n\ne1\). Multiplication by \(a\) permutes \(\mathbb F_q\), so \(a^n\sum_ss^n=\sum_s(as)^n=\sum_ss^n\), and the sum vanishes. \(\blacksquare\)

**Lemma 3.3** (the line certificate). There are \(N\times N\) matrices \(H(z)\) over \(\mathbb F_q\), \(z\in P\), with \(\operatorname{rank}H(z)\le1\) and
\[
\sum_{z:\,i\in I(z)}H(z)=-E_{ii}\qquad(i\in I),
\]
where \(E_{ii}\) is the diagonal matrix unit.

*Proof.* For \(i\in I\) with mark \(a_i=(a_{i1},\dots,a_{ih})\in S^h\), put
\[
f_i(X)=\prod_{t=1}^h\ \prod_{a\in S\setminus\{a_{it}\}}\frac{X_t-a}{a_{it}-a}.
\]
This polynomial has total degree at most \(h(|S|-1)\); it is \(1\) at \(a_i\) and \(0\) at every other point of \(S^h\), in particular at the other marks. Let \(f\) be the column of the \(f_i\), and \(H(z)=f(z)f(z)^{\mathsf T}\); it has rank at most \(1\), and \(H(a_i)=E_{ii}\). Every entry of \(H\) is a polynomial of degree at most
\[
2h(|S|-1)<\frac{2hq}{100}=\frac{2q}5<q-1 .
\]
By Lemma 3.2 its sum over the line \(\ell_i\) is zero, so the sum of \(H(z)\) over \(z\in\ell_i\setminus\{a_i\}\), which is exactly the set of \(z\) with \(i\in I(z)\), equals \(-H(a_i)=-E_{ii}\). Other marks on \(\ell_i\), if any, remain in the sum. \(\blacksquare\)

**Theorem 3.4** ([OpenAI-RF, Section 2.5]). No homomorphism from \(G\) onto a finite group keeps every rectangular word nontrivial.

*Proof.* Suppose \(\pi\colon G\to Q\) does, and use the matrices above. Exchanging finite sums and using Lemma 3.3,
\[
\begin{aligned}
&\sum_{z\in P}H(z)\otimes Z(z)\\
&\quad=\sum_{i\in I}\Bigl(\sum_{z:\,i\in I(z)}H(z)\Bigr)\otimes Y_i\\
&\quad=-\sum_{i\in I}E_{ii}\otimes Y_i ,
\end{aligned}
\]
which is the block diagonal matrix \(-\bigoplus_iY_i\). By Proposition 2.2 its rank is at least \(NrD/4\). The image of \(H(z)\otimes Z(z)\) lies in the tensor product of the images, of dimension at most \(\operatorname{rank}Z(z)\), since \(\operatorname{rank}H(z)\le1\). By subadditivity of rank and Lemma 3.1,
\[
\begin{aligned}
\frac{NrD}4&\le2D\,|P\setminus E|+rD\,|E|\\
&\le2mD+r|E|D .
\end{aligned}
\]
Dividing by \(D>0\) contradicts the budget \(Nr/4>2m+r|E|\). \(\blacksquare\)

## 4. Residual finiteness and linear representations

A group is *residually finite* if every nonidentity element has a nonidentity image under some homomorphism to a finite group. The intersection \(R_f(G)\) of the kernels of all homomorphisms from \(G\) to finite groups is its *finite residual*; \(G\) is residually finite exactly when \(R_f(G)=1\).

**Theorem 4.1** (the theorem of the course; [OpenAI-RF, Theorem 1.1]). The group \(G=\pi_1(K)\) is torsion-free and word-hyperbolic, and it is not residually finite: some rectangular word lies in \(R_f(G)\).

*Proof.* Torsion-freeness and hyperbolicity follow from the triangle complex criterion and Lemma 3.1 of the previous lesson (Section 4 there). Suppose that every \(w\in\mathcal R\) has a nonidentity image under some homomorphism \(\varphi_w\colon G\to F_w\) to a finite group. The product homomorphism \(G\to\prod_{w\in\mathcal R}F_w\), followed by its image, is a homomorphism onto a finite group that keeps every rectangular word nontrivial, contradicting Theorem 3.4. So some \(w\in\mathcal R\) has trivial image under every homomorphism to a finite group, that is, \(w\in R_f(G)\); and \(w\ne1\) by Proposition 4.2 of the previous lesson. \(\blacksquare\)

The argument is existential: one member of the finite set \(\mathcal R\) works for all finite quotients, without identifying which one.

**Theorem 4.2** (Malcev). A finitely generated subgroup \(\Gamma\) of \(\mathrm{GL}_n(F)\), for a field \(F\), is residually finite.

*Proof.* Let \(A\subset F\) be the subring generated by the entries of finitely many generators of \(\Gamma\) and of their inverses. Then \(\Gamma\subset\mathrm{GL}_n(A)\), and \(A\) is a domain of finite type over \(\mathbb Z\). The ring \(\mathbb Z\) is a Jacobson ring, so \(A\) is Jacobson, and for every maximal ideal \(\mathfrak n\subset A\) the residue field \(A/\mathfrak n\) is a finite extension of \(\mathbb Z/(p)\) for the prime \(p\) with \(\mathfrak n\cap\mathbb Z=(p)\) ([The Nullstellensatz and Jacobson rings](course:AG-CA/the-nullstellensatz-and-jacobson-rings), Proposition 3.2 and Theorem 4.2). Let \(g\in\Gamma\), \(g\ne1\), and choose a nonzero entry \(a\) of \(g-1\). In the Jacobson domain \(A\) the maximal ideals intersect in \(0\), so some maximal ideal \(\mathfrak n\) does not contain \(a\). Reduction modulo \(\mathfrak n\) is a homomorphism \(\mathrm{GL}_n(A)\to\mathrm{GL}_n(A/\mathfrak n)\) to a finite group, and the image of \(g\) is not \(1\), because the image of \(a\) is not \(0\). \(\blacksquare\)

**Corollary 4.3** ([OpenAI-RF, Corollary 1.2]). For every field \(F\), every \(n\ge1\) and every homomorphism \(\rho\colon G\to\mathrm{GL}_n(F)\), \(R_f(G)\subset\ker\rho\). In particular the nonidentity rectangular word of Theorem 4.1 is killed by all these representations, and \(G\) is not linear over any field.

*Proof.* \(\rho(G)\) is finitely generated, hence residually finite by Theorem 4.2. If \(g\in R_f(G)\) had \(\rho(g)\ne1\), a homomorphism from \(\rho(G)\) to a finite group not killing \(\rho(g)\), composed with \(\rho\), would not kill \(g\), contrary to \(g\in R_f(G)\). \(\blacksquare\)

The corollary does not say that every representation of \(G\) is trivial, and it concerns commutative fields and finite dimensions only.

## 5. Exercises

**5.1.** Show that a finite group \(Q\) acts on itself by left multiplication without fixed points for \(g\ne1\), and compute \(\operatorname{tr}U(g)\).

**5.2.** Give an integer matrix whose rank drops modulo a prime \(q\), and check that Lemma 1.2 is not contradicted.

**5.3.** In Lemma 3.2, show that \(\sum_{s\in\mathbb F_q}s^{q-1}=-1\), so the degree bound cannot be dropped.

**5.4.** Count the choices of \((u,u',v,v')\in[r]^4\) with \(u=u'\) or \(v=v'\).

**5.5.** Why is it essential that \(q\) was chosen before the finite quotient \(Q\)?

## 6. Solutions

**5.1.** \(\pi(g)x=x\) forces \(\pi(g)=1\). So \(U(g)\) has no diagonal entry \(1\) when \(\pi(g)\ne1\), and \(\operatorname{tr}U(g)=0\); for \(\pi(g)=1\) it is the identity, of trace \(D\).

**5.2.** \(M=\bigl(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\bigr)\) has real rank \(2\) and determinant \(-2\), so rank \(1\) modulo \(2\). Its rows have norm \(\sqrt2\), so Lemma 1.2 requires \(q>2\), and indeed for \(q>2\) the rank is \(2\).

**5.3.** Every \(s\ne0\) has \(s^{q-1}=1\), and \(0^{q-1}=0\), so the sum is \(q-1=-1\).

**5.4.** \(r\cdot r^2\) with \(u=u'\), \(r^2\cdot r\) with \(v=v'\), and \(r^2\) with both, so \(2r^3-r^2\).

**5.5.** The rank comparison needs \(q>r\) and the budget of Lemma 1.2 of the previous lesson, which concern the construction only. If \(q\) had to depend on \(Q\), the complex, and so the group, would change with the quotient, and the argument would say nothing about one fixed group.

## References

- [OpenAI-RF] OpenAI, *A torsion-free hyperbolic group that is not residually finite*, OpenAI Math Release preprint, 23 September 2026, Sections 1, 2.4 and 2.5. https://github.com/openai/math/tree/main/preprints/a-torsion-free-hyperbolic-group-that-is-not-residually-finite-September-23-2026
