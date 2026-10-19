# The Liouville theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(M\) be a von Neumann algebra of type \(\mathrm{II}_1\) with separable predual and faithful normal tracial state \(\tau\), and let \(\mu\) and \(n_1<n_2<\cdots\) be the measure and the times of Theorem 3.1 of the lesson on the random walk. A bounded linear map \(T:M\to M\) is *\(\mu\)-harmonic* if
\[
\begin{gathered}
T(x)=\sum_{U}\mu(\{U\})\,T(xU)\,U^*\\
(x\in M),
\end{gathered}
\]
the sum running over the countably many atoms of \(\mu\); it converges in norm, since \(\|T(xU)U^*\|\le\|T\|\,\|x\|\). Left multiplications \(x\mapsto cx\) are \(\mu\)-harmonic. This lesson proves that, under a continuity condition, they are the only ones.

**Theorem 0.1 (Liouville theorem).** Let \(T:M\to M\) be bounded, linear, continuous on balls for the \(2\)-norm, and \(\mu\)-harmonic. Then \(T(x)=T(1)x\) for all \(x\in M\).

No positivity or complete boundedness of \(T\) is assumed. The proof follows a random walk \(W_n=U_1\cdots U_n\) with independent increments of law \(\mu\). The values \(T(W_n)W_n^*\) form a bounded martingale in \(L^2(M)\), which converges (Section 1). If its limit is constant, density of the atoms gives the theorem (Section 2). If not, the limit takes values near two different points \(a\ne b\) with positive probability. Long independent products then carry the left multiplier \(a\) when read forwards and \(b\) when inverted (Section 3). An ultrapower turns this into a free Haar family on which one map multiplies by \(a\) or \(b\) according to the first letter of a word (Section 4). The rigidity theorem forbids this.

**Prerequisites.** [*The cohomology problem*](the-cohomology-problem.md), Section 2 (Lemma 2.2: maps continuous on balls and their ultrapower extensions). [*Rigidity of first-letter identities*](rigidity-of-first-letter-identities.md), Theorem 0.1. [*A random walk with asymptotically free products*](a-random-walk-with-asymptotically-free-products.md), Theorem 3.1 and Lemma 2.3 (\(L^2(M)\) is separable). Measure theory from the core course [*Measure and Integration*](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10), built on D. H. Fremlin's [*Measure Theory*, Volume 2](https://www1.essex.ac.uk/maths/people/fremlin/cont25.htm): products of probability spaces (Theorem 254F), Fatou's lemma and monotone convergence.

**Setting.** \(H=L^2(M)\) is the completion of \(M\) for \(\|x\|_2=\tau(x^*x)^{1/2}\), and elements of \(M\) are identified with their images in \(H\); \(H\) is separable. Let \(S\) be the countable set of atoms of \(\mu\). On \(\Omega=S^{\mathbb N}\) with the product \(P\) of countably many copies of \(\mu\) (Theorem 254F of Fremlin), the coordinates \(U_1,U_2,\ldots\) are independent with law \(\mu\). Put \(W_0=1\) and \(W_n=U_1\cdots U_n\). For \(k\ge0\), the *atoms of time \(k\)* are the sets \(\{U_1=s_1,\ldots,U_k=s_k\}\), \(s_i\in S\); they have positive probability and partition \(\Omega\). A function is *determined at time \(k\)* if it is constant on each atom of time \(k\). Fix \(T\) as in Theorem 0.1, put \(C=\|T\|\), and
\[
\begin{gathered}
D(g)=T(g)g^*\quad(g\in\mathcal U(M)),\\
Z_n=D(W_n).
\end{gathered}
\]
Each \(Z_n\) takes countably many values in \(M\), is determined at time \(n\), and has \(\|Z_n\|_2\le\|Z_n\|\le C\). Since \(T(x)=D(x)x\) for unitaries \(x\), and right multiplication by a unitary preserves the \(2\)-norm,
\[
\begin{gathered}
\|T(x)-cx\|_2=\|D(x)-c\|_2\\
(x\in\mathcal U(M),\ c\in M).\qquad(0.1)
\end{gathered}
\]

