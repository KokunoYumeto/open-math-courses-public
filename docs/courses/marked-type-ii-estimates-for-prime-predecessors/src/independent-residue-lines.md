# Independent residue lines

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The moment \(\mathfrak m\) of [*From the moment to the pairing*](from-the-moment-to-the-pairing.md) is a sum over closed paths starting at a root position \(P\). Written in coordinates adapted to the root, every condition along the path takes one of two forms: an archimedean condition on the root \((u,v)\) and its ratio \(r\), or a divisibility condition \(p\mid(\text{first coordinate})\), which says that a fixed projective line modulo \(p\) equals the kernel line of the root matrix modulo \(p\). This lesson uses [*Root residues*](root-residues.md) to replace the sum over roots by an integral over the archimedean data and by independent, uniformly distributed kernel lines, one for each group prime. The damping factors involve every group prime, so the product over primes is first truncated by Bonferroni's inequalities; the truncation is accurate because, in the model, a prime that is never in a list affects the path only with probability \(O(N/p)\).

**Prerequisites.** [*Physical states and good positions*](physical-states-and-good-positions.md); [*From the moment to the pairing*](from-the-moment-to-the-pairing.md), Lemma 2.1 and Section 4; [*Root residues*](root-residues.md), Theorem 2.1.

## 1. Coordinates at the root

Let \(P=(u,v)\in\Omega\) be a position and \(g=g(P)=\begin{pmatrix}u&c\\v&d\end{pmatrix}\) its root matrix, with \(r=c/u\). Every position \(Q\) can be written uniquely as \(Q=gz\) with \(z\in\mathbb Z^2\) primitive, and \(\det(gz,gz')=\det(z,z')\). Put \(\tau(z)=z_1+rz_2\). Then

\[
\begin{gathered}
(gz)_1=u\,\tau(z),\\
(gz)_2=v\,\tau(z)+\frac{z_2}u,\quad(1.1)
\end{gathered}
\]

since \(d-vc/u=1/u\). If \(w\) is an integer vector with \(\det(z,w)=1\), then \(gw\) completes \(gz\) to a matrix of determinant one, so the ratio of Lesson 8 at the position \(gz\) is

\[
\begin{gathered}
r_{gz}=\frac{\tau(w)}{\tau(z)}\bmod1 .\quad(1.2)
\end{gathered}
\]

For a prime \(p\), the first row \((u,c)\) of \(g\) is nonzero modulo \(p\), because \(ud-vc=1\). Let \(\ell_p(g)\in\mathbb P^1(\mathbb F_p)\) be the line orthogonal to it, and write \([z]_p\) for the line through \(z\) modulo \(p\) (defined since \(z\) is primitive). Then

\[
\begin{gathered}
p\mid(gz)_1\iff[z]_p=\ell_p(g).\quad(1.3)
\end{gathered}
\]

**Lemma 1.1 (the tube).** Let \(z_0=e_1,z_1,\dots,z_n=e_1\), \(n\le N\), be the coordinates at the root of the positions of a closed path whose consecutive positions are joined by edges with \(\mathcal K\ne0\). Then

\[
\begin{gathered}
|z_{j,2}|\le2560NH,\\
|z_{j,1}|\le2600NH,\\
\frac1{16}\le\tau(z_j)\le16 .
\end{gathered}
\]

**Proof.** By Lemma 2.1 of Lesson 9 the slope changes by at most \(10H/U^2\) along an edge, so the slopes of \(P\) and \(gz_j\) differ by at most \(10NH/U^2\). Hence \(|z_{j,2}|=|\det(e_1,z_j)|\)\(=|\det(P,gz_j)|\)\(\le256U^2\cdot10NH/U^2\). By (1.1), \(\tau(z_j)=(gz_j)_1/u\in[1/16,16]\), and \(z_{j,1}=\tau(z_j)-rz_{j,2}\). \(\square\)

## 2. The moment as a path sum

