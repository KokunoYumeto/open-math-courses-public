# Uniformly bounded representations

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A representation of a group by bounded invertible operators on a Hilbert space is *uniformly bounded* if the norms of all its operators have a common bound. Every unitary representation is uniformly bounded, and so is every representation of the form \(g\mapsto S\,u(g)\,S^{-1}\) with \(u\) unitary and \(S\) a fixed bounded invertible operator. Day and Dixmier showed in 1950 that for an amenable group nothing else occurs: every uniformly bounded representation is of that form (Theorem 1.2). Dixmier asked whether this property characterizes amenable groups. Ehrenpreis and Mautner found uniformly bounded representations of \(SL_2(\mathbb R)\) that are not similar to unitary ones, and such representations were later found for free groups, hence for every group with a free subgroup of rank two; the survey [Pi] describes this work, and [EM] and [MO] treat further classes of groups. OpenAI proved in September 2026 that the answer is yes for every discrete group [OpenAI-U]:

**Theorem.** A discrete group is amenable if and only if every uniformly bounded representation of it on a complex Hilbert space is similar to a unitary representation. If the group is not amenable, then for every \(\varepsilon>0\) it has such a representation with all norms at most \(1+\varepsilon\) that is not similar to a unitary one, on a separable Hilbert space if the group is countable.

This course proves the theorem. The present lesson collects the general facts: similarity to a unitary representation as an invariant inner product (Proposition 1.1), the theorem of Day and Dixmier (Theorem 1.2), representations built from operator cocycles (Proposition 2.2), and two ways of passing between a group and its subgroups (Lemmas 3.1 and 3.3). The lesson [Contracting averages and sparse assignments](contracting-averages-and-sparse-assignments.md) turns nonamenability into a combinatorial structure, the lesson [Random sign frames and masked operators](random-sign-frames-and-masked-operators.md) turns that structure into operators, and the lesson [Unitarizability implies amenability](unitarizability-implies-amenability.md) proves the theorem.