## 1. The martingale

**Lemma 1.1.** Let \(k\ge0\), let \(A\) be an atom of time \(k\), and let \(X\) be a bounded \(H\)-valued function determined at time \(k\). Then \(\mathbb E[Z_{k+1}1_A]=\mathbb E[Z_k1_A]\), and \(\mathbb E\langle Z_{k+1}-Z_k,X\rangle=0\). Consequently, for \(n\ge k\),
\[
\begin{gathered}
\mathbb E\|Z_n-Z_k\|_2^2=\sum_{j=k}^{n-1}\mathbb E\|Z_{j+1}-Z_j\|_2^2,\\
\sum_{j\ge0}\mathbb E\|Z_{j+1}-Z_j\|_2^2\le C^2 .
\end{gathered}
\]

**Proof.** On \(A=\{U_1=s_1,\ldots,U_k=s_k\}\) put \(w=s_1\cdots s_k\). Since \(U_{k+1}\) is independent of \(U_1,\ldots,U_k\), harmonicity at \(x=w\) gives
\[
\begin{aligned}
&\mathbb E[Z_{k+1}1_A]\\
&=P(A)\sum_{s\in S}\mu(\{s\})\,T(ws)s^*w^*\\
&=P(A)\,T(w)w^*=\mathbb E[Z_k1_A].
\end{aligned}
\]
Summing over the atoms of time \(k\), on which \(X\) is constant, gives \(\mathbb E\langle Z_{k+1}-Z_k,X\rangle=0\); the sums converge absolutely because everything is bounded. So each increment \(Z_{j+1}-Z_j\) is orthogonal, in \(\mathbb E\langle\cdot,\cdot\rangle\), to the earlier increments and to \(Z_0=T(1)\). Expanding \(Z_n-Z_k\) and \(Z_n=Z_0+\sum_{j<n}(Z_{j+1}-Z_j)\) gives the identity and \(\|Z_0\|_2^2+\sum_{j<n}\mathbb E\|Z_{j+1}-Z_j\|_2^2\)\(=\mathbb E\|Z_n\|_2^2\le C^2\). \(\square\)

Put
\[
e_k=\sum_{j\ge k}\mathbb E\|Z_{j+1}-Z_j\|_2^2 ,
\]
so \(e_k\to0\), and \(\mathbb E\|Z_n-Z_k\|_2^2\le e_k\) for \(n\ge k\).

**Lemma 1.2.** There is a measurable \(Z_\infty:\Omega\to H\) with \(\mathbb E\|Z_\infty-Z_k\|_2^2\le e_k\) for every \(k\). The ball \(K_C=\{x\in M:\|x\|\le C\}\) is closed in \(H\), and \(Z_\infty\in K_C\) almost surely.

**Proof.** Choose \(k_1<k_2<\cdots\) with \(e_{k_j}\le4^{-j}\). Then \(\mathbb E\|Z_{k_{j+1}}-Z_{k_j}\|_2\)\(\le(\mathbb E\|Z_{k_{j+1}}-Z_{k_j}\|_2^2)^{1/2}\le2^{-j}\), so by monotone convergence \(\sum_j\|Z_{k_{j+1}}-Z_{k_j}\|_2<\infty\) almost surely. Hence \(Z_{k_j}\) converges in \(H\) almost surely; let \(Z_\infty\) be the limit, and \(0\) on the null set where it does not exist. By Fatou's lemma, \(\mathbb E\|Z_\infty-Z_k\|_2^2\)\(\le\liminf_j\mathbb E\|Z_{k_j}-Z_k\|_2^2\le e_k\).

Let \(x_n\in K_C\) converge in \(H\) to \(\xi\). The ball \(K_C\) is ultraweakly compact, so a subnet of \((x_n)\) converges ultraweakly to some \(x\in K_C\). For \(y\in M\), \(\langle x_n,y\rangle=\tau(y^*x_n)\) converges along the subnet to \(\tau(y^*x)=\langle x,y\rangle\), and also to \(\langle\xi,y\rangle\). As \(M\) is dense in \(H\), \(\xi=x\in K_C\). So \(K_C\) is closed in \(H\), and the almost sure limit \(Z_\infty\) of the \(Z_{k_j}\in K_C\) lies in \(K_C\) almost surely. \(\square\)