Expanding the products \(\mathcal A\mathcal A^*\cdots\mathcal A\mathcal A^*\) in (0.1) of Lesson 9, each factor \(\mathcal A=\mathcal G\mathcal S\mathcal T\mathcal S\mathcal G\) contributes a reordering of the source lists, an edge, a reordering of the target lists and the two goodness indicators, and each factor \(\mathcal A^*\) the same with a reversed edge (Lemma 2.1 of Lesson 8). A **path datum** consists of the coordinates \(z_0=e_1,z_1,\dots,z_N=e_1\), the ordered lists at the \(N+1\) visits, and the reorderings used; its **weight** \(w\) is the product of \(\prod_iV_i^{-M}\) for the initial lists, of \(\prod_iV_i^{-1}\) for the new labels of every edge, of \((M!)^{-K}\) for every reordering, and of the multipliers \(\mathcal K\) or \(\overline{\mathcal K}\) *without* their damping factors. By Lemma 1.1 and (1.1)–(1.3), \(w\) does not depend on the root: \(\mathcal K\) depends on \(\det(z_j,z_{j+1})\) and the labels only.

What depends on the root is:

1. the **archimedean factor** \(\mathrm{Arch}(u,v,r)\in\{0,1\}\): all positions \(gz_j\) lie in \(\Omega\), and all states at the visits are good;
2. the **arithmetic factor**: every label at visit \(j\) divides \((gz_j)_1\), and the damping. At visit \(j\) the damping is \(q_j^{\,\omega((gz_j)_1)-KM}\), where

\[
\begin{gathered}
q_j=\varkappa=\tfrac14\ (0<j<N),\\
q_0=q_N=\sqrt\varkappa=\tfrac12,
\end{gathered}
\]

because an interior visit is an endpoint of two edges and the two end visits of one.

Let \(A_p\subseteq\{0,\dots,N\}\) be the set of visits at which the prime \(p\) is in a list, and put \(\eta_j=1-q_j\). By (1.3) the arithmetic factor is \(\prod_p\Phi_p(\ell_p(g))\), the product over all group primes, where

\[
\begin{aligned}
\Phi_p(\ell)&=\prod_{j\in A_p}\mathbf 1_{[z_j]_p=\ell}\\
&\quad\times\prod_{j\notin A_p}\bigl(1-\eta_j\mathbf 1_{[z_j]_p=\ell}\bigr).\quad(2.1)
\end{aligned}
\]

Indeed, a prime in the list at visit \(j\) must divide \((gz_j)_1\), and every other mark of \((gz_j)_1\) contributes one factor \(q_j=1-\eta_j\). Therefore

\[
\begin{aligned}
\mathfrak m&=\sum_{\text{data}}w\sum_{P}\mathrm{Arch}(u,v,r)\\
&\quad\times\prod_p\Phi_p\bigl(\ell_p(g(P))\bigr),\quad(2.2)
\end{aligned}
\]

the inner sum over roots \(P=(u,v)\in\Omega\), primitive.

**Lemma 2.1 (budgets).** The data with nonzero weight satisfy \(\sum|w|\le\exp(O_K(L^{0.73}))\). At most \((N+1)KM\) primes are active (in some list) along a datum, and their product is at most \(\exp(O_K(L^{0.72}))\).

**Proof.** By Lemma 1.1 there are \(\exp(O(N\log(NH)))=\exp(O_K(L^{0.71}))\) choices of the \(z_j\). The labels number \(KM+KN\), each chosen among at most \(\exp(2L^{0.2})\) primes, giving \(\exp(O_K(L^{0.71}))\) choices, and the reorderings cost \((M!)^{2KN}=\exp(O_K(L^{0.52}))\). Each factor of \(w\) is bounded: \(V_i^{-1}\le2\), \(|\mathcal K|\le2\) because \(D\ge d_0\) and \(|\mathfrak M|\le1\), and \((M!)^{-K}\le1\). The product of the active primes is at most \(\exp(2L^{0.2})^{(N+1)KM}\). \(\square\)

## 3. Bonferroni's inequalities for numbers

**Lemma 3.1.** Let \(X_1,\dots,X_n\in[0,1]\) and let \(e_k\) be their elementary symmetric functions. For every \(T\ge0\),

\[
\begin{gathered}
\Bigl|\prod_{i=1}^n(1-X_i)-\sum_{k=0}^T(-1)^ke_k\Bigr|\\
\le e_{T+1}.\quad(3.1)
\end{gathered}
\]

