# States and a catalytic comparison

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Theorem 5.2 bounds every character on matrix multiplication. To turn this into a bound on the exponent \(\nu\), one needs characters that are large on \(T_d\): for every integer \(k<d^\nu\), a character with \(\lambda(T_d)\ge k\). This is a special case of Strassen's spectral theorem; see [CVZ] for the general theory. The proof given here, OpenAI's [OpenAI-MM, Appendix A], has two parts. This lesson shows that the *states* (additive, monotone, normalized maps on \(S\)) satisfying \(\mu(T_dU)\ge k\mu(U)\) for all \(U\) form a nonempty compact convex set (Proposition 6.7): if the set were empty, a separation argument would produce a *catalytic comparison* \(E+kU\ge E+m+T_dU\), and repeating it would contradict \(k<d^\nu\). The next lesson, [Multiplicative states and the proof of Theorem A](multiplicative-states-and-the-proof-of-theorem-a.md), finds a multiplicative state in this set.

## 1. States

**Definition 6.1.** A *state* is a map \(\mu:S\to[0,\infty)\) with \(\mu(A+U)=\mu(A)+\mu(U)\) for all \(A,U\), \(\mu(A)\ge\mu(A')\) whenever \(A\ge A'\), and \(\mu(1)=1\).

A character is a multiplicative state. As in Lemma 2.2, every state satisfies \(\mu(0)=0\), \(\mu(m)=m\), and \(1\le\mu(A)\le R(A)\) for \(A\ne0\).

Fix integers \(d\ge2\) and \(k\ge0\). Let \(\mathcal K=\mathcal K_{d,k}\) be the set of states \(\mu\) such that, for every \(U\in S\),
\[
\mu(T_dU)\ge k\,\mu(U). \tag{6.1}
\]

## 2. The box of functions

The set \(S\) is countable: every tensor is isomorphic to one with index sets \(\{1,\dots,n_1\}\), \(\{1,\dots,n_2\}\), \(\{1,\dots,n_3\}\), and for fixed sizes such tensors correspond to the elements of the countable set \(F^{n_1n_2n_3}\). It is infinite, since the classes \(m\) are distinct (\(\rho_X(m)=m\)). Enumerate it as \(S=\{s_1,s_2,\dots\}\), and for functions \(\mu:S\to\mathbf R\) put
\[
\|\mu\|=\sum_{i\ge1}\frac{2^{-i}\,|\mu(s_i)|}{1+R(s_i)}.
\]
The functions with \(\|\mu\|<\infty\) form a real vector space \(V\), and \(\|\cdot\|\) is a norm on it. Let \(Q\) be the set of functions \(\mu:S\to\mathbf R\) with \(0\le\mu(s)\le R(s)\) for all \(s\in S\). Every \(\mu\in Q\) has \(\|\mu\|\le1\), so \(Q\subseteq V\), and every state lies in \(Q\).

**Lemma 6.3.** (a) A sequence in \(Q\) converges in norm to an element of \(Q\) if and only if it converges at every point of \(S\).

(b) \(Q\) is compact.

(c) Each of the conditions \(\mu(1)=1\), \(\mu(A+U)=\mu(A)+\mu(U)\), \(\mu(A)\ge\mu(A')\) and \(\mu(T_dU)\ge k\mu(U)\), for fixed elements \(A,U,A'\) of \(S\), defines a closed convex subset of \(Q\). In particular \(\mathcal K\) is a compact convex subset of the normed space \(V\).

**Proof.** (a) If \(\|\mu_n-\mu\|\to0\), then for each \(i\) the difference \(|\mu_n(s_i)-\mu(s_i)|\) is at most \(2^i(1+R(s_i))\|\mu_n-\mu\|\), which tends to \(0\). Conversely, suppose \(\mu_n\to\mu\) pointwise, all in \(Q\). Each term of \(\|\mu_n-\mu\|\) is at most \(2^{-i}\), because \(|\mu_n(s_i)-\mu(s_i)|\le R(s_i)\). Given \(\eta>0\), choose \(N\) with \(2^{-N}<\eta/2\); the terms with \(i\le N\) tend to \(0\), and the others add up to at most \(2^{-N}\).

(b) Let \((\mu_n)\) be a sequence in \(Q\). Each sequence \((\mu_n(s_i))_n\) lies in the compact interval \([0,R(s_i)]\). Choose successively nested subsequences along which the values at \(s_1\), at \(s_2\), and so on converge; the diagonal subsequence converges at every point, to a function in \(Q\). By (a) it converges in norm. A sequentially compact subset of a normed space is compact.

(c) Each condition involves finitely many values of \(\mu\), which depend continuously on \(\mu\in Q\) by (a), and each is linear in \(\mu\). The set \(\mathcal K\) is the intersection of these sets over all choices of the fixed elements; it is a closed convex subset of the compact set \(Q\). \(\square\)

## 3. The Grothendieck group

**Lemma 6.4.** Let \((M,+,0)\) be a commutative monoid. On \(M\times M\) put \((a,b)\sim(a',b')\) if \(a+b'+c=a'+b+c\) for some \(c\in M\). This is an equivalence relation. The classes \([a,b]\) form an abelian group \(G(M)\) with \([a,b]+[a',b']=[a+a',b+b']\), zero \([0,0]\) and \(-[a,b]=[b,a]\). Writing \([a]=[a,0]\), one has \([a,b]=[a]-[b]\), and \([a]=[a']\) if and only if \(a+c=a'+c\) for some \(c\in M\).

**Proof.** Reflexivity and symmetry follow from the definition. Suppose \(a+b'+c=a'+b+c\) and \(a'+b''+c'=a''+b'+c'\). Adding \(b''+c'\) to both sides of the first equation and \(b+c\) to both sides of the second gives
\[
\begin{aligned}
&a+b'+b''+c+c'\\
&\quad=a'+b+b''+c+c'\\
&\quad=a''+b+b'+c+c',
\end{aligned}
\]
so \(a+b''+c''=a''+b+c''\) with \(c''=b'+c+c'\), and \((a,b)\sim(a'',b'')\). Addition is compatible with \(\sim\): if \((a,b)\sim(a_1,b_1)\) through \(c\), then \((a+a',b+b')\sim(a_1+a',b_1+b')\) through the same \(c\). Associativity, commutativity and the zero are inherited from \(M\), and \([a,b]+[b,a]=[a+b,a+b]=[0,0]\) because \(a+b+0+0=0+(a+b)+0\). Finally \([a]-[b]=[a,0]+[0,b]=[a,b]\), and \([a,0]=[a',0]\) means \(a+c=a'+c\) for some \(c\). \(\square\)

We use \(G(S)\) for the monoid \((S,+)\).

## 4. Cones and rational solutions

**Lemma 6.5.** Let \(v_1,\dots,v_n\) be vectors of a finite-dimensional real vector space \(Y\), and let \(C=\{\sum_i\alpha_iv_i:\alpha_i\ge0\}\) be the cone they generate.

(a) Every point of \(C\) is a nonnegative combination of a linearly independent subfamily of the \(v_i\).

(b) \(C\) is closed.

(c) If \(p\notin C\), there is a linear functional \(\ell\) on \(Y\) with \(\ell\ge0\) on \(C\) and \(\ell(p)<0\).

**Proof.** (a) Write \(p=\sum_i\alpha_iv_i\) with \(\alpha\ge0\) and the fewest nonzero coefficients. If the \(v_i\) with \(\alpha_i>0\) were dependent, choose \(\gamma\ne0\), supported where \(\alpha_i>0\), with \(\sum_i\gamma_iv_i=0\) and some \(\gamma_i>0\). Then \(p=\sum_i(\alpha_i-\tau\gamma_i)v_i\) for every \(\tau\), and \(\tau=\min_{\gamma_i>0}\alpha_i/\gamma_i\) gives a nonnegative representation with fewer nonzero coefficients.

(b) For a linearly independent subfamily \((v_i)_{i\in I}\), the map \(\alpha\mapsto\sum_{i\in I}\alpha_iv_i\) is a linear isomorphism of \(\mathbf R^I\) onto a subspace of \(Y\), so it maps the closed set \([0,\infty)^I\) onto a closed subset of that closed subspace. By (a), \(C\) is the union of these finitely many closed sets.

(c) Choose an inner product on \(Y\). The set \(C\cap\{c:|c-p|\le|p|\}\) is compact and contains \(0\); let \(c_0\) be a point of it nearest to \(p\), which is then nearest to \(p\) in all of \(C\). For \(c\in C\) and \(\tau>0\), \(c_0+\tau c\in C\), so \(|p-c_0-\tau c|^2\ge|p-c_0|^2\), that is, \(-2\tau\langle p-c_0,c\rangle+\tau^2|c|^2\ge0\); dividing by \(\tau\) and letting \(\tau\to0\) gives \(\langle p-c_0,c\rangle\le0\). Also \(sc_0\in C\) for all \(s\ge0\), and \(s\mapsto|p-sc_0|^2\) is smallest at \(s=1\), so \(\langle p-c_0,c_0\rangle=0\). Put \(\ell(y)=-\langle p-c_0,y\rangle\). Then \(\ell\ge0\) on \(C\), and \(\ell(p)=-|p-c_0|^2-\langle p-c_0,c_0\rangle\), which equals \(-|p-c_0|^2<0\), since \(p\ne c_0\). \(\square\)

**Lemma 6.6.** Let \(A\) be a matrix and \(b\) a vector, both with rational entries. If the system \(Ax=b\) has a real solution with \(x\ge0\), then it has a rational solution with \(x\ge0\).

**Proof.** Choose a real solution \(x\ge0\) with the fewest nonzero coordinates, and let \(J\) be the set of its nonzero coordinates. The columns \(a_j\), \(j\in J\), of \(A\) are linearly independent: otherwise there is \(\gamma\ne0\) supported in \(J\) with \(A\gamma=0\) and some \(\gamma_j>0\), and \(x-\tau\gamma\) with \(\tau=\min_{\gamma_j>0}x_j/\gamma_j\) is a nonnegative solution with fewer nonzero coordinates. So the system \(\sum_{j\in J}y_ja_j=b\) has exactly one real solution, namely \(y=(x_j)_{j\in J}\). Row reduction of its augmented matrix uses only field operations, so it gives the same reduced echelon form over \(\mathbf Q\) as over \(\mathbf R\). Because the system is solvable over \(\mathbf R\), this form contains no row \((0,\dots,0\mid1)\), and it exhibits a rational solution; by uniqueness, this solution is \(y\). Hence \(x\) is rational. \(\square\)

## 5. The detecting states exist

**Proposition 6.7.** If \(k<d^\nu\), then \(\mathcal K_{d,k}\) is nonempty.

**Proof.** Suppose \(\mathcal K=\mathcal K_{d,k}\) is empty.

*Step 1: a finite inconsistent system.* By Lemma 6.3(c), \(\mathcal K\) is the intersection of closed subsets of the compact set \(Q\), one for each condition \(\mu(1)=1\), \(\mu(A+U)=\mu(A)+\mu(U)\), \(\mu(A)\ge\mu(A')\) (\(A\ge A'\)), \(\mu(T_dU)\ge k\mu(U)\). Since the intersection is empty, finitely many of these conditions already define the empty subset of \(Q\). Let \(\mathcal F\subseteq S\) be a finite set containing \(0\), \(1\) and all elements of \(S\) occurring in these finitely many conditions. Consider the linear system, in the unknowns \(\mu_s\) for \(s\in\mathcal F\), consisting of these conditions together with \(\mu_1=1\), \(\mu_0=0\) and \(0\le\mu_s\le R(s)\) for \(s\in\mathcal F\). It has no real solution: a solution, extended by \(\mu(s)=0\) for \(s\notin\mathcal F\), would be a point of \(Q\) satisfying the finitely many conditions.

*Step 2: separation.* Let \((e_s)_{s\in\mathcal F}\) be the standard basis of \(\mathbf R^{\mathcal F}\), and regard \(\mu\) as the linear functional with \(\mu(e_s)=\mu_s\). Let \(\Omega\) be the span of \(e_0\) and of the vectors \(e_{A+U}-e_A-e_U\) of the additivity conditions in the system. The *inequality vectors* are \(e_A-e_{A'}\) for the monotonicity conditions, \(e_{T_dU}-ke_U\) for the conditions (6.1) in the system, and \(e_s\) and \(R(s)e_1-e_s\) for \(s\in\mathcal F\); using \(\mu_1=1\), the bound \(\mu_s\le R(s)\) is the inequality \(\mu(R(s)e_1-e_s)\ge0\). So the system says: \(\mu\) vanishes on \(\Omega\), \(\mu(e_1)=1\), and \(\mu\ge0\) on the inequality vectors. In the quotient space \(Y=\mathbf R^{\mathcal F}/\Omega\) let \(u\) be the image of \(e_1\) and \(C\) the cone generated by the images of the inequality vectors. If \(-u\notin C\), Lemma 6.5(c) gives a linear functional \(\ell\) on \(Y\) with \(\ell\ge0\) on \(C\) and \(\ell(-u)<0\), and \(\ell/\ell(u)\), composed with the quotient map, solves the system. Hence \(-u\in C\): there are \(\alpha_g\ge0\) and real \(\beta_r\) with
\[
-e_1=\sum_g\alpha_gv_g+\sum_r\beta_r\omega_r,
\]
where the \(v_g\) are the inequality vectors and the \(\omega_r\) the spanning vectors of \(\Omega\).

*Step 3: integers.* All these vectors have integer coordinates. Writing \(\beta_r=\beta_r^+-\beta_r^-\) with \(\beta_r^\pm\ge0\), the identity is a linear system with integer coefficients and nonnegative unknowns that has a real solution. By Lemma 6.6 it has a rational one, and clearing denominators gives an integer \(m\ge1\), integers \(n_g\ge0\) and integers \(b_r\) with
\[
-m\,e_1=\sum_gn_gv_g+\sum_rb_r\omega_r.
\]

*Step 4: back to tensors.* The homomorphism \(\mathbf Z^{\mathcal F}\to G(S)\) with \(e_s\mapsto[s]\) sends each \(\omega_r\) to \(0\), because \([A+U]=[A]+[U]\) and \([0]=0\). It sends \(e_A-e_{A'}\) to \([A]-[A']\) with \(A\ge A'\); \(e_s\) to \([s]-[0]\) with \(s\ge0\); \(R(s)e_1-e_s\) to \([R(s)]-[s]\) with \(R(s)\ge s\), where \(R(s)\) stands for the element \(R(s)\cdot1\) of \(S\); and \(e_{T_dU}-ke_U\) to \([T_dU]-k[U]\). The images of the first three kinds are differences \([y_g]-[x_g]\) with \(y_g\ge x_g\); by Lemma 1.2(b), \(\sum_gn_g([y_g]-[x_g])=[y]-[x]\) with \(y=\sum_gn_gy_g\ge x=\sum_gn_gx_g\). By distributivity, \(\sum_gn_g([T_dU_g]-k[U_g])=[T_dU]-k[U]\) with \(U=\sum_gn_gU_g\). So the integer identity of Step 3 becomes
\[
-m[1]=[y]-[x]+[T_dU]-k[U],
\]
that is, \([m+y+T_dU]=[x+kU]\). By Lemma 6.4 there is \(c\in S\) with
\[
m+y+T_dU+c=x+kU+c.
\]

*Step 5: the catalytic comparison.* Put \(E=y+c\). Since \(y\ge x\),
\[
E+kU\ge x+c+kU=E+m+T_dU.
\]
Here \(U\ne0\): otherwise this comparison says \(E\ge E+m\), and \(\rho_X\) would give \(\rho_X(E)\ge\rho_X(E)+m\) with \(m\ge1\).

*Step 6: amplification.* By induction on \(n\ge1\), \(E+nkU\ge E+nm+nT_dU\): adding \(kU\) to the inequality for \(n\) and applying the catalytic comparison gives
\[
\begin{aligned}
&E+(n+1)kU\\
&\quad\ge(E+kU)+nm+nT_dU\\
&\quad\ge E+(n+1)(m+T_dU).
\end{aligned}
\]
Dropping summands, \(E+nkU\ge nT_dU\). Since \(U\ge1\), also \(R(E)U\ge R(E)\ge E\). With \(K=nk+R(E)\) this gives
\[
KU\ge nkU+E\ge nT_dU.
\]
Then \(K\ge1\), because \(nT_dU\ne0\). By induction on \(j\),
\[
K^jU\ge n^jT_{d^j}U\qquad(j\ge1):
\]
multiplying the inequality for \(j\) by \(K\) and using \(KU\ge nT_dU\) gives \(K^{j+1}U\ge n^jT_{d^j}(KU)\ge n^{j+1}T_{d^{j+1}}U\), by Lemma 1.6(a).

*Step 7: a second matrix multiplication.* Fix \(n\) and \(\delta>0\), and choose \(u\ge2\) with \(R(T_u)\le u^{\nu+\delta}\). Put \(\ell_j=\lfloor j\log_un/(\nu+\delta)\rfloor\) and \(g_j=u^{\ell_j}\). By Lemma 1.4 and Lemma 1.6(a),
\[
R(T_{g_j})\le R(T_u)^{\ell_j}\le u^{(\nu+\delta)\ell_j}\le n^j,
\]
so \(n^j\ge T_{g_j}\). Multiplying by \(T_{d^j}U\) and using \(U\ge1\),
\[
K^jU\ge n^jT_{d^j}U\ge T_{d^jg_j}U\ge T_{d^jg_j}.
\]
Taking ranks, \(K^jR(U)\ge R(T_{d^jg_j})\ge(d^jg_j)^\nu\). Take \(j\)-th roots and let \(j\to\infty\); since \(g_j^{1/j}\to n^{1/(\nu+\delta)}\),
\[
nk+R(E)\ge d^\nu\,n^{\nu/(\nu+\delta)}.
\]
Let \(\delta\to0\): \(nk+R(E)\ge nd^\nu\). Divide by \(n\) and let \(n\to\infty\); the catalyst \(E\) does not depend on \(n\), so \(k\ge d^\nu\), contrary to the hypothesis. \(\square\)

## 6. Exercises

**6.1** (easy). Show that \(\rho_X\in\mathcal K_{d,k}\) if and only if \(k\le d^2\).

**6.2** (easy). Show that the convex cone \(\{(0,0)\}\cup\{(y_1,y_2):y_2>0\}\) in \(\mathbf R^2\) is not closed, so the finiteness in Lemma 6.5 cannot be dropped.

**6.3** (medium). Show that if \(\mathcal K_{d,k}\) is nonempty, then \(k\le d^\nu\).

## 7. Solutions

**6.1.** \(\rho_X\) is multiplicative with \(\rho_X(T_d)=d^2\), so \(\rho_X(T_dU)=d^2\rho_X(U)\). Condition (6.1) holds for all \(U\) if and only if \(d^2\ge k\) (take \(U=1\) for the converse).

**6.2.** The points \((1,1/n)\) lie in the cone and converge to \((1,0)\), which does not.

**6.3.** Let \(\mu\in\mathcal K_{d,k}\). Applying (6.1) with \(U=T_d^{j-1}\) repeatedly gives \(\mu(T_{d^j})\ge k^j\). Since \(\mu\le R\), \(k\le R(T_{d^j})^{1/j}\) for all \(j\), and by Exercise 1.5 the right side tends to \(d^\nu\).

## References

- [OpenAI-MM] OpenAI, *An upper bound of 9/4 for the matrix multiplication exponent*, OpenAI Math Release preprint, 2 October 2026, Appendix A. https://github.com/openai/math/tree/main/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026
- [CVZ] M. Christandl, P. Vrana and J. Zuiddam, *Universal points in the asymptotic spectrum of tensors*, Journal of the American Mathematical Society 36 (2023), 31–79; arXiv:1709.07851. https://arxiv.org/abs/1709.07851
