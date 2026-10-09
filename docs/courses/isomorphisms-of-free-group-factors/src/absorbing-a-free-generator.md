# Absorbing a free generator

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the rank step of the course.

**Theorem 3.1** (OpenAI). For every integer \(n\ge3\) there is a unital normal trace-preserving \(*\)-isomorphism \(L(\mathbb F_n)\to L(\mathbb F_{n+1})\).

Start with \(M=L(\mathbb F_{n+1})\) and its canonical freely generating Haar tuple \((A_1,\ldots,A_n,C)\). Proposition 1.1 combines the flows of [Trace-preserving polynomial flows](trace-preserving-polynomial-flows.md) with the coefficients of [A small cocycle with a prescribed word value](a-small-cocycle-with-a-prescribed-word-value.md): it gives a trace-preserving automorphism that moves each \(A_j\) by less than \(\varepsilon\) in operator norm, while a word in the moved \(A_j\) comes within \(\varepsilon\) of the old \(C\). Iterating with summable tolerances, the \(n\)-tuples converge in norm to a free Haar \(n\)-tuple. The tolerances are chosen adaptively, so that the limit tuple still approximates a dense sequence of \(L^2(M)\); a conditional expectation argument then shows that it generates \(M\). Lemma 2.4 of [Free independence and Haar tuples](free-independence-and-haar-tuples.md) identifies \(M\) with \(L(\mathbb F_n)\).

