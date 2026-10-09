# Unitarizability implies amenability

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson completes the proof of OpenAI's theorem [OpenAI-U, Sections 2 and 5], which answers Dixmier's question for discrete groups.

**Theorem 4.1** (OpenAI). A discrete group is amenable if and only if it is unitarizable. If \(G\) is not amenable, then for every \(\varepsilon>0\) there is a representation \(\pi\) of \(G\) by bounded invertible operators on a complex Hilbert space, with \(\|\pi(g)\|\le1+\varepsilon\) for all \(g\), that is not similar to a unitary representation; the Hilbert space can be chosen separable when \(G\) is countable.

The last ingredient is a lower bound for the distance from an operator \(T\) on \(\ell^2(G;\mathbb C^k)\) to the commutant of the translations (Lemma 1.1). It compares one block row of \(T\) and one block column of \(A-T\) with the Hilbert–Schmidt energy of a translation-invariant operator \(A\). The operators of [Random sign frames and masked operators](random-sign-frames-and-masked-operators.md) have bounded rows, columns and conjugation differences, while their energy per fibre dimension grows without bound. A direct sum of their cocycles is then bounded but not inner (Proposition 2.1), and Proposition 2.2 of [Uniformly bounded representations](uniformly-bounded-representations.md) turns it into the required representation.