## 2. A constant limit

**Proposition 2.1.** If \(Z_\infty=c\) almost surely for some \(c\in H\), then \(T(x)=T(1)x\) for all \(x\in M\).

**Proof.** Let \(A\) be an atom of time \(1\), \(A=\{U_1=s\}\), or \(A=\Omega\), and let \(y\in H\). For \(k\ge1\) (for \(A=\Omega\), \(k\ge0\)), \(A\) is a disjoint union of atoms of time \(k\), so summing Lemma 1.1 over them shows that \(\mathbb E[\langle Z_n,y\rangle1_A]\) does not depend on \(n\ge1\) (for \(A=\Omega\), on \(n\ge0\)). Also
\[
\bigl|\mathbb E[\langle Z_\infty-Z_n,y\rangle1_A]\bigr|\le\|y\|_2\,e_n^{1/2}\to0 .
\]
So \(\langle c,y\rangle P(A)\) equals \(\mathbb E[\langle Z_1,y\rangle1_A]=\langle D(s),y\rangle P(A)\) for \(A=\{U_1=s\}\), and \(\langle Z_0,y\rangle=\langle T(1),y\rangle\) for \(A=\Omega\). As \(y\) is arbitrary and \(P(A)>0\), \(D(s)=c=T(1)\) for every atom \(s\) of \(\mu\).

Let \(u\in\mathcal U(M)\). The atoms of \(\mu\) contain a sequence \(s_j\) with \(\|s_j-u\|_2\to0\) (Theorem 3.1 of the lesson on the random walk). Continuity on balls gives \(\|T(s_j)-T(u)\|_2\to0\), and \(T(s_j)=D(s_j)s_j=cs_j\to cu\) in \(2\)-norm. So \(T(u)=cu\). Every element of \(M\) is a linear combination of unitaries, so \(T(x)=cx=T(1)x\). \(\square\)

## 3. Two endpoints and independent blocks

For the rest of the proof assume that \(Z_\infty\) is not almost surely constant. The law of \(Z_\infty\) is a Borel probability measure \(\pi\) on the separable Hilbert space \(H\). Its *support* is the set of points all of whose neighbourhoods have positive measure. The complement of the support is the union of the \(\pi\)-null open balls with centres in a countable dense set and rational radii, so it is null, and the support has full measure. It is not a single point, so it contains two points \(a\ne b\). The open complement of \(K_C\) is null by Lemma 1.2, so it does not meet the support, and \(a,b\in K_C\subseteq M\).

**Lemma 3.1 (two endpoints).** For every \(\delta>0\) there are \(\eta_\delta>0\) and \(N_\delta\) such that, if \(n\ge N_\delta\) and \(G\) has law \(\mu^{*n}\),
\[
\begin{aligned}
&P\bigl(\|D(G)-a\|_2<\delta,\\
&\qquad\|D(G^{-1})-b\|_2<\delta\bigr)\ge\eta_\delta .
\end{aligned}
\]