**Proof.** Let \(\xi_1,\dots,\xi_n\) be independent random variables with \(\Pr(\xi_i=1)=X_i\) and \(\Pr(\xi_i=0)=1-X_i\), and let \(\nu=\sum_i\xi_i\). Then \(\mathbb E\binom\nu k=e_k\) and \(\Pr(\nu=0)=\prod(1-X_i)\). For an integer \(\nu\ge1\), \(\sum_{k\le T}(-1)^k\binom\nu k=(-1)^T\binom{\nu-1}T\), which has absolute value at most \(\binom\nu{T+1}\) (Lemma 4.1 of [*Primes, divisors, mean squares and rough numbers*](primes-divisors-mean-squares-and-rough-numbers.md)); for \(\nu=0\) the sum is \(1\). Take expectations. \(\square\)

The variables \(\xi_i\) are an auxiliary device: (3.1) is an inequality between numbers, valid for every choice of the \(X_i\) in \([0,1]\).

## 4. The model and the replacement

The **model** replaces the root by a point \(\mathbf a=(a_1,a_2,a_3)\in Q_0\)\(=[1,16]\times[1,2]\times[0,1]\), with the real matrix

\[
\begin{gathered}
g(\mathbf a)=\begin{pmatrix}Ua_1&Ua_1a_3\\ Va_2&Va_2a_3+1/(Ua_1)\end{pmatrix}\\
\in\mathrm{SL}_2(\mathbb R),
\end{gathered}
\]

so that \(u=Ua_1\), \(v=Va_2\), \(r=a_3\), and (1.1), (1.2) define \(\mathrm{Arch}(\mathbf a)\) for real \(\mathbf a\). The kernel lines are replaced by independent random lines \(\ell_p\), uniformly distributed in \(\mathbb P^1(\mathbb F_p)\), one for each group prime. The **model moment** at \(\mathbf a\) is

\[
\begin{aligned}
\mathfrak m(\mathbf a)&=\sum_{\text{data}}w\,\mathrm{Arch}(\mathbf a)\\
&\quad\times\mathbb E\prod_p\Phi_p(\ell_p).\quad(4.1)
\end{aligned}
\]

**Theorem 4.1 (replacement of the root average).** For every fixed \(A>0\) and large \(x\),

\[
\begin{gathered}
\frac{\mathfrak m}{UV}=\frac1{\zeta(2)}\int_{Q_0}\mathfrak m(\mathbf a)\,d\mathbf a\\
+O\bigl(L^{-AN}\bigr).\quad(4.2)
\end{gathered}
\]

The same holds, with the same proof, for any path sum of the form (2.2) with at most \(N\) edges and weights satisfying the budget of Lemma 2.1, and also with \(|w|\) in place of \(w\) and with \(\mathrm{Arch}\) replaced by the indicator that some visit fails a goodness test.

**Proof.** *Truncating the damping.* Fix a datum. Let \(\mathcal P_{\rm act}\) be its active primes and \(\mathcal P_{\rm rest}\) the other group primes. For \(p\in\mathcal P_{\rm rest}\) put \(X_p(\ell)=1-\Phi_p(\ell)\in[0,1]\). Let \(T=\lceil L^{0.76}\rceil\) and let \(B_T=\sum_{k\le T}(-1)^ke_k\) and \(e_{T+1}\) be formed from the numbers \(X_p(\ell_p)\), \(p\in\mathcal P_{\rm rest}\). Since \(|\Phi_p|\le1\) and \(\mathrm{Arch}\in\{0,1\}\), Lemma 3.1 gives, for every choice of lines,

\[
\begin{gathered}
\Bigl|\prod_p\Phi_p-\prod_{p\in\mathcal P_{\rm act}}\Phi_p\cdot B_T\Bigr|\le e_{T+1} .\quad(4.3)
\end{gathered}
\]

