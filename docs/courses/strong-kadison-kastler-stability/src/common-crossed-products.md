# Common crossed products

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

After the previous lesson, two close algebras \(P\) and \(Q\) on one Hilbert space are normalized by a single strongly continuous unitary group \(U\). This lesson forms the two crossed products by the action \(\operatorname{Ad}U\) on the same Hilbert space \(L^2(\mathbb R,H)\). It describes them as fixed-point algebras (Lemma 1.1), shows that they are as close as \(P\) and \(Q\) at every matrix level (Lemma 2.1), and proves that if the crossed product of \(Q\) is a factor of type II\(_\infty\), then \(P\) and \(Q\) are conjugate by a unitary near the identity (Proposition 3.2). The proof conjugates finite corners of the crossed products with the theorem for finite factors, inflates the conjugating unitary, and descends to \(H\) through the completely positive criterion. No factoriality of the crossed product of \(P\) is assumed [OpenAI-289, Section 8].

We use: [Close operator algebras](close-operator-algebras.md) (Lemmas 1.4 and 1.5); [Averaging and the completely positive criterion](averaging-and-the-completely-positive-criterion.md) (Lemma 2.2, Theorem 3.1, Proposition 4.1 and Lemma 5.1); [Irreducible hyperfinite subfactors](irreducible-hyperfinite-subfactors.md) (Lemma 1.1); [Stability of finite factors](stability-of-finite-factors.md) (Theorem 2.1, with \(t_{\rm fin}\) and \(\eta_{\rm fin}\)); [Frequency nests and analytic multipliers](frequency-nests-and-analytic-multipliers.md) (Lemma 4.1); Corollary 5.4 of [Traces on von Neumann algebras](course:OA-FOUND-REMAINDER/reader/supplements/traces-on-von-neumann-algebras-part-a-def-v-2-1-to-def-v-2-17#OA-FND-TA-12) (equal trace gives equivalence in a finite factor); Lemma 4.3 of [Measurable operators for a trace](course:traces-and-noncommutative-integration/measurable-operators-for-a-trace-examples-convergence-and-the-commutant#4-minimal-projections-and-diffuse-algebras) (subprojections of every trace); Proposition 7.4 of the [tensor product lesson](course:tensor-products-of-operator-algebras/spatial-tensor-products-of-von-neumann-algebras#7-tensor-products-with-b-k-commutants-and-matrix-units) (a matrix unit with sum \(1\) generates a copy of \(B(\ell^2)\)); and Corollary 5.2 of [Injective von Neumann algebras](course:injective-factors/injective-von-neumann-algebras) (type I algebras are injective).

## 1. Crossed products as fixed points

Let \(P\subseteq B(H)\) be a unital von Neumann algebra on a separable Hilbert space and \((U_s)_{s\in\mathbb R}\) a strongly continuous unitary group with \(U_sPU_s^*=P\). On \(\mathcal K=L^2(\mathbb R,H)=H\otimes L^2(\mathbb R)\) put
\[
\begin{gathered}
(\lambda_s\xi)(t)=\xi(t-s),\\
(\rho_s\xi)(t)=\xi(t+s),\\
(\pi(x)\xi)(t)=U_t^*xU_t\,\xi(t),
\end{gathered}
\]
for \(x\in B(H)\). Then \(\pi\) is a faithful normal representation of all of \(B(H)\), and completely isometric: at each matrix level its norm is the essential supremum of the norms of unitary conjugates. Let
\[
C(P,U)=\bigl(\pi(P)\cup\{\lambda_s:s\in\mathbb R\}\bigr)'' ,
\]
the crossed product of \(P\) by \(\operatorname{Ad}U\). For a second algebra normalized by the same group, its crossed product lives on the same space. Let \(Q_a\) be multiplication by \(e^{iat}\) and \(\beta_a=\operatorname{Ad}Q_a\).

**Lemma 1.1** (fixed points). With \(\alpha_s=\operatorname{Ad}(U_s\otimes\rho_s)\),
\[
\begin{gathered}
C(P,U)=\bigl(P\bar\otimes B(L^2(\mathbb R))\bigr)^\alpha,\\
C(P,U)^\beta=\pi(P).
\end{gathered}
\]

**Proof.** *Inclusion.* \(\pi(x)\) is multiplication by a field with values in \(P\), and \(\lambda_r\in1\otimes B(L^2(\mathbb R))\), so both lie in \(P\bar\otimes B(L^2(\mathbb R))\). A direct computation gives \(\alpha_s(\pi(x))=\pi(x)\), using \(U_sU_{t+s}^*xU_{t+s}U_s^*=U_t^*xU_t\), and \(\alpha_s(\lambda_r)=\lambda_r\).

*Smoothing.* Let \(X\) be \(\alpha\)-fixed in \(P\bar\otimes B(L^2(\mathbb R))\). For \(f,g\in C_c(\mathbb R)\) let \(\lambda(f)=\int f(s)\lambda_s\,ds\) and \(Y=\lambda(f)X\lambda(g)^*\), again \(\alpha\)-fixed, since translations commute with \(U_s\otimes\rho_s\). The operators \(R_{f,t}:\mathcal K\to H\), \(R_{f,t}\xi=\int f(t-s)\xi(s)\,ds\), have norm at most \(\|f\|_2\), depend norm continuously on \(t\), and \((\lambda(f)\xi)(t)=R_{f,t}\xi\). For compactly supported \(\xi\), Fubini's theorem gives
\[
\begin{gathered}
(Y\xi)(t)=\int k(t,r)\xi(r)\,dr,\\
k(t,r)=R_{f,t}XR_{g,r}^* .
\end{gathered}
\]
The kernel is bounded and jointly norm continuous. Its values lie in \(P\): \(R_{f,t}\) intertwines the constant action of \(P'\), with which \(X\) commutes. Invariance of \(Y\) under \(\alpha_s\) gives \(k(t+s,r+s)=U_s^*k(t,r)U_s\), first almost everywhere and then everywhere by continuity; hence
\[
k(t,r)=U_t^*k(0,r-t)U_t .
\tag{1.1}
\]

*Reconstruction.* Let \(\chi_j(v)=(1-|v|/j)_+\). It is the Fourier transform of the probability measure \(\mu_j\) with density \(\frac j{2\pi}\bigl(\frac{\sin(ja/2)}{ja/2}\bigr)^2\), so multiplying a kernel by \(\chi_j(t-r)\) is the contraction \(Y\mapsto\int Q_aYQ_a^*\,d\mu_j(a)\). The resulting operator is, by (1.1) and \((\rho_v\xi)(t)=\xi(t+v)\),
\[
Y_j=\int_{\mathbb R}\chi_j(v)\,\pi(k(0,v))\,\rho_v\,dv ,
\]
a strong integral of a compactly supported strongly continuous function with values in \(C(P,U)\), since \(\rho_v=\lambda_{-v}\); so \(Y_j\in C(P,U)\). On compactly supported vectors the kernels are bounded on sets of finite measure and \(\chi_j\to1\), so \(Y_j\to Y\) weakly by dominated convergence, and \(Y\in C(P,U)\). Finally, with nonnegative \(f_n\) of integral one and supports shrinking to \(0\), \(\lambda(f_n)\to1\) strongly, so \(\lambda(f_n)X\lambda(f_n)^*\to X\) weakly and \(X\in C(P,U)\).

*Characters.* \(\beta_a(\pi(x))=\pi(x)\) and \(\beta_a(\lambda_s)=e^{ias}\lambda_s\), so \(\beta\) preserves \(C(P,U)\). An element fixed by all \(\beta_a\) commutes with all \(Q_a\), so by Lemma 4.1 of [Frequency nests and analytic multipliers](frequency-nests-and-analytic-multipliers.md) it is multiplication by a bounded field \(F\), with values in \(P\) almost everywhere because it commutes with the constant action of \(P'\). Invariance under \(\alpha_s\) gives \(F(t+s)=U_s^*F(t)U_s\) almost everywhere, for each \(s\). Then \(G(t)=U_tF(t)U_t^*\) is invariant under translations; testing on a countable dense set of pairs of vectors and convolving with approximate identities shows that each coefficient is almost everywhere constant, so \(G=x\) almost everywhere, with \(x\in P\) because \(U\) normalizes \(P\). So \(F(t)=U_t^*xU_t\) and the element is \(\pi(x)\). \(\square\)

With the invariant mean of the averaging lesson, every unitary representation \(V\) of \(\mathbb R_d\) gives the UCP map \(E_V(T)=m_sV_sTV_s^*\), which fixes the operators commuting with all \(V_s\) and preserves every von Neumann algebra invariant under the conjugations (Lemma 2.2 there).

## 2. Close crossed products

**Lemma 2.1.** Let \(P,Q\subseteq B(H)\) be unital von Neumann algebras on a separable space, normalized by the same strongly continuous unitary group \(U\). If \(d_{\rm cb}(P,Q)<\gamma\), then \(d_{\rm cb}(C(P,U),C(Q,U))<\gamma\).

**Proof.** Choose \(\gamma'<\gamma\) with \(d_{\rm cb}(P,Q)\le\gamma'\). By Lemma 5.1(1) of the averaging lesson, \(d_{\rm cb}(P\bar\otimes B(L^2(\mathbb R)),Q\bar\otimes B(L^2(\mathbb R)))\le\gamma'\). Let \(V_s=U_s\otimes\rho_s\). For a contraction \(X\) in \(M_n(C(P,U))\), choose a contraction \(Y\) in \(M_n(Q\bar\otimes B(L^2(\mathbb R)))\) within \(\gamma'\) plus a small slack. The amplification of \(E_V\) fixes \(X\), by Lemma 1.1; it maps \(Y\) to an \(\alpha\)-fixed element of \(M_n(Q\bar\otimes B(L^2(\mathbb R)))\), that is, into \(M_n(C(Q,U))\); and it is completely contractive. So \(\operatorname{dist}(X,M_n(C(Q,U))_1)\le\gamma'\). Exchange \(P\) and \(Q\). \(\square\)

## 3. Conjugacy through a crossed product

**Lemma 3.1** (matrix units). A type II\(_\infty\) factor \(B\) on a separable Hilbert space contains matrix units \((e_{ij})_{i,j\ge1}\) with \(\sum_ie_{ii}=1\) strongly and \(e_{11}\) finite and nonzero. The von Neumann algebra they generate is a copy of \(B(\ell^2)\), hence injective.

**Proof.** Let \(\tau\) be a faithful normal semifinite trace on \(B\). A maximal family of mutually orthogonal nonzero projections of finite trace is countable, since \(B\) is countably decomposable, and has sum \(1\), since \(\tau\) is semifinite; call them \(q_1,q_2,\dots\). Then \(\sum_k\tau(q_k)=\tau(1)=\infty\). Fix \(c>0\) and fill consecutive bins of trace \(c\): go through \(q_1,q_2,\dots\) and, by Lemma 4.3 of the measurable-operators lesson (a type II factor has no minimal projections), split off from the current \(q_k\) a subprojection of trace equal to the smaller of the trace still needed in the current bin and the trace remaining in \(q_k\). Since \(\sum_k\tau(q_k)=\infty\), each bin is filled after finitely many steps, and every \(q_k\) is used up. This gives mutually orthogonal projections \(f_i\), \(i\ge1\), with \(\tau(f_i)=c\) and \(\sum_if_i=1\). For \(i\ne j\), the corner \((f_i+f_j)B(f_i+f_j)\) is a finite factor in which \(f_i\) and \(f_j\) have equal trace, so they are equivalent by Corollary 5.4 of the traces lesson. Partial isometries \(w_i\) with \(w_i^*w_i=f_1\) and \(w_iw_i^*=f_i\) give \(e_{ij}=w_iw_j^*\). By Proposition 7.4 of the tensor product lesson, the algebra they generate is spatially a copy of \(B(\ell^2)\otimes1\). \(\square\)

**Proposition 3.2** (conjugacy through a crossed product). There are an absolute \(\gamma_0>0\) and a nondecreasing function \(\zeta:(0,\gamma_0)\to(0,\infty)\) with \(\zeta(\gamma)\to0\) as \(\gamma\to0\), with the following property. Let \(P,Q\subseteq B(H)\) be unital von Neumann algebras on a separable Hilbert space with \(d_{\rm cb}(P,Q)<\gamma<\gamma_0\), normalized by the same strongly continuous unitary group \(U\). If \(C(Q,U)\) is a factor of type II\(_\infty\), there is a unitary \(a\in B(H)\) with
\[
aPa^*=Q,\qquad\|a-1\|\le\zeta(\gamma).
\]

**Proof.** Choose \(\gamma_0\) so that, for \(\gamma<\gamma_0\), \(301\gamma<\min\{1/10,t_{\rm fin}\}\) and \(e(\gamma):=2(150\gamma+\eta_{\rm fin}(301\gamma))<10^{-3}\); and put \(\zeta(\gamma)=32e(\gamma)\). Write \(\mathcal A=C(P,U)\) and \(\mathcal B=C(Q,U)\); by Lemma 2.1, \(d_{\rm cb}(\mathcal A,\mathcal B)<\gamma\).

*A common copy of \(B(\ell^2)\).* Lemma 3.1 gives matrix units \((e_{ij})\) in \(\mathcal B\) with \(e=e_{11}\) finite and nonzero, generating an injective algebra \(S\). Since \(S\subset_\gamma\mathcal A\), Christensen's theorem gives a unitary \(w\) with \(wSw^*\subseteq\mathcal A\) and \(\|w-1\|\le150\gamma\). Put \(\mathcal A_1=w^*\mathcal Aw\). Then \(S\subseteq\mathcal A_1\cap\mathcal B\) and \(d(\mathcal A_1,\mathcal B)<301\gamma=:\kappa\).

*Finite corners.* Compressing by the common projection \(e\) gives von Neumann algebras \(A_0=e\mathcal A_1e\) and \(B_0=e\mathcal Be\) on \(e\mathcal K\), with identity \(e\) and \(d(A_0,B_0)<\kappa\). The corner \(B_0\) of the II\(_\infty\) factor by a finite projection is a II\(_1\) factor. By Lemma 1.1 of the hyperfinite lesson, \(A_0\) is a finite factor, and Theorem 2.1 of [Stability of finite factors](stability-of-finite-factors.md), applied on the separable space \(e\mathcal K\) with the finite factor \(B_0\), gives a unitary \(v_0\) on \(e\mathcal K\) with
\[
v_0A_0v_0^*=B_0,\qquad\|v_0-e\|\le\eta_{\rm fin}(\kappa).
\]

*Inflation.* Put \(V=\sum_{i\ge1}e_{i1}v_0e_{1i}\). It is the direct sum of copies of \(v_0\) on the spaces \(e_{ii}\mathcal K\), so it is a unitary, \(\|V-1\|=\|v_0-e\|\), and \(Ve_{ij}=e_{i1}v_0e_{1j}=e_{ij}V\). For \(x\in\mathcal A_1\), the entries \(e_{1i}xe_{j1}\) lie in \(A_0\), so \(e_{1i}VxV^*e_{j1}=v_0e_{1i}xe_{j1}v_0^*\in B_0\), and
\[
VxV^*=\sum_{i,j}e_{i1}\bigl(e_{1i}VxV^*e_{j1}\bigr)e_{1j}
\]
is a strong limit of finite sums in \(\mathcal B\). So \(V\mathcal A_1V^*\subseteq\mathcal B\), and the same argument with \(v_0^*\) gives equality. With \(Z=Vw^*\),
\[
\begin{gathered}
Z\mathcal AZ^*=\mathcal B,\\
\|Z-1\|\le150\gamma+\eta_{\rm fin}(301\gamma).
\end{gathered}
\]

*Descent to \(H\).* Average the characters: \(E_\beta(T)=m_aQ_aTQ_a^*\) on \(B(\mathcal K)\). It fixes every \(\pi(x)\), \(x\in B(H)\), and maps \(\mathcal B\) into \(\mathcal B^\beta=\pi(Q)\) by Lemma 1.1. So
\[
F(x)=\pi^{-1}\bigl(E_\beta(Z\pi(x)Z^*)\bigr)\qquad(x\in P)
\]
is a UCP map from \(P\) to \(Q\). Since \(E_\beta\) fixes \(\pi(x)\) and \(\pi\) is completely isometric, \(\|F-\mathrm{id}_P\|_{\rm cb}\le2\|Z-1\|\le e(\gamma)\), where \(\mathrm{id}_P\) is the inclusion of \(P\) in \(B(H)\). The reverse ordinary gap from \(Q\) to \(P\) is less than \(\gamma\), and \(\gamma+e(\gamma)<1\). Proposition 4.1 of the averaging lesson gives a unitary \(a\) with \(aPa^*=Q\) and \(\|a-1\|\le32e(\gamma)=\zeta(\gamma)\). \(\square\)

## 4. Exercises

**Exercise 4.1.** Check \(\alpha_s(\pi(x))=\pi(x)\) and \(\beta_a(\lambda_s)=e^{ias}\lambda_s\).

**Exercise 4.2.** Verify that \(\chi_j(v)=(1-|v|/j)_+\) is the Fourier transform of the stated probability density.

**Exercise 4.3.** For \(P=B(H)\) and \(U\) trivial, identify \(C(P,U)\) and check Lemma 1.1 directly.

**Exercise 4.4.** Show that \(V=\sum_ie_{i1}v_0e_{1i}\) commutes with every \(e_{ij}\).

**Exercise 4.5.** In Proposition 3.2, why is the factoriality of \(C(P,U)\) not needed?

## 5. Solutions

**Solution 4.1.** \(\bigl((U_s\otimes\rho_s)\pi(x)(U_s\otimes\rho_s)^*\xi\bigr)(t)\)\(=U_sU_{t+s}^*xU_{t+s}U_s^*\xi(t)\)\(=U_t^*xU_t\xi(t)\), since \(U_{t+s}U_s^*=U_t\). For the second, \((Q_a\lambda_sQ_a^*\xi)(t)=e^{iat}e^{-ia(t-s)}\xi(t-s)\).

**Solution 4.2.** \(\chi_j=j^{-1}\,1_{[-j/2,j/2]}*1_{[-j/2,j/2]}\), and \(\int_{-j/2}^{j/2}e^{-iav}\,dv=2\sin(ja/2)/a\). Since the Fourier transform of a convolution is the product of the transforms, \(\frac1{2\pi}\int e^{-iav}\chi_j(v)\,dv=\frac j{2\pi}\bigl(\frac{\sin(ja/2)}{ja/2}\bigr)^2\), and Fourier inversion gives \(\chi_j(v)=\int e^{iav}\,d\mu_j(a)\). The total mass of \(\mu_j\) is \(\chi_j(0)=1\).

**Solution 4.3.** \(\pi(x)=x\otimes1\), and \(C(P,U)\) is generated by \(B(H)\otimes1\) and the translations, so it is \(B(H)\bar\otimes\lambda(\mathbb R)''\). The \(\alpha\)-fixed points of \(B(H)\bar\otimes B(L^2(\mathbb R))\) are the operators commuting with \(1\otimes\rho_s\), and the commutant of the right translations is the algebra generated by the left translations.

**Solution 4.4.** \(Ve_{ij}=\sum_ke_{k1}v_0e_{1k}e_{ij}=e_{i1}v_0e_{1j}\) and \(e_{ij}V=\sum_ke_{ij}e_{k1}v_0e_{1k}=e_{i1}v_0e_{1j}\).

**Solution 4.5.** Only the finite corner \(A_0\) needs to be a finite factor, and Lemma 1.1 of the hyperfinite lesson derives this from its closeness to the II\(_1\) factor \(B_0\).

## References

- [OpenAI-289] OpenAI, Universal strong Kadison–Kastler stability, preprint, 23 September 2026, Section 8. https://github.com/openai/math/tree/main/preprints/Universal-strong-Kadison-Kastler-stability-September-23-2026