**Proof.** Realize \(G=V_1\cdots V_n\) with independent \(V_i\) of law \(\mu\), let \(h=\lfloor n/2\rfloor\), and put
\[
\begin{gathered}
A_n=D(V_1\cdots V_h),\\
B_n=D(V_n^{-1}\cdots V_{n-h+1}^{-1}).
\end{gathered}
\]
They depend on the disjoint sets \(\{1,\ldots,h\}\) and \(\{n-h+1,\ldots,n\}\) of increments, so they are independent. The forward products \(V_1\cdots V_j\) have the same joint law as the \(W_j\). Since \(\mu\) is symmetric, the variables \(V_n^{-1},V_{n-1}^{-1},\ldots,V_1^{-1}\) are again independent with law \(\mu\), so the products \(V_n^{-1}\cdots V_{n-j+1}^{-1}\) also have the joint law of the \(W_j\). Hence \((D(G),A_n)\) and \((D(G^{-1}),B_n)\) both have the law of \((Z_n,Z_h)\), and
\[
\begin{gathered}
\mathbb E\|D(G)-A_n\|_2^2\le e_h,\\
\mathbb E\|D(G^{-1})-B_n\|_2^2\le e_h .
\end{gathered}
\]
Since \(a\) and \(b\) lie in the support, \(p_a=P(\|Z_\infty-a\|_2<\delta/3)\) and \(p_b=P(\|Z_\infty-b\|_2<\delta/3)\) are positive. By Lemma 1.2 and Chebyshev's inequality,
\[
\begin{aligned}
P(\|Z_h-a\|_2<2\delta/3)&\ge p_a-9e_h/\delta^2\\
&\ge p_a/2
\end{aligned}
\]
for all large \(h\), and similarly for \(b\). The event in the lemma contains the event that \(\|A_n-a\|_2<2\delta/3\) and \(\|B_n-b\|_2<2\delta/3\), minus the events \(\|D(G)-A_n\|_2\ge\delta/3\) and \(\|D(G^{-1})-B_n\|_2\ge\delta/3\). By independence and Chebyshev's inequality its probability is at least
\[
\frac{p_ap_b}4-\frac{18e_h}{\delta^2},
\]
which is at least \(p_ap_b/8\) for large \(n\). \(\square\)

The variables \(G\) and \(G^{-1}\) are dependent; the independence used is that of the disjoint initial pieces \(A_n\) and \(B_n\).

**Lemma 3.2 (independent blocks).** Let \(G_1,\ldots,G_m\) be independent with law \(\mu^{*n}\). Let \(v=x_{i_1}^{\sigma_1}\cdots x_{i_t}^{\sigma_t}\) with \(t\ge1\), \(\sigma_j=\pm1\) and pairwise distinct indices \(i_1,\ldots,i_t\in\{1,\ldots,m\}\). Then
\[
\mathbb E\bigl\|D(v(G))-D(G_{i_1}^{\sigma_1})\bigr\|_2^2\le e_n .
\]

**Proof.** Write each \(G_i\) as a product of \(n\) independent increments, and each \(G_i^{-1}\) as the product of the inverted increments in reverse order, which are again independent with law \(\mu\). As the indices are distinct, \(v(G)\) is the product of \(tn\) independent increments of law \(\mu\), the first \(n\) of which form \(G_{i_1}^{\sigma_1}\). So \((D(v(G)),D(G_{i_1}^{\sigma_1}))\) has the law of \((Z_{tn},Z_n)\), and \(\mathbb E\|Z_{tn}-Z_n\|_2^2\le e_n\). \(\square\)

A repeated index would reuse a block, and the estimate would not follow: \(G_iG_i^{-1}=1\).

## 4. The ultrapower and the proof

**Proof of Theorem 0.1.** By Proposition 2.1 it suffices to rule out the case of Section 3; let \(a\ne b\) be as there, and write \(a_1=a\), \(a_{-1}=b\).