*Residue conditions.* Each \(\Phi_p\) and each \(X_p\) depends on \(\ell\) only through the indicators \(\mathbf 1_{\ell=\lambda}\) for the at most \(N+1\) lines \(\lambda\in\{[z_j]_p\}\): for \(p\in\mathcal P_{\rm act}\), \(\Phi_p\) is a constant times \(\mathbf 1_{\ell=\lambda_p}\) for the common active line \(\lambda_p\) (or zero if the active lines disagree), and for \(p\in\mathcal P_{\rm rest}\), \(X_p(\ell)=\sum_\lambda X_p(\lambda)\mathbf 1_{\ell=\lambda}\). Expanding, \(\prod_{\rm act}\Phi_p\cdot B_T\) and \(e_{T+1}\) become linear combinations, with coefficients of modulus at most \(1\), of products \(\prod_{p\in\mathcal S}\mathbf 1_{\ell_p=\lambda_p}\) over sets \(\mathcal S\) of at most \(|\mathcal P_{\rm act}|+T+1\) primes. The number of such products is at most \((N+2)^{T+1}\bigl(K\exp(2L^{0.2})\bigr)^{T+1}\)\(=\exp(O_K(L^{0.96}))\). For each of them, \(S=\prod_{p\in\mathcal S}p\) satisfies \(\log S\le O_K(L^{0.72})+2(T+1)L^{0.2}\)\(\le L^{0.99}\), and the condition \(\ell_p(g)=\lambda_p\) for all \(p\in\mathcal S\) holds for exactly \(\prod_{p\in\mathcal S}p(p-1)\) residue classes \(g_0\in\mathrm{SL}_2(\mathbb Z/S\mathbb Z)\), a fraction \(\prod_{p\in\mathcal S}(p+1)^{-1}\) of the group (Exercise 11.3).

*The archimedean grid.* Fix a datum and put \(\epsilon=\delta/1600\). Divide \(Q_0\) into cubes of side about \(x^{-\epsilon}\). The factor \(\mathrm{Arch}\) is constant on every cube that does not meet the following set \(\mathcal B\): the surfaces \(a_1\tau(z_j)\in\{1,16\}\) and \(a_2\tau(z_j)+z_{j,2}/(UVa_1)\in\{1,2\}\), and the planes \(a_3=r_0\) at which a goodness test at some visit changes its outcome. By (1.2), on the region \(\tau(z_j)\ge1/32\) the function \(a_3\mapsto r_{gz_j}\) is monotone with derivative \(1/\tau(z_j)^2\le1024\), and each test involves at most \(\exp(o(L))\) conditions of the form \(\|n\,r_{gz_j}\|\le\epsilon_0\) with integers \(|n|\le\exp(o(L))\) (Definition 3.1 of Lesson 8, including the weighted exceptional sets of (G2), which change only where one of their conditions does). So there are \(\exp(o(L))\) such planes. Where \(\tau(z_j)<1/16\), the condition \(a_1\tau(z_j)\ge1\) fails and \(\mathrm{Arch}=0\), so only the region \(\tau(z_j)\ge1/16\) matters. There the first surface is the graph \(a_1=c/\tau(z_j)\), \(c\in\{1,16\}\), of a function of \(a_3\) whose derivative \(cz_{j,2}/\tau(z_j)^2\) is at most \(\exp(o(L))\) by Lemma 1.1, and the second is the graph of a function \(a_2\) of \((a_1,a_3)\) with partial derivatives at most \(\exp(o(L))\). A graph over a square with derivatives at most \(\Lambda\) meets \(O((\Lambda+1)x^{2\epsilon})\) cubes, and a plane \(a_3=r_0\) meets \(O(x^{2\epsilon})\). Hence the cubes meeting \(\mathcal B\) have total volume \(x^{-\epsilon+o(1)}\).

For each residue condition \(g\equiv g_0\ (S)\) and each cube, Theorem 2.1 of Lesson 10 counts the roots with \(\mathbf a\) in the cube, with relative main term \(\mathrm{vol}/(\zeta(2)|\mathrm{SL}_2(\mathbb Z/S\mathbb Z)|)\) and error \(O(UVx^{-\delta/200})\). Summing over the \(O(x^{3\epsilon})\) cubes, treating the cubes meeting \(\mathcal B\) by the upper bound \(0\le\mathrm{Arch}\le1\), and then over the \(\exp(O_K(L^{0.96}))\) residue conditions and the \(\exp(O_K(L^{0.73}))\) weighted data, the replacement of the sum over roots of \(w\,\mathrm{Arch}\prod_{\rm act}\Phi_p\,B_T\) by \(UV/\zeta(2)\) times the integral of its model expectation costs

\[
\begin{gathered}
UV\,x^{-\delta/200+3\epsilon+o(1)}+UV\,x^{-\epsilon+o(1)}\\
=UV\,x^{-\epsilon+o(1)} .
\end{gathered}
\]