We use: Theorem 3.1 of [Hilbert spaces and compact operators](course:foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators#OA-FND-HS-03) (a bounded sesquilinear form \(B\) is \(B(\xi,\eta)=\langle t\xi,\eta\rangle\) for a unique bounded \(t\), with \(\langle t\xi,\xi\rangle\ge0\) when \(B\) is positive); Proposition 8.5(10) of [C\*-algebras: continuous functional calculus](course:foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones#OA-FND-CF-15) (positive square roots in a C\*-algebra, commuting with everything that commutes with the given element); the inverse mapping theorem, [Corollary 5.2 of the Banach space lesson](course:foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces#OA-FND-HB-05); the Banach–Alaoglu theorem, [Theorem 3.1 of the weak topologies lesson](course:foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian#OA-FND-WT-03); and the definition of amenability by invariant means in Section 1 of [Means, Følner sets, and regular representations](course:OA-ERGODIC/reader/means-folner-sets-and-regular-representations#1-invariant-averaging).

## 1. Similarity to unitary representations

Throughout, \(G\) is a group, regarded as a discrete group, and Hilbert spaces are complex. For a Hilbert space \(H\), \(GL(H)\) is the group of bounded operators on \(H\) with bounded inverse. A *representation* \(\pi:G\to GL(H)\) is a homomorphism, and it is *uniformly bounded* if
\[
|\pi|=\sup_{g\in G}\|\pi(g)\|<\infty.
\]
Then \(\|\pi(g)^{-1}\|=\|\pi(g^{-1})\|\le|\pi|\) as well. The representation is *unitarizable* if some \(S\in GL(H)\) makes every \(S\pi(g)S^{-1}\) unitary, and the group \(G\) is *unitarizable* if every uniformly bounded representation of \(G\) on every complex Hilbert space is unitarizable.

An inner product \([\cdot,\cdot]\) on \(H\) is *equivalent* to \(\langle\cdot,\cdot\rangle\) if \(a\|\xi\|^2\le[\xi,\xi]\le b\|\xi\|^2\) for some constants \(0<a\le b\).

**Proposition 1.1.** For a uniformly bounded representation \(\pi:G\to GL(H)\) the following are equivalent:

(a) \(\pi\) is unitarizable;

(b) there is a bounded self-adjoint operator \(Q\) with \(a\le Q\le b\) for constants \(0<a\le b\) such that \(\pi(g)^*Q\pi(g)=Q\) for every \(g\);

(c) \(H\) carries an equivalent inner product \([\cdot,\cdot]\) with \([\pi(g)\xi,\pi(g)\eta]=[\xi,\eta]\) for all \(g,\xi,\eta\).

**Proof.** (a) ⇒ (b). Let \(V(g)=S\pi(g)S^{-1}\) be unitary and put \(Q=S^*S\). Then \(\pi(g)=S^{-1}V(g)S\) and \(\pi(g)^*Q\pi(g)=S^*V(g)^*V(g)S=Q\). Moreover \(\langle Q\xi,\xi\rangle=\|S\xi\|^2\) lies between \(\|S^{-1}\|^{-2}\|\xi\|^2\) and \(\|S\|^2\|\xi\|^2\).

(b) ⇒ (c). Put \([\xi,\eta]=\langle Q\xi,\eta\rangle\).

(c) ⇒ (b). The form \([\cdot,\cdot]\) is bounded: by the Cauchy–Schwarz inequality for it, \(|[\xi,\eta]|\le[\xi,\xi]^{1/2}[\eta,\eta]^{1/2}\le b\|\xi\|\|\eta\|\). Theorem 3.1 of the Hilbert space lesson gives a bounded \(Q\) with \([\xi,\eta]=\langle Q\xi,\eta\rangle\); it is self-adjoint because \(\langle Q\xi,\xi\rangle=[\xi,\xi]\) is real, and \(a\le Q\le b\). Invariance gives \(\langle\pi(g)^*Q\pi(g)\xi,\eta\rangle=[\pi(g)\xi,\pi(g)\eta]=[\xi,\eta]=\langle Q\xi,\eta\rangle\).

(b) ⇒ (a). First, \(Q\) is invertible: \(a\|\xi\|^2\le\langle Q\xi,\xi\rangle\le\|Q\xi\|\|\xi\|\) gives \(\|Q\xi\|\ge a\|\xi\|\), so \(Q\) is injective with closed range, and the range is dense because its orthogonal complement is \(\ker Q^*=\ker Q=0\). So \(Q\) is a bijection, and \(\|Q^{-1}\|\le1/a\). Let \(S=Q^{1/2}\) be the positive square root (Proposition 8.5(10) of the C\*-algebra lesson). It commutes with \(Q\), hence with \(Q^{-1}\), and \(S\cdot SQ^{-1}=SQ^{-1}\cdot S=1\); so \(S\in GL(H)\). Now \(V(g)=S\pi(g)S^{-1}\) is invertible and
\[
V(g)^*V(g)=S^{-1}\pi(g)^*S^2\pi(g)S^{-1}=S^{-1}QS^{-1}=1,
\]
so \(V(g)\) is an invertible isometry, that is, a unitary. \(\square\)

**Theorem 1.2** (Day, Dixmier). Every amenable group is unitarizable.

**Proof.** Let \(m\) be a left invariant mean on \(\ell^\infty(G)\): a positive linear functional with \(m(1)=1\) and \(m(L_hf)=m(f)\), where \((L_hf)(x)=f(h^{-1}x)\). A positive functional takes real values on real functions, so \(m(\bar f)=\overline{m(f)}\). Put \(m_{\rm r}(f)=m(x\mapsto f(x^{-1}))\). It is again positive with \(m_{\rm r}(1)=1\), and it is right invariant: the function \(x\mapsto f(x^{-1}h)\) is \(L_h\) applied to \(x\mapsto f(x^{-1})\), so \(m_{\rm r}(x\mapsto f(xh))=m_{\rm r}(f)\).

Let \(\pi:G\to GL(H)\) be uniformly bounded, \(M=|\pi|\). For \(\xi,\eta\in H\) the function \(g\mapsto\langle\pi(g)\xi,\pi(g)\eta\rangle\) is bounded by \(M^2\|\xi\|\|\eta\|\); put
\[
[\xi,\eta]=m_{\rm r}\bigl(g\mapsto\langle\pi(g)\xi,\pi(g)\eta\rangle\bigr).
\]
This is linear in \(\xi\), conjugate-linear in \(\eta\), and \([\eta,\xi]=\overline{[\xi,\eta]}\). Since \(\|\xi\|=\|\pi(g)^{-1}\pi(g)\xi\|\le M\|\pi(g)\xi\|\), the function \(g\mapsto\|\pi(g)\xi\|^2\) takes values in \([M^{-2}\|\xi\|^2,M^2\|\xi\|^2]\), and positivity of \(m_{\rm r}\) gives \(M^{-2}\|\xi\|^2\le[\xi,\xi]\le M^2\|\xi\|^2\). So \([\cdot,\cdot]\) is an equivalent inner product. For \(h\in G\), the function \(g\mapsto\langle\pi(gh)\xi,\pi(gh)\eta\rangle\) is the right translate by \(h\) of the function defining \([\xi,\eta]\), so \([\pi(h)\xi,\pi(h)\eta]=[\xi,\eta]\). Proposition 1.1 shows that \(\pi\) is unitarizable. \(\square\)

## 2. Operator cocycles

Let \(U:G\to GL(H)\) be a unitary representation. A *bounded operator cocycle* for \(U\) is a map \(D:G\to B(H)\) with \(\sup_g\|D(g)\|<\infty\) and
\[
D(gh)=D(g)+U(g)D(h)U(g)^{-1}\qquad(g,h\in G).\tag{2.1}
\]
It is *inner* if there is \(B\in B(H)\) with \(D(g)=B-U(g)BU(g)^{-1}\) for all \(g\).

**Example 2.1.** For every \(T\in B(H)\), the map \(D_T(g)=T-U(g)TU(g)^{-1}\) satisfies (2.1):
\[
D_T(g)+U(g)D_T(h)U(g)^{-1}=T-U(g)TU(g)^{-1}+U(g)TU(g)^{-1}-U(gh)TU(gh)^{-1}=D_T(gh).
\]
It is inner, implemented by \(T\). The construction of the course takes direct sums of cocycles \(D_{T_j}\) on spaces \(H_j\) for which \(\sup_{j,g}\|D_{T_j}(g)\|<\infty\) while \(\|T_j\|\) is unbounded. The direct sum of the \(D_{T_j}\) is a bounded cocycle, and the question is whether some other bounded operator implements it.

**Proposition 2.2.** Let \(D\) be a bounded operator cocycle for a unitary representation \(U\) on \(H\). On \(H\oplus H\),
\[
\pi(g)=\begin{pmatrix}U(g)&D(g)U(g)\\0&U(g)\end{pmatrix}
\]
defines a uniformly bounded representation with \(\|\pi(g)\|\le1+\|D(g)\|\). If \(\pi\) is unitarizable, then \(D\) is inner.

**Proof.** Setting \(g=h=e\) in (2.1) gives \(D(e)=0\), so \(\pi(e)=1\). The upper right entry of \(\pi(g)\pi(h)\) is \(U(g)D(h)U(h)+D(g)U(g)U(h)\), which equals \(D(gh)U(gh)\) by (2.1) applied after multiplication by \(U(gh)\) on the right. So \(\pi(g)\pi(h)=\pi(gh)\), and \(\pi(g)^{-1}=\pi(g^{-1})\). The factorization
\[
\pi(g)=\begin{pmatrix}1&D(g)\\0&1\end{pmatrix}\begin{pmatrix}U(g)&0\\0&U(g)\end{pmatrix}
\]
into the identity plus an operator of norm \(\|D(g)\|\) and a unitary gives the norm bound.

Suppose \(S\in GL(H\oplus H)\) makes every \(V(g)=S\pi(g)S^{-1}\) unitary. The closed subspace \(M=H\oplus0\) satisfies \(\pi(g)M\subseteq M\) for every \(g\), hence \(\pi(g)^{-1}M=\pi(g^{-1})M\subseteq M\). So the closed subspace \(SM\) is invariant under every \(V(g)\) and \(V(g)^{-1}=V(g)^*\), and therefore its orthogonal complement is invariant under every \(V(g)\). Thus \(N=S^{-1}((SM)^\perp)\) is a closed subspace, invariant under every \(\pi(g)\), with \(M\cap N=0\) and \(M+N=H\oplus H\), because \(SM\) and \((SM)^\perp\) have these properties and \(S\) is a linear homeomorphism.

Let \(P_1,P_2:H\oplus H\to H\) be the coordinate projections. The restriction \(P_2|_N:N\to H\) is injective, since its kernel is \(M\cap N\), and surjective, since \((0,\eta)=m+n\) with \(m\in M\), \(n\in N\) gives \(P_2n=\eta\). By the inverse mapping theorem it has a bounded inverse, and \(B=P_1(P_2|_N)^{-1}\in B(H)\) satisfies \(N=\{(B\eta,\eta):\eta\in H\}\). Invariance of \(N\) under \(\pi(g)\) says that \(\pi(g)(B\eta,\eta)=(U(g)B\eta+D(g)U(g)\eta,\ U(g)\eta)\) lies in \(N\), that is,
\[
U(g)B\eta+D(g)U(g)\eta=BU(g)\eta\qquad(\eta\in H).
\]
Substituting \(\eta=U(g)^{-1}\zeta\) gives \(D(g)=B-U(g)BU(g)^{-1}\). \(\square\)

The converse holds as well (Exercise 5.2).

## 3. Subgroups

**Lemma 3.1** (induction). Let \(K\) be a subgroup of \(G\) and \(\sigma:K\to GL(E)\) a uniformly bounded representation. There is a uniformly bounded representation \(\Pi\) of \(G\) on \(\ell^2(G/K;E)\) with \(|\Pi|=|\sigma|\). If \(\Pi\) is unitarizable, so is \(\sigma\). If \(G\) is countable and \(E\) separable, then \(\ell^2(G/K;E)\) is separable.

**Proof.** Let \(X=G/K\) be the set of left cosets and choose representatives \(s:X\to G\), \(s(x)\in x\), with \(s(K)=e\). For \(g\in G\) and \(x\in X\) put \(c(g,x)=s(gx)^{-1}g\,s(x)\). Since \(g\,s(x)\in gx=s(gx)K\), we have \(c(g,x)\in K\). Directly,
\[
c(gh,x)=s(ghx)^{-1}g\,s(hx)\cdot s(hx)^{-1}h\,s(x)=c(g,hx)\,c(h,x),\qquad c(e,x)=e.
\]
For \(\xi=(\xi_x)_{x\in X}\) in the Hilbert direct sum \(\ell^2(X;E)\) define \(\Pi(g)\xi\) by \((\Pi(g)\xi)_{gx}=\sigma(c(g,x))\xi_x\). As \(x\mapsto gx\) is a bijection of \(X\), \(\|\Pi(g)\xi\|^2=\sum_x\|\sigma(c(g,x))\xi_x\|^2\le|\sigma|^2\|\xi\|^2\). The cocycle identity gives
\[
(\Pi(g)\Pi(h)\xi)_{ghx}=\sigma(c(g,hx))\sigma(c(h,x))\xi_x=\sigma(c(gh,x))\xi_x=(\Pi(gh)\xi)_{ghx},
\]
and \(\Pi(e)=1\), so \(\Pi\) is a representation with \(|\Pi|\le|\sigma|\).

Let \(j:E\to\ell^2(X;E)\) be the isometric inclusion at the coset \(K\). For \(k\in K\) we have \(kK=K\) and \(c(k,K)=s(K)^{-1}k\,s(K)=k\), so \(\Pi(k)j=j\sigma(k)\). Hence \(\|\sigma(k)\|\le\|\Pi(k)\|\), and \(|\Pi|=|\sigma|\).

If \(\Pi\) is unitarizable, Proposition 1.1 gives \(Q\) with \(a\le Q\le b\) and \(\Pi(g)^*Q\Pi(g)=Q\). The compression \(Q_K=j^*Qj\) satisfies \(a\le Q_K\le b\), and for \(k\in K\), using \(\Pi(k)j=j\sigma(k)\),
\[
\sigma(k)^*Q_K\sigma(k)=j^*\Pi(k)^*Q\Pi(k)j=j^*Qj=Q_K.
\]
By Proposition 1.1, \(\sigma\) is unitarizable. If \(G\) is countable, \(X\) is countable, and \(\ell^2(X;E)\) is separable when \(E\) is. \(\square\)

**Corollary 3.2.** Every subgroup of a unitarizable group is unitarizable. \(\square\)

**Lemma 3.3.** If every finitely generated subgroup of \(G\) is amenable, then \(G\) is amenable. Consequently every nonamenable group has a finitely generated, hence countable, nonamenable subgroup.

**Proof.** Let \(\mathcal M\) be the set of means on \(\ell^\infty(G)\). A mean has norm \(m(1)=1\): for \(|f|\le1\) and a scalar \(\theta\) with \(|\theta|=1\) and \(\theta m(f)=|m(f)|\), we have \(|m(f)|=m(\operatorname{Re}\theta f)\le m(1)\). The set \(\mathcal M\) is weak\* closed in the unit ball of \(\ell^\infty(G)^*\), which is weak\* compact by the Banach–Alaoglu theorem; so \(\mathcal M\) is weak\* compact.

For a finitely generated subgroup \(K\), choose a left invariant mean \(m_K\) on \(\ell^\infty(K)\) and put \(\mu_K(f)=m_K(f|_K)\). For \(k\in K\) and \(x\in K\), \((L_kf)(x)=f(k^{-1}x)\) with \(k^{-1}x\in K\), so \((L_kf)|_K=L_k(f|_K)\) and \(\mu_K(L_kf)=\mu_K(f)\). Let \(C_K\subseteq\mathcal M\) be the weak\* closure of \(\{\mu_{K'}:K'\supseteq K\text{ finitely generated}\}\). Each \(C_K\) is nonempty, and \(C_{K_1}\cap\dots\cap C_{K_n}\supseteq C_{\langle K_1,\dots,K_n\rangle}\neq\varnothing\). By compactness some \(\mu\) lies in every \(C_K\). For \(g\in G\) and \(f\in\ell^\infty(G)\), the set \(\{\nu\in\mathcal M:\nu(L_gf)=\nu(f)\}\) is weak\* closed and contains every \(\mu_{K'}\) with \(K'\supseteq\langle g\rangle\); hence it contains \(C_{\langle g\rangle}\ni\mu\). So \(\mu\) is a left invariant mean on \(\ell^\infty(G)\). \(\square\)

## 4. The plan of the proof

By Lemma 3.3 and Lemma 3.1, it suffices to produce, for every countable nonamenable group \(G\) and every \(\varepsilon>0\), a representation \(\pi\) with \(|\pi|\le1+\varepsilon\) that is not unitarizable. By Proposition 2.2 it suffices to find a unitary representation \(U\) and a cocycle \(D\) with \(\sup_g\|D(g)\|\le\varepsilon\) that is not inner. The representation \(U\) will be a direct sum of left regular representations on \(\ell^2(G;\mathbb C^{k_j})\), and \(D\) a direct sum of cocycles \(D_{T_j}\) as in Example 2.1. The operators \(T_j\) have uniformly bounded conjugation differences \(T_j-U(g)T_jU(g)^{-1}\), but every operator implementing their direct sum would have to be far from the commutant of \(U\) in every summand by an amount that grows with \(j\).

## 5. Exercises

**Exercise 5.1** (easy). Let \(\pi:G\to GL(H)\) be a representation, not assumed uniformly bounded, that preserves an inner product \([\cdot,\cdot]\) with \(a\|\xi\|^2\le[\xi,\xi]\le b\|\xi\|^2\). Show that \(|\pi|\le(b/a)^{1/2}\).

**Exercise 5.2** (easy). In Proposition 2.2, suppose \(D(g)=B-U(g)BU(g)^{-1}\) with \(B\in B(H)\). Show that \(R=\begin{pmatrix}1&-B\\0&1\end{pmatrix}\) satisfies \(R\pi(g)R^{-1}=U(g)\oplus U(g)\), so \(\pi\) is unitarizable.

**Exercise 5.3** (medium). Show that a finite group is unitarizable directly, by averaging \(\langle\pi(g)\xi,\pi(g)\eta\rangle\) over the group, and compute the constants \(a,b\) of the resulting equivalent inner product in terms of \(|\pi|\).

**Exercise 5.4** (medium). For \(j\in\mathbb N\) let \(U_j\) be a unitary representation on \(H_j\) and \(D_j\) a bounded operator cocycle for \(U_j\), with \(\sup_{j,g}\|D_j(g)\|<\infty\). Show that \(D=\bigoplus_jD_j\) is a bounded operator cocycle for \(U=\bigoplus_jU_j\), and that if \(D\) is inner with implementer \(B\), then every \(D_j\) has an implementer \(B_j\) with \(\|B_j\|\le\|B\|\).

## 6. Solutions

**5.1.** If \(a\|\xi\|^2\le[\xi,\xi]\le b\|\xi\|^2\) and \([\pi(g)\xi,\pi(g)\xi]=[\xi,\xi]\), then \(a\|\pi(g)\xi\|^2\le[\pi(g)\xi,\pi(g)\xi]=[\xi,\xi]\le b\|\xi\|^2\), so \(\|\pi(g)\|\le(b/a)^{1/2}\) for every \(g\).

**5.2.** Here \(R^{-1}=\begin{pmatrix}1&B\\0&1\end{pmatrix}\), and
\[
R\pi(g)R^{-1}=\begin{pmatrix}U(g)&D(g)U(g)-BU(g)\\0&U(g)\end{pmatrix}\begin{pmatrix}1&B\\0&1\end{pmatrix}=\begin{pmatrix}U(g)&U(g)B+D(g)U(g)-BU(g)\\0&U(g)\end{pmatrix}.
\]
Since \(D(g)U(g)=BU(g)-U(g)B\), the upper right entry vanishes.

**5.3.** Put \([\xi,\eta]=\frac1{|G|}\sum_{g\in G}\langle\pi(g)\xi,\pi(g)\eta\rangle\). Replacing \(g\) by \(gh\) permutes the terms, so the form is invariant, and as in the proof of Theorem 1.2, \(|\pi|^{-2}\|\xi\|^2\le[\xi,\xi]\le|\pi|^2\|\xi\|^2\); so \(a=|\pi|^{-2}\), \(b=|\pi|^2\). This is the proof of Theorem 1.2 with the uniform average in place of the mean.

**5.4.** The direct sum \(D(g)=\bigoplus_jD_j(g)\) is a bounded operator of norm \(\sup_j\|D_j(g)\|\), and (2.1) holds summand by summand. Let \(I_j:H_j\to\bigoplus_iH_i\) be the inclusion and \(B_j=I_j^*BI_j\), so \(\|B_j\|\le\|B\|\). Each summand reduces \(U\): \(U(g)I_j=I_jU_j(g)\) and \(I_j^*U(g)=U_j(g)I_j^*\). Hence \(I_j^*U(g)BU(g)^{-1}I_j=U_j(g)B_jU_j(g)^{-1}\), and compressing \(D(g)=B-U(g)BU(g)^{-1}\) by \(I_j\) gives \(D_j(g)=B_j-U_j(g)B_jU_j(g)^{-1}\). The compression does not require \(B\) to preserve the summands. This step is used in the lesson [Unitarizability implies amenability](unitarizability-implies-amenability.md).

## References

- [EM] I. Epstein and N. Monod, *Nonunitarizable representations and random forests*, Int. Math. Res. Not. IMRN 2009; arXiv:0811.3422. https://arxiv.org/abs/0811.3422
- [MO] N. Monod and N. Ozawa, *The Dixmier problem, lamplighters and Burnside groups*, J. Funct. Anal. 258 (2010); arXiv:0902.4585. https://arxiv.org/abs/0902.4585
- [OpenAI-U] OpenAI, *Unitarizability implies amenability for discrete groups*, OpenAI Math Release preprint, 23 September 2026, Sections 1, 2 and 5. https://github.com/openai/math/blob/main/preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026
- [Pi] G. Pisier, *Are unitarizable groups amenable?*, in: Infinite Groups: Geometric, Combinatorial and Dynamical Aspects, Progr. Math. 248, Birkhäuser, 2005; arXiv:math/0405282. https://arxiv.org/abs/math/0405282