*Finite selections.* Fix \(m\ge1\). For \(n\ge N_{1/m}\) and independent \(G_1,\ldots,G_m\) of law \(\mu^{*n}\), let \(E_{m,n}\) be the event that \(\|D(G_i)-a\|_2<1/m\) and \(\|D(G_i^{-1})-b\|_2<1/m\) for \(1\le i\le m\). By Lemma 3.1 and independence, \(P(E_{m,n})\ge c_m=(\eta_{1/m})^m\). Let \(\mathcal Q_m\) be the finite set of reduced words \(q\ne e\) of length at most \(m\) in \(x_1,\ldots,x_m\), and \(\mathcal V_m\) the finite set of words \(x_{i_1}^{\sigma_1}\cdots x_{i_t}^{\sigma_t}\), \(t\ge1\), with pairwise distinct indices in \(\{1,\ldots,m\}\). Consider the requirements
\[
\begin{aligned}
&|\tau(q(G_1,\ldots,G_m))|<1/m\quad(q\in\mathcal Q_m),\\
&\|D(v(G))-D(G_{i_1}^{\sigma_1})\|_2<1/m\\
&\qquad(v\in\mathcal V_m).
\end{aligned}
\]
Along the times \(n=n_\ell\), the probability that one of the first fails tends to \(0\) by Theorem 3.1 of the lesson on the random walk. By Lemma 3.2 and Chebyshev's inequality, the probability that one of the second fails is at most \(|\mathcal V_m|\,m^2e_{n_\ell}\), which tends to \(0\). Choose \(\ell_m>\ell_{m-1}\) with \(n_{\ell_m}\ge N_{1/m}\) such that the total failure probability is less than \(c_m/2\) at \(n=n_{\ell_m}\). Then \(E_{m,n_{\ell_m}}\) together with all the requirements has probability at least \(c_m/2>0\). The \(G_i\) take countably many values, so some value \((u^{(m)}_1,\ldots,u^{(m)}_m)\in\mathcal U(M)^m\) of \((G_1,\ldots,G_m)\) satisfies all of these conditions.

For \(v=x_{i_1}^{\sigma_1}\cdots x_{i_t}^{\sigma_t}\in\mathcal V_m\), the triangle inequality and (0.1) give
\[
\begin{aligned}
&\bigl\|T(v(u^{(m)}))-a_{\sigma_1}v(u^{(m)})\bigr\|_2\\
&\qquad<2/m .\qquad(4.1)
\end{aligned}
\]

*The ultrapower.* Put \(u^{(m)}_i=1\) for \(i>m\). Let \(\omega\) be a free ultrafilter on \(\mathbb N\), \(N=M^\omega\) the tracial ultrapower, \(g_i\in N\) the class of \((u^{(m)}_i)_{m\ge1}\), and \(R=T^\omega\). By Lemma 2.2 of the lesson on the cohomology problem, \(R\) is a bounded linear map on \(N\), continuous on balls for the \(2\)-norm. Each \(g_i\) is unitary. A reduced word \(q\ne e\) in finitely many \(x_i\) lies in \(\mathcal Q_m\) for all large \(m\), so \(\tau_\omega(q(g))=\lim_{m\to\omega}\tau(q(u^{(m)}))=0\): the \(g_i\) form a free Haar family. Identify \(a,b\) with their constant images in \(N\). A word \(v\) with pairwise distinct indices lies in \(\mathcal V_m\) for all large \(m\), and \(R(v(g))-a_{\sigma_1}v(g)\) is the class of the sequence in (4.1). Its \(2\)-norm is \(0\), so
\[
R(v(g))=\begin{cases}a\,v(g),&\sigma_1=1,\\ b\,v(g),&\sigma_1=-1.\end{cases}
\]
These are the hypotheses of the rigidity theorem (Theorem 0.1 of the lesson on rigidity) for \((N,\tau_\omega)\), \(R\), the family \((g_i)\) and \(a,b\). Hence \(a=b\) in \(N\). The constant embedding preserves the \(2\)-norm, so \(a=b\) in \(M\), a contradiction. So \(Z_\infty\) is almost surely constant, and Proposition 2.1 proves the theorem. \(\square\)

Only the traces of words in the \(g_i\) and the first-letter identities enter the rigidity theorem; freeness of the \(g_i\) from \(a\) or \(b\) is neither claimed nor needed.

## 5. Exercises

**5.1** (easy). Show that \(x\mapsto cx\) is \(\mu\)-harmonic and continuous on balls for the \(2\)-norm, for every \(c\in M\).

**5.2** (medium). Let \(c\in M\). Show that \(x\mapsto xc\) is \(\mu\)-harmonic if and only if \(\sum_U\mu(\{U\})\,UcU^*=c\). Deduce from Theorem 0.1 that this holds only for central \(c\).