We use: Lemma 2.4 and Corollary 2.5 of the first lesson, Theorem 6.2 of the second and Theorem 4.1 of the third; and the trace-preserving conditional expectation, [Theorem 9.1 of the lesson on integration for a trace](course:traces-and-noncommutative-integration/integration-for-a-trace-the-commutation-theorem-and-applications#9-conditional-expectations-that-preserve-a-trace).

## 1. One step

Let \((M,\tau)\) be a von Neumann algebra with a faithful normal tracial state and \(\Gamma=\mathbb F_n\subseteq\mathbb F_{n+1}\), where \(\mathbb F_{n+1}\) has free generators \(x_1,\ldots,x_n,c\).

**Proposition 1.1.** Let \(n\ge3\) and let \((A_1,\ldots,A_n,C)\) be a freely generating Haar tuple in \(M\). For every \(\varepsilon>0\) there are a trace-preserving normal automorphism \(\alpha\) of \(M\) and a word \(w\in\Gamma\) such that, with \(A_j'=\alpha(A_j)\) and \(C'=\alpha(C)\),
\[
\max_{1\le j\le n}\|A_j'-A_j\|<\varepsilon,\qquad \|A'_w-C\|<\varepsilon,\qquad C'=CA_w^* .
\]
The tuple \((A_1',\ldots,A_n',C')\) is again a freely generating Haar tuple.

**Proof.** Let \(K=3\pi\) and \(\eta=\varepsilon/(2K)\). Theorem 4.1 of the third lesson gives \(w\in\Gamma\) and \(h\in\mathbb R^{(\Gamma)}\) with \(\|h\|_{\ell^2}<\eta\) and \(\|D^h_w-\delta_e\|_{\ell^2}<\eta\), where \(D^h\) is the cocycle with generator values \(h_1=h\), \(h_2=\cdots=h_n=0\). Let \(\beta=\beta_1\) be the time-one automorphism of Theorem 6.2 of the second lesson for these generator values. It is trace-preserving and normal, fixes \(C\), and
\[
\max_j\|\beta(A_j)-A_j\|\le K\|h\|_{\ell^2}<\varepsilon,\qquad \|\beta(A_w)-CA_w\|\le K\|D^h_w-\delta_e\|_{\ell^2}<\varepsilon .
\]
The endomorphism \(\theta\) of \(\mathbb F_{n+1}\) that fixes every \(x_j\) and sends \(c\) to \(cw\) is an automorphism: it fixes \(w\), so the endomorphism that fixes every \(x_j\) and sends \(c\) to \(cw^{-1}\) is its inverse. By Corollary 2.5(2) of the first lesson there is a trace-preserving normal automorphism \(\gamma\) of \(M\) with \(\gamma(A_j)=A_j\) and \(\gamma(C)=CA_w\). Put \(\alpha=\gamma^{-1}\circ\beta\). Since \(\gamma\) fixes every \(A_j\) and hence \(A_w\),
\[
\alpha(A_j)-A_j=\gamma^{-1}\big(\beta(A_j)-A_j\big),\qquad \alpha(A_w)-C=\gamma^{-1}\big(\beta(A_w)-\gamma(C)\big)=\gamma^{-1}\big(\beta(A_w)-CA_w\big),
\]
and automorphisms are isometric, which gives the two estimates. Finally \(C'=\gamma^{-1}(\beta(C))=\gamma^{-1}(C)=CA_w^*\), because \(\gamma(CA_w^*)=CA_wA_w^*=C\), and the image of a freely generating Haar tuple under \(\alpha\) is one again (Corollary 2.5(4) of the first lesson). \(\square\)

The word \(A'_w\) is evaluated at the new tuple, while the target \(C\) is the old completion; the new completion \(C'\) is different.

## 2. Word polynomials

A *word polynomial* in \(d\) variables is a finite linear combination \(F=\sum_\nu c_\nu v_\nu\) of words \(v_\nu\) in the letters \(x_1^{\pm1},\ldots,x_d^{\pm1}\), not necessarily reduced. For a \(d\)-tuple \(U\) of unitaries, \(F(U)=\sum_\nu c_\nu U_{v_\nu}\). Put \(L(F)=\sum_\nu|c_\nu|\,|v_\nu|\), where \(|v_\nu|\) is the number of letters of \(v_\nu\), and, for \(d\)-tuples \(U,V\) of unitaries, \(d_2(U,V)=\max_j\|U_j-V_j\|_2\).

**Lemma 2.1.** For a word \(v\) with \(r\) letters and \(d\)-tuples \(U,V\) of unitaries, \(\|U_v-V_v\|_2\le r\,d_2(U,V)\) and \(\|U_v-V_v\|\le r\max_j\|U_j-V_j\|\). Consequently \(\|F(U)-F(V)\|_2\le L(F)\,d_2(U,V)\) for every word polynomial \(F\).

**Proof.** Write \(v=y_1\cdots y_r\) and telescope:
\[
U_v-V_v=\sum_{k=1}^rU_{y_1}\cdots U_{y_{k-1}}\big(U_{y_k}-V_{y_k}\big)V_{y_{k+1}}\cdots V_{y_r}.
\]
Multiplication by unitaries on either side preserves both norms, and \(\|U_j^*-V_j^*\|_2=\|U_j-V_j\|_2\) by the trace property. \(\square\)

## 3. The generating limit

**Proof of Theorem 3.1.** Let \(M=L(\mathbb F_{n+1})\) with its trace, and let \((A^{(0)},C^{(0)})\) be the canonical freely generating Haar tuple \((\lambda(x_1),\ldots,\lambda(x_n),\lambda(c))\); write \(A^{(k)}=(A^{(k)}_1,\ldots,A^{(k)}_n)\). The finite combinations of the \(\lambda(g)\), \(g\in\mathbb F_{n+1}\), with coefficients in \(\mathbb Q+i\mathbb Q\) form a countable set whose image in \(L^2(M)\) is dense, because the vectors \(\lambda(g)\Omega\) form an orthonormal basis. Enumerate it as \((y_j)_{j\ge1}\). Put \(r_0=1\).

*Stage \(k\ge1\).* Suppose a freely generating Haar tuple \((A^{(k-1)},C^{(k-1)})\) and \(r_{k-1}>0\) have been constructed. Make the following choices, in this order.

(a) For \(1\le j\le k\), choose a word polynomial \(F_{j,k}\) in \(n+1\) variables with
\[
\big\|F_{j,k}(A^{(k-1)},C^{(k-1)})-y_j\big\|_2<2^{-k}.
\]
This is possible because the word algebra of a freely generating Haar tuple is dense in \(L^2(M)\) (Lemma 2.4 of the first lesson). Let \(H_k=\max_jL(F_{j,k})\).

(b) Choose \(\varepsilon_k\) with \(0<\varepsilon_k<\min\big(r_{k-1}/2,\;2^{-k}/(1+H_k)\big)\).

(c) Apply Proposition 1.1 to \((A^{(k-1)},C^{(k-1)})\) and \(\varepsilon_k\), obtaining \(\alpha_k\) and \(w_k\in\Gamma\), and put \(A^{(k)}_j=\alpha_k(A^{(k-1)}_j)\), \(C^{(k)}=\alpha_k(C^{(k-1)})\). Then \((A^{(k)},C^{(k)})\) is a freely generating Haar tuple, and
\[
\max_j\|A^{(k)}_j-A^{(k-1)}_j\|<\varepsilon_k,\qquad \|A^{(k)}_{w_k}-C^{(k-1)}\|<\varepsilon_k .
\tag{3.1}
\]

(d) Let \(G_{j,k}\) be the word polynomial in \(n\) variables obtained from \(F_{j,k}\) by replacing the letter for the last variable by the reduced word of \(w_k\), and its inverse by the reduced word of \(w_k^{-1}\); so \(G_{j,k}(X)=F_{j,k}(X,X_{w_k})\). The \((n+1)\)-tuples \((A^{(k)},A^{(k)}_{w_k})\) and \((A^{(k-1)},C^{(k-1)})\) are at \(d_2\)-distance less than \(\varepsilon_k\) by (3.1), since \(\|\cdot\|_2\le\|\cdot\|\). By Lemma 2.1 and (a),
\[
\big\|G_{j,k}(A^{(k)})-y_j\big\|_2\le H_k\varepsilon_k+2^{-k}<2\cdot2^{-k}\qquad(1\le j\le k).
\tag{3.2}
\]
The word \(A^{(k)}_{w_k}\) is used here as a single unitary entry of \(F_{j,k}\), so the length of \(w_k\) does not enter this estimate.

(e) Let \(L_k=\max_jL(G_{j,k})\) and choose \(r_k\) with \(0<r_k\le\min\big(r_{k-1}/2,\;2^{-k}/(1+L_k)\big)\).

The budget \(r_k\) is chosen after \(w_k\) is known, so a long word \(w_k\) only makes the later steps smaller.

*Convergence.* For \(\ell>k\) we have \(\varepsilon_\ell<r_{\ell-1}/2\le2^{-(\ell-k)}r_k\). By (3.1), for \(p>k\),
\[
\max_j\|A^{(p)}_j-A^{(k)}_j\|<\sum_{\ell=k+1}^p2^{-(\ell-k)}r_k<r_k .
\]
Since \(r_k\le2^{-k}\), each sequence \((A^{(k)}_j)_k\) converges in operator norm to a unitary \(A^{(\infty)}_j\), and
\[
\max_j\|A^{(\infty)}_j-A^{(k)}_j\|\le r_k .
\tag{3.3}
\]
*Free Haar distribution.* For \(v\in\Gamma\setminus\{e\}\), \(\tau(A^{(k)}_v)=0\) because \((A^{(k)},C^{(k)})\) is a freely generating Haar tuple, and \(A^{(k)}_v\to A^{(\infty)}_v\) in norm by Lemma 2.1. So \(\tau(A^{(\infty)}_v)=0\).

*Generation.* Let \(N=W^*(A^{(\infty)}_1,\ldots,A^{(\infty)}_n)\). For \(j\le k\), (3.2), Lemma 2.1, (3.3) and the choice of \(r_k\) give
\[
\big\|G_{j,k}(A^{(\infty)})-y_j\big\|_2\le L_kr_k+2\cdot2^{-k}<3\cdot2^{-k}.
\]
Let \(E\colon M\to N\) be the trace-preserving conditional expectation (Theorem 9.1 of the lesson on integration for a trace; \(\tau\) is finite). For \(x\in M\) and \(y\in N\), \(\langle x\Omega-E(x)\Omega,y\Omega\rangle=\tau(xy^*)-\tau(E(x)y^*)=0\) by (9.1) there, so \(E(x)\Omega\) is the orthogonal projection of \(x\Omega\) onto the closure \(\mathcal K\) of \(N\Omega\). Since \(G_{j,k}(A^{(\infty)})\in N\), the distance from \(y_j\Omega\) to \(\mathcal K\) is less than \(3\cdot2^{-k}\) for every \(k\ge j\), so \(y_j\Omega\in\mathcal K\). The \(y_j\Omega\) are dense, so \(\mathcal K=L^2(M)\). Hence \(E(x)\Omega=x\Omega\), that is \(E(x)=x\in N\), for every \(x\in M\): \(N=M\).

Thus \(A^{(\infty)}\) is a freely generating Haar \(n\)-tuple in \(M=L(\mathbb F_{n+1})\), and Lemma 2.4 of the first lesson gives a unital normal trace-preserving \(*\)-isomorphism \(L(\mathbb F_n)\to L(\mathbb F_{n+1})\) with \(\lambda(x_j)\mapsto A^{(\infty)}_j\). \(\square\)

Only the \(n\)-tuples converge. The completions \(C^{(k)}\) need not converge, and the operator norms of the approximating elements \(G_{j,k}(A^{(\infty)})\) may grow with \(k\): the approximations are in \(L^2\), and the conditional expectation turns \(L^2\)-density into generation.

**Corollary 3.2.** For all integers \(3\le m\le n\), there is a unital normal trace-preserving \(*\)-isomorphism \(L(\mathbb F_m)\to L(\mathbb F_n)\).

**Proof.** Compose the isomorphisms of Theorem 3.1 for \(m,m+1,\ldots,n-1\). \(\square\)

## 4. The rank-two factor

Theorem 3.1 needs \(n\ge3\) because the free prefixes of the third lesson use three generators. [OAI, Theorem 1.2] also proves \(L(\mathbb F_2)\cong L(\mathbb F_3)\). It applies Theorem 3.1 with \(n=3\) and \(n=4\) to get \(L(\mathbb F_3)\cong L(\mathbb F_5)\), amplifies this isomorphism by \(\sqrt2\), and identifies the amplifications with Dykema's formula \(L(\mathbb F_s)^t\cong L(\mathbb F_{1+(s-1)t^{-2}})\) for interpolated free group factors [D, Theorem 2.4]: \(L(\mathbb F_3)^{\sqrt2}\cong L(\mathbb F_2)\) and \(L(\mathbb F_5)^{\sqrt2}\cong L(\mathbb F_3)\).

This course takes another route, through the integer case of that formula, which is due to Voiculescu (see [D, before Theorem 2.4]): \(pL(\mathbb F_n)p\cong L(\mathbb F_{4n-3})\) for a projection \(p\) of trace \(\frac12\). With \(n=2\) and \(n=3\) the corners are \(L(\mathbb F_5)\) and \(L(\mathbb F_9)\), isomorphic by Corollary 3.2, and a II₁ factor \(Q\) is isomorphic to \(M_2(\mathbb C)\otimes pQp\) when \(\tau(p)=\frac12\) (Exercise 5.3). The next three lessons develop the free probability needed for the corner formula, and [Corners of free group factors](corners-of-free-group-factors.md) proves it and concludes that \(L(\mathbb F_2)\cong L(\mathbb F_3)\).

## 5. Exercises

**Exercise 5.1.** In the proof of Theorem 3.1, show that \(C^{(k)}=C^{(k-1)}\big(A^{(k-1)}_{w_k}\big)^*\), and deduce from \(\tau(C^{(k)})=0\) that the word \(w_k\) has more than \(1/\varepsilon_k-1\) letters.

**Exercise 5.2.** Let \((A_1,\ldots,A_n,C)\) be a freely generating Haar tuple and \(w\in\mathbb F_n\). Show directly from the definition that \((A_1,\ldots,A_n,CA_w)\) is a freely generating Haar tuple.

**Exercise 5.3.** Let \(Q\) be a II₁ factor with trace \(\tau\) and \(p\in Q\) a projection with \(\tau(p)=\frac12\). Show that \(Q\cong M_2(\mathbb C)\otimes pQp\).

**Exercise 5.4.** Where does the proof of Theorem 3.1 use that the tolerance \(\varepsilon_k\) is chosen before the word \(w_k\), and where that \(r_k\) is chosen after it?

## 6. Solutions

**5.1.** Proposition 1.1, applied at stage \(k\) to the tuple \((A^{(k-1)},C^{(k-1)})\), gives \(C^{(k)}=C^{(k-1)}(A^{(k-1)}_{w_k})^*\). Hence
\[
1=|\tau(C^{(k)})-1|\le\|C^{(k)}-1\|=\|C^{(k-1)}-A^{(k-1)}_{w_k}\|\le\|C^{(k-1)}-A^{(k)}_{w_k}\|+\|A^{(k)}_{w_k}-A^{(k-1)}_{w_k}\|<\varepsilon_k+|w_k|\varepsilon_k,
\]
by (3.1) and Lemma 2.1.

**5.2.** The tuple generates \(M\), since \(C=(CA_w)A_w^*\). The value of a word \(g\) in \(x_1,\ldots,x_n,c\) at the new tuple is the value at the old tuple of \(\theta(g)\), where \(\theta\) fixes the \(x_j\) and sends \(c\) to \(cw\). Since \(\theta\) is an automorphism, \(\theta(g)\ne e\) when \(g\ne e\), so the trace is \(0\).

**5.3.** In a factor with a faithful tracial state, projections of equal trace are equivalent (Lemma 2.3 of [Haar unitaries, freeness and tracial ultraproducts](course:generators-of-ii1-factors/haar-unitaries-freeness-and-ultraproducts#2-haar-unitaries)), so there is \(v\in Q\) with \(v^*v=p\) and \(vv^*=1-p\). Then \(e_{11}=p\), \(e_{21}=v\), \(e_{12}=v^*\), \(e_{22}=1-p\) are matrix units with \(e_{11}+e_{22}=1\), and \(\sum_{i,j}x_{ij}\otimes e_{ij}\mapsto\sum_{i,j}e_{i1}x_{ij}e_{1j}\) (\(x_{ij}\in pQp\)) is a \(*\)-isomorphism of \(pQp\otimes M_2(\mathbb C)\) onto \(Q\); its inverse sends \(x\) to \(\sum_{i,j}e_{1i}xe_{j1}\otimes e_{ij}\).

**5.4.** \(\varepsilon_k\) must make \(H_k\varepsilon_k\) small in (3.2) and must fit into the budget \(r_{k-1}\) of the earlier stages; both are known before \(w_k\). The word \(w_k\) enters the polynomials \(G_{j,k}\), whose Lipschitz constants \(L_k\) can be large when \(w_k\) is long; \(r_k\) must make \(L_kr_k\) small, so it can only be chosen once \(w_k\) is known.

## References

- [OAI] OpenAI, *An isomorphism of the free group factors* (September 23, 2026), OpenAI Math Release preprint, Sections 5–7. https://github.com/openai/math/blob/main/preprints/An-isomorphism-of-the-free-group-factors-September-23-2026/An-isomorphism-of-the-free-group-factors-September-23-2026.pdf
- [D] K. Dykema, *Interpolated free group factors*, Pacific J. Math. 163 (1994), 123–135. https://arxiv.org/abs/funct-an/9211012