*The truncation error.* The same replacement applies to \(\sum|w|\sum_Pe_{T+1}\). In the model, the lines are independent and \(\mathbb E X_p(\ell_p)\le\sum_j\eta_j/(p+1)\le(N+1)/p\), so

\[
\begin{aligned}
\mathbb E\,e_{T+1}&\le\frac1{(T+1)!}\Bigl(\sum_p\mathbb EX_p\Bigr)^{T+1}\\
&\le\Bigl(\frac{2eK(N+1)}{T+1}\Bigr)^{T+1}\\
&\le\exp\bigl(-\tfrac15L^{0.76}\log L\bigr),
\end{aligned}
\]

because \(\sum_p1/p\le2K\) over the group primes and \(N+1\le L^{0.51}\). Multiplied by the budget \(\exp(O_K(L^{0.73}))\), this is far smaller than \(L^{-AN}=\exp(-O(L^{0.5}\log L))\). The same bound controls the model counterpart of (4.3). Collecting the errors and dividing by \(UV\) proves (4.2). The variants stated after the theorem only change the weights or the archimedean indicator, and the indicator of failing a test is again constant off the planes described above. \(\square\)

In the model the structure of the moment is transparent: each group prime contributes an independent factor \(\mathbb E\,\Phi_p(\ell_p)\), and \(\ell_p\) is a uniform line, so a prescribed line has probability \(1/(p+1)\). The next lesson evaluates these factors exactly.

## 5. Exercises

**11.1.** Verify (1.1) and (1.2) directly from the matrix \(g\) and \(\det(z,w)=1\).

**11.2.** Show that if \(g\) is uniformly distributed in \(\mathrm{SL}_2(\mathbb F_p)\), then \(\ell_p(g)\) is uniformly distributed among the \(p+1\) lines.

**11.3.** Show that the condition \(\ell_p(g)=\lambda\) holds for exactly \(p(p-1)\) elements of \(\mathrm{SL}_2(\mathbb F_p)\).

**11.4.** Let \(X_1=X_2=\frac12\). Compute both sides of (3.1) for \(T=0,1,2\).

**11.5.** Explain why the damping at the two end visits is \(\sqrt\varkappa\) per extra mark, and at interior visits \(\varkappa\).

## 6. Solutions

**11.1.** \((gz)_1=uz_1+cz_2=u(z_1+rz_2)\). \((gz)_2=vz_1+dz_2=v\tau(z)+(d-vr)z_2\) and \(d-vr=(ud-vc)/u=1/u\). The matrix with columns \(gz,gw\) is \(g\) times the matrix with columns \(z,w\), so its determinant is \(1\), and its ratio is \((gw)_1/(gz)_1=\tau(w)/\tau(z)\).

**11.2.** The first row of a uniform element of \(\mathrm{SL}_2(\mathbb F_p)\) is uniform among the \(p^2-1\) nonzero vectors, since each has exactly \(p\) completions. The orthogonal line of a nonzero row is determined by the row up to the \(p-1\) nonzero scalars, so each line arises from \(p-1\) rows, with probability \((p-1)/(p^2-1)=1/(p+1)\).

**11.3.** By the previous solution: \(p-1\) rows, each with \(p\) completions.

**11.4.** The product is \(\frac14\), \(e_1=1\), \(e_2=\frac14\), \(e_3=0\). For \(T=0\): \(|\frac14-1|=\frac34\le e_1=1\). For \(T=1\): \(|\frac14-0|=\frac14\le e_2\). For \(T=2\): \(|\frac14-\frac14|=0\le e_3=0\).

**11.5.** In (2.2) of Lesson 8 every edge contributes \(\varkappa^{(\omega-KM)/2}\) at each of its two endpoints. An interior visit is the target of one edge and the source of the next, so it receives \(\varkappa^{\omega-KM}\); the first and last visits belong to one edge each.

## References

- [PD] OpenAI, *The Poisson–Dirichlet law for prime predecessors*, OpenAI Math Release preprint, 24 September 2026, Section 3.5. https://github.com/openai/math/tree/main/preprints/The-Poisson-Dirichlet-Law-for-Prime-Predecessors-September-24-2026