**5.3** (medium). Show that the density of the atoms cannot be dropped. Let \(B\subseteq M\) be a von Neumann subalgebra whose relative commutant \(B'\cap M\) is not contained in the centre of \(M\), and let \(\nu\) be a probability measure on \(\mathcal U(B)\) with countable support. Give a map \(T\), bounded, linear, continuous on balls and \(\nu\)-harmonic, with \(T(x)\ne T(1)x\) for some \(x\).

**5.4** (easy). Let \(\pi\) be a Borel probability measure on a separable metric space whose support is a single point \(c\). Show that \(\pi(\{c\})=1\).

**5.5** (medium). In the proof of Lemma 3.1, show that \(B_n\) has the law of \(Z_h\) by writing out the joint law of \(V_n^{-1},\ldots,V_{n-h+1}^{-1}\).

## 6. Solutions

**5.1.** \(\sum_U\mu(\{U\})\,cxUU^*=cx\). If \(\sup_j\|x_j\|<\infty\) and \(\|x_j\|_2\to0\), then \(\|cx_j\|_2\le\|c\|\,\|x_j\|_2\to0\).

**5.2.** \(\sum_U\mu(\{U\})\,xUcU^*\)\(=x\sum_U\mu(\{U\})\,UcU^*\), which equals \(xc\) for all \(x\) exactly when the sum equals \(c\) (take \(x=1\)). The map \(x\mapsto xc\) is bounded and continuous on balls, since \(\|xc\|_2\le\|x\|_2\,\|c\|\). If it is harmonic, Theorem 0.1 gives \(xc=T(1)x=cx\) for all \(x\), so \(c\) is central. Conversely, if \(c\) is central the sum is \(c\).

**5.3.** Choose \(c\in B'\cap M\) and \(x\in M\) with \(xc\ne cx\), and let \(T(x)=xc\). For \(U\in\mathcal U(B)\), \(UcU^*=c\), so \(\sum_U\nu(\{U\})\,xUcU^*=xc\), and \(T\) is \(\nu\)-harmonic, bounded and continuous on balls. But \(T(x)=xc\ne cx=T(1)x\). For instance, in \(M=Q\bar\otimes Q\) for a II₁ factor \(Q\), the subalgebra \(B=Q\otimes1\) commutes with \(c=1\otimes q\), and \(c\) does not commute with \(x=1\otimes q'\) when \(qq'\ne q'q\).

**5.4.** Every point \(x\ne c\) has a neighbourhood of measure \(0\). The complement of \(\{c\}\) is covered by the null open balls with centres in a countable dense set and rational radii that do not contain \(c\): for \(x\ne c\), take a null ball around \(x\), then a centre \(z\) of the dense set and a rational radius \(r\) with \(x\in B(z,r)\), \(B(z,r)\) inside that null ball and \(c\notin B(z,r)\). A countable union of null sets is null.

**5.5.** For \(s_1,\ldots,s_h\in S\),
\[
\begin{aligned}
&P(V_n^{-1}=s_1,\ldots,V_{n-h+1}^{-1}=s_h)\\
&=\prod_{i=1}^h\mu(\{s_i^{-1}\})=\prod_{i=1}^h\mu(\{s_i\}),
\end{aligned}
\]
by independence and symmetry. This is the joint law of \(U_1,\ldots,U_h\), so \(B_n=D(V_n^{-1}\cdots V_{n-h+1}^{-1})\) has the law of \(D(U_1\cdots U_h)=Z_h\).

## Sources

- [OpenAI-295] OpenAI, *Vanishing of higher bounded Hochschild cohomology*, OpenAI Math Release preprint, 23 September 2026, Section 3 (the Liouville theorem). https://github.com/openai/math/tree/main/preprints/Vanishing-of-higher-bounded-Hochschild-cohomology-September-23-2026
- H. Furstenberg, [*Noncommuting random products*](https://www.ams.org/journals/tran/1963-108-03/S0002-9947-1963-0163345-0/), Trans. Amer. Math. Soc. 108 (1963), 377–428, page 415: the passage from harmonic functions to martingales along random products.