We use: from [Uniformly bounded representations](uniformly-bounded-representations.md), Proposition 1.1, Theorem 1.2, Example 2.1, Proposition 2.2, Lemma 3.1 and Lemma 3.3; from [Contracting averages and sparse assignments](contracting-averages-and-sparse-assignments.md), Lemma 1.2, Proposition 3.2 and Corollary 3.3; from [Random sign frames and masked operators](random-sign-frames-and-masked-operators.md), Proposition 1.5, Corollary 3.1, Proposition 3.2 and Lemma 3.3. Section 5 also uses Proposition 1.3 of [Thompson's group F and dyadic partitions](course:thompsons-group-f-and-amenability/thompsons-group-f-and-dyadic-partitions#1-the-group), Theorem 5.1 of [Thompson's group F is not amenable](course:thompsons-group-f-and-amenability/thompsons-group-f-is-not-amenable#5-the-theorem), and Kadison's similarity theorem, [Theorem 2.1 of Kadison's similarity theorem](course:kadisons-similarity-problem/kadisons-similarity-theorem#2-the-similarity-theorem).

## 1. Distance from the translation commutant

Let \(G\) be a countable group and \(k\ge1\). On \(\mathcal H_k=\ell^2(G;\mathbb C^k)\) let \((U_k(g)\xi)(x)=\xi(g^{-1}x)\), let \(\iota_x:\mathbb C^k\to\mathcal H_k\) be the inclusion at \(x\) and \(q_x=\iota_x^*\). For \(F\in B(\mathcal H_k)\) put \(F[x,y]=q_xF\iota_y\), a \(k\times k\) matrix, and
\[
\operatorname{row}_e(F)=q_eF:\mathcal H_k\to\mathbb C^k,\qquad\operatorname{col}_e(F)=F\iota_e:\mathbb C^k\to\mathcal H_k.
\]
Let \(U_k(G)'\) be the set of bounded operators commuting with every \(U_k(g)\). Since \(U_k(g)\iota_y=\iota_{gy}\) and \(q_xU_k(x)=q_e\), every \(F\in U_k(G)'\) satisfies
\[
F[x,y]=q_xFU_k(x)\iota_{x^{-1}y}=q_xU_k(x)F\iota_{x^{-1}y}=F[e,x^{-1}y].\tag{1.1}
\]
Two Hilbert–Schmidt computations are used. If \(R:\mathcal H_k\to\mathbb C^k\) is bounded, then, with the orthonormal bases \((\iota_se_b)\) of \(\mathcal H_k\) and \((e_a)\) of \(\mathbb C^k\),
\[
\sum_{s\in G}\|R\iota_s\|_{\rm HS}^2=\sum_{s,b}\sum_a|\langle\iota_se_b,R^*e_a\rangle|^2=\sum_a\|R^*e_a\|^2\le k\|R\|^2.\tag{1.2}
\]
If \(L:\mathbb C^k\to\mathcal H_k\) is bounded, then
\[
\sum_{x\in G}\|q_xL\|_{\rm HS}^2=\sum_b\sum_x\|q_xLe_b\|^2=\sum_b\|Le_b\|^2\le k\|L\|^2.\tag{1.3}
\]

**Lemma 1.1.** Let \(A,T\in B(\mathcal H_k)\) with \(A\in U_k(G)'\), write \(A[x,y]=W(x^{-1}y)\) and \(E=\sum_s\|W(s)\|_{\rm HS}^2\), and suppose that \(\|\operatorname{row}_e(T)\|\le K\) and \(\|\operatorname{col}_e(A-T)\|\le K\). Then every \(C\in U_k(G)'\) satisfies
\[
E\le4k\bigl(K+\|T-C\|\bigr)^2,\qquad\text{hence}\qquad\inf_{C\in U_k(G)'}\|T-C\|\ge\frac12\sqrt{\frac Ek}-K.
\]

**Proof.** Put \(B=T-C\), \(h=K+\|B\|\) and \(Q(s)=C[e,s]\), so \(C[x,y]=Q(x^{-1}y)\) by (1.1). The row \(\operatorname{row}_e(C)=\operatorname{row}_e(T)-\operatorname{row}_e(B)\) has norm at most \(h\), and its blocks are \(q_eC\iota_s=Q(s)\); by (1.2), \(\sum_s\|Q(s)\|_{\rm HS}^2\le kh^2\). The column \(\operatorname{col}_e(A-C)=\operatorname{col}_e(A-T)+\operatorname{col}_e(B)\) has norm at most \(h\), and its blocks are \((A-C)[x,e]=W(x^{-1})-Q(x^{-1})\); by (1.3) and the bijection \(x\mapsto x^{-1}\), \(\sum_s\|W(s)-Q(s)\|_{\rm HS}^2\le kh^2\). The triangle inequality for square-summable families of matrices in the Hilbert–Schmidt norm gives \(\sqrt E\le2\sqrt k\,h\). \(\square\)

## 2. A cocycle without a bounded implementer

**Proposition 2.1.** Let \(G\) be countable. For \(j\in\mathbb N\) let \(k_j\ge1\), \(\mathcal H_j=\ell^2(G;\mathbb C^{k_j})\) with the representation \(U_j\) as above, and \(A_j,T_j\in B(\mathcal H_j)\) with \(A_j\in U_j(G)'\), \(A_j[x,y]=W_j(x^{-1}y)\) and \(E_j=\sum_s\|W_j(s)\|_{\rm HS}^2\). Suppose that one constant \(K\) satisfies
\[
\|\operatorname{row}_e(T_j)\|\le K,\qquad\|\operatorname{col}_e(A_j-T_j)\|\le K,\qquad\|T_j-U_j(g)T_jU_j(g)^{-1}\|\le K
\]
for all \(j\) and \(g\), and that \(E_j/k_j\to\infty\). Then \(G\) has a representation on a separable Hilbert space with \(\sup_g\|\pi(g)\|\le1+K\) that is not unitarizable. No bound on \(\|T_j\|\) or \(\|A_j\|\) is needed.

**Proof.** On \(\mathcal H=\bigoplus_j\mathcal H_j\) let \(U=\bigoplus_jU_j\), a unitary representation, and \(D(g)=\bigoplus_jD_j(g)\) with \(D_j(g)=T_j-U_j(g)T_jU_j(g)^{-1}\). Each \(D_j\) satisfies the cocycle identity (Example 2.1 of the first lesson), \(\|D(g)\|\le K\), and so \(D\) is a bounded operator cocycle for \(U\). The space \(\mathcal H\) is separable because \(G\) is countable. Let \(\pi\) on \(\mathcal H\oplus\mathcal H\) be the representation of Proposition 2.2 of the first lesson; it satisfies \(\|\pi(g)\|\le1+K\).

Suppose \(\pi\) were unitarizable. By Proposition 2.2 of the first lesson there is \(B\in B(\mathcal H)\) with \(D(g)=B-U(g)BU(g)^{-1}\). Let \(I_j:\mathcal H_j\to\mathcal H\) be the inclusion and \(B_j=I_j^*BI_j\), so \(\|B_j\|\le\|B\|\). Since \(U(g)I_j=I_jU_j(g)\) and \(I_j^*U(g)=U_j(g)I_j^*\), compressing gives \(D_j(g)=B_j-U_j(g)B_jU_j(g)^{-1}\). Comparing with the definition of \(D_j\), the operator \(C_j=T_j-B_j\) commutes with every \(U_j(g)\). Lemma 1.1 with \(C=C_j\) gives
\[
E_j\le4k_j\bigl(K+\|B_j\|\bigr)^2\le4k_j\bigl(K+\|B\|\bigr)^2
\]
for every \(j\), contradicting \(E_j/k_j\to\infty\). \(\square\)

Each \(D_j\) separately is inner, implemented by \(T_j\). Lemma 1.1 shows that every implementer of \(D_j\) has norm at least \(\frac12\sqrt{E_j/k_j}-K\), and these lower bounds are unbounded in \(j\). The argument assumes a similarity for the single representation \(\pi\) and needs no a priori bound on similarities.

## 3. Countable nonamenable groups

**Theorem 3.1.** Let \(G\) be a countable nonamenable group and \(\varepsilon>0\). There is a representation of \(G\) on a separable Hilbert space with \(\sup_g\|\pi(g)\|\le1+\varepsilon\) that is not unitarizable.

**Proof.** Choose \(S\), \(d\ge2\) and \(\rho<1\) by Lemma 1.2 of the lesson on contracting averages. For \(\ell\ge1\) let \(n_\ell=d^\ell\ge2\), \(r_\ell=\lceil n_\ell\rho^\ell\rceil\), let \(s_1,\dots,s_{n_\ell}\) be the products of the words of length \(\ell\) in \(S\), and let \(a_\ell\) be the assignment of Proposition 3.2 of that lesson. With \(n=n_\ell\) and \(r=r_\ell\) choose \(k_\ell=\lceil2r_\ell\log(2n_\ell)\rceil\) and unit vectors \(v_1,\dots,v_{n_\ell}\in\mathbb C^{k_\ell}\) by Proposition 1.5 of the lesson on frames, and form the operators \(A_\ell=T_{\mathbf1}\) and \(T_\ell=T_{a_\ell}\) on \(\mathcal H_\ell=\ell^2(G;\mathbb C^{k_\ell})\) as in Section 3 of that lesson. By its Corollary 3.1 and Proposition 3.2,
\[
\|q_eT_\ell\|\le100,\qquad\|(A_\ell-T_\ell)\iota_e\|\le100,\qquad\|T_\ell-U_\ell(g)T_\ell U_\ell(g)^{-1}\|\le100,
\]
and \(A_\ell\) commutes with \(U_\ell\). By its Lemma 3.3 the kernel \(W_\ell\) of \(A_\ell\) has energy \(E_\ell\ge n_\ell\). Moreover
\[
\frac{k_\ell}{n_\ell}\le\frac{2r_\ell\log(2n_\ell)+1}{n_\ell}\longrightarrow0
\]
by Corollary 3.3 of the lesson on contracting averages, so \(E_\ell/k_\ell\ge n_\ell/k_\ell\to\infty\).

Put \(t=\varepsilon/100\) and apply Proposition 2.1 to \(tA_\ell\) and \(tT_\ell\). The three bounds hold with \(K=100t=\varepsilon\); the kernel of \(tA_\ell\) is \(tW_\ell\), with energy \(t^2E_\ell\), and \(t^2E_\ell/k_\ell\to\infty\). \(\square\)

## 4. All discrete groups

**Proof of Theorem 4.1.** If \(G\) is amenable, it is unitarizable by Theorem 1.2 of the first lesson. Suppose \(G\) is not amenable and let \(\varepsilon>0\). By Lemma 3.3 of the first lesson, \(G\) has a finitely generated nonamenable subgroup \(K\), which is countable. Theorem 3.1 gives a representation \(\sigma\) of \(K\) on a separable Hilbert space \(E\) with \(|\sigma|\le1+\varepsilon\) that is not unitarizable. The induced representation \(\Pi\) of Lemma 3.1 of the first lesson acts on \(\ell^2(G/K;E)\), has \(|\Pi|=|\sigma|\le1+\varepsilon\), and is not unitarizable, since \(\sigma\) would otherwise be. If \(G\) is countable, \(\ell^2(G/K;E)\) is separable. So a nonamenable group is not unitarizable. \(\square\)

For an uncountable nonamenable group, the subgroup \(K\) has uncountable index and the induced representation acts on a nonseparable space; unitarizability is defined with all Hilbert spaces, so this is allowed. The theorem concerns discrete groups; for locally compact groups representations are usually required to be strongly continuous, and the argument does not address that setting.

## 5. Consequences

**Corollary 5.1** (Thompson's group). For every \(\varepsilon>0\), Thompson's group \(F\) has a representation on a separable Hilbert space with \(\sup_{g\in F}\|\pi(g)\|\le1+\varepsilon\) that is not similar to a unitary representation.

**Proof.** \(F\) is a countable group (Proposition 1.3 of the lesson on dyadic partitions) and is not amenable (Theorem 5.1 of the lesson [Thompson's group F is not amenable](course:thompsons-group-f-and-amenability/thompsons-group-f-is-not-amenable#5-the-theorem)). Apply Theorem 3.1. \(\square\)

Let \(G\) be a discrete group. The group algebra \(\mathbb C[G]\) of finitely supported functions carries the convolution product and the involution \(f^*(g)=\overline{f(g^{-1})}\). For a unitary representation \(u\) put \(u(f)=\sum_gf(g)u(g)\); then \(\|u(f)\|\le\|f\|_1\). The number \(\|f\|_{\max}=\sup_u\|u(f)\|\), the supremum over all unitary representations, is a C\*-seminorm on \(\mathbb C[G]\), and a norm because the left regular representation \(\lambda\) gives \(\|f\|_{\max}\ge\|\lambda(f)\delta_e\|=\|f\|_2\). The completion is the *full group C\*-algebra* \(C^*(G)\); write \(u_g\) for the image of \(\delta_g\), a unitary. Every unitary representation \(u\) extends to a unital \(*\)-homomorphism of \(C^*(G)\) sending \(u_g\) to \(u(g)\). The *reduced group C\*-algebra* \(C^*_r(G)\) is the norm closure of \(\lambda(\mathbb C[G])\) in \(B(\ell^2(G))\), and \(\lambda\) extends to a unital \(*\)-homomorphism \(q:C^*(G)\to C^*_r(G)\) with \(q(u_g)=\lambda_g\).

**Theorem 5.2.** Let \(G\) be a discrete group and \(\pi:G\to GL(H)\) a uniformly bounded representation that is not unitarizable.

(a) \(T_\pi(f)=\sum_gf(g)\pi(g)\) defines a bounded unital homomorphism \(T_\pi:\ell^1(G)\to B(H)\) with \(\|T_\pi(f)\|\le|\pi|\,\|f\|_1\).

(b) There is no bounded unital homomorphism \(\Phi:C^*(G)\to B(H)\) with \(\Phi(u_g)=\pi(g)\) for all \(g\).

(c) There is no bounded unital homomorphism \(\Psi:C^*_r(G)\to B(H)\) with \(\Psi(\lambda_g)=\pi(g)\) for all \(g\).

By Theorem 4.1, every nonamenable discrete group has such representations \(\pi\) with \(|\pi|\le1+\varepsilon\), for every \(\varepsilon>0\).

**Proof.** (a) The series converges absolutely in norm. For \(f,f'\in\ell^1(G)\), absolute convergence allows rearrangement:
\[
T_\pi(f*f')=\sum_g\sum_hf(h)f'(h^{-1}g)\pi(g)=\sum_h\sum_{k}f(h)f'(k)\pi(h)\pi(k)=T_\pi(f)T_\pi(f'),
\]
and \(T_\pi(\delta_e)=1\).

(b) Suppose \(\Phi\) exists. By Kadison's similarity theorem there is an invertible \(S\in B(H)\) such that \(a\mapsto S\Phi(a)S^{-1}\) is a \(*\)-homomorphism; it is unital. A unital \(*\)-homomorphism maps unitaries to unitaries, so every \(S\pi(g)S^{-1}=S\Phi(u_g)S^{-1}\) is unitary, and \(\pi\) is unitarizable, a contradiction.

(c) If \(\Psi\) existed, \(\Psi\circ q\) would contradict (b). \(\square\)

So for a nonamenable group the norm \(\|f\|_1\) controls \(T_\pi\) on \(\mathbb C[G]\), but neither C\*-norm does. For an amenable group every uniformly bounded representation has the form \(S^{-1}V(\cdot)S\) with \(V\) unitary (Theorem 1.2 of the first lesson), and \(\Phi(a)=S^{-1}\bar V(a)S\), with \(\bar V\) the extension of \(V\) to \(C^*(G)\), is a bounded extension.

## 6. Remarks

**Ulam stability.** The same OpenAI family contains a second theorem [OpenAI-UL]. A map \(\mu:G\to U(H)\) into the unitary group with \(\mu(e)=1\) has *defect* \(\sup_{g,h}\|\mu(gh)-\mu(g)\mu(h)\|\), and a countable group is *strongly Ulam stable* if for every \(\varepsilon>0\) there is \(\delta>0\) such that every such map of defect at most \(\delta\), on any Hilbert space, lies within \(\varepsilon\) of a unitary representation on the same space, uniformly on \(G\). Kazhdan proved that amenable groups are strongly Ulam stable, and OpenAI proved the converse for countable groups [OpenAI-UL, Theorem 1.1]. That proof uses a different construction and is not part of this course.

**Earlier partial results.** Before Theorem 4.1, non-unitarizable representations were known for groups containing a free subgroup of rank two (see [Pi]), for residually finite groups with positive first \(\ell^2\)-Betti number [EM], and for wreath products \(A\wr G\) with \(A\) an infinite abelian group and \(G\) nonamenable [MO]; the survey [Pi] describes the state of the question in 2004.

## 7. Exercises

**Exercise 7.1** (easy). Let \(A\in U_k(G)'\) have kernel \(W\) with energy \(E\). Show directly that \(\|q_eA\|\ge\sqrt{E/k}\). Explain why Lemma 1.1 nevertheless needs the decomposition \(A=T+(A-T)\): what does it bound that \(\|q_eA\|\) does not?

**Exercise 7.2** (easy). Show that a quotient of a unitarizable group is unitarizable. Deduce from Theorem 4.1 that a quotient of an amenable group is amenable.

**Exercise 7.3** (easy). In Theorem 5.2(a), show that the operator norm of \(T_\pi:\ell^1(G)\to B(H)\) equals \(|\pi|\).

**Exercise 7.4** (medium). Show that every group containing Thompson's group \(F\) as a subgroup has, for every \(\varepsilon>0\), a representation with \(\sup_g\|\pi(g)\|\le1+\varepsilon\) that is not unitarizable.

## 8. Solutions

**7.1.** The blocks of \(q_eA\) are \(A[e,s]=W(s)\), so by (1.2), \(E=\sum_s\|q_eA\iota_s\|_{\rm HS}^2\le k\|q_eA\|^2\). This bounds the norm of \(A\) from below, but \(A\) itself commutes with \(U_k\), so its cocycle \(D_A\) is \(0\). Lemma 1.1 bounds the distance from \(T\) to every \(C\) commuting with \(U_k\). If \(C\) were close to \(T\), the row of \(C\) at \(e\) would be small, as that of \(T\) is, and the column of \(A-C\) at \(e\) would be small, as that of \(A-T\) is. By (1.1) the row and the column of \(C\) at \(e\) carry the same kernel \(Q\), so \(W=Q+(W-Q)\) would split into two families of small energy, which is impossible when \(E/k\) is large. The decomposition \(A=T+(A-T)\) puts the energy of \(W\) into a row of \(T\) and a column of \(A-T\) of bounded norm.

**7.2.** If \(N\) is normal in \(G\) and \(\pi\) is a uniformly bounded representation of \(G/N\), then \(\pi\circ p\), with \(p:G\to G/N\) the quotient map, is a uniformly bounded representation of \(G\) with the same operators. A similarity unitarizing \(\pi\circ p\) unitarizes \(\pi\). If \(G\) is amenable, it is unitarizable by Theorem 1.2 of the first lesson, so \(G/N\) is unitarizable and, by Theorem 4.1, amenable.

**7.3.** \(\|T_\pi(f)\|\le\sum_g|f(g)|\,\|\pi(g)\|\le|\pi|\|f\|_1\), and \(T_\pi(\delta_g)=\pi(g)\) with \(\|\delta_g\|_1=1\), so the norm is \(\sup_g\|\pi(g)\|=|\pi|\).

**7.4.** Let \(G\supseteq F'\cong F\). By Corollary 5.1, \(F'\) has a non-unitarizable representation \(\sigma\) with \(|\sigma|\le1+\varepsilon\), and Lemma 3.1 of the first lesson induces it to \(G\) with the same bound and without a unitarizing similarity.

## References

- [EM] I. Epstein and N. Monod, *Nonunitarizable representations and random forests*, Int. Math. Res. Not. IMRN 2009; arXiv:0811.3422. https://arxiv.org/abs/0811.3422
- [MO] N. Monod and N. Ozawa, *The Dixmier problem, lamplighters and Burnside groups*, J. Funct. Anal. 258 (2010); arXiv:0902.4585. https://arxiv.org/abs/0902.4585
- [OpenAI-U] OpenAI, *Unitarizability implies amenability for discrete groups*, OpenAI Math Release preprint, 23 September 2026, Sections 2, 5 and 6. https://github.com/openai/math/blob/main/preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026
- [OpenAI-UL] OpenAI, *Strong Ulam stability characterizes amenability*, OpenAI Math Release preprint, 5 October 2026, Theorem 1.1. https://github.com/openai/math/blob/main/preprints/Strong-Ulam-Stability-Characterizes-Amenability-October-5-2026
- [Pi] G. Pisier, *Are unitarizable groups amenable?*, in: Infinite Groups: Geometric, Combinatorial and Dynamical Aspects, Progr. Math. 248, Birkhäuser, 2005; arXiv:math/0405282. https://arxiv.org/abs/math/0405282
